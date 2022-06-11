from __future__ import annotations

from soulstruct.game_types import *


# Stone Platform 1000 range
# TODO: There is seemingly one vanilla flag in this range that needs to be avoided:
#   19001100
BASE_FLAG = 19001000
BOUGHT_BASE_FLAG = 18001000  # no vanilla flags used in here
ALLOW_UPGRADE_BASE_FLAG = 11051000  # 377 slots in Stranded Graveyard; constantly monitored so no saving needed


class SurvivalText(IntEnum):
    """Map event text, mostly."""
    MildHeatWarning = 50000
    ModerateHeatWarning = 50001
    SevereHeatWarning = 50002
    MildColdWarning = 50003
    ModerateColdWarning = 50004
    SevereColdWarning = 50005

    # Dialog for disease cure usage
    CuredLimgraveDisease = 50010
    CuredLiurniaDisease = 50011
    CuredCaelidDisease = 50012
    CuredAltusDisease = 50013
    CuredMtGelmirDisease = 50014
    CuredMountaintopsDisease = 50015
    CuredSiofraDisease = 50016
    CuredAinselDisease = 50017
    CuredDeeprootDisease = 50018
    CuredStormveilDisease = 50019
    CuredRayaLucariaDisease = 50020
    CuredRadahnDisease = 50021
    CuredVolcanoManorDisease = 50022
    CuredLeyndellDisease = 50023
    CuredSewersDisease = 50024
    CuredHaligtreeDisease = 50025
    CuredFarumAzulaDisease = 50026
    CuredMohgwynDisease = 50027
    CuredCatacombsDisease = 50028
    CuredCaveDisease = 50029
    CuredTunnelDisease = 50030

    Dehydration = 50050


