"""New common EMEVD events for Elden Ring Survival Mode.

Kept separate to `common.evs.py` because I will probably regenerate the vanilla events in that file from time to time as
my understanding of ER EMEVD instructions becomes better.
"""
from soulstruct.eldenring.events import *
from .survival_enums import *
from .survival_goods import *


@NeverRestart(0)
def Constructor():
    """Will be merged with vanilla Common."""

    # TODO: Debugging. Remove for release.
    # AwardItemLot(500)
    # AwardItemLot(600)
    # AwardItemLot(610)
    # AwardItemLot(700)
    AddSpecialEffect(PLAYER, 39999)  # SUPER DEFENSE
    DEBUG_ResetDiseases()
    # DEBUG_GetAllMaps()
    # DEBUG_GetDectusMedallions()

    # region Hunger/Thirst
    GrowingHunger()
    GrowingThirst()
    SaveHungerAfterDeath()
    SaveThirstAfterDeath()

    RelieveHunger_1()
    RelieveHunger_2()
    RelieveHunger_3()
    RelieveHunger_4()
    RelieveHunger_5()
    RelieveHunger_6()
    # RelieveHunger_7()  # no items that relieve 7 hunger
    RelieveHunger_8()
    RelieveThirst_1()
    RelieveThirst_2()
    RelieveThirst_3()
    RelieveThirst_4()
    RelieveThirst_5()
    RelieveThirst_6()
    # RelieveThirst_7()  # no items that relieve 7 thirst
    IncreaseThirst_1()  # dried/cured vanilla meats
    IncreaseThirst_3()  # Jar Brittle
    JarBrittleEffects()
    # endregion

    # region Map area checks
    MonitorInLimgrave()
    MonitorInLiurnia()
    MonitorInCaelid()
    MonitorInAltus()
    MonitorInMtGelmir()
    MonitorInMountaintops()
    MonitorInGenericDungeon()
    MonitorInLegacyDungeon()
    # endregion

    # region Temperature effect checks

    # Disable all warning trigger flags on map load (in case you quit the game while one was enabled).
    DisableFlagRange((Flags.ShowMildHeatWarning, Flags.ShowSevereColdWarning))

    CheckMildHeatArea()
    MildHeatWarning()
    CheckModerateHeatArea()
    ModerateHeatWarning()
    CheckSevereHeatArea()
    SevereHeatWarning()
    CheckMildColdArea()
    MildColdWarning()
    CheckModerateColdArea()
    ModerateColdWarning()
    CheckSevereColdArea()
    SevereColdWarning()
    # endregion

    # region Disease checks
    DisableFlag(Flags.DiseaseRollLock)
    GetDiseaseOverworld(
        0,
        SurvivalEffects.LimgraveDisease,
        Flags.PlayerInLimgrave,
        Flags.LimgraveDiseaseOnce,
        Flags.LimgraveDiseaseTwice,
        DiseaseIndicators.LimgraveDisease,
        DiseaseItemLots.LimgraveDisease,
    )
    GetDiseaseOverworld(
        1,
        SurvivalEffects.LiurniaDisease,
        Flags.PlayerInLiurnia,
        Flags.LiurniaDiseaseOnce,
        Flags.LiurniaDiseaseTwice,
        DiseaseIndicators.LiurniaDisease,
        DiseaseItemLots.LiurniaDisease,
    )
    GetDiseaseOverworld(
        2,
        SurvivalEffects.CaelidDisease,
        Flags.PlayerInCaelid,
        Flags.CaelidDiseaseOnce,
        Flags.CaelidDiseaseTwice,
        DiseaseIndicators.CaelidDisease,
        DiseaseItemLots.CaelidDisease,
    )
    GetDiseaseOverworld(
        3,
        SurvivalEffects.AltusDisease,
        Flags.PlayerInAltus,
        Flags.AltusDiseaseOnce,
        Flags.AltusDiseaseTwice,
        DiseaseIndicators.AltusDisease,
        DiseaseItemLots.AltusDisease,
    )
    GetDiseaseOverworld(
        4,
        SurvivalEffects.MtGelmirDisease,
        Flags.PlayerInMtGelmir,
        Flags.MtGelmirDiseaseOnce,
        Flags.MtGelmirDiseaseTwice,
        DiseaseIndicators.MtGelmirDisease,
        DiseaseItemLots.MtGelmirDisease,
    )
    GetDiseaseOverworld(
        5,
        SurvivalEffects.MountaintopsDisease,
        Flags.PlayerInMountaintops,
        Flags.MountaintopsDiseaseOnce,
        Flags.MountaintopsDiseaseTwice,
        DiseaseIndicators.MountaintopsDisease,
        DiseaseItemLots.MountaintopsDisease,
    )

    GetDiseaseLegacyDungeon(
        0,
        SurvivalEffects.StormveilDisease,
        10, 0, 0, 0,  # STORMVEIL_CASTLE
        Flags.StormveilDiseaseOnce,
        Flags.StormveilDiseaseTwice,
        DiseaseIndicators.StormveilDisease,
        DiseaseItemLots.StormveilDisease,
    )
    GetDiseaseLegacyDungeon(
        1,
        SurvivalEffects.RayaLucariaDisease,
        14, 0, 0, 0,  # RAYA_LUCARIA
        Flags.RayaLucariaDiseaseOnce,
        Flags.RayaLucariaDiseaseTwice,
        DiseaseIndicators.RayaLucariaDisease,
        DiseaseItemLots.RayaLucariaDisease,
    )
    GetDiseaseLegacyDungeon(
        2,
        SurvivalEffects.VolcanoManorDisease,
        16, 0, 0, 0,  # VOLCANO_MANOR (does not matter if you're in the no-attack zone)
        Flags.VolcanoManorDiseaseOnce,
        Flags.VolcanoManorDiseaseTwice,
        DiseaseIndicators.VolcanoManorDisease,
        DiseaseItemLots.VolcanoManorDisease,
    )
    GetDiseaseLegacyDungeon(
        3,
        SurvivalEffects.LeyndellDisease,
        11, 0, 0, 0,  # LEYNDELL_ROYAL_CAPITAL (no disease in Ashen Capital)
        Flags.LeyndellDiseaseOnce,
        Flags.LeyndellDiseaseTwice,
        DiseaseIndicators.LeyndellDisease,
        DiseaseItemLots.LeyndellDisease,
    )
    GetDiseaseLegacyDungeon(
        4,
        SurvivalEffects.SewersDisease,
        35, 0, 0, 0,  # SHUNNING_GROUNDS
        Flags.SewersDiseaseOnce,
        Flags.SewersDiseaseTwice,
        DiseaseIndicators.SewersDisease,
        DiseaseItemLots.SewersDisease,
    )
    GetDiseaseLegacyDungeon(
        5,
        SurvivalEffects.HaligtreeDisease,
        15, 0, 0, 0,  # HALIGTREE
        Flags.HaligtreeDiseaseOnce,
        Flags.HaligtreeDiseaseTwice,
        DiseaseIndicators.HaligtreeDisease,
        DiseaseItemLots.HaligtreeDisease,
    )
    GetDiseaseLegacyDungeon(
        6,
        SurvivalEffects.FarumAzulaDisease,
        13, 0, 0, 0,  # CRUMBLING_FARUM_AZULA
        Flags.FarumAzulaDiseaseOnce,
        Flags.FarumAzulaDiseaseTwice,
        DiseaseIndicators.FarumAzulaDisease,
        DiseaseItemLots.FarumAzulaDisease,
    )
    GetDiseaseLegacyDungeon(
        7,
        SurvivalEffects.MohgwynDisease,
        12, 5, 0, 0,  # MOHGWYN_PALACE
        Flags.MohgwynDiseaseOnce,
        Flags.MohgwynDiseaseTwice,
        DiseaseIndicators.MohgwynDisease,
        DiseaseItemLots.MohgwynDisease,
    )

    GetDiseaseSiofra()
    GetDiseaseAinsel()
    GetDiseaseDeeprootAstel()
    GetDiseaseRadahn()
    GetDiseaseCatacombs()
    GetDiseaseCaves()
    GetDiseaseTunnels()
    CaveDiseaseInDaylight()
    # Skipping Pure Scarlet Rot.
    # endregion

    # region Disease cures
    CureDisease(
        0, 
        SurvivalEffects.LimgraveDisease, 
        SurvivalEffects.CureLimgraveDisease, 
        DiseaseIndicators.LimgraveDisease, 
        SurvivalText.CuredLimgraveDisease,
    )
    CureDisease(
        1, 
        SurvivalEffects.LiurniaDisease, 
        SurvivalEffects.CureLiurniaDisease, 
        DiseaseIndicators.LiurniaDisease, 
        SurvivalText.CuredLiurniaDisease,
    )
    CureDisease(
        2, 
        SurvivalEffects.CaelidDisease, 
        SurvivalEffects.CureCaelidDisease, 
        DiseaseIndicators.CaelidDisease, 
        SurvivalText.CuredCaelidDisease,
    )
    CureDisease(
        3, 
        SurvivalEffects.AltusDisease, 
        SurvivalEffects.CureAltusDisease, 
        DiseaseIndicators.AltusDisease, 
        SurvivalText.CuredAltusDisease,
    )
    CureDisease(
        4, 
        SurvivalEffects.MtGelmirDisease, 
        SurvivalEffects.CureMtGelmirDisease, 
        DiseaseIndicators.MtGelmirDisease, 
        SurvivalText.CuredMtGelmirDisease,
    )
    CureDisease(
        5, 
        SurvivalEffects.MountaintopsDisease, 
        SurvivalEffects.CureMountaintopsDisease, 
        DiseaseIndicators.MountaintopsDisease, 
        SurvivalText.CuredMountaintopsDisease,
    )
    CureDisease(
        6, 
        SurvivalEffects.SiofraDisease, 
        SurvivalEffects.CureSiofraDisease, 
        DiseaseIndicators.SiofraDisease, 
        SurvivalText.CuredSiofraDisease,
    )
    CureDisease(
        7, 
        SurvivalEffects.AinselDisease, 
        SurvivalEffects.CureAinselDisease, 
        DiseaseIndicators.AinselDisease, 
        SurvivalText.CuredAinselDisease,
    )
    CureDisease(
        8, 
        SurvivalEffects.DeeprootDisease, 
        SurvivalEffects.CureDeeprootDisease, 
        DiseaseIndicators.DeeprootDisease, 
        SurvivalText.CuredDeeprootDisease,
    )
    CureDisease(
        9, 
        SurvivalEffects.StormveilDisease, 
        SurvivalEffects.CureStormveilDisease, 
        DiseaseIndicators.StormveilDisease, 
        SurvivalText.CuredStormveilDisease,
    )
    CureDisease(
        10, 
        SurvivalEffects.RayaLucariaDisease, 
        SurvivalEffects.CureRayaLucariaDisease, 
        DiseaseIndicators.RayaLucariaDisease, 
        SurvivalText.CuredRayaLucariaDisease,
    )
    CureDisease(
        11, 
        SurvivalEffects.RadahnDisease, 
        SurvivalEffects.CureRadahnDisease, 
        DiseaseIndicators.RadahnDisease, 
        SurvivalText.CuredRadahnDisease,
    )
    CureDisease(
        12, 
        SurvivalEffects.VolcanoManorDisease, 
        SurvivalEffects.CureVolcanoManorDisease, 
        DiseaseIndicators.VolcanoManorDisease, 
        SurvivalText.CuredVolcanoManorDisease,
    )
    CureDisease(
        13, 
        SurvivalEffects.LeyndellDisease, 
        SurvivalEffects.CureLeyndellDisease, 
        DiseaseIndicators.LeyndellDisease, 
        SurvivalText.CuredLeyndellDisease,
    )
    CureDisease(
        14, 
        SurvivalEffects.SewersDisease, 
        SurvivalEffects.CureSewersDisease, 
        DiseaseIndicators.SewersDisease, 
        SurvivalText.CuredSewersDisease,
    )
    CureDisease(
        15, 
        SurvivalEffects.HaligtreeDisease, 
        SurvivalEffects.CureHaligtreeDisease, 
        DiseaseIndicators.HaligtreeDisease, 
        SurvivalText.CuredHaligtreeDisease,
    )
    CureDisease(
        16, 
        SurvivalEffects.FarumAzulaDisease, 
        SurvivalEffects.CureFarumAzulaDisease, 
        DiseaseIndicators.FarumAzulaDisease, 
        SurvivalText.CuredFarumAzulaDisease,
    )
    CureDisease(
        17, 
        SurvivalEffects.MohgwynDisease, 
        SurvivalEffects.CureMohgwynDisease, 
        DiseaseIndicators.MohgwynDisease, 
        SurvivalText.CuredMohgwynDisease,
    )
    CureDisease(
        18, 
        SurvivalEffects.CatacombsDisease, 
        SurvivalEffects.CureCatacombsDisease, 
        DiseaseIndicators.CatacombsDisease, 
        SurvivalText.CuredCatacombsDisease,
    )
    CureDisease(
        19, 
        SurvivalEffects.CaveDisease, 
        SurvivalEffects.CureCaveDisease, 
        DiseaseIndicators.CaveDisease, 
        SurvivalText.CuredCaveDisease,
    )
    CureDisease(
        20, 
        SurvivalEffects.TunnelDisease, 
        SurvivalEffects.CureTunnelDisease, 
        DiseaseIndicators.TunnelDisease, 
        SurvivalText.CuredTunnelDisease,
    )
    # CurePureScarletRot()
    # endregion

    # Swap dummy weapons for real weapons and monitor weapon possession (plus a Smith's Hammer) for upgrading.
    # region Dummy Weapons
    CraftDummyWeapon(0, 60010000, 40010000, 0)
    AllowWeaponUpgrade(0, 1000000, 0, 19004000)
    CraftDummyWeapon(1, 60010100, 40010100, 1160009)
    AllowWeaponUpgrade(1, 1010010, 8404, 19004001)
    CraftDummyWeapon(2, 60010200, 40010200, 1140006)
    AllowWeaponUpgrade(2, 1020009, 8402, 19004002)
    CraftDummyWeapon(3, 60010300, 40010300, 1140006)
    AllowWeaponUpgrade(3, 1030009, 8402, 19004003)
    CraftDummyWeapon(4, 60010400, 40010400, 1160009)
    AllowWeaponUpgrade(4, 1040010, 8404, 19004004)
    CraftDummyWeapon(5, 60010500, 40010500, 1100012)
    AllowWeaponUpgrade(5, 1050015, 8404, 19004005)
    CraftDummyWeapon(6, 60010600, 40010600, 1030009)
    AllowWeaponUpgrade(6, 1060012, 8403, 19004006)
    CraftDummyWeapon(7, 60010700, 40010700, 1050015)
    AllowWeaponUpgrade(7, 1070010, 8404, 19004007)
    CraftDummyWeapon(8, 60010800, 40010800, 1130015)
    AllowWeaponUpgrade(8, 1080010, 8404, 19004008)
    CraftDummyWeapon(9, 60010900, 40010900, 1000000)
    AllowWeaponUpgrade(9, 1090003, 8400, 19004009)
    CraftDummyWeapon(10, 60011000, 40011000, 1020009)
    AllowWeaponUpgrade(10, 1100012, 8403, 19004010)
    CraftDummyWeapon(11, 60011100, 40011100, 1100012)
    AllowWeaponUpgrade(11, 1110010, 8404, 19004011)
    CraftDummyWeapon(12, 60011300, 40011300, 1060012)
    AllowWeaponUpgrade(12, 1130015, 8404, 19004012)
    CraftDummyWeapon(13, 60011400, 40011400, 1090003)
    AllowWeaponUpgrade(13, 1140006, 8401, 19004013)
    CraftDummyWeapon(14, 60011500, 40011500, 1100012)
    AllowWeaponUpgrade(14, 1150015, 8404, 19004014)
    CraftDummyWeapon(15, 60011600, 40011600, 1150015)
    AllowWeaponUpgrade(15, 1160009, 8404, 19004015)
    CraftDummyWeapon(16, 60020000, 40020000, 2050004)
    AllowWeaponUpgrade(16, 2000006, 8401, 19004016)
    CraftDummyWeapon(17, 60020100, 40020100, 1000000)
    AllowWeaponUpgrade(17, 2010002, 0, 19004017)
    CraftDummyWeapon(18, 60020200, 40020200, 2000006)
    AllowWeaponUpgrade(18, 2020008, 8401, 19004018)
    CraftDummyWeapon(19, 60020400, 40020400, 2020008)
    AllowWeaponUpgrade(19, 2040010, 8402, 19004019)
    CraftDummyWeapon(20, 60020500, 40020500, 2010002)
    AllowWeaponUpgrade(20, 2050004, 8400, 19004020)
    CraftDummyWeapon(21, 60020600, 40020600, 2040010)
    AllowWeaponUpgrade(21, 2060006, 8403, 19004021)
    CraftDummyWeapon(22, 60020700, 40020700, 2110008)
    AllowWeaponUpgrade(22, 2070009, 8404, 19004022)
    CraftDummyWeapon(23, 60020800, 40020800, 7060015)
    AllowWeaponUpgrade(23, 2080009, 8404, 19004023)
    CraftDummyWeapon(24, 60020900, 40020900, 3050014)
    AllowWeaponUpgrade(24, 2090008, 8404, 19004024)
    CraftDummyWeapon(25, 60021100, 40021100, 2060006)
    AllowWeaponUpgrade(25, 2110008, 8404, 19004025)
    CraftDummyWeapon(26, 60021400, 40021400, 2180008)
    AllowWeaponUpgrade(26, 2140010, 8404, 19004026)
    CraftDummyWeapon(27, 60021500, 40021500, 2000006)
    AllowWeaponUpgrade(27, 2150004, 8401, 19004027)
    CraftDummyWeapon(28, 60021800, 40021800, 2190007)
    AllowWeaponUpgrade(28, 2180008, 8404, 19004028)
    CraftDummyWeapon(29, 60021900, 40021900, 2250006)
    AllowWeaponUpgrade(29, 2190007, 8403, 19004029)
    CraftDummyWeapon(30, 60022000, 40022000, 2070009)
    AllowWeaponUpgrade(30, 2200010, 8404, 19004030)
    CraftDummyWeapon(31, 60022100, 40022100, 2230012)
    AllowWeaponUpgrade(31, 2210015, 8404, 19004031)
    CraftDummyWeapon(32, 60022200, 40022200, 2240018)
    AllowWeaponUpgrade(32, 2220010, 8404, 19004032)
    CraftDummyWeapon(33, 60022300, 40022300, 2040010)
    AllowWeaponUpgrade(33, 2230012, 8403, 19004033)
    CraftDummyWeapon(34, 60022400, 40022400, 2210015)
    AllowWeaponUpgrade(34, 2240018, 8404, 19004034)
    CraftDummyWeapon(35, 60022500, 40022500, 2260005)
    AllowWeaponUpgrade(35, 2250006, 8403, 19004035)
    CraftDummyWeapon(36, 60022600, 40022600, 2150004)
    AllowWeaponUpgrade(36, 2260005, 8402, 19004036)
    CraftDummyWeapon(37, 60030000, 40030000, 2020008)
    AllowWeaponUpgrade(37, 3000009, 8402, 19004037)
    CraftDummyWeapon(38, 60030100, 40030100, 3180010)
    AllowWeaponUpgrade(38, 3010012, 8403, 19004038)
    CraftDummyWeapon(39, 60030200, 40030200, 3080014)
    AllowWeaponUpgrade(39, 3020015, 8404, 19004039)
    CraftDummyWeapon(40, 60030300, 40030300, 3180010)
    AllowWeaponUpgrade(40, 3030012, 8403, 19004040)
    CraftDummyWeapon(41, 60030400, 40030400, 3080014)
    AllowWeaponUpgrade(41, 3040015, 8404, 19004041)
    CraftDummyWeapon(42, 60030500, 40030500, 3010012)
    AllowWeaponUpgrade(42, 3050014, 8403, 19004042)
    CraftDummyWeapon(43, 60030600, 40030600, 3140009)
    AllowWeaponUpgrade(43, 3060010, 8404, 19004043)
    CraftDummyWeapon(44, 60030700, 40030700, 3040015)
    AllowWeaponUpgrade(44, 3070008, 8404, 19004044)
    CraftDummyWeapon(45, 60030800, 40030800, 3030012)
    AllowWeaponUpgrade(45, 3080014, 8403, 19004045)
    CraftDummyWeapon(46, 60030900, 40030900, 3130009)
    AllowWeaponUpgrade(46, 3090010, 8404, 19004046)
    CraftDummyWeapon(47, 60031000, 40031000, 2090008)
    AllowWeaponUpgrade(47, 3100010, 8404, 19004047)
    CraftDummyWeapon(48, 60031300, 40031300, 3070008)
    AllowWeaponUpgrade(48, 3130009, 8404, 19004048)
    CraftDummyWeapon(49, 60031400, 40031400, 3040015)
    AllowWeaponUpgrade(49, 3140009, 8404, 19004049)
    CraftDummyWeapon(50, 60031500, 40031500, 3040015)
    AllowWeaponUpgrade(50, 3150010, 8404, 19004050)
    CraftDummyWeapon(51, 60031600, 40031600, 3050014)
    AllowWeaponUpgrade(51, 3160008, 8404, 19004051)
    CraftDummyWeapon(52, 60031700, 40031700, 2090008)
    AllowWeaponUpgrade(52, 3170010, 8404, 19004052)
    CraftDummyWeapon(53, 60031800, 40031800, 3000009)
    AllowWeaponUpgrade(53, 3180010, 8402, 19004053)
    CraftDummyWeapon(54, 60031900, 40031900, 3040015)
    AllowWeaponUpgrade(54, 3190018, 8404, 19004054)
    CraftDummyWeapon(55, 60032000, 40032000, 3160008)
    AllowWeaponUpgrade(55, 3200010, 8404, 19004055)
    CraftDummyWeapon(56, 60032100, 40032100, 3190018)
    AllowWeaponUpgrade(56, 3210010, 8404, 19004056)
    CraftDummyWeapon(57, 60040000, 40040000, 4010017)
    AllowWeaponUpgrade(57, 4000018, 8404, 19004057)
    CraftDummyWeapon(58, 60040100, 40040100, 4040016)
    AllowWeaponUpgrade(58, 4010017, 8404, 19004058)
    CraftDummyWeapon(59, 60040200, 40040200, 4010017)
    AllowWeaponUpgrade(59, 4020010, 8404, 19004059)
    CraftDummyWeapon(60, 60040300, 40040300, 4040016)
    AllowWeaponUpgrade(60, 4030017, 8404, 19004060)
    CraftDummyWeapon(61, 60040400, 40040400, 3020015)
    AllowWeaponUpgrade(61, 4040016, 8404, 19004061)
    CraftDummyWeapon(62, 60040500, 40040500, 4010017)
    AllowWeaponUpgrade(62, 4050010, 8404, 19004062)
    CraftDummyWeapon(63, 60040600, 40040600, 4110009)
    AllowWeaponUpgrade(63, 4060010, 8404, 19004063)
    CraftDummyWeapon(64, 60040700, 40040700, 4110009)
    AllowWeaponUpgrade(64, 4070010, 8404, 19004064)
    CraftDummyWeapon(65, 60040800, 40040800, 4000018)
    AllowWeaponUpgrade(65, 4080010, 8404, 19004065)
    CraftDummyWeapon(66, 60041000, 40041000, 4000018)
    AllowWeaponUpgrade(66, 4100010, 8404, 19004066)
    CraftDummyWeapon(67, 60041100, 40041100, 4030017)
    AllowWeaponUpgrade(67, 4110009, 8404, 19004067)
    CraftDummyWeapon(68, 60050000, 40050000, 5060010)
    AllowWeaponUpgrade(68, 5000012, 8403, 19004068)
    CraftDummyWeapon(69, 60050100, 40050100, 5000012)
    AllowWeaponUpgrade(69, 5010014, 8403, 19004069)
    CraftDummyWeapon(70, 60050200, 40050200, 2000006)
    AllowWeaponUpgrade(70, 5020008, 8401, 19004070)
    CraftDummyWeapon(71, 60050300, 40050300, 5000012)
    AllowWeaponUpgrade(71, 5030014, 8403, 19004071)
    CraftDummyWeapon(72, 60050400, 40050400, 5030014)
    AllowWeaponUpgrade(72, 5040017, 8404, 19004072)
    CraftDummyWeapon(73, 60050500, 40050500, 5040017)
    AllowWeaponUpgrade(73, 5050010, 8404, 19004073)
    CraftDummyWeapon(74, 60050600, 40050600, 5020008)
    AllowWeaponUpgrade(74, 5060010, 8402, 19004074)
    CraftDummyWeapon(75, 60060000, 40060000, 6010017)
    AllowWeaponUpgrade(75, 6000010, 8404, 19004075)
    CraftDummyWeapon(76, 60060100, 40060100, 6020016)
    AllowWeaponUpgrade(76, 6010017, 8404, 19004076)
    CraftDummyWeapon(77, 60060200, 40060200, 5010014)
    AllowWeaponUpgrade(77, 6020016, 8404, 19004077)
    CraftDummyWeapon(78, 60060400, 40060400, 6010017)
    AllowWeaponUpgrade(78, 6040010, 8404, 19004078)
    CraftDummyWeapon(79, 60070000, 40070000, 7030006)
    AllowWeaponUpgrade(79, 7000008, 8401, 19004079)
    CraftDummyWeapon(80, 60070100, 40070100, 7110010)
    AllowWeaponUpgrade(80, 7010012, 8403, 19004080)
    CraftDummyWeapon(81, 60070200, 40070200, 7060015)
    AllowWeaponUpgrade(81, 7020018, 8404, 19004081)
    CraftDummyWeapon(82, 60070300, 40070300, 7140004)
    AllowWeaponUpgrade(82, 7030006, 8401, 19004082)
    CraftDummyWeapon(83, 60070400, 40070400, 7030006)
    AllowWeaponUpgrade(83, 7040008, 8401, 19004083)
    CraftDummyWeapon(84, 60070500, 40070500, 2080009)
    AllowWeaponUpgrade(84, 7050010, 8404, 19004084)
    CraftDummyWeapon(85, 60070600, 40070600, 7120012)
    AllowWeaponUpgrade(85, 7060015, 8404, 19004085)
    CraftDummyWeapon(86, 60070700, 40070700, 2080009)
    AllowWeaponUpgrade(86, 7070010, 8404, 19004086)
    CraftDummyWeapon(87, 60070800, 40070800, 7000008)
    AllowWeaponUpgrade(87, 7080010, 8402, 19004087)
    CraftDummyWeapon(88, 60071000, 40071000, 7020018)
    AllowWeaponUpgrade(88, 7100010, 8404, 19004088)
    CraftDummyWeapon(89, 60071100, 40071100, 7040008)
    AllowWeaponUpgrade(89, 7110010, 8402, 19004089)
    CraftDummyWeapon(90, 60071200, 40071200, 7080010)
    AllowWeaponUpgrade(90, 7120012, 8403, 19004090)
    CraftDummyWeapon(91, 60071400, 40071400, 2010002)
    AllowWeaponUpgrade(91, 7140004, 8400, 19004091)
    CraftDummyWeapon(92, 60071500, 40071500, 7010012)
    AllowWeaponUpgrade(92, 7150014, 8403, 19004092)
    CraftDummyWeapon(93, 60080100, 40080100, 8060018)
    AllowWeaponUpgrade(93, 8010010, 8404, 19004093)
    CraftDummyWeapon(94, 60080200, 40080200, 7150014)
    AllowWeaponUpgrade(94, 8020016, 8404, 19004094)
    CraftDummyWeapon(95, 60080300, 40080300, 8050008)
    AllowWeaponUpgrade(95, 8030009, 8404, 19004095)
    CraftDummyWeapon(96, 60080400, 40080400, 8060018)
    AllowWeaponUpgrade(96, 8040010, 8404, 19004096)
    CraftDummyWeapon(97, 60080500, 40080500, 8070012)
    AllowWeaponUpgrade(97, 8050008, 8404, 19004097)
    CraftDummyWeapon(98, 60080600, 40080600, 8020016)
    AllowWeaponUpgrade(98, 8060018, 8404, 19004098)
    CraftDummyWeapon(99, 60080700, 40080700, 7080010)
    AllowWeaponUpgrade(99, 8070012, 8403, 19004099)
    CraftDummyWeapon(100, 60080800, 40080800, 8060018)
    AllowWeaponUpgrade(100, 8080020, 8404, 19004100)
    CraftDummyWeapon(101, 60081000, 40081000, 8030009)
    AllowWeaponUpgrade(101, 8100010, 8404, 19004101)
    CraftDummyWeapon(102, 60090000, 40090000, 7080010)
    AllowWeaponUpgrade(102, 9000012, 8403, 19004102)
    CraftDummyWeapon(103, 60090100, 40090100, 9080015)
    AllowWeaponUpgrade(103, 9010017, 8404, 19004103)
    CraftDummyWeapon(104, 60090200, 40090200, 9010017)
    AllowWeaponUpgrade(104, 9020010, 8404, 19004104)
    CraftDummyWeapon(105, 60090300, 40090300, 9080015)
    AllowWeaponUpgrade(105, 9030009, 8404, 19004105)
    CraftDummyWeapon(106, 60090400, 40090400, 9070008)
    AllowWeaponUpgrade(106, 9040010, 8404, 19004106)
    CraftDummyWeapon(107, 60090600, 40090600, 9030009)
    AllowWeaponUpgrade(107, 9060010, 8404, 19004107)
    CraftDummyWeapon(108, 60090700, 40090700, 9080015)
    AllowWeaponUpgrade(108, 9070008, 8404, 19004108)
    CraftDummyWeapon(109, 60090800, 40090800, 9000012)
    AllowWeaponUpgrade(109, 9080015, 8404, 19004109)
    CraftDummyWeapon(110, 60100000, 40100000, 2040010)
    AllowWeaponUpgrade(110, 10000012, 8403, 19004110)
    CraftDummyWeapon(111, 60100100, 40100100, 10030014)
    AllowWeaponUpgrade(111, 10010016, 8404, 19004111)
    CraftDummyWeapon(112, 60100300, 40100300, 10000012)
    AllowWeaponUpgrade(112, 10030014, 8403, 19004112)
    CraftDummyWeapon(113, 60100500, 40100500, 10010016)
    AllowWeaponUpgrade(113, 10050010, 8404, 19004113)
    CraftDummyWeapon(114, 60100800, 40100800, 10030014)
    AllowWeaponUpgrade(114, 10080017, 8404, 19004114)
    CraftDummyWeapon(115, 60100900, 40100900, 10080017)
    AllowWeaponUpgrade(115, 10090010, 8404, 19004115)
    CraftDummyWeapon(116, 60110000, 40110000, 11070006)
    AllowWeaponUpgrade(116, 11000009, 8402, 19004116)
    CraftDummyWeapon(117, 60110100, 40110100, 0)
    AllowWeaponUpgrade(117, 11010000, 0, 19004117)
    CraftDummyWeapon(118, 60110300, 40110300, 11010000)
    AllowWeaponUpgrade(118, 11030003, 8400, 19004118)
    CraftDummyWeapon(119, 60110400, 40110400, 11010000)
    AllowWeaponUpgrade(119, 11040003, 8400, 19004119)
    CraftDummyWeapon(120, 60110500, 40110500, 11000009)
    AllowWeaponUpgrade(120, 11050012, 8403, 19004120)
    CraftDummyWeapon(121, 60110600, 40110600, 11090016)
    AllowWeaponUpgrade(121, 11060010, 8404, 19004121)
    CraftDummyWeapon(122, 60110700, 40110700, 11030003)
    AllowWeaponUpgrade(122, 11070006, 8401, 19004122)
    CraftDummyWeapon(123, 60110800, 40110800, 11040003)
    AllowWeaponUpgrade(123, 11080006, 8401, 19004123)
    CraftDummyWeapon(124, 60110900, 40110900, 11050012)
    AllowWeaponUpgrade(124, 11090016, 8404, 19004124)
    CraftDummyWeapon(125, 60111000, 40111000, 11130007)
    AllowWeaponUpgrade(125, 11100008, 8404, 19004125)
    CraftDummyWeapon(126, 60111100, 40111100, 11090016)
    AllowWeaponUpgrade(126, 11110010, 8404, 19004126)
    CraftDummyWeapon(127, 60111200, 40111200, 11130007)
    AllowWeaponUpgrade(127, 11120010, 8404, 19004127)
    CraftDummyWeapon(128, 60111300, 40111300, 11140009)
    AllowWeaponUpgrade(128, 11130007, 8403, 19004128)
    CraftDummyWeapon(129, 60111400, 40111400, 11080006)
    AllowWeaponUpgrade(129, 11140009, 8402, 19004129)
    CraftDummyWeapon(130, 60111500, 40111500, 11100008)
    AllowWeaponUpgrade(130, 11150010, 8404, 19004130)
    CraftDummyWeapon(131, 60120000, 40120000, 11140009)
    AllowWeaponUpgrade(131, 12000010, 8402, 19004131)
    CraftDummyWeapon(132, 60120100, 40120100, 12140014)
    AllowWeaponUpgrade(132, 12010016, 8404, 19004132)
    CraftDummyWeapon(133, 60120200, 40120200, 12140014)
    AllowWeaponUpgrade(133, 12020016, 8404, 19004133)
    CraftDummyWeapon(134, 60120600, 40120600, 12000010)
    AllowWeaponUpgrade(134, 12060012, 8403, 19004134)
    CraftDummyWeapon(135, 60120800, 40120800, 12000010)
    AllowWeaponUpgrade(135, 12080012, 8403, 19004135)
    CraftDummyWeapon(136, 60121300, 40121300, 12000010)
    AllowWeaponUpgrade(136, 12130012, 8403, 19004136)
    CraftDummyWeapon(137, 60121400, 40121400, 12080012)
    AllowWeaponUpgrade(137, 12140014, 8403, 19004137)
    CraftDummyWeapon(138, 60121500, 40121500, 12130012)
    AllowWeaponUpgrade(138, 12150008, 8404, 19004138)
    CraftDummyWeapon(139, 60121600, 40121600, 11100008)
    AllowWeaponUpgrade(139, 12160009, 8404, 19004139)
    CraftDummyWeapon(140, 60121700, 40121700, 12210018)
    AllowWeaponUpgrade(140, 12170010, 8404, 19004140)
    CraftDummyWeapon(141, 60121800, 40121800, 11090016)
    AllowWeaponUpgrade(141, 12180020, 8404, 19004141)
    CraftDummyWeapon(142, 60121900, 40121900, 12060012)
    AllowWeaponUpgrade(142, 12190014, 8403, 19004142)
    CraftDummyWeapon(143, 60122000, 40122000, 12150008)
    AllowWeaponUpgrade(143, 12200010, 8404, 19004143)
    CraftDummyWeapon(144, 60122100, 40122100, 12020016)
    AllowWeaponUpgrade(144, 12210018, 8404, 19004144)
    CraftDummyWeapon(145, 60130000, 40130000, 13010015)
    AllowWeaponUpgrade(145, 13000016, 8404, 19004145)
    CraftDummyWeapon(146, 60130100, 40130100, 11050012)
    AllowWeaponUpgrade(146, 13010015, 8404, 19004146)
    CraftDummyWeapon(147, 60130200, 40130200, 13000016)
    AllowWeaponUpgrade(147, 13020009, 8404, 19004147)
    CraftDummyWeapon(148, 60130300, 40130300, 13020009)
    AllowWeaponUpgrade(148, 13030010, 8404, 19004148)
    CraftDummyWeapon(149, 60130400, 40130400, 13010015)
    AllowWeaponUpgrade(149, 13040018, 8404, 19004149)
    CraftDummyWeapon(150, 60140000, 40140000, 14020000)
    AllowWeaponUpgrade(150, 14000003, 8400, 19004150)
    CraftDummyWeapon(151, 60140100, 40140100, 14060005)
    AllowWeaponUpgrade(151, 14010010, 8402, 19004151)
    CraftDummyWeapon(152, 60140200, 40140200, 0)
    AllowWeaponUpgrade(152, 14020000, 0, 19004152)
    CraftDummyWeapon(153, 60140300, 40140300, 14100008)
    AllowWeaponUpgrade(153, 14030010, 8402, 19004153)
    CraftDummyWeapon(154, 60140400, 40140400, 15010010)
    AllowWeaponUpgrade(154, 14040013, 8403, 19004154)
    CraftDummyWeapon(155, 60140500, 40140500, 14080008)
    AllowWeaponUpgrade(155, 14050020, 8404, 19004155)
    CraftDummyWeapon(156, 60140600, 40140600, 14000003)
    AllowWeaponUpgrade(156, 14060005, 8400, 19004156)
    CraftDummyWeapon(157, 60140800, 40140800, 14010010)
    AllowWeaponUpgrade(157, 14080008, 8404, 19004157)
    CraftDummyWeapon(158, 60141000, 40141000, 14060005)
    AllowWeaponUpgrade(158, 14100008, 8401, 19004158)
    CraftDummyWeapon(159, 60141100, 40141100, 14040013)
    AllowWeaponUpgrade(159, 14110015, 8404, 19004159)
    CraftDummyWeapon(160, 60141200, 40141200, 14110015)
    AllowWeaponUpgrade(160, 14120010, 8404, 19004160)
    CraftDummyWeapon(161, 60141400, 40141400, 14110015)
    AllowWeaponUpgrade(161, 14140010, 8404, 19004161)
    CraftDummyWeapon(162, 60150000, 40150000, 15060013)
    AllowWeaponUpgrade(162, 15000014, 8403, 19004162)
    CraftDummyWeapon(163, 60150100, 40150100, 14100008)
    AllowWeaponUpgrade(163, 15010010, 8402, 19004163)
    CraftDummyWeapon(164, 60150200, 40150200, 15060013)
    AllowWeaponUpgrade(164, 15020015, 8404, 19004164)
    CraftDummyWeapon(165, 60150300, 40150300, 15020015)
    AllowWeaponUpgrade(165, 15030018, 8404, 19004165)
    CraftDummyWeapon(166, 60150400, 40150400, 15080016)
    AllowWeaponUpgrade(166, 15040009, 8404, 19004166)
    CraftDummyWeapon(167, 60150500, 40150500, 15010010)
    AllowWeaponUpgrade(167, 15050012, 8403, 19004167)
    CraftDummyWeapon(168, 60150600, 40150600, 15050012)
    AllowWeaponUpgrade(168, 15060013, 8403, 19004168)
    CraftDummyWeapon(169, 60150800, 40150800, 15000014)
    AllowWeaponUpgrade(169, 15080016, 8404, 19004169)
    CraftDummyWeapon(170, 60151100, 40151100, 15030018)
    AllowWeaponUpgrade(170, 15110010, 8404, 19004170)
    CraftDummyWeapon(171, 60151200, 40151200, 14080008)
    AllowWeaponUpgrade(171, 15120020, 8404, 19004171)
    CraftDummyWeapon(172, 60151300, 40151300, 15020015)
    AllowWeaponUpgrade(172, 15130018, 8404, 19004172)
    CraftDummyWeapon(173, 60151400, 40151400, 15130018)
    AllowWeaponUpgrade(173, 15140010, 8404, 19004173)
    CraftDummyWeapon(174, 60160000, 40160000, 1000000)
    AllowWeaponUpgrade(174, 16000003, 8400, 19004174)
    CraftDummyWeapon(175, 60160100, 40160100, 16000003)
    AllowWeaponUpgrade(175, 16010006, 8401, 19004175)
    CraftDummyWeapon(176, 60160200, 40160200, 16030015)
    AllowWeaponUpgrade(176, 16020008, 8404, 19004176)
    CraftDummyWeapon(177, 60160300, 40160300, 16140014)
    AllowWeaponUpgrade(177, 16030015, 8404, 19004177)
    CraftDummyWeapon(178, 60160400, 40160400, 16140014)
    AllowWeaponUpgrade(178, 16040010, 8404, 19004178)
    CraftDummyWeapon(179, 60160500, 40160500, 16150009)
    AllowWeaponUpgrade(179, 16050012, 8403, 19004179)
    CraftDummyWeapon(180, 60160600, 40160600, 16010006)
    AllowWeaponUpgrade(180, 16060009, 8402, 19004180)
    CraftDummyWeapon(181, 60160700, 40160700, 16050012)
    AllowWeaponUpgrade(181, 16070014, 8403, 19004181)
    CraftDummyWeapon(182, 60160800, 40160800, 16060009)
    AllowWeaponUpgrade(182, 16080012, 8403, 19004182)
    CraftDummyWeapon(183, 60160900, 40160900, 16110017)
    AllowWeaponUpgrade(183, 16090010, 8404, 19004183)
    CraftDummyWeapon(184, 60161100, 40161100, 16140014)
    AllowWeaponUpgrade(184, 16110017, 8404, 19004184)
    CraftDummyWeapon(185, 60161200, 40161200, 16160009)
    AllowWeaponUpgrade(185, 16120010, 8404, 19004185)
    CraftDummyWeapon(186, 60161300, 40161300, 16140014)
    AllowWeaponUpgrade(186, 16130009, 8404, 19004186)
    CraftDummyWeapon(187, 60161400, 40161400, 16080012)
    AllowWeaponUpgrade(187, 16140014, 8403, 19004187)
    CraftDummyWeapon(188, 60161500, 40161500, 16010006)
    AllowWeaponUpgrade(188, 16150009, 8402, 19004188)
    CraftDummyWeapon(189, 60161600, 40161600, 16020008)
    AllowWeaponUpgrade(189, 16160009, 8404, 19004189)
    CraftDummyWeapon(190, 60170100, 40170100, 17060016)
    AllowWeaponUpgrade(190, 17010010, 8404, 19004190)
    CraftDummyWeapon(191, 60170200, 40170200, 17070018)
    AllowWeaponUpgrade(191, 17020010, 8404, 19004191)
    CraftDummyWeapon(192, 60170300, 40170300, 0)
    CraftDummyWeapon(193, 60170500, 40170500, 16130009)
    AllowWeaponUpgrade(193, 17050010, 8404, 19004193)
    CraftDummyWeapon(194, 60170600, 40170600, 16070014)
    AllowWeaponUpgrade(194, 17060016, 8404, 19004194)
    CraftDummyWeapon(195, 60170700, 40170700, 17060016)
    AllowWeaponUpgrade(195, 17070018, 8404, 19004195)
    CraftDummyWeapon(196, 60180000, 40180000, 16150009)
    AllowWeaponUpgrade(196, 18000010, 8402, 19004196)
    CraftDummyWeapon(197, 60180100, 40180100, 18000010)
    AllowWeaponUpgrade(197, 18010012, 8403, 19004197)
    CraftDummyWeapon(198, 60180200, 40180200, 18030012)
    AllowWeaponUpgrade(198, 18020014, 8403, 19004198)
    CraftDummyWeapon(199, 60180300, 40180300, 18000010)
    AllowWeaponUpgrade(199, 18030012, 8403, 19004199)
    CraftDummyWeapon(200, 60180400, 40180400, 18110017)
    AllowWeaponUpgrade(200, 18040010, 8404, 19004200)
    CraftDummyWeapon(201, 60180500, 40180500, 18090016)
    AllowWeaponUpgrade(201, 18050016, 8404, 19004201)
    CraftDummyWeapon(202, 60180600, 40180600, 18130017)
    AllowWeaponUpgrade(202, 18060020, 8404, 19004202)
    CraftDummyWeapon(203, 60180700, 40180700, 18010012)
    AllowWeaponUpgrade(203, 18070014, 8403, 19004203)
    CraftDummyWeapon(204, 60180800, 40180800, 18140008)
    AllowWeaponUpgrade(204, 18080009, 8404, 19004204)
    CraftDummyWeapon(205, 60180900, 40180900, 18020014)
    AllowWeaponUpgrade(205, 18090016, 8404, 19004205)
    CraftDummyWeapon(206, 60181000, 40181000, 18130017)
    AllowWeaponUpgrade(206, 18100010, 8404, 19004206)
    CraftDummyWeapon(207, 60181100, 40181100, 18020014)
    AllowWeaponUpgrade(207, 18110017, 8404, 19004207)
    CraftDummyWeapon(208, 60181300, 40181300, 18070014)
    AllowWeaponUpgrade(208, 18130017, 8404, 19004208)
    CraftDummyWeapon(209, 60181400, 40181400, 18020014)
    AllowWeaponUpgrade(209, 18140008, 8404, 19004209)
    CraftDummyWeapon(210, 60181500, 40181500, 18090016)
    AllowWeaponUpgrade(210, 18150018, 8404, 19004210)
    CraftDummyWeapon(211, 60181600, 40181600, 18150018)
    AllowWeaponUpgrade(211, 18160010, 8404, 19004211)
    CraftDummyWeapon(212, 60190000, 40190000, 18020014)
    AllowWeaponUpgrade(212, 19000016, 8404, 19004212)
    CraftDummyWeapon(213, 60190100, 40190100, 19000016)
    AllowWeaponUpgrade(213, 19010018, 8404, 19004213)
    CraftDummyWeapon(214, 60190200, 40190200, 19000016)
    AllowWeaponUpgrade(214, 19020009, 8404, 19004214)
    CraftDummyWeapon(215, 60190600, 40190600, 19020009)
    AllowWeaponUpgrade(215, 19060010, 8404, 19004215)
    CraftDummyWeapon(216, 60200000, 40200000, 0)
    AllowWeaponUpgrade(216, 20000010, 8402, 19004216)
    CraftDummyWeapon(217, 60200200, 40200200, 20000010)
    AllowWeaponUpgrade(217, 20020013, 8403, 19004217)
    CraftDummyWeapon(218, 60200300, 40200300, 20000010)
    AllowWeaponUpgrade(218, 20030010, 8404, 19004218)
    CraftDummyWeapon(219, 60200500, 40200500, 20070017)
    AllowWeaponUpgrade(219, 20050020, 8404, 19004219)
    CraftDummyWeapon(220, 60200600, 40200600, 20000010)
    AllowWeaponUpgrade(220, 20060010, 8404, 19004220)
    CraftDummyWeapon(221, 60200700, 40200700, 20020013)
    AllowWeaponUpgrade(221, 20070017, 8404, 19004221)
    CraftDummyWeapon(222, 60210000, 40210000, 0)
    AllowWeaponUpgrade(222, 21000000, 0, 19004222)
    CraftDummyWeapon(223, 60210100, 40210100, 21000000)
    AllowWeaponUpgrade(223, 21010003, 8400, 19004223)
    CraftDummyWeapon(224, 60210600, 40210600, 21120008)
    AllowWeaponUpgrade(224, 21060010, 8404, 19004224)
    CraftDummyWeapon(225, 60210700, 40210700, 21100006)
    AllowWeaponUpgrade(225, 21070009, 8402, 19004225)
    CraftDummyWeapon(226, 60210800, 40210800, 21070009)
    AllowWeaponUpgrade(226, 21080012, 8403, 19004226)
    CraftDummyWeapon(227, 60211000, 40211000, 21010003)
    AllowWeaponUpgrade(227, 21100006, 8401, 19004227)
    CraftDummyWeapon(228, 60211100, 40211100, 22030018)
    AllowWeaponUpgrade(228, 21110010, 8404, 19004228)
    CraftDummyWeapon(229, 60211200, 40211200, 21080012)
    AllowWeaponUpgrade(229, 21120008, 8404, 19004229)
    CraftDummyWeapon(230, 60211300, 40211300, 22030018)
    AllowWeaponUpgrade(230, 21130010, 8404, 19004230)
    CraftDummyWeapon(231, 60220000, 40220000, 21100006)
    AllowWeaponUpgrade(231, 22000009, 8402, 19004231)
    CraftDummyWeapon(232, 60220100, 40220100, 22000009)
    AllowWeaponUpgrade(232, 22010012, 8403, 19004232)
    CraftDummyWeapon(233, 60220200, 40220200, 22010012)
    AllowWeaponUpgrade(233, 22020015, 8404, 19004233)
    CraftDummyWeapon(234, 60220300, 40220300, 22020015)
    AllowWeaponUpgrade(234, 22030018, 8404, 19004234)
    CraftDummyWeapon(235, 60230000, 40230000, 23020018)
    AllowWeaponUpgrade(235, 23000020, 8404, 19004235)
    CraftDummyWeapon(236, 60230100, 40230100, 12130012)
    AllowWeaponUpgrade(236, 23010008, 8404, 19004236)
    CraftDummyWeapon(237, 60230200, 40230200, 12190014)
    AllowWeaponUpgrade(237, 23020018, 8404, 19004237)
    CraftDummyWeapon(238, 60230300, 40230300, 12160009)
    AllowWeaponUpgrade(238, 23030010, 8404, 19004238)
    CraftDummyWeapon(239, 60230400, 40230400, 15000014)
    AllowWeaponUpgrade(239, 23040017, 8404, 19004239)
    CraftDummyWeapon(240, 60230500, 40230500, 15040009)
    AllowWeaponUpgrade(240, 23050010, 8404, 19004240)
    CraftDummyWeapon(241, 60230600, 40230600, 23040017)
    AllowWeaponUpgrade(241, 23060010, 8404, 19004241)
    CraftDummyWeapon(242, 60230700, 40230700, 23010008)
    AllowWeaponUpgrade(242, 23070010, 8404, 19004242)
    CraftDummyWeapon(243, 60230800, 40230800, 17060016)
    AllowWeaponUpgrade(243, 23080010, 8404, 19004243)
    CraftDummyWeapon(244, 60231000, 40231000, 19010018)
    AllowWeaponUpgrade(244, 23100010, 8404, 19004244)
    CraftDummyWeapon(245, 60231100, 40231100, 23020018)
    AllowWeaponUpgrade(245, 23110020, 8404, 19004245)
    CraftDummyWeapon(246, 60231200, 40231200, 18080009)
    AllowWeaponUpgrade(246, 23120020, 8404, 19004246)
    CraftDummyWeapon(247, 60231300, 40231300, 12010016)
    AllowWeaponUpgrade(247, 23130020, 8404, 19004247)
    CraftDummyWeapon(248, 60231400, 40231400, 23010008)
    AllowWeaponUpgrade(248, 23140010, 8404, 19004248)
    CraftDummyWeapon(249, 60231500, 40231500, 23040017)
    AllowWeaponUpgrade(249, 23150020, 8404, 19004249)
    CraftDummyWeapon(250, 60240000, 40240000, 0)
    CraftDummyWeapon(251, 60240200, 40240200, 0)
    CraftDummyWeapon(252, 60240400, 40240400, 0)
    CraftDummyWeapon(253, 60240500, 40240500, 0)
    CraftDummyWeapon(254, 60240600, 40240600, 0)
    CraftDummyWeapon(255, 60240700, 40240700, 0)
    CraftDummyWeapon(256, 60300000, 40300000, 0)
    CraftDummyWeapon(257, 60300100, 40300100, 0)
    CraftDummyWeapon(258, 60300200, 40300200, 0)
    CraftDummyWeapon(259, 60300300, 40300300, 0)
    CraftDummyWeapon(260, 60300400, 40300400, 0)
    CraftDummyWeapon(261, 60300600, 40300600, 0)
    CraftDummyWeapon(262, 60300700, 40300700, 0)
    CraftDummyWeapon(263, 60300800, 40300800, 0)
    CraftDummyWeapon(264, 60300900, 40300900, 0)
    CraftDummyWeapon(265, 60301000, 40301000, 0)
    CraftDummyWeapon(266, 60301100, 40301100, 0)
    CraftDummyWeapon(267, 60301200, 40301200, 0)
    CraftDummyWeapon(268, 60301300, 40301300, 0)
    CraftDummyWeapon(269, 60301400, 40301400, 0)
    CraftDummyWeapon(270, 60301500, 40301500, 0)
    CraftDummyWeapon(271, 60301900, 40301900, 0)
    CraftDummyWeapon(272, 60302000, 40302000, 0)
    CraftDummyWeapon(273, 60310000, 40310000, 0)
    CraftDummyWeapon(274, 60310100, 40310100, 0)
    CraftDummyWeapon(275, 60310200, 40310200, 0)
    CraftDummyWeapon(276, 60310300, 40310300, 0)
    CraftDummyWeapon(277, 60310400, 40310400, 0)
    CraftDummyWeapon(278, 60310500, 40310500, 0)
    CraftDummyWeapon(279, 60310600, 40310600, 0)
    CraftDummyWeapon(280, 60310700, 40310700, 0)
    CraftDummyWeapon(281, 60310800, 40310800, 0)
    CraftDummyWeapon(282, 60310900, 40310900, 0)
    CraftDummyWeapon(283, 60311000, 40311000, 0)
    CraftDummyWeapon(284, 60311300, 40311300, 0)
    CraftDummyWeapon(285, 60311400, 40311400, 0)
    CraftDummyWeapon(286, 60311700, 40311700, 0)
    CraftDummyWeapon(287, 60311900, 40311900, 0)
    CraftDummyWeapon(288, 60312300, 40312300, 0)
    CraftDummyWeapon(289, 60312400, 40312400, 0)
    CraftDummyWeapon(290, 60312500, 40312500, 0)
    CraftDummyWeapon(291, 60312600, 40312600, 0)
    CraftDummyWeapon(292, 60312700, 40312700, 0)
    CraftDummyWeapon(293, 60312800, 40312800, 0)
    CraftDummyWeapon(294, 60312900, 40312900, 0)
    CraftDummyWeapon(295, 60313000, 40313000, 0)
    CraftDummyWeapon(296, 60313100, 40313100, 0)
    CraftDummyWeapon(297, 60313200, 40313200, 0)
    CraftDummyWeapon(298, 60313300, 40313300, 0)
    CraftDummyWeapon(299, 60313400, 40313400, 0)
    CraftDummyWeapon(300, 60320000, 40320000, 0)
    CraftDummyWeapon(301, 60320200, 40320200, 0)
    CraftDummyWeapon(302, 60320300, 40320300, 0)
    CraftDummyWeapon(303, 60320400, 40320400, 0)
    CraftDummyWeapon(304, 60320500, 40320500, 0)
    CraftDummyWeapon(305, 60320800, 40320800, 0)
    CraftDummyWeapon(306, 60320900, 40320900, 0)
    CraftDummyWeapon(307, 60321200, 40321200, 0)
    CraftDummyWeapon(308, 60321300, 40321300, 0)
    CraftDummyWeapon(309, 60321400, 40321400, 0)
    CraftDummyWeapon(310, 60321500, 40321500, 0)
    CraftDummyWeapon(311, 60321600, 40321600, 0)
    CraftDummyWeapon(312, 60321700, 40321700, 0)
    CraftDummyWeapon(313, 60321900, 40321900, 0)
    CraftDummyWeapon(314, 60322000, 40322000, 0)
    CraftDummyWeapon(315, 60322100, 40322100, 0)
    CraftDummyWeapon(316, 60322200, 40322200, 0)
    CraftDummyWeapon(317, 60322300, 40322300, 0)
    CraftDummyWeapon(318, 60322400, 40322400, 0)
    CraftDummyWeapon(319, 60322500, 40322500, 0)
    CraftDummyWeapon(320, 60322600, 40322600, 0)
    CraftDummyWeapon(321, 60322700, 40322700, 0)
    CraftDummyWeapon(322, 60322800, 40322800, 0)
    CraftDummyWeapon(323, 60322900, 40322900, 0)
    CraftDummyWeapon(324, 60323000, 40323000, 0)
    CraftDummyWeapon(325, 60330000, 40330000, 0)
    CraftDummyWeapon(326, 60330400, 40330400, 0)
    CraftDummyWeapon(327, 60330500, 40330500, 0)
    CraftDummyWeapon(328, 60330600, 40330600, 0)
    CraftDummyWeapon(329, 60330900, 40330900, 0)
    CraftDummyWeapon(330, 60331200, 40331200, 0)
    CraftDummyWeapon(331, 60331300, 40331300, 0)
    CraftDummyWeapon(332, 60331700, 40331700, 0)
    CraftDummyWeapon(333, 60331800, 40331800, 0)
    CraftDummyWeapon(334, 60331900, 40331900, 0)
    CraftDummyWeapon(335, 60332000, 40332000, 0)
    CraftDummyWeapon(336, 60332100, 40332100, 0)
    CraftDummyWeapon(337, 60332300, 40332300, 0)
    CraftDummyWeapon(338, 60332400, 40332400, 0)
    CraftDummyWeapon(339, 60332500, 40332500, 0)
    CraftDummyWeapon(340, 60332600, 40332600, 0)
    CraftDummyWeapon(341, 60332700, 40332700, 0)
    CraftDummyWeapon(342, 60332800, 40332800, 0)
    CraftDummyWeapon(343, 60340000, 40340000, 0)
    CraftDummyWeapon(344, 60340100, 40340100, 0)
    CraftDummyWeapon(345, 60340200, 40340200, 0)
    CraftDummyWeapon(346, 60340300, 40340300, 0)
    CraftDummyWeapon(347, 60340400, 40340400, 0)
    CraftDummyWeapon(348, 60340600, 40340600, 0)
    CraftDummyWeapon(349, 60340700, 40340700, 0)
    CraftDummyWeapon(350, 60340800, 40340800, 0)
    CraftDummyWeapon(351, 60340900, 40340900, 0)
    CraftDummyWeapon(352, 60400000, 40400000, 0)
    AllowWeaponUpgrade(352, 40000000, 0, 19004352)
    CraftDummyWeapon(353, 60400100, 40400100, 40000000)
    AllowWeaponUpgrade(353, 40010005, 8400, 19004353)
    CraftDummyWeapon(354, 60400200, 40400200, 40030003)
    AllowWeaponUpgrade(354, 40020008, 8401, 19004354)
    CraftDummyWeapon(355, 60400300, 40400300, 40000000)
    AllowWeaponUpgrade(355, 40030003, 8401, 19004355)
    CraftDummyWeapon(356, 60400500, 40400500, 40030003)
    AllowWeaponUpgrade(356, 40050010, 8402, 19004356)
    CraftDummyWeapon(357, 60410000, 40410000, 40020008)
    AllowWeaponUpgrade(357, 41000010, 8402, 19004357)
    CraftDummyWeapon(358, 60410100, 40410100, 41000010)
    AllowWeaponUpgrade(358, 41010015, 8404, 19004358)
    CraftDummyWeapon(359, 60410200, 40410200, 41000010)
    AllowWeaponUpgrade(359, 41020015, 8404, 19004359)
    CraftDummyWeapon(360, 60410300, 40410300, 41000010)
    AllowWeaponUpgrade(360, 41030010, 8404, 19004360)
    CraftDummyWeapon(361, 60410400, 40410400, 41000010)
    AllowWeaponUpgrade(361, 41040010, 8404, 19004361)
    CraftDummyWeapon(362, 60410600, 40410600, 40010005)
    AllowWeaponUpgrade(362, 41060008, 8404, 19004362)
    CraftDummyWeapon(363, 60410700, 40410700, 41010015)
    AllowWeaponUpgrade(363, 41070010, 8404, 19004363)
    CraftDummyWeapon(364, 60420000, 40420000, 42010008)
    AllowWeaponUpgrade(364, 42000010, 8404, 19004364)
    CraftDummyWeapon(365, 60420100, 40420100, 42040014)
    AllowWeaponUpgrade(365, 42010008, 8404, 19004365)
    CraftDummyWeapon(366, 60420300, 40420300, 42040014)
    AllowWeaponUpgrade(366, 42030010, 8404, 19004366)
    CraftDummyWeapon(367, 60420400, 40420400, 41000010)
    AllowWeaponUpgrade(367, 42040014, 8403, 19004367)
    CraftDummyWeapon(368, 60430000, 40430000, 41060008)
    AllowWeaponUpgrade(368, 43000010, 8402, 19004368)
    CraftDummyWeapon(369, 60430200, 40430200, 43000010)
    AllowWeaponUpgrade(369, 43020013, 8403, 19004369)
    CraftDummyWeapon(370, 60430300, 40430300, 43020013)
    AllowWeaponUpgrade(370, 43030016, 8404, 19004370)
    CraftDummyWeapon(371, 60430500, 40430500, 43030016)
    AllowWeaponUpgrade(371, 43050010, 8404, 19004371)
    CraftDummyWeapon(372, 60430600, 40430600, 43020013)
    AllowWeaponUpgrade(372, 43060010, 8404, 19004372)
    CraftDummyWeapon(373, 60430800, 40430800, 43030016)
    AllowWeaponUpgrade(373, 43080018, 8404, 19004373)
    CraftDummyWeapon(374, 60431100, 40431100, 43030016)
    AllowWeaponUpgrade(374, 43110010, 8404, 19004374)
    CraftDummyWeapon(375, 60440000, 40440000, 43080018)
    AllowWeaponUpgrade(375, 44000020, 8404, 19004375)
    CraftDummyWeapon(376, 60440100, 40440100, 43080018)
    AllowWeaponUpgrade(376, 44010010, 8404, 19004376)
    # endregion
    
    # Monitor possession of Smith's Hammers for recipe appearance.
    # region Smith's Hammer possession
    MonitorSmithsHammerPossession(0, SmithsHammers.NoviceSmithsHammer, Flags.HasNoviceSmithsHammer)
    MonitorSmithsHammerPossession(1, SmithsHammers.ApprenticeSmithsHammer, Flags.HasApprenticeSmithsHammer)
    MonitorSmithsHammerPossession(2, SmithsHammers.JourneymanSmithsHammer, Flags.HasJourneymanSmithsHammer)
    MonitorSmithsHammerPossession(3, SmithsHammers.ExpertSmithsHammer, Flags.HasExpertSmithsHammer)
    MonitorSmithsHammerPossession(4, SmithsHammers.MasterSmithsHammer, Flags.HasMasterSmithsHammer)
    # endregion


