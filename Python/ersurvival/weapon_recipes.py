"""Lists the recipes for weapons.

TODO: Region tier guidelines.
    - These should inform rough recipe 'difficulty' and any naturally-found ingredients.
    - New components will be randomly scattered across merchants and dungeons, but bosses will tend to drop more of
      these (and rarer ones) as the game progresses. These can vary in quantity only.
    - That said, 0-4 tier weapons should probably not use any of the new rare components like Meteorite Chunk.
    - Stone Fragment usage should basically scale perfectly with tier:
        - e.g., fragment number = tier / 2
    - Number of 'wild' ingredients should also scale with tier, but even moreso than stone fragments:
        - common: count = tier * 1.5 (Herbs, Rowa, Moss, etc.
        - uncommon: count = tier (Fireflies, etc.)
        - rare: count = tier * 0.5 (Arteria Leaf, Trina's Lily, etc.)
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
from survival_enums import Flags


# Weapons crafted from scratch. The Whip+10 requires a note, but the others can be crafted immediately.
# Not actually used anywhere - mostly just for reference.
SCRATCH_WEAPONS = [
    "Dagger",
    "Club",
    "Hand Axe",
    "Whip",  # +10 (requires special recipe note)
    "Caestus",
    "Shortbow",
    "Rickety Shield",
    "Glintstone Staff",
    "Finger Seal",
]

# TODO: Event flags are automatically determined for each weapon/recipe based on its index in this list. If it ever
#  changes, make sure those flags/events are regenerated!
WEAPON_RECIPES = {

    # region Daggers
    "Dagger": {
        "visibility_flag": 0,
        "previous": None,
        "tier": 0,
        "somber": False,
        "id": 100,
        "recipe": [
            (2, Materials.MetalShards),
        ],
        "cost": 50,
    },
    "Black Knife": {
        "previous": "Blade of Calling",
        "tier": 20,
        "somber": True,
        "id": 101,
        "recipe": [
            (1, Materials.MetalPlate),
            (12, Materials.SacramentalBud),
            (12, Materials.SomberStoneFragment),
            (4, Materials.BlackMark),
        ],
    },
    "Parrying Dagger": {
        "previous": "Bloodstained Dagger",
        "tier": 9,
        "somber": False,
        "id": 102,
        "recipe": [
            (1, Materials.MetalPlate),
            (5, Materials.StoneFragment),
            (10, Materials.SilverFirefly),
        ],
    },
    "Misericorde": {
        "previous": "Bloodstained Dagger",
        "tier": 9,
        "somber": False,
        "id": 103,
        "recipe": [
            (1, Materials.MetalPlate),
            (4, Materials.MetalShards),
            (5, Materials.StoneFragment),
            (9, Materials.GraveViolet),
        ],
    },
    "Reduvia": {
        "previous": "Blade of Calling",
        "tier": 20,
        "somber": True,
        "id": 104,
        "recipe": [
            (3, Materials.GruesomeBone),
            (30, Materials.Bloodrose),
            (10, Materials.BloodTaintedExcrement),
        ],
    },
    "Crystal Knife": {
        "previous": "Wakizashi",
        "tier": 15,
        "somber": False,
        "id": 105,
        "recipe": [
            (22, Materials.CrackedCrystal),
            (8, Materials.StoneFragment),
            (4, Materials.GlintstoneDust),
            (10, Materials.GlintstoneFirefly),
        ],
    },
    "Celebrant's Sickle": {
        "previous": "Misericorde",
        "tier": 12,
        "somber": False,
        "id": 106,
        "recipe": [
            (6, Materials.StoneFragment),
            (10, Materials.GoldFirefly),
            (12, Materials.HumanBoneShard),
            (18, Materials.TarnishedGoldenSunflower),
        ],
    },
    "Glintstone Kris": {
        "previous": "Crystal Knife",
        "tier": 20,
        "somber": True,
        "id": 107,
        "recipe": [
            (1, Materials.MetalPlate),
            (15, Materials.CrystalBud),
            (10, Materials.SomberStoneFragment),
        ],
    },
    "Scorpion's Stinger": {
        "previous": "Ivory Sickle",
        "tier": 20,
        "somber": True,
        "id": 108,
        "recipe": [
            (1, Materials.MetalPlate),
            (15, Materials.AeonianButterfly),
            (10, Materials.SomberStoneFragment),
        ],
    },
    "Great Knife": {
        "previous": "Dagger",
        "tier": 3,
        "somber": False,
        "id": 109,
        "recipe": [
            (1, Materials.MetalPlate),
            (1, Materials.MetalShards),
            (3, Materials.StoneFragment),
        ],
    },
    "Wakizashi": {
        "previous": "Parrying Dagger",
        "tier": 12,
        "somber": False,
        "id": 110,
        "recipe": [
            (1, Materials.MetalPlate),
            (8, Materials.MetalShards),
            (6, Materials.StoneFragment),
            (15, Materials.AltusBloom),
        ],
    },
    "Cinquedea": {
        "previous": "Wakizashi",
        "tier": 20,
        "somber": True,
        "id": 111,
        "recipe": [
            (20, Materials.SanctuaryStone),
            (10, Materials.BeastBlood),
            (10, Materials.SomberStoneFragment),
            (7, Materials.GravelStone),
        ],
    },
    "Ivory Sickle": {
        "previous": "Celebrant's Sickle",
        "tier": 15,
        "somber": False,
        "id": 113,
        "recipe": [
            (3, Materials.GruesomeBone),
            (10, Materials.HeftyBeastBone),
            (8, Materials.StoneFragment),
            (10, Materials.SilverFirefly),
        ],
    },
    "Bloodstained Dagger": {
        "previous": "Great Knife",
        "tier": 6,
        "somber": False,
        "id": 114,
        "recipe": [
            (1, Materials.MetalPlate),
            (4, Materials.StoneFragment),
            (3, Materials.BeastBlood),
        ],
    },
    "Erdsteel Dagger": {
        "previous": "Wakizashi",
        "tier": 15,
        "somber": False,
        "id": 115,
        "recipe": [
            (1, Materials.MetalPlate),
            (9, Materials.StoneFragment),
            (4, Materials.ErdtreeWood),
            (10, Materials.GoldenSunflower),
        ],
    },
    "Blade of Calling": {
        "previous": "Erdsteel Dagger",
        "tier": 18,
        "somber": True,
        "id": 116,
        "recipe": [
            (1, Materials.MetalPlate),
            (9, Materials.SomberStoneFragment),
            (13, Materials.ArteriaLeaf),
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
            (2, Materials.MetalPlate),
            (6, Materials.MetalShards),
        ],
    },
    "Short Sword": {
        "previous": "Dagger",
        "tier": 2,
        "somber": False,
        "id": 201,
        "recipe": [
            (1, Materials.MetalPlate),
            (2, Materials.MetalShards),
        ],
    },
    "Broadsword": {
        "previous": "Longsword",
        "tier": 8,
        "somber": False,
        "id": 202,
        "recipe": [
            (2, Materials.MetalPlate),
            (8, Materials.MetalShards),
            (9, Materials.SilverFirefly),
        ],
    },
    "Lordsworn's Straight Sword": {
        "previous": "Broadsword",
        "tier": 10,
        "somber": False,
        "id": 204,
        "recipe": [
            (2, Materials.MetalPlate),
            (7, Materials.MetalShards),
            (7, Materials.RootResin),
            (8, Materials.AltusBloom),
        ],
    },
    "Weathered Straight Sword": {
        "previous": "Short Sword",
        "tier": 4,
        "somber": False,
        "id": 205,
        "recipe": [
            (2, Materials.MetalPlate),
            (4, Materials.MetalShards),
        ],
    },
    "Ornamental Straight Sword": {
        "previous": "Lordsworn's Straight Sword",
        "tier": 12,
        "somber": True,
        "id": 206,
        "recipe": [
            (2, Materials.MetalPlate),
            (6, Materials.SomberStoneFragment),
            (6, Materials.GoldenCentipede),
        ],
    },
    "Golden Epitaph": {
        "previous": "Coded Sword",
        "tier": 18,
        "somber": True,
        "id": 207,
        "recipe": [
            (2, Materials.MetalPlate),
            (9, Materials.StoneFragment),
            (25, Materials.AltusBloom),
            (16, Materials.GoldenSunflower),
        ],
    },
    "Nox Flowing Sword": {
        "previous": "Flowing Curved Sword",
        "tier": 18,
        "somber": True,
        "id": 208,
        "recipe": [
            (2, Materials.MetalPlate),
            (6, Materials.PliableMetal),
            (15, Materials.SilverTearHusk),
        ],
    },
    "Inseparable Sword": {
        "previous": "Flamberge",
        "tier": 16,
        "somber": True,
        "id": 209,
        "recipe": [
            (3, Materials.MetalPlate),
            (8, Materials.SomberStoneFragment),
            (15, Materials.SilverFirefly),
            (15, Materials.GoldFirefly),
        ],
    },
    "Coded Sword": {
        "previous": "Ornamental Straight Sword",
        "tier": 16,
        "somber": True,
        "id": 211,
        "recipe": [
            (8, Materials.SomberStoneFragment),
            (10, Materials.GoldTingedExcrement),
            (10, Materials.GoldenCentipede),
        ],
    },
    "Sword of Night and Flame": {
        "previous": "Carian Knight's Sword",
        "tier": 20,
        "somber": True,
        "id": 214,
        "recipe": [
            (15, Materials.SomberStoneFragment),
            (12, Materials.GlintstoneDust),
            (6, Materials.ErdtreeAmber),
            (6, Materials.MeteoriteChunk),
        ],
    },
    "Crystal Sword": {
        "previous": "Longsword",
        "tier": 8,
        "somber": True,
        "id": 215,
        "recipe": [
            (4, Materials.GlintstoneDust),
            (5, Materials.GlintstoneFirefly),
            (10, Materials.CrackedCrystal),
        ],
    },
    "Carian Knight's Sword": {
        "previous": "Sword of St. Trina",
        "tier": 16,
        "somber": True,
        "id": 218,
        "recipe": [
            (2, Materials.MetalPlate),
            (8, Materials.RimedCrystalBud),
            (5, Materials.GlintstoneDust),
            (15, Materials.GlintstoneFirefly),
        ],
    },
    "Sword of St. Trina": {
        "previous": "Lazuli Glintstone Sword",
        "tier": 14,
        "somber": True,
        "id": 219,
        "recipe": [
            (2, Materials.MetalPlate),
            (7, Materials.StoneFragment),
            (8, Materials.SlumberingEgg),
            (8, Materials.TrinasLily),
        ],
    },
    "Miquellan Knight's Sword": {
        "previous": "Golden Epitaph",
        "tier": 20,
        "somber": True,
        "id": 220,
        "recipe": [
            (2, Materials.MetalPlate),
            (5, Materials.ErdtreeAmber),
            (20, Materials.MiquellasLily),
        ],
    },
    "Cane Sword": {
        "previous": "Noble's Slender Sword",
        "tier": 15,
        "somber": False,
        "id": 221,
        "recipe": [
            (1, Materials.MetalPlate),
            (8, Materials.SoftWood),
            (8, Materials.ArteriaLeaf),
            (15, Materials.MetalShards),
        ],
    },
    "Regalia of Eochaid": {
        "previous": "Warhawk's Talon",
        "tier": 20,
        "somber": True,
        "id": 222,
        "recipe": [
            (2, Materials.MetalPlate),
            (5, Materials.GruesomeBone),
            (10, Materials.Bloodrose),
            (15, Materials.SacramentalBud),
        ],
    },
    "Noble's Slender Sword": {
        "previous": "Lordsworn's Straight Sword",
        "tier": 12,
        "somber": False,
        "id": 223,
        "recipe": [
            (1, Materials.MetalPlate),
            (10, Materials.MetalShards),
            (12, Materials.AltusBloom),
            (15, Materials.TarnishedGoldenSunflower),
        ],
    },
    "Warhawk's Talon": {
        "previous": "Cane Sword",
        "tier": 18,
        "somber": False,
        "id": 224,
        "recipe": [
            (2, Materials.MetalPlate),
            (15, Materials.MetalShards),
            (10, Materials.StoneFragment),
            (12, Materials.StormhawkFeather),
        ],
    },
    "Lazuli Glintstone Sword": {
        "previous": "Rotten Crystal Sword",
        "tier": 12,
        "somber": True,
        "id": 225,
        "recipe": [
            (10, Materials.SoftWood),
            (5, Materials.RefinedWood),
            (4, Materials.GlintstoneDust),
        ],
    },
    "Rotten Crystal Sword": {
        "previous": "Crystal Sword",
        "tier": 10,
        "somber": True,
        "id": 226,
        "recipe": [
            (3, Materials.AeonianButterfly),
            (5, Materials.SomberStoneFragment),
            (12, Materials.CrackedCrystal),
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
            (3, Materials.MetalPlate),
            (8, Materials.MetalShards),
        ],
    },
    "Forked Greatsword": {
        "previous": "Claymore",
        "tier": 12,
        "somber": False,
        "id": 301,
        "recipe": [
            (2, Materials.MetalPlate),
            (10, Materials.MetalShards),
            (6, Materials.StoneFragment),
            (10, Materials.GraveViolet),
        ],
    },
    "Iron Greatsword": {
        "previous": "Banished Knight's Greatsword",
        "tier": 15,
        "somber": False,
        "id": 302,
        "recipe": [
            (3, Materials.MetalPlate),
            (5, Materials.GravelStone),
            (10, Materials.MetalShards),
            (10, Materials.StoneFragment),
        ],
    },
    "Lordsworn's Greatsword": {
        "previous": "Claymore",
        "tier": 12,
        "somber": False,
        "id": 303,
        "recipe": [
            (2, Materials.MetalPlate),
            (15, Materials.AltusBloom),
            (10, Materials.MetalShards),
        ],
    },
    "Knight's Greatsword": {
        "previous": "Banished Knight's Greatsword",
        "tier": 15,
        "somber": False,
        "id": 304,
        "recipe": [
            (3, Materials.MetalPlate),
            (12, Materials.MetalShards),
            (12, Materials.AltusBloom),
        ],
    },
    "Flamberge": {
        "previous": "Forked Greatsword",
        "tier": 14,
        "somber": False,
        "id": 305,
        "recipe": [
            (2, Materials.MetalPlate),
            (9, Materials.MetalShards),
            (15, Materials.Bloodrose),
            (5, Materials.SacramentalBud),
        ],
    },
    "Ordovis's Greatsword": {
        "previous": "Blasphemous Blade",
        "tier": 20,
        "somber": True,
        "id": 306,
        "recipe": [
            (3, Materials.MetalPlate),
            (10, Materials.SomberStoneFragment),
            (15, Materials.GoldTingedExcrement),
            (5, Materials.ErdtreeAmber),
        ],
    },
    "Alabaster Lord's Sword": {
        "previous": "Knight's Greatsword",
        "tier": 16,
        "somber": True,
        "id": 307,
        "recipe": [
            (5, Materials.MeteoriteChunk),
            (8, Materials.SomberStoneFragment),
            (6, Materials.GlintstoneDust),
        ],
    },
    "Banished Knight's Greatsword": {
        "previous": "Lordsworn's Greatsword",
        "tier": 14,
        "somber": False,
        "id": 308,
        "recipe": [
            (3, Materials.MetalPlate),
            (10, Materials.MetalShards),
            (12, Materials.SanctuaryStone),
        ],
    },
    "Dark Moon Greatsword": {
        "previous": "Helphen's Steeple",
        "tier": 20,
        "somber": True,
        "id": 309,
        "recipe": [
            (3, Materials.MetalPlate),
            (12, Materials.SomberStoneFragment),
            (6, Materials.PliableMetal),
            (7, Materials.MeteoriteChunk),
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
            (2, Materials.MetalPlate),
            (5, Materials.PliableMetal),
            (3, Materials.BlackMark),
            (20, Materials.GraveViolet),
        ],
    },
    "Blasphemous Blade": {
        "previous": "Knight's Greatsword",
        "tier": 18,
        "somber": True,
        "id": 314,
        "recipe": [
            (1, Materials.Remembrance_Rykard),
            (3, Materials.MetalPlate),
            (8, Materials.BloodTaintedExcrement),
            (30, Materials.VolcanicStone),
        ],
    },
    "Marais Executioner's Sword": {
        "previous": "Knight's Greatsword",
        "tier": 20,
        "somber": True,
        "id": 315,
        "recipe": [
            (3, Materials.MetalPlate),
            (15, Materials.MetalShards),
            (10, Materials.SomberStoneFragment),
            (8, Materials.BloodTaintedExcrement),
        ],
    },
    "Sword of Milos": {
        "previous": "Flamberge",
        "tier": 16,
        "somber": True,
        "id": 316,
        "recipe": [
            (3, Materials.MetalPlate),
            (12, Materials.HeftyBeastBone),
            (12, Materials.FormicRock),
            (5, Materials.BloodTaintedExcrement),
        ],
    },
    "Golden Order Greatsword": {
        "previous": "Inseparable Sword",
        "tier": 20,
        "somber": True,
        "id": 317,
        "recipe": [
            (3, Materials.MetalPlate),
            (10, Materials.SomberStoneFragment),
            (7, Materials.ErdtreeAmber),
            (30, Materials.GoldenSunflower),
        ],
    },
    "Claymore": {
        "previous": "Bastard Sword",
        "tier": 10,
        "somber": False,
        "id": 318,
        "recipe": [
            (2, Materials.MetalPlate),
            (7, Materials.MetalShards),
            (6, Materials.StoneFragment),
        ],
    },
    "Gargoyle's Greatsword": {
        "previous": "Knight's Greatsword",
        "tier": 18,
        "somber": False,
        "id": 319,
        "recipe": [
            (3, Materials.MetalPlate),
            (12, Materials.StoneFragment),
            (10, Materials.RootResin),
            (20, Materials.MeltedMushroom),
        ],
    },
    "Death's Poker": {
        "previous": "Sword of Milos",
        "tier": 20,
        "somber": True,
        "id": 320,
        "recipe": [
            (10, Materials.SomberStoneFragment),
            (15, Materials.BuddingHorn),
            (20, Materials.HumanBoneShard),
            (30, Materials.FlightPinion),
        ],
    },
    "Gargoyle's Blackblade": {
        "previous": "Gargoyle's Greatsword",
        "tier": 20,
        "somber": True,
        "id": 321,
        "recipe": [
            (3, Materials.MetalPlate),
            (10, Materials.SomberStoneFragment),
            (3, Materials.BlackMark),
            (3, Materials.ErdtreeAmber),
        ],
    },
    "Greatsword": {
        "previous": "Watchdog's Greatsword",
        "tier": 18,
        "somber": False,
        "id": 400,
        "recipe": [
            (3, Materials.MetalPlate),
            (12, Materials.MetalShards),
            (9, Materials.StoneFragment),
            (2, Materials.MeteoriteChunk),
        ],
    },
    "Watchdog's Greatsword": {
        "previous": "Zweihander",
        "tier": 17,
        "somber": False,
        "id": 401,
        "recipe": [
            (3, Materials.MetalPlate),
            (13, Materials.StoneFragment),
            (15, Materials.GraveViolet),
        ],
    },
    "Maliketh's Black Blade": {
        "previous": "Watchdog's Greatsword",
        "tier": 20,
        "somber": True,
        "id": 402,
        "recipe": [
            (1, Materials.Remembrance_Maliketh),
            (20, Materials.SomberStoneFragment),
            (20, Materials.GravelStone),
            (5, Materials.BlackMark),
        ],
    },
    "Troll's Golden Sword": {
        "previous": "Zweihander",
        "tier": 17,
        "somber": False,
        "id": 403,
        "recipe": [
            (3, Materials.MetalPlate),
            (10, Materials.MetalShards),
            (15, Materials.GoldTingedExcrement),
        ],
    },
    "Zweihander": {
        "previous": "Iron Greatsword",
        "tier": 16,
        "somber": False,
        "id": 404,
        "recipe": [
            (4, Materials.MetalPlate),
            (7, Materials.StoneFragment),
            (12, Materials.ArteriaLeaf),
        ],
    },
    "Starscourge Greatsword": {
        "previous": "Watchdog's Greatsword",
        "tier": 20,
        "somber": True,
        "id": 405,
        "recipe": [
            (1, Materials.Remembrance_Radahn),
            (3, Materials.MetalPlate),
            (6, Materials.MeteoriteChunk),
            (12, Materials.SomberStoneFragment),
        ],
    },
    "Royal Greatsword": {
        "previous": "Troll Knight's Sword",
        "tier": 20,
        "somber": True,
        "id": 406,
        "recipe": [
            (3, Materials.MetalPlate),
            (8, Materials.GlintstoneDust),
            (20, Materials.RimedCrystalBud),
            (4, Materials.MeteoriteChunk),
        ],
    },
    "Godslayer's Greatsword": {
        "previous": "Troll Knight's Sword",
        "tier": 20,
        "somber": True,
        "id": 407,
        "recipe": [
            (3, Materials.MetalPlate),
            (12, Materials.MetalShards),
            (7, Materials.PliableMetal),
            (4, Materials.BlackMark),
        ],
    },
    "Ruins Greatsword": {
        "previous": "Greatsword",
        "tier": 20,
        "somber": True,
        "id": 408,
        "recipe": [
            (5, Materials.MeteoriteChunk),
            (20, Materials.SomberStoneFragment),
            (30, Materials.SanctuaryStone),
            (10, Materials.GravelStone),
        ],
    },
    "Grafted Blade Greatsword": {
        "previous": "Greatsword",
        "tier": 20,
        "somber": True,
        "id": 410,
        "recipe": [
            (3, Materials.MetalPlate),
            (25, Materials.MetalShards),
        ],
    },
    "Troll Knight's Sword": {
        "previous": "Troll's Golden Sword",
        "tier": 18,
        "somber": True,
        "id": 411,
        "recipe": [
            (3, Materials.MetalPlate),
            (9, Materials.GlintstoneDust),
            (9, Materials.RimedCrystalBud),
            (2, Materials.MeteoriteChunk),
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
            (2, Materials.MetalPlate),
            (5, Materials.MetalShards),
            (6, Materials.StoneFragment),
            (10, Materials.AltusBloom),
        ],
    },
    "Cleanrot Knight's Sword": {
        "previous": "Estoc",
        "tier": 14,
        "somber": False,
        "id": 501,
        "recipe": [
            (2, Materials.MetalPlate),
            (8, Materials.StoneFragment),
            (2, Materials.ErdtreeWood),
        ],
    },
    "Rapier": {
        "previous": "Longsword",
        "tier": 8,
        "somber": False,
        "id": 502,
        "recipe": [
            (2, Materials.MetalPlate),
            (5, Materials.StoneFragment),
            (7, Materials.SilverFirefly),
        ],
    },
    "Rogier's Rapier": {
        "previous": "Estoc",
        "tier": 14,
        "somber": False,
        "id": 503,
        "recipe": [
            (2, Materials.MetalPlate),
            (8, Materials.StoneFragment),
            (10, Materials.GlintstoneFirefly),
            (2, Materials.GlintstoneDust),
        ],
    },
    "Antspur Rapier": {
        "previous": "Rogier's Rapier",
        "tier": 17,
        "somber": False,
        "id": 504,
        "recipe": [
            (4, Materials.PliableMetal),
            (13, Materials.ToxicMushroom),
            (7, Materials.FormicRock),
            (7, Materials.AeonianButterfly),
        ],
    },
    "Frozen Needle": {
        "previous": "Antspur Rapier",
        "tier": 20,
        "somber": True,
        "id": 505,
        "recipe": [
            (5, Materials.PliableMetal),
            (5, Materials.GlintstoneDust),
            (12, Materials.RimedCrystalBud),
            (15, Materials.AlbinauricBloodclot),
        ],
    },
    "Noble's Estoc": {
        "previous": "Rapier",
        "tier": 10,
        "somber": False,
        "id": 506,
        "recipe": [
            (2, Materials.MetalPlate),
            (8, Materials.StoneFragment),
            (12, Materials.TarnishedGoldenSunflower),
        ],
    },
    "Bloody Helice": {
        "previous": "Godskin Stitcher",
        "tier": 20,
        "somber": True,
        "id": 600,
        "recipe": [
            (5, Materials.PliableMetal),
            (3, Materials.GruesomeBone),
            (13, Materials.BeastBlood),
            (13, Materials.BloodTaintedExcrement),
        ],
    },
    "Godskin Stitcher": {
        "previous": "Great Epee",
        "tier": 17,
        "somber": False,
        "id": 601,
        "recipe": [
            (3, Materials.MetalPlate),
            (10, Materials.StoneFragment),
            (15, Materials.StripOfWhiteFlesh),
            (1, Materials.BlackMark),
        ],
    },
    "Great Epee": {
        "previous": "Cleanrot Knight's Sword",
        "tier": 16,
        "somber": False,
        "id": 602,
        "recipe": [
            (3, Materials.MetalPlate),
            (10, Materials.MetalShards),
            (10, Materials.StoneFragment),
        ],
    },
    "Dragon King's Cragblade": {
        "previous": "Godskin Stitcher",
        "tier": 20,
        "somber": True,
        "id": 604,
        "recipe": [
            (1, Materials.Remembrance_Dragonlord),
            (10, Materials.DragonTeeth),
            (15, Materials.StoneFragment),
            (15, Materials.GravelStone),
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
            (2, Materials.MetalPlate),
            (4, Materials.StoneFragment),
            (6, Materials.SilverFirefly),
        ],
    },
    "Beastman's Curved Sword": {
        "previous": "Serpent-God's Curved Sword",
        "tier": 12,
        "somber": False,
        "id": 701,
        "recipe": [
            (2, Materials.MetalPlate),
            (6, Materials.MetalShards),
            (10, Materials.ThinBeastBones),
            (5, Materials.BeastBlood),
        ],
    },
    "Shotel": {
        "previous": "Flowing Curved Sword",
        "tier": 18,
        "somber": False,
        "id": 702,
        "recipe": [
            (2, Materials.MetalPlate),
            (11, Materials.StoneFragment),
            (10, Materials.FormicRock),
            (9, Materials.ArteriaLeaf),
        ],
    },
    "Shamshir": {
        "previous": "Scimitar",
        "tier": 6,
        "somber": False,
        "id": 703,
        "recipe": [
            (1, Materials.MetalPlate),
            (4, Materials.StoneFragment),
            (4, Materials.OldFang),
        ],
    },
    "Bandit's Curved Sword": {
        "previous": "Shamshir",
        "tier": 8,
        "somber": False,
        "id": 704,
        "recipe": [
            (2, Materials.MetalPlate),
            (5, Materials.StoneFragment),
            (5, Materials.SanctuaryStone),
            (5, Materials.RootResin),
        ],
    },
    "Magma Blade": {
        "previous": "Nox Flowing Sword",
        "tier": 20,
        "somber": True,
        "id": 705,
        "recipe": [
            (2, Materials.MetalPlate),
            (12, Materials.SomberStoneFragment),
            (15, Materials.VolcanicStone),
            (20, Materials.FireBlossom),
        ],
    },
    "Flowing Curved Sword": {
        "previous": "Mantis Blade",
        "tier": 15,
        "somber": False,
        "id": 706,
        "recipe": [
            (2, Materials.MetalPlate),
            (9, Materials.StoneFragment),
            (3, Materials.PliableMetal),
            (10, Materials.RimedCrystalBud),
        ],
    },
    "Wing of Astel": {
        "previous": "Nox Flowing Sword",
        "tier": 20,
        "somber": True,
        "id": 707,
        "recipe": [
            (2, Materials.MetalPlate),
            (12, Materials.SomberStoneFragment),
            (3, Materials.MeteoriteChunk),
            (10, Materials.GlintstoneDust),
        ],
    },
    "Scavenger's Curved Sword": {
        "previous": "Falchion",
        "tier": 10,
        "somber": False,
        "id": 708,
        "recipe": [
            (2, Materials.MetalPlate),
            (5, Materials.StoneFragment),
            (10, Materials.MetalShards),
            (1, Materials.DragonTeeth),
        ],
    },
    "Eclipse Shotel": {
        "previous": "Shotel",
        "tier": 20,
        "somber": True,
        "id": 710,
        "recipe": [
            (2, Materials.MetalPlate),
            (15, Materials.SomberStoneFragment),
            (6, Materials.PliableMetal),
            (2, Materials.BlackMark),
        ],
    },
    "Serpent-God's Curved Sword": {
        "previous": "Bandit's Curved Sword",
        "tier": 10,
        "somber": False,
        "id": 711,
        "recipe": [
            (2, Materials.MetalPlate),
            (6, Materials.StoneFragment),
            (8, Materials.SacramentalBud),
            (6, Materials.BeastBlood),
        ],
    },
    "Mantis Blade": {
        "previous": "Scavenger's Curved Sword",
        "tier": 12,
        "somber": False,
        "id": 712,
        "recipe": [
            (1, Materials.MetalPlate),
            (7, Materials.StoneFragment),
            (5, Materials.String),
            (12, Materials.GraveViolet),
        ],
    },
    "Scimitar": {
        "previous": "Short Sword",
        "tier": 4,
        "somber": False,
        "id": 714,
        "recipe": [
            (1, Materials.MetalPlate),
            (4, Materials.StoneFragment),
            (10, Materials.TarnishedGoldenSunflower),
        ],
    },
    "Grossmesser": {
        "previous": "Beastman's Curved Sword",
        "tier": 14,
        "somber": False,
        "id": 715,
        "recipe": [
            (2, Materials.MetalPlate),
            (10, Materials.StoneFragment),
            (8, Materials.GoldFirefly),
        ],
    },
    "Onyx Lord's Greatsword": {
        "previous": "Omen Cleaver",
        "tier": 20,
        "somber": True,
        "id": 801,
        "recipe": [
            (7, Materials.MeteoriteChunk),
            (14, Materials.SomberStoneFragment),
            (15, Materials.GoldFirefly),
            (8, Materials.GoldTingedExcrement),
        ],
    },
    "Dismounter": {
        "previous": "Grossmesser",
        "tier": 16,
        "somber": False,
        "id": 802,
        "recipe": [
            (3, Materials.MetalPlate),
            (10, Materials.StoneFragment),
            (10, Materials.FormicRock),
        ],
    },
    "Bloodhound's Fang": {
        "previous": "Zamor Curved Sword",
        "tier": 18,
        "somber": True,
        "id": 803,
        "recipe": [
            (2, Materials.MetalPlate),
            (11, Materials.SomberStoneFragment),
            (3, Materials.PliableMetal),
            (7, Materials.BloodTaintedExcrement),
        ],
    },
    "Magma Wyrm's Scalesword": {
        "previous": "Omen Cleaver",
        "tier": 20,
        "somber": True,
        "id": 804,
        "recipe": [
            (17, Materials.SomberStoneFragment),
            (5, Materials.DragonTeeth),
            (20, Materials.VolcanicStone),
            (15, Materials.FireBlossom),
        ],
    },
    "Zamor Curved Sword": {
        "previous": "Monk's Flameblade",
        "tier": 16,
        "somber": True,
        "id": 805,
        "recipe": [
            (3, Materials.MetalPlate),
            (2, Materials.PliableMetal),
            (10, Materials.SomberStoneFragment),
            (11, Materials.RimedCrystalBud),
        ],
    },
    "Omen Cleaver": {
        "previous": "Dismounter",
        "tier": 18,
        "somber": False,
        "id": 806,
        "recipe": [
            (3, Materials.MetalPlate),
            (12, Materials.StoneFragment),
            (10, Materials.MetalShards),
            (15, Materials.GoldenSunflower),
        ],
    },
    "Monk's Flameblade": {
        "previous": "Scavenger's Curved Sword",
        "tier": 12,
        "somber": False,
        "id": 807,
        "recipe": [
            (3, Materials.MetalPlate),
            (7, Materials.MetalShards),
            (7, Materials.StoneFragment),
            (10, Materials.VolcanicStone),
        ],
    },
    "Beastman's Cleaver": {
        "previous": "Omen Cleaver",
        "tier": 20,
        "somber": False,
        "id": 808,
        "recipe": [
            (5, Materials.MetalPlate),
            (20, Materials.StoneFragment),
            (5, Materials.HeftyBeastBone),
        ],
    },
    "Morgott's Cursed Sword": {
        "previous": "Bloodhound's Fang",
        "tier": 20,
        "somber": True,
        "id": 810,
        "recipe": [
            (1, Materials.Remembrance_Morgott),
            (9, Materials.PliableMetal),
            (9, Materials.ErdtreeAmber),
            (13, Materials.ArteriaLeaf),
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
            (2, Materials.MetalPlate),
            (12, Materials.StoneFragment),
            (10, Materials.Bloodrose),
            (10, Materials.AltusBloom),
        ],
    },
    "Nagakiba": {
        "previous": "Serpentbone Blade",
        "tier": 17,
        "somber": False,
        "id": 901,
        "recipe": [
            (3, Materials.MetalPlate),
            (17, Materials.StoneFragment),
            (10, Materials.FourToedFowlFoot),
        ],
    },
    "Hand of Malenia": {
        "previous": "Nagakiba",
        "tier": 20,
        "somber": True,
        "id": 902,
        "recipe": [
            (1, Materials.Remembrance_Malenia),
            (8, Materials.PliableMetal),
            (5, Materials.ErdtreeWood),
            (30, Materials.MiquellasLily),
        ],
    },
    "Meteoric Ore Blade": {
        "previous": "Serpentbone Blade",
        "tier": 18,
        "somber": True,
        "id": 903,
        "recipe": [
            (6, Materials.MeteoriteChunk),
            (18, Materials.SomberStoneFragment),
            (15, Materials.SacramentalBud),
        ],
    },
    "Rivers of Blood": {
        "previous": "Dragonscale Blade",
        "tier": 20,
        "somber": True,
        "id": 904,
        "recipe": [
            (2, Materials.MetalPlate),
            (20, Materials.SomberStoneFragment),
            (20, Materials.Bloodrose),
            (10, Materials.BloodTaintedExcrement),
        ],
    },
    "Moonveil": {
        "previous": "Meteoric Ore Blade",
        "tier": 20,
        "somber": True,
        "id": 906,
        "recipe": [
            (30, Materials.CrackedCrystal),
            (10, Materials.GlintstoneDust),
            (20, Materials.SomberStoneFragment),
            (20, Materials.NascentButterfly),
        ],
    },
    "Dragonscale Blade": {
        "previous": "Serpentbone Blade",
        "tier": 16,
        "somber": True,
        "id": 907,
        "recipe": [
            (10, Materials.GravelStone),
            (5, Materials.DragonTeeth),
            (16, Materials.SomberStoneFragment),
            (12, Materials.FormicRock),
        ],
    },
    "Serpentbone Blade": {
        "previous": "Uchigatana",
        "tier": 15,
        "somber": False,
        "id": 908,
        "recipe": [
            (2, Materials.MetalPlate),
            (4, Materials.GruesomeBone),
            (10, Materials.MirandaPowder),
            (20, Materials.Poisonbloom),
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
            (2, Materials.MetalPlate),
            (9, Materials.StoneFragment),
            (8, Materials.String),
            (10, Materials.Fulgurbloom),
        ],
    },
    "Godskin Peeler": {
        "previous": "Twinned Knight Swords",
        "tier": 16,
        "somber": False,
        "id": 1001,
        "recipe": [
            (2, Materials.MetalPlate),
            (12, Materials.StoneFragment),
            (8, Materials.ArteriaLeaf),
            (1, Materials.BlackMark),
        ],
    },
    "Twinned Knight Swords": {
        "previous": "Twinblade",
        "tier": 14,
        "somber": False,
        "id": 1003,
        "recipe": [
            (2, Materials.MetalPlate),
            (10, Materials.StoneFragment),
            (15, Materials.AltusBloom),
        ],
    },
    "Eleonora's Poleblade": {
        "previous": "Godskin Peeler",
        "tier": 20,
        "somber": True,
        "id": 1005,
        "recipe": [
            (2, Materials.MetalPlate),
            (4, Materials.GruesomeBone),
            (18, Materials.Bloodrose),
            (12, Materials.BloodTaintedExcrement),
        ],
    },
    "Gargoyle's Twinblade": {
        "previous": "Twinned Knight Swords",
        "tier": 17,
        "somber": False,
        "id": 1008,
        "recipe": [
            (3, Materials.MetalPlate),
            (14, Materials.StoneFragment),
            (10, Materials.RootResin),
            (12, Materials.GoldFirefly),
        ],
    },
    "Gargoyle's Black Blades": {
        "previous": "Gargoyle's Twinblade",
        "tier": 20,
        "somber": True,
        "id": 1009,
        "recipe": [
            (2, Materials.MetalPlate),
            (3, Materials.BlackMark),
            (4, Materials.ErdtreeAmber),
            (20, Materials.MeltedMushroom),
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
            (2, Materials.MetalPlate),
            (10, Materials.MetalShards),
        ],
    },
    "Club": {
        "visibility_flag": 0,
        "previous": None,
        "tier": 0,
        "somber": False,
        "id": 1101,
        "recipe": [
            (3, Materials.SoftWood),
        ],
        "cost": 50,
    },
    "Curved Club": {
        "previous": "Club",
        "tier": 3,
        "somber": False,
        "id": 1103,
        "recipe": [
            (5, Materials.SoftWood),
        ],
    },
    "Warpick": {
        "previous": "Club",
        "tier": 3,
        "somber": False,
        "id": 1104,
        "recipe": [
            (1, Materials.MetalPlate),
            (3, Materials.MetalShards),
            (3, Materials.SoftWood),
        ],
    },
    "Morning Star": {
        "previous": "Mace",
        "tier": 12,
        "somber": False,
        "id": 1105,
        "recipe": [
            (2, Materials.MetalPlate),
            (12, Materials.MetalShards),
            (8, Materials.StoneFragment),
        ],
    },
    "Varre's Bouquet": {
        "previous": "Monk's Flamemace",
        "tier": 20,
        "somber": True,
        "id": 1106,
        "recipe": [
            (2, Materials.MetalPlate),
            (20, Materials.MetalShards),
            (25, Materials.Bloodrose),
            (10, Materials.BloodTaintedExcrement),
        ],
    },
    "Spiked Club": {
        "previous": "Curved Club",
        "tier": 6,
        "somber": False,
        "id": 1107,
        "recipe": [
            (5, Materials.SoftWood),
            (1, Materials.RefinedWood),
            (5, Materials.OldFang),
            (3, Materials.String),
        ],
    },
    "Hammer": {
        "previous": "Warpick",
        "tier": 6,
        "somber": False,
        "id": 1108,
        "recipe": [
            (2, Materials.MetalPlate),
            (10, Materials.SanctuaryStone),
            (8, Materials.StoneFragment),
        ],
    },
    "Monk's Flamemace": {
        "previous": "Morning Star",
        "tier": 16,
        "somber": False,
        "id": 1109,
        "recipe": [
            (2, Materials.MetalPlate),
            (1, Materials.PliableMetal),
            (20, Materials.MetalShards),
            (8, Materials.StoneFragment),
        ],
    },
    "Envoy's Horn": {
        "previous": "Ringed Finger",
        "tier": 16,
        "somber": True,
        "id": 1110,
        "recipe": [
            (2, Materials.MetalPlate),
            (2, Materials.PliableMetal),
            (15, Materials.GoldFirefly),
            (15, Materials.GoldenSunflower),
        ],
    },
    "Scepter of the All-Knowing": {
        "previous": "Monk's Flamemace",
        "tier": 20,
        "somber": True,
        "id": 1111,
        "recipe": [
            (2, Materials.MetalPlate),
            (5, Materials.PliableMetal),
            (15, Materials.AlbinauricBloodclot),
            (12, Materials.GlintstoneDust),
        ],
    },
    "Nox Flowing Hammer": {
        "previous": "Ringed Finger",
        "tier": 20,
        "somber": True,
        "id": 1112,
        "recipe": [
            (2, Materials.MetalPlate),
            (10, Materials.PliableMetal),
            (30, Materials.SilverTearHusk),
            (5, Materials.RimedCrystalBud),
        ],
    },
    "Ringed Finger": {
        "previous": "Stone Club",
        "tier": 14,
        "somber": True,
        "id": 1113,
        "recipe": [
            (3, Materials.PliableMetal),
            (10, Materials.LivingJarShard),
            (20, Materials.LumpOfFlesh),
            (20, Materials.GraveViolet),
        ],
    },
    "Stone Club": {
        "previous": "Hammer",
        "tier": 9,
        "somber": False,
        "id": 1114,
        "recipe": [
            (12, Materials.StoneFragment),
            (12, Materials.CrackedCrystal),
            (3, Materials.GlintstoneDust),
        ],
    },
    "Marika's Hammer": {
        "previous": "Envoy's Horn",
        "tier": 20,
        "somber": True,
        "id": 1115,
        "recipe": [
            (1, Materials.Remembrance_EldenBeast),
            (10, Materials.ErdtreeAmber),
            (20, Materials.StoneFragment),
            (20, Materials.SomberStoneFragment),
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
            (12, Materials.SoftWood),
            (5, Materials.AltusBloom),
            (5, Materials.SacramentalBud),
        ],
    },
    "Greathorn Hammer": {
        "previous": "Pickaxe",
        "tier": 16,
        "somber": False,
        "id": 1201,
        "recipe": [
            (8, Materials.StoneFragment),
            (10, Materials.HeftyBeastBone),
            (20, Materials.BuddingHorn),
        ],
    },
    "Battle Hammer": {
        "previous": "Pickaxe",
        "tier": 16,
        "somber": False,
        "id": 1202,
        "recipe": [
            (4, Materials.MetalPlate),
            (9, Materials.MetalShards),
            (2, Materials.MeteoriteChunk),
            (2, Materials.PliableMetal),
        ],
    },
    "Great Mace": {
        "previous": "Large Club",
        "tier": 12,
        "somber": False,
        "id": 1206,
        "recipe": [
            (3, Materials.MetalPlate),
            (20, Materials.MetalShards),
            (8, Materials.StoneFragment),
            (3, Materials.MeteoriteChunk),
        ],
    },
    "Curved Great Club": {
        "previous": "Large Club",
        "tier": 12,
        "somber": False,
        "id": 1208,
        "recipe": [
            (13, Materials.SoftWood),
            (3, Materials.RefinedWood),
        ],
    },
    "Celebrant's Skull": {
        "previous": "Large Club",
        "tier": 12,
        "somber": False,
        "id": 1213,
        "recipe": [
            (10, Materials.StoneFragment),
            (2, Materials.GruesomeBone),
            (15, Materials.HumanBoneShard),
            (7, Materials.String),
        ],
    },
    "Pickaxe": {
        "previous": "Curved Great Club",
        "tier": 14,
        "somber": False,
        "id": 1214,
        "recipe": [
            (2, Materials.MetalPlate),
            (3, Materials.RefinedWood),
            (12, Materials.StoneFragment),
            (12, Materials.AltusBloom),
        ],
    },
    "Beastclaw Greathammer": {
        "previous": "Celebrant's Skull",
        "tier": 16,
        "somber": True,
        "id": 1215,
        "recipe": [
            (3, Materials.MetalPlate),
            (20, Materials.GoldenSunflower),
            (10, Materials.SomberStoneFragment),
            (10, Materials.BeastBlood),
        ],
    },
    "Envoy's Long Horn": {
        "previous": "Envoy's Horn",
        "tier": 18,
        "somber": True,
        "id": 1216,
        "recipe": [
            (3, Materials.MetalPlate),
            (4, Materials.PliableMetal),
            (3, Materials.ErdtreeAmber),
            (30, Materials.GoldTingedExcrement),
        ],
    },
    "Cranial Vessel Candlestand": {
        "previous": "Rotten Battle Hammer",
        "tier": 20,
        "somber": True,
        "id": 1217,
        "recipe": [
            (4, Materials.GruesomeBone),
            (30, Materials.SmolderingButterfly),
            (10, Materials.VolcanicStone),
            (25, Materials.FireBlossom),
        ],
    },
    "Great Stars": {
        "previous": "Monk's Flamemace",
        "tier": 20,
        "somber": False,
        "id": 1218,
        "recipe": [
            (3, Materials.MetalPlate),
            (25, Materials.MetalShards),
            (20, Materials.SacramentalBud),
            (10, Materials.BloodTaintedExcrement),
        ],
    },
    "Brick Hammer": {
        "previous": "Great Mace",
        "tier": 14,
        "somber": False,
        "id": 1219,
        "recipe": [
            (20, Materials.StoneFragment),
            (20, Materials.SanctuaryStone),
            (10, Materials.RootResin),
            (6, Materials.String),
        ],
    },
    "Devourer's Scepter": {
        "previous": "Beastclaw Greathammer",
        "tier": 20,
        "somber": True,
        "id": 1220,
        "recipe": [
            (9, Materials.PliableMetal),
            (6, Materials.GruesomeBone),
            (20, Materials.FireBlossom),
            (20, Materials.VolcanicStone),
        ],
    },
    "Rotten Battle Hammer": {
        "previous": "Battle Hammer",
        "tier": 18,
        "somber": False,
        "id": 1221,
        "recipe": [
            (4, Materials.MetalPlate),
            (15, Materials.AeonianButterfly),
            (20, Materials.ToxicMushroom),
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
            (2, Materials.MetalPlate),
            (16, Materials.MetalShards),
            (12, Materials.StoneFragment),
            (2, Materials.MeteoriteChunk),
        ],
    },
    "Flail": {
        "previous": "Morning Star",
        "tier": 15,
        "somber": False,
        "id": 1301,
        "recipe": [
            (3, Materials.RefinedWood),
            (2, Materials.MetalPlate),
            (13, Materials.MetalShards),
            (15, Materials.SilverTearHusk),
        ],
    },
    "Family Heads": {
        "previous": "Nightrider Flail",
        "tier": 18,
        "somber": True,
        "id": 1302,
        "recipe": [
            (2, Materials.MetalPlate),
            (4, Materials.PliableMetal),
            (2, Materials.GruesomeBone),
            (20, Materials.GraveViolet),
        ],
    },
    "Bastard's Stars": {
        "previous": "Family Heads",
        "tier": 20,
        "somber": True,
        "id": 1303,
        "recipe": [
            (1, Materials.Remembrance_Astel),
            (7, Materials.PliableMetal),
            (6, Materials.MeteoriteChunk),
            (12, Materials.GlintstoneDust),
        ],
    },
    "Chainlink Flail": {
        "previous": "Flail",
        "tier": 18,
        "somber": False,
        "id": 1304,
        "recipe": [
            (3, Materials.MetalPlate),
            (3, Materials.RefinedWood),
            (15, Materials.MetalShards),
            (5, Materials.BloodTaintedExcrement),
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
            (1, Materials.MetalPlate),
            (2, Materials.MetalShards),
            (2, Materials.StoneFragment),
        ],
    },
    "Forked Hatchet": {
        "previous": "Celebrant's Cleaver",
        "tier": 10,
        "somber": False,
        "id": 1401,
        "recipe": [
            (2, Materials.MetalPlate),
            (1, Materials.PliableMetal),
            (8, Materials.StoneFragment),
            (8, Materials.GraveViolet),
        ],
    },
    "Hand Axe": {
        "visibility_flag": 0,
        "previous": None,
        "tier": 0,
        "somber": False,
        "id": 1402,
        "recipe": [
            (1, Materials.MetalPlate),
            (1, Materials.SoftWood),
        ],
        "cost": 50,
    },
    "Jawbone Axe": {
        "previous": "Highland Axe",
        "tier": 10,
        "somber": False,
        "id": 1403,
        "recipe": [
            (3, Materials.RefinedWood),
            (2, Materials.GruesomeBone),
            (8, Materials.HeftyBeastBone),
            (10, Materials.GoldTingedExcrement),
        ],
    },
    "Iron Cleaver": {
        "previous": "Warped Axe",
        "tier": 13,
        "somber": False,
        "id": 1404,
        "recipe": [
            (2, Materials.MetalPlate),
            (8, Materials.StoneFragment),
            (8, Materials.MetalShards),
            (10, Materials.Fulgurbloom),
        ],
    },
    "Ripple Blade": {
        "previous": "Icerind Hatchet",
        "tier": 20,
        "somber": False,
        "id": 1405,
        "recipe": [
            (6, Materials.PliableMetal),
            (15, Materials.SomberStoneFragment),
            (20, Materials.SilverFirefly),
            (20, Materials.AlbinauricBloodclot),
        ],
    },
    "Celebrant's Cleaver": {
        "previous": "Battle Axe",
        "tier": 5,
        "somber": False,
        "id": 1406,
        "recipe": [
            (4, Materials.StoneFragment),
            (1, Materials.GruesomeBone),
            (5, Materials.HumanBoneShard),
        ],
    },
    "Icerind Hatchet": {
        "previous": "Forked Hatchet",
        "tier": 16,
        "somber": True,
        "id": 1408,
        "recipe": [
            (2, Materials.MetalPlate),
            (10, Materials.MetalShards),
            (3, Materials.DragonTeeth),
            (12, Materials.RimedCrystalBud),
        ],
    },
    "Highland Axe": {
        "previous": "Celebrant's Cleaver",
        "tier": 8,
        "somber": False,
        "id": 1410,
        "recipe": [
            (2, Materials.MetalPlate),
            (4, Materials.SoftWood),
            (2, Materials.RefinedWood),
            (3, Materials.BeastBlood),
        ],
    },
    "Sacrificial Axe": {
        "previous": "Iron Cleaver",
        "tier": 15,
        "somber": False,
        "id": 1411,
        "recipe": [
            (2, Materials.MetalPlate),
            (10, Materials.SomberStoneFragment),
            (15, Materials.FlightPinion),
            (3, Materials.BloodTaintedExcrement),
        ],
    },
    "Rosus' Axe": {
        "previous": "Sacrificial Axe",
        "tier": 20,
        "somber": True,
        "id": 1412,
        "recipe": [
            (2, Materials.MetalPlate),
            (9, Materials.ErdtreeWood),
            (5, Materials.GruesomeBone),
            (3, Materials.BlackMark),
        ],
    },
    "Stormhawk Axe": {
        "previous": "Sacrificial Axe",
        "tier": 20,
        "somber": True,
        "id": 1414,
        "recipe": [
            (2, Materials.MetalPlate),
            (30, Materials.Fulgurbloom),
            (20, Materials.FourToedFowlFoot),
            (20, Materials.StormhawkFeather),
        ],
    },
    "Greataxe": {
        "previous": "Rusted Anchor",
        "tier": 14,
        "somber": False,
        "id": 1500,
        "recipe": [
            (3, Materials.MetalPlate),
            (12, Materials.SoftWood),
            (10, Materials.MetalShards),
            (10, Materials.StoneFragment),
        ],
    },
    "Warped Axe": {
        "previous": "Highland Axe",
        "tier": 10,
        "somber": False,
        "id": 1501,
        "recipe": [
            (3, Materials.MetalPlate),
            (2, Materials.PliableMetal),
            (10, Materials.RootResin),
            (10, Materials.VolcanicStone),
        ],
    },
    "Great Omenkiller Cleaver": {
        "previous": "Rusted Anchor",
        "tier": 15,
        "somber": False,
        "id": 1502,
        "recipe": [
            (2, Materials.ErdtreeWood),
            (10, Materials.StoneFragment),
            (15, Materials.BuddingHorn),
            (3, Materials.BloodTaintedExcrement),
        ],
    },
    "Crescent Moon Axe": {
        "previous": "Great Omenkiller Cleaver",
        "tier": 18,
        "somber": False,
        "id": 1503,
        "recipe": [
            (3, Materials.MetalPlate),
            (7, Materials.RefinedWood),
            (3, Materials.PliableMetal),
            (10, Materials.RimedCrystalBud),
        ],
    },
    "Axe of Godrick": {
        "previous": "Executioner's Greataxe",
        "tier": 18,
        "somber": True,
        "id": 1504,
        "recipe": [
            (1, Materials.Remembrance_Godrick),
            (3, Materials.MetalPlate),
            (15, Materials.GoldFirefly),
            (25, Materials.TarnishedGoldenSunflower),
        ],
    },
    "Longhaft Axe": {
        "previous": "Warped Axe",
        "tier": 12,
        "somber": False,
        "id": 1505,
        "recipe": [
            (4, Materials.MetalPlate),
            (8, Materials.StoneFragment),
            (12, Materials.AltusBloom),
        ],
    },
    "Rusted Anchor": {
        "previous": "Longhaft Axe",
        "tier": 13,
        "somber": False,
        "id": 1506,
        "recipe": [
            (4, Materials.MetalPlate),
            (10, Materials.MetalShards),
            (10, Materials.StoneFragment),
            (10, Materials.FourToedFowlFoot),
        ],
    },
    "Executioner's Greataxe": {
        "previous": "Greataxe",
        "tier": 16,
        "somber": False,
        "id": 1508,
        "recipe": [
            (3, Materials.MetalPlate),
            (12, Materials.MetalShards),
            (10, Materials.YellowEmber),
            (8, Materials.BloodTaintedExcrement),
        ],
    },
    "Winged Greathorn": {
        "previous": "Crescent Moon Axe",
        "tier": 20,
        "somber": True,
        "id": 1511,
        "recipe": [
            (1, Materials.Remembrance_RegalAncestor),
            (10, Materials.RefinedWood),
            (25, Materials.BuddingHorn),
            (30, Materials.DewkissedHerba),
        ],
    },
    "Butchering Knife": {
        "previous": "Icerind Hatchet",
        "tier": 20,
        "somber": False,
        "id": 1512,
        "recipe": [
            (3, Materials.MetalPlate),
            (5, Materials.PliableMetal),
            (20, Materials.StoneFragment),
            (20, Materials.SacramentalBud),
        ],
    },
    "Gargoyle's Great Axe": {
        "previous": "Great Omenkiller Cleaver",
        "tier": 18,
        "somber": False,
        "id": 1513,
        "recipe": [
            (3, Materials.MetalPlate),
            (12, Materials.MetalShards),
            (12, Materials.RootResin),
            (15, Materials.MeltedMushroom),
        ],
    },
    "Gargoyle's Black Axe": {
        "previous": "Gargoyle's Great Axe",
        "tier": 20,
        "somber": True,
        "id": 1514,
        "recipe": [
            (3, Materials.MetalPlate),
            (15, Materials.SomberStoneFragment),
            (4, Materials.ErdtreeAmber),
            (3, Materials.BlackMark),
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
            (1, Materials.MetalPlate),
            (1, Materials.SoftWood),
        ],
    },
    "Spear": {
        "previous": "Short Spear",
        "tier": 6,
        "somber": False,
        "id": 1601,
        "recipe": [
            (4, Materials.SoftWood),
            (4, Materials.StoneFragment),
        ],
    },
    "Crystal Spear": {
        "previous": "Clayman's Harpoon",
        "tier": 16,
        "somber": True,
        "id": 1602,
        "recipe": [
            (15, Materials.CrackedCrystal),
            (7, Materials.GlintstoneDust),
            (12, Materials.SomberStoneFragment),
        ],
    },
    "Clayman's Harpoon": {
        "previous": "Spiked Spear",
        "tier": 15,
        "somber": False,
        "id": 1603,
        "recipe": [
            (8, Materials.SoftWood),
            (3, Materials.RefinedWood),
            (12, Materials.StoneFragment),
            (3, Materials.MeteoriteChunk),
        ],
    },
    "Cleanrot Spear": {
        "previous": "Spiked Spear",
        "tier": 20,
        "somber": True,
        "id": 1604,
        "recipe": [
            (2, Materials.MetalPlate),
            (9, Materials.ErdtreeWood),
            (6, Materials.ErdtreeAmber),
            (20, Materials.SomberStoneFragment),
        ],
    },
    "Partisan": {
        "previous": "Iron Spear",
        "tier": 12,
        "somber": False,
        "id": 1605,
        "recipe": [
            (2, Materials.MetalPlate),
            (6, Materials.RefinedWood),
            (8, Materials.MetalShards),
            (10, Materials.StoneFragment),
        ],
    },
    "Celebrant's Rib-Rake": {
        "previous": "Spear",
        "tier": 9,
        "somber": False,
        "id": 1606,
        "recipe": [
            (8, Materials.StoneFragment),
            (2, Materials.GruesomeBone),
            (8, Materials.HumanBoneShard),
            (12, Materials.ThinBeastBones),
        ],
    },
    "Pike": {
        "previous": "Partisan",
        "tier": 14,
        "somber": False,
        "id": 1607,
        "recipe": [
            (3, Materials.MetalPlate),
            (12, Materials.StoneFragment),
            (12, Materials.Fulgurbloom),
            (5, Materials.SacramentalBud),
        ],
    },
    "Torchpole": {
        "previous": "Celebrant's Rib-Rake",
        "tier": 12,
        "somber": False,
        "id": 1608,
        "recipe": [
            (5, Materials.RefinedWood),
            (8, Materials.RootResin),
            (10, Materials.AltusBloom),
            (20, Materials.SmolderingButterfly),
        ],
    },
    "Bolt of Gransax": {
        "previous": "Cross-Naginata",
        "tier": 20,
        "somber": True,
        "id": 1609,
        "recipe": [
            (1, Materials.Remembrance_Fortissax),
            (7, Materials.DragonTeeth),
            (15, Materials.GravelStone),
            (25, Materials.Fulgurbloom),
        ],
    },
    "Cross-Naginata": {
        "previous": "Spiked Spear",
        "tier": 17,
        "somber": False,
        "id": 1611,
        "recipe": [
            (2, Materials.MetalPlate),
            (7, Materials.RefinedWood),
            (10, Materials.MetalShards),
            (16, Materials.StoneFragment),
        ],
    },
    "Death Ritual Spear": {
        "previous": "Rotten Crystal Spear",
        "tier": 20,
        "somber": True,
        "id": 1612,
        "recipe": [
            (7, Materials.PliableMetal),
            (20, Materials.SomberStoneFragment),
            (20, Materials.GraveViolet),
            (3, Materials.BlackMark),
        ],
    },
    "Inquisitor's Girandole": {
        "previous": "Spiked Spear",
        "tier": 18,
        "somber": True,
        "id": 1613,
        "recipe": [
            (2, Materials.MetalPlate),
            (15, Materials.MetalShards),
            (15, Materials.VolcanicStone),
            (15, Materials.FireBlossom),
        ],
    },
    "Spiked Spear": {
        "previous": "Torchpole",
        "tier": 14,
        "somber": False,
        "id": 1614,
        "recipe": [
            (2, Materials.MetalPlate),
            (5, Materials.RefinedWood),
            (12, Materials.MetalShards),
            (9, Materials.SacramentalBud),
        ],
    },
    "Iron Spear": {
        "previous": "Spear",
        "tier": 9,
        "somber": False,
        "id": 1615,
        "recipe": [
            (2, Materials.MetalPlate),
            (5, Materials.MetalShards),
            (8, Materials.StoneFragment),
            (5, Materials.RootResin),
        ],
    },
    "Rotten Crystal Spear": {
        "previous": "Crystal Spear",
        "tier": 18,
        "somber": True,
        "id": 1616,
        "recipe": [
            (15, Materials.SomberStoneFragment),
            (3, Materials.GruesomeBone),
            (10, Materials.AeonianButterfly),
            (7, Materials.GlintstoneDust),
        ],
    },
    "Mohgwyn's Sacred Spear": {
        "previous": "Lance",
        "tier": 20,
        "somber": True,
        "id": 1701,
        "recipe": [
            (1, Materials.Remembrance_Mohg),
            (7, Materials.PliableMetal),
            (25, Materials.SacramentalBud),
            (20, Materials.BloodTaintedExcrement),
        ],
    },
    "Siluria's Tree": {
        "previous": "Treespear",
        "tier": 20,
        "somber": True,
        "id": 1702,
        "recipe": [
            (2, Materials.MetalPlate),
            (7, Materials.ErdtreeWood),
            (7, Materials.ErdtreeAmber),
            (15, Materials.BuddingHorn),
        ],
    },
    "Serpent-Hunter": {
        "visibility_flag": Flags.Note_SerpentHunter_Bought,
        "id": 1703,
        "recipe": [
            (3, Materials.MetalPlate),
            (5, Materials.DragonTeeth),
            (15, Materials.Fulgurbloom),
            (1, Materials.BlackMark),
        ],
        "cost": 10000,
    },
    "Vyke's War Spear": {
        "previous": "Inquisitor's Girandole",
        "tier": 20,
        "somber": True,
        "id": 1705,
        "recipe": [
            (3, Materials.MetalPlate),
            (20, Materials.SomberStoneFragment),
            (20, Materials.YellowEmber),
            (30, Materials.EyeOfYelough),
        ],
    },
    "Lance": {
        "previous": "Pike",
        "tier": 16,
        "somber": False,
        "id": 1706,
        "recipe": [
            (3, Materials.MetalPlate),
            (3, Materials.PliableMetal),
            (15, Materials.StoneFragment),
            (15, Materials.RimedRowa),
        ],
    },
    "Treespear": {
        "previous": "Lance",
        "tier": 18,
        "somber": False,
        "id": 1707,
        "recipe": [
            (3, Materials.MetalPlate),
            (18, Materials.StoneFragment),
            (15, Materials.GoldFirefly),
            (3, Materials.ErdtreeAmber),
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
            (2, Materials.MetalPlate),
            (8, Materials.SoftWood),
            (3, Materials.RefinedWood),
            (7, Materials.MetalShards),
        ],
    },
    "Pest's Glaive": {
        "previous": "Halberd",
        "tier": 12,
        "somber": False,
        "id": 1801,
        "recipe": [
            (10, Materials.StoneFragment),
            (3, Materials.GruesomeBone),
            (5, Materials.GoldenCentipede),
            (3, Materials.AeonianButterfly),
        ],
    },
    "Lucerne": {
        "previous": "Banished Knight's Halberd",
        "tier": 14,
        "somber": False,
        "id": 1802,
        "recipe": [
            (2, Materials.MetalPlate),
            (4, Materials.RefinedWood),
            (12, Materials.StoneFragment),
            (8, Materials.Fulgurbloom),
        ],
    },
    "Banished Knight's Halberd": {
        "previous": "Halberd",
        "tier": 12,
        "somber": False,
        "id": 1803,
        "recipe": [
            (2, Materials.MetalPlate),
            (3, Materials.RefinedWood),
            (10, Materials.StoneFragment),
            (15, Materials.FlightPinion),
        ],
    },
    "Commander's Standard": {
        "previous": "Guardian's Swordspear",
        "tier": 20,
        "somber": True,
        "id": 1804,
        "recipe": [
            (2, Materials.MetalPlate),
            (10, Materials.AeonianButterfly),
            (15, Materials.SomberStoneFragment),
            (8, Materials.BloodTaintedExcrement),
        ],
    },
    "Nightrider Glaive": {
        "previous": "Glaive",
        "tier": 16,
        "somber": False,
        "id": 1805,
        "recipe": [
            (3, Materials.MetalPlate),
            (13, Materials.SomberStoneFragment),
            (13, Materials.GraveViolet),
            (1, Materials.BlackMark),
        ],
    },
    "Ripple Crescent Halberd": {
        "previous": "Vulgar Militia Shotel",
        "tier": 20,
        "somber": False,
        "id": 1806,
        "recipe": [
            (7, Materials.PliableMetal),
            (20, Materials.StoneFragment),
            (20, Materials.SilverFirefly),
            (25, Materials.AlbinauricBloodclot),
        ],
    },
    "Vulgar Militia Saw": {
        "previous": "Pest's Glaive",
        "tier": 14,
        "somber": False,
        "id": 1807,
        "recipe": [
            (2, Materials.MetalPlate),
            (10, Materials.SoftWood),
            (15, Materials.Bloodrose),
            (12, Materials.StoneFragment),
        ],
    },
    "Golden Halberd": {
        "previous": "Dragon Halberd",
        "tier": 18,
        "somber": True,
        "id": 1808,
        "recipe": [
            (3, Materials.MetalPlate),
            (3, Materials.ErdtreeAmber),
            (20, Materials.GoldenSunflower),
            (15, Materials.GoldFirefly),
        ],
    },
    "Glaive": {
        "previous": "Lucerne",
        "tier": 16,
        "somber": False,
        "id": 1809,
        "recipe": [
            (2, Materials.MetalPlate),
            (13, Materials.StoneFragment),
            (15, Materials.RootResin),
            (18, Materials.AltusBloom),
        ],
    },
    "Loretta's War Sickle": {
        "previous": "Vulgar Militia Shotel",
        "tier": 20,
        "somber": True,
        "id": 1810,
        "recipe": [
            (2, Materials.MetalPlate),
            (6, Materials.PliableMetal),
            (6, Materials.ErdtreeAmber),
            (20, Materials.GoldFirefly),
        ],
    },
    "Guardian's Swordspear": {
        "previous": "Lucerne",
        "tier": 17,
        "somber": False,
        "id": 1811,
        "recipe": [
            (2, Materials.MetalPlate),
            (7, Materials.ErdtreeWood),
            (15, Materials.StoneFragment),
            (15, Materials.GoldenSunflower),
        ],
    },
    "Vulgar Militia Shotel": {
        "previous": "Vulgar Militia Saw",
        "tier": 17,
        "somber": False,
        "id": 1813,
        "recipe": [
            (2, Materials.MetalPlate),
            (6, Materials.RefinedWood),
            (15, Materials.StoneFragment),
            (10, Materials.ArteriaLeaf),
        ],
    },
    "Dragon Halberd": {
        "previous": "Lucerne",
        "tier": 16,
        "somber": True,
        "id": 1814,
        "recipe": [
            (2, Materials.MetalPlate),
            (3, Materials.DragonTeeth),
            (10, Materials.RimedCrystalBud),
            (20, Materials.Fulgurbloom),
        ],
    },
    "Gargoyle's Halberd": {
        "previous": "Glaive",
        "tier": 18,
        "somber": False,
        "id": 1815,
        "recipe": [
            (3, Materials.MetalPlate),
            (16, Materials.StoneFragment),
            (10, Materials.RootResin),
            (20, Materials.MeltedMushroom),
        ],
    },
    "Gargoyle's Black Halberd": {
        "previous": "Gargoyle's Halberd",
        "tier": 20,
        "somber": True,
        "id": 1816,
        "recipe": [
            (2, Materials.MetalPlate),
            (20, Materials.SomberStoneFragment),
            (5, Materials.ErdtreeAmber),
            (3, Materials.BlackMark),
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
            (2, Materials.MetalPlate),
            (5, Materials.RefinedWood),
            (16, Materials.StoneFragment),
            (15, Materials.Bloodrose),
        ],
    },
    "Grave Scythe": {
        "previous": "Scythe",
        "tier": 18,
        "somber": False,
        "id": 1901,
        "recipe": [
            (2, Materials.MetalPlate),
            (7, Materials.RefinedWood),
            (20, Materials.GraveViolet),
            (3, Materials.BlackMark),
        ],
    },
    "Halo Scythe": {
        "previous": "Scythe",
        "tier": 18,
        "somber": True,
        "id": 1902,
        "recipe": [
            (2, Materials.MetalPlate),
            (16, Materials.SomberStoneFragment),
            (6, Materials.ErdtreeWood),
            (3, Materials.ErdtreeAmber),
        ],
    },
    "Winged Scythe": {
        "previous": "Halo Scythe",
        "tier": 20,
        "somber": True,
        "id": 1906,
        "recipe": [
            (2, Materials.MetalPlate),
            (10, Materials.RefinedWood),
            (20, Materials.StormhawkFeather),
            (3, Materials.BlackMark),
        ],
    },
    # endregion

    # region Whips
    "Whip": {
        "visibility_flag": Flags.Note_Whip_Bought,
        "previous": None,
        "tier": 10,
        "somber": False,
        "id": 2000,
        "recipe": [
            (3, Materials.RefinedWood),
            (1, Materials.PliableMetal),
            (8, Materials.BeastBlood),
            (8, Materials.String),
        ],
        "cost": 20000,
    },
    "Thorned Whip": {
        "previous": "Whip",
        "tier": 13,
        "somber": False,
        "id": 2002,
        "recipe": [
            (3, Materials.RefinedWood),
            (15, Materials.Bloodrose),
            (8, Materials.SacramentalBud),
            (8, Materials.BeastBlood),
        ],
    },
    "Magma Whip Candlestick": {
        "previous": "Whip",
        "tier": 20,
        "somber": True,
        "id": 2003,
        "recipe": [
            (5, Materials.PliableMetal),
            (3, Materials.DragonTeeth),
            (15, Materials.VolcanicStone),
            (20, Materials.FireBlossom),
        ],
    },
    "Hoslow's Petal Whip": {
        "previous": "Urumi",
        "tier": 20,
        "somber": False,
        "id": 2005,
        "recipe": [
            (5, Materials.PliableMetal),
            (15, Materials.MetalShards),
            (8, Materials.String),
            (10, Materials.BloodTaintedExcrement),
        ],
    },
    "Giant's Red Braid": {
        "previous": "Whip",
        "tier": 20,
        "somber": True,
        "id": 2006,
        "recipe": [
            (1, Materials.Remembrance_FireGiant),
            (7, Materials.GruesomeBone),
            (15, Materials.SomberStoneFragment),
            (25, Materials.FireBlossom),
        ],
    },
    "Urumi": {
        "previous": "Thorned Whip",
        "tier": 17,
        "somber": False,
        "id": 2007,
        "recipe": [
            (2, Materials.MetalPlate),
            (10, Materials.MetalShards),
            (4, Materials.PliableMetal),
            (15, Materials.SilverTearHusk),
        ],
    },
    # endregion

    # region Fists
    "Caestus": {
        "visibility_flag": 0,
        "previous": None,
        "tier": 0,
        "somber": False,
        "id": 2100,
        "recipe": [
            (2, Materials.MetalShards),
            (2, Materials.LumpOfFlesh),
        ],
        "cost": 50,
    },
    "Spiked Caestus": {
        "previous": "Caestus",
        "tier": 3,
        "somber": False,
        "id": 2101,
        "recipe": [
            (4, Materials.MetalShards),
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
            (5, Materials.DragonTeeth),
            (6, Materials.GruesomeBone),
            (15, Materials.SomberStoneFragment),
        ],
    },
    "Iron Ball": {
        "previous": "Katar",
        "tier": 9,
        "somber": False,
        "id": 2107,
        "recipe": [
            (2, Materials.MetalPlate),
            (2, Materials.MeteoriteChunk),
        ],
    },
    "Star Fist": {
        "previous": "Iron Ball",
        "tier": 12,
        "somber": False,
        "id": 2108,
        "recipe": [
            (15, Materials.MetalShards),
            (8, Materials.StoneFragment),
            (10, Materials.Bloodrose),
        ],
    },
    "Katar": {
        "previous": "Spiked Caestus",
        "tier": 6,
        "somber": False,
        "id": 2110,
        "recipe": [
            (2, Materials.MetalPlate),
            (6, Materials.StoneFragment),
            (6, Materials.TarnishedGoldenSunflower),
        ],
    },
    "Clinging Bone": {
        "previous": "Raptor Talons",
        "tier": 20,
        "somber": True,
        "id": 2111,
        "recipe": [
            (4, Materials.GruesomeBone),
            (20, Materials.HumanBoneShard),
            (15, Materials.SomberStoneFragment),
            (15, Materials.YellowEmber),
        ],
    },
    "Veteran's Prosthesis": {
        "previous": "Star Fist",
        "tier": 16,
        "somber": True,
        "id": 2112,
        "recipe": [
            (2, Materials.MetalPlate),
            (16, Materials.SomberStoneFragment),
            (12, Materials.StormhawkFeather),
            (18, Materials.Fulgurbloom),
        ],
    },
    "Cipher Pata": {
        "previous": "Raptor Talons",
        "tier": 20,
        "somber": True,
        "id": 2113,
        "recipe": [
            (8, Materials.ErdtreeAmber),
            (20, Materials.GoldTingedExcrement),
            (20, Materials.GoldenSunflower),
            (20, Materials.GoldFirefly),
        ],
    },
    "Hookclaws": {
        "previous": "Katar",
        "tier": 9,
        "somber": False,
        "id": 2200,
        "recipe": [
            (2, Materials.MetalPlate),
            (9, Materials.StoneFragment),
            (9, Materials.SilverFirefly),
            (5, Materials.ArteriaLeaf),
        ],
    },
    "Venomous Fang": {
        "previous": "Hookclaws",
        "tier": 12,
        "somber": False,
        "id": 2201,
        "recipe": [
            (2, Materials.MetalPlate),
            (12, Materials.Poisonbloom),
            (10, Materials.MirandaPowder),
            (10, Materials.ToxicMushroom),
        ],
    },
    "Bloodhound Claws": {
        "previous": "Venomous Fang",
        "tier": 15,
        "somber": False,
        "id": 2202,
        "recipe": [
            (3, Materials.MetalPlate),
            (15, Materials.StoneFragment),
            (10, Materials.BeastBlood),
            (5, Materials.BloodTaintedExcrement),
        ],
    },
    "Raptor Talons": {
        "previous": "Bloodhound Claws",
        "tier": 18,
        "somber": False,
        "id": 2203,
        "recipe": [
            (2, Materials.MetalPlate),
            (4, Materials.PliableMetal),
            (12, Materials.StormhawkFeather),
            (12, Materials.FourToedFowlFoot),
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
            (5, Materials.MetalPlate),
            (15, Materials.MetalShards),
            (20, Materials.FireBlossom),
            (20, Materials.EyeOfYelough),
        ],
    },
    "Watchdog's Staff": {
        "previous": "Celebrant's Skull",
        "tier": 16,
        "somber": True,
        "id": 2301,
        "recipe": [
            (15, Materials.StoneFragment),
            (15, Materials.SomberStoneFragment),
            (15, Materials.GraveViolet),
            (8, Materials.GlintstoneDust),
        ],
    },
    "Great Club": {
        "previous": "Brick Hammer",
        "tier": 18,
        "somber": False,
        "id": 2302,
        "recipe": [
            (10, Materials.SoftWood),
            (10, Materials.RefinedWood),
            (8, Materials.ErdtreeWood),
            (2, Materials.ErdtreeAmber),
        ],
    },
    "Envoy's Greathorn": {
        "previous": "Envoy's Long Horn",
        "tier": 20,
        "somber": True,
        "id": 2303,
        "recipe": [
            (5, Materials.MetalPlate),
            (5, Materials.PliableMetal),
            (5, Materials.ErdtreeAmber),
            (20, Materials.GoldenCentipede),
        ],
    },
    "Duelist Greataxe": {
        "previous": "Greataxe",
        "tier": 17,
        "somber": False,
        "id": 2304,
        "recipe": [
            (4, Materials.MetalPlate),
            (12, Materials.MetalShards),
            (12, Materials.StoneFragment),
            (12, Materials.AltusBloom),
        ],
    },
    "Axe of Godfrey": {
        "previous": "Axe of Godrick",
        "tier": 20,
        "somber": True,
        "id": 2305,
        "recipe": [
            (1, Materials.Remembrance_HoarahLoux),
            (5, Materials.MetalPlate),
            (10, Materials.ErdtreeWood),
            (40, Materials.TarnishedGoldenSunflower),
        ],
    },
    "Dragon Greatclaw": {
        "previous": "Duelist Greataxe",
        "tier": 20,
        "somber": True,
        "id": 2306,
        "recipe": [
            (5, Materials.DragonTeeth),
            (5, Materials.GruesomeBone),
            (20, Materials.SomberStoneFragment),
            (20, Materials.Fulgurbloom),
        ],
    },
    "Staff of the Avatar": {
        "previous": "Watchdog's Staff",
        "tier": 20,
        "somber": True,
        "id": 2307,
        "recipe": [
            (4, Materials.MetalPlate),
            (8, Materials.ErdtreeWood),
            (5, Materials.ErdtreeAmber),
            (30, Materials.GoldenSunflower),
        ],
    },
    "Fallingstar Beast Jaw": {
        "previous": "Lance",
        "tier": 20,
        "somber": True,
        "id": 2308,
        "recipe": [
            (8, Materials.MeteoriteChunk),
            (4, Materials.GruesomeBone),
            (15, Materials.SomberStoneFragment),
            (15, Materials.FormicRock),
        ],
    },
    "Ghiza's Wheel": {
        "previous": "Grave Scythe",
        "tier": 20,
        "somber": True,
        "id": 2310,
        "recipe": [
            (4, Materials.MetalPlate),
            (7, Materials.PliableMetal),
            (20, Materials.MetalShards),
            (30, Materials.Bloodrose),
        ],
    },
    "Giant-Crusher": {
        "previous": "Great Club",
        "tier": 20,
        "somber": False,
        "id": 2311,
        "recipe": [
            (40, Materials.StoneFragment),
            (20, Materials.SomberStoneFragment),
            (15, Materials.FireBlossom),
        ],
    },
    "Golem's Halberd": {
        "previous": "Golden Halberd",
        "tier": 20,
        "somber": False,
        "id": 2312,
        "recipe": [
            (25, Materials.StoneFragment),
            (15, Materials.SomberStoneFragment),
            (5, Materials.MeteoriteChunk),
            (1, Materials.BlackMark),
        ],
    },
    "Troll's Hammer": {
        "previous": "Greathorn Hammer",
        "tier": 20,
        "somber": False,
        "id": 2313,
        "recipe": [
            (30, Materials.StoneFragment),
            (5, Materials.ErdtreeWood),
            (3, Materials.ErdtreeAmber),
            (15, Materials.FireBlossom),
        ],
    },
    "Rotten Staff": {
        "previous": "Watchdog's Staff",
        "tier": 20,
        "somber": True,
        "id": 2314,
        "recipe": [
            (4, Materials.MetalPlate),
            (8, Materials.ErdtreeWood),
            (5, Materials.ErdtreeAmber),
            (20, Materials.AeonianButterfly),
        ],
    },
    "Rotten Greataxe": {
        "previous": "Duelist Greataxe",
        "tier": 20,
        "somber": False,
        "id": 2315,
        "recipe": [
            (4, Materials.MetalPlate),
            (15, Materials.StoneFragment),
            (15, Materials.AeonianButterfly),
            (15, Materials.ToxicMushroom),
        ],
    },
    # endregion

    # region Torches
    "Torch": {
        "visibility_flag": 0,
        "id": 2400,
        "recipe": [
            (1, Materials.SoftWood),
            (1, Materials.RootResin),
            (2, Materials.SmolderingButterfly),
        ],
        "cost": 50,
    },
    "Steel-Wire Torch": {
        "visibility_flag": Flags.Recipe_SteelWireTorch_Bought,
        "id": 2402,
        "recipe": [
            (1, Materials.RefinedWood),
            (2, Materials.String),
            (1, Materials.MetalShards),
            (5, Materials.SmolderingButterfly),
        ],
        "cost": 1000,
    },
    "St. Trina's Torch": {
        "visibility_flag": Flags.Recipe_StTrinasTorch_Bought,
        "id": 2404,
        "recipe": [
            (1, Materials.MetalPlate),
            (1, Materials.ErdtreeWood),
            (10, Materials.TrinasLily),
            (5, Materials.NascentButterfly),
        ],
        "cost": 5000,
    },
    "Ghostflame Torch": {
        "visibility_flag": Flags.Recipe_GhostflameTorch_Bought,
        "id": 2405,
        "recipe": [
            (1, Materials.MetalPlate),
            (10, Materials.HumanBoneShard),
            (10, Materials.SilverTearHusk),
            (5, Materials.NascentButterfly),
        ],
        "cost": 3000,
    },
    "Beast-Repellent Torch": {
        "visibility_flag": Flags.Recipe_BeastRepellentTorch_Bought,
        "id": 2406,
        "recipe": [
            (2, Materials.RefinedWood),
            (2, Materials.MirandaPowder),
            (10, Materials.DewkissedHerba),
            (10, Materials.SmolderingButterfly),
        ],
        "cost": 4000,
    },
    "Sentry's Torch": {
        "visibility_flag": Flags.Recipe_SentrysTorch_Bought,
        "id": 2407,
        "recipe": [
            (1, Materials.ErdtreeWood),
            (1, Materials.ErdtreeAmber),
            (1, Materials.BlackMark),
            (15, Materials.SmolderingButterfly),
        ],
        "cost": 5000,
    },
    # endregion

    # NOTE: Beastman's Jar-Shield (a Medium Shield) is in here.
    # NOTE: Shield of the Guilty (a Small Shield) is missing here, and instead appears in Medium Shields below.
    # region Small Shields
    "Buckler": {
        "visibility_flag": Flags.Recipes_MetalSmallShields_Bought,
        "cost": 4000,
        "id": 3000,
        "recipe": [
            (1, Materials.ShieldGrip),
            (2, Materials.PliableMetal),
            (10, Materials.SilverFirefly),
        ],
    },
    "Perfumer's Shield": {
        "visibility_flag": Flags.Recipes_RareSmallShields_Bought,
        "cost": 8000,
        "id": 3001,
        "recipe": [
            (1, Materials.ShieldGrip),
            (1, Materials.MetalPlate),
            (1, Materials.ErdtreeAmber),
            (15, Materials.GoldenSunflower),
        ],
    },
    "Man-Serpent's Shield": {
        "visibility_flag": Flags.Recipes_MetalSmallShields_Bought,
        "cost": 4000,
        "id": 3002,
        "recipe": [
            (1, Materials.ShieldGrip),
            (1, Materials.MetalPlate),
            (12, Materials.VolcanicStone),
        ],
    },
    "Rickety Shield": {
        "visibility_flag": 0,  # always craftable
        "cost": 50,
        "id": 3003,
        "recipe": [
            (1, Materials.ShieldGrip),
            (1, Materials.SoftWood),
        ],
    },
    "Pillory Shield": {
        "visibility_flag": Flags.Recipes_WoodenSmallShields_Bought,
        "cost": 1000,
        "id": 3004,
        "recipe": [
            (1, Materials.ShieldGrip),
            (3, Materials.SoftWood),
            (3, Materials.MetalShards),
        ],
    },
    "Beastman's Jar-Shield": {  # NOTE: this is the one Medium Shield buried among otherwise contiguous Small Shields
        "visibility_flag": Flags.Recipes_RareMediumShields_Bought,
        "cost": 10000,
        "id": 3006,
        "recipe": [
            (2, Materials.ShieldGrip),
            (10, Materials.LivingJarShard),
            (5, Materials.HeftyBeastBone),
        ],
    },
    "Red Thorn Roundshield": {
        "visibility_flag": Flags.Recipes_WoodenSmallShields_Bought,
        "cost": 1000,
        "id": 3007,
        "recipe": [
            (1, Materials.ShieldGrip),
            (2, Materials.SoftWood),
            (2, Materials.RootResin),
        ],
    },
    "Scripture Wooden Shield": {
        "visibility_flag": Flags.Recipes_WoodenSmallShields_Bought,
        "cost": 1000,
        "id": 3008,
        "recipe": [
            (1, Materials.ShieldGrip),
            (2, Materials.SoftWood),
            (12, Materials.ErdleafFlower),
        ],
    },
    "Riveted Wooden Shield": {
        "visibility_flag": Flags.Recipes_WoodenSmallShields_Bought,
        "cost": 1000,
        "id": 3009,
        "recipe": [
            (1, Materials.ShieldGrip),
            (2, Materials.SoftWood),
            (4, Materials.MetalShards),
        ],
    },
    "Blue-White Wooden Shield": {
        "visibility_flag": Flags.Recipes_WoodenSmallShields_Bought,
        "cost": 1000,
        "id": 3010,
        "recipe": [
            (1, Materials.ShieldGrip),
            (2, Materials.SoftWood),
            (4, Materials.MetalShards),
            (4, Materials.AlbinauricBloodclot),
        ],
    },
    "Rift Shield": {
        "visibility_flag": Flags.Recipes_MetalSmallShields_Bought,
        "cost": 4000,
        "id": 3011,
        "recipe": [
            (1, Materials.ShieldGrip),
            (1, Materials.MetalPlate),
            (3, Materials.MetalShards),
            (5, Materials.StoneFragment),
        ],
    },
    "Iron Roundshield": {
        "visibility_flag": Flags.Recipes_MetalSmallShields_Bought,
        "cost": 4000,
        "id": 3012,
        "recipe": [
            (1, Materials.ShieldGrip),
            (1, Materials.MetalPlate),
            (2, Materials.StoneFragment),
            (5, Materials.SilverFirefly),
        ],
    },
    "Gilded Iron Shield": {
        "visibility_flag": Flags.Recipes_MetalSmallShields_Bought,
        "cost": 4000,
        "id": 3013,
        "recipe": [
            (1, Materials.ShieldGrip),
            (1, Materials.MetalPlate),
            (10, Materials.TarnishedGoldenSunflower),
        ],
    },
    "Ice Crest Shield": {
        "visibility_flag": Flags.Recipes_MetalSmallShields_Bought,
        "cost": 4000,
        "id": 3014,
        "recipe": [
            (1, Materials.ShieldGrip),
            (1, Materials.MetalPlate),
            (1, Materials.GlintstoneDust),
            (10, Materials.SilverFirefly),
        ],
    },
    "Smoldering Shield": {
        "visibility_flag": Flags.Recipes_RareSmallShields_Bought,
        "cost": 8000,
        "id": 3015,
        "recipe": [
            (1, Materials.ShieldGrip),
            (8, Materials.StoneFragment),
            (12, Materials.VolcanicStone),
        ],
    },
    "Spiralhorn Shield": {
        "visibility_flag": Flags.Recipes_RareSmallShields_Bought,
        "cost": 8000,
        "id": 3019,
        "recipe": [
            (1, Materials.ShieldGrip),
            (8, Materials.BuddingHorn),
            (15, Materials.DewkissedHerba),
        ],
    },
    "Coil Shield": {
        "visibility_flag": Flags.Recipes_RareSmallShields_Bought,
        "cost": 8000,
        "id": 3020,
        "recipe": [
            (1, Materials.ShieldGrip),
            (1, Materials.MetalPlate),
            (5, Materials.Poisonbloom),
            (5, Materials.MirandaPowder),
        ],
    },
    # endregion

    # NOTE: Shield of the Guilty (a Small Shield) is in here.
    # NOTE: Beastman's Jar-Shield (a Medium Shield) is missing here, and instead appears in Small Shields above.
    # region Medium Shields
    "Kite Shield": {
        "visibility_flag": Flags.Recipes_KiteMediumShields_Bought,
        "cost": 6000,
        "id": 3100,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.MetalPlate),
        ],
    },
    "Marred Leather Shield": {
        "visibility_flag": Flags.Recipes_CommonMediumShields_Bought,
        "cost": 1000,
        "id": 3101,
        "recipe": [
            (2, Materials.ShieldGrip),
            (1, Materials.LumpOfFlesh),
            (7, Materials.TarnishedGoldenSunflower),
        ],
    },
    "Marred Wooden Shield": {
        "visibility_flag": Flags.Recipes_WoodenMediumShields_Bought,
        "cost": 2000,
        "id": 3102,
        "recipe": [
            (2, Materials.ShieldGrip),
            (3, Materials.SoftWood),
            (7, Materials.TarnishedGoldenSunflower),
        ],
    },
    "Banished Knight's Shield": {
        "visibility_flag": Flags.Recipes_RareMediumShields_Bought,
        "cost": 10000,
        "id": 3103,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.MetalPlate),
            (12, Materials.AltusBloom),
        ],
    },
    "Albinauric Shield": {
        "visibility_flag": Flags.Recipes_RareMediumShields_Bought,
        "cost": 10000,
        "id": 3104,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.MetalPlate),
            (2, Materials.GlintstoneDust),
            (5, Materials.AlbinauricBloodclot),
        ],
    },
    "Sun Realm Shield": {
        "visibility_flag": Flags.Recipes_CommonMediumShields_Bought,
        "cost": 1000,
        "id": 3105,
        "recipe": [
            (2, Materials.ShieldGrip),
            (1, Materials.MetalPlate),
            (4, Materials.HumanBoneShard),
        ],
    },
    "Silver Mirrorshield": {
        "visibility_flag": Flags.Recipes_RareMediumShields_Bought,
        "cost": 10000,
        "id": 3106,
        "recipe": [
            (2, Materials.ShieldGrip),
            (3, Materials.PliableMetal),
            (10, Materials.SilverTearHusk),
            (5, Materials.AlbinauricBloodclot),
        ],
    },
    "Round Shield": {
        "visibility_flag": Flags.Recipes_CommonMediumShields_Bought,
        "cost": 1000,
        "id": 3107,
        "recipe": [
            (2, Materials.ShieldGrip),
            (5, Materials.SoftWood),
            (1, Materials.RefinedWood),
            (5, Materials.MetalShards),
        ],
    },
    "Scorpion Kite Shield": {
        "visibility_flag": Flags.Recipes_KiteMediumShields_Bought,
        "cost": 6000,
        "id": 3108,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.MetalPlate),
            (5, Materials.YellowEmber),
        ],
    },
    "Twinbird Kite Shield": {
        "visibility_flag": Flags.Recipes_KiteMediumShields_Bought,
        "cost": 6000,
        "id": 3109,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.MetalPlate),
            (7, Materials.StormhawkFeather),
            (1, Materials.BlackMark),
        ],
    },
    "Blue-Gold Kite Shield": {
        "visibility_flag": Flags.Recipes_KiteMediumShields_Bought,
        "cost": 6000,
        "id": 3110,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.MetalPlate),
            (10, Materials.AltusBloom),
            (10, Materials.CrystalBud),
        ],
    },
    "Brass Shield": {
        "visibility_flag": Flags.Recipes_RareMediumShields_Bought,
        "cost": 10000,
        "id": 3113,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.MetalPlate),
            (7, Materials.MetalShards),
            (10, Materials.GoldenSunflower),
        ],
    },
    "Great Turtle Shell": {
        "visibility_flag": Flags.Recipes_RareMediumShields_Bought,
        "cost": 10000,
        "id": 3114,
        "recipe": [
            (2, Materials.ShieldGrip),
            (8, Materials.TurtleNeckMeat),
            (4, Materials.CaveMoss),
            (4, Materials.HeftyBeastBone),
        ],
    },
    "Shield of the Guilty": {  # SMALL SHIELD
        "visibility_flag": Flags.Recipes_RareSmallShields_Bought,
        "cost": 8000,
        "id": 3117,
        "recipe": [
            (1, Materials.ShieldGrip),
            (1, Materials.PliableMetal),
            (10, Materials.EyeOfYelough),
            (10, Materials.MetalShards),
        ],
    },
    "Carian Knight's Shield": {
        "visibility_flag": Flags.Recipes_RareMediumShields_Bought,
        "cost": 10000,
        "id": 3119,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.MetalPlate),
            (5, Materials.GlintstoneDust),
            (10, Materials.CrystalBud),
        ],
    },
    "Large Leather Shield": {
        "visibility_flag": Flags.Recipes_CommonMediumShields_Bought,
        "cost": 1000,
        "id": 3123,
        "recipe": [
            (2, Materials.ShieldGrip),
            (3, Materials.RefinedWood),
            (3, Materials.LumpOfFlesh),
            (4, Materials.String),
        ],
    },
    "Horse Crest Wooden Shield": {
        "visibility_flag": Flags.Recipes_WoodenMediumShields_Bought,
        "cost": 2000,
        "id": 3124,
        "recipe": [
            (2, Materials.ShieldGrip),
            (3, Materials.RefinedWood),
            (10, Materials.RowaFruit),
        ],
    },
    "Candletree Wooden Shield": {
        "visibility_flag": Flags.Recipes_WoodenMediumShields_Bought,
        "cost": 2000,
        "id": 3125,
        "recipe": [
            (2, Materials.ShieldGrip),
            (3, Materials.RefinedWood),
            (5, Materials.RimedCrystalBud),
        ],
    },
    "Flame Crest Wooden Shield": {
        "visibility_flag": Flags.Recipes_WoodenMediumShields_Bought,
        "cost": 2000,
        "id": 3126,
        "recipe": [
            (2, Materials.ShieldGrip),
            (3, Materials.RefinedWood),
            (4, Materials.MetalShards),
            (8, Materials.YellowEmber),
        ],
    },
    "Hawk Crest Wooden Shield": {
        "visibility_flag": Flags.Recipes_WoodenMediumShields_Bought,
        "cost": 2000,
        "id": 3127,
        "recipe": [
            (2, Materials.ShieldGrip),
            (3, Materials.RefinedWood),
            (5, Materials.StormhawkFeather),
        ],
    },
    "Beast Crest Heater Shield": {
        "visibility_flag": Flags.Recipes_HeaterMediumShields_Bought,
        "cost": 5000,
        "id": 3128,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.MetalPlate),
            (3, Materials.BeastBlood),
        ],
    },
    "Red Crest Heater Shield": {
        "visibility_flag": Flags.Recipes_HeaterMediumShields_Bought,
        "cost": 5000,
        "id": 3129,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.MetalPlate),
            (3, Materials.BeastBlood),
        ],
    },
    "Blue Crest Heater Shield": {
        "visibility_flag": Flags.Recipes_HeaterMediumShields_Bought,
        "cost": 5000,
        "id": 3130,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.MetalPlate),
            (4, Materials.MetalShards),
            (4, Materials.SilverFirefly),
        ],
    },
    "Eclipse Crest Heater Shield": {
        "visibility_flag": Flags.Recipes_HeaterMediumShields_Bought,
        "cost": 5000,
        "id": 3131,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.MetalPlate),
            (5, Materials.SilverFirefly),
        ],
    },
    "Inverted Hawk Heater Shield": {
        "visibility_flag": Flags.Recipes_HeaterMediumShields_Bought,
        "cost": 5000,
        "id": 3132,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.MetalPlate),
            (7, Materials.FlightPinion),
        ],
    },
    "Heater Shield": {
        "visibility_flag": Flags.Recipes_HeaterMediumShields_Bought,
        "cost": 5000,
        "id": 3133,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.MetalPlate),
            (4, Materials.MetalShards),
        ],
    },
    "Black Leather Shield": {
        "visibility_flag": Flags.Recipes_CommonMediumShields_Bought,
        "cost": 1000,
        "id": 3134,
        "recipe": [
            (2, Materials.ShieldGrip),
            (2, Materials.RefinedWood),
            (5, Materials.RimedRowa),
            (5, Materials.BuddingCaveMoss),
        ],
    },
    # endregion

    # region Greatshields
    "Dragon Towershield": {
        "visibility_flag": Flags.Recipes_RareGreatshields_Bought,
        "cost": 15000,
        "id": 3200,
        "recipe": [
            (3, Materials.ShieldGrip),
            (4, Materials.MetalPlate),
            (8, Materials.GravelStone),
            (3, Materials.DragonTeeth),
        ],
    },
    "Distinguished Greatshield": {
        "visibility_flag": Flags.Recipes_CommonGreatshields_Bought,
        "cost": 5000,
        "id": 3202,
        "recipe": [
            (3, Materials.ShieldGrip),
            (3, Materials.MetalPlate),
            (3, Materials.RefinedWood),
            (12, Materials.TarnishedGoldenSunflower),
        ],
    },
    "Crucible Hornshield": {
        "visibility_flag": Flags.Recipes_UncommonGreatshields_Bought,
        "cost": 10000,
        "id": 3203,
        "recipe": [
            (3, Materials.ShieldGrip),
            (12, Materials.BuddingHorn),
            (8, Materials.SomberStoneFragment),
            (2, Materials.ErdtreeAmber),
        ],
    },
    "Dragonclaw Shield": {
        "visibility_flag": Flags.Recipes_RareGreatshields_Bought,
        "cost": 15000,
        "id": 3204,
        "recipe": [
            (3, Materials.ShieldGrip),
            (5, Materials.DragonTeeth),
            (10, Materials.GravelStone),
            (14, Materials.Fulgurbloom),
        ],
    },
    "Briar Greatshield": {
        "visibility_flag": Flags.Recipes_UncommonGreatshields_Bought,
        "cost": 10000,
        "id": 3205,
        "recipe": [
            (3, Materials.ShieldGrip),
            (3, Materials.MetalPlate),
            (15, Materials.MetalShards),
            (15, Materials.Bloodrose),
        ],
    },
    "Erdtree Greatshield": {
        "visibility_flag": Flags.Recipes_RareGreatshields_Bought,
        "cost": 15000,
        "id": 3208,
        "recipe": [
            (3, Materials.ShieldGrip),
            (3, Materials.MetalPlate),
            (3, Materials.ErdtreeAmber),
            (25, Materials.GoldenSunflower),
        ],
    },
    "Golden Beast Crest Shield": {
        "visibility_flag": Flags.Recipes_UncommonGreatshields_Bought,
        "cost": 10000,
        "id": 3209,
        "recipe": [
            (3, Materials.ShieldGrip),
            (3, Materials.MetalPlate),
            (13, Materials.TarnishedGoldenSunflower),
            (20, Materials.ErdleafFlower),
        ],
    },
    "Jellyfish Shield": {
        "visibility_flag": Flags.Recipes_RareGreatshields_Bought,
        "cost": 15000,
        "id": 3212,
        "recipe": [
            (3, Materials.ShieldGrip),
            (15, Materials.NascentButterfly),
            (5, Materials.GlintstoneDust),
            (10, Materials.AlbinauricBloodclot),
        ],
    },
    "Fingerprint Stone Shield": {
        "visibility_flag": Flags.Recipes_RareGreatshields_Bought,
        "cost": 15000,
        "id": 3213,
        "recipe": [
            (3, Materials.ShieldGrip),
            (25, Materials.SomberStoneFragment),
            (10, Materials.YellowEmber),
            (25, Materials.StoneFragment),
        ],
    },
    "Icon Shield": {
        "visibility_flag": Flags.Recipes_UncommonGreatshields_Bought,
        "cost": 10000,
        "id": 3214,
        "recipe": [
            (3, Materials.ShieldGrip),
            (2, Materials.MetalShards),
            (8, Materials.RefinedWood),
            (15, Materials.AltusBloom)
        ],
    },
    "One-Eyed Shield": {
        "visibility_flag": Flags.Recipes_VeryRareGreatshields_Bought,
        "cost": 20000,
        "id": 3215,
        "recipe": [
            (3, Materials.ShieldGrip),
            (2, Materials.MetalPlate),
            (25, Materials.SomberStoneFragment),
            (25, Materials.FireBlossom),
        ],
    },
    "Visage Shield": {
        "visibility_flag": Flags.Recipes_RareGreatshields_Bought,
        "cost": 15000,
        "id": 3216,
        "recipe": [
            (3, Materials.ShieldGrip),
            (5, Materials.MetalPlate),
            (20, Materials.VolcanicStone),
            (20, Materials.FireBlossom),
        ],
    },
    "Spiked Palisade Shield": {
        "visibility_flag": Flags.Recipes_UncommonGreatshields_Bought,
        "cost": 10000,
        "id": 3217,
        "recipe": [
            (3, Materials.ShieldGrip),
            (2, Materials.MetalPlate),
            (5, Materials.RefinedWood),
            (15, Materials.MetalShards),
        ],
    },
    "Manor Towershield": {
        "visibility_flag": Flags.Recipes_CommonGreatshields_Bought,
        "cost": 5000,
        "id": 3219,
        "recipe": [
            (3, Materials.ShieldGrip),
            (4, Materials.MetalPlate),
            (15, Materials.TarnishedGoldenSunflower),
            (12, Materials.StoneFragment),
        ],
    },
    "Crossed-Tree Towershield": {
        "visibility_flag": Flags.Recipes_UncommonGreatshields_Bought,
        "cost": 10000,
        "id": 3220,
        "recipe": [
            (3, Materials.ShieldGrip),
            (3, Materials.MetalPlate),
            (12, Materials.StoneFragment),
            (1, Materials.ErdtreeAmber),
        ],
    },
    "Inverted Hawk Towershield": {
        "visibility_flag": Flags.Recipes_UncommonGreatshields_Bought,
        "cost": 10000,
        "id": 3221,
        "recipe": [
            (3, Materials.ShieldGrip),
            (3, Materials.MetalPlate),
            (10, Materials.MetalShards),
            (8, Materials.StormhawkFeather),
        ],
    },
    "Ant's Skull Plate": {
        "visibility_flag": Flags.Recipes_RareGreatshields_Bought,
        "cost": 15000,
        "id": 3222,
        "recipe": [
            (3, Materials.ShieldGrip),
            (4, Materials.GruesomeBone),
            (8, Materials.BuddingHorn),
            (10, Materials.MirandaPowder),
        ],
    },
    "Redmane Greatshield": {
        "visibility_flag": Flags.Recipes_UncommonGreatshields_Bought,
        "cost": 10000,
        "id": 3223,
        "recipe": [
            (3, Materials.ShieldGrip),
            (3, Materials.MetalPlate),
            (10, Materials.VolcanicStone),
            (15, Materials.FadedErdleafFlower),
        ],
    },
    "Eclipse Crest Greatshield": {
        "visibility_flag": Flags.Recipes_RareGreatshields_Bought,
        "cost": 15000,
        "id": 3224,
        "recipe": [
            (3, Materials.ShieldGrip),
            (3, Materials.MetalPlate),
            (2, Materials.MeteoriteChunk),
            (1, Materials.BlackMark),
        ],
    },
    "Cuckoo Greatshield": {
        "visibility_flag": Flags.Recipes_UncommonGreatshields_Bought,
        "cost": 10000,
        "id": 3225,
        "recipe": [
            (3, Materials.ShieldGrip),
            (3, Materials.MetalPlate),
            (5, Materials.GlintstoneDust),
            (10, Materials.CrystalBud),
        ],
    },
    "Golden Greatshield": {
        "visibility_flag": Flags.Recipes_UncommonGreatshields_Bought,
        "cost": 10000,
        "id": 3226,
        "recipe": [
            (3, Materials.ShieldGrip),
            (3, Materials.MetalPlate),
            (20, Materials.GoldenSunflower),
            (8, Materials.GoldenCentipede),
        ],
    },
    "Gilded Greatshield": {
        "visibility_flag": Flags.Recipes_CommonGreatshields_Bought,
        "cost": 5000,
        "id": 3227,
        "recipe": [
            (3, Materials.ShieldGrip),
            (3, Materials.MetalPlate),
            (20, Materials.RowaFruit),
            (15, Materials.TarnishedGoldenSunflower),
        ],
    },
    "Haligtree Crest Greatshield": {
        "visibility_flag": Flags.Recipes_VeryRareGreatshields_Bought,
        "cost": 20000,
        "id": 3228,
        "recipe": [
            (3, Materials.ShieldGrip),
            (3, Materials.MetalPlate),
            (20, Materials.GoldFirefly),
            (15, Materials.MiquellasLily),
        ],
    },
    "Wooden Greatshield": {
        "visibility_flag": Flags.Recipes_CommonGreatshields_Bought,
        "cost": 5000,
        "id": 3229,
        "recipe": [
            (3, Materials.ShieldGrip),
            (7, Materials.SoftWood),
            (2, Materials.RefinedWood),
            (8, Materials.MetalShards),
        ],
    },
    "Lordsworn's Shield": {
        "visibility_flag": Flags.Recipes_CommonGreatshields_Bought,
        "cost": 5000,
        "id": 3230,
        "recipe": [
            (3, Materials.ShieldGrip),
            (2, Materials.MetalPlate),
            (7, Materials.StoneFragment),
            (3, Materials.MetalShards),
        ],
    },
    # endregion

    # region Staffs
    "Glintstone Staff": {
        "visibility_flag": 0,  # always craftable
        "cost": 200,
        "id": 3300,
        "recipe": [
            (1, Materials.StaffPole),
            (2, Materials.CrystalBud),
        ],
    },
    "Crystal Staff": {
        "visibility_flag": Flags.Recipes_RareStaffs_Bought,
        "cost": 15000,
        "id": 3304,
        "recipe": [
            (1, Materials.StaffPole),
            (5, Materials.SomberStoneFragment),
            (3, Materials.GlintstoneDust),
            (5, Materials.CrackedCrystal),
        ],
    },
    "Gelmir Glintstone Staff": {
        "visibility_flag": Flags.Recipes_UncommonStaffs_Bought,
        "cost": 10000,
        "id": 3305,
        "recipe": [
            (1, Materials.StaffPole),
            (15, Materials.VolcanicStone),
            (7, Materials.SomberStoneFragment),
            (3, Materials.GlintstoneDust),
        ],
    },
    "Demi-Human Queen's Staff": {
        "visibility_flag": Flags.Recipes_CommonStaffs_Bought,
        "cost": 5000,
        "id": 3306,
        "recipe": [
            (1, Materials.StaffPole),
            (2, Materials.SoftWood),
            (1, Materials.CrystalBud),
        ],
    },
    "Carian Regal Scepter": {
        "visibility_flag": Flags.Recipes_VeryRareStaffs_Bought,
        "cost": 20000,
        "id": 3309,
        "recipe": [
            (1, Materials.Remembrance_Rennala),
            (20, Materials.RimedCrystalBud),
            (8, Materials.GlintstoneDust),
            (2, Materials.MeteoriteChunk),
        ],
    },
    "Digger's Staff": {
        "visibility_flag": Flags.Recipes_UncommonStaffs_Bought,
        "cost": 10000,
        "id": 3312,
        "recipe": [
            (1, Materials.StaffPole),
            (2, Materials.RefinedWood),
            (3, Materials.CrackedCrystal),
            (2, Materials.GlintstoneDust),
        ],
    },
    "Astrologer's Staff": {
        "visibility_flag": Flags.Recipes_CommonStaffs_Bought,
        "cost": 5000,
        "id": 3313,
        "recipe": [
            (1, Materials.StaffPole),
            (2, Materials.SoftWood),
            (2, Materials.CrackedCrystal)
        ],
    },
    "Carian Glintblade Staff": {
        "visibility_flag": Flags.Recipes_UncommonStaffs_Bought,
        "cost": 10000,
        "id": 3317,
        "recipe": [
            (1, Materials.StaffPole),
            (3, Materials.GlintstoneDust),
            (7, Materials.CrystalBud),
            (7, Materials.GlintstoneFirefly)
        ],
    },
    "Prince of Death's Staff": {
        "visibility_flag": Flags.Recipes_RareStaffs_Bought,
        "cost": 15000,
        "id": 3318,
        "recipe": [
            (1, Materials.StaffPole),
            (2, Materials.ErdtreeAmber),
            (6, Materials.GlintstoneDust),
            (2, Materials.BlackMark),
        ],
    },
    "Albinauric Staff": {
        "visibility_flag": Flags.Recipes_RareStaffs_Bought,
        "cost": 15000,
        "id": 3319,
        "recipe": [
            (1, Materials.StaffPole),
            (5, Materials.SilverTearHusk),
            (3, Materials.GlintstoneDust),
            (5, Materials.AlbinauricBloodclot),
        ],
    },
    "Academy Glintstone Staff": {
        "visibility_flag": Flags.Recipes_UncommonStaffs_Bought,
        "cost": 10000,
        "id": 3320,
        "recipe": [
            (1, Materials.StaffPole),
            (2, Materials.RefinedWood),
            (2, Materials.GlintstoneDust),
            (10, Materials.GlintstoneFirefly),
        ],
    },
    "Carian Glintstone Staff": {
        "visibility_flag": Flags.Recipes_UncommonStaffs_Bought,
        "cost": 10000,
        "id": 3321,
        "recipe": [
            (1, Materials.StaffPole),
            (3, Materials.GlintstoneDust),
            (7, Materials.CrystalBud),
            (7, Materials.GlintstoneFirefly)
        ],
    },
    "Azur's Glintstone Staff": {
        "visibility_flag": Flags.Recipes_VeryRareStaffs_Bought,
        "cost": 20000,
        "id": 3323,
        "recipe": [
            (1, Materials.StaffPole),
            (25, Materials.GlintstoneFirefly),
            (8, Materials.GlintstoneDust),
            (3, Materials.MeteoriteChunk),
        ],
    },
    "Lusat's Glintstone Staff": {
        "visibility_flag": Flags.Recipes_VeryRareStaffs_Bought,
        "cost": 20000,
        "id": 3324,
        "recipe": [
            (1, Materials.StaffPole),
            (25, Materials.SilverFirefly),
            (8, Materials.GlintstoneDust),
            (3, Materials.MeteoriteChunk),
        ],
    },
    "Meteorite Staff": {
        "visibility_flag": Flags.Recipes_RareStaffs_Bought,
        "cost": 15000,
        "id": 3325,
        "recipe": [
            (1, Materials.StaffPole),
            (3, Materials.RefinedWood),
            (3, Materials.MeteoriteChunk),
        ],
    },
    "Staff of the Guilty": {
        "visibility_flag": Flags.Recipes_UncommonStaffs_Bought,
        "cost": 10000,
        "id": 3326,
        "recipe": [
            (1, Materials.StaffPole),
            (1, Materials.ErdtreeWood),
            (10, Materials.Bloodrose),
            (10, Materials.FireBlossom),
        ],
    },
    "Rotten Crystal Staff": {
        "visibility_flag": Flags.Recipes_RareStaffs_Bought,
        "cost": 15000,
        "id": 3327,
        "recipe": [
            (1, Materials.StaffPole),
            (5, Materials.SomberStoneFragment),
            (3, Materials.GlintstoneDust),
            (10, Materials.AeonianButterfly),
        ],
    },
    "Staff of Loss": {
        "visibility_flag": Flags.Recipes_RareStaffs_Bought,
        "cost": 15000,
        "id": 3328,
        "recipe": [
            (1, Materials.StaffPole),
            (3, Materials.RefinedWood),
            (10, Materials.NascentButterfly),
        ],
    },
    # endregion

    # region Seals
    "Finger Seal": {
        "visibility_flag": 0,
        "cost": 200,
        "id": 3400,
        "recipe": [
            (3, Materials.StoneFragment),
            (3, Materials.SomberStoneFragment),
            (5, Materials.ErdleafFlower),
        ],
    },
    "Godslayer's Seal": {
        "visibility_flag": Flags.Recipes_RareSeals_Bought,
        "cost": 15000,
        "id": 3401,
        "recipe": [
            (15, Materials.StoneFragment),
            (15, Materials.SomberStoneFragment),
            (2, Materials.BlackMark),
        ],
    },
    "Giant's Seal": {
        "visibility_flag": Flags.Recipes_UncommonSeals_Bought,
        "cost": 10000,
        "id": 3402,
        "recipe": [
            (12, Materials.StoneFragment),
            (12, Materials.SomberStoneFragment),
            (20, Materials.FireBlossom),
            (10, Materials.String),
        ],
    },
    "Gravel Stone Seal": {
        "visibility_flag": Flags.Recipes_RareSeals_Bought,
        "cost": 15000,
        "id": 3403,
        "recipe": [
            (12, Materials.GravelStone),
            (3, Materials.DragonTeeth),
            (20, Materials.Fulgurbloom),
        ],
    },
    "Clawmark Seal": {
        "visibility_flag": Flags.Recipes_UncommonSeals_Bought,
        "cost": 10000,
        "id": 3404,
        "recipe": [
            (10, Materials.StoneFragment),
            (10, Materials.SomberStoneFragment),
            (8, Materials.OldFang),
            (8, Materials.BeastBlood),
        ],
    },
    "Golden Order Seal": {
        "visibility_flag": Flags.Recipes_RareSeals_Bought,
        "cost": 15000,
        "id": 3406,
        "recipe": [
            (4, Materials.ErdtreeAmber),
            (10, Materials.GoldenCentipede),
            (15, Materials.GoldFirefly),
        ],
    },
    "Erdtree Seal": {
        "visibility_flag": Flags.Recipes_VeryRareSeals_Bought,
        "cost": 20000,
        "id": 3407,
        "recipe": [
            (5, Materials.ErdtreeAmber),
            (30, Materials.ErdleafFlower),
            (25, Materials.GoldenSunflower),
        ],
    },
    "Dragon Communion Seal": {
        "visibility_flag": Flags.Recipes_UncommonSeals_Bought,
        "cost": 10000,
        "id": 3408,
        "recipe": [
            (13, Materials.BeastBlood),
            (3, Materials.DragonTeeth),
            (20, Materials.SacramentalBud),
        ],
    },
    "Frenzied Flame Seal": {
        "visibility_flag": Flags.Recipes_VeryRareSeals_Bought,
        "cost": 20000,
        "id": 3409,
        "recipe": [
            (25, Materials.YellowEmber),
            (25, Materials.EyeOfYelough),
            (15, Materials.ArteriaLeaf),
        ],
    },
    # endregion

    # region Bows
    "Shortbow": {
        "visibility_flag": 0,
        "previous": None,
        "tier": 0,
        "somber": False,
        "id": 4000,
        "recipe": [
            (2, Materials.SoftWood),
            (1, Materials.String),
        ],
        "cost": 50,
    },
    "Misbegotten Shortbow": {
        "previous": "Shortbow",
        "tier": 5,
        "somber": False,
        "id": 4001,
        "recipe": [
            (3, Materials.SoftWood),
            (2, Materials.RefinedWood),
            (15, Materials.ThinBeastBones),
            (6, Materials.String),
        ],
    },
    "Red Branch Shortbow": {
        "previous": "Harp Bow",
        "tier": 8,
        "somber": False,
        "id": 4002,
        "recipe": [
            (8, Materials.RefinedWood),
            (5, Materials.String),
            (15, Materials.AltusBloom),
        ],
    },
    "Harp Bow": {
        "previous": "Shortbow",
        "tier": 6,
        "somber": True,
        "id": 4003,
        "recipe": [
            (4, Materials.RefinedWood),
            (8, Materials.String),
            (15, Materials.CaveMoss),
        ],
    },
    "Composite Bow": {
        "previous": "Harp Bow",
        "tier": 10,
        "somber": False,
        "id": 4005,
        "recipe": [
            (6, Materials.SoftWood),
            (4, Materials.RefinedWood),
            (1, Materials.ErdtreeWood),
            (5, Materials.String),
        ],
    },
    "Longbow": {
        "previous": "Red Branch Shortbow",
        "tier": 10,
        "somber": False,
        "id": 4100,
        "recipe": [
            (6, Materials.RefinedWood),
            (2, Materials.ErdtreeWood),
            (5, Materials.String),
        ],
    },
    "Albinauric Bow": {
        "previous": "Longbow",
        "tier": 15,
        "somber": False,
        "id": 4101,
        "recipe": [
            (8, Materials.RefinedWood),
            (15, Materials.AlbinauricBloodclot),
            (13, Materials.SilverFirefly),
            (6, Materials.String),
        ],
    },
    "Horn Bow": {
        "previous": "Longbow",
        "tier": 15,
        "somber": False,
        "id": 4102,
        "recipe": [
            (20, Materials.BuddingHorn),
            (6, Materials.String),
            (10, Materials.MeltedMushroom),
            (4, Materials.GlintstoneDust),
        ],
    },
    "Erdtree Bow": {
        "previous": "Longbow",
        "tier": 20,
        "somber": True,
        "id": 4103,
        "recipe": [
            (8, Materials.ErdtreeWood),
            (12, Materials.String),
            (10, Materials.RimedRowa),
            (5, Materials.ErdtreeAmber),
        ],
    },
    "Serpent Bow": {
        "previous": "Longbow",
        "tier": 20,
        "somber": True,
        "id": 4104,
        "recipe": [
            (10, Materials.RefinedWood),
            (12, Materials.String),
            (8, Materials.GruesomeBone),
            (20, Materials.MirandaPowder),
        ],
    },
    "Pulley Bow": {
        "previous": "Misbegotten Shortbow",
        "tier": 16,
        "somber": True,
        "id": 4106,
        "recipe": [
            (8, Materials.RefinedWood),
            (5, Materials.ErdtreeWood),
            (10, Materials.String),
            (15, Materials.StormhawkFeather),
        ],
    },
    "Black Bow": {
        "previous": "Albinauric Bow",
        "tier": 20,
        "somber": True,
        "id": 4107,
        "recipe": [
            (13, Materials.RefinedWood),
            (13, Materials.String),
            (3, Materials.BlackMark),
            (10, Materials.BloodTaintedExcrement),
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
            (4, Materials.MetalPlate),
            (6, Materials.MeteoriteChunk),
            (15, Materials.String),
        ],
    },
    "Golem Greatbow": {
        "previous": "Greatbow",
        "tier": 16,
        "somber": True,
        "id": 4201,
        "recipe": [
            (13, Materials.StoneFragment),
            (13, Materials.SomberStoneFragment),
            (3, Materials.MeteoriteChunk),
            (12, Materials.String),
        ],
    },
    "Erdtree Greatbow": {
        "previous": "Greatbow",
        "tier": 20,
        "somber": True,
        "id": 4203,
        "recipe": [
            (15, Materials.ErdtreeWood),
            (15, Materials.String),
            (25, Materials.GoldenCentipede),
            (6, Materials.ErdtreeAmber),
        ],
    },
    "Greatbow": {
        "previous": "Longbow",
        "tier": 14,
        "somber": False,
        "id": 4204,
        "recipe": [
            (9, Materials.RefinedWood),
            (3, Materials.ErdtreeWood),
            (10, Materials.String),
            (20, Materials.AltusBloom),
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
            (8, Materials.SoftWood),
            (2, Materials.RefinedWood),
            (2, Materials.MetalPlate),
            (7, Materials.String),
        ],
    },
    "Light Crossbow": {
        "previous": "Soldier's Crossbow",
        "tier": 13,
        "somber": False,
        "id": 4302,
        "recipe": [
            (6, Materials.RefinedWood),
            (2, Materials.MetalPlate),
            (7, Materials.String),
            (5, Materials.MetalShards),
        ],
    },
    "Heavy Crossbow": {
        "previous": "Light Crossbow",
        "tier": 16,
        "somber": False,
        "id": 4303,
        "recipe": [
            (8, Materials.RefinedWood),
            (2, Materials.MetalPlate),
            (8, Materials.String),
            (13, Materials.FireBlossom),
        ],
    },
    "Pulley Crossbow": {
        "previous": "Heavy Crossbow",
        "tier": 20,
        "somber": True,
        "id": 4305,
        "recipe": [
            (3, Materials.MetalPlate),
            (7, Materials.ErdtreeWood),
            (10, Materials.String),
            (18, Materials.GoldenCentipede),
        ],
    },
    "Full Moon Crossbow": {
        "previous": "Light Crossbow",
        "tier": 20,
        "somber": True,
        "id": 4306,
        "recipe": [
            (8, Materials.ErdtreeWood),
            (20, Materials.SomberStoneFragment),
            (10, Materials.String),
            (10, Materials.GlintstoneDust),
        ],
    },
    "Arbalest": {
        "previous": "Heavy Crossbow",
        "tier": 18,
        "somber": False,
        "id": 4308,
        "recipe": [
            (15, Materials.SoftWood),
            (5, Materials.RefinedWood),
            (2, Materials.MetalPlate),
            (7, Materials.String),
        ],
    },
    "Crepus's Black-Key Crossbow": {
        "previous": "Heavy Crossbow",
        "tier": 20,
        "somber": True,
        "id": 4311,
        "recipe": [
            (13, Materials.RefinedWood),
            (2, Materials.MetalPlate),
            (10, Materials.String),
            (3, Materials.BlackMark),
        ],
    },
    "Hand Ballista": {
        "previous": "Arbalest",
        "tier": 20,
        "somber": False,
        "id": 4400,
        "recipe": [
            (20, Materials.SoftWood),
            (10, Materials.RefinedWood),
            (3, Materials.MetalPlate),
            (15, Materials.String),
        ],
    },
    "Jar Cannon": {
        "previous": "Arbalest",
        "tier": 20,
        "somber": True,
        "id": 4401,
        "recipe": [
            (30, Materials.LivingJarShard),
            (4, Materials.MetalPlate),
            (30, Materials.FireBlossom),
        ],
    },
    # endregion
}
