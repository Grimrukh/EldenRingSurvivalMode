"""New common EMEVD events for Elden Ring Survival Mode.

Kept separate to `common.evs.py` because I will probably regenerate the vanilla events in that file from time to time as
my understanding of ER EMEVD instructions becomes better.
"""
from soulstruct.eldenring.events import *
from .survival_enums import *


# TODO: Special event that buffs Malenia if you have Pure Scarlet Rot.
#  (Too lazy to put it in Haligtree map; just check for battle start flag.)


@NeverRestart(0)
def Constructor():
    """Will be merged with vanilla Common."""

    # If player is maximally thirsty on load, replace with second-to-max.
    # TODO: Actually, this should only apply AFTER DEATH.
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.Thirst9)
    CancelSpecialEffect(PLAYER, SurvivalEffects.Thirst9)
    AddSpecialEffect(PLAYER, SurvivalEffects.Thirst8)

    GrowingHunger()
    GrowingThirst()

    # Temperature effect checks
    CheckMildHeatArea()
    CheckModerateHeatArea()
    CheckSevereHeatArea()
    CheckMildColdArea()
    CheckModerateColdArea()
    CheckSevereColdArea()

    # Disease checks
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
        SurvivalEffects.RayaLucariaToxin,
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

    # Disease cure checks
    CurePlague()
    CureToxin()
    CureFever()
    CureParasite()
    # CurePureScarletRot()

    # Swap dummy weapons for real weapons.
    # region Dummy Weapons
    ReplaceDummyWeapon(0, 60010000, 40010000)
    ReplaceDummyWeapon(1, 60010100, 40010100)
    ReplaceDummyWeapon(2, 60010200, 40010200)
    ReplaceDummyWeapon(3, 60010300, 40010300)
    ReplaceDummyWeapon(4, 60010400, 40010400)
    ReplaceDummyWeapon(5, 60010500, 40010500)
    ReplaceDummyWeapon(6, 60010600, 40010600)
    ReplaceDummyWeapon(7, 60010700, 40010700)
    ReplaceDummyWeapon(8, 60010800, 40010800)
    ReplaceDummyWeapon(9, 60010900, 40010900)
    ReplaceDummyWeapon(10, 60011000, 40011000)
    ReplaceDummyWeapon(11, 60011100, 40011100)
    ReplaceDummyWeapon(12, 60011300, 40011300)
    ReplaceDummyWeapon(13, 60011400, 40011400)
    ReplaceDummyWeapon(14, 60011500, 40011500)
    ReplaceDummyWeapon(15, 60011600, 40011600)
    ReplaceDummyWeapon(16, 60020000, 40020000)
    ReplaceDummyWeapon(17, 60020100, 40020100)
    ReplaceDummyWeapon(18, 60020200, 40020200)
    ReplaceDummyWeapon(19, 60020400, 40020400)
    ReplaceDummyWeapon(20, 60020500, 40020500)
    ReplaceDummyWeapon(21, 60020600, 40020600)
    ReplaceDummyWeapon(22, 60020700, 40020700)
    ReplaceDummyWeapon(23, 60020800, 40020800)
    ReplaceDummyWeapon(24, 60020900, 40020900)
    ReplaceDummyWeapon(25, 60021100, 40021100)
    ReplaceDummyWeapon(26, 60021400, 40021400)
    ReplaceDummyWeapon(27, 60021500, 40021500)
    ReplaceDummyWeapon(28, 60021800, 40021800)
    ReplaceDummyWeapon(29, 60021900, 40021900)
    ReplaceDummyWeapon(30, 60022000, 40022000)
    ReplaceDummyWeapon(31, 60022100, 40022100)
    ReplaceDummyWeapon(32, 60022200, 40022200)
    ReplaceDummyWeapon(33, 60022300, 40022300)
    ReplaceDummyWeapon(34, 60022400, 40022400)
    ReplaceDummyWeapon(35, 60022500, 40022500)
    ReplaceDummyWeapon(36, 60022600, 40022600)
    ReplaceDummyWeapon(37, 60030000, 40030000)
    ReplaceDummyWeapon(38, 60030100, 40030100)
    ReplaceDummyWeapon(39, 60030200, 40030200)
    ReplaceDummyWeapon(40, 60030300, 40030300)
    ReplaceDummyWeapon(41, 60030400, 40030400)
    ReplaceDummyWeapon(42, 60030500, 40030500)
    ReplaceDummyWeapon(43, 60030600, 40030600)
    ReplaceDummyWeapon(44, 60030700, 40030700)
    ReplaceDummyWeapon(45, 60030800, 40030800)
    ReplaceDummyWeapon(46, 60030900, 40030900)
    ReplaceDummyWeapon(47, 60031000, 40031000)
    ReplaceDummyWeapon(48, 60031300, 40031300)
    ReplaceDummyWeapon(49, 60031400, 40031400)
    ReplaceDummyWeapon(50, 60031500, 40031500)
    ReplaceDummyWeapon(51, 60031600, 40031600)
    ReplaceDummyWeapon(52, 60031700, 40031700)
    ReplaceDummyWeapon(53, 60031800, 40031800)
    ReplaceDummyWeapon(54, 60031900, 40031900)
    ReplaceDummyWeapon(55, 60032000, 40032000)
    ReplaceDummyWeapon(56, 60032100, 40032100)
    ReplaceDummyWeapon(57, 60040000, 40040000)
    ReplaceDummyWeapon(58, 60040100, 40040100)
    ReplaceDummyWeapon(59, 60040200, 40040200)
    ReplaceDummyWeapon(60, 60040300, 40040300)
    ReplaceDummyWeapon(61, 60040400, 40040400)
    ReplaceDummyWeapon(62, 60040500, 40040500)
    ReplaceDummyWeapon(63, 60040600, 40040600)
    ReplaceDummyWeapon(64, 60040700, 40040700)
    ReplaceDummyWeapon(65, 60040800, 40040800)
    ReplaceDummyWeapon(66, 60041000, 40041000)
    ReplaceDummyWeapon(67, 60041100, 40041100)
    ReplaceDummyWeapon(68, 60050000, 40050000)
    ReplaceDummyWeapon(69, 60050100, 40050100)
    ReplaceDummyWeapon(70, 60050200, 40050200)
    ReplaceDummyWeapon(71, 60050300, 40050300)
    ReplaceDummyWeapon(72, 60050400, 40050400)
    ReplaceDummyWeapon(73, 60050500, 40050500)
    ReplaceDummyWeapon(74, 60050600, 40050600)
    ReplaceDummyWeapon(75, 60060000, 40060000)
    ReplaceDummyWeapon(76, 60060100, 40060100)
    ReplaceDummyWeapon(77, 60060200, 40060200)
    ReplaceDummyWeapon(78, 60060400, 40060400)
    ReplaceDummyWeapon(79, 60070000, 40070000)
    ReplaceDummyWeapon(80, 60070100, 40070100)
    ReplaceDummyWeapon(81, 60070200, 40070200)
    ReplaceDummyWeapon(82, 60070300, 40070300)
    ReplaceDummyWeapon(83, 60070400, 40070400)
    ReplaceDummyWeapon(84, 60070500, 40070500)
    ReplaceDummyWeapon(85, 60070600, 40070600)
    ReplaceDummyWeapon(86, 60070700, 40070700)
    ReplaceDummyWeapon(87, 60070800, 40070800)
    ReplaceDummyWeapon(88, 60071000, 40071000)
    ReplaceDummyWeapon(89, 60071100, 40071100)
    ReplaceDummyWeapon(90, 60071200, 40071200)
    ReplaceDummyWeapon(91, 60071400, 40071400)
    ReplaceDummyWeapon(92, 60071500, 40071500)
    ReplaceDummyWeapon(93, 60080100, 40080100)
    ReplaceDummyWeapon(94, 60080200, 40080200)
    ReplaceDummyWeapon(95, 60080300, 40080300)
    ReplaceDummyWeapon(96, 60080400, 40080400)
    ReplaceDummyWeapon(97, 60080500, 40080500)
    ReplaceDummyWeapon(98, 60080600, 40080600)
    ReplaceDummyWeapon(99, 60080700, 40080700)
    ReplaceDummyWeapon(100, 60080800, 40080800)
    ReplaceDummyWeapon(101, 60081000, 40081000)
    ReplaceDummyWeapon(102, 60090000, 40090000)
    ReplaceDummyWeapon(103, 60090100, 40090100)
    ReplaceDummyWeapon(104, 60090200, 40090200)
    ReplaceDummyWeapon(105, 60090300, 40090300)
    ReplaceDummyWeapon(106, 60090400, 40090400)
    ReplaceDummyWeapon(107, 60090600, 40090600)
    ReplaceDummyWeapon(108, 60090700, 40090700)
    ReplaceDummyWeapon(109, 60090800, 40090800)
    ReplaceDummyWeapon(110, 60100000, 40100000)
    ReplaceDummyWeapon(111, 60100100, 40100100)
    ReplaceDummyWeapon(112, 60100300, 40100300)
    ReplaceDummyWeapon(113, 60100500, 40100500)
    ReplaceDummyWeapon(114, 60100800, 40100800)
    ReplaceDummyWeapon(115, 60100900, 40100900)
    ReplaceDummyWeapon(116, 60110000, 40110000)
    ReplaceDummyWeapon(117, 60110100, 40110100)
    ReplaceDummyWeapon(118, 60110300, 40110300)
    ReplaceDummyWeapon(119, 60110400, 40110400)
    ReplaceDummyWeapon(120, 60110500, 40110500)
    ReplaceDummyWeapon(121, 60110600, 40110600)
    ReplaceDummyWeapon(122, 60110700, 40110700)
    ReplaceDummyWeapon(123, 60110800, 40110800)
    ReplaceDummyWeapon(124, 60110900, 40110900)
    ReplaceDummyWeapon(125, 60111000, 40111000)
    ReplaceDummyWeapon(126, 60111100, 40111100)
    ReplaceDummyWeapon(127, 60111200, 40111200)
    ReplaceDummyWeapon(128, 60111300, 40111300)
    ReplaceDummyWeapon(129, 60111400, 40111400)
    ReplaceDummyWeapon(130, 60111500, 40111500)
    ReplaceDummyWeapon(131, 60120000, 40120000)
    ReplaceDummyWeapon(132, 60120100, 40120100)
    ReplaceDummyWeapon(133, 60120200, 40120200)
    ReplaceDummyWeapon(134, 60120600, 40120600)
    ReplaceDummyWeapon(135, 60120800, 40120800)
    ReplaceDummyWeapon(136, 60121300, 40121300)
    ReplaceDummyWeapon(137, 60121400, 40121400)
    ReplaceDummyWeapon(138, 60121500, 40121500)
    ReplaceDummyWeapon(139, 60121600, 40121600)
    ReplaceDummyWeapon(140, 60121700, 40121700)
    ReplaceDummyWeapon(141, 60121800, 40121800)
    ReplaceDummyWeapon(142, 60121900, 40121900)
    ReplaceDummyWeapon(143, 60122000, 40122000)
    ReplaceDummyWeapon(144, 60122100, 40122100)
    ReplaceDummyWeapon(145, 60130000, 40130000)
    ReplaceDummyWeapon(146, 60130100, 40130100)
    ReplaceDummyWeapon(147, 60130200, 40130200)
    ReplaceDummyWeapon(148, 60130300, 40130300)
    ReplaceDummyWeapon(149, 60130400, 40130400)
    ReplaceDummyWeapon(150, 60140000, 40140000)
    ReplaceDummyWeapon(151, 60140100, 40140100)
    ReplaceDummyWeapon(152, 60140200, 40140200)
    ReplaceDummyWeapon(153, 60140300, 40140300)
    ReplaceDummyWeapon(154, 60140400, 40140400)
    ReplaceDummyWeapon(155, 60140500, 40140500)
    ReplaceDummyWeapon(156, 60140600, 40140600)
    ReplaceDummyWeapon(157, 60140800, 40140800)
    ReplaceDummyWeapon(158, 60141000, 40141000)
    ReplaceDummyWeapon(159, 60141100, 40141100)
    ReplaceDummyWeapon(160, 60141200, 40141200)
    ReplaceDummyWeapon(161, 60141400, 40141400)
    ReplaceDummyWeapon(162, 60150000, 40150000)
    ReplaceDummyWeapon(163, 60150100, 40150100)
    ReplaceDummyWeapon(164, 60150200, 40150200)
    ReplaceDummyWeapon(165, 60150300, 40150300)
    ReplaceDummyWeapon(166, 60150400, 40150400)
    ReplaceDummyWeapon(167, 60150500, 40150500)
    ReplaceDummyWeapon(168, 60150600, 40150600)
    ReplaceDummyWeapon(169, 60150800, 40150800)
    ReplaceDummyWeapon(170, 60151100, 40151100)
    ReplaceDummyWeapon(171, 60151200, 40151200)
    ReplaceDummyWeapon(172, 60151300, 40151300)
    ReplaceDummyWeapon(173, 60151400, 40151400)
    ReplaceDummyWeapon(174, 60160000, 40160000)
    ReplaceDummyWeapon(175, 60160100, 40160100)
    ReplaceDummyWeapon(176, 60160200, 40160200)
    ReplaceDummyWeapon(177, 60160300, 40160300)
    ReplaceDummyWeapon(178, 60160400, 40160400)
    ReplaceDummyWeapon(179, 60160500, 40160500)
    ReplaceDummyWeapon(180, 60160600, 40160600)
    ReplaceDummyWeapon(181, 60160700, 40160700)
    ReplaceDummyWeapon(182, 60160800, 40160800)
    ReplaceDummyWeapon(183, 60160900, 40160900)
    ReplaceDummyWeapon(184, 60161100, 40161100)
    ReplaceDummyWeapon(185, 60161200, 40161200)
    ReplaceDummyWeapon(186, 60161300, 40161300)
    ReplaceDummyWeapon(187, 60161400, 40161400)
    ReplaceDummyWeapon(188, 60161500, 40161500)
    ReplaceDummyWeapon(189, 60161600, 40161600)
    ReplaceDummyWeapon(190, 60170100, 40170100)
    ReplaceDummyWeapon(191, 60170200, 40170200)
    ReplaceDummyWeapon(192, 60170300, 40170300)
    ReplaceDummyWeapon(193, 60170500, 40170500)
    ReplaceDummyWeapon(194, 60170600, 40170600)
    ReplaceDummyWeapon(195, 60170700, 40170700)
    ReplaceDummyWeapon(196, 60180000, 40180000)
    ReplaceDummyWeapon(197, 60180100, 40180100)
    ReplaceDummyWeapon(198, 60180200, 40180200)
    ReplaceDummyWeapon(199, 60180300, 40180300)
    ReplaceDummyWeapon(200, 60180400, 40180400)
    ReplaceDummyWeapon(201, 60180500, 40180500)
    ReplaceDummyWeapon(202, 60180600, 40180600)
    ReplaceDummyWeapon(203, 60180700, 40180700)
    ReplaceDummyWeapon(204, 60180800, 40180800)
    ReplaceDummyWeapon(205, 60180900, 40180900)
    ReplaceDummyWeapon(206, 60181000, 40181000)
    ReplaceDummyWeapon(207, 60181100, 40181100)
    ReplaceDummyWeapon(208, 60181300, 40181300)
    ReplaceDummyWeapon(209, 60181400, 40181400)
    ReplaceDummyWeapon(210, 60181500, 40181500)
    ReplaceDummyWeapon(211, 60181600, 40181600)
    ReplaceDummyWeapon(212, 60190000, 40190000)
    ReplaceDummyWeapon(213, 60190100, 40190100)
    ReplaceDummyWeapon(214, 60190200, 40190200)
    ReplaceDummyWeapon(215, 60190600, 40190600)
    ReplaceDummyWeapon(216, 60200000, 40200000)
    ReplaceDummyWeapon(217, 60200200, 40200200)
    ReplaceDummyWeapon(218, 60200300, 40200300)
    ReplaceDummyWeapon(219, 60200500, 40200500)
    ReplaceDummyWeapon(220, 60200600, 40200600)
    ReplaceDummyWeapon(221, 60200700, 40200700)
    ReplaceDummyWeapon(222, 60210000, 40210000)
    ReplaceDummyWeapon(223, 60210100, 40210100)
    ReplaceDummyWeapon(224, 60210600, 40210600)
    ReplaceDummyWeapon(225, 60210700, 40210700)
    ReplaceDummyWeapon(226, 60210800, 40210800)
    ReplaceDummyWeapon(227, 60211000, 40211000)
    ReplaceDummyWeapon(228, 60211100, 40211100)
    ReplaceDummyWeapon(229, 60211200, 40211200)
    ReplaceDummyWeapon(230, 60211300, 40211300)
    ReplaceDummyWeapon(231, 60220000, 40220000)
    ReplaceDummyWeapon(232, 60220100, 40220100)
    ReplaceDummyWeapon(233, 60220200, 40220200)
    ReplaceDummyWeapon(234, 60220300, 40220300)
    ReplaceDummyWeapon(235, 60230000, 40230000)
    ReplaceDummyWeapon(236, 60230100, 40230100)
    ReplaceDummyWeapon(237, 60230200, 40230200)
    ReplaceDummyWeapon(238, 60230300, 40230300)
    ReplaceDummyWeapon(239, 60230400, 40230400)
    ReplaceDummyWeapon(240, 60230500, 40230500)
    ReplaceDummyWeapon(241, 60230600, 40230600)
    ReplaceDummyWeapon(242, 60230700, 40230700)
    ReplaceDummyWeapon(243, 60230800, 40230800)
    ReplaceDummyWeapon(244, 60231000, 40231000)
    ReplaceDummyWeapon(245, 60231100, 40231100)
    ReplaceDummyWeapon(246, 60231200, 40231200)
    ReplaceDummyWeapon(247, 60231300, 40231300)
    ReplaceDummyWeapon(248, 60231400, 40231400)
    ReplaceDummyWeapon(249, 60231500, 40231500)
    ReplaceDummyWeapon(250, 60240000, 40240000)
    ReplaceDummyWeapon(251, 60240200, 40240200)
    ReplaceDummyWeapon(252, 60240400, 40240400)
    ReplaceDummyWeapon(253, 60240500, 40240500)
    ReplaceDummyWeapon(254, 60240600, 40240600)
    ReplaceDummyWeapon(255, 60240700, 40240700)
    ReplaceDummyWeapon(256, 60300000, 40300000)
    ReplaceDummyWeapon(257, 60300100, 40300100)
    ReplaceDummyWeapon(258, 60300200, 40300200)
    ReplaceDummyWeapon(259, 60300300, 40300300)
    ReplaceDummyWeapon(260, 60300400, 40300400)
    ReplaceDummyWeapon(261, 60300600, 40300600)
    ReplaceDummyWeapon(262, 60300700, 40300700)
    ReplaceDummyWeapon(263, 60300800, 40300800)
    ReplaceDummyWeapon(264, 60300900, 40300900)
    ReplaceDummyWeapon(265, 60301000, 40301000)
    ReplaceDummyWeapon(266, 60301100, 40301100)
    ReplaceDummyWeapon(267, 60301200, 40301200)
    ReplaceDummyWeapon(268, 60301300, 40301300)
    ReplaceDummyWeapon(269, 60301400, 40301400)
    ReplaceDummyWeapon(270, 60301500, 40301500)
    ReplaceDummyWeapon(271, 60301900, 40301900)
    ReplaceDummyWeapon(272, 60302000, 40302000)
    ReplaceDummyWeapon(273, 60310000, 40310000)
    ReplaceDummyWeapon(274, 60310100, 40310100)
    ReplaceDummyWeapon(275, 60310200, 40310200)
    ReplaceDummyWeapon(276, 60310300, 40310300)
    ReplaceDummyWeapon(277, 60310400, 40310400)
    ReplaceDummyWeapon(278, 60310500, 40310500)
    ReplaceDummyWeapon(279, 60310600, 40310600)
    ReplaceDummyWeapon(280, 60310700, 40310700)
    ReplaceDummyWeapon(281, 60310800, 40310800)
    ReplaceDummyWeapon(282, 60310900, 40310900)
    ReplaceDummyWeapon(283, 60311000, 40311000)
    ReplaceDummyWeapon(284, 60311300, 40311300)
    ReplaceDummyWeapon(285, 60311400, 40311400)
    ReplaceDummyWeapon(286, 60311700, 40311700)
    ReplaceDummyWeapon(287, 60311900, 40311900)
    ReplaceDummyWeapon(288, 60312300, 40312300)
    ReplaceDummyWeapon(289, 60312400, 40312400)
    ReplaceDummyWeapon(290, 60312500, 40312500)
    ReplaceDummyWeapon(291, 60312600, 40312600)
    ReplaceDummyWeapon(292, 60312700, 40312700)
    ReplaceDummyWeapon(293, 60312800, 40312800)
    ReplaceDummyWeapon(294, 60312900, 40312900)
    ReplaceDummyWeapon(295, 60313000, 40313000)
    ReplaceDummyWeapon(296, 60313100, 40313100)
    ReplaceDummyWeapon(297, 60313200, 40313200)
    ReplaceDummyWeapon(298, 60313300, 40313300)
    ReplaceDummyWeapon(299, 60313400, 40313400)
    ReplaceDummyWeapon(300, 60320000, 40320000)
    ReplaceDummyWeapon(301, 60320200, 40320200)
    ReplaceDummyWeapon(302, 60320300, 40320300)
    ReplaceDummyWeapon(303, 60320400, 40320400)
    ReplaceDummyWeapon(304, 60320500, 40320500)
    ReplaceDummyWeapon(305, 60320800, 40320800)
    ReplaceDummyWeapon(306, 60320900, 40320900)
    ReplaceDummyWeapon(307, 60321200, 40321200)
    ReplaceDummyWeapon(308, 60321300, 40321300)
    ReplaceDummyWeapon(309, 60321400, 40321400)
    ReplaceDummyWeapon(310, 60321500, 40321500)
    ReplaceDummyWeapon(311, 60321600, 40321600)
    ReplaceDummyWeapon(312, 60321700, 40321700)
    ReplaceDummyWeapon(313, 60321900, 40321900)
    ReplaceDummyWeapon(314, 60322000, 40322000)
    ReplaceDummyWeapon(315, 60322100, 40322100)
    ReplaceDummyWeapon(316, 60322200, 40322200)
    ReplaceDummyWeapon(317, 60322300, 40322300)
    ReplaceDummyWeapon(318, 60322400, 40322400)
    ReplaceDummyWeapon(319, 60322500, 40322500)
    ReplaceDummyWeapon(320, 60322600, 40322600)
    ReplaceDummyWeapon(321, 60322700, 40322700)
    ReplaceDummyWeapon(322, 60322800, 40322800)
    ReplaceDummyWeapon(323, 60322900, 40322900)
    ReplaceDummyWeapon(324, 60323000, 40323000)
    ReplaceDummyWeapon(325, 60330000, 40330000)
    ReplaceDummyWeapon(326, 60330400, 40330400)
    ReplaceDummyWeapon(327, 60330500, 40330500)
    ReplaceDummyWeapon(328, 60330600, 40330600)
    ReplaceDummyWeapon(329, 60330900, 40330900)
    ReplaceDummyWeapon(330, 60331200, 40331200)
    ReplaceDummyWeapon(331, 60331300, 40331300)
    ReplaceDummyWeapon(332, 60331700, 40331700)
    ReplaceDummyWeapon(333, 60331800, 40331800)
    ReplaceDummyWeapon(334, 60331900, 40331900)
    ReplaceDummyWeapon(335, 60332000, 40332000)
    ReplaceDummyWeapon(336, 60332100, 40332100)
    ReplaceDummyWeapon(337, 60332300, 40332300)
    ReplaceDummyWeapon(338, 60332400, 40332400)
    ReplaceDummyWeapon(339, 60332500, 40332500)
    ReplaceDummyWeapon(340, 60332600, 40332600)
    ReplaceDummyWeapon(341, 60332700, 40332700)
    ReplaceDummyWeapon(342, 60332800, 40332800)
    ReplaceDummyWeapon(343, 60340000, 40340000)
    ReplaceDummyWeapon(344, 60340100, 40340100)
    ReplaceDummyWeapon(345, 60340200, 40340200)
    ReplaceDummyWeapon(346, 60340300, 40340300)
    ReplaceDummyWeapon(347, 60340400, 40340400)
    ReplaceDummyWeapon(348, 60340600, 40340600)
    ReplaceDummyWeapon(349, 60340700, 40340700)
    ReplaceDummyWeapon(350, 60340800, 40340800)
    ReplaceDummyWeapon(351, 60340900, 40340900)
    ReplaceDummyWeapon(352, 60400000, 40400000)
    ReplaceDummyWeapon(353, 60400100, 40400100)
    ReplaceDummyWeapon(354, 60400200, 40400200)
    ReplaceDummyWeapon(355, 60400300, 40400300)
    ReplaceDummyWeapon(356, 60400500, 40400500)
    ReplaceDummyWeapon(357, 60410000, 40410000)
    ReplaceDummyWeapon(358, 60410100, 40410100)
    ReplaceDummyWeapon(359, 60410200, 40410200)
    ReplaceDummyWeapon(360, 60410300, 40410300)
    ReplaceDummyWeapon(361, 60410400, 40410400)
    ReplaceDummyWeapon(362, 60410600, 40410600)
    ReplaceDummyWeapon(363, 60410700, 40410700)
    ReplaceDummyWeapon(364, 60420000, 40420000)
    ReplaceDummyWeapon(365, 60420100, 40420100)
    ReplaceDummyWeapon(366, 60420300, 40420300)
    ReplaceDummyWeapon(367, 60420400, 40420400)
    ReplaceDummyWeapon(368, 60430000, 40430000)
    ReplaceDummyWeapon(369, 60430200, 40430200)
    ReplaceDummyWeapon(370, 60430300, 40430300)
    ReplaceDummyWeapon(371, 60430500, 40430500)
    ReplaceDummyWeapon(372, 60430600, 40430600)
    ReplaceDummyWeapon(373, 60430800, 40430800)
    ReplaceDummyWeapon(374, 60431100, 40431100)
    ReplaceDummyWeapon(375, 60440000, 40440000)
    ReplaceDummyWeapon(376, 60440100, 40440100)
    # endregion


@NeverRestart(SurvivalFlags.GrowingHunger)
def GrowingHunger():
    """Hunger ticks up every 60 seconds."""

    # Hunger cannot grow while Draught of the Undining is active (or hunger is at max).
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.DraughtOfTheUndining)
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

    # INCREMENT HUNGER
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
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.RayaLucariaToxin)
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.VolcanoManorToxin)
    IfConditionTrue(1, -1)

    IfConditionTrue(0, 1)

    CancelSpecialEffect(PLAYER, SurvivalEffects.LiurniaToxin)
    CancelSpecialEffect(PLAYER, SurvivalEffects.CatacombsToxin)
    CancelSpecialEffect(PLAYER, SurvivalEffects.AinselToxin)
    CancelSpecialEffect(PLAYER, SurvivalEffects.RayaLucariaToxin)
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


@NeverRestart(SurvivalFlags.WeaponCraftingBase)
def ReplaceDummyWeapon(_, dummy_weapon_id: int, weapon_item_lot: int):
    IfPlayerHasWeapon(0, dummy_weapon_id)
    RemoveWeaponFromPlayer(dummy_weapon_id, 1)
    AwardItemLot(weapon_item_lot)
    return RESTART
