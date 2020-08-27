import wx, re
import wx.lib.delayedresult as delayedresult
from gff4 import *
from gff4.editorutils import *
from functools import partial

class SearchPanel(wx.Panel):

    def __init__(self, *args, **kwargs):
        super(SearchPanel, self).__init__(*args, **kwargs)
        
        self.truncate = 20
        self.root = None
        self.indices = (0,)
        self.tree = None
        
        self.string_text = wx.SearchCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnSearchText, self.string_text)
        search_menu = wx.Menu()
        self.string_text.Menu = search_menu
        select_root = search_menu.Append(wx.ID_ANY, "Show Root", "Show node being searched from in tree")
        self.Bind(wx.EVT_MENU, self.OnShowRoot, select_root)
        self.search_button = wx.Button(self, label='Search')
        self.Bind(wx.EVT_BUTTON, self.OnSearchText, self.search_button)
        self.results = AutoWidthListCtrl(self, style=wx.LC_REPORT)
        self.results.InsertColumn(0, "Results")
        self.result_indices = []
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnResultActivated, self.results)
        
        self.sizer = wx.GridBagSizer(5, 5)
        self.sizer.AddGrowableCol(0, 1)
        self.sizer.AddGrowableRow(1, 1)
        self.sizer.Add(self.string_text, pos=(0,0), flag=wx.EXPAND)
        self.sizer.Add(self.search_button, pos=(0,1))
        self.sizer.Add(self.results, pos=(1,0), span=(1,2), flag=wx.EXPAND)
        self.SetSizer(self.sizer)
    
    def OnSearchText(self, event):
        if not self.string_text.GetValue():
            return
        self.results.DeleteAllItems()
        del self.result_indices[:]
        pattern = re.compile(self.string_text.GetValue())
        
        if self.root is None and self.indices:
            self.root = self.tree.model.GetItem(self.indices)[2]
        if isinstance(self.root, (List, Structure)):
            self.progress = wx.ProgressDialog("Searching...", 'Searching for "%s"'%pattern.pattern, parent=self, style=wx.PD_CAN_ABORT|wx.PD_ELAPSED_TIME|wx.PD_SMOOTH)
            from random import random
            def check(s):
                if random() < 0.05:
                    cont, skip = self.progress.UpdatePulse()
                    if not cont:
                        raise StopIteration, 'search cancelled'
                m = pattern.search(s)
                return bool(m)
            def store(s, indices):
                #if m.start() > self.truncate:
                #    self.results.Append(('...'+(s[m.start()-self.truncate-3:]),))
                #else:
                self.results.Append((s,))
                self.result_indices.append(indices)
            self.search_button.Enabled = False
            
            #search = SearchString(check, store, self.indices)
            #self.root.accept(search)
            #self.search_button.Enabled = True
            
            search = SearchString(check, partial(wx.CallAfter, store), self.indices)
            delayedresult.startWorker(self.OnSearchDone, self.root.accept, wargs=[search])
        elif isinstance(self.root, unicode):
            if pattern.search(self.root):
                self.results.Append((self.root,))
                self.result_indices.append(self.indices)
    
    def OnSearchDone(self, result):
        self.search_button.Enabled = True
        self.progress.Destroy()
        try:
            result.get()
        except StopIteration:
            pass
    
    def OnResultActivated(self, event):
        self.tree.SelectItemByIndices(self.result_indices[event.GetIndex()])
    
    def SearchFrom(self, root, indices):
        self.root = root
        self.indices = indices
        self.string_text.SetFocus()
    
    def Clear(self):
        self.indices = (0,)
        self.root = None
        self.results.DeleteAllItems()
        del self.result_indices[:]
    
    def OnShowRoot(self, event):
        self.tree.SelectItemByIndices(self.indices)

class SearchString(object):
    def __init__(self, check, store, indices):
        self.check = check
        self.store = store
        self.indices = list(indices)
        self.inlist = [False]
    
    def search(self, s):
        if self.check(s):
            self.store(s, tuple(self.indices))
    
    def visit_data(self, value):
        if self.inlist[-1]:
            self.indices[-1] += 1
        if isinstance(value, unicode):
            self.search(value)
        elif isinstance(value, TlkString):
            if isinstance(value.s, unicode):
                self.search(value.s)
    
    def visit_structure(self, structure):
        if self.inlist[-1]:
            self.indices[-1] += 1
        self.inlist.append(False)
        self.indices.append(-1)
    
    def visit_field(self, field):
        self.indices[-1] += 1
        return field.type is not None and \
            not issubclass(field.type, (List, Structure, ECString, TlkString))
    
    def leave_structure(self):
        self.inlist.pop()
        self.indices.pop()
    
    def visit_list(self, lst):
        self.inlist.append(True)
        self.indices.append(-1)
        return lst.elem_type is not None and \
            not issubclass(lst.elem_type, (Structure, ECString, TlkString))
    
    def leave_list(self):
        self.inlist.pop()
        self.indices.pop()
