"""
Notes: RNG weights

# Vanilla material values. Add value for highest tier present ONCE, then multiply sum with VanillaMaterial.
    # This part kinda sucks.
    VanillaMat_Per = .25
    Tier1Mat = 1 # Early game/Common vanilla Materials
    Tier2Mat = 2 # Mid game or Uncommon vanilla Materials
    Tier3Mat = 4 # Late game or Rare vanilla Materials

    StoneFragment = .4
    SomberStoneFragment = .75
    IronShards = .75
    SoftWood = 1
    IronPlate = 1.5
    RefinedWood = 2
    GlintstoneDust = 4
    ErdtreeAmber = 4
    LiquidMetal = 6
    GruesomeBone = 8
    MeteoriteChunk = 8
    BlackMark = 8
    DragonTeeth = 10
    ErdtreeWood = ?

    # Tier thresholds (Probably worthless now. Instead, order a list by material cost?)
    Tier0 = 0
    Tier1 = 6
    Tier2 = 12
    Tier3 = 16

---------
Logic notes

Things to calculate around:
    Material value total
    Stat requirements
    Base scaling?? 
        This is questionable you remember infusions exist
        But at the same time, things would be less inconsistent for int/faith/arc builds

---------
Other notes
    ErdtreeWood: Currently used in a few bow recipes, but can probably be replaced and cut

"""
from survival_enums import *


class Materials(IntEnum):

    # region Remembrances
    Remembrance_Godrick = 2950
    Remembrance_Radahn = 2951
    Remembrance_Morgott = 2952
    Remembrance_Rykard = 2953
    Remembrance_Malenia = 2954
    Remembrance_Mohg = 2955
    Remembrance_Maliketh = 2956
    Remembrance_HoarahLoux = 2957
    Remembrance_Dragonlord = 2958
    Remembrance_Rennala = 2959
    Remembrance_Fortissax = 2960
    Remembrance_FireGiant = 2961
    Remembrance_RegalAncestor = 2962
    Remembrance_EldenBeast = 2963
    Remembrance_Astel = 2964
    # endregion

    # region Vanilla items
    SliverOfMeat = 15000
    BeastLiver = 15010
    LumpOfFlesh = 15020
    BeastBlood = 15030
    OldFang = 15040
    BuddingHorn = 15050
    FlightPinion = 15060
    FourToedFowlFoot = 15080
    TurtleNeckMeat = 15090
    HumanBoneShard = 15100
    GreatDragonflyHead = 15110
    SlumberingEgg = 15120
    CrabEggs = 15130
    LandOctopusOvary = 15140
    MirandaPowder = 15150
    StripOfWhiteFlesh = 15160
    ThinBeastBones = 15340
    HeftyBeastBone = 15341
    String = 15400
    LivingJarShard = 15410
    AlbinauricBloodclot = 15420
    StormhawkFeather = 15430
    Poisonbloom = 20650
    TrinasLily = 20651
    Fulgurbloom = 20652
    MiquellasLily = 20653
    GraveViolet = 20654
    FadedErdleafFlower = 20660
    ErdleafFlower = 20680
    AltusBloom = 20681
    FireBlossom = 20682
    GoldenSunflower = 20683
    TarnishedGoldenSunflower = 20685
    Herba = 20690
    ArteriaLeaf = 20691
    DewkissedHerba = 20710
    RowaFruit = 20720
    GoldenRowa = 20721
    RimedRowa = 20722
    Bloodrose = 20723
    EyeOfYelough = 20740
    CrystalBud = 20750
    RimedCrystalBud = 20751
    SacramentalBud = 20753
    Mushroom = 20760
    MeltedMushroom = 20761
    ToxicMushroom = 20770
    RootResin = 20775
    CrackedCrystal = 20780
    SanctuaryStone = 20795
    NascentButterfly = 20800
    AeonianButterfly = 20801
    SmolderingButterfly = 20802
    SilverFirefly = 20810
    GoldFirefly = 20811
    GlintstoneFirefly = 20812
    GoldenCentipede = 20820
    SilverTearHusk = 20825
    GoldTingedExcrement = 20830
    BloodTaintedExcrement = 20831
    CaveMoss = 20840
    BuddingCaveMoss = 20841
    CrystalCaveMoss = 20842
    YellowEmber = 20845
    VolcanicStone = 20850
    FormicRock = 20852
    GravelStone = 20855
    # endregion

    # NEW ITEMS

    # Basic equipment components.
    SoftWood = 21000  # Very Common. Weapons with wood. Weaker weapons/arrows.
    RefinedWood = 21001  # Uncommon? Weapons with wood. Stronger weapons/arrows.
    StoneFragment = 21002  # Used for stronger weapons. Replaces many Smithing Stone drops.
    SomberStoneFragment = 21003  # Used for EVEN STRONGER weapons. Replaces many Somber Smithing Stone drops.
    IronShards = 21004  # Generic metal scrap. Very common. Worth a "portion" of an Iron plate. More for DEX/bleed.
    IronPlate = 21005  # Generic metal plate. Base material for most metal weapons. More for STR/heft.
    LiquidMetal = 21006  # Rare. Used for Nox weapons and weird weapons. TODO: rename to something more generic?
    DragonTeeth = 21007  # Rare. Used for Dragon weapons
    GruesomeBone = 21008  # Rare. Used for weird weapons & Arcane weapons
    GlintstoneDust = 21009  # Semi-rare. Int stuff.
    ErdtreeAmber = 21010  # Semi-rare. Faith stuff.
    MeteoriteChunk = 21011  # Rare. Used for outer space stuff
    BlackMark = 21012  # Rare. Used for Mark of Death stuff. Black Knife assassins, gargoyles, godskin/blackflame
    ErdtreeWood = 21013  # mainly from defeating Erdtree Avatars

    # Required single base components for Staffs and Shields.
    StaffPole = 21100
    ShieldGrip = 21101  # 1 for small shields, 2 for medium shields, 3 for greatshields


