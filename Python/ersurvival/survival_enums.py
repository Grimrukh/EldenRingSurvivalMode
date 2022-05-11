from soulstruct.game_types import *


BASE_FLAG = 8000


class SurvivalText(IntEnum):
    """Map event text, mostly."""
    MildHeatWarning = 50000
    ModerateHeatWarning = 50001
    SevereHeatWarning = 50002
    MildColdWarning = 50003
    ModerateColdWarning = 50004
    SevereColdWarning = 50005


class SurvivalFlags(Flag):
    """Flags used by Survival Mode.

    TODO: Try to avoid using the same flags as Matt's randomizers.
    """
    GrowingHunger = BASE_FLAG + 0
    GrowingThirst = BASE_FLAG + 1

    CheckMildHeatArea = BASE_FLAG + 10
    MildHeatWarning = BASE_FLAG + 11
    ShowMildHeatWarning = BASE_FLAG + 12

    CheckModerateHeatArea = BASE_FLAG + 13
    ModerateHeatWarning = BASE_FLAG + 14
    ShowModerateHeatWarning = BASE_FLAG + 15

    CheckSevereHeatArea = BASE_FLAG + 16
    SevereHeatWarning = BASE_FLAG + 17
    ShowSevereHeatWarning = BASE_FLAG + 18

    CheckMildColdArea = BASE_FLAG + 19
    MildColdWarning = BASE_FLAG + 20
    ShowMildColdWarning = BASE_FLAG + 21

    CheckModerateColdArea = BASE_FLAG + 22
    ModerateColdWarning = BASE_FLAG + 23
    ShowModerateColdWarning = BASE_FLAG + 24

    CheckSevereColdArea = BASE_FLAG + 25
    SevereColdWarning = BASE_FLAG + 26
    ShowSevereColdWarning = BASE_FLAG + 27

    # Overworld area monitoring
    MonitorInLimgrave = BASE_FLAG + 40
    MonitorInLiurnia = BASE_FLAG + 41
    MonitorInCaelid = BASE_FLAG + 42
    MonitorInAltus = BASE_FLAG + 43
    MonitorInMtGelmir = BASE_FLAG + 44
    MonitorInMountaintops = BASE_FLAG + 45
    PlayerInLimgrave = BASE_FLAG + 50
    PlayerInLiurnia = BASE_FLAG + 51
    PlayerInCaelid = BASE_FLAG + 52
    PlayerInAltus = BASE_FLAG + 53
    PlayerInMtGelmir = BASE_FLAG + 54
    PlayerInMountaintops = BASE_FLAG + 55

    GetDiseaseOverworld = BASE_FLAG + 60  # 10 slots
    GetDiseaseLegacyDungeon = BASE_FLAG + 70  # 10 slots
    GetDiseaseSiofra = BASE_FLAG + 80
    GetDiseaseAinsel = BASE_FLAG + 81
    GetDiseaseDeeprootAstel = BASE_FLAG + 82
    GetDiseaseRadahn = BASE_FLAG + 83
    GetDiseaseCatacombs = BASE_FLAG + 84
    GetDiseaseCaves = BASE_FLAG + 85
    GetDiseaseTunnels = BASE_FLAG + 86
    GetPureScarletRot = BASE_FLAG + 87

    CurePlague = BASE_FLAG + 90
    CureToxin = BASE_FLAG + 91
    CureFever = BASE_FLAG + 92
    CureParasite = BASE_FLAG + 93
    CurePureScarletRot = BASE_FLAG + 94

    DiseaseRollLock = BASE_FLAG + 99
    DiseaseRollFirst = BASE_FLAG + 100
    DiseaseRollSecond = BASE_FLAG + 101
    DiseaseRollLast = BASE_FLAG + 199

    # Active disease status is tracked using possession of key items, not flags.
    LimgraveDiseaseOnce = BASE_FLAG + 200
    LimgraveDiseaseTwice = BASE_FLAG + 201
    LiurniaDiseaseOnce = BASE_FLAG + 202
    LiurniaDiseaseTwice = BASE_FLAG + 203
    CaelidDiseaseOnce = BASE_FLAG + 204
    CaelidDiseaseTwice = BASE_FLAG + 205
    AltusDiseaseOnce = BASE_FLAG + 206
    AltusDiseaseTwice = BASE_FLAG + 207
    MtGelmirDiseaseOnce = BASE_FLAG + 208
    MtGelmirDiseaseTwice = BASE_FLAG + 209
    MountaintopsDiseaseOnce = BASE_FLAG + 210
    MountaintopsDiseaseTwice = BASE_FLAG + 211
    SiofraDiseaseOnce = BASE_FLAG + 214
    SiofraDiseaseTwice = BASE_FLAG + 215
    AinselDiseaseOnce = BASE_FLAG + 216
    AinselDiseaseTwice = BASE_FLAG + 217
    DeeprootDiseaseOnce = BASE_FLAG + 218
    DeeprootDiseaseTwice = BASE_FLAG + 219
    StormveilDiseaseOnce = BASE_FLAG + 220
    StormveilDiseaseTwice = BASE_FLAG + 221
    RayaLucariaDiseaseOnce = BASE_FLAG + 222
    RayaLucariaDiseaseTwice = BASE_FLAG + 223
    RadahnDiseaseOnce = BASE_FLAG + 224
    RadahnDiseaseTwice = BASE_FLAG + 225
    VolcanoManorDiseaseOnce = BASE_FLAG + 226
    VolcanoManorDiseaseTwice = BASE_FLAG + 227
    LeyndellDiseaseOnce = BASE_FLAG + 228
    LeyndellDiseaseTwice = BASE_FLAG + 229
    SewersDiseaseOnce = BASE_FLAG + 230
    SewersDiseaseTwice = BASE_FLAG + 231
    HaligtreeDiseaseOnce = BASE_FLAG + 232
    HaligtreeDiseaseTwice = BASE_FLAG + 233
    FarumAzulaDiseaseOnce = BASE_FLAG + 234
    FarumAzulaDiseaseTwice = BASE_FLAG + 235
    MohgwynDiseaseOnce = BASE_FLAG + 236
    MohgwynDiseaseTwice = BASE_FLAG + 237
    CatacombsDiseaseOnce = BASE_FLAG + 238
    CatacombsDiseaseTwice = BASE_FLAG + 239
    CaveDiseaseOnce = BASE_FLAG + 240
    CaveDiseaseTwice = BASE_FLAG + 241
    TunnelDiseaseOnce = BASE_FLAG + 242
    TunnelDiseaseTwice = BASE_FLAG + 243

    PureScarletRotOnce = BASE_FLAG + 250