class Flags(Flag):
    """NEW flags and events used by Survival Mode."""
    GrowingHunger = BASE_FLAG + 0
    GrowingThirst = BASE_FLAG + 1
    PlayerPassedTime = BASE_FLAG + 2  # NOTE: Hard-coded in Grace ESD.
    HungerThirstAfterPassTime = BASE_FLAG + 3  # event

    HungerTick1 = BASE_FLAG + 10
    HungerTick2 = BASE_FLAG + 11
    HungerTick3 = BASE_FLAG + 12
    HungerTick4 = BASE_FLAG + 13
    HungerTick5 = BASE_FLAG + 14

    ThirstTick1 = BASE_FLAG + 15
    ThirstTick2 = BASE_FLAG + 16
    ThirstTick3 = BASE_FLAG + 17
    ThirstTick4 = BASE_FLAG + 18
    ThirstTick5 = BASE_FLAG + 19

    CheckMildHeatArea = BASE_FLAG + 20
    MildHeatWarning = BASE_FLAG + 21
    CheckModerateHeatArea = BASE_FLAG + 22
    ModerateHeatWarning = BASE_FLAG + 23
    CheckSevereHeatArea = BASE_FLAG + 24
    SevereHeatWarning = BASE_FLAG + 25
    CheckMildColdArea = BASE_FLAG + 26
    MildColdWarning = BASE_FLAG + 27
    CheckModerateColdArea = BASE_FLAG + 28
    ModerateColdWarning = BASE_FLAG + 29
    CheckSevereColdArea = BASE_FLAG + 30
    SevereColdWarning = BASE_FLAG + 31

    ShowMildHeatWarning = BASE_FLAG + 32
    ShowModerateHeatWarning = BASE_FLAG + 33
    ShowSevereHeatWarning = BASE_FLAG + 34
    ShowMildColdWarning = BASE_FLAG + 35
    ShowModerateColdWarning = BASE_FLAG + 36
    ShowSevereColdWarning = BASE_FLAG + 37

    # Overworld area monitoring
    MonitorInLimgrave = BASE_FLAG + 40
    MonitorInLiurnia = BASE_FLAG + 41
    MonitorInCaelid = BASE_FLAG + 42
    MonitorInAltus = BASE_FLAG + 43
    MonitorInMtGelmir = BASE_FLAG + 44
    MonitorInMountaintops = BASE_FLAG + 45
    MonitorInGenericDungeon = BASE_FLAG + 46
    MonitorInLegacyDungeon = BASE_FLAG + 47
    PlayerInLimgrave = BASE_FLAG + 50
    PlayerInLiurnia = BASE_FLAG + 51
    PlayerInCaelid = BASE_FLAG + 52
    PlayerInAltus = BASE_FLAG + 53
    PlayerInMtGelmir = BASE_FLAG + 54
    PlayerInMountaintops = BASE_FLAG + 55
    PlayerInGenericDungeon = BASE_FLAG + 56
    PlayerInLegacyDungeon = BASE_FLAG + 57

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
    CaveDiseaseInDaylight = BASE_FLAG + 88

    DiseaseRollLock = BASE_FLAG + 99
    # NOTE: Flag 19001100 is used in the vanilla game for something.
    DiseaseRollFirst = BASE_FLAG + 101
    DiseaseRollSecond = BASE_FLAG + 102
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

    RelieveHunger_1 = BASE_FLAG + 260
    RelieveHunger_2 = BASE_FLAG + 261
    RelieveHunger_3 = BASE_FLAG + 262
    RelieveHunger_4 = BASE_FLAG + 263
    RelieveHunger_5 = BASE_FLAG + 264
    RelieveHunger_6 = BASE_FLAG + 265
    RelieveHunger_7 = BASE_FLAG + 266
    RelieveHunger_8 = BASE_FLAG + 267

    RelieveThirst_1 = BASE_FLAG + 270
    RelieveThirst_2 = BASE_FLAG + 271
    RelieveThirst_3 = BASE_FLAG + 272
    RelieveThirst_4 = BASE_FLAG + 273
    RelieveThirst_5 = BASE_FLAG + 274
    RelieveThirst_6 = BASE_FLAG + 275
    RelieveThirst_7 = BASE_FLAG + 276
    IncreaseThirst_1 = BASE_FLAG + 277
    IncreaseThirst_3 = BASE_FLAG + 278

    JarBrittleEffects = BASE_FLAG + 280

    # Disease note/cures
    Note_CuringDiseases_Bought = BASE_FLAG + 299
    # Recipe_LimgraveDiseaseCure_Bought = BASE_FLAG + 300  # TODO: For Lobos
    Recipe_LimgraveDiseaseCure_Bought = BOUGHT_BASE_FLAG + 10 * 0
    Recipe_LiurniaDiseaseCure_Bought = BOUGHT_BASE_FLAG + 10 * 1
    # Recipe_CaelidDiseaseCure_Bought = BASE_FLAG + 302  # TODO: For Lobos
    Recipe_CaelidDiseaseCure_Bought = BOUGHT_BASE_FLAG + 10 * 2
    Recipe_AltusDiseaseCure_Bought = BOUGHT_BASE_FLAG + 10 * 3
    Recipe_MtGelmirDiseaseCure_Bought = BOUGHT_BASE_FLAG + 10 * 4
    Recipe_MountaintopsDiseaseCure_Bought = BOUGHT_BASE_FLAG + 10 * 5
    Recipe_SiofraDiseaseCure_Bought = BOUGHT_BASE_FLAG + 10 * 6
    Recipe_AinselDiseaseCure_Bought = BOUGHT_BASE_FLAG + 10 * 7
    Recipe_DeeprootDiseaseCure_Bought = BOUGHT_BASE_FLAG + 10 * 8
    Recipe_StormveilDiseaseCure_Bought = BOUGHT_BASE_FLAG + 10 * 9
    Recipe_RayaLucariaDiseaseCure_Bought = BOUGHT_BASE_FLAG + 10 * 10
    Recipe_RadahnDiseaseCure_Bought = BOUGHT_BASE_FLAG + 10 * 11
    Recipe_VolcanoManorDiseaseCure_Bought = BOUGHT_BASE_FLAG + 10 * 12
    Recipe_LeyndellDiseaseCure_Bought = BOUGHT_BASE_FLAG + 10 * 13
    Recipe_SewersDiseaseCure_Bought = BOUGHT_BASE_FLAG + 10 * 14
    Recipe_HaligtreeDiseaseCure_Bought = BOUGHT_BASE_FLAG + 10 * 15
    Recipe_FarumAzulaDiseaseCure_Bought = BOUGHT_BASE_FLAG + 10 * 16
    Recipe_MohgwynDiseaseCure_Bought = BOUGHT_BASE_FLAG + 10 * 17
    Recipe_CatacombsDiseaseCure_Bought = BOUGHT_BASE_FLAG + 10 * 18
    # Recipe_CaveDiseaseCure_Bought = BASE_FLAG + 319  # TODO: For Lobos
    Recipe_CaveDiseaseCure_Bought = BOUGHT_BASE_FLAG + 10 * 19
    Recipe_TunnelDiseaseCure_Bought = BOUGHT_BASE_FLAG + 10 * 20

    # Other notes
    Note_SerpentHunter_Bought = BOUGHT_BASE_FLAG + 10 * 30  # found, not bought
    Note_Whip_Bought = BOUGHT_BASE_FLAG + 10 * 31  # found, not bought
    # TODO: Meteor Chuck

    # Survival recipes
    # Recipes_CommonSurvival_Bought = BASE_FLAG + 340  # TODO: For Lobos
    Recipes_CommonSurvival_Bought = BOUGHT_BASE_FLAG + 10 * 32
    # Recipes_UncommonSurvival_Bought = BASE_FLAG + 341  # TODO: For Lobos
    Recipes_UncommonSurvival_Bought = BOUGHT_BASE_FLAG + 10 * 33
    Recipes_RareSurvival_Bought = BOUGHT_BASE_FLAG + 10 * 34
    Recipes_VeryRareSurvival_Bought = BOUGHT_BASE_FLAG + 10 * 35

    # Shield recipe books
    # Recipes_WoodenSmallShields_Bought = BASE_FLAG + 350  # TODO: For Lobos
    Recipes_WoodenSmallShields_Bought = BOUGHT_BASE_FLAG + 10 * 36
    # Recipes_MetalSmallShields_Bought = BASE_FLAG + 351  # TODO: For Lobos
    Recipes_MetalSmallShields_Bought = BOUGHT_BASE_FLAG + 10 * 37
    Recipes_RareSmallShields_Bought = BOUGHT_BASE_FLAG + 10 * 38
    Recipes_VeryRareSmallShields_Bought = BOUGHT_BASE_FLAG + 10 * 39

    Recipes_CommonMediumShields_Bought = BOUGHT_BASE_FLAG + 10 * 40
    Recipes_WoodenMediumShields_Bought = BOUGHT_BASE_FLAG + 10 * 41
    Recipes_HeaterMediumShields_Bought = BOUGHT_BASE_FLAG + 10 * 42
    Recipes_KiteMediumShields_Bought = BOUGHT_BASE_FLAG + 10 * 43
    Recipes_RareMediumShields_Bought = BOUGHT_BASE_FLAG + 10 * 44

    Recipes_CommonGreatshields_Bought = BOUGHT_BASE_FLAG + 10 * 45
    Recipes_UncommonGreatshields_Bought = BOUGHT_BASE_FLAG + 10 * 46
    Recipes_RareGreatshields_Bought = BOUGHT_BASE_FLAG + 10 * 47
    Recipes_VeryRareGreatshields_Bought = BOUGHT_BASE_FLAG + 10 * 48

    # Staff recipe books
    Recipes_CommonStaffs_Bought = BOUGHT_BASE_FLAG + 10 * 49
    Recipes_UncommonStaffs_Bought = BOUGHT_BASE_FLAG + 10 * 50
    Recipes_RareStaffs_Bought = BOUGHT_BASE_FLAG + 10 * 51
    Recipes_VeryRareStaffs_Bought = BOUGHT_BASE_FLAG + 10 * 52

    # Seal recipe books
    # Recipes_CommonSeals_Bought = BOUGHT_BASE_FLAG + 10 * 53  # not used
    Recipes_UncommonSeals_Bought = BOUGHT_BASE_FLAG + 10 * 54
    Recipes_RareSeals_Bought = BOUGHT_BASE_FLAG + 10 * 55
    Recipes_VeryRareSeals_Bought = BOUGHT_BASE_FLAG + 10 * 56

    # Torch recipe notes (actually found, not bought)
    Recipe_SteelWireTorch_Bought = BASE_FLAG + 390
    Recipe_StTrinasTorch_Bought = BASE_FLAG + 391
    Recipe_GhostflameTorch_Bought = BASE_FLAG + 392
    Recipe_BeastRepellentTorch_Bought = BASE_FLAG + 393
    Recipe_SentrysTorch_Bought = BASE_FLAG + 394

    # TIME FLAG. Increments by 1 every 30 in-game minutes.
    MonitorOutdoors = BASE_FLAG + 398  # uses a flag closer to time values

    # Monitor Smith's Hammer possession for recipe appearance.
    ShowSmithsHammerRecipe = BASE_FLAG + 450  # five slots
    ShowNoviceSmithsHammer = BASE_FLAG + 460
    ShowApprenticeSmithsHammer = BASE_FLAG + 461
    ShowJourneymanSmithsHammer = BASE_FLAG + 462
    ShowExpertSmithsHammer = BASE_FLAG + 463
    ShowMasterSmithsHammer = BASE_FLAG + 464

    # For saving hunger/thirst state on death. (Only used to record info across deaths.)
    HasHunger1 = BASE_FLAG + 470
    HasHunger2 = BASE_FLAG + 471
    HasHunger3 = BASE_FLAG + 472
    HasHunger4 = BASE_FLAG + 473
    HasHunger5 = BASE_FLAG + 474
    HasHunger6 = BASE_FLAG + 475
    HasHunger7 = BASE_FLAG + 476
    HasHunger8 = BASE_FLAG + 477
    HasHunger9 = BASE_FLAG + 478
    HasHunger10 = BASE_FLAG + 479
    HasHunger11 = BASE_FLAG + 480
    HasHunger12 = BASE_FLAG + 481
    HasHunger13 = BASE_FLAG + 482
    HasHunger14 = BASE_FLAG + 483
    HasHunger15 = BASE_FLAG + 484
    SaveHungerAfterDeath = BASE_FLAG + 489
    HasThirst1 = BASE_FLAG + 490
    HasThirst2 = BASE_FLAG + 491
    HasThirst3 = BASE_FLAG + 492
    HasThirst4 = BASE_FLAG + 493
    HasThirst5 = BASE_FLAG + 494
    HasThirst6 = BASE_FLAG + 495
    HasThirst7 = BASE_FLAG + 496
    HasThirst8 = BASE_FLAG + 497
    HasThirst9 = BASE_FLAG + 498
    SaveThirstAfterDeath = BASE_FLAG + 499

    # Disease cures (not enough space above for all of them).
    CureDisease = BASE_FLAG + 500  # 21 slots

    # Time flags (one per hour, starting at midnight).
    MonitorHour = BASE_FLAG + 550  # 24 slots
    MonitorPlayerTorch = BASE_FLAG + 583
    PlayerHasTorch = BASE_FLAG + 584
    # NOTE: Do not use any flags between 584 and 591 (so the entire byte is zero IFF 584 is zero).
    PlayerIsOutdoors = BASE_FLAG + 592  # used to tell C# when to add darkness
    # NOTE: Do not use any flags between 593 and 599 (so the entire byte is zero IFF 592 is zero).
    Hour0 = BASE_FLAG + 600
    Hour1 = BASE_FLAG + 601
    Hour2 = BASE_FLAG + 602
    Hour3 = BASE_FLAG + 603
    Hour4 = BASE_FLAG + 604
    Hour5 = BASE_FLAG + 605
    Hour6 = BASE_FLAG + 606
    Hour7 = BASE_FLAG + 607
    Hour8 = BASE_FLAG + 608
    Hour9 = BASE_FLAG + 609
    Hour10 = BASE_FLAG + 610
    Hour11 = BASE_FLAG + 611
    Hour12 = BASE_FLAG + 612
    Hour13 = BASE_FLAG + 613
    Hour14 = BASE_FLAG + 614
    Hour15 = BASE_FLAG + 615
    Hour16 = BASE_FLAG + 616
    Hour17 = BASE_FLAG + 617
    Hour18 = BASE_FLAG + 618
    Hour19 = BASE_FLAG + 619
    Hour20 = BASE_FLAG + 620
    Hour21 = BASE_FLAG + 621
    Hour22 = BASE_FLAG + 622
    Hour23 = BASE_FLAG + 623

    # For crafting weapons.
    CraftDummyWeaponEvent = BASE_FLAG + 1000  # 377 event slots
    AllowWeaponUpgradeEvent = BASE_FLAG + 2000  # 377 slots (event slot)
    AllowWeaponUpgradeFlag = ALLOW_UPGRADE_BASE_FLAG  # 377 slots (actual flag)


