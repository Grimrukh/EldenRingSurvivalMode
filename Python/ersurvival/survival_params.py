"""Scripts for generating Params (regulation.bin).

Modifies CSV files exported by Yapped (Rune Bear), which that program can then re-import.
"""
from __future__ import annotations

import csv
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
            super().__setitem__(key, value)
        else:  # convert to string for CSV
            super().__setitem__(key, str(value))

    @property
    def name(self):
        return self["Row Name"]

    @name.setter
    def name(self, value: str):
        super().__setitem__("Row Name", value)


class YappedParam:

    def __init__(self, field_names: list[str]):
        self.field_names = field_names
        self.rows = []  # type: list[YappedRow]

    def __getitem__(self, row_id: int):
        for row in self.rows:
            if row["Row ID"] == row_id:
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
        new_row = YappedRow(self[source_row_id])
        new_row["Row ID"] = dest_row_id
        if "name" in kwargs:
            new_row.name = kwargs.pop("name")
        for field, value in kwargs.items():
            if field not in new_row:
                raise ValueError(f"Invalid field for this param: {field}")
            new_row[field] = value
        self.add_row(new_row, after_row_id=source_row_id)
        return new_row

    def get_row_ids(self) -> list[int]:
        return [row["Row ID"] for row in self.rows]
    
    def sort_rows(self):
        """Sort rows by row ID."""
        self.rows = sorted(self.rows, key=lambda x: x["Row ID"])

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


class GoodsUseAnimation(IntEnum):
    ITEM_RECOVER = 0
    ITEM_DRINK = 10
    ITEM_EATJERKY = 26


class PotGroupID(IntEnum):
    NoPot = -1
    CrackedPot = 1
    PerfumeBottle = 2
    RitualPot = 3


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
    "Chain": {
        "id": Materials.Chain,
        "icon": 0,  # TODO
    },
    "Erdtree Wood": {
        "id": Materials.ErdtreeWood,
        "icon": 0,  # TODO
    },
    "Fallingstar Jawbone": {
        "id": Materials.FallingstarJawbone,
        "icon": 0,  # TODO
    },
    "Meteorite Chunk": {
        "id": Materials.MeteoriteChunk,
        "icon": 0,  # TODO
    },
    "Grinding Wheel": {
        "id": Materials.GrindingWheel,
        "icon": 0,  # TODO
    },
    "Dragonspear Chunk": {
        "id": Materials.DragonspearChunk,
        "icon": 0,  # TODO
    },
    "Black Mark": {
        "id": Materials.BlackMark,
        "icon": 0,  # TODO
    },
    "Small Hilt": {
        "id": Materials.SmallHilt,
        "icon": 0,  # TODO
    },
    "Standard Hilt": {
        "id": Materials.StandardHilt,
        "icon": 0,  # TODO
    },
    "Curved Hilt": {
        "id": Materials.CurvedHilt,
        "icon": 0,  # TODO
    },
    "Giant Hilt": {
        "id": Materials.GiantHilt,
        "icon": 0,  # TODO
    },
    "Spear Shaft": {
        "id": Materials.SpearShaft,
        "icon": 0,  # TODO
    },
    "Axe Handle": {
        "id": Materials.AxeHandle,
        "icon": 0,  # TODO
    },
    "Bow Grip": {
        "id": Materials.BowGrip,
        "icon": 0,  # TODO
    },
    "Great Bow Grip": {
        "id": Materials.GreatBowGrip,
        "icon": 0,  # TODO
    },
    "Trigger Mechanism": {
        "id": Materials.TriggerMechanism,
        "icon": 0,  # TODO
    },
    "Staff Pole": {
        "id": Materials.StaffPole,
        "icon": 0,  # TODO
    },
    "Shield Handle": {
        "id": Materials.ShieldHandle,
        "icon": 0,  # TODO
    },
    "Greatshield Handle": {
        "id": Materials.GreatshieldHandle,
        "icon": 0,  # TODO
    },
}


WEAPON_BASE_MATERIALS = {
    WeaponType.Dagger: Materials.SmallHilt,
    WeaponType.StraightSword: Materials.StandardHilt,
    WeaponType.Greatsword: Materials.GiantHilt,
    WeaponType.ColossalSword: Materials.GiantHilt,
    WeaponType.CurvedSword: Materials.CurvedHilt,
    WeaponType.CurvedGreatsword: Materials.CurvedHilt,
    WeaponType.Katana: Materials.CurvedHilt,
    WeaponType.Twinblade: Materials.StandardHilt,
    WeaponType.ThrustingSword: Materials.StandardHilt,
    WeaponType.HeavyThrustingSword: Materials.GiantHilt,
    WeaponType.Axe: Materials.AxeHandle,
    WeaponType.Greataxe: Materials.AxeHandle,
    WeaponType.Hammer: Materials.AxeHandle,
    WeaponType.GreatHammer: Materials.AxeHandle,
    WeaponType.Flail: Materials.AxeHandle,
    WeaponType.Spear: Materials.SpearShaft,
    WeaponType.HeavySpear: Materials.SpearShaft,
    WeaponType.Halberd: Materials.SpearShaft,
    WeaponType.Scythe: Materials.SpearShaft,
    WeaponType.Fist: None,
    WeaponType.Claw: None,
    WeaponType.Whip: Materials.SmallHilt,
    WeaponType.ColossalWeapon: None,
    WeaponType.LightBow: Materials.BowGrip,
    WeaponType.Bow: Materials.BowGrip,
    WeaponType.Greatbow: Materials.GreatBowGrip,
    WeaponType.Crossbow: Materials.TriggerMechanism,
    WeaponType.Ballista: Materials.TriggerMechanism,
    WeaponType.Staff: Materials.StaffPole,
    WeaponType.Seal: None,
    WeaponType.SmallShield: Materials.ShieldHandle,
    WeaponType.MediumShield: Materials.ShieldHandle,
    WeaponType.Greatshield: Materials.GreatshieldHandle,
    WeaponType.Torch: None,
}