class VanillaFlags(Flag):
    RadahnBattleActive = 1  # TODO


class VanillaCharacters(Character):
    Radahn = 1  # TODO


class SurvivalEffects(SpecialEffectParam):
    """TODO: Dummy numbering for now."""

    # Fifteen hunger levels, each reducing max HP by an addition 5%.
    # Hunger level increases once per minute. Lower hunger levels are better.
    Hunger1 = 40001  # 5% max HP loss
    Hunger2 = 40002
    Hunger3 = 40003
    Hunger4 = 40004
    Hunger5 = 40005
    Hunger6 = 40006
    Hunger7 = 40007
    Hunger8 = 40008
    Hunger9 = 40009
    Hunger10 = 40010
    Hunger11 = 40011
    Hunger12 = 40012
    Hunger13 = 40013
    Hunger14 = 40014
    Hunger15 = 40015  # 75% max HP loss

    # Nine thirst levels, each reducing max FP by an additional 10%.
    # Thirst level increases once per 100 seconds. Lower thirst levels are better.
    # At maximum thirst, HP will also slowly drain.
    Thirst1 = 40021
    Thirst2 = 40022
    Thirst3 = 40023
    Thirst4 = 40024
    Thirst5 = 40025
    Thirst6 = 40026
    Thirst7 = 40027
    Thirst8 = 40028
    Thirst9 = 40029  # also drains HP slowly (probably slightly less than poison)

    # Three heat levels (mild, moderate, severe).
    Heat_Mild = 52100  # slow HP drain (like poison), thirst slightly accelerated
    Heat_Moderate = 52101  # medium HP drain (like scarlet rot), thirst moderately accelerated
    Heat_Severe = 52102  # fast HP drain (worse than scarlet rot), thirst greatly accelerated

    # Three heat protection levels, which downgrade any heat effects by 1, 2, or 3.
    HeatProtection_Mild = 52200
    HeatProtection_Moderate = 52201
    HeatProtection_Severe = 52202
    # TODO: If any magic effects provide protection, just check those manually in EMEVD too.

    # Three cold levels (mild, moderate, severe).
    Cold_Mild = 52150  # slow stamina regen, slightly reduced defense
    Cold_Moderate = 52151  # medium stamina regen, moderately reduced defense
    Cold_Severe = 52152  # almost no stamina regen, greatly reduced defense

    # Three cold protection levels, which downgrade any cold effects by 1, 2, or 3.
    ColdProtection_Mild = 52250
    ColdProtection_Moderate = 52251
    ColdProtection_Severe = 52252
    # TODO: If any magic effects provide protection, just check those manually in EMEVD too.

    # TODO: Merchants sell notes containing information about local diseases.
    #  They indicate the type of disease (plague, toxin, parasite, or fever) and hint at its effects.

    # TODO: Recipe books for the four main disease cures are awarded by certain bosses.
    #  Maybe multiple bosses drop each one.
    #  Pure Scarlet Rot's cure can be found in a particular dungeon, with a hint to it sold by a merchant in Caelid.

    # Overworld diseases
    LimgravePlague = 53000
    LiurniaToxin = 53001
    CaelidParasite = 53002
    AltusFever = 53003
    MtGelmirPlague = 53004
    MountaintopsParasite = 53005
    SiofraPlague = 53006  # also Nokron
    AinselToxin = 53007  # also Nokstella
    DeeprootParasite = 53008  # also Astel arena

    # Legacy dungeon diseases
    StormveilPlague = 53009
    RayaLucariaToxin = 53010  # maybe also Caria Manor
    RadahnFever = 53011  # only afflicted by Radahn; higher proc chance
    VolcanoManorToxin = 53012
    LeyndellPlague = 53013  # no disease in Ashen Capital
    SewersParasite = 53014
    HaligtreePlague = 53015
    FarumAzulaFever = 53016
    MohgwynFever = 53017

    # Generic dungeon diseases
    CatacombsToxin = 53018
    CaveParasite = 53019
    TunnelFever = 53020  # relatively harmless, as it may take a while to find a cure for Fever
    # No Divine Tower disease.
    # TODO: Maybe some special exceptions, like a Frenzy disease in Yelough Anix Tunnel, etc.

    # Pure Scarlet Rot
    PureScarletRot = 53050
    PureScarletRotItem = 53051  # player re-infects themselves with item

    # Disease cures
    PlagueCure = 53100
    ToxinCure = 53101
    FeverCure = 53102
    ParasiteCure = 53103
    PureScarletRotCure = 53104

    # TODO: Effects for all the different new items, as well as crafting recipes.
    # TODO: EMEVD also checks for existing effects (e.g., cured meat) to change hunger/thirst.
    # TODO: Merchant slots for recipe items.

    # Hunger/thirst only.
    RawSteak = 51900  # 3x Sliver of Meat. Sold by first merchant (Kale).
    SearedSteak = 51901  # 3x Sliver of Meat, 2x Smoldering Butterfly. Sold by first merchant (Kale).
    RawLiverSteak = 51902  # 2x Sliver of Meat, 1x Beast Liver. Sold by ???.
    SearedLiverSteak = 51903  # 2x Sliver of Meat, 1x Beast Liver, 2x Smoldering Butterfly. Sold by ???.
    BoneBroth = 51904  # 5x Thin Beast Bones, Cracked Pot.
    GreatBoneBroth = 51905  # 3x Hefty Beast Bones, Ritual Pot.
    BloodBroth = 51906  # 2x Beast Blood, Ritual Pot.
    BerryMedley1 = 51907  # 10x Rowa Fruit, ???.
    BerryMedley2 = 51908  # 10x Golden Rowa, ???.
    BerryMedley3 = 51909  # 10x Rimed Rowa, ???.
    MushroomStew = 51910  # 3x Mushroom, 1x Herba, Cracked Pot.
    MeltedMushroomStew = 51911  # 3x Melted Mushroom, ???, Cracked Pot.
    DraughtOfTheUndining = 51912  # ???, 3x Grave Violet, ???, Ritual Pot.
    DraughtOfSilverTears = 51913  # 5x Silver Tear Husk, ???, Ritual Pot.

    # Temperature protection.
    MossdewSoup = 51914  # 3x Cave Moss, 5x Dewkissed Herba, Cracked Pot.
    CrystalShardSoup = 51915  # 5x Cracked Crystal, ???, Cracked Pot.
    GiantsSoup = 51916  # 5x Rimed Rowa, 2x Crystal Cave Moss, 2x Rimed Crystal Bud, Ritual Pot.
    AmberEyeBrew = 51917  # 3x Eye of Yelough, 1x Yellow Amber, 3x Herba, Cracked Pot.
    MagmaticBrew = 51918  # 4x Volcanic Stone, 3x Tarnished Golden Sunflowers, Cracked Pot.
    BlossomBrew = 51919  # 5x Fire Blossom, 3x Formic Rock, Ritual Pot.
    JarBrittle = 51920  # 5x Living Jar Shards, ???. (no pot)


