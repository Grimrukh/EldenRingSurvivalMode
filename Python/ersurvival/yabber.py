__all__ = ["yabber"]

import subprocess as sp
from pathlib import Path

YABBER_PATH = Path(r"C:\Dark Souls\Tools\Unpackers\Yabber 1.3.1\Yabber.exe")
YABBER_DCX_PATH = Path(r"C:\Dark Souls\Tools\Unpackers\Yabber 1.3.1\Yabber.DCX.exe")


def yabber(path, dcx_only=False):
    """Call `Yabber.exe` on given file or folder path."""
    if dcx_only:
        sp.call([YABBER_DCX_PATH, str(path)])
    else:
        sp.call([YABBER_PATH, str(path)])
