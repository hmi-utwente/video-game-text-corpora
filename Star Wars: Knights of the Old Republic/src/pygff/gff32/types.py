from struct import Struct
from collections import namedtuple, MutableMapping, MutableSequence, Mapping, Sequence
from numbers import Integral, Real
from math import isnan
from operator import itemgetter

__all__ = [
    'BYTE', 'CHAR', 'WORD', 'SHORT', 'DWORD', 'INT',
    'DWORD64', 'INT64', 'FLOAT', 'DOUBLE', 'ExoString',
    'ResRef', 'ExoLocString', 'VOID', 'Structure', 'List',
    'ALL_TYPES', 'DATA_TYPES',
    'ALL_TYPES_BY_ID', 'DATA_TYPES_BY_ID',
]

_buffer = buffer

class Format(Struct):
    __slots__ = ()
    
    def read_from(self, f):
        return self.unpack(f.read(self.size))
    
    def write_to(self, f, *args):
        f.write(self.pack(*args))

class BiStruct(namedtuple('_BiStruct', 'l b size')):
    __slots__ = ()
    
    def __new__(cls, format):
        if format[0] in ('<', '>', '=', '!'):
            raise ValueError, 'format cannot dictate byte-order'
        le, be = Format('<'+format), Format('>'+format)
        #return super(BiStruct, cls).__new__(cls, le, be, le.size)
        return tuple.__new__(cls, (le, be, le.size))

class naneqfloat(float):
    __slots__ = ()
    
    def __eq__(self, other):
        if isnan(self) and isinstance(other, float) and isnan(other):
            return True
        return super(naneqfloat, self).__eq__(other)
    
    def __ne__(self, other):
        if isnan(self) and isinstance(other, float) and isnan(other):
            return False
        return super(naneqfloat, self).__ne__(other)
    
    @classmethod
    def iscompatible(cls, value):
        return True

class limitedint(int):
    def __new__(cls, *args, **kwargs):
        if cls.minval <= int(*args, **kwargs) <= cls.maxval:
            return super(limitedint, cls).__new__(cls, *args, **kwargs)
        else:
            raise ValueError, 'out of range %d..%d'%(cls.minval, cls.maxval)
    
    @classmethod
    def iscompatible(cls, value):
        return cls.minval <= value <= cls.maxval

class limitedlong(long):
    def __new__(cls, *args, **kwargs):
        if cls.minval <= long(*args, **kwargs) <= cls.maxval:
            return super(limitedlong, cls).__new__(cls, *args, **kwargs)
        else:
            raise ValueError, 'out of range %d..%d'%(cls.minval, cls.maxval)
    
    @classmethod
    def iscompatible(cls, value):
        return cls.minval <= value <= cls.maxval

class FormatValue(object):
    __slots__ = ()
    
    def pack(self, be=False):
        return self._format[be].pack(self)
    
    @classmethod
    def unpack(cls, string, be=False):
        return cls(*cls._format[be].unpack(string))
    
    def pack_into(self, buffer, offset, be=False):
        self._format[be].pack_into(buffer, offset, self)
    
    @classmethod
    def unpack_from(cls, buffer, offset=0, be=False):
        return cls(*cls._format[be].unpack_from(buffer, offset))
    
    def write_to(self, f, be=False):
        self._format[be].write_to(f, self)
    
    @classmethod
    def read_from(cls, f, be=False):
        return cls._format[be].read_from(f)
    
    @classmethod
    def calcsize(cls):
        return cls._format.size

class PrefixValue(object):
    __slots__ = ()
    
    def pack(self, be=False):
        return self._format[be].pack(len(self))+str(self)
    
    @classmethod
    def unpack(cls, string, be=False):
        val, = cls.unpack_from(string, 0, be)
        if val.calcsize() != len(string):
            raise RuntimeError, 'too much data'  # struct.error: unpack requires a string argument of length 4
        return val
    
    def pack_into(self, buffer, offset, be=False):
        self._format[be].pack_into(buffer, offset, len(self))
        offset += self._format.size
        for n in xrange(len(self)): buffer[offset+n] = self[n]
    
    @classmethod
    def unpack_from(cls, buffer, offset=0, be=False):
        length, = cls._format[be].unpack_from(buffer, offset)
        offset += cls._format.size
        s = buffer[offset:offset+length]
        if len(s) != length:
            raise RuntimeError, 'insufficient data'
        return cls(_buffer(s))
    
    def write_to(self, f, be=False):
        self._format[be].write_to(f, len(self))
        f.write(str(self))
    
    @classmethod
    def read_from(cls, f, be=False):
        length, = cls._format[be].read_from(f)
        s = f.read(length)
        if len(s) != length:
            raise RuntimeError, 'insufficient data'
        return cls(s)
    
    def calcsize(cls):
        return self._format.size+len(self)
    
    @classmethod
    def iscompatible(cls, value):
        return len(value) <= cls.maxlen

class BYTE(limitedint, FormatValue):
    __slots__ = ()
    typeid = 0
    complex = False
    _format = BiStruct('B')
    minval = 0x00
    maxval = 0xFF