class CraftingMaterials(IntEnum):
    """These are in order of in-game sort ID."""
    SliverOfMeat = 15000
    StripOfWhiteFlesh = 15160
    BeastLiver = 15010
    LumpOfFlesh = 15020
    TurtleNeckMeat = 15090
    BeastBlood = 15030
    AlbinauricBloodclot = 15420
    BuddingHorn = 15050
    OldFang = 15040
    FlightPinion = 15060
    StormhawkFeather = 15430
    FourToedFowlFoot = 15080
    SlumberingEgg = 15120
    CrabEggs = 15130
    LandOctopusOvary = 15140
    ThinBeastBones = 15340
    HeftyBeastBone = 15341
    HumanBoneShard = 15100
    GreatDragonflyHead = 15110
    GoldFirefly = 20811
    SilverFirefly = 20810
    GlintstoneFirefly = 20812
    SmolderingButterfly = 20802
    AeonianButterfly = 20801
    NascentButterfly = 20800
    GoldenCentipede = 20820
    LivingJarShard = 15410
    SilverTearHusk = 20825
    GoldTingedExcrement = 20830
    BloodTaintedExcrement = 20831
    YellowEmber = 20845
    RowaFruit = 20720
    GoldenRowa = 20721
    RimedRowa = 20722
    Herba = 20690
    DewkissedHerba = 20710
    ArteriaLeaf = 20691
    Mushroom = 20760
    ToxicMushroom = 20770
    MeltedMushroom = 20761
    ErdleafFlower = 20680
    FadedErdleafFlower = 20660
    FireBlossom = 20682
    Poisonbloom = 20650
    Fulgurbloom = 20652
    AltusBloom = 20681
    Bloodrose = 20723
    GraveViolet = 20654
    TarnishedGoldenSunflower = 20685
    GoldenSunflower = 20683
    TrinasLily = 20651
    MiquellasLily = 20653
    CrystalBud = 20750
    RimedCrystalBud = 20751
    SacramentalBud = 20753
    EyeOfYelough = 20740
    MirandaPowder = 15150
    RootResin = 20775
    CaveMoss = 20840
    BuddingCaveMoss = 20841
    CrystalCaveMoss = 20842
    String = 15400
    SanctuaryStone = 20795
    CrackedCrystal = 20780
    VolcanicStone = 20850
    FormicRock = 20852
    GravelStone = 20855
