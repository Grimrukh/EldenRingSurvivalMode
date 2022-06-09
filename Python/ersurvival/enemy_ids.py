
from survival_goods import Materials

ENEMY_MODEL_IDS = {
    # 0000: "Human NPC/Player",
    # 2010: "Blaidd",
    # 2030: "Rennala",
    # 2031: "Rennala",
    # 2040: "Rennala Student",
    # 2041: "Rennala Student",
    # 2050: "Ranni",
    # 2060: "The Two Fingers",
    # 2070: "The Three Fingers",
    # 2100: "Black Knife Assassin/Alecto, Black Knife Ringleader",
    # 2110: "Beast Clergyman/Maliketh",
    # 2120: "Malenia, Blade of Miquella",
    # 2130: "Morgott/Margit",
    # 2131: "Morgott (Defeated)",
    # 2140: "Fell Twins",
    # 2150: "Wisp",
    # 2160: "Finger Reader Crone",
    # 2170: "Finger Reader Enia",
    # 2180: "Melina",
    # 2190: "Radagon",
    # 2200: "Elden Beast",
    # 2270: "Large Crab",
    # 2271: "Small Crab",
    # 2272: "Large Crab",
    # 2273: "Small Crab",
    # 2274: "Small Crab",
    # 2275: "Small Crab",
    # 2276: "Small Crab",
    # 2277: "Small Crab",
    2500: "Crucible Knight",  # rare Erdtree Amber
    3000: "Exile Soldier",  # uncommon Soft Wood
    3010: "Banished Knight",  # uncommon Metal Shards
    3020: "Large Exile Soldier",  # uncommon Soft Wood
    # 3050: "Sol Knight",
    # 3060: "Undead Mariner",
    3061: "Undead Azula Beastman",  # rare Gruesome Bone
    3070: "Dominula Celebrant",  # rare Soft Wood
    # 3080: "Imp",
    # 3100: "Bell Bearing Hunter / Elemer of the Briar",
    3150: "Night's Calvary",  # guaranteed Black Mark
    # 3160: "Night's Calvary Horse",
    # 3170: "Albinauric Archer",
    # 3171: "Albinauric Archer",
    # 3180: "Wolf",
    # 3181: "Red Wolf of Radagon",
    # 3200: "Nomad Trader",
    # 3201: "Nomad Trader",
    # 3210: "Nomad Mule",
    # 3250: "Draconic Tree Sentinel",
    # 3251: "Tree Sentinel",
    # 3252: "Royal Knight Loretta",
    # 3300: "Nox Swordstress/Nox Priest",
    3320: "Silver Tear",  # very rare Pliable Metal
    3330: "Silver Tear Orb",  # rare Pliable Metal
    3350: "Crystalian",  # rare Glintstone Dust
    3360: "Ancestral Follower",  # uncommon Soft Wood
    3361: "Ancestral Follower",  # uncommon Soft Wood
    3370: "Ancestral Follower Shaman",  # rare Refined Wood
    3371: "Ancestral Follower Shaman",  # rare Refined Wood
    3400: "Grave Warden Duelist",  # uncommon Metal Shards
    3450: "Misbegotten",  # uncommon Metal Shards
    # 3451: "Misbegotten / Hewg",
    3460: "Leonine Misbegotten",  # common Metal Shards
    # 3470: "Albinauric",
    # 3471: "Albinauric",
    3500: "Skeleton (Curved Sword)",
    3510: "Skeleton (Scimitar)",
    # 3550: "Sanguine Noble",
    # 3560: "Godskin Apostle",
    # 3570: "Godskin Noble",
    # 3600: "Onyx/Alabaster Lord",
    3610: "Oracle Envoy (Small)",  # very rare Erdtree Wood
    3620: "Oracle Envoy (Medium)",  # rare Erdtree Wood
    3630: "Oracle Envoy (Large)",  # uncommon Erdtree Wood
    3650: "Erdtree Guardian",  # rare Refined Wood
    # 3660: "Commoner",
    # 3661: "Putrid Corpse",
    # 3662: "Putrid Corpse",
    # 3664: "Cemetery Shade",
    # 3665: "Devious Commoner",
    # 3666: "Sunflower Commoner",
    # 3670: "Albinauric Lookout",
    # 3700: "Perfumer Tricia",
    # 3701: "Depraved Perfumer",
    # 3702: "Raya Lucaria Scholar",
    # 3703: "Noble's Page",
    # 3704: "Battle Mage Hughes",
    # 3710: "Crystallized Battlemage",
    # 3720: "Orbhead Sorcerer",
    # 3730: "Arcane Sphere of Faces",
    # 3750: "Clayman",
    3800: "Cleanrot Knight",  # uncommon Metal Shards
    3810: "Kindred of Rot",  # very rare Gruesome Bone
    3850: "Marionette",  # rare String
    3860: "Avionette",  # rare String
    # 3900: "Fire Monk",
    # 3901: "Godskin Monk",
    3910: "Fire Prelate",  # rare Metal Plate
    3950: "Man-Serpent",  # rare Metal Shards
    3970: "Beastman of Farum Azula",  # very rare Dragon Teeth
    # 4000: "Royal Rider",
    4020: "Royal Revenant",  # uncommon Soft Wood
    # 4040: "Sewer Slug",
    4050: "Kaiden Sellsword",  # uncommon Soft Wood
    # 4060: "Kaiden Sellsword Horse",
    # 4070: "Wolf",
    # 4071: "Wolf",
    # 4080: "Rat",
    # 4090: "Giant Rat",
    # 4100: "Demi-Human",
    # 4101: "Large Demi-Human",
    # 4110: "Demi-Human Shaman",
    4120: "Demi-Human Chief",  # common Soft Wood
    # 4130: "Demi-Human Queen",
    # 4140: "Spirit Caller Snail",
    # 4150: "Basilisk",
    # 4160: "Larger Dog",
    # 4161: "Larger Dog",
    # 4162: "Starved Dog",
    # 4163: "Starved Dog",
    # 4164: "Larger Dog With Less Hair",
    # 4165: "Larger Dog With Less Hair",
    # 4166: "Starved Dog",
    # 4167: "Starved Dog",
    # 4170: "Living Mass",
    # 4171: "Living Mass",
    # 4180: "Spirit Jellyfish",
    # 4190: "Scarab",
    # 4191: "Scarab",
    # 4192: "Scarab",
    # 4200: "Giant Bat",
    # 4201: "Chanting Winged Dame",
    # 4210: "Bladed Talon Eagle",
    # 4220: "Giant Octopus",
    # 4230: "Octopus",
    # 4240: "Fingercreeper/Spider Hand",
    # 4241: "Large Fingercreeper/Spider Hand",
    # 4250: "Lesser Fingercreeper/Spider Hand",
    4260: "Erdtree Burial Watchdog",  # common Stone Fragment
    # 4270: "Lion Guardian",
    # 4280: "Giant Ant",
    # 4281: "Giant Ant - Sac",
    # 4290: "Bloodhound Knight",
    # 4300: "Wandering Noble",
    4310: "Soldier",  # uncommon Soft Wood
    4311: "Godrick Soldier",  # uncommon Soft Wood
    4312: "Raya Lucaria Soldier",  # uncommon Soft Wood
    4313: "Leyndell Soldier",  # uncommon Soft Wood
    4314: "Radahn Soldier",  # uncommon Soft Wood
    4315: "Mausoleum Soldier",  # uncommon Soft Wood
    4316: "Haligtree Soldier",  # uncommon Soft Wood
    4320: "Vulgar Militia",  # uncommon Metal Shards
    4321: "Vulgar Militia",  # uncommon Metal Shards
    4340: "Mad Pumpkin Head",  # uncommon Metal Shards
    # 4341: "Lesser Pumpkin Head",
    4350: "Castle Knight",  # uncommon Metal Shards
    4351: "Godrick Knight",  # uncommon Metal Shards
    4352: "Cuckoo Knight",  # uncommon Metal Shards
    4353: "Leyndell Knight",  # uncommon Metal Shards
    4354: "Redmane Knight",  # uncommon Metal Shards
    4355: "Mausoleum Knight",  # uncommon Metal Shards
    4356: "Haligtree Knight",  # uncommon Metal Shards
    # 4360: "Knight's Horse",
    # 4361: "Godrick Knight's Horse",
    # 4362: "Cuckoo Knight's Horse",
    # 4363: "Leyndell Knight's Horse",
    # 4364: "Redmane Knight's Horse",
    # 4365: "Mausoleum Knight's Horse",
    # 4366: "Haligtree Knight's Horse",
    4370: "Foot Soldier",  # rare Soft Wood
    4371: "Godrick Foot Soldier",  # rare Soft Wood
    4372: "Raya Lucaria Foot Soldier",  # rare Soft Wood
    4373: "Leyndell Foot Soldier",  # rare Soft Wood
    4374: "Radahn Foot Soldier",  # rare Soft Wood
    4375: "Mausoleum Foot Soldier",  # rare Soft Wood
    4376: "Haligtree Foot Soldier",  # rare Soft Wood
    # 4377: "Highwayman",
    4380: "Starcaller",  # very rare Meteorite Chunk
    # 4381: "Bloodthorn Exile",
    4382: "Tunnel Miner",  # very rare Stone Fragment
    4383: "Glintstone Miner",  # very rare Somber Stone Fragment
    4384: "Glintstone Miner",  # very rare Somber Stone Fragment
    # 4385: "Fungal Sorcerer",
    # 4420: "Giant Lobster",
    # 4430: "Abnormal Stone Cluster",
    # 4440: "Fungal Pod",
    # 4441: "Giant Fungal Pod",
    # 4442: "Giant Rotten Pod",
    # 4450: "Walking Mausoleum",
    # 4460: "Maneuverable Flamethrower",
    4470: "Abductor Virgin",  # rare Metal Plate
    # 4480: "Miranda the Blighted Bloom/Blossom",
    # 4481: "Miranda Sprout",
    # 4482: "Giant Miranda Sprout",
    # 4483: "Miranda Sprout",
    # 4490: "Living Pot",
    # 4491: "Living Pot",
    # 4492: "Living Pot",
    # 4500: "Flying Dragon Agheel/Greyll",
    # 4501: "Flying Dragon Agheel/Greyll",
    # 4502: "Glintstone Dragon Smarag/Adula",
    # 4503: "Borealis the Freezing Fog",
    # 4504: "Elder Dragon Greyoll",
    # 4505: "Lesser Dragon",
    # 4510: "Ancient Dragon Lansseax",
    # 4511: "Lichdragon Fortissax",
    # 4520: "Dragonlord Placidusax",
    # 4550: "Monstrous Dog",
    # 4560: "Monstrous Crow",
    # 4561: "Monstrous Crow",
    # 4570: "Wormface",
    # 4580: "Wormface",
    # 4600: "Stonedigger Troll/Bols, Carian Knight",
    4601: "Armored Troll Knight",  # rare Metal Plate
    4602: "Troll Knight",  # very rare Metal Plate
    # 4603: "Smithing Master Iji",
    # 4604: "War Counselor Iji",
    # 4620: "Astel, Naturalborn of the Void",
    # 4630: "Runebear",
    # 4640: "Ulcerated/Putrid Tree Spirit",
    # 4650: "Dragonkin Soldier of Nokstella",
    # 4660: "Guardian Golem",
    # 4670: "Ancestor Spirit",
    # 4680: "Fallingstar Beast",
    # 4690: "Grafted Scion",
    # 4710: "God-Devouring Serpent / Rykard",
    # 4711: "Writhing Mass",
    # 4720: "Godfrey, The First Elden Lord",
    # 4721: "Hoarah Loux the Warrior",
    # 4730: "Starscourge Radahn",
    # 4750: "Godrick the Grafted",
    # 4751: "Godrick the Grafted (Defeated)",
    # 4760: "Fire Giant",
    # 4770: "Black Blade Kindred",
    # 4800: "Mohg, The Omen",
    # 4810: "Erdtree Avatar",
    # 4811: "Putrid Avatar",
    # 4820: "Omenkiller",
    # 4910: "Magma Wyrm",
    # 4911: "Great Wyrm Theodorix",
    # 4950: "Tibia Mariner",
    # 4960: "Giant Skeleton Torso",
    # 4980: "Death Rite Bird",
    # 6000: "Eagle",
    # 6001: "Eagle",
    # 6010: "Deer",
    # 6030: "Bear",
    # 6031: "Bear",
    # 6040: "Owl",
    # 6050: "Boar",
    # 6060: "Wild Mouflon",
    # 6070: "Guillemot",
    # 6071: "Guillemot",
    # 6072: "Carrier Pidgeon",
    # 6080: "Giant Dragonfly",
    # 6081: "Giant Dragonfly",
    # 6082: "Giant Dragonfly",
    # 6090: "Turtle",
    # 6091: "Giant Turtle / Miriel Pastor of Vows",
    # 6100: "Rabbitgaroo",
    # 7000: "Fallen Hawks Soldier",
    # 7100: "Ancient Hero of Zamor",
    # 8000: "Torrent",
    # 8100: "Ballista",
    # 8101: "Giant Ballista",
    # 8110: "Dragon-Faced Flamethrower",
    # 8120: "Merciless Chariot",
    # 8900: "Malenia, Blade of Miquella",
    # 8901: "Beast Clergyman/Maliketh, the Black Blade",
    # 8903: "Rennala",
    # 8904: "Morgott",
    # 8905: "Mohg, Lord of Blood",
    # 8906: "Melina",
    # 8907: "Malformed Ranni",
}


