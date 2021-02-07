# kh2-spawn-replacer
 
This script provides an easy to understand interface for creating codes that replace enemies/bosses in various rooms of KH2FM

The data is in two files (locations and enemies). They are somewhat complete, but pull requests with additional data is always welcome

The expected usage is to use "python replacer.py write <description>" to dump a yaml file listing the enemies in the room (lookup the room you want in locations.json and use that description). Then edit the names of the enemies you want replaced (lookup the names in enemies.json), making sure to keep the same number of enemies in the list. Then run "python replacer.py replace <filename>" which will create a pnach file (by default the location is ./F266B00B.pnach but you can use a custom path with the environment variable `USE_KH2_PATCHENGINEDIR` )

If you find any issues with the script, please open an issue. Pull requests for bug fixes/new features are also welcome!

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


For reference, here is a list of all the objects that the spawn replacer supports replacing, sorted by memory usage (estimated, though it seems to be fairly accurate)


```
552 Invisible Target
6980 Nothing
10952 Lingering Will's Ultima Cannon Shot
41084 Bees
73460 Rapid Thruster AL
77342 Tiny Pyramid Dummy
78392 Gargoyle Knight
79594 Gargoyle Warrior
84720 Card Sora
87118 Nobody from Final Battle v1
97616 Dice Sora
102818 Zexions Book
104980 Oogie Box Dummy
109420 Emerald Blues NM
113602 Roxas Oblivion Keyblade
114002 Roxas Oathkeeper Keyblade
122640 Fiery Globe
134096 Jafar Flying Wreckage
180522 Fiery Globe Volcano Lord
186364 Spring Metal
189784 Icy Cube
199256 Berserker Sword
207636 Fire Attack 
212176 Silver Rock
237820 Saix's Claymore  
238004 Data Saix Claymore
245100 Aeroplane WI
251012 Rapid Thruster
258308 Illuminator
272536 Barrel Dummy
279204 Lock Dummy
280926 Cannon Gun
285258 Crimson Jazz AL
290842 Crimson Jazz
292560 Hook Bat AL
296752 Hook Bat
298036 Beffudler
298980 Shock Dummy
337392 Bolt Tower
343104 Crescendo
352940 Runemaster
363704 Strafer
369292 Surveillance Robot
374008 Zexions Something
382620 Magnum Loader
398180 Luxord's Card
400712 Minute Bomb
400712 Minute Bomb WI
434622 Oogie Terminal Dummy
462904 Armored Knight
469358 Driller Mole
469870 Driller Mole NM
477686 Shadow
477686 Shadow WI
535724 Hammer Frame WI
537416 Iron Hammer
547096 Sniper
551572 Fat Bandit
554888 Wight Knight NM
557240 Data Xigbar
563598 Creeper
577800 Grey Triangle Dummy
599504 Lock  
602620 Nightwalker
603180 Aerial Viking
603320 Air Pirate
614828 Toy Soldier NM
616628 Graveyard NM
632600 Fortuneteller
669940 Bolt Tower DC
673368 Tornado Step
698584 Necromancer
698586 Oogie Gift Dummy
699684 Banzai
700580 Ed
732000 Fiery Globe Treasure Room
754672 Lance Soldier
755026 Riku
755432 Yuffie
755608 Lance Warrior
767918 The Experiment Right Hand
771246 The Experiment Head
772142 No. 11
787284 Soldier NM
787284 Soldier
788874 The Experiment Left Hand
791312 Samurai
791734 Hayner
797468 No. 8
799588 Shenzie
809722 No. 7
848210 Berserker
871428 Hot Rod WI
871788 Mad Ride
872152 Icy Cube Treasure Room
882418 Vivi
887908 Shadow Stalker
896764 Past Pete
929856 Hades I
933824 Sark  
939680 Seifer
941282 Devastator
951352 Dancer
961136 Large Body
968770 Pete TR
977672 Shock  
990288 Morning Star
1006700 Barrel  
1013040 Dusk
1017964 Jafar
1020248 Trick Ghost
1020248 Rapid Thruster WI
1020616 Magic Phantom
1022460 Pete Cups
1022804 Pete OC I
1022968 Pete OC II
1053854 Tifa
1150276 Armor Xemnas
1191968 Blizzard Lord
1196392 Scar
1209752 Dragoon
1276992 Hostile Program
1278612 Leon
1330656 Setzer
1342620 Demyx's Water Clone  
1342840 Data Demyx Water Clone
1404236 Assault Rider
1417332 Living Bone
1422564 Hades Escape
1426680 Thresholder
1436676 Luna Bandit
1499488 Grim Reaper I 
1499488 Grim Reaper II
1531924 Assassin
1541496 Sorcerer Doesnt Attack
1642502 Cloud
1657608 The Beast
1665404 Anti-Sora
1672788 Gambler
1720178 Volcano Lord
1741312 Sorcerer
1879368 Axel I 
1939060 Data Zexion
2006116 Storm Rider
2061008 Xigbar  
2132546 Demyx OC
2177276 Dark Thorn
2223500 Oogie Boogie
2280296 Hercules
2314684 Prison Keeper
2347708 Hades Cups
2351052 Hades II
2359752 Lexaeus  
2359752 Data Lexaeus
2415886 Zexion  
2417732 Hydra 
2485952 Sephiroth
2494584 Cerberus
2607408 Xemnas  
2607964 Data Xemnas
2631800 Shan-Yu
2644106 No. 4
2689964 Dragon Xemnas
2741104 Axel II
2741336 Xaldin  
2741808 Data Xaldin
2742180 Data Axel
2854684 Terra
3078386 Groundshaker
3175016 Barbossa
3252168 Marluxia  
3252168 Data Marluxia
3373592 Roxas  
3373592 Data Roxas
3429892 Luxord  
3430732 Data Luxord
3527072 Demyx
3528528 Data Demyx
3549978 The Experiment  
3557686 Saix  
3559034 Data Saix
3691716 Twilight Thorn
4213606 Shadow NM
4443212 Larxene
4443212 Data Larxene
4536360 Final Xemnas  
4538944 Data Final Xemnas
4708244 Vexen  
4708244 Data Vexen
```


