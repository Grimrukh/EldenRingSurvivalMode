"""New common EMEVD events for Elden Ring Survival Mode.

Kept separate to `common.evs.py` because I will probably regenerate the vanilla events in that file from time to time as
my understanding of ER EMEVD instructions becomes better.
"""
from soulstruct.eldenring.events import *
from .survival_enums import *


@NeverRestart(0)
def Constructor():
    """Will be merged with vanilla Common."""

    # TODO: Debugging. Remove for release.
    AwardItemLot(100)

    GrowingHunger()
    GrowingThirst()
    ReduceThirstOnDeath()

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
    # TODO: More hunger/thirst relief items from crab eggs, white meat, etc?

    # region Temperature effect checks
    CheckMildHeatArea()
    CheckModerateHeatArea()
    CheckSevereHeatArea()
    CheckMildColdArea()
    CheckModerateColdArea()
    CheckSevereColdArea()
    # endregion

    # region Disease checks
    GetDiseaseOverworld(
        0,
        SurvivalEffects.LimgravePlague,
        SurvivalFlags.PlayerInLimgrave,
        SurvivalFlags.LimgraveDiseaseOnce,
        SurvivalFlags.LimgraveDiseaseTwice,
        SurvivalText.ContractedLimgraveDisease,
    )
    GetDiseaseOverworld(
        1,
        SurvivalEffects.LiurniaToxin,
        SurvivalFlags.PlayerInLiurnia,
        SurvivalFlags.LiurniaDiseaseOnce,
        SurvivalFlags.LiurniaDiseaseTwice,
        SurvivalText.ContractedLiurniaDisease,
    )
    GetDiseaseOverworld(
        2,
        SurvivalEffects.CaelidParasite,
        SurvivalFlags.PlayerInCaelid,
        SurvivalFlags.CaelidDiseaseOnce,
        SurvivalFlags.CaelidDiseaseTwice,
        SurvivalText.ContractedCaelidDisease,
    )
    GetDiseaseOverworld(
        3,
        SurvivalEffects.AltusFever,
        SurvivalFlags.PlayerInAltus,
        SurvivalFlags.AltusDiseaseOnce,
        SurvivalFlags.AltusDiseaseTwice,
        SurvivalText.ContractedAltusDisease,
    )
    GetDiseaseOverworld(
        4,
        SurvivalEffects.MtGelmirPlague,
        SurvivalFlags.PlayerInMtGelmir,
        SurvivalFlags.MtGelmirDiseaseOnce,
        SurvivalFlags.MtGelmirDiseaseTwice,
        SurvivalText.ContractedMtGelmirDisease,
    )
    GetDiseaseOverworld(
        5,
        SurvivalEffects.MountaintopsParasite,
        SurvivalFlags.PlayerInMountaintops,
        SurvivalFlags.MountaintopsDiseaseOnce,
        SurvivalFlags.MountaintopsDiseaseTwice,
        SurvivalText.ContractedMountaintopsDisease,
    )

    GetDiseaseLegacyDungeon(
        0,
        SurvivalEffects.StormveilPlague,
        10, 0, 0, 0,  # STORMVEIL_CASTLE
        SurvivalFlags.StormveilDiseaseOnce,
        SurvivalFlags.StormveilDiseaseTwice,
        SurvivalText.ContractedStormveilDisease,
    )
    GetDiseaseLegacyDungeon(
        1,
        SurvivalEffects.RayaLucariaFever,
        14, 0, 0, 0,  # RAYA_LUCARIA
        SurvivalFlags.RayaLucariaDiseaseOnce,
        SurvivalFlags.RayaLucariaDiseaseTwice,
        SurvivalText.ContractedRayaLucariaDisease,
    )
    GetDiseaseLegacyDungeon(
        2,
        SurvivalEffects.VolcanoManorToxin,
        16, 0, 0, 0,  # VOLCANO_MANOR (does not matter if you're in the no-attack zone)
        SurvivalFlags.VolcanoManorDiseaseOnce,
        SurvivalFlags.VolcanoManorDiseaseTwice,
        SurvivalText.ContractedVolcanoManorDisease,
    )
    GetDiseaseLegacyDungeon(
        3,
        SurvivalEffects.LeyndellPlague,
        11, 0, 0, 0,  # LEYNDELL_ROYAL_CAPITAL (no disease in Ashen Capital)
        SurvivalFlags.LeyndellDiseaseOnce,
        SurvivalFlags.LeyndellDiseaseTwice,
        SurvivalText.ContractedLeyndellDisease,
    )
    GetDiseaseLegacyDungeon(
        4,
        SurvivalEffects.SewersParasite,
        35, 0, 0, 0,  # SHUNNING_GROUNDS
        SurvivalFlags.SewersDiseaseOnce,
        SurvivalFlags.SewersDiseaseTwice,
        SurvivalText.ContractedSewersDisease,
    )
    GetDiseaseLegacyDungeon(
        5,
        SurvivalEffects.HaligtreePlague,
        15, 0, 0, 0,  # HALIGTREE
        SurvivalFlags.HaligtreeDiseaseOnce,
        SurvivalFlags.HaligtreeDiseaseTwice,
        SurvivalText.ContractedHaligtreeDisease,
    )
    GetDiseaseLegacyDungeon(
        6,
        SurvivalEffects.FarumAzulaFever,
        13, 0, 0, 0,  # CRUMBLING_FARUM_AZULA
        SurvivalFlags.FarumAzulaDiseaseOnce,
        SurvivalFlags.FarumAzulaDiseaseTwice,
        SurvivalText.ContractedFarumAzulaDisease,
    )
    GetDiseaseLegacyDungeon(
        7,
        SurvivalEffects.MohgwynFever,
        12, 5, 0, 0,  # MOHGWYN_PALACE
        SurvivalFlags.MohgwynDiseaseOnce,
        SurvivalFlags.MohgwynDiseaseTwice,
        SurvivalText.ContractedMohgwynDisease,
    )

    GetDiseaseSiofra()
    GetDiseaseAinsel()
    GetDiseaseDeeprootAstel()
    GetDiseaseRadahn()

    GetDiseaseCatacombs()
    GetDiseaseCaves()
    GetDiseaseTunnels()

    # Skipping Pure Scarlet Rot.
    # endregion

    # region Disease cure checks
    CurePlague()
    CureToxin()
    CureFever()
    CureParasite()
    # CurePureScarletRot()
    # endregion

    # Swap dummy weapons for real weapons and monitor weapon possession for upgrading.
    # region Dummy Weapons
    CraftDummyWeapon(0, 60010000, 40010000, 0)
    MonitorWeaponPossession(0, 1000000, 19004000)
    CraftDummyWeapon(1, 60010100, 40010100, 1160009)
    MonitorWeaponPossession(1, 1010010, 19004001)
    CraftDummyWeapon(2, 60010200, 40010200, 1140006)
    MonitorWeaponPossession(2, 1020009, 19004002)
    CraftDummyWeapon(3, 60010300, 40010300, 1140006)
    MonitorWeaponPossession(3, 1030009, 19004003)
    CraftDummyWeapon(4, 60010400, 40010400, 1160009)
    MonitorWeaponPossession(4, 1040010, 19004004)
    CraftDummyWeapon(5, 60010500, 40010500, 1100012)
    MonitorWeaponPossession(5, 1050015, 19004005)
    CraftDummyWeapon(6, 60010600, 40010600, 1030009)
    MonitorWeaponPossession(6, 1060012, 19004006)
    CraftDummyWeapon(7, 60010700, 40010700, 1050015)
    MonitorWeaponPossession(7, 1070010, 19004007)
    CraftDummyWeapon(8, 60010800, 40010800, 1130015)
    MonitorWeaponPossession(8, 1080010, 19004008)
    CraftDummyWeapon(9, 60010900, 40010900, 1000000)
    MonitorWeaponPossession(9, 1090003, 19004009)
    CraftDummyWeapon(10, 60011000, 40011000, 1020009)
    MonitorWeaponPossession(10, 1100012, 19004010)
    CraftDummyWeapon(11, 60011100, 40011100, 1100012)
    MonitorWeaponPossession(11, 1110010, 19004011)
    CraftDummyWeapon(12, 60011300, 40011300, 1060012)
    MonitorWeaponPossession(12, 1130015, 19004012)
    CraftDummyWeapon(13, 60011400, 40011400, 1090003)
    MonitorWeaponPossession(13, 1140006, 19004013)
    CraftDummyWeapon(14, 60011500, 40011500, 1100012)
    MonitorWeaponPossession(14, 1150015, 19004014)
    CraftDummyWeapon(15, 60011600, 40011600, 1150015)
    MonitorWeaponPossession(15, 1160009, 19004015)
    CraftDummyWeapon(16, 60020000, 40020000, 2050004)
    MonitorWeaponPossession(16, 2000006, 19004016)
    CraftDummyWeapon(17, 60020100, 40020100, 1000000)
    MonitorWeaponPossession(17, 2010002, 19004017)
    CraftDummyWeapon(18, 60020200, 40020200, 2000006)
    MonitorWeaponPossession(18, 2020008, 19004018)
    CraftDummyWeapon(19, 60020400, 40020400, 2020008)
    MonitorWeaponPossession(19, 2040010, 19004019)
    CraftDummyWeapon(20, 60020500, 40020500, 2010002)
    MonitorWeaponPossession(20, 2050004, 19004020)
    CraftDummyWeapon(21, 60020600, 40020600, 2040010)
    MonitorWeaponPossession(21, 2060006, 19004021)
    CraftDummyWeapon(22, 60020700, 40020700, 2110008)
    MonitorWeaponPossession(22, 2070009, 19004022)
    CraftDummyWeapon(23, 60020800, 40020800, 7060015)
    MonitorWeaponPossession(23, 2080009, 19004023)
    CraftDummyWeapon(24, 60020900, 40020900, 3050014)
    MonitorWeaponPossession(24, 2090008, 19004024)
    CraftDummyWeapon(25, 60021100, 40021100, 2060006)
    MonitorWeaponPossession(25, 2110008, 19004025)
    CraftDummyWeapon(26, 60021400, 40021400, 2180008)
    MonitorWeaponPossession(26, 2140010, 19004026)
    CraftDummyWeapon(27, 60021500, 40021500, 2000006)
    MonitorWeaponPossession(27, 2150004, 19004027)
    CraftDummyWeapon(28, 60021800, 40021800, 2190007)
    MonitorWeaponPossession(28, 2180008, 19004028)
    CraftDummyWeapon(29, 60021900, 40021900, 2250006)
    MonitorWeaponPossession(29, 2190007, 19004029)
    CraftDummyWeapon(30, 60022000, 40022000, 2070009)
    MonitorWeaponPossession(30, 2200010, 19004030)
    CraftDummyWeapon(31, 60022100, 40022100, 2230012)
    MonitorWeaponPossession(31, 2210015, 19004031)
    CraftDummyWeapon(32, 60022200, 40022200, 2240018)
    MonitorWeaponPossession(32, 2220010, 19004032)
    CraftDummyWeapon(33, 60022300, 40022300, 2040010)
    MonitorWeaponPossession(33, 2230012, 19004033)
    CraftDummyWeapon(34, 60022400, 40022400, 2210015)
    MonitorWeaponPossession(34, 2240018, 19004034)
    CraftDummyWeapon(35, 60022500, 40022500, 2260005)
    MonitorWeaponPossession(35, 2250006, 19004035)
    CraftDummyWeapon(36, 60022600, 40022600, 2150004)
    MonitorWeaponPossession(36, 2260005, 19004036)
    CraftDummyWeapon(37, 60030000, 40030000, 2020008)
    MonitorWeaponPossession(37, 3000009, 19004037)
    CraftDummyWeapon(38, 60030100, 40030100, 3180010)
    MonitorWeaponPossession(38, 3010012, 19004038)
    CraftDummyWeapon(39, 60030200, 40030200, 3080014)
    MonitorWeaponPossession(39, 3020015, 19004039)
    CraftDummyWeapon(40, 60030300, 40030300, 3180010)
    MonitorWeaponPossession(40, 3030012, 19004040)
    CraftDummyWeapon(41, 60030400, 40030400, 3080014)
    MonitorWeaponPossession(41, 3040015, 19004041)
    CraftDummyWeapon(42, 60030500, 40030500, 3010012)
    MonitorWeaponPossession(42, 3050014, 19004042)
    CraftDummyWeapon(43, 60030600, 40030600, 3140009)
    MonitorWeaponPossession(43, 3060010, 19004043)
    CraftDummyWeapon(44, 60030700, 40030700, 3040015)
    MonitorWeaponPossession(44, 3070008, 19004044)
    CraftDummyWeapon(45, 60030800, 40030800, 3030012)
    MonitorWeaponPossession(45, 3080014, 19004045)
    CraftDummyWeapon(46, 60030900, 40030900, 3130009)
    MonitorWeaponPossession(46, 3090010, 19004046)
    CraftDummyWeapon(47, 60031000, 40031000, 2090008)
    MonitorWeaponPossession(47, 3100010, 19004047)
    CraftDummyWeapon(48, 60031300, 40031300, 3070008)
    MonitorWeaponPossession(48, 3130009, 19004048)
    CraftDummyWeapon(49, 60031400, 40031400, 3040015)
    MonitorWeaponPossession(49, 3140009, 19004049)
    CraftDummyWeapon(50, 60031500, 40031500, 3040015)
    MonitorWeaponPossession(50, 3150010, 19004050)
    CraftDummyWeapon(51, 60031600, 40031600, 3050014)
    MonitorWeaponPossession(51, 3160008, 19004051)
    CraftDummyWeapon(52, 60031700, 40031700, 2090008)
    MonitorWeaponPossession(52, 3170010, 19004052)
    CraftDummyWeapon(53, 60031800, 40031800, 3000009)
    MonitorWeaponPossession(53, 3180010, 19004053)
    CraftDummyWeapon(54, 60031900, 40031900, 3040015)
    MonitorWeaponPossession(54, 3190018, 19004054)
    CraftDummyWeapon(55, 60032000, 40032000, 3160008)
    MonitorWeaponPossession(55, 3200010, 19004055)
    CraftDummyWeapon(56, 60032100, 40032100, 3190018)
    MonitorWeaponPossession(56, 3210010, 19004056)
    CraftDummyWeapon(57, 60040000, 40040000, 4010017)
    MonitorWeaponPossession(57, 4000018, 19004057)
    CraftDummyWeapon(58, 60040100, 40040100, 4040016)
    MonitorWeaponPossession(58, 4010017, 19004058)
    CraftDummyWeapon(59, 60040200, 40040200, 4010017)
    MonitorWeaponPossession(59, 4020010, 19004059)
    CraftDummyWeapon(60, 60040300, 40040300, 4040016)
    MonitorWeaponPossession(60, 4030017, 19004060)
    CraftDummyWeapon(61, 60040400, 40040400, 3020015)
    MonitorWeaponPossession(61, 4040016, 19004061)
    CraftDummyWeapon(62, 60040500, 40040500, 4010017)
    MonitorWeaponPossession(62, 4050010, 19004062)
    CraftDummyWeapon(63, 60040600, 40040600, 4110009)
    MonitorWeaponPossession(63, 4060010, 19004063)
    CraftDummyWeapon(64, 60040700, 40040700, 4110009)
    MonitorWeaponPossession(64, 4070010, 19004064)
    CraftDummyWeapon(65, 60040800, 40040800, 4000018)
    MonitorWeaponPossession(65, 4080010, 19004065)
    CraftDummyWeapon(66, 60041000, 40041000, 4000018)
    MonitorWeaponPossession(66, 4100010, 19004066)
    CraftDummyWeapon(67, 60041100, 40041100, 4030017)
    MonitorWeaponPossession(67, 4110009, 19004067)
    CraftDummyWeapon(68, 60050000, 40050000, 5060010)
    MonitorWeaponPossession(68, 5000012, 19004068)
    CraftDummyWeapon(69, 60050100, 40050100, 5000012)
    MonitorWeaponPossession(69, 5010014, 19004069)
    CraftDummyWeapon(70, 60050200, 40050200, 2000006)
    MonitorWeaponPossession(70, 5020008, 19004070)
    CraftDummyWeapon(71, 60050300, 40050300, 5000012)
    MonitorWeaponPossession(71, 5030014, 19004071)
    CraftDummyWeapon(72, 60050400, 40050400, 5030014)
    MonitorWeaponPossession(72, 5040017, 19004072)
    CraftDummyWeapon(73, 60050500, 40050500, 5040017)
    MonitorWeaponPossession(73, 5050010, 19004073)
    CraftDummyWeapon(74, 60050600, 40050600, 5020008)
    MonitorWeaponPossession(74, 5060010, 19004074)
    CraftDummyWeapon(75, 60060000, 40060000, 6010017)
    MonitorWeaponPossession(75, 6000010, 19004075)
    CraftDummyWeapon(76, 60060100, 40060100, 6020016)
    MonitorWeaponPossession(76, 6010017, 19004076)
    CraftDummyWeapon(77, 60060200, 40060200, 5010014)
    MonitorWeaponPossession(77, 6020016, 19004077)
    CraftDummyWeapon(78, 60060400, 40060400, 6010017)
    MonitorWeaponPossession(78, 6040010, 19004078)
    CraftDummyWeapon(79, 60070000, 40070000, 7030006)
    MonitorWeaponPossession(79, 7000008, 19004079)
    CraftDummyWeapon(80, 60070100, 40070100, 7110010)
    MonitorWeaponPossession(80, 7010012, 19004080)
    CraftDummyWeapon(81, 60070200, 40070200, 7060015)
    MonitorWeaponPossession(81, 7020018, 19004081)
    CraftDummyWeapon(82, 60070300, 40070300, 7140004)
    MonitorWeaponPossession(82, 7030006, 19004082)
    CraftDummyWeapon(83, 60070400, 40070400, 7030006)
    MonitorWeaponPossession(83, 7040008, 19004083)
    CraftDummyWeapon(84, 60070500, 40070500, 2080009)
    MonitorWeaponPossession(84, 7050010, 19004084)
    CraftDummyWeapon(85, 60070600, 40070600, 7120012)
    MonitorWeaponPossession(85, 7060015, 19004085)
    CraftDummyWeapon(86, 60070700, 40070700, 2080009)
    MonitorWeaponPossession(86, 7070010, 19004086)
    CraftDummyWeapon(87, 60070800, 40070800, 7000008)
    MonitorWeaponPossession(87, 7080010, 19004087)
    CraftDummyWeapon(88, 60071000, 40071000, 7020018)
    MonitorWeaponPossession(88, 7100010, 19004088)
    CraftDummyWeapon(89, 60071100, 40071100, 7040008)
    MonitorWeaponPossession(89, 7110010, 19004089)
    CraftDummyWeapon(90, 60071200, 40071200, 7080010)
    MonitorWeaponPossession(90, 7120012, 19004090)
    CraftDummyWeapon(91, 60071400, 40071400, 2010002)
    MonitorWeaponPossession(91, 7140004, 19004091)
    CraftDummyWeapon(92, 60071500, 40071500, 7010012)
    MonitorWeaponPossession(92, 7150014, 19004092)
    CraftDummyWeapon(93, 60080100, 40080100, 8060018)
    MonitorWeaponPossession(93, 8010010, 19004093)
    CraftDummyWeapon(94, 60080200, 40080200, 7150014)
    MonitorWeaponPossession(94, 8020016, 19004094)
    CraftDummyWeapon(95, 60080300, 40080300, 8050008)
    MonitorWeaponPossession(95, 8030009, 19004095)
    CraftDummyWeapon(96, 60080400, 40080400, 8060018)
    MonitorWeaponPossession(96, 8040010, 19004096)
    CraftDummyWeapon(97, 60080500, 40080500, 8070012)
    MonitorWeaponPossession(97, 8050008, 19004097)
    CraftDummyWeapon(98, 60080600, 40080600, 8020016)
    MonitorWeaponPossession(98, 8060018, 19004098)
    CraftDummyWeapon(99, 60080700, 40080700, 7080010)
    MonitorWeaponPossession(99, 8070012, 19004099)
    CraftDummyWeapon(100, 60080800, 40080800, 8060018)
    MonitorWeaponPossession(100, 8080020, 19004100)
    CraftDummyWeapon(101, 60081000, 40081000, 8030009)
    MonitorWeaponPossession(101, 8100010, 19004101)
    CraftDummyWeapon(102, 60090000, 40090000, 7080010)
    MonitorWeaponPossession(102, 9000012, 19004102)
    CraftDummyWeapon(103, 60090100, 40090100, 9080015)
    MonitorWeaponPossession(103, 9010017, 19004103)
    CraftDummyWeapon(104, 60090200, 40090200, 9010017)
    MonitorWeaponPossession(104, 9020010, 19004104)
    CraftDummyWeapon(105, 60090300, 40090300, 9080015)
    MonitorWeaponPossession(105, 9030009, 19004105)
    CraftDummyWeapon(106, 60090400, 40090400, 9070008)
    MonitorWeaponPossession(106, 9040010, 19004106)
    CraftDummyWeapon(107, 60090600, 40090600, 9030009)
    MonitorWeaponPossession(107, 9060010, 19004107)
    CraftDummyWeapon(108, 60090700, 40090700, 9080015)
    MonitorWeaponPossession(108, 9070008, 19004108)
    CraftDummyWeapon(109, 60090800, 40090800, 9000012)
    MonitorWeaponPossession(109, 9080015, 19004109)
    CraftDummyWeapon(110, 60100000, 40100000, 2040010)
    MonitorWeaponPossession(110, 10000012, 19004110)
    CraftDummyWeapon(111, 60100100, 40100100, 10030014)
    MonitorWeaponPossession(111, 10010016, 19004111)
    CraftDummyWeapon(112, 60100300, 40100300, 10000012)
    MonitorWeaponPossession(112, 10030014, 19004112)
    CraftDummyWeapon(113, 60100500, 40100500, 10010016)
    MonitorWeaponPossession(113, 10050010, 19004113)
    CraftDummyWeapon(114, 60100800, 40100800, 10030014)
    MonitorWeaponPossession(114, 10080017, 19004114)
    CraftDummyWeapon(115, 60100900, 40100900, 10080017)
    MonitorWeaponPossession(115, 10090010, 19004115)
    CraftDummyWeapon(116, 60110000, 40110000, 11070006)
    MonitorWeaponPossession(116, 11000009, 19004116)
    CraftDummyWeapon(117, 60110100, 40110100, 0)
    MonitorWeaponPossession(117, 11010000, 19004117)
    CraftDummyWeapon(118, 60110300, 40110300, 11010000)
    MonitorWeaponPossession(118, 11030003, 19004118)
    CraftDummyWeapon(119, 60110400, 40110400, 11010000)
    MonitorWeaponPossession(119, 11040003, 19004119)
    CraftDummyWeapon(120, 60110500, 40110500, 11000009)
    MonitorWeaponPossession(120, 11050012, 19004120)
    CraftDummyWeapon(121, 60110600, 40110600, 11090016)
    MonitorWeaponPossession(121, 11060010, 19004121)
    CraftDummyWeapon(122, 60110700, 40110700, 11030003)
    MonitorWeaponPossession(122, 11070006, 19004122)
    CraftDummyWeapon(123, 60110800, 40110800, 11040003)
    MonitorWeaponPossession(123, 11080006, 19004123)
    CraftDummyWeapon(124, 60110900, 40110900, 11050012)
    MonitorWeaponPossession(124, 11090016, 19004124)
    CraftDummyWeapon(125, 60111000, 40111000, 11130007)
    MonitorWeaponPossession(125, 11100008, 19004125)
    CraftDummyWeapon(126, 60111100, 40111100, 11090016)
    MonitorWeaponPossession(126, 11110010, 19004126)
    CraftDummyWeapon(127, 60111200, 40111200, 11130007)
    MonitorWeaponPossession(127, 11120010, 19004127)
    CraftDummyWeapon(128, 60111300, 40111300, 11140009)
    MonitorWeaponPossession(128, 11130007, 19004128)
    CraftDummyWeapon(129, 60111400, 40111400, 11080006)
    MonitorWeaponPossession(129, 11140009, 19004129)
    CraftDummyWeapon(130, 60111500, 40111500, 11100008)
    MonitorWeaponPossession(130, 11150010, 19004130)
    CraftDummyWeapon(131, 60120000, 40120000, 11140009)
    MonitorWeaponPossession(131, 12000010, 19004131)
    CraftDummyWeapon(132, 60120100, 40120100, 12140014)
    MonitorWeaponPossession(132, 12010016, 19004132)
    CraftDummyWeapon(133, 60120200, 40120200, 12140014)
    MonitorWeaponPossession(133, 12020016, 19004133)
    CraftDummyWeapon(134, 60120600, 40120600, 12000010)
    MonitorWeaponPossession(134, 12060012, 19004134)
    CraftDummyWeapon(135, 60120800, 40120800, 12000010)
    MonitorWeaponPossession(135, 12080012, 19004135)
    CraftDummyWeapon(136, 60121300, 40121300, 12000010)
    MonitorWeaponPossession(136, 12130012, 19004136)
    CraftDummyWeapon(137, 60121400, 40121400, 12080012)
    MonitorWeaponPossession(137, 12140014, 19004137)
    CraftDummyWeapon(138, 60121500, 40121500, 12130012)
    MonitorWeaponPossession(138, 12150008, 19004138)
    CraftDummyWeapon(139, 60121600, 40121600, 11100008)
    MonitorWeaponPossession(139, 12160009, 19004139)
    CraftDummyWeapon(140, 60121700, 40121700, 12210018)
    MonitorWeaponPossession(140, 12170010, 19004140)
    CraftDummyWeapon(141, 60121800, 40121800, 11090016)
    MonitorWeaponPossession(141, 12180020, 19004141)
    CraftDummyWeapon(142, 60121900, 40121900, 12060012)
    MonitorWeaponPossession(142, 12190014, 19004142)
    CraftDummyWeapon(143, 60122000, 40122000, 12150008)
    MonitorWeaponPossession(143, 12200010, 19004143)
    CraftDummyWeapon(144, 60122100, 40122100, 12020016)
    MonitorWeaponPossession(144, 12210018, 19004144)
    CraftDummyWeapon(145, 60130000, 40130000, 13010015)
    MonitorWeaponPossession(145, 13000016, 19004145)
    CraftDummyWeapon(146, 60130100, 40130100, 11050012)
    MonitorWeaponPossession(146, 13010015, 19004146)
    CraftDummyWeapon(147, 60130200, 40130200, 13000016)
    MonitorWeaponPossession(147, 13020009, 19004147)
    CraftDummyWeapon(148, 60130300, 40130300, 13020009)
    MonitorWeaponPossession(148, 13030010, 19004148)
    CraftDummyWeapon(149, 60130400, 40130400, 13010015)
    MonitorWeaponPossession(149, 13040018, 19004149)
    CraftDummyWeapon(150, 60140000, 40140000, 14020000)
    MonitorWeaponPossession(150, 14000003, 19004150)
    CraftDummyWeapon(151, 60140100, 40140100, 14060005)
    MonitorWeaponPossession(151, 14010010, 19004151)
    CraftDummyWeapon(152, 60140200, 40140200, 0)
    MonitorWeaponPossession(152, 14020000, 19004152)
    CraftDummyWeapon(153, 60140300, 40140300, 14100008)
    MonitorWeaponPossession(153, 14030010, 19004153)
    CraftDummyWeapon(154, 60140400, 40140400, 15010010)
    MonitorWeaponPossession(154, 14040013, 19004154)
    CraftDummyWeapon(155, 60140500, 40140500, 14080008)
    MonitorWeaponPossession(155, 14050010, 19004155)
    CraftDummyWeapon(156, 60140600, 40140600, 14000003)
    MonitorWeaponPossession(156, 14060005, 19004156)
    CraftDummyWeapon(157, 60140800, 40140800, 14010010)
    MonitorWeaponPossession(157, 14080008, 19004157)
    CraftDummyWeapon(158, 60141000, 40141000, 14060005)
    MonitorWeaponPossession(158, 14100008, 19004158)
    CraftDummyWeapon(159, 60141100, 40141100, 14040013)
    MonitorWeaponPossession(159, 14110015, 19004159)
    CraftDummyWeapon(160, 60141200, 40141200, 14110015)
    MonitorWeaponPossession(160, 14120010, 19004160)
    CraftDummyWeapon(161, 60141400, 40141400, 14110015)
    MonitorWeaponPossession(161, 14140010, 19004161)
    CraftDummyWeapon(162, 60150000, 40150000, 15060013)
    MonitorWeaponPossession(162, 15000014, 19004162)
    CraftDummyWeapon(163, 60150100, 40150100, 14100008)
    MonitorWeaponPossession(163, 15010010, 19004163)
    CraftDummyWeapon(164, 60150200, 40150200, 15060013)
    MonitorWeaponPossession(164, 15020015, 19004164)
    CraftDummyWeapon(165, 60150300, 40150300, 15020015)
    MonitorWeaponPossession(165, 15030018, 19004165)
    CraftDummyWeapon(166, 60150400, 40150400, 15080016)
    MonitorWeaponPossession(166, 15040009, 19004166)
    CraftDummyWeapon(167, 60150500, 40150500, 15010010)
    MonitorWeaponPossession(167, 15050012, 19004167)
    CraftDummyWeapon(168, 60150600, 40150600, 15050012)
    MonitorWeaponPossession(168, 15060013, 19004168)
    CraftDummyWeapon(169, 60150800, 40150800, 15000014)
    MonitorWeaponPossession(169, 15080016, 19004169)
    CraftDummyWeapon(170, 60151100, 40151100, 15030018)
    MonitorWeaponPossession(170, 15110010, 19004170)
    CraftDummyWeapon(171, 60151200, 40151200, 14080008)
    MonitorWeaponPossession(171, 15120020, 19004171)
    CraftDummyWeapon(172, 60151300, 40151300, 15020015)
    MonitorWeaponPossession(172, 15130018, 19004172)
    CraftDummyWeapon(173, 60151400, 40151400, 15130018)
    MonitorWeaponPossession(173, 15140010, 19004173)
    CraftDummyWeapon(174, 60160000, 40160000, 1000000)
    MonitorWeaponPossession(174, 16000003, 19004174)
    CraftDummyWeapon(175, 60160100, 40160100, 16000003)
    MonitorWeaponPossession(175, 16010006, 19004175)
    CraftDummyWeapon(176, 60160200, 40160200, 16030015)
    MonitorWeaponPossession(176, 16020008, 19004176)
    CraftDummyWeapon(177, 60160300, 40160300, 16140014)
    MonitorWeaponPossession(177, 16030015, 19004177)
    CraftDummyWeapon(178, 60160400, 40160400, 16140014)
    MonitorWeaponPossession(178, 16040010, 19004178)
    CraftDummyWeapon(179, 60160500, 40160500, 16150009)
    MonitorWeaponPossession(179, 16050012, 19004179)
    CraftDummyWeapon(180, 60160600, 40160600, 16010006)
    MonitorWeaponPossession(180, 16060009, 19004180)
    CraftDummyWeapon(181, 60160700, 40160700, 16050012)
    MonitorWeaponPossession(181, 16070014, 19004181)
    CraftDummyWeapon(182, 60160800, 40160800, 16060009)
    MonitorWeaponPossession(182, 16080012, 19004182)
    CraftDummyWeapon(183, 60160900, 40160900, 16110017)
    MonitorWeaponPossession(183, 16090010, 19004183)
    CraftDummyWeapon(184, 60161100, 40161100, 16140014)
    MonitorWeaponPossession(184, 16110017, 19004184)
    CraftDummyWeapon(185, 60161200, 40161200, 16160009)
    MonitorWeaponPossession(185, 16120010, 19004185)
    CraftDummyWeapon(186, 60161300, 40161300, 16140014)
    MonitorWeaponPossession(186, 16130009, 19004186)
    CraftDummyWeapon(187, 60161400, 40161400, 16080012)
    MonitorWeaponPossession(187, 16140014, 19004187)
    CraftDummyWeapon(188, 60161500, 40161500, 16010006)
    MonitorWeaponPossession(188, 16150009, 19004188)
    CraftDummyWeapon(189, 60161600, 40161600, 16020008)
    MonitorWeaponPossession(189, 16160009, 19004189)
    CraftDummyWeapon(190, 60170100, 40170100, 17060016)
    MonitorWeaponPossession(190, 17010010, 19004190)
    CraftDummyWeapon(191, 60170200, 40170200, 17070018)
    MonitorWeaponPossession(191, 17020010, 19004191)
    CraftDummyWeapon(192, 60170300, 40170300, 0)
    MonitorWeaponPossession(192, 17030000, 19004192)
    CraftDummyWeapon(193, 60170500, 40170500, 16130009)
    MonitorWeaponPossession(193, 17050010, 19004193)
    CraftDummyWeapon(194, 60170600, 40170600, 16070014)
    MonitorWeaponPossession(194, 17060016, 19004194)
    CraftDummyWeapon(195, 60170700, 40170700, 17060016)
    MonitorWeaponPossession(195, 17070018, 19004195)
    CraftDummyWeapon(196, 60180000, 40180000, 16150009)
    MonitorWeaponPossession(196, 18000010, 19004196)
    CraftDummyWeapon(197, 60180100, 40180100, 18000010)
    MonitorWeaponPossession(197, 18010012, 19004197)
    CraftDummyWeapon(198, 60180200, 40180200, 18030012)
    MonitorWeaponPossession(198, 18020014, 19004198)
    CraftDummyWeapon(199, 60180300, 40180300, 18000010)
    MonitorWeaponPossession(199, 18030012, 19004199)
    CraftDummyWeapon(200, 60180400, 40180400, 18110017)
    MonitorWeaponPossession(200, 18040010, 19004200)
    CraftDummyWeapon(201, 60180500, 40180500, 18090016)
    MonitorWeaponPossession(201, 18050016, 19004201)
    CraftDummyWeapon(202, 60180600, 40180600, 18130017)
    MonitorWeaponPossession(202, 18060020, 19004202)
    CraftDummyWeapon(203, 60180700, 40180700, 18010012)
    MonitorWeaponPossession(203, 18070014, 19004203)
    CraftDummyWeapon(204, 60180800, 40180800, 18140008)
    MonitorWeaponPossession(204, 18080009, 19004204)
    CraftDummyWeapon(205, 60180900, 40180900, 18020014)
    MonitorWeaponPossession(205, 18090016, 19004205)
    CraftDummyWeapon(206, 60181000, 40181000, 18130017)
    MonitorWeaponPossession(206, 18100010, 19004206)
    CraftDummyWeapon(207, 60181100, 40181100, 18020014)
    MonitorWeaponPossession(207, 18110017, 19004207)
    CraftDummyWeapon(208, 60181300, 40181300, 18070014)
    MonitorWeaponPossession(208, 18130017, 19004208)
    CraftDummyWeapon(209, 60181400, 40181400, 18020014)
    MonitorWeaponPossession(209, 18140008, 19004209)
    CraftDummyWeapon(210, 60181500, 40181500, 18090016)
    MonitorWeaponPossession(210, 18150018, 19004210)
    CraftDummyWeapon(211, 60181600, 40181600, 18150018)
    MonitorWeaponPossession(211, 18160020, 19004211)
    CraftDummyWeapon(212, 60190000, 40190000, 18020014)
    MonitorWeaponPossession(212, 19000016, 19004212)
    CraftDummyWeapon(213, 60190100, 40190100, 19000016)
    MonitorWeaponPossession(213, 19010018, 19004213)
    CraftDummyWeapon(214, 60190200, 40190200, 19000016)
    MonitorWeaponPossession(214, 19020009, 19004214)
    CraftDummyWeapon(215, 60190600, 40190600, 19020009)
    MonitorWeaponPossession(215, 19060010, 19004215)
    CraftDummyWeapon(216, 60200000, 40200000, 0)
    MonitorWeaponPossession(216, 20000010, 19004216)
    CraftDummyWeapon(217, 60200200, 40200200, 20000010)
    MonitorWeaponPossession(217, 20020013, 19004217)
    CraftDummyWeapon(218, 60200300, 40200300, 20000010)
    MonitorWeaponPossession(218, 20030010, 19004218)
    CraftDummyWeapon(219, 60200500, 40200500, 20070017)
    MonitorWeaponPossession(219, 20050015, 19004219)
    CraftDummyWeapon(220, 60200600, 40200600, 20000010)
    MonitorWeaponPossession(220, 20060010, 19004220)
    CraftDummyWeapon(221, 60200700, 40200700, 20020013)
    MonitorWeaponPossession(221, 20070017, 19004221)
    CraftDummyWeapon(222, 60210000, 40210000, 0)
    MonitorWeaponPossession(222, 21000000, 19004222)
    CraftDummyWeapon(223, 60210100, 40210100, 21000000)
    MonitorWeaponPossession(223, 21010003, 19004223)
    CraftDummyWeapon(224, 60210600, 40210600, 21120008)
    MonitorWeaponPossession(224, 21060010, 19004224)
    CraftDummyWeapon(225, 60210700, 40210700, 21100006)
    MonitorWeaponPossession(225, 21070009, 19004225)
    CraftDummyWeapon(226, 60210800, 40210800, 21070009)
    MonitorWeaponPossession(226, 21080012, 19004226)
    CraftDummyWeapon(227, 60211000, 40211000, 21010003)
    MonitorWeaponPossession(227, 21100006, 19004227)
    CraftDummyWeapon(228, 60211100, 40211100, 22030018)
    MonitorWeaponPossession(228, 21110010, 19004228)
    CraftDummyWeapon(229, 60211200, 40211200, 21080012)
    MonitorWeaponPossession(229, 21120008, 19004229)
    CraftDummyWeapon(230, 60211300, 40211300, 22030018)
    MonitorWeaponPossession(230, 21130010, 19004230)
    CraftDummyWeapon(231, 60220000, 40220000, 21100006)
    MonitorWeaponPossession(231, 22000009, 19004231)
    CraftDummyWeapon(232, 60220100, 40220100, 22000009)
    MonitorWeaponPossession(232, 22010012, 19004232)
    CraftDummyWeapon(233, 60220200, 40220200, 22010012)
    MonitorWeaponPossession(233, 22020015, 19004233)
    CraftDummyWeapon(234, 60220300, 40220300, 22020015)
    MonitorWeaponPossession(234, 22030018, 19004234)
    CraftDummyWeapon(235, 60230000, 40230000, 23020018)
    MonitorWeaponPossession(235, 23000020, 19004235)
    CraftDummyWeapon(236, 60230100, 40230100, 12130012)
    MonitorWeaponPossession(236, 23010008, 19004236)
    CraftDummyWeapon(237, 60230200, 40230200, 12190014)
    MonitorWeaponPossession(237, 23020018, 19004237)
    CraftDummyWeapon(238, 60230300, 40230300, 12160009)
    MonitorWeaponPossession(238, 23030010, 19004238)
    CraftDummyWeapon(239, 60230400, 40230400, 15000014)
    MonitorWeaponPossession(239, 23040017, 19004239)
    CraftDummyWeapon(240, 60230500, 40230500, 15040009)
    MonitorWeaponPossession(240, 23050010, 19004240)
    CraftDummyWeapon(241, 60230600, 40230600, 23040017)
    MonitorWeaponPossession(241, 23060010, 19004241)
    CraftDummyWeapon(242, 60230700, 40230700, 23010008)
    MonitorWeaponPossession(242, 23070010, 19004242)
    CraftDummyWeapon(243, 60230800, 40230800, 17060016)
    MonitorWeaponPossession(243, 23080010, 19004243)
    CraftDummyWeapon(244, 60231000, 40231000, 19010018)
    MonitorWeaponPossession(244, 23100010, 19004244)
    CraftDummyWeapon(245, 60231100, 40231100, 23020018)
    MonitorWeaponPossession(245, 23110020, 19004245)
    CraftDummyWeapon(246, 60231200, 40231200, 18080009)
    MonitorWeaponPossession(246, 23120010, 19004246)
    CraftDummyWeapon(247, 60231300, 40231300, 12010016)
    MonitorWeaponPossession(247, 23130020, 19004247)
    CraftDummyWeapon(248, 60231400, 40231400, 23010008)
    MonitorWeaponPossession(248, 23140010, 19004248)
    CraftDummyWeapon(249, 60231500, 40231500, 23040017)
    MonitorWeaponPossession(249, 23150020, 19004249)
    CraftDummyWeapon(250, 60240000, 40240000, 0)
    MonitorWeaponPossession(250, 24000000, 19004250)
    CraftDummyWeapon(251, 60240200, 40240200, 0)
    MonitorWeaponPossession(251, 24020000, 19004251)
    CraftDummyWeapon(252, 60240400, 40240400, 0)
    MonitorWeaponPossession(252, 24040000, 19004252)
    CraftDummyWeapon(253, 60240500, 40240500, 0)
    MonitorWeaponPossession(253, 24050000, 19004253)
    CraftDummyWeapon(254, 60240600, 40240600, 0)
    MonitorWeaponPossession(254, 24060000, 19004254)
    CraftDummyWeapon(255, 60240700, 40240700, 0)
    MonitorWeaponPossession(255, 24070000, 19004255)
    CraftDummyWeapon(256, 60300000, 40300000, 0)
    MonitorWeaponPossession(256, 30000000, 19004256)
    CraftDummyWeapon(257, 60300100, 40300100, 0)
    MonitorWeaponPossession(257, 30010000, 19004257)
    CraftDummyWeapon(258, 60300200, 40300200, 0)
    MonitorWeaponPossession(258, 30020000, 19004258)
    CraftDummyWeapon(259, 60300300, 40300300, 0)
    MonitorWeaponPossession(259, 30030000, 19004259)
    CraftDummyWeapon(260, 60300400, 40300400, 0)
    MonitorWeaponPossession(260, 30040000, 19004260)
    CraftDummyWeapon(261, 60300600, 40300600, 0)
    MonitorWeaponPossession(261, 30060000, 19004261)
    CraftDummyWeapon(262, 60300700, 40300700, 0)
    MonitorWeaponPossession(262, 30070000, 19004262)
    CraftDummyWeapon(263, 60300800, 40300800, 0)
    MonitorWeaponPossession(263, 30080000, 19004263)
    CraftDummyWeapon(264, 60300900, 40300900, 0)
    MonitorWeaponPossession(264, 30090000, 19004264)
    CraftDummyWeapon(265, 60301000, 40301000, 0)
    MonitorWeaponPossession(265, 30100000, 19004265)
    CraftDummyWeapon(266, 60301100, 40301100, 0)
    MonitorWeaponPossession(266, 30110000, 19004266)
    CraftDummyWeapon(267, 60301200, 40301200, 0)
    MonitorWeaponPossession(267, 30120000, 19004267)
    CraftDummyWeapon(268, 60301300, 40301300, 0)
    MonitorWeaponPossession(268, 30130000, 19004268)
    CraftDummyWeapon(269, 60301400, 40301400, 0)
    MonitorWeaponPossession(269, 30140000, 19004269)
    CraftDummyWeapon(270, 60301500, 40301500, 0)
    MonitorWeaponPossession(270, 30150000, 19004270)
    CraftDummyWeapon(271, 60301900, 40301900, 0)
    MonitorWeaponPossession(271, 30190000, 19004271)
    CraftDummyWeapon(272, 60302000, 40302000, 0)
    MonitorWeaponPossession(272, 30200000, 19004272)
    CraftDummyWeapon(273, 60310000, 40310000, 0)
    MonitorWeaponPossession(273, 31000000, 19004273)
    CraftDummyWeapon(274, 60310100, 40310100, 0)
    MonitorWeaponPossession(274, 31010000, 19004274)
    CraftDummyWeapon(275, 60310200, 40310200, 0)
    MonitorWeaponPossession(275, 31020000, 19004275)
    CraftDummyWeapon(276, 60310300, 40310300, 0)
    MonitorWeaponPossession(276, 31030000, 19004276)
    CraftDummyWeapon(277, 60310400, 40310400, 0)
    MonitorWeaponPossession(277, 31040000, 19004277)
    CraftDummyWeapon(278, 60310500, 40310500, 0)
    MonitorWeaponPossession(278, 31050000, 19004278)
    CraftDummyWeapon(279, 60310600, 40310600, 0)
    MonitorWeaponPossession(279, 31060000, 19004279)
    CraftDummyWeapon(280, 60310700, 40310700, 0)
    MonitorWeaponPossession(280, 31070000, 19004280)
    CraftDummyWeapon(281, 60310800, 40310800, 0)
    MonitorWeaponPossession(281, 31080000, 19004281)
    CraftDummyWeapon(282, 60310900, 40310900, 0)
    MonitorWeaponPossession(282, 31090000, 19004282)
    CraftDummyWeapon(283, 60311000, 40311000, 0)
    MonitorWeaponPossession(283, 31100000, 19004283)
    CraftDummyWeapon(284, 60311300, 40311300, 0)
    MonitorWeaponPossession(284, 31130000, 19004284)
    CraftDummyWeapon(285, 60311400, 40311400, 0)
    MonitorWeaponPossession(285, 31140000, 19004285)
    CraftDummyWeapon(286, 60311700, 40311700, 0)
    MonitorWeaponPossession(286, 31170000, 19004286)
    CraftDummyWeapon(287, 60311900, 40311900, 0)
    MonitorWeaponPossession(287, 31190000, 19004287)
    CraftDummyWeapon(288, 60312300, 40312300, 0)
    MonitorWeaponPossession(288, 31230000, 19004288)
    CraftDummyWeapon(289, 60312400, 40312400, 0)
    MonitorWeaponPossession(289, 31240000, 19004289)
    CraftDummyWeapon(290, 60312500, 40312500, 0)
    MonitorWeaponPossession(290, 31250000, 19004290)
    CraftDummyWeapon(291, 60312600, 40312600, 0)
    MonitorWeaponPossession(291, 31260000, 19004291)
    CraftDummyWeapon(292, 60312700, 40312700, 0)
    MonitorWeaponPossession(292, 31270000, 19004292)
    CraftDummyWeapon(293, 60312800, 40312800, 0)
    MonitorWeaponPossession(293, 31280000, 19004293)
    CraftDummyWeapon(294, 60312900, 40312900, 0)
    MonitorWeaponPossession(294, 31290000, 19004294)
    CraftDummyWeapon(295, 60313000, 40313000, 0)
    MonitorWeaponPossession(295, 31300000, 19004295)
    CraftDummyWeapon(296, 60313100, 40313100, 0)
    MonitorWeaponPossession(296, 31310000, 19004296)
    CraftDummyWeapon(297, 60313200, 40313200, 0)
    MonitorWeaponPossession(297, 31320000, 19004297)
    CraftDummyWeapon(298, 60313300, 40313300, 0)
    MonitorWeaponPossession(298, 31330000, 19004298)
    CraftDummyWeapon(299, 60313400, 40313400, 0)
    MonitorWeaponPossession(299, 31340000, 19004299)
    CraftDummyWeapon(300, 60320000, 40320000, 0)
    MonitorWeaponPossession(300, 32000000, 19004300)
    CraftDummyWeapon(301, 60320200, 40320200, 0)
    MonitorWeaponPossession(301, 32020000, 19004301)
    CraftDummyWeapon(302, 60320300, 40320300, 0)
    MonitorWeaponPossession(302, 32030000, 19004302)
    CraftDummyWeapon(303, 60320400, 40320400, 0)
    MonitorWeaponPossession(303, 32040000, 19004303)
    CraftDummyWeapon(304, 60320500, 40320500, 0)
    MonitorWeaponPossession(304, 32050000, 19004304)
    CraftDummyWeapon(305, 60320800, 40320800, 0)
    MonitorWeaponPossession(305, 32080000, 19004305)
    CraftDummyWeapon(306, 60320900, 40320900, 0)
    MonitorWeaponPossession(306, 32090000, 19004306)
    CraftDummyWeapon(307, 60321200, 40321200, 0)
    MonitorWeaponPossession(307, 32120000, 19004307)
    CraftDummyWeapon(308, 60321300, 40321300, 0)
    MonitorWeaponPossession(308, 32130000, 19004308)
    CraftDummyWeapon(309, 60321400, 40321400, 0)
    MonitorWeaponPossession(309, 32140000, 19004309)
    CraftDummyWeapon(310, 60321500, 40321500, 0)
    MonitorWeaponPossession(310, 32150000, 19004310)
    CraftDummyWeapon(311, 60321600, 40321600, 0)
    MonitorWeaponPossession(311, 32160000, 19004311)
    CraftDummyWeapon(312, 60321700, 40321700, 0)
    MonitorWeaponPossession(312, 32170000, 19004312)
    CraftDummyWeapon(313, 60321900, 40321900, 0)
    MonitorWeaponPossession(313, 32190000, 19004313)
    CraftDummyWeapon(314, 60322000, 40322000, 0)
    MonitorWeaponPossession(314, 32200000, 19004314)
    CraftDummyWeapon(315, 60322100, 40322100, 0)
    MonitorWeaponPossession(315, 32210000, 19004315)
    CraftDummyWeapon(316, 60322200, 40322200, 0)
    MonitorWeaponPossession(316, 32220000, 19004316)
    CraftDummyWeapon(317, 60322300, 40322300, 0)
    MonitorWeaponPossession(317, 32230000, 19004317)
    CraftDummyWeapon(318, 60322400, 40322400, 0)
    MonitorWeaponPossession(318, 32240000, 19004318)
    CraftDummyWeapon(319, 60322500, 40322500, 0)
    MonitorWeaponPossession(319, 32250000, 19004319)
    CraftDummyWeapon(320, 60322600, 40322600, 0)
    MonitorWeaponPossession(320, 32260000, 19004320)
    CraftDummyWeapon(321, 60322700, 40322700, 0)
    MonitorWeaponPossession(321, 32270000, 19004321)
    CraftDummyWeapon(322, 60322800, 40322800, 0)
    MonitorWeaponPossession(322, 32280000, 19004322)
    CraftDummyWeapon(323, 60322900, 40322900, 0)
    MonitorWeaponPossession(323, 32290000, 19004323)
    CraftDummyWeapon(324, 60323000, 40323000, 0)
    MonitorWeaponPossession(324, 32300000, 19004324)
    CraftDummyWeapon(325, 60330000, 40330000, 0)
    MonitorWeaponPossession(325, 33000000, 19004325)
    CraftDummyWeapon(326, 60330400, 40330400, 0)
    MonitorWeaponPossession(326, 33040000, 19004326)
    CraftDummyWeapon(327, 60330500, 40330500, 0)
    MonitorWeaponPossession(327, 33050000, 19004327)
    CraftDummyWeapon(328, 60330600, 40330600, 0)
    MonitorWeaponPossession(328, 33060000, 19004328)
    CraftDummyWeapon(329, 60330900, 40330900, 0)
    MonitorWeaponPossession(329, 33090000, 19004329)
    CraftDummyWeapon(330, 60331200, 40331200, 0)
    MonitorWeaponPossession(330, 33120000, 19004330)
    CraftDummyWeapon(331, 60331300, 40331300, 0)
    MonitorWeaponPossession(331, 33130000, 19004331)
    CraftDummyWeapon(332, 60331700, 40331700, 0)
    MonitorWeaponPossession(332, 33170000, 19004332)
    CraftDummyWeapon(333, 60331800, 40331800, 0)
    MonitorWeaponPossession(333, 33180000, 19004333)
    CraftDummyWeapon(334, 60331900, 40331900, 0)
    MonitorWeaponPossession(334, 33190000, 19004334)
    CraftDummyWeapon(335, 60332000, 40332000, 0)
    MonitorWeaponPossession(335, 33200000, 19004335)
    CraftDummyWeapon(336, 60332100, 40332100, 0)
    MonitorWeaponPossession(336, 33210000, 19004336)
    CraftDummyWeapon(337, 60332300, 40332300, 0)
    MonitorWeaponPossession(337, 33230000, 19004337)
    CraftDummyWeapon(338, 60332400, 40332400, 0)
    MonitorWeaponPossession(338, 33240000, 19004338)
    CraftDummyWeapon(339, 60332500, 40332500, 0)
    MonitorWeaponPossession(339, 33250000, 19004339)
    CraftDummyWeapon(340, 60332600, 40332600, 0)
    MonitorWeaponPossession(340, 33260000, 19004340)
    CraftDummyWeapon(341, 60332700, 40332700, 0)
    MonitorWeaponPossession(341, 33270000, 19004341)
    CraftDummyWeapon(342, 60332800, 40332800, 0)
    MonitorWeaponPossession(342, 33280000, 19004342)
    CraftDummyWeapon(343, 60340000, 40340000, 0)
    MonitorWeaponPossession(343, 34000000, 19004343)
    CraftDummyWeapon(344, 60340100, 40340100, 0)
    MonitorWeaponPossession(344, 34010000, 19004344)
    CraftDummyWeapon(345, 60340200, 40340200, 0)
    MonitorWeaponPossession(345, 34020000, 19004345)
    CraftDummyWeapon(346, 60340300, 40340300, 0)
    MonitorWeaponPossession(346, 34030000, 19004346)
    CraftDummyWeapon(347, 60340400, 40340400, 0)
    MonitorWeaponPossession(347, 34040000, 19004347)
    CraftDummyWeapon(348, 60340600, 40340600, 0)
    MonitorWeaponPossession(348, 34060000, 19004348)
    CraftDummyWeapon(349, 60340700, 40340700, 0)
    MonitorWeaponPossession(349, 34070000, 19004349)
    CraftDummyWeapon(350, 60340800, 40340800, 0)
    MonitorWeaponPossession(350, 34080000, 19004350)
    CraftDummyWeapon(351, 60340900, 40340900, 0)
    MonitorWeaponPossession(351, 34090000, 19004351)
    CraftDummyWeapon(352, 60400000, 40400000, 0)
    MonitorWeaponPossession(352, 40000000, 19004352)
    CraftDummyWeapon(353, 60400100, 40400100, 40000000)
    MonitorWeaponPossession(353, 40010005, 19004353)
    CraftDummyWeapon(354, 60400200, 40400200, 40030005)
    MonitorWeaponPossession(354, 40020008, 19004354)
    CraftDummyWeapon(355, 60400300, 40400300, 40000000)
    MonitorWeaponPossession(355, 40030005, 19004355)
    CraftDummyWeapon(356, 60400500, 40400500, 40030005)
    MonitorWeaponPossession(356, 40050010, 19004356)
    CraftDummyWeapon(357, 60410000, 40410000, 40020008)
    MonitorWeaponPossession(357, 41000010, 19004357)
    CraftDummyWeapon(358, 60410100, 40410100, 41000010)
    MonitorWeaponPossession(358, 41010015, 19004358)
    CraftDummyWeapon(359, 60410200, 40410200, 41000010)
    MonitorWeaponPossession(359, 41020015, 19004359)
    CraftDummyWeapon(360, 60410300, 40410300, 41000010)
    MonitorWeaponPossession(360, 41030010, 19004360)
    CraftDummyWeapon(361, 60410400, 40410400, 41000010)
    MonitorWeaponPossession(361, 41040010, 19004361)
    CraftDummyWeapon(362, 60410600, 40410600, 40010005)
    MonitorWeaponPossession(362, 41060008, 19004362)
    CraftDummyWeapon(363, 60410700, 40410700, 41010015)
    MonitorWeaponPossession(363, 41070010, 19004363)
    CraftDummyWeapon(364, 60420000, 40420000, 42010008)
    MonitorWeaponPossession(364, 42000010, 19004364)
    CraftDummyWeapon(365, 60420100, 40420100, 42040014)
    MonitorWeaponPossession(365, 42010008, 19004365)
    CraftDummyWeapon(366, 60420300, 40420300, 42040014)
    MonitorWeaponPossession(366, 42030010, 19004366)
    CraftDummyWeapon(367, 60420400, 40420400, 41000010)
    MonitorWeaponPossession(367, 42040014, 19004367)
    CraftDummyWeapon(368, 60430000, 40430000, 41060008)
    MonitorWeaponPossession(368, 43000010, 19004368)
    CraftDummyWeapon(369, 60430200, 40430200, 43000010)
    MonitorWeaponPossession(369, 43020013, 19004369)
    CraftDummyWeapon(370, 60430300, 40430300, 43020013)
    MonitorWeaponPossession(370, 43030016, 19004370)
    CraftDummyWeapon(371, 60430500, 40430500, 43030016)
    MonitorWeaponPossession(371, 43050010, 19004371)
    CraftDummyWeapon(372, 60430600, 40430600, 43020013)
    MonitorWeaponPossession(372, 43060010, 19004372)
    CraftDummyWeapon(373, 60430800, 40430800, 43030016)
    MonitorWeaponPossession(373, 43080018, 19004373)
    CraftDummyWeapon(374, 60431100, 40431100, 43030016)
    MonitorWeaponPossession(374, 43110010, 19004374)
    CraftDummyWeapon(375, 60440000, 40440000, 43080018)
    MonitorWeaponPossession(375, 44000020, 19004375)
    CraftDummyWeapon(376, 60440100, 40440100, 43080018)
    MonitorWeaponPossession(376, 44010010, 19004376)
    # endregion


