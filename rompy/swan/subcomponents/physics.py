"""SWAN physics subcomponents."""
from typing import Literal, Optional
from pydantic import Field, root_validator, confloat
from abc import ABC

from rompy.swan.subcomponents.base import BaseSubComponent


#======================================================================================
# Source terms
#======================================================================================
class SourceTerms(BaseSubComponent, ABC):
    """Source term subcomponent base class."""

    wind_drag: Literal["wu", "fit"] = Field(
        default="wu",
        description="Indicates the wind drag formulation",
    )
    agrow: bool = Field(
        default=False,
        description="Activate the Cavaleri and Malanotte (1981) wave growth term",
    )
    a: Optional[float] = Field(
        default=0.0015,
        description="Proportionality coefficient when activating the Cavaleri and Malanotte (1981) wave growth term",
    )


class JANSSEN(SourceTerms):
    """Janssen source terms subcomponent.

    `JANSSEN [cds1] [delta]`

    References
    ----------
    Janssen, P.A.E.M., 1989: Wave induced stress and the drag of air flow
    over sea waves, J. Phys. Oceanogr., 19, 745-754.

    Janssen, P.A.E.M., 1991: Quasi-linear theory of wind-wave generation
    applied to wave forecasting, J. Phys. Oceanogr., 21, 1631-1642.

    """

    model_type: Literal["janssen"] = Field(
        default="janssen", description="Model type discriminator"
    )
    cds1: Optional[float] = Field(
        description="Coefficient for determining the rate of whitecapping dissipation ($Cds / s^4_{PM}$) (SWAN default: 4.5)"
    )
    delta: Optional[float] = Field(
        description="Coefficient which determines the dependency of the whitecapping on wave number (mix with Komen et al. formulation) (SWAN default: 0.5)"
    )

    def cmd(self):
        repr = "JANSSEN"
        if self.cds1 is not None:
            repr += f" cds1={self.cds1}"
        if self.delta is not None:
            repr += f" delta={self.delta}"
        repr += f" DRAG {self.wind_drag.upper()}"
        if self.agrow:
            repr += f" AGROW a={self.a}"
        return repr


class KOMEN(SourceTerms):
    """Komen source terms subcomponent.

    `KOMEN [cds2] [stpm]`

    References
    ----------
    Komen, G.J., S. Hasselmann, and K. Hasselmann, 1984: On the existence of a fully
    developed wind-sea spectrum, J. Phys. Oceanogr., 14, 1271-1285.

    """

    model_type: Literal["komen"] = Field(
        default="komen", description="Model type discriminator"
    )
    cds2: Optional[float] = Field(
        description="Coefficient for determining the rate of whitecapping dissipation ($Cds$) (SWAN default: 2.36e-5)"
    )
    stpm: Optional[float] = Field(
        description="Value of the wave steepness for a Pierson-Moskowitz spectrum ($s^2_{PM}$) (SWAN default: 3.02e-3)"
    )

    def cmd(self):
        repr = "KOMEN"
        if self.cds2 is not None:
            repr += f" cds2={self.cds2}"
        if self.stpm is not None:
            repr += f" stpm={self.stpm}"
        repr += f" DRAG {self.wind_drag.upper()}"
        if self.agrow:
            repr += f" AGROW a={self.a}"
        return repr


class WESTHUYSEN(SourceTerms):
    """Westhuysen source terms subcomponent.

    `WESTHUYSEN [cds2] [br]`

    Nonlinear saturation-based whitecapping combined with wind input of Yan (1987).

    Notes
    -----
    The two arguments are specified in the Appendix C of the User manual but not in the
    command description for WESTH in Section 4.5.4. They are also options in the
    WCAPPING command. It is not entirely clear if they should/could be specified here.

    References
    ----------
    Van der Westhuysen, A.J., M. Zijlema and J.A. Battjes, 2007: Nonlinear
    saturation-based whitecapping dissipation in SWAN for deep and shallow water,
    Coast. Engng, 54:2, 151-170.

    """

    model_type: Literal["westhuysen"] = Field(
        default="westhuysen", description="Model type discriminator"
    )
    cds2: Optional[float] = Field(
        description="proportionality coefficient due to Alves and Banner (2003) (SWAN default: 5.0e-5)."
    )
    br: Optional[float] = Field(
        description="Threshold saturation level	(SWAN default: 1.75e-3)"
    )

    def cmd(self):
        repr = "WESTHUYSEN"
        if self.cds2 is not None:
            repr += f" cds2={self.cds2}"
        if self.br is not None:
            repr += f" br={self.br}"
        repr += f" DRAG {self.wind_drag.upper()}"
        if self.agrow:
            repr += f" AGROW a={self.a}"
        return repr


