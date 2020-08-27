from gff4 import *
from gff4.datoolset_fields import get_field_name
from yaml import MappingStartEvent as MSE, MappingEndEvent as MEE, SequenceStartEvent, SequenceEndEvent as SEE, ScalarEvent
from base64 import b64encode, encodestring
import yaml

def generate_aliases(ids):
    aliases = dict()
    if len(ids) > 1:
        labels = [(id, get_field_name(id)) for id in ids]
        labels = [(id, label.split('_')) for id, label in labels if id != label]
        if labels:
            minlen = min(len(label) for i, label in labels)
            while minlen > 1:
                s = None
                common = True
                for id, label in labels:
                    if s is None:
                        s = label[0]
                    elif s != label[0]:
                        common = False
                        break
                if common:
                    labels = [(id, label[1:]) for id, label in labels]
                else:
                    break
                minlen -= 1
            for id, label in labels:
                aliases[id] = '_'.join(label)
    elif ids:
        alias = get_field_name(ids[0])
        if alias != ids[0]:
            aliases[ids[0]] = alias
    return aliases

def SE(anchor=None, tag=None, implicit=(True, True), value=None, start_mark=None, end_mark=None, style=None):
    return ScalarEvent(anchor, tag, implicit, value, start_mark, end_mark, style)

def SSE(anchor=None, tag=None, implicit=True, start_mark=None, end_mark=None, flow_style=None):
    return SequenceStartEvent(anchor, tag, implicit, start_mark, end_mark, flow_style)

def gff2yamlevents(data, header, str_labels=False):    
    if str_labels:
        sfa = dict()
    
    yield yaml.StreamStartEvent(encoding='utf-8')
    yield yaml.DocumentStartEvent()
    yield MSE(anchor=None, tag=u'!Header', implicit=False, flow_style=False)
    yield SE(value=u'platform')
    yield SE(value=unicode(header.platform))
    yield SE(value=u'file_type')
    yield SE(value=unicode(header.file_type))
    yield SE(value=u'file_version')
    yield SE(value=unicode(header.file_version))
    yield SE(value=u'structs')
    yield SSE()
    for struct_i, struct in enumerate(header.structs):
        yield MSE(anchor=None, tag=u'!Structure', implicit=True, flow_style=False)
        yield SE(value='name')
        yield SE(value=struct.fourcc)
        yield SE(value='fields')
        yield SSE()
        fa = dict()
        if str_labels:
            fa = generate_aliases([field.label for field in struct.fields])
            sfa[struct_i] = fa
            
        for field in struct.fields:
            if isinstance(field, Field):
                yield MSE(anchor=None, tag=u'!Field', implicit=True, flow_style=True)
                yield SE(value='label')
                yield SE(value=unicode(field.label))
                if str_labels and field.label in fa:
                    yield SE(value='alias')
                    yield SE(value=fa[field.label])
                ftype = field.type
                indirect = field.indirect
                if issubclass(ftype, List):
                    yield SE(value='is_list')
                    yield SE(value='Yes')
                    indirect = ftype.indirect
                    ftype = ftype.elem_type
                if indirect:
                    yield SE(value='is_ref')
                    yield SE(value='Yes')
                if issubclass(ftype, Structure):
                    yield SE(value='is_struct')
                    yield SE(value='Yes')
                    yield SE(value='type')
                    yield SE(value=unicode(header.structs.index(ftype)))
                elif ftype is not None:
                    yield SE(value='type')
                    yield SE(value=unicode(ftype.id))
                yield MEE()
        yield SEE()
        yield MEE()
    yield SEE()
    yield MEE()
    yield yaml.DocumentEndEvent()
    
    def emit_value(value, vtype, indirect):
        if issubclass(vtype, List):
            return emit_list(value, vtype.elem_type, vtype.indirect)
        elif indirect:
            return emit_reference(value, vtype)
        elif issubclass(vtype, Structure):
            return emit_struct(value)
        elif value is None:
            return [SE(tag='!!null', value='')]
        else:
            return emit_primitive(value)
    def emit_primitive(value, implicit=True):
        tag = '!'+type(value).name
        if isinstance(value, tuple):
            yield SSE(tag=tag, implicit=implicit, flow_style=True)
            for v in value:
                if v is None:
                    yield SE(tag='!!null', value='')
                else:
                    yield SE(value=unicode(v))
            yield SEE()
        else:
            yield SE(tag=tag, value=unicode(value), implicit=(implicit, implicit))
    def emit_list(value, vtype, indirect):
        if value is not None:
            if indirect:
                yield SSE()
                if vtype is None:
                    for v in value:
                        if v is None:
                            yield SE(tag='!!null', value='')
                        elif isinstance(v, Structure):
                            for evt in emit_struct(v, False):
                                yield evt
                        else:
                            for evt in emit_primitive(v, False):
                                yield evt
                else:
                    for v in value:
                        if v is None:
                            yield SE(tag='!!null', value='')
                        else:
                            emit_value(v, vtype, True)
                yield SEE()
            elif issubclass(vtype, Structure):
                yield SSE()
                for v in value:
                    for evt in emit_struct(v):
                        yield evt
                yield SEE()
            elif isinstance(value, str):
                yield SE(tag='!binary', value=encodestring(value), style='|', implicit=(False, False))
            else:
                yield SSE()
                for v in value:
                    for evt in emit_primitive(v):
                        yield evt
                yield SEE()
        else:
            yield SE(tag='!!null', value='')
    def emit_struct(struct, implicit=True):
        def simplekind(field):
            return issubclass(field.type, (int, long, float))
        simple = all(simplekind(field) for field in struct.fields)
        yield MSE(anchor=None, tag='!'+struct.fourcc, implicit=implicit, flow_style=simple)
        if str_labels:
            fa = sfa[header.structs.index(type(struct))]
        for label in struct:
            if str_labels and label in fa:
                yield SE(value=fa[label])
            else:
                yield SE(value=unicode(label))
            field = struct.getfieldbylabel(label)
            #print type(struct), field
            for evt in emit_value(struct[label], field.type, field.indirect):
                yield evt
        yield MEE()
    def emit_reference(value, vtype):
        if vtype is None:
            if value is None:
                yield SE(tag='!!null', value='')
            elif isinstance(value, Structure):
                for evt in emit_struct(value, False):
                    yield evt
            else:
                for evt in emit_primitive(value, False):
                    yield evt
        else:
            if value is None:
                yield SE(tag='!!null', value='')
            else:
                for evt in emit_value(value, vtype, False):
                    yield evt
    yield yaml.DocumentStartEvent()
    for evt in emit_struct(data):
        yield evt
    yield yaml.DocumentEndEvent()
    
    yield yaml.StreamEndEvent()

def save_yaml(dest, data, header, str_labels=False):
    with open(dest, 'w') as f:
        yaml.emit(gff2yamlevents(data, header, str_labels), f)

if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'rb') as f:
        data, header = read_gff4(f)
        yaml.emit(gff2yamlevents(data, header, True), sys.stdout)
