import sqlite3, struct, os
from fnv import *

_qstruct = struct.Struct('Q')
_istruct = struct.Struct('I')

def _optcache():
    if os.path.exists('fnvhashes.sqlite'):
        return _getcache()
    return None

def _getcache():
    cache = sqlite3.connect('fnvhashes.sqlite')
    cache.execute('CREATE TABLE IF NOT EXISTS types (hash BLOB UNIQUE, string TEXT UNIQUE COLLATE NOCASE);')
    cache.execute('CREATE TABLE IF NOT EXISTS files (hash BLOB UNIQUE, string TEXT UNIQUE COLLATE NOCASE);')
    return cache

def lookupfile(hash):
    cache = _optcache()
    if cache is not None:
        for row in cache.execute('SELECT string FROM files WHERE hash = ?;', (buffer(_qstruct.pack(hash)),)):
            return row[0]
    return None

def lookuptype(hash):
    cache = _optcache()
    if cache is not None:
        for row in cache.execute('SELECT string FROM types WHERE hash = ?;', (buffer(_istruct.pack(hash)),)):
            return row[0]
    return None

def addfiles(ss):
    cache = _getcache()
    cache.executemany('INSERT OR IGNORE INTO files (hash, string) VALUES (?, ?);',
        ((buffer(_qstruct.pack(fnv64(s.lower()))), s) for s in ss))
    cache.commit()

def addtypes(ss):
    cache = _getcache()
    cache.executemany('INSERT OR IGNORE INTO types (hash, string) VALUES (?, ?);',
        ((buffer(_istruct.pack(fnv32(s.lower()))), s) for s in ss))
    cache.commit()

def dumpfiles(f):
    cache = _optcache()
    count = 0
    if cache is not None:
        for row in cache.execute("SELECT string FROM files ORDER BY string ASC;"):
            print >>f, row[0]
            count += 1
    return count

def dumptypes(f):
    cache = _optcache()
    count = 0
    if cache is not None:
        for row in cache.execute("SELECT string FROM types ORDER BY string ASC;"):
            print >>f, row[0]
            count += 1
    return count

def scan_directory(path=''):
    cache = _getcache()
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.typelist'):
                print filename
                with open(os.path.join(dirpath, filename), 'r') as f:
                    addtypes(s.strip() for s in f)
            elif filename.endswith('.filelist'):
                print filename
                with open(os.path.join(dirpath, filename), 'r') as f:
                    addfiles(s.strip() for s in f)
    cache.execute('VACUUM;')

if __name__ == '__main__':
    scan_directory()