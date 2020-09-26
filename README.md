# kh2-spawn-replacer
 
This script provides an easy to understand interface for creating codes that replace enemies/bosses in various rooms of KH2FM

The data is in two files (locations and enemies). They are somewhat complete, but pull requests with additional data is always welcome

The expected usage is to use "python replacer.py write <description>" to dump a yaml file listing the enemies in the room (lookup the room you want in locations.json and use that description). Then edit the names of the enemies you want replaced (lookup the names in enemies.json), making sure to keep the same number of enemies in the list. Then run "python replacer.py replace <filename>" which will create a pnach file (by default the location is ./F266B00B.pnach but you can use a custom path with the environment variable `USE_KH2_PATCHENGINEDIR` )

# Usage tutorial

Lets say I want to edit the first forced fight in Agrabah. I would run the following command

`python replacer.py write "Agrabah Heartless"`

Which would dump out the following YAML file

```
description: Agrabah Heartless
enemies:
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Shadow
- Shadow
- Shadow
- Shadow
- Shadow
- Shadow
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
```

I want to replace one of the Shadows with Armor Xemnas, so I change the name in the yaml so it looks like below

```
description: Agrabah Heartless
enemies:
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Armor Xemnas
- Shadow
- Shadow
- Shadow
- Shadow
- Shadow
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
- Luna Bandit
```

Then I run 

`python replacer.py replace agrabah_heartless.yaml`

Which produces the following output (and the pnach file is output in my cheats directory of pcsx, due to my setting of the `USE_KH2_PATCHENGINEDIR` environment variable)

```
Warning: New memory use (37415510) is 101% of old memory use, requires testing to see if the game can handle it
// Location: Agrabah Heartless
// Replacing Shadow with Armor Xemnas

patch=1,EE,E0050039,extended,0032BAE4

patch=1,EE,E0040039,extended,0032BAE6

patch=1,EE,E0030039,extended,0032BAE8

patch=1,EE,E0020700,extended,0032BAEO

patch=1,EE,11C3BD84,extended,0000085C

patch=1,EE,11C3BDA4,extended,00000000
```