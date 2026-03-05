#!/usr/bin/env python3
"""Generate ADA technique profile building blocks from a data-driven configuration.

Usage:
    python tools/generate_profiles.py            # generate all profiles
    python tools/generate_profiles.py adaSEM     # generate one profile
    python tools/generate_profiles.py --list     # list all profile names
"""

import argparse
import json
import os
import sys
import textwrap
from pathlib import Path


# Standard supporting component types included in every profile's hasPart enum.
# These are the supplement types from the Components worksheet of
# ADA-AnalyticalMethodsAndAttributes.xlsx (isSupplement = 'supplement'),
# plus "other" as a catch-all.
STANDARD_SUPPORTING_TYPES = [
    "analysisLocation", "annotatedImage", "areaOfInterest", "basemap",
    "calibrationFile", "code", "contextPhotography", "contextVideo",
    "inputFile", "instrumentMetadata", "logFile", "methodDescription",
    "other", "plot", "processingMethod", "quickLook", "report",
    "samplePreparation", "shapefile", "supplementalBasemap",
    "supplementaryImage", "worldFile",
]

# ---------------------------------------------------------------------------
# Profile configurations
# ---------------------------------------------------------------------------

PROFILES = {
    "adaARGT": {
        "title": "ADA ARGT Product Profile",
        "full_name": "Argon Geochronology and Thermochronology (ARGT)",
        "short_name": "ARGT",
        "description": "Argon geochronology and thermochronology dating analysis.",
        "termcodes": ["ARGT"],
        "product_types": ["ARGTDocument", "ARGTCollection"],
        "additional_type_labels": [
            "40Ar/39Ar Geochronology and Thermochronology (ARGT)",
            "40Ar/39Ar geochronology and thermochronology",
        ],
        "component_types": [
            "ARGTDocument", "ARGTCollection",
        ],
        "detail": "detailARGT",
        "tags": ["argt", "argon-geochronology"],
    },
    "adaDSC": {
        "title": "ADA DSC Product Profile",
        "full_name": "Differential Scanning Calorimetry (DSC)",
        "short_name": "DSC",
        "description": "Differential scanning calorimetry thermal analysis.",
        "termcodes": ["DSC"],
        "product_types": ["DSCHeatTabular", "DSCResultsTabular"],
        "additional_type_labels": [
            "Differential Scanning Calorimetry (DSC)",
            "Differential Scanning Calorimetry",
        ],
        "component_types": [
            "DSCHeatTabular", "DSCResultsTabular",
        ],
        "detail": "detailDSC",
        "tags": ["dsc", "differential-scanning-calorimetry"],
    },
    "adaEAIRMS": {
        "title": "ADA EA-IRMS Product Profile",
        "full_name": "Elemental Analysis - Isotope Ratio Mass Spectrometry (EA-IRMS)",
        "short_name": "EA-IRMS",
        "description": "Elemental analysis coupled with isotope ratio mass spectrometry.",
        "termcodes": ["EA-IRMS"],
        "product_types": ["EAIRMSCollection"],
        "additional_type_labels": [
            "Elemental Analysis-Isotope Ratio Mass Spectrometry (EA-IRMS)",
            "Elemental analysis - isotope ratio mass spectrometry",
        ],
        "component_types": [
            "EAIRMSCollection",
        ],
        "detail": "detailEAIRMS",
        "tags": ["ea-irms", "elemental-analysis", "isotope-ratio-mass-spectrometry"],
    },
    "adaICPOES": {
        "title": "ADA ICP-OES Product Profile",
        "full_name": "Inductively Coupled Plasma Optical Emission Spectrometry (ICP-OES)",
        "short_name": "ICP-OES",
        "description": "Inductively coupled plasma optical emission spectrometry analysis.",
        "termcodes": ["ICP-OES"],
        "product_types": [
            "ICPOESIntermediateTabular", "ICPOESProcessedTabular",
            "ICPOESRawTabular",
        ],
        "additional_type_labels": [
            "Inductively Coupled Plasma - Optical Emission Spectroscopy (ICPOES) Raw",
            "Inductively Coupled Plasma - Optical Emission Spectroscopy (ICPOES) Intermediate",
            "Inductively Coupled Plasma - Optical Emission Spectroscopy (ICPOES) Processed",
            "Inductively coupled plasma - optical emission spectrometry",
        ],
        "component_types": [
            "ICPOESIntermediateTabular", "ICPOESProcessedTabular",
            "ICPOESRawTabular",
        ],
        "detail": "detailICPOES",
        "tags": ["icp-oes", "inductively-coupled-plasma"],
    },
    "adaL2MS": {
        "title": "ADA L2MS Product Profile",
        "full_name": "Two-Step Laser Mass Spectrometry (L2MS)",
        "short_name": "L2MS",
        "description": "Two-step laser desorption/ionization mass spectrometry.",
        "termcodes": ["uL2MS"],
        "product_types": ["L2MSCube", "L2MSOverviewImage"],
        "additional_type_labels": [
            "Microprobe Two-Step Laser Mass Spectrometry (L2MS)",
            "Microprobe Two-Step Laser Mass Spectrometry",
        ],
        "component_types": [
            "L2MSCube", "L2MSOverviewImage",
        ],
        "detail": "detailL2MS",
        "tags": ["l2ms", "laser-mass-spectrometry"],
    },
    "adaLAF": {
        "title": "ADA LAF Product Profile",
        "full_name": "Laser-Assisted Fluorination (LAF)",
        "short_name": "LAF",
        "description": "Laser-assisted fluorination isotope analysis.",
        "termcodes": ["LAF"],
        "product_types": ["LAFProcessed", "LAFRaw"],
        "additional_type_labels": [
            "Laser Assisted Fluorination (LAF) Processed",
            "Laser Assisted Fluorination (LAF) Raw",
            "Laser Assisted Fluorination",
        ],
        "component_types": [
            "LAFProcessed", "LAFRaw",
        ],
        "detail": "detailLAF",
        "tags": ["laf", "laser-assisted-fluorination"],
    },
    "adaNanoIR": {
        "title": "ADA NanoIR Product Profile",
        "full_name": "Nano-Infrared Spectroscopy (NanoIR)",
        "short_name": "NanoIR",
        "description": "Nano-infrared spectroscopy and photothermal imaging.",
        "termcodes": ["NanoIR"],
        "product_types": [
            "NanoIRBackground", "NanoIRMap",
            "NanoIRMapCollection", "NanoIRPointCollection",
        ],
        "additional_type_labels": [
            "Nanoscale Infrared Mapping (NanoIR) Background",
            "Nanoscale Infrared Mapping (NanoIR) MapCollection",
            "Nanoscale Infrared Mapping (NanoIR) Point Data",
            "Nanoscale Infrared Mapping",
        ],
        "component_types": [
            "NanoIRBackground", "NanoIRMap",
            "NanoIRMapCollection", "NanoIRPointCollection",
        ],
        "detail": "detailNanoIR",
        "tags": ["nanoir", "nano-infrared-spectroscopy"],
    },
    "adaNanoSIMS": {
        "title": "ADA NanoSIMS Product Profile",
        "full_name": "Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS)",
        "short_name": "NanoSIMS",
        "description": "Nanoscale secondary ion mass spectrometry imaging and analysis.",
        "termcodes": ["NanoSIMS"],
        "product_types": [
            "NanoSIMSCollection", "NanoSIMSImageCollection",
            "NanoSIMSTabular", "NanoSIMSMap", "NanoSIMSImage",
        ],
        "additional_type_labels": [
            "Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) Raw",
            "Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) Image",
            "Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) Tabular",
            "Nanoscale secondary ion mass spectrometry",
        ],
        "component_types": [
            "NanoSIMSCollection", "NanoSIMSImageCollection",
            "NanoSIMSTabular", "NanoSIMSMap", "NanoSIMSImage",
        ],
        "detail": "detailNanoSIMS",
        "tags": ["nanosims", "secondary-ion-mass-spectrometry"],
    },
    "adaPSFD": {
        "title": "ADA PSFD Product Profile",
        "full_name": "Particle Size-Frequency Distribution (PSFD)",
        "short_name": "PSFD",
        "description": "Particle size-frequency distribution analysis.",
        "termcodes": ["PSFD"],
        "product_types": ["PSFDTabular"],
        "additional_type_labels": [
            "Particle Size Frequency Distribution (PSFD)",
            "Particle Size Frequency Distribution",
        ],
        "component_types": [
            "PSFDTabular",
        ],
        "detail": "detailPSFD",
        "tags": ["psfd", "particle-size-frequency-distribution"],
    },
    "adaQRIS": {
        "title": "ADA QRIS Product Profile",
        "full_name": "Quantitative Reflectance Imaging Spectroscopy (QRIS)",
        "short_name": "QRIS",
        "description": "Quantitative reflectance imaging spectroscopy.",
        "termcodes": ["QRIS"],
        "product_types": [
            "QRISCalibratedCollection", "QRISRawCollection",
            "QRISCalibrationFile",
        ],
        "additional_type_labels": [
            "Quantitative Reflective Imaging System (QRIS)",
            "Quantitative Reflective Imaging System",
        ],
        "component_types": [
            "QRISCalibratedCollection", "QRISRawCollection",
            "QRISCalibrationFile",
        ],
        "detail": "detailQRIS",
        "tags": ["qris", "reflectance-imaging-spectroscopy"],
    },
    "adaSLS": {
        "title": "ADA SLS Product Profile",
        "full_name": "Structured Light Scanning (SLS)",
        "short_name": "SLS",
        "description": "Structured light scanning for 3D surface reconstruction.",
        "termcodes": ["SLS"],
        "product_types": ["SLSShapeModel", "SLSPartialScan", "ShapeModelImage"],
        "additional_type_labels": [
            "Structured Light Scanning (SLS) Individual Scan Collection",
            "Structured Light Scanning (SLS) Shape Model",
        ],
        "component_types": [
            "SLSShapeModel", "SLSPartialScan", "ShapeModelImage",
        ],
        "detail": "detailSLS",
        "tags": ["sls", "structured-light-scanning"],
    },
    "adaXCT": {
        "title": "ADA XCT Product Profile",
        "full_name": "X-ray Computed Tomography (XCT)",
        "short_name": "XCT",
        "description": "X-ray computed tomography 3D imaging.",
        "termcodes": ["XCT"],
        "product_types": ["XCTImageCollection"],
        "additional_type_labels": [
            "X-ray Computed Tomography (XCT) Image Collection",
            "X-ray computed tomography",
        ],
        "component_types": [
            "XCTImageCollection",
        ],
        "detail": "detailXCT",
        "tags": ["xct", "x-ray-computed-tomography"],
    },
    # --- Techniques WITHOUT detail building blocks ---
    "adaAIVA": {
        "title": "ADA AIVA Product Profile",
        "full_name": "AI-driven Visual Analysis (AIVA)",
        "short_name": "AIVA",
        "description": "AI-driven visual analysis imaging.",
        "termcodes": ["AIVA"],
        "product_types": ["AIVAImage", "AIVAImageCollection"],
        "additional_type_labels": [
            "Advanced Imaging and Visualization of Astromaterials (AIVA)",
            "Advanced Imaging and Visualization of Astromaterials",
        ],
        "component_types": [
            "AIVAImage", "AIVAImageCollection",
        ],
        "detail": None,
        "tags": ["aiva", "ai-visual-analysis"],
    },
    "adaAMS": {
        "title": "ADA AMS Product Profile",
        "full_name": "Accelerator Mass Spectrometry (AMS)",
        "short_name": "AMS",
        "description": "Accelerator mass spectrometry isotope analysis.",
        "termcodes": ["AMS"],
        "product_types": ["AMSRawData", "AMSProcessedData"],
        "additional_type_labels": [
            "Accelerator Mass Spectrometry (AMS)",
            "Accelerator Mass Spectrometry",
        ],
        "component_types": [
            "AMSRawData", "AMSProcessedData",
        ],
        "detail": None,
        "tags": ["ams", "accelerator-mass-spectrometry"],
    },
    "adaFTICRMS": {
        "title": "ADA FTICR-MS Product Profile",
        "full_name": "Fourier Transform Ion Cyclotron Resonance Mass Spectrometry (FTICR-MS)",
        "short_name": "FTICR-MS",
        "description": "Fourier transform ion cyclotron resonance mass spectrometry.",
        "termcodes": ["FTICR-MS"],
        "product_types": ["FTICRMSTabular", "FTICRMSCube"],
        "additional_type_labels": [
            "Fourier Transform Ion Cyclotron Resonance Mass Spectrometry (FTICRMS) Cube",
            "Fourier Transform Ion Cyclotron Resonance Mass Spectrometry (FTICRMS) Tabular",
            "Fourier Transform Ion Cyclotron Resonance Mass Spectrometry",
        ],
        "component_types": [
            "FTICRMSTabular", "FTICRMSCube",
        ],
        "detail": None,
        "tags": ["fticr-ms", "fourier-transform-mass-spectrometry"],
    },
    "adaGCMS": {
        "title": "ADA GC-MS Product Profile",
        "full_name": "Gas Chromatography Mass Spectrometry (GC-MS)",
        "short_name": "GC-MS",
        "description": "Gas chromatography mass spectrometry analysis.",
        "termcodes": ["GC-MS"],
        "product_types": ["GCMSCollection", "GCMSCube", "GCGCMSCollection"],
        "additional_type_labels": [
            "Gas Chromatography-Mass Spectrometry (GCMS)",
            "Gas Chromatography-Mass Spectrometry",
        ],
        "component_types": [
            "GCMSCollection", "GCMSCube", "GCGCMSCollection",
        ],
        "detail": None,
        "tags": ["gc-ms", "gas-chromatography-mass-spectrometry"],
    },
    "adaGPYC": {
        "title": "ADA GPYC Product Profile",
        "full_name": "Gas Pycnometry (GPYC)",
        "short_name": "GPYC",
        "description": "Gas pycnometry density measurement.",
        "termcodes": ["GPYC"],
        "product_types": ["GPYCProcessedTabular", "GPYCRawTabular"],
        "additional_type_labels": [
            "Gas Pycnometry (GPYC) Processed",
            "Gas Pycnometry (GPYC) Raw",
            "Gas pycnometry",
        ],
        "component_types": [
            "GPYCProcessedTabular", "GPYCRawTabular",
        ],
        "detail": None,
        "tags": ["gpyc", "gas-pycnometry"],
    },
    "adaIC": {
        "title": "ADA IC Product Profile",
        "full_name": "Ion Chromatography (IC)",
        "short_name": "IC",
        "description": "Ion chromatography analysis.",
        "termcodes": ["IC"],
        "product_types": ["ICTabular"],
        "additional_type_labels": [
            "Ion Chromatography (IC)",
            "Ion Chromatography",
        ],
        "component_types": [
            "ICTabular",
        ],
        "detail": None,
        "tags": ["ic", "ion-chromatography"],
    },
    "adaLCMS": {
        "title": "ADA LC-MS Product Profile",
        "full_name": "Liquid Chromatography Mass Spectrometry (LC-MS)",
        "short_name": "LC-MS",
        "description": "Liquid chromatography mass spectrometry analysis.",
        "termcodes": ["LC-MS"],
        "product_types": ["LCMSCollection", "LCMSMSCollection"],
        "additional_type_labels": [
            "Liquid Chromatography - Mass Spectrometry (LCMS) Collection",
            "Liquid chromatography-mass spectrometry",
        ],
        "component_types": [
            "LCMSCollection", "LCMSMSCollection",
        ],
        "detail": None,
        "tags": ["lc-ms", "liquid-chromatography-mass-spectrometry"],
    },
    "adaLIT": {
        "title": "ADA LIT Product Profile",
        "full_name": "Lock-In Thermography (LIT)",
        "short_name": "LIT",
        "description": "Lock-in thermography imaging and data collection.",
        "termcodes": ["LIT"],
        "product_types": ["LITImage", "LIT2DDataCollection", "LITPolarDataCollection"],
        "additional_type_labels": [
            "Lock-In Thermography (LIT) image",
            "Lock-In Thermography (LIT) Collection",
            "Lock-In Thermography",
        ],
        "component_types": [
            "LITImage", "LIT2DDataCollection", "LITPolarDataCollection",
        ],
        "detail": None,
        "tags": ["lit", "lock-in-thermography"],
    },
    "adaNGNSMS": {
        "title": "ADA NG-NS-MS Product Profile",
        "full_name": "Noble Gas and Nitrogen Static Mass Spectrometry (NG-NS-MS)",
        "short_name": "NG-NS-MS",
        "description": "Noble gas and nitrogen static mass spectrometry analysis.",
        "termcodes": ["NG-NS-MS"],
        "product_types": ["NGNSMSRaw", "NGNSMSProcessed"],
        "additional_type_labels": [
            "Noble Gas and Nitrogen Static Mass Spectrometry (NGNSMS) Processed",
            "Noble Gas and Nitrogen Static Mass Spectrometry (NGNSMS) Raw",
            "Noble gas and Nitrogen Static Mass Spectrometry",
        ],
        "component_types": [
            "NGNSMSRaw", "NGNSMSProcessed",
        ],
        "detail": None,
        "tags": ["ng-ns-ms", "noble-gas-mass-spectrometry"],
    },
    "adaRAMAN": {
        "title": "ADA RAMAN Product Profile",
        "full_name": "Raman Spectroscopy (RAMAN)",
        "short_name": "RAMAN",
        "description": "Raman spectroscopy vibrational analysis.",
        "termcodes": ["RAMAN"],
        "product_types": ["RAMANRawTabular"],
        "additional_type_labels": [
            "Raman vibrational spectroscopy",
        ],
        "component_types": [
            "RAMANRawTabular",
        ],
        "detail": None,
        "tags": ["raman", "raman-spectroscopy"],
    },
    "adaRITOFNGMS": {
        "title": "ADA RI-TOF-NGMS Product Profile",
        "full_name": "Resonance Ionization Time-of-Flight Noble Gas Mass Spectrometry (RI-TOF-NGMS)",
        "short_name": "RI-TOF-NGMS",
        "description": "Resonance ionization time-of-flight noble gas mass spectrometry.",
        "termcodes": ["RI-TOF-NGMS"],
        "product_types": ["RITOFNGMSTabular", "RITOFNGMSCollection"],
        "additional_type_labels": [
            "Resonance ionization time of flight noble gas mass spectrometry (RITOFNGMS) Spectra",
            "Resonance ionization time of flight noble gas mass spectrometry (RITOFNGMS) Processed",
            "Resonance ionization time of flight noble gas mass spectrometry",
        ],
        "component_types": [
            "RITOFNGMSTabular", "RITOFNGMSCollection",
        ],
        "detail": None,
        "tags": ["ri-tof-ngms", "resonance-ionization-tof"],
    },
    "adaSEM": {
        "title": "ADA SEM Product Profile",
        "full_name": "Scanning Electron Microscopy (SEM)",
        "short_name": "SEM",
        "description": "Scanning electron microscopy imaging and analysis.",
        "termcodes": ["SEM", "FIB-SEM"],
        "product_types": [
            "SEMImageCollection", "SEMImageMap",
            "SEMEBSDGrainImage", "SEMEBSDGrainImageMap",
            "SEMEBSDGrainImageMapCube",
            "SEMEDSElementalMap", "SEMEDSElementalMaps",
            "SEMEDSElementalMapsCube",
            "SEMEDSPointData", "SEMEDSPointDataCollection",
            "SEMEDSPointDataCube",
            "SEMHRCLImage", "SEMHRCLMap", "SEMHRCLCube",
        ],
        "additional_type_labels": [
            "Scanning Electron Microscopy (SEM) Image",
            "Scanning Electron Microscopy Electron Backscatter Diffraction (SEMEBSD) Grain Image",
            "Scanning Electron Microscopy Energy Dispersive X-ray Spectroscopy (SEMEDS) image",
            "Scanning Electron Microscopy Energy Dispersive X-ray Spectroscopy (SEMEDS) Point Data",
            "Scanning Electron Microscopy High Resolution Cathodoluminescence (SEMHRCL) image",
            "Scanning electron microscopy",
        ],
        "component_types": [
            "SEMImageCollection", "SEMImageMap",
            "SEMEBSDGrainImage", "SEMEBSDGrainImageMap",
            "SEMEBSDGrainImageMapCube",
            "SEMEDSElementalMap", "SEMEDSElementalMaps",
            "SEMEDSElementalMapsCube",
            "SEMEDSPointData", "SEMEDSPointDataCollection",
            "SEMEDSPointDataCube",
            "SEMHRCLImage", "SEMHRCLMap", "SEMHRCLCube",
        ],
        "detail": None,
        "tags": ["sem", "scanning-electron-microscopy"],
    },
    "adaSIMS": {
        "title": "ADA SIMS Product Profile",
        "full_name": "Secondary Ion Mass Spectrometry (SIMS)",
        "short_name": "SIMS",
        "description": "Secondary ion mass spectrometry analysis.",
        "termcodes": ["SIMS"],
        "product_types": ["SIMSTabular", "SIMSCollection"],
        "additional_type_labels": [
            "Secondary Ion Mass Spectrometry (SIMS) Tabular",
            "Secondary ion mass spectrometry",
        ],
        "component_types": [
            "SIMSTabular", "SIMSCollection",
        ],
        "detail": None,
        "tags": ["sims", "secondary-ion-mass-spectrometry"],
    },
    "adaSVRUEC": {
        "title": "ADA SV-RUEC Product Profile",
        "full_name": "Seismic Velocities and Rock Ultrasonic Elastic Constants (SV-RUEC)",
        "short_name": "SV-RUEC",
        "description": "Seismic velocities and rock ultrasonic elastic constants measurement.",
        "termcodes": ["SV-RUEC"],
        "product_types": ["SVRUECTabular"],
        "additional_type_labels": [
            "Seismic Velocities and Rock Ultrasonic Elastic Constants (SVRUEC)",
            "Seismic Velocities and Rock Ultrasonic Elastic Constants",
        ],
        "component_types": [
            "SVRUECTabular",
        ],
        "detail": None,
        "tags": ["sv-ruec", "seismic-velocities"],
    },
    "adaTEM": {
        "title": "ADA TEM Product Profile",
        "full_name": "Transmission Electron Microscopy (TEM)",
        "short_name": "TEM",
        "description": "Transmission electron microscopy imaging and spectroscopy.",
        "termcodes": ["TEM"],
        "product_types": [
            "TEMImage", "TEMPatternsImage", "TEMEDSImageCollection",
            "STEMImage", "STEMEDSTabular", "STEMEDSCube",
            "STEMEDSTomo", "STEMEELSTabular", "STEMEELSCube",
        ],
        "additional_type_labels": [
            "Transmission Electron Microscopy (TEM) Image",
            "Transmission Electron Microscopy (TEM) Patterns Image",
            "Scanning Transmission Electron Microscopy (STEM) Image",
            "Scanning Transmission Electron Microscopy Energy Dispersive X-ray Spectroscopy (STEMEDS) Cube",
            "Scanning Transmission Electron Microscopy Energy Dispersive X-ray Spectroscopy (STEMEDS) Tabular",
            "Scanning Transmission Electron Microscopy Energy Dispersive X-ray Spectroscopy (STEMEDS) Tomography",
            "Scanning Transmission Electron Microscopy Electron Energy-loss Spectra (STEMEELS) Cube",
            "Scanning Transmission Electron Microscopy Electron Energy-loss Spectra (STEMEELS) Tabular",
            "Transmission Electron Microscopy",
        ],
        "component_types": [
            "TEMImage", "TEMPatternsImage", "TEMEDSImageCollection",
            "STEMImage", "STEMEDSTabular", "STEMEDSCube",
            "STEMEDSTomo", "STEMEELSTabular", "STEMEELSCube",
        ],
        "detail": None,
        "tags": ["tem", "transmission-electron-microscopy"],
    },
    "adaToFSIMS": {
        "title": "ADA ToF-SIMS Product Profile",
        "full_name": "Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS)",
        "short_name": "ToF-SIMS",
        "description": "Time-of-flight secondary ion mass spectrometry surface analysis.",
        "termcodes": ["ToF-SIMS"],
        "product_types": ["TOFSIMSCollection"],
        "additional_type_labels": [
            "Time-of-flight secondary ion mass spectrometry (TOFSIMS)",
            "Time-of-Flight Secondary Ion Mass Spectrometry",
        ],
        "component_types": [
            "TOFSIMSCollection",
        ],
        "detail": None,
        "tags": ["tof-sims", "time-of-flight-sims"],
    },
    "adaUVFM": {
        "title": "ADA UVFM Product Profile",
        "full_name": "Ultraviolet Fluorescence Microscopy (UVFM)",
        "short_name": "UVFM",
        "description": "Ultraviolet fluorescence microscopy imaging.",
        "termcodes": ["UVFM"],
        "product_types": ["UVFMImage", "UVFMImageCollection"],
        "additional_type_labels": [
            "Fluorescence Microscopy (UVFM) Image",
            "UV Fluorescence Microscopy",
        ],
        "component_types": [
            "UVFMImage", "UVFMImageCollection",
        ],
        "detail": None,
        "tags": ["uvfm", "ultraviolet-fluorescence-microscopy"],
    },
    "adaVLM": {
        "title": "ADA VLM Product Profile",
        "full_name": "Visible Light Microscopy (VLM)",
        "short_name": "VLM",
        "description": "Visible light microscopy imaging.",
        "termcodes": ["VLM", "VLMBasemap"],
        "product_types": ["VLMImage", "VLMImageCollection"],
        "additional_type_labels": [
            "Visible Light Microscopy (VLM) Image",
            "Basemap",
            "Visible Light Microscopy",
        ],
        "component_types": [
            "VLMImage", "VLMImageCollection",
        ],
        "detail": None,
        "tags": ["vlm", "visible-light-microscopy"],
    },
    "adaXANES": {
        "title": "ADA XANES Product Profile",
        "full_name": "X-ray Absorption Near Edge Structure (XANES)",
        "short_name": "XANES",
        "description": "X-ray absorption near edge structure spectroscopy.",
        "termcodes": ["XANES"],
        "product_types": [
            "XANESImageStack", "XANESStackOverviewImage",
            "XANESRawTabular", "XANESProcessedTabular",
            "XANESimage", "XANESCollection",
        ],
        "additional_type_labels": [
            "X-ray Absorption Near Edge Structure Hyperspectral Image Stack (XANES)",
            "X-ray absorption near edge structure (XANES) spectroscopy",
        ],
        "component_types": [
            "XANESImageStack", "XANESStackOverviewImage",
            "XANESRawTabular", "XANESProcessedTabular",
            "XANESimage", "XANESCollection",
        ],
        "detail": None,
        "tags": ["xanes", "x-ray-absorption-spectroscopy"],
    },
}


