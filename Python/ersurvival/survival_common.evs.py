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
    """TODO: Merge with vanilla common."""

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
    )
    GetDiseaseOverworld(
        1,
        SurvivalEffects.LiurniaToxin,
        SurvivalFlags.PlayerInLiurnia,
        SurvivalFlags.LiurniaDiseaseOnce,
        SurvivalFlags.LiurniaDiseaseTwice,
    )
    GetDiseaseOverworld(
        2,
        SurvivalEffects.CaelidParasite,
        SurvivalFlags.PlayerInCaelid,
        SurvivalFlags.CaelidDiseaseOnce,
        SurvivalFlags.CaelidDiseaseTwice,
    )
    GetDiseaseOverworld(
        3,
        SurvivalEffects.AltusFever,
        SurvivalFlags.PlayerInAltus,
        SurvivalFlags.AltusDiseaseOnce,
        SurvivalFlags.AltusDiseaseTwice,
    )
    GetDiseaseOverworld(
        4,
        SurvivalEffects.MtGelmirPlague,
        SurvivalFlags.PlayerInMtGelmir,
        SurvivalFlags.MtGelmirDiseaseOnce,
        SurvivalFlags.MtGelmirDiseaseTwice,
    )
    GetDiseaseOverworld(
        5,
        SurvivalEffects.MountaintopsParasite,
        SurvivalFlags.PlayerInMountaintops,
        SurvivalFlags.MountaintopsDiseaseOnce,
        SurvivalFlags.MountaintopsDiseaseTwice,
    )

    GetDiseaseLegacyDungeon(
        0,
        SurvivalEffects.StormveilPlague,
        10, 0, 0, 0,  # STORMVEIL_CASTLE
        SurvivalFlags.StormveilDiseaseOnce,
        SurvivalFlags.StormveilDiseaseTwice,
    )
    GetDiseaseLegacyDungeon(
        1,
        SurvivalEffects.RayaLucariaToxin,
        14, 0, 0, 0,  # RAYA_LUCARIA
        SurvivalFlags.RayaLucariaDiseaseOnce,
        SurvivalFlags.RayaLucariaDiseaseTwice,
    )
    GetDiseaseLegacyDungeon(
        2,
        SurvivalEffects.VolcanoManorToxin,
        16, 0, 0, 0,  # VOLCANO_MANOR (does not matter if you're in the no-attack zone)
        SurvivalFlags.VolcanoManorDiseaseOnce,
        SurvivalFlags.VolcanoManorDiseaseTwice,
    )
    GetDiseaseLegacyDungeon(
        3,
        SurvivalEffects.LeyndellPlague,
        11, 0, 0, 0,  # LEYNDELL_ROYAL_CAPITAL (no disease in Ashen Capital)
        SurvivalFlags.LeyndellDiseaseOnce,
        SurvivalFlags.LeyndellDiseaseTwice,
    )
    GetDiseaseLegacyDungeon(
        4,
        SurvivalEffects.SewersParasite,
        35, 0, 0, 0,  # SHUNNING_GROUNDS
        SurvivalFlags.SewersDiseaseOnce,
        SurvivalFlags.SewersDiseaseTwice,
    )
    GetDiseaseLegacyDungeon(
        5,
        SurvivalEffects.HaligtreePlague,
        15, 0, 0, 0,  # HALIGTREE
        SurvivalFlags.HaligtreeDiseaseOnce,
        SurvivalFlags.HaligtreeDiseaseTwice,
    )
    GetDiseaseLegacyDungeon(
        6,
        SurvivalEffects.FarumAzulaFever,
        13, 0, 0, 0,  # CRUMBLING_FARUM_AZULA
        SurvivalFlags.FarumAzulaDiseaseOnce,
        SurvivalFlags.FarumAzulaDiseaseTwice,
    )
    GetDiseaseLegacyDungeon(
        7,
        SurvivalEffects.MohgwynFever,
        12, 5, 0, 0,  # MOHGWYN_PALACE
        SurvivalFlags.MohgwynDiseaseOnce,
        SurvivalFlags.MohgwynDiseaseTwice,
    )

    GetDiseaseSiofra()
    GetDiseaseAinsel()
    GetDiseaseDeeprootAstel()
    GetDiseaseRadahn()

    GetDiseaseCatacombs()
    GetDiseaseCaves()
    GetDiseaseTunnels()

    # TODO: Pure Scarlet Rot check.

    # Disease cure checks
    CurePlague()
    CureToxin()
    CureFever()
    CureParasite()
    CurePureScarletRot()


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
    """TODO"""


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
def GetDiseaseOverworld(_, disease_effect: int, location_flag: Flag, had_once_flag: Flag, had_twice_flag: Flag):
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

    SkipLinesIfFlagOn(2, had_once_flag)
    EnableFlag(had_once_flag)
    End()
    EnableFlag(had_twice_flag)


@NeverRestart(SurvivalFlags.GetDiseaseLegacyDungeon)
def GetDiseaseLegacyDungeon(
    _, disease_effect: int, a: int, b: int, c: int, d: int, had_once_flag: Flag, had_twice_flag: Flag
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

    SkipLinesIfFlagOn(2, SurvivalFlags.CatacombsDiseaseOnce)
    EnableFlag(SurvivalFlags.CatacombsDiseaseOnce)
    End()
    EnableFlag(SurvivalFlags.CatacombsDiseaseTwice)


@NeverRestart(SurvivalFlags.GetDiseaseCaves)
def GetDiseaseCaves():
    EndIfFlagOn(SurvivalFlags.CavesDiseaseTwice)

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


@RestartOnRest(SurvivalFlags.MonitorTimeFlag)
def MonitorTimeFlag():
    """Tracks time in increments of thirty minutes, between midnight and midday."""

    # TODO: I've enlisted JZ to find a way to read the time of day directly from memory.

    ClearEventValue(SurvivalFlags.TimeEventValue, 8)

    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 0, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
    IfTimeOfDay(0, (0, 30, 0), (23, 59, 0))
    IncrementEventValue(SurvivalFlags.TimeEventValue, 8, 48)
