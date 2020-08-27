import wx, sys, gff4
from wx.lib.intctrl import IntCtrl
from gff4 import *
from gff4.editorutils import *
from numbers import Real, Integral
from base64 import encodestring, decodestring
from itertools import count as icount
from traceback import print_exc, format_exc
import zlib

class PlaceholderPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(PlaceholderPanel, self).__init__(*args, **kwargs)
    
    def Edit(self, value, kind, indirect, callback):
        pass

class IntegerEditPanel(wx.Panel):
    edits = Integral
    
    def __init__(self, *args, **kwargs):
        super(IntegerEditPanel, self).__init__(*args, **kwargs)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.intspin = wx.SpinCtrl(self, style=wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS)
        self.intctrl = IntCtrl(self, limited=True, allow_long=True, style=wx.ALIGN_RIGHT)
        self.floatctrl = wx.TextCtrl(self, style=wx.ALIGN_RIGHT)
        self.floatchk = wx.CheckBox(self, label='Treat as floating-point')
        sizer.Add(self.intspin, flag=wx.ALIGN_CENTER_VERTICAL)
        sizer.Add(self.intctrl, flag=wx.ALIGN_CENTER_VERTICAL)
        sizer.Add(self.floatctrl, flag=wx.ALIGN_CENTER_VERTICAL)
        sizer.Add(self.floatchk, flag=wx.ALIGN_CENTER_VERTICAL|wx.LEFT, border=10)
        self.Bind(wx.EVT_CHECKBOX, self.OnFloatToggle, self.floatchk)
        self.SetSizer(sizer)
    
    def SetValue(self, value, kind):
        self.kind = kind
        self.Freeze()
        self.floatchk.Value = False
        self.floatctrl.Hide()
        if type(value).maxval > sys.maxsize:
            self.intspin.Hide()
            self.intctrl.Show()
            self.intctrl.SetBounds(type(value).minval, type(value).maxval)
            self.intctrl.SetValue(long(value))
        else:
            self.intctrl.Hide()
            self.intspin.Show()
            self.intspin.SetRange(type(value).minval, type(value).maxval)
            self.intspin.SetValue(value)
        if kind.size in (4, 8):
            self.floatchk.Show()
            self.intfmt = kind.format[False]
            self.floatfmt = FLOAT32.format[False] if kind.size == 4 else FLOAT64.format[False]
        else:
            self.floatchk.Hide()
        self.Layout()
        self.Thaw()
    
    def GetValue(self):
        if self.intspin.Shown:
            return self.kind(self.intspin.GetValue())
        elif self.intctrl.Shown:
            try:
                return self.kind(self.intctrl.GetValue())
            except ValueError, e:
                raise ValueError, "%r"%e
        else:
            try:
                return self.kind(self.intfmt.unpack(self.floatfmt.pack(float(self.floatctrl.Value)))[0])
            except ValueError, e:
                raise ValueError, "%r"%e
    
    def OnFloatToggle(self, event):
        self.Freeze()
        if event.IsChecked():
            if self.intspin.Shown:
                value = self.intspin.Value
            else:
                value = self.intctrl.GetValue()
            self.floatctrl.Value = str(self.floatfmt.unpack(self.intfmt.pack(value))[0])
            self.intspin.Hide()
            self.intctrl.Hide()
            self.floatctrl.Show()
        else:
            value = 0
            if self.floatctrl.Value:
                try:
                    value = self.intfmt.unpack(self.floatfmt.pack(float(self.floatctrl.Value)))[0]
                except ValueError:
                    pass
            self.floatctrl.Hide()
            if self.kind.maxval > sys.maxsize:
                self.intctrl.Show()
                self.intctrl.SetValue(long(value))
            else:
                self.intspin.Show()
                self.intspin.Value = value
        self.Layout()
        self.Thaw()
    
