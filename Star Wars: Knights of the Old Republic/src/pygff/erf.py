import hashlib, struct, zlibfile, cryptofile, ioutils
from struct import unpack_from, unpack, pack
from collections import namedtuple, Iterable
from numbers import Integral
from binascii import unhexlify, hexlify
try: from cStringIO import StringIO
except ImportError: from StringIO import StringIO
try:
    from Crypto.Cipher.Blowfish import new as Blowfish
    from Crypto.Cipher.XOR import new as XOR
except ImportError:
    Blowfish = None
    XOR = None
from warnings import warn
from traceback import print_exc
from datetime import date
from zlib import decompressobj
from os.path import getmtime, splitext, getsize
from ioutils import copyio
from fnv import *
try:
    from fnvdb import lookupfile, lookuptype
except:
    print_exc()
    
    def lookupfile(hash):
        return None

    def lookuptype(hash):
        return None

__all__ = ['ERF1File', 'ERF2File']

class Struct(struct.Struct):
    __slots__ = ()
    def unpack_file(self, f):
        return self.unpack(f.read(self.size))



FmtTocItem20 = Struct('=64s2I')
FmtTocItem22 = Struct('=64s3I')
FmtTocItem30 = Struct('=IQIIII')
FmtErfHeader1 = Struct('=9I116x')
FmtLocString = Struct('=2I')
FmtKeyItem10 = Struct('=16sIH2x')
FmtKeyItem11 = Struct('=32sIH2x')
FmtResItem = Struct('=2I')
FmtErfHeader20 = Struct('=3Ii')
FmtErfHeader22 = Struct('=3Ii2I16s')
FmtErfHeader30 = Struct('=4I16s')
ResItem = namedtuple('ResItem', 'resref resid restype offset length')
TocItem = namedtuple('TocItem', 'name offset packed_length length')
Toc3Item = namedtuple('TocItem', 'name name_hash type_hash offset packed_length length')

ERF20MAGIC = 'ERF V2.0'.encode('utf-16le')
ERF22MAGIC = 'ERF V2.2'.encode('utf-16le')
ERF30MAGIC = 'ERF V3.0'.encode('utf-16le')

class ERF1File(object):
    def __init__(self, f):
        if isinstance(f, basestring):
            f = open(f, 'rb')
        self._file = f
        
        fourcc = f.read(4)
        ver = f.read(4)
        
        if fourcc not in ('ERF ', 'MOD ', 'SAV ', 'HAK '):
            raise ValueError, ('unsupported type', fourcc)
        if ver not in ('V1.0', 'V1.1'):
            raise ValueError, ('unsupported version', ver)
        
        langcnt, langsize, entrycnt, langoff, keyoff, resoff, self.year, self.day, self.descref = FmtErfHeader1.unpack_file(f)
        
        f.seek(langoff)
        self.localized_strings = {}
        for n in xrange(langcnt):
            langid, length = FmtResItem.unpack_file(f)
            self.localized_strings[langid] = f.read(length)
        
        f.seek(keyoff)
        resources = []
        if ver == 'V1.0':
            unpacker = FmtKeyItem10.unpack_file
        else:
            unpacker = FmtKeyItem11.unpack_file
        for n in xrange(entrycnt):
            resref, resid, restype = unpacker(f)
            resref = resref.strip('\0')
            resources.append((resref, resid, restype))
        
        f.seek(resoff)
        self._toc = {}
        for resref, resid, restype in resources:
            offset, length = FmtResItem.unpack_file(f)
            self._toc[resref.lower()] = ResItem(resref, resid, restype, offset, length)
        self._byoffset = dict((item.offset, item) for item in self._toc.itervalues())
    
    def __iter__(self):
        return iter(self._toc)
    
    def open(self, name):
        if isinstance(name, basestring):
            item = self._toc[name.lower()]
        else:
            item = name
        f = self._file
        f.seek(item.offset)
        return StringIO(f.read(item.length))

    @staticmethod
    def checksample(sample):
        if sample[:4] not in ('ERF ', 'MOD ', 'SAV ', 'HAK '):
            return False
        if sample[4:8] not in ('V1.0', 'V1.1'):
            return False
        return True
    
    @property
    def date(self):
        return date.fromordinal(date(self.year+1900, 1, 1).toordinal() + self.day - 1)

class BiowareZlibReader(zlibfile.ZlibReader):
    def __init__(self, stream, *args, **kwargs):
        super(BiowareZlibReader, self).__init__(stream, *args, **kwargs)
        dec = self.decobj
        c = stream.read(1)
        if c == '\xF9':
            dec.decompress('x\1')
        else:
            c = ord(c)
            raise ValueError, ('Unknown compression method', c)
            #h = (((c & 0xF0) - (8 << 4)) | 0x8
            #r = chr(31 - h * 256 % 31)
            #print hex(ord(data[0])), hex(h), hex(r)
            #dec.decompress(chr(h))
            #dec.decompress(chr(r))

def unhexpw(pw):
    pw = ''.join(c for c in str(pw) if c in '0123456789abcdefABCDEF')
    return unhexlify(pw)

