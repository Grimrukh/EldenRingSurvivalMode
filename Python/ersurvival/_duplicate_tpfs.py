"""Simple script that duplicates '00_Solo' TPFs to all the new IDs I need for large icons."""
import shutil
from pathlib import Path

from survival_text import GAME_ROOT
from survival_goods import NEW_MATERIALS, NEW_CONSUMABLES
from yabber import yabber

ICONS = []
for goods_dict in (NEW_MATERIALS, NEW_CONSUMABLES):
    ICONS += [(good["name"], good["icon"]) for good in goods_dict.values() if good["icon"] >= 19000]
ICONS.sort(key=lambda x: x[1])

SOURCE_ID = "18890"
LOW_SOLO_START_ID = 2416
HI_SOLO_START_ID = 2419

BHD_TEMPLATE = r"""    <file>
      <flags>0x40</flags>
      <id>{}</id>
      <root />
      <path>00_Solo\MENU_Knowledge_{}.tpf.dcx</path>
    </file>"""

LOW_SOURCE_TPF = GAME_ROOT / r"menu\low\00_solo-tpfbhd\00_Solo\MENU_Knowledge_18890-tpf-dcx"
HI_SOURCE_TPF = GAME_ROOT / r"menu\hi\00_solo-tpfbhd\00_Solo\MENU_Knowledge_18890-tpf-dcx"


def print_bhd_headers():
    entry_id = HI_SOLO_START_ID

    for good_name, icon_id in ICONS:
        print(BHD_TEMPLATE.format(entry_id, f"{icon_id:05d}"))
        entry_id += 1


def copy_tpfs():
    """Copy TPF folder but change ID of folder, Yabber XML, and DDS file to new one."""
    for good_name, icon_id in ICONS:
        print(good_name, icon_id)
        continue
        new_stem = f"MENU_Knowledge_{icon_id:05d}"
        dest_dir = SOURCE_TPF.parent / f"{new_stem}-tpf-dcx"
        shutil.copytree(SOURCE_TPF, dest_dir)

        xml_path = dest_dir / "_yabber-tpf.xml"
        xml_text = xml_path.read_text()
        new_xml_text = xml_text.replace(SOURCE_ID, str(icon_id))
        xml_path.write_text(new_xml_text)

        dds_path = dest_dir / "MENU_Knowledge_18890.dds"
        dds_path.rename(dest_dir / f"{new_stem}.dds")


def yabber_tpfs():
    for good_name, icon_id in ICONS:
        unpacked_tpf_path = HI_SOURCE_TPF.parent / f"MENU_Knowledge_{icon_id:05d}-tpf-dcx"
        yabber(unpacked_tpf_path)


if __name__ == '__main__':
    # print_bhd_headers()
    # copy_tpfs()
    yabber_tpfs()
    print("Done.")
