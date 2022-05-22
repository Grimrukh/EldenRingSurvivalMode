"""Lists the recipes for weapons.

TODO: Everything between [something] and Greatshields below.

TODO: Weapons that need particularly difficult recipes:
    - Spears:
        - Spear: requires Stormveil/Liurnia/Caelid
        - Marais Executioner's Sword: requires Mountaintops
        - Bolt of Gransax: requires Mountaintops
        - Cleanrot Spear: requires Haligtree
        - Fallingstar Beast Jaw: requires Mountaintops
        - Sacred Mohgwyn's Spear: requires Mohgwyn Palace
        - Cipher Pata: requires Mountaintops
    - Bows:
        - Composite Bow: requires Caelid/Altus Plateau
        - Erdtree Bow: requires Mountaintops
        - Serpent Bow: requires Mountaintops
    - Whip: big recipe, requires Caelid/Altus Plateau
        - Magma Whip Candlestick: big recipe, requires Mountaintops
        - Giant's Red Braid: big recipe, requires Mountaintops
"""
from crafting import Materials

SCRATCH_WEAPONS = [
    # Weapons crafted from scratch.
    "Dagger",
    "Club",
    "Hand Axe",
    "Whip",  # +10
    "Caestus",
    "Shortbow",
]

WEAPON_RECIPES = {

    # region Daggers
    "Dagger": {
        "id": 100,
        "recipe": [
            (1, Materials.SmallHilt),
            (1, Materials.IronPlate),
        ],
    },
    "Black Knife": {
        "id": 101,
        "recipe": [
            (1, Materials.SmallHilt),
            (1, Materials.IronPlate),
            (1, Materials.BlackMark),
        ],
    },
    "Parrying Dagger": {
        "id": 102,
        "tier": 1,
        "previous": "Dagger",
        "recipe": [
            (1, Materials.SmallHilt),
            (1, Materials.IronPlate),
            (1, Materials.StoneFragment),
        ],
    },
    "Misericorde": {
        "id": 103,
        "recipe": [
            (1, Materials.SmallHilt),
            (1, Materials.IronPlate),
            (5, Materials.GraveViolet),
        ],
    },
    "Reduvia": {
        "id": 104,
        "recipe": [
            (1, Materials.SmallHilt),
            (1, Materials.GruesomeBone),
            (4, Materials.Bloodrose),
        ],
    },
    "Crystal Knife": {
        "id": 105,
        "recipe": [
            (1, Materials.SmallHilt),
            (5, Materials.CrackedCrystal),
            (4, Materials.StoneFragment),
        ],
    },
    "Celebrant's Sickle": {
        "id": 106,
        "recipe": [
            (1, Materials.SmallHilt),
            (2, Materials.StoneFragment),
            (4, Materials.HumanBoneShard),
            (6, Materials.TarnishedGoldenSunflower),
        ],
    },
    "Glintstone Kris": {
        "id": 107,
        "recipe": [
            (1, Materials.SmallHilt),
            (1, Materials.IronPlate),
            (5, Materials.CrystalBud),
            (5, Materials.SomberStoneFragment),
        ],
    },
    "Scorpion's Stinger": {
        "id": 108,
        "recipe": [
            (1, Materials.SmallHilt),
            (1, Materials.IronPlate),
            (5, Materials.AeonianButterfly),
            (5, Materials.SomberStoneFragment),
        ],
    },
    "Great Knife": {
        "id": 109,
        "recipe": [
            (1, Materials.SmallHilt),
            (1, Materials.IronPlate),
            (4, Materials.StoneFragment),
        ],
    },
    "Wakizashi": {
        "id": 110,
        "recipe": [
            (1, Materials.SmallHilt),
            (1, Materials.IronPlate),
            (1, Materials.IronShards),
            (5, Materials.StoneFragment),
        ],
    },
    "Cinquedea": {
        "id": 111,
        "recipe": [
            (1, Materials.SmallHilt),
            (5, Materials.SanctuaryStone),
            (2, Materials.BeastBlood),
            (3, Materials.SomberStoneFragment),
        ],
    },
    "Ivory Sickle": {
        "id": 113,
        "recipe": [
            (1, Materials.SmallHilt),
            (1, Materials.HeftyBeastBone),
            (6, Materials.StoneFragment),
        ],
    },
    "Bloodstained Dagger": {
        "id": 114,
        "recipe": [
            (1, Materials.SmallHilt),
            (1, Materials.IronPlate),
            (1, Materials.BeastBlood),
        ],
    },
    "Erdsteel Dagger": {
        "id": 115,
        "recipe": [
            (1, Materials.SmallHilt),
            (1, Materials.IronPlate),
            (1, Materials.ErdtreeWood),
        ],
    },
    "Blade of Calling": {
        "id": 116,
        "recipe": [
            (1, Materials.SmallHilt),
            (1, Materials.IronPlate),
            (5, Materials.ArteriaLeaf),
        ],
    },
    # endregion

    # OG Grim recipes end here

    # region Straight Swords
    "Longsword": {
        "id": 200,
        "recipe": [
            (1, Materials.StandardHilt),
            (2, Materials.IronPlate),
            (1, Materials.IronShards),
        ],
    },
    "Short Sword": {
        "id": 201,
        "recipe": [
            (1, Materials.StandardHilt),
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
        ],
    },
    "Broadsword": {
        "id": 202,
        "recipe": [
            (1, Materials.StandardHilt),
            (2, Materials.IronPlate),
        ],
    },
    "Lordsworn's Straight Sword": {
        "id": 204,
        "recipe": [
            (1, Materials.StandardHilt),
            (2, Materials.IronPlate),
            (1, Materials.RootResin),
        ],
    },
    "Weathered Straight Sword": {
        "id": 205,
        "recipe": [
            (1, Materials.StandardHilt),
            (4, Materials.IronShards),
        ],
    },
    "Ornamental Straight Sword": {
        "id": 206,
        "recipe": [
            (1, Materials.StandardHilt),
            (2, Materials.IronPlate),
            (3, Materials.SomberStoneFragment),
            (1, Materials.GoldenCentipede),
        ],
    },
    "Golden Epitaph": {
        "id": 207,
        "recipe": [
            (1, Materials.StandardHilt),
            (2, Materials.IronPlate),
            (4, Materials.StoneFragment),
            (4, Materials.AltusBloom),
            (4, Materials.GoldenSunflower),
        ],
    },
    "Nox Flowing Sword": {
        "id": 208,
        "recipe": [
            (1, Materials.CurvedHilt),
            (1, Materials.LiquidMetal),
            (2, Materials.SilverTearHusk),  # ?
        ],
    },
    "Inseparable Sword": {
        "id": 209,
        "recipe": [
            (1, Materials.GiantHilt),
            (3, Materials.IronPlate),
            (4, Materials.SomberStoneFragment),
            (10, Materials.SilverFirefly),
            (10, Materials.GoldFirefly),
        ],
    },
    "Coded Sword": {
        "id": 211,
        "recipe": [
            (1, Materials.StandardHilt),
            (3, Materials.SomberStoneFragment),
            (8, Materials.GoldTingedExcrement),
        ],
    },
    "Sword of Night and Flame": {
        "id": 214,
        "recipe": [
            (1, Materials.StandardHilt),
            (8, Materials.SomberStoneFragment),
            (3, Materials.GlintstoneDust),
            (3, Materials.ErdtreeAmber),
            (2, Materials.MeteoriteChunk),
        ],
    },
    "Crystal Sword": {
        "id": 215,
        "recipe": [
            (1, Materials.StandardHilt),
            (1, Materials.GlintstoneDust),
            (5, Materials.CrackedCrystal),
        ],
    },
    "Carian Knight's Sword": {
        "id": 218,
        "recipe": [
            (1, Materials.StandardHilt),
            (2, Materials.IronPlate),
            (5, Materials.GlintstoneFirefly),
        ],
    },
    "Sword of St. Trina": {
        "id": 219,
        "recipe": [
            (1, Materials.StandardHilt),
            (2, Materials.IronPlate),
            (4, Materials.StoneFragment),
            (2, Materials.SlumberingEgg),
            (7, Materials.TrinasLily),
        ],
    },
    "Miquellan Knight's Sword": {
        "id": 220,
        "recipe": [
            (1, Materials.StandardHilt),
            (2, Materials.IronPlate),
            (1, Materials.ErdtreeAmber),
        ],
    },
    "Cane Sword": {
        "id": 221,
        "recipe": [
            (1, Materials.StandardHilt),
            (1, Materials.SoftWood),
            (3, Materials.IronShards),
        ],
    },
    "Regalia of Eochaid": {
        "id": 222,
        "recipe": [
            (1, Materials.StandardHilt),
            (2, Materials.IronPlate),
            (1, Materials.GruesomeBone),
            (10, Materials.SacramentalBud),
        ],
    },
    "Noble's Slender Sword": {
        "id": 223,
        "recipe": [
            (1, Materials.StandardHilt),
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
            (1, Materials.TarnishedGoldenSunflower),
        ],
    },
    "Warhawk's Talon": {
        "id": 224,
        "recipe": [
            (1, Materials.StandardHilt),
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
            (2, Materials.StoneFragment),
        ],
    },
    "Lazuli Glintstone Sword": {
        "id": 225,
        "recipe": [
            (1, Materials.StandardHilt),
            (2, Materials.SoftWood),
            (1, Materials.GlintstoneDust),
        ],
    },
    "Rotten Crystal Sword": {
        "id": 226,
        "recipe": [
            (1, Materials.StandardHilt),
            (1, Materials.GruesomeBone),
            (8, Materials.SomberStoneFragment),
            (10, Materials.CrackedCrystal),
        ],
    },
    # endregion

    # region Greatswords
    "Bastard Sword": {
        "id": 300,
        "recipe": [
            (1, Materials.GiantHilt),
            (3, Materials.IronPlate),
        ],
    },
    "Forked Greatsword": {
        "id": 301,
        "recipe": [
            (1, Materials.GiantHilt),
            (2, Materials.IronPlate),
            (5, Materials.IronShards),
            (4, Materials.StoneFragment),
            (4, Materials.GraveViolet),
        ],
    },
    "Iron Greatsword": {
        "id": 302,
        "recipe": [
            (1, Materials.GiantHilt),
            (3, Materials.IronPlate),
            (1, Materials.IronShards),
            (2, Materials.StoneFragment),
        ],
    },
    "Lordsworn's Greatsword": {
        "id": 303,
        "recipe": [
            (1, Materials.GiantHilt),
            (2, Materials.IronPlate),
            (2, Materials.IronShards),
        ],
    },
    "Knight's Greatsword": {
        "id": 304,
        "recipe": [
            (1, Materials.GiantHilt),
            (1, Materials.SoftWood),
            (2, Materials.IronPlate),
            (2, Materials.IronShards),
        ],
    },
    "Flamberge": {
        "id": 305,
        "recipe": [
            (1, Materials.GiantHilt),
            (1, Materials.IronPlate),
            (5, Materials.IronShards),
            (1, Materials.Bloodrose),
        ],
    },
    "Ordovis's Greatsword": {
        "id": 306,
        "recipe": [
            (1, Materials.GiantHilt),
            (2, Materials.RefinedWood),
            (2, Materials.IronPlate),
            (6, Materials.SomberStoneFragment),
            (2, Materials.ErdtreeAmber),
        ],
    },
    "Onyx Lord's Sword": {
        "id": 307,
        "recipe": [
            (1, Materials.GiantHilt),
            (8, Materials.StoneFragment),
            (1, Materials.GlintstoneDust),
            (1, Materials.MeteoriteChunk),
        ],
    },
    "Banished Knight's Greatsword": {
        "id": 308,
        "recipe": [
            (1, Materials.GiantHilt),
            (3, Materials.IronPlate),
            (10, Materials.SanctuaryStone),
        ],
    },
    "Dark Moon Greatsword": {
        "id": 309,
        "recipe": [
            (1, Materials.GiantHilt),
            (3, Materials.IronPlate),
            (2, Materials.LiquidMetal),
            (10, Materials.SomberStoneFragment),
        ],
    },
    "Sacred Relic Sword": {
        "id": 310,
        "recipe": [
            (1, Materials.GiantHilt),
            (6, Materials.ErdtreeAmber),
            (20, Materials.LumpOfFlesh),
            (14, Materials.GoldenCentipede),
        ],
    },
    "Helphen's Steeple": {
        "id": 313,
        "recipe": [
            (1, Materials.GiantHilt),
            (1, Materials.LiquidMetal),
            (1, Materials.BlackMark),
            (4, Materials.HumanBoneShard),
        ],
    },
    "Blasphemous Blade": {
        "id": 314,
        "recipe": [
            (1, Materials.GiantHilt),
            (3, Materials.IronPlate),
            (1, Materials.GruesomeBone),
            (6, Materials.BeastBlood),
            (4, Materials.BloodTaintedExcrement),
        ],
    },
    "Marais Executioner's Sword": {
        "id": 315,
        "recipe": [
            (1, Materials.GiantHilt),
            (2, Materials.IronPlate),
            (1, Materials.LiquidMetal),
            (1, Materials.GruesomeBone),
        ],
    },
    "Sword of Milos": {
        "id": 316,
        "recipe": [
            (1, Materials.GiantHilt),
            (3, Materials.IronPlate),
            (4, Materials.HeftyBeastBone),
            (1, Materials.FormicRock),
        ],
    },
    "Golden Order Greatsword": {
        "id": 317,
        "recipe": [
            (1, Materials.GiantHilt),
            (3, Materials.IronPlate),
            (10, Materials.SomberStoneFragment),
            (4, Materials.ErdtreeAmber),
            (1, Materials.GoldenSunflower),
        ],
    },
    "Claymore": {
        "id": 318,
        "recipe": [
            (1, Materials.GiantHilt),
            (3, Materials.IronPlate),
            (2, Materials.StoneFragment),
        ],
    },
    "Gargoyle's Greatsword": {
        "id": 319,
        "recipe": [
            (1, Materials.GiantHilt),
            (3, Materials.IronPlate),
            (12, Materials.StoneFragment),
            (4, Materials.RootResin),
            (4, Materials.MeltedMushroom),
        ],
    },
    "Death's Poker": {
        "id": 320,
        "recipe": [
            (1, Materials.GiantHilt),
            (2, Materials.SomberStoneFragment),
            (2, Materials.BuddingHorn),
            (4, Materials.HumanBoneShard),
        ],
    },
    "Gargoyle's Blackblade": {
        "id": 321,
        "recipe": [
            (1, Materials.GiantHilt),
            (2, Materials.IronPlate),
            (1, Materials.BlackMark),
            (1, Materials.ErdtreeAmber),
            (2, Materials.MeltedMushroom),
        ],
    },
    "Greatsword": {
        "id": 400,
        "recipe": [
            (1, Materials.GiantHilt),
            (3, Materials.IronPlate),
            (1, Materials.SomberStoneFragment),
        ],
    },
    "Watchdog's Greatsword": {
        "id": 401,
        "recipe": [
            (1, Materials.GiantHilt),
            (6, Materials.StoneFragment),
            (4, Materials.SomberStoneFragment),
            (2, Materials.GraveViolet),
        ],
    },
    "Maliketh's Black Blade": {
        "id": 402,
        "recipe": [
            (1, Materials.GiantHilt),
            (4, Materials.IronPlate),
            (14, Materials.SomberStoneFragment),
            (2, Materials.BlackMark),
            (4, Materials.OldFang),
        ],
    },
    "Troll's Golden Sword": {
        "id": 403,
        "recipe": [
            (1, Materials.GiantHilt),
            (4, Materials.IronPlate),
            (2, Materials.GoldTingedExcrement),
        ],
    },
    "Zweihander": {
        "id": 404,
        "recipe": [
            (1, Materials.GiantHilt),
            (4, Materials.IronPlate),
            (2, Materials.StoneFragment),
        ],
    },
    "Starscourge Greatsword": {
        "id": 405,
        "recipe": [
            (1, Materials.GiantHilt),
            (3, Materials.IronPlate),
            (2, Materials.LiquidMetal),
            (1, Materials.GlintstoneDust),
        ],
    },
    "Royal Greatsword": {
        "id": 406,
        "recipe": [
            (1, Materials.GiantHilt),
            (4, Materials.IronPlate),
            (4, Materials.AeonianButterfly),
        ],
    },
    "Godslayer's Greatsword": {
        "id": 407,
        "recipe": [
            (1, Materials.GiantHilt),
            (4, Materials.IronPlate),
            (2, Materials.BlackMark),
            (4, Materials.SmolderingButterfly),
        ],
    },
    "Ruins Greatsword": {
        "id": 408,
        "recipe": [
            (1, Materials.GiantHilt),
            (1, Materials.MeteoriteChunk),
            (4, Materials.SomberStoneFragment),
            (20, Materials.SanctuaryStone),
        ],
    },
    "Grafted Blade Greatsword": {
        "id": 410,
        "recipe": [
            (1, Materials.GiantHilt),
            (12, Materials.IronShards),
        ],
    },
    "Troll Knight's Sword": {
        "id": 411,
        "recipe": [
            (1, Materials.GiantHilt),
            (4, Materials.IronPlate),
            (2, Materials.GlintstoneFirefly),
        ],
    },
    # endregion

    # region Thrusting Swords
    "Estoc": {
        "id": 500,
        "recipe": [
            (1, Materials.StandardHilt),
            (2, Materials.IronPlate),
            (1, Materials.IronShards),
        ],
    },
    "Cleanrot Knight's Sword": {
        "id": 501,
        "recipe": [
            (1, Materials.StandardHilt),
            (1, Materials.SoftWood),
            (2, Materials.IronPlate),
            (1, Materials.ErdtreeAmber),
        ],
    },
    "Rapier": {
        "id": 502,
        "recipe": [
            (1, Materials.StandardHilt),
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
        ],
    },
    "Rogier's Rapier": {
        "id": 503,
        "recipe": [
            (1, Materials.StandardHilt),
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
            (5, Materials.StoneFragment),
        ],
    },
    "Antspur Rapier": {
        "id": 504,
        "recipe": [
            (1, Materials.StandardHilt),
            (1, Materials.RefinedWood),
            (1, Materials.LiquidMetal),
            (8, Materials.ToxicMushroom),
            (4, Materials.FormicRock),
        ],
    },
    "Frozen Needle": {
        "id": 505,
        "recipe": [
            (1, Materials.StandardHilt),
            (1, Materials.IronPlate),
            (1, Materials.LiquidMetal),
            (1, Materials.GlintstoneDust),
        ],
    },
    "Noble's Estoc": {
        "id": 506,
        "recipe": [
            (1, Materials.StandardHilt),
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
            (1, Materials.TarnishedGoldenSunflower),
        ],
    },
    "Bloody Helice": {
        "id": 600,
        "recipe": [
            (1, Materials.GiantHilt),
            (1, Materials.IronPlate),
            (1, Materials.GruesomeBone),
            (2, Materials.BeastBlood),
            (8, Materials.LumpOfFlesh),
        ],
    },
    "Godskin Stitcher": {
        "id": 601,
        "recipe": [
            (1, Materials.GiantHilt),
            (3, Materials.IronPlate),
            (2, Materials.SomberStoneFragment),
            (4, Materials.StripOfWhiteFlesh),
        ],
    },
    "Great epee": {  # NOTE: Typo in name is from Yapped (leave it)
        "id": 602,
        "recipe": [
            (1, Materials.GiantHilt),
            (3, Materials.IronPlate),
            (1, Materials.IronShards),
        ],
    },
    "Dragon King's Cragblade": {
        "id": 604,
        "recipe": [
            (1, Materials.GiantHilt),
            (2, Materials.DragonTeeth),
            (14, Materials.StoneFragment),
            (10, Materials.GravelStone),
        ],
    },
    # endregion

    # region Curved Swords / Curved Greatswords
    "Falchion": {
        "id": 700,
        "recipe": [
            (1, Materials.CurvedHilt),
            (2, Materials.IronPlate),
        ],
    },
    "Beastman's Curved Sword": {
        "id": 701,
        "recipe": [
            (1, Materials.CurvedHilt),
            (1, Materials.IronPlate),
            (1, Materials.IronShards),
            (4, Materials.ThinBeastBones),
        ],
    },
    "Shotel": {
        "id": 702,
        "recipe": [
            (1, Materials.CurvedHilt),
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
            (2, Materials.StoneFragment),
        ],
    },
    "Shamshir": {
        "id": 703,
        "recipe": [
            (1, Materials.CurvedHilt),
            (1, Materials.IronPlate),
            (1, Materials.IronShards),
            (2, Materials.ThinBeastBones),
        ],
    },
    "Bandit's Curved Sword": {
        "id": 704,
        "recipe": [
            (1, Materials.CurvedHilt),
            (2, Materials.IronPlate),
            (1, Materials.IronShards),
            (1, Materials.RootResin),
        ],
    },
    "Magma Blade": {
        "id": 705,
        "recipe": [
            (1, Materials.CurvedHilt),
            (8, Materials.StoneFragment),
            (6, Materials.VolcanicStone),
        ],
    },
    "Flowing Curved Sword": {
        "id": 706,
        "recipe": [
            (1, Materials.CurvedHilt),
            (2, Materials.IronPlate),
            (1, Materials.SomberStoneFragment),
        ],
    },
    "Wing of Astel": {
        "id": 707,
        "recipe": [
            (1, Materials.CurvedHilt),
            (1, Materials.MeteoriteChunk),
            (2, Materials.GlintstoneDust),
        ],
    },
    "Scavenger's Curved Sword": {
        "id": 708,
        "recipe": [
            (1, Materials.CurvedHilt),
            (4, Materials.IronShards),
            (5, Materials.CaveMoss),
        ],
    },
    "Eclipse Shotel": {
        "id": 710,
        "recipe": [
            (1, Materials.CurvedHilt),
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
            (1, Materials.BlackMark),
        ],
    },
    "Serpent-God's Curved Sword": {
        "id": 711,
        "recipe": [
            (1, Materials.CurvedHilt),
            (2, Materials.IronPlate),
            (4, Materials.SacramentalBud),
        ],
    },
    "Mantis Blade": {
        "id": 712,
        "recipe": [
            (1, Materials.CurvedHilt),
            (1, Materials.IronPlate),
            (1, Materials.IronShards),
            (1, Materials.String),
            (1, Materials.RootResin),
        ],
    },
    "Scimitar": {
        "id": 714,
        "recipe": [
            (1, Materials.CurvedHilt),
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
        ],
    },
    "Grossmesser": {
        "id": 715,
        "recipe": [
            (1, Materials.CurvedHilt),
            (2, Materials.IronPlate),
        ],
    },
    "Onyx Lord's Greatsword": {
        "id": 801,
        "recipe": [
            (1, Materials.CurvedHilt),
            (3, Materials.SomberStoneFragment),
            (1, Materials.GlintstoneDust),
            (1, Materials.MeteoriteChunk),
        ],
    },
    "Dismounter": {
        "id": 802,
        "recipe": [
            (1, Materials.CurvedHilt),
            (3, Materials.IronPlate),
        ],
    },
    "Bloodhound's Fang": {
        "id": 803,
        "recipe": [
            (1, Materials.CurvedHilt),
            (2, Materials.IronPlate),
            (2, Materials.IronShards),
        ],
    },
    "Magma Wyrm's Scalesword": {
        "id": 804,
        "recipe": [
            (1, Materials.CurvedHilt),
            (1, Materials.DragonTeeth),
            (4, Materials.VolcanicStone),
        ],
    },
    "Zamor Curved Sword": {
        "id": 805,
        "recipe": [
            (1, Materials.CurvedHilt),
            (2, Materials.IronPlate),
            (2, Materials.GlintstoneDust),
            (4, Materials.RimedCrystalBud),
        ],
    },
    "Omen Cleaver": {
        "id": 806,
        "recipe": [
            (1, Materials.CurvedHilt),
            (2, Materials.IronPlate),
            (2, Materials.IronShards),
            (6, Materials.Herba),
        ],
    },
    "Monk's Flameblade": {
        "id": 807,
        "recipe": [
            (1, Materials.CurvedHilt),
            (1, Materials.IronPlate),
            (4, Materials.IronShards),
            (2, Materials.SomberStoneFragment),
        ],
    },
    "Beastman's Cleaver": {
        "id": 808,
        "recipe": [
            (1, Materials.CurvedHilt),
            (4, Materials.IronPlate),
            (2, Materials.HeftyBeastBone),
            (2, Materials.StoneFragment),
        ],
    },
    "Morgott's Cursed Sword": {
        "id": 810,
        "recipe": [
            (1, Materials.CurvedHilt),
            (1, Materials.GruesomeBone),
            (4, Materials.BeastBlood),
            (6, Materials.ArteriaLeaf),
        ],
    },
    # endregion

    # region Katanas
    "Uchigatana": {
        "id": 900,
        "recipe": [
            (1, Materials.CurvedHilt),
            (2, Materials.IronPlate),
            (2, Materials.StoneFragment),
        ],
    },
    "Nagakiba": {
        "id": 901,
        "recipe": [
            (1, Materials.CurvedHilt),
            (3, Materials.IronPlate),
            (4, Materials.StoneFragment),
            (2, Materials.FourToedFowlFoot),
        ],
    },
    "Hand of Malenia": {
        "id": 902,
        "recipe": [
            (1, Materials.CurvedHilt),
            (4, Materials.RefinedWood),
            (2, Materials.LiquidMetal),
            (8, Materials.MiquellasLily),
        ],
    },
    "Meteoric Ore Blade": {
        "id": 903,
        "recipe": [
            (1, Materials.CurvedHilt),
            (2, Materials.SomberStoneFragment),
            (1, Materials.MeteoriteChunk),
        ],
    },
    "Rivers of Blood": {
        "id": 904,
        "recipe": [
            (1, Materials.CurvedHilt),
            (1, Materials.RefinedWood),
            (2, Materials.IronPlate),
            (2, Materials.GruesomeBone),
            (6, Materials.Bloodrose),
        ],
    },
    "Moonveil": {
        "id": 906,
        "recipe": [
            (1, Materials.CurvedHilt),
            (4, Materials.SomberStoneFragment),
            (4, Materials.GlintstoneDust),
            (6, Materials.NascentButterfly),
        ],
    },
    "Dragonscale Blade": {
        "id": 907,
        "recipe": [
            (1, Materials.CurvedHilt),
            (1, Materials.DragonTeeth),
            (2, Materials.SomberStoneFragment),
            (4, Materials.GravelStone),
        ],
    },
    "Serpentbone Blade": {
        "id": 908,
        "recipe": [
            (1, Materials.StandardHilt),
            (4, Materials.IronShards),
            (8, Materials.MirandaPowder),
            (16, Materials.Poisonbloom),
        ],
    },
    # endregion

    # region Twinblades
    "Twinblade": {
        "id": 1000,
        "recipe": [
            (2, Materials.StandardHilt),
            (2, Materials.IronPlate),
            (2, Materials.IronShards),
        ],
    },
    "Godskin Peeler": {
        "id": 1001,
        "recipe": [
            (2, Materials.StandardHilt),
            (2, Materials.IronPlate),
            (1, Materials.BlackMark),
        ],
    },
    "Twinned Knight Swords": {
        "id": 1003,
        "recipe": [
            (2, Materials.StandardHilt),
            (3, Materials.IronPlate),
            (2, Materials.MeltedMushroom),
        ],
    },
    "Eleonora's Poleblade": {
        "id": 1005,
        "recipe": [
            (2, Materials.StandardHilt),
            (3, Materials.IronPlate),
            (8, Materials.Bloodrose),
        ],
    },
    "Gargoyle's Twinblade": {
        "id": 1008,
        "recipe": [
            (2, Materials.StandardHilt),
            (3, Materials.IronPlate),
            (12, Materials.StoneFragment),
            (2, Materials.RootResin),
            (4, Materials.MeltedMushroom),
        ],
    },
    "Gargoyle's Black Blades": {
        "id": 1009,
        "recipe": [
            (2, Materials.StandardHilt),
            (3, Materials.IronPlate),
            (1, Materials.BlackMark),
            (1, Materials.ErdtreeAmber),
            (2, Materials.MeltedMushroom),
        ],
    },
    # endregion

    # region Hammers
    "Mace": {
        "id": 1100,
        "recipe": [
            (1, Materials.AxeHandle),
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
        ],
    },
    "Club": {
        "id": 1101,
        "recipe": [
            (1, Materials.AxeHandle),
            (2, Materials.SoftWood),
        ],
    },
    "Curved Club": {
        "id": 1103,
        "recipe": [
            (1, Materials.AxeHandle),
            (1, Materials.RefinedWood),
            (1, Materials.SoftWood),
        ],
    },
    "Warpick": {
        "id": 1104,
        "recipe": [
            (1, Materials.AxeHandle),
            (2, Materials.IronPlate),
        ],
    },
    "Morning Star": {
        "id": 1105,
        "recipe": [
            (1, Materials.AxeHandle),
            (2, Materials.IronPlate),
            (2, Materials.IronShards),
            (6, Materials.StoneFragment),
        ],
    },
    "Varre's Bouquet": {
        "id": 1106,
        "recipe": [
            (1, Materials.AxeHandle),
            (4, Materials.IronShards),
            (8, Materials.Bloodrose),
        ],
    },
    "Spiked Club": {
        "id": 1107,
        "recipe": [
            (1, Materials.AxeHandle),
            (1, Materials.RefinedWood),
            (4, Materials.OldFang),
        ],
    },
    "Hammer": {
        "id": 1108,
        "recipe": [
            (1, Materials.AxeHandle),
            (4, Materials.StoneFragment),
            (8, Materials.SanctuaryStone),
        ],
    },
    "Monk's Flamemace": {
        "id": 1109,
        "recipe": [
            (1, Materials.AxeHandle),
            (1, Materials.IronPlate),
            (4, Materials.IronShards),
            (2, Materials.SomberStoneFragment),
        ],
    },
    "Envoy's Horn": {
        "id": 1110,
        "recipe": [
            (1, Materials.AxeHandle),
            (2, Materials.IronPlate),
            (6, Materials.AltusBloom),
        ],
    },
    "Scepter of the All-Knowing": {
        "id": 1111,
        "recipe": [
            (1, Materials.AxeHandle),
            (2, Materials.IronPlate),
            (1, Materials.AlbinauricBloodclot),
            (2, Materials.SilverFirefly),
        ],
    },
    "Nox Flowing Hammer": {
        "id": 1112,
        "recipe": [
            (1, Materials.AxeHandle),
            (1, Materials.LiquidMetal),
            (4, Materials.SilverTearHusk),  # ?
        ],
    },
    "Ringed Finger": {
        "id": 1113,
        "recipe": [
            (1, Materials.AxeHandle),
            (1, Materials.LiquidMetal),
            (10, Materials.LivingJarShard),
            (6, Materials.LumpOfFlesh),
            (4, Materials.BeastBlood),
        ],
    },
    "Stone Club": {
        "id": 1114,
        "recipe": [
            (1, Materials.AxeHandle),
            (6, Materials.SomberStoneFragment),
            (2, Materials.GlintstoneDust),
        ],
    },
    "Marika's Hammer": {
        "id": 1115,
        "recipe": [
            (1, Materials.AxeHandle),
            (4, Materials.ErdtreeAmber),
            (10, Materials.SomberStoneFragment),
        ],
    },
    # endregion / Hammers

    # region Greathammers
    "Large Club": {
        "id": 1200,
        "recipe": [
            (1, Materials.StaffPole),
            (4, Materials.SoftWood),
        ],
    },
    "Greathorn Hammer": {
        "id": 1201,
        "recipe": [
            (1, Materials.StaffPole),
            (4, Materials.StoneFragment),
            (6, Materials.HeftyBeastBone),
        ],
    },
    "Battle Hammer": {
        "id": 1202,
        "recipe": [
            (1, Materials.StaffPole),
            (4, Materials.IronPlate),
        ],
    },
    "Great Mace": {
        "id": 1206,
        "recipe": [
            (1, Materials.StaffPole),
            (3, Materials.IronPlate),
            (2, Materials.IronShards),
            (2, Materials.SomberStoneFragment),
        ],
    },
    "Curved Great Club": {
        "id": 1208,
        "recipe": [
            (1, Materials.StaffPole),
            (1, Materials.RefinedWood),
            (3, Materials.SoftWood),
        ],
    },
    "Celebrant's Skull": {
        "id": 1213,
        "recipe": [
            (1, Materials.StaffPole),
            (4, Materials.StoneFragment),
            (3, Materials.HeftyBeastBone),
            (8, Materials.HumanBoneShard),
        ],
    },
    "Pickaxe": {
        "id": 1214,
        "recipe": [
            (1, Materials.StaffPole),
            (1, Materials.RefinedWood),
            (2, Materials.IronPlate),
            (2, Materials.StoneFragment),
        ],
    },
    "Beastclaw Greathammer": {
        "id": 1215,
        "recipe": [
            (1, Materials.StaffPole),
            (4, Materials.SomberStoneFragment),
            (3, Materials.BeastBlood),
        ],
    },
    "Envoy's Long Horn": {
        "id": 1216,
        "recipe": [
            (1, Materials.StaffPole),
            (3, Materials.IronPlate),
            (1, Materials.ErdtreeAmber),
            (6, Materials.AltusBloom),
        ],
    },
    "Cranial Vessel Candlestand": {
        "id": 1217,
        "recipe": [
            (1, Materials.StaffPole),
            (1, Materials.GruesomeBone),
            (12, Materials.SmolderingButterfly),
            (4, Materials.VolcanicStone),
        ],
    },
    "Great Stars": {
        "id": 1218,
        "recipe": [
            (1, Materials.StaffPole),
            (3, Materials.IronPlate),
            (2, Materials.IronShards),
            (6, Materials.SomberStoneFragment),
            (5, Materials.BloodTaintedExcrement),
        ],
    },
    "Brick Hammer": {
        "id": 1219,
        "recipe": [
            (1, Materials.StaffPole),
            (15, Materials.StoneFragment),
            (15, Materials.SanctuaryStone),
            (4, Materials.RootResin),
        ],
    },
    "Devourer's Scepter": {
        "id": 1220,
        "recipe": [
            (1, Materials.StaffPole),
            (12, Materials.SomberStoneFragment),
            (3, Materials.GruesomeBone),
        ],
    },
    "Rotten Battle Hammer": {
        "id": 1221,
        "recipe": [
            (1, Materials.StaffPole),
            (4, Materials.IronPlate),
            (10, Materials.AeonianButterfly),
            (3, Materials.ToxicMushroom),
            (2, Materials.RimedRowa),
        ],
    },
    # endregion / Great Hammers

    # region Flails
    "Nightrider Flail": {
        "id": 1300,
        "recipe": [
            (1, Materials.AxeHandle),
            (5, Materials.IronShards),
            (2, Materials.SomberStoneFragment),
            (2, Materials.ArteriaLeaf),
        ],
    },
    "Flail": {
        "id": 1301,
        "recipe": [
            (1, Materials.AxeHandle),
            (2, Materials.SoftWood),
            (2, Materials.IronShards),
        ],
    },
    "Family Heads": {
        "id": 1302,
        "recipe": [
            (1, Materials.AxeHandle),
            (2, Materials.IronPlate),
            (3, Materials.HumanBoneShard),
            (6, Materials.GraveViolet),
        ],
    },
    "Bastard's Stars": {
        "id": 1303,
        "recipe": [
            (1, Materials.AxeHandle),
            (1, Materials.LiquidMetal),
            (1, Materials.MeteoriteChunk),
            (1, Materials.GlintstoneDust),
        ],
    },
    "Chainlink Flail": {
        "id": 1304,
        "recipe": [
            (1, Materials.AxeHandle),
            (1, Materials.RefinedWood),
            (1, Materials.SoftWood),
            (2, Materials.IronShards),
        ],
    },
    # endregion

    # region Axes / Greataxes
    "Battle Axe": {
        "id": 1400,
        "recipe": [
            (1, Materials.AxeHandle),
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
        ],
    },
    "Forked Hatchet": {
        "id": 1401,
        "recipe": [
            (1, Materials.AxeHandle),
            (2, Materials.IronPlate),
            (1, Materials.IronShards),
            (2, Materials.GraveViolet),
        ],
    },
    "Hand Axe": {
        "id": 1402,
        "recipe": [
            (1, Materials.AxeHandle),
            (1, Materials.SoftWood),
            (1, Materials.IronPlate),
        ],
    },
    "Jawbone Axe": {
        "id": 1403,
        "recipe": [
            (1, Materials.AxeHandle),
            (2, Materials.RefinedWood),
            (2, Materials.HeftyBeastBone),
        ],
    },
    "Iron Cleaver": {
        "id": 1404,
        "recipe": [
            (1, Materials.AxeHandle),
            (3, Materials.IronPlate),
            (2, Materials.StoneFragment),
        ],
    },
    "Ripple Blade": {
        "id": 1405,
        "recipe": [
            (1, Materials.AxeHandle),
            (1, Materials.LiquidMetal),
            (4, Materials.SomberStoneFragment),
            (4, Materials.AlbinauricBloodclot),
        ],
    },
    "Celebrant's Cleaver": {
        "id": 1406,
        "recipe": [
            (1, Materials.AxeHandle),
            (3, Materials.StoneFragment),
            (3, Materials.HeftyBeastBone),
            (2, Materials.HumanBoneShard),
        ],
    },
    "Icerind Hatchet": {
        "id": 1408,
        "recipe": [
            (1, Materials.AxeHandle),
            (1, Materials.IronPlate),
            (1, Materials.DragonTeeth),
            (2, Materials.RimedCrystalBud),
        ],
    },
    "Highland Axe": {
        "id": 1410,
        "recipe": [
            (1, Materials.AxeHandle),
            (2, Materials.SoftWood),
            (2, Materials.IronPlate),
        ],
    },
    "Sacrificial Axe": {
        "id": 1411,
        "recipe": [
            (1, Materials.AxeHandle),
            (3, Materials.IronPlate),
            (2, Materials.SomberStoneFragment),
            (2, Materials.GraveViolet),
        ],
    },
    "Rosus' Axe": {
        "id": 1412,
        "recipe": [
            (1, Materials.AxeHandle),
            (1, Materials.RefinedWood),
            (2, Materials.IronPlate),
            (1, Materials.GruesomeBone),
        ],
    },
    "Stormhawk Axe": {
        "id": 1414,
        "recipe": [
            (1, Materials.AxeHandle),
            (3, Materials.IronPlate),
            (4, Materials.Fulgurbloom),
            (2, Materials.FourToedFowlFoot),
            (1, Materials.StormhawkFeather),
        ],
    },
    "Greataxe": {
        "id": 1500,
        "recipe": [
            (1, Materials.AxeHandle),
            (2, Materials.SoftWood),
            (2, Materials.IronPlate),
        ],
    },
    "Warped Axe": {
        "id": 1501,
        "recipe": [
            (1, Materials.AxeHandle),
            (4, Materials.IronPlate),
            (2, Materials.RootResin),
        ],
    },
    "Great Omenkiller Cleaver": {
        "id": 1502,
        "recipe": [
            (1, Materials.AxeHandle),
            (2, Materials.RefinedWood),
            (2, Materials.StoneFragment),
            (4, Materials.BuddingHorn),
        ],
    },
    "Crescent Moon Axe": {
        "id": 1503,
        "recipe": [
            (1, Materials.AxeHandle),
            (2, Materials.SoftWood),
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
        ],
    },
    "Axe of Godrick": {
        "id": 1504,
        "recipe": [
            (1, Materials.AxeHandle),
            (4, Materials.IronPlate),
            (4, Materials.GoldenRowa),
            (12, Materials.ErdleafFlower),
        ],
    },
    "Longhaft Axe": {
        "id": 1505,
        "recipe": [
            (1, Materials.AxeHandle),
            (4, Materials.IronPlate),
        ],
    },
    "Rusted Anchor": {
        "id": 1506,
        "recipe": [
            (1, Materials.AxeHandle),
            (4, Materials.IronPlate),
            (2, Materials.SomberStoneFragment),
            (4, Materials.FourToedFowlFoot),
        ],
    },
    "Executioner's Greataxe": {
        "id": 1508,
        "recipe": [
            (1, Materials.AxeHandle),
            (2, Materials.SoftWood),
            (2, Materials.IronPlate),
            (2, Materials.YellowEmber),
        ],
    },
    "Winged Greathorn": {
        "id": 1511,
        "recipe": [
            (1, Materials.AxeHandle),
            (2, Materials.RefinedWood),
            (2, Materials.BuddingHorn),
            (1, Materials.DewkissedHerba),
        ],
    },
    "Butchering Knife": {
        "id": 1512,
        "recipe": [
            (1, Materials.AxeHandle),
            (4, Materials.IronPlate),
            (2, Materials.SomberStoneFragment),
        ],
    },
    "Gargoyle's Great Axe": {
        "id": 1513,
        "recipe": [
            (1, Materials.AxeHandle),
            (3, Materials.IronPlate),
            (10, Materials.StoneFragment),
            (8, Materials.MeltedMushroom),
            (3, Materials.RootResin),
        ],
    },
    "Gargoyle's Black Axe": {
        "id": 1514,
        "recipe": [
            (1, Materials.AxeHandle),
            (3, Materials.IronPlate),
            (1, Materials.BlackMark),
            (1, Materials.ErdtreeAmber),
            (2, Materials.MeltedMushroom),
        ],
    },
    # endregion

    # region Spears / Great Spears
    "Short Spear": {
        "id": 1600,
        "recipe": [
            (1, Materials.SpearShaft),
            (2, Materials.SoftWood),
            (1, Materials.IronPlate),
        ],
    },
    "Spear": {
        "id": 1601,
        "recipe": [
            (1, Materials.SpearShaft),
            (2, Materials.SoftWood),
            (2, Materials.IronShards),
        ],
    },
    "Crystal Spear": {
        "id": 1602,
        "recipe": [
            (1, Materials.SpearShaft),
            (1, Materials.GlintstoneDust),
            (7, Materials.CrackedCrystal),
        ],
    },
    "Clayman's Harpoon": {
        "id": 1603,
        "recipe": [
            (1, Materials.SpearShaft),
            (2, Materials.SoftWood),
            (1, Materials.MeteoriteChunk),
        ],
    },
    "Cleanrot Spear": {
        "id": 1604,
        "recipe": [
            (1, Materials.SpearShaft),
            (2, Materials.IronPlate),
            (2, Materials.ErdtreeAmber),
            (6, Materials.CrystalCaveMoss),
        ],
    },
    "Partisan": {
        "id": 1605,
        "recipe": [
            (1, Materials.SpearShaft),
            (1, Materials.RefinedWood),
            (1, Materials.SoftWood),
            (1, Materials.IronPlate),
            (1, Materials.IronShards),
        ],
    },
    "Celebrant's Rib-Rake": {
        "id": 1606,
        "recipe": [
            (1, Materials.SpearShaft),
            (2, Materials.StoneFragment),
            (6, Materials.ThinBeastBones),
            (4, Materials.HumanBoneShard),
        ],
    },
    "Pike": {
        "id": 1607,
        "recipe": [
            (1, Materials.SpearShaft),
            (4, Materials.IronPlate),
            (4, Materials.StoneFragment),
        ],
    },
    "Torchpole": {
        "id": 1608,
        "recipe": [
            (1, Materials.SpearShaft),
            (2, Materials.SoftWood),
            (1, Materials.RootResin),
            (6, Materials.SmolderingButterfly),
        ],
    },
    "Bolt of Gransax": {
        "id": 1609,
        "recipe": [
            (1, Materials.SpearShaft),
            (1, Materials.DragonTeeth),
            (1, Materials.LiquidMetal),
            (4, Materials.GravelStone),
        ],
    },
    "Cross-Naginata": {
        "id": 1611,
        "recipe": [
            (1, Materials.SpearShaft),
            (2, Materials.RefinedWood),
            (2, Materials.IronPlate),
            (3, Materials.StoneFragment),
        ],
    },
    "Death Ritual Spear": {
        "id": 1612,
        "recipe": [
            (1, Materials.SpearShaft),
            (1, Materials.LiquidMetal),
            (4, Materials.SomberStoneFragment),
            (3, Materials.GraveViolet),
        ],
    },
    "Inquisitor's Girandole": {
        "id": 1613,
        "recipe": [
            (1, Materials.SpearShaft),
            (6, Materials.IronShards),
            (3, Materials.SmolderingButterfly),
            (2, Materials.VolcanicStone),
        ],
    },
    "Spiked Spear": {
        "id": 1614,
        "recipe": [
            (1, Materials.SpearShaft),
            (3, Materials.SoftWood),
            (1, Materials.IronShards),
        ],
    },
    "Iron Spear": {
        "id": 1615,
        "recipe": [
            (1, Materials.SpearShaft),
            (3, Materials.SoftWood),
            (2, Materials.IronShards),
            (1, Materials.RootResin),
        ],
    },
    "Rotten Crystal Spear": {
        "id": 1616,
        "recipe": [
            (1, Materials.SpearShaft),
            (1, Materials.GruesomeBone),
            (7, Materials.SomberStoneFragment),
            (10, Materials.CrackedCrystal),
        ],
    },
    "Sacred Mohgwyn's Spear": {
        "id": 1701,
        "recipe": [
            (1, Materials.SpearShaft),
            (2, Materials.LiquidMetal),
            (1, Materials.GruesomeBone),
            (10, Materials.BloodTaintedExcrement),
        ],
    },
    "Siluria's Tree": {
        "id": 1702,
        "recipe": [
            (1, Materials.SpearShaft),
            (1, Materials.RefinedWood),
            (2, Materials.IronPlate),
            (2, Materials.ErdtreeAmber),
        ],
    },
    "Serpent-Hunter": {
        "id": 1703,
        "recipe": [
            (1, Materials.SpearShaft),
            (1, Materials.DragonTeeth),
            (4, Materials.SomberStoneFragment),
            (6, Materials.LivingJarShard),
        ],
    },
    "Vyke's War Spear": {
        "id": 1705,
        "recipe": [
            (1, Materials.SpearShaft),
            (3, Materials.IronPlate),
            (4, Materials.StoneFragment),
            (6, Materials.YellowEmber),
            (10, Materials.EyeOfYelough),
        ],
    },
    "Lance": {
        "id": 1706,
        "recipe": [
            (1, Materials.SpearShaft),
            (1, Materials.SoftWood),
            (3, Materials.IronPlate),
        ],
    },
    "Treespear": {
        "id": 1707,
        "recipe": [
            (1, Materials.SpearShaft),
            (3, Materials.IronPlate),
            (2, Materials.StoneFragment),
            (1, Materials.ErdtreeAmber),
        ],
    },
    # endregion

    # region Halberds
    "Halberd": {
        "id": 1800,
        "recipe": [
            (1, Materials.SpearShaft),
            (2, Materials.SoftWood),
            (1, Materials.IronPlate),
            (1, Materials.IronShards),
        ],
    },
    "Pest's Glaive": {
        "id": 1801,
        "recipe": [
            (1, Materials.SpearShaft),
            (6, Materials.StoneFragment),
            (4, Materials.TurtleNeckMeat),
            (3, Materials.GoldenCentipede),
        ],
    },
    "Lucerne": {
        "id": 1802,
        "recipe": [
            (1, Materials.SpearShaft),
            (2, Materials.SoftWood),
            (2, Materials.StoneFragment),
            (1, Materials.IronPlate),
            (1, Materials.IronShards),
        ],
    },
    "Banished Knight's Halberd": {
        "id": 1803,
        "recipe": [
            (1, Materials.SpearShaft),
            (1, Materials.RefinedWood),
            (1, Materials.SoftWood),
            (2, Materials.IronPlate),
            (6, Materials.FlightPinion),
        ],
    },
    "Commander's Standard": {
        "id": 1804,
        "recipe": [
            (1, Materials.SpearShaft),
            (2, Materials.RefinedWood),
            (2, Materials.IronPlate),
            (4, Materials.SomberStoneFragment),
            (10, Materials.CaveMoss),
        ],
    },
    "Nightrider Glaive": {
        "id": 1805,
        "recipe": [
            (1, Materials.SpearShaft),
            (4, Materials.IronPlate),
            (5, Materials.SomberStoneFragment),
            (4, Materials.ArteriaLeaf),
        ],
    },
    "Ripple Crescent Halberd": {
        "id": 1806,
        "recipe": [
            (1, Materials.SpearShaft),
            (1, Materials.LiquidMetal),
            (4, Materials.StoneFragment),
            (6, Materials.AlbinauricBloodclot),
        ],
    },
    "Vulgar Militia Saw": {
        "id": 1807,
        "recipe": [
            (1, Materials.SpearShaft),
            (1, Materials.RefinedWood),
            (1, Materials.SoftWood),
            (3, Materials.IronShards),
            (4, Materials.StoneFragment),
        ],
    },
    "Golden Halberd": {
        "id": 1808,
        "recipe": [
            (1, Materials.SpearShaft),
            (4, Materials.IronPlate),
            (1, Materials.ErdtreeAmber),
            (6, Materials.GoldenRowa),
        ],
    },
    "Glaive": {
        "id": 1809,
        "recipe": [
            (1, Materials.SpearShaft),
            (2, Materials.SoftWood),
            (2, Materials.IronPlate),
            (2, Materials.RootResin),
        ],
    },
    "Loretta's War Sickle": {
        "id": 1810,
        "recipe": [
            (1, Materials.SpearShaft),
            (2, Materials.LiquidMetal),
            (2, Materials.IronPlate),
            (4, Materials.GoldFirefly),
            (3, Materials.SilverTearHusk),
        ],
    },
    "Guardian's Swordspear": {
        "id": 1811,
        "recipe": [
            (1, Materials.SpearShaft),
            (3, Materials.RefinedWood),
            (1, Materials.ErdtreeAmber),
            (10, Materials.ErdleafFlower),
        ],
    },
    "Vulgar Militia Shotel": {
        "id": 1813,
        "recipe": [
            (1, Materials.SpearShaft),
            (1, Materials.RefinedWood),
            (1, Materials.SoftWood),
            (1, Materials.IronPlate),
            (1, Materials.IronShards),
        ],
    },
    "Dragon Halberd": {
        "id": 1814,
        "recipe": [
            (1, Materials.SpearShaft),
            (1, Materials.SoftWood),
            (2, Materials.IronPlate),
            (1, Materials.DragonTeeth),
        ],
    },
    "Gargoyle's Halberd": {
        "id": 1815,
        "recipe": [
            (1, Materials.SpearShaft),
            (2, Materials.IronPlate),
            (9, Materials.StoneFragment),
            (6, Materials.RootResin),
            (6, Materials.MeltedMushroom),
        ],
    },
    "Gargoyle's Black Halberd": {
        "id": 1816,
        "recipe": [
            (1, Materials.SpearShaft),
            (2, Materials.IronPlate),
            (1, Materials.BlackMark),
            (1, Materials.ErdtreeAmber),
            (2, Materials.MeltedMushroom),
        ],
    },
    # endregion

    # region Reapers
    "Scythe": {
        "id": 1900,
        "recipe": [
            (1, Materials.SpearShaft),
            (2, Materials.RefinedWood),
            (1, Materials.IronPlate),
            (2, Materials.StoneFragment),
        ],
    },
    "Grave Scythe": {
        "id": 1901,
        "recipe": [
            (1, Materials.SpearShaft),
            (2, Materials.SoftWood),
            (1, Materials.IronPlate),
            (1, Materials.GraveViolet),
        ],
    },
    "Halo Scythe": {
        "id": 1902,
        "recipe": [
            (1, Materials.SpearShaft),
            (2, Materials.RefinedWood),
            (1, Materials.IronPlate),
            (1, Materials.ErdtreeAmber),
            (6, Materials.SomberStoneFragment),
        ],
    },
    "Winged Scythe": {
        "id": 1906,
        "recipe": [
            (1, Materials.SpearShaft),
            (2, Materials.SoftWood),
            (1, Materials.IronPlate),
            (1, Materials.ErdtreeAmber),
            (6, Materials.FlightPinion),
        ],
    },
    # endregion

    # region Whips
    "Whip": {
        "id": 2000,
        "recipe": [
            (1, Materials.SmallHilt),
            (1, Materials.SoftWood),
            (3, Materials.LumpOfFlesh),
            (2, Materials.CaveMoss),
        ],
    },
    "Thorned Whip": {
        "id": 2002,
        "recipe": [
            (1, Materials.SmallHilt),
            (2, Materials.RefinedWood),
            (4, Materials.SomberStoneFragment),
            (6, Materials.Bloodrose),
            (4, Materials.BeastBlood),
        ],
    },
    "Magma Whip Candlestick": {
        "id": 2003,
        "recipe": [
            (1, Materials.SmallHilt),
            (1, Materials.IronPlate),
            (1, Materials.DragonTeeth),
            (6, Materials.VolcanicStone),
        ],
    },
    "Hoslow's Petal Whip": {
        "id": 2005,
        "recipe": [
            (1, Materials.SmallHilt),
            (6, Materials.IronShards),
            (6, Materials.StoneFragment),
            (2, Materials.String),
        ],
    },
    "Giant's Red Braid": {
        "id": 2006,
        "recipe": [
            (1, Materials.SmallHilt),
            (1, Materials.GruesomeBone),
            (4, Materials.SomberStoneFragment),
            (8, Materials.TarnishedGoldenSunflower),
            (4, Materials.SilverTearHusk),
        ],
    },
    "Urumi": {
        "id": 2007,
        "recipe": [
            (1, Materials.SmallHilt),
            (1, Materials.IronPlate),
            (2, Materials.LiquidMetal),
        ],
    },
    # endregion

    # region Fists
    "Caestus": {
        "id": 2100,
        "recipe": [
            (2, Materials.IronShards),
            (2, Materials.LumpOfFlesh),
        ],
    },
    "Spiked Caestus": {
        "id": 2101,
        "recipe": [
            (4, Materials.IronShards),
            (2, Materials.StoneFragment),
            (2, Materials.LumpOfFlesh),
        ],
    },
    "Grafted Dragon": {
        "id": 2106,
        "recipe": [
            (1, Materials.DragonTeeth),
            (4, Materials.BeastLiver),
        ],
    },
    "Iron Ball": {
        "id": 2107,
        "recipe": [
            (2, Materials.IronPlate),
            (2, Materials.SomberStoneFragment),
            (2, Materials.StripOfWhiteFlesh),
        ],
    },
    "Star Fist": {
        "id": 2108,
        "recipe": [
            (2, Materials.IronPlate),
            (2, Materials.IronShards),
            (2, Materials.SomberStoneFragment),
            (6, Materials.StoneFragment),
        ],
    },
    "Katar": {
        "id": 2110,
        "recipe": [
            (3, Materials.IronPlate),
            (4, Materials.SomberStoneFragment),
            (1, Materials.BeastBlood),
        ],
    },
    "Clinging Bone": {
        "id": 2111,
        "recipe": [
            (6, Materials.StoneFragment),
            (4, Materials.HumanBoneShard),
            (2, Materials.LivingJarShard),
            (5, Materials.YellowEmber),
        ],
    },
    "Veteran's Prosthesis": {
        "id": 2112,
        "recipe": [
            (1, Materials.RefinedWood),
            (2, Materials.IronPlate),
            (8, Materials.SomberStoneFragment),
            (8, Materials.Fulgurbloom),
        ],
    },
    "Cipher Pata": {
        "id": 2113,
        "recipe": [
            (1, Materials.StandardHilt),
            (6, Materials.SomberStoneFragment),
            (6, Materials.GoldTingedExcrement),
        ],
    },
    "Hookclaws": {
        "id": 2200,
        "recipe": [
            (1, Materials.SoftWood),
            (2, Materials.IronPlate),
            (5, Materials.ArteriaLeaf),
        ],
    },
    "Venomous Fang": {
        "id": 2201,
        "recipe": [
            (2, Materials.IronPlate),
            (1, Materials.BlackMark),  # ? eh
            (6, Materials.MirandaPowder),
            (4, Materials.ToxicMushroom),
        ],
    },
    "Bloodhound Claws": {
        "id": 2202,
        "recipe": [
            (3, Materials.IronPlate),
            (10, Materials.StoneFragment),
            (6, Materials.LandOctopusOvary),
            (3, Materials.MiquellasLily),
        ],
    },
    "Raptor Talons": {
        "id": 2203,
        "recipe": [
            (1, Materials.IronPlate),
            (1, Materials.LiquidMetal),
            (4, Materials.StormhawkFeather),
            (2, Materials.FourToedFowlFoot),

        ],
    },
    # endregion

    # region Colossal Weapons
    "Prelate's Inferno Crozier": {
        "id": 2300,
        "recipe": [
            (1, Materials.StaffPole),
            (3, Materials.IronPlate),
            (3, Materials.IronShards),
            (8, Materials.TurtleNeckMeat),
            (2, Materials.EyeOfYelough),
        ],
    },
    "Watchdog's Staff": {
        "id": 2301,
        "recipe": [
            (1, Materials.StaffPole),
            (16, Materials.StoneFragment),
            (1, Materials.GlintstoneDust),
        ],
    },
    "Great Club": {
        "id": 2302,
        "recipe": [
            (1, Materials.StaffPole),
            (5, Materials.SoftWood),
        ],
    },
    "Envoy's Greathorn": {
        "id": 2303,
        "recipe": [
            (1, Materials.StaffPole),
            (5, Materials.IronPlate),
            (1, Materials.ErdtreeAmber),
            (5, Materials.AltusBloom),
        ],
    },
    "Duelist Greataxe": {
        "id": 2304,
        "recipe": [
            (1, Materials.StaffPole),
            (3, Materials.RefinedWood),
            (4, Materials.IronPlate),
        ],
    },
    "Axe of Godfrey": {
        "id": 2305,
        "recipe": [
            (1, Materials.StaffPole),
            (2, Materials.RefinedWood),
            (3, Materials.IronPlate),
            (6, Materials.SomberStoneFragment),
        ],
    },
    "Dragon Greatclaw": {
        "id": 2306,
        "recipe": [
            (1, Materials.StaffPole),
            (1, Materials.DragonTeeth),
            (5, Materials.HeftyBeastBone),
            (2, Materials.RootResin),
        ],
    },
    "Staff of the Avatar": {
        "id": 2307,
        "recipe": [
            (1, Materials.StaffPole),
            (4, Materials.SoftWood),
            (2, Materials.IronPlate),
            (2, Materials.ErdtreeAmber),
        ],
    },
    "Fallingstar Beast Jaw": {
        "id": 2308,
        "recipe": [
            (1, Materials.StaffPole),
            (1, Materials.MeteoriteChunk),
            (1, Materials.GruesomeBone),
            (4, Materials.MeltedMushroom),
        ],
    },
    "Ghiza's Wheel": {
        "id": 2310,
        "recipe": [
            (1, Materials.StaffPole),
            (2, Materials.LiquidMetal),
            (2, Materials.IronPlate),
            (12, Materials.IronShards),
        ],
    },
    "Giant-Crusher": {
        "id": 2311,
        "recipe": [
            (1, Materials.StaffPole),
            (20, Materials.SomberStoneFragment),
        ],
    },
    "Golem's Halberd": {
        "id": 2312,
        "recipe": [
            (1, Materials.StaffPole),
            (1, Materials.BlackMark),
            (16, Materials.StoneFragment),
        ],
    },
    "Troll's Hammer": {
        "id": 2313,
        "recipe": [
            (1, Materials.StaffPole),
            (4, Materials.SoftWood),
            (2, Materials.ErdtreeAmber),
            (1, Materials.GlintstoneDust),
        ],
    },
    "Rotten Staff": {
        "id": 2314,
        "recipe": [
            (1, Materials.StaffPole),
            (4, Materials.SoftWood),
            (2, Materials.IronPlate),
            (2, Materials.ErdtreeAmber),
            (9, Materials.AeonianButterfly),
        ],
    },
    "Rotten Greataxe": {
        "id": 2315,
        "recipe": [
            (1, Materials.StaffPole),
            (2, Materials.RefinedWood),
            (3, Materials.IronPlate),
            (12, Materials.ToxicMushroom),
        ],
    },
    # endregion

    # region Torches
    "Torch": {
        "id": 2400,
        "recipe": [
            (1, Materials.SoftWood),
            (2, Materials.String),
            (2, Materials.SmolderingButterfly),
        ],
    },
    "Steel-Wire Torch": {
        "id": 2402,
        "recipe": [
            (1, Materials.RefinedWood),
            (2, Materials.String),
            (1, Materials.IronShards),
            (2, Materials.SmolderingButterfly),
        ],
    },
    "St. Trina's Torch": {
        "id": 2404,
        "recipe": [
            (2, Materials.RefinedWood),
            (3, Materials.String),
            (2, Materials.StoneFragment),
            (1, Materials.IronPlate),
            (3, Materials.TrinasLily),
            (1, Materials.SmolderingButterfly),
        ],
    },
    "Ghostflame Torch": {
        "id": 2405,
        "recipe": [
            (2, Materials.IronShards),
            (4, Materials.StoneFragment),
            (3, Materials.GraveViolet),
            (1, Materials.SmolderingButterfly),
        ],
    },
    "Beast-Repellent Torch": {
        "id": 2406,
        "recipe": [
            (2, Materials.RefinedWood),
            (2, Materials.MirandaPowder),
            (1, Materials.SmolderingButterfly),
        ],
    },
    "Sentry's Torch": {
        "id": 2407,
        "recipe": [
            (1, Materials.ErdtreeWood),
            (4, Materials.IronPlate),
            (2, Materials.GoldenSunflower),
            (1, Materials.ErdtreeAmber),
            (1, Materials.SmolderingButterfly),
        ],
    },
    # endregion

    # region Shields
    "Buckler": {
        "id": 3000,
        "recipe": [
            (1, Materials.ShieldHandle),
            (1, Materials.IronPlate),
            (2, Materials.StoneFragment),
        ],
    },
    "Perfumer's Shield": {
        "id": 3001,
        "recipe": [
            (1, Materials.ShieldHandle),
            (1, Materials.IronPlate),
            (1, Materials.ErdtreeAmber),
        ],
    },
    "Man-Serpent's Shield": {
        "id": 3002,
        "recipe": [
            (1, Materials.ShieldHandle),
            (1, Materials.IronPlate),
            (4, Materials.VolcanicStone),
        ],
    },
    "Rickety Shield": {
        "id": 3003,
        "recipe": [
            (1, Materials.ShieldHandle),
            (2, Materials.SoftWood),
        ],
    },
    "Pillory Shield": {
        "id": 3004,
        "recipe": [
            (1, Materials.ShieldHandle),
            (1, Materials.RefinedWood),
        ],
    },
    "Beastman's Jar-Shield": {
        "id": 3006,
        "recipe": [
            (1, Materials.ShieldHandle),
            (3, Materials.LivingJarShard),
            (1, Materials.HeftyBeastBone),
        ],
    },
    "Red Thorn Roundshield": {
        "id": 3007,
        "recipe": [
            (1, Materials.ShieldHandle),
            (2, Materials.SoftWood),
            (2, Materials.RootResin),
        ],
    },
    "Scripture Wooden Shield": {
        "id": 3008,
        "recipe": [
            (1, Materials.ShieldHandle),
            (2, Materials.SoftWood),
            (5, Materials.ErdleafFlower),
        ],
    },
    "Riveted Wooden Shield": {
        "id": 3009,
        "recipe": [
            (1, Materials.ShieldHandle),
            (2, Materials.SoftWood),
            (3, Materials.IronShards),
        ],
    },
    "Blue-White Wooden Shield": {
        "id": 3010,
        "recipe": [
            (1, Materials.ShieldHandle),
            (2, Materials.SoftWood),
            (1, Materials.AlbinauricBloodclot),
        ],
    },
    "Rift Shield": {
        "id": 3011,
        "recipe": [
            (1, Materials.ShieldHandle),
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
            (3, Materials.StoneFragment),
        ],
    },
    "Iron Roundshield": {
        "id": 3012,
        "recipe": [
            (1, Materials.ShieldHandle),
            (1, Materials.IronPlate),
            (2, Materials.StoneFragment),
        ],
    },
    "Gilded Iron Shield": {
        "id": 3013,
        "recipe": [
            (1, Materials.ShieldHandle),
            (1, Materials.IronPlate),
            (3, Materials.GoldenSunflower),
        ],
    },
    "Ice Crest Shield": {
        "id": 3014,
        "recipe": [
            (1, Materials.ShieldHandle),
            (1, Materials.IronPlate),
            (1, Materials.GlintstoneDust),
            (4, Materials.SilverFirefly),
        ],
    },
    "Smoldering Shield": {
        "id": 3015,
        "recipe": [
            (1, Materials.ShieldHandle),
            (6, Materials.VolcanicStone),
        ],
    },
    "Spiralhorn Shield": {
        "id": 3019,
        "recipe": [
            (1, Materials.ShieldHandle),
            (5, Materials.BuddingHorn),
        ],
    },
    "Coil Shield": {
        "id": 3020,
        "recipe": [
            (1, Materials.ShieldHandle),
            (5, Materials.BuddingHorn),
        ],
    },
    "Kite Shield": {
        "id": 3100,
        "recipe": [
            (1, Materials.ShieldHandle),
            (2, Materials.IronPlate),
        ],
    },
    "Marred Leather Shield": {
        "id": 3101,
        "recipe": [
            (1, Materials.ShieldHandle),
            (1, Materials.LumpOfFlesh),
            (3, Materials.TarnishedGoldenSunflower),
            (1, Materials.Bloodrose),
        ],
    },
    "Marred Wooden Shield": {
        "id": 3102,
        "recipe": [
            (1, Materials.ShieldHandle),
            (3, Materials.SoftWood),
            (3, Materials.TarnishedGoldenSunflower),
        ],
    },
    "Banished Knight's Shield": {
        "id": 3103,
        "recipe": [
            (1, Materials.ShieldHandle),
            (2, Materials.IronPlate),
            (2, Materials.IronPlate),
        ],
    },
    "Albinauric Shield": {
        "id": 3104,
        "recipe": [
            (1, Materials.ShieldHandle),
            (2, Materials.CrystalBud),
            (2, Materials.IronPlate),
            (1, Materials.AlbinauricBloodclot),
        ],
    },
    "Sun Realm Shield": {
        "id": 3105,
        "recipe": [
            (1, Materials.ShieldHandle),
            (2, Materials.IronPlate),
            (1, Materials.SoftWood),
        ],
    },
    "Silver Mirrorshield": {
        "id": 3106,
        "recipe": [
            (1, Materials.ShieldHandle),
            (2, Materials.SilverTearHusk),
            (1, Materials.AlbinauricBloodclot),
            (5, Materials.IronPlate),
            (1, Materials.SomberStoneFragment),
        ],
    },
    "Round Shield": {
        "id": 3107,
        "recipe": [
            (1, Materials.ShieldHandle),
            (2, Materials.RefinedWood),
            (2, Materials.IronShards),
        ],
    },
    "Scorpion Kite Shield": {
        "id": 3108,
        "recipe": [
            (1, Materials.ShieldHandle),
            (1, Materials.IronPlate),
            (2, Materials.RefinedWood),
        ],
    },
    "Twinbird Kite Shield": {
        "id": 3109,
        "recipe": [
            (1, Materials.ShieldHandle),
            (2, Materials.IronPlate),
            (5, Materials.FlightPinion),
            (3, Materials.StormhawkFeather),
        ],
    },
    "Blue-Gold Kite Shield": {
        "id": 3110,
        "recipe": [
            (1, Materials.ShieldHandle),
            (2, Materials.IronShards),
            (2, Materials.SoftWood),
        ],
    },
    "Brass Shield": {
        "id": 3113,
        "recipe": [
            (1, Materials.ShieldHandle),
            (3, Materials.IronPlate),
            (2, Materials.GoldenSunflower),
        ],
    },
    "Great Turtle Shell": {
        "id": 3114,
        "recipe": [
            (1, Materials.ShieldHandle),
            (4, Materials.TurtleNeckMeat),
            (4, Materials.CaveMoss),
            (4, Materials.HeftyBeastBone),
        ],
    },
    "Shield of the Guilty": {
        "id": 3117,
        "recipe": [
            (1, Materials.ShieldHandle),
            (2, Materials.IronPlate),
            (4, Materials.Bloodrose),
            (1, Materials.GruesomeBone),
        ],
    },
    "Carian Knight's Shield": {
        "id": 3119,
        "recipe": [
            (1, Materials.ShieldHandle),
            (5, Materials.IronPlate),
            (5, Materials.GlintstoneFirefly),
            (1, Materials.GoldenSunFlower),
        ],
    },
    "Large Leather Shield": {
        "id": 3123,
        "recipe": [
            (1, Materials.ShieldHandle),
            (2, Materials.RefinedWood),
            (4, Materials.String),
        ],
    },
    "Horse Crest Wooden Shield": {
        "id": 3124,
        "recipe": [
            (1, Materials.ShieldHandle),
            (3, Materials.RefinedWood),
            (3, Materials.RowaFruit),
            (1, Materials.Herba),
        ],
    },
    "Candletree Wooden Shield": {
        "id": 3125,
        "recipe": [
            (1, Materials.ShieldHandle),
            (3, Materials.RefinedWood),
            (2, Materials.RimedRowa),
        ],
    },
    "Flame Crest Wooden Shield": {
        "id": 3126,
        "recipe": [
            (1, Materials.ShieldHandle),
            (3, Materials.RefinedWood),
            (1, Materials.IronShards),
            (1, Materials.YellowEmber),
        ],
    },
    "Hawk Crest Wooden Shield": {
        "id": 3127,
        "recipe": [
            (1, Materials.ShieldHandle),
            (3, Materials.RefinedWood),
            (1, Materials.IronShards),
        ],
    },
    "Beast Crest Heater Shield": {
        "id": 3128,
        "recipe": [
            (1, Materials.ShieldHandle),
            (3, Materials.IronPlate),
            (1, Materials.ThinBeastBones),
        ],
    },
    "Red Crest Heater Shield": {
        "id": 3129,
        "recipe": [
            (1, Materials.ShieldHandle),
            (3, Materials.IronPlate),
            (2, Materials.RowaFruit),
        ],
    },
    "Blue Crest Heater Shield": {
        "id": 3130,
        "recipe": [
            (1, Materials.ShieldHandle),
            (3, Materials.IronPlate),
        ],
    },
    "Eclipse Crest Heater Shield": {
        "id": 3131,
        "recipe": [
            (1, Materials.ShieldHandle),
            (3, Materials.IronPlate),
            (1, Materials.RowaFruit),
        ],
    },
    "Inverted Hawk Heater Shield": {
        "id": 3132,
        "recipe": [
            (1, Materials.ShieldHandle),
            (3, Materials.IronPlate),
        ],
    },
    "Heater Shield": {
        "id": 3133,
        "recipe": [
            (1, Materials.ShieldHandle),
            (2, Materials.IronPlate),
        ],
    },
    "Black Leather Shield": {
        "id": 3134,
        "recipe": [
            (1, Materials.ShieldHandle),
            (3, Materials.RefinedWood),
            (1, Materials.IronPlate),
            (1, Materials.CaveMoss),
            (1, Materials.MeltedMushroom),
        ],
    },
    # endregion

    # region Greatshields
    "Dragon Towershield": {
        "id": 3200,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (2, Materials.IronShards),
            (10, Materials.IronPlate),
            (1, Materials.DragonTeeth),
        ],
    },
    "Distinguished Greatshield": {
        "id": 3202,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (2, Materials.RefinedWood),
            (6, Materials.IronPlate),
        ],
    },
    "Crucible Hornshield": {
        "id": 3203,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (12, Materials.BuddingHorn),
            (5, Materials.SomberStoneFragment),
            (1, Materials.ErdtreeAmber),
            (6, Materials.GoldTingedExcrement),
        ],
    },
    "Dragonclaw Shield": {
        "id": 3204,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (3, Materials.SomberStoneFragment),
            (8, Materials.GravelStone),
            (2, Materials.DragonTeeth),
        ],
    },
    "Briar Greatshield": {
        "id": 3205,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (15, Materials.RefinedWood),
            (3, Materials.IronPlate),
            (6, Materials.Bloodrose),
            (4, Materials.IronShards),
        ],
    },
    "Erdtree Greatshield": {
        "id": 3208,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (3, Materials.IronPlate),
            (5, Materials.ErdtreeWood),
            (3, Materials.ErdtreeAmber),
            (9, Materials.ErdleafFlower),
        ],
    },
    "Golden Beast Crest Shield": {
        "id": 3209,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (10, Materials.RefinedWood),
            (2, Materials.GoldenSunflower),
            (4, Materials.ErdleafFlower),
        ],
    },
    "Jellyfish Shield": {
        "id": 3212,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (2, Materials.SomberStoneFragment),
            (1, Materials.GruesomeBone),
            (1, Materials.LumpOfFlesh),
        ],
    },
    "Fingerprint Stone Shield": {
        "id": 3213,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (4, Materials.IronPlate),
            (8, Materials.SomberStoneFragment),
            (6, Materials.YellowEmber),
            (25, Materials.StoneFragment),
        ],
    },
    "Icon Shield": {
        "id": 3214,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (2, Materials.IronShards),
            (8, Materials.RefinedWood),
            (6, Materials.ErdleafFlower),
            (2, Materials.AltusBloom)
        ],
    },
    "One-Eyed Shield": {
        "id": 3215,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (2, Materials.SomberStoneFragment),
            (2, Materials.IronPlate),
            (8, Materials.StoneFragment),
            (8, Materials.FireBlossom),

        ],
    },
    "Visage Shield": {
        "id": 3216,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (4, Materials.SomberStoneFragment),
            (3, Materials.IronPlate),
            (10, Materials.StoneFragment),
            (10, Materials.FireBlossom),

        ],
    },
    "Spiked Palisade Shield": {
        "id": 3217,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (5, Materials.RefinedWood),
            (5, Materials.IronShards),
            (3, Materials.Bloodrose),
        ],
    },
    "Manor Towershield": {
        "id": 3219,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (5, Materials.IronPlate),
            (1, Materials.LivingJarShard),
        ],
    },
    "Crossed-Tree Towershield": {
        "id": 3220,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (2, Materials.IronShards),
            (3, Materials.IronPlate),
            (7, Materials.Herba),
        ],
    },
    "Inverted Hawk Towershield": {
        "id": 3221,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (4, Materials.IronShards),
            (3, Materials.IronPlate),
            (1, Materials.SomberStoneFragment),
        ],
    },
    "Ant's Skull Plate": {
        "id": 3222,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (1, Materials.SomberStoneFragment),
            (4, Materials.BuddingHorn),
            (6, Materials.HeftyBeastBone),
            (1, Materials.GruesomeBone),
            (1, Materials.BeastBlood),
        ],
    },
    "Redmane Greatshield": {
        "id": 3223,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (6, Materials.IronPlate),
            (1, Materials.SomberStoneFragment),
            (10, Materials.FireBlossom),
        ],
    },
    "Eclipse Crest Greatshield": {
        "id": 3224,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (5, Materials.IronPlate),
            (2, Materials.SomberStoneFragment),
            (1, Materials.GruesomeBone),
        ],
    },
    "Cuckoo Greatshield": {
        "id": 3225,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (3, Materials.RefinedWood),
            (3, Materials.SomberStoneFragment),
            (5, Materials.CrystalBud),
        ],
    },
    "Golden Greatshield": {
        "id": 3226,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (1, Materials.RefinedWood),
            (3, Materials.IronPlate),
            (4, Materials.GoldenCentipede),
            (1, Materials.FireBlossom),
        ],
    },
    "Gilded Greatshield": {
        "id": 3227,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (2, Materials.SoftWood),
            (2, Materials.RefinedWood),
            (2, Materials.IronPlate),
            (1, Materials.GoldenRowa),

        ],
    },
    "Haligtree Crest Greatshield": {
        "id": 3228,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (3, Materials.RefinedWood),
            (3, Materials.IronPlate),
            (3, Materials.MiquellasLily),
        ],
    },
    "Wooden Greatshield": {
        "id": 3229,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (5, Materials.RefinedWood),

        ],
    },
    "Lordsworn's Shield": {
        "id": 3230,
        "recipe": [
            (1, Materials.GreatshieldHandle),
            (4, Materials.RefinedWood),
            (2, Materials.IronShards),
        ],
    },
    # endregion

    # region Staffs
    "Glintstone Staff": {
        "id": 3300,
        "recipe": [
            (1, Materials.StaffPole),
            (2, Materials.CrystalBud),
        ],
    },
    "Crystal Staff": {
        "id": 3304,
        "recipe": [
            (1, Materials.StaffPole),
            (5, Materials.SomberStoneFragment),
            (1, Materials.GlintstoneDust),
            (2, Materials.GlintstoneFirefly),
            (5, Materials.CrackedCrystal),
        ],
    },
    "Gelmir Glintstone Staff": {
        "id": 3305,
        "recipe": [
            (1, Materials.StaffPole),
            (5, Materials.VolcanicStone),
            (2, Materials.SomberStoneFragment),
            (1, Materials.GlintstoneDust),
            (4, Materials.ErdtreeAmber),
        ],
    },
    "Demi-Human Queen's Staff": {
        "id": 3306,
        "recipe": [
            (1, Materials.StaffPole),
            (1, Materials.SomberStoneFragment),
            (2, Materials.CrystalBud),
            (2, Materials.StoneFragment),
        ],
    },
    "Carian Regal Scepter": {
        "id": 3309,
        "recipe": [
            (1, Materials.StaffPole),
            (4, Materials.SomberStoneFragment),
            (3, Materials.GlintstoneDust),
            (5, Materials.GlintstoneFirefly),
            (6, Materials.CrackedCrystal),
        ],
    },
    "Digger's Staff": {
        "id": 3312,
        "recipe": [
            (1, Materials.StaffPole),
            (2, Materials.SoftWood),
            (3, Materials.CrystalBud),
        ],
    },
    "Astrologer's Staff": {
        "id": 3313,
        "recipe": [
            (1, Materials.StaffPole),
            (1, Materials.SoftWood),
            (2, Materials.CrackedCrystal)
        ],
    },
    "Carian Glintblade Staff": {
        "id": 3317,
        "recipe": [
            (1, Materials.StaffPole),
            (2, Materials.StoneFragment),
            (3, Materials.CrystalBud),
            (1, Materials.GlintstoneFirefly)
        ],
    },
    "Prince of Death's Staff": {
        "id": 3318,
        "recipe": [
            (1, Materials.StaffPole),
            (3, Materials.SomberStoneFragment),
            (1, Materials.BuddingHorn),
            (3, Materials.HumanBoneShard),
            (1, Materials.GlintstoneDust),
            (1, Materials.ErdtreeAmber),
        ],
    },
    "Albinauric Staff": {
        "id": 3319,
        "recipe": [
            (1, Materials.StaffPole),
            (2, Materials.RefinedWood),
            (3, Materials.GruesomeBone),
            (1, Materials.SomberStoneFragment),
        ],
    },
    "Academy Glintstone Staff": {
        "id": 3320,
        "recipe": [
            (1, Materials.StaffPole),
            (2, Materials.SoftWood),
            (1, Materials.CrackedCrystal),
            (2, Materials.GlintstoneFirefly),
        ],
    },
    "Carian Glintstone Staff": {
        "id": 3321,
        "recipe": [
            (1, Materials.StaffPole),
            (1, Materials.RefinedWood),
            (1, Materials.CrackedCrystal),
            (2, Materials.GlintstoneFirefly),
        ],
    },
    "Azur's Glintstone Staff": {
        "id": 3323,
        "recipe": [
            (1, Materials.StaffPole),
            (4, Materials.SomberStoneFragment),
            (2, Materials.GlintstoneDust),
            (4, Materials.GlintstoneFirefly),
            (3, Materials.CrystalBud),
            (3, Materials.CrystalCaveMoss),
        ],
    },
    "Lusat's Glintstone Staff": {
        "id": 3324,
        "recipe": [
            (1, Materials.StaffPole),
            (4, Materials.SomberStoneFragment),
            (2, Materials.GlintstoneDust),
            (7, Materials.GlintstoneFirefly),
            (5, Materials.CrystalBud),
        ],
    },
    "Meteorite Staff": {
        "id": 3325,
        "recipe": [
            (1, Materials.StaffPole),
            (1, Materials.RefinedWood),
            (1, Materials.MeteoriteChunk),
        ],
    },
    "Staff of the Guilty": {
        "id": 3326,
        "recipe": [
            (1, Materials.StaffPole),
            (1, Materials.RefinedWood),
            (5, Materials.Bloodrose),
            (2, Materials.BloodTaintedExcrement),
        ],
    },
    "Rotten Crystal Staff": {
        "id": 3327,
        "recipe": [
            (1, Materials.StaffPole),
            (3, Materials.CrystalBud),
            (4, Materials.AeonianButterfly),
            (2, Materials.GruesomeBone),
            (1, Materials.FadedErdleafFlower),
        ],
    },
    "Staff of Loss": {
        "id": 3328,
        "recipe": [
            (1, Materials.StaffPole),
            (1, Materials.RefinedWood),
            (4, Materials.CrackedCrystal),
        ],
    },
    # endregion

    # region Seals
    "Finger Seal": {
        "id": 3400,
        "recipe": [
            (1, Materials.RefinedWood),
            (3, Materials.StoneFragment),
            (3, Materials.ErdleafFlower),
        ],
    },
    "Godslayer's Seal": {
        "id": 3401,
        "recipe": [
            (2, Materials.SomberStoneFragment),
            (3, Materials.StoneFragment),
            (1, Materials.BlackMark),
        ],
    },
    "Giant's Seal": {
        "id": 3402,
        "recipe": [
            (5, Materials.SomberStoneFragment),
            (10, Materials.FireBlossom),
            (3, Materials.HeftyBeastBone),
            (2, Materials.String),
        ],
    },
    "Gravel Stone Seal": {
        "id": 3403,
        "recipe": [
            (2, Materials.SomberStoneFragment),
            (2, Materials.StoneFragment),
            (2, Materials.AltusBloom),
            (6, Materials.GravelStone),
            # Potential use for DragonTeeth
        ],
    },
    "Clawmark Seal": {
        "id": 3404,
        "recipe": [
            (6, Materials.StoneFragment),
            (3, Materials.OldFang),
            (2, Materials.BeastBlood),
        ],
    },
    "Golden Order Seal": {
        "id": 3406,
        "recipe": [
            (5, Materials.SomberStoneFragment),
            (2, Materials.ErdtreeAmber),
            (4, Materials.AltusBloom),
            (3, Materials.GoldFirefly),
            (3, Materials.GlintstoneFirefly),
            (4, Materials.CrystalBud),
        ],
    },
    "Erdtree Seal": {
        "id": 3407,
        "recipe": [
            (5, Materials.SomberStoneFragment),
            (3, Materials.ErdtreeAmber),
            (7, Materials.ErdleafFlower),
            (1, Materials.GoldenSunflower),
        ],
    },
    "Dragon Communion Seal": {
        "id": 3408,
        "recipe": [
            (4, Materials.SomberStoneFragment),
            (6, Materials.StoneFragment),
            # Potential use for DragonTeeth
        ],
    },
    "Frenzied Flame Seal": {
        "id": 3409,
        "recipe": [
            (3, Materials.SomberStoneFragment),
            (8, Materials.YellowEmber),
            (5, Materials.EyeOfYelough),
        ],
    },
    # endregion

    # region Bows
    "Shortbow": {
        "id": 4000,
        "recipe": [
            (1, Materials.BowGrip),
            (1, Materials.String),
            (2, Materials.SoftWood),
        ],
    },
    "Misbegotten Shortbow": {
        "id": 4001,
        "recipe": [
            (1, Materials.BowGrip),
            (1, Materials.String),
            (1, Materials.SoftWood),
            (1, Materials.ThinBeastBones),
        ],
    },
    "Red Branch Shortbow": {
        "id": 4002,
        "recipe": [
            (1, Materials.BowGrip),
            (1, Materials.RefinedWood),
            (1, Materials.String),
            (2, Materials.RowaFruit),
        ],
    },
    "Harp Bow": {
        "id": 4003,
        "recipe": [
            (1, Materials.BowGrip),
            (6, Materials.String),
            (1, Materials.RefinedWood),
        ],
    },
    "Composite Bow": {
        "id": 4005,
        "recipe": [
            (1, Materials.BowGrip),
            (2, Materials.String),
            (2, Materials.SoftWood),
        ],
    },
    "Longbow": {
        "id": 4100,
        "recipe": [
            (1, Materials.BowGrip),
            (1, Materials.String),
            (2, Materials.SoftWood),
        ],
    },
    "Albinauric Bow": {
        "id": 4101,
        "recipe": [
            (1, Materials.BowGrip),
            (2, Materials.RefinedWood),
            (1, Materials.AlbinauricBloodclot),
            (1, Materials.StoneFragment),
        ],
    },
    "Horn Bow": {
        "id": 4102,
        "recipe": [
            (1, Materials.BowGrip),
            (3, Materials.RefinedWood),
            (1, Materials.String),
        ],
    },
    "Erdtree Bow": {
        "id": 4103,
        "recipe": [
            (1, Materials.BowGrip),
            (2, Materials.ErdtreeWood),
            (2, Materials.String),
            (2, Materials.GoldFirefly),
            (1, Materials.ErdtreeAmber),
        ],
    },
    "Serpent Bow": {
        "id": 4104,
        "recipe": [
            (1, Materials.BowGrip),
            (2, Materials.RefinedWood),
            (1, Materials.GruesomeBone),
            (2, Materials.String),
        ],
    },
    "Pulley Bow": {
        "id": 4106,
        "recipe": [
            (1, Materials.BowGrip),
            (3, Materials.String),
            (2, Materials.StoneFragment),
            (2, Materials.RefinedWood),
        ],
    },
    "Black Bow": {
        "id": 4107,
        "recipe": [
            (1, Materials.BowGrip),
            (2, Materials.RefinedWood),
            (2, Materials.StoneFragment),
            (2, Materials.String),
        ],
    },
    # endregion

    # region Greatbows
    "Lion Greatbow": {
        "id": 4200,
        "recipe": [
            (1, Materials.GreatBowGrip),
            (2, Materials.RefinedWood),
            (2, Materials.SomberStoneFragment),
            (2, Materials.IronShards),
            (2, Materials.String),
        ],
    },
    "Golem Greatbow": {
        "id": 4201,
        "recipe": [
            (1, Materials.GreatBowGrip),
            (2, Materials.RefinedWood),
            (4, Materials.IronPlate),
            (2, Materials.MeteoriteChunk),
        ],
    },
    "Erdtree Greatbow": {
        "id": 4203,
        "recipe": [
            (1, Materials.GreatBowGrip),
            (1, Materials.ErdtreeWood),
            (1, Materials.ErdleafFlower),
            (2, Materials.ErdtreeAmber),
        ],
    },
    "Greatbow": {
        "id": 4204,
        "recipe": [
            (1, Materials.GreatBowGrip),
            (3, Materials.String),
            (2, Materials.RefinedWood),
            (2, Materials.IronPlate),
        ],
    },
    # endregion

    # region Crossbows / Guns
    "Soldier's Crossbow": {
        "id": 4300,
        "recipe": [
            (1, Materials.TriggerMechanism),
            (1, Materials.String),
            (1, Materials.SoftWood),
            (1, Materials.StoneFragment),
        ],
    },
    "Light Crossbow": {
        "id": 4302,
        "recipe": [
            (1, Materials.TriggerMechanism),
            (1, Materials.String),
            (1, Materials.SoftWood),
            (2, Materials.StoneFragment),
        ],
    },
    "Heavy Crossbow": {
        "id": 4303,
        "recipe": [
            (1, Materials.TriggerMechanism),
            (1, Materials.String),
            (3, Materials.SoftWood),
            (2, Materials.StoneFragment),
        ],
    },
    "Pulley Crossbow": {
        "id": 4305,
        "recipe": [
            (1, Materials.TriggerMechanism),
            (3, Materials.String),
            (2, Materials.RefinedWood),
            (1, Materials.IronPlate),
        ],
    },
    "Full Moon Crossbow": {
        "id": 4306,
        "recipe": [
            (1, Materials.TriggerMechanism),
            (4, Materials.String),
            (4, Materials.RefinedWood),
            (1, Materials.SomberStoneFragment),
        ],
    },
    "Arbalest": {
        "id": 4308,
        "recipe": [
            (1, Materials.TriggerMechanism),
            (2, Materials.String),
            (2, Materials.RefinedWood),
        ],
    },
    "Crepus's Black-Key Crossbow": {
        "id": 4311,
        "recipe": [
            (1, Materials.TriggerMechanism),
            (1, Materials.IronPlate),
            (2, Materials.RefinedWood),
            (2, Materials.String),
        ],
    },
    "Hand Ballista": {
        "id": 4400,
        "recipe": [
            (1, Materials.TriggerMechanism),
            (4, Materials.String),
            (3, Materials.RefinedWood),
            (2, Materials.IronPlate),
        ],
    },
    "Jar Cannon": {
        "id": 4401,
        "recipe": [
            (1, Materials.TriggerMechanism),
            (2, Materials.IronPlate),
            (2, Materials.SomberStoneFragment),
            (4, Materials.LivingJarShard),
        ],
    },
    # endregion
}
