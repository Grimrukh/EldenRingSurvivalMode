from survival_enums import *


class Consumables(IntEnum):
    """New items that can be crafted."""
    # Hunger/thirst relief
    RawSteak = 1900
    SearedSteak = 1901
    RawLiverSteak = 1902
    SearedLiverSteak = 1903
    BoneBroth = 1904
    GreatBoneBroth = 1905
    BloodBroth = 1906
    BerryMedley1 = 1907
    BerryMedley2 = 1908
    BerryMedley3 = 1909
    MushroomStew = 1910
    MeltedMushroomStew = 1911
    DraughtOfSatiation = 1912
    DraughtOfSilverTears = 1913

    # Temperature protection
    MossdewSoup = 1914
    CrystalShardSoup = 1915
    GiantsSoup = 1916
    AmberEyeBrew = 1917
    MagmaticBrew = 1918
    BlossomBrew = 1919
    JarBrittle = 1920
    # TODO: Leaving slots here for more food/drink.

    # Disease cures
    LimgraveDiseaseCure = 1930
    LiurniaDiseaseCure = 1931
    CaelidDiseaseCure = 1932
    AltusDiseaseCure = 1933
    MtGelmirDiseaseCure = 1934
    MountaintopsDiseaseCure = 1935
    SiofraDiseaseCure = 1936
    AinselDiseaseCure = 1937
    DeeprootDiseaseCure = 1938
    StormveilDiseaseCure = 1939
    RayaLucariaDiseaseCure = 1940
    RadahnDiseaseCure = 1941
    VolcanoManorDiseaseCure = 1942
    LeyndellDiseaseCure = 1943
    SewersDiseaseCure = 1944
    HaligtreeDiseaseCure = 1945
    FarumAzulaDiseaseCure = 1946
    MohgwynDiseaseCure = 1947
    CatacombsDiseaseCure = 1948
    CaveDiseaseCure = 1949
    TunnelDiseaseCure = 1950


class Materials(IntEnum):

    # region Smithing Stones (now also used as Materials)
    SmithingStone1 = 10100
    SmithingStone2 = 10101
    SmithingStone3 = 10102
    SmithingStone4 = 10103
    SmithingStone5 = 10104
    SmithingStone6 = 10105
    SmithingStone7 = 10106
    SmithingStone8 = 10107
    AncientDragonSmithingStone = 10108
    SomberSmithingStone1 = 10160
    SomberSmithingStone2 = 10161
    SomberSmithingStone3 = 10162
    SomberSmithingStone4 = 10163
    SomberSmithingStone5 = 10164
    SomberSmithingStone6 = 10165
    SomberSmithingStone7 = 10166
    SomberSmithingStone8 = 10167
    SomberAncientDragonSmithingStone = 10168
    # endregion

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
    LiquidMetal = 21006  # Rare. Used for Nox weapons and weird weapons.
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

    Recipes_CommonSurvival = 9200
    Recipes_UncommonSurvival = 9201
    Recipes_RareSurvival = 9202
    Recipes_VeryRareSurvival = 9203

    Recipes_WoodenSmallShields = 9210
    Recipes_MetalSmallShields = 9211
    Recipes_RareSmallShields = 9212
    Recipes_VeryRareSmallShields = 9213

    Recipes_CommonMediumShields = 9220
    Recipes_WoodenMediumShields = 9221
    Recipes_HeaterMediumShields = 9222
    Recipes_KiteMediumShields = 9223
    Recipes_RareMediumShields = 9224

    Recipes_CommonGreatshields = 9230
    Recipes_UncommonGreatshields = 9231
    Recipes_RareGreatshields = 9232
    Recipes_VeryRareGreatshields = 9233

    Recipes_CommonStaffs = 9240
    Recipes_UncommonStaffs = 9241
    Recipes_RareStaffs = 9242
    Recipes_VeryRareStaffs = 9243

    # Recipes_CommonSeals = 9250  # not used
    Recipes_UncommonSeals = 9251
    Recipes_RareSeals = 9252
    Recipes_VeryRareSeals = 9253

    Recipe_SteelWireTorch = 9260
    Recipe_StTrinasTorch = 9261
    Recipe_GhostflameTorch = 9262
    Recipe_BeastRepellentTorch = 9263
    Recipe_SentrysTorch = 9264


class SmithsHammers(IntEnum):

    # Possession of smithing hammers allows you to reach higher weapon upgrades.
    # Possession of each hammer (after Novice) also unlocks the recipe for the next.
    NoviceSmithsHammer = 8400  # can upgrade from weapons with tier 3-5
    ApprenticeSmithsHammer = 8401  # can upgrade from weapons with tier 6-8
    JourneymanSmithsHammer = 8402  # can upgrade from weapons with tier 9-11
    ExpertSmithsHammer = 8403  # can upgrade from weapons with tier 12-14
    MasterSmithsHammer = 8404  # can upgrade from weapons with tier 15+


class DiseaseIndicators(IntEnum):
    """Disease indicators. These are present in your inventory as Key Items while you have that disease.

    Item lots with the same ID are used to award them.
    """
    LimgraveDisease = 8410
    LiurniaDisease = 8411
    CaelidDisease = 8412
    AltusDisease = 8413
    MtGelmirDisease = 8414
    MountaintopsDisease = 8415
    SiofraDisease = 8416
    AinselDisease = 8417
    DeeprootDisease = 8418
    StormveilDisease = 8419
    RayaLucariaDisease = 8420
    RadahnDisease = 8421
    VolcanoManorDisease = 8422
    LeyndellDisease = 8423
    SewersDisease = 8424
    HaligtreeDisease = 8425
    FarumAzulaDisease = 8426
    MohgwynDisease = 8427
    CatacombsDisease = 8428
    CaveDisease = 8429
    TunnelDisease = 8430


# Keys are offsets used in all IDs.
    # George: I marked things with XXXX that need to be updated.
