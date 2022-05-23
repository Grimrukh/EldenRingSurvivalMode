"""Loads Yapped FMG XML and makes some simple changes."""
import subprocess as sp
from xml.etree import ElementTree
from pathlib import Path

GAME_ROOT = Path(r"C:\Steam\steamapps\common\ELDEN RING (Modding)\Game")
ITEM_PATH = GAME_ROOT / r"msg\engus\item-msgbnd-dcx\GR\data\INTERROOT_win64\msg\engUS"
MENU_PATH = GAME_ROOT / r"msg\engus\menu-msgbnd-dcx\GR\data\INTERROOT_win64\msg\engUS"
YABBER_PATH = Path(r"C:\Dark Souls\Tools\Unpackers\Yabber 1.3.1\Yabber.exe")


class YabberText:

    def __init__(self, xml_path: Path):
        self.tree = ElementTree.parse(xml_path)

    def __getitem__(self, text_id: int):
        entries = self.tree.getroot().find("entries")
        for e in entries:
            if int(e.get("id")) == text_id:
                return e.text
        raise KeyError(f"Text ID {text_id} does not exist in this XML.")

    def __setitem__(self, text_id: int, text: str):
        """Replace or create text ID with given `text`."""
        entries = self.tree.getroot().find("entries")
        for e in entries:
            if int(e.get("id")) == text_id:
                e.text = text
                return
        else:
            # Create new text ID. (No need to sort, Yabber will do that.)
            new_text = ElementTree.SubElement(entries, "text", id=str(text_id))
            new_text.text = text

    def write(self, xml_path: Path):
        ElementTree.indent(self.tree, "    ")
        self.tree.write(xml_path, encoding="utf-8")


def read_weapon_text():
    return (
        YabberText(ITEM_PATH / "WeaponName_vanilla.fmg.xml"),
        YabberText(ITEM_PATH / "WeaponInfo_vanilla.fmg.xml"),
        YabberText(ITEM_PATH / "WeaponCaption_vanilla.fmg.xml"),
    )


def write_weapon_text(name: YabberText, info: YabberText, caption: YabberText):
    name.write(ITEM_PATH / "WeaponName.fmg.xml")
    info.write(ITEM_PATH / "WeaponInfo.fmg.xml")
    caption.write(ITEM_PATH / "WeaponCaption.fmg.xml")

    sp.call([YABBER_PATH, str(ITEM_PATH / "WeaponName.fmg.xml")])
    sp.call([YABBER_PATH, str(ITEM_PATH / "WeaponInfo.fmg.xml")])
    sp.call([YABBER_PATH, str(ITEM_PATH / "WeaponCaption.fmg.xml")])


GOODS = {
    1900: {
        "name": "Raw Steak",
        "info": "Basic raw meal crafted by hunters",
        "caption": "TODO",
    },
    1901: {
        "name": "Seared Steak",
        "info": "Basic cooked meal crafted by hunters",
        "caption": "TODO",
    },
    1902: {
        "name": "Raw Liver Steak",
        "info": "Raw meal crafted by expert hunters",
        "caption": "TODO",
    },
    1903: {
        "name": "Seared Liver Steak",
        "info": "Cooked meal crafted by expert hunters",
        "caption": "TODO",
    },
    1904: {
        "name": "Bone Broth",
        "info": "Light broth made by hunters",
        "caption": "TODO",
    },
    1905: {
        "name": "Great Bone Broth",
        "info": "Hearty broth made by hunters",
        "caption": "TODO",
    },
    1906: {
        "name": "Blood Broth",
        "info": "Broth made by bloodthirsty hunters",
        "caption": "TODO",
    },
    1907: {
        "name": "Forest Berry Medley",
        "info": "Medley of berries from the lower lands",
        "caption": "TODO",
    },
    1908: {
        "name": "Plateau Berry Medley",
        "info": "Medley of berries from the plateau",
        "caption": "TODO",
    },
    1909: {
        "name": "Mountain Berry Medley",
        "info": "Medley of berries from the mountains",
        "caption": "TODO",
    },
    1910: {
        "name": "Mushroom Stew",
        "info": "Basic mushroom stew",
        "caption": "TODO",
    },
    1911: {
        "name": "Melted Mushroom Stew",
        "info": "Delicious mushroom stew",
        "caption": "TODO",
    },
    1912: {
        "name": "Draught of the Undining",
        "info": "Prevents hunter temporarily",
        "caption": "TODO",
    },
    1913: {
        "name": "Draught of Silver Tears",
        "info": "Prevents thirst temporarily",
        "caption": "TODO",
    },
    1914: {
        "name": "Mossdew Soup",
        "info": "Soup with mild heat protected",
        "caption": "TODO",
    },
    1915: {
        "name": "Crystal Shard Soup",
        "info": "Soup with moderate heat protection",
        "caption": "TODO",
    },
    1916: {
        "name": "Giant's Soup",
        "info": "Soup with great heat protection",
        "caption": "TODO",
    },
    1917: {
        "name": "Amber-Eye Brew",
        "info": "Brew with mild cold protection",
        "caption": "TODO",
    },
    1918: {
        "name": "Magmatic Brew",
        "info": "Brew with moderate cold protection",
        "caption": "TODO",
    },
    1919: {
        "name": "Blossom Brew",
        "info": "Brew with great cold protection",
        "caption": "TODO",
    },
    1920: {
        "name": "Jar Brittle",
        "info": "Crunchy brittle from living jars",
        "caption": "TODO",
    },
}


def set_goods_text():
    goods_name = YabberText(ITEM_PATH / "GoodsName_vanilla.fmg.xml")
    goods_info = YabberText(ITEM_PATH / "GoodsInfo_vanilla.fmg.xml")
    goods_caption = YabberText(ITEM_PATH / "GoodsCaption_vanilla.fmg.xml")  # TODO

    for good_id, good_info in GOODS.items():
        goods_name[good_id] = good_info["name"]
        goods_info[good_id] = good_info["info"]
        goods_caption[good_id] = good_info["caption"]

    from survival_params import NEW_MATERIALS
    for material_name, material_info in NEW_MATERIALS.items():
        goods_name[int(material_info["id"])] = material_name
        # TODO: Info, captions

    goods_name.write(ITEM_PATH / "GoodsName.fmg.xml")
    goods_info.write(ITEM_PATH / "GoodsInfo.fmg.xml")
    goods_caption.write(ITEM_PATH / "GoodsCaption.fmg.xml")

    sp.call([YABBER_PATH, str(ITEM_PATH / "GoodsName.fmg.xml")])
    sp.call([YABBER_PATH, str(ITEM_PATH / "GoodsInfo.fmg.xml")])
    sp.call([YABBER_PATH, str(ITEM_PATH / "GoodsCaption.fmg.xml")])


# TODO: event text
# TODO: Replace "Arrows/Bolts" in crafting menu with "Weapons/Ammo"


def set_all_text():
    set_goods_text()

    # Pack up MSGBNDs with Yabber when done with FMGs.
    sp.call([YABBER_PATH, str(GAME_ROOT / "msg/engus/item-msgbnd-dcx")])
    sp.call([YABBER_PATH, str(GAME_ROOT / "msg/engus/menu-msgbnd-dcx")])


if __name__ == '__main__':
    set_all_text()
