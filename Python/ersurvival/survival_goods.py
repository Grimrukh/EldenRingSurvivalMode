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
    Note_CuringDiseases = 8799
    Recipe_LimgraveDiseaseCure = 8800
    Recipe_LiurniaDiseaseCure = 8801
    Recipe_CaelidDiseaseCure = 8802
    Recipe_AltusDiseaseCure = 8803
    Recipe_MtGelmirDiseaseCure = 8804
    Recipe_MountaintopsDiseaseCure = 8805
    Recipe_SiofraDiseaseCure = 8806
    Recipe_AinselDiseaseCure = 8807
    Recipe_DeeprootDiseaseCure = 8808
    Recipe_StormveilDiseaseCure = 8809
    Recipe_RayaLucariaDiseaseCure = 8810
    Recipe_RadahnDiseaseCure = 8811
    Recipe_VolcanoManorDiseaseCure = 8812
    Recipe_LeyndellDiseaseCure = 8813
    Recipe_SewersDiseaseCure = 8814
    Recipe_HaligtreeDiseaseCure = 8815
    Recipe_FarumAzulaDiseaseCure = 8816
    Recipe_MohgwynDiseaseCure = 8817
    Recipe_CatacombsDiseaseCure = 8818
    Recipe_CaveDiseaseCure = 8819
    Recipe_TunnelDiseaseCure = 8820

    Note_SerpentHunter = 8830
    Note_Whip = 8831
    # TODO: Meteor Chuck note...
    # NOTE: Vanilla IDs start at 8850.

    Recipes_CommonSurvival = 9200  # sold by Kale  TODO: ensure he drops it on death
    # TODO: Give these to multiple merchants with the same purchase flag.
    Recipes_UncommonSurvival = 9201
    Recipes_RareSurvival = 9202
    Recipes_VeryRareSurvival = 9203

    # TODO: Assign rarity to each shield in recipe, which (with its type) determines its recipe visibility flag.
    Recipes_WoodenSmallShields = 9210  # sold by Kale  TODO: ensure he drops it on death
    Recipes_MetalSmallShields = 9211
    Recipes_RareSmallShields = 9212
    Recipes_VeryRareSmallShields = 9213

    Recipes_CommonMediumShields = 9220  # sold by Kale  TODO: ensure he drops it on death
    Recipes_WoodenMediumShields = 9221  # sold by Kale  TODO: ensure he drops it on death
    Recipes_HeaterMediumShields = 9222
    Recipes_KiteMediumShields = 9223
    Recipes_RareMediumShields = 9224

    Recipes_CommonGreatshields = 9230  # sold by Kale  TODO: ensure he drops it on death
    Recipes_UncommonGreatshields = 9231
    Recipes_RareGreatshields = 9232
    Recipes_VeryRareGreatshields = 9233

    Recipes_CommonStaffs = 9240
    Recipes_UncommonStaffs = 9241
    Recipes_RareStaffs = 9242
    Recipes_VeryRareStaffs = 9243

    Recipes_CommonSeals = 9250
    Recipes_UncommonSeals = 9251
    Recipes_RareSeals = 9252
    Recipes_VeryRareSeals = 9253

    Recipe_SteelWireTorch = 9260
    Recipe_StTrinasTorch = 9261
    Recipe_GhostflameTorch = 9262
    Recipe_BeastRepellentTorch = 9263
    Recipe_SentrysTorch = 9264


# Keys are offsets used in all IDs.
    # George: I marked things with XXXX that need to be updated.