Also, here is a list of the names of all the fights that can be replaced, sorted by memory usage (the memory usage doesn't include objects that are not replacable enemies, so it's not very accurate for places like Dark Thorn fight where the chandelier/etc objects likely take up a good chunk of memory)

```
2863574 The Expotition
2997056 Armor Xemnas II Boss Fight
3031644 Scar Boss Fight
3569712 Hostile Program Boss Fight
3685882 The World of Nothing (Cylinder Lasers) Fight
3725606 Hades Paradox Round 10
3726198 Lexaeus AS Fight
3726198 Lexaeus Data Fight
3753048 Armor Xemnas I Boss Fight
3863468 Storm Rider Boss Fight
3945332 Hades Chamber Boss Fight
4011032 Pete (Past) Boss Fight
4184526 Marluxia AS Fight
4184526 Marluxia Data Fight
4202626 Gambler (Ship Graveyard: Seadrift Keep; 1st Fight)
4244178 Hades Boss Phase II
4314254 Hades Paradox Round 25
4319428 Sark Boss Fight
4448568 Lingering Will Boss Fight
4478464 Grim Reaper I Boss Fight
4507606 Prison Keeper Boss Fight
4526214 Station of Serenity Nobodies
4575808 Axel II Boss Fight
4576884 Axel Data Fight
4590810 Dark Thorn Boss Fight
4705796 Pain/Panic Round 10
4762392 Present Collecting Fight
4837582 Xigbar Data Fight
4951984 Titan Round 10
5003784 Cerberus Boss Fight
5013802 Dusk (1st Fight with Keyblade)
5203738 Hades Cup - Semifinals
5207178 Roxas Data Fight
5207178 Roxas Boss Fight
5255622 Sephiroth Boss Fight
5277736 Imperial Square Heartless Fight (1st Visit)
5357840 Xaldin Boss Fight
5358312 Xaldin Data Fight
5488282 Experiment Boss Fight
5669894 Twin Lords Boss Fight
5738090 Elephant Graveyard Heartless
5746726 Larxene AS Fight
5751746 Thresholder Boss Fight
5825890 Pete II Boss Fight
5912778 Hades Cup - Round 1
6107158 Candy Cane Lane Heartless
6170846 Game Grid Heartless Fight
6341350 Xigbar Boss Fight
6661742 Vexen AS Fight
6661742 Vexen Data Fight
6742448 Chasm of Challenges Heartless
6915972 Back Alley Nobodies
6963680 Mushrooms
6969556 Saix Boss Fight
6970904 Saix Data Fight
7135020 The Interceptor Barrels
7159278 Between and Betwix Nobodies Fight 1
7190204 Sandlot (Struggle Tournament) Nobodies
7244708 Mission 3: The Search
7367032 Lilliput Heartless
7405642 The Tower Heartless
7416636 Imperial Square Heartless Fight (2nd Visit)
7540932 Encampment Heartless
7844804 I/O Tower Heartless Fight
7954832 Tower: Star Chamber Heartless
8377210 Tower: Moon Chamber Heartless
8778310 Sandswept Ruins Heartless Fight 1
8899228 Antechamber Nobodies Fight
8924502 Ballroom Nobodies Fight
9043516 Mansion: Basement Hall Nobodies
9204224 Sandswept Ruins Heartless Fight 2
9318026 Town Heartless
9604928 Cavern of Remembrance: Mineshaft Heartless Fight 2
9926528 Parlor Shadows
9956024 Borough Heartless Fight 1
10108770 Borough Nobodies Fight
10792832 Mission 1: The Surprise Attack
10820728 Building Site Heartless
11183722 Mission 2: The Ambush
11236956 Solar Sailer Heartless
11588878 Scene of the Fire Heartless
12519108 Entrance Hall Nobodies Fight
13750902 Sandlot Nobodies Fight
14158996 Hades' Chamber Nobodies Fight
14244818 Corridors Fight
14326472 Cavern of Remembrance: Mineshaft Heartless Fight 1
14332364 Shan-Yu Boss Fight
15213452 Hades Escape
15315438 Ravine Trail Heartless 1
16750534 Restoration Site Nobodies Fight
17417582 The Old Mansion Nobodies Fight
17679782 Mountain Trail Heartless
17975062 The World of Nothing (Energy Core) Fight
18279328 Mickey's House Heartless
18676640 Ravine Trail Heartless 3
20094450 Station Plaza Nobodies
21814304 Transport to Remembrance Nobodies Fight 2
22428502 Between and Betwix Nobodies Fight 2
23016898 Bailey Nobodies Fight
23073128 Ravine Trail Heartless 4
23797522 Escort Queen Minnie Part I
23898422 Village Cave Heartless
27658110 Ravine Trail Heartless 2
27963892 Transport to Remembrance Nobodies Fight 1
36797624 Agrabah Heartless
37226862 The Cave of Wonders: Treasure Room Heartless
40080790 Halloween Town Square Heartless
58631244 Transport to Remembrance Nobodies Fight 3
```