@NeverRestart(Flags.GrowingHunger)
def GrowingHunger():
    """Hunger ticks up every 60 seconds."""

    # Hunger cannot grow while Draught of the Undining is active (or hunger is at max).
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.DraughtOfSatiation)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Hunger15)
    IfConditionTrue(0, 1)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.LimgraveDisease)
    Wait(54.0)  # 10% faster
    SkipLines(1)
    Wait(60.0)

    # INCREMENT HUNGER
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger1)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger1)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger2)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger2)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger2)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger3)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger3)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger3)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger4)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger4)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger4)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger5)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger5)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger5)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger6)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger6)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger6)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger7)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger7)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger7)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger8)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger8)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger8)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger9)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger9)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger9)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger10)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger10)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger10)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger11)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger11)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger11)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger12)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger12)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger12)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger13)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger13)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger13)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger14)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger14)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger14)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger15)
    Restart()

    # Player goes from ZERO hunger to level 1.
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger1)
    Restart()


@NeverRestart(Flags.GrowingThirst)
def GrowingThirst():
    """Thirst ticks up every 100 seconds."""

    # Thirst cannot grow while Draught of Silver Tears is active (or thirst is at max).
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.DraughtOfSilverTears)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Thirst9)
    IfConditionTrue(0, 1)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.LimgraveDisease)
    Wait(90.0)  # 10% faster
    SkipLines(1)
    Wait(100.0)

    # INCREMENT THIRST
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst1)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst1)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst2)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst2)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst2)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst3)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst3)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst3)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst4)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst4)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst4)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst5)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst5)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst5)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst6)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst6)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst6)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst7)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst7)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst7)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst8)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(4, SurvivalEffects.Thirst8)  # 4 lines
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst8)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst9)
    DisplayStatus(SurvivalText.Dehydration)  # Dehydration warning (for health depletion)
    Restart()

    # Player goes from ZERO thirst to level 1.
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst1)
    Restart()