class FloatEditPanel(wx.Panel):
    edits = Real
    
    def __init__(self, *args, **kwargs):
        super(FloatEditPanel, self).__init__(*args, **kwargs)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.floatctrl = wx.TextCtrl(self, style=wx.ALIGN_RIGHT)
        sizer.Add(self.floatctrl, flag=wx.ALIGN_CENTER_VERTICAL)
        self.SetSizer(sizer)
    
    def SetValue(self, value, kind):
        self.kind = kind
        if not value:
            self.floatctrl.SetValue('0.0')
        else:
            self.floatctrl.SetValue(str(float(value)))
    
    def GetValue(self):
        value = self.floatctrl.GetValue()
        if value:
            try:
                return self.kind(value)
            except ValueError:
                raise ValueError, "%s is not a valid float."%value
        else:
            return None

class FloatTupleEditPanel(wx.Panel):
    edits = (Vector3f, Vector4f, Quaternionf, Color4f)
    
    def __init__(self, *args, **kwargs):
        super(FloatTupleEditPanel, self).__init__(*args, **kwargs)
        self.floata = wx.TextCtrl(self, style=wx.ALIGN_RIGHT)
        self.floatb = wx.TextCtrl(self, style=wx.ALIGN_RIGHT)
        self.floatc = wx.TextCtrl(self, style=wx.ALIGN_RIGHT)
        self.floatd = wx.TextCtrl(self, style=wx.ALIGN_RIGHT)
        self.labela = wx.StaticText(self, wx.ID_ANY, 'a')
        self.labelb = wx.StaticText(self, wx.ID_ANY, 'b')
        self.labelc = wx.StaticText(self, wx.ID_ANY, 'c')
        self.labeld = wx.StaticText(self, wx.ID_ANY, 'd')
        self.labelg = wx.StaticText(self, wx.ID_ANY, 'g')
        self.labelr = wx.StaticText(self, wx.ID_ANY, 'r')
        
        self.ctrls = (self.floata, self.floatb, self.floatc, self.floatd)
    
    def SetValue(self, value, kind):
        self.kind = kind
        self.Freeze()
        if issubclass(kind, Color4f):
            self.labelc.Hide()
            self.labeld.Hide()
            self.labelg.Show()
            self.labelr.Show()
            self.floatd.Show()
            
            sizerrgba = wx.BoxSizer(wx.HORIZONTAL)
            sizerrgba.Add(self.labelr, flag=wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, border=5)
            sizerrgba.Add(self.floata, flag=wx.ALIGN_CENTER_VERTICAL)
            sizerrgba.Add(self.labelg, flag=wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, border=5)
            sizerrgba.Add(self.floatb, flag=wx.ALIGN_CENTER_VERTICAL)
            sizerrgba.Add(self.labelb, flag=wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, border=5)
            sizerrgba.Add(self.floatc, flag=wx.ALIGN_CENTER_VERTICAL)
            sizerrgba.Add(self.labela, flag=wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, border=5)
            sizerrgba.Add(self.floatd, flag=wx.ALIGN_CENTER_VERTICAL)
            self.SetSizer(sizerrgba)
        else:
            self.labelg.Hide()
            self.labelr.Hide()
            self.labelc.Show()
            if len(value) < 4:
                self.labeld.Hide()
                self.floatd.Hide()
            else:
                self.labeld.Show()
                self.floatd.Show()
                
            sizerabcd = wx.BoxSizer(wx.HORIZONTAL)
            sizerabcd.Add(self.labela, flag=wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, border=5)
            sizerabcd.Add(self.floata, flag=wx.ALIGN_CENTER_VERTICAL)
            sizerabcd.Add(self.labelb, flag=wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, border=5)
            sizerabcd.Add(self.floatb, flag=wx.ALIGN_CENTER_VERTICAL)
            sizerabcd.Add(self.labelc, flag=wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, border=5)
            sizerabcd.Add(self.floatc, flag=wx.ALIGN_CENTER_VERTICAL)
            sizerabcd.Add(self.labeld, flag=wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, border=5)
            sizerabcd.Add(self.floatd, flag=wx.ALIGN_CENTER_VERTICAL)
            self.SetSizer(sizerabcd)
        for ctrl, v in zip(self.ctrls, value):
            ctrl.SetValue(str(float(v)))
        self.Layout()
        self.Thaw()
    
    def GetValue(self):
        def parse(ctrl):
            value = ctrl.GetValue()
            try:
                return float(value)
            except ValueError:
                raise ValueError, "%s is not a valid float."%value
        return self.kind(*(parse(ctrl) for ctrl in self.ctrls if ctrl.IsShown()))