Finally, when replacing enemies you will need to set their spawn limiter so they all spawn. You can just paste this whole code as is, or you can just take the ones for the enemies you are using (the 05 at the end of each line is the value of the spawn limiter. The variable is 1 byte long).

```
patch=1,EE,11C9457C,extended,0B010104 // Luna Bandit have spawn limiter of 04
patch=1,EE,11C98B9C,extended,0B000104 // Shadow have spawn limiter of 04
patch=1,EE,11C9547C,extended,0B010104 // Icy Cube have spawn limiter of 04
patch=1,EE,11C9541C,extended,0B010104 // Fiery Globe have spawn limiter of 04
patch=1,EE,11C9415C,extended,0B010104 // Fat Bandit have spawn limiter of 04
patch=1,EE,11C9451C,extended,0B010104 // Fortuneteller have spawn limiter of 04
patch=1,EE,11C9523C,extended,0B010104 // Silver Rock have spawn limiter of 04
patch=1,EE,11CADB9C,extended,0B000104 // Icy Cube Treasure Room have spawn limiter of 04
patch=1,EE,11CADB3C,extended,0B000104 // Fiery Globe Treasure Room have spawn limiter of 04
patch=1,EE,11CB1D3C,extended,0B010104 // Rapid Thruster AL have spawn limiter of 04
patch=1,EE,11CB1C7C,extended,0B010104 // Hook Bat AL have spawn limiter of 04
patch=1,EE,11C98C5C,extended,0B010104 // Rapid Thruster have spawn limiter of 04
patch=1,EE,11CB1CDC,extended,0B010104 // Crimson Jazz AL have spawn limiter of 04
patch=1,EE,11C9427C,extended,0B010104 // Hook Bat have spawn limiter of 04
patch=1,EE,11C98DDC,extended,0B010004 // Dragoon have spawn limiter of 04
patch=1,EE,11C9919C,extended,0B010004 // Dusk have spawn limiter of 04
patch=1,EE,11CBD5BC,extended,0B010104 // Beffudler have spawn limiter of 04
patch=1,EE,11CBD55C,extended,0B010104 // Magic Phantom have spawn limiter of 04
patch=1,EE,11CBD85C,extended,0B010104 // Necromancer have spawn limiter of 04
patch=1,EE,11CBD61C,extended,0B010104 // Iron Hammer have spawn limiter of 04
patch=1,EE,11CBD67C,extended,0B010104 // Mad Ride have spawn limiter of 04
patch=1,EE,11CBD79C,extended,0B010104 // Lance Warrior have spawn limiter of 04
patch=1,EE,11CBD91C,extended,0B010104 // Aerial Viking have spawn limiter of 04
patch=1,EE,11CBD8BC,extended,0B010104 // Spring Metal have spawn limiter of 04
patch=1,EE,11CBD97C,extended,0B010104 // Runemaster have spawn limiter of 04
patch=1,EE,11C98E9C,extended,0B010004 // Samurai have spawn limiter of 04
patch=1,EE,11C98E3C,extended,0B010004 // Assassin have spawn limiter of 04
patch=1,EE,11C98EFC,extended,0B010004 // Sniper have spawn limiter of 04
patch=1,EE,11C98FBC,extended,0B020004 // Berserker have spawn limiter of 04
patch=1,EE,11C9901C,extended,0B010004 // Gambler have spawn limiter of 04
patch=1,EE,11C9913C,extended,0B010004 // Creeper have spawn limiter of 04
patch=1,EE,11C98F5C,extended,0B010004 // Dancer have spawn limiter of 04
patch=1,EE,11C990DC,extended,0B000004 // Sorcerer have spawn limiter of 04
patch=1,EE,11C9439C,extended,0B010104 // Minute Bomb have spawn limiter of 04
patch=1,EE,11CBAA9C,extended,0B000104 // Bolt Tower DC have spawn limiter of 04
patch=1,EE,11C9625C,extended,0B010104 // Wight Knight NM have spawn limiter of 04
patch=1,EE,11CB0F5C,extended,0B000104 // Shadow NM have spawn limiter of 04
patch=1,EE,11CB0E3C,extended,0B010104 // Soldier NM have spawn limiter of 04
patch=1,EE,11CB0C5C,extended,0B010104 // Driller Mole NM have spawn limiter of 04
patch=1,EE,11CAFD5C,extended,0B010104 // Toy Soldier NM have spawn limiter of 04
patch=1,EE,11CAFC9C,extended,0B010104 // Graveyard NM have spawn limiter of 04
patch=1,EE,11C98B3C,extended,0B010104 // Soldier have spawn limiter of 04
patch=1,EE,11C98CBC,extended,0B010104 // Armored Knight have spawn limiter of 04
patch=1,EE,11C952FC,extended,0B010104 // Crimson Jazz have spawn limiter of 04
patch=1,EE,11C9637C,extended,0B020104 // Morning Star have spawn limiter of 04
patch=1,EE,11C98D1C,extended,0B010104 // Surveillance Robot have spawn limiter of 04
patch=1,EE,11C944BC,extended,0B010104 // Nightwalker have spawn limiter of 04
patch=1,EE,11C9445C,extended,0B010104 // Assault Rider have spawn limiter of 04
patch=1,EE,11CABCDC,extended,0B010104 // Bolt Tower have spawn limiter of 04
patch=1,EE,11C9475C,extended,0B010104 // Lance Soldier have spawn limiter of 04
patch=1,EE,11C98BFC,extended,0B020104 // Large Body have spawn limiter of 04
patch=1,EE,11C941BC,extended,0B010104 // Trick Ghost have spawn limiter of 04
patch=1,EE,11C947BC,extended,0B010104 // Driller Mole have spawn limiter of 04
patch=1,EE,11C963DC,extended,0B010104 // Tornado Step have spawn limiter of 04
patch=1,EE,11C9643C,extended,0B010104 // Crescendo have spawn limiter of 04
patch=1,EE,11CABC1C,extended,0B000D04 // Bees have spawn limiter of 04
patch=1,EE,11C9463C,extended,0B010104 // Cannon Gun have spawn limiter of 04
patch=1,EE,11C9535C,extended,0B010104 // Air Pirate have spawn limiter of 04
patch=1,EE,11C9469C,extended,0B020104 // Living Bone have spawn limiter of 04
patch=1,EE,11C946FC,extended,0B010104 // Devastator have spawn limiter of 04
patch=1,EE,11C9631C,extended,0B010104 // Magnum Loader have spawn limiter of 04
patch=1,EE,11CB191C,extended,0B000104 // Strafer have spawn limiter of 04
patch=1,EE,11CB0B3C,extended,0B010104 // Hammer Frame WI have spawn limiter of 04
patch=1,EE,11CB0ADC,extended,0B010104 // Minute Bomb WI have spawn limiter of 04
patch=1,EE,11CB0A7C,extended,0B010104 // Aeroplane WI have spawn limiter of 04
patch=1,EE,11CB0EFC,extended,0B000104 // Shadow WI have spawn limiter of 04
patch=1,EE,11CB0B9C,extended,0B010104 // Hot Rod WI have spawn limiter of 04
patch=1,EE,11CB101C,extended,0B010104 // Rapid Thruster WI have spawn limiter of 04
```
