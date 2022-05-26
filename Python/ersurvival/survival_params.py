"""Scripts for generating Params (regulation.bin).

Modifies CSV files exported by Yapped (Rune Bear), which that program can then re-import.
"""
from __future__ import annotations

import csv
import random
import re
import shutil
from pathlib import Path

from survival_goods import *
from survival_text import read_weapon_text, write_weapon_text
from weapon_recipes import WEAPON_RECIPES

CSV_PATH = Path(r"C:\Dark Souls\Tools\Params\Yapped Rune Bear 2.1.4\Projects\ExampleMod\CSV\ER")


class YappedRow(dict):

    def __init__(self, source: dict):
        self.__initialized = False
        super().__init__(source)
        self.__initialized = True

    def to_list(self):
        return list(self.values())

    @property
    def row_id(self):
        return self["Row ID"]

    @row_id.setter
    def row_id(self, value: int):
        super().__setitem__("Row ID", value)

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError(f"Row key must be a string: {key}")
        if self.__initialized and key not in self:
            raise ValueError(f"Invalid YappedRow field: {key}")
        if key == "Row ID":
            super().__setitem__(key, int(value))
        else:  # convert to string for CSV
            if isinstance(value, IntEnum):
                value = value.value
            super().__setitem__(key, str(value))

    @property
    def name(self):
        return self["Row Name"]

    @name.setter
    def name(self, value: str):
        super().__setitem__("Row Name", str(value))


class YappedParam:

    def __init__(self, field_names: list[str]):
        self.field_names = field_names
        self.rows = []  # type: list[YappedRow]

    def __getitem__(self, row_id: int):
        for row in self.rows:
            if row.row_id == int(row_id):
                return row
        return None

    def add_row(self, row_dict: dict[str, str | int], after_row_id: int = None):
        if "Row ID" not in row_dict:
            raise ValueError("Expected at least key 'Row ID' in row dict.")
        row_dict["Row ID"] = int(row_dict["Row ID"])  # convert ID to int

        if after_row_id is not None:
            # Find given row ID and insert new row just after it.
            i = 0
            for row in self.rows:
                i += 1
                if row["Row ID"] == after_row_id:
                    self.rows.insert(i, YappedRow(row_dict))
                    return
            raise ValueError(f"Could not find row ID {after_row_id} to insert new row after.")
        else:  # append to end of row list
            self.rows.append(YappedRow(row_dict))

    def duplicate_row(self, source_row_id: int, dest_row_id: int, **kwargs) -> YappedRow:
        row_ids = self.get_row_ids()
        if source_row_id not in row_ids:
            raise ValueError(f"Source row ID {source_row_id} is not in this param.")
        if dest_row_id in row_ids:
            raise ValueError(f"Dest row ID {dest_row_id} already exists. Delete it first if you want to replace it.")
        source_row = self[source_row_id]
        new_row = YappedRow(source_row)
        new_row["Row ID"] = dest_row_id
        if "name" in kwargs:
            new_row.name = kwargs.pop("name")
        for field, value in kwargs.items():
            if field not in new_row:
                raise ValueError(f"Invalid field for this param: {field}")
            new_row[field] = value
        # Insert at `dest_row_id`.
        for i, row in enumerate(self.rows):
            if row.row_id > dest_row_id:
                self.rows.insert(i, new_row)
                break
        else:
            self.rows.append(new_row)
        return new_row

    def get_row_ids(self) -> list[int]:
        return [row["Row ID"] for row in self.rows]
    
    def sort_rows(self):
        """Sort rows by row ID."""
        self.rows = sorted(self.rows, key=lambda x: x["Row ID"])

    def write_csv(self, param_path: Path):
        if param_path.exists():
            bak_path = param_path.with_suffix(param_path.suffix + ".bak")
            if not bak_path.is_file():
                shutil.copy2(param_path, bak_path)

        with param_path.open("w", newline="") as csvfile:
            param_writer = csv.writer(csvfile, delimiter=';', quotechar='|')
            param_writer.writerow(self.field_names)
            for row in self.rows:
                param_writer.writerow(row.to_list() + [""])  # Yapped seems to put an extra semicolon at the end.

    @classmethod
    def from_csv_path(cls, param_path: Path):

        if not param_path.exists():
            raise FileNotFoundError(f"No such CSV file: {param_path}")

        with param_path.open("r", newline='') as csvfile:
            param_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
            row_iter = iter(param_reader)
            field_names = list(next(row_iter))
            param = cls(field_names)
            i = 0
            for csv_row in row_iter:
                row = {}
                if len(csv_row) < len(field_names):
                    raise ValueError(f"CSV row {i} has less than {len(field_names)} rows (field name count).")
                for name, field in zip(field_names, csv_row):
                    row[name] = field
                param.add_row(row)
                i += 1

        print(f"Loaded YappedParam from CSV with {i} rows.")
        return param


def read_param_csv(param_name: str) -> YappedParam:
    return YappedParam.from_csv_path((CSV_PATH / param_name).with_suffix(".csv"))


def write_param_csv(param: YappedParam, param_name: str):
    param.write_csv((CSV_PATH / param_name).with_suffix(".csv"))


PRESERVE_ITEM_LOTS = [
    16000690,  # Serpent-Hunter treasure
]