class CHAR(limitedint, FormatValue):
    __slots__ = ()
    typeid = 1
    complex = False
    _format = BiStruct('b')
    minval = -0x80
    maxval = 0x7F

class WORD(limitedint, FormatValue):
    __slots__ = ()
    typeid = 2
    complex = False
    _format = BiStruct('H')
    minval = 0x0000
    maxval = 0xFFFF

class SHORT(limitedint, FormatValue):
    __slots__ = ()
    typeid = 3
    complex = False
    _format = BiStruct('h')
    minval = -0x8000
    maxval = 0x7FFF

class DWORD(limitedlong, FormatValue):
    __slots__ = ()
    typeid = 4
    complex = False
    _format = BiStruct('I')
    minval = 0x00000000
    maxval = 0xFFFFFFFF

class INT(limitedint, FormatValue):
    __slots__ = ()
    typeid = 5
    complex = False
    _format = BiStruct('i')
    minval = -0x80000000
    maxval = 0x7FFFFFFF

class DWORD64(limitedlong, FormatValue):
    __slots__ = ()
    typeid = 6
    complex = True
    _format = BiStruct('Q')
    minval = 0x0000000000000000
    maxval = 0xFFFFFFFFFFFFFFFF

class INT64(limitedlong, FormatValue):
    __slots__ = ()
    typeid = 7
    complex = True
    _format = BiStruct('q')
    minval = -0x8000000000000000
    maxval = 0x7FFFFFFFFFFFFFFF

class FLOAT(naneqfloat, FormatValue):
    __slots__ = ()
    typeid = 8
    complex = False
    _format = BiStruct('f')

class DOUBLE(naneqfloat, FormatValue):
    __slots__ = ()
    typeid = 9
    complex = True
    _format = BiStruct('d')

class ExoString(str, PrefixValue):
    __slots__ = ()
    typeid = 10
    complex = True
    _format = DWORD._format
    maxlen = DWORD.maxval

class ResRef(str, PrefixValue):
    __slots__ = ()
    typeid = 11
    complex = True
    _format = BYTE._format
    maxlen = BYTE.maxval
    
    def __new__(cls, object):
        return super(ResRef, cls).__new__(cls, str(object).lower()) 

LocalString = namedtuple('LocalString', 'language gender text')

class ExoLocString(tuple):
    __slots__ = ()
    typeid = 12
    complex = True
    _format1 = BiStruct('3I')
    _format2 = BiStruct('2I')
    stringref = property(itemgetter(0))
    strings = property(itemgetter(1))

    def __new__(cls, stringref, strings):
        stringref = int(stringref)
        def coercestrings():
            for locstr in strings:
                yield LocalString(int(locstr[0]), bool(locstr[1]), str(locstr[2]))
        return super(ExoLocString, cls).__new__(cls, (stringref, tuple(coercestrings())))
    
    def pack(self, be=False):
        def generate():
            tsize, sref, count = self.calcsize(), self.stringref, len(self.strings)
            if sref == -1:
                sref = 0xFFFFFFFF
            yield self._format1[be].pack(tsize, sref, count)
            for locstr in self.strings:
                yield self._format2[be].pack(locstr.language << 2 | locstr.gender, len(locstr.text))
                yield locstr.text
        return ''.join(generate())
    
    @classmethod
    def unpack(cls, string, be=False):
        val = cls.unpack_from(string, 0, be)
        if val.calcsize() != len(string):
            raise RuntimeError, 'too much data'  # struct.error: unpack requires a string argument of length 4
        return val
    
    def pack_into(self, buffer, offset, be=False):
        tsize, sref, count = self.calcsize(), self.stringref, len(self.strings)
        if sref == -1:
            sref = 0xFFFFFFFF
        self._format1[be].pack_into(buffer, offset, tsize, sref, count)
        offset += self._format1.size
        for locstr in self.strings:
            sid = locstr.language << 2 | locstr.gender
            slen = len(locstr.text)
            self._format2[be].pack_into(buffer, offset, sid, slen)
            offset += self._format2.size
            for n in xrange(slen): buffer[offset+n] = locstr.text[n]
            offset += slen
    
    @classmethod
    def unpack_from(cls, buffer, offset=0, be=False):
        tsize, sref, count = cls._format1[be].unpack_from(buffer, offset)
        if sref == 0xFFFFFFFF:
            sref = -1
        offset += cls._format1.size
        def generate():
            soff = offset
            for n in xrange(count):
                sid, slen = cls._format2[be].unpack_from(buffer, soff)
                soff += cls._format2.size
                s = buffer[soff:soff+slen]
                if len(s) != slen:
                    raise RuntimeError, 'insufficient data'
                yield (sid >> 2, sid & 1, _buffer(s))
                soff += slen
        return cls(sref, generate())
    
    def write_to(self, f, be=False):
        tsize, sref, count = self.calcsize(), self.stringref, len(self.strings)
        if sref == -1:
            sref = 0xFFFFFFFF
        self._format1[be].write_to(f, tsize, sref, count)
        for locstr in self.strings:
            sid = locstr.language << 2 | locstr.gender
            slen = len(locstr.text)
            self._format2[be].write_to(f, sid, slen)
            f.write(locstr.text)
    
    @classmethod
    def read_from(cls, f, be=False):
        tsize, sref, scount = cls._format1[be].read_from(f)
        if sref == 0xFFFFFFFF:
            sref = -1
        def generate():
            for n in xrange(count):
                sid, slen = cls._format2[be].read_from(f)
                s = f.read(slen)
                if len(s) != slen:
                    raise RuntimeError, 'insufficient data'
                yield (sid >> 2, sid & 1, s)
        return cls(sref, generate())
    
    def calcsize(self):
        return self._format1.size + sum(self._format2.size + len(locstr.text) for locstr in self.strings)

