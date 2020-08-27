# NOTES:
#  ECStrings are references, thus a reference to a ECString is the same as an ECString
# TODO:
#       make header a property of structs, specifically the root struct (structs[0].fourcc == root.fourcc).
#         also _header for the actual attribute
#       remove header argument to write_gff and read_gff, and header tuple for read_gff
#       tofile and fromfile methods on struct, overridden in lazy
#         fromfile could also be a module level method
#       actual abstract classes

import re, os
from struct import Struct
from collections import namedtuple, deque, MutableMapping, MutableSequence, Sequence
from numbers import Integral, Real
from itertools import count, izip
from math import isnan
from warnings import warn
from array import array

_DEBUG_COMPARISONS = False

import string
_STRUCTNAME_CHARS = set(string.ascii_letters).union(string.digits)
del string

BiStruct = namedtuple('BiStruct', 'l b size')
def _bistruct(format):
    if format[0] in ('<', '>', '=', '!'):
        raise ValueError, 'format cannot dictate byte-order'
    le, be = Struct('<'+format), Struct('>'+format)
    return BiStruct(le, be, le.size)

Header40Format = _bistruct('4s4sII')
Header41Format = _bistruct('4s4sIIII')
StructureFormat = _bistruct('4sIII')
FieldFormat = _bistruct('III')

class Header(namedtuple('Header', 'version platform file_type file_version string_count string_offset data_offset structs')):
    def find(self, name):
        for struct in self.structs:
            if hasattr(struct, 'fourcc'):
                if struct.fourcc == name:
                    return struct
            else:
                if struct.type == name:
                    return struct
        return None
_headerstruct = namedtuple('HeaderStructure', 'type size fields')
_headerfield = namedtuple('HeaderField', 'label type is_list is_struct is_reference offset')

Field = namedtuple('Field', 'label type indirect offset')
GFF4Data = namedtuple('GFF4Data', 'header root')

def repeat(object, times=None):
    # repeat(10, 3) --> 10 10 10
    if times is None:
        while True:
            yield object
    else:
        for i in xrange(times):
            yield object

def _naneq(a, b):
    if a != b:
        if isinstance(a, tuple) and isinstance(b, tuple) and len(a) == len(b):
            for i, x, y in izip(count(), a, b):
                if not _naneq(x, y):
                    return False
        elif not isinstance(a, float) or not isinstance(b, float) or not isnan(a) or not isnan(b):
            return False
    return True

def _integral(type_id, typename, base, minval, maxval, format):
    @staticmethod
    def __new__(cls, *args, **kwargs):
        if minval <= base(*args, **kwargs) <= maxval:
            return base.__new__(cls, *args, **kwargs)
        else:
            raise ValueError, 'out of range %d..%d'%(minval, maxval)
    newtype = _subtype(type_id, typename, base, format)
    newtype.__new__ = __new__
    newtype.minval = minval
    newtype.maxval = maxval
    return newtype

def _real(type_id, typename, base, format):
    newtype = _subtype(type_id, typename, base, format)
    if hasattr(base, '__eq__'):
        oldeq = base.__eq__
        def neweq(self, other):
            if isinstance(other, float) and isnan(self) and isnan(other):
                return True
            return oldeq(self, other)
        newtype.__eq__ = neweq
    if hasattr(base, '__ne__'):
        oldne = base.__ne__
        def newne(self, other):
            if isinstance(other, float) and isnan(self) and isnan(other):
                return False
            return oldne(self, other)
        newtype.__ne__ = newne
    return newtype

def _subtype(type_id, typename, base, format):
    def __repr__(self):
        return '%s(%r)'%(typename, base(self))
    format = _bistruct(format)
    return type(typename, (base,), dict(id=type_id, format=format, size=format.size, name=typename, __repr__=__repr__, __slots__=()))

def _basictype(type_id, typename, field_names, format):
    cls = namedtuple(typename, field_names)
    cls.id = type_id
    cls.format = _bistruct(format)
    cls.size = cls.format.size
    cls.name = typename
    return cls

_use_float_types = True

UINT8       = _integral(  0, 'UINT8',       int,   0x00,               0xFF,                    'B')
INT8        = _integral(  1, 'INT8',        int,  -0x80,               0x7F,                    'b')
UINT16      = _integral(  2, 'UINT16',      int,   0x0000,             0xFFFF,                  'H')
INT16       = _integral(  3, 'INT16',       int,  -0x8000,             0x7FFF,                  'h')
UINT32      = _integral(  4, 'UINT32',      long,  0x00000000,         0xFFFFFFFF,              'I')
INT32       = _integral(  5, 'INT32',       int,  -0x80000000,         0x7FFFFFFF,              'i')
UINT64      = _integral(  6, 'UINT64',      long,  0x0000000000000000, 0xFFFFFFFFFFFFFFFF,      'Q')
INT64       = _integral(  7, 'INT64',       long, -0x8000000000000000, 0x7FFFFFFFFFFFFFFF,      'q')
ECString    = _subtype(  14, 'ECString',    unicode,                                            'I')
TlkString   = _basictype(17, 'TlkString',   'label s',                                          '2I')
if _use_float_types:
    FLOAT32     = _real(      8, 'FLOAT32',     float,                                              'f')
    FLOAT64     = _real(      9, 'FLOAT64',     float,                                              'd')
    Vector3f    = _basictype(10, 'Vector3f',    'a b c',                                            '3f')
    Vector4f    = _basictype(12, 'Vector4f',    'a b c d',                                          '4f')
    Quaternionf = _basictype(13, 'Quaternionf', 'a b c d',                                          '4f')
    Color4f     = _basictype(15, 'Color4f',     'r g b a',                                          '4f')
    Matrix4x4f  = _basictype(16, 'Matrix4x4f',  'aa ab ac ad ba bb bc bd ca cb cc cd da db dc dd',  '16f')
