import logging
from datetime import datetime
from pathlib import Path
from time import time

import xarray as xr
from matplotlib.transforms import Bbox
from pyschism.forcing.hycom.hycom2schism import DownloadHycom
from pyschism.mesh.hgrid import Hgrid

"""
Download hycom data for Fortran scripts.
Default is to download data for generating initial condition (use hgrid 
    as parameter to cover the whole domain).
Optionally, download data for generating th.nc (bnd=True) and nu.nc (nudge=True) 
    (use bbox as parameter to cut small domain).
"""
logging.basicConfig(
    format="[%(asctime)s] %(name)s %(levelname)s: %(message)s",
    force=True,
)
logger = logging.getLogger("pyschism")
logger.setLevel(logging.INFO)


def download_hycom(dest=Path("./"), hgrid=Path("./hgrid.gr3")):
    hgrid = Hgrid.open(hgrid, crs="epsg:4326")
    date = datetime(2023, 1, 1)
    hycom = DownloadHycom(hgrid=hgrid)
    t0 = time()
    hycom.fetch_data(date, rnday=2, bnd=False, nudge=False, sub_sample=5, outdir="./")
    print(f"It took {(time()-t0)/60} mins to download")

    files = Path("./").glob("hycom_*.nc")
    logging.info("Concatenating files...")
    xr.open_mfdataset(files, concat_dim="time", combine="nested")["surf_el"].to_netcdf(
        dest / "hycom.nc"
    )
    for file in files:
        file.unlink()