class ST6(SourceTerms):
    """St6 source terms subcomponent.

    `ST6 [a1sds] [a2sds] [p1sds] [p2sds] UP|DOWN HWANG|FAN|ECMWF VECTAU|SCATAU `
    `    TRUE10|U10PROXY [windscaling] DEBIAS [cdfac]`

    wind input and whitecapping from Rogers et al. (2012) (RBW12).

    Notes
    -----
    The two arguments are specified in the Appendix C of the User manual but not in the
    command description for WESTH in Section 4.5.4. They are also options in the
    WCAPPING command. It is not entirely clear if they should/could be specified here.

    References
    ----------
    Rogers, W.E., A.V. Babanin and D.W. Wang, 2012: Observation-Consistent Input and
    Whitecapping Dissipation in a Model for Wind-Generated Surface Waves: Description
    and Simple Calculations, J. Atmos. Oceanic Technol., 29:9, 1329-1346.

    """

    model_type: Literal["st6"] = Field(
        default="st6", description="Model type discriminator"
    )
    a1sds: float = Field(
        description="Coefficient related to local dissipation term T1 (a1 in RBW12)"
    )
    a2sds: float = Field(
        description="Coefficient related to local dissipation term T2 (a2 in RBW12)"
    )
    p1sds: Optional[float] = Field(
        description="Power coefficient controlling strength of dissipation term T1 (L in RBW12, SWAN default: 4)"
    )
    p2sds: Optional[float] = Field(
        description="Power coefficient controlling strength of dissipation term T2 (M in RBW12, SWAN default: 4)"
    )
    normalization: Literal["up", "down"] = Field(
        default="up",
        description="Selection of normalization of exceedance level by ET(f) (`up`) or E(f) (`down`) as in RBW12 (right column, page 1333), `up` is default and strongly recommended",
    )
    wind_drag: Literal["hwang", "fan", "ecmwf"] = Field(
        default="hwang",
        description="Wind drag formula, `hwang` is the default and is unchanged from RBW12, `fan` is from Fan et al. (2012), `ecmwf` follows teh WAM Cycle 4 methodology",
    )
    tau: Literal["vectau", "scatau"] = Field(
        default="vectau",
        description="Use vector (vectau) or scalar (scatau) calculation for the wind strerss (Eq. 12 in RBW12), `vectau` is the default and strongly recommended",
    )
    u10: Literal["u10proxy", "true10"] = Field(
        default="u10proxy",
        description="Wind velocity definition",
    )
    windscaling: Optional[float] = Field(
        default=32.0,
        description="Factor to scale U10 with U* when using U10PROXY",
    )
    cdfac: Optional[confloat(gt=0.0)] = Field(
        description="Counter bias in the input wind fields by providing a multiplier on the drag coefficient",
    )

    @root_validator
    def debias_only_with_hwang(cls, values):
        debias = values.get("debias")
        wind_drag = values.get("wind_drag", "hwang")
        if debias is not None and wind_drag != "hwang":
            raise ValueError(
                f"Debias is only supported with hwang wind drag, not {wind_drag}"
            )
        return values

    @property
    def u10_cmd(self):
        if self.u10 == "true10":
            return "TRUE10"
        else:
            return f"U10PROXY windscaling={self.windscaling}"

    def cmd(self):
        repr = f"ST6 a1sds={self.a1sds} a2sds={self.a2sds}"
        if self.p1sds is not None:
            repr += f" p1sds={self.p1sds}"
        if self.p2sds is not None:
            repr += f" p2sds={self.p2sds}"
        repr += f" {self.normalization.upper()}"
        repr += f" {self.wind_drag.upper()}"
        repr += f" {self.tau.upper()}"
        repr += f" {self.u10_cmd}"
        if self.cdfac is not None:
            repr += f" DEBIAS cdfac={self.cdfac}"
        if self.agrow:
            repr += f" AGROW a={self.a}"
        return repr


class ST6C1(ST6):
    """First ST6 calibration settings defined in the SWAN user manual."""

    model_type: Literal["st6c1"] = Field(default="st6c1")
    a1sds: Literal[4.7e-7] = Field(default=4.7e-7)
    a2sds: Literal[6.6e-6] = Field(default=6.6e-6)
    p1sds: Literal[4.0] = Field(default=4.0)
    p2sds: Literal[4.0] = Field(default=4.0)
    windscaling: Literal[28.0] = Field(default=28.0)
    agrow: Literal[True] = Field(default=True)