else:
    FLOAT32     = _subtype(   8,  'FLOAT32',    int,                                                'i')
    FLOAT64     = _subtype(   9,  'FLOAT64',    long,                                               'q')
    Vector3f    = _basictype(10, 'Vector3f',    'a b c',                                            '3i')
    Vector4f    = _basictype(12, 'Vector4f',    'a b c d',                                          '4i')
    Quaternionf = _basictype(13, 'Quaternionf', 'a b c d',                                          '4i')
    Color4f     = _basictype(15, 'Color4f',     'r g b a',                                          '4i')
    Matrix4x4f  = _basictype(16, 'Matrix4x4f',  'aa ab ac ad ba bb bc bd ca cb cc cd da db dc dd',  '16i')

Reference   = _subtype(  -1,     'Reference',   int,                                            'I')
Generic     = _basictype(0xFFFF, 'Generic',     'type is_list is_struct is_reference address',  'II')

class Binary(str):
    def __repr__(self):
        return 'Binary(%r)'%str(self)

class Structure(MutableMapping):
    def __init__(self, mapping=None, subsetonly=True):
        self._dict = dict()
        if mapping:
            for key in mapping:
                if subsetonly or key in self:
                    self[key] = mapping[key]
    
    def _coercevalue(self, key, value):
        field = self.getfieldbylabel(key)
        return coercevalue(value, field.type, field.indirect)
    
    def __len__(self):
        return len(self.fields)
    
    def __getitem__(self, key):
        try:
            return self._dict[key]
        except KeyError:
            newvalue = self._coercevalue(key, None)
            self._dict[key] = newvalue
            return newvalue
    
    def __setitem__(self, key, value):
        self._dict[key] = self._coercevalue(key, value)
    
    def __delitem__(self, key):
        raise TypeError, "Structure does not support item deletion"
    
    def __iter__(self):
        return iter(field.label for field in self.fields)
    
    def __contains__(self, key):
        return key in self._fieldlabels
    
    def getfieldbyindex(self, i):
        return self.fields[i]
    
    def __eq__(self, other):
        if not isinstance(other, Structure):
            if _DEBUG_COMPARISONS:
                print 'not a Structure'
            return False
        if self.fourcc != other.fourcc:
            if _DEBUG_COMPARISONS:
                print 'different fourcc'
            return False
        if self.fields != other.fields and not _DEBUG_COMPARISONS:
            return False
        for key in self:
            if not _naneq(self[key], other[key]):
                if _DEBUG_COMPARISONS:
                    print self.fourcc, key, repr(self[key]), repr(other[key])
                return False
        return True
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def accept(self, visitor):
        if visitor.visit_structure(self):
            return visitor.leave_structure()
        for field in self.fields:
            if visitor.visit_field(field):
                continue
            value = self[field.label]
            if isinstance(value, (Structure, List)):
                if value.accept(visitor):
                    break
            else:
                if visitor.visit_data(value):
                    break
        return visitor.leave_structure()

def _structtype(fourcc, fields, size, name=None):
    structtype = _structtype1(fourcc, size, name)
    _structtype2(structtype, fields)
    return structtype

def _structtype1(fourcc, size, name=None):
    if not isinstance(fourcc, str) or len(fourcc) is not 4:
        raise ValueError, ('bad four character struct type', fourcc)
    
    if name is None:
        name = 'Struct'+''.join(c if c in _STRUCTNAME_CHARS else '_%02x'%ord(c) for c in fourcc)
    
    return type(name, (Structure,), dict(fourcc=fourcc, size=size))

def _structtype2(structtype, fields):
    # need more field validation
    fieldsbylabel = dict((field.label, field) for field in fields)
    fieldlabels = frozenset(fieldsbylabel.iterkeys())
    def getfieldbylabel(self, label):
        return fieldsbylabel[label]
    
    structtype.fields = fields
    structtype.getfieldbylabel = getfieldbylabel
    structtype._fieldlabels = property(lambda self: fieldlabels)

