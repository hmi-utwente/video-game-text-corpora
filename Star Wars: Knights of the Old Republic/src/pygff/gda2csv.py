import sys, csv, gff4

def colname(col):
    if 10000 in col:
        return col[10000].encode('utf_8')
    else:
        return '$%08x'%col[10001]

coltypes = {
    0: 'string',
    1: 'int',
    2: 'float',
    3: 'bool',
    4: 'resource',
}

def colvalue(v):
    if v is None:
        return '****'
    elif isinstance(v, unicode):
        return v.encode('utf_8')
    else:
        return v

with open(sys.argv[1], 'rb') as f:
    gff, header = gff4.read_gff4(f)

with open(sys.argv[2], 'wb') as f:
    csv = csv.writer(f)
    csv.writerow([colname(col) for col in gff[10002]])
    csv.writerow([coltypes[col[10999]] for col in gff[10002]])
    for row in gff[10003]:
        csv.writerow([colvalue(v) for k, v in sorted(row.iteritems())])
