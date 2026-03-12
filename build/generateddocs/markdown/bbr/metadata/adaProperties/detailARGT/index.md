
# ARGT Instrument Detail (Schema)

`ada.bbr.metadata.adaProperties.detailARGT` *v0.1*

ARGT (Argon) document type with phase and isotope analysis. Defines properties: @type, phaseAnalyzed, isotopeType.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ARGT Instrument Detail

ARGT (Argon) document type with phase and isotope analysis.

## Examples

### ARGT Instrument Detail Example
Argon geochronology document detail with phase and isotope analysis type.
#### json
```json
{
  "@type": "ada:ARGTDocument",
  "phaseAnalyzed": "sanidine",
  "isotopeType": "40Ar/39Ar"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailARGT/context.jsonld"
  ],
  "@type": "ada:ARGTDocument",
  "phaseAnalyzed": "sanidine",
  "isotopeType": "40Ar/39Ar"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .

[] a ada:ARGTDocument .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ARGT Instrument Detail
description: ARGT (Argon) document type with phase and isotope analysis
type: object
properties:
  '@type':
    const: ada:ARGTDocument
  phaseAnalyzed:
    type: string
  isotopeType:
    type: string
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailARGT/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailARGT/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailARGT/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/adaProperties/detailARGT`

