
# VNMIR Instrument Detail (Schema)

`ada.bbr.metadata.adaProperties.detailVNMIR` *v0.1*

Very-Near Mid-IR spectroscopy with detailed measurement parameters. Defines properties: @type, detector, beamsplitter, calibrationStandards, comments, numberOfScans, eMaxFitRegionMax, eMaxFitRegionMin, emissionAngle, emissivityMaximum, environmentalPressure, incidenceAngle, measurement, measurementEnvironment, phaseAngle, sampleHeated, samplePreparation, sampleTemperature, spectralRangeMax, spectralRangeMin, spectralResolution, spectralSampling, spotSize, uncertaintyNoise, vacuumExposedSample.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# VNMIR Instrument Detail

Very-Near Mid-IR spectroscopy with detailed measurement parameters.

## Examples

### VNMIR Instrument Detail Example
Very-Near Mid-IR spectroscopy spectral point measurement with detailed parameters.
#### json
```json
{
  "@type": "ada:VNMIRSpectralPoint",
  "detector": "MCT",
  "beamsplitter": "KBr",
  "calibrationStandards": "gold mirror",
  "numberOfScans": 256,
  "spectralRangeMin": "400",
  "spectralRangeMax": "4000",
  "spectralResolution": "4 cm-1",
  "spectralSampling": "2 cm-1",
  "spotSize": "100 micrometer",
  "measurement": "reflectance",
  "measurementEnvironment": "ambient",
  "environmentalPressure": 1013.25,
  "sampleHeated": false,
  "sampleTemperature": 25,
  "vacuumExposedSample": false,
  "emissionAngle": 0.0,
  "incidenceAngle": 30.0,
  "phaseAngle": 30.0,
  "uncertaintyNoise": 0.002
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailVNMIR/context.jsonld"
  ],
  "@type": "ada:VNMIRSpectralPoint",
  "detector": "MCT",
  "beamsplitter": "KBr",
  "calibrationStandards": "gold mirror",
  "numberOfScans": 256,
  "spectralRangeMin": "400",
  "spectralRangeMax": "4000",
  "spectralResolution": "4 cm-1",
  "spectralSampling": "2 cm-1",
  "spotSize": "100 micrometer",
  "measurement": "reflectance",
  "measurementEnvironment": "ambient",
  "environmentalPressure": 1013.25,
  "sampleHeated": false,
  "sampleTemperature": 25,
  "vacuumExposedSample": false,
  "emissionAngle": 0.0,
  "incidenceAngle": 30.0,
  "phaseAngle": 30.0,
  "uncertaintyNoise": 0.002
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .

[] a ada:VNMIRSpectralPoint .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: VNMIR Instrument Detail
description: Very-Near Mid-IR spectroscopy with detailed measurement parameters
type: object
properties:
  '@type':
    anyOf:
    - const: ada:VNMIRSpectralPoint
    - const: ada:VNMIROverviewImage
    - const: ada:VNMIRSpectralMap
  detector:
    type: string
  beamsplitter:
    type: string
  calibrationStandards:
    type: string
  comments:
    type: string
  numberOfScans:
    type: integer
  eMaxFitRegionMax:
    type: string
  eMaxFitRegionMin:
    type: string
  emissionAngle:
    type: number
  emissivityMaximum:
    type: string
  environmentalPressure:
    type: number
  incidenceAngle:
    type: number
  measurement:
    type: string
  measurementEnvironment:
    type: string
  phaseAngle:
    type: number
  sampleHeated:
    type: boolean
  samplePreparation:
    type: string
  sampleTemperature:
    type: integer
  spectralRangeMax:
    type: string
  spectralRangeMin:
    type: string
  spectralResolution:
    type: string
  spectralSampling:
    type: string
  spotSize:
    type: string
  uncertaintyNoise:
    type: number
  vacuumExposedSample:
    type: boolean
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailVNMIR/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailVNMIR/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailVNMIR/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/adaProperties/detailVNMIR`

