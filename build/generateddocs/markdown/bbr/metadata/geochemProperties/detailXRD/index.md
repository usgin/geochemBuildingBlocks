
# XRD Instrument Detail (Schema)

`ada.bbr.metadata.geochemProperties.detailXRD` *v0.1*

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
  "ada:geometry": "Bragg-Brentano",
  "ada:sampleMount": "flat plate",
  "ada:stepSize": 0.02,
  "ada:timePerStep": 1.0,
  "ada:wavelength": 1.5406
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailXRD/context.jsonld"
  ],
  "@type": "ada:XRDTabular",
  "ada:geometry": "Bragg-Brentano",
  "ada:sampleMount": "flat plate",
  "ada:stepSize": 0.02,
  "ada:timePerStep": 1.0,
  "ada:wavelength": 1.5406
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a ada:XRDTabular ;
    ada:geometry "Bragg-Brentano" ;
    ada:sampleMount "flat plate" ;
    ada:stepSize 2e-02 ;
    ada:timePerStep 1e+00 ;
    ada:wavelength 1.5406e+00 .


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
  ada:geometry:
    type: string
  ada:sampleMount:
    type: string
  ada:stepSize:
    type: number
  ada:timePerStep:
    type: number
  ada:wavelength:
    type: number
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailXRD/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailXRD/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailXRD/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/detailXRD`

