from kh2lib.kh2lib import kh2lib
import json, yaml, sys

class SpawnReplacer:
    def __init__(self):
        self.kh2lib = kh2lib(cheatsfn="F266B00B.pnach")
        self.locations = json.load(open("locations.json"))
        self.enemies = json.load(open("enemies.json"))
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
            "enemies": [e['enemy']['name'] for e in location['enemies'] ]
        }
        yaml.dump(output, open(description.replace(' ', '_').lower()+'.yaml', "w"))
    def readLocation(self, fn):
        return yaml.load(open(fn), Loader=yaml.FullLoader)
    def checkLocation(self, location):
        description = location["description"]
        old_location = self.lookupLocation(description)
        old_len = len(old_location["enemies"])
        new_len = len(location["enemies"])
        if old_len != new_len:
            raise Exception("File contained {} enemies, needs {}!".format(new_len, old_len))
        old_size = old_location["size_inc_enemies"]
        new_size = old_location["size"]
        for enemy in location["enemies"]:
            new_size += self.lookupEnemy(enemy)["size"]
        usage_percent = int(new_size / old_size * 100)
        if new_size > old_size:
            print("Warning: New memory use ({}) is {}% of old memory use, requires testing to see if the game can handle it".format(new_size,usage_percent))
        return location
    def replaceLocation(self, location):
        old_location = self.lookupLocation(location["description"])
        replacements = []
        comment = "Location: {}".format(location["description"])
        for e in range(len(location["enemies"])):
            new = self.lookupEnemy(location["enemies"][e])
            spawn = old_location["enemies"][e]
            if spawn["enemy"]["name"] == new["name"]:
                continue # This spawn is not changing, no code needed
            addr = spawn["value"]
            ucm = new["ucm"]
            aiparam = '01' if new["aiparam"] == '1' else '00' 
            comment += "\n// Replacing {} with {}".format(spawn["enemy"]["name"], new["name"])
            modelcode = '{} 00{}{}'.format(addr.upper(), aiparam, ucm.upper())
            aiaddr = hex(int(addr, 16)+32)[2:].upper().zfill(8)
            aiparamcode = '{} 000000{}'.format(aiaddr, aiparam)
            replacements.append(modelcode)
            replacements.append(aiparamcode)
            codes = self.kh2lib.cheatengine.apply_event_joker(self.kh2lib.cheatengine.apply_room_joker(replacements, old_location["world"], old_location["room"]), old_location["event"])
            self.kh2lib.cheatengine.apply_ram_code(codes, comment=comment)
            self.kh2lib.cheatengine.write_pnach(debug=True)

if __name__ == '__main__':
    sr = SpawnReplacer()
    if sys.argv[1] == 'replace':
        sr.replaceLocation(sr.checkLocation(sr.readLocation(sys.argv[2])))
    if sys.argv[1] == 'write':
        sr.dumpLocation(sys.argv[2])