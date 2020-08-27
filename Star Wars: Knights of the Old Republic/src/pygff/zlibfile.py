import zlib
from array import array

class ZlibReader(object):
    def __init__(self, source, sizehint=0):
        self.source = source
        self.sizehint = long(sizehint)
        self.decobj = zlib.decompressobj()
        self.ended = False
        self.decompressed = 0
        self.tail = 0
        self.consumed = 0
        self.unconsumed_tail = ''
        self.unused_data = ''
        self._closed = False
    
    def read(self, size=-1):
        if self._closed:
            raise IOError, 'closed'
        if self.ended:
            return ''
        f = self.source
        d = self.decobj
        decompressed = self.decompressed
        tail = self.tail
        consumed = self.consumed
        sizehint = self.sizehint
        unconsumed_tail = self.unconsumed_tail
        unused_data = self.unused_data
        s = array('c')
        if size < 0:
            c = f.read(65536)
            consumed += len(c)
            if unconsumed_tail:
                c = unconsumed_tail + c
                unconsumed_tail = ''
            while c:
                if not tail:
                    c = d.decompress(c)
                    unconsumed_tail = d.unconsumed_tail
                    unused_data = d.unused_data
                    if c:
                        s.extend(c)
                        decompressed += len(c)
                    if unused_data:
                        s.extend(unused_data)
                        tail += len(unused_data)
                        unused_data = ''
                else:
                    s.extend(c)
                    tail += len(c)
                c = f.read(65536)
                consumed += len(c)
                if unconsumed_tail:
                    c = unconsumed_tail + c
                    unconsumed_tail = ''
            self.ended = True
        else:
            while len(s) < size:
                if not tail:
                    if unconsumed_tail:
                        c = unconsumed_tail
                        unconsumed_tail = ''
                    else:
                        c = f.read(min(max(sizehint - consumed, 1), 65536))
                        consumed += len(c)
                    if not c:
                        self.ended = True
                        break
                    c = d.decompress(c, size - len(s))
                    unconsumed_tail = d.unconsumed_tail
                    unused_data = d.unused_data
                    if c:
                        s.extend(c)
                        decompressed += 1
                    if unused_data:
                        s.extend(unused_data)
                        tail += len(unused_data)
                        unused_data = ''
                else:
                    c = f.read(min(65536, size - len(s)))
                    consumed += len(c)
                    if not c:
                        self.ended = True
                        break
                    s.extend(c)
        self.decompressed = decompressed
        self.tail = tail
        self.consumed = consumed
        self.unconsumed_tail = unconsumed_tail
        self.unused_data = unused_data
        return s.tostring()
    
    def close(self):
        self._closed = True
        self.source.close()

if __name__ == '__main__':
    from StringIO import StringIO
    sample = zlib.compress('The quick brown fox jumped over the lazy dog')
    
    print 'Read full test'
    print ZlibReader(StringIO(sample)).read()

    print 'Read 1 test'
    f = ZlibReader(StringIO(sample))
    s = f.read(1)
    while s:
        print s,
        s = f.read(1)
    print
    
    print 'Read part and rest test'
    f = ZlibReader(StringIO(sample))
    print f.read(10),
    print f.read()

    print 'Read full and unused test'
    f = ZlibReader(StringIO(sample+' and then his tail fell off'))
    print f.read()
    print f.decompressed
    print f.tail