NEW_CONSUMABLES = {
    0: {
        "name": "Raw Steak",
        "info": "Basic raw meal crafted by hunters",
        "caption": "Raw cut of meat prepared from scraps of flesh.\nCraftable survival item.\n\nConsume to relieve hunger, but not without risk.",
        "recipe": [  # for `EquipMtrlSetParam`
            (3, Materials.SliverOfMeat),
        ],
        "effect": SurvivalEffects.RawSteak,  # for `EquipGoodsParam`
        "animation": GoodsUseAnimation.ITEM_EATJERKY,  # for `EquipGoodsParam`
        "icon": 19000,
    },
    1: {
        "name": "Seared Steak",
        "info": "Basic cooked meal crafted by hunters",
        "caption": "Cooked cut of meat prepared from scraps of flesh. Smells delicious.\nCraftable survival item.\n\nConsume to relieve hunger.",
        "recipe": [
            (3, Materials.SliverOfMeat),
            (2, Materials.SmolderingButterfly),
        ],
        "effect": SurvivalEffects.SearedSteak,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
        "icon": 19001,
    },
    2: {
        "name": "Raw Liver Steak",
        "info": "Raw meal crafted by expert hunters",
        "caption": "Raw cut of meat prepared from scraps of flesh and liver.\nCraftable survival item.\n\nConsume to relieve hunger, but not without risk.",
        "recipe": [
            (2, Materials.SliverOfMeat),
            (1, Materials.BeastLiver),
        ],
        "effect": SurvivalEffects.RawLiverSteak,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
        "icon": 19002,
    },
    3: {
        "name": "Seared Liver Steak",
        "info": "Cooked meal crafted by expert hunters",
        "caption": "Cooked cut of meat prepared from scraps of flesh and liver. Smells delicious.\nCraftable survival item.\n\nConsume to relieve hunger.",
        "recipe": [
            (2, Materials.SliverOfMeat),
            (1, Materials.BeastLiver),
            (2, Materials.SmolderingButterfly),
        ],
        "effect": SurvivalEffects.SearedLiverSteak,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
        "icon": 19003,
    },
    4: {
        "name": "Bone Broth",
        "info": "Light broth to ward off thirst",
        "caption": "Delicious broth prepared from bones.\nCraftable survival item.\n\nConsume to relieve thirst.",
        "recipe": [
            (5, Materials.ThinBeastBones),
        ],
        "effect": SurvivalEffects.BoneBroth,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
        "icon": 19004,
    },
    5: {
        "name": "Great Bone Broth",
        "info": "Hearty broth to ward off thirst",
        "caption": "Delicious hearty broth prepared from large bones.\nCraftable survival item.\n\nConsume to relieve thirst.",
        "recipe": [
            (3, Materials.HeftyBeastBone),
        ],
        "effect": SurvivalEffects.GreatBoneBroth,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
        "icon": 19005,
    },
    6: {
        "name": "Blood Broth",
        "info": "Broth preferred by bloodthirsty hunters",
        "caption": "Odorous broth prepared from bones and blood. A delicacy, for some.\nCraftable survival item.\n\nConsume to XXXX.",
        "recipe": [
            (3, Materials.ThinBeastBones),
            (2, Materials.BeastBlood),
        ],
        "effect": SurvivalEffects.BloodBroth,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
        "icon": 19006,
    },
    7: {
        "name": "Forest Berry Medley",
        "info": "Medley of berries from the lower lands",
        "caption": "Prepared fruits picked from rowa shrubs. Tannic, but delicious.\nCraftable survival item.\n\nConsume to relieve hunger and thirst.",
        "recipe": [
            (10, Materials.RowaFruit),
        ],
        "effect": SurvivalEffects.BerryMedley1,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
        "icon": 19007,
    },
    8: {
        "name": "Plateau Berry Medley",
        "info": "Medley of berries from the plateau",
        "caption": "Prepared fruits picked from golden rowa shrubs. Sweet and delicious.\nCraftable survival item.\n\nConsume to relieve hunger and thirst.",
        "recipe": [
            (10, Materials.GoldenRowa),
        ],
        "effect": SurvivalEffects.BerryMedley2,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
        "icon": 19008,
    },
    9: {
        "name": "Mountain Berry Medley",
        "info": "Medley of berries from the mountains",
        "caption": "Prepared fruits picked from rimed rowa shrubs. Slightly bitter, but uniquely delicious.\nCraftable survival item.\n\nConsume to relieve hunger and thirst.",
        "recipe": [
            (10, Materials.RimedRowa),
        ],
        "effect": SurvivalEffects.BerryMedley3,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
        "icon": 19009,
    },
    10: {
        "name": "Mushroom Stew",
        "info": "Basic mushroom stew",
        "caption": "Simple, but tasty stew prepared from mushrooms and herba.\nCraftable survival item.\n\nConsume to relieve hunger and thirst.",
        "recipe": [
            (3, Materials.Mushroom),
            (3, Materials.Herba),
        ],
        "effect": SurvivalEffects.MushroomStew,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
        "icon": 19010,
    },
    11: {
        "name": "Melted Mushroom Stew",
        "info": "Thick mushroom stew",
        "caption": "Thick stew prepared from mushrooms and herba. Unusual texture, but incredible taste.\nCraftable survival item.\n\nConsume to relieve hunger and thirst.",
        "recipe": [
            (3, Materials.MeltedMushroom),
            (3, Materials.DewkissedHerba),
        ],
        "effect": SurvivalEffects.MeltedMushroomStew,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
        "icon": 19011,
    },
    12: {
        "name": "Draught of Satiation",
        "info": "Prevents hunter temporarily",
        "caption": "Outlawed concotion made from XXXX. Smells terrible.\nCraftable survival item.\n\nConsume to prevent hunger temporarily.",
        "recipe": [
            (3, Materials.GraveViolet),
            # TODO: More ingredients.
        ],
        "effect": SurvivalEffects.DraughtOfSatiation,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
        "icon": 19012,
    },
    13: {
        "name": "Draught of Silver Tears",
        "info": "Prevents thirst temporarily",
        "caption": "Outlawed concotion made from XXXX. Smells awful.\nCraftable survival item.\n\nConsume to prevent thirst temporarily.",
        "recipe": [
            (7, Materials.SilverTearHusk),
            # TODO: More ingredients.
        ],
        "effect": SurvivalEffects.DraughtOfSilverTears,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
        "icon": 19013,
    },
    14: {
        "name": "Mossdew Soup",
        "info": "Soup with mild heat protection",
        "caption": "Simple medicinal soup. Tastes very bitter.\nCraftable survival item.\n\nConsume for mild heat protection. XXXX MECHANIC INFO NEEDED",
        "recipe": [
            (3, Materials.CaveMoss),
            (4, Materials.DewkissedHerba),
        ],
        "effect": SurvivalEffects.MossdewSoup,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
        "icon": 19014,
    },
    15: {
        "name": "Crystal Shard Soup",
        "info": "Soup with moderate heat protection",
        "caption": "Complex medicinal soup. Tastes slightly sweet.\nCraftable survival item.\n\nConsume for moderate heat protection. XXXX MECHANIC INFO NEEDED",
        "recipe": [
            (2, Materials.BuddingCaveMoss),
            (5, Materials.CrackedCrystal),
        ],
        "effect": SurvivalEffects.CrystalShardSoup,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
        "icon": 19015,
    },
    16: {
        "name": "Giant's Soup",
        "info": "Soup with great heat protection",
        "caption": "Masterful medicinal soup. Tastes pretty good.\nCraftable survival item.\n\nConsume for great heat protection. XXXX MECHANIC INFO NEEDED",
        "recipe": [
            (5, Materials.RimedRowa),
            (2, Materials.CrystalCaveMoss),
            (2, Materials.RimedRowa), #XXXX dupe ingredient whoopsie?
        ],
        "effect": SurvivalEffects.GiantsSoup,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
        "icon": 19016,
    },
    17: {
        "name": "Amber-Eye Brew",
        "info": "Brew with mild cold protection",
        "caption": "Simple medicinal brew. Rather intoxicating.\nCraftable survival item.\n\nConsume for mild cold protection. XXXX MECHANIC INFO NEEDED",
        "recipe": [
            (3, Materials.EyeOfYelough),
            (1, Materials.YellowEmber),
            (3, Materials.Herba),
        ],
        "effect": SurvivalEffects.AmberEyeBrew,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
        "icon": 19017,
    },
    18: {
        "name": "Magmatic Brew",
        "info": "Brew with moderate cold protection",
        "caption": "Complex medicinal brew. Makes your tongue feel like it's on fire!\nCraftable survival item.\n\nConsume for moderate cold protection. XXXX MECHANIC INFO NEEDED",
        "recipe": [
            (4, Materials.VolcanicStone),
            (3, Materials.TarnishedGoldenSunflower),
        ],
        "effect": SurvivalEffects.MagmaticBrew,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
        "icon": 19018,
    },
    19: {
        "name": "Blossom Brew",
        "info": "Brew with great cold protection",
        "caption": "Masterful medicinal brew. Very acidic, and strangely addictive.\nCraftable survival item.\n\nConsume for great cold protection. XXXX MECHANIC INFO NEEDED",
        "recipe": [
            (5, Materials.FireBlossom),
            (3, Materials.FormicRock),
        ],
        "effect": SurvivalEffects.BlossomBrew,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
        "icon": 19019,
    },
    20: {
        "name": "Jar Brittle",
        "info": "Crunchy brittle from living jars",
        "caption": "Aberrant food prepared from the flesh of living jars.\nMost find it abhorrent, but others swear it has a taste like no other.\nCraftable survival item.\n\nConsume to relieve hunger and gain mild heat & cold protection.\nHowever, it increases thirst.",
        "recipe": [
            (5, Materials.LivingJarShard),
        ],
        "effect": SurvivalEffects.JarBrittle,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
        "icon": 19020,
    },
}