NEW_CONSUMABLES = {
    # region Survival Consumables
    Consumables.RawSteak: {
        "name": "Raw Steak",
        "info": "Basic raw meal crafted by hunters",
        "caption": "Raw cut of meat prepared from scraps of flesh.\n"
                   "Craftable survival item.\n\n"
                   ""
                   "Consume to relieve hunger, but not without risk.",
        "recipe": [  # for `EquipMtrlSetParam`
            (3, Materials.SliverOfMeat),
        ],
        "recipe_visibility_flag": Flags.Recipes_CommonSurvival_Bought,
        "effect": SurvivalEffects.RawSteak,  # for `EquipGoodsParam`
        "animation": GoodsUseAnimation.ITEM_EATJERKY,  # for `EquipGoodsParam`
        "icon": 19000,
    },
    Consumables.SearedSteak: {
        "name": "Seared Steak",
        "info": "Basic cooked meal crafted by hunters",
        "caption": "Cooked cut of meat prepared from scraps of flesh. Smells delicious.\n"
                   "Craftable survival item.\n\n"
                   ""
                   "Consume to relieve hunger.",
        "recipe": [
            (3, Materials.SliverOfMeat),
            (2, Materials.SmolderingButterfly),
        ],
        "recipe_visibility_flag": Flags.Recipes_CommonSurvival_Bought,
        "effect": SurvivalEffects.SearedSteak,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
        "icon": 19001,
    },
    Consumables.RawLiverSteak: {
        "name": "Raw Liver Steak",
        "info": "Raw meal crafted by expert hunters",
        "caption": "Raw cut of meat prepared from scraps of flesh and liver.\n"
                   "Craftable survival item.\n\n"
                   ""
                   "Consume to relieve hunger, but not without risk.",
        "recipe": [
            (2, Materials.SliverOfMeat),
            (1, Materials.BeastLiver),
        ],
        "recipe_visibility_flag": Flags.Recipes_RareSurvival_Bought,
        "effect": SurvivalEffects.RawLiverSteak,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
        "icon": 19002,
    },
    Consumables.SearedLiverSteak: {
        "name": "Seared Liver Steak",
        "info": "Cooked meal crafted by expert hunters",
        "caption": "Cooked cut of meat prepared from scraps of flesh and liver. Smells delicious.\n"
                   "Craftable survival item.\n\n"
                   ""
                   "Consume to relieve hunger.",
        "recipe": [
            (2, Materials.SliverOfMeat),
            (1, Materials.BeastLiver),
            (2, Materials.SmolderingButterfly),
        ],
        "recipe_visibility_flag": Flags.Recipes_RareSurvival_Bought,
        "effect": SurvivalEffects.SearedLiverSteak,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
        "icon": 19003,
    },
    Consumables.BoneBroth: {
        "name": "Bone Broth",
        "info": "Light broth to ward off thirst",
        "caption": "Delicious broth prepared from bones.\n"
                   "Craftable survival item.\n\n"
                   ""
                   "Consume to relieve thirst.",
        "recipe": [
            (5, Materials.ThinBeastBones),
        ],
        "recipe_visibility_flag": Flags.Recipes_CommonSurvival_Bought,
        "effect": SurvivalEffects.BoneBroth,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
        "icon": 19004,
    },
    Consumables.GreatBoneBroth: {
        "name": "Great Bone Broth",
        "info": "Hearty broth to ward off thirst",
        "caption": "Delicious hearty broth prepared from large bones.\n"
                   "Craftable survival item.\n\n"
                   ""
                   "Consume to relieve thirst.",
        "recipe": [
            (3, Materials.HeftyBeastBone),
        ],
        "recipe_visibility_flag": Flags.Recipes_UncommonSurvival_Bought,
        "effect": SurvivalEffects.GreatBoneBroth,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
        "icon": 19005,
    },
    Consumables.BloodBroth: {
        "name": "Blood Broth",
        "info": "Broth preferred by bloodthirsty hunters",
        "caption": "Odorous broth prepared from bones and blood. A delicacy, for some.\n"
                   "Craftable survival item.\n\n"
                   ""
                   "Consume to relieve thirst and temporarily boost attack and lower defense.",
        "recipe": [
            (3, Materials.ThinBeastBones),
            (2, Materials.BeastBlood),
        ],
        "recipe_visibility_flag": Flags.Recipes_RareSurvival_Bought,
        "effect": SurvivalEffects.BloodBroth,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
        "icon": 19006,
    },
    Consumables.BerryMedley1: {
        "name": "Forest Berry Medley",
        "info": "Medley of berries from the lower lands",
        "caption": "Prepared fruits picked from rowa shrubs. Tannic, but delicious.\n"
                   "Craftable survival item.\n\n"
                   ""
                   "Consume to relieve hunger and thirst.",
        "recipe": [
            (10, Materials.RowaFruit),
        ],
        "recipe_visibility_flag": Flags.Recipes_CommonSurvival_Bought,
        "effect": SurvivalEffects.BerryMedley1,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
        "icon": 19007,
    },
    Consumables.BerryMedley2: {
        "name": "Plateau Berry Medley",
        "info": "Medley of berries from the plateau",
        "caption": "Prepared fruits picked from golden rowa shrubs. Sweet and delicious.\n"
                   "Craftable survival item.\n\n"
                   ""
                   "Consume to relieve hunger and thirst.",
        "recipe": [
            (10, Materials.GoldenRowa),
        ],
        "recipe_visibility_flag": Flags.Recipes_UncommonSurvival_Bought,
        "effect": SurvivalEffects.BerryMedley2,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
        "icon": 19008,
    },
    Consumables.BerryMedley3: {
        "name": "Mountain Berry Medley",
        "info": "Medley of berries from the mountains",
        "caption": "Prepared fruits picked from rimed rowa shrubs. Slightly bitter, but uniquely delicious.\n"
                   "Craftable survival item.\n\n"
                   ""
                   "Consume to relieve hunger and thirst.",
        "recipe": [
            (10, Materials.RimedRowa),
        ],
        "recipe_visibility_flag": Flags.Recipes_RareSurvival_Bought,
        "effect": SurvivalEffects.BerryMedley3,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
        "icon": 19009,
    },
    Consumables.MushroomStew: {
        "name": "Mushroom Stew",
        "info": "Basic mushroom stew",
        "caption": "Simple, but tasty stew prepared from mushrooms and herba.\n"
                   "Craftable survival item.\n\n"
                   ""
                   "Consume to relieve hunger and thirst.",
        "recipe": [
            (3, Materials.Mushroom),
            (3, Materials.Herba),
        ],
        "recipe_visibility_flag": Flags.Recipes_CommonSurvival_Bought,
        "effect": SurvivalEffects.MushroomStew,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
        "icon": 19010,
    },
    Consumables.MeltedMushroomStew: {
        "name": "Melted Mushroom Stew",
        "info": "Thick mushroom stew",
        "caption": "Thick stew prepared from mushrooms and herba. Unusual texture, but incredible taste.\n"
                   "Craftable survival item.\n\n"
                   ""
                   "Consume to relieve hunger and thirst.",
        "recipe": [
            (3, Materials.MeltedMushroom),
            (3, Materials.DewkissedHerba),
        ],
        "recipe_visibility_flag": Flags.Recipes_UncommonSurvival_Bought,
        "effect": SurvivalEffects.MeltedMushroomStew,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
        "icon": 19011,
    },
    Consumables.DraughtOfSatiation: {
        "name": "Draught of Satiation",
        "info": "Prevents hunter temporarily",
        "caption": "Outlawed concoction once consumed by those seeking to reunite with the dead. Smells terrible.\n"
                   "Craftable survival item.\n\n"
                   ""
                   "Consume to relieve hunger and prevent it from growing temporarily.",
        "recipe": [
            (5, Materials.GraveViolet),
            (3, Materials.CrabEggs),
            (3, Materials.BloodTaintedExcrement),
            (2, Materials.MirandaPowder),
        ],
        "recipe_visibility_flag": Flags.Recipes_VeryRareSurvival_Bought,
        "effect": SurvivalEffects.DraughtOfSatiation,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
        "icon": 19012,
    },
    Consumables.DraughtOfSilverTears: {
        "name": "Draught of Silver Tears",
        "info": "Prevents thirst temporarily",
        "caption": "Outlawed concotion once consumed in a ritual of the Eternal City. Smells awful.\n"
                   "Craftable survival item.\n\n"
                   ""
                   "Consume to relieve thirst and prevent it from growing temporarily.",
        "recipe": [
            (7, Materials.SilverTearHusk),
            (3, Materials.LandOctopusOvary),
            (3, Materials.RimedRowa),
            (2, Materials.AeonianButterfly),
        ],
        "recipe_visibility_flag": Flags.Recipes_VeryRareSurvival_Bought,
        "effect": SurvivalEffects.DraughtOfSilverTears,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
        "icon": 19013,
    },
    Consumables.MossdewSoup: {
        "name": "Mossdew Soup",
        "info": "Soup with mild heat protection",
        "caption": "Simple medicinal soup. Tastes very bitter.\n"
                   "Craftable survival item.\n\n"
                   ""
                   "Consume for mild protection from heat, which may otherwise drain away health.",
        "recipe": [
            (3, Materials.CaveMoss),
            (4, Materials.DewkissedHerba),
        ],
        "recipe_visibility_flag": Flags.Recipes_CommonSurvival_Bought,
        "effect": SurvivalEffects.MossdewSoup,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
        "icon": 19014,
    },
    Consumables.CrystalShardSoup: {
        "name": "Crystal Shard Soup",
        "info": "Soup with moderate heat protection",
        "caption": "Complex medicinal soup. Tastes slightly sweet.\n"
                   "Craftable survival item.\n\n"
                   ""
                   "Consume for moderate protection from heat, which may otherwise drain away health.",
        "recipe": [
            (2, Materials.BuddingCaveMoss),
            (5, Materials.CrackedCrystal),
        ],
        "recipe_visibility_flag": Flags.Recipes_UncommonSurvival_Bought,
        "effect": SurvivalEffects.CrystalShardSoup,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
        "icon": 19015,
    },
    Consumables.GiantsSoup: {
        "name": "Giant's Soup",
        "info": "Soup with great heat protection",
        "caption": "Masterful medicinal soup. Tastes pretty good.\n"
                   "Craftable survival item.\n\n"
                   ""
                   "Consume for great protection from heat, which may otherwise drain away health.",
        "recipe": [
            (5, Materials.RimedRowa),
            (2, Materials.CrystalCaveMoss),
            (2, Materials.RimedCrystalBud),
        ],
        "recipe_visibility_flag": Flags.Recipes_RareSurvival_Bought,
        "effect": SurvivalEffects.GiantsSoup,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
        "icon": 19016,
    },
    Consumables.AmberEyeBrew: {
        "name": "Amber-Eye Brew",
        "info": "Brew with mild cold protection",
        "caption": "Simple medicinal brew. Rather intoxicating.\n"
                   "Craftable survival item.\n\n"
                   ""
                   "Consume for mild protection from the cold, which may otherwise cripple.",
        "recipe": [
            (3, Materials.EyeOfYelough),
            (1, Materials.YellowEmber),
            (3, Materials.Herba),
        ],
        "recipe_visibility_flag": Flags.Recipes_CommonSurvival_Bought,
        "effect": SurvivalEffects.AmberEyeBrew,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
        "icon": 19017,
    },
    Consumables.MagmaticBrew: {
        "name": "Magmatic Brew",
        "info": "Brew with moderate cold protection",
        "caption": "Complex medicinal brew. Makes your tongue feel like it's on fire!\n"
                   "Craftable survival item.\n\n"
                   ""
                   "Consume for moderate protection from the cold, which may otherwise cripple.",
        "recipe": [
            (4, Materials.VolcanicStone),
            (3, Materials.TarnishedGoldenSunflower),
        ],
        "recipe_visibility_flag": Flags.Recipes_UncommonSurvival_Bought,
        "effect": SurvivalEffects.MagmaticBrew,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
        "icon": 19018,
    },
    Consumables.BlossomBrew: {
        "name": "Blossom Brew",
        "info": "Brew with great cold protection",
        "caption": "Masterful medicinal brew. Very acidic, and strangely addictive.\n"
                   "Craftable survival item.\n\n"
                   ""
                   "Consume for great protection from the cold, which may otherwise cripple.",
        "recipe": [
            (5, Materials.FireBlossom),
            (3, Materials.FormicRock),
        ],
        "recipe_visibility_flag": Flags.Recipes_RareSurvival_Bought,
        "effect": SurvivalEffects.BlossomBrew,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
        "icon": 19019,
    },
    Consumables.JarBrittle: {
        "name": "Jar Brittle",
        "info": "Crunchy brittle from living jars",
        "caption": "Aberrant food prepared from the flesh of living jars.\n"
                   "Most find it abhorrent, but others swear it has a taste like no other.\n"
                   "Craftable survival item.\n\n"
                   ""
                   "Consume to relieve hunger and gain mild heat & cold protection.\n"
                   "However, it increases thirst.",
        "recipe": [
            (5, Materials.LivingJarShard),
        ],
        "recipe_visibility_flag": Flags.Recipes_RareSurvival_Bought,
        "effect": SurvivalEffects.JarBrittle,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
        "icon": 19020,
    },
    # endregion

    # TODO: Leaving slots 21-29 here for more food/drink items.

    # region Disease Cures
    Consumables.LimgraveDiseaseCure: {
        "name": "Cure for Plague of Limgrave",
        "info": "",
        "caption": "",
        "recipe": [
            (10, Materials.RowaFruit),
            (8, Materials.Poisonbloom),
            (8, Materials.CaveMoss),
            (6, Materials.CrabEggs),
        ],
        "recipe_visibility_flag": Flags.Recipe_LimgraveDiseaseCure_Bought,
        "effect": SurvivalEffects.CureLimgraveDisease,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "icon": 24,  # Flask of Wondrous Physick
    },
    Consumables.LiurniaDiseaseCure: {
        "name": "Cure for Lake Toxin",
        "info": "",
        "caption": "",
        "recipe": [
            (13, Materials.Mushroom),
            (12, Materials.SilverFirefly),
            (5, Materials.BuddingCaveMoss),
            (5, Materials.AlbinauricBloodclot),
        ],
        "recipe_visibility_flag": Flags.Recipe_LiurniaDiseaseCure_Bought,
        "effect": SurvivalEffects.CureLiurniaDisease,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "icon": 24,  # Flask of Wondrous Physick
    },
    Consumables.CaelidDiseaseCure: {
        "name": "Cure for Scarlet Parasite",
        "info": "",
        "caption": "",
        "recipe": [
            (15, Materials.FadedErdleafFlower),
            (11, Materials.ToxicMushroom),
            (7, Materials.BuddingCaveMoss),
            (7, Materials.SacramentalBud),
        ],
        "recipe_visibility_flag": Flags.Recipe_CaelidDiseaseCure_Bought,
        "effect": SurvivalEffects.CureCaelidDisease,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "icon": 24,  # Flask of Wondrous Physick
    },
    Consumables.AltusDiseaseCure: {
        "name": "Cure for Windmill Fever",
        "info": "",
        "caption": "",
        "recipe": [
            (20, Materials.AltusBloom),
            (10, Materials.GoldenSunflower),
            (10, Materials.Fulgurbloom),
            (7, Materials.NascentButterfly),
        ],
        "recipe_visibility_flag": Flags.Recipe_AltusDiseaseCure_Bought,
        "effect": SurvivalEffects.CureAltusDisease,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "icon": 24,  # Flask of Wondrous Physick
    },
    Consumables.MtGelmirDiseaseCure: {
        "name": "Cure for Plague of Gelmir",
        "info": "",
        "caption": "",
        "recipe": [
            (18, Materials.GoldenRowa),
            (15, Materials.MeltedMushroom),
            (9, Materials.MiquellasLily),
            (4, Materials.FormicRock),
        ],
        "recipe_visibility_flag": Flags.Recipe_MtGelmirDiseaseCure_Bought,
        "effect": SurvivalEffects.CureMtGelmirDisease,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "icon": 24,  # Flask of Wondrous Physick
    },
    Consumables.MountaintopsDiseaseCure: {
        "name": "Cure for Frigid Parasite",
        "info": "",
        "caption": "",
        "recipe": [
            (20, Materials.VolcanicStone),
            (15, Materials.DewkissedHerba),
            (10, Materials.CrystalCaveMoss),
            (5, Materials.AeonianButterfly),
        ],
        "recipe_visibility_flag": Flags.Recipe_MountaintopsDiseaseCure_Bought,
        "effect": SurvivalEffects.CureMountaintopsDisease,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "icon": 24,  # Flask of Wondrous Physick
    },
    Consumables.SiofraDiseaseCure: {
        "name": "Cure for Plague of Nokron",
        "info": "",
        "caption": "",
        "recipe": [
            (15, Materials.TarnishedGoldenSunflower),
            (12, Materials.CrystalBud),
            (10, Materials.CaveMoss),
            (6, Materials.MirandaPowder),
        ],
        "recipe_visibility_flag": Flags.Recipe_SiofraDiseaseCure_Bought,
        "effect": SurvivalEffects.CureSiofraDisease,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "icon": 24,  # Flask of Wondrous Physick
    },
    Consumables.AinselDiseaseCure: {
        "name": "Cure for Ant Toxin",
        "info": "",
        "caption": "",
        "recipe": [
            (30, Materials.Herba),
            (10, Materials.LandOctopusOvary),
            (8, Materials.NascentButterfly),
            (5, Materials.RimedCrystalBud),
        ],
        "recipe_visibility_flag": Flags.Recipe_AinselDiseaseCure_Bought,
        "effect": SurvivalEffects.CureAinselDisease,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "icon": 24,  # Flask of Wondrous Physick
    },
    Consumables.DeeprootDiseaseCure: {
        "name": "Cure for Star-Shaped Parasite",
        "info": "",
        "caption": "",
        "recipe": [
            (25, Materials.SmolderingButterfly),
            (12, Materials.CrystalCaveMoss),
            (10, Materials.FourToedFowlFoot),
            (10, Materials.CrabEggs),
        ],
        "recipe_visibility_flag": Flags.Recipe_DeeprootDiseaseCure_Bought,
        "effect": SurvivalEffects.CureDeeprootDisease,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "icon": 24,  # Flask of Wondrous Physick
    },
    Consumables.StormveilDiseaseCure: {
        "name": "Cure for Grafted Plague",
        "info": "",
        "caption": "",
        "recipe": [
            (20, Materials.ErdleafFlower),
            (12, Materials.CaveMoss),
            (10, Materials.FlightPinion),
            (10, Materials.Poisonbloom),
        ],
        "recipe_visibility_flag": Flags.Recipe_StormveilDiseaseCure_Bought,
        "effect": SurvivalEffects.CureStormveilDisease,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "icon": 24,  # Flask of Wondrous Physick
    },
    Consumables.RayaLucariaDiseaseCure: {
        "name": "Cure for Full Moon Fever",
        "info": "",
        "caption": "",
        "recipe": [
            (10, Materials.CrystalBud),
            (12, Materials.TrinasLily),
            (7, Materials.ArteriaLeaf),
            (7, Materials.FormicRock),
        ],
        "recipe_visibility_flag": Flags.Recipe_RayaLucariaDiseaseCure_Bought,
        "effect": SurvivalEffects.CureRayaLucariaDisease,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "icon": 24,  # Flask of Wondrous Physick
    },
    Consumables.RadahnDiseaseCure: {
        "name": "Cure for Starscourge Fever",
        "info": "",
        "caption": "",
        "recipe": [
            (20, Materials.SilverTearHusk),
            (15, Materials.MeltedMushroom),
            (9, Materials.TrinasLily),
            (5, Materials.GravelStone),
        ],
        "recipe_visibility_flag": Flags.Recipe_RadahnDiseaseCure_Bought,
        "effect": SurvivalEffects.CureRadahnDisease,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "icon": 24,  # Flask of Wondrous Physick
    },
    Consumables.VolcanoManorDiseaseCure: {
        "name": "Cure for Serpent Toxin",
        "info": "",
        "caption": "",
        "recipe": [
            (20, Materials.Fulgurbloom),
            (12, Materials.GoldTingedExcrement),
            (9, Materials.ArteriaLeaf),
            (5, Materials.FormicRock),
        ],
        "recipe_visibility_flag": Flags.Recipe_VolcanoManorDiseaseCure_Bought,
        "effect": SurvivalEffects.CureVolcanoManorDisease,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "icon": 24,  # Flask of Wondrous Physick
    },
    Consumables.LeyndellDiseaseCure: {
        "name": "Cure for Plague of Leyndell",
        "info": "",
        "caption": "",
        "recipe": [
            (12, Materials.SacramentalBud),
            (10, Materials.FourToedFowlFoot),
            (10, Materials.StormhawkFeather),
            (5, Materials.GoldenCentipede),
        ],
        "recipe_visibility_flag": Flags.Recipe_LeyndellDiseaseCure_Bought,
        "effect": SurvivalEffects.CureLeyndellDisease,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "icon": 24,  # Flask of Wondrous Physick
    },
    Consumables.SewersDiseaseCure: {
        "name": "Cure for Omen Parasite",
        "info": "",
        "caption": "",
        "recipe": [
            (30, Materials.Mushroom),
            (10, Materials.FireBlossom),
            (10, Materials.MirandaPowder),
            (8, Materials.LandOctopusOvary),
        ],
        "recipe_visibility_flag": Flags.Recipe_SewersDiseaseCure_Bought,
        "effect": SurvivalEffects.CureSewersDisease,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "icon": 24,  # Flask of Wondrous Physick
    },
    Consumables.HaligtreeDiseaseCure: {
        "name": "Cure for Unalloyed Plague",
        "info": "",
        "caption": "",
        "recipe": [
            (15, Materials.MiquellasLily),
            (10, Materials.ArteriaLeaf),
            (10, Materials.BloodTaintedExcrement),
            (10, Materials.AlbinauricBloodclot),
        ],
        "recipe_visibility_flag": Flags.Recipe_HaligtreeDiseaseCure_Bought,
        "effect": SurvivalEffects.CureHaligtreeDisease,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "icon": 24,  # Flask of Wondrous Physick
    },
    Consumables.FarumAzulaDiseaseCure: {
        "name": "Cure for Beastman's Fever",
        "info": "",
        "caption": "",
        "recipe": [
            (20, Materials.GoldFirefly),
            (15, Materials.CrystalCaveMoss),
            (15, Materials.FlightPinion),
            (10, Materials.GravelStone),
        ],
        "recipe_visibility_flag": Flags.Recipe_FarumAzulaDiseaseCure_Bought,
        "effect": SurvivalEffects.CureFarumAzulaDisease,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "icon": 24,  # Flask of Wondrous Physick
    },
    Consumables.MohgwynDiseaseCure: {
        "name": "Cure for Blood Lord's Fever",
        "info": "",
        "caption": "",
        "recipe": [
            (20, Materials.ThinBeastBones),
            (20, Materials.HeftyBeastBone),
            (20, Materials.BeastLiver),
            (20, Materials.BeastBlood),
        ],
        "recipe_visibility_flag": Flags.Recipe_MohgwynDiseaseCure_Bought,
        "effect": SurvivalEffects.CureMohgwynDisease,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "icon": 24,  # Flask of Wondrous Physick
    },
    Consumables.CatacombsDiseaseCure: {
        "name": "Cure for Catacombs Toxin",
        "info": "",
        "caption": "",
        "recipe": [
            (20, Materials.CaveMoss),
            (15, Materials.TarnishedGoldenSunflower),
            (10, Materials.MeltedMushroom),
            (8, Materials.BeastLiver),
        ],
        "recipe_visibility_flag": Flags.Recipe_CatacombsDiseaseCure_Bought,
        "effect": SurvivalEffects.CureCatacombsDisease,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "icon": 24,  # Flask of Wondrous Physick
    },
    Consumables.CaveDiseaseCure: {
        "name": "Cure for Cave Parasite",
        "info": "",
        "caption": "",
        "recipe": [
            (10, Materials.FlightPinion),
            (10, Materials.FadedErdleafFlower),
            (5, Materials.ArteriaLeaf),
            (5, Materials.CrystalBud),
        ],
        "recipe_visibility_flag": Flags.Recipe_CaveDiseaseCure_Bought,
        "effect": SurvivalEffects.CureCaveDisease,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "icon": 24,  # Flask of Wondrous Physick
    },
    Consumables.TunnelDiseaseCure: {
        "name": "Cure for Miner's Fever",
        "info": "",
        "caption": "",
        "recipe": [
            (15, Materials.ThinBeastBones),
            (10, Materials.GoldTingedExcrement),
            (10, Materials.DewkissedHerba),
            (7, Materials.BeastBlood),
        ],
        "recipe_visibility_flag": Flags.Recipe_TunnelDiseaseCure_Bought,
        "effect": SurvivalEffects.CureTunnelDisease,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "icon": 24,  # Flask of Wondrous Physick
    },
    # endregion
}