def da2keyhash(key):
    arr = ''.join(chr(i) for i in xrange(256))
    arr = Blowfish(key).encrypt(arr)
    md5 = hashlib.md5()
    md5.update(arr)
    return md5.digest()

class ERF2File(object):
    def __init__(self, f, pw=None):
        if isinstance(f, basestring):
            self._file = None
            self._filename = f
            f = open(f, 'rb')
        else:
            self._file = f
            self._filename = None
        fourccver = f.read(16).decode('utf-16')
        
        self._pw = None
        self._pwstr = None
        
        if fourccver == 'ERF V2.0':
            self.encryption = 0
            self.compression = 0
            self.module_id = 0
            self.unknownflag1 = 0
            self.pw_hash = None
            filecount, self.year, self.day, unknown1 = FmtErfHeader20.unpack_file(f)
            
            if unknown1 != -1:
                warn('junk field is %d instead of -1'%unknown1)
            
            self._toc = toc = []
            for n in xrange(filecount):
                name, offset, length = FmtTocItem20.unpack_file(f)
                name = name.decode('utf-16').strip('\0')
                toc.append(TocItem(name, offset, length, length))
        
        elif fourccver == 'ERF V2.2':
            filecount, self.year, self.day, unknown1, flags, self.module_id, self.pw_hash = FmtErfHeader22.unpack_file(f)
            
            self.encryption = (flags >> 4) & 0xF
            if self.encryption not in (0, 1, 2, 3):
                raise ValueError, ('unknown encryption', self.encryption)
            self.compression = (flags >> 29) & 0x7
            if self.compression not in (0, 1, 7):
                raise ValueError, ('unknown compression', self.compression)
            self.unknownflag1 = flags & 1
            if flags & 0x1FFFFF0E:
                warn(('unknown flags', flags & 0x1FFFFF0E))
            if unknown1 != -1:
                warn('junk field is %d instead of -1'%unknown1)
            
            self._toc = toc = []
            for n in xrange(filecount):
                name, offset, packlen, length = FmtTocItem22.unpack_file(f)
                name = name.decode('utf-16').strip('\0')
                while name.endswith('\0'):
                    name = name[:-1]
                toc.append(TocItem(name, offset, packlen, length))
        else:
            raise ValueError, ('unsupported file', fourccver)
        
        if self.encryption and pw is not None:
            try:
                self.password = pw
            except ValueError:
                print_exc()
                
        self._fourccver = fourccver
        self._byname = dict((item.name.lower(), item) for item in toc)
        self._byoffset = dict((item.offset, item) for item in toc)
        
        if self._filename is not None:
            f.close()
    
    def __iter__(self):
        return iter(self._byname)
    
    def _find(self, name):
        return self._byname[name.lower()]
    
    def open(self, name, pw=None):
        if isinstance(name, basestring):
            item = self._find(name)
        else:
            item = name
        
        if self._filename is not None:
            f = open(self._filename, 'rb')
            
            if not self.encryption and not self.compression:
                return ioutils.BoundedReader(f, item.offset, item.offset+item.length)
        
            f.seek(item.offset)
            f = ioutils.LimitedReader(f, item.packed_length)
            if self.encryption:
                method = self.encryption
                pw = self.password
                if pw is None:
                    if method != 1:
                        raise RuntimeError, 'encrypted'
                    else:
                        pw = ''
                if method == 1:
                    f = cryptofile.DecryptReader(f, XOR(pw+chr(0)))
                elif method in (2, 3):
                    f = cryptofile.DecryptReader(f, Blowfish(pw))
                else:
                    raise ValueError, ('unsupported encryption', method)
            if self.compression:
                method = self.compression
                if method == 1:
                    f = BiowareZlibReader(f, item.packed_length)
                else:
                    raise ValueError, ('unsupported compression', method)
                
            return ioutils.MemoReader(ioutils.LimitedReader(f, item.length))
        else:
            f = self._file
        
            f.seek(item.offset)
            data = f.read(item.packed_length)
            if self.encryption:
                method = self.encryption
                pw = self.password
                if pw is None:
                    if method != 1:
                        raise RuntimeError, 'encrypted'
                    else:
                        pw = ''
                if method == 1:
                    data = XOR(pw+chr(0)).decrypt(data)
                elif method in (2, 3):
                    data = Blowfish(pw).decrypt(data)
                else:
                    raise ValueError, ('unsupported encryption', method)
            if self.compression:
                method = self.compression
                if method == 1:
                    dec = decompressobj()
                    if data[0] == '\xF9':
                        dec.decompress('x\1')
                    else:
                        c = ord(data[0])
                        raise ValueError, ('Unknown compression method', c)
                        #h = (((c & 0xF0) - (8 << 4)) | 0x8
                        #r = chr(31 - h * 256 % 31)
                        #print hex(ord(data[0])), hex(h), hex(r)
                        #dec.decompress(chr(h))
                        #dec.decompress(chr(r))
                    data = dec.decompress(data[1:])
                else:
                    raise ValueError, ('unsupported compression', method)
            #print repr(data[:20])
                
            return StringIO(data[:item.length])

    @staticmethod
    def checksample(sample):
        if sample[:16] not in (ERF20MAGIC, ERF22MAGIC):
            return False
        return True
    
    @property
    def date(self):
        return date.fromordinal(date(self.year+1900, 1, 1).toordinal() + self.day)
    
    @property
    def password(self):
        return self._pw
    
    @password.setter
    def password(self, pw):
        if not self.encryption:
            warn('ERF is not encrypted')
            return
        if self.encryption in (1, 2) and isinstance(pw, (basestring, Integral)):
            md5 = hashlib.md5()
            md5.update(str(pw))
            digest = md5.digest()
            if digest != self.pw_hash:
                raise ValueError, ('incorrect password', self.pw_hash, pw, digest)
            self._pw = pack('Q', int(pw))
            self._pwstr = str(pw)
        elif self.encryption == 3 and isinstance(pw, basestring):
            pw2 = unhexpw(pw)
            digest = da2keyhash(pw2)
            if digest != self.pw_hash:
                raise ValueError, ('incorrect password', self.pw_hash, pw, digest)
            self._pw = pw2
            self._pwstr = str(pw)
        else:
            for pww in pw:
                try:
                    self.password = pww
                except ValueError:
                    pass
                else:
                    return
            raise ValueError, ('no correct passwords', self.pw_hash)
    
    @property
    def passwordstring(self):
        return self._pwstr
    
    def export(self, name, dest_path):
        if isinstance(name, basestring):
            item = self._find(name)
        else:
            item = name
        
        f = self.open(item)
        with open(dest_path, 'wb') as o:
            copyio(o, f)
        
        if getsize(dest_path) != item.length:
            raise IOError, 'output file not the length it should be'
    
    @property
    def decryptable(self):
        return not self.encryption or self._pw is not None