NEW_MATERIALS = {
    Materials.SoftWood: {
        "name": "Soft Wood",
        "info": "Unremarkable piece of wood",
        "caption": "TODO",
        "icon": 19100,
    },
    Materials.RefinedWood: {
        "name": "Refined Wood",
        "info": "Robust piece of wood",
        "caption": "TODO",
        "icon": 19101,
    },
    Materials.StoneFragment: {
        "name": "Stone Fragment",
        "info": "Fragment of simple colored stone",
        "caption": "TODO",
        "icon": 19102,
    },
    Materials.SomberStoneFragment: {
        "name": "Somber Stone Fragment",
        "info": "Fragment of rare colorless stone",
        "caption": "TODO",
        "icon": 19103,
    },
    Materials.IronShards: {
        "name": "Iron Shards", #metal scrap? metal shards?
        "info": "Small chips of iron",
        "caption": "TODO",
        "icon": 19104,
    },
    Materials.IronPlate: {
        "name": "Iron Plate", #metal plate
        "info": "Basic component of metallic weaponry",
        "caption": "TODO",
        "icon": 19105,
    },
    Materials.LiquidMetal: {
        "name": "Liquid Metal", #fancy metal
        "info": "Rare component of unusual weapons",
        "caption": "TODO",
        "icon": 19106,
    },
    Materials.DragonTeeth: {
        "name": "Dragon Teeth",
        "info": "",
        "caption": "TODO",
        "icon": 19107,
    },
    Materials.GruesomeBone: {
        "name": "Gruesome Bone",
        "info": "",
        "caption": "TODO",
        "icon": 19108,
    },
    Materials.ErdtreeWood: {
        "name": "Erdtree Wood",
        "info": "",
        "caption": "TODO",
        "icon": 19109,
    },
    Materials.MeteoriteChunk: {
        "name": "Meteorite Chunk",
        "info": "Dense chunk of cosmic debris",
        "caption": "TODO",
        "icon": 19110,
    },
    Materials.BlackMark: {
        "name": "Black Mark",
        "info": "",
        "caption": "TODO",
        "icon": 19111,
    },
    Materials.StaffPole: {
        "name": "Staff Pole",
        "info": "",
        "caption": "TODO",
        "icon": 19112,
    },
    Materials.ShieldGrip: {
        "name": "Shield Handle",
        "info": "Sacred wood from the Erdtree",
        "caption": "TODO",
        "icon": 19113,
    },
    Materials.ErdtreeAmber: {
        "name": "Erdtree Amber",
        "info": "Resin sourced from the Erdtree",
        "caption": "TODO",
        "icon": 19114,
    },
    Materials.GlintstoneDust: {
        "name": "Glintstone Dust",
        "info": "Small grains of Glintstone",
        "caption": "TODO",
        "icon": 19115,
    },
}