@NeverRestart(SurvivalFlags.GrowingHunger)
def GrowingHunger():
    """Hunger ticks up every 60 seconds."""

    # Hunger cannot grow while Draught of the Undining is active (or hunger is at max).
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.DraughtOfSatiation)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Hunger15)
    IfConditionTrue(0, 1)

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


@NeverRestart(SurvivalFlags.GrowingThirst)
def GrowingThirst():
    """Thirst ticks up every 100 seconds."""

    # Hunger cannot grow while Draught of the Undining is active (or hunger is at max).
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.DraughtOfSilverTears)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Thirst9)
    IfConditionTrue(0, 1)

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
    DisplayDialog(SurvivalText.Dehydration)  # Dehydration warning (for health depletion)
    Restart()

    # Player goes from ZERO thirst to level 1.
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst1)
    Restart()


@NeverRestart(SurvivalFlags.ReduceThirstOnDeath)
def ReduceThirstOnDeath():
    """When the player dies while at maximum (health-draining) thirst, they go back to thirst level 8."""
    IfPlayerHasSpecialEffect(1, SurvivalEffects.Thirst9)
    IfHealthLessThanOrEqual(1, PLAYER, 0)
    IfConditionTrue(0, 1)

    # Reduce thirst.
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst9)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst8)
    # No point restarting.