class List(MutableSequence):
    elem_type=None
    indirect=True
    
    def __init__(self, iterable=None):
        self._list = list()
        if iterable:
            for value in iterable:
                self.append(value)
    
    def _coercevalue(self, value):
        return coercevalue(value, self.elem_type, self.indirect)
    
    def __len__(self):
        return len(self._list)
    
    def __getitem__(self, i):
        return self._list[i]
    
    def __setitem__(self, i, value):
        if isinstance(i, int):
            self._list[i] = self._coercevalue(value)
        elif isinstance(i, slice):
            self._list[i] = [self._coercevalue(v) for v in value]
        else:
            raise TypeError, 'list indices must be integers or slices'
    
    def __delitem__(self, i):
        del self._list[i]
    
    def insert(self, i, value):
        self._list.insert(i, self._coercevalue(value))
    
    def __contains__(self, value):
        return self._coercevalue(value) in self._list
    
    def __eq__(self, other):
        if not isinstance(other, List):
            if _DEBUG_COMPARISONS:
                print 'not a List'
            return False
        if self.indirect != other.indirect:
            if _DEBUG_COMPARISONS:
                print 'different indirectness'
            return False
        if self.elem_type != other.elem_type and not _DEBUG_COMPARISONS:
            return False
        if len(self) != len(other):
            if _DEBUG_COMPARISONS:
                print 'different lengths'
            return False
        for i, a, b in izip(count(), self, other):
            if not _naneq(a, b):
                if _DEBUG_COMPARISONS:
                    print i, repr(a), repr(b)
                return False
        return True
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def accept(self, visitor):
        if visitor.visit_list(self):
            return visitor.leave_list()
        for value in self:
            if isinstance(value, (Structure, List)):
                if value.accept(visitor):
                    break
            else:
                if visitor.visit_data(value):
                    break
        return visitor.leave_list()

def _listtype(elemtype, indirect=False):
    indirect = bool(indirect)
    if elemtype is None:
        if not indirect:
            raise ValueError, 'List must be indirect if it has no element type'
    elif elemtype not in DATATYPES and not issubclass(elemtype, Structure):
        raise ValueError, ('Only primitive types and structures can be composed into lists', elemtype, indirect)
    
    if indirect:
        if elemtype is None:
            name = 'ListGeneric'
        else:
            name = 'ListIndirect'+elemtype.__name__
    else:
        name = 'List'+elemtype.__name__
    
    return type(name, (List,), dict(
        elem_type=elemtype,
        indirect=indirect))
    
def coercevalue(value, kind, none_ok=False, strict_struct=False):
    if kind is None:
        if value is None:
            if none_ok:
                return None
            else:
                raise ValueError, 'uncoercable None'
        elif isinstance(value, GENERICTYPES):
            # small loophole here that allows a subclass to sneak in if the caller is naive
            # ie, a lazy struct could be returned when the caller does not like them (but doesn't express that in code)
            return value
        elif isinstance(value, Integral):
            return INT64(value)
        elif isinstance(value, Real):
            return FLOAT64(value)
        elif isinstance(value, basestring):
            return ECString(value)
        else:
            raise ValueError, ('uncoercable value', type(value), value)
    elif kind in DATATYPES:
        if value is None:
            if none_ok:
                return None
            elif issubclass(kind, TlkString):
                return kind(0, None)
            elif issubclass(kind, tuple):
                return kind(*(0,)*len(kind._fields))
            else:
                return kind()
        elif type(value) == kind:
            return value
        elif isinstance(value, Sequence) and not isinstance(value, basestring):
            return kind(*value)
        else:
            return kind(value)
    elif issubclass(kind, (Structure, List)):
        #print kind
        if value is None:
            return None if none_ok else kind()
        elif type(value) == kind:
            return value
        elif isinstance(value, str) and issubclass(kind, List) and kind.elem_type == UINT8 and not kind.indirect:
            # special exception for binary
            return Binary(value) if type(value) != Binary else value
        else:
            if issubclass(kind, Structure):
                if isinstance(value, Structure) and value.fourcc != kind.fourcc:
                    if strict_struct:
                        raise TypeError, 'will not coerce %s structure into a %s structure'%(value.fourcc, kind.fourcc)
                    else:
                        warn('coercing %s structure into a %s structure'%(value.fourcc, kind.fourcc))
            return kind(value)
    else:
        raise ValueError, ('unsupported type', kind)

_LITTLE_ENDIAN_PLATFORMS = ('PC  ',)
_BIG_ENDIAN_PLATFORMS = ('X360 ',)

def isbeplatform(s):
    return s not in _LITTLE_ENDIAN_PLATFORMS

DATATYPES = set([
    UINT8,
    INT8,
    UINT16,
    INT16,
    UINT32,
    INT32,
    UINT64,
    INT64,
    FLOAT32,
    FLOAT64,
    Vector3f,
    Vector4f,
    Quaternionf,
    ECString,
    Color4f,
    Matrix4x4f,
    TlkString
])

GENERICTYPES = (Structure,)+tuple(DATATYPES)

