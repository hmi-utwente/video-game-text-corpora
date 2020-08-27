import csv, gff4, re
from gff4.gdacolnames import lookupcolname, addnames, checksum

CRC_NAME = re.compile(r'^\$[0-9a-f]{8}$', re.I)

def colname(col):
    if 10000 in col:
        return col[10000].encode('utf_8')
    else:
        name = lookupcolname(col[10001])
        return name if name is not None else '$%08x'%col[10001]

coltypes = ('string', 'int', 'float', 'bool', 'resource')
gfftypes = (gff4.ECString, gff4.INT32, gff4.FLOAT32, gff4.UINT8, gff4.ECString)

def colvalue(v):
    if v is None:
        return '****'
    elif isinstance(v, unicode):
        return v.encode('utf_8')
    else:
        return v

def gda2csv(gda, dest):
    if isinstance(gda, basestring):
        with open(gda, 'rb') as f:
            gda, header = gff4.read_gff4(f)
    elif not isinstance(gda, gff4.Structure):
        gda, header = gff4.read_gff4(gda)
        
    close = False
    if isinstance(dest, basestring):
        f = open(dest, 'wb')
        close = True
    
    try:
        csvw = csv.writer(f)
        csvw.writerow([colname(col) for col in gda[10002]])
        csvw.writerow([coltypes[col[10999]] for col in gda[10002]])
        for row in gda[10003]:
            csvw.writerow([colvalue(v) for k, v in sorted(row.iteritems())])
    finally:
        if close:
            f.close()

#G2DA_COLUMN_NAME = gff4.Field(10000, gff4.ECString, False, 0)
#G2DA_COLUMN_HASH = gff4.Field(10001, gff4.UINT32, False, 4)
#G2DA_COLUMN_TYPE = gff4.Field(10999, gff4.UINT8, False, 8)
#Structcolm = gff4._structtype('colm', (G2DA_COLUMN_NAME, G2DA_COLUMN_HASH, G2DA_COLUMN_TYPE), 12)

G2DA_COLUMN_HASH = gff4.Field(10001, gff4.UINT32, False, 0)
G2DA_COLUMN_TYPE = gff4.Field(10999, gff4.UINT8, False, 4)
Structcolm = gff4._structtype('colm', (G2DA_COLUMN_HASH, G2DA_COLUMN_TYPE), 8)
ListStructcolm = gff4._listtype(Structcolm, False)
G2DA_COLUMN_LIST = gff4.Field(10002, ListStructcolm, False, 0)

G2DA_COLUMN_1_LABEL = 10005

def csv2gda(source, dest=None, platform='PC  '):
    f = source
    close = False
    if isinstance(source, basestring):
        f = open(source, 'rb')
        close = True
    
    csvr = csv.reader(f)
    names = csvr.next()
    colcount = len(names)
    types = csvr.next()
    if len(types) != colcount:
        raise RuntimeError, 'inconsistent number of columns'
    if names[0].lower() != 'id':
        raise RuntimeError, 'first column must be ID'
    if types[0] != 'int':
        raise RuntimeError, 'ID column must be int'
    
    goodnames = [s.decode('utf_8') for s in names if not CRC_NAME.match(s)]
    addnames(goodnames)
    
    column_list = ListStructcolm()
    row_fields = []
    field_offset = 0
    field_label = G2DA_COLUMN_1_LABEL
    for name, typename in zip(names, types):
        if typename == 'comment':
            continue
        colm = Structcolm()
        if CRC_NAME.match(name):
            colm[10001] = int(name[1:], 16)
        else:
            colm[10001] = checksum(name)
        coltypeid = coltypes.index(typename)
        colm[10999] = coltypeid
        column_list.append(colm)
        
        field = gff4.Field(field_label, gfftypes[coltypeid], False, field_offset)
        field_label += 1
        field_offset += 4
        row_fields.append(field)
    
    Structrows = gff4._structtype('rows', row_fields, field_offset)
    ListStructrows = gff4._listtype(Structrows, False)
    G2DA_ROW_LIST = gff4.Field(10003, ListStructrows, False, 4)
    Structgtop = gff4._structtype('gtop', (G2DA_COLUMN_LIST, G2DA_ROW_LIST), 8)
    header = gff4.Header('V4.0', platform, 'G2DA', 'V0.2', 0, 0, 0, (Structgtop, Structcolm, Structrows))
    
    rows_list = ListStructrows()
    for cells in csvr:
        if len(cells) != colcount:
            raise RuntimeError, 'inconsistent number of columns'
        field_label = G2DA_COLUMN_1_LABEL
        row = Structrows()
        for cell, typename in zip(cells, types):
            if typename == 'comment':
                continue
            if cell != '****':
                row[field_label] = cell
            field_label += 1
        rows_list.append(row)
    
    gtop = Structgtop()
    gtop[10002] = column_list
    gtop[10003] = rows_list
    
    if close:
        f.close()
    
    if dest is None:
        return gff4.GFF4Data(header, gtop)
    elif isinstance(dest, basestring):
        with open(dest, 'wb') as f:
            gff4.write_gff4(f, gtop, header, 4)
    else:
        gff4.write_gff4(dest, gtop, header, 4)

if __name__ == '__main__':
    import sys, os
    from glob import glob
    
    def replaceext(path, old, new):
        base, ext = os.path.splitext(path)
        if ext.lower() == old.lower():
            return base + new
        else:
            return path + new
    
    def makedest(src, oldext, newext, dest=None):
        if dest is None:
            return replaceext(src, oldext, newext)
        elif os.path.isdir(dest):
            return os.path.join(dest, os.path.basename(replaceext(src, oldext, newext)))
        elif dest.endswith(('\\', '/')):
            os.mkdir(dest)
            return os.path.join(dest, os.path.basename(replaceext(src, oldext, newext)))
        else:
            dirpath = os.path.dirname(dest)
            if not os.path.exists(dirpath):
                os.mkdir(dirpath)
            return dest
    
    if sys.argv[1] == 'gda2csv':
        sourcepath = sys.argv[2]
        dest = sys.argv[3] if len(sys.argv) > 3 else None
        if '*' in sourcepath:
            if dest is not None and not os.path.exists(dest):
                os.mkdir(dest)
            for sourcepath in glob(sourcepath):
                destpath = replaceext(sourcepath, '.gda', '.csv')
                if dest is not None:
                    destpath = os.path.join(dest, os.path.basename(destpath))
                print 'Decompiling', sourcepath, 'to', destpath
                gda2csv(sourcepath, destpath)
        else:
            dest = makedest(sourcepath, '.gda', '.csv', dest)
            print 'Decompiling', sourcepath, 'to', dest
            gda2csv(sourcepath, dest)
    elif sys.argv[1] == 'csv2gda':
        sourcepath = sys.argv[2]
        dest = sys.argv[3] if len(sys.argv) > 3 else None
        if '*' in sourcepath:
            if dest is not None and not os.path.exists(dest):
                os.mkdir(dest)
            for sourcepath in glob(sourcepath):
                destpath = replaceext(sourcepath, '.csv', '.gda')
                if dest is not None:
                    destpath = os.path.join(dest, os.path.basename(destpath))
                print 'Compiling', sourcepath, 'to', destpath
                csv2gda(sourcepath, destpath)
        else:
            dest = makedest(sourcepath, '.csv', '.gda', dest)
            print 'Compiling', sourcepath, 'to', dest
            csv2gda(sourcepath, dest)
    else:
        print 'Unknown command'
        print 'Use: gda2csv <gda file/pattern> [destination file/folder]'
        print 'Use: csv2gda <csv file/pattern> [destination file/folder]'
