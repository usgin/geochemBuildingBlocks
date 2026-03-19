
# L2MS Instrument Detail (Schema)

`ada.bbr.metadata.geochemProperties.detailL2MS` *v0.1*

Laser-2 Mass Spectrometry cube data with ionization parameters. Defines properties: @type, sampleName, ionizationTimeDelay, massGate, photoionizationWavelength, plasmaShutter, timeDelayUnits, wavelengthUnits.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# L2MS Instrument Detail

Laser-2 Mass Spectrometry cube data with ionization parameters.

## Examples

### L2MS Instrument Detail Example
Laser-2 Mass Spectrometry cube data with ionization parameters.
#### json
```json
{
  "@type": "ada:L2MSCube",
  "ada:sampleName": "Murchison_CM2_grain01",
  "ada:ionizationTimeDelay": 500,
  "ada:massGate": true,
  "ada:photoionizationWavelength": 266,
  "ada:plasmaShutter": false,
  "ada:timeDelayUnits": "nanoseconds",
  "ada:wavelengthUnits": "nm"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailL2MS/context.jsonld"
  ],
  "@type": "ada:L2MSCube",
  "ada:sampleName": "Murchison_CM2_grain01",
  "ada:ionizationTimeDelay": 500,
  "ada:massGate": true,
  "ada:photoionizationWavelength": 266,
  "ada:plasmaShutter": false,
  "ada:timeDelayUnits": "nanoseconds",
  "ada:wavelengthUnits": "nm"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a ada:L2MSCube ;
    ada:ionizationTimeDelay 500 ;
    ada:massGate true ;
    ada:photoionizationWavelength 266 ;
    ada:plasmaShutter false ;
    ada:sampleName "Murchison_CM2_grain01" ;
    ada:timeDelayUnits "nanoseconds" ;
    ada:wavelengthUnits "nm" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: L2MS Instrument Detail
description: Laser-2 Mass Spectrometry cube data with ionization parameters
type: object
properties:
  '@type':
    const: ada:L2MSCube
  ada:sampleName:
    type: string
  ada:ionizationTimeDelay:
    type: integer
  ada:massGate:
    type: boolean
  ada:photoionizationWavelength:
    type: integer
  ada:plasmaShutter:
    type: boolean
  ada:timeDelayUnits:
    type: string
  ada:wavelengthUnits:
    type: string
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailL2MS/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailL2MS/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailL2MS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/detailL2MS`