INTEGER_TYPES = set([
    UINT8,
    INT8,
    UINT16,
    INT16,
    UINT32,
    INT32,
    UINT64,
    INT64
])

REAL_TYPES = set([
    FLOAT32,
    FLOAT64
])

TYPES_BY_ID = dict((datatype.id, datatype) for datatype in DATATYPES)

def unpack_flags(flags, check=True):
    if check and flags & 0x1FFF:
        raise ValueError, 'unknown flag(s) in field: %04x'%(flags & 0x1FFF)
    return bool(flags & 0x8000), bool(flags & 0x4000), bool(flags & 0x2000)
    
def pack_flags(is_list=False, is_struct=False, is_reference=False):
    flags = 0
    if is_list: flags |= 0x8000
    if is_struct: flags |= 0x4000
    if is_reference: flags |= 0x2000
    return flags

def real_version(version, platform):
    if platform == 'X360' and version == 'V4.0':
        return 'V4.1'
    return version

def _print_headerstructs(headerstructs):
    for struct in headerstructs:
        print struct._replace(fields='->')
        for field in struct.fields:
            print ' ', field

def _unpack_header(f):
    f.seek(0)
    magic = f.read(4)
    if magic != 'GFF ':
        raise ValueError, ('Unknown filetype', magic)
    gff_version = f.read(4)
    if gff_version not in ('V4.0', 'V4.1'):
        raise ValueError, ('Unknown GFF version', gff_version)
    target_platform = f.read(4)
    bigendian = isbeplatform(target_platform)
    real_version_ = real_version(gff_version, target_platform)
    
    if real_version_ == 'V4.0':
        file_type, file_version, struct_count, data_offset = Header40Format[bigendian].unpack(f.read(16))
        string_count = 0
        string_offset = data_offset
    elif real_version_ == 'V4.1':
        file_type, file_version, struct_count, string_count, string_offset, data_offset = Header41Format[bigendian].unpack(f.read(24))
    
    _FieldFormat = FieldFormat[bigendian]
    _StructureFormat = StructureFormat[bigendian]
    
    #print file_type, file_version, struct_count, string_count, string_offset, data_offset
    
    def read_structs(n):
        def read_struct(struct_type, field_count, field_offset, struct_size):
            #print struct_type, field_count, field_offset, struct_size, f.tell()
            def read_field():
                label, type_id, index = _FieldFormat.unpack(f.read(12))
                type_flags, type_id = type_id >> 16, type_id & 0xffff
                is_list, is_struct, is_reference = unpack_flags(type_flags)
                return _headerfield(label, type_id, is_list, is_struct, is_reference, index)
            assert f.tell() == field_offset
            return _headerstruct(struct_type, struct_size, tuple(read_field() for i in xrange(field_count)))
        return tuple(read_struct(*struct) for struct in [_StructureFormat.unpack(f.read(16)) for i in xrange(n)])
    
    return Header(gff_version, target_platform, file_type, file_version, string_count, string_offset, data_offset, read_structs(struct_count))

def read_header(f, return_roots=False):
    header = _unpack_header(f)
    headerstructs = header.structs
    
    #_print_headerstructs(headerstructs)
    
    queue = set(xrange(len(headerstructs)))
    not_roots = set()
    structs = dict()
    lists = dict()
    def make_field(field):
        if field.is_struct:
            kind = make_structure(field.type)
        elif field.type == 0xFFFF:
            kind = None
        else:
            kind = TYPES_BY_ID[field.type]
        indirect = field.is_reference
        if field.is_list:
            if (kind, indirect) in lists:
                kind = lists[(kind, indirect)]
            else:
                elem_type = kind
                kind = _listtype(elem_type, indirect)
                lists[(elem_type, indirect)] = kind
            indirect = False
        elif kind is None and not indirect:
            raise ValueError, 'Cannot have a generic field that is not a reference'
        return Field(field.label, kind, indirect, field.offset)
    def make_structure(i, root=False):
        if not root:
            not_roots.add(i)
        if i not in structs:
            structdef = headerstructs[i]
            struct = _structtype1(structdef.type, structdef.size)
            structs[i] = struct
            queue.remove(i)
            
            fields = tuple(make_field(field) for field in structdef.fields)
            _structtype2(struct, fields)
            
            return struct
        else:
            return structs[i]
    while queue:
        make_structure(min(queue), True)
    
    header = header._replace(structs=tuple(structs[i] for i in xrange(len(headerstructs))))
    if return_roots:
        roots = set(xrange(len(header.structs))).difference(not_roots)
        return header, roots
    else:
        return header