@NeverRestart(SurvivalFlags.RelieveHunger_1)
def RelieveHunger_1():
    """Monitors for numerous different "food eaten" special effects and reduces hunger level by 1."""
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.BloodBroth)
    IfConditionFalse(0, -1)
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


@NeverRestart(SurvivalFlags.RelieveHunger_2)
def RelieveHunger_2():
    """Monitors for numerous different "food eaten" special effects and reduces hunger level by 2."""
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.BoneBroth)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.BerryMedley1)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.BerryMedley3)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.MushroomStew)
    IfConditionFalse(0, -1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BoneBroth)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BerryMedley1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BerryMedley3)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.MushroomStew)
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


@NeverRestart(SurvivalFlags.RelieveHunger_3)
def RelieveHunger_3():
    """Monitors for numerous different "food eaten" special effects and reduces hunger level by 3."""
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.RawSteak)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.BerryMedley2)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.JarBrittle)
    IfConditionFalse(0, -1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.RawSteak)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BerryMedley2)
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


@NeverRestart(SurvivalFlags.RelieveHunger_4)
def RelieveHunger_4():
    """Monitors for numerous different "food eaten" special effects and reduces hunger level by 4."""
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.GreatBoneBroth)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.BerryMedley3)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.MeltedMushroomStew)
    IfConditionFalse(0, -1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.GreatBoneBroth)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BerryMedley3)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.MeltedMushroomStew)
    IfConditionFalse(0, -2)

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


