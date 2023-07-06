"""Test startup components."""
import pytest
from pydantic import ValidationError

from rompy.swan.components.physics import (
    GEN1,
    GEN2,
    GEN3,
    DCTA,
    LTA,
    SPB,
    VEGETATION,
    MUD,
    SICE,
    R19,
    D15,
    M18,
    R21B,
    TURBULENCE,
    BRAGG,
    BRAGGFT,
    BRAGGFILE,
)


# =====================================================================================
# GEN
# =====================================================================================
def test_gen1_default():
    phys = GEN1()
    assert phys.render() == "GEN1"


def test_gen1_set_all():
    phys = GEN1(
        cf10=188,
        cf20=0.59,
        cf30=0.12,
        cf40=250,
        edmlpm=0.0036,
        cdrag=0.0012,
        umin=1,
        cfpm=0.13,
    )
    assert phys.render() == (
        "GEN1 cf10=188.0 cf20=0.59 cf30=0.12 cf40=250.0 edmlpm=0.0036 cdrag=0.0012 "
        "umin=1.0 cfpm=0.13"
    )


def test_gen2_default():
    phys = GEN2()
    assert phys.render() == "GEN2"


def test_gen2_set_all():
    phys = GEN2(
        cf10=188,
        cf20=0.59,
        cf30=0.12,
        cf40=250,
        cf50=0.0023,
        cf60=-0.223,
        edmlpm=0.0036,
        cdrag=0.0012,
        umin=1,
        cfpm=0.13,
    )
    assert phys.render() == (
        "GEN2 cf10=188.0 cf20=0.59 cf30=0.12 cf40=250.0 cf50=0.0023 cf60=-0.223 "
        "edmlpm=0.0036 cdrag=0.0012 umin=1.0 cfpm=0.13"
    )


def test_gen3_default():
    phys = GEN3()
    assert phys.render() == f"GEN3 {phys.source_terms.render()}"


# =====================================================================================
# TRIADS
# =====================================================================================
def test_triad_dcta():
    phys = DCTA()
    assert phys.render() == "TRIAD DCTA COLL BIPHASE ELDEBERKY"
    phys = DCTA(
        biphase=dict(model_type="dewit", lpar=0.0), trfac=4.4, p=1.3, noncolinear=True
    )
    assert phys.render() == "TRIAD DCTA trfac=4.4 p=1.3 NONC BIPHASE DEWIT lpar=0.0"


def test_triad_lta():
    phys = LTA()
    assert phys.render() == "TRIAD LTA BIPHASE ELDEBERKY"
    phys = LTA(biphase=dict(model_type="dewit", lpar=0.0), trfac=0.8, cutfr=2.5)
    assert phys.render() == "TRIAD LTA trfac=0.8 cutfr=2.5 BIPHASE DEWIT lpar=0.0"


def test_triad_spb():
    phys = SPB()
    assert phys.render() == "TRIAD SPB BIPHASE ELDEBERKY"
    phys = SPB(biphase=dict(model_type="dewit", lpar=0.0), trfac=0.9, a=0.95, b=0.0)
    assert phys.render() == "TRIAD SPB trfac=0.9 a=0.95 b=0.0 BIPHASE DEWIT lpar=0.0"


# =====================================================================================
# VEGETATION
# =====================================================================================
def test_vegetation():
    vegetation = VEGETATION(
        height=1.0,
        diamtr=0.1,
        drag=0.1,
    )
    assert vegetation.render() == (
        "VEGETATION iveg=1 height=1.0 diamtr=0.1 nstems=1 drag=0.1"
    )


def test_vegetation_number_of_layers():
    layers = 3
    v = VEGETATION(
        height=[1.0] * layers,
        diamtr=[0.1] * layers,
        drag=[0.1] * layers,
        nstems=[2] * layers,
    )
    assert v.render().count("height") == layers


