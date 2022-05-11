from pathlib import Path
from soulstruct.eldenring.events import EMEVD


VANILLA_PATH = Path("C:/Steam/steamapps/common/ELDEN RING (Vanilla)/Game")
MODDING_PATH = Path("C:/Steam/steamapps/common/ELDEN RING (Modding)/Game")


def vanilla_common_emevd_to_evs():
    EMEVD(VANILLA_PATH / "event/common.emevd").write_evs(Path(__file__).parent / "common.evs.py")


def install_evs():
    """Install Survival Mode common EMEVD."""
    this_dir = Path(__file__).parent
    common = EMEVD(this_dir / "common.evs.py")
    common.merge(this_dir / "survival_common.evs.py", merge_events=(0,))

    common.write_evs(this_dir / "built_common.evs.py")


if __name__ == '__main__':
    install_evs()