@NeverRestart(SurvivalFlags.RelieveHunger_5)
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


@NeverRestart(SurvivalFlags.RelieveHunger_6)
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


@NeverRestart(SurvivalFlags.RelieveHunger_8)
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


@NeverRestart(SurvivalFlags.RelieveThirst_1)
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


@NeverRestart(SurvivalFlags.RelieveThirst_2)
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


@NeverRestart(SurvivalFlags.RelieveThirst_3)
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


@NeverRestart(SurvivalFlags.RelieveThirst_4)
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


@NeverRestart(SurvivalFlags.RelieveThirst_5)
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


@NeverRestart(SurvivalFlags.RelieveThirst_6)
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


@NeverRestart(SurvivalFlags.IncreaseThirst_1)
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


@NeverRestart(SurvivalFlags.IncreaseThirst_3)
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


@NeverRestart(SurvivalFlags.CheckMildHeatArea)
def CheckMildHeatArea():
    """Checks if mild heat should be applied to the player due to current time and place."""

    # --- CAELID / ALTUS / LEYNDELL in MIDDLE OF DAY ---
    IfTimeOfDay(1, (10, 0, 0), (17, 0, 0))
    IfFlagOn(-1, SurvivalFlags.PlayerInCaelid)
    IfFlagOn(-1, SurvivalFlags.PlayerInAltus)
    IfInsideMap(-1, LEYNDELL_ROYAL_CAPITAL)
    IfInsideMap(-1, LEYNDELL_ASHEN_CAPITAL)
    IfConditionTrue(1, -1)

    # --- MT. GELMIR at NIGHT ---
    IfTimeOfDay(2, (18, 0, 0), (8, 0, 0))
    IfFlagOn(2, SurvivalFlags.PlayerInMtGelmir)

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

    EnableFlag(SurvivalFlags.ShowMildHeatWarning)
    AddSpecialEffect(PLAYER, SurvivalEffects.Heat_Mild)
    Wait(3.0)
    DisableFlag(SurvivalFlags.ShowMildHeatWarning)
    return RESTART


