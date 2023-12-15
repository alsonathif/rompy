from pathlib import Path

import pytest

from rompy.core import DataBlob
from rompy.core.grid import BaseGrid
from rompy.schism import SCHISMGrid2D, SCHISMGrid3D


def test_SCHISMGrid2D(tmpdir):
    hgrid = DataBlob(source="test_data/hgrid.gr3")
    drag = DataBlob(source="test_data/drag.gr3")
    rough = DataBlob(source="test_data/rough.gr3")
    manning = DataBlob(source="test_data/manning.gr3")
    hgridll = DataBlob(source="test_data/hgrid.ll")
    diffmin = DataBlob(source="test_data/diffmin.gr3")
    diffmax = DataBlob(source="test_data/diffmax.gr3")
    hgrid_WWM = DataBlob(source="test_data/hgrid_WWM.gr3")
    wwmbnd = DataBlob(source="test_data/wwmbnd.gr3")

    grid = SCHISMGrid2D(
        hgrid=hgrid,
        # drag=drag,
        # rough=rough,
        # manning=1.2,
        # hgridll=hgridll,
        # diffmin=diffmin,
        # diffmax=diffmax,
        # hgrid_WWM=hgrid_WWM,
        # wwmbnd=wwmbnd,
    )

    assert grid.grid_type == "2D"
    # # assert grid.drag == drag
    # # assert grid.rough == rough
    # assert grid.manning == manning
    # assert grid.hgridll == hgridll
    # assert grid.diffmin == diffmin
    # assert grid.diffmax == diffmax
    # assert grid.hgrid_WWM == hgrid_WWM
    # assert grid.wwmbnd == wwmbnd

    assert grid.validate_rough_drag_manning(grid) == grid
    # assert that the gr3 file for each of the above is in the staging dir
    staging_dir = Path(tmpdir)
    ret = grid.get(staging_dir)

    assert staging_dir.joinpath("hgrid.gr3").exists()
    assert staging_dir.joinpath("hgrid.ll").exists()
    assert staging_dir.joinpath("diffmin.gr3").exists()
    assert staging_dir.joinpath("diffmax.gr3").exists()
    assert staging_dir.joinpath("tvprop.in").exists()
