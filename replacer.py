from kh2replacer.SpawnReplacer import SpawnReplacer
import sys

joker = False if "nojoker" in sys.argv else True
debug = True if "debug" in sys.argv else False
sr = SpawnReplacer(joker=joker, debug=debug)
if sys.argv[1] == 'replace':
    loc = sr.readLocation(sys.argv[2])
    sr.performReplacement(loc=loc)
if sys.argv[1] == 'write':
    sr.dumpLocation(sys.argv[2])