class MatrixEditPanel(wx.Panel):
    edits = Matrix4x4f
    
    def __init__(self, *args, **kwargs):
        super(MatrixEditPanel, self).__init__(*args, **kwargs)
        self.ctrls = []
        sizer = wx.GridBagSizer()
        for i, c in enumerate(('a', 'b', 'c', 'd')):
            label = wx.StaticText(self, wx.ID_ANY, c)
            sizer.Add(label, pos=(i+1,0), flag=wx.ALIGN_CENTER_VERTICAL)
            label = wx.StaticText(self, wx.ID_ANY, c)
            sizer.Add(label, pos=(0,i+1), flag=wx.ALIGN_CENTER)
        for row in xrange(4):
            for col in xrange(4):
                ctrl = wx.TextCtrl(self, style=wx.ALIGN_RIGHT)
                self.ctrls.append(ctrl)
                sizer.Add(ctrl, pos=(row+1,col+1), flag=wx.ALIGN_CENTER_VERTICAL)
        self.SetSizer(sizer)
    
    def SetValue(self, value, kind):
        if not issubclass(kind, Matrix4x4f) or len(value) != 16:
            raise ValueError
        self.kind = kind
        for ctrl, v in zip(self.ctrls, value):
            ctrl.SetValue(str(float(v)))
    
    def GetValue(self):
        def parse(ctrl):
            value = ctrl.GetValue()
            try:
                return float(value)
            except ValueError:
                raise ValueError, "%s is not a valid float."%value
        return self.kind(*(parse(ctrl) for ctrl in self.ctrls))

class TextEditPanel(wx.Panel):
    edits = (unicode, TlkString)
    
    def __init__(self, *args, **kwargs):
        super(TextEditPanel, self).__init__(*args, **kwargs)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.check_zero = wx.CheckBox(self, label='Zero-terminated')
        self.combo_empty = wx.ComboBox(self, style=wx.CB_READONLY|wx.CB_DROPDOWN, value="empty string", choices=["empty string", "null", "zero"])
        self.tlk_id = IntCtrl(self, min=0, max=0xFFFFFFFF, limited=False, allow_long=True, style=wx.ALIGN_RIGHT)  # SpinCtrl for TlkString
        sizer.Add(self.text_ctrl, 1, wx.EXPAND)
        sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer2.Add(self.check_zero, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL)
        sizer2.Add(self.combo_empty, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL)
        sizer2.Add(self.tlk_id, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL)
        sizer.Add(sizer2, 0, wx.EXPAND)
        self.SetSizer(sizer)
    
    def SetValue(self, value, kind):
        self.kind = kind
        if issubclass(kind, TlkString):
            self.tlk_id.Show()
            self.tlk_id.SetValue(value.label)
            value = value.s
        else:
            self.tlk_id.Hide()
        self.combo_empty.SetValue("empty string")
        if value == None:
            self.text_ctrl.SetValue('')
            self.check_zero.SetValue(True)
            self.combo_empty.SetValue("null")
        elif value == 0:
            self.text_ctrl.SetValue('')
            self.check_zero.SetValue(True)
            self.combo_empty.SetValue("zero")
        elif value.endswith(chr(0)):
            self.text_ctrl.SetValue(value[:-1])
            self.check_zero.SetValue(True)
        else:
            self.text_ctrl.SetValue(value)
            self.check_zero.SetValue(False)
        self.Layout()
    
    def GetValue(self):
        if issubclass(self.kind, ECString):
            s = self.text_ctrl.GetValue()
            if not s:
                cv = self.combo_empty.GetValue()
                if cv == 'zero':
                    raise ValueError, 'zero is not a valid treatment of an empty string of this type'
                elif cv == 'null':
                    return None
                elif self.check_zero.GetValue():
                    return chr(0)
                else:
                    return ''
            elif self.check_zero.GetValue():
                return s+chr(0)
            else:
                return s
        elif issubclass(self.kind, TlkString):
            tlkid = long(self.tlk_id.Value)
            s = self.text_ctrl.Value
            if not s:
                cv = self.combo_empty.Value
                if cv == 'zero':
                    return self.kind(tlkid, 0)
                elif cv == 'null':
                    return self.kind(tlkid, None)
                elif self.check_zero.Value:
                    return self.kind(tlkid, chr(0))
                else:
                    return self.kind(tlkid, '')
            elif self.check_zero.Value:
                return self.kind(tlkid, s+chr(0))
            else:
                return self.kind(tlkid, s)