class NotesRecipes(IntEnum):
    """New note/recipe goods, mostly for Merchants.

    Some 'notes' here actually serve as recipes (i.e., their 'bought' flag enables a recipe).
    """
    Note_CurePlague = 8800
    Note_CureToxin = 8801
    Note_CureFever = 8802
    Note_CureParasite = 8803

    # TODO: Meteor Chuck note...

    Recipes_CommonSurvival = 9200  # sold by Kale  TODO: ensure he drops it on death
    # TODO: Give these to multiple merchants with the same purchase flag.
    Recipes_UncommonSurvival = 9201
    Recipes_RareSurvival = 9202
    Recipes_VeryRareSurvival = 9203

    # TODO: Assign rarity to each shield in recipe, which (with its type) determines its recipe visibility flag.
    Recipes_CommonSmallShields = 9210  # sold by Kale  TODO: ensure he drops it on death
    Recipes_UncommonSmallShields = 9211
    Recipes_RareSmallShields = 9212
    Recipes_VeryRareSmallShields = 9213

    Recipes_CommonMediumShields = 9220  # sold by Kale  TODO: ensure he drops it on death
    Recipes_UncommonMediumShields = 9221
    Recipes_RareMediumShields = 9222
    Recipes_VeryRareMediumShields = 9223

    Recipes_CommonGreatshields = 9230  # sold by Kale  TODO: ensure he drops it on death
    Recipes_UncommonGreatshields = 9231
    Recipes_RareGreatshields = 9232
    Recipes_VeryRareGreatshields = 9233

    Note_SerpentHunter = 8810


