
# NanoSIMS Instrument Detail (Schema)

`ada.bbr.metadata.geochemProperties.detailNanoSIMS` *v0.1*

Nano Secondary Ion Mass Spectrometry with isotope tracking. Defines properties: @type, phaseAnalyzed, isotopeAnalyzed. Uses building blocks: stringArray (geochemProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# NanoSIMS Instrument Detail

Nano Secondary Ion Mass Spectrometry with isotope tracking.

## Examples

### NanoSIMS Instrument Detail Example
NanoSIMS detail with isotope and phase tracking for presolar grain analysis.
#### json
```json
{
  "@type": ["ada:NanoSIMSTabular"],
  "ada:phaseAnalyzed": ["presolar SiC", "presolar graphite"],
  "ada:isotopeAnalyzed": ["12C", "13C", "28Si", "29Si"]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailNanoSIMS/context.jsonld"
  ],
  "@type": [
    "ada:NanoSIMSTabular"
  ],
  "ada:phaseAnalyzed": [
    "presolar SiC",
    "presolar graphite"
  ],
  "ada:isotopeAnalyzed": [
    "12C",
    "13C",
    "28Si",
    "29Si"
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .

[] a ada:NanoSIMSTabular ;
    ada:isotopeAnalyzed "12C",
        "13C",
        "28Si",
        "29Si" ;
    ada:phaseAnalyzed "presolar SiC",
        "presolar graphite" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: NanoSIMS Instrument Detail
description: Nano Secondary Ion Mass Spectrometry with isotope tracking
type: object
properties:
  '@type':
    type: array
    minItems: 1
    contains:
      anyOf:
      - const: ada:NanoSIMSCollection
      - const: ada:NanoSIMSImageCollection
      - const: ada:NanoSIMSTabular
      - const: ada:NanoSIMSMap
  ada:phaseAnalyzed:
    $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/stringArray/schema.yaml
  ada:isotopeAnalyzed:
    $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/stringArray/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailNanoSIMS/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailNanoSIMS/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailNanoSIMS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/detailNanoSIMS`

