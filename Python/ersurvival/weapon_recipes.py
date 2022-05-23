"""Lists the recipes for weapons.

TODO: Region tier guidelines.
    - These should inform rough recipe 'difficulty' and any naturally-found ingredients.
    - New components will be randomly scattered across merchants and dungeons, but bosses will tend to drop more of
      these (and rarer ones) as the game progresses. These can vary in quantity only.
    - That said, 0-4 tier weapons should probably not use any of the new rare components like Meteorite Chunk.
    - Regions:
        0-4: Limgrave/Stormveil
            ErdleafFlower
            TarnishedGoldenSunflower
            String
            RootResin
            Poisonbloom
            MirandaPowder
            OldFang
            Mushroom
            GoldFirefly
            BuddingHorn
            CaveMoss
            SmolderingButterfly
        5-9: Liurnia/Raya Lucaria/Siofra
            Bloodrose
            ArteriaLeaf
            MiquellasLily
            AlbinauricBloodclot
            LivingJarShard
            LumpOfFlesh
            SilverFirefly
            GlintstoneFirefly
            CrystalBud
            BuddingCaveMoss
        10-14: Altus/Mt. Gelmir/Caelid/Nokron
            NascentButterfly
            FormicRock
            CrystalCaveMoss
            Fulgurbloom
            AltusBloom
            GoldenRowa
            GoldenSunflower
            VolcanicStone
            FadedErdleafFlower
            ToxicMushroom
            SilverTearHusk
            SacramentalBud
            GravelStone
            GoldenCentipede
        15-19: Mountaintops and beyond
            AeonianButterfly
            FireBlossom
            RimedRowa
            RimedCrystalBud
            BloodTaintedExcrement
"""
from survival_goods import Materials

SCRATCH_WEAPONS = [
    # Weapons crafted from scratch.
    "Dagger",
    "Club",
    "Hand Axe",
    "Whip",  # +10
    "Caestus",
    "Shortbow",
]

