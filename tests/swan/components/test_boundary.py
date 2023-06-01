"""Test SWAN boundary components."""
import pytest

from rompy.swan.components.boundary import BOUNDSPEC, BOUNDNEST1, BOUNDNEST2
from rompy.swan.subcomponents.shape import SHAPESPEC, JONSWAP
from rompy.swan.subcomponents.boundary import SIDE, CONSTANTPAR


def test_boundspec():
    bnd = BOUNDSPEC(
        shapespec=SHAPESPEC(
            shape=JONSWAP(
                gamma=3.3
            ),
            per_type="peak",
            dspr_type="power",
        ),
        location=SIDE(
            side="west",
        ),
        data=CONSTANTPAR(
            hs=1.0,
            per=10.0,
            dir=0.0,
            dd=10.0,
        ),
    )
    assert "BOUND SHAPESPEC JONSWAP gamma=3.3 PEAK DSPR POWER" in bnd.render()
    assert "BOUNDSPEC SIDE WEST CCW CONSTANT PAR hs=1.0" in bnd.render()


def test_boundnest1():
    bnd = BOUNDNEST1(fname="boundary_swan.txt")
    assert bnd.render() == "BOUNDNEST1 NEST fname='boundary_swan.txt' CLOSED"
    bnd = BOUNDNEST1(fname="boundary_swan.txt", rectangle="open")
    assert bnd.render() == "BOUNDNEST1 NEST fname='boundary_swan.txt' OPEN"


def test_boundnest2_format():
    bnd = BOUNDNEST2(fname="boundary_wam.txt", format="free")
    assert bnd.render() == "BOUNDNEST2 WAMNEST fname='boundary_wam.txt' FREE lwdate=12"
    for fmt in ["cray", "wkstat"]:
        bnd = BOUNDNEST2(fname="wam.txt", format=fmt)
        assert bnd.render().endswith(f"UNFORMATTED {fmt.upper()} lwdate=12")
    with pytest.raises(ValueError):
        BOUNDNEST2(fname="boundary_wam.txt", format="unknown")


def test_boundnest2_xygc():
    bnd = BOUNDNEST2(fname="boundary_wam.txt", format="free", xgc=0.0, ygc=0.0)
    assert bnd.render() == "BOUNDNEST2 WAMNEST fname='boundary_wam.txt' FREE xgc=0.0 ygc=0.0 lwdate=12"


def test_boundnest2_lwdate():
    for lwdate in [10, 12, 14]:
        bnd = BOUNDNEST2(fname="boundary_wam.txt", format="free", lwdate=lwdate)
        assert bnd.render() == f"BOUNDNEST2 WAMNEST fname='boundary_wam.txt' FREE lwdate={lwdate}"
    with pytest.raises(ValueError):
        BOUNDNEST2(fname="boundary_wam.txt", format="wkstat", lwdate=11)

