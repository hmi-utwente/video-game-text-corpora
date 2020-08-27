import gff4, os, sqlite3
from binascii import crc32

def _optcache():
    if os.path.exists('gdacolumns.sqlite'):
        return _getcache()
    return None

def _getcache():
    cache = sqlite3.connect('gdacolumns.sqlite')
    cache.execute("CREATE TABLE IF NOT EXISTS names (crc INTEGER PRIMARY KEY, string TEXT UNIQUE COLLATE NOCASE);")
    return cache

def lookupcolname(crc, cache=None):
    if cache is None:
        cache = _optcache()
    if cache is not None:
        for row in cache.execute('SELECT string FROM names WHERE crc = ?;', (crc,)):
            return row[0]
    return None

def checksum(s):
    return crc32(s.strip().lower().encode('utf_16le')) & 0xFFFFFFFF

def addnames(ss):
    def _tuple(s):
        s = s.strip()
        return (crc32(s.lower().encode('utf_16le')) & 0xFFFFFFFF, s)
    cache = _getcache()
    cache.executemany("INSERT OR IGNORE INTO names (crc, string) VALUES (?, ?);", (_tuple(s) for s in ss))
    cache.commit()

def dumpnames(f):
    cache = _optcache()
    count = 0
    if cache is not None:
        for row in cache.execute("SELECT string FROM names ORDER BY string ASC;"):
            print >>f, row[0]
            count += 1
    return count

field10000 = gff4.Field(10000, gff4.ECString, False, 0)
field10001 = gff4.Field(10001, gff4.UINT32, False, 4)
field10999 = gff4.Field(10999, gff4.UINT8, False, 8)
Structcolm = gff4._structtype('colm', (field10000, field10001, field10999), 12)
ListStructcolm = gff4._listtype(Structcolm, False)

def annotate(data, header):
    cache = _optcache()
    if cache is None:
        return None
    for field in header.structs[0].fields:
        if field.label == 10003:
            rowtype = field.type.elem_type
            Structrows = gff4._structtype(rowtype.fourcc, rowtype.fields, rowtype.size)
            field10003 = gff4.Field(field.label, gff4._listtype(Structrows, False), False, field.offset)
        elif field.label == 10002:
            field10002 = gff4.Field(field.label, ListStructcolm, False, field.offset)
    Structgtop = gff4._structtype(header.structs[0].fourcc, (field10002, field10003), header.structs[0].size)
    header = header._replace(structs=(Structgtop, Structcolm, Structrows))
    
    gtop = Structgtop()
    colms = gtop[10002]
    existing = []
    for colm in data[10002]:
        colm = Structcolm(colm)
        if not colm[10000]:
            colname = lookupcolname(colm[10001], cache)
            if colname is not None:
                colm[10000] = colname
        else:
            existing.append(colm[10000])
        colms.append(colm)
    gtop[10003].extend(Structrows(row) for row in data[10003])
    addnames(existing)
    
    return gtop, header

if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'rb') as f:
        g, h = gff4.read_gff4(f)
    
    annotate(g, h)
