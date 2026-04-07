
# NanoIR Instrument Detail (Schema)

`ada.bbr.metadata.geochemProperties.detailNanoIR` *v0.1*

Nano-IR spectroscopy collections with phase analysis. Defines properties: @type, phaseAnalyzed. Uses building blocks: stringArray (geochemProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# NanoIR Instrument Detail

Nano-IR spectroscopy collections with phase analysis.

## Examples

### NanoIR Instrument Detail Example
Nano-IR background spectroscopy detail with phases analyzed.
#### json
```json
{
  "@type": ["ada:NanoIRBackground"],
  "ada:phaseAnalyzed": ["carbonate", "silicate"]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailNanoIR/context.jsonld"
  ],
  "@type": [
    "ada:NanoIRBackground"
  ],
  "ada:phaseAnalyzed": [
    "carbonate",
    "silicate"
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .

[] a ada:NanoIRBackground ;
    ada:phaseAnalyzed "carbonate",
        "silicate" .


```

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
  ada:phaseAnalyzed:
    $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/stringArray/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailNanoIR/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailNanoIR/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailNanoIR/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/detailNanoIR`