# Mostly boss rewards. These will be replaced if they exist, or added otherwise.
MANUAL_ITEM_LOTS = {
    # Bosses
    10012: ("[Stormveil - Godrick] Gruesome Bone", Materials.GruesomeBone, 1),
    10030: ("[Chapel of Anticipation - Grafed Scion] Iron Plate", Materials.IronPlate, 1),
    10031: ("[Chapel of Anticipation - Grafed Scion] Shield Grip0", Materials.ShieldGrip, 1),
    10042: ("[Leyndell - Morgott] Erdtree Amber", Materials.ErdtreeAmber, 1),
    10060: ("[Ashen Leyndell - Gideon] Glintstone Dust", Materials.GlintstoneDust, 3),
    10071: ("[Ashen Leyndell - Hoarah Loux] Erdtree Amber", Materials.ErdtreeAmber, 2),
    10081: ("[Lake of Rot - Astel] Meteorite Chunk", Materials.MeteoriteChunk, 3),
    10100: ("[Siofra - Valiant Gargoyle] Iron Plate", Materials.IronPlate, 2),
    10101: ("[Siofra - Valiant Gargoyle] Gruesome Bone", Materials.GruesomeBone, 1),
    10111: ("[Deeproot Depths - Fortissax] Dragon Teeth", Materials.DragonTeeth, 3),
    10122: ("[Mohgwyn Palace - Mohg] Gruesome Bone", Materials.GruesomeBone, 3),
    10151: ("[Farum Azula - Dragonlord Placidusax] Dragon Teeth", Materials.DragonTeeth, 4),
    10161: ("[Farum Azula - Maliketh] Black Mark", Materials.BlackMark, 3),
    10182: ("[Raya Lucaria - Rennala] Glintstone Dust", Materials.GlintstoneDust, 3),
    10191: ("[Haligtree - Loretta] Erdtree Amber", Materials.ErdtreeAmber, 1),
    10202: ("[Haligtree - Malenia] Liquid Metal", Materials.LiquidMetal, 5),
    10210: ("[Volcano Manor - Godskin Noble] Black Mark", Materials.BlackMark, 1),
    10222: ("[Mt. Gelmir - Rykard] Liquid Metal", Materials.LiquidMetal, 3),
    10260: ("[Ruin-Strewn Precipice - Magma Wyrm Makar] Liquid Metal", Materials.LiquidMetal, 1),
    10290: ("[Volcano Manor - Abducator Virgins] Iron Plate", Materials.IronPlate, 2),
    10302: ("[Caelid - Radahn] Meteorite Chunk", Materials.MeteoriteChunk, 3),
    10311: ("[Mountaintops - Fire Giant] Gruesome Bone", Materials.GruesomeBone, 3),
    10321: ("[Siofra - Ancestor Spirit] Refined Wood", Materials.RefinedWood, 2),
    10331: ("[Nokron - Regal Ancestor Spirit] Refined Wood", Materials.RefinedWood, 3),
    10342: ("[Nokron - Mimic Tear] Liquid Metal", Materials.LiquidMetal, 1),
    10800: ("[Weeping Penisula - Leonine Misbegotten] Iron Plate", Materials.IronPlate, 2),
    10810: ("[Caria Manor - Loretta] String", Materials.String, 3),
    10820: ("[Shaded Castle - Elemer of the Briar] Iron Plate", Materials.IronPlate, 2),
    10821: ("[Shaded Castle - Elemer of the Briar] Shield Grip", Materials.ShieldGrip, 1),
    10830: ("[Redmane Castle - Misbegotten Warrior/Crucible Knight] Iron Plate", Materials.IronPlate, 2),
    10840: ("[Castle Sol - Commander Niall] Liquid Metal", Materials.LiquidMetal, 1),
    # Generic dungeons
    20031: ("[Deathtouched Catacombs - Black Knife Assassin] Black Mark", Materials.BlackMark, 1),
    20100: ("[Auriza Hero's Grave - Crucible Knight Ordovis] Refined Wood", Materials.RefinedWood, 3),
    20170: ("[Giant-Conquering Hero's Grave - Ancient Hero of Zamor] Liquid Metal", Materials.LiquidMetal, 1),
    20212: ("[Black Knife Catacombs - Black Knife Assassin] Black Mark", Materials.BlackMark, 1),
    20400: ("[Volcano Cave - Demi-human Queen Margot] Living Jar Shard", Materials.LivingJarShard, 3),
    20470: ("[Cave of the Forlorn - Misbegotten Crusader] Erdtree Wood", Materials.ErdtreeWood, 2),
    20490: ("[Sage's Cave - Necromancer Garris] Glintstone Dust", Materials.GlintstoneDust, 1),
    20600: ("[Morne Tunnel - Scaly Misbegotten] Iron Plate", Materials.IronPlate, 1),
    20630: ("[Old Altus Tunnel - Stonedigger Troll] Gruesome Bone", Materials.GruesomeBone, 1),
    20640: ("[Sealed Tunnel - Onyx Lord] Meteorite Chunk", Materials.MeteoriteChunk, 1),
    20661: ("[Gael Tunnel - Magma Wyrm] Liquid Metal", Materials.LiquidMetal, 1),
    20670: ("[Sellia Crystal Tunnel - Fallingstar Beast] Meteorite Chunk", Materials.MeteoriteChunk, 1),
    20681: ("[Yelough Anix Tunnel - Astel] Meteorite Chunk", Materials.MeteoriteChunk, 2),
    # Overworld bosses
    30100: ("[Limgrave - Field - Tree Sentinel] Iron Plate", Materials.IronPlate, 1),
    30111: ("[Limgrave - Field - Flying Dragon Agheel] Dragon Teeth", Materials.DragonTeeth, 1),
    30130: ("[Limgrave - Evergaol - Bloodhound Knight Darriwil] Liquid Metal", Materials.LiquidMetal, 1),
    30172: ("[Limgrave - Field - Tibia Mariner] Gruesome Bone", Materials.GruesomeBone, 1),
    30187: ("[Weeping Penisula - Field - Erdtree Avatar] Erdtree Wood", Materials.ErdtreeWood, 1),
    30203: ("[Liurnia - Field - Erdtree Avatar] Erdtree Wood", Materials.ErdtreeWood, 1),
    30207: ("[Liurnia - Field - Erdtree Avatar] Erdtree Wood", Materials.ErdtreeWood, 1),
    30211: ("[Liurnia - Field - Glintstone Dragon Smarag] Dragon Teeth", Materials.DragonTeeth, 1),
    30242: ("[Liurnia - Field - Tibia Mariner] Gruesome Bone", Materials.GruesomeBone, 1),
    30256: ("[Liurnia - Evergaol - Onyx Lord] Meteorite Chunk", Materials.MeteoriteChunk, 1),
    30262: ("[Liurnia - Field - Glintstone Dragon Adula] Dragon Teeth", Materials.DragonTeeth, 1),
    30310: ("[Altus Plateau - Field - Fallingstar Beast] Meteorite Chunk", Materials.MeteoriteChunk, 1),
    30315: ("[Capital Outskirts - Field - Draconic Tree Sentinel] Iron Plate", Materials.IronPlate, 1),
    30316: ("[Capital Outskirts - Field - Draconic Tree Sentinel] Shield Grip", Materials.ShieldGrip, 1),
    30322: ("[Altus Plateau - Field - Wormface] Erdtree Wood", Materials.ErdtreeWood, 1),
    30327: ("[Altus Plateau - Field - Godskin Apostle] Liquid Metal", Materials.LiquidMetal, 1),
    30335: ("[Capital Outskirts - Field - Tree Sentinel Duo] Iron Plate", Materials.IronPlate, 2),
    30350: ("[Altus Plateau - Field - Black Knife Assassin] Black Mark", Materials.BlackMark, 1),
    30377: ("[Mt. Gelmir - Field - Full-grown Fallingstar Beast] Meteorite Chunk", Materials.MeteoriteChunk, 2),
    30382: ("[Mt. Gelmir - Field - Ulcerated Tree Spirit] Erdtree Wood", Materials.ErdtreeWood, 1),
    30387: ("[Altus Plateau - Field - Tibia Mariner] Gruesome Bone", Materials.GruesomeBone, 1),
    30390: ("[Mt. Gelmir - Field - Magma Wyrm] Liquid Metal", Materials.LiquidMetal, 1),
    30400: ("[Mt. Gelmir - Field - Magma Wyrm] Liquid Metal", Materials.LiquidMetal, 1),
    30405: ("[Caelid - Field - Commander O'Neil] Staff Pole", Materials.StaffPole, 1),
    30412: ("[Caelid - Field - Erdtree Avatar] Erdtree Wood", Materials.ErdtreeWood, 1),
    30417: ("[Caelid - Field - Putrid Avatar] Erdtree Wood", Materials.ErdtreeWood, 1),
    30421: ("[Caelid - Field - Flying Dragon Greyll] Dragon Teeth", Materials.DragonTeeth, 1),
    30425: ("[Caelid - Field - Blade Blade Kindred] Black Mark", Materials.BlackMark, 1),
    30426: ("[Caelid - Field - Blade Blade Kindred] Gruesome Bone", Materials.GruesomeBone, 1),
    30505: ("[Forbidden Lands - Field - Black Blade Kindred] Black Mark", Materials.BlackMark, 1),
    30506: ("[Forbidden Lands - Field - Black Blade Kindred] Gruesome Bone", Materials.GruesomeBone, 1),
    30511: ("[Mountaintops of the Giants - Field - Borealis, the Freezing Fog] Dragon Teeth", Materials.DragonTeeth, 1),
    30527: ("[Mountaintops of the Giants - Field - Erdtree Avatar] Erdtree Wood", Materials.ErdtreeWood, 2),
    30530: ("[Mountaintops of the Giants - Field - Death Rite Bird] Black Mark", Materials.BlackMark, 1),
    30551: ("[Mountaintops of the Giants - Field - Great Wyrm Theodorix] Dragon Teeth", Materials.DragonTeeth, 1),
    30557: ("[Consecrated Snowfield - Field - Putrid Avatar] Erdtree Wood", Materials.ErdtreeWood, 1),
    30600: ("[Lake of Rot - Dragonkin Soldier] Dragon Teeth", Materials.DragonTeeth, 1),
    30620: ("[Siofra River - Dragonkin Soldier] Dragon Teeth", Materials.DragonTeeth, 1),

    # Other
    80320: ("[Reward - \"Champion's Song\" Painting] Harp Bow", Materials.ErdtreeAmber, 1),

    # NPC gifts
    100360: ("[White-Faced Varre - Invasion] Iron Shards", Materials.IronShards, 10),
    100770: ("[Tanith] Gruesome Bone", Materials.GruesomeBone, 3),
    101580: ("[Blaidd is the Half-Wolf] Iron Plate", Materials.IronPlate, 3),
    101630: ("[Bloody Finger Hunter Yura] Iron Plate", Materials.IronPlate, 1),
    102200: ("[Kenneth Haight] Erdtree Amber", Materials.ErdtreeAmber, 1),
    102860: ("[Gideon Ofnir - Boss Drop] Glintstone Dust", Materials.GlintstoneDust, 3),
    102921: ("[Knight Bernahl] Gruesome Bone", Materials.GruesomeBone, 2),
    103010: ("[Big Boggart] Iron Plate", Materials.IronPlate, 1),
    103022: ("[Big Boggart] Iron Plate", Materials.IronPlate, 1),
    103410: ("[Prince of Death's Throne] Black Mark", Materials.BlackMark, 1),
    103500: ("[Sorcerer Rogier] Glintstone Dust", Materials.GlintstoneDust, 2),
    103580: ("[Sorcerer Rogier] Glintstone Dust", Materials.GlintstoneDust, 2),
    103930: ("[Ranni the Witch] Meteorite Chunk", Materials.MeteoriteChunk, 4),
    104500: ("[Juno Hoslow] Iron Shards", Materials.IronShards, 5),
    104510: ("[Juno Hoslow] Iron Shards", Materials.IronShards, 5),

    # Corpses
    110300: ("[Corpse - White-Faced Varre - Invasion] Iron Shards", Materials.IronShards, 10),
    110600: ("[Corpse - Edgar] Iron Plate", Materials.IronPlate, 1),
    110610: ("[Corpse - Edgar] Iron Plate", Materials.IronPlate, 1),
    110621: ("[Corpse - Edgar] Iron Plate", Materials.IronPlate, 1),
    111500: ("[Corpse - Blaidd is the Half-Wolf] Iron Plate", Materials.IronPlate, 3),
    111600: ("[Corpse - Bloody Finger Hunter Yura] Iron Plate", Materials.IronPlate, 1),
    112901: ("[Corpse - Knight Bernahl] Gruesome Bone", Materials.GruesomeBone, 2),
    113002: ("[Corpse - Big Boggart] Iron Plate", Materials.IronPlate, 1),
    113012: ("[Corpse - Big Boggart] Iron Plate", Materials.IronPlate, 1),
    113410: ("[Corpse - Prince of Death's Throne] Black Mark", Materials.BlackMark, 1),
    113420: ("[Corpse - Prince of Death's Throne] Black Mark", Materials.BlackMark, 1),
    113601: ("[Corpse - Thops] Staff Pole", Materials.StaffPole, 1),
    113701: ("[Corpse - Brother Corhyn] Iron Shards", Materials.IronShards, 3),
    113800: ("[Corpse - Dung Eater] Iron Plate", Materials.IronPlate, 1),
    113820: ("[Corpse - Dung Eater] Iron Plate", Materials.IronPlate, 1),
    114210: ("[Corpse - Nepheli Loux] Iron Plate", Materials.IronPlate, 1),
    114211: ("[Corpse - Nepheli Loux] Iron Plate", Materials.IronPlate, 1),
    114500: ("[Corpse - Juno Hoslow] Iron Shards", Materials.IronShards, 5),
}


