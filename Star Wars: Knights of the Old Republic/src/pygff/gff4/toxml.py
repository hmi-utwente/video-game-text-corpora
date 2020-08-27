
if __name__ == '__main__':
    import sys
    from gff4.reader import GFF4Reader2
    from gff4.types import TYPES_BY_ID
    from gff4.datoolset_fields import get_field_name
    from withsax import WithXMLGenerator
    from itertools import izip, count
    from base64 import b64encode, encodestring
    
    if sys.argv[1] == 'toxml':
        if len(sys.argv) < 3:
            print 'python -m gff4.xml toxml GFF [XML]'
            sys.exit(-1)
        if len(sys.argv) == 3:
            gff_file = sys.argv[2]
            xml_file = gff_file+'.xml'
        else:
            gff_file = sys.argv[2]
            xml_file = sys.argv[3]
        
        def xml_header(xml, header):
            with xml.element('Header', file_type=header.file_type, file_version=header.file_version, platform=header.platform):
                for i, struct in izip(count(), header.structs):
                    with xml.element('HeaderStructure', type=str(i), label=struct.type, size=str(struct.size)):
                        for field in struct.fields:
                            attrs = {'label': str(field.label), 'type': str(field.type), 'offset': str(field.offset)}
                            labelalias = get_field_name(field.label)
                            if labelalias != field.label: attrs['alias'] = labelalias
                            if field.is_reference: attrs['reference'] = 'true'
                            if field.is_struct: attrs['struct'] = 'true'
                            if field.is_list: attrs['list'] = 'true'
                            xml.startEndElement('HeaderField', **attrs)
        
        def xml_field(xml, id, field, value):
            if field.is_list:
                xml_list(xml, id, field, value)
            elif field.is_reference:
                xml_reference(xml, id, field, value)
            elif field.is_struct:
                xml_struct(xml, value, id, field.type, field.label)
            else:
                xml_primitive(xml, value, id, field.type, field.label)
        
        def xml_primitive(xml, value, id, type, label):
            type = TYPES_BY_ID[type]
            if type.id == 14:
                value = value[:-1]
            #elif type.id == 17:
            #    value = str(value[0])
            elif isinstance(value, tuple):
                value = ', '.join(str(e) for e in value)
            else:
                value = str(value)
            attrs = dict(id=str(id), value=value)
            if label: attrs['label'] = str(label)
            xml.startEndElement(type.name.lower(), **attrs)
        
        def xml_reference(xml, id, field, value):
            if field.is_struct or field.type != 0xFFFF:
                if value is None:
                    attrs = {'type': str(field.type)}
                    if field.label: attrs['label'] = str(field.label)
                    if field.is_struct: attrs['struct'] = 'true'
                    if field.is_list: attrs['list'] = 'true'
                    xml.startEndElement('reference', **attrs)
                #elif value[0] <= id:
                #    xml.startEndElement('reference', label=str(field.label), address=str(value[0]))
                else:
                    attrs = {'address': str(value[0])}
                    if field.label: attrs['label'] = str(field.label)
                    with xml.element('reference', **attrs):
                        xml_field(xml, value[0], value[1], value[2]())
            else:
                raise ValueError, ("Cannot serialize a generic", id, field, value)
                #xml_field(xml, *value())
        
        def xml_list(xml, id, field, values):
            if field.is_reference:
                if field.is_struct or field.type != 0xFFFF:
                    with xml.element('references', id=str(id), type=str(field.type), label=str(field.label)):
                        #raise ValueError, ("Cannot serialize references", id, field, values, values.next())
                        for address, field, ref in values:
                            print field
                            xml_reference(xml, address, field, ref)
                else:
                    with xml.element('generics', id=str(id), label=str(field.label)):
                        for address, field, generic in values:
                            xml_field(xml, generic[0], generic[1], generic[2]())
            elif field.is_struct:
                with xml.element('structs', id=str(id), type=str(field.type), label=str(field.label)):
                    for address, field, struct in values:
                        xml_struct(xml, struct, address, field.type, field.label)
            elif field.type == 0:
                with xml.element('binary', id=str(id), label=str(field.label)):
                    xml.characters(encodestring(values))
            else:
                with xml.element('list', id=str(id), type=str(field.type), label=str(field.label)):
                    for address, field, value in values:
                        xml_primitive(xml, value, address, field.type, field.label)
        
        def xml_struct(xml, struct, id=0, type=0, label=0):
            attrs = dict(id=str(id), type=str(type))
            if label:
                attrs['label'] = str(label)
            with xml.element('struct', **attrs):
                for address, field, value in struct:
                    xml_field(xml, address, field, value)
        
        with open(gff_file, 'rb') as f:
            gff = GFF4Reader2(f)
            with open(xml_file, 'wb') as o:
                xml = WithXMLGenerator(o, 'utf-8')
                with xml.document():
                    with xml.element('GFF'):
                        xml_header(xml, gff.header)
                        xml_struct(xml, gff)