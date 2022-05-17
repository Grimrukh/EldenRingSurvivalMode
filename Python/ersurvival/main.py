import shutil
import subprocess as sp
from pathlib import Path
from soulstruct.eldenring.events import EMEVD


VANILLA_PATH = Path("C:/Steam/steamapps/common/ELDEN RING (Vanilla)/Game")
MODDING_PATH = Path("C:/Steam/steamapps/common/ELDEN RING (Modding)/Game")
YABBER_DCX_PATH = Path(r"C:\Dark Souls\Tools\Unpackers\Yabber 1.3.1\Yabber.DCX.exe")


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
    sp.call([YABBER_DCX_PATH, str(MODDING_PATH / "event/common.emevd")])


def install():
    """TODO: Read some basic options for Lobos from .ini file.
        - Might just need different versions of params and/or common EMEVD.
    """
    install_evs()
    # install_regulation()  # TODO: Live-modding in the game with Yapped atm.
    print("Elden Ring: Survival Mode installed (EMEVD, Params).")


if __name__ == '__main__':
    install_evs()
