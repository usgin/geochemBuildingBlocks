
# SLS Instrument Detail (Schema)

`ada.bbr.metadata.geochemProperties.detailSLS` *v0.1*

Structured Light Scanning shape models and partial scans. Defines properties: @type, countScans, facets, unitsOfMeasurement, version, vertices, watertight.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# SLS Instrument Detail

Structured Light Scanning shape models and partial scans.

## Examples

### SLS Instrument Detail Example
Structured Light Scanning shape model with mesh statistics.
#### json
```json
{
  "@type": ["ada:SLSShapeModel"],
  "ada:countScans": 24,
  "ada:facets": 524288,
  "ada:unitsOfMeasurement": "millimeter",
  "ada:version": 3,
  "ada:vertices": 262145,
  "ada:watertight": true
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailSLS/context.jsonld"
  ],
  "@type": [
    "ada:SLSShapeModel"
  ],
  "ada:countScans": 24,
  "ada:facets": 524288,
  "ada:unitsOfMeasurement": "millimeter",
  "ada:version": 3,
  "ada:vertices": 262145,
  "ada:watertight": true
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a ada:SLSShapeModel ;
    ada:countScans 24 ;
    ada:facets 524288 ;
    ada:unitsOfMeasurement "millimeter" ;
    ada:version 3 ;
    ada:vertices 262145 ;
    ada:watertight true .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SLS Instrument Detail
description: Structured Light Scanning shape models and partial scans
type: object
properties:
  '@type':
    anyOf:
    - const: ada:SLSShapeModel
    - const: ada:SLSPartialScan
  ada:countScans:
    type: integer
  ada:facets:
    type: integer
  ada:unitsOfMeasurement:
    type: string
  ada:version:
    type: integer
  ada:vertices:
    type: integer
  ada:watertight:
    type: boolean
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailSLS/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailSLS/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailSLS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/detailSLS`

