
# VNMIR Instrument Detail (Schema)

`ada.bbr.metadata.geochemProperties.detailVNMIR` *v0.1*

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
  "@type": ["ada:VNMIRSpectralPoint"],
  "ada:detector": "MCT",
  "ada:beamsplitter": "KBr",
  "ada:calibrationStandards": "gold mirror",
  "ada:numberOfScans": 256,
  "ada:spectralRangeMin": "400",
  "ada:spectralRangeMax": "4000",
  "ada:spectralResolution": "4 cm-1",
  "ada:spectralSampling": "2 cm-1",
  "ada:spotSize": "100 micrometer",
  "ada:measurement": "reflectance",
  "ada:measurementEnvironment": "ambient",
  "ada:environmentalPressure": 1013.25,
  "ada:sampleHeated": false,
  "ada:sampleTemperature": 25,
  "ada:vacuumExposedSample": false,
  "ada:emissionAngle": 0.0,
  "ada:incidenceAngle": 30.0,
  "ada:phaseAngle": 30.0,
  "ada:uncertaintyNoise": 0.002
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailVNMIR/context.jsonld"
  ],
  "@type": [
    "ada:VNMIRSpectralPoint"
  ],
  "ada:detector": "MCT",
  "ada:beamsplitter": "KBr",
  "ada:calibrationStandards": "gold mirror",
  "ada:numberOfScans": 256,
  "ada:spectralRangeMin": "400",
  "ada:spectralRangeMax": "4000",
  "ada:spectralResolution": "4 cm-1",
  "ada:spectralSampling": "2 cm-1",
  "ada:spotSize": "100 micrometer",
  "ada:measurement": "reflectance",
  "ada:measurementEnvironment": "ambient",
  "ada:environmentalPressure": 1013.25,
  "ada:sampleHeated": false,
  "ada:sampleTemperature": 25,
  "ada:vacuumExposedSample": false,
  "ada:emissionAngle": 0.0,
  "ada:incidenceAngle": 30.0,
  "ada:phaseAngle": 30.0,
  "ada:uncertaintyNoise": 0.002
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a ada:VNMIRSpectralPoint ;
    ada:beamsplitter "KBr" ;
    ada:calibrationStandards "gold mirror" ;
    ada:detector "MCT" ;
    ada:emissionAngle 0e+00 ;
    ada:environmentalPressure 1.01325e+03 ;
    ada:incidenceAngle 3e+01 ;
    ada:measurement "reflectance" ;
    ada:measurementEnvironment "ambient" ;
    ada:numberOfScans 256 ;
    ada:phaseAngle 3e+01 ;
    ada:sampleHeated false ;
    ada:sampleTemperature 25 ;
    ada:spectralRangeMax "4000" ;
    ada:spectralRangeMin "400" ;
    ada:spectralResolution "4 cm-1" ;
    ada:spectralSampling "2 cm-1" ;
    ada:spotSize "100 micrometer" ;
    ada:uncertaintyNoise 2e-03 ;
    ada:vacuumExposedSample false .


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
  ada:detector:
    type: string
  ada:beamsplitter:
    type: string
  ada:calibrationStandards:
    type: string
  ada:comments:
    type: string
  ada:numberOfScans:
    type: integer
  ada:eMaxFitRegionMax:
    type: string
  ada:eMaxFitRegionMin:
    type: string
  ada:emissionAngle:
    type: number
  ada:emissivityMaximum:
    type: string
  ada:environmentalPressure:
    type: number
  ada:incidenceAngle:
    type: number
  ada:measurement:
    type: string
  ada:measurementEnvironment:
    type: string
  ada:phaseAngle:
    type: number
  ada:sampleHeated:
    type: boolean
  ada:samplePreparation:
    type: string
  ada:sampleTemperature:
    type: integer
  ada:spectralRangeMax:
    type: string
  ada:spectralRangeMin:
    type: string
  ada:spectralResolution:
    type: string
  ada:spectralSampling:
    type: string
  ada:spotSize:
    type: string
  ada:uncertaintyNoise:
    type: number
  ada:vacuumExposedSample:
    type: boolean
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailVNMIR/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailVNMIR/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailVNMIR/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/detailVNMIR`

