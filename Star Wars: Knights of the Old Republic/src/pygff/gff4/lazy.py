from warnings import warn
from functools import partial
from gff4 import *
from array import array

class LazyStructure(object):
    def __init__(self, *args, **kwargs):
        self._changed = set()
        super(LazyStructure, self).__init__(*args, **kwargs)
    
    def __getitem__(self, key):
        value = super(LazyStructure, self).__getitem__(key)
        if isinstance(value, partial):
            value = value()
            self._dict[key] = value
        return value
    
    def __setitem__(self, key, value):
        super(LazyStructure, self).__setitem__(key, value)
        self._changed.add(key)
    
    def isloaded(self, key):
        return key in self._dict and not isinstance(self._dict[key], partial)
    
    def ischanged(self, key):
        return key in self._changed

class LazyList(object):
    def __init__(self, *args, **kwargs):
        self._changed = False
        self._offsets = []
        self._original_size = 0
        super(LazyList, self).__init__(*args, **kwargs)
    
    def __getitem__(self, i):
        value = super(LazyList, self).__getitem__(i)
        if isinstance(i, slice):
            value = [v() if isinstance(v, partial) else v]
            self._list[i] = value
        elif isinstance(value, partial):
            value = value()
            self._list[i] = value
        return value
    
    def __setitem__(self, i, value):
        super(LazyList, self).__setitem__(i, value)
        self._changed = True
        if isinstance(i, slice):
            self._offsets[i] = [None]*len(value)
        else:
            self._offsets[i] = None
    
    def __delitem__(self, i):
        super(LazyList, self).__delitem__(i)
        self._changed = True
        del self._offsets[i]
    
    def insert(self, i, value):
        super(LazyList, self).insert(i, value)
        self._changed = True
        self._offsets.insert(i, None)
    
    def _append(self, value, offset):
        self._list.append(value)
        self._offsets.append(offset)

