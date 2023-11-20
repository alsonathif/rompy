from pydantic import Field
from rompy.schism.namelists.basemodel import NamelistBaseModel

class CORE(NamelistBaseModel):
    ipre: int = Field(0)
    ibc: int = Field(0)
    ibtp: int = Field(1)
    rnday: int = Field(30)
    dt: float = Field(100.0)
    msc2: int = Field(24)
    mdc2: int = Field(30)
    ntracer_gen: int = Field(2)
    ntracer_age: int = Field(4)
    sed_class: int = Field(5)
    eco_class: int = Field(27)
    nspool: int = Field(36)
    ihfskip: int = Field(864)

class OPT(NamelistBaseModel):
    ipre2: int = Field(0)
    itransport_only: int = Field(0)
    iloadtide: int = Field(0)
    loadtide_coef: float = Field(0.1)
    start_year: int = Field(2000)
    start_month: int = Field(1)
    start_day: int = Field(1)
    start_hour: int = Field(0)
    utc_start: int = Field(8)
    ics: int = Field(1)
    ihot: int = Field(0)
    ieos_type: int = Field(0)
    ieos_pres: int = Field(0)
    eos_a: float = Field(-0.1)
    eos_b: float = Field(1001.0)
    dramp: float = Field(1.0)
    drampbc: float = Field(0.0)
    iupwind_mom: int = Field(0)
    indvel: int = Field(0)
    ihorcon: int = Field(0)
    hvis_coef0: float = Field(0.025)
    ishapiro: int = Field(1)
    niter_shap: int = Field(1)
    shapiro0: float = Field(0.5)
    thetai: float = Field(0.6)
    icou_elfe_wwm: int = Field(0)
    nstep_wwm: int = Field(1)
    iwbl: int = Field(0)
    hmin_radstress: float = Field(1.0)
    drampwafo: float = Field(0.0)
    turbinj: float = Field(0.15)
    turbinjds: float = Field(1.0)
    alphaw: float = Field(0.5)
    fwvor_advxy_stokes: int = Field(1)
    fwvor_advz_stokes: int = Field(1)
    fwvor_gradpress: int = Field(1)
    fwvor_breaking: int = Field(1)
    fwvor_streaming: int = Field(1)
    fwvor_wveg: int = Field(0)
    fwvor_wveg_NL: int = Field(0)
    cur_wwm: int = Field(0)
    wafo_obcramp: int = Field(0)
    imm: int = Field(0)
    ibdef: int = Field(10)
    slam0: int = Field(-124)
    sfea0: int = Field(45)
    iunder_deep: int = Field(0)
    h1_bcc: float = Field(50.0)
    h2_bcc: float = Field(100.0)
    hw_depth: str = Field('1.e6')
    hw_ratio: float = Field(0.5)
    ihydraulics: int = Field(0)
    if_source: int = Field(0)
    dramp_ss: int = Field(2)
    meth_sink: int = Field(1)
    lev_tr_source(1): int = Field(-9)
    lev_tr_source(2): int = Field(-9)
    lev_tr_source(3): int = Field(-9)
    lev_tr_source(4): int = Field(-9)
    lev_tr_source(5): int = Field(-9)
    lev_tr_source(6): int = Field(-9)
    lev_tr_source(7): int = Field(-9)
    lev_tr_source(8): int = Field(-9)
    lev_tr_source(9): int = Field(-9)
    lev_tr_source(10): int = Field(-9)
    lev_tr_source(11): int = Field(-9)
    lev_tr_source(12): int = Field(-9)
    level_age: list = Field([9, -999])
    ihdif: int = Field(0)
    nchi: int = Field(0)
    dzb_min: float = Field(0.5)
    hmin_man: float = Field(1.0)
    ncor: int = Field(0)
    rlatitude: int = Field(46)
    coricoef: int = Field(0)
    ic_elev: int = Field(0)
    nramp_elev: int = Field(0)
    inv_atm_bnd: int = Field(0)
    prmsl_ref: float = Field(101325.0)
    flag_ic(1): int = Field(1)
    flag_ic(2): int = Field(1)
    flag_ic(3): int = Field(1)
    flag_ic(5): int = Field(1)
    flag_ic(6): int = Field(1)
    flag_ic(7): int = Field(1)
    flag_ic(8): int = Field(1)
    flag_ic(9): int = Field(1)
    flag_ic(10): int = Field(1)
    flag_ic(11): int = Field(1)
    flag_ic(12): int = Field(0)
    gen_wsett: int = Field(0)
    ibcc_mean: int = Field(0)
    rmaxvel: float = Field(5.0)
    velmin_btrack: str = Field('1.e-4')
    btrack_nudge: str = Field('9.013e-3')
    ihhat: int = Field(1)
    inunfl: int = Field(0)
    h0: float = Field(0.01)
    shorewafo: int = Field(0)
    moitn0: int = Field(50)
    mxitn0: int = Field(1500)
    rtol0: str = Field('1.e-12')
    nadv: int = Field(1)
    dtb_max: float = Field(30.0)
    dtb_min: float = Field(10.0)
    inter_mom: int = Field(0)
    kr_co: int = Field(1)
    itr_met: int = Field(3)
    h_tvd: float = Field(5.0)
    eps1_tvd_imp: str = Field('1.e-4')
    eps2_tvd_imp: str = Field('1.e-14')
    ielm_transport: int = Field(0)
    max_subcyc: int = Field(10)
    ip_weno: int = Field(2)
    courant_weno: float = Field(0.5)
    nquad: int = Field(2)
    ntd_weno: int = Field(1)
    epsilon1: str = Field('1.e-15')
    epsilon2: str = Field('1.e-10')
    i_prtnftl_weno: int = Field(0)
    epsilon3: str = Field('1.e-25')
    ielad_weno: int = Field(0)
    small_elad: str = Field('1.e-4')
    nws: int = Field(0)
    wtiminc: float = Field(150.0)
    drampwind: float = Field(1.0)
    iwindoff: int = Field(0)
    iwind_form: int = Field(1)
    model_type_pahm: int = Field(10)
    ihconsv: int = Field(0)
    isconsv: int = Field(0)
    i_hmin_airsea_ex: int = Field(2)
    hmin_airsea_ex: float = Field(0.2)
    i_hmin_salt_ex: int = Field(2)
    hmin_salt_ex: float = Field(0.2)
    iprecip_off_bnd: int = Field(0)
    itur: int = Field(3)
    dfv0: str = Field('1.e-2')
    dfh0: str = Field('1.e-4')
    mid: str = Field("'KL'")
    stab: str = Field("'KC'")
    xlsc0: float = Field(0.1)
    inu_elev: int = Field(0)
    inu_uv: int = Field(0)
    inu_tr(1): int = Field(0)
    inu_tr(2): int = Field(0)
    inu_tr(3): int = Field(0)
    inu_tr(4): int = Field(0)
    inu_tr(5): int = Field(0)
    inu_tr(6): int = Field(0)
    inu_tr(7): int = Field(0)
    inu_tr(8): int = Field(0)
    inu_tr(9): int = Field(0)
    inu_tr(10): int = Field(0)
    inu_tr(11): int = Field(0)
    inu_tr(12): int = Field(0)
    nu_sum_mult: int = Field(1)

class VERTICAL(NamelistBaseModel):
    vnh1: int = Field(400)
    vnf1: float = Field(0.0)
    vnh2: int = Field(500)
    vnf2: float = Field(0.0)
    step_nu_tr: float = Field(86400.0)
    h_bcc1: float = Field(100.0)
    s1_mxnbt: float = Field(0.5)
    s2_mxnbt: float = Field(3.5)
    iharind: int = Field(0)
    iflux: int = Field(0)
    izonal5: int = Field(0)
    ibtrack_test: int = Field(0)
    irouse_test: int = Field(0)
    flag_fib: int = Field(1)
    slr_rate: float = Field(120.0)
    isav: int = Field(0)
    nstep_ice: int = Field(1)
    rearth_pole: float = Field(6378206.4)
    rearth_eq: float = Field(6378206.4)
    shw: str = Field('4184.d0')
    rho0: str = Field('1000.d0')
    vclose_surf_frac: float = Field(1.0)
    iadjust_mass_consv0(1): int = Field(0)
    iadjust_mass_consv0(2): int = Field(0)
    iadjust_mass_consv0(3): int = Field(0)
    iadjust_mass_consv0(4): int = Field(0)
    iadjust_mass_consv0(5): int = Field(0)
    iadjust_mass_consv0(6): int = Field(0)
    iadjust_mass_consv0(7): int = Field(0)
    iadjust_mass_consv0(8): int = Field(0)
    iadjust_mass_consv0(9): int = Field(0)
    iadjust_mass_consv0(10): int = Field(0)
    iadjust_mass_consv0(11): int = Field(0)
    iadjust_mass_consv0(12): int = Field(0)
    h_massconsv: float = Field(2.0)
    rinflation_icm: str = Field('1.e-3')

class SCHOUT(NamelistBaseModel):
    nc_out: int = Field(1)
    iof_ugrid: int = Field(0)
    nhot: int = Field(0)
    nhot_write: int = Field(8640)
    iout_sta: int = Field(0)
    nspool_sta: int = Field(10)
    iof_hydro(1): int = Field(1)
    iof_hydro(2): int = Field(0)
    iof_hydro(3): int = Field(0)
    iof_hydro(4): int = Field(0)
    iof_hydro(5): int = Field(0)
    iof_hydro(6): int = Field(0)
    iof_hydro(7): int = Field(0)
    iof_hydro(8): int = Field(0)
    iof_hydro(9): int = Field(0)
    iof_hydro(10): int = Field(0)
    iof_hydro(11): int = Field(0)
    iof_hydro(12): int = Field(0)
    iof_hydro(13): int = Field(0)
    iof_hydro(14): int = Field(0)
    iof_hydro(15): int = Field(0)
    iof_hydro(16): int = Field(0)
    iof_hydro(17): int = Field(0)
    iof_hydro(18): int = Field(0)
    iof_hydro(19): int = Field(0)
    iof_hydro(20): int = Field(0)
    iof_hydro(21): int = Field(0)
    iof_hydro(22): int = Field(0)
    iof_hydro(23): int = Field(0)
    iof_hydro(24): int = Field(0)
    iof_hydro(26): int = Field(1)
    iof_hydro(27): int = Field(0)
    iof_hydro(28): int = Field(0)
    iof_hydro(29): int = Field(0)
    iof_hydro(30): int = Field(0)
    iof_hydro(31): int = Field(0)