class VanillaCharacters(Character):
    Radahn = 1052380800


class SurvivalEffects(SpecialEffectParam):
    """New SpEffects used by Survival Mode."""

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

    # Overworld diseases
    LimgraveDisease = 53000
    LiurniaDisease = 53001
    CaelidDisease = 53002
    AltusDisease = 53003
    MtGelmirDisease = 53004
    MountaintopsDisease = 53005
    SiofraDisease = 53006  # also Nokron
    AinselDisease = 53007  # also Nokstella
    DeeprootDisease = 53008  # also Astel arena

    # Legacy dungeon diseases
    StormveilDisease = 53009
    RayaLucariaDisease = 53010  # maybe also Caria Manor
    RadahnDisease = 53011  # only afflicted by Radahn; higher proc chance
    VolcanoManorDisease = 53012
    LeyndellDisease = 53013  # no disease in Ashen Capital
    SewersDisease = 53014
    HaligtreeDisease = 53015
    FarumAzulaDisease = 53016
    MohgwynDisease = 53017

    # Generic dungeon diseases
    CatacombsDisease = 53018
    CaveDisease = 53019
    TunnelDisease = 53020
    CaveDiseaseDaylight = 53030
    # No Ruin-Strewn Precipice or Divine Tower diseases.

    # Pure Scarlet Rot
    PureScarletRot = 53050
    PureScarletRotItem = 53051  # player re-infects themselves with item

    # Disease cures
    CureLimgraveDisease = 53100
    CureLiurniaDisease = 53101
    CureCaelidDisease = 53102
    CureAltusDisease = 53103
    CureMtGelmirDisease = 53104
    CureMountaintopsDisease = 53105
    CureSiofraDisease = 53106
    CureAinselDisease = 53107
    CureDeeprootDisease = 53108
    CureStormveilDisease = 53109
    CureRayaLucariaDisease = 53110
    CureRadahnDisease = 53111
    CureVolcanoManorDisease = 53112
    CureLeyndellDisease = 53113
    CureSewersDisease = 53114
    CureHaligtreeDisease = 53115
    CureFarumAzulaDisease = 53116
    CureMohgwynDisease = 53117
    CureCatacombsDisease = 53118
    CureCaveDisease = 53119
    CureTunnelDisease = 53120

    # Hunger/thirst only.
    RawSteak = 51900  # 3x Sliver of Meat. Sold by first merchant (Kale). -3 hunger
    SearedSteak = 51901  # 3x Sliver of Meat, 2x Smoldering Butterfly. Sold by first merchant (Kale). -5 hunger
    RawLiverSteak = 51902  # 2x Sliver of Meat, 1x Beast Liver. Sold by ???. -6 hunger
    SearedLiverSteak = 51903  # 2x Sliver of Meat, 1x Beast Liver, 2x Smoldering Butterfly. Sold by ???. -8 hunger
    BoneBroth = 51904  # 5x Thin Beast Bones, Cracked Pot. -2 hunger, -3 thirst
    GreatBoneBroth = 51905  # 3x Hefty Beast Bones, Ritual Pot. -4 hunger, -5 thirst
    BloodBroth = 51906  # 2x Beast Blood, Ritual Pot. -1 hunger, -4 thirst, bonus effect
    BerryMedley1 = 51907  # 10x Rowa Fruit, ???. -2 hunger, -1 thirst
    BerryMedley2 = 51908  # 10x Golden Rowa, ???. -3 hunger, -2 thirst
    BerryMedley3 = 51909  # 10x Rimed Rowa, ???. -4 hunger, -3 thirst
    MushroomStew = 51910  # 3x Mushroom, 1x Herba, Cracked Pot. -2 hunger, -2 thirst
    MeltedMushroomStew = 51911  # 3x Melted Mushroom, ???, Cracked Pot. -4 hunger, -3 thirst
    DraughtOfSatiation = 51912  # ???, 3x Grave Violet, ???, Ritual Pot. -8 hunger, bonus effect
    DraughtOfSilverTears = 51913  # 5x Silver Tear Husk, ???, Ritual Pot. -7 thirst, bonus effect

    # Temperature protection.
    MossdewSoup = 51914  # 3x Cave Moss, 5x Dewkissed Herba, Cracked Pot. -1 thirst, other effects
    CrystalShardSoup = 51915  # 5x Cracked Crystal, ???, Cracked Pot. -1 thirst, other effects
    GiantsSoup = 51916  # 5x Rimed Rowa, 2x Crystal Cave Moss, 2x Rimed Crystal Bud, Ritual Pot. -1 thirst, other
    AmberEyeBrew = 51917  # 3x Eye of Yelough, 1x Yellow Amber, 3x Herba, Cracked Pot. -1 thirst, other
    MagmaticBrew = 51918  # 4x Volcanic Stone, 3x Tarnished Golden Sunflowers, Cracked Pot. -1 thirst, other
    BlossomBrew = 51919  # 5x Fire Blossom, 3x Formic Rock, Ritual Pot. -1 thirst, other
    JarBrittle = 51920  # 5x Living Jar Shards, ???. (no pot) -3 hunger, +3 thirst, other

    # Vanilla item effects (in order they appear in Goods param)
    BoiledCrab = 500820  # -2 hunger
    BoiledPrawn = 500830  # -1 hunger
    PickledTurtleNeck = 3953  # -2 hunger
    ImmunizingCuredMeat = 3960  # -3 hunger, +1 thirst
    InvigoratingCuredMeat = 3961  # -3 hunger, +1 thirst
    ClarifyingCuredMeat = 3962  # -3 hunger, +1 thirst
    DappledCuredMeat = 3963  # -3 hunger, +1 thirst
    SpellproofDriedLiver = 3910  # -3 hunger, +1 thirst
    FireproofDriedLiver = 3920  # -3 hunger, +1 thirst
    LightningproofDriedLiver = 3930  # -3 hunger, +1 thirst
    HolyproofDriedLiver = 501180  # -3 hunger, +1 thirst
    SilverPickledFowlFoot = 3970  # -3 hunger
    GoldPickledFowlFoot = 3971  # -3 hunger
    ExaltedFlesh = 3950  # -4 hunger
    # DeathsbaneJerky = 501220  # CUT CONTENT
    RawMeatDumpling = 501235  # -3 hunger
    ImmunizingWhiteCuredMeat = 501310  # -3 hunger, +1 thirst
    InvigoratingWhiteCuredMeat = 501320  # -3 hunger, +1 thirst
    ClarifyingWhiteCuredMeat = 501330  # -3 hunger, +1 thirst
    DappledWhiteCuredMeat = 501340  # -3 hunger, +1 thirst
    # DeathsbaneWhiteJerky = 501350  # CUT CONTENT


