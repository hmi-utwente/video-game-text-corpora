from erf import ERF1File, ERF2File, ERF3File
from optparse import OptionParser
from ioutils import copyio
import os, sys

parser = OptionParser(usage="%prog [options] <ERF> <RESOURCE> <DESTINATION>",
    description="ERF is the ERF to extract the resource from."
    " RESOURCE is the resource's filename."
    " DESTINATION is the full path including filename to extract to.",
    version='%prog 1.0')
parser.add_option("-p", "--password", help="use PASSWORD to decrypt resources", metavar="PASSWORD")
parser.add_option("--filename", help="interpret RESOURCE to be a filename of a resource [default]", dest='search_mode', action='store_const', const=0, default=0)
parser.add_option("--offset", help="interpret RESOURCE to be an offset of a resource", dest='search_mode', action='store_const', const=1)
parser.add_option("--namehash", help="interpret RESOURCE to be a FNV64 hash of a resource's filename", dest='search_mode', action='store_const', const=2)
(options, args) = parser.parse_args()

erfpath, resource, destination = args[:3]

if not os.path.exists(erfpath):
    print >>sys.stderr, 'ERF file not found'
    sys.exit(-1)

if options.search_mode in (1, 2):
    try:
        resource = long(resource, 0)
    except ValueError:
        print >>sys.stderr, 'Uninterpretable RESOURCE'
        sys.exit(-4)
else:
    resource = resource.lower()

with open(erfpath, 'rb') as f:
    sample = f.read(16)

if ERF3File.checksample(sample):
    erf = ERF3File(erfpath)
    if options.password:
        erf.password = options.password
    if options.search_mode == 0:
        lookup = erf._byname
    elif options.search_mode == 1:
        lookup = erf._byoffset
    elif options.search_mode == 2:
        lookup = erf._byfnv
elif ERF2File.checksample(sample):
    erf = ERF2File(erfpath)
    if options.password:
        erf.password = options.password
    if options.search_mode == 0:
        lookup = erf._byname
    elif options.search_mode == 2:
        lookup = erf._byoffset
    else:
        print >>sys.stderr, 'Unsupported search mode'
        sys.exit(-5)
elif ERF1File.checksample(sample):
    erf = ERF1File(erfpath)
    if options.search_mode == 0:
        lookup = erf._toc
    elif options.search_mode == 2:
        lookup = erf._byoffset
    else:
        print >>sys.stderr, 'Unsupported search mode'
        sys.exit(-5)
else:
    print >>sys.stderr, 'Not recognized as an ERF file'
    sys.exit(-2)

try:
    item = lookup[resource]
except:
    print >>sys.stderr, 'Resource not found'
    sys.exit(-7)

try:
    f = erf.open(item)
except:
    print >>sys.stderr, 'Failed to open resource'
    sys.exit(-8)

try:
    out = open(destination, 'wb')
except:
    print >>sys.stderr, 'Failed to open destination'
    sys.exit(-3)

try:
    copyio(out, f)
except:
    f.close()
    os.unlink(destination)
    print >>sys.stderr, 'Failure during extraction'
    sys.exit(-6)

f.close()
    
print 'Successful extraction'