WEAPON_CRAFTING_VISIBILITY = {}  # TODO: Map shield/staff/seal/torch weapon names to "cookbook" flags.


def generate_dummy_weapons(
    weapon_param: YappedParam,
    equip_mtrl_set_param: YappedParam,
    shop_recipe_param: YappedParam,
    item_lots_map_param: YappedParam,  # assuming that this (not 'enemy') is used for EMEVD rewards but shouldn't matter
):
    """Generate dummy weapons for each melee weapon with type 13 (arrow).

    These dummy weapons can appear properly in crafting menus, and will be silently replaced with the real weapon by
    EMEVD as soon as the player receives it.
    """

    def do_weapon(weapon_row: YappedRow):
        if not weapon_row.name:
            return False  # ignore unused weapons
        if 1000000 <= weapon_row.row_id <= 47010000 and weapon_row.row_id % 10000 == 0:
            return True  # all weapons (ignoring infused)

    dummy_offset = 60000000

    new_mtrl_offset = 330000
    mtrl_source = 320010  # 3x Thin Beast Bones

    new_shop_offset = 33000
    shop_source = 1  # unnamed

    item_lot_offset = 40000000
    item_lot_source = 100

    # NOTE: There are some existing high-ID weapons starting with 98990000, but these are above the highest dummy
    # weapon that will be created here (32300000 + 60000000 = 92300000).

    new_weapon_indices = list(WEAPON_RECIPES.keys())
    tiers_dict = parse_weapon_tiers()  # maps weapon names to (weapon_id, previous_id) pair

    names, infos, captions = read_weapon_text()

    slot = 0
    for row in weapon_param.rows:
        if not do_weapon(row):
            continue

        weapon_root_index = row.row_id // 10000
        dummy_id = dummy_offset + 100 * weapon_root_index
        shop_id = new_shop_offset + weapon_root_index
        mtrl_id = new_mtrl_offset + 10 * weapon_root_index
        item_lot_id = item_lot_offset + 100 * weapon_root_index
        weapon_base_id = 10000 * weapon_root_index

        try:
            true_weapon_id, previous_weapon_id = tiers_dict[row.name]
        except KeyError:
            # Weapon is not in the upgrade tree, and is simply crafted from scratch (Shields, Staffs, Seals, Torches)
            true_weapon_id = row.row_id  # no upgrade level (can be upgrading normally at blacksmith)
            previous_weapon_id = None  # no previous weapon in recipe
            remove_reinforcement = False
        else:
            # Remove reinforcement from tiered weapon.
            remove_reinforcement = True

        # Determine rune cost for crafting from upgrade level.
        upgrade_level = true_weapon_id % 100
        if row["materialSetId"] == "2200":
            # Somber. 5000 runes times level.
            rune_cost = 5000 * upgrade_level
        elif row["materialSetId"] == "0":
            # Standard. 2500 runes times level.
            rune_cost = 2500 * upgrade_level
        else:
            raise ValueError(f"Invalid 'materialSetId' for weapon {row.name}: {row['materialSetId']}")

        if rune_cost == 0:
            # TODO: Probably want more hand-crafted costs for shields/staffs/seals/torches.
            rune_cost = 500  # minimum rune cost (for 'from scratch' weapons)

        if remove_reinforcement:
            row["materialSetId"] = -1

        # Create dummy Weapon row.
        dummy = weapon_param.duplicate_row(row.row_id, dummy_id)
        dummy["Row Name"] += " (crafting dummy)"
        dummy["weaponCategory"] = 13  # arrow (for appearing in crafting menu)

        # Set crafting dummy name text.
        if previous_weapon_id is not None:
            previous_weapon_base_id = 10000 * (previous_weapon_id // 10000)  # ignore upgrade level
            previous_weapon_name = names[previous_weapon_base_id]
            infos[dummy_id] = f"Upgrade {previous_weapon_name} into {names[weapon_base_id]}"
        else:
            infos[dummy_id] = f"Craft {names[weapon_base_id]} from raw materials"

        # Copy captions.
        names[dummy_id] = names[weapon_base_id]
        captions[dummy_id] = captions[weapon_base_id]

        # Create item lot for awarding real weapon.
        new_item_lot = item_lots_map_param.duplicate_row(item_lot_source, item_lot_id)
        new_item_lot.name = f"{row.name} (crafted)"
        new_item_lot["lotItemId01"] = true_weapon_id  # potentially upgraded version
        new_item_lot["lotItemCategory01"] = 2  # Weapon
        new_item_lot["lotItemNum01"] = 1

        if row.name in WEAPON_CRAFTING_VISIBILITY:
            visibility_flag = WEAPON_CRAFTING_VISIBILITY[row.name]
        elif previous_weapon_id is None:
            # print(f"# NOTE: Recipe for weapon '{row.name}' will always be visible.")
            visibility_flag = 0
        else:
            # Visibility flag is determined by monitoring previous weapon ID.
            previous_weapon_base_id = 10000 * (previous_weapon_id // 10000)  # ignore upgrade level
            previous_weapon_name = weapon_param[previous_weapon_base_id].name
            visibility_flag = SurvivalFlags.WeaponMonitorBase + new_weapon_indices.index(previous_weapon_name)

        # Create recipe entry.
        new_shop_row = shop_recipe_param.duplicate_row(shop_source, shop_id)
        new_shop_row.name = row.name
        new_shop_row["equipId"] = dummy_id
        new_shop_row["value"] = rune_cost
        new_shop_row["mtrlId"] = mtrl_id
        new_shop_row["eventFlag_forRelease"] = visibility_flag
        new_shop_row["equipType"] = 0  # Weapon
        new_shop_row["setNum"] = 1  # only one

        # TODO: for common EMEVD
        # print(
        #     f"CraftDummyWeapon("
        #     f"{slot}, "
        #     f"{dummy_id}, "
        #     f"{item_lot_id}, "
        #     f"{previous_weapon_id if previous_weapon_id is not None else 0})"
        # )
        # monitor_flag = SurvivalFlags.WeaponMonitorBase + new_weapon_indices.index(row.name)
        # print(
        #     f"MonitorWeaponPossession({slot}, {true_weapon_id}, {monitor_flag})"
        # )
        slot += 1

        # Create ingredients entry.
        # TODO: Staff Pole and Shield Grip are not appearing in recipes.
        # TODO: Serpent-Hunter still has a recipe. Probably good, but need a recipe book drop (note) then.
        new_mtrl_row = equip_mtrl_set_param.duplicate_row(mtrl_source, mtrl_id)
        new_mtrl_row.name = row.name
        ingredients = [ing for ing in WEAPON_RECIPES[row.name]["recipe"] if ing[1] < 21100]  # ignore grips
        if not ingredients:
            # print(f"No recipe ingredients for weapon {row.name}. Skipping for now.")
            pass
        else:
            if len(ingredients) >= 5:
                print(f"WARNING: More than four ingredients for weapon {row.name}. They will not be displayed.")
            for i, (count, ingredient) in enumerate(ingredients):
                new_mtrl_row[f"materialId{i + 1:02d}"] = ingredient.value
                new_mtrl_row[f"itemNum{i + 1:02d}"] = count
                new_mtrl_row[f"materialCate{i + 1:02d}"] = 4  # always Goods

    write_weapon_text(names, infos, captions)
    print("Wrote weapon FMGs successfully.")


def generate_new_consumables(
    goods_param: YappedParam, shop_recipe_param: YappedParam, equip_mtrl_set_param: YappedParam
):
    """Recipes for new "survival" goods (food, drink, protection)."""

    # Goods
    new_good_offset = 1900
    goods_source = 1110  # Immunizing Cured Meat

    # "Shop" lineup entries
    new_shop_offset = 32500
    shop_source = 1  # unnamed

    # Ingredients
    new_mtrl_offset = 325000
    mtrl_source = 320010  # 3x Thin Beast Bones

    for good_base_id, good_info in NEW_CONSUMABLES.items():
        good_id = new_good_offset + good_base_id
        shop_id = new_shop_offset + good_base_id
        mtrl_id = new_mtrl_offset + 10 * good_base_id

        new_good_row = goods_param.duplicate_row(goods_source, good_id)
        new_good_row.name = good_info["name"]
        new_good_row["refId_default"] = good_info["effect"]
        new_good_row["sellValue"] = -1
        new_good_row["iconId"] = 52  # TODO: set for each new good in its dictionary
        new_good_row["goodsUseAnim"] = good_info["animation"].value
        # TODO: Probably other stuff too (e.g., VFX).

        new_shop_row = shop_recipe_param.duplicate_row(shop_source, shop_id)
        new_shop_row.name = good_info["name"]
        new_shop_row["equipId"] = good_id
        # TODO: value (rune cost)?
        new_shop_row["mtrlId"] = mtrl_id
        # TODO: visibility flag?
        new_shop_row["equipType"] = 3  # always Goods
        new_shop_row["setNum"] = 1  # only one

        new_mtrl_row = equip_mtrl_set_param.duplicate_row(mtrl_source, mtrl_id)
        new_mtrl_row.name = good_info["name"]
        for i, (count, ingredient) in enumerate(good_info["recipe"]):
            new_mtrl_row[f"materialId{i + 1:02d}"] = ingredient.value
            new_mtrl_row[f"itemNum{i + 1:02d}"] = count
            new_mtrl_row[f"materialCate{i + 1:02d}"] = 4  # always Goods


def generate_new_materials(goods_param: YappedParam):
    """Add new crafting material Goods. Relatively simple."""
    source_row = 15000  # Sliver of Meat
    for good_id, good_info in NEW_MATERIALS.items():
        new_material = goods_param.duplicate_row(source_row, good_id, iconId=good_info["icon"])
        new_material.name = good_info["name"]


def replace_stone_item_lots(item_lots_param: YappedParam, is_map: bool):
    """Replace [Somber] Smithing Stones with [Somber] Stone Fragments, some percentage of the time.

    Stone Fragment drop count depends on the level of the Smithing Stone it is replacing.

    Ancient Dragon (max level) stones are not replaced.
    """
    leave_odds = 0.2  # proportion of item lots to leave as Smithing Stones
    fragment_odds = 0.75  # rather than Iron Shards

    for row in item_lots_param.rows:
        if row.row_id in PRESERVE_ITEM_LOTS:
            continue  # leave these item lots be (e.g., Serpent-Hunter)
        if row.row_id in MANUAL_ITEM_LOTS:
            continue  # handled already in weapon replacement function

        for slot in range(1, 9):
            item_id = int(row[f"lotItemId{slot:02d}"])
            item_type = int(row[f"lotItemCategory{slot:02d}"])
            item_count = int(row[f"lotItemNum{slot:02d}"])
            # drop rate isn't changed

            if item_type != 1 or item_count <= 0:
                # Ignore non-Goods or empty counts
                continue
            if random.random() < leave_odds:
                continue  # leave

            if 10100 <= item_id <= 10107:
                good_id = Materials.StoneFragment
                stone_level = item_id - 10100 + 1  # 1 to 8
            elif 10160 <= item_id <= 10167:
                good_id = Materials.SomberStoneFragment
                stone_level = item_id - 10160 + 1  # 1 to 8
            else:
                # Ignore non-Stones.
                continue

            if random.random() >= fragment_odds:
                # Iron Shards instead
                good_id = Materials.IronShards

            if random.random() > fragment_odds:
                # Leave this Smithing Stone.
                continue

            # Number of fragments/shards randomly varies between 1 and HALF the Smithing Stone level, rounded down.
            if stone_level <= 3:
                good_count = 1
            else:
                good_count = random.randint(1, int(stone_level / 2))

            row[f"lotItemId{slot:02d}"] = good_id
            row[f"lotItemCategory{slot:02d}"] = 1  # Good
            row[f"lotItemNum{slot:02d}"] = good_count

            print(
                f"{'Map' if is_map else 'Enemy'} Smithing Stone item lot {row.row_id}({slot}) "
                f"-> {good_count} {good_id.name}"
            )


def replace_weapon_item_lots(item_lots_param: YappedParam, weapons_param: YappedParam, is_map: bool):
    """Replace all (non-ammo) weapons in given ItemLotParam with components.

    Shields and Staffs have a chance of being replaced with a Shield Grip or Staff Pole, respectively.
    All other weapons will be replaced with a random number of a random ingredient in that weapon's new recipe.
    The random number can be up to half of the recipe requirement for treasure.

    For enemy item lots, only "animal" materials (ID < 20000), Soft Wood, or Iron Shards can be dropped.
    """
    soft_wood_odds = 0.2  # for enemies (vs. Iron Shards)

    manual_item_lots = MANUAL_ITEM_LOTS.copy() if is_map else {}

    for row in item_lots_param.rows:

        if row.row_id in PRESERVE_ITEM_LOTS:
            continue  # leave these item lots be (e.g., Serpent-Hunter)
        if 40000000 <= row.row_id <= 49999999:
            continue  # ignore my new crafting dummy item lots

        if row.row_id in manual_item_lots:
            # Simply replace slot 1 (guaranteed drop) from dictionary.
            row.name, good_id, good_count = manual_item_lots.pop(row.row_id)
            row["lotItemId01"] = good_id
            row["lotItemCategory01"] = 1  # Good
            row["lotItemNum01"] = good_count
            continue

        for slot in range(1, 9):
            item_id = int(row[f"lotItemId{slot:02d}"])
            item_type = int(row[f"lotItemCategory{slot:02d}"])
            item_count = int(row[f"lotItemNum{slot:02d}"])
            # drop rate isn't changed
            if item_id in {0, -1}:
                # Ignore empty item lots.
                continue
            if item_type not in {2, 6}:
                # Ignore non-weapons (but do replace custom weapons, type 6).
                continue
            if item_count <= 0:
                # Ignore empty counts.
                continue

            # Get base weapon ID (round down to nearest 10000).
            base_weapon_id = 10000 * (item_id // 10000)
            weapon_row = weapons_param[base_weapon_id]

            if not weapon_row:
                print(f"Ignoring item lot {row.row_id} with invalid weapon ID: {item_id}")
                continue
            weapon_category = WeaponCategory(int(weapon_row["weaponCategory"]))
            if weapon_category in (WeaponCategory.Arrow, WeaponCategory.Bolt):
                # Ignore ammo.
                continue

            if not weapon_row.name:
                # Ignore unused weapon drops.
                continue

            if is_map:
                # Roll a random material/count to replace lot.
                good_id, good_count = get_random_material()
            else:
                # Replace enemy drop with either 1 Soft Wood (rarer) or 1 Iron Shards.
                good_id = Materials.SoftWood if random.random() < soft_wood_odds else Materials.IronShards
                good_count = 1

            row[f"lotItemId{slot:02d}"] = good_id
            row[f"lotItemCategory{slot:02d}"] = 1  # Good
            row[f"lotItemNum{slot:02d}"] = good_count

            print(f"{'Map' if is_map else 'Enemy'} item lot {row.row_id}({slot}) -> {good_count} {good_id.name}")

    # Add brand new item lots from manual dictionary. Item lot flags are copied from previous row.
    for lot_id, remaining_lot in manual_item_lots.items():
        copy_flag_row = item_lots_param[lot_id - 1]
        if copy_flag_row is None:
            raise KeyError(f"Could not find previous item lot ({lot_id - 1}) flag to copy to manual item lot {lot_id}.")
        else:
            copy_flag_lot_id = copy_flag_row["getItemFlagId"]
        new_lot = item_lots_param.duplicate_row(10000, lot_id)
        new_lot.name, good_id, good_count = remaining_lot
        new_lot["lotItemId01"] = good_id
        new_lot["lotItemCategory01"] = 1  # Good
        new_lot["lotItemNum01"] = good_count
        new_lot["getItemFlagId"] = copy_flag_lot_id


def parse_weapon_tiers():
    """Parses `weapon_tiers.txt` and returns a dictionary mapping weapon names to weapon ID and previous weapon ID (for
    recipe)."""
    tiers_dict = {}
    line_re = re.compile(r"^( *)(.*) *$")

    tiers = (Path(__file__).parent / "weapon_tiers.txt").read_text()
    previous_weapons = []  # weapon ID and indent level
    added_weapons = []  # (name, level) pairs

    for i, line in enumerate(tiers.split("\n")):
        if "#" in line:
            line = line.split("#")[0].rstrip()  # remove end-line comment
        if not line.strip():
            continue  # ignore empty line
        match = line_re.match(line)
        if not match:
            raise ValueError(f"Invalid line {i} in 'weapon_tiers.txt': {line}")
        indent = len(match.group(1))
        weapon_name = match.group(2)

        if "->" in weapon_name:  # manually specified previous weapon
            if indent != 0:
                raise ValueError(f"Invalid line {i} in 'weapons_tiers.txt'. Cannot use '->' with an indent.")
            previous_weapon_name, weapon_name = weapon_name.split("->")

            previous_weapon_name = previous_weapon_name.strip()
            if "+" in previous_weapon_name:
                name, level_str = previous_weapon_name.split("+")
                previous_weapon_name = name.strip()
                previous_weapon_level = int(level_str.strip())
            else:
                previous_weapon_level = 0
            if (previous_weapon_name, previous_weapon_level) not in added_weapons:
                raise KeyError(
                    f"Line {i}: Manually specified previous weapon ('{previous_weapon_name}', {previous_weapon_level}) "
                    f"has not been added."
                )
            previous_weapon_id = WEAPON_RECIPES[previous_weapon_name]["id"] * 10000 + previous_weapon_level
            previous_weapons.clear()
            weapon_name = weapon_name.strip()
        else:
            if indent > 0 and not previous_weapons:
                raise ValueError(
                    f"Weapon '{weapon_name}' has an indent but there are no previous weapons on the stack.")
            while previous_weapons:
                previous_indent = previous_weapons[-1][1]
                if indent > previous_indent:
                    break  # found correct previous weapon
                # Pop last previous weapon.
                previous_weapons.pop()
            if previous_weapons:
                previous_weapon_id, _ = previous_weapons[-1]
            else:
                previous_weapon_id = None

        if "+" in weapon_name:
            name, level_str = weapon_name.split("+")
            weapon_name = name.strip()
            weapon_level = int(level_str.strip())
        else:
            weapon_level = 0

        try:
            weapon_id = WEAPON_RECIPES[weapon_name]["id"] * 10000 + weapon_level
        except KeyError:
            raise KeyError(f"Line {i}: No weapon recipe for name '{weapon_name}'.")

        if weapon_name in tiers_dict:
            raise KeyError(f"Line {i}: Weapon name '{weapon_name}' appeared multiple times in tiers.")
        tiers_dict[weapon_name] = (weapon_id, previous_weapon_id)
        previous_weapons.append((weapon_id, indent))
        added_weapons.append((weapon_name, weapon_level))

    return tiers_dict


def create_shield_recipe_books():
    """TODO:
        - Assign each shield to a Nomadic Merchant (just do it manually).
        - Create a new recipe book ID for each Nomadic Merchant.
        - Modify shield shop lineup recipe to use that book's flag.

    TODO: Should be called AFTER weapon/shield crafting recipes are done.
    TODO: Set "has book" flags for new books in common EMEVD.
    """


def get_random_material() -> tuple[Materials, int]:
    """Get a random material and drop count based on above dictionary."""
    materials = list(MATERIAL_RARITY_COUNT.keys())
    weights = [v[0] for v in MATERIAL_RARITY_COUNT.values()]
    material = random.choices(materials, weights=weights, k=1)[0]
    return material, random.randint(1, MATERIAL_RARITY_COUNT[material][1])


def replace_merchant_weapons(shop_merchant_param: YappedParam, weapons_param: YappedParam):
    """Replaces weapons sold by merchants with random components.

    Functions basically the same as map item lots.
    """
    price_weight_range = (0.75, 1.25)
    price_m = price_weight_range[1] - price_weight_range[0]
    price_b = price_weight_range[0]

    rows_to_delete = []
    for row in shop_merchant_param.rows:
        if row["equipType"] != "0":
            continue  # ignore non-weapons

        if 100000 <= row.row_id < 100500:
            # Non-Nomadic merchant (other NPC). Continue.
            pass
        elif 100500 <= row.row_id < 101000:
            # Nomadic merchant. Continue.
            pass
        elif 101500 <= row.row_id < 101800:
            # Enia. Can ignore (no weapons).
            continue
        elif 101800 <= row.row_id < 101900:
            # Twin Maiden Husks. Remove weapons with no replacement.
            rows_to_delete.append(row)
            continue
        elif 101900 <= row.row_id < 101950:
            # Remembrance weapons. Remove weapons with no replacement (they can be crafted directly).
            rows_to_delete.append(row)
            continue
        elif 1600000 <= row.row_id:
            # Some kind of debug rows, I think. Change them anyway.
            pass
        else:
            # Skip all other ranges.
            continue

        weapon_id = int(row["equipId"])
        weapon_row = weapons_param[weapon_id]
        if weapon_row is None:
            print(f"Ignoring merchant shop entry {row.row_id} with invalid weapon ID: {weapon_id}")
            continue
        weapon_category = WeaponCategory(int(weapon_row["weaponCategory"]))
        if weapon_category in (WeaponCategory.Arrow, WeaponCategory.Bolt):
            # Ignore ammo.
            continue

        # Get base weapon ID (round down to nearest 10000).
        base_weapon_id = 10000 * (weapon_id // 10000)
        weapon_row = weapons_param[base_weapon_id]

        if not weapon_row.name:
            # Ignore unused weapon drops.
            continue

        good_id, good_count = get_random_material()

        # Get price and randomize it a bit (rounding to nearest 100).
        price_weight = price_b + price_m * random.random()
        good_price = int(100 * round(price_weight * MERCHANT_PRICES[good_id] / 100))

        row["equipId"] = good_id
        row["value"] = good_price
        row["equipType"] = 3  # Good
        row["sellQuantity"] = good_count

        print(f"Merchant shop ID {row.row_id} -> {good_count} {Materials(good_id).name} at {good_price} runes each.")

    for row in rows_to_delete:
        shop_merchant_param.rows.remove(row)


def create_notes_books(goods_param: YappedParam, shop_merchant_param: YappedParam):
    """Create new notes and recipe books and add them to merchant lineup."""


def test_item_lots(item_lots_map: YappedParam):
    """Debugging item lots."""
    item_lots_map[100].name = "Test: Shield Grip"
    item_lots_map[100]["lotItemId01"] = Materials.ShieldGrip
    item_lots_map[100]["lotItemNum01"] = 1

    # cat = item_lots_map.duplicate_row(100, 101, name="Test: Longtail Cat Talisman", )
    # cat["lotItemId01"] = 6040
    # cat["lotItemCategory01"] = 4  # Accessory
    # cat["lotItemNum01"] = 1


def generate_all():
    goods = read_param_csv("EquipParamGoods_vanilla.csv")
    weapons = read_param_csv("EquipParamWeapon_vanilla.csv")
    item_lots_enemy = read_param_csv("ItemLotParam_enemy_vanilla.csv")
    item_lots_map = read_param_csv("ItemLotParam_map_vanilla.csv")
    mtrl = read_param_csv("EquipMtrlSetParam_vanilla.csv")
    shop_recipe = read_param_csv("ShopLineupParam_Recipe_vanilla.csv")
    shop_merchant = read_param_csv("ShopLineupParam_vanilla.csv")

    generate_dummy_weapons(weapons, mtrl, shop_recipe, item_lots_map)

    generate_new_materials(goods)
    generate_new_consumables(goods, shop_recipe, mtrl)

    # TODO: Levelled "Smithing Hammers" (crafted with Smithing Stones) that unlock weapon recipe tiers.
    #  - Novice Smithing Hammer: allows upgrading from weapons with tier 4-7
    #       - Six each of stones [1], [2], [3]
    #       - Three each of Somber stones of same levels
    #  - Journeyman Smithing Hammer: allows upgrading from weapons with tier 8-11
    #       - Six each of stones [4], [5], [6]
    #       - Three each of Somber stones of same levels
    #  - Expert Smithing Hammer: allows upgrading from weapons with tier 12-15
    #       - Nine each of stones [7], [8]
    #       - Nine each of Somber stones of same levels
    #  - Legendary Smithing Hammer: allows upgrading from weapons with tier 16+
    #       - One Ancient Dragon Smithing Stone
    #       - One Somber Ancient Dragon Smithing Stone
    #       - One Meteorite Chunk

    replace_weapon_item_lots(item_lots_enemy, weapons, is_map=False)
    replace_weapon_item_lots(item_lots_map, weapons, is_map=True)
    replace_stone_item_lots(item_lots_enemy, is_map=False)
    replace_stone_item_lots(item_lots_map, is_map=True)
    replace_merchant_weapons(shop_merchant, weapons)
    # TODO: Notes with disease clues for merchants.
    # TODO: New "cookbooks" for consumables, basic weapon crafting, and shield/staff/seal/torch crafting.
    # TODO: Remove class starting weapons and add some starting components instead.

    # TODO: Edit Torrent (NPC param 80000000).
    #  - Less HP.
    #  - Stop Flask of Crimson Tears from healing him.

    # TODO: Remove in final release.
    print("\nNOTE: Debugging item lots created.")
    test_item_lots(item_lots_map)

    write_param_csv(goods, "EquipParamGoods.csv")
    write_param_csv(weapons, "EquipParamWeapon.csv")
    write_param_csv(item_lots_enemy, "ItemLotParam_enemy.csv")
    write_param_csv(item_lots_map, "ItemLotParam_map.csv")
    write_param_csv(mtrl, "EquipMtrlSetParam.csv")
    write_param_csv(shop_recipe, "ShopLineupParam_Recipe.csv")
    write_param_csv(shop_merchant, "ShopLineupParam.csv")

    print("Read, edited, and wrote all Yapped param CSVs successfully.")


if __name__ == '__main__':
    generate_all()