class BinaryEditPanel(wx.Panel):
    edits = str
    
    def __init__(self, *args, **kwargs):
        super(BinaryEditPanel, self).__init__(*args, **kwargs)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.TE_READONLY)
        font = wx.Font(10, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, '')
        self.text_ctrl.SetFont(font)
        self.sizer.Add(self.text_ctrl, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        
        self.exportmenu = wx.Menu()
        exportitem = self.exportmenu.Append(wx.ID_ANY, "Export to file", "Export binary data to file")
        importitem = self.exportmenu.Append(wx.ID_ANY, "Import from file", "Import binary data from file")
        self.Bind(wx.EVT_MENU, self.OnExport, exportitem)
        self.Bind(wx.EVT_MENU, self.OnImport, importitem)
        self.text_ctrl.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)
    
    def SetValue(self, value, kind=Binary):
        if not issubclass(kind, str):
            raise ValueError
        self.kind = kind
        self.real_value = value
        self.text_ctrl.SetValue(encodestring(value))
    
    def GetValue(self):
        #value = self.kind(decodestring(self.text_ctrl.GetValue()))
        return self.real_value
    
    def OnExport(self, event):
        data = self.real_value
        
        with wx.FileDialog(self, "Choose a filename", '', '', "*.*", wx.SAVE|wx.FD_OVERWRITE_PROMPT) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                path = dlg.Path
            else:
                return
        
        if detect_zlib(data[:64]):
            with wx.MessageDialog(self, "Data is compressed, decompress before saving?", "Compressed Data", wx.YES_NO|wx.ICON_QUESTION) as dlg:
                if dlg.ShowModal() == wx.ID_YES:
                    try:
                        data = zlib.decompress(data)
                    except zlib.error:
                        with wx.MessageDialog(self, "Decompression failed, save original data?", "Decompression Failure", wx.YES_NO|wx.ICON_ERROR) as dlg:
                            if dlg.ShowModal() == wx.ID_NO:
                                return
        
        with open(path, 'wb') as f:
            f.write(data)
    
    def OnImport(self, event):
        olddata = self.real_value
        
        with wx.FileDialog(self, "Choose a file", '', '', "*.*", wx.OPEN|wx.FD_FILE_MUST_EXIST) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                path = dlg.Path
            else:
                return
        
        with open(path, 'rb') as f:
            data = f.read()
        length = len(data)
        
        if detect_zlib(olddata[:64]) and not detect_zlib(data[:64]):
            with wx.MessageDialog(self, "Replacing compressed data with uncompressed. Compress before saving?", "Uncompressed Data", wx.YES_NO|wx.ICON_QUESTION) as dlg:
                if dlg.ShowModal() == wx.ID_YES:
                    data = zlib.compress(data)
        
        self.real_value = data
        self.text_ctrl.SetValue(encodestring(data))
        
        with wx.TextEntryDialog(self, 'The following number of bytes were imported:','Import Succeeded', str(length), style=wx.OK|wx.TE_READONLY) as dlg:
            dlg.ShowModal()
    
    def OnRightUp(self, evt):
        self.PopupMenu(self.exportmenu, evt.Position)

