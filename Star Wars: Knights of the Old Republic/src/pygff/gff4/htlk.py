from array import array
import gff4

field19002 = gff4.Field(19002, gff4.UINT32, False, 0)
field19003 = gff4.Field(19003, gff4.ECString, False, 4)
StructSTRN = gff4._structtype('STRN', [field19002, field19003], 8)
field19001 = gff4.Field(19001, gff4._listtype(StructSTRN, False), False, 0)
StructTLK_20 = gff4._structtype('TLK ', [field19001], 4)
tlkheader = gff4.Header(version='V4.0', platform='PC  ', file_type='TLK ', file_version='V0.2', string_count=0, string_offset=96, data_offset=96, structs=(StructTLK_20, StructSTRN))

def htlk2tlk(htlk):
    tlk = StructTLK_20()
    table = htlk[19007]
    data = htlk[19008]
    for hstr in htlk[19006]:
        id = hstr[19004]
        start = hstr[19005]
        tlk[19001].append(StructSTRN({19002: id, 19003: _decompress(start, table, data)}))
    return tlk

def getstring(htlk, id):
    for hstr in htlk[19006]:
        if id == hstr[19004]:
            return _decompress(hstr[19005], htlk=htlk)
    raise KeyError

def _decompress(start, table=None, data=None, htlk=None):
    if table is None:
        table = htlk[19007]
    if data is None:
        data = htlk[19008]
    sb = array('u')
    index = start >> 5
    shift = start & 0x1f
    n = data[index] >> shift
    while True:
        e = len(table) / 2 - 1
        while e >= 0:
            e = table[e * 2 + (n & 1)]
            if shift < 31:
                n >>= 1
                shift += 1
            else:
                index += 1
                n = data[index]
                shift = 0
        if e == -1:
            break
        sb.append(unichr(-e - 1))
    return sb.tounicode()

def _dump(htlk, out):
    table = htlk[19007]
    e = len(table) / 2 - 1
    for n in htlk[19008]:
        for bit in xrange(32):
            e = table[e * 2 + (n & 1)]
            n >>= 1
            if e < 0:
                out.write(unichr(-e - 1).encode('utf_16le'))
                e = len(table) / 2 - 1
    

if __name__ == '__main__':
    from gff4 import read_gff4, write_gff4
    import sys
    
    with open(sys.argv[1], 'rb') as f:
        g, h = read_gff4(f)
    
    tlk = htlk2tlk(g)
    
    with open(sys.argv[2], 'wb') as f:
        write_gff4(f, tlk, tlkheader)
