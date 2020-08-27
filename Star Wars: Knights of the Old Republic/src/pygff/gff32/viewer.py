import wx, wx.gizmos
from wx.lib.mixins.treemixin import VirtualTree
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin, TextEditMixin
from gff32.types import *

_EDITABLE = False

def value_preview(data):
    if isinstance(data, Structure):
        if 'Tag' in data:
            return '# %s'%data['Tag']
        else:
            return '...'
    elif isinstance(data, List):
        return '(%d items)'%len(data)
    elif isinstance(data, ExoLocString):
        return str(data.stringref)
    else:
        return str(data)

class TreeListUtilMixin(object):
    def GetIndicesOfItem(self, item):
        indices = ()
        while item != self.GetRootItem():
            pitem = self.GetItemParent(item)
            citem, what = self.GetFirstChild(pitem)
            i = 0
            while citem != item:
                i += 1
                citem = self.GetNextSibling(citem)
            indices = (i,) + indices
            item = pitem
        return indices
    
    def RefreshItemAncestors(self, item, itemIndex=None):
        if not itemIndex:
            itemIndex = self.GetItemByIndex(item)
        while itemIndex:
            self.RefreshItem(itemIndex)
            itemIndex = itemIndex[:-1]
    
    def SelectItemByIndices(self, indices):
        item = self.GetRootItem()
        while indices:
            self.Expand(item)
            child = self.GetFirstChild(item)[0]
            for n in xrange(indices[0]):
                child = self.GetNextSibling(child)
            indices = indices[1:]
            item = child
        self.ScrollTo(item)
        self.SelectItem(item)
        self.SetFocus()

class GFFTree(VirtualTree, wx.gizmos.TreeListCtrl, TreeListUtilMixin):# ListCtrlAutoWidthMixin):
    def __init__(self, *args, **kwargs):
        super(GFFTree, self).__init__(*args, **kwargs)
        #ListCtrlAutoWidthMixin.__init__(self)
        self.AddColumn('Label', 200)
        self.AddColumn('Type', 90)
        self.AddColumn('Value', 400)
        
        if _EDITABLE:
            self.SetColumnEditable(2, True)
            
            self.Bind(wx.EVT_TREE_BEGIN_LABEL_EDIT, self.OnBeginEdit)
            self.Bind(wx.EVT_TREE_END_LABEL_EDIT, self.OnEndEdit)
    
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, model):
        self._model = model
        self.RefreshItems()
    
    def OnGetItemText(self, index, column=0):
        return self.GetText(index, column)
        
    def OnGetChildrenCount(self, index):
        return self.GetChildrenCount(index)

    def GetItem(self, indices):
        if self.model is None:
            return None, None, None, 0
        if not len(indices):
            return None, None, None, 1
        data = self.model
        container = None
        field = None
        count = len(data)
        for index in indices[1:]:
            container = data
            if isinstance(data, Structure):
                field = data.keys()[index]
                data = data[field]
            elif isinstance(data, List):
                field = None
                data = data[index]
            elif isinstance(data, ExoLocString):
                field = None
                data = data.strings[index]
            else:
                raise ValueError
            
            if isinstance(data, (Structure, List)):
                count = len(data)
            elif isinstance(data, ExoLocString):
                count = len(data.strings)
            else:
                count = 0
        
        return container, field, data, count

    def GetText(self, indices, column):
        container, field, data, count = self.GetItem(indices)
        if column == 0:
            if len(indices) == 1:
                return '%s %s'%(data.filetype, data.fileversion)
            elif field:
                return field
            elif indices:
                return str(indices[-1])
            else:
                return ''
        elif column == 1:
            if isinstance(data, Structure):
                return 'Structure:%d'%data.structid
            else:
                return type(data).__name__
        elif column == 2:
            return value_preview(data)
        return '%s:%s'%(indices, column)
    
    def GetChildrenCount(self, indices):
        return self.GetItem(indices)[3]
    
    def OnBeginEdit(self, event):
        self.edit_column = event.GetInt()
        #print self.GetIndicesOfItem(event.Item)
        event.Skip()
    
    def OnEndEdit(self, event):
        print self.GetIndicesOfItem(event.Item), self.edit_column
