"""Lists the recipes for weapons."""
from crafting import Materials


WEAPON_RECIPES = {
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
            (7, Materials.Bloodrose),
            (2, Materials.BloodTaintedExcrement),
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
    # OG Grim recipes end here
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
            (4, Materials.SilverTearHusk), #?
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
            (3, Materials.MeteoriteChunk),
        ],
    },
    "Crystal Sword": {
        "id": 215,
        "recipe": [
            (1, Materials.StandardHilt),
            (3, Materials.RimedCrystalBud),
            (5, Materials.CrackedCrystal),
        ],
    },
    "Carian Knight's Sword": {
        "id": 218,
        "recipe": [
            (1, Materials.StandardHilt),
            (2, Materials.IronPlate),
            (1, Materials.GlintstoneFirefly),
        ],
    },
    "Sword of St. Trina": {
        "id": 219,
        "recipe": [
            (1, Materials.StandardHilt),
            (2, Materials.IronPlate),
            (2, Materials.StoneFragment),
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
            (1, Materials.StoneFragment),
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
            (1, Materials.SomberStoneFragment),
            (1, Materials.GruesomeBone),
            (10, Materials.CrackedCrystal),
        ],
    },
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
            (2, Materials.IronPlate),
            (3, Materials.IronShards),
        ],
    },
    "Flamberge": {
        "id": 305,
        "recipe": [
            (1, Materials.GiantHilt),
            (1, Materials.IronPlate),
            (5, Materials.IronShards),
            (1, Materials.StoneFragment),
        ],
    },
    "Ordovis's Greatsword": {
        "id": 306,
        "recipe": [
            (1, Materials.GiantHilt),
            (2, Materials.RefinedWood),
            (2, Materials.IronPlate),
            (2, Materials.SomberStoneFragment),
            (5, Materials.ErdtreeAmber),
        ],
    },
    "Onyx Lord's Sword": {
        "id": 307,
        "recipe": [
            (1, Materials.GiantHilt),
            (3, Materials.StoneFragment),
            (2, Materials.MeteoriteChunk),
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
            (8, Materials.GoldenCentipede),
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
            (4, Materials.BeastBlood),
        ],
    },
    "Marais Executioner's Sword": {
        "id": 315,
        "recipe": [
            (1, Materials.GiantHilt),
            (3, Materials.IronPlate),
            (1, Materials.GruesomeBone),
            (4, Materials.AeonianButterfly),
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
            (5, Materials.SomberStoneFragment),
            (5, Materials.ErdtreeAmber),
            (1, Materials.GoldenSunflower),
        ],
    },
    "Claymore": {
        "id": 318,
        "recipe": [
            (1, Materials.GiantHilt),
            (3, Materials.IronPlate),
            (1, Materials.StoneFragment),
        ],
    },
    "Gargoyle's Greatsword": {
        "id": 319,
        "recipe": [
            (1, Materials.GiantHilt),
            (3, Materials.IronPlate),
            (1, Materials.BlackMark),
        ],
    },
    "Death's Poker": {
        "id": 320,
        "recipe": [
            (1, Materials.GiantHilt),
            (2, Materials.StoneFragment),
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
        ],
    },
    "Greatsword": {
        "id": 400,
        "recipe": [
            (1, Materials.GiantHilt),
            (4, Materials.IronPlate),
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
            (2, Materials.BlackMark),
            (4, Materials.OldFang),
            (3, Materials.SomberStoneFragment),
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
            (1, Materials.GlintstoneDust),
            (1, Materials.AeonianButterfly),
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
            (2, Materials.SomberStoneFragment),
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
            (1, Materials.StoneFragment),
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
            (3, Materials.StoneFragment),
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
        ],
    },
    "Antspur Rapier": {
        "id": 504,
        "recipe": [
            (1, Materials.StandardHilt),
            (1, Materials.RefinedWood),
            (1, Materials.GruesomeBone),
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
            (4, Materials.IronShards),
            (1, Materials.GruesomeBone),
            (2, Materials.BeastBlood),
        ],
    },
    "Godskin Stitcher": {
        "id": 601,
        "recipe": [
            (1, Materials.GiantHilt),
            (3, Materials.IronPlate),
            (2, Materials.SomberStoneFragment),
        ],
    },
    "Great epee": {
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
            (14, Materials.StoneFragment),
            (16, Materials.GravelStone),
        ],
    },
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
            (2, Materials.IronShards),
        ],
    },
    "Shotel": {
        "id": 702,
        "recipe": [
            (1, Materials.CurvedHilt),
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
            (1, Materials.StoneFragment),
        ],
    },
    #bookmark
    "Shamshir": {
        "id": 703,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Bandit's Curved Sword": {
        "id": 704,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Magma Blade": {
        "id": 705,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Flowing Curved Sword": {
        "id": 706,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Wing of Astel": {
        "id": 707,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Scavenger's Curved Sword": {
        "id": 708,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Eclipse Shotel": {
        "id": 710,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Serpent-God's Curved Sword": {
        "id": 711,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Mantis Blade": {
        "id": 712,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Scimitar": {
        "id": 714,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Grossmesser": {
        "id": 715,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Onyx Lord's Greatsword": {
        "id": 801,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Dismounter": {
        "id": 802,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Bloodhound's Fang": {
        "id": 803,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Magma Wyrm's Scalesword": {
        "id": 804,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Zamor Curved Sword": {
        "id": 805,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Omen Cleaver": {
        "id": 806,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Monk's Flameblade": {
        "id": 807,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Beastman's Cleaver": {
        "id": 808,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Morgott's Cursed Sword": {
        "id": 810,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Uchigatana": {
        "id": 900,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Nagakiba": {
        "id": 901,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Hand of Malenia": {
        "id": 902,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Meteoric Ore Blade": {
        "id": 903,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Rivers of Blood": {
        "id": 904,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Moonveil": {
        "id": 906,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Dragonscale Blade": {
        "id": 907,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Serpentbone Blade": {
        "id": 908,
        "recipe": [
            (1, Materials.CurvedHilt),
        ],
    },
    "Twinblade": {
        "id": 1000,
        "recipe": [
            (1, Materials.StandardHilt),
        ],
    },
    "Godskin Peeler": {
        "id": 1001,
        "recipe": [
            (1, Materials.StandardHilt),
        ],
    },
    "Twinned Knight Swords": {
        "id": 1003,
        "recipe": [
            (1, Materials.StandardHilt),
        ],
    },
    "Eleonora's Poleblade": {
        "id": 1005,
        "recipe": [
            (1, Materials.StandardHilt),
        ],
    },
    "Gargoyle's Twinblade": {
        "id": 1008,
        "recipe": [
            (1, Materials.StandardHilt),
        ],
    },
    "Gargoyle's Black Blades": {
        "id": 1009,
        "recipe": [
            (1, Materials.StandardHilt),
        ],
    },
    "Mace": {
        "id": 1100,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Club": {
        "id": 1101,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Curved Club": {
        "id": 1103,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Warpick": {
        "id": 1104,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Morning Star": {
        "id": 1105,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Varre's Bouquet": {
        "id": 1106,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Spiked Club": {
        "id": 1107,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Hammer": {
        "id": 1108,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Monk's Flamemace": {
        "id": 1109,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Envoy's Horn": {
        "id": 1110,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Scepter of the All-Knowing": {
        "id": 1111,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Nox Flowing Hammer": {
        "id": 1112,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Ringed Finger": {
        "id": 1113,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Stone Club": {
        "id": 1114,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Marika's Hammer": {
        "id": 1115,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Large Club": {
        "id": 1200,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Greathorn Hammer": {
        "id": 1201,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Battle Hammer": {
        "id": 1202,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Great Mace": {
        "id": 1206,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Curved Great Club": {
        "id": 1208,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Celebrant's Skull": {
        "id": 1213,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Pickaxe": {
        "id": 1214,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Beastclaw Greathammer": {
        "id": 1215,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Envoy's Long Horn": {
        "id": 1216,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Cranial Vessel Candlestand": {
        "id": 1217,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Great Stars": {
        "id": 1218,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Brick Hammer": {
        "id": 1219,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Devourer's Scepter": {
        "id": 1220,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Rotten Battle Hammer": {
        "id": 1221,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Nightrider Flail": {
        "id": 1300,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Flail": {
        "id": 1301,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Family Heads": {
        "id": 1302,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Bastard's Stars": {
        "id": 1303,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Chainlink Flail": {
        "id": 1304,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Battle Axe": {
        "id": 1400,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Forked Hatchet": {
        "id": 1401,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Hand Axe": {
        "id": 1402,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Jawbone Axe": {
        "id": 1403,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Iron Cleaver": {
        "id": 1404,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Ripple Blade": {
        "id": 1405,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Celebrant's Cleaver": {
        "id": 1406,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Icerind Hatchet": {
        "id": 1408,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Highland Axe": {
        "id": 1410,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Sacrificial Axe": {
        "id": 1411,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Rosus' Axe": {
        "id": 1412,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Stormhawk Axe": {
        "id": 1414,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Greataxe": {
        "id": 1500,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Warped Axe": {
        "id": 1501,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Great Omenkiller Cleaver": {
        "id": 1502,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Crescent Moon Axe": {
        "id": 1503,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Axe of Godrick": {
        "id": 1504,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Longhaft Axe": {
        "id": 1505,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Rusted Anchor": {
        "id": 1506,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Executioner's Greataxe": {
        "id": 1508,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Winged Greathorn": {
        "id": 1511,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Butchering Knife": {
        "id": 1512,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Gargoyle's Great Axe": {
        "id": 1513,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Gargoyle's Black Axe": {
        "id": 1514,
        "recipe": [
            (1, Materials.AxeHandle),
        ],
    },
    "Short Spear": {
        "id": 1600,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Spear": {
        "id": 1601,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Crystal Spear": {
        "id": 1602,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Clayman's Harpoon": {
        "id": 1603,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Cleanrot Spear": {
        "id": 1604,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Partisan": {
        "id": 1605,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Celebrant's Rib-Rake": {
        "id": 1606,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Pike": {
        "id": 1607,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Torchpole": {
        "id": 1608,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Bolt of Gransax": {
        "id": 1609,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Cross-Naginata": {
        "id": 1611,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Death Ritual Spear": {
        "id": 1612,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Inquisitor's Girandole": {
        "id": 1613,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Spiked Spear": {
        "id": 1614,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Iron Spear": {
        "id": 1615,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Rotten Crystal Spear": {
        "id": 1616,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Sacred Mohgwyn's Spear": {
        "id": 1701,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Siluria's Tree": {
        "id": 1702,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Serpent-Hunter": {
        "id": 1703,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Vyke's War Spear": {
        "id": 1705,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Lance": {
        "id": 1706,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Treespear": {
        "id": 1707,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Halberd": {
        "id": 1800,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Pest's Glaive": {
        "id": 1801,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Lucerne": {
        "id": 1802,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Banished Knight's Halberd": {
        "id": 1803,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Commander's Standard": {
        "id": 1804,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Nightrider Glaive": {
        "id": 1805,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Ripple Crescent Halberd": {
        "id": 1806,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Vulgar Militia Saw": {
        "id": 1807,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Golden Halberd": {
        "id": 1808,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Glaive": {
        "id": 1809,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Loretta's War Sickle": {
        "id": 1810,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Guardian's Swordspear": {
        "id": 1811,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Vulgar Militia Shotel": {
        "id": 1813,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Dragon Halberd": {
        "id": 1814,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Gargoyle's Halberd": {
        "id": 1815,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Gargoyle's Black Halberd": {
        "id": 1816,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Scythe": {
        "id": 1900,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Grave Scythe": {
        "id": 1901,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Halo Scythe": {
        "id": 1902,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Winged Scythe": {
        "id": 1906,
        "recipe": [
            (1, Materials.SpearShaft),
        ],
    },
    "Whip": {
        "id": 2000,
        "recipe": [
            (1, Materials.SmallHilt),
        ],
    },
    "Thorned Whip": {
        "id": 2002,
        "recipe": [
            (1, Materials.SmallHilt),
        ],
    },
    "Magma Whip Candlestick": {
        "id": 2003,
        "recipe": [
            (1, Materials.SmallHilt),
        ],
    },
    "Hoslow's Petal Whip": {
        "id": 2005,
        "recipe": [
            (1, Materials.SmallHilt),
        ],
    },
    "Giant's Red Braid": {
        "id": 2006,
        "recipe": [
            (1, Materials.SmallHilt),
        ],
    },
    "Urumi": {
        "id": 2007,
        "recipe": [
            (1, Materials.SmallHilt),
        ],
    },
    "Caestus": {
        "id": 2100,
        "recipe": [

        ],
    },
    "Spiked Caestus": {
        "id": 2101,
        "recipe": [

        ],
    },
    "Grafted Dragon": {
        "id": 2106,
        "recipe": [

        ],
    },
    "Iron Ball": {
        "id": 2107,
        "recipe": [

        ],
    },
    "Star Fist": {
        "id": 2108,
        "recipe": [

        ],
    },
    "Katar": {
        "id": 2110,
        "recipe": [

        ],
    },
    "Clinging Bone": {
        "id": 2111,
        "recipe": [

        ],
    },
    "Veteran's Prosthesis": {
        "id": 2112,
        "recipe": [

        ],
    },
    "Cipher Pata": {
        "id": 2113,
        "recipe": [

        ],
    },
    "Hookclaws": {
        "id": 2200,
        "recipe": [

        ],
    },
    "Venomous Fang": {
        "id": 2201,
        "recipe": [

        ],
    },
    "Bloodhound Claws": {
        "id": 2202,
        "recipe": [

        ],
    },
    "Raptor Talons": {
        "id": 2203,
        "recipe": [

        ],
    },
    "Prelate's Inferno Crozier": {
        "id": 2300,
        "recipe": [

        ],
    },
    "Watchdog's Staff": {
        "id": 2301,
        "recipe": [

        ],
    },
    "Great Club": {
        "id": 2302,
        "recipe": [

        ],
    },
    "Envoy's Greathorn": {
        "id": 2303,
        "recipe": [

        ],
    },
    "Duelist Greataxe": {
        "id": 2304,
        "recipe": [

        ],
    },
    "Axe of Godfrey": {
        "id": 2305,
        "recipe": [

        ],
    },
    "Dragon Greatclaw": {
        "id": 2306,
        "recipe": [

        ],
    },
    "Staff of the Avatar": {
        "id": 2307,
        "recipe": [

        ],
    },
    "Fallingstar Beast Jaw": {
        "id": 2308,
        "recipe": [

        ],
    },
    "Ghiza's Wheel": {
        "id": 2310,
        "recipe": [

        ],
    },
    "Giant-Crusher": {
        "id": 2311,
        "recipe": [

        ],
    },
    "Golem's Halberd": {
        "id": 2312,
        "recipe": [

        ],
    },
    "Troll's Hammer": {
        "id": 2313,
        "recipe": [

        ],
    },
    "Rotten Staff": {
        "id": 2314,
        "recipe": [

        ],
    },
    "Rotten Greataxe": {
        "id": 2315,
        "recipe": [

        ],
    },
    "Torch": {
        "id": 2400,
        "recipe": [

        ],
    },
    "Steel-Wire Torch": {
        "id": 2402,
        "recipe": [

        ],
    },
    "St. Trina's Torch": {
        "id": 2404,
        "recipe": [

        ],
    },
    "Ghostflame Torch": {
        "id": 2405,
        "recipe": [

        ],
    },
    "Beast-Repellent Torch": {
        "id": 2406,
        "recipe": [

        ],
    },
    "Sentry's Torch": {
        "id": 2407,
        "recipe": [

        ],
    },
    "Buckler": {
        "id": 3000,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Perfumer's Shield": {
        "id": 3001,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Man-Serpent's Shield": {
        "id": 3002,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Rickety Shield": {
        "id": 3003,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Pillory Shield": {
        "id": 3004,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Beastman's Jar-Shield": {
        "id": 3006,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Red Thorn Roundshield": {
        "id": 3007,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Scripture Wooden Shield": {
        "id": 3008,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Riveted Wooden Shield": {
        "id": 3009,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Blue-White Wooden Shield": {
        "id": 3010,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Rift Shield": {
        "id": 3011,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Iron Roundshield": {
        "id": 3012,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Gilded Iron Shield": {
        "id": 3013,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Ice Crest Shield": {
        "id": 3014,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Smoldering Shield": {
        "id": 3015,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Spiralhorn Shield": {
        "id": 3019,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Coil Shield": {
        "id": 3020,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Kite Shield": {
        "id": 3100,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Marred Leather Shield": {
        "id": 3101,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Marred Wooden Shield": {
        "id": 3102,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Banished Knight's Shield": {
        "id": 3103,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Albinauric Shield": {
        "id": 3104,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Sun Realm Shield": {
        "id": 3105,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Silver Mirrorshield": {
        "id": 3106,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Round Shield": {
        "id": 3107,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Scorpion Kite Shield": {
        "id": 3108,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Twinbird Kite Shield": {
        "id": 3109,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Blue-Gold Kite Shield": {
        "id": 3110,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Brass Shield": {
        "id": 3113,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Great Turtle Shell": {
        "id": 3114,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Shield of the Guilty": {
        "id": 3117,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Carian Knight's Shield": {
        "id": 3119,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Large Leather Shield": {
        "id": 3123,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Horse Crest Wooden Shield": {
        "id": 3124,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Candletree Wooden Shield": {
        "id": 3125,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Flame Crest Wooden Shield": {
        "id": 3126,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Hawk Crest Wooden Shield": {
        "id": 3127,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Beast Crest Heater Shield": {
        "id": 3128,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Red Crest Heater Shield": {
        "id": 3129,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Blue Crest Heater Shield": {
        "id": 3130,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Eclipse Crest Heater Shield": {
        "id": 3131,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Inverted Hawk Heater Shield": {
        "id": 3132,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Heater Shield": {
        "id": 3133,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Black Leather Shield": {
        "id": 3134,
        "recipe": [
            (1, Materials.ShieldHandle),
        ],
    },
    "Dragon Towershield": {
        "id": 3200,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Distinguished Greatshield": {
        "id": 3202,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Crucible Hornshield": {
        "id": 3203,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Dragonclaw Shield": {
        "id": 3204,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Briar Greatshield": {
        "id": 3205,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Erdtree Greatshield": {
        "id": 3208,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Golden Beast Crest Shield": {
        "id": 3209,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Jellyfish Shield": {
        "id": 3212,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Fingerprint Stone Shield": {
        "id": 3213,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Icon Shield": {
        "id": 3214,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "One-Eyed Shield": {
        "id": 3215,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Visage Shield": {
        "id": 3216,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Spiked Palisade Shield": {
        "id": 3217,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Manor Towershield": {
        "id": 3219,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Crossed-Tree Towershield": {
        "id": 3220,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Inverted Hawk Towershield": {
        "id": 3221,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Ant's Skull Plate": {
        "id": 3222,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Redmane Greatshield": {
        "id": 3223,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Eclipse Crest Greatshield": {
        "id": 3224,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Cuckoo Greatshield": {
        "id": 3225,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Golden Greatshield": {
        "id": 3226,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Gilded Greatshield": {
        "id": 3227,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Haligtree Crest Greatshield": {
        "id": 3228,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Wooden Greatshield": {
        "id": 3229,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Lordsworn's Shield": {
        "id": 3230,
        "recipe": [
            (1, Materials.GreatshieldHandle),
        ],
    },
    "Glintstone Staff": {
        "id": 3300,
        "recipe": [
            (1, Materials.StaffPole),
        ],
    },
    "Crystal Staff": {
        "id": 3304,
        "recipe": [
            (1, Materials.StaffPole),
        ],
    },
    "Gelmir Glintstone Staff": {
        "id": 3305,
        "recipe": [
            (1, Materials.StaffPole),
        ],
    },
    "Demi-Human Queen's Staff": {
        "id": 3306,
        "recipe": [
            (1, Materials.StaffPole),
        ],
    },
    "Carian Regal Scepter": {
        "id": 3309,
        "recipe": [
            (1, Materials.StaffPole),
        ],
    },
    "Digger's Staff": {
        "id": 3312,
        "recipe": [
            (1, Materials.StaffPole),
        ],
    },
    "Astrologer's Staff": {
        "id": 3313,
        "recipe": [
            (1, Materials.StaffPole),
        ],
    },
    "Carian Glintblade Staff": {
        "id": 3317,
        "recipe": [
            (1, Materials.StaffPole),
        ],
    },
    "Prince of Death's Staff": {
        "id": 3318,
        "recipe": [
            (1, Materials.StaffPole),
        ],
    },
    "Albinauric Staff": {
        "id": 3319,
        "recipe": [
            (1, Materials.StaffPole),
        ],
    },
    "Academy Glintstone Staff": {
        "id": 3320,
        "recipe": [
            (1, Materials.StaffPole),
        ],
    },
    "Carian Glintstone Staff": {
        "id": 3321,
        "recipe": [
            (1, Materials.StaffPole),
        ],
    },
    "Azur's Glintstone Staff": {
        "id": 3323,
        "recipe": [
            (1, Materials.StaffPole),
        ],
    },
    "Lusat's Glintstone Staff": {
        "id": 3324,
        "recipe": [
            (1, Materials.StaffPole),
        ],
    },
    "Meteorite Staff": {
        "id": 3325,
        "recipe": [
            (1, Materials.StaffPole),
        ],
    },
    "Staff of the Guilty": {
        "id": 3326,
        "recipe": [
            (1, Materials.StaffPole),
        ],
    },
    "Rotten Crystal Staff": {
        "id": 3327,
        "recipe": [
            (1, Materials.StaffPole),
        ],
    },
    "Staff of Loss": {
        "id": 3328,
        "recipe": [
            (1, Materials.StaffPole),
        ],
    },
    "Finger Seal": {
        "id": 3400,
        "recipe": [

        ],
    },
    "Godslayer's Seal": {
        "id": 3401,
        "recipe": [

        ],
    },
    "Giant's Seal": {
        "id": 3402,
        "recipe": [

        ],
    },
    "Gravel Stone Seal": {
        "id": 3403,
        "recipe": [

        ],
    },
    "Clawmark Seal": {
        "id": 3404,
        "recipe": [

        ],
    },
    "Golden Order Seal": {
        "id": 3406,
        "recipe": [

        ],
    },
    "Erdtree Seal": {
        "id": 3407,
        "recipe": [

        ],
    },
    "Dragon Communion Seal": {
        "id": 3408,
        "recipe": [

        ],
    },
    "Frenzied Flame Seal": {
        "id": 3409,
        "recipe": [

        ],
    }, #Bookmark for bows
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
            (1, Materials.SoftWood)
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
    "Lion Greatbow": {
        "id": 4200,
        "recipe": [
            (1, Materials.GreatBowGrip),
            (2, Materials.RefinedWood),
            (2, Materials.SomberStoneFragment),
            (2, Materials.Ironshards),
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
            (3, Materials.String)
            (2, Materials.RefinedWood),
            (2, Materials.IronPlate),
        ],
    },
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
}
