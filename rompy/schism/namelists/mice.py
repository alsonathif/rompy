from pydantic import Field
from rompy.schism.namelists.basemodel import NamelistBaseModel

class Mice_in(NamelistBaseModel):
    ice_tests: int = Field(0)
    ihot_mice: int = Field(1)
    ice_advection: int = Field(6)
    ice_therm_on: int = Field(1)
    ievp: int = Field(2)
    ice_cutoff: float = Field(0.001)
    evp_rheol_steps: int = Field(500)
    mevp_rheol_steps: int = Field(500)
    delta_min: str = Field('1.0e-11')
    theta_io: float = Field(0.0)
    mevp_alpha1: float = Field(200.0)
    mevp_alpha2: float = Field(200.0)
    pstar: float = Field(27500.0)
    ellipse: float = Field(2.0)
    c_pressure: float = Field(20.0)
    niter_fct: int = Field(3)
    ice_gamma_fct: float = Field(0.25)
    h_ml0: float = Field(0.1)
    salt_ice: float = Field(5.0)
    salt_water: float = Field(34.0)

class Mice(NamelistBaseModel):
    """
        
    This file was auto generated from a schism namelist file on 2023-11-15.
    The full contents of the namelist file are shown below providing
    associated documentation for the objects:
    
    !parameter inputs via namelist convention.
    !(1)Use '' for chars; (2) integer values are fine for real vars/arrays;
    !(3) if multiple entries for a parameter are found, the last one wins - please avoid this
    !(4) array inputs follow column major and can spill to multiple lines
    !(5) space allowed before/after '='
    !(6) Not all required variables need to be present, but all that are present must belong to the list below. Best to list _all_ parameters.
    
    &mice_in
      ice_tests = 0  !box test flag
      ihot_mice = 1  !0: cold start 1: restart 2: hotstart_from_HYCOM
      ice_advection = 6 !advection on/off 3: upwind 4: center-difference 5: tvd 6: tvd-up 7: TVD_Casulli
      ice_therm_on = 1 !ice thermodynamics on/off flag
      ievp=2 !1: EVP; 2: mEVP
      ice_cutoff=0.001 !cut-off thickness [m] or fraction for ice. No ice velocity if *<=ice_cuttoff
      evp_rheol_steps=500  ! the number of sybcycling steps in EVP
      mevp_rheol_steps=500  ! the number of iterations in mEVP
      delta_min=1.0e-11     ! (1/s) Limit for minimum divergence (Hibler, Hunke
                           ! normally use 2.0e-9, which does much stronger
                           ! limiting; valid for both VP and EVP
      theta_io=0.       ! ice/ocean rotation angle. [degr]
      mevp_alpha1=200. !const used in mEVP (constitutive eq)
      mevp_alpha2=200. !const used in mEVP for momentum eq
      pstar=27500. ![N/m^2]
      ellipse=2.  !ellipticity
      c_pressure=20.0  !C [-]
      !FCT
      niter_fct=3 !# of iterartions in higher-order solve
      ice_gamma_fct=0.25 ! smoothing parameter
    
      !Thermodynamics
      h_ml0=0.1 !ocean mixed layer depth [m]
      salt_ice=5. !salinity for ice [PSU] (>=0)
      salt_water=34. !salinity for water [PSU] (>=0)
    /
    
    """
    mice_in: Mice_in = Mice_in()