@NeverRestart(Flags.SaveHungerAfterDeath)
def SaveHungerAfterDeath():
    """Synchronizes hunger state across death using flags."""

    # First, if any hunger state flags are enabled, resolve them (apply effect and disable flag).
    SkipLinesIfFlagOff(2, Flags.HasHunger1)
    DisableFlag(Flags.HasHunger1)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger1)

    SkipLinesIfFlagOff(2, Flags.HasHunger2)
    DisableFlag(Flags.HasHunger2)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger2)

    SkipLinesIfFlagOff(2, Flags.HasHunger3)
    DisableFlag(Flags.HasHunger3)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger3)

    SkipLinesIfFlagOff(2, Flags.HasHunger4)
    DisableFlag(Flags.HasHunger4)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger4)

    SkipLinesIfFlagOff(2, Flags.HasHunger5)
    DisableFlag(Flags.HasHunger5)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger5)

    SkipLinesIfFlagOff(2, Flags.HasHunger6)
    DisableFlag(Flags.HasHunger6)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger6)

    SkipLinesIfFlagOff(2, Flags.HasHunger7)
    DisableFlag(Flags.HasHunger7)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger7)

    SkipLinesIfFlagOff(2, Flags.HasHunger8)
    DisableFlag(Flags.HasHunger8)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger8)

    SkipLinesIfFlagOff(2, Flags.HasHunger9)
    DisableFlag(Flags.HasHunger9)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger9)

    SkipLinesIfFlagOff(2, Flags.HasHunger10)
    DisableFlag(Flags.HasHunger10)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger10)

    SkipLinesIfFlagOff(2, Flags.HasHunger11)
    DisableFlag(Flags.HasHunger11)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger11)

    SkipLinesIfFlagOff(2, Flags.HasHunger12)
    DisableFlag(Flags.HasHunger12)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger12)

    SkipLinesIfFlagOff(2, Flags.HasHunger13)
    DisableFlag(Flags.HasHunger13)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger13)

    SkipLinesIfFlagOff(2, Flags.HasHunger14)
    DisableFlag(Flags.HasHunger14)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger14)

    SkipLinesIfFlagOff(2, Flags.HasHunger15)
    DisableFlag(Flags.HasHunger15)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger15)

    # Now, wait for player to die, then enable the appropriate flag for this event to work on next load.
    IfHealthLessThanOrEqual(0, PLAYER, 0)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Hunger1)
    EnableFlag(Flags.HasHunger1)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Hunger2)
    EnableFlag(Flags.HasHunger2)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Hunger3)
    EnableFlag(Flags.HasHunger3)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Hunger4)
    EnableFlag(Flags.HasHunger4)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Hunger5)
    EnableFlag(Flags.HasHunger5)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Hunger6)
    EnableFlag(Flags.HasHunger6)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Hunger7)
    EnableFlag(Flags.HasHunger7)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Hunger8)
    EnableFlag(Flags.HasHunger8)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Hunger9)
    EnableFlag(Flags.HasHunger9)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Hunger10)
    EnableFlag(Flags.HasHunger10)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Hunger11)
    EnableFlag(Flags.HasHunger11)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Hunger12)
    EnableFlag(Flags.HasHunger12)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Hunger13)
    EnableFlag(Flags.HasHunger13)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Hunger14)
    EnableFlag(Flags.HasHunger14)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Hunger15)
    EnableFlag(Flags.HasHunger15)
    return


