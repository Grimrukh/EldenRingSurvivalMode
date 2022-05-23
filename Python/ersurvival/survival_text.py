"""Loads Yapped FMG XML and makes some simple changes."""
import subprocess as sp
from xml.etree import ElementTree
from pathlib import Path

from survival_enums import *
from survival_goods import *

GAME_ROOT = Path(r"C:\Steam\steamapps\common\ELDEN RING (Modding)\Game")
ITEM_PATH = GAME_ROOT / r"msg\engus\item-msgbnd-dcx\GR\data\INTERROOT_win64\msg\engUS"
MENU_PATH = GAME_ROOT / r"msg\engus\menu-msgbnd-dcx\GR\data\INTERROOT_win64\msg\engUS"
YABBER_PATH = Path(r"C:\Dark Souls\Tools\Unpackers\Yabber 1.3.1\Yabber.exe")


class YabberText:

    def __init__(self, xml_path: Path):
        self.tree = ElementTree.parse(xml_path)

    def __getitem__(self, text_id: int):
        text_id = int(text_id)
        entries = self.tree.getroot().find("entries")
        for e in entries:
            if int(e.get("id")) == text_id:
                return e.text
        raise KeyError(f"Text ID {text_id} does not exist in this XML.")

    def __setitem__(self, text_id: int, text: str):
        """Replace or create text ID with given `text`."""
        text_id = int(text_id)
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


EVENT_TEXT = {
    SurvivalText.MildHeatWarning: "The heat is draining",
    SurvivalText.ModerateHeatWarning: "The heat is unbearable",
    SurvivalText.SevereHeatWarning: "The heat spells imminent death",
    SurvivalText.MildColdWarning: "You are cold",
    SurvivalText.ModerateColdWarning: "You are very cold",
    SurvivalText.SevereColdWarning: "You are extremely cold",
    SurvivalText.ContractedLimgraveDisease: "Infected with Limgrave plague",
    SurvivalText.ContractedLiurniaDisease: "Infected with Liurnia toxin",
    SurvivalText.ContractedCaelidDisease: "Infected with Caelid parasite",
    SurvivalText.ContractedAltusDisease: "Infected with Altus fever",
    SurvivalText.ContractedMtGelmirDisease: "Infected with Gelmir plague",
    SurvivalText.ContractedMountaintopsDisease: "Infected with Mountaintops parasite",
    SurvivalText.ContractedSiofraDisease: "Infected with Siofra plague",
    SurvivalText.ContractedAinselDisease: "Infected with Ainsel toxin",
    SurvivalText.ContractedDeeprootDisease: "Infected with Deeproot parasite",
    SurvivalText.ContractedStormveilDisease: "Infected with Stormveil plague",
    SurvivalText.ContractedRayaLucariaDisease: "Infected with Raya Lucaria toxin",
    SurvivalText.ContractedRadahnDisease: "Infected with Radahn fever",
    SurvivalText.ContractedVolcanoManorDisease: "Infected with Volcano toxin",
    SurvivalText.ContractedLeyndellDisease: "Infected with Leyndell plague",
    SurvivalText.ContractedSewersDisease: "Infected with Sewers parasite",
    SurvivalText.ContractedHaligtreeDisease: "Infected with Haligtree plague",
    SurvivalText.ContractedFarumAzulaDisease: "Infected with Farum Azula fever",
    SurvivalText.ContractedMohgwynDisease: "Infected with Mohgwyn fever",
    SurvivalText.ContractedCatacombsDisease: "Infected with Catacombs toxin",
    SurvivalText.ContractedCaveDisease: "Infected with Cave parasite",
    SurvivalText.ContractedTunnelDisease: "Infected with Tunnel fever",
    SurvivalText.CuredPlague: "Cured plague",
    SurvivalText.CuredToxin: "Cured toxin",
    SurvivalText.CuredFever: "Cured fever",
    SurvivalText.CuredParasite: "Cured parasite",
    SurvivalText.Dehydration: "You are suffering from dehydration",
}


def set_goods_text():
    goods_name = YabberText(ITEM_PATH / "GoodsName_vanilla.fmg.xml")
    goods_info = YabberText(ITEM_PATH / "GoodsInfo_vanilla.fmg.xml")
    goods_caption = YabberText(ITEM_PATH / "GoodsCaption_vanilla.fmg.xml")  # TODO

    for good_id, good_info in NEW_CONSUMABLES.items():
        goods_name[good_id] = good_info["name"]
        goods_info[good_id] = good_info["info"]
        goods_caption[good_id] = good_info["caption"]

    for good_id, good_info in NEW_MATERIALS.items():
        goods_name[good_id] = good_info["name"]
        goods_info[good_id] = good_info["info"]
        goods_caption[good_id] = good_info["caption"]

    goods_name.write(ITEM_PATH / "GoodsName.fmg.xml")
    goods_info.write(ITEM_PATH / "GoodsInfo.fmg.xml")
    goods_caption.write(ITEM_PATH / "GoodsCaption.fmg.xml")

    sp.call([YABBER_PATH, str(ITEM_PATH / "GoodsName.fmg.xml")])
    sp.call([YABBER_PATH, str(ITEM_PATH / "GoodsInfo.fmg.xml")])
    sp.call([YABBER_PATH, str(ITEM_PATH / "GoodsCaption.fmg.xml")])


def set_event_text():
    event_text = YabberText(MENU_PATH / "EventTextForMap_vanilla.fmg.xml")

    for text_id, text in EVENT_TEXT.items():
        event_text[text_id] = text

    event_text.write(MENU_PATH / "EventTextForMap.fmg.xml")
    sp.call([YABBER_PATH, str(MENU_PATH / "EventTextForMap.fmg.xml")])


def set_menu_text():
    menu_text = YabberText(MENU_PATH / "GR_MenuText_vanilla.fmg.xml")

    # TODO: Same text is used in standard Inventory, unfortunately. Probably have to leave it.
    # menu_text[40511] = "Weapons/Ammo"

    menu_text.write(MENU_PATH / "GR_MenuText.fmg.xml")
    sp.call([YABBER_PATH, str(MENU_PATH / "GR_MenuText.fmg.xml")])


def set_all_text():
    set_goods_text()
    set_event_text()
    # set_menu_text()

    # Pack up MSGBNDs with Yabber when done with FMGs.
    sp.call([YABBER_PATH, str(GAME_ROOT / "msg/engus/item-msgbnd-dcx")])
    sp.call([YABBER_PATH, str(GAME_ROOT / "msg/engus/menu-msgbnd-dcx")])


if __name__ == '__main__':
    set_all_text()
