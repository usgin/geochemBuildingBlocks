
# SLS Instrument Detail (Schema)

`ada.bbr.metadata.adaProperties.detailSLS` *v0.1*

Structured Light Scanning shape models and partial scans. Defines properties: @type, countScans, facets, unitsOfMeasurement, version, vertices, watertight.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# SLS Instrument Detail

Structured Light Scanning shape models and partial scans.

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
  countScans:
    type: integer
  facets:
    type: integer
  unitsOfMeasurement:
    type: string
  version:
    type: integer
  vertices:
    type: integer
  watertight:
    type: boolean
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailSLS/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailSLS/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailSLS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/adaProperties/detailSLS`

