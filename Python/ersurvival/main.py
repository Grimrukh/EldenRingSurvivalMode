from pathlib import Path
from soulstruct.eldenring.events import EMEVD


GAME = Path("C:/Dark Souls/ELDEN RING/GAME")


def vanilla_common_emevd_to_evs():
    EMEVD(GAME / "event/common.emevd").write_evs(Path(__file__).parent / "common.evs.py")


if __name__ == '__main__':
    vanilla_common_emevd_to_evs()
