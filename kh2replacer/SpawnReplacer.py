from kh2lib.kh2lib import kh2lib
import json, yaml, sys, os

CAMERA_START_OFFSET = 0x1C
ENMP_START_OFFSET = 0x11d119ac # Technically in the memdump it's found with a 0 in the first digit, but the hp scaling doesn't always work that way
ENMP_HP_OFFSET = 0x4
ENMP_HEADER_LENGTH = 0x8
ENMP_ENTRY_LENGTH = 0x5C
class SpawnReplacer:
    def __init__(self, useCond=True, debug=False, version="xeey"):
        self.kh2lib = kh2lib(cheatsfn="F266B00B.pnach")
        self.locations = json.load(open("locations.json"))
        self.enemies = json.load(open("enemies.json"))
        self.debug = debug
        self.useCond = useCond
        self.version_offset = self.getVersionOffset(version)
    def getVersionOffset(self, version):
        # Only matters for mdlx hacks
        if version in ["vanilla", "jp"]:
            return 0
        if version in ["xeey", "xeeynamo"]:
            return 4096
        if version in ["crazycat"]:
            return 4096
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
            "scaleHP": False,
            "applyFixes": True,
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
    def replaceLocation(self, location, allow_same_spawn=True):
        disableCamera = "disableCamera" in location and location["disableCamera"]
        scaleHP = "scaleHP" in location and location["scaleHP"]
        location_details = self.lookupLocation(location["description"])
        applyFixes = "applyFixes" in location and location["applyFixes"]
        replacements = []
        comment = "Location: {}".format(location["description"])
        for e in range(len(location["enemies"])):
            new = self.lookupEnemy(location["enemies"][e])
            spawn = location_details["enemies"][e]
            old = self.lookupEnemy(spawn["name"])
            if not allow_same_spawn and spawn["name"] == new["name"]:
                continue # This spawn is not changing, no code needed
            comment += "\n// Replacing {}) {} with {}".format(e,spawn["name"], new["name"])
            replacement = self.replaceEnemy(new, location, spawn)
            replacements = replacements + replacement
            if scaleHP:
                comment += "\n  // Scaling {} HP to match location".format(new["name"])
                address = hex(ENMP_START_OFFSET + ENMP_HEADER_LENGTH + ENMP_HP_OFFSET + (ENMP_ENTRY_LENGTH * new["enmp"]))[2:].zfill(8)
                # hp gets converted to 2 bytes, where HP=b1+256*b2
                hp_byte1 = hex(old["hp"] % 256)[2:].zfill(2)
                hp_byte2 = hex((old["hp"] - int(hp_byte1,16)) // 256)[2:].zfill(2)
                hp = "{}{}".format(hp_byte2, hp_byte1)
                if "setHP" in location:
                    hp = hex(location["setHP"])[2:].zfill(4)
                # hp = hex(location["setHP"] if "setHP" in location else new["hp"])[2:].zfill(4)
                other_hp_bytes = new["hp_extra_bytes"] if "hp_extra_bytes" in new else '0000'
                value = "{}{}".format(other_hp_bytes, hp)
                replacements += ["{} {}".format(address, value)]
            if applyFixes:
                fixes_dir = os.path.join(__file__, "..","fixes", new["name"].lower().replace(" ", ""))
                ai_start_offset = int(location_details["mdlx_offset"],16) + self.version_offset + int(new["ai_start_offset"],16) 
                def _getRealAddress(line):
                    address, value = line.split(" ")[0], line.split(" ")[1]
                    address = hex(int(address, 16) + ai_start_offset)[2:].zfill(8)
                    address = "2" + address[1:]
                    return "{} {}".format(address, value)
                if os.path.isdir(fixes_dir):
                    for fn in os.listdir(fixes_dir):
                        # Fixes are normal ADDRESS VALUE format but ADDRESS is only the offset from the start of the AI file
                        fix = [_getRealAddress(l) for l in open(os.path.join(fixes_dir,fn)).read().split("\n") if l]
                        replacements = replacements + fix
                        comment += " // {}".format(fn)
        codes = replacements
        if disableCamera:
            if not "msn_offset" in location_details:
                raise Exception("MSN Offset needed") 
            comment += "\n// Disabling intro camera"
            offset_dec = int(location_details["msn_offset"],16) + CAMERA_START_OFFSET
            offset = hex(offset_dec)[2:].upper().zfill(8)
            value = "00000000" # I think this is fine but double check
            codes += ["{} {}".format(offset, value)]
        if "extraCodes" in location and len(location["extraCodes"]) >0:
            codes += location["extraCodes"]
        if self.useCond:
            codes = self.kh2lib.cheatengine.apply_room_cond(self.kh2lib.cheatengine.apply_event_cond(replacements, location_details["event"]),  location_details["room"], location_details["world"])
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
    def replaceBoss(self, old_boss, new_boss, description=None, disableCamera=False, scaleHP=False, applyFixes=True, teleportJoker=False, extraCodes = []):
        loc = {
            "description": description or "{} Fight".format(old_boss),
            "disableCamera": disableCamera,
            "scaleHP": scaleHP,
            "applyFixes": applyFixes,
            "teleportJoker": teleportJoker,
            "enemies": [new_boss] if type(new_boss) == str else new_boss, # assuming str or array type
            "extraCodes": extraCodes
        }
        self.performReplacement(loc)