class ST6C2(ST6C1):
    """Second ST6 calibration settings defined in the SWAN user manual."""

    model_type: Literal["st6c2"] = Field(default="st6c2")
    wind_drag: Literal["fan"] = Field(default="fan")


class ST6C3(ST6C1):
    """Third ST6 calibration settings defined in the SWAN user manual."""

    model_type: Literal["st6c3"] = Field(default="st6c3")
    a1sds: Literal[2.8e-6] = Field(default=2.8e-6)
    a2sds: Literal[3.5e-5] = Field(default=3.5e-5)
    windscaling: Literal[32.0] = Field(default=32.0)


class ST6C4(ST6C3):
    """Forth ST6 calibration settings defined in the SWAN user manual."""

    model_type: Literal["st6c4"] = Field(default="st6c4")
    cdfac: Literal[0.89] = Field(default=0.89)


class ST6C5(ST6C1):
    """Fifth ST6 calibration settings defined in the SWAN user manual."""

    model_type: Literal["st6c5"] = Field(default="st6c5")
    cdfac: Literal[0.89] = Field(default=0.89)
    a1sds: Literal[6.5e-6] = Field(default=6.5e-6)
    a2sds: Literal[8.5e-5] = Field(default=8.5e-5)
    windscaling: Literal[35.0] = Field(default=35.0)


class NEGATINP(BaseSubComponent):
    """Nonbreaking dissipation of Young et al. (2013) updated by Zieger et al. (2015).

    With this optional command the user activates negative wind input. This is intended
    only for use with non-breaking swell dissipation SSWELL ZIEGER. Parameter `rdcoef`
    is a fraction between 0 and 1, representing the strength of negative wind input. As
    an example, with [rdcoef]=0.04, for a spectral bin that is opposed to the wind
    direction, the wind input factor W(k, θ) is negative, and its magnitude is 4% of
    the corresponding value of the spectral bin that is in the opposite direction
    (i.e. in the wind direction). See Zieger et al. (2015) eq. 11, where a0 is their
    notation for [rdcoef]. Default [rdcoef]=0.0 and `rdcoef=0.04` is recommended,
    though as implied by Zieger et al. (2015), this value is not well-established, so
    the user is encouraged to experiment with other values.

    References
    ----------
    Zieger, S., A.V. Babanin, W. E. Rogers and I.R. Young, 2015: Observation-based
    source terms in the third-generation wave model WAVEWATCH, Ocean Model., 96, 2-25.

    """

    model_type: Literal["negatinp"] = Field(
        default="negatinp", description="Model type discriminator"
    )
    rdcoef: confloat(ge=0.0, le=1.0) = Field(
        default=0.0,
        description="Coefficient representing the strength of negative wind input",
    )

    def cmd(self):
        return f"NEGATINP rdcoef={self.rdcoef}"


#======================================================================================
# SSWELL
#======================================================================================
class SSWELL(BaseSubComponent):
    """Swell dissipation sub-component.

    `SSWELL`

    With this command the user can influence the type of swell dissipation included in
    the computations. The Zieger option is intended for use with negative wind input
    via the NEGATINP command. Zieger non-breaking dissipation follows the method used
    in WAVEWATCH III version 4 and does not include the steepness-dependent swell
    coefficient introduced in WAVEWATCH III version 5. As noted already, if
    `GEN3 ST6...` command is used, this SSWELL command should be provided.

    """

    model_type: Literal["sswell"] = Field(
        default="sswell", description="Model type discriminator"
    )

    def cmd(self):
        return "SSWELL"


class ROGERS(SSWELL):
    """Nonbreaking dissipation of Rogers et al. (2012).

    References
    ----------
    Rogers, W.E., A.V. Babanin and D.W. Wang, 2012: Observation-Consistent Input and
    Whitecapping Dissipation in a Model for Wind-Generated Surface Waves: Description
    and Simple Calculations, J. Atmos. Oceanic Technol., 29:9, 1329-1346.

    """

    model_type: Literal["rogers"] = Field(
        default="rogers", description="Model type discriminator"
    )
    cdsv: Optional[float] = Field(
        description="Coefficient related to laminar atmospheric boundary layer (SWAN default: 1.2)"
    )
    feswell: Optional[float] = Field(
        description="Swell dissipation factor"
    )

    def cmd(self):
        repr = f"{super().cmd()} ROGERS"
        if self.cdsv is not None:
            repr += f" cdsv={self.cdsv}"
        if self.feswell is not None:
            repr += f" feswell={self.feswell}"
        return repr