class ERF3File(ERF2File):
    def __init__(self, f, pw=None):
        if isinstance(f, basestring):
            self._file = None
            self._filename = f
            f = open(f, 'rb')
        else:
            self._file = f
            self._filename = None
        
        fourccver = f.read(16).decode('utf-16')
        
        self._pw = None
        self._pwstr = None
        
        if fourccver == 'ERF V3.0':
            self.year = 0
            self.day = 0
            namesize, filecount, flags, self.module_id, self.pw_hash = FmtErfHeader30.unpack_file(f)
            
            self.encryption = (flags >> 4) & 0xF
            if self.encryption not in (0, 1, 2, 3):
                raise ValueError, ('unknown encryption', self.encryption)
            self.compression = (flags >> 29) & 0x7
            if self.compression not in (0, 1, 7):
                raise ValueError, ('unknown compression', self.compression)
            self.unknownflag1 = flags & 1
            if flags & 0x1FFFFF0E:
                warn(('unknown flags', flags & 0x1FFFFF0E))
            
            self.names = names = dict()
            offset = 0
            for name in f.read(namesize).split('\0')[:-1]:
                names[offset] = name
                offset += len(name) + 1
                
            self._toc = toc = []
            for n in xrange(filecount):
                nameindex, namehash, typehash, offset, packlen, unpacklen = FmtTocItem30.unpack_file(f)
                name = None
                if nameindex != 0xFFFFFFFF:
                    name = self.names[nameindex]
                else:
                    name = lookupfile(namehash)
                    if name is None:
                        ext = lookuptype(typehash)
                        if ext is None:
                            name = '[%016x].[%08x]'%(namehash, typehash)
                        else:
                            name = '[%016x].%s'%(namehash, ext)
                #print namehash, typehash, name if nameindex != 0xFFFFFFFF else ''
                toc.append(Toc3Item(name, namehash, typehash, offset, packlen, unpacklen))
        else:
            raise ValueError, ('unsupported file', fourccver)
        
        if self.encryption and pw is not None:
            try:
                self.password = pw
            except ValueError:
                print_exc()
        
        self._fourccver = fourccver
        self._byname = dict((item.name.lower(), item) for item in toc)
        self._byoffset = dict((item.offset, item) for item in toc)
        self._byfnv = dict((item.name_hash, item) for item in toc)
        
        if self._filename is not None:
            f.close()
    
    def _find(self, name):
        try:
            return self._byfnv[fnv64(name.lower().encode('utf-8'))]
        except KeyError:
            return self._byname[name.lower()]

    @staticmethod
    def checksample(sample):
        if sample[:16] not in (ERF30MAGIC,):
            return False
        return True

def open_erf(path, sample=None, passwords=None):
    if sample is None or len(sample) < 16:
        if isinstance(path, basestring):
            with open(path, 'rb') as f:
                sample = f.read(16)
        else:
            sample = path.read(16)
            path.seek(0)
    
    if ERF1File.checksample(sample):
        return ERF1File(path)
    elif ERF2File.checksample(sample):
        return ERF2File(path, passwords)
    elif ERF3File.checksample(sample):
        return ERF3File(path, passwords)
    
    return None

if __name__ == '__main__':
    pass
