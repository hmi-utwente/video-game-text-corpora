from sys import stderr as _stderr
from collections import namedtuple, deque
from array import array
from gff32.types import *
from gff32.types import Format

__all__ = [
    'read_gff', 'write_gff'
]

HeaderFormat = Format('4s4s12I')
StructFormat = Format('3I')
FieldFormat = Format('2I4s')
FmtUINT32 = Format('I')
LabelFormat = Format('16s')

Header = namedtuple('Header', 'filetype fileversion structoffset structcount'
    ' fieldoffset fieldcount labeloffset labelcount fielddataoffset fielddatacount'
    ' fieldindicesoffset fieldindicescount listindicesoffset listindicescount')

def read_header(f):
    return Header(*HeaderFormat.read_from(f))

def read_gff(f):
    header = read_header(f)
    if header.fileversion != 'V3.2':
        raise RuntimeError, 'unsupported file format'
    
    structs = []
    fields = {}
    fieldindices = []
    fieldoffsets = []
    dataoffsets = []
    listoffsets = []
    
    f.seek(header.structoffset)
    data = f.read(header.fieldoffset - header.structoffset)
    offset = 0
    for structindex in xrange(header.structcount):
        structid, fieldoffset, fieldcount = StructFormat.unpack_from(data, offset)
        if structid == 0xFFFFFFFF:
            structid = -1
        offset += StructFormat.size
        if fieldcount > 1:
            fieldoffsets.append((fieldoffset, structindex, fieldcount))
        elif fieldcount == 1:
            fieldindices.append((structindex, fieldoffset))
        struct = Structure()
        if not structs:
            struct.filetype = header.filetype
            struct.fileversion = header.fileversion
        struct.structid = structid
        structs.append(struct)
    
    #f.seek(header.fieldoffset)
    data = f.read(header.labeloffset - header.fieldoffset)
    offset = 0
    for fieldindex in xrange(header.fieldcount):
        typeid, labelindex, dataoffset = FieldFormat.unpack_from(data, offset)
        offset += FieldFormat.size
        try:
            type_ = ALL_TYPES_BY_ID[typeid] # Breakpoint A
        except Exception as e:
            #print("Gff32 parser encountered an unknown type at breakpoint A. Ignoring this error...")
            pass
        if not type_.complex:
            fields[fieldindex] = (labelindex, type_.unpack_from(dataoffset))
        else:
            dataoffset, = FmtUINT32.unpack(dataoffset)
            if typeid == 14:
                fields[fieldindex] = (labelindex, structs[dataoffset])
            elif typeid == 15:
                listoffsets.append((dataoffset, fieldindex, labelindex))
            else:
                dataoffsets.append((dataoffset, fieldindex, labelindex, typeid))
    
    #f.seek(header.labeloffset)
    data = f.read(header.fielddataoffset - header.labeloffset)
    labels = [data[offset:offset+16].strip(chr(0)) for offset in xrange(0, header.labelcount*16, 16)]
    
    #f.seek(header.fielddataoffset)
    data = f.read(header.fieldindicesoffset - header.fielddataoffset)
    for offset, fieldindex, labelindex, typeid in sorted(dataoffsets):
        try:
            type_ = ALL_TYPES_BY_ID[typeid] # Breakpoint B
        except Exception as e:
            #print("Gff32 parser encountered an unknown type at breakpoint B. Ignoring this error...")
            pass
        fields[fieldindex] = (labelindex, type_.unpack_from(data, offset))
    del dataoffsets
    
    #f.seek(header.fieldindicesoffset)
    data = f.read(header.listindicesoffset - header.fieldindicesoffset)
    for offset, structindex, fieldcount in sorted(fieldoffsets):
        for m in xrange(fieldcount):
            fieldindex, = FmtUINT32.unpack_from(data, offset)
            offset += FmtUINT32.size
            fieldindices.append((structindex, fieldindex))
    del fieldoffsets
    
    #f.seek(header.listindicesoffset)
    data = f.read()
    for offset, fieldindex, labelindex in sorted(listoffsets):
        count, = FmtUINT32.unpack_from(data, offset)
        offset += FmtUINT32.size
        list_ = List()
        for n in xrange(count):
            structindex, = FmtUINT32.unpack_from(data, offset)
            offset += FmtUINT32.size
            list_.append(structs[structindex])
        fields[fieldindex] = (labelindex, list_)
    del listoffsets
    
    for structindex, fieldindex in fieldindices:
        labelindex, field = fields[fieldindex]
        structs[structindex]._set(labels[labelindex], field)
    
    return structs[0]