@NeverRestart(Flags.SaveThirstAfterDeath)
def SaveThirstAfterDeath():
    """Synchronizes thirst state across death using flags."""

    # First, if any thirst state flags are enabled, resolve them (apply effect and disable flag).
    SkipLinesIfFlagOff(2, Flags.HasThirst1)
    DisableFlag(Flags.HasThirst1)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst1)

    SkipLinesIfFlagOff(2, Flags.HasThirst2)
    DisableFlag(Flags.HasThirst2)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst2)

    SkipLinesIfFlagOff(2, Flags.HasThirst3)
    DisableFlag(Flags.HasThirst3)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst3)

    SkipLinesIfFlagOff(2, Flags.HasThirst4)
    DisableFlag(Flags.HasThirst4)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst4)

    SkipLinesIfFlagOff(2, Flags.HasThirst5)
    DisableFlag(Flags.HasThirst5)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst5)

    SkipLinesIfFlagOff(2, Flags.HasThirst6)
    DisableFlag(Flags.HasThirst6)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst6)

    SkipLinesIfFlagOff(2, Flags.HasThirst7)
    DisableFlag(Flags.HasThirst7)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst7)

    SkipLinesIfFlagOff(2, Flags.HasThirst8)
    DisableFlag(Flags.HasThirst8)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst8)

    SkipLinesIfFlagOff(2, Flags.HasThirst9)
    DisableFlag(Flags.HasThirst9)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst9)

    # Now, wait for player to die, then enable the appropriate flag for this event to work on next load.
    IfHealthLessThanOrEqual(0, PLAYER, 0)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Thirst1)
    EnableFlag(Flags.HasThirst1)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Thirst2)
    EnableFlag(Flags.HasThirst2)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Thirst3)
    EnableFlag(Flags.HasThirst3)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Thirst4)
    EnableFlag(Flags.HasThirst4)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Thirst5)
    EnableFlag(Flags.HasThirst5)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Thirst6)
    EnableFlag(Flags.HasThirst6)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Thirst7)
    EnableFlag(Flags.HasThirst7)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Thirst8)
    EnableFlag(Flags.HasThirst8)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Thirst9)
    EnableFlag(Flags.HasThirst8)  # NOTE: Thirst 9 on death leads to thirst 8 on reload.
    return


