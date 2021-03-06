from survival_enums import *


class ModSubcategory(IntEnum):
    """Marks installation type of various dictionary entries below."""
    Survival = 0
    Weapons = 1
    Diseases = 2


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
    AncientDragonSmithingStone = 10140
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
    MetalShards = 21004  # Generic metal scrap. Very common. Worth a "portion" of an Iron plate. More for DEX/bleed.
    MetalPlate = 21005  # Generic metal plate. Base material for most metal weapons. More for STR/heft.
    PliableMetal = 21006  # Rare. Used for Nox weapons and weird weapons.
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


class DiseaseItemLots(IntEnum):
    LimgraveDisease = 10 * DiseaseIndicators.LimgraveDisease
    LiurniaDisease = 10 * DiseaseIndicators.LiurniaDisease
    CaelidDisease = 10 * DiseaseIndicators.CaelidDisease
    AltusDisease = 10 * DiseaseIndicators.AltusDisease
    MtGelmirDisease = 10 * DiseaseIndicators.MtGelmirDisease
    MountaintopsDisease = 10 * DiseaseIndicators.MountaintopsDisease
    SiofraDisease = 10 * DiseaseIndicators.SiofraDisease
    AinselDisease = 10 * DiseaseIndicators.AinselDisease
    DeeprootDisease = 10 * DiseaseIndicators.DeeprootDisease
    StormveilDisease = 10 * DiseaseIndicators.StormveilDisease
    RayaLucariaDisease = 10 * DiseaseIndicators.RayaLucariaDisease
    RadahnDisease = 10 * DiseaseIndicators.RadahnDisease
    VolcanoManorDisease = 10 * DiseaseIndicators.VolcanoManorDisease
    LeyndellDisease = 10 * DiseaseIndicators.LeyndellDisease
    SewersDisease = 10 * DiseaseIndicators.SewersDisease
    HaligtreeDisease = 10 * DiseaseIndicators.HaligtreeDisease
    FarumAzulaDisease = 10 * DiseaseIndicators.FarumAzulaDisease
    MohgwynDisease = 10 * DiseaseIndicators.MohgwynDisease
    CatacombsDisease = 10 * DiseaseIndicators.CatacombsDisease
    CaveDisease = 10 * DiseaseIndicators.CaveDisease
    TunnelDisease = 10 * DiseaseIndicators.TunnelDisease


# Keys are offsets used in all IDs.
    # George: I marked things with XXXX that need to be updated.