def write_gff(f, root):
    if root.structid != -1:
        raise RuntimeError, ('not a root struct', root.structid)
    if root.fileversion != 'V3.2':
        raise RuntimeError, ('unsupported file format', root.fileversion)
    if not isinstance(root.filetype, str) or len(root.filetype) != 4:
        raise RuntimeError, ('invalid filetype', root.filetype)
    
    struct_buf = array('c')
    field_buf = array('c')
    label_buf = array('c')
    fielddata_buf = array('c')
    fieldindices_buf = array('c')
    listindices_buf = array('c')
    
    queue = deque()
    queue.append(root)
    struct_count = 0
    total_structs = 1
    field_count = 0
    label_cache = dict()
    list_offset = 0
    list_count = 0
    list_start = 0
    list_counts = deque()
    
    while queue:
        struct = queue.popleft()
        
        if list_count and list_start <= struct_count:
            listindices_buf.extend(FmtUINT32.pack(struct_count))
            list_count -= 1
        
        fieldoffset = len(fieldindices_buf)
        use_indices = len(struct) != 1
        
        for key, data in struct.iteritems():
            if isinstance(data, List):
                queue.extend(data)
                dataoffset = FmtUINT32.pack(list_offset)
                list_counts.append((total_structs, len(data)))
                total_structs += len(data)
                list_offset += FmtUINT32.size * (len(data) + 1)
            elif isinstance(data, Structure):
                queue.append(data)
                dataoffset = FmtUINT32.pack(total_structs)
                total_structs += 1
            elif not type(data).complex:
                dataoffset = data.pack()
            else:
                dataoffset = FmtUINT32.pack(len(fielddata_buf))
                fielddata_buf.extend(data.pack())
            
            label_index = label_cache.get(key)
            if label_index is None:
                label_cache[key] = label_index = len(label_cache)
                label_buf.extend(LabelFormat.pack(key))
            
            field_buf.extend(FieldFormat.pack(data.typeid, label_index, dataoffset))
            
            if use_indices:
                fieldindices_buf.extend(FmtUINT32.pack(field_count))
            else:
                fieldoffset = field_count
            field_count += 1
        
        structid = struct.structid
        if structid == -1:
            structid = 0xFFFFFFFF
        struct_buf.extend(StructFormat.pack(structid, fieldoffset, len(struct)))
        struct_count += 1
        
        while list_count == 0 and list_counts:
            list_start, list_count = list_counts.popleft()
            listindices_buf.extend(FmtUINT32.pack(list_count))
    
    struct_offset = HeaderFormat.size
    field_offset = struct_offset + len(struct_buf)
    label_offset = field_offset + len(field_buf)
    fielddata_offset = label_offset + len(label_buf)
    fieldindices_offset = fielddata_offset + len(fielddata_buf)
    listindices_offset = fieldindices_offset + len(fieldindices_buf)
    
    f.write(HeaderFormat.pack(
        root.filetype, root.fileversion,
        struct_offset, struct_count,
        field_offset, field_count,
        label_offset, len(label_cache),
        fielddata_offset, len(fielddata_buf),
        fieldindices_offset, len(fieldindices_buf),
        listindices_offset, len(listindices_buf)
    ))
    
    if isinstance(f, file):
        struct_buf.tofile(f)
        field_buf.tofile(f)
        label_buf.tofile(f)
        fielddata_buf.tofile(f)
        fieldindices_buf.tofile(f)
        listindices_buf.tofile(f)
    else:
        f.write(struct_buf.tostring())
        f.write(field_buf.tostring())
        f.write(label_buf.tostring())
        f.write(fielddata_buf.tostring())
        f.write(fieldindices_buf.tostring())
        f.write(listindices_buf.tostring())

if __name__ == '__main__':
    from pprint import pprint
    from StringIO import StringIO
    import sys
    
    
    if sys.argv[1] == 'pprint':
        with open(sys.argv[2], 'rb') as f:
            g = read_gff(f)
        pprint(g)
    elif sys.argv[1] == 'dump':
        with open(sys.argv[2], 'rb') as f:
            print read_header(f)
            f.seek(0)
            g = read_gff(f)
        f = StringIO()
        write_gff(f, g)
        f.seek(0)
        print read_header(f)
        f.seek(0)
        if len(sys.argv) > 3:
            with open(sys.argv[3], 'wb') as o:
                o.write(f.read())
            f.seek(0)
        g = read_gff(f)
        pprint(g)
