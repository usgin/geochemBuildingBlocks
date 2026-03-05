
# EMPA Instrument Detail (Schema)

`ada.bbr.metadata.adaProperties.detailEMPA` *v0.1*

Electron Microprobe Analysis instrument-specific detail properties. Defines properties: @type, spectrometersUsed, signalUsed.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# EMPA Instrument Detail

Electron Microprobe Analysis with spectrometer and signal details.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: EMPA Instrument Detail
description: Electron Microprobe Analysis with spectrometer and signal details.
type: object
properties:
  '@type':
    anyOf:
    - const: ada:EMPAImage
    - const: ada:EMPAQEATabular
    - const: ada:EMPAImageCollection
  spectrometersUsed:
    type: string
    description: Spectrometers used in analysis
  signalUsed:
    type: string
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailEMPA/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailEMPA/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailEMPA/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/adaProperties/detailEMPA`