NEW_CONSUMABLES = {
    # region Survival Consumables
    Consumables.RawSteak: {
        "name": "Raw Steak",
        "info": "Basic raw meal crafted by hunters",
        "caption": "Raw cut of meat prepared from scraps of flesh.\n"
                   "Craftable survival item.\n"
                   "\n"
                   "Consume to relieve hunger, but not without risk.",
        "recipe": [  # for `EquipMtrlSetParam`
            (2, Materials.SliverOfMeat),
        ],
        "recipe_visibility_flag": Flags.Recipes_CommonSurvival_Bought,
        "effect": SurvivalEffects.RawSteak,  # for `EquipGoodsParam`
        "animation": GoodsUseAnimation.ITEM_EATJERKY,  # for `EquipGoodsParam`
        "icon": 19000,
        "category": ModSubcategory.Survival,
    },
    Consumables.SearedSteak: {
        "name": "Seared Steak",
        "info": "Basic cooked meal crafted by hunters",
        "caption": "Cooked cut of meat prepared from scraps of flesh. Smells delicious.\n"
                   "Craftable survival item.\n"
                   "\n"
                   "Consume to relieve hunger.",
        "recipe": [
            (2, Materials.SliverOfMeat),
            (2, Materials.SmolderingButterfly),
        ],
        "recipe_visibility_flag": Flags.Recipes_CommonSurvival_Bought,
        "effect": SurvivalEffects.SearedSteak,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
        "icon": 19001,
        "category": ModSubcategory.Survival,
    },
    Consumables.RawLiverSteak: {
        "name": "Raw Liver Steak",
        "info": "Raw meal crafted by expert hunters",
        "caption": "Raw cut of meat prepared from scraps of flesh and liver.\n"
                   "Craftable survival item.\n"
                   "\n"
                   "Consume to relieve hunger, but not without risk.",
        "recipe": [
            (2, Materials.SliverOfMeat),
            (1, Materials.BeastLiver),
        ],
        "recipe_visibility_flag": Flags.Recipes_RareSurvival_Bought,
        "effect": SurvivalEffects.RawLiverSteak,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
        "icon": 19002,
        "category": ModSubcategory.Survival,
    },
    Consumables.SearedLiverSteak: {
        "name": "Seared Liver Steak",
        "info": "Cooked meal crafted by expert hunters",
        "caption": "Cooked cut of meat prepared from scraps of flesh and liver. Smells delicious.\n"
                   "Craftable survival item.\n"
                   "\n"
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
        "category": ModSubcategory.Survival,
    },
    Consumables.BoneBroth: {
        "name": "Bone Broth",
        "info": "Light broth to ward off thirst",
        "caption": "Delicious broth prepared from bones.\n"
                   "Craftable survival item.\n"
                   "\n"
                   "Consume to relieve thirst.",
        "recipe": [
            (5, Materials.ThinBeastBones),
        ],
        "recipe_visibility_flag": Flags.Recipes_CommonSurvival_Bought,
        "effect": SurvivalEffects.BoneBroth,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
        "icon": 19004,
        "category": ModSubcategory.Survival,
    },
    Consumables.GreatBoneBroth: {
        "name": "Great Bone Broth",
        "info": "Hearty broth to ward off thirst",
        "caption": "Delicious hearty broth prepared from large bones.\n"
                   "Craftable survival item.\n"
                   "\n"
                   "Consume to relieve thirst.",
        "recipe": [
            (3, Materials.HeftyBeastBone),
        ],
        "recipe_visibility_flag": Flags.Recipes_UncommonSurvival_Bought,
        "effect": SurvivalEffects.GreatBoneBroth,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
        "icon": 19005,
        "category": ModSubcategory.Survival,
    },
    Consumables.BloodBroth: {
        "name": "Blood Broth",
        "info": "Broth preferred by bloodthirsty hunters",
        "caption": "Odorous broth prepared from bones and blood. A delicacy, for some.\n"
                   "Craftable survival item.\n"
                   "\n"
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
        "category": ModSubcategory.Survival,
    },
    Consumables.BerryMedley1: {
        "name": "Forest Berry Medley",
        "info": "Medley of berries from the lower lands",
        "caption": "Prepared fruits picked from rowa shrubs. Tannic, but delicious.\n"
                   "Craftable survival item.\n"
                   "\n"
                   "Consume to relieve hunger and thirst.",
        "recipe": [
            (10, Materials.RowaFruit),
        ],
        "recipe_visibility_flag": Flags.Recipes_CommonSurvival_Bought,
        "effect": SurvivalEffects.BerryMedley1,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
        "icon": 19007,
        "category": ModSubcategory.Survival,
    },
    Consumables.BerryMedley2: {
        "name": "Plateau Berry Medley",
        "info": "Medley of berries from the plateau",
        "caption": "Prepared fruits picked from golden rowa shrubs. Sweet and delicious.\n"
                   "Craftable survival item.\n"
                   "\n"
                   "Consume to relieve hunger and thirst.",
        "recipe": [
            (10, Materials.GoldenRowa),
        ],
        "recipe_visibility_flag": Flags.Recipes_UncommonSurvival_Bought,
        "effect": SurvivalEffects.BerryMedley2,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
        "icon": 19008,
        "category": ModSubcategory.Survival,
    },
    Consumables.BerryMedley3: {
        "name": "Mountain Berry Medley",
        "info": "Medley of berries from the mountains",
        "caption": "Prepared fruits picked from rimed rowa shrubs. Slightly bitter, but uniquely delicious.\n"
                   "Craftable survival item.\n"
                   "\n"
                   "Consume to relieve hunger and thirst.",
        "recipe": [
            (10, Materials.RimedRowa),
        ],
        "recipe_visibility_flag": Flags.Recipes_RareSurvival_Bought,
        "effect": SurvivalEffects.BerryMedley3,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
        "icon": 19009,
        "category": ModSubcategory.Survival,
    },
    Consumables.MushroomStew: {
        "name": "Mushroom Stew",
        "info": "Basic mushroom stew",
        "caption": "Simple, but tasty stew prepared from mushrooms and herba.\n"
                   "Craftable survival item.\n"
                   "\n"
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
        "category": ModSubcategory.Survival,
    },
    Consumables.MeltedMushroomStew: {
        "name": "Melted Mushroom Stew",
        "info": "Thick mushroom stew",
        "caption": "Thick stew prepared from mushrooms and herba. Unusual texture, but incredible taste.\n"
                   "Craftable survival item.\n"
                   "\n"
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
        "category": ModSubcategory.Survival,
    },
    Consumables.DraughtOfSatiation: {
        "name": "Draught of Satiation",
        "info": "Prevents hunter temporarily",
        "caption": "Outlawed concoction once consumed by those seeking to reunite with the dead. Smells terrible.\n"
                   "Craftable survival item.\n"
                   "\n"
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
        "category": ModSubcategory.Survival,
    },
    Consumables.DraughtOfSilverTears: {
        "name": "Draught of Silver Tears",
        "info": "Prevents thirst temporarily",
        "caption": "Outlawed concotion once consumed in a ritual of the Eternal City. Smells awful.\n"
                   "Craftable survival item.\n"
                   "\n"
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
        "category": ModSubcategory.Survival,
    },
    Consumables.MossdewSoup: {
        "name": "Mossdew Soup",
        "info": "Soup with mild heat protection",
        "caption": "Simple medicinal soup. Tastes very bitter.\n"
                   "Craftable survival item.\n"
                   "\n"
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
        "category": ModSubcategory.Survival,
    },
    Consumables.CrystalShardSoup: {
        "name": "Crystal Shard Soup",
        "info": "Soup with moderate heat protection",
        "caption": "Complex medicinal soup. Tastes slightly sweet.\n"
                   "Craftable survival item.\n"
                   "\n"
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
        "category": ModSubcategory.Survival,
    },
    Consumables.GiantsSoup: {
        "name": "Giant's Soup",
        "info": "Soup with great heat protection",
        "caption": "Masterful medicinal soup. Tastes pretty good.\n"
                   "Craftable survival item.\n"
                   "\n"
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
        "category": ModSubcategory.Survival,
    },
    Consumables.AmberEyeBrew: {
        "name": "Amber-Eye Brew",
        "info": "Brew with mild cold protection",
        "caption": "Simple medicinal brew. Rather intoxicating.\n"
                   "Craftable survival item.\n"
                   "\n"
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
        "category": ModSubcategory.Survival,
    },
    Consumables.MagmaticBrew: {
        "name": "Magmatic Brew",
        "info": "Brew with moderate cold protection",
        "caption": "Complex medicinal brew. Makes your tongue feel like it's on fire!\n"
                   "Craftable survival item.\n"
                   "\n"
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
        "category": ModSubcategory.Survival,
    },
    Consumables.BlossomBrew: {
        "name": "Blossom Brew",
        "info": "Brew with great cold protection",
        "caption": "Masterful medicinal brew. Very acidic, and strangely addictive.\n"
                   "Craftable survival item.\n"
                   "\n"
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
        "category": ModSubcategory.Survival,
    },
    Consumables.JarBrittle: {
        "name": "Jar Brittle",
        "info": "Crunchy brittle from living jars",
        "caption": "Aberrant food prepared from the flesh of living jars.\n"
                   "Most find it abhorrent, but others swear it has a taste like no other.\n"
                   "Craftable survival item.\n"
                   "\n"
                   "Consume to relieve hunger and gain mild heat & cold protection.\n"
                   "However, it increases thirst.",
        "recipe": [
            (5, Materials.LivingJarShard),
        ],
        "recipe_visibility_flag": Flags.Recipes_UncommonSurvival_Bought,
        "effect": SurvivalEffects.JarBrittle,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
        "icon": 19020,
        "category": ModSubcategory.Survival,
    },
    # endregion

    # TODO: Leaving slots 21-29 here for more food/drink items.

    # region Disease Cures
    Consumables.LimgraveDiseaseCure: {
        "name": "Cure for Plague of Limgrave",
        "info": "Single-use cure for Plague of Limgrave",
        "caption": "Foul-tasting concoction that will cure the Plague of Limgrave.\n"
                   "\n"
                   "Diseases cured once are less likely to be caught a second time, and a second cure will bestow "
                   "full immunity.",
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
        "category": ModSubcategory.Diseases,
    },
    Consumables.LiurniaDiseaseCure: {
        "name": "Cure for Lake Toxin",
        "info": "Single-use cure for Lake Toxin",
        "caption": "Foul-tasting concoction that will cure Lake Toxin.\n"
                   "\n"
                   "Diseases cured once are less likely to be caught a second time, and a second cure will bestow "
                   "full immunity.",
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
        "category": ModSubcategory.Diseases,
    },
    Consumables.CaelidDiseaseCure: {
        "name": "Cure for Scarlet Parasite",
        "info": "Single-use cure for Scarlet Parasite",
        "caption": "Foul-tasting concoction that will kill the Scarlet Parasite.\n"
                   "\n"
                   "Diseases cured once are less likely to be caught a second time, and a second cure will bestow "
                   "full immunity.",
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
        "category": ModSubcategory.Diseases,
    },
    Consumables.AltusDiseaseCure: {
        "name": "Cure for Windmill Fever",
        "info": "Single-use cure for Windmill Fever",
        "caption": "Foul-tasting concoction that will cure Windmill Fever.\n"
                   "\n"
                   "Diseases cured once are less likely to be caught a second time, and a second cure will bestow "
                   "full immunity.",
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
        "category": ModSubcategory.Diseases,
    },
    Consumables.MtGelmirDiseaseCure: {
        "name": "Cure for Plague of Gelmir",
        "info": "Single-use cure for Plague of Gelmir",
        "caption": "Foul-tasting concoction that will cure the Plague of Gelmir.\n"
                   "\n"
                   "Diseases cured once are less likely to be caught a second time, and a second cure will bestow "
                   "full immunity.",
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
        "category": ModSubcategory.Diseases,
    },
    Consumables.MountaintopsDiseaseCure: {
        "name": "Cure for Frigid Parasite",
        "info": "Single-use cure for Frigid Parasite",
        "caption": "Foul-tasting concoction that will kill the Frigid Parasite.\n"
                   "\n"
                   "Diseases cured once are less likely to be caught a second time, and a second cure will bestow "
                   "full immunity.",
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
        "category": ModSubcategory.Diseases,
    },
    Consumables.SiofraDiseaseCure: {
        "name": "Cure for Plague of Nokron",
        "info": "Single-use cure for Plague of Nokron",
        "caption": "Foul-tasting concoction that will cure the Plague of Nokron.\n"
                   "\n"
                   "Diseases cured once are less likely to be caught a second time, and a second cure will bestow "
                   "full immunity.",
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
        "category": ModSubcategory.Diseases,
    },
    Consumables.AinselDiseaseCure: {
        "name": "Cure for Ant Toxin",
        "info": "Single-use cure for Ant Toxin",
        "caption": "Foul-tasting concoction that will cure Ant Toxin.\n"
                   "\n"
                   "Diseases cured once are less likely to be caught a second time, and a second cure will bestow "
                   "full immunity.",
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
        "category": ModSubcategory.Diseases,
    },
    Consumables.DeeprootDiseaseCure: {
        "name": "Cure for Star-Shaped Parasite",
        "info": "Single-use cure for Star-Shaped Parasite",
        "caption": "Foul-tasting concoction that will kill the Star-Shaped Parasite.\n"
                   "\n"
                   "Diseases cured once are less likely to be caught a second time, and a second cure will bestow "
                   "full immunity.",
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
        "category": ModSubcategory.Diseases,
    },
    Consumables.StormveilDiseaseCure: {
        "name": "Cure for Grafted Plague",
        "info": "Single-use cure for Grafted Plague",
        "caption": "Foul-tasting concoction that will cure Grafted Plague.\n"
                   "\n"
                   "Diseases cured once are less likely to be caught a second time, and a second cure will bestow "
                   "full immunity.",
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
        "category": ModSubcategory.Diseases,
    },
    Consumables.RayaLucariaDiseaseCure: {
        "name": "Cure for Full Moon Fever",
        "info": "Single-use cure for Full Moon Fever",
        "caption": "Foul-tasting concoction that will cure Full Moon Fever.\n"
                   "\n"
                   "Diseases cured once are less likely to be caught a second time, and a second cure will bestow "
                   "full immunity.",
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
        "category": ModSubcategory.Diseases,
    },
    Consumables.RadahnDiseaseCure: {
        "name": "Cure for Starscourge Fever",
        "info": "Single-use cure for Starscourge Fever",
        "caption": "Foul-tasting concoction that will cure Starscourge Fever.\n"
                   "\n"
                   "Diseases cured once are less likely to be caught a second time, and a second cure will bestow "
                   "full immunity.",
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
        "category": ModSubcategory.Diseases,
    },
    Consumables.VolcanoManorDiseaseCure: {
        "name": "Cure for Serpent Toxin",
        "info": "Single-use cure for Serpent Toxin",
        "caption": "Foul-tasting concoction that will cure Serpent Toxin.\n"
                   "\n"
                   "Diseases cured once are less likely to be caught a second time, and a second cure will bestow "
                   "full immunity.",
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
        "category": ModSubcategory.Diseases,
    },
    Consumables.LeyndellDiseaseCure: {
        "name": "Cure for Plague of Leyndell",
        "info": "Single-use cure for Plague of Leyndell",
        "caption": "Foul-tasting concoction that will cure the Plague of Leyndell.\n"
                   "\n"
                   "Diseases cured once are less likely to be caught a second time, and a second cure will bestow "
                   "full immunity.",
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
        "category": ModSubcategory.Diseases,
    },
    Consumables.SewersDiseaseCure: {
        "name": "Cure for Omen Parasite",
        "info": "Single-use cure for Omen Parasite",
        "caption": "Foul-tasting concoction that will kill the Omen Parasite.\n"
                   "\n"
                   "Diseases cured once are less likely to be caught a second time, and a second cure will bestow "
                   "full immunity.",
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
        "category": ModSubcategory.Diseases,
    },
    Consumables.HaligtreeDiseaseCure: {
        "name": "Cure for Unalloyed Plague",
        "info": "Single-use cure for Unalloyed Plague",
        "caption": "Foul-tasting concoction that will cure the Unalloyed Plague.\n"
                   "\n"
                   "Diseases cured once are less likely to be caught a second time, and a second cure will bestow "
                   "full immunity.",
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
        "category": ModSubcategory.Diseases,
    },
    Consumables.FarumAzulaDiseaseCure: {
        "name": "Cure for Beastman's Fever",
        "info": "Single-use cure for Beastman's Fever",
        "caption": "Foul-tasting concoction that will cure Beastman's Fever.\n"
                   "\n"
                   "Diseases cured once are less likely to be caught a second time, and a second cure will bestow "
                   "full immunity.",
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
        "category": ModSubcategory.Diseases,
    },
    Consumables.MohgwynDiseaseCure: {
        "name": "Cure for Blood Lord's Fever",
        "info": "Single-use cure for Blood Lord's Fever",
        "caption": "Foul-tasting concoction that will cure the Blood Lord's Fever.\n"
                   "\n"
                   "Diseases cured once are less likely to be caught a second time, and a second cure will bestow "
                   "full immunity.",
        "recipe": [  # a bit easier than most due to the brutal nature of the disease
            (10, Materials.ThinBeastBones),
            (10, Materials.HeftyBeastBone),
            (10, Materials.BeastLiver),
            (10, Materials.BeastBlood),
        ],
        "recipe_visibility_flag": Flags.Recipe_MohgwynDiseaseCure_Bought,
        "effect": SurvivalEffects.CureMohgwynDisease,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "icon": 24,  # Flask of Wondrous Physick
        "category": ModSubcategory.Diseases,
    },
    Consumables.CatacombsDiseaseCure: {
        "name": "Cure for Catacombs Toxin",
        "info": "Single-use cure for Catacombs Toxin",
        "caption": "Foul-tasting concoction that will cure Catacombs Toxin.\n"
                   "\n"
                   "Diseases cured once are less likely to be caught a second time, and a second cure will bestow "
                   "full immunity.",
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
        "category": ModSubcategory.Diseases,
    },
    Consumables.CaveDiseaseCure: {
        "name": "Cure for Cave Parasite",
        "info": "Single-use cure for Cave Parasite",
        "caption": "Foul-tasting concoction that will kill the Cave Parasite.\n"
                   "\n"
                   "Diseases cured once are less likely to be caught a second time, and a second cure will bestow "
                   "full immunity.",
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
        "category": ModSubcategory.Diseases,
    },
    Consumables.TunnelDiseaseCure: {
        "name": "Cure for Miner's Fever",
        "info": "Single-use cure for Miner's Fever",
        "caption": "Foul-tasting concoction that will cure Miner's Fever.\n"
                   "\n"
                   "Diseases cured once are less likely to be caught a second time, and a second cure will bestow "
                   "full immunity.",
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
        "category": ModSubcategory.Diseases,
    },
    # endregion
}