# ---------------------------------------------------------------------------
# Template generators
# ---------------------------------------------------------------------------

def _generate_schema_yaml(cfg: dict) -> str:
    """Generate schema.yaml content for a profile."""
    product_types = cfg["product_types"]
    labels = cfg.get("additional_type_labels", [])

    # Build the full list of accepted additionalType values:
    # human-readable product type names + technique labels (no ada: prefixes)
    all_values = labels

    # additionalType constraint: const for single, enum for multiple
    if len(all_values) == 1:
        contains_block = f'          const: "{all_values[0]}"'
    else:
        lines = [f'            - "{v}"' for v in all_values]
        contains_block = "          enum:\n" + "\n".join(lines)

    # Build technique-specific componentType enum lines (no universal types)
    # Indentation for distribution-level (inside oneOf branch)
    technique_ct_lines = "\n".join(
        f'                            - "ada:{ct}"' for ct in cfg["component_types"]
    )

    # Indentation for hasPart-level (deeper nesting in second oneOf branch)
    haspart_ct_lines = "\n".join(
        f'                                  - "ada:{ct}"' for ct in cfg["component_types"]
    )

    detail_note = ""
    if cfg["detail"]:
        detail_note = f" and {cfg['detail']} requirements"

    return f"""$schema: https://json-schema.org/draft/2020-12/schema
title: {cfg['title']}
description: >-
  Technique-specific profile for {cfg['full_name']} products.
  Extends the base ADA product profile with constraints on valid {cfg['short_name']} component
  types{detail_note}.
allOf:
  - $ref: ../adaProduct/schema.yaml
  - type: object
    properties:
      "schema:additionalType":
        description: >-
          Must include a {cfg['short_name']} product type identifier.
        contains:
{contains_block}
      "schema:distribution":
        items:
          oneOf:
            - required:
                - componentType
              properties:
                componentType:
                  anyOf:
                    - properties:
                        "@type":
                          enum:
{technique_ct_lines}
                    - $ref: ../adaProduct/schema.yaml#/$defs/universalComponentType
            - required:
                - "schema:hasPart"
              properties:
                "schema:hasPart":
                  items:
                    properties:
                      componentType:
                        anyOf:
                          - properties:
                              "@type":
                                enum:
{haspart_ct_lines}
                          - $ref: ../adaProduct/schema.yaml#/$defs/universalComponentType
"""