def print_weapon_recipe_starter(row: YappedRow):
    weapon_type = int(row["wepType"])
    base_material = WEAPON_BASE_MATERIALS[WeaponType(weapon_type)]

    base_str = "" if base_material is None else f"(1, CraftingMaterials.{base_material.name}),"

    print(f"""
    "{row.name}": {{
        "id": {row.row_id // 10000},
        "recipe": [
            {base_str}
        ],
    }},""", end="")


def generate_dummy_weapons(
    weapon_param: YappedParam,
    equip_mtrl_set_param: YappedParam,
    shop_recipe_param: YappedParam,
    item_lots_map_param: YappedParam,
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

    # TODO: Specify recipes and add Mtrl and Shop rows.

    # TODO: Equivalent stuff for armor (and talismans?).

    slot = 0
    for row in weapon_param.rows:
        if not do_weapon(row):
            continue
        # print_weapon_recipe_starter(row)

        weapon_id = row.row_id // 10000
        dummy_id = dummy_offset + 100 * weapon_id
        shop_id = new_shop_offset + weapon_id
        mtrl_id = new_mtrl_offset + 10 * weapon_id
        item_lot_id = item_lot_offset + 100 * weapon_id

        # Create dummy Weapon row.
        dummy = weapon_param.duplicate_row(row.row_id, dummy_id)
        dummy["Row Name"] += " (crafting dummy)"
        dummy["weaponCategory"] = 13  # arrow (for appearing in crafting menu)

        # TODO: Create item lot for awarding real weapon.
        new_item_lot = item_lots_map_param.duplicate_row(item_lot_source, item_lot_id)
        new_item_lot.name = f"{row.name} (crafted)"
        new_item_lot["lotItemId01"] = row.row_id
        new_item_lot["lotItemCategory01"] = 2  # Weapon
        new_item_lot["lotItemNum01"] = 1
        print(f"ReplaceDummyWeapon({slot}, {dummy_id}, {item_lot_id})")
        slot += 1

        # Create recipe entry.
        new_shop_row = shop_recipe_param.duplicate_row(shop_source, shop_id)
        new_shop_row.name = row.name
        new_shop_row["equipId"] = dummy_id
        # TODO: value (rune cost)
        new_shop_row["mtrlId"] = mtrl_id
        # TODO: visibility flag (from new recipe book)
        new_shop_row["equipType"] = 0  # Weapon
        new_shop_row["setNum"] = 1  # only one

        # Create ingredients entry.
        new_mtrl_row = equip_mtrl_set_param.duplicate_row(mtrl_source, mtrl_id)
        new_mtrl_row.name = row.name
        weapon_recipe = WEAPON_RECIPES[row.name]["recipe"]
        if not weapon_recipe:
            # print(f"No recipe ingredients for weapon {row.name}. Skipping for now.")
            pass
        else:
            for i, (count, ingredient) in enumerate(weapon_recipe):
                new_mtrl_row[f"materialId{i + 1:02d}"] = ingredient.value
                new_mtrl_row[f"itemNum{i + 1:02d}"] = count
                new_mtrl_row[f"materialCate{i + 1:02d}"] = 4  # always Goods


def generate_new_consumables(
    goods_param: YappedParam, shop_recipe_param: YappedParam, equip_mtrl_set_param: YappedParam
):
    """
    TODO: Generate 'assembly' recipes for weapons/armor.
     These will have a real recipe book of some kind.
    """

    # Recipes for new "survival" goods (food, drink, protection).

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
        new_good_row["iconId"] = 52  # TODO: add to dictionary
        new_good_row["goodsUseAnim"] = good["animation"].value
        # TODO: Probably other stuff too (e.g., VFX).

        new_shop_row = shop_recipe_param.duplicate_row(shop_source, shop_id)
        new_shop_row.name = good_name
        new_shop_row["equipId"] = good_id
        # TODO: value (rune cost)
        new_shop_row["mtrlId"] = mtrl_id
        # TODO: visibility flag
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


def generate_all():
    goods = read_param_csv("EquipParamGoods_vanilla.csv")
    weapons = read_param_csv("EquipParamWeapon_vanilla.csv")
    item_lots_map = read_param_csv("ItemLotParam_map_vanilla.csv")
    mtrl = read_param_csv("EquipMtrlSetParam_vanilla.csv")
    shop_recipe = read_param_csv("ShopLineupParam_Recipe_vanilla.csv")
    shop_merchant = read_param_csv("ShopLineupParam_vanilla.csv")

    generate_dummy_weapons(weapons, mtrl, shop_recipe, item_lots_map)


if __name__ == '__main__':
    generate_all()
