"""Types for the swan wrapper."""
from enum import Enum, IntEnum


class IDLA(IntEnum):
    """Order of values in the input files.

    Attributes
    ----------
    ONE: 1
        SWAN reads the map from left to right starting in the upper-left-hand corner of
        the map. A new line in the map should start on a new line in the file.
    TWO: 2
        As `1` but a new line in the map need not start on a new line in the file.
    THREE: 3
        SWAN reads the map from left to right starting in the lower-left-hand corner of
        the map. A new line in the map should start on a new line in the file.
    FOUR: 4
        As `3` but a new line in the map need not start on a new line in the file.
    FIVE: 5
        SWAN reads the map from top to bottom starting in the lower-left-hand corner of
        the map. A new column in the map should start on a new line in the file.
    SIX: 6
        As `5` but a new column in the map need not start on a new line in the file.

    Notes
    -----
    It is assumed that the x-axis of the grid is pointing to the right and the y-axis
    upwards.

    """

    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6


class GridOptions(str, Enum):
    """Valid options for the input grid type.

    Attributes
    ----------
    BOTTOM: "bottom"
        Bottom level grid.
    WLEVEL: "wlevel"
        Water level grid.
    CURRENT: "current"
        Current field grid.
    VX: "vx"
        Current field x-component grid.
    VY: "vy"
        Current field y-component grid.
    WIND: "wind"
        Wind velocity grid.
    WX: "wx"
        Wind velocity x-component grid.
    WY: "wy"
        Wind velocity y-component grid.
    FRICTION: "friction"
        Bottom friction grid.
    NPLANTS: "nplants"
        Horizontally varying vegetation density grid.
    TURBVISC: "turbvisc"
        Horizontally varying turbulent viscosity grid.
    MUDLAYER: "mudlayer"
        Horizontally varying mud layer thickness grid.
    AICE: "aice"
        Areal ice fraction grid, a number between 0 and 1.
    HICE: "hice"
        Ice thickness grid.
    HSS: "hss"
        Sea-swell significant wave height grid.
    TSS: "tss"
        Sea-swell mean wave period.

    """

    BOTTOM = "bottom"
    WLEVEL = "wlevel"
    CURRENT = "current"
    VX = "vx"
    VY = "vy"
    WIND = "wind"
    WX = "wx"
    WY = "wy"
    FRICTION = "friction"
    NPLANTS = "nplants"
    TURBVISC = "turbvisc"
    MUDLAYER = "mudlayer"
    AICE = "aice"
    HICE = "hice"
    HSS = "hss"
    TSS = "tss"


class BoundShapeOptions(str, Enum):
    """Valid options for the boundary shape type.

    Attributes
    ----------
    JONSWAP: "jonswap"
        JONSWAP spectrum.
    PM: "pm"
        Pierson-Moskowitz spectrum.
    GAUSS: "gauss"
        Gaussian spectrum.
    BIN: "bin"
        Energy at a single bin spectrum.
    TMA: "tma"
        TMA spectrum.

    """

    JONSWAP = "jonswap"
    PM = "pm"
    GAUSS = "gauss"
    BIN = "bin"
    TMA = "tma"


class SideOptions(str, Enum):
    """Valid options for the boundary shape type.

    Attributes
    ----------
    NORTH: "north"
        North side.
    NW: "nw"
        North-west side.
    WEST: "west"
        West side.
    SW: "sw"
        South-west side.
    SOUTH: "south"
        South side.
    SE: "se"
        South-east side.
    EAST: "east"
        East side.
    NE: "ne"
        North-east side.

    """

    NORTH = "north"
    NW = "nw"
    WEST = "west"
    SW = "sw"
    SOUTH = "south"
    SE = "se"
    EAST = "east"
    NE = "ne"