class WeaponCategory(IntEnum):
    """Vanilla enum."""
    Dagger = 0
    StraightSword = 1
    ThrustingSword = 2
    CurvedSwordKatana = 3
    Axe = 4
    Hammer = 5
    Spear = 6
    HalberdReaper = 7
    StaffSeal = 8
    Fists = 9
    Bow = 10
    Crossbow = 11
    Shield = 12
    Arrow = 13
    Bolt = 14


class WeaponType(IntEnum):
    Dagger = 1
    StraightSword = 3
    Greatsword = 5
    ColossalSword = 7
    CurvedSword = 9
    CurvedGreatsword = 11
    Katana = 13
    Twinblade = 14
    ThrustingSword = 15
    HeavyThrustingSword = 16
    Axe = 17
    Greataxe = 19
    Hammer = 21
    GreatHammer = 23
    Flail = 24
    Spear = 25
    HeavySpear = 28
    Halberd = 29
    Scythe = 31
    Fist = 35
    Claw = 37
    Whip = 39
    ColossalWeapon = 41
    LightBow = 50
    Bow = 51
    Greatbow = 53
    Crossbow = 55
    Ballista = 56
    Staff = 57
    Seal = 61
    SmallShield = 65
    MediumShield = 67
    Greatshield = 69
    Arrow = 81
    Greatarrow = 83
    Bolt = 85
    BallistaBolt = 86
    Torch = 87


class GoodsUseAnimation(IntEnum):
    ITEM_RECOVER = 0
    ITEM_DRINK = 10
    ITEM_EATJERKY = 26


class PotGroupID(IntEnum):
    NoPot = -1
    CrackedPot = 1
    PerfumeBottle = 2
    RitualPot = 3


class HudIcons(IntEnum):
    HeatProtection = 20032
    ColdProtection = 20033
    Dehydration = 20034
    DiseasePlague = 20035
    DiseaseParasite = 20036
    DiseaseToxin = 20037
    DiseaseFever = 20038
    Heat_Mild = 20039
    Heat_Moderate = 20040
    Heat_Severe = 20041
    Cold_Mild = 20042
    Cold_Moderate = 20043
    Cold_Severe = 20044