NEW_MATERIALS = {
    Materials.SoftWood: {
        "name": "Soft Wood",
        "info": "Unremarkable piece of wood",
        "caption": "Inferior quality wood, fit for cinder.\nCommon material for crafting weapons and shields.\n",
        "icon": 19036,
    },
    Materials.RefinedWood: {
        "name": "Refined Wood",
        "info": "Robust piece of wood",
        "caption": "Superior quality wood that has been treated.\nMaterial for crafting weapons and shields.\n",
        "icon": 19037,
    },
    Materials.StoneFragment: {
        "name": "Stone Fragment",
        "info": "Fragment of simple colored stone",
        "caption": "Fragment of an extremely durable stone.\nMaterial for crafting weapons and shields.\n",
        "icon": 19038,
    },
    Materials.SomberStoneFragment: {
        "name": "Somber Stone Fragment",
        "info": "Fragment of rare colorless stone",
        "caption": "Fragment of an extremely durable white stone.\nMaterial for crafting weapons and shields.\n",
        "icon": 19039,
    },
    Materials.IronShards: {
        "name": "Metal Shards",
        "info": "Shards of metal for forging",
        "caption": "Shards of metal that came from a larger piece.\nMaterial for crafting weapons and shields.\n",
        "icon": 19040,
    },
    Materials.IronPlate: {
        "name": "Metal Plate",
        "info": "Sheet of metal for forging",
        "caption": "Sheet of metal perfect for forging metal weapons.\nMaterial for crafting weapons and shields.\n",
        "icon": 19041,
    },
    Materials.LiquidMetal: {
        "name": "Pliable Metal",
        "info": "Rare metal used for forging",
        "caption": "Prized metal that bends, but never breaks.\nMaterial for crafting weapons and shields.\n",
        "icon": 19042,
    },
    Materials.DragonTeeth: {
        "name": "Dragon Teeth",
        "info": "Collection of small dragon teeth",
        "caption": "Small dragon teeth with latent power, perfect for forging dragon weapons.\n"
                   "Material for crafting weapons and shields.\n"
                   "",  #\nSuch small teeth for such large beasts... perhaps draconic youth shed their teeth?
        "icon": 19043,
    },
    Materials.GruesomeBone: {
        "name": "Gruesome Bone",
        "info": "Disgusting large bone used for forging",
        "caption": "Very large, disturbing bone prized by arcane smiths for its unique properties.\n"
                   "Material for crafting weapons and shields.\n"
                   "",  #\nSome try these bones to their stock out of hunger.
        "icon": 19044,
    },
    Materials.ErdtreeWood: {
        "name": "Erdtree Wood",
        "info": "Holy wood from the Erdtree",
        "caption": "Wood highly prized by craftsmen. Very light, but quite tough.\n"
                   "Material for crafting weapons and shields.\n",
        "icon": 19045,
    },
    Materials.MeteoriteChunk: {
        "name": "Meteorite Chunk",
        "info": "Dense chunk of cosmic debris",
        "caption": "Very heavy chunk of metal of cosmic origin.\nMaterial for crafting weapons and shields.\n",
        "icon": 19046,
    },
    Materials.BlackMark: {
        "name": "Black Mark",
        "info": "Residue from the stolen Rune of Death",
        "caption": "Faint remnant of death scattered when the Rune of Death was stolen\nMaterial for crafting weapons and shields.\n",
        "icon": 19047,
    },
    Materials.StaffPole: {
        "name": "Staff Pole",
        "info": "Wooden staff perfect for a magic catalyst",
        "caption": "Intricately prepared wooden staff perfect for creating a catalyst.\nMaterial for crafting weapons and shields.\n",
        "icon": 19048,
    },
    Materials.ShieldGrip: {
        "name": "Shield Handle",
        "info": "Sturdy handle perfect for a shield",
        "caption": "Heavy-duty handle designed to withstand large impacts, perfect for any shield.\nMaterial for crafting weapons and shields.\n",
        "icon": 19049,
    },
    Materials.ErdtreeAmber: {
        "name": "Erdtree Amber",
        "info": "Amber formed from the Erdtree's resin",
        "caption": "Holy amber that came from Erdtree resin, a highly sought-after material.\nMaterial for crafting weapons and shields.\n",
        "icon": 19050,
    },
    Materials.GlintstoneDust: {
        "name": "Glintstone Dust",
        "info": "Fine grains of purified Glintstone",
        "caption": "Small amount of purified glintstone, ground into a powder specifically for crafting.\nMaterial for crafting weapons and shields.\n",
        "icon": 19051,
    },
}