NEW_MATERIALS = {
    Materials.SoftWood: {
        "name": "Soft Wood",
        "info": "Unremarkable piece of wood",
        "caption": "Inferior quality wood, fit for cinder.\n"
                   "Common material for crafting weapons and shields.",
        "material_info": "Found commonly as loot or dropped by foes",
        "icon": 19036,
        "category": ModSubcategory.Weapons,
    },
    Materials.RefinedWood: {
        "name": "Refined Wood",
        "info": "Robust piece of wood",
        "caption": "Superior quality wood that has been treated.\n"
                   "Uncommon material for crafting weapons and shields.",
        "material_info": "Found sometimes as loot",
        "icon": 19037,
        "category": ModSubcategory.Weapons,
    },
    Materials.StoneFragment: {
        "name": "Stone Fragment",
        "info": "Fragment of simple colored stone",
        "caption": "Fragment of an extremely durable stone.\n"
                   "Common material for crafting weapons and shields.",
        "material_info": "Found commonly in mines",
        "icon": 19038,
        "category": ModSubcategory.Weapons,
    },
    Materials.SomberStoneFragment: {
        "name": "Somber Stone Fragment",
        "info": "Fragment of rare colorless stone",
        "caption": "Fragment of an extremely durable white stone.\n"
                   "Uncommon material for crafting weapons and shields.",
        "material_info": "Found sometimes in mines",
        "icon": 19039,
        "category": ModSubcategory.Weapons,
    },
    Materials.MetalShards: {
        "name": "Metal Shards",
        "info": "Shards of metal for forging",
        "caption": "Shards of metal that came from a larger piece.\n"
                   "Common material for crafting weapons and shields.",
        "material_info": "Found commonly as loot or dropped by foes",
        "icon": 19040,
        "category": ModSubcategory.Weapons,
    },
    Materials.MetalPlate: {
        "name": "Metal Plate",
        "info": "Sheet of metal for forging",
        "caption": "Sheet of metal perfect for forging metallic weapons.\n"
                   "Uncommon material for crafting weapons and shields.",
        "material_info": "Found sometimes as loot",
        "icon": 19041,
        "category": ModSubcategory.Weapons,
    },
    Materials.PliableMetal: {
        "name": "Pliable Metal",
        "info": "Rare metal used for forging",
        "caption": "Prized metal that bends, but never breaks.\n"
                   "Rare material for crafting weapons and shields.",
        "material_info": "Found rarely as loot",
        "icon": 19042,
        "category": ModSubcategory.Weapons,
    },
    Materials.DragonTeeth: {
        "name": "Dragon Teeth",
        "info": "Collection of small dragon teeth",
        "caption": "Small dragon teeth with latent power, perfect for forging dragon weapons.\n"
                   "Very rare material for crafting weapons and shields.",
        "material_info": "Found rarely as loot or dropped by dragons",
        "icon": 19043,
        "category": ModSubcategory.Weapons,
    },
    Materials.GruesomeBone: {
        "name": "Gruesome Bone",
        "info": "Disgusting large bone used for forging",
        "caption": "Very large, disturbing bone prized by arcane smiths for its unique properties.\n"
                   "Rare material for crafting weapons and shields.",
        "material_info": "Found rarely as loot",
        "icon": 19044,
        "category": ModSubcategory.Weapons,
    },
    Materials.ErdtreeWood: {
        "name": "Erdtree Wood",
        "info": "Holy wood from the Erdtree",
        "caption": "Wood highly prized by craftsmen. Very light, but quite tough.\n"
                   "Rare material for crafting weapons and shields.",
        "material_info": "Found rarely as loot",
        "icon": 19045,
        "category": ModSubcategory.Weapons,
    },
    Materials.MeteoriteChunk: {
        "name": "Meteorite Chunk",
        "info": "Dense chunk of cosmic debris",
        "caption": "Very heavy chunk of metal of cosmic origin.\n"
                   "Rare material for crafting weapons and shields.",
        "material_info": "Found rarely as loot",
        "icon": 19046,
        "category": ModSubcategory.Weapons,
    },
    Materials.BlackMark: {
        "name": "Black Mark",
        "info": "Residue from the stolen Rune of Death",
        "caption": "Faint remnant of death scattered when the Rune of Death was stolen.\n"
                   "Very rare material for crafting weapons and shields.",
        "material_info": "Found very rarely as loot",
        "icon": 19047,
        "category": ModSubcategory.Weapons,
    },
    Materials.StaffPole: {
        "name": "Staff Pole",
        "info": "Wooden staff perfect for a magic catalyst",
        "caption": "Intricately prepared wooden branch perfect for creating a glintstone staff.\n"
                   "Rare material for crafting weapons and shields.",
        "material_info": "Found rarely as loot",
        "icon": 19048,
        "category": ModSubcategory.Weapons,
    },
    Materials.ShieldGrip: {
        "name": "Shield Handle",
        "info": "Sturdy handle perfect for a shield",
        "caption": "Reliable handle designed to withstand large impacts, perfect for any shield.\n"
                   "Uncommon material for crafting weapons and shields.",
        "material_info": "Found sometimes as loot",
        "icon": 19049,
        "category": ModSubcategory.Weapons,
    },
    Materials.ErdtreeAmber: {
        "name": "Erdtree Amber",
        "info": "Amber formed from the Erdtree's resin",
        "caption": "Holy amber that came from Erdtree resin. Highly prized by the Golden Order.\n"
                   "Very rare material for crafting weapons and shields.",
        "material_info": "Found very rarely as loot",
        "icon": 19050,
        "category": ModSubcategory.Weapons,
    },
    Materials.GlintstoneDust: {
        "name": "Glintstone Dust",
        "info": "Fine grains of purified Glintstone",
        "caption": "Small amount of purified glintstone, ground into a powder specifically for crafting.\n"
                   "Rare material for crafting weapons and shields.",
        "material_info": "Found sometimes as loot",
        "icon": 19051,
        "category": ModSubcategory.Weapons,
    },
}


