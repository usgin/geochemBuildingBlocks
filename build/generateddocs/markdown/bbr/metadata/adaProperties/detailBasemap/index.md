
# Basemap Instrument Detail (Schema)

`ada.bbr.metadata.adaProperties.detailBasemap` *v0.1*

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
  "pixelUnits": "micrometer",
  "pixelScaleX": 0.5,
  "pixelScaleY": 0.5,
  "channel1": "BSE",
  "channel2": "",
  "channel3": ""
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
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailBasemap/context.jsonld"
  ],
  "@type": [
    "ada:basemap",
    "schema:Map"
  ],
  "schema:description": "BSE basemap image of thin section",
  "pixelUnits": "micrometer",
  "pixelScaleX": 0.5,
  "pixelScaleY": 0.5,
  "channel1": "BSE",
  "channel2": "",
  "channel3": ""
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .

[] a schema1:Map,
        ada:basemap ;
    schema1:description "BSE basemap image of thin section" .


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
    const:
    - ada:basemap
    - schema:Map
  schema:description:
    type: string
  pixelUnits:
    type: string
  pixelScaleX:
    type: number
  pixelScaleY:
    type: number
  channel1:
    type: string
  channel2:
    type: string
  channel3:
    type: string
required:
- '@type'
- pixelScaleX
- pixelScaleY
- pixelUnits
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailBasemap/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailBasemap/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailBasemap/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/adaProperties/detailBasemap`

