
# Instrument Detail Types (Schema)

`ada.bbr.metadata.geochemProperties.details` *v0.1*

Instrument-specific detail types for ADA analytical techniques. Defines types: detailBasemap, detailARGT, detailDSC, detailEMPA, detailEAIRMS, detailICPOES, detailL2MS, detailLAF, detailNanoIR, detailNanoSIMS, detailPSFD, detailVNMIR, detailQRIS, detailSLS, detailXCT, detailXRD. Uses building blocks: detailBasemap (geochemProperties), detailARGT (geochemProperties), detailDSC (geochemProperties), detailEMPA (geochemProperties), detailEAIRMS (geochemProperties), detailICPOES (geochemProperties), detailL2MS (geochemProperties), detailLAF (geochemProperties), detailNanoIR (geochemProperties), detailNanoSIMS (geochemProperties), detailPSFD (geochemProperties), detailVNMIR (geochemProperties), detailQRIS (geochemProperties), detailSLS (geochemProperties), detailXCT (geochemProperties), detailXRD (geochemProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Instrument Detail Types

Umbrella schema referencing all instrument-specific detail type building blocks. Individual detail types are now separate building blocks under `geochemProperties/detailXxx/`:

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

## Examples

### Instrument Detail Types Example
The details building block is an umbrella schema. See individual detail type examples
(detailARGT, detailBasemap, detailDSC, etc.) for specific instances.
Below is an example of a basemap detail as one representative member.
#### json
```json
{
  "@type": ["ada:basemap", "schema:Map"],
  "schema:description": "BSE overview basemap",
  "ada:pixelUnits": "micrometer",
  "ada:pixelScaleX": 0.25,
  "ada:pixelScaleY": 0.25,
  "ada:channel1": "BSE"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/details/context.jsonld"
  ],
  "@type": [
    "ada:basemap",
    "schema:Map"
  ],
  "schema:description": "BSE overview basemap",
  "ada:pixelUnits": "micrometer",
  "ada:pixelScaleX": 0.25,
  "ada:pixelScaleY": 0.25,
  "ada:channel1": "BSE"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a schema1:Map,
        ada:basemap ;
    schema1:description "BSE overview basemap" ;
    ada:channel1 "BSE" ;
    ada:pixelScaleX 2.5e-01 ;
    ada:pixelScaleY 2.5e-01 ;
    ada:pixelUnits "micrometer" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Instrument Detail Types
description: Umbrella schema referencing all instrument-specific detail type building
  blocks. Individual detail types are now separate building blocks under geochemProperties/detailXxx/.
type: object
anyOf:
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailBasemap/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailARGT/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailDSC/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailEMPA/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailEAIRMS/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailICPOES/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailL2MS/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailLAF/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailNanoIR/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailNanoSIMS/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailPSFD/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailVNMIR/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailQRIS/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailSLS/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailXCT/schema.yaml
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailXRD/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/details/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/details/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/details/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/details`