def detect_zlib(sample):
    try:
        zlib.decompressobj().decompress(sample)
    except:
        return False
    else:
        return True

class PrimitiveEditPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(PrimitiveEditPanel, self).__init__(*args, **kwargs)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.panels = []
        for cls in (IntegerEditPanel, FloatEditPanel, FloatTupleEditPanel, MatrixEditPanel, TextEditPanel, BinaryEditPanel):
            panel = cls(self)
            self.panels.append(panel)
            sizer.Add(panel, 1, wx.EXPAND)
            panel.Hide()
        
        self.active_panel = self.panels[0]
        
        self.button_panel = wx.Panel(self)
        bsizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.save_button = wx.Button(self.button_panel, label='&Save')
        bsizer.Add(self.save_button, flag=wx.TOP, border=5)
        self.Bind(wx.EVT_BUTTON, self.OnSave, self.save_button)
        
        self.reset_button = wx.Button(self.button_panel, label='&Reset')
        bsizer.Add(self.reset_button, flag=wx.TOP, border=5)
        self.Bind(wx.EVT_BUTTON, self.OnReset, self.reset_button)
        
        self.delete_button = wx.Button(self.button_panel, label='&Delete')
        bsizer.Add(self.delete_button, flag=wx.TOP, border=5)
        self.Bind(wx.EVT_BUTTON, self.OnDelete, self.delete_button)
        
        self.create_button = wx.Button(self.button_panel, label='&Create')
        bsizer.Add(self.create_button, flag=wx.TOP, border=5)
        self.Bind(wx.EVT_BUTTON, self.OnCreate, self.create_button)
        
        self.button_panel.SetSizer(bsizer)
        sizer.Add(self.button_panel, 0, wx.EXPAND)
        
        self.SetSizer(sizer)
    
    def Edit(self, value, kind, indirect, callback):
        self.Freeze()
        self.active_panel.Hide()
        self.delete_button.Hide()
        self.create_button.Hide()
        if indirect:
            if value is not None:
                self.delete_button.Show()
            else:
                self.create_button.Show()
        
        if issubclass(kind, List):
            if issubclass(kind.elem_type, UINT8) and not indirect:
                kind = Binary
            else:
                raise ValueError
        
        self.active_panel = None
        for panel in self.panels:
            if issubclass(kind, panel.edits):
                self.active_panel = panel
                break
        if not self.active_panel:
            raise ValueError
        
        self.value = value
        self.kind = kind
        self.indirect = indirect
        self.current_callback = callback
        self.active_panel.SetValue(value, kind)
        self.active_panel.Show()
        self.Layout()
        self.Thaw()
    
    def OnReset(self, event):
        self.active_panel.SetValue(self.value, self.kind)
    
    def OnSave(self, event):
        try:
            value = self.active_panel.GetValue()
            self.current_callback(value)
            self.value = value
        except ValueError, e:
            with wx.MessageDialog(self, repr(e), "Edit Error", wx.OK|wx.ICON_ERROR) as dlg:
                dlg.ShowModal()
    
    def OnDelete(self, event):
        value, kind, indirect = self.current_callback()
        if kind:
            self.Edit(value, kind, indirect, self.current_callback)
    
    def OnCreate(self, event):
        value, kind, indirect = self.current_callback(create_new=True)
        self.Edit(value, kind, indirect, self.current_callback)

class StructureEditPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(StructureEditPanel, self).__init__(*args, **kwargs)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        panel = wx.Panel(self)
        sizer.Add(panel, 1, wx.EXPAND)
        
        self.button_panel = wx.Panel(self)
        bsizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.delete_button = wx.Button(self.button_panel, label='&Delete')
        bsizer.Add(self.delete_button)
        self.Bind(wx.EVT_BUTTON, self.OnDelete, self.delete_button)
        self.delete_button.Hide()
        
        self.create_button = wx.Button(self.button_panel, label='&Create')
        bsizer.Add(self.create_button)
        self.Bind(wx.EVT_BUTTON, self.OnCreate, self.create_button)
        self.create_button.Hide()
        
        self.button_panel.SetSizer(bsizer)
        sizer.Add(self.button_panel, 0, wx.EXPAND)
        
        self.SetSizer(sizer)
    
    def Edit(self, value, kind, indirect, callback):
        self.Freeze()
        self.delete_button.Hide()
        self.create_button.Hide()
        if indirect:
            if value is not None:
                self.delete_button.Show()
            else:
                self.create_button.Show()
        
        self.current_callback = callback
        self.Layout()
        self.Thaw()
    
    def OnDelete(self, event):
        value, kind, indirect = self.current_callback()
        if kind:
            self.Edit(value, kind, indirect, self.current_callback)
    
    def OnCreate(self, event):
        value, kind, indirect = self.current_callback(create_new=True)
        if kind:
            self.Edit(value, kind, indirect, self.current_callback)

def GetTypeByDialog(self, types, default=None):
    with wx.SingleChoiceDialog(self,
            "Choose the type that will be created", "Choose Type",
            [cls.fourcc if issubclass(cls, Structure) else cls.__name__ for cls in types]) as dlg:
        if default:
            dlg.SetSelection(types.index(default))
        kind = None
        if dlg.ShowModal() == wx.ID_OK:
            kind = types[dlg.GetSelection()]
    return kind

class ListEditPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(ListEditPanel, self).__init__(*args, **kwargs)
        
        self.lst = AutoWidthListCtrl(self, style=wx.LC_REPORT)
        self.lst.InsertColumn(0, "Index")
        self.lst.InsertColumn(1, "Type")
        self.lst.InsertColumn(2, "Value")
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnItemActivated, self.lst)
        
        listbtns = wx.Panel(self)
        
        add_button = wx.Button(listbtns, label='&Add')
        self.Bind(wx.EVT_BUTTON, self.OnAdd, add_button)
        
        remove_button = wx.Button(listbtns, label='&Remove')
        self.Bind(wx.EVT_BUTTON, self.OnRemove, remove_button)
        
        moveup = wx.Button(listbtns, label='Move &Up')
        self.Bind(wx.EVT_BUTTON, self.OnMoveUp, moveup)
        
        movedown = wx.Button(listbtns, label='Move &Down')
        self.Bind(wx.EVT_BUTTON, self.OnMoveDown, movedown)
        
        aTable = wx.AcceleratorTable([
            (wx.ACCEL_ALT, wx.WXK_UP, moveup.GetId()),
            (wx.ACCEL_ALT, wx.WXK_DOWN, movedown.GetId()),
            (wx.ACCEL_NORMAL, wx.WXK_INSERT, add_button.GetId()),
            (wx.ACCEL_NORMAL, wx.WXK_DELETE, remove_button.GetId())
        ])
        self.SetAcceleratorTable(aTable)
        
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(add_button)
        vsizer.Add(remove_button)
        vsizer.Add(moveup)
        vsizer.Add(movedown)
        listbtns.SetSizer(vsizer)
        
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(listbtns, 0, wx.ALIGN_CENTER_VERTICAL)
        hsizer.Add(self.lst, 1, wx.EXPAND)
        self.SetSizer(hsizer)

    def Edit(self, value, kind, indirect, callback):
        if indirect:
            raise ValueError
        self.current_value = value
        self.current_kind = kind
        self.current_callback = callback
        lst = self.lst
        lst.DeleteAllItems()
        if value:
            for v in value:
                self._Append(v, lst)
    
    def OnItemActivated(self, event):
        tree = self.tree
        indices = tree.GetIndicesOfItem(tree.Selection) + (event.Index,)
        item = tree.GetRootItem()
        while indices:
            tree.Expand(item)
            child = tree.GetFirstChild(item)[0]
            for n in xrange(indices[0]):
                child = tree.GetNextSibling(child)
            indices = indices[1:]
            item = child
        tree.ScrollTo(item)
        tree.SelectItem(item)
        tree.SetFocus()
    
    def OnAdd(self, evt):
        self.Freeze()
        lst = self.lst
        val = self.current_value
        i = lst.GetFirstSelected()
        kind = self.current_kind.elem_type
        if kind is None:
            if i >= 0:
                v = val[i]
                kind = type(v)
            kind = GetTypeByDialog(self, self.types, kind)
        if kind is None:
            return
        item = coercevalue(None, kind)
        if i < 0:
            i = lst.ItemCount
            j = i
            val.append(item)
            self._Append(item, lst)
            state = wx.LIST_STATE_FOCUSED
        else:
            j = i + 1
            val.insert(j, item)
            self._Insert(j, item, lst)
            state = wx.LIST_STATE_SELECTED|wx.LIST_STATE_FOCUSED
        self._FixIndices(j)
        for i in selectedIndices(lst, i):
            lst.Select(i, False)
        lst.SetItemState(i, state, state)
        self.current_callback()
        self.Thaw()
    
    def OnRemove(self, evt):
        self.Freeze()
        elems, start, end = self._RemoveSelected()
        if start is not None:
            self._FixIndices(start-1)
        #lst.SetFocus()
        self.current_callback()
        self.Thaw()
    
    def OnMoveUp(self, evt):
        self.Freeze()
        elems, start, end = self._RemoveSelected()
        if start is not None:
            if start > 0:
                start -= 1
            self._InsertItems(start, elems)
            self._FixIndices(start+len(elems)-1)
            self.lst.SetItemState(start, wx.LIST_STATE_FOCUSED, wx.LIST_STATE_FOCUSED)
        #lst.SetFocus()
        self.current_callback()
        self.Thaw()
    
    def OnMoveDown(self, evt):
        self.Freeze()
        items, start, end = self._RemoveSelected()
        if end is not None:
            index = start + 1 + (end - start + 1) - len(items)
            if index >= self.lst.ItemCount:
                index = self.lst.ItemCount
            self._InsertItems(index, items)
            self._FixIndices(start - 1)
            self.lst.SetItemState(index+len(items)-1, wx.LIST_STATE_FOCUSED, wx.LIST_STATE_FOCUSED)
        #lst.SetFocus()
        self.current_callback()
        self.Thaw()
    
    def _Append(self, item, lst=None):
        if lst is None:
            lst = self.lst
        if item is None:
            lst.Append((lst.ItemCount, '?', '?'))
        elif isinstance(item, Structure):
            lst.Append((lst.ItemCount, item.fourcc, value_preview(item, 200)))
        else:
            lst.Append((lst.ItemCount, type(item).__name__, value_preview(item, 200)))
    
    def _Insert(self, index, item, lst=None):
        if lst is None:
            lst = self.lst
        if item is None:
            t, s = '?', '?'
        elif isinstance(item, Structure):
            t, s = item.fourcc, value_preview(item, 200)
        else:
            t, s = type(item).__name__, value_preview(item, 200)
        it = wx.ListItem()
        it.SetColumn(0)
        it.SetId(index)
        it.SetText(str(index))
        lst.InsertItem(it)
        it = wx.ListItem()
        it.SetColumn(1)
        it.SetId(index)
        it.SetText(t)
        lst.SetItem(it)
        it = wx.ListItem()
        it.SetColumn(2)
        it.SetId(index)
        it.SetText(s)
        lst.SetItem(it)
        lst.Select(index)
    
    def _FixIndices(self, last_good=-1):
        lst = self.lst
        for i in xrange(last_good+1, lst.ItemCount):
            it = wx.ListItem()
            it.SetColumn(0)
            it.SetId(i)
            it.SetText(str(i))
            lst.SetItem(it)
    
    def _RemoveSelected(self):
        elems = []
        value = self.current_value
        lst = self.lst
        start, end = None, None
        for i in reversed(list(selectedIndices(lst))):
            start = i
            if end is None: end = i
            elems.append(value.pop(i))
            lst.DeleteItem(i)
        elems.reverse()
        return elems, start, end
    
    def _InsertItems(self, index, items):
        value = self.current_value
        lst = self.lst
        value[index:index] = items
        for i, v in zip(icount(index), items):
            self._Insert(i, v, lst)

class GenericReferenceEditPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(GenericReferenceEditPanel, self).__init__(*args, **kwargs)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        panel = wx.Panel(self)
        sizer.Add(panel, 1, wx.EXPAND)
        
        self.button_panel = wx.Panel(self)
        bsizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.create_button = wx.Button(self.button_panel, label='&Create')
        bsizer.Add(self.create_button)
        self.Bind(wx.EVT_BUTTON, self.OnCreate, self.create_button)
        
        self.button_panel.SetSizer(bsizer)
        sizer.Add(self.button_panel, 0, wx.EXPAND)
        
        self.SetSizer(sizer)
    
    def Edit(self, value, kind, indirect, callback):
        self.current_callback = callback
    
    def OnCreate(self, event):
        kind = GetTypeByDialog(self, self.types)
        if kind is not None:
            self.current_callback(kind, True)

class EditPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(EditPanel, self).__init__(*args, **kwargs)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.nothing_panel = PlaceholderPanel(self)
        self.sizer.Add(self.nothing_panel, 1, wx.EXPAND)
        self.active_panel = self.nothing_panel
        
        self.prim_panel = PrimitiveEditPanel(self)
        self.sizer.Add(self.prim_panel, 1, wx.EXPAND)
        self.prim_panel.Hide()
        
        self.strct_panel = StructureEditPanel(self)
        self.sizer.Add(self.strct_panel, 1, wx.EXPAND)
        self.strct_panel.Hide()
        
        self.lst_panel = ListEditPanel(self)
        self.sizer.Add(self.lst_panel, 1, wx.EXPAND)
        self.lst_panel.Hide()
        
        self.ref_panel = GenericReferenceEditPanel(self)
        self.sizer.Add(self.ref_panel, 1, wx.EXPAND)
        self.ref_panel.Hide()
        
        self.SetSizer(self.sizer)
    
    def Edit(self, value, kind, indirect, callback):
        self.Freeze()
        self.active_panel.Hide()
        
        oldkind = kind
        if indirect and kind is None and value is not None:
            kind = type(value)
        
        #print type(value), type(kind)
        
        if oldkind is None:
            if value is None:
                self.active_panel = self.ref_panel
            elif isinstance(value, List):
                self.active_panel = self.lst_panel
            elif isinstance(value, Structure):
                self.active_panel = self.strct_panel
            else:
                self.active_panel = self.prim_panel
        elif issubclass(oldkind, List):
            if isinstance(value, Binary):
                self.active_panel = self.prim_panel
            else:
                self.active_panel = self.lst_panel
        elif issubclass(oldkind, Structure):
            self.active_panel = self.strct_panel
        else:
            self.active_panel = self.prim_panel
            
        self.value = value
        self.kind = kind
        self.indirect = indirect
        self.callback = callback
        
        self.active_panel.Edit(value, kind, indirect, callback)
        self.active_panel.Show()
        self.Layout()
        self.Thaw()
    
    def Clear(self):
        self.Freeze()
        self.active_panel.Hide()
        self.active_panel = self.nothing_panel
        self.value = None
        self.kind = None
        self.indirect = None
        self.callback = None
        self.active_panel.Show()
        self.Layout()
        self.Thaw()
