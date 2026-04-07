
# ARGT Instrument Detail (Schema)

`ada.bbr.metadata.geochemProperties.detailARGT` *v0.1*

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
  "@type": ["ada:ARGTDocument"],
  "ada:phaseAnalyzed": "sanidine",
  "ada:isotopeType": "40Ar/39Ar"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailARGT/context.jsonld"
  ],
  "@type": [
    "ada:ARGTDocument"
  ],
  "ada:phaseAnalyzed": "sanidine",
  "ada:isotopeType": "40Ar/39Ar"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .

[] a ada:ARGTDocument ;
    ada:isotopeType "40Ar/39Ar" ;
    ada:phaseAnalyzed "sanidine" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ARGT Instrument Detail
description: ARGT (Argon) document type with phase and isotope analysis
type: object
properties:
  '@type':
    type: array
    contains:
      const: ada:ARGTDocument
    minItems: 1
  ada:phaseAnalyzed:
    type: string
  ada:isotopeType:
    type: string
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailARGT/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailARGT/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailARGT/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/detailARGT`