def test_vegetation_number_of_layers_mismatch():
    with pytest.raises(ValidationError):
        VEGETATION(
            height=1.0,
            diamtr=[0.1, 0.1],
            drag=[0.1],
            nstems=[2, 2, 2],
        )


# =====================================================================================
# MUD
# =====================================================================================
def test_mud_default():
    phys = MUD()
    assert phys.render() == "MUD"


def test_mud_arguments():
    phys = MUD(layer=2.0, rhom=1300, viscm=0.0076)
    assert phys.render() == "MUD layer=2.0 rhom=1300.0 viscm=0.0076"


# =====================================================================================
# SICE
# =====================================================================================
def test_sice_default():
    sice = SICE()
    assert sice.render() == "SICE"
    sice = SICE(aice=0.5)
    assert sice.render() == "SICE aice=0.5"
    with pytest.raises(ValidationError):
        SICE(aice=1.1)


def test_sice_r19():
    sice = R19()
    assert sice.render() == "SICE R19"
    sice = R19(
        aice=0.5,
        c0=0.0,
        c1=0.0,
        c2=1.06e-3,
        c3=0.0,
        c4=2.3e-2,
        c5=0.0,
        c6=0.0,
    )
    assert sice.render() == (
        "SICE aice=0.5 R19 c0=0.0 c1=0.0 c2=0.00106 c3=0.0 c4=0.023 c5=0.0 c6=0.0"
    )


def test_sice_d15():
    sice = D15()
    assert sice.render() == "SICE D15"
    sice = D15(aice=0.5, chf=0.1)
    assert sice.render() == "SICE aice=0.5 D15 chf=0.1"


def test_sice_m18():
    sice = M18()
    assert sice.render() == "SICE M18"
    sice = M18(aice=0.5, chf=0.059)
    assert sice.render() == "SICE aice=0.5 M18 chf=0.059"


def test_sice_r21b():
    sice = R21B()
    assert sice.render() == "SICE R21B"
    sice = R21B(aice=0.5, chf=2.9, npf=4.5)
    assert sice.render() == "SICE aice=0.5 R21B chf=2.9 npf=4.5"


# =====================================================================================
# TURBULENCE
# =====================================================================================
def test_turbulence_current():
    turb = TURBULENCE(tbcur=0.004)
    assert turb.render() == "TURBULENCE CURRENT tbcur=0.004"


def test_turbulence_no_current():
    turb = TURBULENCE(ctb=0.01, current=False)
    assert turb.render() == "TURBULENCE ctb=0.01"


def test_turbulence_tbcur_only_with_current():
    with pytest.raises(ValidationError):
        TURBULENCE(tbcur=0.004, current=False)


# =====================================================================================
# BRAGG
# =====================================================================================
def test_bragg_default():
    bragg = BRAGG()
    assert bragg.render() == "BRAGG"
    bragg = BRAGG(ibrag=1, nreg=200, cutoff=5.0)
    assert bragg.render() == "BRAGG ibrag=1 nreg=200 cutoff=5.0"


def test_bragg_ft():
    bragg = BRAGGFT()
    assert bragg.render() == "BRAGG FT"
    bragg = BRAGGFT(ibrag=1, nreg=200, cutoff=5.0)
    assert bragg.render() == "BRAGG ibrag=1 nreg=200 cutoff=5.0 FT"


def test_bragg_file():
    bragg = BRAGGFILE(fname="bragg.txt", mkx=200, dkx=0.1)
    assert bragg.render() == "BRAGG FILE fname='bragg.txt' mkx=200 dkx=0.1"
    bragg = BRAGGFILE(fname="bragg.txt", idla=1, mkx=200, mky=200, dkx=0.1, dky=0.1)
    assert bragg.render() == (
        "BRAGG FILE fname='bragg.txt' idla=1 mkx=200 mky=200 dkx=0.1 dky=0.1"
    )


def test_bragg_file_idla():
    with pytest.raises(ValidationError):
        BRAGGFILE(fname="bragg.txt", idla=7, mkx=200, mky=200, dkx=0.1, dky=0.1)
