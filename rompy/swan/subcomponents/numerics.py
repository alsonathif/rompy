"""SWAN numerics subcomponents."""
from typing import Annotated, Literal, Optional, Union
from pydantic import field_validator, Field, model_validator
from abc import ABC
from pydantic_numpy.typing import Np2DArray
import numpy as np

from rompy.swan.subcomponents.base import BaseSubComponent


class BSBT(BaseSubComponent):
    """BSBT first order propagation scheme.

    .. code-block:: text

        BSTB

    Examples
    --------

    .. ipython:: python
        :okwarning:
        :okexcept:

        @suppress
        from rompy.swan.subcomponents.numerics import BSBT

        scheme = BSBT()
        print(scheme.render())

    """

    model_type: Literal["bsbt", "BSBT"] = Field(
        default="bsbt", description="Model type discriminator"
    )

    def cmd(self) -> str:
        """Command file string for this component."""
        return "BSBT"


class GSE(BaseSubComponent):
    """Garden-sprinkler effect.

    .. code-block:: text

        GSE [waveage] Sec|MIn|HR|DAy

    Garden-sprinkler effect is to be counteracted in the S&L propagation scheme
    (default for nonstationary regular grid computations) or in the propagation
    scheme for unstructured grids by adding a diffusion term to the basic equation.
    This may affect the numerical stability of SWAN.

    Examples
    --------

    .. ipython:: python
        :okwarning:
        :okexcept:

        @suppress
        from rompy.swan.subcomponents.numerics import GSE

        scheme = GSE(waveage=1, units="day")
        print(scheme.render())

    """

    model_type: Literal["gse", "GSE"] = Field(
        default="gse", description="Model type discriminator"
    )
    waveage: Optional[float] = Field(
        default=None,
        description=(
            "The time interval used to determine the diffusion which counteracts the "
            "so-called garden-sprinkler effect. The default value of `waveage` is "
            "zero, i.e. no added diffusion. The value of `waveage` should correspond "
            "to the travel time of the waves over the computational region."
        ),
    )
    units: Literal["sec", "min", "hr", "day"] = Field(
        default="hr", description="Units for waveage",
    )

    def cmd(self) -> str:
        """Command file string for this component."""
        repr = "GSE"
        if self.waveage is not None:
            repr += f" waveage={self.waveage} {self.units.upper()}"
        return repr


class STAT(BaseSubComponent):
    """Iteration termination for stationary computations.

    .. code-block:: text

        STAT [mxitst] [alfa]

    Examples
    --------
    .. ipython:: python
        :okwarning:
        :okexcept:

        @suppress
        from rompy.swan.subcomponents.numerics import STAT

        stat = STAT()
        print(stat.render())
        stat = STAT(mxitst=10, alfa=0.1)
        print(stat.render())

    """
    model_type: Literal["stat", "STAT"] = Field(
        default="stat", description="Model type discriminator"
    )
    mxitst: Optional[int] = Field(
        default=None,
        description=(
            "Maximum number of iterations for stationary computations, the "
            "computation stops when this number is exceeded (SWAN default: 50)"
        ),
    )
    alfa: Optional[float] = Field(
        default=None,
        description=(
            "Proportionality constant used in the frequency-dependent under-"
            "relaxation technique. Based on experiences, a suggestion for this "
            "parameter is `alfa = 0.01`. In case of diffraction computations, the use "
            "of this parameter is recommended (SWAN default: 0.00)"
        ),
    )

    def cmd(self) -> str:
        """Command file string for this component."""
        repr = "STAT"
        if self.mxitst is not None:
            repr += f" mxitst={self.mxitst}"
        if self.alfa is not None:
            repr += f" alfa={self.alfa}"
        return repr


class NONSTAT(BaseSubComponent):
    """Iteration termination for nonstationary computations.

    .. code-block:: text

        NONSTAT [mxitst]

    Examples
    --------
    .. ipython:: python
        :okwarning:
        :okexcept:

        @suppress
        from rompy.swan.subcomponents.numerics import NONSTAT

        nonstat = NONSTAT()
        print(nonstat.render())
        nonstat = NONSTAT(mxitst=3)
        print(nonstat.render())

    """
    model_type: Literal["nonstat", "NONSTAT"] = Field(
        default="nonstat", description="Model type discriminator"
    )
    mxitst: Optional[int] = Field(
        default=None,
        description=(
            "Maximum number of iterations for stationary computations, the "
            "computation moves to the next time step when this number is exceeded "
            "(SWAN default: 1)"
        ),
    )

    def cmd(self) -> str:
        """Command file string for this component."""
        repr = "NONSTAT"
        if self.mxitst is not None:
            repr += f" mxitst={self.mxitst}"
        return repr


