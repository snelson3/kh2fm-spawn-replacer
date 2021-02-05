from kh2lib.kh2lib import kh2lib
import json, yaml, sys

CAMERA_START_OFFSET = 0x1C

class SpawnReplacer:
    def __init__(self, joker=True, debug=False, version="xeemo"):
        self.kh2lib = kh2lib(cheatsfn="F266B00B.pnach")
        self.locations = json.load(open("locations.json"))
        self.enemies = json.load(open("enemies.json"))
        self.debug = debug
        self.joker = joker
        self.version_offset = self.getVersionOffset(version)
    def getVersionOffset(self, version):
        if version in ["vanilla", "jp"]:
            return 0
        if version in ["xeemo"]:
            return 99 # TODO FILL IN WITH REAL NUMBER
        if version in ["crazycat"]:
            return 999 # TODO FILL IN WITH REAL NUMBER
        raise Exception("unknown version")
    def lookupLocation(self, description):
        for loc in self.locations:
            if loc["description"].lower() == description.lower():
                return loc
        raise Exception("Location not found: {}".format(description))
    def lookupEnemy(self, name):
        if name in self.enemies:
            return self.enemies[name]
        raise Exception("Enemy not found: {}".format(enemy))
    def dumpLocation(self, description):
        location = self.lookupLocation(description)
        output = {
            "description": description,
            "disableCamera": False,
            "enemies": [e['name'] for e in location['enemies'] ]
        }
        yaml.dump(output, open(description.replace("/","_").replace(' ', '_').replace(':', '').lower()+'.yaml', "w"))
    def readLocation(self, fn):
        return yaml.load(open(fn), Loader=yaml.FullLoader)
    def checkLocation(self, location):
        description = location["description"]
        location_details = self.lookupLocation(description)
        old_len = len(location_details["enemies"])
        new_len = len(location["enemies"])
        if old_len != new_len:
            raise Exception("File contained {} enemies, needs {}!".format(new_len, old_len))
        old_size = location_details["size_inc_enemies"]
        new_size = location_details["size"]
        for enemy in location["enemies"]:
            new_size += self.lookupEnemy(enemy)["size"]
        usage_percent = int(new_size / old_size * 100)
        if new_size > old_size:
            print("Warning: New memory use ({}) is {}% of old memory use, requires testing to see if the game can handle it".format(new_size,usage_percent))
        return location
    def replaceEnemy(self, new_enemy, location, spawn):
        addr = spawn["value"]
        ucm = new_enemy["ucm"]
        aiparam = '01' if new_enemy["aiparam"] == '1' else '00'
        
        modelcode = '{} 00{}{}'.format(addr.upper(), aiparam, ucm.upper())
        aiaddr = hex(int(addr, 16)+32)[2:].upper().zfill(8)
        aiparamcode = '{} 000000{}'.format(aiaddr, aiparam)
        codes = [modelcode, aiparamcode]
        return codes
    def replaceLocation(self, location):
        disableCamera = "disableCamera" in location and location["disableCamera"]
            
        location_details = self.lookupLocation(location["description"])
        replacements = []
        comment = "Location: {}".format(location["description"])
        for e in range(len(location["enemies"])):
            new = self.lookupEnemy(location["enemies"][e])
            spawn = location_details["enemies"][e]
            if spawn["name"] == new["name"]:
                continue # This spawn is not changing, no code needed
            comment += "\n// Replacing {}) {} with {}".format(e,spawn["name"], new["name"])
            replacement = self.replaceEnemy(new, location, spawn)
            replacements = replacements + replacement
        codes = replacements
        if disableCamera:
            if not "msn_offset" in location_details:
                raise Exception("MSN Offset needed") 
            comment += "\n// Disabling intro camera"
            offset_dec = int(location_details["msn_offset"],16) + self.version_offset + CAMERA_START_OFFSET # Verify this is correct
            offset = hex(offset_dec)[2:].upper().zfill(8)
            value = "00000000" # I think this is fine but double check
            codes += ["{} {}".format(offset, value)]
        if self.joker:
            codes = self.kh2lib.cheatengine.apply_room_joker(self.kh2lib.cheatengine.apply_event_joker(replacements, location_details["event"]), location_details["world"], location_details["room"])
        else:
            codes = replacements
        self.kh2lib.cheatengine.apply_ram_code(codes, comment=comment)
        self.kh2lib.cheatengine.write_pnach(debug=self.debug)
    def performReplacement(self, loc=None, description=None, enemylist=None, disableCamera=False):
        if not loc:
            if not enemylist:
                raise Exception("No enemies listed for replacement!")
            loc = {"description":description, "enemies": enemylist, "disableCamera": disableCamera}
        self.replaceLocation(self.checkLocation(loc))
    def replaceBoss(self, old_boss, new_boss, description=None, disableCamera=False, scaleHP=False, applyFixes=True, teleportJoker=False):
        loc = {
            "description": description or "{} Fight".format(old_boss),
            "disableCamera": disableCamera,
            "scaleHP": scaleHP,
            "applyFixes": applyFixes,
            "teleportJoker": teleportJoker,
            "enemies": [new_boss]
        }
        self.performReplacement(loc)
