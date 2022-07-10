"""New common EMEVD events for Elden Ring Survival Mode.

Kept separate to `common.evs.py` because I will probably regenerate the vanilla events in that file from time to time as
my understanding of ER EMEVD instructions becomes better.
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
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

    # DARKNESS
    # region Time of Day / Torch Monitors
    MonitorHour(0, 0, Flags.Hour0)
    MonitorHour(1, 1, Flags.Hour1)
    MonitorHour(2, 2, Flags.Hour2)
    MonitorHour(3, 3, Flags.Hour3)
    MonitorHour(4, 4, Flags.Hour4)
    MonitorHour(5, 5, Flags.Hour5)
    MonitorHour(6, 6, Flags.Hour6)
    MonitorHour(7, 7, Flags.Hour7)
    MonitorHour(8, 8, Flags.Hour8)
    MonitorHour(9, 9, Flags.Hour9)
    MonitorHour(10, 10, Flags.Hour10)
    MonitorHour(11, 11, Flags.Hour11)
    MonitorHour(12, 12, Flags.Hour12)
    MonitorHour(13, 13, Flags.Hour13)
    MonitorHour(14, 14, Flags.Hour14)
    MonitorHour(15, 15, Flags.Hour15)
    MonitorHour(16, 16, Flags.Hour16)
    MonitorHour(17, 17, Flags.Hour17)
    MonitorHour(18, 18, Flags.Hour18)
    MonitorHour(19, 19, Flags.Hour19)
    MonitorHour(20, 20, Flags.Hour20)
    MonitorHour(21, 21, Flags.Hour21)
    MonitorHour(22, 22, Flags.Hour22)
    MonitorHour(23, 23, Flags.Hour23)
    MonitorPlayerTorch()
    # endregion

    # SHARED
    # region Map area checks
    MonitorInLimgrave()
    MonitorInLiurnia()
    MonitorInCaelid()
    MonitorInAltus()
    MonitorInMtGelmir()
    MonitorInMountaintops()
    MonitorInGenericDungeon()
    MonitorInLegacyDungeon()
    MonitorOutdoors()
    # endregion

    # DEBUG_Hour18()
    # DEBUG_AlternateFlag()


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
    IfFlagDisabled(1, Flags.PlayerInLegacyDungeon)
    IfFlagDisabled(1, Flags.PlayerInGenericDungeon)

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
    IfFlagDisabled(2, Flags.PlayerInLegacyDungeon)
    IfFlagDisabled(2, Flags.PlayerInGenericDungeon)

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
    IfFlagDisabled(1, Flags.PlayerInLegacyDungeon)
    IfFlagDisabled(1, Flags.PlayerInGenericDungeon)

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
    IfFlagDisabled(2, Flags.PlayerInLegacyDungeon)
    IfFlagDisabled(2, Flags.PlayerInGenericDungeon)

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
    IfFlagDisabled(1, Flags.PlayerInLegacyDungeon)
    IfFlagDisabled(1, Flags.PlayerInGenericDungeon)

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
    IfFlagDisabled(2, Flags.PlayerInLegacyDungeon)
    IfFlagDisabled(2, Flags.PlayerInGenericDungeon)

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
    IfFlagDisabled(1, Flags.PlayerInLegacyDungeon)
    IfFlagDisabled(1, Flags.PlayerInGenericDungeon)

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
    IfFlagDisabled(2, Flags.PlayerInLegacyDungeon)
    IfFlagDisabled(2, Flags.PlayerInGenericDungeon)

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
    IfFlagDisabled(1, Flags.PlayerInLegacyDungeon)
    IfFlagDisabled(1, Flags.PlayerInGenericDungeon)

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
    IfFlagDisabled(2, Flags.PlayerInLegacyDungeon)
    IfFlagDisabled(2, Flags.PlayerInGenericDungeon)

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
    IfFlagDisabled(1, Flags.PlayerInLegacyDungeon)
    IfFlagDisabled(1, Flags.PlayerInGenericDungeon)

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
    IfFlagDisabled(2, Flags.PlayerInLegacyDungeon)
    IfFlagDisabled(2, Flags.PlayerInGenericDungeon)

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


@NeverRestart(Flags.MonitorOutdoors)
def MonitorOutdoors():
    """Enables a flag when player is outdoors, for darkness."""
    DisableFlag(Flags.PlayerIsOutdoors)

    IfFlagEnabled(-1, Flags.PlayerInLimgrave)
    IfFlagEnabled(-1, Flags.PlayerInLiurnia)
    IfFlagEnabled(-1, Flags.PlayerInCaelid)
    IfFlagEnabled(-1, Flags.PlayerInAltus)
    IfFlagEnabled(-1, Flags.PlayerInMtGelmir)
    IfFlagEnabled(-1, Flags.PlayerInMountaintops)
    IfInsideMap(-1, STORMVEIL_CASTLE)
    IfInsideMap(-1, RAYA_LUCARIA)
    IfInsideMap(-1, VOLCANO_MANOR)
    IfInsideMap(-1, LEYNDELL_ROYAL_CAPITAL)
    IfInsideMap(-1, LEYNDELL_ASHEN_CAPITAL)
    IfInsideMap(-1, HALIGTREE)
    IfInsideMap(-1, CRUMBLING_FARUM_AZULA)
    # Not Sewers, Siofra, Ainsel, or Mohgwyn.

    IfConditionTrue(0, -1)

    EnableFlag(Flags.PlayerIsOutdoors)

    IfFlagEnabled(-2, Flags.PlayerInLimgrave)
    IfFlagEnabled(-2, Flags.PlayerInLiurnia)
    IfFlagEnabled(-2, Flags.PlayerInCaelid)
    IfFlagEnabled(-2, Flags.PlayerInAltus)
    IfFlagEnabled(-2, Flags.PlayerInMtGelmir)
    IfFlagEnabled(-2, Flags.PlayerInMountaintops)
    IfInsideMap(-2, STORMVEIL_CASTLE)
    IfInsideMap(-2, RAYA_LUCARIA)
    IfInsideMap(-2, VOLCANO_MANOR)
    IfInsideMap(-2, LEYNDELL_ROYAL_CAPITAL)
    IfInsideMap(-2, LEYNDELL_ASHEN_CAPITAL)
    IfInsideMap(-2, HALIGTREE)
    IfInsideMap(-2, CRUMBLING_FARUM_AZULA)
    # Not Sewers, Siofra, Ainsel, or Mohgwyn.

    IfConditionFalse(0, -2)

    return RESTART


@NeverRestart(Flags.MonitorHour)
def MonitorHour(_, hour: uchar, hour_flag: int):
    DisableFlag(hour_flag)

    IfTimeOfDay(0, (hour, 0, 0), (hour, 59, 59))
    DisableFlagRange((Flags.Hour0, Flags.Hour23))
    EnableFlag(hour_flag)

    # Wait for it to NOT be this hour before restarting to check again.
    IfTimeOfDay(1, (hour, 0, 0), (hour, 59, 59))
    IfConditionFalse(0, 1)
    Wait(1.0)
    return RESTART


@NeverRestart(Flags.MonitorPlayerTorch)
def MonitorPlayerTorch():
    """Simply monitors Torch SpEffect 415."""
    DisableFlag(Flags.PlayerHasTorch)
    IfPlayerHasSpecialEffect(0, 415)
    EnableFlag(Flags.PlayerHasTorch)
    IfPlayerDoesNotHaveSpecialEffect(0, 415)
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


@NeverRestart(15003996)
def DEBUG_AlternateFlag():
    # 85
    DisableFlag(19000000)
    EnableFlag(19000001)
    DisableFlag(19000002)
    EnableFlag(19000003)
    DisableFlag(19000004)
    EnableFlag(19000005)
    DisableFlag(19000006)
    EnableFlag(19000007)

    Wait(10.0)
    DisplayBanner(BannerType.BloodyFingerVanquished)
    # 170
    EnableFlag(19000000)
    DisableFlag(19000001)
    EnableFlag(19000002)
    DisableFlag(19000003)
    EnableFlag(19000004)
    DisableFlag(19000005)
    EnableFlag(19000006)
    DisableFlag(19000007)
    Wait(10.0)
    return RESTART


@NeverRestart(15003995)
def DEBUG_Hour18():
    Await(FlagEnabled(Flags.Hour20))
    DisplayBanner(BannerType.BloodyFingerVanquished)
    Wait(5.0)
    return RESTART