class PhysicsOff(str, Enum):
    """Physics commands to be switched off.

    Attributes
    ----------
    WINDGROWTH : str = "windgrowth"
        Switches off wind growth (in commands GEN1, GEN2, GEN3).
    QUADRUPL : str = "quadrupl"
        Switches off quadruplet wave interactions (in command GEN3).
    WCAPPING : str = "wcapping"
        Switches off whitecapping (in command GEN3).
    BREAKING : str = "breaking"
        Switches off wave breaking dissipation.
    REFRAC : str = "refrac"
        Switches off wave refraction (action transport in theta space).
    FSHIFT : str = "fshift"
        Switches off frequency shifting (action transport in sigma space).
    BNDCHK : str = "bndchk"
        Switches off the checking of the delta imposed and computed Hs at the boundary.

    """

    WINDGROWTH = "windgrowth"
    QUADRUPL = "quadrupl"
    WCAPPING = "wcapping"
    BREAKING = "breaking"
    REFRAC = "refrac"
    FSHIFT = "fshift"
    BNDCHK = "bndchk"


class BlockOptions(str, Enum):
    """Valid options for block output parameters.

    Attributes
    ----------
    HSIGN: "hsign"
        Significant wave height (in m).
    HSWELL: "hswell"
        Swell wave height (in m).
    DIR:
        Mean wave direction (in degrees).
    PDIR:
        Peak wave direction (in degrees).
    TDIR:
        Direction of energy transport (in degrees).
    TM01:
        Mean absolute wave period (in s).
    RTM01:
        Mean relative wave period (in s).
    RTP:
        Peak period of the (relative frequency) variance density spectrum (in s).
    TPS:
        Smoothed peak period (in s).
    PER:
        Mean absolute wave period (in s).
    RPER:
        Mean relative wave period (in s).
    TMM10:
        Mean absolute wave period (in s).
    RTMM10:
        Mean relative wave period (in s).
    TM02:
        Mean absolute zero-crossing period (in s).
    FSPR:
        The normalised width of the frequency spectrum.
    DSPR:
        Directional spreading of the waves (in degrees).
    QP:
        Peakedness of the wave spectrum (dimensionless).
    DEPTH:
        Water depth (in m).
    WATLEV:
        Water level (in m).
    BOTLEV:
        Bottom level (in m).
    VEL:
        Current velocity (vector; in m/s).
    FRCOEF:
        Friction coefficient (equal to `cfw` or `kn` in command `FRICTION`).
    WIND:
        Wind velocity (vector; in m/s).
    AICE:
        Ice concentration (as a fraction from 0 to 1).
    PROPAGAT:
        Sum of PROPXY, PROPTHETA and PROPSIGMA (in W/m2 or m2/s).
    PROPXY:
        Energy propagation in geographic space; sum of x- and y-direction
        (in W/m2 or m2/s).
    PROPTHETA:
        Energy propagation in theta space (in W/m2 or m2/s).
    PROPSIGMA:
        Energy propagation in sigma space (in W/m2 or m2/s).
    GENERAT:
        Total energy generation (in W/m2 or m2/s).
    GENWIND:
        Energy generation due to wind (in W/m2 or m2/s).
    REDIST:
        Total energy redistribution (in W/m2 or m2/s).
    REDQUAD:
        Energy redistribution due to quadruplets (in W/m2 or m2/s).
    REDTRIAD:
        Energy redistribution due to triads (in W/m2 or m2/s).
    DISSIP:
        Total energy dissipation (in W/m2 or m2/s).
    DISBOT:
        Energy dissipation due to bottom friction (in W/m2 or m2/s).
    DISSURF:
        Energy dissipation due to surf breaking (in W/m2 or m2/s).
    DISWCAP:
        Energy dissipation due to whitecapping (in W/m2 or m2/s).
    DISSWELL:
        Energy dissipation due to swell dissipation (in W/m2 or m2/s).
    DISVEG:
        Energy dissipation due to vegetation (in W/m2 or m2/s).
    DISMUD:
        Energy dissipation due to mud (in W/m2 or m2/s).
    DISICE:
        Energy dissipation due to sea ice (in W/m2 or m2/s).
    RADSTR:
        Energy transfer between waves and currents due to radiation stress
        (in W/m2 or m2/s).
    QB:
        Fraction of breaking waves due to depth-induced breaking.
    TRANSP:
        Transport of energy (vector; in W/m2 or m2/s).
    FORCE:
        Wave-induced force per unit surface area (vector; in N/m2).
    UBOT:
        The rms-value of the maxima of the orbital velocity near the bottom (in m/s).
    URMS:
        The rms-value of the orbital velocity near the bottom (in m/s).
    TMBOT:
        The bottom wave period (in s).
    WLENGTH:
        Average wave length (in m).
    LWAVP:
        Peak wave length (in m).
    STEEPNESS:
        Average wave steepness (dimensionless).
    BFI:
        Benjamin-Feir index (dimensionless).
    NPLANTS:
        Number of plants per square meter.
    DHSIGN:
        Difference in significant wave height from the last two iterations (in m).
    DRTM01:
        Difference in average wave period (RTM01) from the last two iterations (in s).
    LEAK:
        Numerical loss of energy equal to `cthetaE(omega,theta)` across boundaries.
    TIME:
        Full date-time string as part of line used in TABLE only.
    TSEC:
        Time in seconds with respect to a reference time (see command QUANTITY).
    XP:
        The x-coordinate in the problem coordinate system of the output location.
    YP:
        The y-coordinate in the problem coordinate system of the output location.
    DIST:
        If output has been requested along a curve then the distance along the curve
        can be obtained with the command TABLE. DIST is the distance along the curve
        measured from teh first point on the curve to the output location on the curve
        in meters (also in the case of spherical coordinates).
    SETUP:
        Set-up due to waves (in m).
    PTHSIGN:
        Watershed partitions of the significant wave height (in m).
    PTRTP:
        Watershed partitions of the relative peak period (in s).
    PTWLEN:
        Watershed partitions of the average wave length (in m).
    PTDIR:
        Watershed partitions of the peak wave direction (in degrees).
    PTDSPR:
        Watershed partitions of the directional spreading (in degrees).
    PTWFRAC:
        Watershed partitions of the wind fraction (dimensionless).
    PTSTEEPNE:
        Watershed partition of the wave steepness (dimensionless).
    PARTITION:
        The raw spectral partition for wave system tracking post-processing.

    Note
    ----
    Energy given in W/m2 or m2/s depending on command SET.

    Note
    ----
    UBOT and URMS required command `FRICTION` to be used. If friction is ignored in the
    computation, then one should use the command `FRICTION` with the value of the
    friction set to zero (e.g., `FRICTION COLLINS 0`).

    """

    HSIGN = "hsign"
    HSWELL = "hswell"
    DIR = "dir"
    PDIR = "pdir"
    TDIR = "tdir"
    TM01 = "tm01"
    RTM01 = "rtm01"
    RTP = "rtp"
    TPS = "tps"
    PER = "per"
    RPER = "rper"
    TMM10 = "tmm10"
    RTMM10 = "rtmm10"
    TM02 = "tm02"
    FSPR = "fspr"
    DSPR = "dspr"
    QP = "qp"
    DEPTH = "depth"
    WATLEV = "watlev"
    BOTLEV = "botlev"
    VEL = "vel"
    FRCOEF = "frcoef"
    WIND = "wind"
    AICE = "aice"
    PROPAGAT = "propagat"
    PROPXY = "propxy"
    PROPTHETA = "proptheta"
    PROPSIGMA = "propsigma"
    GENERAT = "generat"
    GENWIND = "genwind"
    REDIST = "redist"
    REDQUAD = "redquad"
    REDTRIAD = "redtriad"
    DISSIP = "dissip"
    DISBOT = "disbot"
    DISSURF = "dissurf"
    DISWCAP = "diswcap"
    DISSWELL = "disswell"
    DISVEG = "disveg"
    DISMUD = "dismud"
    DISICE = "disice"
    RADSTR = "radstr"
    QB = "qb"
    TRANSP = "transp"
    FORCE = "force"
    UBOT = "ubot"
    URMS = "urms"
    TMBOT = "tmbot"
    WLEN = "wlen"
    LWAVP = "lwavp"
    STEEPNESS = "steepness"
    BFI = "bfi"
    NPLANTS = "nplants"
    DHSIGN = "dhsign"
    DRTM01 = "drtm01"
    LEAK = "leak"
    TIME = "time"
    TSEC = "tsec"
    XP = "xp"
    YP = "yp"
    DIST = "dist"
    SETUP = "setup"
    PTHSIGN = "pthsign"
    PTRTP = "ptrtp"
    PTWLEN = "ptwlen"
    PTDIR = "ptdir"
    PTDSPR = "ptdspr"
    PTWFRAC = "ptwfrac"
    PTSTEEP = "ptsteep"
    PTSTEEPNE = "ptsteepne"
    PARTITION = "partition"