def _generate_bblock_json(cfg: dict) -> str:
    """Generate bblock.json content for a profile."""
    tags = ["ada", "astromat"] + cfg["tags"] + ["profile"]
    bblock = {
        "$schema": "metaschema.yaml",
        "name": cfg["title"].replace(" Product Profile", " Profile"),
        "abstract": f"Technique-specific profile for {cfg['full_name']} products",
        "status": "under-development",
        "dateTimeAddition": "2026-02-12T00:00:00Z",
        "itemClass": "schema",
        "register": "cdif-building-block-register",
        "version": "0.1",
        "dateOfLastChange": "2026-02-12",
        "link": "https://github.com/usgin/geochemBuildingBlocks",
        "maturity": "draft",
        "scope": "unstable",
        "tags": tags,
        "sources": [
            {
                "title": "ADA Metadata Schema v3",
                "link": "https://github.com/amds-ldeo/metadata",
            }
        ],
    }
    return json.dumps(bblock, indent=2) + "\n"


def _generate_context_jsonld() -> str:
    """Generate context.jsonld (identical for all ADA profiles)."""
    ctx = {
        "@context": {
            "schema": "http://schema.org/",
            "ada": "https://ada.astromat.org/metadata/",
            "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
            "csvw": "http://www.w3.org/ns/csvw#",
            "prov": "http://www.w3.org/ns/prov#",
            "spdx": "http://spdx.org/rdf/terms#",
            "nxs": "http://purl.org/nexusformat/definitions/",
            "dcterms": "http://purl.org/dc/terms/",
            "geosparql": "http://www.opengis.net/ont/geosparql#",
        }
    }
    return json.dumps(ctx, indent=2) + "\n"