class VOID(str, PrefixValue):
    __slots__ = ()
    typeid = 13
    complex = True
    _format = DWORD._format
    maxlen = DWORD.maxval

class Structure(MutableMapping):
    typeid = 14
    complex = True
    
    @staticmethod
    def _coercevalue(value, old=None):
        if value is None:
            raise ValueError, 'None is not allowed'
        if isinstance(value, DATA_TYPES):
            return value
        if isinstance(old, DATA_TYPES) and old.iscompatible(value):
            return type(old)(value)
        if isinstance(value, str):
            return ExoString(value)
        if isinstance(value, Integral):
            for cls in INTEGER_TYPES[4:8]:
                if cls.iscompatible(value):
                    return cls(value)
            raise ValueError, ('Integer outside bounds of largest type', value)
        if isinstance(value, Real):
            return DOUBLE(value)
        if isinstance(value, Sequence):
            return List(value)
        if isinstance(value, Mapping):
            return Structure(value)
        raise TypeError, ('Not a convertible type', value)
    
    @staticmethod
    def _checkkey(key):
        if type(key) != str:
            raise TypeError, ('key must be a str', key)
        if len(key) > 16:
            raise ValueError, ('key must be <= 16 characters', key)
        return key
    
    def __init__(self, *arg, **kwargs):
        self._dict = dict()
        self._fieldlabels = list()
        self.update(*arg, **kwargs)
    
    def __contains__(self, key):
        return key in self._dict
    
    def __iter__(self):
        return iter(self._fieldlabels)
    
    def __len__(self):
        return len(self._dict)
    
    def __getitem__(self, key):
        key = Structure._checkkey(key)
        return self._dict[key]
    
    def __setitem__(self, key, value):
        key = Structure._checkkey(key)
        if key in self._dict:
            self._dict[key] = Structure._coercevalue(value, self._dict[key])
        else:
            self._dict[key] = Structure._coercevalue(value)
            self._fieldlabels.append(key)
    
    def __delitem__(self, key):
        key = Structure._checkkey(key)
        del self._dict[key]
        self._fieldlabels.remove(key)
    
    def _set(self, key, value):
        add = key not in self._dict
        self._dict[key] = value
        if add:
            self._fieldlabels.append(key)

    def __repr__(self):
    #    if 'Speaker' in self.keys():
    #        # we have a dialogue act, stringify accordingly
    #        return str((self["Speaker"], self["Listener"], self["Text"][0]))
    #    else:
    #        return str(self.items())
        return str(dict(self))

class List(MutableSequence):
    typeid = 15
    complex = True
    
    @staticmethod
    def _coercevalue(value):
        if isinstance(value, Structure):
            return value
        elif isinstance(value, Mapping):
            return Structure(value)
        else:
            raise TypeError, 'Not a Structure or convertible type'
    
    def __init__(self, iterable=None):
        self._list = list()
        if iterable is not None:
            self.extend(iterable)
    
    def __contains__(self, key):
        return key in self._list
    
    def __iter__(self):
        return iter(self._list)
    
    def __len__(self):
        return len(self._list)
    
    def __getitem__(self, index):
        return self._list[index]
    
    def __setitem__(self, index, value):
        if isinstance(index, slice):
            value = [List._coercevalue(v) for v in value]
        else:
            value = List._coercevalue(v)
        self._list[index] = value
    
    def insert(self, index, value):
        self._list.insert(index, List._coercevalue(value))
    
    def __delitem__(self, index):
        del self._list[index]
    
    def _append(self, value):
        self._list.append(value)

    def __repr__(self):
        #return "[" + ",".join([str(i) for i in self]) + "]"
        return str(list(self))


ALL_TYPES = tuple([
    BYTE,
    CHAR,
    WORD,
    SHORT,
    DWORD,
    INT,
    DWORD64,
    INT64,
    FLOAT,
    DOUBLE,
    ExoString,
    ResRef,
    ExoLocString,
    VOID,
    Structure,
    List,
])

DATA_TYPES = ALL_TYPES[0:14]
INTEGER_TYPES = ALL_TYPES[0:8]
REAL_TYPES = ALL_TYPES[8:10]
STRING_TYPES = ALL_TYPES[10:12] + ALL_TYPES[13:14]

ALL_TYPES_BY_ID = dict((_type.typeid, _type) for _type in ALL_TYPES)
DATA_TYPES_BY_ID = dict((_type.typeid, _type) for _type in DATA_TYPES)