@NeverRestart(SurvivalFlags.CheckModerateHeatArea)
def CheckModerateHeatArea():
    """Checks if moderate heat should be applied to the player due to current time and place."""

    # --- MT.GELMIR at DAY ---
    IfTimeOfDay(1, (8, 0, 0), (18, 0, 0))
    IfFlagOn(1, SurvivalFlags.PlayerInMtGelmir)

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

    EnableFlag(SurvivalFlags.ShowModerateHeatWarning)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.HeatProtection_Mild)
    AddSpecialEffect(PLAYER, SurvivalEffects.Heat_Mild)
    SkipLines(1)
    AddSpecialEffect(PLAYER, SurvivalEffects.Heat_Moderate)
    Wait(3.0)
    DisableFlag(SurvivalFlags.ShowModerateHeatWarning)
    return RESTART


@NeverRestart(SurvivalFlags.CheckSevereHeatArea)
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

    EnableFlag(SurvivalFlags.ShowSevereHeatWarning)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.HeatProtection_Moderate)
    AddSpecialEffect(PLAYER, SurvivalEffects.Heat_Mild)
    SkipLines(4)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.HeatProtection_Mild)
    AddSpecialEffect(PLAYER, SurvivalEffects.Heat_Moderate)
    SkipLines(1)
    AddSpecialEffect(PLAYER, SurvivalEffects.Heat_Severe)

    Wait(3.0)
    DisableFlag(SurvivalFlags.ShowSevereHeatWarning)
    return RESTART


