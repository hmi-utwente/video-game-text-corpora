from array import array

class DecryptReader(object):
    def __init__(self, source, cipher):
        self.source = source
        self.cipher = cipher
        if hasattr(cipher, 'mode'):
            self._stream = cipher.mode in (3, 4, 5, 6)
        else:
            self._stream = False
        self._extra = ''
        self._closed = False
    
    def read(self, size=-1):
        if self._closed:
            raise IOError, 'closed'
        f = self.source
        d = self.cipher
        block_size = d.block_size
        s = array('c')
        e = self._extra
        if size < 0:
            c = self.read(65536)
            while c:
                c = e + d.decrypt(c)
                e = ''
                s.extend(c)
                c = f.read(65536)
        else:
            while len(s) < size:
                n = min(65536, size - len(s)) - len(e)
                if self._stream:
                    c = f.read(n)
                    try:
                        c = e + d.decrypt(c)
                    except ValueError:
                        self._stream = False
                        r = n % block_size
                        c += f.read(block_size - r)
                        c = e + d.decrypt(c)
                else:
                    r = n % block_size
                    if r: n += block_size - r
                    c = f.read(n)
                    c = e + d.decrypt(c)
                n = size - len(s)
                if len(c) > n:
                    e = c[n:]
                    c = c[:n]
                else:
                    e = ''
                s.extend(c)
        self._extra = e
        return s.tostring()
    
    def close(self):
        self._closed = True
        self.source.close()

class EncryptWriter(object):
    def __init__(self, dest, cipher, stream=False):
        self._dest = dest
        self._cipher = cipher
        if stream:
            self._stream = True
        elif hasattr(cipher, 'mode'):
            self._stream = cipher.mode in (3, 4, 5, 6)
        else:
            self._stream = False
        self._extra = ''
        self._closed = False
    
    def write(self, s):
        if self._closed:
            raise IOError, 'closed'
        c = self._cipher
        if self._stream:
            try:
                s = c.encrypt(s)
            except ValueError:
                self._stream = False
                self.write(s)
            else:
                self._dest.write(s)
        else:
            block_size = c.block_size
            s = self._extra + s
            r = len(s) % block_size
            if r:
                i = len(s) - r
                self._dest.write(c.encrypt(s[:i]))
                self._extra = s[i:]
            else:
                self._dest.write(c.encrypt(s))
                self._extra = ''
    
    def close(self):
        if self._extra:
            try:
                s = c.encrypt(self._extra)
            except ValueError:
                raise IOError, 'Cannot close, need %d bytes'%(self._cipher.block_size - len(self._extra))
            else:
                self._dest.write(s)
                self._extra = ''
        self._closed = True

if __name__ == '__main__':
    from StringIO import StringIO
    #sample = zlib.compress('The quick brown fox jumped over the lazy dog')
    