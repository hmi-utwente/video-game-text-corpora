import wx
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin
from gff4 import *
from string import ascii_letters, digits

id_letters = ascii_letters+digits+'_'

class AutoWidthListCtrl(wx.ListCtrl, ListCtrlAutoWidthMixin):
    def __init__(self, *args, **kwargs):
        wx.ListCtrl.__init__(self, *args, **kwargs)
        ListCtrlAutoWidthMixin.__init__(self)

def value_preview(data, maxlen=100):
    if isinstance(data, List):
        if data is None or not len(data):
            return '(no items)'
        elif len(data) == 1:
            return '(1 item)'
        else:
            return '(%d items)'%len(data)
    elif isinstance(data, Structure):
        strs = []
        totallen = 0
        for label in data:
            if strs:
                totallen += 2
            item = data[label]
            if isinstance(item, (Structure, List, tuple)):
                strs.append('...')
                break
            #elif isinstance(item, Structure):
            #    return '' #strs.append('{...}')
            #elif isinstance(item, List):
            #    return '' #strs.append('[...]')
            #elif isinstance(item, tuple):
            #    return '' #strs.append('(...)')
            elif isinstance(item, basestring):
                #if len(item) > 20:
                #    strs.append(repr(unicode(item[0:20]+'...')))
                #else:
                if any(c in ascii_letters for c in item) and all(c in id_letters for c in item.strip(chr(0))):
                    strs.append(item.strip(chr(0)))
                elif isinstance(item, unicode):
                    strs.append(repr(item.strip('\0').replace('\0',' '))[1:])
                else:
                    strs.append(repr(str(item)))
            elif item is None:
                strs.append('?')
            else:
                strs.append(unicode(item))
            totallen += len(strs[-1])
            if totallen > maxlen:
                strs[-1] = '...'
                break
        return ', '.join(strs)
    elif isinstance(data, tuple):
        return ', '.join(unicode(x) for x in data)
    elif data is None:
        return '?'
    elif isinstance(data, str):
        return repr(str(data))
    elif isinstance(data, unicode):
        #return repr(unicode(data))
        return data.replace('\0',' ')
    else:
        return unicode(data)

def selectedIndices(lst, i=-1):
    if i < 0:
        i = lst.GetFirstSelected()
    while i >= 0:
        yield i
        i = lst.GetNextSelected(i)