def read_gff4(f, header=None):
    return_header = False
    if header is None:
        f.seek(0)
        header = read_header(f)
        return_header = True
    data_offset = header.data_offset
    bigendian = isbeplatform(header.platform)
    version = real_version(header.version, header.platform)
    use_cstring = ('V4.1' <= version)
    if use_cstring:
        f.seek(header.string_offset)
        stringcache = f.read(header.data_offset - header.string_offset)
        stringcache = stringcache.split('\0')[:header.string_count]
        stringcache = [s.decode('utf-8') for s in stringcache]
    else:
        stringcache = dict()
    #counts = dict()

    def read_struct(structtype):
        offset = f.tell()
        res = structtype()
        for field in structtype.fields:
            if offset + field.offset != f.tell():
                f.seek(offset + field.offset)
            res._dict[field.label] = read_field(field)
        return res

    def read_field(field):
        fieldtype = field.type
        if field.indirect:
            return read_reference(fieldtype)
        elif issubclass(fieldtype, List):
            return read_list(fieldtype)
        elif issubclass(fieldtype, Structure):
            return read_struct(fieldtype)
        else:
            return read_value(fieldtype)
    
    def read_list(listtype):
        elemtype = listtype.elem_type
        res = listtype()
        
        address, = UINT32.format[bigendian].unpack(f.read(4))
        if address == 0xFFFFFFFF:
            return res
        f.seek(data_offset + address)
        
        length, = UINT32.format[bigendian].unpack(f.read(4))
        offset = f.tell()
        
        if listtype.indirect:
            if elemtype is None:
                # GENERIC LIST - no lists, generics are reduced, odd behavior in toolset on ref - can't change value, hidden on open, unless it's a struct and it gets reduced
                g_refs = []
                for i in xrange(length):
                    g_ref = read_generic()
                    if g_ref.is_list or g_ref.is_reference: # leaving references as an error, since they don't work well in the toolset
                        raise Exception('generic list with list or reference element %s'%(g_ref,))
                    g_refs.append(g_ref)
                for g_ref in g_refs:
                    if g_ref.address == 0xFFFFFFFF:
                        warn('null generic list value %r'%(g_ref,))
                        res._list.append(None)
                    else:
                        f.seek(data_offset + g_ref.address)
                        if g_ref.is_struct:
                            res._list.append(read_struct(header.structs[g_ref.type]))
                        elif g_ref.type == ECString.id:
                            res._list.append(ECString(parse_string()))
                        else:
                            res._list.append(read_value(TYPES_BY_ID[g_ref.type]))
            else:
                refs = []
                for i in xrange(length):
                    address, = UINT32.format[bigendian].unpack(f.read(4))
                    refs.append(address)
                for address in refs:
                    if address == 0xFFFFFFFF:
                        res._list.append(None)
                    else:
                        f.seek(data_offset + address)
                        if issubclass(elemtype, Structure):
                            res._list.append(read_struct(elemtype))
                        elif issubclass(elemtype, ECString):
                            res._list.append(ECString(parse_string()))
                        else:
                            res._list.append(read_value(elemtype))
        elif issubclass(elemtype, Structure):
            for i in xrange(length):
                if offset != f.tell():
                    f.seek(offset)
                res._list.append(read_struct(elemtype))
                offset += elemtype.size
        elif issubclass(elemtype, UINT8):
            return Binary(f.read(length))
        else:
            for i in xrange(length):
                if offset != f.tell():
                    f.seek(offset)
                res._list.append(read_value(elemtype))
                offset += elemtype.format.size
        return res
    
    def read_reference(reftype):
        if reftype is None:
            g_ref = read_generic()
            if g_ref.address == 0xFFFFFFFF:
                #warn('null generic value %r'%g_ref)
                return None
            elif g_ref.is_list or g_ref.is_reference:
                raise Exception('generic list or reference element %s'%(g_ref,))
            f.seek(data_offset + g_ref.address)
            if g_ref.is_struct:
                return read_struct(header.structs[g_ref.type])
            elif g_ref.type == ECString.id:
                return ECString(parse_string())
            else:
                return read_value(TYPES_BY_ID[g_ref.type])
        else:
            address, = UINT32.format[bigendian].unpack(f.read(4))
            if address == 0xFFFFFFFF:
                return None
            #ref = Reference(field, address)
            f.seek(data_offset + address)
            if issubclass(reftype, Structure):
                return read_struct(reftype)
            elif issubclass(reftype, ECString):
                return ECString(parse_string())
            else:
                return read_value(reftype)

    def read_value(datatype):
        #counts[datatype] = counts.get(datatype, 0) + 1
        
        if datatype is ECString:
            address, = datatype.format[bigendian].unpack(f.read(4))
            if address == 0xFFFFFFFF:
                return None
            elif use_cstring:
                return ECString(stringcache[address])
            f.seek(data_offset + address)
            return ECString(parse_string())
        elif datatype is TlkString:
            label, address = datatype.format[bigendian].unpack(f.read(8))
            if address == 0xFFFFFFFF:
                return TlkString(label, None)
            elif use_cstring:
                return TlkString(label, stringcache[address])
            elif address == 0:
                return TlkString(label, 0)
            else:
                f.seek(data_offset + address)
                return TlkString(label, parse_string())
        else:
            return datatype(*datatype.format[bigendian].unpack(f.read(datatype.size)))
    
    def parse_string():
        length, = UINT32.format[bigendian].unpack(f.read(4))
        s = f.read(length * 2)
        try:
            return s.decode('utf_16le')
        except:
            import sys
            print >>sys.stderr, 'Bad data', repr(s)
            raise

    def read_generic():
        type_id, address = Generic.format[bigendian].unpack(f.read(8))
        type_flags, type_id = type_id >> 16, type_id & 0xffff
        is_list, is_struct, is_reference = unpack_flags(type_flags, address != 0xFFFFFFFF)
        return Generic(type_id, is_list, is_struct, is_reference, address)
    
    try:
        f.seek(data_offset)
        struct = read_struct(header.structs[0])
        struct.header = header
        #print counts
        if return_header:
            return struct, header
        else:
            return struct
    except:
        import sys
        print >>sys.stderr, 'Failed before', f.tell()
        raise

