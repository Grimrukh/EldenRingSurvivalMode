"""Scripts for generating Params (regulation.bin).

Modifies CSV files exported by Yapped (Rune Bear), which that program can then re-import.

- In Yapped, import all the CSV param files generated from here:
    - EquipMtrlSetParam
    - EquipParamGoods
    - EquipParamWeapon
    - ItemLotParam_enemy
    - ItemLotParam_map
    - Npc_Param
    - ShopLineupParam
    - ShopLineupParam_Recipe
- Ensure that manually-set Yapped tables are also imported:
    - CharaInitParam
    - SpEffectParam
- Save Yapped to generate final `regulation.bin`.

TODO: Will need to undo CharaInit changes without WEAPONS activated.
"""
from __future__ import annotations

import csv
import random
import re
import shutil
from pathlib import Path

from survival_goods import *
from survival_text import read_weapon_text, write_weapon_text
from enemy_ids import EXTRA_ENEMY_DROPS
from weapon_recipes import WEAPON_RECIPES

READ_CSV_PATH = Path(r"C:\Dark Souls\Tools\Params\Yapped Rune Bear 2.1.4\Projects\ExampleMod\CSV\ER")
WRITE_CSV_PATH = Path(r"C:\Dark Souls\Projects\EldenRingSurvivalMode\EldenRingSurvivalMode\CSV")

DO_SURVIVAL = True
DO_WEAPONS = True
DO_DISEASES = True


def do_category(info_dict):
    if info_dict["category"] == ModSubcategory.Survival:
        return DO_SURVIVAL
    if info_dict["category"] == ModSubcategory.Weapons:
        return DO_WEAPONS
    if info_dict["category"] == ModSubcategory.Diseases:
        return DO_DISEASES
    else:
        raise ValueError(f"Invalid mod category: {info_dict['category']}")


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
    return YappedParam.from_csv_path((READ_CSV_PATH / param_name).with_suffix(".csv"))


def write_param_csv(param: YappedParam, param_name: str):
    param_path = WRITE_CSV_PATH / param_name
    param_path.parent.mkdir(parents=True, exist_ok=True)
    param.write_csv(param_path.with_suffix(".csv"))


