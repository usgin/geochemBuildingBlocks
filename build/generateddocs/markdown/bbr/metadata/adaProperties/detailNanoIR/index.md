
# NanoIR Instrument Detail (Schema)

`ada.bbr.metadata.adaProperties.detailNanoIR` *v0.1*

Nano-IR spectroscopy collections with phase analysis. Defines properties: @type, phaseAnalyzed. Uses building blocks: stringArray (adaProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# NanoIR Instrument Detail

Nano-IR spectroscopy collections with phase analysis.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: NanoIR Instrument Detail
description: Nano-IR spectroscopy collections with phase analysis
type: object
properties:
  '@type':
    anyOf:
    - const: ada:NanoIRBackground
  phaseAnalyzed:
    $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/stringArray/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailNanoIR/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailNanoIR/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailNanoIR/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/adaProperties/detailNanoIR`