@NeverRestart(Flags.RelieveHunger_1)
def RelieveHunger_1():
    """Monitors for numerous different "food eaten" special effects and reduces hunger level by 1."""
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.BoneBroth)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.BloodBroth)
    IfConditionFalse(0, -1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BoneBroth)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BloodBroth)
    IfConditionTrue(0, -2)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger1)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger1)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger2)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger2)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger1)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger3)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger3)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger2)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger4)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger4)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger3)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger5)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger5)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger4)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger6)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger6)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger5)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger7)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger7)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger6)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger8)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger8)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger7)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger9)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger9)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger8)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger10)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger10)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger9)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger11)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger11)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger10)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger12)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger12)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger11)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger13)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger13)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger12)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger14)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger14)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger13)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger15)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger15)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger14)
    Restart()

    # Player is not hungry (no effect).
    Restart()


@NeverRestart(Flags.RelieveHunger_2)
def RelieveHunger_2():
    """Monitors for numerous different "food eaten" special effects and reduces hunger level by 2."""
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.BerryMedley1)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.BerryMedley2)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.BerryMedley3)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.MushroomStew)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.GreatBoneBroth)
    IfConditionFalse(0, -1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BerryMedley1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BerryMedley2)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BerryMedley3)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.MushroomStew)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.GreatBoneBroth)
    IfConditionTrue(0, -2)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger1)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger1)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger2)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger2)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger3)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger3)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger1)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger4)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger4)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger2)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger5)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger5)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger3)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger6)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger6)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger4)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger7)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger7)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger5)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger8)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger8)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger6)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger9)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger9)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger7)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger10)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger10)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger8)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger11)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger11)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger9)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger12)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger12)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger10)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger13)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger13)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger11)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger14)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger14)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger12)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger15)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger15)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger13)
    Restart()

    # Player is not hungry (no effect).
    Restart()


@NeverRestart(Flags.RelieveHunger_3)
def RelieveHunger_3():
    """Monitors for numerous different "food eaten" special effects and reduces hunger level by 3."""
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.RawSteak)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.JarBrittle)
    IfConditionFalse(0, -1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.RawSteak)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.JarBrittle)
    IfConditionTrue(0, -2)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger1)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger1)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger2)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger2)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger3)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger3)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger4)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger4)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger1)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger5)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger5)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger2)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger6)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger6)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger3)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger7)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger7)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger4)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger8)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger8)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger5)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger9)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger9)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger6)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger10)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger10)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger7)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger11)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger11)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger8)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger12)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger12)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger9)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger13)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger13)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger10)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger14)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger14)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger11)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger15)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger15)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger12)
    Restart()

    # Player is not hungry (no effect).
    Restart()


@NeverRestart(Flags.RelieveHunger_4)
def RelieveHunger_4():
    """Monitors for numerous different "food eaten" special effects and reduces hunger level by 4."""
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.BerryMedley3)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.MeltedMushroomStew)
    IfConditionFalse(0, -1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BerryMedley3)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.MeltedMushroomStew)
    IfConditionTrue(0, -2)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger1)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger1)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger2)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger2)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger3)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger3)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger4)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger4)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger5)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger5)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger1)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger6)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger6)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger2)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger7)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger7)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger3)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger8)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger8)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger4)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger9)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger9)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger5)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger10)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger10)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger6)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger11)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger11)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger7)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger12)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger12)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger8)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger13)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger13)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger9)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger14)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger14)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger10)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger15)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger15)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger11)
    Restart()

    # Player is not hungry (no effect).
    Restart()


@NeverRestart(Flags.RelieveHunger_5)
def RelieveHunger_5():
    """Monitors for numerous different "food eaten" special effects and reduces hunger level by 5."""
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.SearedSteak)
    IfConditionFalse(0, -1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.SearedSteak)
    IfConditionTrue(0, -2)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger1)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger1)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger2)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger2)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger3)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger3)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger4)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger4)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger5)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger5)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger6)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger6)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger1)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger7)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger7)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger2)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger8)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger8)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger3)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger9)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger9)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger4)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger10)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger10)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger5)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger11)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger11)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger6)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger12)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger12)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger7)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger13)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger13)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger8)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger14)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger14)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger9)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger15)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger15)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger10)
    Restart()

    # Player is not hungry (no effect).
    Restart()


@NeverRestart(Flags.RelieveHunger_6)
def RelieveHunger_6():
    """Monitors for numerous different "food eaten" special effects and reduces hunger level by 6."""
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.RawLiverSteak)
    IfConditionFalse(0, -1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.RawLiverSteak)
    IfConditionTrue(0, -2)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger1)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger1)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger2)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger2)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger3)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger3)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger4)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger4)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger5)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger5)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger6)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger6)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger7)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger7)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger1)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger8)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger8)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger2)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger9)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger9)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger3)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger10)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger10)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger4)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger11)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger11)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger5)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger12)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger12)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger6)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger13)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger13)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger7)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger14)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger14)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger8)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger15)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger15)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger9)
    Restart()

    # Player is not hungry (no effect).
    Restart()


@NeverRestart(Flags.RelieveHunger_8)
def RelieveHunger_8():
    """Monitors for numerous different "food eaten" special effects and reduces hunger level by 8."""
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.SearedLiverSteak)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.DraughtOfSatiation)
    IfConditionFalse(0, -1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.SearedLiverSteak)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.DraughtOfSatiation)
    IfConditionTrue(0, -2)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger1)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger1)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger2)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger2)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger3)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger3)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger4)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger4)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger5)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger5)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger6)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger6)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger7)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger7)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Hunger8)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger8)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger9)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger9)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger1)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger10)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger10)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger2)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger11)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger11)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger3)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger12)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger12)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger4)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger13)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger13)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger5)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger14)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger14)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger6)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Hunger15)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Hunger15)
    AddSpecialEffect(PLAYER, SurvivalEffects.Hunger7)
    Restart()

    # Player is not hungry (no effect).
    Restart()


@NeverRestart(Flags.RelieveThirst_1)
def RelieveThirst_1():
    """Monitors for numerous different "drink consumed" special effects and reduces thirst level by 1."""
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.BerryMedley1)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.MossdewSoup)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.CrystalShardSoup)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.GiantsSoup)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.AmberEyeBrew)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.MagmaticBrew)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.BlossomBrew)
    IfConditionFalse(0, -1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BerryMedley1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.MossdewSoup)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.CrystalShardSoup)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.GiantsSoup)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.AmberEyeBrew)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.MagmaticBrew)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BlossomBrew)
    IfConditionTrue(0, -2)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Thirst1)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst1)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst2)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst2)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst1)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst3)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst3)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst2)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst4)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst4)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst3)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst5)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst5)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst4)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst6)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst6)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst5)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst7)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst7)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst6)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst8)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst8)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst7)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst9)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst9)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst8)
    Restart()

    # No thirst to reduce.
    Restart()


@NeverRestart(Flags.RelieveThirst_2)
def RelieveThirst_2():
    """Monitors for numerous different "drink consumed" special effects and reduces thirst level by 2."""
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.BerryMedley2)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.MushroomStew)
    IfConditionFalse(0, -1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BerryMedley2)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.MushroomStew)
    IfConditionTrue(0, -2)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Thirst1)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst1)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Thirst2)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst2)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst3)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst3)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst1)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst4)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst4)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst2)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst5)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst5)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst3)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst6)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst6)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst4)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst7)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst7)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst5)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst8)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst8)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst6)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst9)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst9)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst7)
    Restart()

    # No thirst to reduce.
    Restart()


@NeverRestart(Flags.RelieveThirst_3)
def RelieveThirst_3():
    """Monitors for numerous different "drink consumed" special effects and reduces thirst level by 3."""
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.BoneBroth)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.BerryMedley3)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.MeltedMushroomStew)
    IfConditionFalse(0, -1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BoneBroth)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BerryMedley3)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.MeltedMushroomStew)
    IfConditionTrue(0, -2)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Thirst1)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst1)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Thirst2)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst2)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Thirst3)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst3)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst4)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst4)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst1)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst5)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst5)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst2)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst6)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst6)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst3)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst7)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst7)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst4)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst8)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst8)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst5)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst9)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst9)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst6)
    Restart()

    # No thirst to reduce.
    Restart()


@NeverRestart(Flags.RelieveThirst_4)
def RelieveThirst_4():
    """Monitors for numerous different "drink consumed" special effects and reduces thirst level by 4."""
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.BloodBroth)
    IfConditionFalse(0, -1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BloodBroth)
    IfConditionTrue(0, -2)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Thirst1)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst1)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Thirst2)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst2)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Thirst3)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst3)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Thirst4)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst4)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst5)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst5)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst1)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst6)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst6)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst2)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst7)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst7)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst3)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst8)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst8)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst4)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst9)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst9)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst5)
    Restart()

    # No thirst to reduce.
    Restart()


@NeverRestart(Flags.RelieveThirst_5)
def RelieveThirst_5():
    """Monitors for numerous different "drink consumed" special effects and reduces thirst level by 5."""
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.GreatBoneBroth)
    IfConditionFalse(0, -1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.GreatBoneBroth)
    IfConditionTrue(0, -2)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Thirst1)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst1)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Thirst2)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst2)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Thirst3)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst3)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Thirst4)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst4)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Thirst5)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst5)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst6)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst6)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst1)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst7)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst7)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst2)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst8)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst8)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst3)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst9)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst9)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst4)
    Restart()

    # No thirst to reduce.
    Restart()


@NeverRestart(Flags.RelieveThirst_6)
def RelieveThirst_6():
    """Monitors for numerous different "drink consumed" special effects and reduces thirst level by 6."""
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.DraughtOfSilverTears)
    IfConditionFalse(0, -1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.DraughtOfSilverTears)
    IfConditionTrue(0, -2)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Thirst1)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst1)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Thirst2)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst2)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Thirst3)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst3)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Thirst4)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst4)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Thirst5)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst5)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Thirst6)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst6)  # no replacement effect
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst7)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst7)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst1)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst8)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst8)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst2)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst9)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst9)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst3)
    Restart()

    # No thirst to reduce.
    Restart()


@NeverRestart(Flags.IncreaseThirst_1)
def IncreaseThirst_1():
    """Various dried/cured meats make you MORE thirsty."""
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.ImmunizingCuredMeat)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.InvigoratingCuredMeat)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.ClarifyingCuredMeat)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.DappledCuredMeat)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.SpellproofDriedLiver)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.FireproofDriedLiver)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.LightningproofDriedLiver)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.HolyproofDriedLiver)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.ImmunizingWhiteCuredMeat)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.InvigoratingWhiteCuredMeat)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.ClarifyingWhiteCuredMeat)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.DappledWhiteCuredMeat)
    IfConditionFalse(0, -1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.ImmunizingCuredMeat)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.InvigoratingCuredMeat)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.ClarifyingCuredMeat)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.DappledCuredMeat)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.SpellproofDriedLiver)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.FireproofDriedLiver)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.LightningproofDriedLiver)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.HolyproofDriedLiver)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.ImmunizingWhiteCuredMeat)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.InvigoratingWhiteCuredMeat)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.ClarifyingWhiteCuredMeat)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.DappledWhiteCuredMeat)
    IfConditionTrue(0, -2)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst1)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst1)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst2)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst2)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst2)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst3)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst3)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst3)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst4)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst4)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst4)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst5)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst5)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst5)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst6)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst6)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst6)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst7)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst7)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst7)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst8)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst8)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst8)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst9)  # max
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Thirst9)
    Restart()  # already at max

    # Thirst increases from 0 to 1.
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst1)
    Restart()


@NeverRestart(Flags.IncreaseThirst_3)
def IncreaseThirst_3():
    """Jar Brittle makes you MORE thirsty."""
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.JarBrittle)
    IfConditionFalse(0, -1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.JarBrittle)
    IfConditionTrue(0, -2)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst1)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst1)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst4)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst2)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst2)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst5)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst3)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst3)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst6)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst4)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst4)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst7)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst5)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst5)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst8)
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst6)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst6)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst9)  # max
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst7)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst7)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst9)  # max
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.Thirst8)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst8)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst9)  # max
    Restart()

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Thirst9)
    Restart()  # already at max

    # Thirst increases from 0 to 3.
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst3)
    Restart()


@NeverRestart(Flags.JarBrittleEffects)
def JarBrittleEffects():
    """Manually chains Jar Brittle SpEffect (which handles hunger/thirst) into temperature protection."""
    IfPlayerHasSpecialEffect(0, SurvivalEffects.JarBrittle)
    IfPlayerDoesNotHaveSpecialEffect(0, SurvivalEffects.JarBrittle)
    AddSpecialEffect(PLAYER, SurvivalEffects.HeatProtection_Moderate)
    AddSpecialEffect(PLAYER, SurvivalEffects.ColdProtection_Moderate)
    return RESTART


@NeverRestart(Flags.CheckMildHeatArea)
def CheckMildHeatArea():
    """Checks if mild heat should be applied to the player due to current time and place."""

    # --- CAELID / ALTUS / LEYNDELL in MIDDLE OF DAY ---
    IfTimeOfDay(1, (10, 0, 0), (17, 0, 0))
    IfFlagOn(-1, Flags.PlayerInCaelid)
    IfFlagOn(-1, Flags.PlayerInAltus)
    IfInsideMap(-1, LEYNDELL_ROYAL_CAPITAL)
    IfInsideMap(-1, LEYNDELL_ASHEN_CAPITAL)
    IfConditionTrue(1, -1)

    # --- MT. GELMIR at NIGHT ---
    IfTimeOfDay(2, (18, 0, 0), (8, 0, 0))
    IfFlagOn(2, Flags.PlayerInMtGelmir)

    # -3: Player is in right time and place.
    IfConditionTrue(-3, 1)
    IfConditionTrue(-3, 2)

    # 3: Player is in right time and place, and does not have any protection.
    IfConditionTrue(3, -3)
    IfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.HeatProtection_Mild)
    IfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.HeatProtection_Moderate)
    IfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.HeatProtection_Severe)

    # MAIN
    IfConditionTrue(0, 3)

    EnableFlag(Flags.ShowMildHeatWarning)
    AddSpecialEffect(PLAYER, SurvivalEffects.Heat_Mild)
    Wait(3.0)
    DisableFlag(Flags.ShowMildHeatWarning)
    return RESTART


@NeverRestart(Flags.CheckModerateHeatArea)
def CheckModerateHeatArea():
    """Checks if moderate heat should be applied to the player due to current time and place."""

    # --- MT.GELMIR at DAY ---
    IfTimeOfDay(1, (8, 0, 0), (18, 0, 0))
    IfFlagOn(1, Flags.PlayerInMtGelmir)

    # --- VOLCANO MANOR at NIGHT ---
    IfTimeOfDay(2, (18, 0, 0), (8, 0, 0))
    IfInsideMap(2, VOLCANO_MANOR)
    # TODO: Exclude initial indoor sections of Volcano Manor, somehow. Hopefully a flag to check.

    # -3: Player is in right time and place.
    IfConditionTrue(-3, 1)
    IfConditionTrue(-3, 2)

    # 3: Player is in right time and place, and does not have MODERATE or SEVERE protection.
    IfConditionTrue(3, -3)
    IfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.HeatProtection_Moderate)
    IfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.HeatProtection_Severe)

    # MAIN
    IfConditionTrue(0, 3)

    EnableFlag(Flags.ShowModerateHeatWarning)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.HeatProtection_Mild)
    AddSpecialEffect(PLAYER, SurvivalEffects.Heat_Mild)
    SkipLines(1)
    AddSpecialEffect(PLAYER, SurvivalEffects.Heat_Moderate)
    Wait(3.0)
    DisableFlag(Flags.ShowModerateHeatWarning)
    return RESTART


@NeverRestart(Flags.CheckSevereHeatArea)
def CheckSevereHeatArea():
    """Checks if severe heat should be applied to the player due to current time and place."""

    # --- VOLCANO MANOR in DAY ---
    IfTimeOfDay(1, (8, 0, 0), (18, 0, 0))
    IfInsideMap(1, VOLCANO_MANOR)
    # TODO: Exclude initial indoor sections of Volcano Manor, somehow. Hopefully a flag to check.

    # --- MOHGWYN PALACE at ANY TIME ---
    IfInsideMap(2, MOHGWYN_PALACE)

    # -3: Player is in right time and place.
    IfConditionTrue(-3, 1)
    IfConditionTrue(-3, 2)

    # 3: Player is in right time and place, and does not have SEVERE protection.
    IfConditionTrue(3, -3)
    IfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.HeatProtection_Severe)

    # MAIN
    IfConditionTrue(0, 3)

    EnableFlag(Flags.ShowSevereHeatWarning)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.HeatProtection_Moderate)
    AddSpecialEffect(PLAYER, SurvivalEffects.Heat_Mild)
    SkipLines(4)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.HeatProtection_Mild)
    AddSpecialEffect(PLAYER, SurvivalEffects.Heat_Moderate)
    SkipLines(1)
    AddSpecialEffect(PLAYER, SurvivalEffects.Heat_Severe)

    Wait(3.0)
    DisableFlag(Flags.ShowSevereHeatWarning)
    return RESTART


