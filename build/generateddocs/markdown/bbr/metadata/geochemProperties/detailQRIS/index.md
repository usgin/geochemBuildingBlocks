
# QRIS Instrument Detail (Schema)

`ada.bbr.metadata.geochemProperties.detailQRIS` *v0.1*

QRIS (Raman) with calibration and illumination parameters. Defines properties: @type, calibrationFile, pipelineVersion, focalLength, illuminationColor, illuminationLevel, exposureTime, target.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# QRIS Instrument Detail

QRIS (Raman) with calibration and illumination parameters. (Extension type, not in v3 source schema.)

## Examples

### QRIS Instrument Detail Example
QRIS (Raman spectroscopy) calibrated data with illumination and calibration details.
#### json
```json
{
  "@type": "ada:QRISCalibrated",
  "ada:calibrationFile": "calibration_neon_20240301.csv",
  "ada:pipelineVersion": "2.1.0",
  "ada:focalLength": 300,
  "ada:illuminationColor": ["532nm green"],
  "ada:illuminationLevel": 50,
  "ada:exposureTime": 10,
  "ada:target": "olivine grain"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailQRIS/context.jsonld"
  ],
  "@type": "ada:QRISCalibrated",
  "ada:calibrationFile": "calibration_neon_20240301.csv",
  "ada:pipelineVersion": "2.1.0",
  "ada:focalLength": 300,
  "ada:illuminationColor": [
    "532nm green"
  ],
  "ada:illuminationLevel": 50,
  "ada:exposureTime": 10,
  "ada:target": "olivine grain"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a ada:QRISCalibrated ;
    ada:calibrationFile "calibration_neon_20240301.csv" ;
    ada:exposureTime 10 ;
    ada:focalLength 300 ;
    ada:illuminationColor "532nm green" ;
    ada:illuminationLevel 50 ;
    ada:pipelineVersion "2.1.0" ;
    ada:target "olivine grain" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: QRIS Instrument Detail
description: QRIS (Raman) with calibration and illumination parameters. (Extension
  type, not in v3 source schema.)
type: object
properties:
  '@type':
    anyOf:
    - const: ada:QRISCalibrated
    - const: ada:QRISRaw
  ada:calibrationFile:
    type: string
  ada:pipelineVersion:
    type: string
  ada:focalLength:
    type: integer
  ada:illuminationColor:
    type: array
    minItems: 0
    items:
      type: string
  ada:illuminationLevel:
    type: integer
  ada:exposureTime:
    type: integer
  ada:target:
    type: string
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailQRIS/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailQRIS/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailQRIS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/detailQRIS`

