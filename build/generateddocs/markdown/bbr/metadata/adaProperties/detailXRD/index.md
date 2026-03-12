
# XRD Instrument Detail (Schema)

`ada.bbr.metadata.adaProperties.detailXRD` *v0.1*

X-ray Diffraction tabular data with geometry and wavelength. Defines properties: @type, geometry, sampleMount, stepSize, timePerStep, wavelength.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# XRD Instrument Detail

X-ray Diffraction tabular data with geometry and wavelength.

## Examples

### XRD Instrument Detail Example
X-ray Diffraction tabular data with geometry and wavelength parameters.
#### json
```json
{
  "@type": "ada:XRDTabular",
  "geometry": "Bragg-Brentano",
  "sampleMount": "flat plate",
  "stepSize": 0.02,
  "timePerStep": 1.0,
  "wavelength": 1.5406
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailXRD/context.jsonld"
  ],
  "@type": "ada:XRDTabular",
  "geometry": "Bragg-Brentano",
  "sampleMount": "flat plate",
  "stepSize": 0.02,
  "timePerStep": 1.0,
  "wavelength": 1.5406
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .

[] a ada:XRDTabular .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: XRD Instrument Detail
description: X-ray Diffraction tabular data with geometry and wavelength
type: object
properties:
  '@type':
    const: ada:XRDTabular
  geometry:
    type: string
  sampleMount:
    type: string
  stepSize:
    type: number
  timePerStep:
    type: number
  wavelength:
    type: number
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailXRD/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailXRD/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailXRD/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/adaProperties/detailXRD`