@NeverRestart(Flags.CheckMildColdArea)
def CheckMildColdArea():

    # --- NIGHT ---
    IfTimeOfDay(1, (18, 0, 0), (8, 0, 0))

    IfFlagOn(-1, Flags.PlayerInLiurnia)
    IfInsideMap(-1, RAYA_LUCARIA)

    IfConditionTrue(1, -1)

    # --- ALL THE TIME ---

    # SIOFRA RIVER
    IfInsideMap(-2, SIOFRA_RIVER)
    IfInsideMap(-2, SIOFRA_RIVER_START)
    IfConditionTrue(2, -2)

    # -3: Player is in right time and place.
    IfConditionTrue(-3, 1)
    IfConditionTrue(-3, 2)

    # 3: Player is in right time and place, and does not have any protection.
    IfConditionTrue(3, -3)
    IfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.ColdProtection_Mild)
    IfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.ColdProtection_Moderate)
    IfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.ColdProtection_Severe)

    # MAIN
    IfConditionTrue(0, 3)

    EnableFlag(Flags.ShowMildColdWarning)

    AddSpecialEffect(PLAYER, SurvivalEffects.Cold_Mild)
    Wait(3.0)
    DisableFlag(Flags.ShowMildColdWarning)
    return RESTART


@NeverRestart(Flags.CheckModerateColdArea)
def CheckModerateColdArea():
    # --- MOUNTAINTOPS in DAY ---
    IfTimeOfDay(1, (8, 0, 0), (18, 0, 0))
    IfFlagOn(1, Flags.PlayerInMountaintops)

    # --- AINSEL RIVER / DEEPROOT DEPTHS at ANY TIME ---

    # AINSEL RIVER + DEEPROOT DEPTHS
    IfInsideMap(-2, AINSEL_RIVER)  # will include Lake of Rot, which is actually appropriate
    IfInsideMap(-2, DEEPROOT_DEPTHS)
    IfConditionTrue(2, -2)

    # -3: Player is in right time and place.
    IfConditionTrue(-3, 1)
    IfConditionTrue(-3, 2)

    # 3: Player is in right time and place, and does not have any protection.
    IfConditionTrue(3, -3)
    IfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.ColdProtection_Moderate)
    IfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.ColdProtection_Severe)

    # MAIN
    IfConditionTrue(0, 3)

    EnableFlag(Flags.ShowModerateColdWarning)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.ColdProtection_Mild)
    AddSpecialEffect(PLAYER, SurvivalEffects.Cold_Mild)
    SkipLines(1)
    AddSpecialEffect(PLAYER, SurvivalEffects.Cold_Moderate)
    Wait(3.0)
    DisableFlag(Flags.ShowModerateColdWarning)
    return RESTART


@NeverRestart(Flags.CheckSevereColdArea)
def CheckSevereColdArea():
    # --- MOUNTAINTOPS / FARUM AZULA at NIGHT ---
    IfTimeOfDay(1, (18, 0, 0), (8, 0, 0))
    IfFlagOn(-1, Flags.PlayerInMountaintops)
    IfInsideMap(-1, CRUMBLING_FARUM_AZULA)
    IfConditionTrue(1, -1)

    # --- ASTEL at ANY TIME ---
    IfInsideMap(2, ASTEL_ARENA)

    # -3: Player is in right time and place.
    IfConditionTrue(-3, 1)
    IfConditionTrue(-3, 2)

    # 3: Player is in right time and place, and does not have any protection.
    IfConditionTrue(3, -3)
    IfPlayerDoesNotHaveSpecialEffect(3, SurvivalEffects.ColdProtection_Severe)

    # MAIN
    IfConditionTrue(0, 3)

    EnableFlag(Flags.ShowSevereColdWarning)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.ColdProtection_Moderate)
    AddSpecialEffect(PLAYER, SurvivalEffects.Cold_Mild)
    SkipLines(4)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.ColdProtection_Mild)
    AddSpecialEffect(PLAYER, SurvivalEffects.Cold_Moderate)
    SkipLines(1)
    AddSpecialEffect(PLAYER, SurvivalEffects.Cold_Severe)
    Wait(3.0)
    DisableFlag(Flags.ShowSevereColdWarning)
    return RESTART


@NeverRestart(Flags.MildHeatWarning)
def MildHeatWarning():
    Wait(5.0)
    IfFlagOn(0, Flags.ShowMildHeatWarning)
    DisplayStatus(SurvivalText.MildHeatWarning)
    DisableFlag(Flags.ShowMildHeatWarning)
    Wait(115.0)
    return RESTART


@NeverRestart(Flags.ModerateHeatWarning)
def ModerateHeatWarning():
    Wait(5.0)
    IfFlagOn(0, Flags.ShowModerateHeatWarning)
    DisplayStatus(SurvivalText.ModerateHeatWarning)
    DisableFlag(Flags.ShowModerateHeatWarning)
    Wait(115.0)
    return RESTART


@NeverRestart(Flags.SevereHeatWarning)
def SevereHeatWarning():
    Wait(5.0)
    IfFlagOn(0, Flags.ShowSevereHeatWarning)
    DisplayStatus(SurvivalText.SevereHeatWarning)
    DisableFlag(Flags.ShowSevereHeatWarning)
    Wait(115.0)
    return RESTART


@NeverRestart(Flags.MildColdWarning)
def MildColdWarning():
    Wait(5.0)
    IfFlagOn(0, Flags.ShowMildColdWarning)
    DisplayStatus(SurvivalText.MildColdWarning)
    DisableFlag(Flags.ShowMildColdWarning)
    Wait(115.0)
    return RESTART


@NeverRestart(Flags.ModerateColdWarning)
def ModerateColdWarning():
    Wait(5.0)
    IfFlagOn(0, Flags.ShowModerateColdWarning)
    DisplayStatus(SurvivalText.ModerateColdWarning)
    DisableFlag(Flags.ShowModerateColdWarning)
    Wait(115.0)
    return RESTART


@NeverRestart(Flags.SevereColdWarning)
def SevereColdWarning():
    Wait(5.0)
    IfFlagOn(0, Flags.ShowSevereColdWarning)
    DisplayStatus(SurvivalText.SevereColdWarning)
    DisableFlag(Flags.ShowSevereColdWarning)
    Wait(115.0)
    return RESTART


@NeverRestart(Flags.GetDiseaseOverworld)
def GetDiseaseOverworld(
    _, disease_effect: int, location_flag: Flag, had_once_flag: Flag, had_twice_flag: Flag, item: int, item_lot: int
):
    IfPlayerHasGood(7, item)
    SkipLinesIfConditionFalse(2, 7)  # just re-apply effect and end
    AddSpecialEffect(PLAYER, disease_effect)
    End()

    EndIfFlagOn(had_twice_flag)

    IfFlagOn(1, location_flag)
    IfAttackedWithDamageType(1, PLAYER, -1, DamageType.Unspecified)
    IfPlayerDoesNotHaveSpecialEffect(1, disease_effect)
    IfFlagOff(1, Flags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.DiseaseRollLock)
    DisableFlagRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))
    EnableRandomFlagInRange((Flags.DiseaseRollFirst, Flags.DiseaseRollSecond))  # TODO: Last

    IfFlagOn(-2, Flags.DiseaseRollFirst)
    IfFlagOff(2, had_once_flag)
    IfFlagOn(2, Flags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(Flags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(Flags.DiseaseRollLock)

    AwardItemLot(item_lot)  # disease indicator
    AddSpecialEffect(PLAYER, disease_effect)

    SkipLinesIfFlagOn(2, had_once_flag)
    EnableFlag(had_once_flag)
    SkipLines(1)
    EnableFlag(had_twice_flag)


@NeverRestart(Flags.GetDiseaseLegacyDungeon)
def GetDiseaseLegacyDungeon(
    _,
    disease_effect: int,
    a: uchar,
    b: uchar, 
    c: uchar, 
    d: uchar, 
    had_once_flag: Flag, 
    had_twice_flag: Flag,
    item: int,
    item_lot: int,
):
    """Same as overworld check, but checks if player is in map (a, b, c, d) instead."""
    IfPlayerHasGood(7, item)
    SkipLinesIfConditionFalse(2, 7)  # just re-apply disease effect and end
    AddSpecialEffect(PLAYER, disease_effect)
    End()

    EndIfFlagOn(had_twice_flag)

    IfInsideMap(1, (a, b, c, d))
    IfAttackedWithDamageType(1, PLAYER, -1, DamageType.Unspecified)
    IfPlayerDoesNotHaveSpecialEffect(1, disease_effect)
    IfFlagOff(1, Flags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.DiseaseRollLock)
    DisableFlagRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))
    EnableRandomFlagInRange((Flags.DiseaseRollFirst, Flags.DiseaseRollSecond))  # TODO: Last

    IfFlagOn(-2, Flags.DiseaseRollFirst)
    IfFlagOff(2, had_once_flag)
    IfFlagOn(2, Flags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(Flags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(Flags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, disease_effect)
    AwardItemLot(item_lot)  # disease indicator

    SkipLinesIfFlagOn(2, had_once_flag)
    EnableFlag(had_once_flag)
    End()
    EnableFlag(had_twice_flag)


# --- SPECIFIC DISEASE EVENTS ---


@NeverRestart(Flags.GetDiseaseSiofra)
def GetDiseaseSiofra():
    IfPlayerHasGood(7, DiseaseIndicators.SiofraDisease)
    SkipLinesIfConditionFalse(2, 7)  # just re-apply disease effect and end
    AddSpecialEffect(PLAYER, SurvivalEffects.SiofraDisease)
    End()

    EndIfFlagOn(Flags.SiofraDiseaseTwice)

    IfInsideMap(-1, SIOFRA_RIVER)
    IfInsideMap(-1, SIOFRA_RIVER_START)
    IfConditionTrue(1, -1)
    IfAttackedWithDamageType(1, PLAYER, -1, DamageType.Unspecified)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.SiofraDisease)
    IfFlagOff(1, Flags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.DiseaseRollLock)
    DisableFlagRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))
    EnableRandomFlagInRange((Flags.DiseaseRollFirst, Flags.DiseaseRollSecond))  # TODO: Last

    IfFlagOn(-2, Flags.DiseaseRollFirst)
    IfFlagOff(2, Flags.SiofraDiseaseOnce)
    IfFlagOn(2, Flags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(Flags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(Flags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, SurvivalEffects.SiofraDisease)
    AwardItemLot(DiseaseItemLots.SiofraDisease)

    SkipLinesIfFlagOn(2, Flags.SiofraDiseaseOnce)
    EnableFlag(Flags.SiofraDiseaseOnce)
    End()
    EnableFlag(Flags.SiofraDiseaseTwice)


@NeverRestart(Flags.GetDiseaseAinsel)
def GetDiseaseAinsel():
    IfPlayerHasGood(7, DiseaseIndicators.AinselDisease)
    SkipLinesIfConditionFalse(2, 7)  # just re-apply disease effect and end
    AddSpecialEffect(PLAYER, SurvivalEffects.AinselDisease)
    End()

    EndIfFlagOn(Flags.AinselDiseaseTwice)

    IfInsideMap(1, AINSEL_RIVER)
    IfAttackedWithDamageType(1, PLAYER, -1, DamageType.Unspecified)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.AinselDisease)
    IfFlagOff(1, Flags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.DiseaseRollLock)
    DisableFlagRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))
    EnableRandomFlagInRange((Flags.DiseaseRollFirst, Flags.DiseaseRollSecond))  # TODO: Last

    IfFlagOn(-2, Flags.DiseaseRollFirst)
    IfFlagOff(2, Flags.AinselDiseaseOnce)
    IfFlagOn(2, Flags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(Flags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(Flags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, SurvivalEffects.AinselDisease)
    AwardItemLot(DiseaseItemLots.AinselDisease)

    SkipLinesIfFlagOn(2, Flags.AinselDiseaseOnce)
    EnableFlag(Flags.AinselDiseaseOnce)
    End()
    EnableFlag(Flags.AinselDiseaseTwice)


@NeverRestart(Flags.GetDiseaseDeeprootAstel)
def GetDiseaseDeeprootAstel():
    IfPlayerHasGood(7, DiseaseIndicators.DeeprootDisease)
    SkipLinesIfConditionFalse(2, 7)  # just re-apply disease effect and end
    AddSpecialEffect(PLAYER, SurvivalEffects.DeeprootDisease)
    End()

    EndIfFlagOn(Flags.DeeprootDiseaseTwice)

    IfInsideMap(-1, DEEPROOT_DEPTHS)
    IfInsideMap(-1, ASTEL_ARENA)
    IfConditionTrue(1, -1)
    IfAttackedWithDamageType(1, PLAYER, -1, DamageType.Unspecified)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.DeeprootDisease)
    IfFlagOff(1, Flags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.DiseaseRollLock)
    DisableFlagRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))
    EnableRandomFlagInRange((Flags.DiseaseRollFirst, Flags.DiseaseRollSecond))  # TODO: Last

    IfFlagOn(-2, Flags.DiseaseRollFirst)
    IfFlagOff(2, Flags.DeeprootDiseaseOnce)
    IfFlagOn(2, Flags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(Flags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(Flags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, SurvivalEffects.DeeprootDisease)
    AwardItemLot(DiseaseItemLots.DeeprootDisease)

    SkipLinesIfFlagOn(2, Flags.DeeprootDiseaseOnce)
    EnableFlag(Flags.DeeprootDiseaseOnce)
    End()
    EnableFlag(Flags.DeeprootDiseaseTwice)


@NeverRestart(Flags.GetDiseaseRadahn)
def GetDiseaseRadahn():
    """Only afflicted by Radahn himself."""
    IfPlayerHasGood(7, DiseaseIndicators.RadahnDisease)
    SkipLinesIfConditionFalse(2, 7)  # just re-apply disease effect and end
    AddSpecialEffect(PLAYER, SurvivalEffects.RadahnDisease)
    End()

    EndIfFlagOn(Flags.RadahnDiseaseTwice)

    IfAttackedWithDamageType(1, PLAYER, VanillaCharacters.Radahn, DamageType.Unspecified)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.RadahnDisease)
    IfFlagOff(1, Flags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.DiseaseRollLock)
    DisableFlagRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))
    EnableRandomFlagInRange((Flags.DiseaseRollFirst, Flags.DiseaseRollSecond))  # TODO: Last

    IfFlagOn(-2, Flags.DiseaseRollFirst)
    IfFlagOff(2, Flags.RadahnDiseaseOnce)
    IfFlagOn(2, Flags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(Flags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(Flags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, SurvivalEffects.RadahnDisease)
    AwardItemLot(DiseaseItemLots.RadahnDisease)

    SkipLinesIfFlagOn(2, Flags.RadahnDiseaseOnce)
    EnableFlag(Flags.RadahnDiseaseOnce)
    End()
    EnableFlag(Flags.RadahnDiseaseTwice)


# --- GENERIC DUNGEON DISEASES ---


@NeverRestart(Flags.GetDiseaseCatacombs)
def GetDiseaseCatacombs():
    IfPlayerHasGood(7, DiseaseIndicators.CatacombsDisease)
    SkipLinesIfConditionFalse(2, 7)  # just re-apply disease effect and end
    AddSpecialEffect(PLAYER, SurvivalEffects.CatacombsDisease)
    End()

    EndIfFlagOn(Flags.CatacombsDiseaseTwice)

    # NOTE: Excludes Hero's Graves, just because I personally think they're distinct.
    IfInsideMap(-1, TOMBSWARD_CATACOMBS)
    IfInsideMap(-1, IMPALERS_CATACOMBS)
    IfInsideMap(-1, STORMFOOT_CATACOMBS)
    IfInsideMap(-1, ROADS_END_CATACOMBS)
    IfInsideMap(-1, MURKWATER_CATACOMBS)
    IfInsideMap(-1, BLACK_KNIFE_CATACOMBS)
    IfInsideMap(-1, CLIFFBOTTOM_CATACOMBS)
    IfInsideMap(-1, WYNDHAM_CATACOMBS)
    IfInsideMap(-1, DEATHTOUCHED_CATACOMBS)
    IfInsideMap(-1, UNSIGHTLY_CATACOMBS)
    IfInsideMap(-1, AURIZA_SIDE_TOMB)
    IfInsideMap(-1, MINOR_ERDTREE_CATACOMBS)
    IfInsideMap(-1, CAELID_CATACOMBS)
    IfInsideMap(-1, WAR_DEAD_CATACOMBS)
    IfInsideMap(-1, GIANTS_MOUNTAINTOP_CATACOMBS)
    IfInsideMap(-1, CONSECRATED_SNOWFIELD_CATACOMBS)
    IfInsideMap(-1, HIDDEN_PATH_TO_THE_HALIGTREE)
    IfConditionTrue(1, -1)
    IfAttackedWithDamageType(1, PLAYER, -1, DamageType.Unspecified)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.CatacombsDisease)
    IfFlagOff(1, Flags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.DiseaseRollLock)
    DisableFlagRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))
    EnableRandomFlagInRange((Flags.DiseaseRollFirst, Flags.DiseaseRollSecond))  # TODO: Last

    IfFlagOn(-2, Flags.DiseaseRollFirst)
    IfFlagOff(2, Flags.CatacombsDiseaseOnce)
    IfFlagOn(2, Flags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(Flags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(Flags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, SurvivalEffects.CatacombsDisease)
    AwardItemLot(DiseaseItemLots.CatacombsDisease)

    SkipLinesIfFlagOn(2, Flags.CatacombsDiseaseOnce)
    EnableFlag(Flags.CatacombsDiseaseOnce)
    End()
    EnableFlag(Flags.CatacombsDiseaseTwice)


@NeverRestart(Flags.GetDiseaseCaves)
def GetDiseaseCaves():
    IfPlayerHasGood(7, DiseaseIndicators.CaveDisease)
    SkipLinesIfConditionFalse(2, 7)  # just re-apply disease effect and end
    AddSpecialEffect(PLAYER, SurvivalEffects.CaveDisease)
    End()

    EndIfFlagOn(Flags.CaveDiseaseTwice)

    IfInsideMap(-1, MURKWATER_CAVE)
    IfInsideMap(-1, EARTHBORE_CAVE)
    IfInsideMap(-1, TOMBSWARD_CAVE)
    IfInsideMap(-1, GROVESIDE_CAVE)
    IfInsideMap(-1, STILLWATER_CAVE)
    IfInsideMap(-1, LAKESIDE_CRYSTAL_CAVE)
    IfInsideMap(-1, ACADEMY_CRYSTAL_CAVE)
    IfInsideMap(-1, SEETHEWATER_CAVE)
    IfInsideMap(-1, VOLCANO_CAVE)
    IfInsideMap(-1, DRAGONBARROW_CAVE)
    IfInsideMap(-1, SELLIA_HIDEAWAY)
    IfInsideMap(-1, CAVE_OF_THE_FORLORN)
    IfInsideMap(-1, COASTAL_CAVE)
    IfInsideMap(-1, HIGHROAD_CAVE)
    IfInsideMap(-1, PERFUMERS_GROTTO)
    IfInsideMap(-1, SAGES_CAVE)
    IfInsideMap(-1, ABANDONED_CAVE)
    IfInsideMap(-1, GAOL_CAVE)
    IfInsideMap(-1, SPIRITCALLER_CAVE)
    IfConditionTrue(1, -1)
    IfAttackedWithDamageType(1, PLAYER, -1, DamageType.Unspecified)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.CaveDisease)
    IfFlagOff(1, Flags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.DiseaseRollLock)
    DisableFlagRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))
    EnableRandomFlagInRange((Flags.DiseaseRollFirst, Flags.DiseaseRollSecond))  # TODO: Last

    IfFlagOn(-2, Flags.DiseaseRollFirst)
    IfFlagOff(2, Flags.CaveDiseaseOnce)
    IfFlagOn(2, Flags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(Flags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(Flags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, SurvivalEffects.CaveDisease)
    AwardItemLot(DiseaseItemLots.CaveDisease)

    SkipLinesIfFlagOn(2, Flags.CaveDiseaseOnce)
    EnableFlag(Flags.CaveDiseaseOnce)
    End()
    EnableFlag(Flags.CaveDiseaseTwice)


@NeverRestart(Flags.GetDiseaseTunnels)
def GetDiseaseTunnels():
    IfPlayerHasGood(7, DiseaseIndicators.TunnelDisease)
    SkipLinesIfConditionFalse(2, 7)  # just re-apply disease effect and end
    AddSpecialEffect(PLAYER, SurvivalEffects.TunnelDisease)
    End()

    EndIfFlagOn(Flags.TunnelDiseaseTwice)

    IfInsideMap(-1, MORNE_TUNNEL)
    IfInsideMap(-1, LIMGRAVE_TUNNELS)
    IfInsideMap(-1, RAYA_LUCARIA_CRYSTAL_TUNNEL)
    IfInsideMap(-1, OLD_ALTUS_TUNNEL)
    IfInsideMap(-1, ALTUS_TUNNEL)
    IfInsideMap(-1, GAEL_TUNNEL)
    IfInsideMap(-1, SELLIA_CRYSTAL_TUNNEL)
    IfInsideMap(-1, YELOUGH_ANIX_TUNNEL)
    IfConditionTrue(1, -1)
    IfAttackedWithDamageType(1, PLAYER, -1, DamageType.Unspecified)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.TunnelDisease)
    IfFlagOff(1, Flags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.DiseaseRollLock)
    DisableFlagRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))
    EnableRandomFlagInRange((Flags.DiseaseRollFirst, Flags.DiseaseRollSecond))  # TODO: Last

    IfFlagOn(-2, Flags.DiseaseRollFirst)
    IfFlagOff(2, Flags.TunnelDiseaseOnce)
    IfFlagOn(2, Flags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(Flags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(Flags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, SurvivalEffects.TunnelDisease)
    AwardItemLot(DiseaseItemLots.TunnelDisease)

    SkipLinesIfFlagOn(2, Flags.TunnelDiseaseOnce)
    EnableFlag(Flags.TunnelDiseaseOnce)
    End()
    EnableFlag(Flags.TunnelDiseaseTwice)


@RestartOnRest(Flags.CaveDiseaseInDaylight)
def CaveDiseaseInDaylight():
    CancelSpecialEffect(PLAYER, SurvivalEffects.CaveDiseaseDaylight)

    IfPlayerHasSpecialEffect(1, SurvivalEffects.CaveDisease)
    IfTimeOfDay(1, (6, 0, 0), (19, 0, 0))
    IfConditionTrue(0, 1)

    AddSpecialEffect(PLAYER, SurvivalEffects.CaveDiseaseDaylight)

    IfPlayerHasSpecialEffect(2, SurvivalEffects.CaveDisease)
    IfTimeOfDay(2, (6, 0, 0), (19, 0, 0))
    IfConditionFalse(0, 2)

    return RESTART


# --- PURE SCARLET ROT ---


@NeverRestart(Flags.GetPureScarletRot)
def GetPureScarletRot():
    """Chance of proccing each time you get normal scarlet rot.

    100% chance if you are in the Lake of Rot (checking if you're in Ainsel River is sufficient).
    """
    # Not bothering with this for now.
    End()


# --- DISEASE CURES ---


@NeverRestart(Flags.CureDisease)
def CureDisease(_, disease_effect: int, cure_effect: int, disease_item: int, cure_text: int):
    IfPlayerHasSpecialEffect(1, cure_effect)
    IfPlayerHasSpecialEffect(1, disease_effect)
    IfConditionTrue(0, 1)

    CancelSpecialEffect(PLAYER, disease_effect)
    DisplayStatus(cure_text)
    RemoveGoodFromPlayer(disease_item, 99)

    IfPlayerDoesNotHaveSpecialEffect(0, cure_effect)
    return RESTART


# --- MAP CHECKS ---


@NeverRestart(Flags.MonitorInLimgrave)
def MonitorInLimgrave():
    DisableFlag(Flags.PlayerInLimgrave)

    # Most of Limgrave:
    for b in range(40, 46):
        for c in range(30, 40):
            IfInsideMap(-1, (60, b, c, 0))
    # Divine Tower Bridge:
    IfInsideMap(-1, (60, 42, 40, 0))
    IfInsideMap(-1, (60, 43, 40, 0))
    IfInsideMap(-1, (60, 44, 40, 0))
    # Far east:
    IfInsideMap(-1, (60, 46, 36, 0))
    IfInsideMap(-1, (60, 46, 37, 0))
    IfInsideMap(-1, (60, 46, 38, 0))
    # (46, 39) overlaps with Caelid too much.

    IfConditionTrue(1, -1)
    IfFlagOff(1, Flags.PlayerInLegacyDungeon)
    IfFlagOff(1, Flags.PlayerInGenericDungeon)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.PlayerInLimgrave)

    # Most of Limgrave:
    for b in range(40, 46):
        for c in range(30, 40):
            IfInsideMap(-2, (60, b, c, 0))
    # Divine Tower Bridge:
    IfInsideMap(-2, (60, 42, 40, 0))
    IfInsideMap(-2, (60, 43, 40, 0))
    IfInsideMap(-2, (60, 44, 40, 0))
    # Far east:
    IfInsideMap(-2, (60, 46, 36, 0))
    IfInsideMap(-2, (60, 46, 37, 0))
    IfInsideMap(-2, (60, 46, 38, 0))
    # (46, 39) overlaps with Caelid too much.

    IfConditionTrue(2, -2)
    IfFlagOff(2, Flags.PlayerInLegacyDungeon)
    IfFlagOff(2, Flags.PlayerInGenericDungeon)

    IfConditionFalse(0, 2)

    return RESTART


@NeverRestart(Flags.MonitorInLiurnia)
def MonitorInLiurnia():
    DisableFlag(Flags.PlayerInLiurnia)

    # Most of Liurnia can be captured in one rectangle of small maps.
    for b in range(32, 39):
        for c in range(40, 50):
            IfInsideMap(-1, (60, b, c, 0))
    # Caria Manor:
    IfInsideMap(-1, (60, 34, 50, 0))
    IfInsideMap(-1, (60, 35, 50, 0))
    IfInsideMap(-1, (60, 36, 50, 0))
    IfInsideMap(-1, (60, 34, 51, 0))
    IfInsideMap(-1, (60, 35, 51, 0))
    # (37, 50) overlaps Altus too much.

    # Far east (b = 39), excluding Stormveil Castle:
    for c in range(41, 50):
        IfInsideMap(-1, (60, 39, c, 0))

    IfConditionTrue(1, -1)
    IfFlagOff(1, Flags.PlayerInLegacyDungeon)
    IfFlagOff(1, Flags.PlayerInGenericDungeon)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.PlayerInLiurnia)

    # Most of Liurnia can be captured in one rectangle of small maps.
    for b in range(32, 39):
        for c in range(40, 50):
            IfInsideMap(-2, (60, b, c, 0))
    # Caria Manor:
    IfInsideMap(-2, (60, 34, 50, 0))
    IfInsideMap(-2, (60, 35, 50, 0))
    IfInsideMap(-2, (60, 36, 50, 0))
    IfInsideMap(-2, (60, 34, 51, 0))
    IfInsideMap(-2, (60, 35, 51, 0))
    # (37, 50) overlaps Altus too much.

    # Far east (b = 39), excluding Stormveil Castle:
    for c in range(41, 50):
        IfInsideMap(-2, (60, 39, c, 0))

    IfConditionTrue(2, -2)
    IfFlagOff(2, Flags.PlayerInLegacyDungeon)
    IfFlagOff(2, Flags.PlayerInGenericDungeon)

    IfConditionFalse(0, 2)

    return RESTART


