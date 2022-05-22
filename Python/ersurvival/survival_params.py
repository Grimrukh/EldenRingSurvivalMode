"""Scripts for generating Params (regulation.bin).

Modifies CSV files exported by Yapped (Rune Bear), which that program can then re-import.
"""
from __future__ import annotations

import csv
import random
import re
import shutil
from pathlib import Path

from Python.ersurvival.crafting import Materials
from survival_enums import *
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


class GoodsUseAnimation(IntEnum):
    ITEM_RECOVER = 0
    ITEM_DRINK = 10
    ITEM_EATJERKY = 26


class PotGroupID(IntEnum):
    NoPot = -1
    CrackedPot = 1
    PerfumeBottle = 2
    RitualPot = 3


PRESERVE_ITEM_LOTS = [
    16000690,  # Serpent-Hunter treasure
]


NEW_CONSUMABLES = {
    "Raw Steak": {
        "id": 0,  # offset used in all IDs
        "recipe": [  # for `EquipMtrlSetParam`
            (3, Materials.SliverOfMeat),
        ],
        "effect": SurvivalEffects.RawSteak,  # for `EquipGoodsParam`
        "animation": GoodsUseAnimation.ITEM_EATJERKY,  # for `EquipGoodsParam`
    },
    "Seared Steak": {
        "id": 1,
        "recipe": [
            (3, Materials.SliverOfMeat),
            (2, Materials.SmolderingButterfly),
        ],
        "effect": SurvivalEffects.SearedSteak,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
    },
    "Raw Liver Steak": {
        "id": 2,
        "recipe": [
            (2, Materials.SliverOfMeat),
            (1, Materials.BeastLiver),
        ],
        "effect": SurvivalEffects.RawLiverSteak,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
    },
    "Seared Liver Steak": {
        "id": 3,
        "recipe": [
            (2, Materials.SliverOfMeat),
            (1, Materials.BeastLiver),
            (2, Materials.SmolderingButterfly),
        ],
        "effect": SurvivalEffects.SearedLiverSteak,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
    },
    "Bone Broth": {
        "id": 4,
        "recipe": [
            (5, Materials.ThinBeastBones),
        ],
        "effect": SurvivalEffects.BoneBroth,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
    },
    "Great Bone Broth": {
        "id": 5,
        "recipe": [
            (3, Materials.HeftyBeastBone),
        ],
        "effect": SurvivalEffects.GreatBoneBroth,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
    },
    "Blood Broth": {
        "id": 6,
        "recipe": [
            (3, Materials.ThinBeastBones),
            (2, Materials.BeastBlood),
        ],
        "effect": SurvivalEffects.BloodBroth,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
    },
    "Forest Berry Medley": {
        "id": 7,
        "recipe": [
            (10, Materials.RowaFruit),
        ],
        "effect": SurvivalEffects.BerryMedley1,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
    },
    "Plateau Berry Medley": {
        "id": 8,
        "recipe": [
            (10, Materials.GoldenRowa),
        ],
        "effect": SurvivalEffects.BerryMedley2,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
    },
    "Mountain Berry Medley": {
        "id": 9,
        "recipe": [
            (10, Materials.RimedRowa),
        ],
        "effect": SurvivalEffects.BerryMedley3,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
    },
    "Mushroom Stew": {
        "id": 10,
        "recipe": [
            (3, Materials.Mushroom),
            (3, Materials.Herba),
        ],
        "effect": SurvivalEffects.MushroomStew,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
    },
    "Melted Mushroom Stew": {
        "id": 11,
        "recipe": [
            (3, Materials.MeltedMushroom),
            (3, Materials.DewkissedHerba),
        ],
        "effect": SurvivalEffects.MeltedMushroomStew,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
    },
    "Draught of the Undining": {
        "id": 12,
        "recipe": [
            (3, Materials.GraveViolet),
            # TODO: More ingredients.
        ],
        "effect": SurvivalEffects.DraughtOfTheUndining,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
    },
    "Draught of Silver Tears": {
        "id": 13,
        "recipe": [
            (7, Materials.SilverTearHusk),
            # TODO: More ingredients.
        ],
        "effect": SurvivalEffects.DraughtOfSilverTears,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
    },
    "Mossdew Soup": {
        "id": 14,
        "recipe": [
            (3, Materials.CaveMoss),
            (4, Materials.DewkissedHerba),
        ],
        "effect": SurvivalEffects.MossdewSoup,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
    },
    "Crystal Shard Soup": {
        "id": 15,
        "recipe": [
            (2, Materials.BuddingCaveMoss),
            (5, Materials.CrackedCrystal),
        ],
        "effect": SurvivalEffects.CrystalShardSoup,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
    },
    "Giant's Soup": {
        "id": 16,
        "recipe": [
            (5, Materials.RimedRowa),
            (2, Materials.CrystalCaveMoss),
            (2, Materials.RimedRowa),
        ],
        "effect": SurvivalEffects.GiantsSoup,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
    },
    "Amber-Eye Brew": {
        "id": 17,
        "recipe": [
            (3, Materials.EyeOfYelough),
            (1, Materials.YellowEmber),
            (3, Materials.Herba),
        ],
        "effect": SurvivalEffects.AmberEyeBrew,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
    },
    "Magmatic Brew": {
        "id": 18,
        "recipe": [
            (4, Materials.VolcanicStone),
            (3, Materials.TarnishedGoldenSunflower),
        ],
        "effect": SurvivalEffects.MagmaticBrew,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.CrackedPot,
    },
    "Blossom Brew": {
        "id": 19,
        "recipe": [
            (5, Materials.FireBlossom),
            (3, Materials.FormicRock),
        ],
        "effect": SurvivalEffects.BlossomBrew,
        "animation": GoodsUseAnimation.ITEM_DRINK,
        "pot": PotGroupID.RitualPot,
    },
    "Jar Brittle": {
        "id": 20,
        "recipe": [
            (5, Materials.LivingJarShard),
        ],
        "effect": SurvivalEffects.JarBrittle,
        "animation": GoodsUseAnimation.ITEM_EATJERKY,
    },
}