NEW_SMITHS_HAMMERS = {
    SmithsHammers.NoviceSmithsHammer: {
        "name": "Novice Smith's Hammer",
        "info": "Hammer required for weapon upgrades",
        "caption": "Craftable hammer that can be used in the field.\n"
                   "\n"
                   "Allows basic weapons to be upgraded into more powerful tools of battle.",
        "icon": 10407,  # Hammer weapon
        "recipe_visibility_flag": Flags.ShowNoviceSmithsHammer,
        "recipe": [
            (6, Materials.SmithingStone1),
            (6, Materials.SmithingStone2),
            (3, Materials.SomberSmithingStone1),
            (3, Materials.SomberSmithingStone2),
        ],
        "category": ModSubcategory.Weapons,
    },
    SmithsHammers.ApprenticeSmithsHammer: {
        "name": "Apprentice Smith's Hammer",
        "info": "Hammer required for weapon upgrades",
        "caption": "Craftable hammer that can be used in the field.\n"
                   "\n"
                   "Allows slightly advanced weapons to be upgraded into more powerful tools of battle.",
        "icon": 10407,  # Hammer weapon
        "recipe_visibility_flag": Flags.ShowApprenticeSmithsHammer,
        "recipe": [
            (6, Materials.SmithingStone3),
            (6, Materials.SmithingStone4),
            (3, Materials.SomberSmithingStone3),
            (3, Materials.SomberSmithingStone4),
        ],
        "category": ModSubcategory.Weapons,
    },
    SmithsHammers.JourneymanSmithsHammer: {
        "name": "Journeyman Smith's Hammer",
        "info": "Hammer required for weapon upgrades",
        "caption": "Craftable hammer that can be used in the field.\n"
                   "\n"
                   "Allows moderately advanced weapons to be upgraded into more powerful tools of battle.",
        "icon": 10407,  # Hammer weapon
        "recipe_visibility_flag": Flags.ShowJourneymanSmithsHammer,
        "recipe": [
            (6, Materials.SmithingStone5),
            (6, Materials.SmithingStone6),
            (3, Materials.SomberSmithingStone5),
            (3, Materials.SomberSmithingStone6),
        ],
        "category": ModSubcategory.Weapons,
    },
    SmithsHammers.ExpertSmithsHammer: {
        "name": "Expert Smith's Hammer",
        "info": "Hammer required for weapon upgrades",
        "caption": "Craftable hammer that can be used in the field.\n"
                   "\n"
                   "Allows greatly advanced weapons to be upgraded into more powerful tools of battle.",
        "icon": 10407,  # Hammer weapon
        "recipe_visibility_flag": Flags.ShowExpertSmithsHammer,
        "recipe": [
            (6, Materials.SmithingStone7),
            (6, Materials.SmithingStone8),
            (3, Materials.SomberSmithingStone7),
            (3, Materials.SomberSmithingStone8),
        ],
        "category": ModSubcategory.Weapons,
    },
    SmithsHammers.MasterSmithsHammer: {
        "name": "Master Smith's Hammer",
        "info": "Hammer required for weapon upgrades",
        "caption": "Craftable hammer that can be used in the field.\n"
                   "\n"
                   "Allows extremely advanced weapons to be transformed into legendary armaments.",
        "icon": 10414,  # Marika's Hammer weapon
        "recipe_visibility_flag": Flags.ShowMasterSmithsHammer,
        "recipe": [
            (1, Materials.AncientDragonSmithingStone),
            (1, Materials.SomberAncientDragonSmithingStone),
            (1, Materials.MeteoriteChunk),
            (1, Materials.ErdtreeAmber),
        ],
        "category": ModSubcategory.Weapons,
    },
}


