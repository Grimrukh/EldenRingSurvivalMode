"""INSTALLATION INSTRUCTIONS (for me):

- Run `install_evs()`, `generate_all_params()`, and `set_all_text()` here.
    - This will generate the final `common.emevd.dcx`, `item.msgbnd.dcx`, and `menu.msgbnd.dcx`.

TODO:
    - Sacred Tear crafting?

TODO (Notes for Player):
    - If you "infuse" a weapon (Heavy, Keen, Fire, etc.) then you will not be able to upgrade it. For now, it's
      recommended that you avoid infusion for playthroughs (or just clear the infusion when it's upgrade time).
    - When you craft a weapon upgrade, the crafting menu will not update until you change tabs or go out and back in.
      If you try to craft an "invalid" upgrade recipe (e.g., because you no longer have the required weapon but the menu
      has not refreshed), the ingredients you put into it will be wasted.
"""
import shutil
from pathlib import Path
from soulstruct.eldenring.events import EMEVD

from survival_params import generate_all_params
from survival_text import set_all_text


VANILLA_PATH = Path("C:/Steam/steamapps/common/ELDEN RING (Vanilla)/Game")
MODDING_PATH = Path("C:/Steam/steamapps/common/ELDEN RING (Modding)/Game")

DO_SURVIVAL = True
DO_WEAPON_TREE = True
DO_DISEASES = True
DIST_PATH = Path("../../dist/GAME (OPTIONS)")


def vanilla_common_emevd_to_evs():
    EMEVD(VANILLA_PATH / "event/common.emevd").write_evs(Path(__file__).parent / "common.evs.py")


def install_regulation():
    modded_regulation_path = Path(__file__).parent.parent / "regulation.bin"
    shutil.copy2(modded_regulation_path, MODDING_PATH / "regulation.bin")
    print("Copied modded `regulation.bin` to game directory.")


def install_evs():
    """Install Survival Mode common EMEVD."""
    this_dir = Path(__file__).parent
    common = EMEVD(this_dir / "common.evs.py")
    common_shared = EMEVD(this_dir / "common_shared.evs.py")
    common = common.merge(common_shared, merge_events=(0,))

    if DO_SURVIVAL:
        common_extra = EMEVD(this_dir / "common_survival.evs.py")
        common = common.merge(common_extra, merge_events=(0,))
        print("Merged survival EMEVD.")
    if DO_WEAPON_TREE:
        common_extra = EMEVD(this_dir / "common_weapons.evs.py")
        common = common.merge(common_extra, merge_events=(0,))
        print("Merged weapon tree EMEVD.")
    if DO_DISEASES:
        common_extra = EMEVD(this_dir / "common_diseases.evs.py")
        common = common.merge(common_extra, merge_events=(0,))
        print("Merged disease EMEVD.")

    # EVS for inspection
    common.write_evs(this_dir / "built_common.evs.py")

    # Game common
    common.dcx_magic = None
    common.write(MODDING_PATH / "event/common.emevd.dcx")

    # Copy to DIST_PATH
    dist_path = DIST_PATH
    dist_path /= "Survival ENABLED" if DO_SURVIVAL else "Survival DISABLED"
    dist_path /= "Weapon Tree ENABLED" if DO_WEAPON_TREE else "Weapon Tree DISABLED"
    dist_path /= "Diseases ENABLED" if DO_DISEASES else "Diseases DISABLED"
    shutil.copy2(MODDING_PATH / "event/common.emevd.dcx", dist_path / "event/common.emevd.dcx")


def install_all_evs_variants():
    global DO_SURVIVAL, DO_WEAPON_TREE, DO_DISEASES, DIST_PATH

    DO_SURVIVAL = True
    DO_WEAPON_TREE = DO_DISEASES = False
    install_evs()

    DO_WEAPON_TREE = True
    DO_SURVIVAL = DO_DISEASES = False
    install_evs()

    DO_DISEASES = True
    DO_SURVIVAL = DO_WEAPON_TREE = False
    install_evs()

    DO_SURVIVAL = DO_WEAPON_TREE = True
    DO_DISEASES = False
    install_evs()

    DO_SURVIVAL = DO_DISEASES = True
    DO_WEAPON_TREE = False
    install_evs()

    DO_WEAPON_TREE = DO_DISEASES = True
    DO_SURVIVAL = False
    install_evs()

    DO_SURVIVAL = DO_WEAPON_TREE = DO_DISEASES = True
    install_evs()


def get_vanilla_common_emevd():
    """Just converts vanilla common EMEVD to EVS in repo, into which my add-on scripts can be merged."""


if __name__ == '__main__':
    # install_all_evs_variants()

    install_evs()
    # generate_all_params()
    # set_all_text()
    print("Full SurvivalMode Python installation complete. (Now use Yapped to convert CSVs to `regulation.bin`.")