NEW_SMITHS_HAMMERS = {
    SmithsHammers.NoviceSmithsHammer: {
        "name": "Novice Smith's Hammer",
        "info": "",
        "caption": "",
        "icon": 10407,  # Hammer weapon
        "recipe_visibility_flag": 0,  # always craftable
        "recipe": [
            (6, Materials.SmithingStone1),
            (6, Materials.SmithingStone2),
            (3, Materials.SomberSmithingStone1),
            (3, Materials.SomberSmithingStone2),
        ],
    },
    SmithsHammers.ApprenticeSmithsHammer: {
        "name": "Apprentice Smith's Hammer",
        "info": "",
        "caption": "",
        "icon": 10407,  # Hammer weapon
        "recipe_visibility_flag": Flags.HasNoviceSmithsHammer,
        "recipe": [
            (6, Materials.SmithingStone3),
            (6, Materials.SmithingStone4),
            (3, Materials.SomberSmithingStone3),
            (3, Materials.SomberSmithingStone4),
        ],
    },
    SmithsHammers.JourneymanSmithsHammer: {
        "name": "Journeyman Smith's Hammer",
        "info": "",
        "caption": "",
        "icon": 10407,  # Hammer weapon
        "recipe_visibility_flag": Flags.HasApprenticeSmithsHammer,
        "recipe": [
            (6, Materials.SmithingStone5),
            (6, Materials.SmithingStone6),
            (3, Materials.SomberSmithingStone5),
            (3, Materials.SomberSmithingStone6),
        ],
    },
    SmithsHammers.ExpertSmithsHammer: {
        "name": "Expert Smith's Hammer",
        "info": "",
        "caption": "",
        "icon": 10407,  # Hammer weapon
        "recipe_visibility_flag": Flags.HasJourneymanSmithsHammer,
        "recipe": [
            (6, Materials.SmithingStone7),
            (6, Materials.SmithingStone8),
            (3, Materials.SomberSmithingStone7),
            (3, Materials.SomberSmithingStone8),
        ],
    },
    SmithsHammers.MasterSmithsHammer: {
        "name": "Master Smith's Hammer",
        "info": "",
        "caption": "",
        "icon": 10414,  # Marika's Hammer weapon
        "recipe_visibility_flag": Flags.HasExpertSmithsHammer,
        "recipe": [
            (1, Materials.AncientDragonSmithingStone),
            (1, Materials.SomberAncientDragonSmithingStone),
            (1, Materials.MeteoriteChunk),
            (1, Materials.ErdtreeAmber),
        ],
    },
}