DISEASE_INDICATORS = {
    DiseaseIndicators.LimgraveDisease: {
        "name": "Disease: Plague of Limgrave",
        "info": "Disease contracted in the hills of Limgrave",
        "caption": "Illness not uncommon in the lower lands.\n"
                   "Accelerates the effects of thirst and hunger.\n"
                   "\n"
                   "Some believe this plague was spread to Limgrave intentionally, to inflict even more suffering upon "
                   "the scattered crucified.",
        "icon": 3739,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.LiurniaDisease: {
        "name": "Disease: Lake Toxin",
        "info": "Disease contracted in the lakes of Liurnia",
        "caption": "Mild toxin found in and around the lakes of Liurnia.\n"
                   "Lowers intelligence and arcane ability.\n"
                   "\n"
                   "The Carian royals blame the glintstone sorcerers of Raya Lucaria for creating this poison, and "
                   "vice versa. Perhaps only the crayfish know the truth.",
        "icon": 3735,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.CaelidDisease: {
        "name": "Disease: Scarlet Parasite",
        "info": "Disease contracted in the wastes of Caelid",
        "caption": "Malicious red parasite borne of blood and war.\n"
                   "Reduces the effectiveness of Crimson Tears.\n"
                   "\n"
                   "These vermin line the throat and subsist on stolen restorative tears. Though they have the same "
                   "hue as scarlet rot, any relation between the two is unclear, aside from their shared breeding of "
                   "misery.",
        "icon": 3736,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.AltusDisease: {
        "name": "Disease: Windmill Fever",
        "info": "Disease contracted on the Altus Plateau",
        "caption": "Illness not uncommon in the upper lands.\n"
                   "Greatly reduces poise.\n"
                   "\n"
                   "Cryptic illness first observed in commoners who stared too long at windmills, though it has since "
                   "become more widely endemic in the hills surrounding the Royal Capital.",
        "icon": 3734,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.MtGelmirDisease: {
        "name": "Disease: Plague of Gelmir",
        "info": "Disease contracted atop Mt. Gelmir",
        "caption": "Rare disease bred only in the warm rocks of Mt. Gelmir.\n"
                   "Greatly reduces hemorrhage resistance.\n"
                   "\n"
                   "This high-altitude illness thins the blood, making one more vulnerable to cutting attacks.",
        "icon": 3739,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.MountaintopsDisease: {
        "name": "Disease: Frigid Parasite",
        "info": "Disease contracted upon the Mountaintops",
        "caption": "Ice-blue tick originating in the mountaintops far above Leyndell.\n"
                   "Greatly reduces stamina recovery speed.\n"
                   "\n"
                   "Mercifully, this aberrant lifeform breeds only in the frozen peaks of the Giants. It is "
                   "customary in Leyndell to execute any traveller suspected of carrying it.",
        "icon": 3736,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.SiofraDisease: {
        "name": "Disease: Plague of Nokron",
        "info": "Disease contracted near the Eternal City of Nokron",
        "caption": "Illness found in the underground silver city of Nokron.\n"
                   "Greatly reduces magic defense.\n"
                   "\n"
                   "This disease originated in the poorest areas of the Eternal City of Nokron, and was carried "
                   "further downstream by the Siofra River.",
        "icon": 3739,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.AinselDisease: {
        "name": "Disease: Ant Toxin",
        "info": "Disease contracted from the nests of the Ainsel River",
        "caption": "Numbing venom originating from ants along the Ainsel River.\n"
                   "Lowers mind and endurance.\n"
                   "\n"
                   "Rarely, claymen have been seen aggravating the giant ants intentionally. Perhaps they simply wish "
                   "to feel something.",
        "icon": 3735,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.DeeprootDisease: {
        "name": "Disease: Star-Shaped Parasite",
        "info": "Disease contracted from the roots deep below the Royal Capital",
        "caption": "Eldritch spider-like entity found only in the nameless eternal city.\n"
                   "Lowers FP to essentially nothing.\n"
                   "\n"
                   "This creature sits in the ear canal and whispers the incomprehensible words of an outer god, "
                   "making it extremely difficult to focus on anything else.",
        "icon": 3736,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.StormveilDisease: {
        "name": "Disease: Grafted Plague",
        "info": "Disease contracted from Stormveil Castle",
        "caption": "Illness borne from the failed experiments of Godrick.\n"
                   "Greatly reduces poison and scarlet rot resistance.\n"
                   "\n"
                   "Additional limbs may improve battle prowess for some, but for many, it does little beyond increase "
                   "vulnerability to other afflictions.",
        "icon": 3739,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.RayaLucariaDisease: {
        "name": "Disease: Full Moon Fever",
        "info": "Disease contracted from the Academy of Raya Lucaria",
        "caption": "Affliction that spreads within the Academy of Raya Lucaria.\n"
                   "Greatly reduces equip load.\n"
                   "\n"
                   "After Queen Rennala was sealed inside the library, a growing number of new pupils found themselves "
                   "transfixed by the full moon and burdened by its implications.",
        "icon": 3734,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.RadahnDisease: {
        "name": "Disease: Starscourge Fever",
        "info": "Disease contracted from Starscourge Radahn",
        "caption": "Mad battle fever that afflicts General Radahn.\n"
                   "Makes it difficult to take enemies by surprise.\n"
                   "\n"
                   "The Red Lion General is not known for his subtlety, and those infected by his lust for battle may "
                   "find it equally difficult to approach foes unannounced.",
        "icon": 3734,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.VolcanoManorDisease: {
        "name": "Disease: Serpent Toxin",
        "info": "Disease contracted from the Volcano Manor",
        "caption": "Paralyzing venom spread by the serpents of the Volcano Manor.\n"
                   "Reduces strength and dexterity.\n"
                   "\n"
                   "This powerful toxin is said to originate from Praetor Rykard himself, though in truth, it likely "
                   "predates his fateful encounter with the Serpent-God.",
        "icon": 3735,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.LeyndellDisease: {
        "name": "Disease: Plague of Leyndell",
        "info": "Disease contracted from the Royal Capital",
        "caption": "Illness that is increasingly pervasive in Leyndell.\n"
                   "Greatly reduces resistance to death blight.\n"
                   "\n"
                   "Plague of unknown origin that has been slowly spreading in Leyndell. Some blame the Omen sealed "
                   "beneath the city, but others believe it is a manifestation of the Erdtree's decay.",
        "icon": 3739,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.SewersDisease: {
        "name": "Disease: Omen Parasite",
        "info": "Disease contracted from the tunnels beneath Leyndell",
        "caption": "Horned insect that resides in the shunning-grounds beneath the Royal Capital.\n"
                   "Halves runes gained from felling enemies.\n"
                   "\n"
                   "Many Omen beneath the Capital have formed a pair-bond with this light-feeding creature, but "
                   "it shows no interest in pursuing any sort of symbiosis with lowly Tarnished.",
        "icon": 3736,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.HaligtreeDisease: {
        "name": "Disease: Unalloyed Plague",
        "info": "Disease contracted from Miquella's Haligtree",
        "caption": "Disease that sometimes manifests among the unalloyed of the Haligtree.\n"
                   "Greatly reduces fire and lightning defense.\n"
                   "\n"
                   "Miquella's attempts to resist the afflictions of the outer gods were noble, but unalloyed gold "
                   "is a poor defense against the elements of the ancient dragons.",
        "icon": 3739,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.FarumAzulaDisease: {
        "name": "Disease: Beastman's Fever",
        "info": "Disease contracted from Farum Azula",
        "caption": "Illness common among the beastmen of crumbling Farum Azula.\n"
                   "Reduces physical attack power.\n"
                   "\n"
                   "Among the thick-skinned beastmen, this disease is considered fairly harmless.",
        "icon": 3734,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.MohgwynDisease: {
        "name": "Disease: Blood Lord's Fever",
        "info": "Disease contracted from Mohgwyn Dynasty Palace",
        "caption": "Deadly affliction originating in the Blood Lord's palace.\n"
                   "Causes gradual bleed build-up.\n"
                   "\n"
                   "To be marked with the blood of Mohgwyn is to be marked with death. For the truly devout, it is an "
                   "honor beyond words.",
        "icon": 3734,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.CatacombsDisease: {
        "name": "Disease: Catacombs Toxin",
        "info": "Disease contracted from a sealed crypt",
        "caption": "Haunting poison that can be found in catacombs across the Lands Between.\n"
                   "Reduces vigor and faith.\n"
                   "\n"
                   "This dark substance coats many statues and bones in crypts. Death comes more swiftly for any who "
                   "touch it, as does despair.",
        "icon": 3735,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.CaveDisease: {
        "name": "Disease: Cave Parasite",
        "info": "Disease contracted from a dark cave",
        "caption": "Tiny organism that breeds in cave moss.\n"
                   "Reduces all defenses during daylight.\n"
                   "\n"
                   "Travellers who spend too long underground are known to become nocturnal, perhaps through no "
                   "fault of their own.",
        "icon": 3736,  # faded skull in Icon_02_A
    },
    DiseaseIndicators.TunnelDisease: {
        "name": "Disease: Miner's Fever",
        "info": "Disease contracted from a mining tunnel",
        "caption": "Illness not uncommon among miners.\n"
                   "Greatly reduces madness resistance.\n"
                   "\n"
                   "Touching too much unrefined glintstone is a hazard for miners, but most are given little choice "
                   "but to risk it.",
        "icon": 3734,  # faded skull in Icon_02_A
    },
}


NEW_NOTES = {
    # region Disease Cures
    NotesRecipes.Note_CuringDiseases : {
        "name": "Note: Surviving in the Lands Between",
        "info": "Note imparting knowledge in brief",
        "caption": "Note sold by a nomadic merchant imparting knowledge in brief.\n"
                   "\n"
                   "\"Survival is difficult in the Lands Between. Maintain a supply of food and drink to stave off "
                   "hunger and thirst. Soups and brews can resist the effects of extreme temperatures.\n"
                   "\n"
                   "Beware of the varying diseases across different regions. Recipes for cures may be found or sold "
                   "somewhere in the same area or the same type of underground dungeon.\"",
        "icon": 298,  # Note: Hidden Cave
        "shop_row": 100509,  # Kale
        "cost": 200,
        "bought_flag": Flags.Note_CuringDiseases_Bought,
        "category": ModSubcategory.Diseases,
    },
    NotesRecipes.Recipe_LimgraveDiseaseCure : {
        "name": "Cure: Plague of Limgrave",
        "info": "Note imparting a disease cure recipe",
        "caption": "Torn page revealing a recipe for curing the Plague of Limgrave.\n"
                   "\n"
                   "Complete the recipe to obtain a single-use cure for the disease.",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "shop_row": 100596,  # Coastal Cave merchant (TESTED)
        "cost": 2000,
        "bought_flag": Flags.Recipe_LimgraveDiseaseCure_Bought,
        "category": ModSubcategory.Diseases,
    },
    NotesRecipes.Recipe_LiurniaDiseaseCure : {
        "name": "Cure: Lake Toxin",
        "info": "Note imparting a disease cure recipe",
        "caption": "Torn page revealing a recipe for cleansing lake toxins.\n"
                   "\n"
                   "Complete the recipe to obtain a single-use cure for the disease.",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "shop_row": 100697,  # Academy of Raya Lucaria merchant
        "cost": 3000,
        "bought_flag": Flags.Recipe_LiurniaDiseaseCure_Bought,
        "category": ModSubcategory.Diseases,
    },
    NotesRecipes.Recipe_CaelidDiseaseCure : {
        "name": "Cure: Scarlet Parasite",
        "info": "Note imparting a disease cure recipe",
        "caption": "Torn page revealing a recipe for exterminating scarlet parasites.\n"
                   "\n"
                   "Complete the recipe to obtain a single-use cure for the disease.",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "shop_row": 100894,  # Dragonbarrow merchant
        "cost": 4000,
        "bought_flag": Flags.Recipe_CaelidDiseaseCure_Bought,
        "category": ModSubcategory.Diseases,
    },
    NotesRecipes.Recipe_AltusDiseaseCure : {
        "name": "Cure: Windmill Fever",
        "info": "Note imparting a disease cure recipe",
        "caption": "Torn page revealing a recipe for curing Windmill Fever.\n"
                   "\n"
                   "Complete the recipe to obtain a single-use cure for the disease.",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "shop_row": 100756,  # Altus Plateau merchant
        "cost": 4000,
        "bought_flag": Flags.Recipe_AltusDiseaseCure_Bought,
        "category": ModSubcategory.Diseases,
    },
    NotesRecipes.Recipe_MtGelmirDiseaseCure : {
        "name": "Cure: Plague of Gelmir",
        "info": "Note imparting a disease cure recipe",
        "caption": "Torn page revealing a recipe for curing the Plague of Gelmir.\n"
                   "\n"
                   "Complete the recipe to obtain a single-use cure for the disease.",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "shop_row": 100799,  # Mt. Gelmir merchant
        "cost": 4000,
        "bought_flag": Flags.Recipe_MtGelmirDiseaseCure_Bought,
        "category": ModSubcategory.Diseases,
    },
    NotesRecipes.Recipe_MountaintopsDiseaseCure : {
        "name": "Cure: Frigid Parasite",
        "info": "Note imparting a disease cure recipe",
        "caption": "Torn page revealing a recipe for exterminating frigid parasites.\n"
                   "\n"
                   "Complete the recipe to obtain a single-use cure for the disease.",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "shop_row": 100919,  # Mountaintops merchant
        "cost": 5000,
        "bought_flag": Flags.Recipe_MountaintopsDiseaseCure_Bought,
        "category": ModSubcategory.Diseases,
    },
    NotesRecipes.Recipe_SiofraDiseaseCure : {
        "name": "Cure: Plague of Nokron",
        "info": "Note imparting a disease cure recipe",
        "caption": "Torn page revealing a recipe for curing the Plague of Nokron.\n"
                   "\n"
                   "Complete the recipe to obtain a single-use cure for the disease.",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "shop_row": 100942,  # Siofra merchant
        "cost": 2000,
        "bought_flag": Flags.Recipe_SiofraDiseaseCure_Bought,
        "category": ModSubcategory.Diseases,
    },
    NotesRecipes.Recipe_AinselDiseaseCure : {
        "name": "Cure: Ant Toxin",
        "info": "Note imparting a disease cure recipe",
        "caption": "Torn page revealing a recipe for ant antivenom.\n"
                   "\n"
                   "Complete the recipe to obtain a single-use cure for the disease.",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "shop_row": 100968,  # Ainsel merchant
        "cost": 3000,
        "bought_flag": Flags.Recipe_AinselDiseaseCure_Bought,
        "category": ModSubcategory.Diseases,
    },
    NotesRecipes.Recipe_DeeprootDiseaseCure : {
        "name": "Cure: Star-Shaped Parasite",
        "info": "Note imparting a disease cure recipe",
        "caption": "Torn page revealing a recipe for exterminating star-shaped parasites.\n"
                   "\n"
                   "Complete the recipe to obtain a single-use cure for the disease.",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lot": 12030521,  # with Mausoleum Soldier Ashes
        "bought_flag": Flags.Recipe_DeeprootDiseaseCure_Bought,
        "category": ModSubcategory.Diseases,
    },
    NotesRecipes.Recipe_StormveilDiseaseCure : {
        "name": "Cure: Grafted Plague",
        "info": "Note imparting a disease cure recipe",
        "caption": "Torn page revealing a recipe for curing the Grafted Plague.\n"
                   "\n"
                   "Complete the recipe to obtain a single-use cure for the disease.",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lot": 10000991,  # with Godskin Prayerbook
        "bought_flag": Flags.Recipe_StormveilDiseaseCure_Bought,
        "category": ModSubcategory.Diseases,
    },
    NotesRecipes.Recipe_RayaLucariaDiseaseCure : {
        "name": "Cure: Full Moon Fever",
        "info": "Note imparting a disease cure recipe",
        "caption": "Torn page revealing a recipe for curing Full Moon Fever.\n"
                   "\n"
                   "Complete the recipe to obtain a single-use cure for the disease.",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lot": 14000941,  # with Radagon Icon
        "bought_flag": Flags.Recipe_RayaLucariaDiseaseCure_Bought,
        "category": ModSubcategory.Diseases,
    },
    NotesRecipes.Recipe_RadahnDiseaseCure : {
        "name": "Cure: Starscourge Fever",
        "info": "Note imparting a disease cure recipe",
        "caption": "Torn page revealing a recipe for curing Starscourge Fever.\n"
                   "\n"
                   "Complete the recipe to obtain a single-use cure for the disease.",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lot": 30160041,  # with Collapsing Stars (in War-Dead Catacombs)
        "bought_flag": Flags.Recipe_RadahnDiseaseCure_Bought,
        "category": ModSubcategory.Diseases,
    },
    NotesRecipes.Recipe_VolcanoManorDiseaseCure : {
        "name": "Cure: Serpent Toxin",
        "info": "Note imparting a disease cure recipe",
        "caption": "Torn page revealing a recipe for serpent antivenom.\n"
                   "\n"
                   "Complete the recipe to obtain a single-use cure for the disease.",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lot": 16000621,  # with Dagger Talisman
        "bought_flag": Flags.Recipe_VolcanoManorDiseaseCure_Bought,
        "category": ModSubcategory.Diseases,
    },
    NotesRecipes.Recipe_LeyndellDiseaseCure : {
        "name": "Cure: Plague of Leyndell",
        "info": "Note imparting a disease cure recipe",
        "caption": "Torn page revealing a recipe for curing the Plague of Leyndell.\n"
                   "\n"
                   "Complete the recipe to obtain a single-use cure for the disease.",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lot": 11000911,  # with Golden Order Principia
        "bought_flag": Flags.Recipe_LeyndellDiseaseCure_Bought,
        "category": ModSubcategory.Diseases,
    },
    NotesRecipes.Recipe_SewersDiseaseCure : {
        "name": "Cure: Omen Parasite",
        "info": "Note imparting a disease cure recipe",
        "caption": "Torn page revealing a recipe for exterminating Omen parasites.\n"
                   "\n"
                   "Complete the recipe to obtain a single-use cure for the disease.",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lot": 35000271,  # with Nomad Ashes
        "bought_flag": Flags.Recipe_SewersDiseaseCure_Bought,
        "category": ModSubcategory.Diseases,
    },
    NotesRecipes.Recipe_HaligtreeDiseaseCure : {
        "name": "Cure: Unalloyed Plague",
        "info": "Note imparting a disease cure recipe",
        "caption": "Torn page revealing a recipe for curing the Unalloyed plague.\n"
                   "\n"
                   "Complete the recipe to obtain a single-use cure for the disease.",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lot": 15000801,  # with Marika's Soreseal
        "bought_flag": Flags.Recipe_HaligtreeDiseaseCure_Bought,
        "category": ModSubcategory.Diseases,
    },
    NotesRecipes.Recipe_FarumAzulaDiseaseCure : {
        "name": "Cure: Beastman's Fever",
        "info": "Note imparting a disease cure recipe",
        "caption": "Torn page revealing a recipe for curing Beastman's Fever.\n"
                   "\n"
                   "Complete the recipe to obtain a single-use cure for the disease.",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lot": 13000941,  # with Dragon Towershield
        "bought_flag": Flags.Recipe_FarumAzulaDiseaseCure_Bought,
        "category": ModSubcategory.Diseases,
    },
    NotesRecipes.Recipe_MohgwynDiseaseCure : {
        "name": "Cure: Blood Lord's Fever",
        "info": "Note imparting a disease cure recipe",
        "caption": "Torn, bloody page revealing a recipe for curing the Blood Lord's Fever.\n"
                   "\n"
                   "Complete the recipe to obtain a single-use cure for the disease.",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "shop_row": 100987,  # Mohgwyn merchant
        "cost": 10000,
        "bought_flag": Flags.Recipe_MohgwynDiseaseCure_Bought,
        "category": ModSubcategory.Diseases,
    },
    NotesRecipes.Recipe_CatacombsDiseaseCure : {
        "name": "Cure: Catacombs Toxin",
        "info": "Note imparting a disease cure recipe",
        "caption": "Torn page revealing a recipe for curing catacombs toxin.\n"
                   "\n"
                   "Complete the recipe to obtain a single-use cure for the disease.",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lots": [  # Catacombs boss rewards after Limgrave
            20072,  # Cliffbottom
            20062,  # Road's End
            20052,  # Black Knife
            20112,  # Unsightly
            20122,  # Wyndham
            20222,  # Leyndell
            20142,  # Minor Erdtree
            20152,  # Caelid
            20163,  # War-Dead
            20183,  # Giants' Mountaintop
            20193,  # Consecrated Snowfield
        ],
        "bought_flag": Flags.Recipe_CatacombsDiseaseCure_Bought,
        "category": ModSubcategory.Diseases,
    },
    NotesRecipes.Recipe_CaveDiseaseCure : {
        "name": "Cure: Cave Parasite",
        "info": "Note imparting a disease cure recipe",
        "caption": "Torn page revealing a recipe for exterminating cave parasites.\n"
                   "\n"
                   "Complete the recipe to obtain a single-use cure for the disease.",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lots": [  # Caves boss rewards after Limgrave
            20362,  # Stillwater
            20372,  # Lakeside Crystal
            20382,  # Academy Crystal
            20392,  # Seethewater
            20401,  # Volcano
            20422,  # Sage's (Black Knife Assassin)
            20432,  # Gaol
            20442,  # Dragonbarrow
            20452,  # Abandoned
            20471,  # Cave of the Forlorn
            20483,  # Spiritcaller's
            20492,  # Sage's (Garris)
        ],
        "bought_flag": Flags.Recipe_CaveDiseaseCure_Bought,
        "category": ModSubcategory.Diseases,
    },
    NotesRecipes.Recipe_TunnelDiseaseCure : {
        "name": "Cure: Miner's Fever",
        "info": "Note imparting a disease cure recipe",
        "caption": "Torn page revealing a recipe for curing Miner's Fever.\n"
                   "\n"
                   "Complete the recipe to obtain a single-use cure for the disease.",
        "icon": 288,  # Note: Flask of Wondrous Physick
        "item_lots": [  # Tunnels boss rewards after Limgrave
            20622,  # Raya Lucaria
            20631,  # Old Altus
            20641,  # Sealed
            20652,  # Altus
            20662,  # Gael
            20674,  # Sellia Crystal
            # Yelough Anix omitted (drops Very Rare staff recipe book instead)
        ],
        "bought_flag": Flags.Recipe_TunnelDiseaseCure_Bought,
        "category": ModSubcategory.Diseases,
    },
    # endregion

    # region Weapon Recipe Notes
    NotesRecipes.Note_SerpentHunter: {
        "name": "Note: The Serpent-Hunter",
        "info": "Note imparting knowledge in brief",
        "caption": "Bloodstained note imparting knowledge in brief.\n"
                   "\n"
                   "\"We found the great serpent-slaying spear, but alas... Our Lord devoured it, along with the rest "
                   "of our mutinous band.\n"
                   "\n"
                   "Ye who reads my final words, I implore you. Forge another spear, and preserve what little remains "
                   "of our Lord's honor.\"",
        "icon": 294,  # Note: Below the Capital
        "item_lot": 16000690,  # old Serpent-Hunter location (deleted prior to this addition)
        "bought_flag": Flags.Note_SerpentHunter_Bought,
        "category": ModSubcategory.Weapons,
    },
    NotesRecipes.Note_Whip: {
        "name": "Note: Whip",
        "info": "Note imparting knowledge in brief",
        "caption": "Discarded note imparting knowledge in brief.\n"
                   "\n"
                   "It describes a means of fabricating a deadly whip known only to the Volcano Manor.",
        "icon": 294,  # Note: Below the Capital
        "item_lot": 16000611,  # with former Smoldering Shield
        "bought_flag": Flags.Note_Whip_Bought,
        "category": ModSubcategory.Weapons,
    },
    NotesRecipes.Recipe_SteelWireTorch: {
        "name": "Note: Steel-Wire Torch",
        "info": "Note imparting knowledge in brief",
        "caption": "Discarded note imparting knowledge in brief.\n"
                   "\n"
                   "It describes a means of crafting a more potent torch.",
        "icon": 294,
        "shop_rows": [
            100003,  # Gostoc
        ],
        "cost": 800,
        "bought_flag": Flags.Recipe_SteelWireTorch_Bought,
        "category": ModSubcategory.Weapons,
    },
    NotesRecipes.Recipe_StTrinasTorch: {
        "name": "Note: St. Trina's Torch",
        "info": "Note imparting knowledge in brief",
        "caption": "Discarded note imparting knowledge in brief.\n"
                   "\n"
                   "It describes a means of crafting a more potent torch.",
        "icon": 294,
        "item_lot": 1047400911,  # with former Sword of St. Trina
        "bought_flag": Flags.Recipe_StTrinasTorch_Bought,
        "category": ModSubcategory.Weapons,
    },
    NotesRecipes.Recipe_GhostflameTorch: {
        "name": "Note: Ghostflame Torch",
        "info": "Note imparting knowledge in brief",
        "caption": "Discarded note imparting knowledge in brief.\n"
                   "\n"
                   "It describes a means of crafting a more potent torch.",
        "icon": 294,
        "item_lot": 12070501,  # with former Ghostflame Torch
        "bought_flag": Flags.Recipe_GhostflameTorch_Bought,
        "category": ModSubcategory.Weapons,
    },
    NotesRecipes.Recipe_BeastRepellentTorch: {
        "name": "Note: Beast-Repellent Torch",
        "info": "Note imparting knowledge in brief",
        "caption": "Discarded note imparting knowledge in brief.\n"
                   "\n"
                   "It describes a means of crafting a more potent torch.",
        "icon": 294,
        "item_lot": 1047380701,  # with Ash of War: Lion's Claw
        "bought_flag": Flags.Recipe_BeastRepellentTorch_Bought,
        "category": ModSubcategory.Weapons,
    },
    NotesRecipes.Recipe_SentrysTorch: {
        "name": "Note: Sentry's Torch",
        "info": "Note imparting knowledge in brief",
        "caption": "Discarded note imparting knowledge in brief.\n"
                   "\n"
                   "It describes a means of crafting a more potent torch.",
        "icon": 294,
        "item_lot": 1048550601,  # with Stalwart Horn Charm +1
        "bought_flag": Flags.Recipe_SentrysTorch_Bought,
        "category": ModSubcategory.Weapons,
    },
    # endregion
}


NEW_RECIPE_BOOKS = {
    # region Survival Recipes
    NotesRecipes.Recipes_CommonSurvival: {
        "name": "Survivalist's Cookbook [1]",
        "info": "Expands crafting repertoire",
        "caption": "A record of crafting techniques left by keen survivalists.\n"
                   "Contains knowledge for enduring life in the Lands Between.\n"
                   "\n"
                   "Acquire the knowledge to craft the following:\n"
                   "\n"
                   "- Raw/Seared Steak, Bone Broth\n"
                   "- Mushroom Stew, Forest Berry Medley\n"
                   "- Mossdew Soup, Amber-Eye Brew",
        "icon": 3122,  # Missionary's Cookbook [1]
        "shop_row": 100508,  # Kale
        "cost": 300,
        "bought_flag": Flags.Recipes_CommonSurvival_Bought,
        "category": ModSubcategory.Survival,
    },
    NotesRecipes.Recipes_UncommonSurvival: {
        "name": "Survivalist's Cookbook [2]",
        "info": "Expands crafting repertoire",
        "caption": "A record of crafting techniques left by keen survivalists.\n"
                   "Contains knowledge for enduring life in the Lands Between.\n"
                   "\n"
                   "Acquire the knowledge to craft the following:\n"
                   "\n"
                   "- Jar Brittle, Great Bone Broth\n"
                   "- Melted Mushroom Stew, Plateau Berry Medley\n"
                   "- Crystal Shard Soup, Magmatic Brew",
        "icon": 3122,  # Missionary's Cookbook [1]
        "shop_rows": [
            100638,  # Merchant - Liurnia of the Lakes
            100666,  # Isolated Merchant - Weeping Peninsula
            100846,  # Merchant - South Caelid
        ],
        "cost": 1500,
        "bought_flag": Flags.Recipes_UncommonSurvival_Bought,
        "category": ModSubcategory.Survival,
    },
    NotesRecipes.Recipes_RareSurvival: {
        "name": "Survivalist's Cookbook [3]",
        "info": "Expands crafting repertoire",
        "caption": "A record of crafting techniques left by keen survivalists.\n"
                   "Contains knowledge for enduring life in the Lands Between.\n"
                   "\n"
                   "Acquire the knowledge to craft the following:\n"
                   "\n"
                   "- Raw/Seared Liver Steak, Blood Broth\n"
                   "- Mountain Berry Medley\n"
                   "- Giant's Soup, Blossom Brew",
        "icon": 3122,  # Missionary's Cookbook [1]
        "shop_rows": [
            100779,  # Merchant - Mt. Gelmir
            100755,  # Merchant - Altus Plateau
        ],
        "cost": 3000,
        "bought_flag": Flags.Recipes_RareSurvival_Bought,
        "category": ModSubcategory.Survival,
    },
    NotesRecipes.Recipes_VeryRareSurvival: {
        "name": "Survivalist's Cookbook [4]",
        "info": "Expands crafting repertoire",
        "caption": "A record of crafting techniques left by determined survivalists.\n"
                   "Contains knowledge of forbidden life-extending draughts.\n"
                   "\n"
                   "Acquire the knowledge to craft the following:\n"
                   "\n"
                   "- Draught of Satiation\n"
                   "- Draught of Silver Tears",
        "icon": 3122,  # Missionary's Cookbook [1]
        "shop_rows": [
            100744,  # Hermit Merchant - Leyndell
            100920,  # Merchant - Mountaintops
        ],
        "cost": 8000,
        "bought_flag": Flags.Recipes_VeryRareSurvival_Bought,
        "category": ModSubcategory.Survival,
    },
    # endregion

    # region Shield Recipes
    NotesRecipes.Recipes_WoodenSmallShields: {
        "name": "Small Shield Smithbook [1]",
        "info": "Expands shield-smithing repertoire",
        "caption": "A record of crafting techniques left by wandering smiths.\n"
                   "Contains knowledge for surviving enemy attacks.\n"
                   "\n"
                   "Acquire the knowledge to craft wooden small shields.",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100512,  # Kale
        ],
        "cost": 500,
        "bought_flag": Flags.Recipes_WoodenSmallShields_Bought,
        "category": ModSubcategory.Weapons,
    },
    NotesRecipes.Recipes_MetalSmallShields: {
        "name": "Small Shield Smithbook [2]",
        "info": "Expands shield-smithing repertoire",
        "caption": "A record of crafting techniques left by wandering smiths.\n"
                   "Contains knowledge for surviving enemy attacks.\n"
                   "\n"
                   "Acquire the knowledge to craft metal small shields.",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100019,  # Gostoc
            100568,  # Merchant - East Limgrave
            100929,  # Merchant - Siofra
        ],
        "cost": 2000,
        "bought_flag": Flags.Recipes_MetalSmallShields_Bought,
        "category": ModSubcategory.Weapons,
    },
    NotesRecipes.Recipes_RareSmallShields: {
        "name": "Small Shield Smithbook [3]",
        "info": "Expands shield-smithing repertoire",
        "caption": "A record of crafting techniques left by wandering smiths.\n"
                   "Contains knowledge for surviving enemy attacks.\n"
                   "\n"
                   "Acquire the knowledge to craft rare or unique small shields.",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100745,  # Hermit Merchant - Leyndell
            100955,  # Merchant - Ainsel
        ],
        "cost": 5000,
        "bought_flag": Flags.Recipes_RareSmallShields_Bought,
        "category": ModSubcategory.Weapons,
    },
    NotesRecipes.Recipes_VeryRareSmallShields: {
        "name": "Small Shield Smithbook [4]",
        "info": "Expands shield-smithing repertoire",
        "caption": "A record of crafting techniques left by wandering smiths.\n"
                   "Contains knowledge for surviving enemy attacks.\n"
                   "\n"
                   "Acquire the knowledge to craft very rare small shields.",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100988,  # Imprisoned Merchant - Mohgwyn
        ],
        "cost": 8000,
        "bought_flag": Flags.Recipes_VeryRareSmallShields_Bought,
        "category": ModSubcategory.Weapons,
    },

    NotesRecipes.Recipes_CommonMediumShields: {
        "name": "Medium Shield Smithbook [1]",
        "info": "Expands shield-smithing repertoire",
        "caption": "A record of crafting techniques left by wandering smiths.\n"
                   "Contains knowledge for surviving enemy attacks.\n"
                   "\n"
                   "Acquire the knowledge to craft basic medium shields.",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100548,  # Merchant - North Limgrave
            100619,  # Merchant - East Weeping Peninsula
        ],
        "cost": 1000,
        "bought_flag": Flags.Recipes_CommonMediumShields_Bought,
        "category": ModSubcategory.Weapons,
    },
    NotesRecipes.Recipes_WoodenMediumShields: {
        "name": "Medium Shield Smithbook [2]",
        "info": "Expands shield-smithing repertoire",
        "caption": "A record of crafting techniques left by wandering smiths.\n"
                   "Contains knowledge for surviving enemy attacks.\n"
                   "\n"
                   "Acquire the knowledge to craft wooden medium shields.",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100597,  # Merchant - Coastal Cave
            100558,  # Merchant - East Limgrave
        ],
        "cost": 2000,
        "bought_flag": Flags.Recipes_WoodenMediumShields_Bought,
        "category": ModSubcategory.Weapons,
    },
    NotesRecipes.Recipes_HeaterMediumShields: {
        "name": "Medium Shield Smithbook [3]",
        "info": "Expands shield-smithing repertoire",
        "caption": "A record of crafting techniques left by wandering smiths.\n"
                   "Contains knowledge for surviving enemy attacks.\n"
                   "\n"
                   "Acquire the knowledge to craft medium heater shields.",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100721,  # Merchant - North Liurnia
        ],
        "cost": 5000,
        "bought_flag": Flags.Recipes_HeaterMediumShields_Bought,
        "category": ModSubcategory.Weapons,
    },
    NotesRecipes.Recipes_KiteMediumShields: {
        "name": "Medium Shield Smithbook [4]",
        "info": "Expands shield-smithing repertoire",
        "caption": "A record of crafting techniques left by wandering smiths.\n"
                   "Contains knowledge for surviving enemy attacks.\n"
                   "\n"
                   "Acquire the knowledge to craft medium kite shields.",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100778,  # Merchant - Mt. Gelmir
        ],
        "cost": 6000,
        "bought_flag": Flags.Recipes_KiteMediumShields_Bought,
        "category": ModSubcategory.Weapons,
    },
    NotesRecipes.Recipes_RareMediumShields: {
        "name": "Medium Shield Smithbook [5]",
        "info": "Expands shield-smithing repertoire",
        "caption": "A record of crafting techniques left by wandering smiths.\n"
                   "Contains knowledge for surviving enemy attacks.\n"
                   "\n"
                   "Acquire the knowledge to craft very rare medium shields.",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100969,  # Merchant - Ainsel River
            100895,  # Isolated Merchant - Dragonbarrow
        ],
        "cost": 9000,
        "bought_flag": Flags.Recipes_RareMediumShields_Bought,
        "category": ModSubcategory.Weapons,
    },

    NotesRecipes.Recipes_CommonGreatshields: {
        "name": "Greatshield Smithbook [1]",
        "info": "Expands shield-smithing repertoire",
        "caption": "A record of crafting techniques left by wandering smiths.\n"
                   "Contains knowledge for surviving enemy attacks.\n"
                   "\n"
                   "Acquire the knowledge to craft basic greatshields.",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100639,  # Merchant - Liurnia of the Lakes
        ],
        "cost": 2000,
        "bought_flag": Flags.Recipes_CommonGreatshields_Bought,
        "category": ModSubcategory.Weapons,
    },
    NotesRecipes.Recipes_UncommonGreatshields: {
        "name": "Greatshield Smithbook [2]",
        "info": "Expands shield-smithing repertoire",
        "caption": "A record of crafting techniques left by wandering smiths.\n"
                   "Contains knowledge for surviving enemy attacks.\n"
                   "\n"
                   "Acquire the knowledge to craft uncommon greatshields.",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100754,  # Merchant - Altus Plateau
        ],
        "cost": 5000,
        "bought_flag": Flags.Recipes_UncommonGreatshields_Bought,
        "category": ModSubcategory.Weapons,
    },
    NotesRecipes.Recipes_RareGreatshields: {
        "name": "Greatshield Smithbook [3]",
        "info": "Expands shield-smithing repertoire",
        "caption": "A record of crafting techniques left by wandering smiths.\n"
                   "Contains knowledge for surviving enemy attacks.\n"
                   "\n"
                   "Acquire the knowledge to craft rare greatshields.",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100904,  # Merchant - Mountaintops
        ],
        "cost": 8000,
        "bought_flag": Flags.Recipes_RareGreatshields_Bought,
        "category": ModSubcategory.Weapons,
    },
    NotesRecipes.Recipes_VeryRareGreatshields: {
        "name": "Greatshield Smithbook [4]",
        "info": "Expands shield-smithing repertoire",
        "caption": "A record of crafting techniques left by wandering smiths.\n"
                   "Contains knowledge for surviving enemy attacks.\n"
                   "\n"
                   "Acquire the knowledge to craft very rare greatshields.",
        "icon": 3119,  # Nomadic Warrior's Cookbook
        "shop_rows": [
            100979,  # Imprisoned Merchant - Mohgwyn
        ],
        "cost": 10000,
        "bought_flag": Flags.Recipes_VeryRareGreatshields_Bought,
        "category": ModSubcategory.Weapons,
    },
    # endregion

    # region Staff/Seal Recipes
    NotesRecipes.Recipes_CommonStaffs: {
        "name": "Glintstone Staff Craftbook [1]",
        "info": "Expands staff-crafting repertoire",
        "caption": "A record of crafting techniques left by nomadic mages.\n"
                   "Contains knowledge for creating tools of sorcery.\n"
                   "\n"
                   "Acquire the knowledge to craft common glintstone staves.",
        "icon": 3121,
        "shop_rows": [
            100063,  # Sorceress Sellen
            100203,  # Sorcerer Rogier
        ],
        "cost": 1000,
        "bought_flag": Flags.Recipes_CommonStaffs_Bought,
        "category": ModSubcategory.Weapons,
    },
    NotesRecipes.Recipes_UncommonStaffs: {
        "name": "Glintstone Staff Craftbook [2]",
        "info": "Expands staff-crafting repertoire",
        "caption": "A record of crafting techniques left by nomadic mages.\n"
                   "Contains knowledge for creating tools of sorcery.\n"
                   "\n"
                   "Acquire the knowledge to craft uncommon glintstone staves.",
        "icon": 3121,
        "shop_rows": [
            100679,  # Merchant - Academy of Raya Lucaria
        ],
        "cost": 4000,
        "bought_flag": Flags.Recipes_UncommonStaffs_Bought,
        "category": ModSubcategory.Weapons,
    },
    NotesRecipes.Recipes_RareStaffs: {
        "name": "Glintstone Staff Craftbook [3]",
        "info": "Expands staff-crafting repertoire",
        "caption": "A record of crafting techniques left by nomadic mages.\n"
                   "Contains knowledge for creating tools of sorcery.\n"
                   "\n"
                   "Acquire the knowledge to craft rare glintstone staves.",
        "icon": 3121,
        "shop_rows": [
            100253,  # Preceptor Seluvis
            100178,  # Gowry
        ],
        "cost": 8000,
        "bought_flag": Flags.Recipes_RareStaffs_Bought,
        "category": ModSubcategory.Weapons,
    },
    NotesRecipes.Recipes_VeryRareStaffs: {
        "name": "Glintstone Staff Craftbook [4]",
        "info": "Expands staff-crafting repertoire",
        "caption": "A record of crafting techniques left by nomadic mages.\n"
                   "Contains knowledge for creating tools of sorcery.\n"
                   "\n"
                   "Acquire the knowledge to craft very rare glintstone staves.",
        "icon": 3121,
        "item_lot": 20682,  # Yelough Anix boss reward
        "bought_flag": Flags.Recipes_VeryRareStaffs_Bought,
        "category": ModSubcategory.Weapons,
    },
    NotesRecipes.Recipes_UncommonSeals: {
        "name": "Sacred Seal Craftbook [1]",
        "info": "Expands seal-crafting repertoire",
        "caption": "A record of crafting techniques left by devout artisans.\n"
                   "Contains knowledge for creating sacred seals for incantations.\n"
                   "\n"
                   "Acquire the knowledge to craft uncommon sacred seals.",
        "icon": 3122,
        "item_lot": 10282,  # Fringefolk Hero's Grave boss reward
        "bought_flag": Flags.Recipes_UncommonSeals_Bought,
        "category": ModSubcategory.Weapons,
    },
    NotesRecipes.Recipes_RareSeals: {
        "name": "Sacred Seal Craftbook [2]",
        "info": "Expands seal-crafting repertoire",
        "caption": "A record of crafting techniques left by devout artisans.\n"
                   "Contains knowledge for creating sacred seals for incantations.\n"
                   "\n"
                   "Acquire the knowledge to craft rare sacred seals.",
        "icon": 3122,
        "shop_rows": [
            100408,  # Miriel
        ],
        "cost": 5000,
        "bought_flag": Flags.Recipes_RareSeals_Bought,
        "category": ModSubcategory.Weapons,
    },
    NotesRecipes.Recipes_VeryRareSeals: {
        "name": "Sacred Seal Craftbook [3]",
        "info": "Expands seal-crafting repertoire",
        "caption": "A record of crafting techniques left by devout artisans.\n"
                   "Contains knowledge for creating sacred seals for incantations.\n"
                   "\n"
                   "Acquire the knowledge to craft very rare sacred seals.",
        "icon": 3122,
        "item_lot": 20081,  # Sainted Hero's Grave boss reward
        "bought_flag": Flags.Recipes_VeryRareSeals_Bought,
        "category": ModSubcategory.Weapons,
    },
    # endregion
}


# Prices for replaced merchant items.
MERCHANT_PRICES = {
    Materials.SoftWood: 400,
    Materials.RefinedWood: 2500,
    Materials.StoneFragment: 500,  # not actually sold
    Materials.SomberStoneFragment: 1000,  # not actually sold
    Materials.MetalShards: 500,
    Materials.MetalPlate: 3000,
    Materials.PliableMetal: 8000,
    Materials.DragonTeeth: 9000,
    Materials.GruesomeBone: 7000,
    Materials.GlintstoneDust: 8000,
    Materials.ErdtreeAmber: 15000,
    Materials.MeteoriteChunk: 12000,
    Materials.BlackMark: 20000,
    Materials.ErdtreeWood: 10000,
    Materials.StaffPole: 3000,
    Materials.ShieldGrip: 1000,
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
    Materials.MetalShards: (MaterialRarity.Common, 4),
    Materials.MetalPlate: (MaterialRarity.Uncommon, 1),
    Materials.PliableMetal: (MaterialRarity.Rare, 1),
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


ALL_GOODS_DICTS = (
    NEW_CONSUMABLES,
    NEW_MATERIALS,
    NEW_SMITHS_HAMMERS,
    NEW_NOTES,
    NEW_RECIPE_BOOKS,
    DISEASE_INDICATORS,
)
