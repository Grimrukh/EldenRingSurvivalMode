"""INSTALLATION INSTRUCTIONS (for me):

- Run `install_evs()`, `generate_all_params()`, and `set_all_text()` here.
    - This will generate the final `common.emevd.dcx`, `item.msgbnd.dcx`, and `menu.msgbnd.dcx`.

TODO: Feature sets:
    SURVIVAL: Hunger, thirst, temperature, and Torrent nerf
        - To disable, remove the relevant events, recipes, cookbooks, and Torrent (NpcParam) change.
    WEAPONS: Craftable weapon trees and recipe books
        - To disable, remove the relevant events, recipes, Hammers, reinforcement disable, and new component drops
    DISEASES: Regional diseases and findable cure recipes
        - To disable, remove the relevant events and cure items/recipes
    DARKNESS: Night time is much darker
        - To disable, remove the relevant events and/or just don't run the executable

TODO:
    - Have three nested levels of `Game` packages with binary ENABLE/DISABLE options for each of the above three.
    - Also have a 'Darkness Only' option in the root folder.
    - Darkness can be specifically disabled in any of the others by simply not running the executable.
    - No need to vary text between installations (except Darkness Only).
    -

TODO:
    - Sacred Tear crafting?

TODO (Notes for Player):
    - If you "infuse" a weapon (Heavy, Keen, Fire, etc.) then you will not be able to upgrade it. For now, it's
      recommended that you avoid infusion for playthroughs (or just clear the infusion when it's upgrade time).
    - When you craft a weapon upgrade, the crafting menu will not update until you change tabs or go out and back in.
      If you try to craft an "invalid" upgrade recipe (e.g., because you no longer have the required weapon but the menu
      has not refreshed), the ingredients you put into it will be wasted.
    - "Night" is so bright in some areas of the game that you may notice TRUE DARKNESS appearing and disappearing quite
      abruptly at times. Not much can be done about this right now, unfortunately.
"""
import shutil
from pathlib import Path
from soulstruct.eldenring.events import EMEVD

from survival_params import generate_all_params
from survival_text import set_all_text
from yabber import yabber


VANILLA_PATH = Path("C:/Steam/steamapps/common/ELDEN RING (Vanilla)/Game")
MODDING_PATH = Path("C:/Steam/steamapps/common/ELDEN RING (Modding)/Game")


def vanilla_common_emevd_to_evs():
    EMEVD(VANILLA_PATH / "event/common.emevd").write_evs(Path(__file__).parent / "common.evs.py")


def write_yabber_dcx_xml():
    """Generates XML for Yabber packing of ER EMEVD."""
    xml = """<?xml version="1.0" encoding="utf-8"?>
<dcx>
  <compression>DarkSouls3</compression>
</dcx>"""
    with (MODDING_PATH / "event/common.emevd-yabber-dcx.xml").open("w") as f:
        f.write(xml)


def install_regulation():
    modded_regulation_path = Path(__file__).parent.parent / "regulation.bin"
    shutil.copy2(modded_regulation_path, MODDING_PATH / "regulation.bin")
    print("Copied modded `regulation.bin` to game directory.")


def install_evs():
    """Install Survival Mode common EMEVD."""
    this_dir = Path(__file__).parent
    common = EMEVD(this_dir / "common.evs.py")
    survival_common = EMEVD(this_dir / "survival_common.evs.py")
    survival_common.write_numeric(this_dir / "survival_common.txt")
    num = EMEVD(this_dir / "survival_common.txt")
    num.write_evs(this_dir / "num.evs.py")
    merged = common.merge(survival_common, merge_events=(0,))

    # EVS for inspection
    merged.write_evs(this_dir / "built_common.evs.py")

    # Game common
    merged.dcx_magic = None
    merged.write(MODDING_PATH / "event/common.emevd")

    # Call Yabber to apply DCX
    write_yabber_dcx_xml()
    yabber(MODDING_PATH / "event/common.emevd", dcx_only=True)


def install():
    install_evs()
    # install_regulation()  # TODO: Live-modding in the game with Yapped atm.
    print("Elden Ring: Survival Mode installed (EMEVD, Params).")


if __name__ == '__main__':
    install_evs()
    # generate_all_params()
    # set_all_text()
    print("Full SurvivalMode Python installation complete. (Now use Yapped to convert CSVs to `regulation.bin`.")