# Mostly boss rewards. These will be replaced if they exist, or added otherwise.
MANUAL_ITEM_LOTS = {
    # Bosses
    10012: ("[Stormveil - Godrick] Gruesome Bone", Materials.GruesomeBone, 1),
    10030: ("[Chapel of Anticipation - Grafed Scion] Metal Plate", Materials.MetalPlate, 1),
    10031: ("[Chapel of Anticipation - Grafed Scion] Shield Grip", Materials.ShieldGrip, 1),
    10042: ("[Leyndell - Morgott] Erdtree Amber", Materials.ErdtreeAmber, 2),
    10060: ("[Ashen Leyndell - Gideon] Glintstone Dust", Materials.GlintstoneDust, 3),
    10071: ("[Ashen Leyndell - Hoarah Loux] Erdtree Amber", Materials.ErdtreeAmber, 2),
    10081: ("[Lake of Rot - Astel] Meteorite Chunk", Materials.MeteoriteChunk, 3),
    10100: ("[Siofra - Valiant Gargoyle] Metal Plate", Materials.MetalPlate, 2),
    10101: ("[Siofra - Valiant Gargoyle] Gruesome Bone", Materials.GruesomeBone, 2),
    10111: ("[Deeproot Depths - Fortissax] Dragon Teeth", Materials.DragonTeeth, 3),
    10122: ("[Mohgwyn Palace - Mohg] Gruesome Bone", Materials.GruesomeBone, 5),
    10142: ("[Farum Azula - Godskin Duo]", Materials.BlackMark, 1),
    10151: ("[Farum Azula - Dragonlord Placidusax] Dragon Teeth", Materials.DragonTeeth, 4),
    10161: ("[Farum Azula - Maliketh] Black Mark", Materials.BlackMark, 3),
    10171: ("[Raya Lucaria - Red Wolf of Radagon]", Materials.GlintstoneDust, 2),
    10182: ("[Raya Lucaria - Rennala] Glintstone Dust", Materials.GlintstoneDust, 5),
    10191: ("[Haligtree - Loretta] Erdtree Amber", Materials.ErdtreeAmber, 1),
    10202: ("[Haligtree - Malenia] Pliable Metal", Materials.PliableMetal, 5),
    10210: ("[Volcano Manor - Godskin Noble] Black Mark", Materials.BlackMark, 1),
    10222: ("[Mt. Gelmir - Rykard] Pliable Metal", Materials.PliableMetal, 3),
    10241: ("[Shunning-Grounds - Mohg] Gruesome Bone", Materials.GruesomeBone, 2),
    10260: ("[Ruin-Strewn Precipice - Magma Wyrm Makar] Pliable Metal", Materials.PliableMetal, 2),
    10290: ("[Volcano Manor - Abducator Virgins] Metal Plate", Materials.MetalPlate, 2),
    10302: ("[Caelid - Radahn] Meteorite Chunk", Materials.MeteoriteChunk, 3),
    10311: ("[Mountaintops - Fire Giant] Gruesome Bone", Materials.GruesomeBone, 3),
    10321: ("[Siofra - Ancestor Spirit] Refined Wood", Materials.RefinedWood, 2),
    10331: ("[Nokron - Regal Ancestor Spirit] Refined Wood", Materials.RefinedWood, 3),
    10342: ("[Nokron - Mimic Tear] Pliable Metal", Materials.PliableMetal, 1),
    10351: ("[Deeproot Depths - Fia's Champions]", Materials.MetalPlate, 3),
    10734: ("[Mountaintops - Sanguine Noble]", Materials.PliableMetal, 1),
    10741: ("[Capital Outskirts - Fell Twins]", Materials.GruesomeBone, 2),
    10800: ("[Weeping Penisula - Leonine Misbegotten] Metal Plate", Materials.MetalPlate, 2),
    10810: ("[Caria Manor - Loretta] String", Materials.String, 5),
    10812: ("[Caria Manor - Loretta] Glintstone Dust", Materials.GlintstoneDust, 3),
    10820: ("[Shaded Castle - Elemer of the Briar] Metal Plate", Materials.MetalPlate, 2),
    10821: ("[Shaded Castle - Elemer of the Briar] Shield Grip", Materials.ShieldGrip, 1),
    10830: ("[Redmane Castle - Misbegotten Warrior/Crucible Knight] Metal Plate", Materials.MetalPlate, 2),
    10840: ("[Castle Sol - Commander Niall] Pliable Metal", Materials.PliableMetal, 2),
    # Generic dungeons
    20001: ("[Tombsward Catacombs - Cemetery Shade] Metal Plate", Materials.MetalPlate, 1),
    20011: ("[Impaler's Catacombs - Erdtree Burial Watchdog] Metal Shards", Materials.MetalShards, 5),
    20021: ("[Stormfoot Catacombs - Erdtree Burial Watchdog] Metal Plate", Materials.MetalPlate, 1),
    20031: ("[Deathtouched Catacombs - Black Knife Assassin] Black Mark", Materials.BlackMark, 1),
    20040: ("[Murkwater Catacombs - Grave Warden Duelist] Metal Plate", Materials.MetalPlate, 1),
    20051: ("[Black Knife Catacombs - Cemetery Shade] Metal Plate", Materials.MetalPlate, 2),
    20061: ("[Road's End Catacombs - Spirit-caller Snail] Glintstone Dust", Materials.GlintstoneDust, 3),
    20071: ("[Cliffbottom Catacombs - Erdtree Burial Watchdog] Meteorite Chunk", Materials.MeteoriteChunk, 1),
    20091: ("[Gelmir's Heo's Grave - Mt. Gelmir] Pliable Metal", Materials.PliableMetal, 1),
    20100: ("[Auriza Hero's Grave - Crucible Knight Ordovis] Refined Wood", Materials.RefinedWood, 3),
    20111: ("[Unslightly Catacombs - Perfumer Tricia] Refined Wood", Materials.RefinedWood, 2),
    20121: ("[Wyndham Catacombs - Erdtree Burial Watchdog] Metal Plate", Materials.MetalPlate, 1),
    20131: ("[Auriza Side Tomb - Grave Warden Duelist] Pliable Metal", Materials.PliableMetal, 1),
    20141: ("[Minor Erdtree Catacombs - Erdtree Burial Watchdog] Metal Plate", Materials.MetalPlate, 2),
    20151: ("[Caelid Catacombs - Cemetery Shade] Gruesome Bone", Materials.GruesomeBone, 1),
    20162: ("[War-Dead Catacombs - Putrid Tree Spirit] Erdtree Wood", Materials.ErdtreeWood, 1),
    20170: ("[Giant-Conquering Hero's Grave - Ancient Hero of Zamor] Pliable Metal", Materials.PliableMetal, 2),
    20182: ("[Giants' Mountaintop Catacombs - Ulcerated Tree Spirit] Erdtree Wood", Materials.ErdtreeWood, 1),
    20192: ("[Consecrated Snowfiled Catacombs - Putrid Grave Warden Duelist] Metal Plate", Materials.MetalPlate, 2),
    20201: ("[Hidden Path ot the Haligtree - Stray Mimic Tear] Pliable Metal", Materials.PliableMetal, 2),
    20212: ("[Black Knife Catacombs - Black Knife Assassin] Black Mark", Materials.BlackMark, 1),
    20221: ("[Leyndell Catacombs - Esgar, Priest of Blood] Gruesome Bone", Materials.GruesomeBone, 1),
    20301: ("[Tombsward Cave - Miranda the Blighted Bloom] Refined Wood", Materials.RefinedWood, 1),
    20311: ("[Earthbore Cave - Runebear] Gruesome Bone", Materials.GruesomeBone, 1),
    20331: ("[Groveside Cave - Beastman of Farum Azula] Metal Plate", Materials.MetalPlate, 1),
    20342: ("[Coastal Cave - Demi-Human Chief] Metal Shards", Materials.MetalShards, 5),
    20351: ("[Highroad Cave - Guardian Golem] Metal Plate", Materials.MetalPlate, 1),
    20361: ("[Stillwater Cave - Cleanrot Knight] Metal Plate", Materials.MetalPlate, 1),
    20371: ("[Lakeside Crystal Cave - Bloodhound Knight] Metal Shards", Materials.MetalShards, 7),
    20381: ("[Academy Crystal Cave - Crystalians] Glintstone Dust", Materials.GlintstoneDust, 2),
    20391: ("[Seethewater Cave - Kindred of Rot] Gruesome Bone", Materials.GruesomeBone, 1),
    20400: ("[Volcano Cave - Demi-human Queen Margot] Metal Shards", Materials.MetalShards, 6),
    20411: ("[Omenkiller - Perfumer's Grotto] Metal Plate", Materials.MetalPlate, 1),
    20421: ("[Sage's Cave - Black Knife Assassin] Pliable Metal", Materials.PliableMetal, 1),
    20431: ("[Goal Cave - Frenzied Duelist] Metal Plate", Materials.MetalPlate, 1),
    20441: ("[Dragonbarrow Cave - Beastman of Farum Azula] Metal Shards", Materials.MetalShards, 10),
    20451: ("[Abandoned Cave - Cleanrot Knight Duo] Metal Plate", Materials.MetalPlate, 2),
    20461: ("[Sellia Hideaway - Putrid Crystalians] Meteorite Chunk", Materials.MeteoriteChunk, 1),
    20470: ("[Cave of the Forlorn - Misbegotten Crusader] Erdtree Wood", Materials.ErdtreeWood, 2),
    20482: ("[Spiritcaller's Cave - Godskin Apostle/Noble] Pliable Metal", Materials.PliableMetal, 2),
    20490: ("[Sage's Cave - Necromancer Garris] Staff Pole", Materials.StaffPole, 1),
    20491: ("[Sage's Cave - Necromancer Garris] Gruesome Bone", Materials.GruesomeBone, 1),
    20600: ("[Morne Tunnel - Scaly Misbegotten] Metal Plate", Materials.MetalPlate, 1),
    20611: ("[Limgrave Tunnels - Stonedigger Troll] Metal Shards", Materials.MetalShards, 3),
    20621: ("[Raya Lucaria Crystal Tunnel - Crystalian] Metal Shards", Materials.MetalShards, 5),
    20630: ("[Old Altus Tunnel - Stonedigger Troll] Gruesome Bone", Materials.GruesomeBone, 1),
    20640: ("[Sealed Tunnel - Onyx Lord] Meteorite Chunk", Materials.MeteoriteChunk, 1),
    20651: ("[Altus Tunnel - Crystalians] Meteorite Chunk", Materials.MeteoriteChunk, 1),
    20661: ("[Gael Tunnel - Magma Wyrm] Pliable Metal", Materials.PliableMetal, 1),
    20670: ("[Sellia Crystal Tunnel - Fallingstar Beast] Meteorite Chunk", Materials.MeteoriteChunk, 1),
    20681: ("[Yelough Anix Tunnel - Astel] Meteorite Chunk", Materials.MeteoriteChunk, 2),
    # Overworld bosses
    30100: ("[Limgrave - Field - Tree Sentinel] Metal Plate", Materials.MetalPlate, 1),
    30111: ("[Limgrave - Field - Flying Dragon Agheel] Dragon Teeth", Materials.DragonTeeth, 1),
    30121: ("[Limgrave - Evergaol - Crucible Knight] Refined Wood", Materials.RefinedWood, 1),
    30130: ("[Limgrave - Evergaol - Bloodhound Knight Darriwil] Pliable Metal", Materials.PliableMetal, 1),
    30172: ("[Limgrave - Field - Tibia Mariner] Gruesome Bone", Materials.GruesomeBone, 1),
    30187: ("[Weeping Penisula - Field - Erdtree Avatar] Erdtree Wood", Materials.ErdtreeWood, 1),
    30203: ("[Liurnia - Field - Erdtree Avatar] Erdtree Wood", Materials.ErdtreeWood, 1),
    30207: ("[Liurnia - Field - Erdtree Avatar] Erdtree Wood", Materials.ErdtreeWood, 1),
    30211: ("[Liurnia - Field - Glintstone Dragon Smarag] Dragon Teeth", Materials.DragonTeeth, 1),
    30226: ("[Liurnia - Field - Omenkiller] Metal Plate", Materials.MetalPlate, 1),
    30242: ("[Liurnia - Field - Tibia Mariner] Gruesome Bone", Materials.GruesomeBone, 1),
    30246: ("[Liurnia - Evergaol - Adan, Thief of Fire] Pliable Metal", Materials.PliableMetal, 1),
    30251: ("[Liurnia - Evergaol - Bols, Carian Knight] Glintstone Dust", Materials.GlintstoneDust, 2),
    30256: ("[Liurnia - Evergaol - Onyx Lord] Meteorite Chunk", Materials.MeteoriteChunk, 1),
    30262: ("[Liurnia - Field - Glintstone Dragon Adula] Dragon Teeth", Materials.DragonTeeth, 1),
    30266: ("[Liurnia - Evergaol - Alecto, Black Knife Ringleader] Black Mark", Materials.BlackMark, 1),
    30301: ("[Altus Plateau - Field - Ancient Dragon Lansseax] Dragon Teeth", Materials.DragonTeeth, 1),
    30310: ("[Altus Plateau - Field - Fallingstar Beast] Meteorite Chunk", Materials.MeteoriteChunk, 1),
    30315: ("[Capital Outskirts - Field - Draconic Tree Sentinel] Metal Plate", Materials.MetalPlate, 1),
    30316: ("[Capital Outskirts - Field - Draconic Tree Sentinel] Shield Grip", Materials.ShieldGrip, 1),
    30322: ("[Altus Plateau - Field - Wormface] Erdtree Wood", Materials.ErdtreeWood, 1),
    30327: ("[Altus Plateau - Field - Godskin Apostle] Pliable Metal", Materials.PliableMetal, 1),
    30335: ("[Capital Outskirts - Field - Tree Sentinel Duo] Metal Plate", Materials.MetalPlate, 2),
    30350: ("[Altus Plateau - Field - Black Knife Assassin] Black Mark", Materials.BlackMark, 1),
    30377: ("[Mt. Gelmir - Field - Full-grown Fallingstar Beast] Meteorite Chunk", Materials.MeteoriteChunk, 2),
    30382: ("[Mt. Gelmir - Field - Ulcerated Tree Spirit] Erdtree Wood", Materials.ErdtreeWood, 1),
    30387: ("[Altus Plateau - Field - Tibia Mariner] Gruesome Bone", Materials.GruesomeBone, 1),
    30390: ("[Mt. Gelmir - Field - Magma Wyrm] Pliable Metal", Materials.PliableMetal, 1),
    30396: ("[Mt. Gelmir - Field - Demi-Human Queen Maggie] Staff Pole", Materials.StaffPole, 1),
    30400: ("[Mt. Gelmir - Field - Magma Wyrm] Pliable Metal", Materials.PliableMetal, 1),
    30405: ("[Caelid - Field - Commander O'Neil] Staff Pole", Materials.StaffPole, 1),
    30412: ("[Caelid - Field - Erdtree Avatar] Erdtree Wood", Materials.ErdtreeWood, 1),
    30417: ("[Caelid - Field - Putrid Avatar] Erdtree Wood", Materials.ErdtreeWood, 1),
    30421: ("[Caelid - Field - Flying Dragon Greyll] Dragon Teeth", Materials.DragonTeeth, 1),
    30425: ("[Caelid - Field - Blade Blade Kindred] Black Mark", Materials.BlackMark, 1),
    30426: ("[Caelid - Field - Blade Blade Kindred] Gruesome Bone", Materials.GruesomeBone, 1),
    30505: ("[Forbidden Lands - Field - Black Blade Kindred] Black Mark", Materials.BlackMark, 1),
    30506: ("[Forbidden Lands - Field - Black Blade Kindred] Gruesome Bone", Materials.GruesomeBone, 1),
    30511: ("[Mountaintops of the Giants - Field - Borealis, the Freezing Fog] Dragon Teeth", Materials.DragonTeeth, 1),
    30520: ("[Mountaintops of the Giants - Evergaol - Roundtable Knight Vyke] Metal Plate", Materials.MetalPlate, 2),
    30527: ("[Mountaintops of the Giants - Field - Erdtree Avatar] Erdtree Wood", Materials.ErdtreeWood, 2),
    30530: ("[Mountaintops of the Giants - Field - Death Rite Bird] Black Mark", Materials.BlackMark, 1),
    30551: ("[Mountaintops of the Giants - Field - Great Wyrm Theodorix] Dragon Teeth", Materials.DragonTeeth, 1),
    30557: ("[Consecrated Snowfield - Field - Putrid Avatar] Erdtree Wood", Materials.ErdtreeWood, 1),
    30600: ("[Lake of Rot - Dragonkin Soldier] Dragon Teeth", Materials.DragonTeeth, 1),
    30620: ("[Siofra River - Dragonkin Soldier] Dragon Teeth", Materials.DragonTeeth, 1),

    # Other
    80320: ("[Reward - \"Champion's Song\" Painting] Harp Bow", Materials.ErdtreeAmber, 1),

    # NPC gifts
    100360: ("[White-Faced Varre - Invasion] Metal Shards", Materials.MetalShards, 10),
    100770: ("[Tanith] Gruesome Bone", Materials.GruesomeBone, 3),
    101580: ("[Blaidd is the Half-Wolf] Metal Plate", Materials.MetalPlate, 3),
    101630: ("[Bloody Finger Hunter Yura] Metal Plate", Materials.MetalPlate, 1),
    102200: ("[Kenneth Haight] Erdtree Amber", Materials.ErdtreeAmber, 1),
    102860: ("[Gideon Ofnir - Boss Drop] Glintstone Dust", Materials.GlintstoneDust, 3),
    102921: ("[Knight Bernahl] Gruesome Bone", Materials.GruesomeBone, 2),
    103010: ("[Big Boggart] Metal Plate", Materials.MetalPlate, 1),
    103022: ("[Big Boggart] Metal Plate", Materials.MetalPlate, 1),
    103410: ("[Prince of Death's Throne] Black Mark", Materials.BlackMark, 1),
    103500: ("[Sorcerer Rogier] Glintstone Dust", Materials.GlintstoneDust, 2),
    103580: ("[Sorcerer Rogier] Glintstone Dust", Materials.GlintstoneDust, 2),
    103930: ("[Ranni the Witch] Meteorite Chunk", Materials.MeteoriteChunk, 4),
    104500: ("[Juno Hoslow] Metal Shards", Materials.MetalShards, 5),
    104510: ("[Juno Hoslow] Metal Shards", Materials.MetalShards, 5),

    # Corpses
    110300: ("[Corpse - White-Faced Varre - Invasion] Metal Shards", Materials.MetalShards, 10),
    110600: ("[Corpse - Edgar] Metal Plate", Materials.MetalPlate, 1),
    110610: ("[Corpse - Edgar] Metal Plate", Materials.MetalPlate, 1),
    110621: ("[Corpse - Edgar] Metal Plate", Materials.MetalPlate, 1),
    111500: ("[Corpse - Blaidd is the Half-Wolf] Metal Plate", Materials.MetalPlate, 3),
    111600: ("[Corpse - Bloody Finger Hunter Yura] Metal Plate", Materials.MetalPlate, 1),
    112901: ("[Corpse - Knight Bernahl] Gruesome Bone", Materials.GruesomeBone, 2),
    113002: ("[Corpse - Big Boggart] Metal Plate", Materials.MetalPlate, 1),
    113012: ("[Corpse - Big Boggart] Metal Plate", Materials.MetalPlate, 1),
    113410: ("[Corpse - Prince of Death's Throne] Black Mark", Materials.BlackMark, 1),
    113420: ("[Corpse - Prince of Death's Throne] Black Mark", Materials.BlackMark, 1),
    113601: ("[Corpse - Thops] Staff Pole", Materials.StaffPole, 1),
    113701: ("[Corpse - Brother Corhyn] Metal Shards", Materials.MetalShards, 3),
    113800: ("[Corpse - Dung Eater] Metal Plate", Materials.MetalPlate, 1),
    113820: ("[Corpse - Dung Eater] Metal Plate", Materials.MetalPlate, 1),
    114210: ("[Corpse - Nepheli Loux] Metal Plate", Materials.MetalPlate, 1),
    114211: ("[Corpse - Nepheli Loux] Metal Plate", Materials.MetalPlate, 1),
    114500: ("[Corpse - Juno Hoslow] Metal Shards", Materials.MetalShards, 5),
}


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
    if not DO_WEAPONS:
        return

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

        weapon_root_index = row.row_id // 10000  # e.g., 1000 for Dagger
        dummy_id = dummy_offset + 100 * weapon_root_index
        shop_id = new_shop_offset + weapon_root_index
        mtrl_id = new_mtrl_offset + 10 * weapon_root_index
        item_lot_id = item_lot_offset + 100 * weapon_root_index
        weapon_base_id = 10000 * weapon_root_index

        try:
            recipe_info = WEAPON_RECIPES[row.name]
        except KeyError:
            raise KeyError(f"Weapon '{row.name}' is missing from WEAPON_RECIPES.")

        try:
            true_weapon_id, previous_weapon_id = tiers_dict[row.name]
        except KeyError:
            # Weapon is not in the upgrade tree, and is simply crafted from scratch (Shields, Staffs, Seals, Torches).
            true_weapon_id = row.row_id  # no upgrade level (can be upgrading normally at blacksmith)
            previous_weapon_id = None  # no previous weapon in recipe
            hammer_id = -1  # 'AllowWeaponUpgrade' event not needed
            try:
                visibility_flag = recipe_info["visibility_flag"]
            except KeyError:
                raise KeyError(f"Non-tiered weapon '{row.name}' does not have a 'visibility_flag' in recipe dict.")
            try:
                rune_cost = recipe_info["cost"]
            except KeyError:
                raise KeyError(f"Non-tiered weapon '{row.name}' does not have a 'cost' in recipe dict.")
        else:
            tier = recipe_info["tier"]
            if previous_weapon_id is None:
                # Recipe must have a 'visibility_flag' (usually zero).
                try:
                    visibility_flag = recipe_info["visibility_flag"]
                except KeyError:
                    raise KeyError(f"Basic weapon '{row.name}' does not have a 'visibility_flag' in recipe dict.")
                try:
                    rune_cost = recipe_info["cost"]
                except KeyError:
                    raise KeyError(f"Basic weapon '{row.name}' does not have a 'cost' in recipe dict.")
            else:
                # Visibility flag is determined by monitoring previous weapon ID (and potentially a Smith's Hammer).
                previous_weapon_base_id = 10000 * (previous_weapon_id // 10000)  # ignore upgrade level
                previous_weapon_name = weapon_param[previous_weapon_base_id].name
                visibility_flag = Flags.AllowWeaponUpgradeFlag + new_weapon_indices.index(previous_weapon_name)

                # Determine rune cost for crafting from upgrade level.
                rune_cost = tier * 1000

            # Determine Hammer required to upgrade weapon from its tier (for EMEVD printing only).
            if 0 <= tier <= 2:
                hammer_id = 0  # no hammer required
            elif 3 <= tier <= 5:
                hammer_id = SmithsHammers.NoviceSmithsHammer.value
            elif 6 <= tier <= 8:
                hammer_id = SmithsHammers.ApprenticeSmithsHammer.value
            elif 9 <= tier <= 11:
                hammer_id = SmithsHammers.JourneymanSmithsHammer.value
            elif 12 <= tier <= 14:
                hammer_id = SmithsHammers.ExpertSmithsHammer.value
            elif 15 <= tier:
                hammer_id = SmithsHammers.MasterSmithsHammer.value
            else:
                raise ValueError(f"Invalid tier for weapon '{row.name}': {tier}")

            # Tiered weapon cannot be reinforced (including infused/affinity variants).
            row["materialSetId"] = -1
            for infusion_variant in range(0, 1201, 100):
                infusion_row = weapon_param[weapon_base_id + infusion_variant]
                if infusion_row is not None:  # many weapons cannot be infused (ignore these)
                    for origin_level in range(26):
                        origin_field = "originEquipWep" if origin_level == 0 else f"originEquipWep{origin_level}"
                        infusion_row[origin_field] = -1

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

        # Copy FMG names and captions (but add Hammer to both captions if required).
        names[dummy_id] = names[weapon_base_id]
        if hammer_id > 0:
            hammer_name = NEW_SMITHS_HAMMERS[hammer_id]["name"]
            new_caption = f"{captions[weapon_base_id]}\n\n{hammer_name} is required to upgrade it."
        elif hammer_id == 0:
            new_caption = f"{captions[weapon_base_id]}\n\nCan be upgraded without a Smith's Hammer."
        else:  # standard reinforcement
            new_caption = captions[weapon_base_id]
        captions[dummy_id] = captions[weapon_base_id] = new_caption
        # TODO: Haven't checked that all weapon captions can support two extra lines, but I'm optimistic.

        # Create item lot for awarding real weapon.
        new_item_lot = item_lots_map_param.duplicate_row(item_lot_source, item_lot_id)
        new_item_lot.name = f"{row.name} (crafted)"
        new_item_lot["lotItemId01"] = true_weapon_id  # potentially upgraded version
        new_item_lot["lotItemCategory01"] = 2  # Weapon
        new_item_lot["lotItemNum01"] = 1

        # Create recipe entry.
        new_shop_row = shop_recipe_param.duplicate_row(shop_source, shop_id)
        new_shop_row.name = row.name
        new_shop_row["equipId"] = dummy_id
        new_shop_row["sellQuantity"] = -1
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
        # allow_weapon_upgrade_flag = Flags.AllowWeaponUpgradeFlag + new_weapon_indices.index(row.name)
        # if hammer_id != -1:
        #     print(
        #         f"AllowWeaponUpgrade({slot}, {true_weapon_id}, {hammer_id}, {allow_weapon_upgrade_flag})"
        #     )
        slot += 1

        # Create ingredients entry.
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


def generate_smiths_hammers(
    goods_param: YappedParam, shop_recipe_param: YappedParam, equip_mtrl_set_param: YappedParam
):
    """Recipes for new Smith's Hammers, which allow further weapon upgrades."""
    if not DO_WEAPONS:
        return

    # Goods
    # TODO: This is definitely a Key Item, but Hammers appear as 'reusable' in crafting menu. Probably no solution.
    goods_source = 8590  # Whetstone Knife

    # "Shop" lineup entries
    new_shop_offset = 32600
    shop_source = 1  # unnamed

    # Ingredients
    new_mtrl_offset = 326000
    mtrl_source = 320010  # 3x Thin Beast Bones

    for i, (good_id, good_info) in enumerate(NEW_SMITHS_HAMMERS.items()):
        shop_id = new_shop_offset + i
        mtrl_id = new_mtrl_offset + 10 * i

        new_good_row = goods_param.duplicate_row(goods_source, good_id)
        new_good_row.name = good_info["name"]
        new_good_row["iconId"] = good_info["icon"]
        # TODO: Sort ID?

        new_shop_row = shop_recipe_param.duplicate_row(shop_source, shop_id)
        new_shop_row.name = good_info["name"]
        new_shop_row["equipId"] = good_id
        new_shop_row["sellQuantity"] = -1
        new_shop_row["mtrlId"] = mtrl_id
        new_shop_row["eventFlag_forRelease"] = good_info["recipe_visibility_flag"]
        new_shop_row["equipType"] = 3  # always Goods
        new_shop_row["setNum"] = 1  # only one

        new_mtrl_row = equip_mtrl_set_param.duplicate_row(mtrl_source, mtrl_id)
        new_mtrl_row.name = good_info["name"]
        for j, (count, ingredient) in enumerate(good_info["recipe"]):
            new_mtrl_row[f"materialId{j + 1:02d}"] = ingredient.value
            new_mtrl_row[f"itemNum{j + 1:02d}"] = count
            new_mtrl_row[f"materialCate{j + 1:02d}"] = 4  # always Goods


def generate_new_consumables(
    goods_param: YappedParam, shop_recipe_param: YappedParam, equip_mtrl_set_param: YappedParam
):
    """Recipes for new "survival" goods (food, drink, protection)."""

    # Goods
    goods_source = 1110  # Immunizing Cured Meat

    # "Shop" lineup entries
    new_shop_offset = 32500
    shop_source = 1  # unnamed

    # Ingredients
    new_mtrl_offset = 325000
    mtrl_source = 320010  # 3x Thin Beast Bones

    for i, (good_id, good_info) in enumerate(NEW_CONSUMABLES.items()):
        if not do_category(good_info):
            continue

        shop_id = new_shop_offset + i
        mtrl_id = new_mtrl_offset + 10 * i

        new_good_row = goods_param.duplicate_row(goods_source, good_id)
        new_good_row.name = good_info["name"]
        new_good_row["refId_default"] = good_info["effect"]
        new_good_row["sellValue"] = -1
        new_good_row["iconId"] = good_info["icon"]
        new_good_row["goodsUseAnim"] = good_info["animation"].value
        # TODO: Probably other stuff too (e.g., VFX).
        # TODO: Sort ID?

        new_shop_row = shop_recipe_param.duplicate_row(shop_source, shop_id)
        new_shop_row.name = good_info["name"]
        new_shop_row["equipId"] = good_id
        new_shop_row["sellQuantity"] = -1
        new_shop_row["value"] = 0  # no rune cost for these
        new_shop_row["mtrlId"] = mtrl_id
        new_shop_row["eventFlag_forRelease"] = good_info["recipe_visibility_flag"]
        new_shop_row["equipType"] = 3  # always Goods
        new_shop_row["setNum"] = 1  # only one

        new_mtrl_row = equip_mtrl_set_param.duplicate_row(mtrl_source, mtrl_id)
        new_mtrl_row.name = good_info["name"]
        for j, (count, ingredient) in enumerate(good_info["recipe"]):
            new_mtrl_row[f"materialId{j + 1:02d}"] = ingredient.value
            new_mtrl_row[f"itemNum{j + 1:02d}"] = count
            new_mtrl_row[f"materialCate{j + 1:02d}"] = 4  # always Goods


def generate_new_materials(goods_param: YappedParam):
    """Add new crafting material Goods. Relatively simple."""
    source_row = 15000  # Sliver of Meat
    for good_id, good_info in NEW_MATERIALS.items():
        if not do_category(good_info):
            continue
        new_material = goods_param.duplicate_row(source_row, good_id)
        new_material.name = good_info["name"]
        new_material["iconId"] = good_info["icon"]
        new_material["sortGroupId"] = 40


def add_stone_recipes(mtrl_param: YappedParam, shop_recipe_param: YappedParam):
    """Add recipes (always available) that let you 'break' [Somber] Smithing Stones into [Somber] Stone Fragments."""
    if not DO_WEAPONS:
        return

    # "Shop" recipe lineup entries
    new_shop_offset = 32700
    shop_source = 1  # unnamed

    # Ingredients
    new_mtrl_offset = 327000
    mtrl_source = 320010  # 3x Thin Beast Bones

    # Each Stone level (1 to 8) can be broken to get you HALF that many Fragments, rounded down.
    # So Smithing Stone [1] and Smithing Stone [2] both get you one Stone Fragment.
    for stone_level, fragment_count in zip(
        (0, 1, 2, 3, 4, 5, 6, 7),  # [Somber] Smithing Stone [1] to [8]
        (1, 1, 2, 2, 3, 3, 4, 4),
    ):
        # Standard
        new_shop_row = shop_recipe_param.duplicate_row(shop_source, new_shop_offset + stone_level)
        new_shop_row.name = f"Stone Fragment x{fragment_count}"
        new_shop_row["equipId"] = Materials.StoneFragment
        new_shop_row["sellQuantity"] = -1
        new_shop_row["value"] = 0  # no rune cost for these
        new_shop_row["mtrlId"] = new_mtrl_offset + stone_level
        new_shop_row["eventFlag_forRelease"] = 0  # always available
        new_shop_row["equipType"] = 3  # always Goods
        new_shop_row["setNum"] = fragment_count

        new_mtrl_row = mtrl_param.duplicate_row(mtrl_source, new_mtrl_offset + stone_level)
        new_mtrl_row.name = f"Stone Fragment x{fragment_count}"
        new_mtrl_row["materialId01"] = Materials.SmithingStone1 + stone_level
        new_mtrl_row["itemNum01"] = 1
        new_mtrl_row["materialCate01"] = 4  # always Goods

        # Somber
        new_shop_row = shop_recipe_param.duplicate_row(shop_source, new_shop_offset + stone_level + 10)
        new_shop_row.name = f"Somber Stone Fragment x{fragment_count}"
        new_shop_row["equipId"] = Materials.SomberStoneFragment
        new_shop_row["sellQuantity"] = -1
        new_shop_row["value"] = 0  # no rune cost for these
        new_shop_row["mtrlId"] = new_mtrl_offset + stone_level + 10
        new_shop_row["eventFlag_forRelease"] = 0  # always available
        new_shop_row["equipType"] = 3  # always Goods
        new_shop_row["setNum"] = fragment_count

        new_mtrl_row = mtrl_param.duplicate_row(mtrl_source, new_mtrl_offset + stone_level + 10)
        new_mtrl_row.name = f"Somber Stone Fragment x{fragment_count}"
        new_mtrl_row["materialId01"] = Materials.SomberSmithingStone1 + stone_level
        new_mtrl_row["itemNum01"] = 1
        new_mtrl_row["materialCate01"] = 4  # always Goods


def replace_stone_item_lots(item_lots_param: YappedParam, is_map: bool):
    """Replace [Somber] Smithing Stones with [Somber] Stone Fragments, some percentage of the time.

    Stone Fragment drop count depends on the level of the Smithing Stone it is replacing.

    Ancient Dragon (max level) stones are not replaced.
    """
    if not DO_WEAPONS:
        return

    leave_odds = 0.2  # proportion of item lots to leave as Smithing Stones
    fragment_odds = 0.75  # rather than Metal Shards

    for row in item_lots_param.rows:
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
                # Metal Shards instead
                good_id = Materials.MetalShards

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


def fix_enemy_item_lots(item_lots_param: YappedParam, weapons_param: YappedParam):
    if not DO_WEAPONS:
        return

    item_lot_source = 227000000  # Giant Crab (Crab Eggs)

    def find_item_lot(first_item_lot: int):
        """Find item lot to use for new drop, which must be within 10 of `first_item_lot`."""
        for i in range(10):
            item_lot = item_lots_param[first_item_lot + i]
            if item_lot is None:
                # Use this lot (new ID).
                return item_lots_param.duplicate_row(item_lot_source, first_item_lot + i)
            else:
                if int(item_lot["lotItemCategory01"]) == 0 and int(item_lot["lotItemCategory02"]) == 2:
                    # Replace non-guaranteed weapon (it will be deleted later otherwise anyway).
                    return item_lot
                elif all(int(item_lot[f"lotItemCategory{s:02d}"]) == 0 for s in range(1, 9)):
                    # Replace empty item lot.
                    return item_lot
        else:
            raise ValueError(f"Could not find a free item lot within 10 of: {first_item_lot}")

    for good_id, enemies in EXTRA_ENEMY_DROPS.items():
        # Find every "base" item lot for this enemy (row IDs that are zero modulo 100).
        for (model_id, odds) in enemies:
            first_lot = model_id * 100000
            enemy_base_lots = [
                row for row in item_lots_param.rows
                if first_lot <= row.row_id <= first_lot + 99999
                and row.row_id % 10 == 0
            ]
            for base_lot in enemy_base_lots:
                row = find_item_lot(base_lot.row_id)

                if base_lot.name:
                    row.name = base_lot.name.split("]")[0] + "]" + f" {good_id.name}"
                else:
                    row.name = f"[Drop] {good_id.name}"

                # First slot: no drop.
                row["lotItemId01"] = 0
                row["lotItemCategory01"] = 0  # None
                row["lotItemNum01"] = 0
                row["lotItemBasePoint01"] = 1000 - odds

                # Second slot: drop.
                row["lotItemId02"] = good_id
                row["lotItemCategory02"] = 1  # Good
                row["lotItemNum02"] = 1
                row["lotItemBasePoint02"] = odds

                # Remaining slots: empty.
                for slot in range(3, 9):
                    row[f"lotItemId{slot:02d}"] = 0
                    row[f"lotItemCategory{slot:02d}"] = 0  # None
                    row[f"lotItemNum{slot:02d}"] = 0
                    row[f"lotItemBasePoint{slot:02d}"] = 0

                # Remove any acquisition flag.
                row["getItemFlagId"] = 0

    # Now nullify all remaining enemy weapon drops.
    for row in item_lots_param.rows:

        row_name = row.name

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

            # Nullify drop slot.
            row[f"lotItemId{slot:02d}"] = 0
            row[f"lotItemCategory{slot:02d}"] = 0  # None
            row[f"lotItemNum{slot:02d}"] = 0
            row[f"lotItemBasePoint{slot:02d}"] = 0

            # If ANY slot is a weapon, also nullify drop flag and remove name.
            row["getItemFlagId"] = 0
            row.name = f"{row_name} (Removed)"

    # Double odds of ALL Goods drops (including new ones just added above).
    for item_lot in item_lots_param.rows:
        if not item_lot.name:
            continue
        if (
            "Smithing Stone" in item_lot.name
            or "Rune" in item_lot.name
            or "Glass Shard" in item_lot.name
            or "Ruin Fragment" in item_lot.name
        ):
            continue
        if int(item_lot["lotItemCategory02"]) != 1:
            continue
        odds_1 = int(item_lot["lotItemBasePoint01"])
        odds_2 = int(item_lot["lotItemBasePoint02"])
        if odds_1 + odds_2 == 1000 and odds_1 > 0 and odds_2 < 200:
            old_odds = int(item_lot["lotItemBasePoint02"])
            new_odds = item_lot["lotItemBasePoint02"] = int(2 * old_odds)
            print(f"Doubling drop odds for: {item_lot.name} ({old_odds} -> {new_odds})")
            item_lot["lotItemBasePoint01"] = int(item_lot["lotItemBasePoint01"]) - (new_odds - old_odds)


def replace_weapon_item_lots(item_lots_param: YappedParam, weapons_param: YappedParam, is_map: bool):
    """Replace all (non-ammo) weapons in given ItemLotParam with components."""
    if not DO_WEAPONS:
        return

    soft_wood_odds = 0.2  # for enemies (vs. Metal Shards)

    manual_item_lots = MANUAL_ITEM_LOTS.copy() if is_map else {}

    for row in item_lots_param.rows:

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
                # Replace enemy drop with either 1 Soft Wood (rarer) or 1 Metal Shards.
                good_id = Materials.SoftWood if random.random() < soft_wood_odds else Materials.MetalShards
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


def get_random_material() -> tuple[Materials, int]:
    """Get a random material and drop count based on above dictionary."""
    materials = list(MATERIAL_RARITY_COUNT.keys())
    weights = [v[0] for v in MATERIAL_RARITY_COUNT.values()]
    material = random.choices(materials, weights=weights, k=1)[0]
    return material, random.randint(1, MATERIAL_RARITY_COUNT[material][1])


def replace_merchant_weapons(shop_merchant_param: YappedParam, weapons_param: YappedParam):
    """Replaces weapons sold by merchants with random components.

    Functions basically the same as map item lots.

    NOTE: Manual merchant slot replacements may overwrite these again. No big deal.
    """
    if not DO_WEAPONS:
        return

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


def generate_notes_recipes(
    goods_param: YappedParam,
    shop_merchant_param: YappedParam,
    item_lot_map: YappedParam,
):
    """Create new notes and recipe books and add them to merchant lineup."""

    note_source = 8700  # Note: Hidden Cave
    recipe_source = 9300  # Nomadic Warrior's Cookbook
    shop_source = 1  # unnamed
    item_lot_source = 10000  # Margit reward

    added_shop_rows = []

    def create_shop_row(_row_id, _good_id, _info):
        if _row_id in added_shop_rows:
            raise ValueError(f"Shop row ID used more than once: {_row_id}")
        added_shop_rows.append(_row_id)
        new_row = shop_merchant_param.duplicate_row(shop_source, _row_id)
        new_row.name = f"[Shop] {_info['name']}"
        new_row["equipId"] = _good_id
        new_row["sellQuantity"] = 1  # sell one
        try:
            new_row["value"] = _info["cost"]
        except KeyError:
            raise KeyError(f"No 'cost' for good ID {_good_id}")
        new_row["eventFlag_forStock"] = _info["bought_flag"]
        new_row["equipType"] = 3  # Good
        new_row["setNum"] = 1  # receive one

    def create_item_lot(_row_id, _good_id, _info):
        new_row = item_lot_map.duplicate_row(item_lot_source, _row_id)
        new_row.name = f"[Treasure] {_info['name']}"
        new_row["lotItemId01"] = _good_id
        new_row["lotItemCategory01"] = 1  # Good
        new_row["lotItemNum01"] = 1
        new_row["getItemFlagId"] = _info["bought_flag"]  # bought == found

    for item_dict, good_source in zip(
        (NEW_NOTES, NEW_RECIPE_BOOKS),
        (note_source, recipe_source),
    ):
        for good_id, good_info in item_dict.items():
            if not do_category(good_info):
                continue

            # Create good.
            new_good_row = goods_param.duplicate_row(good_source, good_id)
            new_good_row.name = good_info["name"]
            new_good_row["iconId"] = good_info["icon"]

            if "shop_row" in good_info:
                create_shop_row(good_info["shop_row"], good_id, good_info)
            elif "shop_rows" in good_info:
                for shop_row_id in good_info["shop_rows"]:  # quantity flag shared
                    create_shop_row(shop_row_id, good_id, good_info)
            elif "item_lot" in good_info:
                create_item_lot(good_info["item_lot"], good_id, good_info)
            elif "item_lots" in good_info:
                for item_lot_id in good_info["item_lots"]:  # acquisition flag shared
                    create_item_lot(item_lot_id, good_id, good_info)
            else:
                raise KeyError(f"Note/recipe {good_id} does not have a 'shop_row(s)' or 'item_lot(s)' field.")


def generate_disease_indicators(goods: YappedParam, item_lots_map: YappedParam):
    """Item lot IDs for disease indicators are identical to the goods themselves."""
    if not DO_DISEASES:
        return

    goods_source = 8010  # Rusty Key
    item_lot_source = 10000  # Margit reward

    for good_id, good_info in DISEASE_INDICATORS.items():
        # Indicator Key Item
        new_good = goods.duplicate_row(goods_source, good_id)
        new_good.name = good_info["name"]
        new_good["iconId"] = good_info["icon"]

        # Item Lot (good ID * 10)
        new_item_lot = item_lots_map.duplicate_row(item_lot_source, 10 * good_id)
        new_item_lot.name = good_info["name"]
        new_item_lot["lotItemId01"] = good_id
        new_item_lot["lotItemCategory01"] = 1  # Good
        new_item_lot["lotItemNum01"] = 1
        new_item_lot["getItemFlagId"] = 0  # no acquirement flag


def modify_torrent(npc_param: YappedParam):
    """Make some changes to Torrent's NPC values."""
    if not DO_SURVIVAL:
        return
    torrent = npc_param[80000000]
    torrent["hp"] = 500  # down from 1939


def fix_survival_shops(shop_merchant_param: YappedParam):
    if not DO_SURVIVAL:
        return

    crab = shop_merchant_param[100155]
    crab["sellQuantity"] = 10
    crab["value"] = 1800  # from 600
    prawn = shop_merchant_param[100160]
    prawn["sellQuantity"] = 10
    prawn["value"] = 1800  # from 600

    bearing_thin_bones = shop_merchant_param[101847]
    bearing_thin_bones["value"] = 1500  # from 150
    bearing_hefty_bone = shop_merchant_param[101848]
    bearing_hefty_bone["value"] = 2500  # from 250

    bearing_sliver_meat = shop_merchant_param[101849]
    bearing_sliver_meat["value"] = 5000


def test_item_lots(item_lots_map: YappedParam):
    """Debugging item lots."""
    item_lots_map[100].name = "Test: Lord's Rune"
    item_lots_map[100]["lotItemId01"] = 2919
    item_lots_map[100]["lotItemNum01"] = 5

    for i, test_good in enumerate(
        (Materials.MetalPlate, Materials.MetalShards, Materials.StoneFragment, Materials.SomberStoneFragment)
    ):
        row = item_lots_map.duplicate_row(100, 101 + i, name=f"Test: {test_good.name}")
        row["lotItemId01"] = test_good
        row["lotItemCategory01"] = 1  # Good
        row["lotItemNum01"] = 3

    # For quick hunger/thirst management.
    food_row = item_lots_map.duplicate_row(100, 500, name="Test: Great Bone Broth")
    food_row["lotItemId01"] = Consumables.GreatBoneBroth
    food_row["lotItemCategory01"] = 1  # Good
    food_row["lotItemNum01"] = 3

    # Disease cure testing.
    for i, cure in enumerate(range(Consumables.LimgraveDiseaseCure, Consumables.TunnelDiseaseCure + 1)):
        cure_item_lot = item_lots_map.duplicate_row(100, 600 + i, name="Test: Disease Cure")
        cure_item_lot["lotItemId01"] = cure
        cure_item_lot["lotItemCategory01"] = 1  # Good
        cure_item_lot["lotItemNum01"] = 1

    # Temperature protection testing.
    for i, item in enumerate(range(Consumables.MossdewSoup, Consumables.BlossomBrew + 1)):
        cure_item_lot = item_lots_map.duplicate_row(100, 700 + i, name="Test: Temp Protection")
        cure_item_lot["lotItemId01"] = item
        cure_item_lot["lotItemCategory01"] = 1  # Good
        cure_item_lot["lotItemNum01"] = 1


def enable_all_warps(bonfire_warp_param: YappedParam):
    for row in bonfire_warp_param.rows:
        if row.row_id < 100000:
            continue
        row["eventflagId"] = 0  # warp will always be enabled


def generate_all_params():
    bonfire_warp = read_param_csv("BonfireWarpParam_vanilla.csv")
    goods = read_param_csv("EquipParamGoods_vanilla.csv")
    weapons = read_param_csv("EquipParamWeapon_vanilla.csv")
    item_lots_enemy = read_param_csv("ItemLotParam_enemy_vanilla.csv")
    item_lots_map = read_param_csv("ItemLotParam_map_vanilla.csv")
    mtrl = read_param_csv("EquipMtrlSetParam_vanilla.csv")
    npc = read_param_csv("NpcParam_vanilla.csv")
    shop_recipe = read_param_csv("ShopLineupParam_Recipe_vanilla.csv")
    shop_merchant = read_param_csv("ShopLineupParam_vanilla.csv")

    # Delete Serpent-Hunter item lot (it will be replaced with a new recipe below).
    item_lots_map.rows.remove(item_lots_map[16000690])

    generate_dummy_weapons(weapons, mtrl, shop_recipe, item_lots_map)
    add_stone_recipes(mtrl, shop_recipe)

    generate_new_materials(goods)
    generate_new_consumables(goods, shop_recipe, mtrl)
    generate_smiths_hammers(goods, shop_recipe, mtrl)
    generate_notes_recipes(goods, shop_merchant, item_lots_map)
    generate_disease_indicators(goods, item_lots_map)

    fix_enemy_item_lots(item_lots_enemy, weapons)
    replace_weapon_item_lots(item_lots_map, weapons, is_map=True)
    replace_stone_item_lots(item_lots_enemy, is_map=False)
    replace_stone_item_lots(item_lots_map, is_map=True)
    replace_merchant_weapons(shop_merchant, weapons)
    fix_survival_shops(shop_merchant)

    modify_torrent(npc)
    # NOTE: SpEffects 501075-501087 have had their healing effects and VFX (5030) removed.

    # TODO: Remove in final release.
    print("\nNOTE: Debugging item lots created.")
    test_item_lots(item_lots_map)
    # print("\nNOTE: All Site of Grace warps enabled.")
    # enable_all_warps(bonfire_warp)

    write_param_csv(bonfire_warp, "BonfireWarpParam.csv")
    write_param_csv(mtrl, "EquipMtrlSetParam.csv")
    write_param_csv(goods, "EquipParamGoods.csv")
    write_param_csv(weapons, "EquipParamWeapon.csv")
    write_param_csv(item_lots_enemy, "ItemLotParam_enemy.csv")
    write_param_csv(item_lots_map, "ItemLotParam_map.csv")
    write_param_csv(npc, "NpcParam.csv")
    write_param_csv(shop_merchant, "ShopLineupParam.csv")
    write_param_csv(shop_recipe, "ShopLineupParam_Recipe.csv")
    # NOTE: SpEffectParam and CharaInitParam edited manually in Yapped.

    print("Read, edited, and wrote all Yapped param CSVs successfully.")


def generate_all_variants():
    global WRITE_CSV_PATH, DO_SURVIVAL, DO_WEAPONS, DO_DISEASES

    base_write_csv_path = WRITE_CSV_PATH

    WRITE_CSV_PATH = base_write_csv_path / "Survival"
    DO_SURVIVAL = True
    DO_WEAPONS = DO_DISEASES = False
    generate_all_params()

    WRITE_CSV_PATH = base_write_csv_path / "Weapons"
    DO_WEAPONS = True
    DO_SURVIVAL = DO_DISEASES = False
    generate_all_params()

    WRITE_CSV_PATH = base_write_csv_path / "Diseases"
    DO_DISEASES = True
    DO_SURVIVAL = DO_WEAPONS = False
    generate_all_params()

    WRITE_CSV_PATH = base_write_csv_path / "Survival_Weapons"
    DO_SURVIVAL = DO_WEAPONS = True
    DO_DISEASES = False
    generate_all_params()

    WRITE_CSV_PATH = base_write_csv_path / "Survival_Diseases"
    DO_SURVIVAL = DO_DISEASES = True
    DO_WEAPONS = False
    generate_all_params()

    WRITE_CSV_PATH = base_write_csv_path / "Weapons_Diseases"
    DO_WEAPONS = DO_DISEASES = True
    DO_SURVIVAL = False
    generate_all_params()

    WRITE_CSV_PATH = base_write_csv_path / "Survival_Weapons_Diseases"
    DO_SURVIVAL = DO_WEAPONS = DO_DISEASES = True
    generate_all_params()


if __name__ == '__main__':
    # generate_all_params()
    generate_all_variants()