class PARAM(NamelistBaseModel):
    """
        
    This file was auto generated from a schism namelist file on 2023-11-20.
    The full contents of the namelist file are shown below providing
    associated documentation for the objects:
    
    !parameter inputs via namelist convention.
    !(1) Use ' ' (single quotes) for chars;
    !(2) integer values are fine for real vars/arrays;
    !(3) if multiple entries for a parameter are found, the last one wins - please avoid this
    !(4) array inputs follow column major (like FORTRAN) and can spill to multiple lines. 
    !    Values can be separated by commas or spaces.
    !(5) space allowed before/after '='
    
    &CORE
    !+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ! Core (mandatory) parameters; no defaults
    !+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ! Pre-processing option. Useful for checking grid errors etc. Need to use 1 
    ! core only for compute (plus necessary scribe cores). Under scribe I/O, the 
    ! code (the scribe part) will hang but the outputs will be there. Just kill 
    ! the job.
      ipre = 0 !Pre-processor flag (1: on; 0: off)
    
    ! Baroclinic/barotropic option. If ibc=0 (baroclinic model), ibtp is not used.
      ibc = 0 !Baroclinic option
      ibtp = 1 
    
      rnday = 30 !total run time in days
      dt = 100. !Time step in sec
    
    ! Grid for WWM (USE_WWM)
      msc2 = 24     !same as msc in .nml ... for consitency check between SCHISM and WWM
      mdc2 = 30     !same as mdc in .nml
    
    ! Define # of tracers in tracer modules (if enabled)
      ntracer_gen = 2 !user defined module (USE_GEN)
      ntracer_age = 4 !age calculation (USE_AGE). Must be =2*N where N is # of age tracers
      sed_class = 5 !SED3D (USE_SED)
      eco_class = 27 !EcoSim (USE_ECO): must be between [25,60]
    
    ! Global output controls
      nspool = 36 !output step spool
      ihfskip = 864 !stack spool; every ihfskip steps will be put into 1_*, 2_*, etc...
    /
    
    &OPT
    !+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ! Optional parameters. The values shown below are default unless otherwise noted
    !+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    !-----------------------------------------------------------------------
    ! Optional offline partitioning using NO_PARMETIS. If on, need partition.prop (like global_to_local.prop).
    !-----------------------------------------------------------------------
    
    
    !-----------------------------------------------------------------------
    ! 2nd pre-proc flag. If ipre2/=0, code will output some diagnotic outputs and stop.
    ! These outputs are: drag coefficients (Cdp)
    !-----------------------------------------------------------------------
      ipre2 = 0
    
    !-----------------------------------------------------------------------
    ! Option to only solve tracer transport (and bypass most b-tropic solver)
    ! Usage: turn the flag on ('1' or '2') and turn on your tracer modules and make sure
    ! (1) your inputs are consistent with the original hydro-only run (with additional tracers
    ! of course); (2) hydro-only run results are in hydro_out/schout*.nc, which must
    ! have 'hvel_side' (not normal hvel), 'elev', 'diffusivity', 'temp_elem', 'salt_elem' (for
    ! new scribe outputs, use corresponding files/var names); (3) dt above is 
    ! multiple of _output_ step used in the original hydro-only run 
    ! (as found in in hydro_out/schout*.nc); e.g. dt = 1 hour. (4). When itransport_only=2,
    ! additional variables ('totalSuspendedLoad','sedBedStress') are needed.
    ! Hotstart should work also, but you'd probably not use an aggressively large dt especially
    ! when air-sea exchange is involved.
    !-----------------------------------------------------------------------
      itransport_only = 0
    
    !-----------------------------------------------------------------------
    ! Option to add self-attracting and loading tide (SAL) into tidal potential 
    ! (usually for basin-scale applications). 
    ! If iloadtide=0, no SAL.
    ! If iloadtide=1, needs inputs: loadtide_[FREQ].gr3, 
    ! where [FREQ] are freq names (shared with tidal potential, in upper cases) 
    ! and the _two_ 'depths' inside are amplitude (m) and phases (degrees behind GMT), 
    ! interpolated from global tide model (e.g. FES2014). In this option, SAL is 
    ! lumped into tidal potential so it shares some parameters with tidal potential 
    ! in bctides.in (cut-off depth, frequencies).
    ! If iloadtide=2 or 3, use a simple scaling for gravity approach (in this option,
    ! SAL is applied everywhere and does not share parameters with tidal potential).
    ! For iloadtide=2, a const scaling (1-loadtide_coef) is used; for iloadtide=3, the scaling is 
    ! dependent on depth (Stepanov & Hughes 2004) with max of loadtide_coef.
    !-----------------------------------------------------------------------
      iloadtide = 0
      loadtide_coef = 0.1 !only used if iloadtide=2,3 (for '3', the default should be 0.12)
    
    ! Starting time
      start_year = 2000 !int
      start_month = 1 !int
      start_day = 1 !int
      start_hour = 0 !double
      utc_start = 8 !double
    
    !-----------------------------------------------------------------------
    ! Coordinate option: 1: Cartesian; 2: lon/lat (hgrid.gr3=hgrid.ll in this case,
    ! and orientation of element is outward of earth)
    ! Notes for lon/lat: make sure hgrid.ll and grid in sflux are consistent in 
    ! longitude range!
    !-----------------------------------------------------------------------
      ics = 1 !Coordinate option
    
    !-----------------------------------------------------------------------
    ! Hotstart option. 0: cold start; 1: hotstart with time reset to 0; 2: 
    ! continue from the step in hotstart.nc
    !-----------------------------------------------------------------------
      ihot = 0
    
    !-----------------------------------------------------------------------
    ! Equation of State type used
    ! ieos_type=0: UNESCO 1980 (nonlinear); =1: linear function of T ONLY, i.e. 
    ! \rho=eos_b+eos_a*T, where eos_a<=0 in kg/m^3/C
    !-----------------------------------------------------------------------
      ieos_type = 0
      ieos_pres = 0 !used only if ieos_type=0. 0: without pressure effects 
      eos_a = -0.1 !needed if ieos_type=1; should be <=0 
      eos_b = 1001. !needed if ieos_type=1
    
    !-----------------------------------------------------------------------
    ! Main ramp option
    !-----------------------------------------------------------------------
    !  nramp = 1 !ramp-up option (1: on; 0: off)
      dramp = 1. !ramp-up period in days for b.c. etc (no ramp-up if <=0)
    
    !  nrampbc = 0 !ramp-up flag for baroclinic force
      drampbc = 0. !ramp-up period in days for baroclinic force
    
    !-----------------------------------------------------------------------
    ! Method for momentum advection. 0: ELM; 1: upwind (not quite working yet)
    !-----------------------------------------------------------------------
      iupwind_mom = 0
    
    !-----------------------------------------------------------------------
    ! Methods for computing velocity at nodes. 
    ! If indvel=0, conformal linear shape function is used; if indvel=1, averaging method is used.
    ! For indvel=0, a stabilization method is needed (see below). 
    !-----------------------------------------------------------------------
      indvel = 0 
     
    !-----------------------------------------------------------------------
    ! 2 stabilization methods, mostly for indvel=0.
    ! (1) Horizontal viscosity option. ihorcon=0: no viscosity is used; =1: Lapacian;
    ! =2: bi-harmonic. If ihorcon=1, horizontal viscosity _coefficient_ (<=1/8, related
    ! to diffusion number) is given in hvis_coef0, and the diffusion # 
    ! is problem dependent; [0.001-1/8] seems to work well.
    ! If ihorcon=2, diffusion number is given by hvis_coef0 (<=0.025).
    ! If indvel=1, no horizontal viscosity is needed. 
    ! (2) Shapiro filter (see below)
    !
    ! For non-eddying regime applications (nearshore, estuary, river), an easiest option is: 
    !  indvel=0, ishapiro=1 (shapiro0=0.5), ihorcon=inter_mom=0.
    ! For applications that include eddying regime, refer to the manual.
    !-----------------------------------------------------------------------
      ihorcon = 0
      hvis_coef0 = 0.025 !const. diffusion # if ihorcon/=0; <=0.025 for ihorcon=2, <=0.125 for ihorcon=1
    !  cdh = 0.01 !needed only if ihorcon/=0; land friction coefficient - not active yet
    
    !-----------------------------------------------------------------------
    ! 2nd stabilization method via Shapiro filter. This should normally be used 
    ! if indvel=0. ishapiro=0: off; =1: constant filter strength in shapiro0; =-1:
    ! variable filter strength specified in shapiro.gr3; =2: variable filter strength specified
    ! as a Smagorinsky-like filter, with the coefficient specified in shapiro.gr3.
    ! To transition between eddying/non-eddying regimes, use
    ! indvel=0, ihorcon/=0, and ishapiro=-1 (requiring shapiro.gr3) or 2 (Smagorinsky-like filter).
    !-----------------------------------------------------------------------
      ishapiro = 1 !options
      niter_shap = 1 !needed if ishapiro/=0: # of iterations with Shapiro filter
      !shapiro0: Shapiro filter strength, needed only if ishapiro=1 
      !If ishapiro=1, shapiro0 is the filter strength (max is 0.5).
      !If ishapiro=2, the coefficient in tanh() is specified in shapiro.gr3. Experiences so far suggest 100 to 1.e3
      !If ishapiro=-1, the filter strength is directly read in from shapiro.gr3
      shapiro0 = 0.5 !needed only if ishapiro=1
    
    !-----------------------------------------------------------------------
    ! Implicitness factor (0.5<thetai<=1).
    !-----------------------------------------------------------------------
      thetai = 0.6 
    
    !-----------------------------------------------------------------------
    ! If WWM is used, set coupling/decoupling flag 'icou_elfe_wwm'. 
    ! No effects if USE_WWM is distabled in Makefile.
    ! Note that all these parameters must be present in this file (even when not used).
    !       0: no elevation and no currents in wwm, no wave force in SCHISM (but wave turbulecne, WBL etc are still in SCHISM);
    !       1: full coupled (elevation, vel, and wind are all passed to WWM); 
    !       2: elevation and currents in wwm, no wave force in SCHISM;  
    !       3: no elevation and no currents in wwm, wave force in SCHISM;
    !       4: elevation but no currents in wwm, wave force in SCHISM;
    !       5: elevation but no currents in wwm, no wave force in SCHISM;
    !       6: no elevation but currents in wwm, wave force in SCHISM;
    !       7: no elevation but currents in wwm, no wave force in SCHISM;
    ! If WWM is used and RADFLAG='VOR' in wwminput.nml, some parameters (fwvor_*)
    ! are added to take into account (1) or not (0) the different terms in vortex
    ! force expression.
    ! To get SCHISM-only result withno feedback from WWM, compile without WWM.
    !-----------------------------------------------------------------------
      icou_elfe_wwm = 0 
      nstep_wwm = 1  !call WWM every this many time steps 
      iwbl = 0 !wave boundary layer formulation (used only if USE_WMM and 
               !icou_elfe_wwm/=0 and nchi=1. If icou_elfe_wwm=0, set iwbl=0): 
               !1-modified Grant-Madsen formulation; 2-Soulsby (1997)
      hmin_radstress = 1. !min. total water depth used only in radiation stress calculation [m]
    !  nrampwafo = 0       !ramp-up option for the wave forces (1: on; 0: off)
      drampwafo = 0.      !ramp-up period in days for the wave forces (no ramp-up if <=0)
      turbinj = 0.15      !% of depth-induced wave breaking energy injected in turbulence 
                          !(default: 0.15 (15%), as proposed by Feddersen, 2012)
      turbinjds = 1.0     !% of wave energy dissipated through whitecapping injected in turbulence 
                          !(default: 1 (100%), as proposed by Paskyabi et al. 2012)
      alphaw = 0.5        !for itur=4 : scaling parameter for the surface roughness z0s = alphaw*Hm0. 
                          !If negative z0s = abs(alphaw) e.g. z0s=0.2 m (Feddersen and Trowbridge, 2005)
                             ! Vortex Force terms (off/on:0/1)
      fwvor_advxy_stokes = 1 !  --> Stokes drift advection (xy), Coriolis
      fwvor_advz_stokes = 1  !  --> Stokes drift advection (z) , Coriolis
      fwvor_gradpress = 1    !  --> Pressure term
      fwvor_breaking = 1     !  --> Wave breaking
      fwvor_streaming = 1    !  --> Wave streaming (works with iwbl /= 0)
      fwvor_wveg = 0         !  --> Wave dissipation by vegetation acceleration term
      fwvor_wveg_NL = 0      !  --> Non linear intrawave vegetation force (see Dean and Bender, 2006 or van Rooijen et al., 2016 for details) 
      cur_wwm = 0            ! Coupling current in WWM
                             ! 0: surface layer current
                             ! 1: depth-averaged current
                             ! 2: computed according to Kirby and Chen (1989)
      wafo_obcramp = 0       ! Ramp on wave forces at open boundary (1: on / 0: off)
                             !  --> this option requires the input file wafo_ramp.gr3
                             !      which defines the ramp value (between 0 and 1)
                             !      at nodes over the whole domain
    
    !-----------------------------------------------------------------------
    ! Bed deformation option (0: off; 1: vertical deformation only; 2: 3D bed deformation). 
    ! If imm=1, bdef.gr3 is needed; if imm=2, user needs to update depth info etc
    ! in the code (not working for ics=2 yet).
    !-----------------------------------------------------------------------
      imm = 0
      ibdef = 10 !needed if imm=1; # of steps used in deformation
    
    !-----------------------------------------------------------------------
    ! Reference latitude for beta-plane approximation when ncor=1 (not used if ics=2)
    !-----------------------------------------------------------------------
      slam0 = -124  !lon - not really used
      sfea0 = 45 !lat
    
    !-----------------------------------------------------------------------
    ! Option to deal with under resolution near steep slopes in deeper depths
    ! 0: use h[12,_bcc below; /=0: use hw_* below
    !-----------------------------------------------------------------------
      iunder_deep = 0 
    
    !-----------------------------------------------------------------------
    ! Baroclinicity calculation in off/nearshore with iunder_deep=ibc=0. 
    ! The 'below-bottom' gradient
    ! is zeroed out if h>=h2_bcc (i.e. like Z) or uses const extrap
    ! (i.e. like terrain-following) if h<=h1_bcc(<h2_bcc) (and linear
    ! transition in between based on local depth)
    !-----------------------------------------------------------------------
      h1_bcc = 50. ![m]
      h2_bcc = 100. ![m]; >h1_bcc
    
    !-----------------------------------------------------------------------
    ! Hannah-Wright-like ratio & depth used to account for under-resolution
    ! in a b-clinic model. Used only if ibc=0 and iunder_deep/=0.
    ! The b-clinic force at prism centers is calculated with a reconstruction
    ! method in horizontal that has a stencil of an element and its adjacent elements.
    ! If the depths change is too much between the elem and its adjacent elem
    ! the under-resolution occurs (with steep bottom slope) and b-clinic force
    ! needs to be zeroed out below the (higher) bottom, specifically, if
    ! max(2 depths)>=hw_depth and abs(diff(2 depths))>=hw_ratio*max(2 depths).
    !-----------------------------------------------------------------------
      hw_depth = 1.e6 !threshold depth in [m]
      hw_ratio = 0.5 !ratio
    
    !-----------------------------------------------------------------------
    ! Hydraulic model option. If ihydraulics/=0, hydraulics.in 
    ! is required. This option cannot be used with non-hydrostatic model.
    !-----------------------------------------------------------------------
      ihydraulics = 0
    
    !-----------------------------------------------------------------------
    ! Point sources/sinks option (0: no; 1: ASCII inputs; -1: netcdf). 
    ! If =1, needs source_sink.in (list of elements),
    ! vsource,th, vsink.th, and msource.th (the source/sink values must be single precision). 
    ! If =-1, all info is in source.nc
    ! and each type of volume/mass source/sink can have its own time step and
    ! # of records.
    ! Source/sinks can be specified at an elem more
    ! than once, and the code will accumulate the volumes; for mass conc, 
    ! values are applied at _net_ source elem (no summation for conc).
    
    ! meth_sink: options to treat sinks @ dry elem: no speacial treatment if meth_sink=0;
    ! zero out sink if the elem is dry if meth_sink=1
    ! If USE_NWM_BMI is on with if_source/=0, some parts of the reading and some b.c. will be bypassed (but the inputs
    ! will still be needed).
    !-----------------------------------------------------------------------
      if_source = 0
    !  nramp_ss = 1 !needed if if_source=1; ramp-up flag for source/sinks
      dramp_ss = 2 !needed if if_source/=0; ramp-up period in days for source/sinks (no ramp-up if <=0)
      meth_sink = 1 !options to treat sinks @ dry elem
    
    !----------------------------------------------------------------------
    ! Specify vertical level to inject source concentration for each tracer _module_.
    ! Code will extrapolate below bottom/above surface unless level 0 is specified. In
    ! the latter case, the incoming tracer mass will be distributed across all vertical layers - 
    ! this approach works best in shallow waters. 
    ! NOTE: AGE module has its own way of injecting age tracers, so make sure the age concentrations
    !  are all -9999. in msource.th so as to not interfere!
    !----------------------------------------------------------------------
      lev_tr_source(1) = -9 !T
      lev_tr_source(2) = -9 !S
      lev_tr_source(3) = -9 !GEN
      lev_tr_source(4) = -9 !AGE: set -9999. in msource's AGE section
      lev_tr_source(5) = -9 !SED3D
      lev_tr_source(6) = -9 !EcoSim
      lev_tr_source(7) = -9 !ICM
      lev_tr_source(8) = -9 !CoSINE
      lev_tr_source(9) = -9 !Feco
      lev_tr_source(10) = -9 !TIMOR
      lev_tr_source(11) = -9 !FABM
      lev_tr_source(12) = -9 !DVD
    
    !----------------------------------------------------------------------
    ! Specify level #'s if age module is invoked (USE_AGE), for 1st half of tracers only
    !----------------------------------------------------------------------
      level_age = 9, -999 !default: -999 (all levels)
    
    !-----------------------------------------------------------------------
    ! Horizontal diffusivity option. if ihdif=1, horizontal diffusivity is given in hdif.gr3
    !-----------------------------------------------------------------------
      ihdif = 0 
    
    !-----------------------------------------------------------------------
    ! Bottom friction. 
    !           nchi=0: drag coefficients specified in drag.gr3; nchi=-1: Manning's 
    !           formulation (even for 3D prisms) with n specified in manning.gr3. 
    !           nchi=1: bottom roughness (in meters) specified in rough.gr3 (and in this case, negative
    !           or 0 depths in rough.gr3 indicate time-independent Cd, not roughness!).
    !           Cd is calculated using the log law, when dzb>=dzb_min; when dzb<dzb_min,
    !           Cd=Cdmax, where Cdmax=Cd(dzb=dzb_min).
    !           If iwbl/=0, nchi must =1.
    !-----------------------------------------------------------------------
      nchi = 0 
      dzb_min = 0.5 !needed if nchi=1; min. bottom boundary layer thickness [m].
    !  dzb_decay = 0. !needed if nchi=1; a decay const. [-]. should =0
      hmin_man = 1. !needed if nchi=-1: min. depth in Manning's formulation [m]
    
    !-----------------------------------------------------------------------
    ! Coriolis. If ncor=-1, specify "rlatitude" (in degrees); if ncor=0,
    ! specify Coriolis parameter in "coricoef"; if ncor=1, model uses
    ! lat/lon in hgrid.ll for beta-plane approximation if ics=1, and in this case,
    ! the latitude specified in CPP projection ('sfea0') is used. If ncor=1 and ics=2,
    ! Coriolis is calculated from local latitude, and 'sfea0' is not used.
    !-----------------------------------------------------------------------
      ncor = 0 !should usually be 1 if ics=2
      rlatitude = 46 !if ncor=-1
      coricoef = 0 !if ncor=0
    
    !-----------------------------------------------------------------------
    ! Elevation initial condition flag for cold start only. For hotstart, set this to 0
    ! (and elev will be read in from hotstart.nc).
    ! If ic_elev=1, elev.ic (in *.gr3 format) is needed
    ! to specify the initial elevations; otherwise elevation is initialized to 0 everywhere 
    !-----------------------------------------------------------------------
      ic_elev = 0
    
    !-----------------------------------------------------------------------
    ! Elevation boundary condition ramp-up flag. =0: ramp up from 0; =1: ramp up from
    ! elev. values read in from elev.ic or hotstart.nc - if neither is present, from 0.
    ! This flag is mainly used to start the simulation from non-zero elev.
    ! The ramp-up period is 'dramp' (so if dramp=0, full strength is applied).
    !-----------------------------------------------------------------------
      nramp_elev = 0
    
    !-----------------------------------------------------------------------
    ! Optional inverse barometric effects on the elev. b.c.
    ! If inv_atm_bnd=1, the elev.'s at boundary are corrected by the difference
    ! between the actual atmos. pressure and a reference pressure (prmsl_ref below)
    !-----------------------------------------------------------------------
      inv_atm_bnd = 0 !0: off; 1: on
      prmsl_ref = 101325. !reference atmos. pressure on bnd [Pa]
    
    !-----------------------------------------------------------------------
    ! Initial condition for T,S. This value only matters for ihot=0 (cold start).
    ! If flag_ic(1:2)=1, the initial T,S field is read in from temp.ic and salt.ic (horizontally varying).
    ! If flag_ic(1:2)=2, the initial T,S field is read in from ts.ic (vertical varying).
    ! If ihot=0 && flag_ic(1:2)=2 || ibcc_mean=1, ts.ic is used for removing mean density profile.
    ! flag_ic(1) must =flag_ic(2)
    !-----------------------------------------------------------------------
      flag_ic(1) = 1 !T
      flag_ic(2) = 1 !S
    
    ! initial conditions for other tracers.
    ! 1: needs inputs [MOD]_hvar_[1,2,...].ic ('1...' is tracer id); format of each file is similar to salt.ic;
    !    i.e. horizontally varying i.c. is used for each tracer.
    ! 2: needs [MOD]_vvar_[1,2,...].ic. Format of each file (for each tracer in tis MOD) is similar to ts.ic
    !    (i.e. level #, z-coord., tracer value). Verically varying i.c. is used for each tracer.
    ! 0: model sets own i.c. (EcoSim; TIMOR)
      flag_ic(3) = 1 !GEN (user defined module)
    !  flag_ic(4) = 1 !Age i.c. flag set inside code
      flag_ic(5) = 1 !SED3D
      flag_ic(6) = 1 !EcoSim
      flag_ic(7) = 1 !ICM
      flag_ic(8) = 1 !CoSINE
      flag_ic(9) = 1 !FIB
      flag_ic(10) = 1 !TIMOR
      flag_ic(11) = 1 !FABM
      flag_ic(12) = 0 !DVD (must=0)
    
    !-----------------------------------------------------------------------
    ! Settling vel [m/s] for GEN module (positive downward)
    !-----------------------------------------------------------------------
      gen_wsett = 0 !1.e-4
    
    !-----------------------------------------------------------------------
    ! Mean T,S profile option. If ibcc_mean=1 (or ihot=0 and flag_ic(1)=2), mean profile
    ! is read in from ts.ic, and will be removed when calculating baroclinic force.
    ! No ts.ic is needed if ibcc_mean=0.
    !-----------------------------------------------------------------------
      ibcc_mean = 0 
    
    !-----------------------------------------------------------------------
    ! Max. horizontal velocity magnitude, used mainly to prevent problem in 
    ! bulk aerodynamic module
    !-----------------------------------------------------------------------
      rmaxvel = 5.
    
    !-----------------------------------------------------------------------
    !  Following parameters control backtracking
    !-----------------------------------------------------------------------
    !-----------------------------------------------------------------------
    !  min. vel for invoking btrack and for abnormal exit in quicksearch
    !-----------------------------------------------------------------------
      velmin_btrack = 1.e-4
    !-----------------------------------------------------------------------
    ! Nudging factors for starting side/node - add noise to avoid underflow
    ! The starting location is nudged to: old*(1-btrack_nudge)+btrack_nudge*centroid
    ! Suggested value: btrack_nudge=9.013e-3
    !-----------------------------------------------------------------------
      btrack_nudge= 9.013e-3 
    
    !-----------------------------------------------------------------------
    ! Behavior when trajectory hits open bnd. If ibtrack_openbnd=0, slide with
    ! tangential vel; otherwise, stop and exit btrack 
    !-----------------------------------------------------------------------
    !  ibtrack_openbnd = 1 !hardwired
    
    !-----------------------------------------------------------------------
    ! Wetting and drying. 
    ! - if ihhat=1, \hat{H} is made non-negative to enhance robustness near 
    ! wetting and drying; if ihhat=0, no retriction is imposed for this quantity. 
    ! - inunfl=0 is used for normal cases and inunfl=1 is used for more accurate wetting
    ! and drying if grid resolution is sufficiently fine.
    ! - if shorewafo=1, we impose radiation stress R_s = g*grad(eta) (balance between radiation stress
    ! gradients and the barotropic gradients) at the numerical shoreline (boundary between
    ! dry and wet elements). This option ensures that the shallow depth in dry elements does not
    ! create unphysical and very high wave forces at the shoreline (advised for morphodynamics runs).
    !-----------------------------------------------------------------------
      ihhat = 1 
      inunfl = 0
      h0 = 0.01     !min. water depth for wetting/drying [m]
      shorewafo = 0 !Matters only if USE_WWM
    
    !-----------------------------------------------------------------------
    ! Solver options
    ! USE_PETSC controls the solver type. If it's diabled, the default JCG 
    ! solver is used. If it's enabled, use PetSc lib. Some of the parameters
    ! have different meanings under these 2 options. Also with PetSc one can
    ! use cmd line options to choose solver etc.
    !-----------------------------------------------------------------------
      moitn0 = 50 !output spool for solver info; used only with JCG
      mxitn0 = 1500 !max. iteration allowed
      rtol0 = 1.e-12 !error tolerance
    
    !-----------------------------------------------------------------------
    ! Advection (ELM) option. If nadv=1, backtracking is done using Euler method; 
    ! nadv=2, using 2nd order Runge-Kutta; if nadv=0, advection in momentum 
    ! is turned off/on in adv.gr3 (the depths=0,1, or 2 also control methods 
    ! in backtracking as above). dtb_max/min are the max/min steps allowed -
    ! actual step is calculated adaptively based on local gradient.
    !-----------------------------------------------------------------------
      nadv = 1
      dtb_max = 30. !in sec
      dtb_min = 10.
    
    !-----------------------------------------------------------------------
    ! If inter_mom=0, linear interpolation is used for velocity at foot of char. line.
    ! If inter_mom=1 or -1, Kriging is used, and the choice of covariance function is
    ! specified in 'kr_co'. If inter_mom=1, Kriging is applied to whole domain;
    ! if inter_mom=-1, the regions where Kriging is used is specified in krvel.gr3 
    ! (depth=0: no kriging; depth=1: with kriging). 
    !-----------------------------------------------------------------------
      inter_mom = 0 
      kr_co = 1 !not used if inter_mom=0
    
    !-----------------------------------------------------------------------
    ! Tracer transport method. TVD or WENO method requires tvd.prop.
    ! TVD or WENO method is used on an element/prism if the total depth (at all nodes of the elem.)>=h_tvd and the flag in
    ! tvd.prop = 1 for the elem; otherwise upwind is used for efficiency. 
    ! itr_met=3 (horizontal TVD) or 4 (horizontal WENO): implicit TVD in the vertical dimension. 
    ! Also if itr_met==3 and h_tvd>=1.e5, some parts of the code are bypassed for efficiency.
    ! Controls for WENO are not yet in place.
    !-----------------------------------------------------------------------
      itr_met = 3 
      h_tvd = 5. !cut-off depth (m) 
      !If itr_met=3 or 4, need the following 2 tolerances of convergence. The convergence
      !is achieved when sqrt[\sum_i(T_i^s+1-T_i^s)^2]<=eps1_tvd_imp*sqrt[\sum_i(T_i^s)^2]+eps2_tvd_imp
      eps1_tvd_imp = 1.e-4 !suggested value is 1.e-4, but for large suspended load, need to use a smaller value (e.g. 1.e-9)
      eps2_tvd_imp = 1.e-14  
    
      !Optional hybridized ELM transport for efficiency
      ielm_transport = 0 !1: turn on 
      max_subcyc = 10 !used only if ielm_transport/=0. Max # of subcycling per time step in transport allowed
    
      !if itr_met = 4, the following parameters are needed
      !if itr_met=4 and ipre=1, diagnostic outputs are generated for weno accuracy and stencil quality, 
      !  see subroutine weno_diag in src/Hydro/misc_subs.F90 for details
      ip_weno = 2   !order of accuracy: 0- upwind; 1- linear polynomial, 2nd order; 2- quadratic polynomial, 3rd order
      courant_weno=0.5 !Courant number for weno transport
      nquad = 2  !number of quad points on each side, nquad= 1 or 2
      ntd_weno = 1 !order of temporal discretization: (1) Euler (default); (3): 3rd-order Runge-Kutta (only for benchmarking)
      epsilon1 = 1.e-15   !coefficient for 2nd order weno smoother (larger values are more prone to numerical dispersion)
      epsilon2 = 1.e-10  !1st coefficient for 3rd order weno smoother (larger values are more prone to numerical dispersion
                         !, 1.e-10 should be fairly safe, recommended values: 1.e-8 ~ 1.e-6 (from the real applications so far)
      i_prtnftl_weno = 0 !option for writing nonfatal errors on invalid temp. or salinity for density: (0) off; (1) on.
    
      !Inactive at the moment:
      epsilon3 = 1.e-25  !2nd coefficient for 3rd order weno smoother (inactive at the moment)
      !Elad filter has not been implemented yet; preliminary tests showed it might not be necessary
      ielad_weno = 0      !ielad, if ielad=1, use ELAD method to suppress dispersion (inactive at the moment)
      small_elad = 1.e-4  !small (inactive at the moment)
    
    !-----------------------------------------------------------------------
    ! Atmos. option. Use nws=2 and USE_ATMOS for coupling with atmospheric model.
    ! If nws=0, no atmos. forcing is applied. If nws=1, atmos.
    ! variables are read in from wind.th. If nws=2, atmos. variables are
    ! read in from sflux_ files.
    ! If nws=4, ascii format is used for wind and atmos. pressure at each node (see source code).
    ! If nws=-1 (requires USE_PAHM), use Holland parametric wind model (barotropic only with wind and atmos. pressure).
    !  In this case, the Holland model is called every step so wtiminc is not used. An extra 
    !  input file is needed: hurricane-track.dat, in addition to a few parameters below.
    !
    ! Stress calculation:
    ! If nws=2, ihconsv=1 and iwind_form=0, the stress is calculated from heat exchange
    ! routine; in this case USE_ATMOS cannot be on.
    ! Otherwise if iwind_form=-1, the stress is calculated from Pond & Pichard formulation;
    ! if iwind_form=1, Hwang (2018) formulation (Cd tapers off at high wind).
    ! If WWM is enabled and icou_elfe_wwm>0 and iwind_form=-2 or -3, stress is overwritten by WWM:
    ! If iwind_form=-2, stress=rho_air*ufric^2; scaled by rho_water
    ! If iwind_form=-3, the stress is calculated according to the param. of Donelan et al. (1993) based on the wave age.
    ! In all cases, if USE_ICE the stress in ice-covered portion is calculated by ICE routine.
    !-----------------------------------------------------------------------
      nws = 0 
      wtiminc = 150. !time step for atmos. forcing. Default: same as dt
    !  nrampwind = 1 !ramp-up option for atmos. forcing
      drampwind = 1. !ramp-up period in days for wind (no ramp-up if <=0)
      iwindoff = 0 !needed only if nws/=0; '1': needs windfactor.gr3
      iwind_form = 1 !needed if nws/=0
      model_type_pahm=10 !only used if nws=-1: hurricane model type (1: Holland; 10: GAHM)
    
      !If IMPOSE_NET_FLUX is on and nws=2, read in net _surface_ heat flux as var 'dlwrf' 
      !(Downward Long Wave) in sflux_rad (solar radiation is still used separately),
      !and if PREC_EVAP is on, also read in net P-E as 'prate' (Surface Precipitation Rate) in sflux_prc.
    
    !-----------------------------------------------------------------------
    ! Heat and salt exchange using Zeng's (default) or Fairall (USE_BULK_FAIRALL) scheme.
    ! isconsv=1 needs ihconsv=1; ihconsv=1 needs nws=2.
    ! If isconsv=1, need to compile with precip/evap module turned on.
    ! If at least one of ihconsv and isconsv is set to 1,
    ! locally turning off air-sea exchange in shallow waters (<0.25 m) is recommended.
    ! Options for locally turning off heat/salt exchange are specified by
    ! i_hmin_airsea_ex, i_hmin_salt_ex respectively:
    !   0: not turned off locally;
    !   1: locally turned off, based on grid depth, i.e.,
    !      off when the local grid depth (z in hgrid) < hmin_airsea_ex or hmin_salt_ex;
    !   2 (recommended): locally turned off, based on local total water depth, i.e.,
    !      off when the local total water depth < hmin_airsea_ex or hmin_salt_ex,
    ! hmin_airsea_ex, hmin_salt_ex:
    !   0.2 m is recommended for both "1" and "2"
    !-----------------------------------------------------------------------
      ihconsv = 0 !heat exchange option
      isconsv = 0 !evaporation/precipitation model
      i_hmin_airsea_ex = 2 ! no effect if ihconsv=0 
      hmin_airsea_ex = 0.2 ![m], no effect if ihconsv=0 
      i_hmin_salt_ex = 2 ! no effect if isconsv=0 
      hmin_salt_ex = 0.2 ![m], no effect if isconsv=0 
      iprecip_off_bnd = 0 !if /=0, precip will be turned off near land bnd
    
    !-----------------------------------------------------------------------
    ! Turbulence closure.
    !-----------------------------------------------------------------------
      itur = 3 !Default: 0
      dfv0 = 1.e-2 !needed if itur=0
      dfh0 = 1.e-4 !needed if itur=0
      mid = 'KL' !needed if itur=3,5. Use KE if itur=5 
      stab = 'KC' !needed if itur=3 or 5. Use 'GA' if turb_met='MY'; otherwise use 'KC'. 
      xlsc0 = 0.1 !needed if itur=3 or 5. Scale for surface & bottom mixing length (>0)
    
    !-----------------------------------------------------------------------
    ! Sponge layer for elevation and vel.
    ! If inu_elev=0, no relaxation is applied to elev.
    ! If inu_elev=1, relax. constants (in 1/sec, i.e. relax*dt<=1) are specified in elev_nudge.gr3
    ! and applied to eta=0 (thus a depth=0 means no relaxation).
    ! Similarly for inu_uv (with input uv_nudge.gr3)
    !-----------------------------------------------------------------------
      inu_elev = 0
      inu_uv = 0
    
    !-----------------------------------------------------------------------
    ! Nudging options for tracers. If inu_[MOD]=0, no nudging is used. If inu_tr=1,
    ! nudge to initial condition according to relaxation constants specified.
    ! If inu_tr=2, nudge to values in [MOD]_nu.nc (with step 'step_nu_tr').
    ! The relaxation constants = [horizontal relax (specified in [MOD]_nudge.gr3) + or x
    ! vertical relax] times dt, where vertical relax is a linear function of 
    ! vnh[1,2] and vnf[1,2], and [MOD] are tracer model names. 'nu_sum_mult' decides
    ! '+' or 'x' in the calculation of final relax.
    ! Code will ignore junk values (<=-99) inside [MOD]_nu.nc, so 1 way to avoid 
    ! nudging for a tracer is to set its nudged values to -9999
    !-----------------------------------------------------------------------
      inu_tr(1) = 0 !T
      inu_tr(2) = 0 !S
      inu_tr(3) = 0 !GEN
      inu_tr(4) = 0 !Age
      inu_tr(5) = 0 !SED3D
      inu_tr(6) = 0 !EcoSim 
      inu_tr(7) = 0 !ICM 
      inu_tr(8) = 0 !CoSINE 
      inu_tr(9) = 0 !FIB
      inu_tr(10) = 0 !TIMOR 
      inu_tr(11) = 0 !FABM 
      inu_tr(12) = 0 !DVD (must=0)
    
      nu_sum_mult=1 !1: final relax is sum of horizontal&vertical; 2: product
      vnh1 = 400 !vertical nudging depth 1
      vnf1 = 0. !vertical relax \in [0,1]
      vnh2 = 500 !vertical nudging depth 2 (must >vnh1)
      vnf2 = 0. !vertical relax
    
      step_nu_tr = 86400. !time step [sec] in all [MOD]_nu.nc (for inu_[MOD]=2)
    
    !-----------------------------------------------------------------------
    ! Cut-off depth for cubic spline interpolation near bottom when computing horizontal gradients
    ! e.g. using hgrad_nodes() (radiation stress, and gradients of qnon and qhat in non-hydro model). 
    ! If depth > h_bcc1 ('deep'),
    ! a min. (e.g. max bottom z-cor for the element) is imposed in the spline and so a more
    ! conservative method is used without extrapolation beyond bottom; 
    ! otherwise constant extrapolation below bottom is used.
    !-----------------------------------------------------------------------
      h_bcc1 = 100. !h_bcc1
    
    !-----------------------------------------------------------------------
    ! Dimensioning parameters for inter-subdomain btrack. 
    ! If error occurs like 'bktrk_subs: overflow' or 'MAIN: nbtrk > mxnbt'
    ! gradually increasing these will solve the problem
    !-----------------------------------------------------------------------
      s1_mxnbt = 0.5
      s2_mxnbt = 3.5
    
    !-----------------------------------------------------------------------
    ! Flag for harmonic analysis for elevation. If used , need to turn on USE_HA
    ! in Makefile, and input harm.in. Otherwise set it to 0. Hotstart ihot=2 is not working with HA
    ! Outputs are harme_* and use combine_outHA to combine.
    !-----------------------------------------------------------------------
      iharind = 0
    
    !-----------------------------------------------------------------------
    ! Conservation check option. If iflux/=0, some fluxes are computed
    ! in regions specified in fluxflag.prop (regional number from -1 to an arbitrary integer)
    ! in output flux.out, positive means flux from region n to region n-1 (n>=1).
    ! Output file flux.out will be appended on ihot=2.
    ! iflux=1: basic output; =2: more elaborate outputs
    !-----------------------------------------------------------------------
      iflux = 0
    
    !-----------------------------------------------------------------------
    ! Test flags for debugging. These flags should be turned off normally.
    !-----------------------------------------------------------------------
    ! Williamson test #5 (zonal flow over an isolated mount); if
    ! on, ics must =2
    !-----------------------------------------------------------------------
      izonal5 = 0 !"0" - no test; otherwise on
    
    !-----------------------------------------------------------------------
    ! Rotating Gausshill test with stratified T,S (1: on; 0: off)
    ! Surface T,S read in from *.ic; code generates stratification
    !-----------------------------------------------------------------------
      ibtrack_test = 0
    
    !-----------------------------------------------------------------------
    ! Rouse profile test (1: on; 0: off)
    ! If on, must turn on USE_TIMOR
    !-----------------------------------------------------------------------
      irouse_test = 0
    
    !-----------------------------------------------------------------------
    ! Flag to choose FIB model for bacteria decay (used with USE_FIB)
    ! flag_fib = 1 - Constant decay rate (/day) in .gr3 format
    !                (kkfib_1.gr3 and kkfib_2.gr3)
    ! flag_fib = 2 - Decay rate computed from Canteras et al., 1995
    ! flag_fib = 3 - Decay rate computed from Servais et al., 2007
    !----------------------------------------------------------------------
      flag_fib = 1
    
    !----------------------------------------------------------------------
    ! Marsh model parameters (only if USE_MARSH is on)
    !----------------------------------------------------------------------
      slr_rate = 120. !sea-level rise rate in mm/yr, times morphological acceleration if used
    
    !----------------------------------------------------------------------
    ! Vegetation model
    ! If isav=1, need 4 extra inputs: (1) sav_D.gr3 (depth is stem diameter in meters);
    ! (2) sav_N.gr3 (depth is # of stems per m^2);
    ! (3) sav_h.gr3 (height of canopy in meters);
    ! (4) sav_cd.gr3 (drag coefficient).									
    ! If one of these depths=0 at a node, the code will set all to 0. 
    ! If USE_MARSH is on and isav=1, all .gr3 must have constant depths!
    !----------------------------------------------------------------------
      isav = 0 !on/off flag
    
    !----------------------------------------------------------------------
    ! Coupling step with ICE module.
    !----------------------------------------------------------------------
      nstep_ice = 1 !call ice module every nstep_ice steps of SCHISM
    
    
    !+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ! Physical constants
    !+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    !-----------------------------------------------------------------------
    ! Earth's radii at pole and equator (to define an ellipsoid)
    !-----------------------------------------------------------------------
      rearth_pole = 6378206.4
      rearth_eq = 6378206.4
    
    !-----------------------------------------------------------------------
    ! Specific heat of water (C_p) in J/kg/K
    !-----------------------------------------------------------------------
      shw = 4184.d0
    
    !-----------------------------------------------------------------------
    ! Reference water density for Boussinesq approximation
    !-----------------------------------------------------------------------
      rho0 = 1000.d0 !kg/m^3
    
    !-----------------------------------------------------------------------
    ! Fraction of vertical flux closure adjustment applied at surface, then subtracted
    ! from all vertical fluxes. This is currently done for T,S only
    ! 0.0 <= vclose_surf_frac < 1.0
    ! 1: fully from surface (i.e. no correction as before); 0: fully from bottom 
    !-----------------------------------------------------------------------
      vclose_surf_frac=1.0
    
    !-----------------------------------------------------------------------
    ! Option to enforce strict mass conservation for each tracer model (only works with itr_met=3,4)
    ! At moment the scheme has not accounted for bottom 'leaking' (e.g. in SED), 
    ! so iadjust_mass_consv0(5) must =0
    !-----------------------------------------------------------------------
      iadjust_mass_consv0(1)=0 !T
      iadjust_mass_consv0(2)=0 !S
      iadjust_mass_consv0(3)=0 !GEN
      iadjust_mass_consv0(4)=0 !AGE
      iadjust_mass_consv0(5)=0 !SED3D (code won't allow non-0 for this module)
      iadjust_mass_consv0(6)=0 !EcoSim
      iadjust_mass_consv0(7)=0 !ICM
      iadjust_mass_consv0(8)=0 !CoSiNE
      iadjust_mass_consv0(9)=0 !Feco
      iadjust_mass_consv0(10)=0 !TIMOR
      iadjust_mass_consv0(11)=0 !FABM
      iadjust_mass_consv0(12)=0 !DVD (must=0)
    
    ! For ICM, impose mass conservation for depths larger than a threshold by considering prism 
    ! volume change from step n to n+1. rinflation_icm is the max ratio btw H^{n+1} and H^n allowed.
      h_massconsv = 2. ![m]
      rinflation_icm = 1.e-3
    
    /
    
    &SCHOUT
    !-----------------------------------------------------------------------
    ! Output section - all optional. Values shown are default unless otherwise stated,
    ! and default for most global outputs is off
    !-----------------------------------------------------------------------
    
    !-----------------------------------------------------------------------
    ! Main switch to control netcdf. If =0, SCHISM won't output nc files 
    ! at all (useful for other programs like ESMF to output)
    !-----------------------------------------------------------------------
      nc_out = 1
    
    !-----------------------------------------------------------------------
    ! UGRID option for _3D_ outputs under scribed IO (out2d*.nc always has meta
    ! data info). If iof_ugrid/=0, 3D outputs will also have UGRID metadata (at
    ! the expense of file size). 
    !-----------------------------------------------------------------------
      iof_ugrid = 0
    
    !-----------------------------------------------------------------------
    ! Option for hotstart outputs
    !-----------------------------------------------------------------------
      nhot = 0 !1: output *_hotstart every 'nhot_write' steps
      nhot_write = 8640 !must be a multiple of ihfskip if nhot=1
    
    !-----------------------------------------------------------------------
    ! Station output option. If iout_sta/=0, need output skip (nspool_sta) and
    ! a station.in. If ics=2, the cordinates in station.in must be in lon., lat,
    ! and z (positive upward; not used for 2D variables). 
    !-----------------------------------------------------------------------
      iout_sta = 0
      nspool_sta = 10 !needed if iout_sta/=0; mod(nhot_write,nspool_sta) must=0
    
    !-----------------------------------------------------------------------
    ! Global output options
    ! The variable names that appear in nc output are shown in {}
    !-----------------------------------------------------------------------
      iof_hydro(1) = 1 !0: off; 1: on - elev. [m]  {elevation}  2D
      iof_hydro(2) = 0 !air pressure [Pa]  {airPressure}  2D
      iof_hydro(3) = 0 !air temperature [C] {airTemperature}  2D
      iof_hydro(4) = 0 !Specific humidity [-] {specificHumidity}  2D
      iof_hydro(5) = 0 !Net downward solar (shortwave) radiation after albedo [W/m/m] {solarRadiation}  2D
      iof_hydro(6) = 0 !sensible flux (positive upward) [W/m/m]  {sensibleHeat}  2D
      iof_hydro(7) = 0 !latent heat flux (positive upward) [W/m/m] {latentHeat}  2D
      iof_hydro(8) = 0 !upward longwave radiation (positive upward) [W/m/m] {upwardLongwave}  2D
      iof_hydro(9) = 0 !downward longwave radiation (positive downward) [W/m/m] {downwardLongwave}  2D
      iof_hydro(10) = 0 !total flux=-flsu-fllu-(radu-radd) [W/m/m] {totalHeat}  2D
      iof_hydro(11) = 0 !evaporation rate [kg/m/m/s] {evaporationRate}  2D
      iof_hydro(12) = 0 !precipitation rate [kg/m/m/s] {precipitationRate}  2D
      iof_hydro(13) = 0 !Bottom stress vector [kg/m/s^2(Pa)] {bottomStressX,Y}  2D vector
      iof_hydro(14) = 0 !wind velocity vector [m/s] {windSpeedX,Y}  2D vector
      iof_hydro(15) = 0 !wind stress vector [m^2/s/s] {windStressX,Y}  2D vector
      iof_hydro(16) = 0 !depth-averaged vel vector [m/s] {depthAverageVelX,Y}  2D vector
      iof_hydro(17) = 0 !vertical velocity [m/s] {verticalVelocity}  3D
      iof_hydro(18) = 0 !water temperature [C] {temperature}  3D
      iof_hydro(19) = 0 !water salinity [PSU] {salinity}  3D
      iof_hydro(20) = 0 !water density [kg/m^3] {waterDensity}  3D
      iof_hydro(21) = 0 !vertical eddy diffusivity [m^2/s] {diffusivity}  3D
      iof_hydro(22) = 0 !vertical eddy viscosity [m^2/s] {viscosity}  3D
      iof_hydro(23) = 0 !turbulent kinetic energy {turbulentKineticEner}   3D
      iof_hydro(24) = 0 !turbulent mixing length [m] {mixingLength}  3D
    !  iof_hydro(25) = 1 !z-coord {zCoordinates} 3D - this flag should be on for visIT etc
      iof_hydro(26) = 1 !horizontal vel vector [m/s] {horizontalVelX,Y} 3D vector
      iof_hydro(27) = 0 !horizontal vel vector defined @side [m/s] {horizontalSideVelX,Y} 3D vector
      iof_hydro(28) = 0 !vertical vel. @elem [m/s] {verticalVelAtElement} 3D
      iof_hydro(29) = 0 !T @prism centers [C] {temperatureAtElement} 3D
      iof_hydro(30) = 0 !S @prism centers [PSU] {salinityAtElement} 3D
      iof_hydro(31) = 0 !Barotropic pressure gradient force vector (m.s-2) @side centers  {pressure_gradient} 2D vector
    
    !-----------------------------------------------------------------------
    ! Outputs from optional modules. Only uncomment these if the USE_* is on
    !-----------------------------------------------------------------------
    !-----------------------------------------------------------------------
    ! Outputs from DVD (USE_DVD must be on in Makefile)
    !-----------------------------------------------------------------------
    !  iof_dvd(1) = 1 !num mixing for S (PSU^2/s) {DVD_1}   3D elem
    
    !-----------------------------------------------------------------------
    ! Outputs from WWM (USE_WWM must be on in Makefile)
    !-----------------------------------------------------------------------
    !  iof_wwm(1)  = 0 !sig. height (m) {sigWaveHeight}   2D
    !  iof_wwm(2)  = 0 !Mean average period (sec) - TM01 {meanWavePeriod}  2D
    !  iof_wwm(3)  = 0 !Zero down crossing period for comparison with buoy (s) - TM02 {zeroDowncrossPeriod}  2D
    !  iof_wwm(4)  = 0 !Average period of wave runup/overtopping - TM10 {TM10}  2D
    !  iof_wwm(5)  = 0 !Mean wave number (1/m) {meanWaveNumber}  2D
    !  iof_wwm(6)  = 0 !Mean wave length (m) {meanWaveLength}  2D
    !  iof_wwm(7)  = 0 !Mean average energy transport direction (degr) - MWD in NDBC? {meanWaveDirection}  2D
    !  iof_wwm(8) = 0 !Mean directional spreading (degr) {meanDirSpreading}  2D
    !  iof_wwm(9) = 0 !Discrete peak period (sec) - Tp {peakPeriod}  2D
    !  iof_wwm(10) = 0 !Continuous peak period based on higher order moments (sec) {continuousPeakPeriod}  2D
    !  iof_wwm(11) = 0 !Peak phase vel. (m/s) {peakPhaseVel}  2D
    !  iof_wwm(12) = 0 !Peak n-factor {peakNFactor}   2D
    !  iof_wwm(13) = 0 !Peak group vel. (m/s) {peakGroupVel}   2D
    !  iof_wwm(14) = 0 !Peak wave number {peakWaveNumber}  2D
    !  iof_wwm(15) = 0 !Peak wave length {peakWaveLength}  2D
    !  iof_wwm(16) = 0 !Peak (dominant) direction (degr) {dominantDirection}  2D
    !  iof_wwm(17) = 0 !Peak directional spreading {peakSpreading}  2D
    !  iof_wwm(18) = 0 !Discrete peak direction (radian?) {discretePeakDirectio}  2D
    !  iof_wwm(19) = 0 !Orbital vel. (m/s) {orbitalVelocity}  2D
    !  iof_wwm(20) = 0 !RMS Orbital vel. (m/s) {rmsOrbitalVelocity}  2D
    !  iof_wwm(21) = 0 !Bottom excursion period (sec?) {bottomExcursionPerio}  2D
    !  iof_wwm(22) = 0 !Bottom wave period (sec) {bottomWavePeriod}  2D
    !  iof_wwm(23) = 0 !Uresell number based on peak period {UresellNumber}  2D
    !  iof_wwm(24) = 0 !Friction velocity (m/s?) {frictionalVelocity}  2D
    !  iof_wwm(25) = 0 !Charnock coefficient {CharnockCoeff}  2D
    !  iof_wwm(26) = 0 !Rougness length {rougnessLength}  2D
    
    !  iof_wwm(27) = 0 !Roller energy dissipation rate (W/m²) @nodes {Drol} 2D
    !  iof_wwm(28) = 0 !Total wave energy dissipation rate by depth-induced breaking (W/m²) @nodes {wave_sbrtot}  2D
    !  iof_wwm(29) = 0 !Total wave energy dissipation rate by bottom friction (W/m²) @nodes {wave_sbftot} 2D
    !  iof_wwm(30) = 0 !Total wave energy dissipation rate by whitecapping (W/m²) @nodes {wave_sdstot} 2D
    !  iof_wwm(31) = 0 !Total wave energy dissipation rate by vegetation (W/m²) @nodes {wave_svegtot} 2D
    !  iof_wwm(32) = 0 !Total wave energy input rate from atmospheric forcing (W/m²) @nodes {wave_sintot} 2D
    !  iof_wwm(33) = 0 !WWM_energy vector {waveEnergyDirX,Y}  2D vector
    
    !  iof_wwm(34) = 0 !Vertical Stokes velocity (m.s-1) @sides and whole levels {stokes_wvel}  3D
    !  iof_wwm(35) = 0 !Wave force vector (m.s-2) computed by wwm @side centers and whole levels {waveForceX,Y}   3D vector
    
    !  iof_wwm(36) = 0 !Horizontal Stokes velocity (m.s-1) @nodes and whole levels {stokes_hvel} 3D vector
    !  iof_wwm(37) = 0 !Roller contribution to horizontal Stokes velocity (m.s-1) @nodes and whole levels {roller_stokes_hvel} 3D vector 
    
    !-----------------------------------------------------------------------
    ! Tracer module outputs. In most cases, actual # of outputs depends on # of tracers used
    !-----------------------------------------------------------------------
    ! Outputs for user-defined tracer module (USE_GEN)
    !-----------------------------------------------------------------------
    !  iof_gen(1) = 0 !1st tracer {GEN_1}  3D
    !  iof_gen(2) = 0 !2nd tracer {GEN_2}  3D
    
    !-----------------------------------------------------------------------
    ! Outputs for (age). Indices from "1" to "ntracer_age/2"; [days]
    !-----------------------------------------------------------------------
    !  iof_age(1) = 0 !{AGE_1}  3D
    !  iof_age(2) = 0 !{AGE_2}  3D
    
    !-----------------------------------------------------------------------
    ! Specific outputs in SED3D (USE_SED must be on in Makefile;
    ! otherwise these are not needed)
    !-----------------------------------------------------------------------
    !  iof_sed(1) = 0 ! total bed thickness @elem (m) {sedBedThickness}  2D
    !  iof_sed(2) = 0 ! total bed age over all layers @elem (sec) {sedBedAge}  2D
    !  iof_sed(3) = 0 ! Sediment transport roughness length @elem (m) (sedTransportRough) {z0st}  2D
    !  iof_sed(4) = 0 !current-ripples roughness length @elem (m) (sedRoughCurrentRippl) {z0cr}  2D
    !  iof_sed(5) = 0 !sand-waves roughness length (m) @elem (z0sw_elem) {sedRoughSandWave}  2D
    !  iof_sed(6) = 0 !wave-ripples roughness length @elem (m) (z0wr_elem) {sedRoughWaveRipple}  2D
    
    !  iof_sed(7) = 0 !bottom depth _change_ from init. condition (m) {sedDepthChange}  2D
    !  iof_sed(8) = 0 ! Bed median grain size in the active layer (mm) {sedD50}  2D
    !  iof_sed(9) = 0 ! Bottom shear stress (Pa) {sedBedStress}  2D
    !  iof_sed(10) = 0 ! Bottom roughness lenghth (mm) {sedBedRoughness}  2D
    !  iof_sed(11) = 0 ! sediment porosity in the top layer (-) {sedPorocity}  2D
    !  iof_sed(12) = 0 ! erosion flux for suspended transport (kg/m/m/s) {sedErosionalFlux}  2D
    !  iof_sed(13) = 0 ! deposition flux for suspended transport (kg/m/m/s) {sedDepositionalFlux}  2D
    !  iof_sed(14) = 0 ! Bedload transport rate vector due to wave acceleration (kg/m/s) {sedBedloadTransportX,Y}  2D vector
    
    !  Example of using 2 classes
    !  iof_sed(15) = 0 !Bedload transport rate _vector_ (kg.m-1.s-1) for 1st tracer (one output per class) {sedBedload[X,Y]_1}  2D vector
    !  iof_sed(16) = 0 !Bedload transport of 2nd class {sedBedFraction_[X,Y]_2}  2D vector
    !  iof_sed(17) = 0 !Bed fraction 1st tracer (one output per class) [-] {sedBedFraction_1}   2D
    !  iof_sed(18) = 0 !Bed fraction of 2nd class {sedBedFraction_2}   2D
    
    !  iof_sed(19) = 0 !conc. of 1st class (one output need by each class) [g/L] {sedConcentration_1}   3D
    !  iof_sed(20) = 0 !conc. of 2nd class {sedConcentration_2}   3D
    
    !  iof_sed(21) = 0 !total suspended concentration (g/L) {totalSuspendedLoad}  3D
    
    !-----------------------------------------------------------------------
    ! EcoSim outputs 
    !-----------------------------------------------------------------------
    !  iof_eco(1) = 0 {ECO_1}  3D
    
    !-----------------------------------------------------------------------
    ! ICM outputs 
    !-----------------------------------------------------------------------
    !  !core Module
    !  iof_icm_core(1)  = 1 !PB1
    !  iof_icm_core(2)  = 1 !PB2
    !  iof_icm_core(3)  = 1 !PB3
    !  iof_icm_core(4)  = 1 !RPOC
    !  iof_icm_core(5)  = 1 !LPOC
    !  iof_icm_core(6)  = 1 !DOC
    !  iof_icm_core(7)  = 1 !RPON
    !  iof_icm_core(8)  = 1 !LPON
    !  iof_icm_core(9)  = 1 !DON
    !  iof_icm_core(10) = 1 !NH4
    !  iof_icm_core(11) = 1 !NO3
    !  iof_icm_core(12) = 1 !RPOP
    !  iof_icm_core(13) = 1 !LPOP
    !  iof_icm_core(14) = 1 !DOP
    !  iof_icm_core(15) = 1 !PO4
    !  iof_icm_core(16) = 1 !COD
    !  iof_icm_core(17) = 1 !DOX
    !
    !  !silica module
    !  iof_icm_silica(1) = 1 !SU
    !  iof_icm_silica(2) = 1 !SA
    !
    !  !zooplankton module
    !  iof_icm_zb(1)  = 1 !ZB1
    !  iof_icm_zb(2)  = 1 !ZB2
    !
    !  !pH model
    !  iof_icm_ph(1) = 1 !TIC
    !  iof_icm_ph(2) = 1 !ALK
    !  iof_icm_ph(3) = 1 !CA
    !  iof_icm_ph(4) = 1 !CACO3
    !
    !  !CBP model
    !  iof_icm_cbp(1) = 1 !SRPOC
    !  iof_icm_cbp(2) = 1 !SRPON
    !  iof_icm_cbp(3) = 1 !SRPOP
    !  iof_icm_cbp(4) = 1 !PIP
    !
    !  !SAV model
    !  iof_icm_sav(1) = 1 !stleaf: total leaf biomass @elem [gC/m^2]
    !  iof_icm_sav(2) = 1 !ststem: total stem biomass @elem [gC/m^2]
    !  iof_icm_sav(3) = 1 !stroot: total root biomass @elem [gC/m^2]
    !  iof_icm_sav(4) = 1 !sht:    canopy height @elem [m]
    !
    !  !VEG model
    !  iof_icm_veg(1)  = 1 !vtleaf1: leaf biomass group 1 [gC/m^2]
    !  iof_icm_veg(2)  = 1 !vtleaf2: leaf biomass group 2 [gC/m^2]
    !  iof_icm_veg(3)  = 1 !vtleaf3: leaf biomass group 3 [gC/m^2]
    !  iof_icm_veg(4)  = 1 !vtstem1: stem biomass group 1 [gC/m^2]
    !  iof_icm_veg(5)  = 1 !vtstem2: stem biomass group 2 [gC/m^2]
    !  iof_icm_veg(6)  = 1 !vtstem3: stem biomass group 3 [gC/m^2]
    !  iof_icm_veg(7)  = 1 !vtroot1: root biomass group 1 [gC/m^2]
    !  iof_icm_veg(8)  = 1 !vtroot2: root biomass group 2 [gC/m^2]
    !  iof_icm_veg(9)  = 1 !vtroot3: root biomass group 3 [gC/m^2]
    !  iof_icm_veg(10) = 1 !vht1:    canopy height group 1 [m]
    !  iof_icm_veg(11) = 1 !vht2:    canopy height group 2 [m]
    !  iof_icm_veg(12) = 1 !vht3:    canopy height group 3 [m]
    !
    !  !SFM model
    !  iof_icm_sed(1)   = 1 !bPOC1 (g.m-3)
    !  iof_icm_sed(2)   = 1 !bPOC2 (g.m-3)
    !  iof_icm_sed(3)   = 1 !bPOC3 (g.m-3)
    !  iof_icm_sed(4)   = 1 !bPON1 (g.m-3)
    !  iof_icm_sed(5)   = 1 !bPON2 (g.m-3)
    !  iof_icm_sed(6)   = 1 !bPON3 (g.m-3)
    !  iof_icm_sed(7)   = 1 !bPOP1 (g.m-3)
    !  iof_icm_sed(8)   = 1 !bPOP2 (g.m-3)
    !  iof_icm_sed(9)   = 1 !bPOP3 (g.m-3)
    !  iof_icm_sed(10)  = 1 !bNH4  (g.m-3)
    !  iof_icm_sed(11)  = 1 !bNO3  (g.m-3)
    !  iof_icm_sed(12)  = 1 !bPO4  (g.m-3)
    !  iof_icm_sed(13)  = 1 !bH2S  (g.m-3)
    !  iof_icm_sed(14)  = 1 !bCH4  (g.m-3)
    !  iof_icm_sed(15)  = 1 !bPOS  (g.m-3)
    !  iof_icm_sed(16)  = 1 !bSA   (g.m-3)
    !  iof_icm_sed(17)  = 1 !bstc: surface transfer coeff. (m/day)
    !  iof_icm_sed(18)  = 1 !bSTR: benthic stress      (day)
    !  iof_icm_sed(19)  = 1 !bThp: consective days of hypoxia (day)
    !  iof_icm_sed(20)  = 1 !bTox: consective days of oxic condition after hypoxia (day)
    !  iof_icm_sed(21)  = 1 !SOD   (g.m-2.day-1)
    !  iof_icm_sed(22)  = 1 !JNH4  (g.m-2.day-1)
    !  iof_icm_sed(23)  = 1 !JNO3  (g.m-2.day-1)
    !  iof_icm_sed(24)  = 1 !JPO4  (g.m-2.day-1)
    !  iof_icm_sed(25)  = 1 !JSA   (g.m-2.day-1)
    !  iof_icm_sed(26)  = 1 !JCOD  (g.m-2.day-1)
    !
    !  !Benthic Algae model
    !  iof_icm_ba(1)    = 1 !BA    (g[C].m-2)
    !
    !  !ICM Debug Outputs (need coding, for developers)
    !  iof_icm_dbg(1)   = 1 !2D ICM debug variables
    !  iof_icm_dbg(2)   = 1 !3D ICM debug variables
               
    !-----------------------------------------------------------------------
    ! CoSINE outputs: all 3D
    !-----------------------------------------------------------------------
    !  iof_cos(1)  = 0 !NO3 (uM)
    !  iof_cos(2)  = 0 !SiO4(uM)
    !  iof_cos(3)  = 0 !NH4 (uM)
    !  iof_cos(4)  = 0 !S1  (uM)
    !  iof_cos(5)  = 0 !S2  (uM)
    !  iof_cos(6)  = 0 !Z1  (uM)
    !  iof_cos(7)  = 0 !Z2  (uM)
    !  iof_cos(8)  = 0 !DN  (uM) 
    !  iof_cos(9)  = 0 !DSi (uM) 
    !  iof_cos(10) = 0 !PO4 (uM) 
    !  iof_cos(11) = 0 !DOX (uM) 
    !  iof_cos(12) = 0 !CO2 (uM) 
    !  iof_cos(13) = 0 !ALK (uM) 
    
    !-----------------------------------------------------------------------
    ! Fecal indicating bacteria module
    !-----------------------------------------------------------------------
    !  iof_fib(1) = 0 ! {FIB_1}  3D
    
    !-----------------------------------------------------------------------
    ! Specific outputs in SED2D (USE_SED2D must be on in Makefile;
    ! otherwise these are not needed) - not implemented yet
    !-----------------------------------------------------------------------
    !  iof_sed2d(1)  = 0 !bottom depth _change_ from init. condition (m) {SED2D_depth_change}
    !  iof_sed2d(2)  = 0 !drag coefficient used in transport formulae SED2D_Cd{}
    !  iof_sed2d(3) = 0 !Courant number (b.qtot.dt / h.dx) {SED2D_cflsed}
    !  iof_sed2d(4)    = 0 !Top layer d50 (m) {SED2D_d50}
    !  iof_sed2d(5)   = 0 !total transport rate vector (kg/m/s) {SED2D_total_transport}
    !  iof_sed2d(6)   = 0 !suspended tranport rate vector (kg/m/s) {SED2D_susp_load}
    !  iof_sed2d(7)   = 0 !bedload transport rate vector (kg/m/s) {SED2D_bed_load}
    !  iof_sed2d(8)    = 0 !time averaged total transport rate vector (kg/m/s) {SED2D_average_transport}
    !  iof_sed2d(9)  = 0 !bottom slope vector (m/m); negative uphill {SED2D_bottom_slope}
    !  iof_sed2d(10) = 0 !Total roughness length @elem (m) (z0eq) {z0eq}
    !  iof_sed2d(11) = 0 !current-ripples roughness length @elem (m) (z0cr) {z0cr}
    !  iof_sed2d(12) = 0 !sand-waves roughness length @elem (m) (z0sw) {z0sw}
    !  iof_sed2d(13) = 0 !wave-ripples roughness length @elem (m) (z0wr) {z0wr}
     
    !-----------------------------------------------------------------------
    !  marsh flags (USE_MARSH on)
    !-----------------------------------------------------------------------
    !  iof_marsh(1) = 0 ! {marshFlag}  2D elem
    
    !-----------------------------------------------------------------------
    ! Ice module outputs (if USE_ICE is on)
    !-----------------------------------------------------------------------
    !  iof_ice(1)= 0 !divergence @ elem ('Delta') [1/sec] {iceStrainRate}  2D
    !  iof_ice(2)= 0 !ice advective velcoity vector [m/s] {iceVelocityX,Y}  2D vector
    !  iof_ice(3)= 0 !net heat flux to ocean (>0 warm up SST) [W/m/m] {iceNetHeatFlux}  2D
    !  iof_ice(4)= 0 !net fresh water flux to ocean (>0 freshens up SSS) [kg/s/m/m] {iceFreshwaterFlux}  2D
    !  iof_ice(5)= 0 !ice temperature [C] at air-ice interface {iceTopTemperature}  2D
    
    !  iof_ice(6)= 0 !ice volume [m] {iceTracer_1}   2D
    !  iof_ice(7)= 0 !ice concentration [-] {iceTracer_2}  2D
    !  iof_ice(8)= 0 !snow volume [m] {iceTracer_3}  2D
    
    !-----------------------------------------------------------------------
    ! Analysis module outputs (USE_ANALYSIS)
    !-----------------------------------------------------------------------
    !  iof_ana(1) = 0 !min time step at each element over all subcycles in horizontal transport solver [s]   {minTransportTimeStep}  2D
    !  iof_ana(2) = 0 !x-component of \nabla air_pres /\rho_0 [m/s/s] {airPressureGradientX}  2D
    !  iof_ana(3) = 0 !y-component of \nabla air_pres /\rho_0 [m/s/s] {airPressureGradientY}  2D
    !  iof_ana(4) = 0  !\alpha*g*\nabla \Psi [m/s/s] (gradient of tidal potential) {tidePotentialGradX}  2D
    !  iof_ana(5) = 0  !\alpha*g*\nabla \Psi [m/s/s] {tidePotentialGradY}  2D
    !  iof_ana(6) = 0 !\nabla \cdot (\mu \nabla u) [m/s/s] (horizontal momentum mixing) {horzontalViscosityX}  3D side
    !  iof_ana(7) = 0 !\nabla \cdot (\mu \nabla v) [m/s/s] {horzontalViscosityY}   3D side
    !  iof_ana(8) = 0 !-g/rho0* \int_z^\eta dr_dx dz  [m/s/s] (b-clinic gradient) {baroclinicForceX}  3D side
    !  iof_ana(9) = 0 !-g/rho0* \int_z^\eta dr_dy dz  [m/s/s] {baroclinicForceY}  3D side
    !  iof_ana(10) = 0 !d (\nu du/dz)/dz [m/s/s] - no vegetation effects (vertical momentum mixing) {verticalViscosityX}  3D side
    !  iof_ana(11) = 0 !d (\nu dv/dz)/dz [m/s/s] - no vegetation effects {verticalViscosityY}  3D side
    !  iof_ana(12) = 0 !(u \cdot \nabla) u [m/s/s] (momentum advection) {mommentumAdvectionX}  3D side
    !  iof_ana(13) = 0 !(u \cdot \nabla) u [m/s/s] {mommentumAdvectionY}  3D side
    !  iof_ana(14) = 0 !gradient Richardson number [-] {gradientRichardson}   3D
    /
    
    """
    CORE: CORE = CORE()
    OPT: OPT = OPT()
    VERTICAL: VERTICAL = VERTICAL()
    SCHOUT: SCHOUT = SCHOUT()
