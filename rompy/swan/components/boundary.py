"""Boundary for SWAN."""
from typing import Literal, Optional, Any
from pathlib import Path
from typing_extensions import Literal
from pydantic import root_validator, confloat, constr

from rompy.swan.components.base import BaseComponent
from rompy.swan.subcomponents.shape import SHAPESPEC
from rompy.swan.subcomponents.boundary import (
    SIDE,
    SEGMENTXY,
    SEGMENTIJ,
    CONSTANTPAR,
    VARIABLEPAR,
    CONSTANTFILE,
    VARIABLEFILE,
)


HERE = Path(__file__).parent


class BOUNDSPEC(BaseComponent):
    """SWAN BOUNDSPEC boundary component.

    `BOUNDSPEC SIDE|SEGMENT ... CONSTANT|VARIABLE PAR|FILE ...`

    This command BOUNDSPEC defines parametric spectra at the boundary. It consists of
    two parts, the first part defines the boundary side or segment where the spectra
    will be given, the second part defines the spectral parameters of these spectra.
    Note that in fact only the incoming wave components of these spectra are used by
    SWAN. The fact that complete spectra are calculated at the model boundaries from
    the spectral parameters should not be misinterpreted. Only the incoming components
    are effective in the computation.

    Parameters
    ----------
    model_type: Literal["boundspec"]
        Model type discriminator.
    shapespec: Optional[SHAPESPEC]
        Spectral shape specification.
    location: SIDE | SEGMENTXY | SEGMENTIJ
        Location to apply th boundary.
    data: CONSTANTPAR | CONSTANTFILE | VARIABLEPAR | VARIABLEFILE
        Spectral data.

    TODO: Add support for unstructured grid (k).

    """

    model_type: Literal["boundspec"] = "boundspec"
    shapespec: SHAPESPEC = SHAPESPEC()
    location: SIDE | SEGMENTXY | SEGMENTIJ
    data: CONSTANTPAR | CONSTANTFILE | VARIABLEPAR | VARIABLEFILE

    def __repr__(self):
        repr = f"{self.shapespec.render()}\n"
        repr += f"BOUNDSPEC {self.location.render()}{self.data.render()}"
        return repr


class BOUNDNEST1(BaseComponent):
    """Boundary spectra from a coarser SWAN nest at all sides of computational domain.

    `BOUNDNEST1 NEST 'fname CLOSED|OPEN`

    Parameters
    ----------
    model_type: Literal["boundnest1"]
        Model type discriminator.
    fname: str
        Name of the file containing the boundary conditions for the present run,
        created by the previous SWAN coarse grid run. This file is structured
        according to the rules given in Appendix D for 2D spectra.
    rectangle: Literal["closed", "open"]
        Defines if the boundary is defined over a closed (default) or an open
        rectangle. Boundary generated from the NESTOUT command is aways closed.

    With this optional command a nested SWAN run can be carried out with the boundary
    conditions obtained from a coarse grid SWAN run (generated in that previous SWAN
    run with command NESTOUT). The spectral frequencies and directions of the coarse
    grid run do not have to coincide with the frequencies and directions used in the
    nested SWAN run; SWAN will interpolate to these frequencies and directions in the
    nested run (see Section 2.6.3). To generate the nest boundary in the coarse grid
    run, use command NGRID. For the nested run, use the command CGRID with identical
    geographical information except the number of meshes (which will be much higher for
    the nested run). This BOUNDNEST1 command is not available for 1D computations; in
    such cases the commands SPECOUT and BOUNDSPEC can be used for the same purpose. A
    nested SWAN run must use the same coordinate system as the coarse grid SWAN run.
    For a curvilinear grid, it is advised to use the commands POINTS or CURVE and
    SPECOUT instead of NGRID and NESTOUT.

    """

    model_type: Literal["boundnest1"] = "boundnest1"
    fname: constr(min_length=1, max_length=98)
    rectangle: Literal["closed", "open"] = "closed"

    def __repr__(self):
        return f"BOUNDNEST1 NEST fname='{self.fname}' {self.rectangle.upper()}"