# Maps material IDs to lists of enemy model IDs that can drop them, and odds out of 1000.
# The item lots corresponding to these enemy IDs will be extended to include the new item.
#   common = 100
#   uncommon = 50
#   rare = 20
#   very rare = 5
EXTRA_ENEMY_DROPS = {
    Materials.SoftWood: (
        (3000, 100),  # "Exile Soldier"
        (3020, 100),  # "Large Exile Soldier"
        (3070, 100),  # "Dominula Celebrant"
        (3360, 100),  # "Ancestral Follower"
        (3361, 100),  # "Ancestral Follower"
        (4020, 100),  # "Royal Revenant"
        (4050, 100),  # "Kaiden Sellsword"
        (4120, 100),  # "Demi-Human Chief"
        (4310, 50),  # "Soldier"
        (4311, 100),  # "Godrick Soldier"
        (4312, 100),  # "Raya Lucaria Soldier"
        (4313, 100),  # "Leyndell Soldier"
        (4314, 100),  # "Radahn Soldier"
        (4315, 100),  # "Mausoleum Soldier"
        (4316, 100),  # "Haligtree Soldier"
        (4370, 50),  # "Foot Soldier"
        (4371, 50),  # "Godrick Foot Soldier"
        (4372, 50),  # "Raya Lucaria Foot Soldier"
        (4373, 50),  # "Leyndell Foot Soldier"
        (4374, 50),  # "Radahn Foot Soldier"
        (4375, 50),  # "Mausoleum Foot Soldier"
        (4376, 50),  # "Haligtree Foot Soldier"
    ),
    Materials.RefinedWood: (
        (3370, 20),  # "Ancestral Follower Shaman"
        (3371, 20),  # "Ancestral Follower Shaman"
        (3650, 20),  # "Erdtree Guardian"
    ),
    Materials.ErdtreeWood: (
        (3610, 5),  # "Oracle Envoy (Small)"
        (3620, 20),  # "Oracle Envoy (Medium)"
        (3630, 50),  # "Oracle Envoy (Large)"
    ),
    Materials.MetalShards: (
        (3010, 200),  # "Banished Knight"
        (3400, 1000),  # "Grave Warden Duelist"
        (3450, 200),  # "Misbegotten"
        (3460, 900),  # "Leonine Misbegotten"
        (3800, 900),  # "Cleanrot Knight"
        (3950, 500),  # "Man-Serpent"
        (4320, 100),  # "Vulgar Militia"
        (4321, 100),  # "Vulgar Militia"
        (4340, 250),  # "Mad Pumpkin Head"
        (4350, 50),  # "Castle Knight"
        (4351, 50),  # "Godrick Knight"
        (4352, 50),  # "Cuckoo Knight"
        (4353, 50),  # "Leyndell Knight"
        (4354, 50),  # "Redmane Knight"
        (4355, 50),  # "Mausoleum Knight"
        (4356, 50),  # "Haligtree Knight"
    ),
    Materials.MetalPlate: (
        (3910, 500),  # "Fire Prelate"
        (4470, 100),  # "Abductor Virgin"
        (4601, 100),  # "Armored Troll Knight"
        (4602, 50),  # "Troll Knight"
    ),
    Materials.PliableMetal: (
        (3320, 20),  # "Silver Tear",
        (3330, 50),  # "Silver Tear Orb"
    ),
    Materials.BlackMark: (
        (3150, 1000),  # "Night's Calvary"
    ),
    Materials.GruesomeBone: (
        (3061, 75),  # "Undead Azula Beastman"
        (3810, 25),  # "Kindred of Rot"
    ),
    Materials.MeteoriteChunk: (
        (4380, 5),  # "Starcaller"
    ),
    Materials.GlintstoneDust: (
        (3350, 100),  # "Crystalian"
    ),
    Materials.ErdtreeAmber: (
        (2500, 100),  # "Crucible Knight"
    ),
    Materials.DragonTeeth: (
        (3970, 25),  # "Beastman of Farum Azula"
    ),
    Materials.StoneFragment: (
        (4260, 100),  # "Erdtree Burial Watchdog"
        (4382, 5),  # "Tunnel Miner"
    ),
    Materials.SomberStoneFragment: (
        (4383, 5),  # "Glintstone Miner"
        (4384, 5),  # "Glintstone Miner"
    ),
    Materials.String: (
        (3850, 50),  # "Marionette"
        (3860, 50),  # "Avionette"
    ),
    Materials.SacramentalBud: (
        (3550, 500),  # Sanguine Noble
    ),
    Materials.ArteriaLeaf: (
        (4201, 200),  # Chanting Winged Dame
    ),
    Materials.FormicRock: (
        (4280, 100),  # Giant Ant
    ),
}
