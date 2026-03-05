
# Instrument Detail Types (Schema)

`ada.bbr.metadata.adaProperties.details` *v0.1*

Instrument-specific detail types for ADA analytical techniques. Defines types: detailBasemap, detailARGT, detailDSC, detailEMPA, detailEAIRMS, detailICPOES, detailL2MS, detailLAF, detailNanoIR, detailNanoSIMS, detailPSFD, detailVNMIR, detailQRIS, detailSLS, detailXCT, detailXRD. Uses building blocks: detailBasemap (adaProperties), detailARGT (adaProperties), detailDSC (adaProperties), detailEMPA (adaProperties), detailEAIRMS (adaProperties), detailICPOES (adaProperties), detailL2MS (adaProperties), detailLAF (adaProperties), detailNanoIR (adaProperties), detailNanoSIMS (adaProperties), detailPSFD (adaProperties), detailVNMIR (adaProperties), detailQRIS (adaProperties), detailSLS (adaProperties), detailXCT (adaProperties), detailXRD (adaProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Instrument Detail Types

Umbrella schema referencing all instrument-specific detail type building blocks. Individual detail types are now separate building blocks under `adaProperties/detailXxx/`:

- **detailARGT** - ARGT (Argon) document type with phase and isotope analysis
- **detailBasemap** - Basemap images with RGB channels and pixel scaling
- **detailDSC** - Differential Scanning Calorimetry heat tabular data
- **detailEAIRMS** - Elemental Analysis Isotope Ratio Mass Spectrometry collection
- **detailEMPA** - Electron Microprobe Analysis with spectrometer and signal details
- **detailICPOES** - Inductively Coupled Plasma Optical Emission Spectrometry
- **detailL2MS** - Laser-2 Mass Spectrometry cube data with ionization parameters
- **detailLAF** - Laser Ablation Fluorescence processed/raw data
- **detailNanoIR** - Nano-IR spectroscopy collections with phase analysis
- **detailNanoSIMS** - Nano Secondary Ion Mass Spectrometry with isotope tracking
- **detailPSFD** - Point Spread Function Data with image names and conditions
- **detailQRIS** - QRIS (Raman) with calibration and illumination parameters
- **detailSLS** - Structured Light Scanning shape models and partial scans
- **detailVNMIR** - Very-Near Mid-IR spectroscopy with detailed measurement parameters
- **detailXCT** - X-ray Computed Tomography images with detailed scan parameters
- **detailXRD** - X-ray Diffraction tabular data with geometry and wavelength

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Instrument Detail Types
description: Umbrella schema referencing all instrument-specific detail type building
  blocks. Individual detail types are now separate building blocks under adaProperties/detailXxx/.
type: object
anyOf:
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailBasemap/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailARGT/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailDSC/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailEMPA/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailEAIRMS/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailICPOES/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailL2MS/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailLAF/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailNanoIR/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailNanoSIMS/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailPSFD/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailVNMIR/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailQRIS/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailSLS/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailXCT/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailXRD/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/details/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/details/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/details/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/adaProperties/details`

