
# Basemap Instrument Detail (Schema)

`ada.bbr.metadata.geochemProperties.detailBasemap` *v0.1*

Basemap images with RGB channels and pixel scaling. Defines properties: @type, schema:description, pixelUnits, pixelScaleX, pixelScaleY, channel1, channel2, channel3.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Basemap Instrument Detail

Basemap images with RGB channels and pixel scaling. (Extension type, not in v3 source schema.)

## Examples

### Basemap Detail Example
A basemap image with RGB channels and pixel scaling for spatial reference.
#### json
```json
{
  "@type": ["ada:basemap", "schema:Map"],
  "schema:description": "BSE basemap image of thin section",
  "ada:pixelUnits": "micrometer",
  "ada:pixelScaleX": 0.5,
  "ada:pixelScaleY": 0.5,
  "ada:channel1": "BSE",
  "ada:channel2": "",
  "ada:channel3": ""
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
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailBasemap/context.jsonld"
  ],
  "@type": [
    "ada:basemap",
    "schema:Map"
  ],
  "schema:description": "BSE basemap image of thin section",
  "ada:pixelUnits": "micrometer",
  "ada:pixelScaleX": 0.5,
  "ada:pixelScaleY": 0.5,
  "ada:channel1": "BSE",
  "ada:channel2": "",
  "ada:channel3": ""
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a schema1:Map,
        ada:basemap ;
    schema1:description "BSE basemap image of thin section" ;
    ada:channel1 "BSE" ;
    ada:channel2 "" ;
    ada:channel3 "" ;
    ada:pixelScaleX 5e-01 ;
    ada:pixelScaleY 5e-01 ;
    ada:pixelUnits "micrometer" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Basemap Instrument Detail
description: Basemap images with RGB channels and pixel scaling. (Extension type,
  not in v3 source schema.)
type: object
properties:
  '@type':
    type: array
    minItems: 2
    allOf:
    - contains:
        const: ada:basemap
    - contains:
        const: schema:Map
  schema:description:
    type: string
  ada:pixelUnits:
    type: string
  ada:pixelScaleX:
    type: number
  ada:pixelScaleY:
    type: number
  ada:channel1:
    type: string
  ada:channel2:
    type: string
  ada:channel3:
    type: string
required:
- '@type'
- ada:pixelScaleX
- ada:pixelScaleY
- ada:pixelUnits
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailBasemap/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailBasemap/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailBasemap/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/detailBasemap`