# Keys are offsets used in all IDs.
NEW_CONSUMABLES = {
    0: {
        "name": "Raw Steak",
        "info": "Basic raw meal crafted by hunters",
        "caption": "TODO",
        "recipe": [  # for `EquipMtrlSetParam`
            (3, Materials.SliverOfMeat),
        ],
        "effect": SurvivalEffects.RawSteak,  # for `EquipGoodsParam`
        "animation": GoodsUseAnimation.ITEM_EATJERKY,  # for `EquipGoodsParam`
    },
    1: {
        "name": "Seared Steak",
        "info": "Basic cooked meal crafted by hunters",
        "caption": "TODO",
        "recipe": [
            (3, Materials.SliverOfMeat),
            (2, Materials.SmolderingButterfly),
        ],
        "effect": SurvivalEffects.SearedSteak,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
    },
    2: {
        "name": "Raw Liver Steak",
        "info": "Raw meal crafted by expert hunters",
        "caption": "TODO",
        "recipe": [
            (2, Materials.SliverOfMeat),
            (1, Materials.BeastLiver),
        ],
        "effect": SurvivalEffects.RawLiverSteak,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
    },
    3: {
        "name": "Seared Liver Steak",
        "info": "Cooked meal crafted by expert hunters",
        "caption": "TODO",
        "recipe": [
            (2, Materials.SliverOfMeat),
            (1, Materials.BeastLiver),
            (2, Materials.SmolderingButterfly),
        ],
        "effect": SurvivalEffects.SearedLiverSteak,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
    },
    4: {
        "name": "Bone Broth",
        "info": "Light broth to ward off thirst",
        "caption": "TODO",
        "recipe": [
            (5, Materials.ThinBeastBones),
        ],
        "effect": SurvivalEffects.BoneBroth,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
    },
    5: {
        "name": "Great Bone Broth",
        "info": "Hearty broth to ward off thirst",
        "caption": "TODO",
        "recipe": [
            (3, Materials.HeftyBeastBone),
        ],
        "effect": SurvivalEffects.GreatBoneBroth,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
    },
    6: {
        "name": "Blood Broth",
        "info": "Broth preferred by bloodthirsty hunters",
        "caption": "TODO",
        "recipe": [
            (3, Materials.ThinBeastBones),
            (2, Materials.BeastBlood),
        ],
        "effect": SurvivalEffects.BloodBroth,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
    },
    7: {
        "name": "Forest Berry Medley",
        "info": "Medley of berries from the lower lands",
        "caption": "TODO",
        "recipe": [
            (10, Materials.RowaFruit),
        ],
        "effect": SurvivalEffects.BerryMedley1,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
    },
    8: {
        "name": "Plateau Berry Medley",
        "info": "Medley of berries from the plateau",
        "caption": "TODO",
        "recipe": [
            (10, Materials.GoldenRowa),
        ],
        "effect": SurvivalEffects.BerryMedley2,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
    },
    9: {
        "name": "Mountain Berry Medley",
        "info": "Medley of berries from the mountains",
        "caption": "TODO",
        "recipe": [
            (10, Materials.RimedRowa),
        ],
        "effect": SurvivalEffects.BerryMedley3,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
    },
    10: {
        "name": "Mushroom Stew",
        "info": "Basic mushroom stew",
        "caption": "TODO",
        "recipe": [
            (3, Materials.Mushroom),
            (3, Materials.Herba),
        ],
        "effect": SurvivalEffects.MushroomStew,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
    },
    11: {
        "name": "Melted Mushroom Stew",
        "info": "Delicious mushroom stew",
        "caption": "TODO",
        "recipe": [
            (3, Materials.MeltedMushroom),
            (3, Materials.DewkissedHerba),
        ],
        "effect": SurvivalEffects.MeltedMushroomStew,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
    },
    12: {
        "name": "Draught of the Undining",
        "info": "Prevents hunter temporarily",
        "caption": "TODO",
        "recipe": [
            (3, Materials.GraveViolet),
            # TODO: More ingredients.
        ],
        "effect": SurvivalEffects.DraughtOfTheUndining,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
    },
    13: {
        "name": "Draught of Silver Tears",
        "info": "Prevents thirst temporarily",
        "caption": "TODO",
        "recipe": [
            (7, Materials.SilverTearHusk),
            # TODO: More ingredients.
        ],
        "effect": SurvivalEffects.DraughtOfSilverTears,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
    },
    14: {
        "name": "Mossdew Soup",
        "info": "Soup with mild heat protected",
        "caption": "TODO",
        "recipe": [
            (3, Materials.CaveMoss),
            (4, Materials.DewkissedHerba),
        ],
        "effect": SurvivalEffects.MossdewSoup,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
    },
    15: {
        "name": "Crystal Shard Soup",
        "info": "Soup with moderate heat protection",
        "caption": "TODO",
        "recipe": [
            (2, Materials.BuddingCaveMoss),
            (5, Materials.CrackedCrystal),
        ],
        "effect": SurvivalEffects.CrystalShardSoup,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
    },
    16: {
        "name": "Giant's Soup",
        "info": "Soup with great heat protection",
        "caption": "TODO",
        "recipe": [
            (5, Materials.RimedRowa),
            (2, Materials.CrystalCaveMoss),
            (2, Materials.RimedRowa),
        ],
        "effect": SurvivalEffects.GiantsSoup,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
    },
    17: {
        "name": "Amber-Eye Brew",
        "info": "Brew with mild cold protection",
        "caption": "TODO",
        "recipe": [
            (3, Materials.EyeOfYelough),
            (1, Materials.YellowEmber),
            (3, Materials.Herba),
        ],
        "effect": SurvivalEffects.AmberEyeBrew,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
    },
    18: {
        "name": "Magmatic Brew",
        "info": "Brew with moderate cold protection",
        "caption": "TODO",
        "recipe": [
            (4, Materials.VolcanicStone),
            (3, Materials.TarnishedGoldenSunflower),
        ],
        "effect": SurvivalEffects.MagmaticBrew,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
    },
    19: {
        "name": "Blossom Brew",
        "info": "Brew with great cold protection",
        "caption": "TODO",
        "recipe": [
            (5, Materials.FireBlossom),
            (3, Materials.FormicRock),
        ],
        "effect": SurvivalEffects.BlossomBrew,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
    },
    20: {
        "name": "Jar Brittle",
        "info": "Crunchy brittle from living jars",
        "caption": "TODO",
        "recipe": [
            (5, Materials.LivingJarShard),
        ],
        "effect": SurvivalEffects.JarBrittle,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
    },
}