# TODO: New key items: indicators that you have a disease.


# TODO: Specify their merchant shop lineup row ID.
#  I think some (e.g. for Kale) may have to override other shop entries.
NEW_NOTES_RECIPES = {
    # region Disease Cures
    NotesRecipes.Note_CuringDiseases : {
        "name": "Note: Finding Disease Cures",
        "info": "",
        "caption": "",
        "shop_row": 100521,  # Kale. TODO: Confirm this shop row appears (as with the rest).
        "bought_flag": SurvivalFlags.Note_CuringDiseases_Bought,
    },
    NotesRecipes.Recipe_LimgraveDiseaseCure : {
        "name": "Cure: Plague of Limgrave",
        "info": "",
        "caption": "",
        "shop_row": 100596,  # Coastal Cave merchant
        "bought_flag": SurvivalFlags.Recipe_LimgraveDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_LiurniaDiseaseCure : {
        "name": "Cure: Lake Toxin",
        "info": "",
        "caption": "",
        "shop_row": 100697,  # Academy of Raya Lucaria merchant
        "bought_flag": SurvivalFlags.Recipe_LiurniaDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_CaelidDiseaseCure : {
        "name": "Cure: Scarlet Parasite",
        "info": "",
        "caption": "",
        "shop_row": 100894,  # Dragonbarrow merchant
        "bought_flag": SurvivalFlags.Recipe_CaelidDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_AltusDiseaseCure : {
        "name": "Cure: Windmill Fever",
        "info": "",
        "caption": "",
        "shop_row": 100772,  # Altus Plateau merchant
        "bought_flag": SurvivalFlags.Recipe_AltusDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_MtGelmirDiseaseCure : {
        "name": "Cure: Plague of Gelmir",
        "info": "",
        "caption": "",
        "shop_row": 100799,  # Mt. Gelmir merchant
        "bought_flag": SurvivalFlags.Recipe_MtGelmirDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_MountaintopsDiseaseCure : {
        "name": "Cure: Frigid Parasite",
        "info": "",
        "caption": "",
        "shop_row": 100919,  # Mountaintops merchant
        "bought_flag": SurvivalFlags.Recipe_MountaintopsDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_SiofraDiseaseCure : {
        "name": "Cure: Plague of Nokron",
        "info": "",
        "caption": "",
        "shop_row": 100942,  # Siofra merchant
        "bought_flag": SurvivalFlags.Recipe_SiofraDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_AinselDiseaseCure : {
        "name": "Cure: Ant Toxin",
        "info": "",
        "caption": "",
        "shop_row": 100968,  # Ainsel merchant
        "bought_flag": SurvivalFlags.Recipe_AinselDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_DeeprootDiseaseCure : {
        "name": "Cure: Star-Shaped Parasite",
        "info": "",
        "caption": "",
        "item_lot": -1,  # TODO
        "bought_flag": SurvivalFlags.Recipe_DeeprootDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_StormveilDiseaseCure : {
        "name": "Cure: Grafted Plague",
        "info": "",
        "caption": "",
        "item_lot": -1,  # TODO
        "bought_flag": SurvivalFlags.Recipe_StormveilDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_RayaLucariaDiseaseCure : {
        "name": "Cure: Full Moon Fever",
        "info": "",
        "caption": "",
        "item_lot": -1,  # TODO
        "bought_flag": SurvivalFlags.Recipe_RayaLucariaDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_RadahnDiseaseCure : {
        "name": "Cure: Starscourge Fever",
        "info": "",
        "caption": "",
        "item_lot": -1,  # TODO
        "bought_flag": SurvivalFlags.Recipe_RadahnDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_VolcanoManorDiseaseCure : {
        "name": "Cure: Serpent Toxin",
        "info": "",
        "caption": "",
        "item_lot": -1,  # TODO
        "bought_flag": SurvivalFlags.Recipe_VolcanoManorDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_LeyndellDiseaseCure : {
        "name": "Cure: Plague of Leyndell",
        "info": "",
        "caption": "",
        "item_lot": -1,  # TODO
        "bought_flag": SurvivalFlags.Recipe_LeyndellDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_SewersDiseaseCure : {
        "name": "Cure: Omen Parasite",
        "info": "",
        "caption": "",
        "item_lot": -1,  # TODO
        "bought_flag": SurvivalFlags.Recipe_SewersDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_HaligtreeDiseaseCure : {
        "name": "Cure: Unalloyed Plague",
        "info": "",
        "caption": "",
        "item_lot": -1,  # TODO
        "bought_flag": SurvivalFlags.Recipe_HaligtreeDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_FarumAzulaDiseaseCure : {
        "name": "Cure: Beastman's Fever",
        "info": "",
        "caption": "",
        "item_lot": -1,  # TODO
        "bought_flag": SurvivalFlags.Recipe_FarumAzulaDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_MohgwynDiseaseCure : {
        "name": "Cure: Blood Lord's Fever",
        "info": "",
        "caption": "",
        "shop_row": 100987,  # Mohgwyn merchant
        "bought_flag": SurvivalFlags.Recipe_MohgwynDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_CatacombsDiseaseCure : {
        "name": "Cure: Catacombs Toxin",
        "info": "",
        "caption": "",
        "item_lot": -1,  # TODO
        "bought_flag": SurvivalFlags.Recipe_CatacombsDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_CaveDiseaseCure : {
        "name": "Cure: Cave Parasite",
        "info": "",
        "caption": "",
        "item_lot": -1,  # TODO
        "bought_flag": SurvivalFlags.Recipe_CaveDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_TunnelDiseaseCure : {
        "name": "Cure: Miner's Fever",
        "info": "",
        "caption": "",
        "item_lot": -1,  # TODO
        "bought_flag": SurvivalFlags.Recipe_TunnelDiseaseCure_Bought,
    },
    # endregion
    # region Survival Recipes
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
    # endregion
    # region Shield Recipes
    NotesRecipes.Recipes_WoodenSmallShields: {
        "name": "Wooden Small Shield Smithbook",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_WoodenSmallShields_Bought,
    },
    NotesRecipes.Recipes_MetalSmallShields: {
        "name": "Metal Small Shield Smithbook",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_MetalSmallShields_Bought,
    },
    NotesRecipes.Recipes_RareSmallShields: {
        "name": "Rare Small Shield Smithbook",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_RareSmallShields_Bought,
    },
    NotesRecipes.Recipes_VeryRareSmallShields: {
        "name": "Very Rare Small Shield Smithbook",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_VeryRareSmallShields_Bought,
    },

    NotesRecipes.Recipes_CommonMediumShields: {
        "name": "Common Medium Shield Smithbook",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_CommonMediumShields_Bought,
    },
    NotesRecipes.Recipes_WoodenMediumShields: {
        "name": "Wooden Medium Shield Smithbook",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_WoodenMediumShields_Bought,
    },
    NotesRecipes.Recipes_HeaterMediumShields: {
        "name": "Heater Medium Shield Smithbook",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_HeaterMediumShields_Bought,
    },
    NotesRecipes.Recipes_KiteMediumShields: {
        "name": "Kite Medium Shield Smithbook",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_KiteMediumShields_Bought,
    },
    NotesRecipes.Recipes_RareMediumShields: {
        "name": "Rare Medium Shield Smithbook",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Recipes_RareMediumShields_Bought,
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
    # endregion
    NotesRecipes.Note_SerpentHunter: {
        "name": "Note: The Serpent-Hunter",
        "info": "",
        "caption": "",
        "bought_flag": SurvivalFlags.Note_SerpentHunter_Bought,
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