_use_string_cache = False

def write_gff4(f, data, header=None, def_align=8):
    if not isinstance(data, Structure):
        raise ValueError, ('data is not a Structure', type(data))
    #print header
    if header is None:
        header = build_header(data)
    elif not isinstance(header, Header):
        raise ValueError, ('header is not a Header', type(header))
    if header.version not in ('V4.0', 'V4.1'):
        raise ValueError, ('Unsupported GFF version', header.version)
    
    version = real_version(header.version, header.platform)
    use_cstring = 'V4.1' <= version
    bigendian = isbeplatform(header.platform)
    def_align = 4
    if def_align < 1:
        def_align = 1
    header_section = array('c')
    string_section = array('c')
    data_section = array('c')
    string_cache = dict()
    
    if use_cstring:
        string_cache[u''] = 0
        string_section.extend('\0')
        
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
    
    type2struct = dict()
    for i, struct in enumerate(header.structs):
        if struct.fourcc in type2struct:
            raise ValueError, 'Does not support different struct definitions with the same label'
        else:
            type2struct[struct.fourcc] = i
    
    def enqueue(code, data, datatype, size):
        current_offset = self_offset[0]
        queue.append((code, data, datatype, current_offset))
        if size % align > 0:
            size += align - size % align
        self_offset[0] += size
        return current_offset

    def write_struct(structure, data, offset):
        #print 'write struct %08X'%f.tell()
        for field in structure.fields:
            write_field(field, data[field.label], offset + field.offset)

    def write_field(field, data, offset):
        #print 'write field %08X'%f.tell()
        if issubclass(field.type, List):
            if not data:
                UINT32.format[bigendian].pack_into(data_section, offset, 0xFFFFFFFF)
            else:
                address = align_end()
                UINT32.format[bigendian].pack_into(data_section, offset, address)
                data_section.extend(UINT32.format[bigendian].pack(len(data)))
                datatype = field.type.elem_type
                if field.type.indirect:
                    if datatype is None:
                        elem_offset = allocate(len(data) * Generic.size, 1)
                        for item in data:
                            write_generic(item, elem_offset)
                            elem_offset += Generic.size
                    else:
                        elem_offset = allocate(len(data) * Reference.size, 1)
                        for item in data:
                            write_reference(datatype, item, elem_offset)
                            elem_offset += Reference.size
                elif issubclass(datatype, Structure):
                    elem_offset = allocate(len(data) * datatype.size, 1)
                    for structure in data:
                        write_struct(datatype, structure, elem_offset)
                        elem_offset += datatype.size
                elif isinstance(data, str):
                    data_section.extend(data)
                else:
                    elem_offset = allocate(len(data) * datatype.size, 1)
                    for value in data:
                        write_value(datatype, value, elem_offset)
                        elem_offset += datatype.size
        elif field.indirect:
            if field.type is None:
                write_generic(data, offset)
            else:
                write_reference(field.type, data, offset)
        elif issubclass(field.type, Structure):
            write_struct(field.type, data, offset)
        else:
            write_value(field.type, data, offset)

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

    def write_generic(data, offset):
        #print 'write generic %08X'%f.tell()
        if data is None:
            Generic.format[bigendian].pack_into(data_section, offset, 0xFFFFFFFF, 0xFFFFFFFF)
        elif isinstance(data, Structure):
            id = type2struct[data.fourcc]
            datatype = type(data)
            address = allocate(datatype.size)
            write_struct(datatype, data, address)
            Generic.format[bigendian].pack_into(data_section, offset, 0x40000000 | id, address)
        elif type(data) in DATATYPES:
            # TODO: Special case for zero-length string?
            datatype = type(data)
            if datatype is not ECString:
                address = allocate(datatype.size)
                write_value(datatype, data, address)
            else: 
                address = cache_string(data, datatype)
            Generic.format[bigendian].pack_into(data_section, offset, datatype.id, address)
        elif type(data) is Generic:
            flags = pack_flags(data.is_list, data.is_struct, data.is_reference)
            Generic.format[bigendian].pack_into(data_section, offset, flags << 16 | data.type, 0xFFFFFFFF)
        else:
            raise Exception('cannot infer type', data)

    def write_reference(datatype, data, offset):
        if data is None:
            Reference.format[bigendian].pack_into(data_section, offset, 0xFFFFFFFF)
        else:
            if issubclass(datatype, Structure):
                address = allocate(datatype.size)
                write_struct(datatype, data, address)
            elif datatype is ECString:
                address = cache_string(data, datatype)
            else:
                address = allocate(datatype.size)
                write_value(datatype, data, address)
            Reference.format[bigendian].pack_into(data_section, offset, address)
    
    if use_cstring:
        def cache_string(data, datatype):
            data = unicode(data)
            offset = string_cache.get(data)
            if offset is None:
                string_cache[data] = offset = len(string_cache)
                string_section.extend(data.encode('utf-8'))
                string_section.append('\0')
            return offset
    elif _use_string_cache:
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
    
    allocate(type(data).size)
    write_struct(type(data), data, 0)
    
    _StructureFormat = StructureFormat[bigendian]
    _FieldFormat = FieldFormat[bigendian]
    
    if version == 'V4.0':
        struct_offset = 12 + Header40Format.size
        field_offset = struct_offset + len(header.structs) * _StructureFormat.size
        data_offset = field_offset + sum(len(structure.fields) for structure in header.structs) * _FieldFormat.size
        
        if data_offset % 16:
            data_offset += 16 - data_offset % 16
        
        header_section.extend('GFF ')
        header_section.extend(header.version)
        header_section.extend(header.platform)
        header_section.extend(Header40Format[bigendian].pack(header.file_type, header.file_version, len(header.structs), data_offset))
    elif version == 'V4.1':
        struct_offset = 12 + Header41Format.size
        field_offset = struct_offset + len(header.structs) * _StructureFormat.size
        string_offset = field_offset + sum(len(structure.fields) for structure in header.structs) * _FieldFormat.size
        data_offset = string_offset + len(string_section)
        
        if data_offset % 16:
            data_offset += 16 - data_offset % 16
        
        header_section.extend('GFF ')
        header_section.extend(header.version)
        header_section.extend(header.platform)
        header_section.extend(Header41Format[bigendian].pack(header.file_type, header.file_version, len(header.structs), len(string_cache), string_offset, data_offset))
    
    for structure in header.structs:
        header_section.extend(_StructureFormat.pack(structure.fourcc, len(structure.fields), field_offset, structure.size))
        field_offset += len(structure.fields) * _FieldFormat.size
    
    for structure in header.structs:
        for field in structure.fields:
            fieldtype = field.type
            is_list = False
            is_struct = False
            is_reference = field.indirect
            if issubclass(fieldtype, List):
                is_list = True
                is_reference = fieldtype.indirect
                fieldtype = fieldtype.elem_type
            if fieldtype is None:
                type_i = 0xFFFF
            elif issubclass(fieldtype, Structure):
                is_struct = True
                #print fieldtype, header.structs
                type_i = header.structs.index(fieldtype)
                #type_i = type2struct[fieldtype.fourcc]
            else:
                type_i = fieldtype.id
            flags = pack_flags(is_list, is_struct, is_reference)
            header_section.extend(_FieldFormat.pack(field.label, flags << 16 | type_i, field.offset))

    try:
        f.write(header_section)
    except TypeError:
        try:
            header_section.tofile(f)
        except TypeError:
            f.write(header_section.tostring())
            if use_cstring:
                f.seek(string_offset)
                f.write(string_section.tostring())
            f.write('\xff' * (data_offset - f.tell()))
            #f.seek(data_offset)
            f.write(data_section.tostring())
        else:
            if use_cstring:
                f.seek(string_offset)
                string_section.tofile(f)
            f.write('\xff' * (data_offset - f.tell()))
            # f.seek(data_offset)
            data_section.tofile(f)
    else:
        if use_cstring:
            f.seek(string_offset)
            f.write(string_section)
        f.write('\xff' * (data_offset - f.tell()))
        # f.seek(data_offset)
        f.write(data_section)

