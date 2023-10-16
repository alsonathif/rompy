import pytest
from pathlib import Path
from datetime import datetime

from utils import compare_files

from rompy.model import ModelRun
from rompy.core import BaseConfig, TimeRange

here = Path(__file__).parent


@pytest.mark.skip(reason="frequency removed from ModelRun so this template breaks")
def test_swanbasic(tmpdir):
    """Test the swantemplate function."""
    time = TimeRange(
        start=datetime(2020, 2, 21, 4), end=datetime(2020, 2, 24, 4), interval="15M"
    )
    runtime = ModelRun(
        run_id="test_swantemplatebasic",
        output_dir=str(tmpdir),
        config=BaseConfig(
            friction_coefficient=0.1,
            model_type="base",
            template=str(here.parent / "rompy/templates/swanbasic"),
        ),
    )
    runtime.generate()
    compare_files(
        here / "simulations" / "test_swan_ref" / "INPUT_NEW",
        tmpdir / runtime.run_id / "INPUT",
    )
