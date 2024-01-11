import os
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
import xarray as xr

from rompy.core import BaseGrid, DataBlob, DataGrid, TimeRange
from rompy.core.data import (SourceDatamesh, SourceDataset, SourceFile,
                             SourceIntake)
from rompy.schism import SCHISMGrid
from rompy.schism.data import (SCHISMDataBoundary, SCHISMDataOcean,
                               SCHISMDataSflux, SCHISMDataTides, SfluxAir,
                               TidalDataset)
from rompy.schism.namelists import Sflux_Inputs

HERE = Path(__file__).parent
DATAMESH_TOKEN = os.environ.get("DATAMESH_TOKEN")
import logging

logging.basicConfig(level=logging.INFO)


@pytest.fixture
def grid2d():
    return SCHISMGrid(hgrid=DataBlob(source=HERE / "test_data/hgrid.gr3"), drag=1)


@pytest.fixture
def grid_atmos_source():
    return SourceIntake(
        dataset_id="era5",
        catalog_uri=HERE / ".." / "data" / "catalog.yaml",
    )


@pytest.fixture
def hycom_bnd():
    hycomdata = HERE / "test_data" / "hycom.nc"
    if not hycomdata.exists():
        from utils import download_hycom

        logging.info("Hycom test data not found, downloading...")
        logging.info("This may take a while...only has to be done once.")
        download_hycom(dest=HERE / "test_data", hgrid=HERE / "test_data" / "hgrid.gr3")
    return SCHISMDataBoundary(
        id="hycom",
        source=SourceFile(
            uri=HERE / "test_data" / "hycom.nc",
        ),
        variable="surf_el",
        coords={"t": "time", "y": "ylat", "x": "xlon", "z": "depth"},
    )


def test_atmos(tmp_path, grid_atmos_source):
    data = SCHISMDataSflux(
        air_1=SfluxAir(
            id="air_1",
            source=grid_atmos_source,
            filter={
                "sort": {"coords": ["latitude"]},
                "crop": {
                    "time": slice("2023-01-01", "2023-01-02"),
                    "latitude": slice(0, 20),
                    "longitude": slice(0, 20),
                },
            },
        )
    )
    data.get(tmp_path)


def test_oceandataboundary(tmp_path, grid2d, hycom_bnd):
    hycom_bnd.get(tmp_path, grid2d)


def test_oceandata(tmp_path, grid2d, hycom_bnd):
    oceandata = SCHISMDataOcean(elev2D=hycom_bnd)
    oceandata.get(tmp_path, grid2d)


def test_tidal_boundary(tmp_path, grid2d):
    tides = SCHISMDataTides(
        tidal_data=TidalDataset(
            elevations=HERE / "test_data" / "tpxo9-test" / "h_m2s2n2.nc",
            velocities=HERE / "test_data" / "tpxo9-test" / "u_m2s2n2.nc",
        ),
        constituents=["M2", "S2", "N2"],
    )
    tides.get(
        destdir=tmp_path,
        grid=grid2d,
        time=TimeRange(start="2023-01-01", end="2023-01-02", dt=3600),
    )