NEW_MATERIALS = {
    Materials.SoftWood: {
        "name": "Soft Wood",
        "info": "Unremarkable piece of wood",
        "caption": "TODO",
        "icon": 623,  # TODO: Bewitching Branch for now
    },
    Materials.RefinedWood: {
        "name": "Refined Wood",
        "info": "Robust piece of wood",
        "caption": "TODO",
        "icon": 623,  # TODO: Bewitching Branch for now
    },
    Materials.StoneFragment: {
        "name": "Stone Fragment",
        "info": "Fragment of simple colored stone",
        "caption": "TODO",
        "icon": 2000,  # TODO: Smithing Stone [1] for now
    },
    Materials.SomberStoneFragment: {
        "name": "Somber Stone Fragment",
        "info": "Fragment of rare colorless stone",
        "caption": "TODO",
        "icon": 2010,  # TODO: Somber Smithing Stone [1] for now
    },
    Materials.IronShards: {
        "name": "Iron Shards",
        "info": "Small chips of iron",
        "caption": "TODO",
        "icon": 90,  # TODO: Rainbow Stone for now
    },
    Materials.IronPlate: {
        "name": "Iron Plate",
        "info": "Basic component of metallic weaponry",
        "caption": "TODO",
        "icon": 210,  # TODO: Warming Stone for now
    },
    Materials.LiquidMetal: {
        "name": "Liquid Metal",
        "info": "Rare component of unusual weapons",
        "caption": "TODO",
        "icon": 91,  # TODO: Glowstone for now
    },
    Materials.DragonTeeth: {
        "name": "Dragon Teeth",
        "info": "",
        "caption": "TODO",
        "icon": 2008,  # TODO: Ancient Dragon Smithing Stone for now
    },
    Materials.GruesomeBone: {
        "name": "Gruesome Bone",
        "info": "",
        "caption": "TODO",
        "icon": 1020,  # TODO: Hefty Beast Bone for now
    },
    Materials.ErdtreeWood: {
        "name": "Erdtree Wood",
        "info": "",
        "caption": "TODO",
        "icon": 321,  # TODO: Erdtree Codex for now
    },
    Materials.MeteoriteChunk: {
        "name": "Meteorite Chunk",
        "info": "Resin sourced from the Erdtree",
        "caption": "TODO",
        "icon": 200,  # TODO: Gravity Stone Chunk for now
    },
    Materials.BlackMark: {
        "name": "Black Mark",
        "info": "Dense chunk of cosmic debris",
        "caption": "TODO",
        "icon": 3228,  # TODO: Cursemark of Death for now
    },
    Materials.StaffPole: {
        "name": "Staff Pole",
        "info": "",
        "caption": "TODO",
        "icon": 92,  # TODO: Telescope for now
    },
    Materials.ShieldGrip: {
        "name": "Shield Handle",
        "info": "Sacred wood from the Erdtree",
        "caption": "TODO",
        "icon": 591,  # TODO: Soft Cotton for now
    },
}