DISEASE_INDICATORS = {
    DiseaseIndicators.LimgraveDisease: {
        "name": "Disease: Plague of Limgrave",
        "info": "",
        "caption": "",
        "icon": 3739,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.LiurniaDisease: {
        "name": "Disease: Lake Toxin",
        "info": "",
        "caption": "",
        "icon": 3735,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.CaelidDisease: {
        "name": "Disease: Scarlet Parasite",
        "info": "",
        "caption": "",
        "icon": 3736,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.AltusDisease: {
        "name": "Disease: Windmill Fever",
        "info": "",
        "caption": "",
        "icon": 3734,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.MtGelmirDisease: {
        "name": "Disease: Plague of Gelmir",
        "info": "",
        "caption": "",
        "icon": 3739,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.MountaintopsDisease: {
        "name": "Disease: Frigid Parasite",
        "info": "",
        "caption": "",
        "icon": 3736,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.SiofraDisease: {
        "name": "Disease: Plague of Nokron",
        "info": "",
        "caption": "",
        "icon": 3739,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.AinselDisease: {
        "name": "Disease: Ant Toxin",
        "info": "",
        "caption": "",
        "icon": 3735,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.DeeprootDisease: {
        "name": "Disease: Star-Shaped Parasite",
        "info": "",
        "caption": "",
        "icon": 3736,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.StormveilDisease: {
        "name": "Disease: Grafted Plague",
        "info": "",
        "caption": "",
        "icon": 3739,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.RayaLucariaDisease: {
        "name": "Disease: Full Moon Fever",
        "info": "",
        "caption": "",
        "icon": 3734,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.RadahnDisease: {
        "name": "Disease: Starscourge Fever",
        "info": "",
        "caption": "",
        "icon": 3734,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.VolcanoManorDisease: {
        "name": "Disease: Serpent Toxin",
        "info": "",
        "caption": "",
        "icon": 3735,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.LeyndellDisease: {
        "name": "Disease: Plague of Leyndell",
        "info": "",
        "caption": "",
        "icon": 3739,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.SewersDisease: {
        "name": "Disease: Omen Parasite",
        "info": "",
        "caption": "",
        "icon": 3736,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.HaligtreeDisease: {
        "name": "Disease: Unalloyed Plague",
        "info": "",
        "caption": "",
        "icon": 3739,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.FarumAzulaDisease: {
        "name": "Disease: Beastman's Fever",
        "info": "",
        "caption": "",
        "icon": 3734,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.MohgwynDisease: {
        "name": "Disease: Blood Lord's Fever",
        "info": "",
        "caption": "",
        "icon": 3734,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.CatacombsDisease: {
        "name": "Disease: Catacombs Toxin",
        "info": "",
        "caption": "",
        "icon": 3735,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.CaveDisease: {
        "name": "Disease: Cave Parasite",
        "info": "",
        "caption": "",
        "icon": 3736,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.TunnelDisease: {
        "name": "Disease: Miner's Fever",
        "info": "",
        "caption": "",
        "icon": 3734,  # faded skull in Icon_02_A
    },
}


NEW_NOTES_RECIPES = {
    # region Disease Cures
    NotesRecipes.Note_CuringDiseases : {
        "name": "Note: Finding Disease Cures",
        "info": "",
        "caption": "",
        "icon": 298,  # Note: Hidden Cave
        "shop_row": 100509,  # Kale
        "cost": 200,
        "bought_flag": Flags.Note_CuringDiseases_Bought,
    },
    NotesRecipes.Recipe_LimgraveDiseaseCure : {
        "name": "Cure: Plague of Limgrave",
        "info": "",
        "caption": "",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "shop_row": 100596,  # Coastal Cave merchant
        "cost": 2000,
        "bought_flag": Flags.Recipe_LimgraveDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_LiurniaDiseaseCure : {
        "name": "Cure: Lake Toxin",
        "info": "",
        "caption": "",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "shop_row": 100697,  # Academy of Raya Lucaria merchant
        "cost": 3000,
        "bought_flag": Flags.Recipe_LiurniaDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_CaelidDiseaseCure : {
        "name": "Cure: Scarlet Parasite",
        "info": "",
        "caption": "",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "shop_row": 100894,  # Dragonbarrow merchant
        "cost": 4000,
        "bought_flag": Flags.Recipe_CaelidDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_AltusDiseaseCure : {
        "name": "Cure: Windmill Fever",
        "info": "",
        "caption": "",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "shop_row": 100756,  # Altus Plateau merchant
        "cost": 4000,
        "bought_flag": Flags.Recipe_AltusDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_MtGelmirDiseaseCure : {
        "name": "Cure: Plague of Gelmir",
        "info": "",
        "caption": "",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "shop_row": 100799,  # Mt. Gelmir merchant
        "cost": 4000,
        "bought_flag": Flags.Recipe_MtGelmirDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_MountaintopsDiseaseCure : {
        "name": "Cure: Frigid Parasite",
        "info": "",
        "caption": "",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "shop_row": 100919,  # Mountaintops merchant
        "cost": 5000,
        "bought_flag": Flags.Recipe_MountaintopsDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_SiofraDiseaseCure : {
        "name": "Cure: Plague of Nokron",
        "info": "",
        "caption": "",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "shop_row": 100942,  # Siofra merchant
        "cost": 2000,
        "bought_flag": Flags.Recipe_SiofraDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_AinselDiseaseCure : {
        "name": "Cure: Ant Toxin",
        "info": "",
        "caption": "",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "shop_row": 100968,  # Ainsel merchant
        "cost": 3000,
        "bought_flag": Flags.Recipe_AinselDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_DeeprootDiseaseCure : {
        "name": "Cure: Star-Shaped Parasite",
        "info": "",
        "caption": "",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lot": 12030521,  # with Mausoleum Soldier Ashes
        "bought_flag": Flags.Recipe_DeeprootDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_StormveilDiseaseCure : {
        "name": "Cure: Grafted Plague",
        "info": "",
        "caption": "",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lot": 10000991,  # with Godskin Prayerbook
        "bought_flag": Flags.Recipe_StormveilDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_RayaLucariaDiseaseCure : {
        "name": "Cure: Full Moon Fever",
        "info": "",
        "caption": "",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lot": 14000941,  # with Radagon Icon
        "bought_flag": Flags.Recipe_RayaLucariaDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_RadahnDiseaseCure : {
        "name": "Cure: Starscourge Fever",
        "info": "",
        "caption": "",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lot": 30160041,  # with Collapsing Stars (in War-Dead Catacombs)
        "bought_flag": Flags.Recipe_RadahnDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_VolcanoManorDiseaseCure : {
        "name": "Cure: Serpent Toxin",
        "info": "",
        "caption": "",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lot": 16000621,  # with Dagger Talisman
        "bought_flag": Flags.Recipe_VolcanoManorDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_LeyndellDiseaseCure : {
        "name": "Cure: Plague of Leyndell",
        "info": "",
        "caption": "",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lot": 11000911,  # with Golden Order Principia
        "bought_flag": Flags.Recipe_LeyndellDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_SewersDiseaseCure : {
        "name": "Cure: Omen Parasite",
        "info": "",
        "caption": "",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lot": 35000271,  # with Nomad Ashes
        "bought_flag": Flags.Recipe_SewersDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_HaligtreeDiseaseCure : {
        "name": "Cure: Unalloyed Plague",
        "info": "",
        "caption": "",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lot": 15000801,  # with Marika's Soreseal
        "bought_flag": Flags.Recipe_HaligtreeDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_FarumAzulaDiseaseCure : {
        "name": "Cure: Beastman's Fever",
        "info": "",
        "caption": "",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lot": 13000941,  # with Dragon Towershield
        "bought_flag": Flags.Recipe_FarumAzulaDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_MohgwynDiseaseCure : {
        "name": "Cure: Blood Lord's Fever",
        "info": "",
        "caption": "",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "shop_row": 100987,  # Mohgwyn merchant
        "cost": 10000,
        "bought_flag": Flags.Recipe_MohgwynDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_CatacombsDiseaseCure : {
        "name": "Cure: Catacombs Toxin",
        "info": "",
        "caption": "",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lots": [  # Catacombs boss rewards after Limgrave
            20071,  # Cliffbottom
            20061,  # Road's End
            20051,  # Black Knife
            20111,  # Unsightly
            20121,  # Wyndham
            20221,  # Leyndell
            20141,  # Minor Erdtree
            20151,  # Caelid
            20162,  # War-Dead
            20182,  # Giants' Mountaintop
            20192,  # Consecrated Snowfield
        ],
        "bought_flag": Flags.Recipe_CatacombsDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_CaveDiseaseCure : {
        "name": "Cure: Cave Parasite",
        "info": "",
        "caption": "",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lots": [  # Caves boss rewards after Limgrave
            20361,  # Stillwater
            20371,  # Lakeside Crystal
            20381,  # Academy Crystal
            20491,  # Sage's (Garris)
            20391,  # Seethewater
            20401,  # Volcano
            20451,  # Abandoned
            20431,  # Gaol
            20441,  # Dragonbarrow
            20482,  # Spiritcaller's
            20471,  # Cave of the Forlorn
        ],
        "bought_flag": Flags.Recipe_CaveDiseaseCure_Bought,
    },
    NotesRecipes.Recipe_TunnelDiseaseCure : {
        "name": "Cure: Miner's Fever",
        "info": "",
        "caption": "",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lots": [  # Tunnels boss rewards after Limgrave
            20621,  # Raya Lucaria
            20631,  # Old Altus
            20651,  # Altus
            20641,  # Sealed
            20662,  # Gael
            20674,  # Sellia Crystal
            # Yelough Anix omitted (drops Very Rare staff recipe book instead)
        ],
        "bought_flag": Flags.Recipe_TunnelDiseaseCure_Bought,
    },
    # endregion
    # region Survival Recipes
    NotesRecipes.Recipes_CommonSurvival: {
        "name": "Survivalist's Cookbook [1]",
        "info": "",
        "caption": "",
        "icon": 3122,  # Missionary's Cookbook [1]
        "shop_row": 100508,  # Kale
        "cost": 300,
        "bought_flag": Flags.Recipes_CommonSurvival_Bought,
    },
    NotesRecipes.Recipes_UncommonSurvival: {
        "name": "Survivalist's Cookbook [2]",
        "info": "",
        "caption": "",
        "icon": 3122,  # Missionary's Cookbook [1]
        "shop_rows": [
            100638,  # Merchant - Liurnia of the Lakes
            100666,  # Isolated Merchant - Weeping Peninsula
        ],
        "cost": 1500,
        "bought_flag": Flags.Recipes_UncommonSurvival_Bought,
    },
    NotesRecipes.Recipes_RareSurvival: {
        "name": "Survivalist's Cookbook [3]",
        "info": "",
        "caption": "",
        "icon": 3122,  # Missionary's Cookbook [1]
        "shop_rows": [
            100779,  # Merchant - Mt. Gelmir
            100755,  # Merchant - Altus Plateau
            100846,  # Merchant - South Caelid
        ],
        "cost": 3000,
        "bought_flag": Flags.Recipes_RareSurvival_Bought,
    },
    NotesRecipes.Recipes_VeryRareSurvival: {
        "name": "Survivalist's Cookbook [4]",
        "info": "",
        "caption": "",
        "icon": 3122,  # Missionary's Cookbook [1]
        "shop_rows": [
            100744,  # Hermit Merchant - Leyndell
            100920,  # Merchant - Mountaintops
        ],
        "cost": 8000,
        "bought_flag": Flags.Recipes_VeryRareSurvival_Bought,
    },
    # endregion
    # region Shield Recipes
    NotesRecipes.Recipes_WoodenSmallShields: {
        "name": "Small Shield Smithbook [1]",
        "info": "",
        "caption": "",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100512,  # Kale
        ],
        "cost": 500,
        "bought_flag": Flags.Recipes_WoodenSmallShields_Bought,
    },
    NotesRecipes.Recipes_MetalSmallShields: {
        "name": "Small Shield Smithbook [2]",
        "info": "",
        "caption": "",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100019,  # Gostoc
            100568,  # Merchant - East Limgrave
            100929,  # Merchant - Siofra
        ],
        "cost": 2000,
        "bought_flag": Flags.Recipes_MetalSmallShields_Bought,
    },
    NotesRecipes.Recipes_RareSmallShields: {
        "name": "Small Shield Smithbook [3]",
        "info": "",
        "caption": "",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100745,  # Hermit Merchant - Leyndell
            100955,  # Merchant - Ainsel
        ],
        "cost": 5000,
        "bought_flag": Flags.Recipes_RareSmallShields_Bought,
    },
    NotesRecipes.Recipes_VeryRareSmallShields: {
        "name": "Small Shield Smithbook [4]",
        "info": "",
        "caption": "",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100988,  # Imprisoned Merchant - Mohgwyn
        ],
        "cost": 8000,
        "bought_flag": Flags.Recipes_VeryRareSmallShields_Bought,
    },

    NotesRecipes.Recipes_CommonMediumShields: {
        "name": "Medium Shield Smithbook [1]",
        "info": "",
        "caption": "",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100548,  # Merchant - North Limgrave
            100619,  # Merchant - East Weeping Peninsula
        ],
        "cost": 1000,
        "bought_flag": Flags.Recipes_CommonMediumShields_Bought,
    },
    NotesRecipes.Recipes_WoodenMediumShields: {
        "name": "Medium Shield Smithbook [2]",
        "info": "",
        "caption": "",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100597,  # Merchant - Coastal Cave
            100558,  # Merchant - East Limgrave
        ],
        "cost": 2000,
        "bought_flag": Flags.Recipes_WoodenMediumShields_Bought,
    },
    NotesRecipes.Recipes_HeaterMediumShields: {
        "name": "Medium Shield Smithbook [3]",
        "info": "",
        "caption": "",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100721,  # Merchant - North Liurnia
        ],
        "cost": 5000,
        "bought_flag": Flags.Recipes_HeaterMediumShields_Bought,
    },
    NotesRecipes.Recipes_KiteMediumShields: {
        "name": "Medium Shield Smithbook [4]",
        "info": "",
        "caption": "",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100778,  # Merchant - Mt. Gelmir
        ],
        "cost": 6000,
        "bought_flag": Flags.Recipes_KiteMediumShields_Bought,
    },
    NotesRecipes.Recipes_RareMediumShields: {
        "name": "Medium Shield Smithbook [5]",
        "info": "",
        "caption": "",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100969,  # Merchant - Ainsel River
            100895,  # Isolated Merchant - Dragonbarrow
        ],
        "cost": 9000,
        "bought_flag": Flags.Recipes_RareMediumShields_Bought,
    },

    NotesRecipes.Recipes_CommonGreatshields: {
        "name": "Greatshield Smithbook [1]",
        "info": "",
        "caption": "",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100639,  # Merchant - Liurnia of the Lakes
        ],
        "cost": 2000,
        "bought_flag": Flags.Recipes_CommonGreatshields_Bought,
    },
    NotesRecipes.Recipes_UncommonGreatshields: {
        "name": "Greatshield Smithbook [2]",
        "info": "",
        "caption": "",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100754,  # Merchant - Altus Plateau
        ],
        "cost": 5000,
        "bought_flag": Flags.Recipes_UncommonGreatshields_Bought,
    },
    NotesRecipes.Recipes_RareGreatshields: {
        "name": "Greatshield Smithbook [3]",
        "info": "",
        "caption": "",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100904,  # Merchant - Mountaintops
        ],
        "cost": 8000,
        "bought_flag": Flags.Recipes_RareGreatshields_Bought,
    },
    NotesRecipes.Recipes_VeryRareGreatshields: {
        "name": "Greatshield Smithbook [4]",
        "info": "",
        "caption": "",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100979,  # Imprisoned Merchant - Mohgwyn
        ],
        "cost": 10000,
        "bought_flag": Flags.Recipes_VeryRareGreatshields_Bought,
    },
    # endregion

    # region Staff/Seal Recipes
    NotesRecipes.Recipes_CommonStaffs: {
        "name": "Glintstone Staff Craftbook [1]",
        "info": "",
        "caption": "",
        "icon": 3121,
        "shop_rows": [
            100063,  # Sorceress Sellen
            100203,  # Sorcerer Rogier
        ],
        "cost": 1000,
        "bought_flag": Flags.Recipes_CommonStaffs_Bought,
    },
    NotesRecipes.Recipes_UncommonStaffs: {
        "name": "Glintstone Staff Craftbook [2]",
        "info": "",
        "caption": "",
        "icon": 3121,
        "shop_rows": [
            100679,  # Merchant - Academy of Raya Lucaria
        ],
        "cost": 4000,
        "bought_flag": Flags.Recipes_UncommonStaffs_Bought,
    },
    NotesRecipes.Recipes_RareStaffs: {
        "name": "Glintstone Staff Craftbook [3]",
        "info": "",
        "caption": "",
        "icon": 3121,
        "shop_rows": [
            100253,  # Preceptor Seluvis
            100178,  # Gowry
        ],
        "cost": 8000,
        "bought_flag": Flags.Recipes_RareStaffs_Bought,
    },
    NotesRecipes.Recipes_VeryRareStaffs: {
        "name": "Glintstone Staff Craftbook [4]",
        "info": "",
        "caption": "",
        "icon": 3121,
        "item_lot": 20682,  # Yelough Anix boss reward
        "bought_flag": Flags.Recipes_VeryRareStaffs_Bought,
    },
    NotesRecipes.Recipes_UncommonSeals: {
        "name": "Sacred Seal Craftbook [1]",
        "info": "",
        "caption": "",
        "icon": 3122,
        "item_lot": 10282,  # Fringefolk Hero's Grave boss reward
        "bought_flag": Flags.Recipes_UncommonSeals_Bought,
    },
    NotesRecipes.Recipes_RareSeals: {
        "name": "Sacred Seal Craftbook [2]",
        "info": "",
        "caption": "",
        "icon": 3122,
        "shop_rows": [
            100408,  # Miriel
        ],
        "cost": 5000,
        "bought_flag": Flags.Recipes_RareSeals_Bought,
    },
    NotesRecipes.Recipes_VeryRareSeals: {
        "name": "Sacred Seal Craftbook [3]",
        "info": "",
        "caption": "",
        "icon": 3122,
        "item_lot": 20081,  # Sainted Hero's Grave boss reward
        "bought_flag": Flags.Recipes_VeryRareSeals_Bought,
    },
    # endregion

    # region Torches
    NotesRecipes.Recipe_SteelWireTorch: {
        "name": "Recipe: Steel-Wire Torch",
        "info": "",
        "caption": "",
        "icon": 3120,
        "shop_rows": [
            100003,  # Gostoc
        ],
        "cost": 800,
        "bought_flag": Flags.Recipe_SteelWireTorch_Bought,
    },
    NotesRecipes.Recipe_StTrinasTorch: {
        "name": "Recipe: St. Trina's Torch",
        "info": "",
        "caption": "",
        "icon": 3120,
        "item_lot": 1047400911,  # with former Sword of St. Trina
        "bought_flag": Flags.Recipe_StTrinasTorch_Bought,
    },
    NotesRecipes.Recipe_GhostflameTorch: {
        "name": "Recipe: Ghostflame Torch",
        "info": "",
        "caption": "",
        "icon": 3120,
        "item_lot": 12070501,  # with former Ghostflame Torch
        "bought_flag": Flags.Recipe_GhostflameTorch_Bought,
    },
    NotesRecipes.Recipe_BeastRepellentTorch: {
        "name": "Recipe: Beast-Repellent Torch",
        "info": "",
        "caption": "",
        "icon": 3120,
        "item_lot": 1047380701,  # with Ash of War: Lion's Claw
        "bought_flag": Flags.Recipe_BeastRepellentTorch_Bought,
    },
    NotesRecipes.Recipe_SentrysTorch: {
        "name": "Recipe: Sentry's Torch",
        "info": "",
        "caption": "",
        "icon": 3120,
        "item_lot": 1048550601,  # with Stalwart Horn Charm +1
        "bought_flag": Flags.Recipe_SentrysTorch_Bought,
    },
    # endregion

    NotesRecipes.Note_SerpentHunter: {
        "name": "Note: The Serpent-Hunter",
        "info": "",
        "caption": "",
        "icon": 294,  # Note: Below the Capital
        "item_lot": 16000690,  # old Serpent-Hunter location (deleted prior to this addition)
        "bought_flag": Flags.Note_SerpentHunter_Bought,
    },
    NotesRecipes.Note_Whip: {
        "name": "Recipe: Whip",
        "info": "",
        "caption": "",
        "icon": 294,  # Note: Below the Capital
        "item_lot": 16000611,  # with former Smoldering Shield
        "bought_flag": Flags.Note_Whip_Bought,
    }
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
