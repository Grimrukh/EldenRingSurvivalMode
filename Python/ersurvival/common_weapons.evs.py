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

    # region WEAPONS
    # Swap dummy weapons for real weapons and monitor weapon possession (plus a Smith's Hammer) for upgrading.
    # region Dummy Weapons
    CraftDummyWeapon(0, 60010000, 40010000, 0)
    AllowWeaponUpgrade(0, 1000000, 0, 11051000)
    CraftDummyWeapon(1, 60010100, 40010100, 1160009)
    AllowWeaponUpgrade(1, 1010010, 8404, 11051001)
    CraftDummyWeapon(2, 60010200, 40010200, 1140006)
    AllowWeaponUpgrade(2, 1020009, 8402, 11051002)
    CraftDummyWeapon(3, 60010300, 40010300, 1140006)
    AllowWeaponUpgrade(3, 1030009, 8402, 11051003)
    CraftDummyWeapon(4, 60010400, 40010400, 1160009)
    AllowWeaponUpgrade(4, 1040010, 8404, 11051004)
    CraftDummyWeapon(5, 60010500, 40010500, 1100012)
    AllowWeaponUpgrade(5, 1050015, 8404, 11051005)
    CraftDummyWeapon(6, 60010600, 40010600, 1030009)
    AllowWeaponUpgrade(6, 1060012, 8403, 11051006)
    CraftDummyWeapon(7, 60010700, 40010700, 1050015)
    AllowWeaponUpgrade(7, 1070010, 8404, 11051007)
    CraftDummyWeapon(8, 60010800, 40010800, 1130015)
    AllowWeaponUpgrade(8, 1080010, 8404, 11051008)
    CraftDummyWeapon(9, 60010900, 40010900, 1000000)
    AllowWeaponUpgrade(9, 1090003, 8400, 11051009)
    CraftDummyWeapon(10, 60011000, 40011000, 1020009)
    AllowWeaponUpgrade(10, 1100012, 8403, 11051010)
    CraftDummyWeapon(11, 60011100, 40011100, 1100012)
    AllowWeaponUpgrade(11, 1110010, 8404, 11051011)
    CraftDummyWeapon(12, 60011300, 40011300, 1060012)
    AllowWeaponUpgrade(12, 1130015, 8404, 11051012)
    CraftDummyWeapon(13, 60011400, 40011400, 1090003)
    AllowWeaponUpgrade(13, 1140006, 8401, 11051013)
    CraftDummyWeapon(14, 60011500, 40011500, 1100012)
    AllowWeaponUpgrade(14, 1150015, 8404, 11051014)
    CraftDummyWeapon(15, 60011600, 40011600, 1150015)
    AllowWeaponUpgrade(15, 1160009, 8404, 11051015)
    CraftDummyWeapon(16, 60020000, 40020000, 2050004)
    AllowWeaponUpgrade(16, 2000006, 8401, 11051016)
    CraftDummyWeapon(17, 60020100, 40020100, 1000000)
    AllowWeaponUpgrade(17, 2010002, 0, 11051017)
    CraftDummyWeapon(18, 60020200, 40020200, 2000006)
    AllowWeaponUpgrade(18, 2020008, 8401, 11051018)
    CraftDummyWeapon(19, 60020400, 40020400, 2020008)
    AllowWeaponUpgrade(19, 2040010, 8402, 11051019)
    CraftDummyWeapon(20, 60020500, 40020500, 2010002)
    AllowWeaponUpgrade(20, 2050004, 8400, 11051020)
    CraftDummyWeapon(21, 60020600, 40020600, 2040010)
    AllowWeaponUpgrade(21, 2060006, 8403, 11051021)
    CraftDummyWeapon(22, 60020700, 40020700, 2110008)
    AllowWeaponUpgrade(22, 2070009, 8404, 11051022)
    CraftDummyWeapon(23, 60020800, 40020800, 7060015)
    AllowWeaponUpgrade(23, 2080009, 8404, 11051023)
    CraftDummyWeapon(24, 60020900, 40020900, 3050014)
    AllowWeaponUpgrade(24, 2090008, 8404, 11051024)
    CraftDummyWeapon(25, 60021100, 40021100, 2060006)
    AllowWeaponUpgrade(25, 2110008, 8404, 11051025)
    CraftDummyWeapon(26, 60021400, 40021400, 2180008)
    AllowWeaponUpgrade(26, 2140010, 8404, 11051026)
    CraftDummyWeapon(27, 60021500, 40021500, 2000006)
    AllowWeaponUpgrade(27, 2150004, 8401, 11051027)
    CraftDummyWeapon(28, 60021800, 40021800, 2190007)
    AllowWeaponUpgrade(28, 2180008, 8404, 11051028)
    CraftDummyWeapon(29, 60021900, 40021900, 2250006)
    AllowWeaponUpgrade(29, 2190007, 8403, 11051029)
    CraftDummyWeapon(30, 60022000, 40022000, 2070009)
    AllowWeaponUpgrade(30, 2200010, 8404, 11051030)
    CraftDummyWeapon(31, 60022100, 40022100, 2230012)
    AllowWeaponUpgrade(31, 2210015, 8404, 11051031)
    CraftDummyWeapon(32, 60022200, 40022200, 2240018)
    AllowWeaponUpgrade(32, 2220010, 8404, 11051032)
    CraftDummyWeapon(33, 60022300, 40022300, 2040010)
    AllowWeaponUpgrade(33, 2230012, 8403, 11051033)
    CraftDummyWeapon(34, 60022400, 40022400, 2210015)
    AllowWeaponUpgrade(34, 2240018, 8404, 11051034)
    CraftDummyWeapon(35, 60022500, 40022500, 2260005)
    AllowWeaponUpgrade(35, 2250006, 8403, 11051035)
    CraftDummyWeapon(36, 60022600, 40022600, 2150004)
    AllowWeaponUpgrade(36, 2260005, 8402, 11051036)
    CraftDummyWeapon(37, 60030000, 40030000, 2020008)
    AllowWeaponUpgrade(37, 3000009, 8402, 11051037)
    CraftDummyWeapon(38, 60030100, 40030100, 3180010)
    AllowWeaponUpgrade(38, 3010012, 8403, 11051038)
    CraftDummyWeapon(39, 60030200, 40030200, 3080014)
    AllowWeaponUpgrade(39, 3020015, 8404, 11051039)
    CraftDummyWeapon(40, 60030300, 40030300, 3180010)
    AllowWeaponUpgrade(40, 3030012, 8403, 11051040)
    CraftDummyWeapon(41, 60030400, 40030400, 3080014)
    AllowWeaponUpgrade(41, 3040015, 8404, 11051041)
    CraftDummyWeapon(42, 60030500, 40030500, 3010012)
    AllowWeaponUpgrade(42, 3050014, 8403, 11051042)
    CraftDummyWeapon(43, 60030600, 40030600, 3140009)
    AllowWeaponUpgrade(43, 3060010, 8404, 11051043)
    CraftDummyWeapon(44, 60030700, 40030700, 3040015)
    AllowWeaponUpgrade(44, 3070008, 8404, 11051044)
    CraftDummyWeapon(45, 60030800, 40030800, 3030012)
    AllowWeaponUpgrade(45, 3080014, 8403, 11051045)
    CraftDummyWeapon(46, 60030900, 40030900, 3130009)
    AllowWeaponUpgrade(46, 3090010, 8404, 11051046)
    CraftDummyWeapon(47, 60031000, 40031000, 2090008)
    AllowWeaponUpgrade(47, 3100010, 8404, 11051047)
    CraftDummyWeapon(48, 60031300, 40031300, 3070008)
    AllowWeaponUpgrade(48, 3130009, 8404, 11051048)
    CraftDummyWeapon(49, 60031400, 40031400, 3040015)
    AllowWeaponUpgrade(49, 3140009, 8404, 11051049)
    CraftDummyWeapon(50, 60031500, 40031500, 3040015)
    AllowWeaponUpgrade(50, 3150010, 8404, 11051050)
    CraftDummyWeapon(51, 60031600, 40031600, 3050014)
    AllowWeaponUpgrade(51, 3160008, 8404, 11051051)
    CraftDummyWeapon(52, 60031700, 40031700, 2090008)
    AllowWeaponUpgrade(52, 3170010, 8404, 11051052)
    CraftDummyWeapon(53, 60031800, 40031800, 3000009)
    AllowWeaponUpgrade(53, 3180010, 8402, 11051053)
    CraftDummyWeapon(54, 60031900, 40031900, 3040015)
    AllowWeaponUpgrade(54, 3190018, 8404, 11051054)
    CraftDummyWeapon(55, 60032000, 40032000, 3160008)
    AllowWeaponUpgrade(55, 3200010, 8404, 11051055)
    CraftDummyWeapon(56, 60032100, 40032100, 3190018)
    AllowWeaponUpgrade(56, 3210010, 8404, 11051056)
    CraftDummyWeapon(57, 60040000, 40040000, 4010017)
    AllowWeaponUpgrade(57, 4000018, 8404, 11051057)
    CraftDummyWeapon(58, 60040100, 40040100, 4040016)
    AllowWeaponUpgrade(58, 4010017, 8404, 11051058)
    CraftDummyWeapon(59, 60040200, 40040200, 4010017)
    AllowWeaponUpgrade(59, 4020010, 8404, 11051059)
    CraftDummyWeapon(60, 60040300, 40040300, 4040016)
    AllowWeaponUpgrade(60, 4030017, 8404, 11051060)
    CraftDummyWeapon(61, 60040400, 40040400, 3020015)
    AllowWeaponUpgrade(61, 4040016, 8404, 11051061)
    CraftDummyWeapon(62, 60040500, 40040500, 4010017)
    AllowWeaponUpgrade(62, 4050010, 8404, 11051062)
    CraftDummyWeapon(63, 60040600, 40040600, 4110009)
    AllowWeaponUpgrade(63, 4060010, 8404, 11051063)
    CraftDummyWeapon(64, 60040700, 40040700, 4110009)
    AllowWeaponUpgrade(64, 4070010, 8404, 11051064)
    CraftDummyWeapon(65, 60040800, 40040800, 4000018)
    AllowWeaponUpgrade(65, 4080010, 8404, 11051065)
    CraftDummyWeapon(66, 60041000, 40041000, 4000018)
    AllowWeaponUpgrade(66, 4100010, 8404, 11051066)
    CraftDummyWeapon(67, 60041100, 40041100, 4030017)
    AllowWeaponUpgrade(67, 4110009, 8404, 11051067)
    CraftDummyWeapon(68, 60050000, 40050000, 5060010)
    AllowWeaponUpgrade(68, 5000012, 8403, 11051068)
    CraftDummyWeapon(69, 60050100, 40050100, 5000012)
    AllowWeaponUpgrade(69, 5010014, 8403, 11051069)
    CraftDummyWeapon(70, 60050200, 40050200, 2000006)
    AllowWeaponUpgrade(70, 5020008, 8401, 11051070)
    CraftDummyWeapon(71, 60050300, 40050300, 5000012)
    AllowWeaponUpgrade(71, 5030014, 8403, 11051071)
    CraftDummyWeapon(72, 60050400, 40050400, 5030014)
    AllowWeaponUpgrade(72, 5040017, 8404, 11051072)
    CraftDummyWeapon(73, 60050500, 40050500, 5040017)
    AllowWeaponUpgrade(73, 5050010, 8404, 11051073)
    CraftDummyWeapon(74, 60050600, 40050600, 5020008)
    AllowWeaponUpgrade(74, 5060010, 8402, 11051074)
    CraftDummyWeapon(75, 60060000, 40060000, 6010017)
    AllowWeaponUpgrade(75, 6000010, 8404, 11051075)
    CraftDummyWeapon(76, 60060100, 40060100, 6020016)
    AllowWeaponUpgrade(76, 6010017, 8404, 11051076)
    CraftDummyWeapon(77, 60060200, 40060200, 5010014)
    AllowWeaponUpgrade(77, 6020016, 8404, 11051077)
    CraftDummyWeapon(78, 60060400, 40060400, 6010017)
    AllowWeaponUpgrade(78, 6040010, 8404, 11051078)
    CraftDummyWeapon(79, 60070000, 40070000, 7030006)
    AllowWeaponUpgrade(79, 7000008, 8401, 11051079)
    CraftDummyWeapon(80, 60070100, 40070100, 7110010)
    AllowWeaponUpgrade(80, 7010012, 8403, 11051080)
    CraftDummyWeapon(81, 60070200, 40070200, 7060015)
    AllowWeaponUpgrade(81, 7020018, 8404, 11051081)
    CraftDummyWeapon(82, 60070300, 40070300, 7140004)
    AllowWeaponUpgrade(82, 7030006, 8401, 11051082)
    CraftDummyWeapon(83, 60070400, 40070400, 7030006)
    AllowWeaponUpgrade(83, 7040008, 8401, 11051083)
    CraftDummyWeapon(84, 60070500, 40070500, 2080009)
    AllowWeaponUpgrade(84, 7050010, 8404, 11051084)
    CraftDummyWeapon(85, 60070600, 40070600, 7120012)
    AllowWeaponUpgrade(85, 7060015, 8404, 11051085)
    CraftDummyWeapon(86, 60070700, 40070700, 2080009)
    AllowWeaponUpgrade(86, 7070010, 8404, 11051086)
    CraftDummyWeapon(87, 60070800, 40070800, 7000008)
    AllowWeaponUpgrade(87, 7080010, 8402, 11051087)
    CraftDummyWeapon(88, 60071000, 40071000, 7020018)
    AllowWeaponUpgrade(88, 7100010, 8404, 11051088)
    CraftDummyWeapon(89, 60071100, 40071100, 7040008)
    AllowWeaponUpgrade(89, 7110010, 8402, 11051089)
    CraftDummyWeapon(90, 60071200, 40071200, 7080010)
    AllowWeaponUpgrade(90, 7120012, 8403, 11051090)
    CraftDummyWeapon(91, 60071400, 40071400, 2010002)
    AllowWeaponUpgrade(91, 7140004, 8400, 11051091)
    CraftDummyWeapon(92, 60071500, 40071500, 7010012)
    AllowWeaponUpgrade(92, 7150014, 8403, 11051092)
    CraftDummyWeapon(93, 60080100, 40080100, 8060018)
    AllowWeaponUpgrade(93, 8010010, 8404, 11051093)
    CraftDummyWeapon(94, 60080200, 40080200, 7150014)
    AllowWeaponUpgrade(94, 8020016, 8404, 11051094)
    CraftDummyWeapon(95, 60080300, 40080300, 8050008)
    AllowWeaponUpgrade(95, 8030009, 8404, 11051095)
    CraftDummyWeapon(96, 60080400, 40080400, 8060018)
    AllowWeaponUpgrade(96, 8040010, 8404, 11051096)
    CraftDummyWeapon(97, 60080500, 40080500, 8070012)
    AllowWeaponUpgrade(97, 8050008, 8404, 11051097)
    CraftDummyWeapon(98, 60080600, 40080600, 8020016)
    AllowWeaponUpgrade(98, 8060018, 8404, 11051098)
    CraftDummyWeapon(99, 60080700, 40080700, 7080010)
    AllowWeaponUpgrade(99, 8070012, 8403, 11051099)
    CraftDummyWeapon(100, 60080800, 40080800, 8060018)
    AllowWeaponUpgrade(100, 8080020, 8404, 11051100)
    CraftDummyWeapon(101, 60081000, 40081000, 8030009)
    AllowWeaponUpgrade(101, 8100010, 8404, 11051101)
    CraftDummyWeapon(102, 60090000, 40090000, 7080010)
    AllowWeaponUpgrade(102, 9000012, 8403, 11051102)
    CraftDummyWeapon(103, 60090100, 40090100, 9080015)
    AllowWeaponUpgrade(103, 9010017, 8404, 11051103)
    CraftDummyWeapon(104, 60090200, 40090200, 9010017)
    AllowWeaponUpgrade(104, 9020010, 8404, 11051104)
    CraftDummyWeapon(105, 60090300, 40090300, 9080015)
    AllowWeaponUpgrade(105, 9030009, 8404, 11051105)
    CraftDummyWeapon(106, 60090400, 40090400, 9070008)
    AllowWeaponUpgrade(106, 9040010, 8404, 11051106)
    CraftDummyWeapon(107, 60090600, 40090600, 9030009)
    AllowWeaponUpgrade(107, 9060010, 8404, 11051107)
    CraftDummyWeapon(108, 60090700, 40090700, 9080015)
    AllowWeaponUpgrade(108, 9070008, 8404, 11051108)
    CraftDummyWeapon(109, 60090800, 40090800, 9000012)
    AllowWeaponUpgrade(109, 9080015, 8404, 11051109)
    CraftDummyWeapon(110, 60100000, 40100000, 2040010)
    AllowWeaponUpgrade(110, 10000012, 8403, 11051110)
    CraftDummyWeapon(111, 60100100, 40100100, 10030014)
    AllowWeaponUpgrade(111, 10010016, 8404, 11051111)
    CraftDummyWeapon(112, 60100300, 40100300, 10000012)
    AllowWeaponUpgrade(112, 10030014, 8403, 11051112)
    CraftDummyWeapon(113, 60100500, 40100500, 10010016)
    AllowWeaponUpgrade(113, 10050010, 8404, 11051113)
    CraftDummyWeapon(114, 60100800, 40100800, 10030014)
    AllowWeaponUpgrade(114, 10080017, 8404, 11051114)
    CraftDummyWeapon(115, 60100900, 40100900, 10080017)
    AllowWeaponUpgrade(115, 10090010, 8404, 11051115)
    CraftDummyWeapon(116, 60110000, 40110000, 11070006)
    AllowWeaponUpgrade(116, 11000009, 8402, 11051116)
    CraftDummyWeapon(117, 60110100, 40110100, 0)
    AllowWeaponUpgrade(117, 11010000, 0, 11051117)
    CraftDummyWeapon(118, 60110300, 40110300, 11010000)
    AllowWeaponUpgrade(118, 11030003, 8400, 11051118)
    CraftDummyWeapon(119, 60110400, 40110400, 11010000)
    AllowWeaponUpgrade(119, 11040003, 8400, 11051119)
    CraftDummyWeapon(120, 60110500, 40110500, 11000009)
    AllowWeaponUpgrade(120, 11050012, 8403, 11051120)
    CraftDummyWeapon(121, 60110600, 40110600, 11090016)
    AllowWeaponUpgrade(121, 11060010, 8404, 11051121)
    CraftDummyWeapon(122, 60110700, 40110700, 11030003)
    AllowWeaponUpgrade(122, 11070006, 8401, 11051122)
    CraftDummyWeapon(123, 60110800, 40110800, 11040003)
    AllowWeaponUpgrade(123, 11080006, 8401, 11051123)
    CraftDummyWeapon(124, 60110900, 40110900, 11050012)
    AllowWeaponUpgrade(124, 11090016, 8404, 11051124)
    CraftDummyWeapon(125, 60111000, 40111000, 11130007)
    AllowWeaponUpgrade(125, 11100008, 8404, 11051125)
    CraftDummyWeapon(126, 60111100, 40111100, 11090016)
    AllowWeaponUpgrade(126, 11110010, 8404, 11051126)
    CraftDummyWeapon(127, 60111200, 40111200, 11130007)
    AllowWeaponUpgrade(127, 11120010, 8404, 11051127)
    CraftDummyWeapon(128, 60111300, 40111300, 11140009)
    AllowWeaponUpgrade(128, 11130007, 8403, 11051128)
    CraftDummyWeapon(129, 60111400, 40111400, 11080006)
    AllowWeaponUpgrade(129, 11140009, 8402, 11051129)
    CraftDummyWeapon(130, 60111500, 40111500, 11100008)
    AllowWeaponUpgrade(130, 11150010, 8404, 11051130)
    CraftDummyWeapon(131, 60120000, 40120000, 11140009)
    AllowWeaponUpgrade(131, 12000010, 8402, 11051131)
    CraftDummyWeapon(132, 60120100, 40120100, 12140014)
    AllowWeaponUpgrade(132, 12010016, 8404, 11051132)
    CraftDummyWeapon(133, 60120200, 40120200, 12140014)
    AllowWeaponUpgrade(133, 12020016, 8404, 11051133)
    CraftDummyWeapon(134, 60120600, 40120600, 12000010)
    AllowWeaponUpgrade(134, 12060012, 8403, 11051134)
    CraftDummyWeapon(135, 60120800, 40120800, 12000010)
    AllowWeaponUpgrade(135, 12080012, 8403, 11051135)
    CraftDummyWeapon(136, 60121300, 40121300, 12000010)
    AllowWeaponUpgrade(136, 12130012, 8403, 11051136)
    CraftDummyWeapon(137, 60121400, 40121400, 12080012)
    AllowWeaponUpgrade(137, 12140014, 8403, 11051137)
    CraftDummyWeapon(138, 60121500, 40121500, 12130012)
    AllowWeaponUpgrade(138, 12150008, 8404, 11051138)
    CraftDummyWeapon(139, 60121600, 40121600, 11100008)
    AllowWeaponUpgrade(139, 12160009, 8404, 11051139)
    CraftDummyWeapon(140, 60121700, 40121700, 12210018)
    AllowWeaponUpgrade(140, 12170010, 8404, 11051140)
    CraftDummyWeapon(141, 60121800, 40121800, 11090016)
    AllowWeaponUpgrade(141, 12180020, 8404, 11051141)
    CraftDummyWeapon(142, 60121900, 40121900, 12060012)
    AllowWeaponUpgrade(142, 12190014, 8403, 11051142)
    CraftDummyWeapon(143, 60122000, 40122000, 12150008)
    AllowWeaponUpgrade(143, 12200010, 8404, 11051143)
    CraftDummyWeapon(144, 60122100, 40122100, 12020016)
    AllowWeaponUpgrade(144, 12210018, 8404, 11051144)
    CraftDummyWeapon(145, 60130000, 40130000, 13010015)
    AllowWeaponUpgrade(145, 13000016, 8404, 11051145)
    CraftDummyWeapon(146, 60130100, 40130100, 11050012)
    AllowWeaponUpgrade(146, 13010015, 8404, 11051146)
    CraftDummyWeapon(147, 60130200, 40130200, 13000016)
    AllowWeaponUpgrade(147, 13020009, 8404, 11051147)
    CraftDummyWeapon(148, 60130300, 40130300, 13020009)
    AllowWeaponUpgrade(148, 13030010, 8404, 11051148)
    CraftDummyWeapon(149, 60130400, 40130400, 13010015)
    AllowWeaponUpgrade(149, 13040018, 8404, 11051149)
    CraftDummyWeapon(150, 60140000, 40140000, 14020000)
    AllowWeaponUpgrade(150, 14000003, 8400, 11051150)
    CraftDummyWeapon(151, 60140100, 40140100, 14060005)
    AllowWeaponUpgrade(151, 14010010, 8402, 11051151)
    CraftDummyWeapon(152, 60140200, 40140200, 0)
    AllowWeaponUpgrade(152, 14020000, 0, 11051152)
    CraftDummyWeapon(153, 60140300, 40140300, 14100008)
    AllowWeaponUpgrade(153, 14030010, 8402, 11051153)
    CraftDummyWeapon(154, 60140400, 40140400, 15010010)
    AllowWeaponUpgrade(154, 14040013, 8403, 11051154)
    CraftDummyWeapon(155, 60140500, 40140500, 14080008)
    AllowWeaponUpgrade(155, 14050020, 8404, 11051155)
    CraftDummyWeapon(156, 60140600, 40140600, 14000003)
    AllowWeaponUpgrade(156, 14060005, 8400, 11051156)
    CraftDummyWeapon(157, 60140800, 40140800, 14010010)
    AllowWeaponUpgrade(157, 14080008, 8404, 11051157)
    CraftDummyWeapon(158, 60141000, 40141000, 14060005)
    AllowWeaponUpgrade(158, 14100008, 8401, 11051158)
    CraftDummyWeapon(159, 60141100, 40141100, 14040013)
    AllowWeaponUpgrade(159, 14110015, 8404, 11051159)
    CraftDummyWeapon(160, 60141200, 40141200, 14110015)
    AllowWeaponUpgrade(160, 14120010, 8404, 11051160)
    CraftDummyWeapon(161, 60141400, 40141400, 14110015)
    AllowWeaponUpgrade(161, 14140010, 8404, 11051161)
    CraftDummyWeapon(162, 60150000, 40150000, 15060013)
    AllowWeaponUpgrade(162, 15000014, 8403, 11051162)
    CraftDummyWeapon(163, 60150100, 40150100, 14100008)
    AllowWeaponUpgrade(163, 15010010, 8402, 11051163)
    CraftDummyWeapon(164, 60150200, 40150200, 15060013)
    AllowWeaponUpgrade(164, 15020015, 8404, 11051164)
    CraftDummyWeapon(165, 60150300, 40150300, 15020015)
    AllowWeaponUpgrade(165, 15030018, 8404, 11051165)
    CraftDummyWeapon(166, 60150400, 40150400, 15080016)
    AllowWeaponUpgrade(166, 15040009, 8404, 11051166)
    CraftDummyWeapon(167, 60150500, 40150500, 15010010)
    AllowWeaponUpgrade(167, 15050012, 8403, 11051167)
    CraftDummyWeapon(168, 60150600, 40150600, 15050012)
    AllowWeaponUpgrade(168, 15060013, 8403, 11051168)
    CraftDummyWeapon(169, 60150800, 40150800, 15000014)
    AllowWeaponUpgrade(169, 15080016, 8404, 11051169)
    CraftDummyWeapon(170, 60151100, 40151100, 15030018)
    AllowWeaponUpgrade(170, 15110010, 8404, 11051170)
    CraftDummyWeapon(171, 60151200, 40151200, 14080008)
    AllowWeaponUpgrade(171, 15120020, 8404, 11051171)
    CraftDummyWeapon(172, 60151300, 40151300, 15020015)
    AllowWeaponUpgrade(172, 15130018, 8404, 11051172)
    CraftDummyWeapon(173, 60151400, 40151400, 15130018)
    AllowWeaponUpgrade(173, 15140010, 8404, 11051173)
    CraftDummyWeapon(174, 60160000, 40160000, 1000000)
    AllowWeaponUpgrade(174, 16000003, 8400, 11051174)
    CraftDummyWeapon(175, 60160100, 40160100, 16000003)
    AllowWeaponUpgrade(175, 16010006, 8401, 11051175)
    CraftDummyWeapon(176, 60160200, 40160200, 16030015)
    AllowWeaponUpgrade(176, 16020008, 8404, 11051176)
    CraftDummyWeapon(177, 60160300, 40160300, 16140014)
    AllowWeaponUpgrade(177, 16030015, 8404, 11051177)
    CraftDummyWeapon(178, 60160400, 40160400, 16140014)
    AllowWeaponUpgrade(178, 16040010, 8404, 11051178)
    CraftDummyWeapon(179, 60160500, 40160500, 16150009)
    AllowWeaponUpgrade(179, 16050012, 8403, 11051179)
    CraftDummyWeapon(180, 60160600, 40160600, 16010006)
    AllowWeaponUpgrade(180, 16060009, 8402, 11051180)
    CraftDummyWeapon(181, 60160700, 40160700, 16050012)
    AllowWeaponUpgrade(181, 16070014, 8403, 11051181)
    CraftDummyWeapon(182, 60160800, 40160800, 16060009)
    AllowWeaponUpgrade(182, 16080012, 8403, 11051182)
    CraftDummyWeapon(183, 60160900, 40160900, 16110017)
    AllowWeaponUpgrade(183, 16090010, 8404, 11051183)
    CraftDummyWeapon(184, 60161100, 40161100, 16140014)
    AllowWeaponUpgrade(184, 16110017, 8404, 11051184)
    CraftDummyWeapon(185, 60161200, 40161200, 16160009)
    AllowWeaponUpgrade(185, 16120010, 8404, 11051185)
    CraftDummyWeapon(186, 60161300, 40161300, 16140014)
    AllowWeaponUpgrade(186, 16130009, 8404, 11051186)
    CraftDummyWeapon(187, 60161400, 40161400, 16080012)
    AllowWeaponUpgrade(187, 16140014, 8403, 11051187)
    CraftDummyWeapon(188, 60161500, 40161500, 16010006)
    AllowWeaponUpgrade(188, 16150009, 8402, 11051188)
    CraftDummyWeapon(189, 60161600, 40161600, 16020008)
    AllowWeaponUpgrade(189, 16160009, 8404, 11051189)
    CraftDummyWeapon(190, 60170100, 40170100, 17060016)
    AllowWeaponUpgrade(190, 17010010, 8404, 11051190)
    CraftDummyWeapon(191, 60170200, 40170200, 17070018)
    AllowWeaponUpgrade(191, 17020010, 8404, 11051191)
    CraftDummyWeapon(192, 60170300, 40170300, 0)
    CraftDummyWeapon(193, 60170500, 40170500, 16130009)
    AllowWeaponUpgrade(193, 17050010, 8404, 11051193)
    CraftDummyWeapon(194, 60170600, 40170600, 16070014)
    AllowWeaponUpgrade(194, 17060016, 8404, 11051194)
    CraftDummyWeapon(195, 60170700, 40170700, 17060016)
    AllowWeaponUpgrade(195, 17070018, 8404, 11051195)
    CraftDummyWeapon(196, 60180000, 40180000, 16150009)
    AllowWeaponUpgrade(196, 18000010, 8402, 11051196)
    CraftDummyWeapon(197, 60180100, 40180100, 18000010)
    AllowWeaponUpgrade(197, 18010012, 8403, 11051197)
    CraftDummyWeapon(198, 60180200, 40180200, 18030012)
    AllowWeaponUpgrade(198, 18020014, 8403, 11051198)
    CraftDummyWeapon(199, 60180300, 40180300, 18000010)
    AllowWeaponUpgrade(199, 18030012, 8403, 11051199)
    CraftDummyWeapon(200, 60180400, 40180400, 18110017)
    AllowWeaponUpgrade(200, 18040010, 8404, 11051200)
    CraftDummyWeapon(201, 60180500, 40180500, 18090016)
    AllowWeaponUpgrade(201, 18050016, 8404, 11051201)
    CraftDummyWeapon(202, 60180600, 40180600, 18130017)
    AllowWeaponUpgrade(202, 18060020, 8404, 11051202)
    CraftDummyWeapon(203, 60180700, 40180700, 18010012)
    AllowWeaponUpgrade(203, 18070014, 8403, 11051203)
    CraftDummyWeapon(204, 60180800, 40180800, 18140008)
    AllowWeaponUpgrade(204, 18080009, 8404, 11051204)
    CraftDummyWeapon(205, 60180900, 40180900, 18020014)
    AllowWeaponUpgrade(205, 18090016, 8404, 11051205)
    CraftDummyWeapon(206, 60181000, 40181000, 18130017)
    AllowWeaponUpgrade(206, 18100010, 8404, 11051206)
    CraftDummyWeapon(207, 60181100, 40181100, 18020014)
    AllowWeaponUpgrade(207, 18110017, 8404, 11051207)
    CraftDummyWeapon(208, 60181300, 40181300, 18070014)
    AllowWeaponUpgrade(208, 18130017, 8404, 11051208)
    CraftDummyWeapon(209, 60181400, 40181400, 18020014)
    AllowWeaponUpgrade(209, 18140008, 8404, 11051209)
    CraftDummyWeapon(210, 60181500, 40181500, 18090016)
    AllowWeaponUpgrade(210, 18150018, 8404, 11051210)
    CraftDummyWeapon(211, 60181600, 40181600, 18150018)
    AllowWeaponUpgrade(211, 18160010, 8404, 11051211)
    CraftDummyWeapon(212, 60190000, 40190000, 18020014)
    AllowWeaponUpgrade(212, 19000016, 8404, 11051212)
    CraftDummyWeapon(213, 60190100, 40190100, 19000016)
    AllowWeaponUpgrade(213, 19010018, 8404, 11051213)
    CraftDummyWeapon(214, 60190200, 40190200, 19000016)
    AllowWeaponUpgrade(214, 19020009, 8404, 11051214)
    CraftDummyWeapon(215, 60190600, 40190600, 19020009)
    AllowWeaponUpgrade(215, 19060010, 8404, 11051215)
    CraftDummyWeapon(216, 60200000, 40200000, 0)
    AllowWeaponUpgrade(216, 20000010, 8402, 11051216)
    CraftDummyWeapon(217, 60200200, 40200200, 20000010)
    AllowWeaponUpgrade(217, 20020013, 8403, 11051217)
    CraftDummyWeapon(218, 60200300, 40200300, 20000010)
    AllowWeaponUpgrade(218, 20030010, 8404, 11051218)
    CraftDummyWeapon(219, 60200500, 40200500, 20070017)
    AllowWeaponUpgrade(219, 20050020, 8404, 11051219)
    CraftDummyWeapon(220, 60200600, 40200600, 20000010)
    AllowWeaponUpgrade(220, 20060010, 8404, 11051220)
    CraftDummyWeapon(221, 60200700, 40200700, 20020013)
    AllowWeaponUpgrade(221, 20070017, 8404, 11051221)
    CraftDummyWeapon(222, 60210000, 40210000, 0)
    AllowWeaponUpgrade(222, 21000000, 0, 11051222)
    CraftDummyWeapon(223, 60210100, 40210100, 21000000)
    AllowWeaponUpgrade(223, 21010003, 8400, 11051223)
    CraftDummyWeapon(224, 60210600, 40210600, 21120008)
    AllowWeaponUpgrade(224, 21060010, 8404, 11051224)
    CraftDummyWeapon(225, 60210700, 40210700, 21100006)
    AllowWeaponUpgrade(225, 21070009, 8402, 11051225)
    CraftDummyWeapon(226, 60210800, 40210800, 21070009)
    AllowWeaponUpgrade(226, 21080012, 8403, 11051226)
    CraftDummyWeapon(227, 60211000, 40211000, 21010003)
    AllowWeaponUpgrade(227, 21100006, 8401, 11051227)
    CraftDummyWeapon(228, 60211100, 40211100, 22030018)
    AllowWeaponUpgrade(228, 21110010, 8404, 11051228)
    CraftDummyWeapon(229, 60211200, 40211200, 21080012)
    AllowWeaponUpgrade(229, 21120008, 8404, 11051229)
    CraftDummyWeapon(230, 60211300, 40211300, 22030018)
    AllowWeaponUpgrade(230, 21130010, 8404, 11051230)
    CraftDummyWeapon(231, 60220000, 40220000, 21100006)
    AllowWeaponUpgrade(231, 22000009, 8402, 11051231)
    CraftDummyWeapon(232, 60220100, 40220100, 22000009)
    AllowWeaponUpgrade(232, 22010012, 8403, 11051232)
    CraftDummyWeapon(233, 60220200, 40220200, 22010012)
    AllowWeaponUpgrade(233, 22020015, 8404, 11051233)
    CraftDummyWeapon(234, 60220300, 40220300, 22020015)
    AllowWeaponUpgrade(234, 22030018, 8404, 11051234)
    CraftDummyWeapon(235, 60230000, 40230000, 23020018)
    AllowWeaponUpgrade(235, 23000020, 8404, 11051235)
    CraftDummyWeapon(236, 60230100, 40230100, 12130012)
    AllowWeaponUpgrade(236, 23010008, 8404, 11051236)
    CraftDummyWeapon(237, 60230200, 40230200, 12190014)
    AllowWeaponUpgrade(237, 23020018, 8404, 11051237)
    CraftDummyWeapon(238, 60230300, 40230300, 12160009)
    AllowWeaponUpgrade(238, 23030010, 8404, 11051238)
    CraftDummyWeapon(239, 60230400, 40230400, 15000014)
    AllowWeaponUpgrade(239, 23040017, 8404, 11051239)
    CraftDummyWeapon(240, 60230500, 40230500, 15040009)
    AllowWeaponUpgrade(240, 23050010, 8404, 11051240)
    CraftDummyWeapon(241, 60230600, 40230600, 23040017)
    AllowWeaponUpgrade(241, 23060010, 8404, 11051241)
    CraftDummyWeapon(242, 60230700, 40230700, 23010008)
    AllowWeaponUpgrade(242, 23070010, 8404, 11051242)
    CraftDummyWeapon(243, 60230800, 40230800, 17060016)
    AllowWeaponUpgrade(243, 23080010, 8404, 11051243)
    CraftDummyWeapon(244, 60231000, 40231000, 19010018)
    AllowWeaponUpgrade(244, 23100010, 8404, 11051244)
    CraftDummyWeapon(245, 60231100, 40231100, 23020018)
    AllowWeaponUpgrade(245, 23110020, 8404, 11051245)
    CraftDummyWeapon(246, 60231200, 40231200, 18080009)
    AllowWeaponUpgrade(246, 23120020, 8404, 11051246)
    CraftDummyWeapon(247, 60231300, 40231300, 12010016)
    AllowWeaponUpgrade(247, 23130020, 8404, 11051247)
    CraftDummyWeapon(248, 60231400, 40231400, 23010008)
    AllowWeaponUpgrade(248, 23140010, 8404, 11051248)
    CraftDummyWeapon(249, 60231500, 40231500, 23040017)
    AllowWeaponUpgrade(249, 23150020, 8404, 11051249)
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
    AllowWeaponUpgrade(352, 40000000, 0, 11051352)
    CraftDummyWeapon(353, 60400100, 40400100, 40000000)
    AllowWeaponUpgrade(353, 40010005, 8400, 11051353)
    CraftDummyWeapon(354, 60400200, 40400200, 40030003)
    AllowWeaponUpgrade(354, 40020008, 8401, 11051354)
    CraftDummyWeapon(355, 60400300, 40400300, 40000000)
    AllowWeaponUpgrade(355, 40030003, 8401, 11051355)
    CraftDummyWeapon(356, 60400500, 40400500, 40030003)
    AllowWeaponUpgrade(356, 40050010, 8402, 11051356)
    CraftDummyWeapon(357, 60410000, 40410000, 40020008)
    AllowWeaponUpgrade(357, 41000010, 8402, 11051357)
    CraftDummyWeapon(358, 60410100, 40410100, 41000010)
    AllowWeaponUpgrade(358, 41010015, 8404, 11051358)
    CraftDummyWeapon(359, 60410200, 40410200, 41000010)
    AllowWeaponUpgrade(359, 41020015, 8404, 11051359)
    CraftDummyWeapon(360, 60410300, 40410300, 41000010)
    AllowWeaponUpgrade(360, 41030010, 8404, 11051360)
    CraftDummyWeapon(361, 60410400, 40410400, 41000010)
    AllowWeaponUpgrade(361, 41040010, 8404, 11051361)
    CraftDummyWeapon(362, 60410600, 40410600, 40010005)
    AllowWeaponUpgrade(362, 41060008, 8404, 11051362)
    CraftDummyWeapon(363, 60410700, 40410700, 41010015)
    AllowWeaponUpgrade(363, 41070010, 8404, 11051363)
    CraftDummyWeapon(364, 60420000, 40420000, 42010008)
    AllowWeaponUpgrade(364, 42000010, 8404, 11051364)
    CraftDummyWeapon(365, 60420100, 40420100, 42040014)
    AllowWeaponUpgrade(365, 42010008, 8404, 11051365)
    CraftDummyWeapon(366, 60420300, 40420300, 42040014)
    AllowWeaponUpgrade(366, 42030010, 8404, 11051366)
    CraftDummyWeapon(367, 60420400, 40420400, 41000010)
    AllowWeaponUpgrade(367, 42040014, 8403, 11051367)
    CraftDummyWeapon(368, 60430000, 40430000, 41060008)
    AllowWeaponUpgrade(368, 43000010, 8402, 11051368)
    CraftDummyWeapon(369, 60430200, 40430200, 43000010)
    AllowWeaponUpgrade(369, 43020013, 8403, 11051369)
    CraftDummyWeapon(370, 60430300, 40430300, 43020013)
    AllowWeaponUpgrade(370, 43030016, 8404, 11051370)
    CraftDummyWeapon(371, 60430500, 40430500, 43030016)
    AllowWeaponUpgrade(371, 43050010, 8404, 11051371)
    CraftDummyWeapon(372, 60430600, 40430600, 43020013)
    AllowWeaponUpgrade(372, 43060010, 8404, 11051372)
    CraftDummyWeapon(373, 60430800, 40430800, 43030016)
    AllowWeaponUpgrade(373, 43080018, 8404, 11051373)
    CraftDummyWeapon(374, 60431100, 40431100, 43030016)
    AllowWeaponUpgrade(374, 43110010, 8404, 11051374)
    CraftDummyWeapon(375, 60440000, 40440000, 43080018)
    AllowWeaponUpgrade(375, 44000020, 8404, 11051375)
    CraftDummyWeapon(376, 60440100, 40440100, 43080018)
    AllowWeaponUpgrade(376, 44010010, 8404, 11051376)
    # endregion

    # Monitor possession of Smith's Hammers for recipe appearance.
    # region Smith's Hammer possession
    ShowSmithsHammerRecipe(
        0, 0, SmithsHammers.NoviceSmithsHammer, Flags.ShowNoviceSmithsHammer
    )
    ShowSmithsHammerRecipe(
        1, SmithsHammers.NoviceSmithsHammer, SmithsHammers.ApprenticeSmithsHammer, Flags.ShowApprenticeSmithsHammer
    )
    ShowSmithsHammerRecipe(
        2, SmithsHammers.ApprenticeSmithsHammer, SmithsHammers.JourneymanSmithsHammer, Flags.ShowJourneymanSmithsHammer
    )
    ShowSmithsHammerRecipe(
        3, SmithsHammers.JourneymanSmithsHammer, SmithsHammers.ExpertSmithsHammer, Flags.ShowExpertSmithsHammer
    )
    ShowSmithsHammerRecipe(
        4, SmithsHammers.ExpertSmithsHammer, SmithsHammers.MasterSmithsHammer, Flags.ShowMasterSmithsHammer
    )
    # endregion
    # endregion