@NeverRestart(Flags.MonitorInCaelid)
def MonitorInCaelid():
    DisableFlag(Flags.PlayerInCaelid)

    # Most of Caelid:
    for b in range(47, 50):
        for c in range(36, 42):
            IfInsideMap(-1, (60, b, c, 0))
    # Redmane Castle:
    IfInsideMap(-1, (60, 50, 36, 0))
    IfInsideMap(-1, (60, 51, 36, 0))
    IfInsideMap(-1, (60, 51, 35, 0))
    # Great Jar:
    IfInsideMap(-1, (60, 47, 42, 0))
    # (46, 40) is too close to Limgrave.
    # Sellia/Dragonbarrow:
    IfInsideMap(-1, (60, 50, 39, 0))
    IfInsideMap(-1, (60, 50, 40, 0))
    IfInsideMap(-1, (60, 50, 41, 0))
    IfInsideMap(-1, (60, 51, 40, 0))
    IfInsideMap(-1, (60, 51, 41, 0))
    IfInsideMap(-1, (60, 51, 42, 0))
    IfInsideMap(-1, (60, 51, 43, 0))
    IfInsideMap(-1, (60, 52, 41, 0))
    IfInsideMap(-1, (60, 52, 42, 0))
    IfInsideMap(-1, (60, 52, 43, 0))
    # (51, 39) contains too much of the Wailing Dunes.

    IfConditionTrue(1, -1)
    IfFlagOff(1, Flags.PlayerInLegacyDungeon)
    IfFlagOff(1, Flags.PlayerInGenericDungeon)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.PlayerInCaelid)

    # Most of Caelid:
    for b in range(47, 50):
        for c in range(36, 42):
            IfInsideMap(-2, (60, b, c, 0))
    # Redmane Castle:
    IfInsideMap(-2, (60, 50, 36, 0))
    IfInsideMap(-2, (60, 51, 36, 0))
    IfInsideMap(-2, (60, 51, 35, 0))
    # Great Jar:
    IfInsideMap(-2, (60, 47, 42, 0))
    # (46, 40) is too close to Limgrave.
    # Sellia/Dragonbarrow:
    IfInsideMap(-2, (60, 50, 39, 0))
    IfInsideMap(-2, (60, 50, 40, 0))
    IfInsideMap(-2, (60, 50, 41, 0))
    IfInsideMap(-2, (60, 51, 40, 0))
    IfInsideMap(-2, (60, 51, 41, 0))
    IfInsideMap(-2, (60, 51, 42, 0))
    IfInsideMap(-2, (60, 51, 43, 0))
    IfInsideMap(-2, (60, 52, 41, 0))
    IfInsideMap(-2, (60, 52, 42, 0))
    IfInsideMap(-2, (60, 52, 43, 0))
    # (51, 39) contains too much of the Wailing Dunes.

    IfConditionTrue(2, -2)
    IfFlagOff(2, Flags.PlayerInLegacyDungeon)
    IfFlagOff(2, Flags.PlayerInGenericDungeon)

    IfConditionFalse(0, 2)

    return RESTART


@NeverRestart(Flags.MonitorInAltus)
def MonitorInAltus():
    """Does NOT include Mt. Gelmir."""
    DisableFlag(Flags.PlayerInAltus)

    # Most of Altus:
    for b in range(39, 44):
        for c in range(50, 56):
            IfInsideMap(-1, (60, b, c, 0))
    # Ignoring western lake (too close to Liurnia and Mt. Gelmir).
    # Far east:
    IfInsideMapTile(-1, (60, 44, 52, 0))
    IfInsideMapTile(-1, (60, 44, 53, 0))
    IfInsideMapTile(-1, (60, 45, 52, 0))
    IfInsideMapTile(-1, (60, 45, 53, 0))

    IfConditionTrue(1, -1)
    IfFlagOff(1, Flags.PlayerInLegacyDungeon)
    IfFlagOff(1, Flags.PlayerInGenericDungeon)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.PlayerInAltus)

    # Most of Altus:
    for b in range(39, 44):
        for c in range(50, 56):
            IfInsideMap(-2, (60, b, c, 0))
    # Ignoring western lake (too close to Liurnia and Mt. Gelmir).
    # Far east:
    IfInsideMapTile(-2, (60, 44, 52, 0))
    IfInsideMapTile(-2, (60, 44, 53, 0))
    IfInsideMapTile(-2, (60, 45, 52, 0))
    IfInsideMapTile(-2, (60, 45, 53, 0))

    IfConditionTrue(2, -2)
    IfFlagOff(2, Flags.PlayerInLegacyDungeon)
    IfFlagOff(2, Flags.PlayerInGenericDungeon)

    IfConditionFalse(0, 2)

    return RESTART


@NeverRestart(Flags.MonitorInMtGelmir)
def MonitorInMtGelmir():
    """Does NOT include rest of Altus."""
    DisableFlag(Flags.PlayerInMtGelmir)

    # Most of Mt. Gelmir:
    for b in range(34, 38):
        for c in range(52, 56):
            IfInsideMap(-1, (60, b, c, 0))
    # Western side:
    IfInsideMapTile(-1, (60, 38, 52, 0))
    IfInsideMapTile(-1, (60, 38, 53, 0))
    IfInsideMapTile(-1, (60, 38, 54, 0))

    IfConditionTrue(1, -1)
    IfFlagOff(1, Flags.PlayerInLegacyDungeon)
    IfFlagOff(1, Flags.PlayerInGenericDungeon)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.PlayerInMtGelmir)

    # Most of Mt. Gelmir:
    for b in range(34, 38):
        for c in range(52, 56):
            IfInsideMap(-2, (60, b, c, 0))
    # Western side:
    IfInsideMapTile(-2, (60, 38, 52, 0))
    IfInsideMapTile(-2, (60, 38, 53, 0))
    IfInsideMapTile(-2, (60, 38, 54, 0))

    IfConditionTrue(2, -2)
    IfFlagOff(2, Flags.PlayerInLegacyDungeon)
    IfFlagOff(2, Flags.PlayerInGenericDungeon)

    IfConditionFalse(0, -2)

    return RESTART


@NeverRestart(Flags.MonitorInMountaintops)
def MonitorInMountaintops():
    DisableFlag(Flags.PlayerInMountaintops)

    # Most of Mountaintops:
    for b in range(47, 54):
        for c in range(53, 59):
            IfInsideMap(-1, (60, b, c, 0))
    # Fire Giant arena:
    IfInsideMap(-1, (60, 52, 52, 0))
    IfInsideMap(-1, (60, 53, 52, 0))

    IfConditionTrue(1, -1)
    IfFlagOff(1, Flags.PlayerInLegacyDungeon)
    IfFlagOff(1, Flags.PlayerInGenericDungeon)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.PlayerInMountaintops)

    # Most of Mountaintops:
    for b in range(47, 54):
        for c in range(53, 59):
            IfInsideMap(-2, (60, b, c, 0))
    # Fire Giant arena:
    IfInsideMap(-2, (60, 52, 52, 0))
    IfInsideMap(-2, (60, 53, 52, 0))

    IfConditionTrue(2, -2)
    IfFlagOff(2, Flags.PlayerInLegacyDungeon)
    IfFlagOff(2, Flags.PlayerInGenericDungeon)

    IfConditionFalse(0, 2)

    return RESTART


