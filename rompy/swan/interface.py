"""SWAN interface objects."""
import logging
from typing import Optional, Literal, Any
from pathlib import Path
from pydantic import Field, model_validator

from rompy.core import RompyBaseModel, TimeRange
from rompy.swan.grid import SwanGrid
from rompy.swan.data import SwanDataGrid
from rompy.swan.boundary import DataBoundary

from rompy.swan.subcomponents.time import TimeRangeOpen, STATIONARY, NONSTATIONARY


logger = logging.getLogger(__name__)


class ForcingData(RompyBaseModel):
    """SWAN forcing data interface.

    Examples
    --------

    .. ipython:: python
        :okwarning:

        from rompy.swan.interface import ForcingData

    """
    model_type: Literal["forcing", "FORCING"] = Field(
        default="forcing", description="Model type discriminator"
    )
    bottom: Optional[SwanDataGrid] = Field(default=None, description="Bathymetry data")
    input: list[SwanDataGrid] = Field(default=[], description="Input grid data")
    boundary: Optional[DataBoundary] = Field(default=None, description="Boundary data")

    def get(self, grid: SwanGrid, period: TimeRange, staging_dir: Path):
        cmds = []
        # Bottom grid
        if self.bottom is not None:
            self.bottom._filter_grid(grid)
            self.bottom._filter_time(period)
            cmds.append(self.bottom.get(staging_dir, grid))
        # Input grids
        for input in self.input:
            input._filter_grid(grid)
            input._filter_time(period)
            cmds.append(input.get(staging_dir, grid))
        # Boundary data
        if self.boundary is not None:
            self.boundary._filter_grid(grid)
            self.boundary._filter_time(period)
            cmds.append(self.boundary.get(staging_dir, grid))
        return "\n".join(cmds)

    def render(self, *args, **kwargs):
        """Make this class consistent with the components API."""
        return self.get(*args, **kwargs)

    def __str__(self):
        ret = ""
        if self.bottom:
            ret += self.bottom.source
        for input in self.input:
            ret += input.source
        if self.boundary:
            ret += self.boundary.source
        return ret


class TimeInterface(RompyBaseModel):
    """Base interface to pass time to group components.

    This class is used to set consistent time parameters in a group component by
    redefining existing `times` component attribute based on the `period` field.

    """

    model_type: Literal["interface", "INTERFACE"] = Field(
        default="interface", description="Model type discriminator"
    )
    group: Any = Field(description="Group component to set times to")
    period: TimeRange = Field(description="Time period to write the output over")


class OutputInterface(TimeInterface):
    """Output group component with consistent times."""

    model_type: Literal["outputinterface", "OUTPUTINTERFACE"] = Field(
        default="outputinterface", description="Model type discriminator"
    )

    @model_validator(mode="after")
    def time_interface(self) -> "OutputInterface":
        """Set the time parameter for all WRITE components."""
        for component in self.group._write_fields:
            obj = getattr(self.group, component)
            if obj is not None:
                times = obj.times or TimeRangeOpen()
                obj.times = self._timerange(times.tfmt, times.dfmt, obj.suffix)

    def _timerange(self, tfmt: int, dfmt: str, suffix: str) -> TimeRangeOpen:
        """Convert generic TimeRange into the Swan TimeRangeOpen subcomponent."""
        return TimeRangeOpen(
            tbeg=self.period.start,
            delt=self.period.interval,
            tfmt=tfmt,
            dfmt=dfmt,
            suffix=suffix,
        )


class LockupInterface(TimeInterface):
    """Lockup group component with consistent times."""

    model_type: Literal["lockupinterface", "LOCKUPINTERFACE"] = Field(
        default="lockupinterface", description="Model type discriminator"
    )

    def _nonstationary(self, tfmt: str, dfmt: str) -> NONSTATIONARY:
        return NONSTATIONARY(
            tbeg=self.period.start,
            tend=self.period.end,
            delt=self.period.interval,
            tfmt=tfmt,
            dfmt=dfmt,
            suffix="c",
        )

    def _stationary(self, tfmt: str) -> STATIONARY:
        return STATIONARY(time=self.period.start, tfmt=tfmt)

    @model_validator(mode="after")
    def time_interface(self) -> "LockupInterface":
        """Set the time parameter for COMPUTE components."""
        times = self.group.compute.times or NONSTATIONARY()
        if isinstance(times, NONSTATIONARY):
            times = self._nonstationary(times.tfmt, times.dfmt)
        elif isinstance(times, STATIONARY):
            times = self._stationary(times.tfmt)
        else:
            raise ValueError(f"Unknown time type {type(times)}")
        self.group.compute.times = times
