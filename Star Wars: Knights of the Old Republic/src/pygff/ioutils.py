from array import array

class LimitedReader(object):
    def __init__(self, stream, limit):
        self.stream = stream
        self.limit = limit
        self.count = 0
        self.closed = False
    
    def read(self, n=-1):
        if self.closed:
            raise IOError, 'closed'
        f = self.stream
        count = self.count
        limit = self.limit
        if n < 0:
            s = f.read(limit - count)
        else:
            s = f.read(min(n, limit - count))
        self.count = count + len(s)
        return s
    
    def close(self):
        self.closed = True
        self.stream.close()

class BoundedReader(object):
    def __init__(self, stream, start, end, rewind=True):
        self.stream = stream
        self.start = start
        self.end = end
        self.closed = False
        if rewind:
            stream.seek(start)
    
    def tell(self):
        if self.closed:
            raise IOError, 'closed'
        return self.stream.tell() - self.start
    
    def seek(self, offset, whence=0):
        if self.closed:
            raise IOError, 'closed'
        if whence == 0:
            self.stream.seek(min(self.start + max(0, offset), self.end))
        elif whence == 2:
            self.stream.seek(max(self.end - min(0, offset), self.start), 2)
        elif whence == 1:
            self.stream.seek(min(self.start + max(0, self.tell() + offset), self.end))
    
    def read(self, n=-1):
        if self.closed:
            raise IOError, 'closed'
        if n < 0:
            return self.stream.read(self.end - self.stream.tell())
        else:
            return self.stream.read(min(n, self.end - self.stream.tell()))
    
    def close(self):
        self.closed = True
        self.stream.close()
        self.stream = None

class MemoReader(object):
    def __init__(self, stream):
        self.stream = stream
        self.buffer = array('c')
        self.pos = 0
        self.closed = False
    
    def read(self, n=-1):
        if self.closed:
            raise IOError, 'closed'
        if n < 0:
            s = self.stream.read()
            if s:
                self.buffer.extend(s)
            s = self.buffer[self.pos:]
        else:
            if self.pos + n <= len(self.buffer):
                s = self.buffer[self.pos:self.pos+n]
            else:
                s = self.stream.read(self.pos + n - len(self.buffer))
                if s:
                    self.buffer.extend(s)
                s = self.buffer[self.pos:]
        self.pos += len(s)
        return s.tostring()
    
    def tell(self):
        if self.closed:
            raise IOError, 'closed'
        return self.pos
    
    def seek(self, offset, whence=0):
        if self.closed:
            raise IOError, 'closed'
        if whence == 0:
            if offset < 0:
                raise ValueError
            if offset > len(self.buffer):
                s = self.stream.read(offset - len(self.buffer))
                if s:
                    self.buffer.extend(s)
            self.pos = min(offset, len(self.buffer))
        elif whence == 1:
            if self.pos + offset > len(self.buffer):
                s = self.stream.read(self.pos + offset - len(self.buffer))
                if s:
                    self.buffer.extend(s)
            self.pos = min(max(offset + self.pos, 0), len(self.buffer))
        elif whence == 2:
            if offset > 0:
                raise ValueError
            s = self.stream.read()
            if s:
                self.buffer.extend(s)
            self.pos = max(len(self.buffer) - offset, 0)
    
    def close(self):
        self.closed = True
        self.buffer = None
        self.stream.close()

class CloseBlocker(object):
    def __init__(self, stream):
        self.stream = stream
    def __getattr__(self, name):
        return getattr(self.stream, name)
    def close(self):
        pass

def copyio(to, fro, chunksize=65536):
    s = fro.read(chunksize)
    while s:
        to.write(s)
        s = fro.read(chunksize)