NEW_MATERIALS = {
    "Soft Wood": {
        "id": Materials.SoftWood,
        "icon": 0,  # TODO
    },
    "Refined Wood": {
        "id": Materials.RefinedWood,
        "icon": 0,  # TODO
    },
    "Stone Fragment": {
        "id": Materials.StoneFragment,
        "icon": 0,  # TODO
    },
    "Somber Stone Fragment": {
        "id": Materials.SomberStoneFragment,
        "icon": 0,  # TODO
    },
    "Iron Shards": {
        "id": Materials.IronShards,
        "icon": 0,  # TODO
    },
    "Iron Plate": {
        "id": Materials.IronPlate,
        "icon": 0,  # TODO
    },
    "Liquid Metal": {
        "id": Materials.LiquidMetal,
        "icon": 0,  # TODO
    },
    "Dragon Teeth": {
        "id": Materials.DragonTeeth,
        "icon": 0,  # TODO
    },
    "Gruesome Bone": {
        "id": Materials.GruesomeBone,
        "icon": 0,  # TODO
    },
    "Erdtree Wood": {
        "id": Materials.ErdtreeWood,
        "icon": 0,  # TODO
    },
    "Meteorite Chunk": {
        "id": Materials.MeteoriteChunk,
        "icon": 0,  # TODO
    },
    "Black Mark": {
        "id": Materials.BlackMark,
        "icon": 0,  # TODO
    },
    "Staff Pole": {
        "id": Materials.StaffPole,
        "icon": 0,  # TODO
    },
    "Shield Handle": {
        "id": Materials.ShieldGrip,
        "icon": 0,  # TODO
    },
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

    new_mtrl_offset = 400000
    mtrl_source = 320010  # 3x Thin Beast Bones

    new_shop_offset = 40000
    shop_source = 1  # unnamed

    item_lot_offset = 40000000
    item_lot_source = 100

    # NOTE: There are some existing high-ID weapons starting with 98990000, but these are above the highest dummy
    # weapon that will be created here (32300000 + 60000000 = 92300000).

    new_weapon_indices = list(WEAPON_RECIPES.keys())
    tiers_dict = parse_weapon_tiers()  # maps weapon names to (weapon_id, previous_id) pair

    slot = 0
    for row in weapon_param.rows:
        if not do_weapon(row):
            continue

        weapon_base_id = row.row_id // 10000
        dummy_id = dummy_offset + 100 * weapon_base_id
        shop_id = new_shop_offset + weapon_base_id
        mtrl_id = new_mtrl_offset + 10 * weapon_base_id
        item_lot_id = item_lot_offset + 100 * weapon_base_id

        try:
            true_weapon_id, previous_weapon_id = tiers_dict[row.name]
        except KeyError:
            # Weapon is not in the upgrade tree, and is simply crafted from scratch (Shields, Staffs, Seals, Torches)
            true_weapon_id = row.row_id  # no upgrade level (can be upgrading normally at blacksmith)
            previous_weapon_id = None  # no previous weapon in recipe

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

        # Create dummy Weapon row.
        dummy = weapon_param.duplicate_row(row.row_id, dummy_id)
        dummy["Row Name"] += " (crafting dummy)"
        dummy["weaponCategory"] = 13  # arrow (for appearing in crafting menu)

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
        # monitor_flag = SurvivalFlags.WeaponMonitorBase + new_weapon_indices.index(row.name)
        # print(
        #     f"CraftDummyWeapon("
        #     f"{slot}, "
        #     f"{dummy_id}, "
        #     f"weapon_item_lot={item_lot_id}, "
        #     f"previous_weapon={previous_weapon_id if previous_weapon_id is not None else 0})"
        # )
        # print(
        #     f"MonitorWeaponPossession({slot}, {true_weapon_id}, {monitor_flag})"
        # )
        slot += 1

        # Create ingredients entry.
        new_mtrl_row = equip_mtrl_set_param.duplicate_row(mtrl_source, mtrl_id)
        new_mtrl_row.name = row.name
        ingredients = [ing for ing in WEAPON_RECIPES[row.name]["recipe"] if ing[1] < 21100]  # ignore grips
        if not ingredients:
            # print(f"No recipe ingredients for weapon {row.name}. Skipping for now.")
            pass
        else:
            i = 0
            if previous_weapon_id is not None:
                new_mtrl_row[f"materialId{i + 1:02d}"] = previous_weapon_id
                new_mtrl_row[f"itemNum{i + 1:02d}"] = 1
                new_mtrl_row[f"materialCate{i + 1:02d}"] = 0  # Weapon
                i += 1

            for count, ingredient in ingredients:
                new_mtrl_row[f"materialId{i + 1:02d}"] = ingredient.value
                new_mtrl_row[f"itemNum{i + 1:02d}"] = count
                new_mtrl_row[f"materialCate{i + 1:02d}"] = 4  # always Goods
                i += 1


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

    for good_name, good in NEW_CONSUMABLES.items():
        good_id = new_good_offset + good["id"]
        shop_id = new_shop_offset + good["id"]
        mtrl_id = new_mtrl_offset + 10 * good["id"]

        new_good_row = goods_param.duplicate_row(goods_source, good_id)
        new_good_row.name = good_name
        new_good_row["refId_default"] = good["effect"]
        new_good_row["sellValue"] = -1
        new_good_row["iconId"] = 52  # TODO: set for each new good in its dictionary
        new_good_row["goodsUseAnim"] = good["animation"].value
        # TODO: Probably other stuff too (e.g., VFX).

        new_shop_row = shop_recipe_param.duplicate_row(shop_source, shop_id)
        new_shop_row.name = good_name
        new_shop_row["equipId"] = good_id
        # TODO: value (rune cost)?
        new_shop_row["mtrlId"] = mtrl_id
        # TODO: visibility flag?
        new_shop_row["equipType"] = 3  # always Goods
        new_shop_row["setNum"] = 1  # only one

        new_mtrl_row = equip_mtrl_set_param.duplicate_row(mtrl_source, mtrl_id)
        new_mtrl_row.name = good_name
        for i, (count, ingredient) in enumerate(good["recipe"]):
            new_mtrl_row[f"materialId{i + 1:02d}"] = ingredient.value
            new_mtrl_row[f"itemNum{i + 1:02d}"] = count
            new_mtrl_row[f"materialCate{i + 1:02d}"] = 4  # always Goods


def generate_new_materials(goods_param: YappedParam):
    """Add new crafting material Goods. Relatively simple."""
    source_row = 15000  # Sliver of Meat
    for good_name, material in NEW_MATERIALS.items():
        new_material = goods_param.duplicate_row(source_row, material["id"], iconId=material["icon"])
        new_material.name = good_name


def replace_weapon_item_lots(item_lots_param: YappedParam, weapons_param: YappedParam, is_map: bool):
    """Replace all (non-ammo) weapons in given ItemLotParam with components.

    Shields and Staffs have a chance of being replaced with a Shield Grip or Staff Pole, respectively.
    All other weapons will be replaced with a random number of a random ingredient in that weapon's new recipe.
    The random number can be up to half of the recipe requirement for treasure.

    For enemy item lots, only "animal" materials (ID < 20000), Soft Wood, or Iron Shards can be dropped.
    """
    shield_grip_odds = 0.1
    staff_pole_odds = 0.15

    for row in item_lots_param.rows:

        if row.row_id in PRESERVE_ITEM_LOTS:
            continue  # leave these item lots be (e.g., Serpent-Hunter)

        for slot in range(1, 9):
            item_id = int(row[f"lotItemId{slot:02d}"])
            item_type = int(row[f"lotItemCategory{slot:02d}"])
            item_count = int(row[f"lotItemNum{slot:02d}"])
            # drop rate isn't changed
            if item_id in {0, -1}:
                # Ignore empty item lots.
                continue
            if item_type != 2:
                # Ignore non-weapons.
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
            weapon_type = WeaponType(int(weapon_row["wepType"]))
            if weapon_category in (WeaponCategory.Arrow, WeaponCategory.Bolt):
                # Ignore ammo.
                continue

            if not weapon_row.name:
                # Ignore unused weapon drops.
                continue

            # Look up recipe here.
            try:
                weapon_recipe = WEAPON_RECIPES[weapon_row.name]
            except KeyError:
                raise KeyError(f"Missing weapon recipe for name: '{weapon_row.name}' (item lot {row.row_id})")

            # If weapon is a shield, and this is treasure, roll for a Shield Grip drop.
            if is_map and weapon_type in (WeaponType.SmallShield, WeaponType.MediumShield, WeaponType.Greatshield):
                if random.random() <= shield_grip_odds:
                    # Replace with one Shield Grip.
                    row[f"lotItemId{slot:02d}"] = Materials.ShieldGrip
                    row[f"lotItemCategory{slot:02d}"] = 1  # Good
                    row[f"lotItemNum{slot:02d}"] = 1
                    continue

            # If weapon is a staff, and this is treasure, roll for a Staff Pole drop.
            if is_map and 33000000 <= base_weapon_id <= 33300000:
                if random.random() <= staff_pole_odds:
                    # Replace with one Staff Pole.
                    row[f"lotItemId{slot:02d}"] = Materials.StaffPole
                    row[f"lotItemCategory{slot:02d}"] = 1  # Good
                    row[f"lotItemNum{slot:02d}"] = 1
                    continue

            # Get a random recipe ingredient (including its count), excluding "grip" items.
            ingredients = [ing for ing in weapon_recipe["recipe"] if ing[1] < 21100]
            if not weapon_recipe["recipe"]:
                print(f"Recipe for weapon '{weapon_row.name}' has no non-base ingredients. Skipping item lot.")
                continue
            good_count, good_id = random.choice(ingredients)

            if not is_map and good_id >= 20000 and good_id not in (Materials.SoftWood, Materials.IronShards):
                # The only (non-animal-part) goods that enemies can drop are Soft Wood and Iron Shards.
                # Give them ONE more chance to choose a valid drop:
                good_count, good_id = random.choice(ingredients)
                # If one of these was STILL not chosen, the enemy drops nothing instead.
                if not is_map and good_id >= 20000 and good_id not in (Materials.SoftWood, Materials.IronShards):
                    row[f"lotItemId{slot:02d}"] = 0
                    row[f"lotItemCategory{slot:02d}"] = 0
                    row[f"lotItemNum{slot:02d}"] = 0
                    continue

            # Replace item lot slot.
            if is_map:
                # Treasure good count randomly varies between 1 and HALF the recipe count, rounded down.
                good_count = int(max(1, int(random.random() * 0.5 * good_count)))
            else:
                good_count = 1  # enemies only ever drop 1
            row[f"lotItemId{slot:02d}"] = good_id
            row[f"lotItemCategory{slot:02d}"] = 1  # Good
            row[f"lotItemNum{slot:02d}"] = good_count


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


def replace_merchant_weapons(shop_merchant_param: YappedParam, weapons_param: YappedParam):
    """Replaces weapons sold by merchants with random components.

    Functions basically the same as map item lots.
    """
    shield_grip_odds = 0.1
    staff_pole_odds = 0.15

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
        weapon_type = WeaponType(int(weapon_row["wepType"]))
        if weapon_category in (WeaponCategory.Arrow, WeaponCategory.Bolt):
            # Ignore ammo.
            continue

        # Get base weapon ID (round down to nearest 10000).
        base_weapon_id = 10000 * (weapon_id // 10000)
        weapon_row = weapons_param[base_weapon_id]

        if not weapon_row.name:
            # Ignore unused weapon drops.
            continue

        # Look up recipe here.
        try:
            weapon_recipe = WEAPON_RECIPES[weapon_row.name]
        except KeyError:
            raise KeyError(f"Missing weapon recipe for name: '{weapon_row.name}' (item lot {row.row_id})")

        # If weapon is a shield, and this is treasure, roll for a Shield Grip drop.
        if weapon_type in (WeaponType.SmallShield, WeaponType.MediumShield, WeaponType.Greatshield):
            if random.random() <= shield_grip_odds:
                # Replace with one Shield Grip.
                row["equipId"] = Materials.ShieldGrip
                row["equipType"] = 3  # Good
                row["sellQuantity"] = 1
                continue

        # If weapon is a staff, and this is treasure, roll for a Staff Pole drop.
        if 33000000 <= base_weapon_id <= 33300000:
            if random.random() <= staff_pole_odds:
                # Replace with one Staff Pole.
                row["equipId"] = Materials.StaffPole
                row["equipType"] = 3  # Good
                row["sellQuantity"] = 1
                continue

        # Get a random recipe ingredient (including its count), excluding "grip" items.
        ingredients = [ing for ing in weapon_recipe["recipe"] if ing not in range(21600, 21620)]
        if not ingredients:
            print(f"Recipe for weapon '{weapon_row.name}' has no non-base ingredients. Skipping item lot.")
            continue
        good_count, good_id = random.choice(ingredients)

        # Treasure good count randomly varies between 1 and HALF the recipe count, rounded down.
        good_count = int(max(1, int(random.random() * 0.5 * good_count)))
        row["equipId"] = good_id
        row["equipType"] = 3  # Good
        row["sellQuantity"] = good_count

    for row in rows_to_delete:
        shop_merchant_param.rows.remove(row)


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

    replace_weapon_item_lots(item_lots_enemy, weapons, is_map=False)
    replace_weapon_item_lots(item_lots_map, weapons, is_map=True)
    replace_merchant_weapons(shop_merchant, weapons)
    # TODO: Notes with disease clues for merchants.
    # TODO: New "cookbooks" for consumables, basic weapon crafting, and shield/staff/seal/torch crafting.

    write_param_csv(goods, "EquipParamGoods_test.csv")


if __name__ == '__main__':
    generate_all()
