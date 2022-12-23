"""New common EMEVD events for Elden Ring Survival Mode.

Kept separate to `common.evs.py` because I will probably regenerate the vanilla events in that file from time to time as
my understanding of ER EMEVD instructions becomes better.
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .survival_enums import *
from .survival_goods import *


@ContinueOnRest(0)
def Constructor():
    """Will be merged with vanilla Common."""

    # region DISEASES
    # region Disease affliction
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
    # endregion


@ContinueOnRest(Flags.GetDiseaseOverworld)
def GetDiseaseOverworld(
    _, disease_effect: int, location_flag: Flag, had_once_flag: Flag, had_twice_flag: Flag, item: int, item_lot: int
):
    IfPlayerHasGood(7, item)
    SkipLinesIfConditionFalse(2, 7)  # just re-apply effect and end
    AddSpecialEffect(PLAYER, disease_effect)
    End()

    EndIfFlagEnabled(had_twice_flag)

    # Avoid triggering multiple times when raw meat is eaten.
    IfPlayerDoesNotHaveSpecialEffect(6, SurvivalEffects.RawSteak)
    IfPlayerDoesNotHaveSpecialEffect(6, SurvivalEffects.RawLiverSteak)
    IfConditionTrue(0, 6)

    IfFlagEnabled(1, location_flag)
    IfPlayerHasSpecialEffect(-3, SurvivalEffects.RawSteak)
    IfPlayerHasSpecialEffect(-3, SurvivalEffects.RawLiverSteak)
    IfAttackedWithDamageType(-3, PLAYER, -1, DamageType.Unspecified)
    IfConditionTrue(1, -3)
    IfPlayerDoesNotHaveSpecialEffect(1, disease_effect)
    IfFlagDisabled(1, Flags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.DiseaseRollLock)
    DisableFlagRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))
    EnableRandomFlagInRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))

    IfFlagEnabled(-2, Flags.DiseaseRollFirst)
    IfFlagDisabled(2, had_once_flag)
    IfFlagEnabled(2, Flags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(Flags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(Flags.DiseaseRollLock)

    AwardItemLot(item_lot)  # disease indicator
    AddSpecialEffect(PLAYER, disease_effect)

    SkipLinesIfFlagEnabled(2, had_once_flag)
    EnableFlag(had_once_flag)
    SkipLines(1)
    EnableFlag(had_twice_flag)


@ContinueOnRest(Flags.GetDiseaseLegacyDungeon)
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

    EndIfFlagEnabled(had_twice_flag)

    # Avoid triggering multiple times when raw meat is eaten.
    IfPlayerDoesNotHaveSpecialEffect(6, SurvivalEffects.RawSteak)
    IfPlayerDoesNotHaveSpecialEffect(6, SurvivalEffects.RawLiverSteak)
    IfConditionTrue(0, 6)

    IfInsideMap(1, (a, b, c, d))
    IfPlayerHasSpecialEffect(-3, SurvivalEffects.RawSteak)
    IfPlayerHasSpecialEffect(-3, SurvivalEffects.RawLiverSteak)
    IfAttackedWithDamageType(-3, PLAYER, -1, DamageType.Unspecified)
    IfConditionTrue(1, -3)
    IfPlayerDoesNotHaveSpecialEffect(1, disease_effect)
    IfFlagDisabled(1, Flags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.DiseaseRollLock)
    DisableFlagRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))
    EnableRandomFlagInRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))

    IfFlagEnabled(-2, Flags.DiseaseRollFirst)
    IfFlagDisabled(2, had_once_flag)
    IfFlagEnabled(2, Flags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(Flags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(Flags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, disease_effect)
    AwardItemLot(item_lot)  # disease indicator

    SkipLinesIfFlagEnabled(2, had_once_flag)
    EnableFlag(had_once_flag)
    End()
    EnableFlag(had_twice_flag)


# --- SPECIFIC DISEASE EVENTS ---


@ContinueOnRest(Flags.GetDiseaseSiofra)
def GetDiseaseSiofra():
    IfPlayerHasGood(7, DiseaseIndicators.SiofraDisease)
    SkipLinesIfConditionFalse(2, 7)  # just re-apply disease effect and end
    AddSpecialEffect(PLAYER, SurvivalEffects.SiofraDisease)
    End()

    EndIfFlagEnabled(Flags.SiofraDiseaseTwice)

    # Avoid triggering multiple times when raw meat is eaten.
    IfPlayerDoesNotHaveSpecialEffect(6, SurvivalEffects.RawSteak)
    IfPlayerDoesNotHaveSpecialEffect(6, SurvivalEffects.RawLiverSteak)
    IfConditionTrue(0, 6)

    IfInsideMap(-1, SIOFRA_RIVER)
    IfInsideMap(-1, SIOFRA_RIVER_START)
    IfConditionTrue(1, -1)
    IfPlayerHasSpecialEffect(-3, SurvivalEffects.RawSteak)
    IfPlayerHasSpecialEffect(-3, SurvivalEffects.RawLiverSteak)
    IfAttackedWithDamageType(-3, PLAYER, -1, DamageType.Unspecified)
    IfConditionTrue(1, -3)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.SiofraDisease)
    IfFlagDisabled(1, Flags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.DiseaseRollLock)
    DisableFlagRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))
    EnableRandomFlagInRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))

    IfFlagEnabled(-2, Flags.DiseaseRollFirst)
    IfFlagDisabled(2, Flags.SiofraDiseaseOnce)
    IfFlagEnabled(2, Flags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(Flags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(Flags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, SurvivalEffects.SiofraDisease)
    AwardItemLot(DiseaseItemLots.SiofraDisease)

    SkipLinesIfFlagEnabled(2, Flags.SiofraDiseaseOnce)
    EnableFlag(Flags.SiofraDiseaseOnce)
    End()
    EnableFlag(Flags.SiofraDiseaseTwice)


@ContinueOnRest(Flags.GetDiseaseAinsel)
def GetDiseaseAinsel():
    IfPlayerHasGood(7, DiseaseIndicators.AinselDisease)
    SkipLinesIfConditionFalse(2, 7)  # just re-apply disease effect and end
    AddSpecialEffect(PLAYER, SurvivalEffects.AinselDisease)
    End()

    EndIfFlagEnabled(Flags.AinselDiseaseTwice)

    # Avoid triggering multiple times when raw meat is eaten.
    IfPlayerDoesNotHaveSpecialEffect(6, SurvivalEffects.RawSteak)
    IfPlayerDoesNotHaveSpecialEffect(6, SurvivalEffects.RawLiverSteak)
    IfConditionTrue(0, 6)

    IfInsideMap(1, AINSEL_RIVER)
    IfPlayerHasSpecialEffect(-3, SurvivalEffects.RawSteak)
    IfPlayerHasSpecialEffect(-3, SurvivalEffects.RawLiverSteak)
    IfAttackedWithDamageType(-3, PLAYER, -1, DamageType.Unspecified)
    IfConditionTrue(1, -3)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.AinselDisease)
    IfFlagDisabled(1, Flags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.DiseaseRollLock)
    DisableFlagRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))
    EnableRandomFlagInRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))

    IfFlagEnabled(-2, Flags.DiseaseRollFirst)
    IfFlagDisabled(2, Flags.AinselDiseaseOnce)
    IfFlagEnabled(2, Flags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(Flags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(Flags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, SurvivalEffects.AinselDisease)
    AwardItemLot(DiseaseItemLots.AinselDisease)

    SkipLinesIfFlagEnabled(2, Flags.AinselDiseaseOnce)
    EnableFlag(Flags.AinselDiseaseOnce)
    End()
    EnableFlag(Flags.AinselDiseaseTwice)


@ContinueOnRest(Flags.GetDiseaseDeeprootAstel)
def GetDiseaseDeeprootAstel():
    IfPlayerHasGood(7, DiseaseIndicators.DeeprootDisease)
    SkipLinesIfConditionFalse(2, 7)  # just re-apply disease effect and end
    AddSpecialEffect(PLAYER, SurvivalEffects.DeeprootDisease)
    End()

    EndIfFlagEnabled(Flags.DeeprootDiseaseTwice)

    # Avoid triggering multiple times when raw meat is eaten.
    IfPlayerDoesNotHaveSpecialEffect(6, SurvivalEffects.RawSteak)
    IfPlayerDoesNotHaveSpecialEffect(6, SurvivalEffects.RawLiverSteak)
    IfConditionTrue(0, 6)

    IfInsideMap(-1, DEEPROOT_DEPTHS)
    IfInsideMap(-1, ASTEL_ARENA)
    IfConditionTrue(1, -1)
    IfPlayerHasSpecialEffect(-3, SurvivalEffects.RawSteak)
    IfPlayerHasSpecialEffect(-3, SurvivalEffects.RawLiverSteak)
    IfAttackedWithDamageType(-3, PLAYER, -1, DamageType.Unspecified)
    IfConditionTrue(1, -3)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.DeeprootDisease)
    IfFlagDisabled(1, Flags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.DiseaseRollLock)
    DisableFlagRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))
    EnableRandomFlagInRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))

    IfFlagEnabled(-2, Flags.DiseaseRollFirst)
    IfFlagDisabled(2, Flags.DeeprootDiseaseOnce)
    IfFlagEnabled(2, Flags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(Flags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(Flags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, SurvivalEffects.DeeprootDisease)
    AwardItemLot(DiseaseItemLots.DeeprootDisease)

    SkipLinesIfFlagEnabled(2, Flags.DeeprootDiseaseOnce)
    EnableFlag(Flags.DeeprootDiseaseOnce)
    End()
    EnableFlag(Flags.DeeprootDiseaseTwice)


@ContinueOnRest(Flags.GetDiseaseRadahn)
def GetDiseaseRadahn():
    """Only afflicted by Radahn himself."""
    IfPlayerHasGood(7, DiseaseIndicators.RadahnDisease)
    SkipLinesIfConditionFalse(2, 7)  # just re-apply disease effect and end
    AddSpecialEffect(PLAYER, SurvivalEffects.RadahnDisease)
    End()

    EndIfFlagEnabled(Flags.RadahnDiseaseTwice)

    # This disease does NOT trigger when eating raw meat. You are magically safe from raw meat diseases if you eat
    # them while fighting Radahn.
    IfAttackedWithDamageType(1, PLAYER, VanillaCharacters.Radahn, DamageType.Unspecified)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.RadahnDisease)
    IfFlagDisabled(1, Flags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.DiseaseRollLock)
    DisableFlagRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))
    EnableRandomFlagInRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))

    IfFlagEnabled(-2, Flags.DiseaseRollFirst)
    IfFlagDisabled(2, Flags.RadahnDiseaseOnce)
    IfFlagEnabled(2, Flags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(Flags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(Flags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, SurvivalEffects.RadahnDisease)
    AwardItemLot(DiseaseItemLots.RadahnDisease)

    SkipLinesIfFlagEnabled(2, Flags.RadahnDiseaseOnce)
    EnableFlag(Flags.RadahnDiseaseOnce)
    End()
    EnableFlag(Flags.RadahnDiseaseTwice)


# --- GENERIC DUNGEON DISEASES ---


@ContinueOnRest(Flags.GetDiseaseCatacombs)
def GetDiseaseCatacombs():
    IfPlayerHasGood(7, DiseaseIndicators.CatacombsDisease)
    SkipLinesIfConditionFalse(2, 7)  # just re-apply disease effect and end
    AddSpecialEffect(PLAYER, SurvivalEffects.CatacombsDisease)
    End()

    EndIfFlagEnabled(Flags.CatacombsDiseaseTwice)

    # Avoid triggering multiple times when raw meat is eaten.
    IfPlayerDoesNotHaveSpecialEffect(6, SurvivalEffects.RawSteak)
    IfPlayerDoesNotHaveSpecialEffect(6, SurvivalEffects.RawLiverSteak)
    IfConditionTrue(0, 6)

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
    IfPlayerHasSpecialEffect(-3, SurvivalEffects.RawSteak)
    IfPlayerHasSpecialEffect(-3, SurvivalEffects.RawLiverSteak)
    IfAttackedWithDamageType(-3, PLAYER, -1, DamageType.Unspecified)
    IfConditionTrue(1, -3)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.CatacombsDisease)
    IfFlagDisabled(1, Flags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.DiseaseRollLock)
    DisableFlagRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))
    EnableRandomFlagInRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))

    IfFlagEnabled(-2, Flags.DiseaseRollFirst)
    IfFlagDisabled(2, Flags.CatacombsDiseaseOnce)
    IfFlagEnabled(2, Flags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(Flags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(Flags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, SurvivalEffects.CatacombsDisease)
    AwardItemLot(DiseaseItemLots.CatacombsDisease)

    SkipLinesIfFlagEnabled(2, Flags.CatacombsDiseaseOnce)
    EnableFlag(Flags.CatacombsDiseaseOnce)
    End()
    EnableFlag(Flags.CatacombsDiseaseTwice)


@ContinueOnRest(Flags.GetDiseaseCaves)
def GetDiseaseCaves():
    IfPlayerHasGood(7, DiseaseIndicators.CaveDisease)
    SkipLinesIfConditionFalse(2, 7)  # just re-apply disease effect and end
    AddSpecialEffect(PLAYER, SurvivalEffects.CaveDisease)
    End()

    EndIfFlagEnabled(Flags.CaveDiseaseTwice)

    # Avoid triggering multiple times when raw meat is eaten.
    IfPlayerDoesNotHaveSpecialEffect(6, SurvivalEffects.RawSteak)
    IfPlayerDoesNotHaveSpecialEffect(6, SurvivalEffects.RawLiverSteak)
    IfConditionTrue(0, 6)

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
    IfPlayerHasSpecialEffect(-3, SurvivalEffects.RawSteak)
    IfPlayerHasSpecialEffect(-3, SurvivalEffects.RawLiverSteak)
    IfAttackedWithDamageType(-3, PLAYER, -1, DamageType.Unspecified)
    IfConditionTrue(1, -3)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.CaveDisease)
    IfFlagDisabled(1, Flags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.DiseaseRollLock)
    DisableFlagRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))
    EnableRandomFlagInRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))

    IfFlagEnabled(-2, Flags.DiseaseRollFirst)
    IfFlagDisabled(2, Flags.CaveDiseaseOnce)
    IfFlagEnabled(2, Flags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(Flags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(Flags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, SurvivalEffects.CaveDisease)
    AwardItemLot(DiseaseItemLots.CaveDisease)

    SkipLinesIfFlagEnabled(2, Flags.CaveDiseaseOnce)
    EnableFlag(Flags.CaveDiseaseOnce)
    End()
    EnableFlag(Flags.CaveDiseaseTwice)


@ContinueOnRest(Flags.GetDiseaseTunnels)
def GetDiseaseTunnels():
    IfPlayerHasGood(7, DiseaseIndicators.TunnelDisease)
    SkipLinesIfConditionFalse(2, 7)  # just re-apply disease effect and end
    AddSpecialEffect(PLAYER, SurvivalEffects.TunnelDisease)
    End()

    EndIfFlagEnabled(Flags.TunnelDiseaseTwice)

    # Avoid triggering multiple times when raw meat is eaten.
    IfPlayerDoesNotHaveSpecialEffect(6, SurvivalEffects.RawSteak)
    IfPlayerDoesNotHaveSpecialEffect(6, SurvivalEffects.RawLiverSteak)
    IfConditionTrue(0, 6)

    IfInsideMap(-1, MORNE_TUNNEL)
    IfInsideMap(-1, LIMGRAVE_TUNNELS)
    IfInsideMap(-1, RAYA_LUCARIA_CRYSTAL_TUNNEL)
    IfInsideMap(-1, OLD_ALTUS_TUNNEL)
    IfInsideMap(-1, ALTUS_TUNNEL)
    IfInsideMap(-1, GAEL_TUNNEL)
    IfInsideMap(-1, SELLIA_CRYSTAL_TUNNEL)
    IfInsideMap(-1, YELOUGH_ANIX_TUNNEL)
    IfConditionTrue(1, -1)
    IfPlayerHasSpecialEffect(-3, SurvivalEffects.RawSteak)
    IfPlayerHasSpecialEffect(-3, SurvivalEffects.RawLiverSteak)
    IfAttackedWithDamageType(-3, PLAYER, -1, DamageType.Unspecified)
    IfConditionTrue(1, -3)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.TunnelDisease)
    IfFlagDisabled(1, Flags.DiseaseRollLock)

    IfConditionTrue(0, 1)

    EnableFlag(Flags.DiseaseRollLock)
    DisableFlagRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))
    EnableRandomFlagInRange((Flags.DiseaseRollFirst, Flags.DiseaseRollLast))

    IfFlagEnabled(-2, Flags.DiseaseRollFirst)
    IfFlagDisabled(2, Flags.TunnelDiseaseOnce)
    IfFlagEnabled(2, Flags.DiseaseRollSecond)
    IfConditionTrue(-2, 2)

    SkipLinesIfConditionTrue(2, -2)
    DisableFlag(Flags.DiseaseRollLock)
    Restart()  # no proc, try again next time

    DisableFlag(Flags.DiseaseRollLock)

    AddSpecialEffect(PLAYER, SurvivalEffects.TunnelDisease)
    AwardItemLot(DiseaseItemLots.TunnelDisease)

    SkipLinesIfFlagEnabled(2, Flags.TunnelDiseaseOnce)
    EnableFlag(Flags.TunnelDiseaseOnce)
    End()
    EnableFlag(Flags.TunnelDiseaseTwice)


@RestartOnRest(Flags.CaveDiseaseInDaylight)
def CaveDiseaseInDaylight():
    RemoveSpecialEffect(PLAYER, SurvivalEffects.CaveDiseaseDaylight)

    IfPlayerHasSpecialEffect(1, SurvivalEffects.CaveDisease)
    IfTimeOfDay(1, (6, 0, 0), (19, 0, 0))
    IfConditionTrue(0, 1)

    AddSpecialEffect(PLAYER, SurvivalEffects.CaveDiseaseDaylight)

    IfPlayerHasSpecialEffect(2, SurvivalEffects.CaveDisease)
    IfTimeOfDay(2, (6, 0, 0), (19, 0, 0))
    IfConditionFalse(0, 2)

    return RESTART


# --- DISEASE CURES ---


@ContinueOnRest(Flags.CureDisease)
def CureDisease(_, disease_effect: int, cure_effect: int, disease_item: int, cure_text: int):
    IfPlayerHasSpecialEffect(1, cure_effect)
    IfPlayerHasSpecialEffect(1, disease_effect)
    IfConditionTrue(0, 1)

    RemoveSpecialEffect(PLAYER, disease_effect)
    DisplayStatus(cure_text)
    RemoveGoodFromPlayer(disease_item, 99)

    IfPlayerDoesNotHaveSpecialEffect(0, cure_effect)
    return RESTART
