"""
Notes: RNG weights

# Vanilla material values. Add value for highest tier present ONCE, then multiply sum with VanillaMaterial.
    # This part kinda sucks.
    VanillaMat_Per = .25
    Tier1Mat = 1 # Early game/Common vanilla Materials
    Tier2Mat = 2 # Mid game or Uncommon vanilla Materials
    Tier3Mat = 4 # Late game or Rare vanilla Materials

    StoneFragment = .4
    SomberStoneFragment = .75
    IronShards = .75
    SoftWood = 1
    IronPlate = 1.5
    RefinedWood = 2
    GlintstoneDust = 4
    ErdtreeAmber = 4
    LiquidMetal = 6
    GruesomeBone = 8
    MeteoriteChunk = 8
    BlackMark = 8
    DragonTeeth = 10
    ErdtreeWood = ?

    # Tier thresholds (Probably worthless now. Instead, order a list by material cost?)
    Tier0 = 0
    Tier1 = 6
    Tier2 = 12
    Tier3 = 16

---------
Logic notes

Things to calculate around:
    Material value total
    Stat requirements
    Base scaling?? 
        This is questionable you remember infusions exist
        But at the same time, things would be less inconsistent for int/faith/arc builds

---------
Other notes
    ErdtreeWood: Currently used in a few bow recipes, but can probably be replaced and cut

"""
from enum import IntEnum


class Materials(IntEnum):

    # Vanilla items.
    SliverOfMeat = 15000
    BeastLiver = 15010
    LumpOfFlesh = 15020
    BeastBlood = 15030
    OldFang = 15040
    BuddingHorn = 15050
    FlightPinion = 15060
    FourToedFowlFoot = 15080
    TurtleNeckMeat = 15090
    HumanBoneShard = 15100
    GreatDragonflyHead = 15110
    SlumberingEgg = 15120
    CrabEggs = 15130
    LandOctopusOvary = 15140
    MirandaPowder = 15150
    StripOfWhiteFlesh = 15160
    ThinBeastBones = 15340
    HeftyBeastBone = 15341
    String = 15400
    LivingJarShard = 15410
    AlbinauricBloodclot = 15420
    StormhawkFeather = 15430
    Poisonbloom = 20650
    TrinasLily = 20651
    Fulgurbloom = 20652
    MiquellasLily = 20653
    GraveViolet = 20654
    FadedErdleafFlower = 20660
    ErdleafFlower = 20680
    AltusBloom = 20681
    FireBlossom = 20682
    GoldenSunflower = 20683
    TarnishedGoldenSunflower = 20685
    Herba = 20690
    ArteriaLeaf = 20691
    DewkissedHerba = 20710
    RowaFruit = 20720
    GoldenRowa = 20721
    RimedRowa = 20722
    Bloodrose = 20723
    EyeOfYelough = 20740
    CrystalBud = 20750
    RimedCrystalBud = 20751
    SacramentalBud = 20753
    Mushroom = 20760
    MeltedMushroom = 20761
    ToxicMushroom = 20770
    RootResin = 20775
    CrackedCrystal = 20780
    SanctuaryStone = 20795
    NascentButterfly = 20800
    AeonianButterfly = 20801
    SmolderingButterfly = 20802
    SilverFirefly = 20810
    GoldFirefly = 20811
    GlintstoneFirefly = 20812
    GoldenCentipede = 20820
    SilverTearHusk = 20825
    GoldTingedExcrement = 20830
    BloodTaintedExcrement = 20831
    CaveMoss = 20840
    BuddingCaveMoss = 20841
    CrystalCaveMoss = 20842
    YellowEmber = 20845
    VolcanicStone = 20850
    FormicRock = 20852
    GravelStone = 20855

    # NEW ITEMS

    # Basic equipment components.
        # Guidelines are in progress
    SoftWood = 21000
        # Very Common. Weapons with wood
        # Weaker weapons/arrows
    RefinedWood = 21001
        # Uncommon? Weapons with wood
        # Stronger weapons/arrows
    StoneFragment = 21002
        # Used for stronger weapons
        # Obtained by "breaking" Smithing Stones
    SomberStoneFragment = 21003
        # Used for EVEN STRONGER weapons
        # Obtained by "breaking" Somber Smithing Stones
    IronShards = 21004  # Generic metal scrap
        # Very common. Worth a "portion" of an Iron plate
        # More for DEX weapons vs Iron Plate
        # Used for bleed/spiky weapons
    IronPlate = 21005  # Generic metal plate
        # Common. Base material for most weapons
        # More for heavier weapons types (1 dagger -> 2 straight sword -> 3 greatsword -> etc)
        # More for STR weapons vs Iron Shards
    LiquidMetal = 21006 # Fancy Metal
        # Rename to [some sort of Fancy Metal]
        # Rare. Used for Nox weapons and weird weapons
        # Possibly replace usage with silver tear husks?
    DragonTeeth = 21007
        # Rare. Used for Dragon weapons
    GruesomeBone = 21008
        # Rare. Used for weird weapons & Arcane weapons
    GlintstoneDust = 0  # TODO
        # Semi-rare. Int stuff.
    ErdtreeAmber = 0  # TODO
        # Semi-rare. Faith stuff.
    
    MeteoriteChunk = 21503
        # Rare. Used for outer space stuff
    BlackMark = 21506 
        # Rare. Used for Mark of Death stuff 
            # Black Knife assassins, gargoyles, godskin/blackflame
    
    # Special equipment components. These are all quite rare.
        # Probably don't use these at the moment until their fate is decided
    Chain = 21500  # rare drop from Iron Virgin; rare treasure
    ErdtreeWood = 21501  # mainly from defeating Erdtree Avatars
    FallingstarJawbone = 21502  # reward from Fallingstar Beast
    # MeteoriteChunk = 21503 # moved to the above section
    GrindingWheel = 21504  # for Ghiza's Wheel only (replaces that item)
    DragonspearChunk = 21505  # for Bolt of Gransax only (replaces that item)
    # BlackMark = 21506 # moved to the above section

    # Required single base components. These are all rare treasure or bought from merchants.
    SmallHilt = 21600  # daggers, whips
    StandardHilt = 21601  # straight swords, thrusting swords, katanas
    CurvedHilt = 21602  # curved swords, curved greatswords, katanas
    GiantHilt = 21603  # greatswords, colossal swords
    SpearShaft = 21604  # spears, halberds, reapers
    AxeHandle = 21605  # axes, greataxes, hammers, flails
    BowGrip = 21606  # bows
    GreatBowGrip = 21607  # greatbows
    TriggerMechanism = 21608  # crossbows, guns/cannons
    StaffPole = 21609  # glintstone staves
    ShieldHandle = 21610  # small/medium shields
    GreatshieldHandle = 21611  # greatshields
    # No base component for Seals or Fists (just varying recipes).