class BOUNDNEST2(BaseComponent):
    """Boundary spectra from a coarser SWAN nest at all sides of computational domain.

    `BOUNDNEST2 WAMNEST 'fname FREE|UNFORMATTED (CRAY|WKSTAT) [xgc] [ygc] [lwdate]`

    Parameters
    ----------
    model_type: Literal["boundnest2"]
        Model type discriminator.
    fname: str
        A file name that contains all the names of WAM files containing the nested
        boundary conditions in time-sequence (usually one file per day). For example,
        the contents of 'fname' can look like:
            CBO9212010000
            CBO9212020000
            CBO9212030000
    format: Literal["cray", wkstat", "free"]
        Format of the WAM files.
        - cray: CRAY version of WAM.
        - wkstat: WORKSTATION version of WAM.
        - free: Free format (these files are not generated standard by WAM).
    xgc: float
        - If SWAN is used with Cartesian coordinates: longitude of south-west corner of
          SWAN computational grid (in degrees); if the south-west corner of the nest in
          the WAM computation is on land this value is required.
        - If SWAN is used with spherical coordinates then [xgc] is ignored by SWAN.
          Default: the location of the first spectrum encountered in the nest file.
    ygc: float
        - if SWAN is used with Cartesian coordinates: latitude of south-west corner of
          SWAN computational grid (in degrees); if the south-west corner of the nest in
          the WAM computation is on land this value is required.
        - If SWAN is used with spherical coordinates then [ygc] is ignored by SWAN.
          Default: the location of the first spectrum encountered in the nest file.
    lwdate: str
        Length of character string for date-time as used in the WAM files. Possible
        values are: 10 (i.e. YYMMDDHHMM), 12 (i.e. YYMMDDHHMMSS) or
        14 (i.e. YYYYMMDDHHMMSS). Default: `lwdate` = 12

    With this optional command (not fully tested) a nested SWAN run can be carried out
    with the boundary conditions obtained from a coarse grid WAM run (WAM Cycle 4.5,
    source code as distributed by the Max Planck Institute in Hamburg). The spectral
    frequencies and directions of the coarse grid run do not have to coincide with the
    frequencies and directions used in the nested SWAN run; SWAN will interpolate to
    these frequencies and directions in the nested run (see Section 2.6.3). Note that
    SWAN will accept output of a WAM output location only if the SWAN grid point on the
    nest boundary lies within a rectangle between two consecutive WAM output locations
    with a width equal to 0.1 times the distance between these output locations on
    either side of the line between these WAM output locations. This BOUNDNEST2 command
    is not available for 1D computations. Only boundary conditions generated by WAM
    Cycle 4.5 can be read properly by SWAN. A nested SWAN run may use either Cartesian
    or spherical coordinates. A curvilinear grid may be used in the nested grid but the
    boundaries of this nest should conform to the rectangular course grid nest
    boundaries. WAM output files are unformatted (binary); this usually implies that
    WAM and SWAN have to run on the same computer. For those cases where WAM and SWAN
    run on different types of machines (binary files do not transfer properly), the
    option FREE is available in this command. The distributed version of WAM does not
    support the required free format nesting output; WAM users who modify WAM such that
    it can make formatted output, must modify WAM such that the files made by WAM can
    be read in free format, i.e. with at least a blank or comma between numbers.

    """

    model_type: Literal["boundnest2"] = "boundnest2"
    fname: constr(min_length=1, max_length=98)
    format: Literal["cray", "wkstat", "free"]
    xgc: Optional[float]
    ygc: Optional[float]
    lwdate: Literal[10, 12, 14] = 12

    @property
    def format_str(self):
        if self.format == "cray":
            return "UNFORMATTED CRAY"
        elif self.format == "wkstat":
            return "UNFORMATTED WKSTAT"
        elif self.format == "free":
            return "FREE"
        else:
            raise ValueError(f"Unknown format {self.format}")

    def __repr__(self):
        repr = f"BOUNDNEST2 WAMNEST fname='{self.fname}' {self.format_str}"
        if self.xgc is not None:
            repr += f" xgc={self.xgc}"
        if self.ygc is not None:
            repr += f" ygc={self.ygc}"
        repr += f" lwdate={self.lwdate}"
        return repr