@NeverRestart(SurvivalFlags.CheckMildColdArea)
def CheckMildColdArea():

    # --- NIGHT ---
    IfTimeOfDay(1, (18, 0, 0), (8, 0, 0))

    IfFlagOn(-1, SurvivalFlags.PlayerInLiurnia)
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

    EnableFlag(SurvivalFlags.ShowMildColdWarning)

    AddSpecialEffect(PLAYER, SurvivalEffects.Cold_Mild)
    Wait(3.0)
    DisableFlag(SurvivalFlags.ShowMildColdWarning)
    return RESTART


@NeverRestart(SurvivalFlags.CheckModerateColdArea)
def CheckModerateColdArea():
    # --- MOUNTAINTOPS in DAY ---
    IfTimeOfDay(1, (8, 0, 0), (18, 0, 0))
    IfFlagOn(1, SurvivalFlags.PlayerInMountaintops)

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

    EnableFlag(SurvivalFlags.ShowModerateColdWarning)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.ColdProtection_Mild)
    AddSpecialEffect(PLAYER, SurvivalEffects.Cold_Mild)
    SkipLines(1)
    AddSpecialEffect(PLAYER, SurvivalEffects.Cold_Moderate)
    Wait(3.0)
    DisableFlag(SurvivalFlags.ShowModerateColdWarning)
    return RESTART


@NeverRestart(SurvivalFlags.CheckSevereColdArea)
def CheckSevereColdArea():
    # --- MOUNTAINTOPS / FARUM AZULA at NIGHT ---
    IfTimeOfDay(1, (18, 0, 0), (8, 0, 0))
    IfFlagOn(-1, SurvivalFlags.PlayerInMountaintops)
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

    EnableFlag(SurvivalFlags.ShowSevereColdWarning)

    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.ColdProtection_Moderate)
    AddSpecialEffect(PLAYER, SurvivalEffects.Cold_Mild)
    SkipLines(4)
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.ColdProtection_Mild)
    AddSpecialEffect(PLAYER, SurvivalEffects.Cold_Moderate)
    SkipLines(1)
    AddSpecialEffect(PLAYER, SurvivalEffects.Cold_Severe)
    Wait(3.0)
    DisableFlag(SurvivalFlags.ShowSevereColdWarning)
    return RESTART


@NeverRestart(SurvivalFlags.MildHeatWarning)
def MildHeatWarning():
    IfFlagOn(0, SurvivalFlags.ShowMildHeatWarning)
    DisplayDialog(SurvivalText.MildHeatWarning)
    Wait(60.0)
    return RESTART


@NeverRestart(SurvivalFlags.ModerateHeatWarning)
def ModerateHeatWarning():
    IfFlagOn(0, SurvivalFlags.ShowModerateHeatWarning)
    DisplayDialog(SurvivalText.ModerateHeatWarning)
    Wait(60.0)
    return RESTART


@NeverRestart(SurvivalFlags.SevereHeatWarning)
def SevereHeatWarning():
    IfFlagOn(0, SurvivalFlags.ShowSevereHeatWarning)
    DisplayDialog(SurvivalText.SevereHeatWarning)
    Wait(60.0)
    return RESTART


@NeverRestart(SurvivalFlags.MildColdWarning)
def MildColdWarning():
    IfFlagOn(0, SurvivalFlags.ShowMildColdWarning)
    DisplayDialog(SurvivalText.MildColdWarning)
    Wait(60.0)
    return RESTART


@NeverRestart(SurvivalFlags.ModerateColdWarning)
def ModerateColdWarning():
    IfFlagOn(0, SurvivalFlags.ShowModerateColdWarning)
    DisplayDialog(SurvivalText.ModerateColdWarning)
    Wait(60.0)
    return RESTART


@NeverRestart(SurvivalFlags.SevereColdWarning)
def SevereColdWarning():
    IfFlagOn(0, SurvivalFlags.ShowSevereColdWarning)
    DisplayDialog(SurvivalText.SevereColdWarning)
    Wait(60.0)
    return RESTART