class STOPC(BaseSubComponent):
    """Stop the iterative procedure.

    .. code-block:: text

        STOPC [dabs] [drel] [curvat] [npnts] ->STAT|NONSTAT [limiter]

    With this option the user can influence the criterion for terminating the iterative
    procedure in the SWAN computations (both stationary and nonstationary). The
    criterion make use of the second derivative, or curvature, of the iteration curve
    of the significant wave height. As the solution of a simulation approaches full
    convergence, the curvature of the iteration curve will tend to zero. SWAN stops the
    process if the relative change in Hs from one iteration to the next is less than
    `drel` and the curvature of the iteration curve of Hs normalized with Hs is less
    than `curvat` or the absolute change in Hs from one iteration to the next is less
    than `dabs`. Both conditions need to be fulfilled in more than fraction `npnts`% of
    all wet grid points.

    With respect to the QC modelling, another stopping criteria will be employed.
    Namely, SWAN stops the iteration process if the absolute change in Hs from one
    iterate to another is less than `dabs` * Hinc, where Hinc is the representative
    incident wave height, or the relative change in Hs from one to the next iteration
    is less than `drel`. These criteria must be fulfilled in more than `npnts`% of
    all active, well-defined points.

    Examples
    --------

    .. ipython:: python
        :okwarning:
        :okexcept:

        @suppress
        from rompy.swan.subcomponents.numerics import STOPC

        stop = STOPC()
        print(stop.render())
        stop=STOPC(
            dabs=0.005,
            drel=0.01,
            curvat=0.005,
            npnts=99.5,
            mode=dict(model_type="nonstat", mxitns=1),
        )
        print(stop.render())

    """
    model_type: Literal["stopc", "STOPC"] = Field(
        default="stopc", description="Model type discriminator"
    )
    dabs: Optional[float] = Field(
        default=None,
        description=(
            "Maximum absolute change in Hs from one iteration to the next "
            "(SWAN default: 0.005 [m] or 0.05 [-] in case of QC model)"
        ),
    )
    drel: Optional[float] = Field(
        default=None,
        description=(
            "Maximum relative change in Hs from one iteration to the next "
            "(SWAN default: 0.01 [-])"
        ),
    )
    curvat: Optional[float] = Field(
        default=None,
        description=(
            "Maximum curvature of the iteration curve of Hs normalised with Hs "
            "(SWAN default: 0.005 [-] (not used in the QC model))"
        ),
    )
    npnts: Optional[float] = Field(
        default=None,
        description=(
            "Percentage of points in the computational grid above which the stopping "
            "criteria needs to be satisfied (SWAN default: 99.5 [-])"
        ),
    )
    mode: Optional[Union[STAT, NONSTAT]] = Field(
        default=None,
        description=(
            "Iteration termination criteria for stationary or nonstationary runs"
        ),
    )
    limiter: Optional[float] = Field(
        default=None,
        description=(
            "Determines the maximum change per iteration of the energy density per "
            "spectral-bin given in terms of a fraction of the omni-directional "
            "Phillips level (SWAN default: 0.1)"
        ),
    )

    def cmd(self) -> str:
        """Command file string for this component."""
        repr = "STOPC"
        if self.dabs is not None:
            repr += f" dabs={self.dabs}"
        if self.drel is not None:
            repr += f" drel={self.drel}"
        if self.curvat is not None:
            repr += f" curvat={self.curvat}"
        if self.npnts is not None:
            repr += f" npnts={self.npnts}"
        if self.mode is not None:
            repr += f" {self.mode.render()}"
        if self.limiter is not None:
            repr += f" limiter={self.limiter}"
        return repr


class DIRIMPL(BaseSubComponent):
    """Numerical scheme for refraction.

    .. code-block:: text

        DIRIMPL [cdd]

    Examples
    --------
    .. ipython:: python
        :okwarning:
        :okexcept:

        @suppress
        from rompy.swan.subcomponents.numerics import DIRIMPL

        dirimpl = DIRIMPL()
        print(dirimpl.render())
        dirimpl = DIRIMPL(cdd=0.5)
        print(dirimpl.render())

    """
    model_type: Literal["dirimpl", "DIRIMPL"] = Field(
        default="dirimpl", description="Model type discriminator"
    )
    cdd: Optional[float] = Field(
        default=None,
        description=(
            "A value of `cdd=0` corresponds to a central scheme and has the largest "
            "accuracy (diffusion ≈ 0) but the computation may more easily generate"
            "spurious fluctuations. A value of `cdd=1` corresponds to a first order"
            "upwind scheme and it is more diffusive and therefore preferable if "
            "(strong) gradients in depth or current are present (SWAN default: 0.5)"
        ),
    )

    def cmd(self) -> str:
        """Command file string for this component."""
        repr = "DIRIMPL"
        if self.cdd is not None:
            repr += f" cdd={self.cdd}"
        return repr