# TODO: Event flags are automatically determined for each weapon/recipe based on its index in this list. If it ever
#  changes, make sure those flags/events are regenerated!
WEAPON_RECIPES = {

    # region Daggers
    "Dagger": {
        "previous": "None",
        "tier": 0,
        "somber": False,
        "id": 100,
        "recipe": [
            (1, Materials.IronPlate),
        ],
    },
    "Black Knife": {
        "previous": "Blade of Calling",
        "tier": 20,
        "somber": True,
        "id": 101,
        "recipe": [
            (1, Materials.IronPlate),
            (1, Materials.BlackMark),
        ],
    },
    "Parrying Dagger": {
        "previous": "Bloodstained Dagger",
        "tier": 9,
        "somber": False,
        "id": 102,
        "recipe": [
            (1, Materials.IronPlate),
            (1, Materials.StoneFragment),
        ],
    },
    "Misericorde": {
        "previous": "Bloodstained Dagger",
        "tier": 9,
        "somber": False,
        "id": 103,
        "recipe": [
            (1, Materials.IronPlate),
            (5, Materials.GraveViolet),
        ],
    },
    "Reduvia": {
        "previous": "Blade of Calling",
        "tier": 20,
        "somber": True,
        "id": 104,
        "recipe": [
            (1, Materials.GruesomeBone),
            (4, Materials.Bloodrose),
        ],
    },
    "Crystal Knife": {
        "previous": "Wakizashi",
        "tier": 15,
        "somber": False,
        "id": 105,
        "recipe": [
            (5, Materials.CrackedCrystal),
            (4, Materials.StoneFragment),
        ],
    },
    "Celebrant's Sickle": {
        "previous": "Misericorde",
        "tier": 12,
        "somber": False,
        "id": 106,
        "recipe": [
            (2, Materials.StoneFragment),
            (4, Materials.HumanBoneShard),
            (6, Materials.TarnishedGoldenSunflower),
        ],
    },
    "Glintstone Kris": {
        "previous": "Crystal Knife",
        "tier": 20,
        "somber": True,
        "id": 107,
        "recipe": [
            (1, Materials.IronPlate),
            (5, Materials.CrystalBud),
            (5, Materials.SomberStoneFragment),
        ],
    },
    "Scorpion's Stinger": {
        "previous": "Ivory Sickle",
        "tier": 20,
        "somber": True,
        "id": 108,
        "recipe": [
            (1, Materials.IronPlate),
            (5, Materials.AeonianButterfly),
            (5, Materials.SomberStoneFragment),
        ],
    },
    "Great Knife": {
        "previous": "Dagger",
        "tier": 3,
        "somber": False,
        "id": 109,
        "recipe": [
            (1, Materials.IronPlate),
            (4, Materials.StoneFragment),
        ],
    },
    "Wakizashi": {
        "previous": "Parrying Dagger",
        "tier": 12,
        "somber": False,
        "id": 110,
        "recipe": [
            (1, Materials.IronPlate),
            (1, Materials.IronShards),
            (5, Materials.StoneFragment),
        ],
    },
    "Cinquedea": {
        "previous": "Wakizashi",
        "tier": 20,
        "somber": True,
        "id": 111,
        "recipe": [
            (5, Materials.SanctuaryStone),
            (2, Materials.BeastBlood),
            (3, Materials.SomberStoneFragment),
        ],
    },
    "Ivory Sickle": {
        "previous": "Celebrant's Sickle",
        "tier": 15,
        "somber": False,
        "id": 113,
        "recipe": [
            (1, Materials.HeftyBeastBone),
            (6, Materials.StoneFragment),
        ],
    },
    "Bloodstained Dagger": {
        "previous": "Great Knife",
        "tier": 6,
        "somber": False,
        "id": 114,
        "recipe": [
            (1, Materials.IronPlate),
            (1, Materials.BeastBlood),
        ],
    },
    "Erdsteel Dagger": {
        "previous": "Wakizashi",
        "tier": 15,
        "somber": False,
        "id": 115,
        "recipe": [
            (1, Materials.IronPlate),
            (1, Materials.ErdtreeWood),
        ],
    },
    "Blade of Calling": {
        "previous": "Erdsteel Dagger",
        "tier": 18,
        "somber": True,
        "id": 116,
        "recipe": [
            (1, Materials.IronPlate),
            (5, Materials.ArteriaLeaf),
        ],
    },
    # endregion

    # region Straight Swords
    "Longsword": {
        "previous": "Weathered Straight Sword",
        "tier": 6,
        "somber": False,
        "id": 200,
        "recipe": [
            (2, Materials.IronPlate),
            (1, Materials.IronShards),
        ],
    },
    "Short Sword": {
        "previous": "Dagger",
        "tier": 2,
        "somber": False,
        "id": 201,
        "recipe": [
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
        ],
    },
    "Broadsword": {
        "previous": "Longsword",
        "tier": 8,
        "somber": False,
        "id": 202,
        "recipe": [
            (2, Materials.IronPlate),
        ],
    },
    "Lordsworn's Straight Sword": {
        "previous": "Broadsword",
        "tier": 10,
        "somber": False,
        "id": 204,
        "recipe": [
            (2, Materials.IronPlate),
            (1, Materials.RootResin),
        ],
    },
    "Weathered Straight Sword": {
        "previous": "Short Sword",
        "tier": 4,
        "somber": False,
        "id": 205,
        "recipe": [
            (4, Materials.IronShards),
        ],
    },
    "Ornamental Straight Sword": {
        "previous": "Lordsworn's Straight Sword",
        "tier": 12,
        "somber": True,
        "id": 206,
        "recipe": [
            (2, Materials.IronPlate),
            (3, Materials.SomberStoneFragment),
            (1, Materials.GoldenCentipede),
        ],
    },
    "Golden Epitaph": {
        "previous": "Coded Sword",
        "tier": 18,
        "somber": True,
        "id": 207,
        "recipe": [
            (2, Materials.IronPlate),
            (4, Materials.StoneFragment),
            (4, Materials.AltusBloom),
            (4, Materials.GoldenSunflower),
        ],
    },
    "Nox Flowing Sword": {
        "previous": "Flowing Curved Sword",
        "tier": 18,
        "somber": True,
        "id": 208,
        "recipe": [
            (1, Materials.LiquidMetal),
            (2, Materials.SilverTearHusk),  # ?
        ],
    },
    "Inseparable Sword": {
        "previous": "Flamberge",
        "tier": 16,
        "somber": True,
        "id": 209,
        "recipe": [
            (3, Materials.IronPlate),
            (4, Materials.SomberStoneFragment),
            (10, Materials.SilverFirefly),
            (10, Materials.GoldFirefly),
        ],
    },
    "Coded Sword": {
        "previous": "Ornamental Straight Sword",
        "tier": 16,
        "somber": True,
        "id": 211,
        "recipe": [
            (3, Materials.SomberStoneFragment),
            (8, Materials.GoldTingedExcrement),
        ],
    },
    "Sword of Night and Flame": {
        "previous": "Carian Knight's Sword",
        "tier": 20,
        "somber": True,
        "id": 214,
        "recipe": [
            (8, Materials.SomberStoneFragment),
            (3, Materials.GlintstoneDust),
            (3, Materials.ErdtreeAmber),
            (2, Materials.MeteoriteChunk),
        ],
    },
    "Crystal Sword": {
        "previous": "Longsword",
        "tier": 8,
        "somber": True,
        "id": 215,
        "recipe": [
            (1, Materials.GlintstoneDust),
            (5, Materials.CrackedCrystal),
        ],
    },
    "Carian Knight's Sword": {
        "previous": "Sword of St. Trina",
        "tier": 16,
        "somber": True,
        "id": 218,
        "recipe": [
            (2, Materials.IronPlate),
            (5, Materials.GlintstoneFirefly),
        ],
    },
    "Sword of St. Trina": {
        "previous": "Lazuli Glintstone Sword",
        "tier": 14,
        "somber": True,
        "id": 219,
        "recipe": [
            (2, Materials.IronPlate),
            (4, Materials.StoneFragment),
            (2, Materials.SlumberingEgg),
            (7, Materials.TrinasLily),
        ],
    },
    "Miquellan Knight's Sword": {
        "previous": "Golden Epitaph",
        "tier": 20,
        "somber": True,
        "id": 220,
        "recipe": [
            (2, Materials.IronPlate),
            (1, Materials.ErdtreeAmber),
        ],
    },
    "Cane Sword": {
        "previous": "Noble's Slender Sword",
        "tier": 15,
        "somber": False,
        "id": 221,
        "recipe": [
            (1, Materials.SoftWood),
            (3, Materials.IronShards),
        ],
    },
    "Regalia of Eochaid": {
        "previous": "Warhawk's Talon",
        "tier": 20,
        "somber": True,
        "id": 222,
        "recipe": [
            (2, Materials.IronPlate),
            (1, Materials.GruesomeBone),
            (10, Materials.SacramentalBud),
        ],
    },
    "Noble's Slender Sword": {
        "previous": "Lordsworn's Straight Sword",
        "tier": 12,
        "somber": False,
        "id": 223,
        "recipe": [
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
            (1, Materials.TarnishedGoldenSunflower),
        ],
    },
    "Warhawk's Talon": {
        "previous": "Cane Sword",
        "tier": 18,
        "somber": False,
        "id": 224,
        "recipe": [
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
            (2, Materials.StoneFragment),
        ],
    },
    "Lazuli Glintstone Sword": {
        "previous": "Rotten Crystal Sword",
        "tier": 12,
        "somber": True,
        "id": 225,
        "recipe": [
            (2, Materials.SoftWood),
            (1, Materials.GlintstoneDust),
        ],
    },
    "Rotten Crystal Sword": {
        "previous": "Crystal Sword",
        "tier": 10,
        "somber": True,
        "id": 226,
        "recipe": [
            (1, Materials.GruesomeBone),
            (8, Materials.SomberStoneFragment),
            (10, Materials.CrackedCrystal),
        ],
    },
    # endregion

    # region Greatswords
    "Bastard Sword": {
        "previous": "Broadsword",
        "tier": 9,
        "somber": False,
        "id": 300,
        "recipe": [
            (3, Materials.IronPlate),
        ],
    },
    "Forked Greatsword": {
        "previous": "Claymore",
        "tier": 12,
        "somber": False,
        "id": 301,
        "recipe": [
            (2, Materials.IronPlate),
            (5, Materials.IronShards),
            (4, Materials.StoneFragment),
            (4, Materials.GraveViolet),
        ],
    },
    "Iron Greatsword": {
        "previous": "Banished Knight's Greatsword",
        "tier": 15,
        "somber": False,
        "id": 302,
        "recipe": [
            (3, Materials.IronPlate),
            (1, Materials.IronShards),
            (2, Materials.StoneFragment),
        ],
    },
    "Lordsworn's Greatsword": {
        "previous": "Claymore",
        "tier": 12,
        "somber": False,
        "id": 303,
        "recipe": [
            (2, Materials.IronPlate),
            (2, Materials.IronShards),
        ],
    },
    "Knight's Greatsword": {
        "previous": "Banished Knight's Greatsword",
        "tier": 15,
        "somber": False,
        "id": 304,
        "recipe": [
            (1, Materials.SoftWood),
            (2, Materials.IronPlate),
            (2, Materials.IronShards),
        ],
    },
    "Flamberge": {
        "previous": "Forked Greatsword",
        "tier": 14,
        "somber": False,
        "id": 305,
        "recipe": [
            (1, Materials.IronPlate),
            (5, Materials.IronShards),
            (1, Materials.Bloodrose),
        ],
    },
    "Ordovis's Greatsword": {
        "previous": "Blasphemous Blade",
        "tier": 20,
        "somber": True,
        "id": 306,
        "recipe": [
            (2, Materials.RefinedWood),
            (2, Materials.IronPlate),
            (6, Materials.SomberStoneFragment),
            (2, Materials.ErdtreeAmber),
        ],
    },
    "Alabaster Lord's Sword": {
        "previous": "Knight's Greatsword",
        "tier": 16,
        "somber": True,
        "id": 307,
        "recipe": [
            (8, Materials.StoneFragment),
            (1, Materials.GlintstoneDust),
            (1, Materials.MeteoriteChunk),
        ],
    },
    "Banished Knight's Greatsword": {
        "previous": "Lordsworn's Greatsword",
        "tier": 14,
        "somber": False,
        "id": 308,
        "recipe": [
            (3, Materials.IronPlate),
            (10, Materials.SanctuaryStone),
        ],
    },
    "Dark Moon Greatsword": {
        "previous": "Helphen's Steeple",
        "tier": 20,
        "somber": True,
        "id": 309,
        "recipe": [
            (3, Materials.IronPlate),
            (2, Materials.LiquidMetal),
            (10, Materials.SomberStoneFragment),
        ],
    },
    "Sacred Relic Sword": {
        "previous": "Inseparable Sword",
        "tier": 20,
        "somber": True,
        "id": 310,
        "recipe": [
            (1, Materials.Remembrance_EldenBeast),
            (6, Materials.ErdtreeAmber),
            (20, Materials.LumpOfFlesh),
            (14, Materials.GoldenCentipede),
        ],
    },
    "Helphen's Steeple": {
        "previous": "Alabaster Lord's Sword",
        "tier": 18,
        "somber": True,
        "id": 313,
        "recipe": [
            (1, Materials.LiquidMetal),
            (1, Materials.BlackMark),
            (4, Materials.HumanBoneShard),
        ],
    },
    "Blasphemous Blade": {
        "previous": "Knight's Greatsword",
        "tier": 18,
        "somber": True,
        "id": 314,
        "recipe": [
            (1, Materials.Remembrance_Rykard),
            (3, Materials.IronPlate),
            (6, Materials.BeastBlood),
            (4, Materials.BloodTaintedExcrement),
        ],
    },
    "Marais Executioner's Sword": {
        "previous": "Knight's Greatsword",
        "tier": 20,
        "somber": True,
        "id": 315,
        "recipe": [
            (2, Materials.IronPlate),
            (1, Materials.LiquidMetal),
            (1, Materials.GruesomeBone),
        ],
    },
    "Sword of Milos": {
        "previous": "Flamberge",
        "tier": 16,
        "somber": True,
        "id": 316,
        "recipe": [
            (3, Materials.IronPlate),
            (4, Materials.HeftyBeastBone),
            (1, Materials.FormicRock),
        ],
    },
    "Golden Order Greatsword": {
        "previous": "Inseparable Sword",
        "tier": 20,
        "somber": True,
        "id": 317,
        "recipe": [
            (3, Materials.IronPlate),
            (10, Materials.SomberStoneFragment),
            (4, Materials.ErdtreeAmber),
            (1, Materials.GoldenSunflower),
        ],
    },
    "Claymore": {
        "previous": "Bastard Sword",
        "tier": 10,
        "somber": False,
        "id": 318,
        "recipe": [
            (3, Materials.IronPlate),
            (2, Materials.StoneFragment),
        ],
    },
    "Gargoyle's Greatsword": {
        "previous": "Knight's Greatsword",
        "tier": 18,
        "somber": False,
        "id": 319,
        "recipe": [
            (3, Materials.IronPlate),
            (12, Materials.StoneFragment),
            (4, Materials.RootResin),
            (4, Materials.MeltedMushroom),
        ],
    },
    "Death's Poker": {
        "previous": "Sword of Milos",
        "tier": 20,
        "somber": True,
        "id": 320,
        "recipe": [
            (2, Materials.SomberStoneFragment),
            (2, Materials.BuddingHorn),
            (4, Materials.HumanBoneShard),
        ],
    },
    "Gargoyle's Blackblade": {
        "previous": "Gargoyle's Greatsword",
        "tier": 20,
        "somber": True,
        "id": 321,
        "recipe": [
            (2, Materials.IronPlate),
            (1, Materials.BlackMark),
            (1, Materials.ErdtreeAmber),
            (2, Materials.MeltedMushroom),
        ],
    },
    "Greatsword": {
        "previous": "Watchdog's Greatsword",
        "tier": 18,
        "somber": False,
        "id": 400,
        "recipe": [
            (3, Materials.IronPlate),
            (1, Materials.SomberStoneFragment),
        ],
    },
    "Watchdog's Greatsword": {
        "previous": "Zweihander",
        "tier": 17,
        "somber": False,
        "id": 401,
        "recipe": [
            (6, Materials.StoneFragment),
            (4, Materials.SomberStoneFragment),
            (2, Materials.GraveViolet),
        ],
    },
    "Maliketh's Black Blade": {
        "previous": "Watchdog's Greatsword",
        "tier": 20,
        "somber": True,
        "id": 402,
        "recipe": [
            (1, Materials.Remembrance_Maliketh),
            (4, Materials.IronPlate),
            (14, Materials.SomberStoneFragment),
            (2, Materials.BlackMark),
        ],
    },
    "Troll's Golden Sword": {
        "previous": "Zweihander",
        "tier": 17,
        "somber": False,
        "id": 403,
        "recipe": [
            (4, Materials.IronPlate),
            (2, Materials.GoldTingedExcrement),
        ],
    },
    "Zweihander": {
        "previous": "Iron Greatsword",
        "tier": 16,
        "somber": False,
        "id": 404,
        "recipe": [
            (4, Materials.IronPlate),
            (2, Materials.StoneFragment),
        ],
    },
    "Starscourge Greatsword": {
        "previous": "Watchdog's Greatsword",
        "tier": 20,
        "somber": True,
        "id": 405,
        "recipe": [
            (1, Materials.Remembrance_Radahn),
            (3, Materials.IronPlate),
            (2, Materials.LiquidMetal),
            (1, Materials.GlintstoneDust),
        ],
    },
    "Royal Greatsword": {
        "previous": "Troll Knight's Sword",
        "tier": 20,
        "somber": True,
        "id": 406,
        "recipe": [
            (4, Materials.IronPlate),
            (4, Materials.AeonianButterfly),
        ],
    },
    "Godslayer's Greatsword": {
        "previous": "Troll Knight's Sword",
        "tier": 20,
        "somber": True,
        "id": 407,
        "recipe": [
            (4, Materials.IronPlate),
            (2, Materials.BlackMark),
            (4, Materials.SmolderingButterfly),
        ],
    },
    "Ruins Greatsword": {
        "previous": "Greatsword",
        "tier": 20,
        "somber": True,
        "id": 408,
        "recipe": [
            (1, Materials.MeteoriteChunk),
            (4, Materials.SomberStoneFragment),
            (20, Materials.SanctuaryStone),
        ],
    },
    "Grafted Blade Greatsword": {
        "previous": "Greatsword",
        "tier": 20,
        "somber": True,
        "id": 410,
        "recipe": [
            (12, Materials.IronShards),
        ],
    },
    "Troll Knight's Sword": {
        "previous": "Troll's Golden Sword",
        "tier": 18,
        "somber": True,
        "id": 411,
        "recipe": [
            (4, Materials.IronPlate),
            (2, Materials.GlintstoneFirefly),
        ],
    },
    # endregion

    # region Thrusting Swords
    "Estoc": {
        "previous": "Noble's Estoc",
        "tier": 12,
        "somber": False,
        "id": 500,
        "recipe": [
            (2, Materials.IronPlate),
            (1, Materials.IronShards),
        ],
    },
    "Cleanrot Knight's Sword": {
        "previous": "Estoc",
        "tier": 14,
        "somber": False,
        "id": 501,
        "recipe": [
            (1, Materials.SoftWood),
            (2, Materials.IronPlate),
            (1, Materials.ErdtreeAmber),
        ],
    },
    "Rapier": {
        "previous": "Longsword",
        "tier": 8,
        "somber": False,
        "id": 502,
        "recipe": [
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
        ],
    },
    "Rogier's Rapier": {
        "previous": "Estoc",
        "tier": 14,
        "somber": False,
        "id": 503,
        "recipe": [
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
            (5, Materials.StoneFragment),
        ],
    },
    "Antspur Rapier": {
        "previous": "Rogier's Rapier",
        "tier": 17,
        "somber": False,
        "id": 504,
        "recipe": [
            (1, Materials.RefinedWood),
            (1, Materials.LiquidMetal),
            (8, Materials.ToxicMushroom),
            (4, Materials.FormicRock),
        ],
    },
    "Frozen Needle": {
        "previous": "Antspur Rapier",
        "tier": 20,
        "somber": True,
        "id": 505,
        "recipe": [
            (1, Materials.IronPlate),
            (1, Materials.LiquidMetal),
            (1, Materials.GlintstoneDust),
        ],
    },
    "Noble's Estoc": {
        "previous": "Rapier",
        "tier": 10,
        "somber": False,
        "id": 506,
        "recipe": [
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
            (1, Materials.TarnishedGoldenSunflower),
        ],
    },
    "Bloody Helice": {
        "previous": "Godskin Stitcher",
        "tier": 20,
        "somber": True,
        "id": 600,
        "recipe": [
            (1, Materials.IronPlate),
            (1, Materials.GruesomeBone),
            (2, Materials.BeastBlood),
            (8, Materials.LumpOfFlesh),
        ],
    },
    "Godskin Stitcher": {
        "previous": "Great Epee",
        "tier": 17,
        "somber": False,
        "id": 601,
        "recipe": [
            (3, Materials.IronPlate),
            (2, Materials.SomberStoneFragment),
            (4, Materials.StripOfWhiteFlesh),
        ],
    },
    "Great Epee": {  # NOTE: Typo in name is from Yapped (leave it)
        "id": 602,
        "recipe": [
            (3, Materials.IronPlate),
            (1, Materials.IronShards),
        ],
    },
    "Dragon King's Cragblade": {
        "previous": "Godskin Stitcher",
        "tier": 20,
        "somber": True,
        "id": 604,
        "recipe": [
            (1, Materials.Remembrance_Dragonlord),
            (2, Materials.DragonTeeth),
            (14, Materials.StoneFragment),
            (10, Materials.GravelStone),
        ],
    },
    # endregion

    # region Curved Swords / Curved Greatswords
    "Falchion": {
        "previous": "Shamshir",
        "tier": 8,
        "somber": False,
        "id": 700,
        "recipe": [
            (2, Materials.IronPlate),
        ],
    },
    "Beastman's Curved Sword": {
        "previous": "Serpent-God's Curved Sword",
        "tier": 12,
        "somber": False,
        "id": 701,
        "recipe": [
            (1, Materials.IronPlate),
            (1, Materials.IronShards),
            (4, Materials.ThinBeastBones),
        ],
    },
    "Shotel": {
        "previous": "Flowing Curved Sword",
        "tier": 18,
        "somber": False,
        "id": 702,
        "recipe": [
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
            (2, Materials.StoneFragment),
        ],
    },
    "Shamshir": {
        "previous": "Scimitar",
        "tier": 6,
        "somber": False,
        "id": 703,
        "recipe": [
            (1, Materials.IronPlate),
            (1, Materials.IronShards),
            (2, Materials.ThinBeastBones),
        ],
    },
    "Bandit's Curved Sword": {
        "previous": "Shamshir",
        "tier": 8,
        "somber": False,
        "id": 704,
        "recipe": [
            (2, Materials.IronPlate),
            (1, Materials.IronShards),
            (1, Materials.RootResin),
        ],
    },
    "Magma Blade": {
        "previous": "Nox Flowing Sword",
        "tier": 20,
        "somber": True,
        "id": 705,
        "recipe": [
            (8, Materials.StoneFragment),
            (6, Materials.VolcanicStone),
        ],
    },
    "Flowing Curved Sword": {
        "previous": "Mantis Blade",
        "tier": 15,
        "somber": False,
        "id": 706,
        "recipe": [
            (2, Materials.IronPlate),
            (1, Materials.SomberStoneFragment),
        ],
    },
    "Wing of Astel": {
        "previous": "Nox Flowing Sword",
        "tier": 20,
        "somber": True,
        "id": 707,
        "recipe": [
            (1, Materials.MeteoriteChunk),
            (2, Materials.GlintstoneDust),
        ],
    },
    "Scavenger's Curved Sword": {
        "previous": "Falchion",
        "tier": 10,
        "somber": False,
        "id": 708,
        "recipe": [
            (4, Materials.IronShards),
            (5, Materials.CaveMoss),
        ],
    },
    "Eclipse Shotel": {
        "previous": "Shotel",
        "tier": 20,
        "somber": True,
        "id": 710,
        "recipe": [
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
            (1, Materials.BlackMark),
        ],
    },
    "Serpent-God's Curved Sword": {
        "previous": "Bandit's Curved Sword",
        "tier": 10,
        "somber": False,
        "id": 711,
        "recipe": [
            (2, Materials.IronPlate),
            (4, Materials.SacramentalBud),
        ],
    },
    "Mantis Blade": {
        "previous": "Scavenger's Curved Sword",
        "tier": 12,
        "somber": False,
        "id": 712,
        "recipe": [
            (1, Materials.IronPlate),
            (1, Materials.IronShards),
            (1, Materials.String),
            (1, Materials.RootResin),
        ],
    },
    "Scimitar": {
        "previous": "Short Sword",
        "tier": 4,
        "somber": False,
        "id": 714,
        "recipe": [
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
        ],
    },
    "Grossmesser": {
        "previous": "Beastman's Curved Sword",
        "tier": 14,
        "somber": False,
        "id": 715,
        "recipe": [
            (2, Materials.IronPlate),
        ],
    },
    "Onyx Lord's Greatsword": {
        "previous": "Omen Cleaver",
        "tier": 20,
        "somber": True,
        "id": 801,
        "recipe": [
            (3, Materials.SomberStoneFragment),
            (1, Materials.GlintstoneDust),
            (1, Materials.MeteoriteChunk),
        ],
    },
    "Dismounter": {
        "previous": "Grossmesser",
        "tier": 16,
        "somber": False,
        "id": 802,
        "recipe": [
            (3, Materials.IronPlate),
        ],
    },
    "Bloodhound's Fang": {
        "previous": "Zamor Curved Sword",
        "tier": 18,
        "somber": True,
        "id": 803,
        "recipe": [
            (2, Materials.IronPlate),
            (2, Materials.IronShards),
        ],
    },
    "Magma Wyrm's Scalesword": {
        "previous": "Omen Cleaver",
        "tier": 20,
        "somber": True,
        "id": 804,
        "recipe": [
            (1, Materials.DragonTeeth),
            (4, Materials.VolcanicStone),
        ],
    },
    "Zamor Curved Sword": {
        "previous": "Monk's Flameblade",
        "tier": 16,
        "somber": True,
        "id": 805,
        "recipe": [
            (2, Materials.IronPlate),
            (2, Materials.GlintstoneDust),
            (4, Materials.RimedCrystalBud),
        ],
    },
    "Omen Cleaver": {
        "previous": "Dismounter",
        "tier": 18,
        "somber": False,
        "id": 806,
        "recipe": [
            (2, Materials.IronPlate),
            (2, Materials.IronShards),
            (6, Materials.Herba),
        ],
    },
    "Monk's Flameblade": {
        "previous": "Scavenger's Curved Sword",
        "tier": 12,
        "somber": False,
        "id": 807,
        "recipe": [
            (1, Materials.IronPlate),
            (4, Materials.IronShards),
            (2, Materials.SomberStoneFragment),
        ],
    },
    "Beastman's Cleaver": {
        "previous": "Omen Cleaver",
        "tier": 20,
        "somber": False,
        "id": 808,
        "recipe": [
            (4, Materials.IronPlate),
            (2, Materials.HeftyBeastBone),
            (2, Materials.StoneFragment),
        ],
    },
    "Morgott's Cursed Sword": {
        "previous": "Bloodhound's Fang",
        "tier": 20,
        "somber": True,
        "id": 810,
        "recipe": [
            (1, Materials.Remembrance_Morgott),
            (1, Materials.GruesomeBone),
            (4, Materials.BeastBlood),
            (6, Materials.ArteriaLeaf),
        ],
    },
    # endregion

    # region Katanas
    "Uchigatana": {
        "previous": "Scavenger's Curved Sword",
        "tier": 12,
        "somber": False,
        "id": 900,
        "recipe": [
            (2, Materials.IronPlate),
            (2, Materials.StoneFragment),
        ],
    },
    "Nagakiba": {
        "previous": "Serpentbone Blade",
        "tier": 17,
        "somber": False,
        "id": 901,
        "recipe": [
            (3, Materials.IronPlate),
            (4, Materials.StoneFragment),
            (2, Materials.FourToedFowlFoot),
        ],
    },
    "Hand of Malenia": {
        "previous": "Nagakiba",
        "tier": 20,
        "somber": True,
        "id": 902,
        "recipe": [
            (1, Materials.Remembrance_Malenia),
            (4, Materials.RefinedWood),
            (2, Materials.LiquidMetal),
            (8, Materials.MiquellasLily),
        ],
    },
    "Meteoric Ore Blade": {
        "previous": "Serpentbone Blade",
        "tier": 18,
        "somber": True,
        "id": 903,
        "recipe": [
            (2, Materials.SomberStoneFragment),
            (1, Materials.MeteoriteChunk),
        ],
    },
    "Rivers of Blood": {
        "previous": "Dragonscale Blade",
        "tier": 20,
        "somber": True,
        "id": 904,
        "recipe": [
            (1, Materials.RefinedWood),
            (2, Materials.IronPlate),
            (2, Materials.GruesomeBone),
            (6, Materials.Bloodrose),
        ],
    },
    "Moonveil": {
        "previous": "Meteoric Ore Blade",
        "tier": 20,
        "somber": True,
        "id": 906,
        "recipe": [
            (4, Materials.SomberStoneFragment),
            (4, Materials.GlintstoneDust),
            (6, Materials.NascentButterfly),
        ],
    },
    "Dragonscale Blade": {
        "previous": "Serpentbone Blade",
        "tier": 16,
        "somber": True,
        "id": 907,
        "recipe": [
            (1, Materials.DragonTeeth),
            (2, Materials.SomberStoneFragment),
            (4, Materials.GravelStone),
        ],
    },
    "Serpentbone Blade": {
        "previous": "Uchigatana",
        "tier": 15,
        "somber": False,
        "id": 908,
        "recipe": [
            (4, Materials.IronShards),
            (8, Materials.MirandaPowder),
            (16, Materials.Poisonbloom),
        ],
    },
    # endregion

    # region Twinblades
    "Twinblade": {
        "previous": "Lordsworn's Straight Sword",
        "tier": 12,
        "somber": False,
        "id": 1000,
        "recipe": [
            (2, Materials.IronPlate),
            (2, Materials.IronShards),
        ],
    },
    "Godskin Peeler": {
        "previous": "Twinned Knight Swords",
        "tier": 16,
        "somber": False,
        "id": 1001,
        "recipe": [
            (2, Materials.IronPlate),
            (1, Materials.BlackMark),
        ],
    },
    "Twinned Knight Swords": {
        "previous": "Twinblade",
        "tier": 14,
        "somber": False,
        "id": 1003,
        "recipe": [
            (3, Materials.IronPlate),
            (2, Materials.MeltedMushroom),
        ],
    },
    "Eleonora's Poleblade": {
        "previous": "Godskin Peeler",
        "tier": 20,
        "somber": True,
        "id": 1005,
        "recipe": [
            (3, Materials.IronPlate),
            (8, Materials.Bloodrose),
        ],
    },
    "Gargoyle's Twinblade": {
        "previous": "Twinned Knight Swords",
        "tier": 17,
        "somber": False,
        "id": 1008,
        "recipe": [
            (3, Materials.IronPlate),
            (12, Materials.StoneFragment),
            (2, Materials.RootResin),
            (4, Materials.MeltedMushroom),
        ],
    },
    "Gargoyle's Black Blades": {
        "previous": "Gargoyle's Twinblade",
        "tier": 20,
        "somber": True,
        "id": 1009,
        "recipe": [
            (3, Materials.IronPlate),
            (1, Materials.BlackMark),
            (1, Materials.ErdtreeAmber),
            (2, Materials.MeltedMushroom),
        ],
    },
    # endregion

    # region Hammers
    "Mace": {
        "previous": "Spiked Club",
        "tier": 9,
        "somber": False,
        "id": 1100,
        "recipe": [
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
        ],
    },
    "Club": {
        "previous": "None",
        "tier": 0,
        "somber": False,
        "id": 1101,
        "recipe": [
            (2, Materials.SoftWood),
        ],
    },
    "Curved Club": {
        "previous": "Club",
        "tier": 3,
        "somber": False,
        "id": 1103,
        "recipe": [
            (1, Materials.RefinedWood),
            (1, Materials.SoftWood),
        ],
    },
    "Warpick": {
        "previous": "Club",
        "tier": 3,
        "somber": False,
        "id": 1104,
        "recipe": [
            (2, Materials.IronPlate),
        ],
    },
    "Morning Star": {
        "previous": "Mace",
        "tier": 12,
        "somber": False,
        "id": 1105,
        "recipe": [
            (2, Materials.IronPlate),
            (2, Materials.IronShards),
            (6, Materials.StoneFragment),
        ],
    },
    "Varre's Bouquet": {
        "previous": "Monk's Flamemace",
        "tier": 20,
        "somber": True,
        "id": 1106,
        "recipe": [
            (4, Materials.IronShards),
            (8, Materials.Bloodrose),
        ],
    },
    "Spiked Club": {
        "previous": "Curved Club",
        "tier": 6,
        "somber": False,
        "id": 1107,
        "recipe": [
            (1, Materials.RefinedWood),
            (4, Materials.OldFang),
        ],
    },
    "Hammer": {
        "previous": "Warpick",
        "tier": 6,
        "somber": False,
        "id": 1108,
        "recipe": [
            (4, Materials.StoneFragment),
            (8, Materials.SanctuaryStone),
        ],
    },
    "Monk's Flamemace": {
        "previous": "Morning Star",
        "tier": 16,
        "somber": False,
        "id": 1109,
        "recipe": [
            (1, Materials.IronPlate),
            (4, Materials.IronShards),
            (2, Materials.SomberStoneFragment),
        ],
    },
    "Envoy's Horn": {
        "previous": "Ringed Finger",
        "tier": 16,
        "somber": True,
        "id": 1110,
        "recipe": [
            (2, Materials.IronPlate),
            (6, Materials.AltusBloom),
        ],
    },
    "Scepter of the All-Knowing": {
        "previous": "Monk's Flamemace",
        "tier": 20,
        "somber": True,
        "id": 1111,
        "recipe": [
            (2, Materials.IronPlate),
            (1, Materials.AlbinauricBloodclot),
            (2, Materials.SilverFirefly),
        ],
    },
    "Nox Flowing Hammer": {
        "previous": "Ringed Finger",
        "tier": 20,
        "somber": True,
        "id": 1112,
        "recipe": [
            (1, Materials.LiquidMetal),
            (4, Materials.SilverTearHusk),  # ?
        ],
    },
    "Ringed Finger": {
        "previous": "Stone Club",
        "tier": 14,
        "somber": True,
        "id": 1113,
        "recipe": [
            (1, Materials.LiquidMetal),
            (10, Materials.LivingJarShard),
            (6, Materials.LumpOfFlesh),
            (4, Materials.BeastBlood),
        ],
    },
    "Stone Club": {
        "previous": "Hammer",
        "tier": 9,
        "somber": False,
        "id": 1114,
        "recipe": [
            (6, Materials.SomberStoneFragment),
            (2, Materials.GlintstoneDust),
        ],
    },
    "Marika's Hammer": {
        "previous": "Envoy's Horn",
        "tier": 20,
        "somber": True,
        "id": 1115,
        "recipe": [
            (1, Materials.Remembrance_EldenBeast),
            (4, Materials.ErdtreeAmber),
            (10, Materials.SomberStoneFragment),
        ],
    },
    # endregion / Hammers

    # region Greathammers
    "Large Club": {
        "previous": "Stone Club",
        "tier": 10,
        "somber": False,
        "id": 1200,
        "recipe": [
            (4, Materials.SoftWood),
        ],
    },
    "Greathorn Hammer": {
        "previous": "Pickaxe",
        "tier": 16,
        "somber": False,
        "id": 1201,
        "recipe": [
            (4, Materials.StoneFragment),
            (6, Materials.HeftyBeastBone),
        ],
    },
    "Battle Hammer": {
        "previous": "Pickaxe",
        "tier": 16,
        "somber": False,
        "id": 1202,
        "recipe": [
            (4, Materials.IronPlate),
        ],
    },
    "Great Mace": {
        "previous": "Large Club",
        "tier": 12,
        "somber": False,
        "id": 1206,
        "recipe": [
            (3, Materials.IronPlate),
            (2, Materials.IronShards),
            (2, Materials.SomberStoneFragment),
        ],
    },
    "Curved Great Club": {
        "previous": "Large Club",
        "tier": 12,
        "somber": False,
        "id": 1208,
        "recipe": [
            (1, Materials.RefinedWood),
            (3, Materials.SoftWood),
        ],
    },
    "Celebrant's Skull": {
        "previous": "Large Club",
        "tier": 12,
        "somber": False,
        "id": 1213,
        "recipe": [
            (4, Materials.StoneFragment),
            (3, Materials.HeftyBeastBone),
            (8, Materials.HumanBoneShard),
        ],
    },
    "Pickaxe": {
        "previous": "Curved Great Club",
        "tier": 14,
        "somber": False,
        "id": 1214,
        "recipe": [
            (1, Materials.RefinedWood),
            (2, Materials.IronPlate),
            (2, Materials.StoneFragment),
        ],
    },
    "Beastclaw Greathammer": {
        "previous": "Celebrant's Skull",
        "tier": 16,
        "somber": True,
        "id": 1215,
        "recipe": [
            (4, Materials.SomberStoneFragment),
            (3, Materials.BeastBlood),
        ],
    },
    "Envoy's Long Horn": {
        "previous": "Envoy's Horn",
        "tier": 18,
        "somber": True,
        "id": 1216,
        "recipe": [
            (3, Materials.IronPlate),
            (1, Materials.ErdtreeAmber),
            (6, Materials.AltusBloom),
        ],
    },
    "Cranial Vessel Candlestand": {
        "previous": "Rotten Battle Hammer",
        "tier": 20,
        "somber": True,
        "id": 1217,
        "recipe": [
            (1, Materials.GruesomeBone),
            (12, Materials.SmolderingButterfly),
            (4, Materials.VolcanicStone),
        ],
    },
    "Great Stars": {
        "previous": "Monk's Flamemace",
        "tier": 20,
        "somber": False,
        "id": 1218,
        "recipe": [
            (3, Materials.IronPlate),
            (2, Materials.IronShards),
            (6, Materials.SomberStoneFragment),
            (5, Materials.BloodTaintedExcrement),
        ],
    },
    "Brick Hammer": {
        "previous": "Great Mace",
        "tier": 14,
        "somber": False,
        "id": 1219,
        "recipe": [
            (15, Materials.StoneFragment),
            (15, Materials.SanctuaryStone),
            (4, Materials.RootResin),
        ],
    },
    "Devourer's Scepter": {
        "previous": "Beastclaw Greathammer",
        "tier": 20,
        "somber": True,
        "id": 1220,
        "recipe": [
            (12, Materials.SomberStoneFragment),
            (3, Materials.GruesomeBone),
        ],
    },
    "Rotten Battle Hammer": {
        "previous": "Battle Hammer",
        "tier": 18,
        "somber": False,
        "id": 1221,
        "recipe": [
            (4, Materials.IronPlate),
            (10, Materials.AeonianButterfly),
            (3, Materials.ToxicMushroom),
            (2, Materials.RimedRowa),
        ],
    },
    # endregion / Great Hammers

    # region Flails
    "Nightrider Flail": {
        "previous": "Flail",
        "tier": 16,
        "somber": False,
        "id": 1300,
        "recipe": [
            (5, Materials.IronShards),
            (2, Materials.SomberStoneFragment),
            (2, Materials.ArteriaLeaf),
        ],
    },
    "Flail": {
        "previous": "Morning Star",
        "tier": 15,
        "somber": False,
        "id": 1301,
        "recipe": [
            (2, Materials.SoftWood),
            (2, Materials.IronShards),
        ],
    },
    "Family Heads": {
        "previous": "Nightrider Flail",
        "tier": 18,
        "somber": True,
        "id": 1302,
        "recipe": [
            (2, Materials.IronPlate),
            (3, Materials.HumanBoneShard),
            (6, Materials.GraveViolet),
        ],
    },
    "Bastard's Stars": {
        "previous": "Family Heads",
        "tier": 20,
        "somber": True,
        "id": 1303,
        "recipe": [
            (1, Materials.Remembrance_Astel),
            (1, Materials.LiquidMetal),
            (1, Materials.MeteoriteChunk),
            (1, Materials.GlintstoneDust),
        ],
    },
    "Chainlink Flail": {
        "previous": "Flail",
        "tier": 18,
        "somber": False,
        "id": 1304,
        "recipe": [
            (1, Materials.RefinedWood),
            (1, Materials.SoftWood),
            (2, Materials.IronShards),
        ],
    },
    # endregion

    # region Axes / Greataxes
    "Battle Axe": {
        "previous": "Hand Axe",
        "tier": 3,
        "somber": False,
        "id": 1400,
        "recipe": [
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
        ],
    },
    "Forked Hatchet": {
        "previous": "Celebrant's Cleaver",
        "tier": 10,
        "somber": False,
        "id": 1401,
        "recipe": [
            (2, Materials.IronPlate),
            (1, Materials.IronShards),
            (2, Materials.GraveViolet),
        ],
    },
    "Hand Axe": {
        "previous": "None",
        "tier": 0,
        "somber": False,
        "id": 1402,
        "recipe": [
            (1, Materials.SoftWood),
            (1, Materials.IronPlate),
        ],
    },
    "Jawbone Axe": {
        "previous": "Highland Axe",
        "tier": 10,
        "somber": False,
        "id": 1403,
        "recipe": [
            (2, Materials.RefinedWood),
            (2, Materials.HeftyBeastBone),
        ],
    },
    "Iron Cleaver": {
        "previous": "Warped Axe",
        "tier": 13,
        "somber": False,
        "id": 1404,
        "recipe": [
            (3, Materials.IronPlate),
            (2, Materials.StoneFragment),
        ],
    },
    "Ripple Blade": {
        "previous": "Icerind Hatchet",
        "tier": 10,
        "somber": False,
        "id": 1405,
        "recipe": [
            (1, Materials.LiquidMetal),
            (4, Materials.SomberStoneFragment),
            (4, Materials.AlbinauricBloodclot),
        ],
    },
    "Celebrant's Cleaver": {
        "previous": "Battle Axe",
        "tier": 5,
        "somber": False,
        "id": 1406,
        "recipe": [
            (3, Materials.StoneFragment),
            (3, Materials.HeftyBeastBone),
            (2, Materials.HumanBoneShard),
        ],
    },
    "Icerind Hatchet": {
        "previous": "Forked Hatchet",
        "tier": 16,
        "somber": True,
        "id": 1408,
        "recipe": [
            (1, Materials.IronPlate),
            (1, Materials.DragonTeeth),
            (2, Materials.RimedCrystalBud),
        ],
    },
    "Highland Axe": {
        "previous": "Celebrant's Cleaver",
        "tier": 8,
        "somber": False,
        "id": 1410,
        "recipe": [
            (2, Materials.SoftWood),
            (2, Materials.IronPlate),
        ],
    },
    "Sacrificial Axe": {
        "previous": "Iron Cleaver",
        "tier": 15,
        "somber": False,
        "id": 1411,
        "recipe": [
            (3, Materials.IronPlate),
            (2, Materials.SomberStoneFragment),
            (2, Materials.GraveViolet),
        ],
    },
    "Rosus' Axe": {
        "previous": "Sacrificial Axe",
        "tier": 20,
        "somber": True,
        "id": 1412,
        "recipe": [
            (1, Materials.RefinedWood),
            (2, Materials.IronPlate),
            (1, Materials.GruesomeBone),
        ],
    },
    "Stormhawk Axe": {
        "previous": "Sacrificial Axe",
        "tier": 20,
        "somber": True,
        "id": 1414,
        "recipe": [
            (3, Materials.IronPlate),
            (4, Materials.Fulgurbloom),
            (2, Materials.FourToedFowlFoot),
            (1, Materials.StormhawkFeather),
        ],
    },
    "Greataxe": {
        "previous": "Rusted Anchor",
        "tier": 14,
        "somber": False,
        "id": 1500,
        "recipe": [
            (2, Materials.SoftWood),
            (2, Materials.IronPlate),
        ],
    },
    "Warped Axe": {
        "previous": "Highland Axe",
        "tier": 10,
        "somber": False,
        "id": 1501,
        "recipe": [
            (4, Materials.IronPlate),
            (2, Materials.RootResin),
        ],
    },
    "Great Omenkiller Cleaver": {
        "previous": "Rusted Anchor",
        "tier": 15,
        "somber": False,
        "id": 1502,
        "recipe": [
            (2, Materials.RefinedWood),
            (2, Materials.StoneFragment),
            (4, Materials.BuddingHorn),
        ],
    },
    "Crescent Moon Axe": {
        "previous": "Great Omenkiller Cleaver",
        "tier": 18,
        "somber": False,
        "id": 1503,
        "recipe": [
            (2, Materials.SoftWood),
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
        ],
    },
    "Axe of Godrick": {
        "previous": "Executioner's Greataxe",
        "tier": 18,
        "somber": True,
        "id": 1504,
        "recipe": [
            (1, Materials.Remembrance_Godrick),
            (4, Materials.IronPlate),
            (4, Materials.GoldenRowa),
            (12, Materials.ErdleafFlower),
        ],
    },
    "Longhaft Axe": {
        "previous": "Warped Axe",
        "tier": 12,
        "somber": False,
        "id": 1505,
        "recipe": [
            (4, Materials.IronPlate),
        ],
    },
    "Rusted Anchor": {
        "previous": "Longhaft Axe",
        "tier": 13,
        "somber": False,
        "id": 1506,
        "recipe": [
            (4, Materials.IronPlate),
            (2, Materials.SomberStoneFragment),
            (4, Materials.FourToedFowlFoot),
        ],
    },
    "Executioner's Greataxe": {
        "previous": "Greataxe",
        "tier": 16,
        "somber": False,
        "id": 1508,
        "recipe": [
            (2, Materials.SoftWood),
            (2, Materials.IronPlate),
            (2, Materials.YellowEmber),
        ],
    },
    "Winged Greathorn": {
        "previous": "Crescent Moon Axe",
        "tier": 20,
        "somber": True,
        "id": 1511,
        "recipe": [
            (1, Materials.Remembrance_RegalAncestor),
            (2, Materials.RefinedWood),
            (2, Materials.BuddingHorn),
            (1, Materials.DewkissedHerba),
        ],
    },
    "Butchering Knife": {
        "previous": "Icerind Hatchet",
        "tier": 20,
        "somber": False,
        "id": 1512,
        "recipe": [
            (4, Materials.IronPlate),
            (2, Materials.SomberStoneFragment),
        ],
    },
    "Gargoyle's Great Axe": {
        "previous": "Great Omenkiller Cleaver",
        "tier": 18,
        "somber": False,
        "id": 1513,
        "recipe": [
            (3, Materials.IronPlate),
            (10, Materials.StoneFragment),
            (8, Materials.MeltedMushroom),
            (3, Materials.RootResin),
        ],
    },
    "Gargoyle's Black Axe": {
        "previous": "Gargoyle's Great Axe",
        "tier": 20,
        "somber": True,
        "id": 1514,
        "recipe": [
            (3, Materials.IronPlate),
            (1, Materials.BlackMark),
            (1, Materials.ErdtreeAmber),
            (2, Materials.MeltedMushroom),
        ],
    },
    # endregion

    # region Spears / Great Spears
    "Short Spear": {
        "previous": "Dagger",
        "tier": 3,
        "somber": False,
        "id": 1600,
        "recipe": [
            (2, Materials.SoftWood),
            (1, Materials.IronPlate),
        ],
    },
    "Spear": {
        "previous": "Short Spear",
        "tier": 6,
        "somber": False,
        "id": 1601,
        "recipe": [
            (2, Materials.SoftWood),
            (2, Materials.IronShards),
        ],
    },
    "Crystal Spear": {
        "previous": "Clayman's Harpoon",
        "tier": 16,
        "somber": True,
        "id": 1602,
        "recipe": [
            (1, Materials.GlintstoneDust),
            (7, Materials.CrackedCrystal),
        ],
    },
    "Clayman's Harpoon": {
        "previous": "Spiked Spear",
        "tier": 15,
        "somber": False,
        "id": 1603,
        "recipe": [
            (2, Materials.SoftWood),
            (1, Materials.MeteoriteChunk),
        ],
    },
    "Cleanrot Spear": {
        "previous": "Spiked Spear",
        "tier": 20,
        "somber": True,
        "id": 1604,
        "recipe": [
            (2, Materials.IronPlate),
            (2, Materials.ErdtreeAmber),
            (6, Materials.CrystalCaveMoss),
        ],
    },
    "Partisan": {
        "previous": "Iron Spear",
        "tier": 12,
        "somber": False,
        "id": 1605,
        "recipe": [
            (1, Materials.RefinedWood),
            (1, Materials.SoftWood),
            (1, Materials.IronPlate),
            (1, Materials.IronShards),
        ],
    },
    "Celebrant's Rib-Rake": {
        "previous": "Spear",
        "tier": 9,
        "somber": False,
        "id": 1606,
        "recipe": [
            (2, Materials.StoneFragment),
            (6, Materials.ThinBeastBones),
            (4, Materials.HumanBoneShard),
        ],
    },
    "Pike": {
        "previous": "Partisan",
        "tier": 14,
        "somber": False,
        "id": 1607,
        "recipe": [
            (4, Materials.IronPlate),
            (4, Materials.StoneFragment),
        ],
    },
    "Torchpole": {
        "previous": "Celebrant's Rib-Rake",
        "tier": 12,
        "somber": False,
        "id": 1608,
        "recipe": [
            (2, Materials.SoftWood),
            (1, Materials.RootResin),
            (6, Materials.SmolderingButterfly),
        ],
    },
    "Bolt of Gransax": {
        "previous": "Cross-Naginata",
        "tier": 20,
        "somber": True,
        "id": 1609,
        "recipe": [
            (1, Materials.DragonTeeth),
            (1, Materials.LiquidMetal),
            (4, Materials.GravelStone),
        ],
    },
    "Cross-Naginata": {
        "previous": "Spiked Spear",
        "tier": 17,
        "somber": False,
        "id": 1611,
        "recipe": [
            (2, Materials.RefinedWood),
            (2, Materials.IronPlate),
            (3, Materials.StoneFragment),
        ],
    },
    "Death Ritual Spear": {
        "previous": "Rotten Crystal Spear",
        "tier": 20,
        "somber": True,
        "id": 1612,
        "recipe": [
            (1, Materials.LiquidMetal),
            (4, Materials.SomberStoneFragment),
            (3, Materials.GraveViolet),
        ],
    },
    "Inquisitor's Girandole": {
        "previous": "Spiked Spear",
        "tier": 18,
        "somber": True,
        "id": 1613,
        "recipe": [
            (6, Materials.IronShards),
            (3, Materials.SmolderingButterfly),
            (2, Materials.VolcanicStone),
        ],
    },
    "Spiked Spear": {
        "previous": "Torchpole",
        "tier": 14,
        "somber": False,
        "id": 1614,
        "recipe": [
            (3, Materials.SoftWood),
            (1, Materials.IronShards),
        ],
    },
    "Iron Spear": {
        "previous": "Spear",
        "tier": 9,
        "somber": False,
        "id": 1615,
        "recipe": [
            (3, Materials.SoftWood),
            (2, Materials.IronShards),
            (1, Materials.RootResin),
        ],
    },
    "Rotten Crystal Spear": {
        "previous": "Crystal Spear",
        "tier": 18,
        "somber": True,
        "id": 1616,
        "recipe": [
            (1, Materials.GruesomeBone),
            (7, Materials.SomberStoneFragment),
            (10, Materials.CrackedCrystal),
        ],
    },
    "Mohgwyn's Sacred Spear": {
        "previous": "Lance",
        "tier": 20,
        "somber": True,
        "id": 1701,
        "recipe": [
            (1, Materials.Remembrance_Mohg),
            (2, Materials.LiquidMetal),
            (1, Materials.GruesomeBone),
            (10, Materials.BloodTaintedExcrement),
        ],
    },
    "Siluria's Tree": {
        "previous": "Treespear",
        "tier": 20,
        "somber": True,
        "id": 1702,
        "recipe": [
            (1, Materials.RefinedWood),
            (2, Materials.IronPlate),
            (2, Materials.ErdtreeAmber),
        ],
    },
    "Serpent-Hunter": {
        "id": 1703,
        "recipe": [
            (1, Materials.DragonTeeth),
            (4, Materials.SomberStoneFragment),
            (6, Materials.LivingJarShard),
        ],
    },
    "Vyke's War Spear": {
        "previous": "Inquisitor's Girandole",
        "tier": 20,
        "somber": True,
        "id": 1705,
        "recipe": [
            (3, Materials.IronPlate),
            (4, Materials.StoneFragment),
            (6, Materials.YellowEmber),
            (10, Materials.EyeOfYelough),
        ],
    },
    "Lance": {
        "previous": "Pike",
        "tier": 16,
        "somber": False,
        "id": 1706,
        "recipe": [
            (1, Materials.SoftWood),
            (3, Materials.IronPlate),
        ],
    },
    "Treespear": {
        "previous": "Lance",
        "tier": 18,
        "somber": False,
        "id": 1707,
        "recipe": [
            (3, Materials.IronPlate),
            (2, Materials.StoneFragment),
            (1, Materials.ErdtreeAmber),
        ],
    },
    # endregion

    # region Halberds
    "Halberd": {
        "previous": "Iron Spear",
        "tier": 10,
        "somber": False,
        "id": 1800,
        "recipe": [
            (2, Materials.SoftWood),
            (1, Materials.IronPlate),
            (1, Materials.IronShards),
        ],
    },
    "Pest's Glaive": {
        "previous": "Halberd",
        "tier": 12,
        "somber": False,
        "id": 1801,
        "recipe": [
            (6, Materials.StoneFragment),
            (4, Materials.TurtleNeckMeat),
            (3, Materials.GoldenCentipede),
        ],
    },
    "Lucerne": {
        "previous": "Banished Knight's Halberd",
        "tier": 14,
        "somber": False,
        "id": 1802,
        "recipe": [
            (2, Materials.SoftWood),
            (2, Materials.StoneFragment),
            (1, Materials.IronPlate),
            (1, Materials.IronShards),
        ],
    },
    "Banished Knight's Halberd": {
        "previous": "Halberd",
        "tier": 12,
        "somber": False,
        "id": 1803,
        "recipe": [
            (1, Materials.RefinedWood),
            (1, Materials.SoftWood),
            (2, Materials.IronPlate),
            (6, Materials.FlightPinion),
        ],
    },
    "Commander's Standard": {
        "previous": "Guardian's Swordspear",
        "tier": 20,
        "somber": True,
        "id": 1804,
        "recipe": [
            (2, Materials.RefinedWood),
            (2, Materials.IronPlate),
            (4, Materials.SomberStoneFragment),
            (10, Materials.CaveMoss),
        ],
    },
    "Nightrider Glaive": {
        "previous": "Glaive",
        "tier": 16,
        "somber": False,
        "id": 1805,
        "recipe": [
            (4, Materials.IronPlate),
            (5, Materials.SomberStoneFragment),
            (4, Materials.ArteriaLeaf),
        ],
    },
    "Ripple Crescent Halberd": {
        "previous": "Vulgar Militia Shotel",
        "tier": 20,
        "somber": False,
        "id": 1806,
        "recipe": [
            (1, Materials.LiquidMetal),
            (4, Materials.StoneFragment),
            (6, Materials.AlbinauricBloodclot),
        ],
    },
    "Vulgar Militia Saw": {
        "previous": "Pest's Glaive",
        "tier": 14,
        "somber": False,
        "id": 1807,
        "recipe": [
            (1, Materials.RefinedWood),
            (1, Materials.SoftWood),
            (3, Materials.IronShards),
            (4, Materials.StoneFragment),
        ],
    },
    "Golden Halberd": {
        "previous": "Dragon Halberd",
        "tier": 18,
        "somber": True,
        "id": 1808,
        "recipe": [
            (4, Materials.IronPlate),
            (1, Materials.ErdtreeAmber),
            (6, Materials.GoldenRowa),
        ],
    },
    "Glaive": {
        "previous": "Lucerne",
        "tier": 16,
        "somber": False,
        "id": 1809,
        "recipe": [
            (2, Materials.SoftWood),
            (2, Materials.IronPlate),
            (2, Materials.RootResin),
        ],
    },
    "Loretta's War Sickle": {
        "previous": "Vulgar Militia Shotel",
        "tier": 20,
        "somber": True,
        "id": 1810,
        "recipe": [
            (2, Materials.LiquidMetal),
            (2, Materials.IronPlate),
            (4, Materials.GoldFirefly),
            (3, Materials.SilverTearHusk),
        ],
    },
    "Guardian's Swordspear": {
        "previous": "Lucerne",
        "tier": 17,
        "somber": False,
        "id": 1811,
        "recipe": [
            (3, Materials.RefinedWood),
            (1, Materials.ErdtreeAmber),
            (10, Materials.ErdleafFlower),
        ],
    },
    "Vulgar Militia Shotel": {
        "previous": "Vulgar Militia Saw",
        "tier": 17,
        "somber": False,
        "id": 1813,
        "recipe": [
            (1, Materials.RefinedWood),
            (1, Materials.SoftWood),
            (1, Materials.IronPlate),
            (1, Materials.IronShards),
        ],
    },
    "Dragon Halberd": {
        "previous": "Lucerne",
        "tier": 16,
        "somber": True,
        "id": 1814,
        "recipe": [
            (1, Materials.SoftWood),
            (2, Materials.IronPlate),
            (1, Materials.DragonTeeth),
        ],
    },
    "Gargoyle's Halberd": {
        "previous": "Glaive",
        "tier": 18,
        "somber": False,
        "id": 1815,
        "recipe": [
            (2, Materials.IronPlate),
            (9, Materials.StoneFragment),
            (6, Materials.RootResin),
            (6, Materials.MeltedMushroom),
        ],
    },
    "Gargoyle's Black Halberd": {
        "previous": "Gargoyle's Halberd",
        "tier": 40,
        "somber": True,
        "id": 1816,
        "recipe": [
            (2, Materials.IronPlate),
            (1, Materials.BlackMark),
            (1, Materials.ErdtreeAmber),
            (2, Materials.MeltedMushroom),
        ],
    },
    # endregion

    # region Reapers
    "Scythe": {
        "previous": "Lucerne",
        "tier": 16,
        "somber": False,
        "id": 1900,
        "recipe": [
            (2, Materials.RefinedWood),
            (1, Materials.IronPlate),
            (2, Materials.StoneFragment),
        ],
    },
    "Grave Scythe": {
        "previous": "Scythe",
        "tier": 18,
        "somber": False,
        "id": 1901,
        "recipe": [
            (2, Materials.SoftWood),
            (1, Materials.IronPlate),
            (1, Materials.GraveViolet),
        ],
    },
    "Halo Scythe": {
        "previous": "Scythe",
        "tier": 18,
        "somber": True,
        "id": 1902,
        "recipe": [
            (2, Materials.RefinedWood),
            (1, Materials.IronPlate),
            (1, Materials.ErdtreeAmber),
            (6, Materials.SomberStoneFragment),
        ],
    },
    "Winged Scythe": {
        "previous": "Halo Scythe",
        "tier": 20,
        "somber": True,
        "id": 1906,
        "recipe": [
            (2, Materials.SoftWood),
            (1, Materials.IronPlate),
            (1, Materials.ErdtreeAmber),
            (6, Materials.FlightPinion),
        ],
    },
    # endregion

    # region Whips
    "Whip": {
        "previous": "None",
        "tier": 10,
        "somber": False,
        "id": 2000,
        "recipe": [
            (1, Materials.SoftWood),
            (3, Materials.LumpOfFlesh),
            (2, Materials.CaveMoss),
        ],
    },
    "Thorned Whip": {
        "previous": "Whip",
        "tier": 13,
        "somber": False,
        "id": 2002,
        "recipe": [
            (2, Materials.RefinedWood),
            (4, Materials.SomberStoneFragment),
            (6, Materials.Bloodrose),
            (4, Materials.BeastBlood),
        ],
    },
    "Magma Whip Candlestick": {
        "previous": "Whip",
        "tier": 20,
        "somber": True,
        "id": 2003,
        "recipe": [
            (1, Materials.IronPlate),
            (1, Materials.DragonTeeth),
            (6, Materials.VolcanicStone),
        ],
    },
    "Hoslow's Petal Whip": {
        "previous": "Urumi",
        "tier": 15,
        "somber": False,
        "id": 2005,
        "recipe": [
            (6, Materials.IronShards),
            (6, Materials.StoneFragment),
            (2, Materials.String),
        ],
    },
    "Giant's Red Braid": {
        "previous": "Whip",
        "tier": 20,
        "somber": True,
        "id": 2006,
        "recipe": [
            (1, Materials.Remembrance_FireGiant),
            (4, Materials.SomberStoneFragment),
            (8, Materials.TarnishedGoldenSunflower),
            (4, Materials.SilverTearHusk),
        ],
    },
    "Urumi": {
        "previous": "Thorned Whip",
        "tier": 17,
        "somber": False,
        "id": 2007,
        "recipe": [
            (1, Materials.IronPlate),
            (2, Materials.LiquidMetal),
        ],
    },
    # endregion

    # region Fists
    "Caestus": {
        "previous": "None",
        "tier": 0,
        "somber": False,
        "id": 2100,
        "recipe": [
            (2, Materials.IronShards),
            (2, Materials.LumpOfFlesh),
        ],
    },
    "Spiked Caestus": {
        "previous": "Caestus",
        "tier": 3,
        "somber": False,
        "id": 2101,
        "recipe": [
            (4, Materials.IronShards),
            (2, Materials.StoneFragment),
            (2, Materials.LumpOfFlesh),
        ],
    },
    "Grafted Dragon": {
        "previous": "Veteran's Prosthesis",
        "tier": 20,
        "somber": True,
        "id": 2106,
        "recipe": [
            (1, Materials.Remembrance_Godrick),
            (1, Materials.DragonTeeth),
            (4, Materials.BeastLiver),
        ],
    },
    "Iron Ball": {
        "previous": "Katar",
        "tier": 9,
        "somber": False,
        "id": 2107,
        "recipe": [
            (2, Materials.IronPlate),
            (2, Materials.SomberStoneFragment),
            (2, Materials.StripOfWhiteFlesh),
        ],
    },
    "Star Fist": {
        "previous": "Iron Ball",
        "tier": 12,
        "somber": False,
        "id": 2108,
        "recipe": [
            (2, Materials.IronPlate),
            (2, Materials.IronShards),
            (2, Materials.SomberStoneFragment),
            (6, Materials.StoneFragment),
        ],
    },
    "Katar": {
        "previous": "Spiked Caestus",
        "tier": 6,
        "somber": False,
        "id": 2110,
        "recipe": [
            (3, Materials.IronPlate),
            (4, Materials.SomberStoneFragment),
            (1, Materials.BeastBlood),
        ],
    },
    "Clinging Bone": {
        "previous": "Raptor Talons",
        "tier": 20,
        "somber": True,
        "id": 2111,
        "recipe": [
            (6, Materials.StoneFragment),
            (4, Materials.HumanBoneShard),
            (2, Materials.LivingJarShard),
            (5, Materials.YellowEmber),
        ],
    },
    "Veteran's Prosthesis": {
        "previous": "Star Fist",
        "tier": 16,
        "somber": True,
        "id": 2112,
        "recipe": [
            (1, Materials.RefinedWood),
            (2, Materials.IronPlate),
            (8, Materials.SomberStoneFragment),
            (8, Materials.Fulgurbloom),
        ],
    },
    "Cipher Pata": {
        "previous": "Raptor Talons",
        "tier": 20,
        "somber": True,
        "id": 2113,
        "recipe": [
            (6, Materials.SomberStoneFragment),
            (6, Materials.GoldTingedExcrement),
        ],
    },
    "Hookclaws": {
        "previous": "Katar",
        "tier": 9,
        "somber": False,
        "id": 2200,
        "recipe": [
            (1, Materials.SoftWood),
            (2, Materials.IronPlate),
            (5, Materials.ArteriaLeaf),
        ],
    },
    "Venomous Fang": {
        "previous": "Hookclaws",
        "tier": 12,
        "somber": False,
        "id": 2201,
        "recipe": [
            (2, Materials.IronPlate),
            (1, Materials.BlackMark),  # ? eh
            (6, Materials.MirandaPowder),
            (4, Materials.ToxicMushroom),
        ],
    },
    "Bloodhound Claws": {
        "previous": "Venomous Fang",
        "tier": 15,
        "somber": False,
        "id": 2202,
        "recipe": [
            (3, Materials.IronPlate),
            (10, Materials.StoneFragment),
            (6, Materials.LandOctopusOvary),
            (3, Materials.MiquellasLily),
        ],
    },
    "Raptor Talons": {
        "previous": "Bloodhound Claws",
        "tier": 18,
        "somber": False,
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
        "previous": "Great Club",
        "tier": 20,
        "somber": False,
        "id": 2300,
        "recipe": [
            (3, Materials.IronPlate),
            (3, Materials.IronShards),
            (8, Materials.TurtleNeckMeat),
            (2, Materials.EyeOfYelough),
        ],
    },
    "Watchdog's Staff": {
        "previous": "Celebrant's Skull",
        "tier": 16,
        "somber": True,
        "id": 2301,
        "recipe": [
            (16, Materials.StoneFragment),
            (1, Materials.GlintstoneDust),
        ],
    },
    "Great Club": {
        "previous": "Brick Hammer",
        "tier": 18,
        "somber": False,
        "id": 2302,
        "recipe": [
            (5, Materials.SoftWood),
        ],
    },
    "Envoy's Greathorn": {
        "previous": "Envoy's Long Horn",
        "tier": 20,
        "somber": True,
        "id": 2303,
        "recipe": [
            (5, Materials.IronPlate),
            (1, Materials.ErdtreeAmber),
            (5, Materials.AltusBloom),
        ],
    },
    "Duelist Greataxe": {
        "previous": "Greataxe",
        "tier": 17,
        "somber": False,
        "id": 2304,
        "recipe": [
            (3, Materials.RefinedWood),
            (4, Materials.IronPlate),
        ],
    },
    "Axe of Godfrey": {
        "previous": "Axe of Godrick",
        "tier": 20,
        "somber": True,
        "id": 2305,
        "recipe": [
            (1, Materials.Remembrance_HoarahLoux),
            (2, Materials.RefinedWood),
            (3, Materials.IronPlate),
            (6, Materials.SomberStoneFragment),
        ],
    },
    "Dragon Greatclaw": {
        "previous": "Duelist Greataxe",
        "tier": 20,
        "somber": True,
        "id": 2306,
        "recipe": [
            (1, Materials.DragonTeeth),
            (5, Materials.HeftyBeastBone),
            (2, Materials.RootResin),
        ],
    },
    "Staff of the Avatar": {
        "previous": "Watchdog's Staff",
        "tier": 20,
        "somber": True,
        "id": 2307,
        "recipe": [
            (4, Materials.SoftWood),
            (2, Materials.IronPlate),
            (2, Materials.ErdtreeAmber),
        ],
    },
    "Fallingstar Beast Jaw": {
        "previous": "Lance",
        "tier": 20,
        "somber": True,
        "id": 2308,
        "recipe": [
            (1, Materials.MeteoriteChunk),
            (1, Materials.GruesomeBone),
            (4, Materials.MeltedMushroom),
        ],
    },
    "Ghiza's Wheel": {
        "previous": "Grave Scythe",
        "tier": 20,
        "somber": True,
        "id": 2310,
        "recipe": [
            (2, Materials.LiquidMetal),
            (2, Materials.IronPlate),
            (12, Materials.IronShards),
        ],
    },
    "Giant-Crusher": {
        "previous": "Great Club",
        "tier": 20,
        "somber": False,
        "id": 2311,
        "recipe": [
            (20, Materials.SomberStoneFragment),
        ],
    },
    "Golem's Halberd": {
        "previous": "Golden Halberd",
        "tier": 10,
        "somber": False,
        "id": 2312,
        "recipe": [
            (1, Materials.BlackMark),
            (16, Materials.StoneFragment),
        ],
    },
    "Troll's Hammer": {
        "previous": "Greathorn Hammer",
        "tier": 20,
        "somber": False,
        "id": 2313,
        "recipe": [
            (4, Materials.SoftWood),
            (2, Materials.ErdtreeAmber),
            (1, Materials.GlintstoneDust),
        ],
    },
    "Rotten Staff": {
        "previous": "Watchdog's Staff",
        "tier": 20,
        "somber": True,
        "id": 2314,
        "recipe": [
            (4, Materials.SoftWood),
            (2, Materials.IronPlate),
            (2, Materials.ErdtreeAmber),
            (9, Materials.AeonianButterfly),
        ],
    },
    "Rotten Greataxe": {
        "previous": "Duelist Greataxe",
        "tier": 20,
        "somber": False,
        "id": 2315,
        "recipe": [
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
            (1, Materials.ErdtreeAmber),
            (1, Materials.SmolderingButterfly),
        ],
    },
    # endregion

    # region Shields
    "Buckler": {
        "id": 3000,
        "recipe": [
            (1, Materials.ShieldGrip),
            (1, Materials.IronPlate),
            (2, Materials.StoneFragment),
        ],
    },
    "Perfumer's Shield": {
        "id": 3001,
        "recipe": [
            (1, Materials.ShieldGrip),
            (1, Materials.IronPlate),
            (1, Materials.ErdtreeAmber),
        ],
    },
    "Man-Serpent's Shield": {
        "id": 3002,
        "recipe": [
            (1, Materials.ShieldGrip),
            (1, Materials.IronPlate),
            (4, Materials.VolcanicStone),
        ],
    },
    "Rickety Shield": {
        "id": 3003,
        "recipe": [
            (1, Materials.ShieldGrip),
            (2, Materials.SoftWood),
        ],
    },
    "Pillory Shield": {
        "id": 3004,
        "recipe": [
            (1, Materials.ShieldGrip),
            (1, Materials.RefinedWood),
        ],
    },
    "Beastman's Jar-Shield": {
        "id": 3006,
        "recipe": [
            (2, Materials.ShieldGrip),
            (3, Materials.LivingJarShard),
            (1, Materials.HeftyBeastBone),
        ],
    },
    "Red Thorn Roundshield": {
        "id": 3007,
        "recipe": [
            (1, Materials.ShieldGrip),
            (2, Materials.SoftWood),
            (2, Materials.RootResin),
        ],
    },
    "Scripture Wooden Shield": {
        "id": 3008,
        "recipe": [
            (1, Materials.ShieldGrip),
            (2, Materials.SoftWood),
            (5, Materials.ErdleafFlower),
        ],
    },
    "Riveted Wooden Shield": {
        "id": 3009,
        "recipe": [
            (1, Materials.ShieldGrip),
            (2, Materials.SoftWood),
            (3, Materials.IronShards),
        ],
    },
    "Blue-White Wooden Shield": {
        "id": 3010,
        "recipe": [
            (1, Materials.ShieldGrip),
            (2, Materials.SoftWood),
            (1, Materials.AlbinauricBloodclot),
        ],
    },
    "Rift Shield": {
        "id": 3011,
        "recipe": [
            (1, Materials.ShieldGrip),
            (1, Materials.IronPlate),
            (2, Materials.IronShards),
            (3, Materials.StoneFragment),
        ],
    },
    "Iron Roundshield": {
        "id": 3012,
        "recipe": [
            (1, Materials.ShieldGrip),
            (1, Materials.IronPlate),
            (2, Materials.StoneFragment),
        ],
    },
    "Gilded Iron Shield": {
        "id": 3013,
        "recipe": [
            (1, Materials.ShieldGrip),
            (1, Materials.IronPlate),
            (3, Materials.GoldenSunflower),
        ],
    },
    "Ice Crest Shield": {
        "id": 3014,
        "recipe": [
            (1, Materials.ShieldGrip),
            (1, Materials.IronPlate),
            (1, Materials.GlintstoneDust),
            (4, Materials.SilverFirefly),
        ],
    },
    "Smoldering Shield": {
        "id": 3015,
        "recipe": [
            (1, Materials.ShieldGrip),
            (6, Materials.VolcanicStone),
        ],
    },
    "Spiralhorn Shield": {
        "id": 3019,
        "recipe": [
            (1, Materials.ShieldGrip),
            (5, Materials.BuddingHorn),
        ],
    },
    "Coil Shield": {
        "id": 3020,
        "recipe": [
            (1, Materials.ShieldGrip),
            (5, Materials.BuddingHorn),
        ],
    },
    # Medium shields generally start here
    "Kite Shield": {
        "id": 3100,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.IronPlate),
        ],
    },
    "Marred Leather Shield": {
        "id": 3101,
        "recipe": [
            (2, Materials.ShieldGrip),
            (1, Materials.LumpOfFlesh),
            (3, Materials.TarnishedGoldenSunflower),
            (1, Materials.Bloodrose),
        ],
    },
    "Marred Wooden Shield": {
        "id": 3102,
        "recipe": [
            (2, Materials.ShieldGrip),
            (3, Materials.SoftWood),
            (3, Materials.TarnishedGoldenSunflower),
        ],
    },
    "Banished Knight's Shield": {
        "id": 3103,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.IronPlate),
            (2, Materials.IronPlate),
        ],
    },
    "Albinauric Shield": {
        "id": 3104,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.CrystalBud),
            (2, Materials.IronPlate),
            (1, Materials.AlbinauricBloodclot),
        ],
    },
    "Sun Realm Shield": {
        "id": 3105,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.IronPlate),
            (1, Materials.SoftWood),
        ],
    },
    "Silver Mirrorshield": {
        "id": 3106,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.SilverTearHusk),
            (1, Materials.AlbinauricBloodclot),
            (5, Materials.IronPlate),
            (1, Materials.SomberStoneFragment),
        ],
    },
    "Round Shield": {
        "id": 3107,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.RefinedWood),
            (2, Materials.IronShards),
        ],
    },
    "Scorpion Kite Shield": {
        "id": 3108,
        "recipe": [
            (2, Materials.ShieldGrip),
            (1, Materials.IronPlate),
            (2, Materials.RefinedWood),
        ],
    },
    "Twinbird Kite Shield": {
        "id": 3109,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.IronPlate),
            (5, Materials.FlightPinion),
            (3, Materials.StormhawkFeather),
        ],
    },
    "Blue-Gold Kite Shield": {
        "id": 3110,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.IronShards),
            (2, Materials.SoftWood),
        ],
    },
    "Brass Shield": {
        "id": 3113,
        "recipe": [
            (2, Materials.ShieldGrip),
            (3, Materials.IronPlate),
            (2, Materials.GoldenSunflower),
        ],
    },
    "Great Turtle Shell": {
        "id": 3114,
        "recipe": [
            (2, Materials.ShieldGrip),
            (4, Materials.TurtleNeckMeat),
            (4, Materials.CaveMoss),
            (4, Materials.HeftyBeastBone),
        ],
    },
    "Shield of the Guilty": {
        "id": 3117,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.IronPlate),
            (4, Materials.Bloodrose),
            (1, Materials.GruesomeBone),
        ],
    },
    "Carian Knight's Shield": {
        "id": 3119,
        "recipe": [
            (2, Materials.ShieldGrip),
            (5, Materials.IronPlate),
            (5, Materials.GlintstoneFirefly),
            (1, Materials.GoldenSunflower),
        ],
    },
    "Large Leather Shield": {
        "id": 3123,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.RefinedWood),
            (4, Materials.String),
        ],
    },
    "Horse Crest Wooden Shield": {
        "id": 3124,
        "recipe": [
            (2, Materials.ShieldGrip),
            (3, Materials.RefinedWood),
            (3, Materials.RowaFruit),
            (1, Materials.Herba),
        ],
    },
    "Candletree Wooden Shield": {
        "id": 3125,
        "recipe": [
            (2, Materials.ShieldGrip),
            (3, Materials.RefinedWood),
            (2, Materials.RimedRowa),
        ],
    },
    "Flame Crest Wooden Shield": {
        "id": 3126,
        "recipe": [
            (2, Materials.ShieldGrip),
            (3, Materials.RefinedWood),
            (1, Materials.IronShards),
            (1, Materials.YellowEmber),
        ],
    },
    "Hawk Crest Wooden Shield": {
        "id": 3127,
        "recipe": [
            (2, Materials.ShieldGrip),
            (3, Materials.RefinedWood),
            (1, Materials.IronShards),
        ],
    },
    "Beast Crest Heater Shield": {
        "id": 3128,
        "recipe": [
            (2, Materials.ShieldGrip),
            (3, Materials.IronPlate),
            (1, Materials.ThinBeastBones),
        ],
    },
    "Red Crest Heater Shield": {
        "id": 3129,
        "recipe": [
            (2, Materials.ShieldGrip),
            (3, Materials.IronPlate),
            (2, Materials.RowaFruit),
        ],
    },
    "Blue Crest Heater Shield": {
        "id": 3130,
        "recipe": [
            (2, Materials.ShieldGrip),
            (3, Materials.IronPlate),
        ],
    },
    "Eclipse Crest Heater Shield": {
        "id": 3131,
        "recipe": [
            (2, Materials.ShieldGrip),
            (3, Materials.IronPlate),
            (1, Materials.RowaFruit),
        ],
    },
    "Inverted Hawk Heater Shield": {
        "id": 3132,
        "recipe": [
            (2, Materials.ShieldGrip),
            (3, Materials.IronPlate),
        ],
    },
    "Heater Shield": {
        "id": 3133,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.IronPlate),
        ],
    },
    "Black Leather Shield": {
        "id": 3134,
        "recipe": [
            (2, Materials.ShieldGrip),
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
            (3, Materials.ShieldGrip),
            (2, Materials.IronShards),
            (10, Materials.IronPlate),
            (1, Materials.DragonTeeth),
        ],
    },
    "Distinguished Greatshield": {
        "id": 3202,
        "recipe": [
            (3, Materials.ShieldGrip),
            (2, Materials.RefinedWood),
            (6, Materials.IronPlate),
        ],
    },
    "Crucible Hornshield": {
        "id": 3203,
        "recipe": [
            (3, Materials.ShieldGrip),
            (12, Materials.BuddingHorn),
            (5, Materials.SomberStoneFragment),
            (1, Materials.ErdtreeAmber),
            (6, Materials.GoldTingedExcrement),
        ],
    },
    "Dragonclaw Shield": {
        "id": 3204,
        "recipe": [
            (3, Materials.ShieldGrip),
            (3, Materials.SomberStoneFragment),
            (8, Materials.GravelStone),
            (2, Materials.DragonTeeth),
        ],
    },
    "Briar Greatshield": {
        "id": 3205,
        "recipe": [
            (3, Materials.ShieldGrip),
            (15, Materials.RefinedWood),
            (3, Materials.IronPlate),
            (6, Materials.Bloodrose),
            (4, Materials.IronShards),
        ],
    },
    "Erdtree Greatshield": {
        "id": 3208,
        "recipe": [
            (3, Materials.ShieldGrip),
            (3, Materials.IronPlate),
            (5, Materials.ErdtreeWood),
            (3, Materials.ErdtreeAmber),
            (9, Materials.ErdleafFlower),
        ],
    },
    "Golden Beast Crest Shield": {
        "id": 3209,
        "recipe": [
            (3, Materials.ShieldGrip),
            (10, Materials.RefinedWood),
            (2, Materials.GoldenSunflower),
            (4, Materials.ErdleafFlower),
        ],
    },
    "Jellyfish Shield": {
        "id": 3212,
        "recipe": [
            (3, Materials.ShieldGrip),
            (2, Materials.SomberStoneFragment),
            (1, Materials.GruesomeBone),
            (1, Materials.LumpOfFlesh),
        ],
    },
    "Fingerprint Stone Shield": {
        "id": 3213,
        "recipe": [
            (3, Materials.ShieldGrip),
            (4, Materials.IronPlate),
            (8, Materials.SomberStoneFragment),
            (6, Materials.YellowEmber),
            (25, Materials.StoneFragment),
        ],
    },
    "Icon Shield": {
        "id": 3214,
        "recipe": [
            (3, Materials.ShieldGrip),
            (2, Materials.IronShards),
            (8, Materials.RefinedWood),
            (6, Materials.ErdleafFlower),
            (2, Materials.AltusBloom)
        ],
    },
    "One-Eyed Shield": {
        "id": 3215,
        "recipe": [
            (3, Materials.ShieldGrip),
            (2, Materials.SomberStoneFragment),
            (2, Materials.IronPlate),
            (8, Materials.StoneFragment),
            (8, Materials.FireBlossom),

        ],
    },
    "Visage Shield": {
        "id": 3216,
        "recipe": [
            (3, Materials.ShieldGrip),
            (4, Materials.SomberStoneFragment),
            (3, Materials.IronPlate),
            (10, Materials.StoneFragment),
            (10, Materials.FireBlossom),

        ],
    },
    "Spiked Palisade Shield": {
        "id": 3217,
        "recipe": [
            (3, Materials.ShieldGrip),
            (5, Materials.RefinedWood),
            (5, Materials.IronShards),
            (3, Materials.Bloodrose),
        ],
    },
    "Manor Towershield": {
        "id": 3219,
        "recipe": [
            (3, Materials.ShieldGrip),
            (5, Materials.IronPlate),
            (1, Materials.LivingJarShard),
        ],
    },
    "Crossed-Tree Towershield": {
        "id": 3220,
        "recipe": [
            (3, Materials.ShieldGrip),
            (2, Materials.IronShards),
            (3, Materials.IronPlate),
            (7, Materials.Herba),
        ],
    },
    "Inverted Hawk Towershield": {
        "id": 3221,
        "recipe": [
            (3, Materials.ShieldGrip),
            (4, Materials.IronShards),
            (3, Materials.IronPlate),
            (1, Materials.SomberStoneFragment),
        ],
    },
    "Ant's Skull Plate": {
        "id": 3222,
        "recipe": [
            (3, Materials.ShieldGrip),
            (1, Materials.SomberStoneFragment),
            (4, Materials.BuddingHorn),
            (2, Materials.GruesomeBone),
        ],
    },
    "Redmane Greatshield": {
        "id": 3223,
        "recipe": [
            (3, Materials.ShieldGrip),
            (6, Materials.IronPlate),
            (1, Materials.SomberStoneFragment),
            (10, Materials.FireBlossom),
        ],
    },
    "Eclipse Crest Greatshield": {
        "id": 3224,
        "recipe": [
            (3, Materials.ShieldGrip),
            (5, Materials.IronPlate),
            (2, Materials.SomberStoneFragment),
            (1, Materials.GruesomeBone),
        ],
    },
    "Cuckoo Greatshield": {
        "id": 3225,
        "recipe": [
            (3, Materials.ShieldGrip),
            (3, Materials.RefinedWood),
            (3, Materials.SomberStoneFragment),
            (5, Materials.CrystalBud),
        ],
    },
    "Golden Greatshield": {
        "id": 3226,
        "recipe": [
            (3, Materials.ShieldGrip),
            (1, Materials.RefinedWood),
            (3, Materials.IronPlate),
            (4, Materials.GoldenCentipede),
        ],
    },
    "Gilded Greatshield": {
        "id": 3227,
        "recipe": [
            (3, Materials.ShieldGrip),
            (2, Materials.SoftWood),
            (2, Materials.RefinedWood),
            (2, Materials.IronPlate),
            (1, Materials.GoldenRowa),

        ],
    },
    "Haligtree Crest Greatshield": {
        "id": 3228,
        "recipe": [
            (3, Materials.ShieldGrip),
            (3, Materials.RefinedWood),
            (3, Materials.IronPlate),
            (3, Materials.MiquellasLily),
        ],
    },
    "Wooden Greatshield": {
        "id": 3229,
        "recipe": [
            (3, Materials.ShieldGrip),
            (5, Materials.RefinedWood),

        ],
    },
    "Lordsworn's Shield": {
        "id": 3230,
        "recipe": [
            (3, Materials.ShieldGrip),
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
            (1, Materials.Remembrance_Rennala),
            (4, Materials.SomberStoneFragment),
            (3, Materials.GlintstoneDust),
            (5, Materials.GlintstoneFirefly),
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
            (7, Materials.GlintstoneFirefly),
        ],
    },
    "Lusat's Glintstone Staff": {
        "id": 3324,
        "recipe": [
            (1, Materials.StaffPole),
            (4, Materials.SomberStoneFragment),
            (2, Materials.GlintstoneDust),
            (7, Materials.GlintstoneFirefly),
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
            (3, Materials.GoldFirefly),
            (3, Materials.GlintstoneFirefly),
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
        "previous": "None",
        "tier": 0,
        "somber": False,
        "id": 4000,
        "recipe": [
            (1, Materials.String),
            (2, Materials.SoftWood),
        ],
    },
    "Misbegotten Shortbow": {
        "previous": "Shortbow",
        "tier": 5,
        "somber": False,
        "id": 4001,
        "recipe": [
            (1, Materials.String),
            (1, Materials.SoftWood),
            (1, Materials.ThinBeastBones),
        ],
    },
    "Red Branch Shortbow": {
        "previous": "Harp Bow",
        "tier": 8,
        "somber": False,
        "id": 4002,
        "recipe": [
            (1, Materials.RefinedWood),
            (1, Materials.String),
            (2, Materials.RowaFruit),
        ],
    },
    "Harp Bow": {
        "previous": "Shortbow",
        "tier": 10,
        "somber": True,
        "id": 4003,
        "recipe": [
            (6, Materials.String),
            (1, Materials.RefinedWood),
        ],
    },
    "Composite Bow": {
        "previous": "Harp Bow",
        "tier": 10,
        "somber": False,
        "id": 4005,
        "recipe": [
            (2, Materials.String),
            (2, Materials.SoftWood),
        ],
    },
    "Longbow": {
        "previous": "Red Branch Shortbow",
        "tier": 10,
        "somber": False,
        "id": 4100,
        "recipe": [
            (1, Materials.String),
            (2, Materials.SoftWood),
        ],
    },
    "Albinauric Bow": {
        "previous": "Longbow",
        "tier": 15,
        "somber": False,
        "id": 4101,
        "recipe": [
            (2, Materials.RefinedWood),
            (1, Materials.AlbinauricBloodclot),
            (1, Materials.StoneFragment),
        ],
    },
    "Horn Bow": {
        "previous": "Longbow",
        "tier": 15,
        "somber": False,
        "id": 4102,
        "recipe": [
            (3, Materials.RefinedWood),
            (1, Materials.String),
        ],
    },
    "Erdtree Bow": {
        "previous": "Longbow",
        "tier": 20,
        "somber": True,
        "id": 4103,
        "recipe": [
            (2, Materials.ErdtreeWood),
            (2, Materials.String),
            (2, Materials.GoldFirefly),
            (1, Materials.ErdtreeAmber),
        ],
    },
    "Serpent Bow": {
        "previous": "Longbow",
        "tier": 20,
        "somber": True,
        "id": 4104,
        "recipe": [
            (2, Materials.RefinedWood),
            (1, Materials.GruesomeBone),
            (2, Materials.String),
        ],
    },
    "Pulley Bow": {
        "previous": "Misbegotten Shortbow",
        "tier": 16,
        "somber": True,
        "id": 4106,
        "recipe": [
            (3, Materials.String),
            (2, Materials.StoneFragment),
            (2, Materials.RefinedWood),
        ],
    },
    "Black Bow": {
        "previous": "Albinauric Bow",
        "tier": 20,
        "somber": True,
        "id": 4107,
        "recipe": [
            (2, Materials.RefinedWood),
            (2, Materials.StoneFragment),
            (2, Materials.String),
        ],
    },
    # endregion

    # region Greatbows
    "Lion Greatbow": {
        "previous": "Golem Greatbow",
        "tier": 20,
        "somber": True,
        "id": 4200,
        "recipe": [
            (1, Materials.Remembrance_Radahn),
            (2, Materials.RefinedWood),
            (2, Materials.SomberStoneFragment),
            (2, Materials.String),
        ],
    },
    "Golem Greatbow": {
        "previous": "Greatbow",
        "tier": 16,
        "somber": True,
        "id": 4201,
        "recipe": [
            (2, Materials.RefinedWood),
            (4, Materials.IronPlate),
            (2, Materials.MeteoriteChunk),
        ],
    },
    "Erdtree Greatbow": {
        "previous": "Greatbow",
        "tier": 20,
        "somber": True,
        "id": 4203,
        "recipe": [
            (1, Materials.ErdtreeWood),
            (1, Materials.ErdleafFlower),
            (2, Materials.ErdtreeAmber),
        ],
    },
    "Greatbow": {
        "previous": "Longbow",
        "tier": 14,
        "somber": False,
        "id": 4204,
        "recipe": [
            (3, Materials.String),
            (2, Materials.RefinedWood),
            (2, Materials.IronPlate),
        ],
    },
    # endregion

    # region Crossbows / Guns
    "Soldier's Crossbow": {
        "previous": "Pulley Bow",
        "tier": 10,
        "somber": False,
        "id": 4300,
        "recipe": [
            (1, Materials.String),
            (1, Materials.SoftWood),
            (1, Materials.StoneFragment),
        ],
    },
    "Light Crossbow": {
        "previous": "Soldier's Crossbow",
        "tier": 13,
        "somber": False,
        "id": 4302,
        "recipe": [
            (1, Materials.String),
            (1, Materials.SoftWood),
            (2, Materials.StoneFragment),
        ],
    },
    "Heavy Crossbow": {
        "previous": "Light Crossbow",
        "tier": 16,
        "somber": False,
        "id": 4303,
        "recipe": [
            (1, Materials.String),
            (3, Materials.SoftWood),
            (2, Materials.StoneFragment),
        ],
    },
    "Pulley Crossbow": {
        "previous": "Heavy Crossbow",
        "tier": 20,
        "somber": True,
        "id": 4305,
        "recipe": [
            (3, Materials.String),
            (2, Materials.RefinedWood),
            (1, Materials.IronPlate),
        ],
    },
    "Full Moon Crossbow": {
        "previous": "Light Crossbow",
        "tier": 20,
        "somber": True,
        "id": 4306,
        "recipe": [
            (4, Materials.String),
            (4, Materials.RefinedWood),
            (1, Materials.SomberStoneFragment),
        ],
    },
    "Arbalest": {
        "previous": "Heavy Crossbow",
        "tier": 18,
        "somber": False,
        "id": 4308,
        "recipe": [
            (2, Materials.String),
            (2, Materials.RefinedWood),
        ],
    },
    "Crepus's Black-Key Crossbow": {
        "previous": "Heavy Crossbow",
        "tier": 20,
        "somber": True,
        "id": 4311,
        "recipe": [
            (1, Materials.IronPlate),
            (2, Materials.RefinedWood),
            (2, Materials.String),
        ],
    },
    "Hand Ballista": {
        "previous": "Arbalest",
        "tier": 20,
        "somber": False,
        "id": 4400,
        "recipe": [
            (4, Materials.String),
            (3, Materials.RefinedWood),
            (2, Materials.IronPlate),
        ],
    },
    "Jar Cannon": {
        "previous": "Arbalest",
        "tier": 20,
        "somber": True,
        "id": 4401,
        "recipe": [
            (2, Materials.IronPlate),
            (2, Materials.SomberStoneFragment),
            (4, Materials.LivingJarShard),
        ],
    },
    # endregion
}