def _generate_description_md(cfg: dict) -> str:
    """Generate description.md content for a profile."""
    profile_name = cfg["title"].replace(" Product Profile", " Profile")
    pt_lines = "\n".join(
        f"- `ada:{pt}`" for pt in cfg["product_types"]
    )
    ct_all = list(cfg["component_types"]) + STANDARD_SUPPORTING_TYPES
    ct_lines = "\n".join(f"- `ada:{ct}`" for ct in ct_all)

    detail_section = ""
    if cfg["detail"]:
        detail_section = f"\n## Detail Type\n`{cfg['detail']}`\n"

    return f"""# {profile_name}

Technique-specific metadata profile for {cfg['full_name']} products in the Astromat Data Archive. {cfg['description']}

## Product Types
{pt_lines}

## Valid Component Types
{ct_lines}
{detail_section}"""


def _generate_rules_shacl(cfg: dict) -> str:
    """Generate rules.shacl content for a technique profile.

    Produces a SHACL shapes graph that:
    - Inherits all base validation from adaProduct rules.shacl
    - Constrains schema:additionalType to the technique's allowed values
    """
    short = cfg["short_name"]
    # Shape name: lowercase short name with hyphens removed
    short_lower = short.replace("-", "").replace(" ", "").lower()
    labels = cfg.get("additional_type_labels", [])
    all_values = labels

    # Build sh:or list for additionalType hasValue alternatives
    or_entries = []
    for val in all_values:
        or_entries.append(f'        [sh:hasValue "{val}"]')

    or_block = "\n".join(or_entries)

    return f"""@prefix rdf:         <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:        <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sh:          <http://www.w3.org/ns/shacl#> .
@prefix xsd:         <http://www.w3.org/2001/XMLSchema#> .
@prefix schema:      <http://schema.org/> .
@prefix ada:         <https://ada.astromat.org/metadata/> .
@prefix cdifd: <https://cdif.org/validation/0.1/shacl#> .
@base <https://www.ogc.org/rules/template/> .

# {short} technique profile SHACL rules.
# Base product validation (creator, distribution, wasGeneratedBy, etc.)
# is inherited from adaProduct rules.shacl.
# This shape constrains schema:additionalType to valid {short} values.

cdifd:{short_lower}ProductShape
    a sh:NodeShape ;
    sh:target [
        a sh:SPARQLTarget ;
        sh:select \"\"\"
            PREFIX schema: <http://schema.org/>
            SELECT ?this
            WHERE {{
                ?this a schema:Dataset .
                ?this a schema:Product .
                MINUS {{
                    ?parent a schema:Dataset .
                    ?parent ?p ?this .
                    FILTER (?parent != ?this)
                    FILTER (?p != schema:about)
                }}
            }}
        \"\"\" ;
    ] ;
    sh:property [
        sh:path schema:additionalType ;
        sh:qualifiedMinCount 1 ;
        sh:qualifiedValueShape [
            sh:or (
{or_block}
            )
        ] ;
        sh:message "{short} products must have at least one schema:additionalType matching a valid {short} type." ;
    ] ;
    sh:message "{short} technique profile: additionalType must identify a valid {short} product type." ;
    .
"""


