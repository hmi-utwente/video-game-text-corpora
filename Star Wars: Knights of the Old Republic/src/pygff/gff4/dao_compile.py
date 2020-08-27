from distutils.core import setup
import py2exe

setup(windows=['daosavegame.py'], options = { "py2exe":{'includes': 'types', "dll_excludes":["MSVCP90.dll"]}})