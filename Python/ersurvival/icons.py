"""Icon notes/generators.

Icons are in TPF files inside the `menu/01_common.tpf.dcx` archive.

The icon layouts are in the adjacent `01_common.sblytbnd.dcx` binder, in XML format '.layout' files.

Fortunately, these should be pretty easy to generate from a dictionary, though I will have to drag and drop in the icons
in Paint.NET.

`SB_Icon_06.dds` has the most space in it: 71 icons (60 in brand new columns). That should be MORE than enough.
Remember that notes and recipes do not need new icons - just the new materials and consumables (and Meteor Chuck).

There are also NO goods that use icon ID 19000-19999. Of course, these could appear in another item type, but I have
my doubts that they'd use a range so close to the rest of the goods.

The `hi` and `low` TPF/layouts are *identical* for these icons, fortunately, so I just have to duplicate my edited ones.
"""
from survival_params import YappedParam, read_param_csv
from survival_goods import NEW_CONSUMABLES, NEW_MATERIALS


SHEET = "SB_Icon_06"
DIM = 160  # width and height of all icons
BASE_ID = 19000  # actually hard-coded into item dictionaries, but here for reference
PAD = 4  # empty pixels between adjacent textures
X_START = 3280  # fifth-to-last free column
Y_START = 0  # top


LAYOUT_TEMPLATE = (
    "\t<SubTexture name=\"MENU_ItemIcon_{id}.png\" x=\"{x}\" y=\"{y}\" width=\"160\" height=\"160\" half=\"0\"/>"
)


def print_layout_entries():
    x, y = X_START, Y_START
    row = 0  # max index is 11
    icon_id = BASE_ID  # first ID
    for _ in range(60):
        print(LAYOUT_TEMPLATE.format(id=icon_id, x=x, y=y))
        row += 1
        icon_id += 1
        if row > 11:  # new column
            row = 0
            y = 0
            x += DIM + PAD
        else:  # go down same column
            y += DIM + PAD


def find_good_icon_id(goods_param: YappedParam, icon_id: int):
    for row in goods_param.rows:
        if int(row["iconId"]) == icon_id:
            print(f"Icon ID {icon_id} used by good {row.row_id} named: '{row.name}'")
            return row
    return None


# TODO: Yabber up TPF files here.


if __name__ == '__main__':
    print_layout_entries()
    # find_good_icon_id(read_param_csv("EquipParamGoods_vanilla.csv"), 3739)
