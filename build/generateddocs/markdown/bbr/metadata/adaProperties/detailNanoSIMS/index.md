
# NanoSIMS Instrument Detail (Schema)

`ada.bbr.metadata.adaProperties.detailNanoSIMS` *v0.1*

Nano Secondary Ion Mass Spectrometry with isotope tracking. Defines properties: @type, phaseAnalyzed, isotopeAnalyzed. Uses building blocks: stringArray (adaProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# NanoSIMS Instrument Detail

Nano Secondary Ion Mass Spectrometry with isotope tracking.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: NanoSIMS Instrument Detail
description: Nano Secondary Ion Mass Spectrometry with isotope tracking
type: object
properties:
  '@type':
    type: string
    enum:
    - ada:NanoSIMSCollection
    - ada:NanoSIMSImageCollection
    - ada:NanoSIMSTabular
    - ada:NanoSIMSMap
  phaseAnalyzed:
    $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/stringArray/schema.yaml
  isotopeAnalyzed:
    $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/stringArray/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailNanoSIMS/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailNanoSIMS/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailNanoSIMS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/adaProperties/detailNanoSIMS`