class LazyGFF4(object):
    def __init__(self, f, preload=False):
        self.file = f
        self.oldheader = read_header(f)
        f.seek(0)
        self._headerdata = f.read(self.oldheader.string_offset)
        self._bigendian = isbeplatform(self.oldheader.platform)
        version = real_version(self.oldheader.version, self.oldheader.platform)
        self.use_cstring = (version >= 'V4.1')
        self._preload_embedded_structs = True
        self._preload_references = preload
        self._off2obj = dict()
        self._objid2off = dict()
        
        headerstructs = self.oldheader.structs
        structrange = xrange(len(headerstructs))
        queue = set(structrange)
        not_roots = set()
        structs = dict()
        lists = dict()
        def make_field(field):
            kind = field.type
            if issubclass(kind, List):
                elem_type = kind.elem_type
                if issubclass(elem_type, Structure):
                    elem_type = make_structure(headerstructs.index(elem_type))
                if (elem_type, kind.indirect) in lists:
                    kind = lists[(elem_type, kind.indirect)]
                else:
                    #possibly don't do this for primitive non-string non-reference lists
                    kind = type(kind.__name__+'Lazy', (LazyList, kind), dict(__slots__=(), elem_type=elem_type))
                    #print kind, kind.elem_type
                    lists[(elem_type, kind.indirect)] = kind
            elif issubclass(kind, Structure):
                kind = make_structure(headerstructs.index(kind))
            elif kind is None and not field.indirect:
                raise ValueError, 'Cannot have a generic field that is not a reference'
            return Field(field.label, kind, field.indirect, field.offset)
        def make_structure(i, root=False):
            if not root:
                not_roots.add(i)
            if i not in structs:
                oldstruct = headerstructs[i]
                struct = type(oldstruct.__name__+'Lazy', (LazyStructure, oldstruct), dict(__slots__=()))
                
                structs[i] = struct
                queue.remove(i)
                
                fields = tuple(make_field(field) for field in oldstruct.fields)
                fieldsbylabel = dict((field.label, field) for field in fields)
                def getfieldbylabel(self, label):
                    return fieldsbylabel[label]
                struct.fields = fields
                struct.getfieldbylabel = getfieldbylabel
                
                return struct
            else:
                return structs[i]
        while queue:
            make_structure(min(queue), True)
        self._header = self.oldheader._replace(structs=tuple(structs[i] for i in structrange))
        self.roots = set(structrange).difference(not_roots)
        self._root = None
        
        if self.use_cstring:
            f.seek(self.header.string_offset)
            strings = f.read(self.header.data_offset - self.header.string_offset)
            strings = strings.split('\0')
            #print len(strings), self.header.string_count
            strings = strings[:self.header.string_count]
            self.stringcache = [s.decode('utf-8') for s in strings]
        else:
            self.stringcache = dict()
        
        f.seek(self.header.data_offset)
        self._data = f.read()
    
    @property
    def root(self):
        if self._root is None:
            self._root = root = self._read_struct(self.header.structs[0], 0)
            root.gff = self
            root.header = self._header
        return self._root
    
    @property
    def header(self):
        return self._header
    
    def __getitem__(self, i):
        if i == 0:
            return self.header
        elif i == 1:
            return self.root
        else:
            raise IndexError
    
    def __len__(self):
        return 2
    
    def __iter__(self):
        yield self.header
        yield self.root

    def _read_struct(self, structtype, offset):
        res = structtype()
        self._off2obj[offset] = res
        self._objid2off[id(res)] = offset
        for field in structtype.fields:
            res._dict[field.label] = self._read_field(field, offset + field.offset)
        return res

    def _read_field(self, field, offset):
        fieldtype = field.type
        if field.indirect:
            return self._read_reference(fieldtype, offset)
        elif issubclass(fieldtype, List):
            address, = UINT32.format[self._bigendian].unpack_from(self._data, offset)
            if address == 0xFFFFFFFF:
                return fieldtype()
            else:
                return self._defer_list(fieldtype, address)
        elif issubclass(fieldtype, Structure):
            if self._preload_embedded_structs:
                return self._read_struct(fieldtype, offset)
            else:
                return self._defer_struct(fieldtype, offset)
        else:
            return self._read_value(fieldtype, offset)
    
    def _read_list(self, listtype, offset):
        elemtype = listtype.elem_type
        bigendian = self._bigendian
        
        #print f.tell(), elemtype, listtype.indirect
        
        length, = UINT32.format[bigendian].unpack_from(self._data, offset)
        elem_offset = offset + UINT32.size
        res = listtype()
        res._original_size = length
        self._off2obj[offset] = res
        self._objid2off[id(res)] = offset
        
        if listtype.indirect:
            if elemtype is None:
                for i in xrange(length):
                    g_ref = self._read_generic(elem_offset)
                    if g_ref.is_list or g_ref.is_reference:
                        raise Exception('generic list with list or reference element %s'%(g_ref,))
                    elif g_ref.address == 0xFFFFFFFF:
                        warn('null generic list value')
                        res._append(None, elem_offset)
                    elif g_ref.is_struct:
                        res._append(self._defer_struct(self.header.structs[g_ref.type], g_ref.address), elem_offset)
                    elif g_ref.type == ECString.id:
                        res._append(self._defer_string(g_ref.address), elem_offset)
                    else:
                        res._append(self._defer_value(TYPES_BY_ID[g_ref.type], g_ref.address), elem_offset)
                    elem_offset += Generic.size
            else:
                for i in xrange(length):
                    address, = UINT32.format[bigendian].unpack_from(self._data, elem_offset)
                    if address == 0xFFFFFFFF:
                        warn('null list value')
                        res._append(None, elem_offset)
                    elif issubclass(elemtype, Structure):
                        res._append(self._defer_struct(elemtype, address), elem_offset)
                    elif issubclass(elemtype, ECString):
                        res._append(self._defer_string(address), elem_offset)
                    else:
                        res._append(self._defer_value(elemtype, address), elem_offset)
                    elem_offset += Reference.size
        elif issubclass(elemtype, Structure):
            for i in xrange(length):
                res._append(self._read_struct(elemtype, elem_offset), elem_offset)
                elem_offset += elemtype.size
        elif issubclass(elemtype, UINT8):
            return Binary(self._data[elem_offset:elem_offset+length])
        else:
            for i in xrange(length):
                res._append(self._read_value(elemtype, elem_offset), elem_offset)
                elem_offset += elemtype.size
        return res
    
    def _read_reference(self, reftype, offset):
        if reftype is None:
            g_ref = self._read_generic(offset)
            if g_ref.address == 0xFFFFFFFF:
                return None
            elif g_ref.is_list or g_ref.is_reference:
                raise Exception('generic list or reference element %s'%(g_ref,))
            elif g_ref.is_struct:
                return self._defer_struct(self.header.structs[g_ref.type], g_ref.address)
            elif g_ref.type == ECString.id:
                return self._defer_string(g_ref.address)
            else:
                return self._defer_value(TYPES_BY_ID[g_ref.type], g_ref.address)
        else:
            address, = UINT32.format[self._bigendian].unpack_from(self._data, offset)
            if address == 0xFFFFFFFF:
                return None
            elif issubclass(reftype, Structure):
                return self._defer_struct(reftype, address)
            elif isinstance(reftype, ECString):
                return self._defer_string(address)
            else:
                return self._defer_value(reftype, address)

    def _read_value(self, datatype, offset):
        if datatype is ECString:
            address, = datatype.format[self._bigendian].unpack_from(self._data, offset)
            if address == 0xFFFFFFFF:
                return None
            return self._defer_string(address)
        elif datatype is TlkString:
            label, address = datatype.format[self._bigendian].unpack_from(self._data, offset)
            if address == 0xFFFFFFFF:
                return TlkString(label, None)
            elif address != 0 or self.use_cstring:
                return self._defer_string(address, label)
            else:
                return TlkString(label, 0)
        else:
            return datatype(*datatype.format[self._bigendian].unpack_from(self._data, offset))
    
    def _read_string(self, offset, tlk=None):
        if self.use_cstring:
            try:
                s = self.stringcache[offset]
            except IndexError:
                raise IndexError, ('list index out of range', offset, len(self.stringcache))
        else:
            try:
                s = self.stringcache[offset]
            except KeyError:
                length, = UINT32.format[self._bigendian].unpack_from(self._data, offset)
                s = self._data[offset+4:offset+4+2*length].decode('utf_16le')
                self.stringcache[offset] = s
        if tlk is not None:
            return TlkString(tlk, s)
        else:
            return ECString(s)

    def _read_generic(self, offset):
        type_id, address = Generic.format[self._bigendian].unpack_from(self._data, offset)
        type_flags, type_id = type_id >> 16, type_id & 0xffff
        is_list, is_struct, is_reference = unpack_flags(type_flags, address != 0xFFFFFFFF)
        return Generic(type_id, is_list, is_struct, is_reference, address)
    
    def _defer_struct(self, structtype, offset):
        if self._preload_references:
            return self._read_struct(structtype, offset)
        else:
            return partial(self._read_struct, structtype, offset)
    
    def _defer_list(self, listtype, offset):
        if self._preload_references:
            return self._read_list(listtype, offset)
        else:
            return partial(self._read_list, listtype, offset)
    
    def _defer_value(self, datatype, offset):
        if self._preload_references:
            return self._read_value(datatype, offset)
        else:
            return partial(self._read_value, datatype, offset)
    
    def _defer_string(self, offset, tlk=None):
        if self._preload_references:
            return self._read_string(offset, tlk)
        else:
            return partial(self._read_string, offset, tlk)
    
    def tofile(self, f):
        if self.use_cstring:
            string_list = list(self.stringcache)
            string_cache = dict((s, i) for i, s in enumerate(self.stringcache))
        else:
            string_cache = dict()
        
        def_align = 4
        data_section = array('c', self._data)
        header = self.header
        version = real_version(header.version, header.platform)
        bigendian = self._bigendian
        
        type2struct = dict()
        for i, struct in enumerate(header.structs):
            if struct.fourcc in type2struct:
                raise ValueError, 'Does not support different struct definitions with the same label'
            else:
                type2struct[struct.fourcc] = i
        
        def align_end(align=def_align):
            offset = len(data_section)
            if offset % align:
                padding = align - offset % align
                data_section.extend(repeat('\xFF', padding))
                offset += padding
            return offset
        
        def allocate(size, align=def_align):
            offset = len(data_section)
            if offset % align:
                padding = align - offset % align
                size += padding
                offset += padding
            data_section.extend(repeat('\xFF', size))
            return offset

        def write_struct(structure, data, offset, changed):
            #print data
            #print 'write struct %08X'%f.tell()
            for field in structure.fields:
                if changed or data.isloaded(field.label):
                    write_field(field, data[field.label], offset + field.offset, changed or data.ischanged(field.label))

        def write_field(field, data, offset, changed):
            #print 'write field %08X'%f.tell()
            if issubclass(field.type, List):
                write_list(field, data, offset, changed)
            elif field.indirect:
                if field.type is None:
                    write_generic(data, offset, changed)
                else:
                    write_reference(field.type, data, offset, changed)
            elif issubclass(field.type, Structure):
                write_struct(field.type, data, offset, changed)
            else:
                if changed:
                    write_value(field.type, data, offset)

        def write_list(field, data, offset, changed):
            if not data:
                if changed or (data._changed if hasattr(data, '_changed') else True):
                    UINT32.format[bigendian].pack_into(data_section, offset, 0xFFFFFFFF)
            elif isinstance(data, str):
                if changed:
                    # somehow need to handle shrinking data in-place...
                    address = align_end()
                    data_section.extend(UINT32.format[bigendian].pack(len(data)))
                    data_section.extend(data)
                    UINT32.format[bigendian].pack_into(data_section, offset, address)
            else:
                datatype = data.elem_type
                if data.indirect:
                    if datatype is None:
                        elem_size = Generic.size
                    else:
                        elem_size = Reference.size
                else:
                    elem_size = datatype.size
                size = 4 + len(data) * elem_size
                
                data_changed = data._changed if hasattr(data, '_changed') else True
                address = self._objid2off.get(id(data))
                in_data = address is not None
                if not in_data or self._off2obj[address] is not data or len(data) > data._original_size:
                    if data_changed or not in_data:
                        address = allocate(size)
                    else:
                        address = align_end()
                    changed = True
                
                if data_changed or not in_data:
                    #print 'full list rebuild'
                    UINT32.format[bigendian].pack_into(data_section, address, len(data))
                    elem_start = address + UINT32.size
                    elem_end = address + size
                    elem_offsets = xrange(elem_start, elem_end, elem_size)
                    
                    if data.indirect:
                        if datatype is None:
                            def write(datatype, item, elem_offset, elem_changed):
                                write_generic(item, elem_offset, elem_changed)
                        else:
                            def write(datatype, item, elem_offset, elem_changed):
                                write_reference(datatype, item, elem_offset, elem_changed)
                    elif issubclass(datatype, Structure):
                        def write(datatype, item, elem_offset, elem_changed):
                            write_struct(datatype, item, elem_offset, elem_changed)
                    else:
                        def write(datatype, item, elem_offset, elem_changed):
                            if elem_changed:
                                write_value(datatype, item, elem_offset)
                    
                    if in_data:
                        orig_offsets = data._offsets
                    else:
                        orig_offsets = [None] * len(data)
                    
                    for elem_offset, orig_offset, item in zip(elem_offsets, orig_offsets, data._list):
                        elem_changed = True
                        if orig_offset is None and issubclass(datatype, Structure):
                            if isinstance(item, partial):
                                #print 'unwrapping'
                                item = item()
                            orig_offset = self._objid2off.get(id(item))
                        if orig_offset is not None:
                            if orig_offset != elem_offset:
                                data_section[elem_offset:elem_offset+elem_size] = array('c', self._data[orig_offset:orig_offset+elem_size])
                            elem_changed = False
                        #print orig_offset, elem_changed
                        if isinstance(item, partial):
                            if orig_offset is not None:
                                continue
                            else:
                                #print 'unwrapping'
                                item = item()
                        write(datatype, item, elem_offset, elem_changed)
                
                else:
                    if changed:
                        #print 'list copy and save'
                        data_section.extend(self._data[address:address+size])
                    
                    if data.indirect:
                        if datatype is None:
                            def write(datatype, item, elem_offset):
                                write_generic(item, elem_offset, False)
                        else:
                            def write(datatype, item, elem_offset):
                                write_reference(datatype, item, elem_offset, False)
                    elif issubclass(datatype, Structure):
                        def write(datatype, item, elem_offset):
                            write_struct(datatype, item, elem_offset, False)
                    else:
                        write = None
                    
                    if write is not None:
                        for orig_offset, item in zip(data._offsets, data._list):
                            if not isinstance(item, partial):
                                write(datatype, item, orig_offset)
                
                if changed:
                    UINT32.format[bigendian].pack_into(data_section, offset, address)

        def write_value(datatype, data, offset):
            #print 'write value %08X'%f.tell()
            if datatype is ECString:
                if data is None:
                    datatype.format[bigendian].pack_into(data_section, offset, 0xFFFFFFFF)
                else:
                    datatype.format[bigendian].pack_into(data_section, offset, cache_string(data, datatype))
            elif datatype is TlkString:
                label, string = data
                if string is None:
                    datatype.format[bigendian].pack_into(data_section, offset, label, 0xFFFFFFFF)
                elif string == 0:
                    datatype.format[bigendian].pack_into(data_section, offset, label, 0)
                else:
                    datatype.format[bigendian].pack_into(data_section, offset, label, cache_string(string, datatype))
            else:
                if isinstance(data, tuple):
                    datatype.format[bigendian].pack_into(data_section, offset, *data)
                else:
                    datatype.format[bigendian].pack_into(data_section, offset, data)

        def write_generic(data, offset, changed):
            #print 'write generic %08X'%f.tell()
            if changed:
                if data is None:
                    Generic.format[bigendian].pack_into(data_section, offset, 0xFFFFFFFF, 0xFFFFFFFF)
                elif isinstance(data, Structure):
                    typeid = type2struct[data.fourcc]
                    datatype = type(data)
                    address = self._objid2off.get(id(data))
                    if address is None or self._off2obj[address] is not data:
                        address = allocate(datatype.size)
                        write_struct(datatype, data, address, True)
                    else:
                        write_struct(datatype, data, address, False)
                    Generic.format[bigendian].pack_into(data_section, offset, 0x40000000 | typeid, address)
                elif type(data) in DATATYPES:
                    datatype = type(data)
                    if datatype is not ECString:
                        address = allocate(datatype.size)
                        write_value(datatype, data, address)
                    else: 
                        address = cache_string(data, datatype)
                    Generic.format[bigendian].pack_into(data_section, offset, datatype.id, address)
                elif type(data) is Generic:
                    if changed:
                        flags = pack_flags(data.is_list, data.is_struct, data.is_reference)
                        Generic.format[bigendian].pack_into(data_section, offset, flags << 16 | data.type, 0xFFFFFFFF)
                else:
                    raise Exception('cannot infer type', data)
            elif isinstance(data, Structure):
                write_struct(type(data), data, self._objid2off[id(data)], False)

        def write_reference(datatype, data, offset, changed):
            if changed:
                if data is None:
                    Reference.format[bigendian].pack_into(data_section, offset, 0xFFFFFFFF)
                else:
                    if issubclass(datatype, Structure):
                        address = self._objid2off.get(id(data))
                        if address is None or self._off2obj[address] is not data:
                            address = allocate(datatype.size)
                            write_struct(datatype, data, address, True)
                        else:
                            write_struct(datatype, data, address, False)
                    elif datatype is ECString:
                        address = cache_string(data, datatype)
                    else:
                        address = allocate(datatype.size)
                        write_value(datatype, data, address)
                    Reference.format[bigendian].pack_into(data_section, offset, address)
            elif isinstance(data, Structure):
                write_struct(datatype, data, self._objid2off[id(data)], False)
        
        if self.use_cstring:
            def cache_string(data, datatype):
                data = unicode(data).replace(u'\0', '')
                offset = string_cache.get(data)
                if offset is None:
                    string_cache[data] = offset = len(string_list)
                    string_list.append(data)
                return offset
        elif False:
            def cache_string(data, datatype):
                data = unicode(data)
                offset = string_cache.get(data)
                if offset is None:
                    offset = align_end()
                    data_section.extend(UINT32.format[bigendian].pack(len(data)))
                    data_section.extend(data.encode('utf_16le'))
                    string_cache[data] = offset
                return offset
        else:
            def cache_string(data, datatype):
                data = unicode(data)
                offset = align_end()
                data_section.extend(UINT32.format[bigendian].pack(len(data)))
                data_section.extend(data.encode('utf_16le'))
                return offset
        
        #import time
        #start = time.time()
        write_struct(type(self.root), self.root, 0, False)
        #print 'finished building data'
        #data_finish = time.time()
        
        if self.use_cstring:
            string_section = array('c')
            for s in string_list:
                string_section.extend(s.encode('utf-8'))
                string_section.append('\0')
        else:
            string_section = ''
        #string_finish = time.time()
        
        header_section = array('c', self._headerdata)
        string_offset = len(header_section)
        data_offset = string_offset + len(string_section)
        if data_offset % 16:
            data_offset += 16 - data_offset % 16
        
        if version == 'V4.0':
            Header40Format[bigendian].pack_into(header_section, 12, header.file_type, header.file_version, len(header.structs), data_offset)
        elif version == 'V4.1':
            Header41Format[bigendian].pack_into(header_section, 12, header.file_type, header.file_version, len(header.structs), len(string_list), string_offset, data_offset)
        #header_finish = time.time()
        
        f.write(header_section.tostring())
        if self.use_cstring:
            f.seek(string_offset)
            f.write(string_section.tostring())
        f.write('\xff' * (data_offset - f.tell()))
        #f.seek(data_offset)
        f.write(data_section.tostring())
        #write_finish = time.time()
        #print data_finish - start, string_finish - data_finish, header_finish - string_finish, write_finish - header_finish

if __name__ == '__main__':
    import sys, gff4
    from gff4 import write_gff4, read_gff4
    from cStringIO import StringIO
    from time import clock
    
    filename = sys.argv[1]
    
    gff4._DEBUG_COMPARISONS = True
    
    t = clock()
    with open(filename, 'rb') as f:
        mem = StringIO(f.read())
    print 'file read in %.2f seconds'%(clock()-t)
    
    t = clock()
    gff = LazyGFF4(mem)
    data, header = gff.root, gff.header
    print 'data loaded in %.2f seconds'%(clock()-t)
    
    #from gff4.toyaml import gff2yamlevents
    #import yaml
    #yaml.emit(gff2yamlevents(data, header, True), sys.stdout)
    
    t = clock()
    hold = StringIO()
    write_gff4(hold, data, header)
    print 'data dumped in %.2f seconds'%(clock()-t)
        
    t = clock()
    hold.seek(0)
    data2, header2 = read_gff4(hold)
    print 'data reloaded in %.2f seconds'%(clock()-t)
    
    t = clock()
    if data != data2:
        print 'data dumped is not the same as that that was loaded'
    print 'data compared in %.2f seconds'%(clock()-t)