# TODO: Specify their merchant shop lineup row ID.
#  I think some (e.g. for Kale) may have to override other shop entries.
NEW_NOTES_RECIPES = {
    NotesRecipes.Note_CurePlague: {
        "name": "Note: Cure for Plagues",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Note_CurePlague_Bought,
    },
    NotesRecipes.Note_CureToxin: {
        "name": "Note: Cure for Toxins",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Note_CureToxin_Bought,
    },
    NotesRecipes.Note_CureFever: {
        "name": "Note: Cure for Fever",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Note_CureFever_Bought,
    },
    NotesRecipes.Note_CureParasite: {
        "name": "Note: Cure for Parasites",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Note_CureParasite_Bought,
    },
    NotesRecipes.Recipes_CommonSurvival: {
        "name": "Survivalist's Cookbook [1]",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_CommonSurvival_Bought,
    },
    NotesRecipes.Recipes_UncommonSurvival: {
        "name": "Survivalist's Cookbook [2]",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_UncommonSurvival_Bought,
    },
    NotesRecipes.Recipes_RareSurvival: {
        "name": "Survivalist's Cookbook [3]",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_RareSurvival_Bought,
    },
    NotesRecipes.Recipes_VeryRareSurvival: {
        "name": "Survivalist's Cookbook [4]",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_VeryRareSurvival_Bought,
    },
    NotesRecipes.Recipes_CommonSmallShields: {
        "name": "Small Shield Smithbook [1]",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_CommonSmallShields_Bought,
    },
    NotesRecipes.Recipes_UncommonSmallShields: {
        "name": "Small Shield Smithbook [2]",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_UncommonSmallShields_Bought,
    },
    NotesRecipes.Recipes_RareSmallShields: {
        "name": "Small Shield Smithbook [3]",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_RareSmallShields_Bought,
    },
    NotesRecipes.Recipes_VeryRareSmallShields: {
        "name": "Small Shield Smithbook [4]",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_VeryRareSmallShields_Bought,
    },
    NotesRecipes.Recipes_CommonMediumShields: {
        "name": "Medium Shield Smithbook [1]",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_CommonMediumShields_Bought,
    },
    NotesRecipes.Recipes_UncommonMediumShields: {
        "name": "Medium Shield Smithbook [2]",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_UncommonMediumShields_Bought,
    },
    NotesRecipes.Recipes_RareMediumShields: {
        "name": "Medium Shield Smithbook [3]",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_RareMediumShields_Bought,
    },
    NotesRecipes.Recipes_VeryRareMediumShields: {
        "name": "Medium Shield Smithbook [4]",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_VeryRareMediumShields_Bought,
    },
    NotesRecipes.Recipes_CommonGreatshields: {
        "name": "Greatshield Smithbook [1]",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_CommonGreatshields_Bought,
    },
    NotesRecipes.Recipes_UncommonGreatshields: {
        "name": "Greatshield Smithbook [2]",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_UncommonGreatshields_Bought,
    },
    NotesRecipes.Recipes_RareGreatshields: {
        "name": "Greatshield Smithbook [3]",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_RareGreatshields_Bought,
    },
    NotesRecipes.Recipes_VeryRareGreatshields: {
        "name": "Greatshield Smithbook [4]",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_VeryRareGreatshields_Bought,
    },
    NotesRecipes.Note_SerpentHunter: {
        "name": "Note: The Serpent-Hunter",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Note_SerpentHunter,
    },
}


# Prices for replaced merchant items.
MERCHANT_PRICES = {
    Materials.SoftWood: 400,
    Materials.RefinedWood: 2500,
    Materials.StoneFragment: 1000,  # not actually sold
    Materials.SomberStoneFragment: 3000,  # not actually sold
    Materials.IronShards: 1200,
    Materials.IronPlate: 4000,
    Materials.LiquidMetal: 8000,
    Materials.DragonTeeth: 9000,
    Materials.GruesomeBone: 7000,
    Materials.GlintstoneDust: 8000,
    Materials.ErdtreeAmber: 15000,
    Materials.MeteoriteChunk: 12000,
    Materials.BlackMark: 20000,
    Materials.ErdtreeWood: 10000,
    Materials.StaffPole: 5000,
    Materials.ShieldGrip: 3000,
}


class MaterialRarity(IntEnum):
    Common = 40
    Uncommon = 30
    Rare = 20
    VeryRare = 10


# Rarity and max count for each material that could replace a weapon (map only).
MATERIAL_RARITY_COUNT = {
    Materials.SoftWood: (MaterialRarity.Common, 3),
    Materials.RefinedWood: (MaterialRarity.Uncommon, 2),
    # Materials.StoneFragment: (0, 1),  # does not replace weapons
    # Materials.SomberStoneFragment: (0, 1),  # does not replace weapons
    Materials.IronShards: (MaterialRarity.Common, 4),
    Materials.IronPlate: (MaterialRarity.Uncommon, 1),
    Materials.LiquidMetal: (MaterialRarity.Rare, 1),
    Materials.DragonTeeth: (MaterialRarity.Rare, 1),
    Materials.GruesomeBone: (MaterialRarity.Rare, 1),
    Materials.GlintstoneDust: (MaterialRarity.Uncommon, 1),
    Materials.ErdtreeAmber: (MaterialRarity.VeryRare, 1),
    Materials.MeteoriteChunk: (MaterialRarity.Rare, 1),
    Materials.BlackMark: (MaterialRarity.VeryRare, 1),
    Materials.ErdtreeWood: (MaterialRarity.Rare, 1),
    Materials.StaffPole: (MaterialRarity.Rare, 1),
    Materials.ShieldGrip: (MaterialRarity.Uncommon, 1),
}
