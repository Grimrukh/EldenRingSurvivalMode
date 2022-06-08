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

    # region TODO: Debugging. Remove for release.
    # DisableFlagRange((18001000, 18001999))
    # AwardItemLot(600)
    # AwardItemLot(610)
    # AwardItemLot(700)
    # AwardItemLot(40240000)  # Torch
    # AwardItemLot(300)  # Torch
    # AddSpecialEffect(PLAYER, 3999 9)  # SUPER DEFENSE
    # DEBUG_ResetDiseases()
    # DEBUG_GetAllMaps()
    # DEBUG_GetDectusMedallions()
    # DEBUG_AlternateFlag()
    # endregion

    # region SURVIVAL
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
    # endregion


@NeverRestart(Flags.GrowingHunger)
def GrowingHunger():
    """Hunger ticks up every 60 seconds."""

    # Hunger cannot grow while Draught of the Undining is active (or hunger is at max).
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.DraughtOfSatiation)
    IfPlayerDoesNotHaveSpecialEffect(1, SurvivalEffects.Hunger15)
    IfConditionTrue(0, 1)

    for tick_flag in (Flags.HungerTick1, Flags.HungerTick2, Flags.HungerTick3, Flags.HungerTick4, Flags.HungerTick5):
        SkipLinesIfFlagOn(5, tick_flag)
        SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.LimgraveDisease)
        Wait(25.0)  # 16% faster
        SkipLines(1)
        Wait(30.0)
        EnableFlag(tick_flag)

    # Final tick.
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.LimgraveDisease)
    Wait(25.0)  # 16% faster
    SkipLines(1)
    Wait(30.0)

    DisableFlagRange((Flags.HungerTick1, Flags.HungerTick5))

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

    for tick_flag in (Flags.ThirstTick1, Flags.ThirstTick2, Flags.ThirstTick3, Flags.ThirstTick4, Flags.ThirstTick5):
        SkipLinesIfFlagOn(5, tick_flag)
        SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.LimgraveDisease)
        Wait(40.0)  # 20% faster
        SkipLines(1)
        Wait(50.0)
        EnableFlag(tick_flag)

    # Final tick.
    SkipLinesIfPlayerDoesNotHaveSpecialEffect(2, SurvivalEffects.LimgraveDisease)
    Wait(40.0)  # 20% faster
    SkipLines(1)
    Wait(50.0)

    DisableFlagRange((Flags.ThirstTick1, Flags.ThirstTick5))

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
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.BoiledCrab)
    IfConditionFalse(0, -1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BerryMedley1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BerryMedley2)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BerryMedley3)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.MushroomStew)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.GreatBoneBroth)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BoiledCrab)
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
    IfPlayerHasSpecialEffect(-1, SurvivalEffects.BoiledPrawn)
    IfConditionFalse(0, -1)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BerryMedley3)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.MeltedMushroomStew)
    IfPlayerHasSpecialEffect(-2, SurvivalEffects.BoiledPrawn)
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