def build_header(root_struct, platform='PC  ', file_type='\0\0\0\0', file_version='\0\0\0\0', gff_version='V4.0'):
    if not all(isinstance(s, str) for s in (gff_version, platform, file_type, file_version)):
        raise TypeError
    if not all(len(s) == 4 for s in (gff_version, platform, file_type, file_version)):
        raise ValueError
    if not gff_version in ('V4.0', 'V4.1'):
        raise ValueError
    if not isinstance(root_struct, Structure):
        raise TypeError
    structs = []
    fourcc2i = {}
    def collect_struct(structtype):
        if structtype not in structs:
            if structtype.fourcc not in fourcc2i:
                fourcc2i[structtype.fourcc] = len(structs)
            else:
                warn('duplicate fourcc encountered while building header')
            structs.append(structtype)
            return True
        return False
    def collectbyval(struct):
        structtype = type(struct)
        collect_struct(structtype)
        #print struct
        for field in structtype.fields:
            fieldtype = field.type
            if fieldtype is not None and not issubclass(fieldtype, (Structure, List)):
                continue
            value = struct[field.label]
            if value is None:
                if issubclass(fieldtype, List):
                    fieldtype = fieldtype.elem_type
                if issubclass(fieldtype, Structure):
                    collectbytype(fieldtype)
            elif isinstance(value, Structure):
                collectbyval(value)
            elif isinstance(value, List):
                listtype = value.elem_type
                if listtype is None:
                    for item in value:
                        if isinstance(item, Structure):
                            collectbyval(item)
                elif issubclass(listtype, Structure):
                    if not len(value):
                        #print struct, value
                        collectbytype(listtype)
                    else:
                        for item in value:
                            collectbyval(item)
    def collectbytype(structtype):
        if collect_struct(structtype):
            #print structtype
            for field in structtype.fields:
                fieldtype = field.type
                if issubclass(fieldtype, List):
                    listtype = fieldtype.elem_type
                    if issubclass(listtype, Structure):
                        collectbytype(listtype)
                elif issubclass(fieldtype, Structure):
                    collectbytype(fieldtype)
    collectbyval(root_struct)
    #print map(lambda x: x.fourcc, structs)
    return Header(gff_version, platform, file_type, file_version, 0, 0, 0, tuple(structs))