@NeverRestart(Flags.MonitorInGenericDungeon)
def MonitorInGenericDungeon():
    DisableFlag(Flags.PlayerInGenericDungeon)

    IfInsideMap(-1, TOMBSWARD_CATACOMBS)
    IfInsideMap(-1, IMPALERS_CATACOMBS)
    IfInsideMap(-1, STORMFOOT_CATACOMBS)
    IfInsideMap(-1, ROADS_END_CATACOMBS)
    IfInsideMap(-1, MURKWATER_CATACOMBS)
    IfInsideMap(-1, BLACK_KNIFE_CATACOMBS)
    IfInsideMap(-1, CLIFFBOTTOM_CATACOMBS)
    IfInsideMap(-1, WYNDHAM_CATACOMBS)
    IfInsideMap(-1, DEATHTOUCHED_CATACOMBS)
    IfInsideMap(-1, UNSIGHTLY_CATACOMBS)
    IfInsideMap(-1, AURIZA_SIDE_TOMB)
    IfInsideMap(-1, MINOR_ERDTREE_CATACOMBS)
    IfInsideMap(-1, CAELID_CATACOMBS)
    IfInsideMap(-1, WAR_DEAD_CATACOMBS)
    IfInsideMap(-1, GIANTS_MOUNTAINTOP_CATACOMBS)
    IfInsideMap(-1, CONSECRATED_SNOWFIELD_CATACOMBS)
    IfInsideMap(-1, HIDDEN_PATH_TO_THE_HALIGTREE)

    IfInsideMap(-1, SAINTED_HEROS_GRAVE)
    IfInsideMap(-1, GELMIR_HEROS_GRAVE)
    IfInsideMap(-1, AURIZA_HEROS_GRAVE)
    IfInsideMap(-1, GIANT_CONQUERING_HEROS_GRAVE)

    IfInsideMap(-1, MURKWATER_CAVE)
    IfInsideMap(-1, EARTHBORE_CAVE)
    IfInsideMap(-1, TOMBSWARD_CAVE)
    IfInsideMap(-1, GROVESIDE_CAVE)
    IfInsideMap(-1, STILLWATER_CAVE)
    IfInsideMap(-1, LAKESIDE_CRYSTAL_CAVE)
    IfInsideMap(-1, ACADEMY_CRYSTAL_CAVE)
    IfInsideMap(-1, SEETHEWATER_CAVE)
    IfInsideMap(-1, VOLCANO_CAVE)
    IfInsideMap(-1, DRAGONBARROW_CAVE)
    IfInsideMap(-1, SELLIA_HIDEAWAY)
    IfInsideMap(-1, CAVE_OF_THE_FORLORN)
    IfInsideMap(-1, COASTAL_CAVE)
    IfInsideMap(-1, HIGHROAD_CAVE)
    IfInsideMap(-1, PERFUMERS_GROTTO)
    IfInsideMap(-1, SAGES_CAVE)
    IfInsideMap(-1, ABANDONED_CAVE)
    IfInsideMap(-1, GAOL_CAVE)
    IfInsideMap(-1, SPIRITCALLER_CAVE)

    IfInsideMap(-1, MORNE_TUNNEL)
    IfInsideMap(-1, LIMGRAVE_TUNNELS)
    IfInsideMap(-1, RAYA_LUCARIA_CRYSTAL_TUNNEL)
    IfInsideMap(-1, OLD_ALTUS_TUNNEL)
    IfInsideMap(-1, ALTUS_TUNNEL)
    IfInsideMap(-1, GAEL_TUNNEL)
    IfInsideMap(-1, SELLIA_CRYSTAL_TUNNEL)
    IfInsideMap(-1, YELOUGH_ANIX_TUNNEL)

    IfConditionTrue(0, -1)

    EnableFlag(Flags.PlayerInGenericDungeon)

    IfInsideMap(-2, TOMBSWARD_CATACOMBS)
    IfInsideMap(-2, IMPALERS_CATACOMBS)
    IfInsideMap(-2, STORMFOOT_CATACOMBS)
    IfInsideMap(-2, ROADS_END_CATACOMBS)
    IfInsideMap(-2, MURKWATER_CATACOMBS)
    IfInsideMap(-2, BLACK_KNIFE_CATACOMBS)
    IfInsideMap(-2, CLIFFBOTTOM_CATACOMBS)
    IfInsideMap(-2, WYNDHAM_CATACOMBS)
    IfInsideMap(-2, DEATHTOUCHED_CATACOMBS)
    IfInsideMap(-2, UNSIGHTLY_CATACOMBS)
    IfInsideMap(-2, AURIZA_SIDE_TOMB)
    IfInsideMap(-2, MINOR_ERDTREE_CATACOMBS)
    IfInsideMap(-2, CAELID_CATACOMBS)
    IfInsideMap(-2, WAR_DEAD_CATACOMBS)
    IfInsideMap(-2, GIANTS_MOUNTAINTOP_CATACOMBS)
    IfInsideMap(-2, CONSECRATED_SNOWFIELD_CATACOMBS)
    IfInsideMap(-2, HIDDEN_PATH_TO_THE_HALIGTREE)

    IfInsideMap(-2, SAINTED_HEROS_GRAVE)
    IfInsideMap(-2, GELMIR_HEROS_GRAVE)
    IfInsideMap(-2, AURIZA_HEROS_GRAVE)
    IfInsideMap(-2, GIANT_CONQUERING_HEROS_GRAVE)

    IfInsideMap(-2, MURKWATER_CAVE)
    IfInsideMap(-2, EARTHBORE_CAVE)
    IfInsideMap(-2, TOMBSWARD_CAVE)
    IfInsideMap(-2, GROVESIDE_CAVE)
    IfInsideMap(-2, STILLWATER_CAVE)
    IfInsideMap(-2, LAKESIDE_CRYSTAL_CAVE)
    IfInsideMap(-2, ACADEMY_CRYSTAL_CAVE)
    IfInsideMap(-2, SEETHEWATER_CAVE)
    IfInsideMap(-2, VOLCANO_CAVE)
    IfInsideMap(-2, DRAGONBARROW_CAVE)
    IfInsideMap(-2, SELLIA_HIDEAWAY)
    IfInsideMap(-2, CAVE_OF_THE_FORLORN)
    IfInsideMap(-2, COASTAL_CAVE)
    IfInsideMap(-2, HIGHROAD_CAVE)
    IfInsideMap(-2, PERFUMERS_GROTTO)
    IfInsideMap(-2, SAGES_CAVE)
    IfInsideMap(-2, ABANDONED_CAVE)
    IfInsideMap(-2, GAOL_CAVE)
    IfInsideMap(-2, SPIRITCALLER_CAVE)

    IfInsideMap(-2, MORNE_TUNNEL)
    IfInsideMap(-2, LIMGRAVE_TUNNELS)
    IfInsideMap(-2, RAYA_LUCARIA_CRYSTAL_TUNNEL)
    IfInsideMap(-2, OLD_ALTUS_TUNNEL)
    IfInsideMap(-2, ALTUS_TUNNEL)
    IfInsideMap(-2, GAEL_TUNNEL)
    IfInsideMap(-2, SELLIA_CRYSTAL_TUNNEL)
    IfInsideMap(-2, YELOUGH_ANIX_TUNNEL)

    IfConditionFalse(0, -2)

    return RESTART


@NeverRestart(Flags.MonitorInLegacyDungeon)
def MonitorInLegacyDungeon():
    """Includes underground rivers - basically anywhere except an m60 map tile."""
    DisableFlag(Flags.PlayerInLegacyDungeon)

    IfInsideMap(-1, STORMVEIL_CASTLE)
    IfInsideMap(-1, CHAPEL_OF_ANTICIPATION)
    IfInsideMap(-1, LEYNDELL_ROYAL_CAPITAL)
    IfInsideMap(-1, LEYNDELL_ASHEN_CAPITAL)
    IfInsideMap(-1, ROUNDTABLE_HOLD)
    IfInsideMap(-1, AINSEL_RIVER)
    IfInsideMap(-1, SIOFRA_RIVER)
    IfInsideMap(-1, DEEPROOT_DEPTHS)
    IfInsideMap(-1, ASTEL_ARENA)
    IfInsideMap(-1, MOHGWYN_PALACE)
    IfInsideMap(-1, SIOFRA_RIVER_START)
    IfInsideMap(-1, REGAL_ANCESTOR_LOWER)
    IfInsideMap(-1, REGAL_ANCESTOR_UPPER)
    IfInsideMap(-1, CRUMBLING_FARUM_AZULA)
    IfInsideMap(-1, RAYA_LUCARIA)
    IfInsideMap(-1, HALIGTREE)
    IfInsideMap(-1, VOLCANO_MANOR)
    IfInsideMap(-1, STRANDED_GRAVEYARD)
    IfInsideMap(-1, STONE_PLATFORM)
    IfInsideMap(-1, SHUNNING_GROUNDS)
    IfInsideMap(-1, RUIN_STREWN_PRECIPICE)

    IfConditionTrue(0, -1)

    EnableFlag(Flags.PlayerInLegacyDungeon)

    IfInsideMap(-2, STORMVEIL_CASTLE)
    IfInsideMap(-2, CHAPEL_OF_ANTICIPATION)
    IfInsideMap(-2, LEYNDELL_ROYAL_CAPITAL)
    IfInsideMap(-2, LEYNDELL_ASHEN_CAPITAL)
    IfInsideMap(-2, ROUNDTABLE_HOLD)
    IfInsideMap(-2, AINSEL_RIVER)
    IfInsideMap(-2, SIOFRA_RIVER)
    IfInsideMap(-2, DEEPROOT_DEPTHS)
    IfInsideMap(-2, ASTEL_ARENA)
    IfInsideMap(-2, MOHGWYN_PALACE)
    IfInsideMap(-2, SIOFRA_RIVER_START)
    IfInsideMap(-2, REGAL_ANCESTOR_LOWER)
    IfInsideMap(-2, REGAL_ANCESTOR_UPPER)
    IfInsideMap(-2, CRUMBLING_FARUM_AZULA)
    IfInsideMap(-2, RAYA_LUCARIA)
    IfInsideMap(-2, HALIGTREE)
    IfInsideMap(-2, VOLCANO_MANOR)
    IfInsideMap(-2, STRANDED_GRAVEYARD)
    IfInsideMap(-2, STONE_PLATFORM)
    IfInsideMap(-2, SHUNNING_GROUNDS)
    IfInsideMap(-2, RUIN_STREWN_PRECIPICE)

    IfConditionFalse(0, -2)

    return RESTART


@NeverRestart(Flags.CraftDummyWeaponBase)
def CraftDummyWeapon(_, dummy_weapon_id: int, weapon_item_lot: int, previous_weapon: int):
    """Wait for player to obtain a crafted dummy weapon, then remove it, remove the previous "required" weapon in
    the recipe (if nonzero), and award the real item."""
    IfPlayerHasWeapon(0, dummy_weapon_id)
    RemoveWeaponFromPlayer(dummy_weapon_id, 1)
    AwardItemLot(weapon_item_lot)
    if previous_weapon != 0:
        RemoveWeaponFromPlayer(previous_weapon, 1)  # let's hope the count field actually works now :/
    return RESTART


@NeverRestart(Flags.MonitorWeaponPossessionBase)
def AllowWeaponUpgrade(_, weapon_id: int, hammer_id: int, upgrade_visible_flag: int):
    """Enable `upgrade_visible_flag` as long as player has exactly `weapon_id` AND (if non-zero) `hammer_id`.

    This flag is used to enable the visibility of upgrade recipes that require this weapon.
    """
    DisableFlag(upgrade_visible_flag)
    IfPlayerHasWeapon(1, weapon_id)
    SkipLinesIfEqual(1, hammer_id, 0)
    IfPlayerHasGood(1, hammer_id)
    IfConditionTrue(0, 1)

    EnableFlag(upgrade_visible_flag)  # recipes upgrading from this weapon will be visible

    IfPlayerDoesNotHaveWeapon(-1, weapon_id)
    SkipLinesIfEqual(1, hammer_id, 0)
    IfPlayerDoesNotHaveGood(-1, hammer_id)
    IfConditionTrue(0, -1)

    return RESTART


@NeverRestart(Flags.MonitorSmithsHammerPossession)
def MonitorSmithsHammerPossession(_, hammer_id: int, possession_flag: int):
    DisableFlag(possession_flag)
    IfPlayerHasGood(0, hammer_id)
    EnableFlag(possession_flag)
    IfPlayerDoesNotHaveGood(0, hammer_id)  # will never happen, but whatever
    return RESTART


@NeverRestart(15003999)
def DEBUG_ResetDiseases():
    """Debug event for removing all disease indicators and disabling immunity flags."""
    RemoveGoodFromPlayer(DiseaseIndicators.LimgraveDisease, 99)
    RemoveGoodFromPlayer(DiseaseIndicators.LiurniaDisease, 99)
    RemoveGoodFromPlayer(DiseaseIndicators.CaelidDisease, 99)
    RemoveGoodFromPlayer(DiseaseIndicators.AltusDisease, 99)
    RemoveGoodFromPlayer(DiseaseIndicators.MtGelmirDisease, 99)
    RemoveGoodFromPlayer(DiseaseIndicators.MountaintopsDisease, 99)
    RemoveGoodFromPlayer(DiseaseIndicators.SiofraDisease, 99)
    RemoveGoodFromPlayer(DiseaseIndicators.AinselDisease, 99)
    RemoveGoodFromPlayer(DiseaseIndicators.DeeprootDisease, 99)
    RemoveGoodFromPlayer(DiseaseIndicators.StormveilDisease, 99)
    RemoveGoodFromPlayer(DiseaseIndicators.RayaLucariaDisease, 99)
    RemoveGoodFromPlayer(DiseaseIndicators.RadahnDisease, 99)
    RemoveGoodFromPlayer(DiseaseIndicators.VolcanoManorDisease, 99)
    RemoveGoodFromPlayer(DiseaseIndicators.LeyndellDisease, 99)
    RemoveGoodFromPlayer(DiseaseIndicators.SewersDisease, 99)
    RemoveGoodFromPlayer(DiseaseIndicators.HaligtreeDisease, 99)
    RemoveGoodFromPlayer(DiseaseIndicators.FarumAzulaDisease, 99)
    RemoveGoodFromPlayer(DiseaseIndicators.MohgwynDisease, 99)
    RemoveGoodFromPlayer(DiseaseIndicators.CatacombsDisease, 99)
    RemoveGoodFromPlayer(DiseaseIndicators.CaveDisease, 99)
    RemoveGoodFromPlayer(DiseaseIndicators.TunnelDisease, 99)
    DisableFlagRange((Flags.LimgraveDiseaseOnce, Flags.TunnelDiseaseTwice))

    CancelSpecialEffect(PLAYER, SurvivalEffects.LimgraveDisease)
    CancelSpecialEffect(PLAYER, SurvivalEffects.LiurniaDisease)
    CancelSpecialEffect(PLAYER, SurvivalEffects.CaelidDisease)
    CancelSpecialEffect(PLAYER, SurvivalEffects.AltusDisease)
    CancelSpecialEffect(PLAYER, SurvivalEffects.MtGelmirDisease)
    CancelSpecialEffect(PLAYER, SurvivalEffects.MountaintopsDisease)
    CancelSpecialEffect(PLAYER, SurvivalEffects.SiofraDisease)
    CancelSpecialEffect(PLAYER, SurvivalEffects.AinselDisease)
    CancelSpecialEffect(PLAYER, SurvivalEffects.DeeprootDisease)
    CancelSpecialEffect(PLAYER, SurvivalEffects.StormveilDisease)
    CancelSpecialEffect(PLAYER, SurvivalEffects.RayaLucariaDisease)
    CancelSpecialEffect(PLAYER, SurvivalEffects.RadahnDisease)
    CancelSpecialEffect(PLAYER, SurvivalEffects.VolcanoManorDisease)
    CancelSpecialEffect(PLAYER, SurvivalEffects.LeyndellDisease)
    CancelSpecialEffect(PLAYER, SurvivalEffects.SewersDisease)
    CancelSpecialEffect(PLAYER, SurvivalEffects.HaligtreeDisease)
    CancelSpecialEffect(PLAYER, SurvivalEffects.FarumAzulaDisease)
    CancelSpecialEffect(PLAYER, SurvivalEffects.MohgwynDisease)
    CancelSpecialEffect(PLAYER, SurvivalEffects.CatacombsDisease)
    CancelSpecialEffect(PLAYER, SurvivalEffects.CaveDisease)
    CancelSpecialEffect(PLAYER, SurvivalEffects.TunnelDisease)


@NeverRestart(15003998)
def DEBUG_GetAllMaps():
    """Award all map item lots."""
    AwardItemLot(12010000)
    AwardItemLot(12010010)
    AwardItemLot(12020060)
    AwardItemLot(12030000)
    AwardItemLot(12050000)
    AwardItemLot(1034480200)
    AwardItemLot(1035450100)
    AwardItemLot(1036540500)
    AwardItemLot(1037440210)
    AwardItemLot(1038410200)
    AwardItemLot(1040520500)
    AwardItemLot(1042370200)
    AwardItemLot(1042510500)
    AwardItemLot(1044320000)
    AwardItemLot(1045370020)
    AwardItemLot(1048560700)
    AwardItemLot(1049370500)
    AwardItemLot(1049400500)
    AwardItemLot(1049530700)
    AwardItemLot(1052540700)


@NeverRestart(15003997)
def DEBUG_GetDectusMedallions():
    """Award Dectus item lots."""
    AwardItemLot(1046360500)
    AwardItemLot(1051390900)
