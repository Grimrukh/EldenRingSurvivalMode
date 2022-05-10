from soulstruct.game_types import *


class SurvivalFlags(Flag):
    """Flags used by Survival Mode.

    TODO: Try to avoid using the same flags as Matt's randomizers.
    """
    # TODO: 100-flag range for disease proc.
    #  Most diseases have a 2/100 change (first time), then 1/100 (second time), then zero.

    # TODO: Flags to track how many times each disease has been caught (for above).

    ShowMildHeatWarning = 1
    ShowModerateHeatWarning = 2
    ShowSevereHeatWarning = 3
    ShowMildColdWarning = 4
    ShowModerateColdWarning = 5
    ShowSevereColdWarning = 6

    # Overworld area monitoring
    PlayerInLimgrave = 50
    PlayerInLiurnia = 51
    PlayerInCaelid = 52
    PlayerInAltus = 53
    PlayerInMtGelmir = 54
    PlayerInMountaintops = 55

    DiseaseRollLock = 99
    DiseaseRollFirst = 100
    DiseaseRollSecond = 101
    DiseaseRollLast = 199

    LimgraveDiseaseOnce = 200
    LimgraveDiseaseTwice = 201
    LiurniaDiseaseOnce = 202
    LiurniaDiseaseTwice = 203
    CaelidDiseaseOnce = 204
    CaelidDiseaseTwice = 205
    AltusDiseaseOnce = 206
    AltusDiseaseTwice = 207
    MtGelmirDiseaseOnce = 208
    MtGelmirDiseaseTwice = 209
    MountaintopsDiseaseOnce = 210
    MountaintopsDiseaseTwice = 211
    SiofraDiseaseOnce = 214
    SiofraDiseaseTwice = 215
    AinselDiseaseOnce = 216
    AinselDiseaseTwice = 217
    DeeprootDiseaseOnce = 218
    DeeprootDiseaseTwice = 219

    StormveilDiseaseOnce = 220
    StormveilDiseaseTwice = 221
    RayaLucariaDiseaseOnce = 222
    RayaLucariaDiseaseTwice = 223
    RadahnDiseaseOnce = 224
    RadahnDiseaseTwice = 225
    VolcanoManorDiseaseOnce = 226
    VolcanoManorDiseaseTwice = 227
    LeyndellDiseaseOnce = 228
    LeyndellDiseaseTwice = 229
    SewersDiseaseOnce = 230
    SewersDiseaseTwice = 231
    HaligtreeDiseaseOnce = 232
    HaligtreeDiseaseTwice = 233
    FarumAzulaDiseaseOnce = 234
    FarumAzulaDiseaseTwice = 235
    MohgwynDiseaseOnce = 236
    MohgwynDiseaseTwice = 237

    CatacombsDiseaseOnce = 238
    CatacombsDiseaseTwice = 239
    CaveDiseaseOnce = 240
    CaveDiseaseTwice = 241
    TunnelDiseaseOnce = 242
    TunnelDiseaseTwice = 243


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
