from kh2replacer.SpawnReplacer import SpawnReplacer
import sys

useCond = False if "nocond" in sys.argv else True
debug = True if "debug" in sys.argv else False
version = "vanilla" if "vanilla" in sys.argv else "xeey"
sr = SpawnReplacer(useCond=useCond, debug=debug, version=version)
if sys.argv[1] == 'replace':
    loc = sr.readLocation(sys.argv[2])
    sr.performReplacement(loc=loc)
if sys.argv[1] == 'write':
    sr.dumpLocation(sys.argv[2])