class ARDHUIN(SSWELL):
    """Nonbreaking dissipation of Ardhuin et al. (2010).

    References
    ----------
    Ardhuin, F., A. Rogers, A. Babanin, J. Filipot, J. Magne, A. Roland, and P. van
    der Westhuysen, 2010: Semiempirical dissipation source functions for ocean waves.
    Part I: Definition, calibration, and validation, J. Phys. Oceanogr., 40, 1917-1941.

    """

    model_type: Literal["ardhuin"] = Field(
        default="ardhuin", description="Model type discriminator"
    )
    cdsv: Optional[float] = Field(
        description="Coefficient related to laminar atmospheric boundary layer (SWAN default: 1.2)"
    )

    def cmd(self):
        repr = f"{super().cmd()} ARDHUIN"
        if self.cdsv is not None:
            repr += f" cdsv={self.cdsv}"
        return repr


class ZIEGER(SSWELL):
    """Nonbreaking dissipation of Young et al. (2013) updated by Zieger et al. (2015).

    References
    ----------
    Zieger, S., A.V. Babanin, W. E. Rogers and I.R. Young, 2015: Observation-based
    source terms in the third-generation wave model WAVEWATCH, Ocean Model., 96, 2-25.

    Young, I.R., A.V.Babanin and S. Zieger, 2013: The Decay Rate of Ocean Swell
    Observed by Altimeter, J. Phys. Oceanogr., 43, 3233-3233.

    """

    model_type: Literal["zieger"] = Field(
        default="zieger", description="Model type discriminator"
    )
    b1: Optional[float] = Field(
        description="Non-dimensional proportionality coefficient"
    )
    negatinp: NEGATINP = Field(
        default=NEGATINP(),
        description="Negative wind input specification",
    )

    def cmd(self):
        repr = f"{super().cmd()} ZIEGER"
        if self.b1 is not None:
            repr += f" b1={self.b1}"
        return repr


#======================================================================================
# WCAPPING
#======================================================================================
class WCAPKOMEN(KOMEN):
    """Komen whitecapping sub-component.

    `WCAPPING KOMEN [cds2] [stpm] [powst] [delta] [powk]`

    Notes
    -----
    The SWAN default for `delta` has been changed since version 40.91A. The setting
    `delta = 1` will improve the prediction of the wave energy at low frequencies, and
    hence the mean wave period. The original default was `delta = 0`, which corresponds
    to WAM Cycle 3. See the Scientific/Technical documentation for further details.

    """
    model_type: Literal["wcapkomen"] = Field(
        default="wcapkomen", description="Model type discriminator"
    )
    powst: Optional[float] = Field(
        description="Power of steepness normalized with the wave steepness of a Pierson-Moskowitz spectrum (SWAN default: 2)"
    )
    delta: Optional[float] = Field(
        description="Coefficient which determines the dependency of the whitecapping on wave number (SWAN default: 1)"
    )
    powk: Optional[float] = Field(
        description="power of wave number normalized with the mean wave number (SWAN default: 1)",
    )

    def cmd(self):
        repr = f"WCAPPING KOMEN"
        if self.cds2 is not None:
            repr += f" cds2={self.cds2}"
        if self.stpm is not None:
            repr += f" stpm={self.stpm}"
        if self.powst is not None:
            repr += f" powst={self.powst}"
        if self.delta is not None:
            repr += f" delta={self.delta}"
        if self.powk is not None:
            repr += f" powk={self.powk}"
        return repr


class WCAPAB(WESTHUYSEN):
    """Whitecapping according to Alves and Banner (2003).

    `WCAPPING AB [cds2] [br] [cds3]`

    References
    ----------
    Alves, J.H.G.M. and M.L. Banner, 2003: A unified formulation of the wave-action
    balance equation, J. Phys. Oceanogr., 33, 2343-2356.

    """
    model_type: Literal["wcapab"] = Field(
        default="wcapab", description="Model type discriminator"
    )
    current: bool = Field(
        default=False,
        description="Indicates that enhanced current-induced dissipation as proposed by Van der Westhuysen (2012) is to be added",
    )
    cds3: Optional[float] = Field(
        description="Proportionality coefficient (SWAN default: 0.8)"
    )

    def cmd(self):
        repr = f"WCAPPING AB"
        if self.cds2 is not None:
            repr += f" cds2={self.cds2}"
        if self.br is not None:
            repr += f" br={self.br}"
        if self.current:
            repr += f" CURRENT"
        if self.cds3 is not None:
            repr += f" cds3={self.cds3}"
        return repr