@NeverRestart(SurvivalFlags.GetDiseaseOverworld)
def GetDiseaseOverworld(
    _, disease_effect: int, location_flag: Flag, had_once_flag: Flag, had_twice_flag: Flag, text: int
):
    EndIfFlagOn(had_twice_flag)

    IfFlagOn(1, location_flag)
    IfAttackedWithDamageType(1, PLAYER, -1, DamageType.Unspecified)
    IfPlayerDoesNotHaveSpecialEffect(1, disease_effect)
    IfFlagOff(1, SurvivalFlags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(SurvivalFlags.DiseaseRollLock)
    DisableFlagRange((SurvivalFlags.DiseaseRollFirst, SurvivalFlags.DiseaseRollLast))
    EnableRandomFlagInRange((SurvivalFlags.DiseaseRollFirst, SurvivalFlags.DiseaseRollLast))

    IfFlagOn(-2, SurvivalFlags.DiseaseRollFirst)
    IfFlagOff(2, had_once_flag)
    IfFlagOn(2, SurvivalFlags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(SurvivalFlags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(SurvivalFlags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, disease_effect)
    DisplayDialog(text)

    SkipLinesIfFlagOn(2, had_once_flag)
    EnableFlag(had_once_flag)
    End()
    EnableFlag(had_twice_flag)


@NeverRestart(SurvivalFlags.GetDiseaseLegacyDungeon)
def GetDiseaseLegacyDungeon(
    _, disease_effect: int, a: uchar, b: uchar, c: uchar, d: uchar, had_once_flag: Flag, had_twice_flag: Flag, text: int
):
    """Same as overworld check, but checks if player is in map (a, b, c, d) instead."""
    EndIfFlagOn(had_twice_flag)

    # TODO: Not sure my system can support this map argument, but it should if not.
    IfInsideMap(1, (a, b, c, d))
    IfAttackedWithDamageType(1, PLAYER, -1, DamageType.Unspecified)
    IfPlayerDoesNotHaveSpecialEffect(1, disease_effect)
    IfFlagOff(1, SurvivalFlags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(SurvivalFlags.DiseaseRollLock)
    DisableFlagRange((SurvivalFlags.DiseaseRollFirst, SurvivalFlags.DiseaseRollLast))
    EnableRandomFlagInRange((SurvivalFlags.DiseaseRollFirst, SurvivalFlags.DiseaseRollLast))

    IfFlagOn(-2, SurvivalFlags.DiseaseRollFirst)
    IfFlagOff(2, had_once_flag)
    IfFlagOn(2, SurvivalFlags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(SurvivalFlags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(SurvivalFlags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, disease_effect)
    DisplayDialog(text)

    SkipLinesIfFlagOn(2, had_once_flag)
    EnableFlag(had_once_flag)
    End()
    EnableFlag(had_twice_flag)


# --- SPECIFIC DISEASE EVENTS ---


@NeverRestart(SurvivalFlags.GetDiseaseSiofra)
def GetDiseaseSiofra():
    EndIfFlagOn(SurvivalFlags.SiofraDiseaseTwice)

    IfInsideMap(-1, SIOFRA_RIVER)
    IfInsideMap(-1, SIOFRA_RIVER_START)
    IfConditionTrue(1, -1)
    IfAttackedWithDamageType(1, PLAYER, -1, DamageType.Unspecified)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.SiofraPlague)
    IfFlagOff(1, SurvivalFlags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(SurvivalFlags.DiseaseRollLock)
    DisableFlagRange((SurvivalFlags.DiseaseRollFirst, SurvivalFlags.DiseaseRollLast))
    EnableRandomFlagInRange((SurvivalFlags.DiseaseRollFirst, SurvivalFlags.DiseaseRollLast))

    IfFlagOn(-2, SurvivalFlags.DiseaseRollFirst)
    IfFlagOff(2, SurvivalFlags.SiofraDiseaseOnce)
    IfFlagOn(2, SurvivalFlags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(SurvivalFlags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(SurvivalFlags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, SurvivalEffects.SiofraPlague)
    DisplayDialog(SurvivalText.ContractedSiofraDisease)

    SkipLinesIfFlagOn(2, SurvivalFlags.SiofraDiseaseOnce)
    EnableFlag(SurvivalFlags.SiofraDiseaseOnce)
    End()
    EnableFlag(SurvivalFlags.SiofraDiseaseTwice)


@NeverRestart(SurvivalFlags.GetDiseaseAinsel)
def GetDiseaseAinsel():
    EndIfFlagOn(SurvivalFlags.AinselDiseaseTwice)

    IfInsideMap(1, AINSEL_RIVER)
    IfAttackedWithDamageType(1, PLAYER, -1, DamageType.Unspecified)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.AinselToxin)
    IfFlagOff(1, SurvivalFlags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(SurvivalFlags.DiseaseRollLock)
    DisableFlagRange((SurvivalFlags.DiseaseRollFirst, SurvivalFlags.DiseaseRollLast))
    EnableRandomFlagInRange((SurvivalFlags.DiseaseRollFirst, SurvivalFlags.DiseaseRollLast))

    IfFlagOn(-2, SurvivalFlags.DiseaseRollFirst)
    IfFlagOff(2, SurvivalFlags.AinselDiseaseOnce)
    IfFlagOn(2, SurvivalFlags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(SurvivalFlags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(SurvivalFlags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, SurvivalEffects.AinselToxin)
    DisplayDialog(SurvivalText.ContractedAinselDisease)

    SkipLinesIfFlagOn(2, SurvivalFlags.AinselDiseaseOnce)
    EnableFlag(SurvivalFlags.AinselDiseaseOnce)
    End()
    EnableFlag(SurvivalFlags.AinselDiseaseTwice)


@NeverRestart(SurvivalFlags.GetDiseaseDeeprootAstel)
def GetDiseaseDeeprootAstel():
    EndIfFlagOn(SurvivalFlags.DeeprootDiseaseTwice)

    IfInsideMap(-1, DEEPROOT_DEPTHS)
    IfInsideMap(-1, ASTEL_ARENA)
    IfConditionTrue(1, -1)
    IfAttackedWithDamageType(1, PLAYER, -1, DamageType.Unspecified)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.DeeprootParasite)
    IfFlagOff(1, SurvivalFlags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(SurvivalFlags.DiseaseRollLock)
    DisableFlagRange((SurvivalFlags.DiseaseRollFirst, SurvivalFlags.DiseaseRollLast))
    EnableRandomFlagInRange((SurvivalFlags.DiseaseRollFirst, SurvivalFlags.DiseaseRollLast))

    IfFlagOn(-2, SurvivalFlags.DiseaseRollFirst)
    IfFlagOff(2, SurvivalFlags.DeeprootDiseaseOnce)
    IfFlagOn(2, SurvivalFlags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(SurvivalFlags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(SurvivalFlags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, SurvivalEffects.DeeprootParasite)
    DisplayDialog(SurvivalText.ContractedDeeprootDisease)

    SkipLinesIfFlagOn(2, SurvivalFlags.DeeprootDiseaseOnce)
    EnableFlag(SurvivalFlags.DeeprootDiseaseOnce)
    End()
    EnableFlag(SurvivalFlags.DeeprootDiseaseTwice)


@NeverRestart(SurvivalFlags.GetDiseaseRadahn)
def GetDiseaseRadahn():
    """Only afflicted by Radahn himself."""
    EndIfFlagOn(SurvivalFlags.RadahnDiseaseTwice)

    IfAttackedWithDamageType(1, PLAYER, VanillaCharacters.Radahn, DamageType.Unspecified)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.RadahnFever)
    IfFlagOff(1, SurvivalFlags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(SurvivalFlags.DiseaseRollLock)
    DisableFlagRange((SurvivalFlags.DiseaseRollFirst, SurvivalFlags.DiseaseRollLast))
    EnableRandomFlagInRange((SurvivalFlags.DiseaseRollFirst, SurvivalFlags.DiseaseRollLast))

    IfFlagOn(-2, SurvivalFlags.DiseaseRollFirst)
    IfFlagOff(2, SurvivalFlags.RadahnDiseaseOnce)
    IfFlagOn(2, SurvivalFlags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(SurvivalFlags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(SurvivalFlags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, SurvivalEffects.RadahnFever)
    DisplayDialog(SurvivalText.ContractedRadahnDisease)

    SkipLinesIfFlagOn(2, SurvivalFlags.RadahnDiseaseOnce)
    EnableFlag(SurvivalFlags.RadahnDiseaseOnce)
    End()
    EnableFlag(SurvivalFlags.RadahnDiseaseTwice)


# --- GENERIC DUNGEON DISEASES ---


@NeverRestart(SurvivalFlags.GetDiseaseCatacombs)
def GetDiseaseCatacombs():
    EndIfFlagOn(SurvivalFlags.CatacombsDiseaseTwice)

    IfInsideMap(1, (30, 255, 255, 255))  # ANY Catacombs
    IfAttackedWithDamageType(1, PLAYER, -1, DamageType.Unspecified)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.CatacombsToxin)
    IfFlagOff(1, SurvivalFlags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(SurvivalFlags.DiseaseRollLock)
    DisableFlagRange((SurvivalFlags.DiseaseRollFirst, SurvivalFlags.DiseaseRollLast))
    EnableRandomFlagInRange((SurvivalFlags.DiseaseRollFirst, SurvivalFlags.DiseaseRollLast))

    IfFlagOn(-2, SurvivalFlags.DiseaseRollFirst)
    IfFlagOff(2, SurvivalFlags.CatacombsDiseaseOnce)
    IfFlagOn(2, SurvivalFlags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(SurvivalFlags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(SurvivalFlags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, SurvivalEffects.CatacombsToxin)
    DisplayDialog(SurvivalText.ContractedCatacombsDisease)

    SkipLinesIfFlagOn(2, SurvivalFlags.CatacombsDiseaseOnce)
    EnableFlag(SurvivalFlags.CatacombsDiseaseOnce)
    End()
    EnableFlag(SurvivalFlags.CatacombsDiseaseTwice)


@NeverRestart(SurvivalFlags.GetDiseaseCaves)
def GetDiseaseCaves():
    EndIfFlagOn(SurvivalFlags.CaveDiseaseTwice)

    IfInsideMap(1, (31, 255, 255, 255))  # ANY Cave
    IfAttackedWithDamageType(1, PLAYER, -1, DamageType.Unspecified)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.CaveParasite)
    IfFlagOff(1, SurvivalFlags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(SurvivalFlags.DiseaseRollLock)
    DisableFlagRange((SurvivalFlags.DiseaseRollFirst, SurvivalFlags.DiseaseRollLast))
    EnableRandomFlagInRange((SurvivalFlags.DiseaseRollFirst, SurvivalFlags.DiseaseRollLast))

    IfFlagOn(-2, SurvivalFlags.DiseaseRollFirst)
    IfFlagOff(2, SurvivalFlags.CaveDiseaseOnce)
    IfFlagOn(2, SurvivalFlags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(SurvivalFlags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(SurvivalFlags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, SurvivalEffects.CaveParasite)
    DisplayDialog(SurvivalText.ContractedCaveDisease)

    SkipLinesIfFlagOn(2, SurvivalFlags.CaveDiseaseOnce)
    EnableFlag(SurvivalFlags.CaveDiseaseOnce)
    End()
    EnableFlag(SurvivalFlags.CaveDiseaseTwice)


@NeverRestart(SurvivalFlags.GetDiseaseTunnels)
def GetDiseaseTunnels():
    EndIfFlagOn(SurvivalFlags.TunnelDiseaseTwice)

    IfInsideMap(1, (32, 255, 255, 255))  # ANY Tunnel
    IfAttackedWithDamageType(1, PLAYER, -1, DamageType.Unspecified)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.TunnelFever)
    IfFlagOff(1, SurvivalFlags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(SurvivalFlags.DiseaseRollLock)
    DisableFlagRange((SurvivalFlags.DiseaseRollFirst, SurvivalFlags.DiseaseRollLast))
    EnableRandomFlagInRange((SurvivalFlags.DiseaseRollFirst, SurvivalFlags.DiseaseRollLast))

    IfFlagOn(-2, SurvivalFlags.DiseaseRollFirst)
    IfFlagOff(2, SurvivalFlags.TunnelDiseaseOnce)
    IfFlagOn(2, SurvivalFlags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(SurvivalFlags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(SurvivalFlags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, SurvivalEffects.TunnelFever)
    DisplayDialog(SurvivalText.ContractedTunnelDisease)

    SkipLinesIfFlagOn(2, SurvivalFlags.TunnelDiseaseOnce)
    EnableFlag(SurvivalFlags.TunnelDiseaseOnce)
    End()
    EnableFlag(SurvivalFlags.TunnelDiseaseTwice)


# --- PURE SCARLET ROT ---


@NeverRestart(SurvivalFlags.GetPureScarletRot)
def GetPureScarletRot():
    """Chance of proccing each time you get normal scarlet rot.

    100% chance if you are in the Lake of Rot (checking if you're in Ainsel River is sufficient).
    """
    # TODO: Not bothering with this for now.
    End()


# --- DISEASE CURES ---


@NeverRestart(SurvivalFlags.CurePlague)
def CurePlague():
    IfPlayerHasSpecialEffect(1, SurvivalEffects.PlagueCure)

    IfPlayerHasSpecialEffect(-1, SurvivalEffects.LimgravePlague)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.SiofraPlague)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.LeyndellPlague)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.HaligtreePlague)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.StormveilPlague)
    IfConditionTrue(1, -1)

    IfConditionTrue(0, 1)

    CancelSpecialEffect(PLAYER, SurvivalEffects.LimgravePlague)
    CancelSpecialEffect(PLAYER, SurvivalEffects.SiofraPlague)
    CancelSpecialEffect(PLAYER, SurvivalEffects.LeyndellPlague)
    CancelSpecialEffect(PLAYER, SurvivalEffects.HaligtreePlague)
    CancelSpecialEffect(PLAYER, SurvivalEffects.StormveilPlague)

    DisplayDialog(SurvivalText.CuredPlague)

    IfPlayerDoesNotHaveSpecialEffect(0, SurvivalEffects.PlagueCure)

    return RESTART


@NeverRestart(SurvivalFlags.CureToxin)
def CureToxin():
    IfPlayerHasSpecialEffect(1, SurvivalEffects.ToxinCure)

    IfPlayerHasSpecialEffect(-1, SurvivalEffects.LiurniaToxin)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.CatacombsToxin)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.AinselToxin)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.RayaLucariaFever)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.VolcanoManorToxin)
    IfConditionTrue(1, -1)

    IfConditionTrue(0, 1)

    CancelSpecialEffect(PLAYER, SurvivalEffects.LiurniaToxin)
    CancelSpecialEffect(PLAYER, SurvivalEffects.CatacombsToxin)
    CancelSpecialEffect(PLAYER, SurvivalEffects.AinselToxin)
    CancelSpecialEffect(PLAYER, SurvivalEffects.RayaLucariaFever)
    CancelSpecialEffect(PLAYER, SurvivalEffects.VolcanoManorToxin)

    DisplayDialog(SurvivalText.CuredToxin)

    IfPlayerDoesNotHaveSpecialEffect(0, SurvivalEffects.ToxinCure)

    return RESTART


@NeverRestart(SurvivalFlags.CureFever)
def CureFever():
    IfPlayerHasSpecialEffect(1, SurvivalEffects.FeverCure)

    IfPlayerHasSpecialEffect(-1, SurvivalEffects.AltusFever)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.TunnelFever)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.RadahnFever)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.FarumAzulaFever)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.MohgwynFever)
    IfConditionTrue(1, -1)

    IfConditionTrue(0, 1)

    CancelSpecialEffect(PLAYER, SurvivalEffects.AltusFever)
    CancelSpecialEffect(PLAYER, SurvivalEffects.TunnelFever)
    CancelSpecialEffect(PLAYER, SurvivalEffects.RadahnFever)
    CancelSpecialEffect(PLAYER, SurvivalEffects.FarumAzulaFever)
    CancelSpecialEffect(PLAYER, SurvivalEffects.MohgwynFever)

    DisplayDialog(SurvivalText.CuredFever)

    IfPlayerDoesNotHaveSpecialEffect(0, SurvivalEffects.FeverCure)

    return RESTART


@NeverRestart(SurvivalFlags.CureParasite)
def CureParasite():
    IfPlayerHasSpecialEffect(1, SurvivalEffects.ParasiteCure)

    IfPlayerHasSpecialEffect(-1, SurvivalEffects.CaveParasite)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.CaelidParasite)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.SewersParasite)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.MountaintopsParasite)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.DeeprootParasite)
    IfConditionTrue(1, -1)

    IfConditionTrue(0, 1)

    CancelSpecialEffect(PLAYER, SurvivalEffects.CaveParasite)
    CancelSpecialEffect(PLAYER, SurvivalEffects.CaelidParasite)
    CancelSpecialEffect(PLAYER, SurvivalEffects.SewersParasite)
    CancelSpecialEffect(PLAYER, SurvivalEffects.MountaintopsParasite)
    CancelSpecialEffect(PLAYER, SurvivalEffects.DeeprootParasite)

    DisplayDialog(SurvivalText.CuredParasite)

    IfPlayerDoesNotHaveSpecialEffect(0, SurvivalEffects.ParasiteCure)

    return RESTART


@NeverRestart(SurvivalFlags.CurePureScarletRot)
def CurePureScarletRot():
    IfPlayerHasSpecialEffect(1, SurvivalEffects.PureScarletRotCure)
    IfPlayerHasSpecialEffect(1, SurvivalEffects.PureScarletRot)

    IfConditionTrue(0, 1)

    CancelSpecialEffect(PLAYER, SurvivalEffects.PureScarletRot)

    # TODO: Award Pure Scarlet Rot self-affliction item if not already given.

    IfPlayerDoesNotHaveSpecialEffect(0, SurvivalEffects.PureScarletRotCure)

    return RESTART


# --- MAP CHECKS ---


@NeverRestart(SurvivalFlags.MonitorInLimgrave)
def MonitorInLimgrave():
    DisableFlag(SurvivalFlags.PlayerInLimgrave)

    # LIMGRAVE (including Weeping Peninsula)
    IfInsideMapTile(-1, (60, 10, 9, 2))
    IfInsideMapTile(-1, (60, 10, 8, 2))
    IfInsideMapTile(-1, (60, 10, 7, 2))
    IfInsideMapTile(-1, (60, 11, 7, 2))
    IfInsideMapTile(-1, (60, 11, 8, 2))
    IfInsideMapTile(-1, (60, 22, 19, 1))  # Caelid border
    IfInsideMapTile(-1, (60, 22, 18, 1))
    IfInsideMapTile(-1, (60, 46, 36, 0))
    IfInsideMapTile(-1, (60, 46, 37, 0))
    IfInsideMapTile(-1, (60, 46, 38, 0))

    IfConditionTrue(0, -1)

    EnableFlag(SurvivalFlags.PlayerInLimgrave)

    IfInsideMapTile(-2, (60, 10, 9, 2))
    IfInsideMapTile(-2, (60, 10, 8, 2))
    IfInsideMapTile(-2, (60, 10, 7, 2))
    IfInsideMapTile(-2, (60, 11, 7, 2))
    IfInsideMapTile(-2, (60, 11, 8, 2))
    IfInsideMapTile(-2, (60, 22, 19, 1))  # Caelid border
    IfInsideMapTile(-2, (60, 22, 18, 1))
    IfInsideMapTile(-2, (60, 46, 36, 0))
    IfInsideMapTile(-2, (60, 46, 37, 0))
    IfInsideMapTile(-2, (60, 46, 38, 0))

    IfConditionFalse(0, -2)

    return RESTART


@NeverRestart(SurvivalFlags.MonitorInLiurnia)
def MonitorInLiurnia():
    DisableFlag(SurvivalFlags.PlayerInLiurnia)

    IfInsideMapTile(-1, SOUTHWEST_LIURNIA)
    IfInsideMapTile(-1, WEST_LIURNIA)
    IfInsideMapTile(-1, NORTHWEST_LIURNIA)
    IfInsideMapTile(-1, EAST_LIURNIA)
    IfInsideMapTile(-1, (60, 18, 20, 1))  # entrance from Stormveil
    IfInsideMapTile(-1, (60, 18, 21, 1))
    IfInsideMapTile(-1, (60, 19, 21, 1))
    IfInsideMapTile(-1, (60, 38, 40, 0))
    IfInsideMapTile(-1, (60, 38, 41, 0))
    IfInsideMapTile(-1, (60, 39, 41, 0))
    IfInsideMapTile(-1, (60, 18, 24, 1))  # approach to Dectus
    IfInsideMapTile(-1, (60, 19, 24, 1))
    IfInsideMapTile(-1, (60, 36, 50, 0))

    IfConditionTrue(0, -1)

    EnableFlag(SurvivalFlags.PlayerInLiurnia)

    IfInsideMapTile(-2, SOUTHWEST_LIURNIA)
    IfInsideMapTile(-2, WEST_LIURNIA)
    IfInsideMapTile(-2, NORTHWEST_LIURNIA)
    IfInsideMapTile(-2, EAST_LIURNIA)
    IfInsideMapTile(-2, (60, 18, 20, 1))  # entrance from Stormveil
    IfInsideMapTile(-2, (60, 18, 21, 1))
    IfInsideMapTile(-2, (60, 19, 21, 1))
    IfInsideMapTile(-2, (60, 38, 40, 0))
    IfInsideMapTile(-2, (60, 38, 41, 0))
    IfInsideMapTile(-2, (60, 39, 41, 0))
    IfInsideMapTile(-2, (60, 18, 24, 1))  # approach to Dectus
    IfInsideMapTile(-2, (60, 19, 24, 1))
    IfInsideMapTile(-2, (60, 36, 50, 0))

    IfConditionFalse(0, -2)

    return RESTART


@NeverRestart(SurvivalFlags.MonitorInCaelid)
def MonitorInCaelid():
    DisableFlag(SurvivalFlags.PlayerInCaelid)

    IfInsideMapTile(-1, NORTH_CAELID)
    IfInsideMapTile(-1, SOUTH_CAELID)
    IfInsideMapTile(-1, NORTHEAST_CAELID)
    IfInsideMapTile(-1, SOUTHEAST_CAELID)
    IfInsideMapTile(-1, FAR_SOUTH_CAELID)  # just water and a sliver of Redmane Castle
    IfInsideMapTile(-1, (60, 23, 20, 1))
    IfInsideMapTile(-1, (60, 23, 21, 1))
    IfInsideMapTile(-1, (60, 47, 37, 0))
    IfInsideMapTile(-1, (60, 47, 38, 0))
    IfInsideMapTile(-1, (60, 47, 39, 0))

    IfConditionTrue(0, -1)

    EnableFlag(SurvivalFlags.PlayerInCaelid)

    IfInsideMapTile(-2, NORTH_CAELID)
    IfInsideMapTile(-2, SOUTH_CAELID)
    IfInsideMapTile(-2, NORTHEAST_CAELID)
    IfInsideMapTile(-2, SOUTHEAST_CAELID)
    IfInsideMapTile(-2, FAR_SOUTH_CAELID)  # just water and a sliver of Redmane Castle
    IfInsideMapTile(-2, (60, 23, 20, 1))
    IfInsideMapTile(-2, (60, 23, 21, 1))
    IfInsideMapTile(-2, (60, 47, 37, 0))
    IfInsideMapTile(-2, (60, 47, 38, 0))
    IfInsideMapTile(-2, (60, 47, 39, 0))

    IfConditionFalse(0, -2)

    return RESTART


@NeverRestart(SurvivalFlags.MonitorInAltus)
def MonitorInAltus():
    """Does NOT include Mt. Gelmir."""
    DisableFlag(SurvivalFlags.PlayerInAltus)

    IfInsideMapTile(-1, (60, 10, 12, 2))
    IfInsideMapTile(-1, (60, 10, 13, 2))
    IfInsideMapTile(-1, (60, 22, 26, 1))
    IfInsideMapTile(-1, (60, 36, 51, 0))
    IfInsideMapTile(-1, (60, 37, 51, 0))
    IfInsideMapTile(-1, (60, 38, 51, 0))
    IfInsideMapTile(-1, (60, 39, 50, 0))
    IfInsideMapTile(-1, (60, 39, 51, 0))
    IfInsideMapTile(-1, (60, 39, 52, 0))
    IfInsideMapTile(-1, (60, 39, 53, 0))
    IfInsideMapTile(-1, (60, 39, 54, 0))  # Shaded Castle

    IfConditionTrue(0, -1)

    IfInsideMapTile(-2, (60, 10, 12, 2))
    IfInsideMapTile(-2, (60, 10, 13, 2))
    IfInsideMapTile(-2, (60, 22, 26, 1))
    IfInsideMapTile(-2, (60, 36, 51, 0))
    IfInsideMapTile(-2, (60, 37, 51, 0))
    IfInsideMapTile(-2, (60, 38, 51, 0))
    IfInsideMapTile(-2, (60, 39, 50, 0))
    IfInsideMapTile(-2, (60, 39, 51, 0))
    IfInsideMapTile(-2, (60, 39, 52, 0))
    IfInsideMapTile(-2, (60, 39, 53, 0))
    IfInsideMapTile(-2, (60, 39, 54, 0))  # Shaded Castle

    IfConditionFalse(0, -2)

    return RESTART


@NeverRestart(SurvivalFlags.MonitorInMtGelmir)
def MonitorInMtGelmir():
    """Does NOT include rest of Altus."""
    DisableFlag(SurvivalFlags.PlayerInMtGelmir)

    IfInsideMapTile(-1, (60, 17, 26, 1))
    IfInsideMapTile(-1, (60, 17, 27, 1))
    IfInsideMapTile(-1, (60, 18, 26, 1))
    IfInsideMapTile(-1, (60, 18, 27, 1))
    IfInsideMapTile(-1, (60, 38, 52, 0))
    IfInsideMapTile(-1, (60, 38, 52, 0))
    IfInsideMapTile(-1, (60, 38, 53, 0))
    IfInsideMapTile(-1, (60, 38, 54, 0))

    IfConditionTrue(0, -1)

    IfInsideMapTile(-2, (60, 17, 26, 1))
    IfInsideMapTile(-2, (60, 17, 27, 1))
    IfInsideMapTile(-2, (60, 18, 26, 1))
    IfInsideMapTile(-2, (60, 18, 27, 1))
    IfInsideMapTile(-2, (60, 38, 52, 0))
    IfInsideMapTile(-2, (60, 38, 52, 0))
    IfInsideMapTile(-2, (60, 38, 53, 0))
    IfInsideMapTile(-2, (60, 38, 54, 0))

    IfConditionFalse(0, -2)

    return RESTART


@NeverRestart(SurvivalFlags.MonitorInMountaintops)
def MonitorInMountaintops():
    DisableFlag(SurvivalFlags.PlayerInMountaintops)

    IfInsideMapTile(-1, WEST_CONSECRATED_SNOWFIELD)
    IfInsideMapTile(-1, NORTHWEST_MOUNTAINTOPS)
    IfInsideMapTile(-1, NORTHEAST_MOUNTAINTOPS)
    IfInsideMapTile(-1, SOUTHEAST_MOUNTAINTOPS)
    IfInsideMapTile(-1, (60, 24, 27, 1))
    IfInsideMapTile(-1, (60, 25, 26, 1))  # entrance from Rold
    IfInsideMapTile(-1, (60, 25, 27, 1))
    IfInsideMapTile(-1, (60, 23, 27, 1))  # edge facing Leyndell

    IfConditionTrue(0, -1)

    EnableFlag(SurvivalFlags.PlayerInMountaintops)

    IfInsideMapTile(-2, WEST_CONSECRATED_SNOWFIELD)
    IfInsideMapTile(-2, NORTHWEST_MOUNTAINTOPS)
    IfInsideMapTile(-2, NORTHEAST_MOUNTAINTOPS)
    IfInsideMapTile(-2, SOUTHEAST_MOUNTAINTOPS)
    IfInsideMapTile(-2, (60, 24, 27, 1))
    IfInsideMapTile(-2, (60, 25, 26, 1))  # entrance from Rold
    IfInsideMapTile(-2, (60, 25, 27, 1))
    IfInsideMapTile(-2, (60, 23, 27, 1))  # edge facing Leyndell

    IfConditionFalse(0, -2)

    return RESTART


@NeverRestart(SurvivalFlags.CraftDummyWeaponBase)
def CraftDummyWeapon(_, dummy_weapon_id: int, weapon_item_lot: int, previous_weapon: int):
    """Wait for player to obtain a crafted dummy weapon, then remove it, remove the previous "required" weapon in
    the recipe (if nonzero), and award the real item."""
    IfPlayerHasWeapon(0, dummy_weapon_id)
    RemoveWeaponFromPlayer(dummy_weapon_id, 1)
    AwardItemLot(weapon_item_lot)
    if previous_weapon != 0:
        RemoveWeaponFromPlayer(previous_weapon, 1)  # let's hope the count field actually works now :/
    return RESTART


@NeverRestart(SurvivalFlags.MonitorWeaponPossessionBase)
def MonitorWeaponPossession(_, weapon_id: int, possession_flag: int):
    """Enable `possession_flag` as long as player has exactly `weapon_id`. This possession flag is used to enable
    the visibility of upgrade recipes that require this weapon."""
    DisableFlag(possession_flag)
    IfPlayerHasWeapon(0, weapon_id)
    EnableFlag(possession_flag)  # future recipes will be visible
    IfPlayerDoesNotHaveWeapon(0, weapon_id)
    return RESTART
