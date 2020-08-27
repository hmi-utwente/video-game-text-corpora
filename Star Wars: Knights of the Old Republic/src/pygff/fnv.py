import array

def fnv32(s):
    if not isinstance(s, str) and not (isinstance(s, array.array) and s.typecode == 'c'):
        raise TypeError, ('Not a str', type(s))
    hash = 2166136261
    for c in s:
        hash = ((hash * 16777619) & 0xFFFFFFFF) ^ ord(c)
    return hash

def fnv64(s):
    if not isinstance(s, str) and not (isinstance(s, array.array) and s.typecode == 'c'):
        raise TypeError, ('Not a str', type(s))
    hash = 14695981039346656037
    for c in s:
        hash = ((hash * 1099511628211) & 0xFFFFFFFFFFFFFFFF) ^ ord(c)
    return hash