def _generate_examples_yaml(cfg: dict, profile_name: str) -> str:
    """Generate examples.yaml content for a profile."""
    short = cfg["short_name"]
    return f"""- title: {short} Product Example
  content: |-
    Example {cfg['full_name']} product metadata with all properties populated.
    Mock data for validation and testing.
  prefixes:
    schema: http://schema.org/
    ada: https://ada.astromat.org/metadata/
    cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
    prov: http://www.w3.org/ns/prov#
    dcterms: http://purl.org/dc/terms/
  snippets:
    - language: json
      ref: example{profile_name}.json
"""


# ---------------------------------------------------------------------------
# Main generation logic
# ---------------------------------------------------------------------------

def generate_profile(name: str, cfg: dict, base_dir: Path) -> None:
    """Generate all files for a single profile."""
    profile_dir = base_dir / "_sources" / "profiles" / "adaProfiles" / name
    profile_dir.mkdir(parents=True, exist_ok=True)

    files = {
        "schema.yaml": _generate_schema_yaml(cfg),
        "bblock.json": _generate_bblock_json(cfg),
        "context.jsonld": _generate_context_jsonld(),
        "description.md": _generate_description_md(cfg),
        "examples.yaml": _generate_examples_yaml(cfg, name),
        "rules.shacl": _generate_rules_shacl(cfg),
    }

    for filename, content in files.items():
        filepath = profile_dir / filename
        filepath.write_text(content, encoding="utf-8")

    print(f"  Generated {name}/ ({len(files)} files)")


