"""Loads Yapped FMG XML and makes some simple changes."""
from xml.etree import ElementTree
from pathlib import Path

GAME_ROOT = Path(r"C:\Steam\steamapps\common\ELDEN RING (Modding)\Game")
ITEM_PATH = GAME_ROOT / r"msg\engus\item-msgbnd-dcx\GR\data\INTERROOT_win64\msg\engUS"
MENU_PATH = GAME_ROOT / r"msg\engus\menu-msgbnd-dcx\GR\data\INTERROOT_win64\msg\engUS"


def get_text_id(text_xml: ElementTree, text_id: int):
    entries = text_xml.getroot().find("entries")
    for e in entries:
        if int(e.get("id")) == text_id:
            return e.text
    raise KeyError(f"Text ID {text_id} does not exist in this XML.")


def set_text_id(text_xml: ElementTree, text_id: int, text: str):
    """Replace or create text ID with given `text`."""
    entries = text_xml.getroot().find("entries")
    for e in entries:
        if int(e.get("id")) == text_id:
            e.text = text
            return
    else:
        # Create new text ID. (No need to sort, Yabber will do that.)
        new_text = ElementTree.SubElement(entries, "text")
        new_text.set("id", str(text_id))
        new_text.text = text


def load_xml(xml_name: str):
    # TODO: Auto-run Yabber to generate XML?
    return ElementTree.parse(ITEM_PATH / xml_name)


if __name__ == '__main__':
    weapons = load_xml("WeaponName.fmg.xml")
    set_text_id(weapons, 1000001, "Daggerest")
    weapons.write(ITEM_PATH / "WeaponName.fmg.xml")