if __name__ == '__main__':
    import sys
    if sys.argv[1] == 'read':
        from io import BufferedRandom
        from numbers import Number
        from inspect import isfunction, isgenerator
        def print_recursive(generator, level=0, indent=' '):
            for item in generator:
                print_item(item, level, indent)
        def print_item(item, level=0, indent=' '):
            if isfunction(item):
                lazy = item()
                print_item(lazy, level+1)
            elif isgenerator(item):
                print_recursive(item, level+1)
            elif isinstance(item, tuple):
                if isfunction(item[-1]) or isgenerator(item[-1]) or isinstance(item[-1], tuple):
                    print indent*level+repr(item[:-1])
                    print_item(item[-1], level+1)
                else:
                    print indent*level+repr(item)
            else:
                print indent*level+repr(item)
            
        with open(sys.argv[2], 'rb') as f:
            header = read_header(f)
            #print header.data_offset
            #print header._replace(structs=())
            #for struct in header.structs:
            #    print ' ', struct._replace(fields=())
            #    for field in struct.fields:
            #        print '   ', field
            #print
            data = read_gff4(f, header)
            #print_recursive(data)
    
    elif sys.argv[1] == 'header':            
        with open(sys.argv[2], 'rb') as f:
            header = _unpack_header(f)
            print header._replace(structs='->')
            _print_headerstructs(header.structs)
    
    elif sys.argv[1] == 'readtest':
        from cStringIO import StringIO
        from ioutils import copyio
        import cProfile
        buffer = StringIO()
        with open(sys.argv[2], 'rb') as f:
            copyio(buffer, f)
        buffer.seek(0)
        def readtest():
            read_gff4(buffer)
        cProfile.run('readtest()', sys.argv[3] if len(sys.argv) > 3 else None)
    
    elif sys.argv[1] == 'writetest':
        from cStringIO import StringIO
        from ioutils import copyio
        import cProfile
        buffer = StringIO()
        with open(sys.argv[2], 'rb') as f:
            copyio(buffer, f)
        buffer.seek(0)
        data, header = read_gff4(buffer)
        buffer = StringIO()
        def writetest():
            write_gff4(buffer, data, header)
        cProfile.run('writetest()', sys.argv[3] if len(sys.argv) > 3 else None)
    
    elif sys.argv[1] == 'write':
        from cStringIO import StringIO
        from time import clock
        
        filename = sys.argv[3]
        
        gff4._DEBUG_COMPARISONS = True
        
        t = clock()
        with open(filename, 'rb') as f:
            mem = StringIO(f.read())
        print 'file read in %.2f seconds'%(clock()-t)
        
        t = clock()
        data, header = read_gff4(mem)
        print 'data loaded in %.2f seconds'%(clock()-t)
        
        if sys.argv[2] == 'full':
            t = clock()
            hold = StringIO()
            write_gff4(hold, data, header)
            print 'data dumped in %.2f seconds'%(clock()-t)
            
            t = clock()
            with open(filename+'.temp', 'wb') as f:
                f.write(hold.getvalue())
            print 'file written in %.2f seconds'%(clock()-t)
        elif sys.argv[2] == 'retry':
            t = clock()
            with open(filename+'.temp', 'rb') as f:
                hold = StringIO(f.read())
            print 'file reread in %.2f seconds'%(clock()-t)
        
        t = clock()
        hold.seek(0)
        data2, header2 = read_gff4(hold)
        print 'data reloaded in %.2f seconds'%(clock()-t)
        
        t = clock()
        if data != data2:
            print 'data dumped is not the same as that that was loaded'
        print 'data compared in %.2f seconds'%(clock()-t)