def main():
    parser = argparse.ArgumentParser(
        description="Generate ADA technique profile building blocks"
    )
    parser.add_argument(
        "profiles",
        nargs="*",
        help="Profile names to generate (default: all)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all available profile names",
    )
    parser.add_argument(
        "--base-dir",
        type=Path,
        default=None,
        help="Base directory (default: parent of tools/)",
    )
    args = parser.parse_args()

    if args.list:
        for name in sorted(PROFILES.keys()):
            tc = ", ".join(PROFILES[name]["termcodes"])
            detail = PROFILES[name]["detail"] or "(none)"
            print(f"  {name:20s}  termcodes={tc:15s}  detail={detail}")
        return

    base_dir = args.base_dir or Path(__file__).resolve().parent.parent

    if args.profiles:
        to_generate = {}
        for name in args.profiles:
            if name not in PROFILES:
                print(f"ERROR: Unknown profile '{name}'", file=sys.stderr)
                print(f"Available: {', '.join(sorted(PROFILES.keys()))}", file=sys.stderr)
                sys.exit(1)
            to_generate[name] = PROFILES[name]
    else:
        to_generate = PROFILES

    print(f"Generating {len(to_generate)} profile(s) in {base_dir}/_sources/profiles/adaProfiles/")
    for name, cfg in sorted(to_generate.items()):
        generate_profile(name, cfg, base_dir)
    print("Done.")


if __name__ == "__main__":
    main()