@NeverRestart(Flags.CraftDummyWeaponEvent)
def CraftDummyWeapon(_, dummy_weapon_id: int, weapon_item_lot: int, previous_weapon: int):
    """Wait for player to obtain a crafted dummy weapon, then remove it, remove the previous "required" weapon in
    the recipe (if nonzero), and award the real item."""
    IfPlayerHasWeapon(0, dummy_weapon_id)
    RemoveWeaponFromPlayer(dummy_weapon_id, 1)
    AwardItemLot(weapon_item_lot)
    if previous_weapon != 0:
        RemoveWeaponFromPlayer(previous_weapon, 1)  # let's hope the count field actually works now :/
    return RESTART


@RestartOnRest(Flags.AllowWeaponUpgradeEvent)
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


@NeverRestart(Flags.ShowSmithsHammerRecipe)
def ShowSmithsHammerRecipe(_, required_hammer_id: int, hammer_id: int, possession_flag: int):
    DisableFlag(possession_flag)
    SkipLinesIfEqual(1, required_hammer_id, 0)
    IfPlayerHasGood(1, required_hammer_id)
    IfPlayerDoesNotHaveGood(1, hammer_id)
    IfConditionTrue(0, 1)
    EnableFlag(possession_flag)
    SkipLinesIfEqual(1, required_hammer_id, 0)
    IfPlayerDoesNotHaveGood(-1, required_hammer_id)
    IfPlayerHasGood(-1, hammer_id)
    IfConditionTrue(0, -1)
    return RESTART