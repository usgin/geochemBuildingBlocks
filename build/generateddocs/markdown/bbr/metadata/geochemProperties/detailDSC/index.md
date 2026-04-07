
# DSC Instrument Detail (Schema)

`ada.bbr.metadata.geochemProperties.detailDSC` *v0.1*

Differential Scanning Calorimetry heat tabular data. Defines properties: @type, analysisType.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# DSC Instrument Detail

Differential Scanning Calorimetry heat tabular data.

## Examples

### DSC Instrument Detail Example
Differential Scanning Calorimetry heat flow data detail.
#### json
```json
{
  "@type": ["ada:DSCHeatTabular"],
  "ada:analysisType": "heating"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailDSC/context.jsonld"
  ],
  "@type": [
    "ada:DSCHeatTabular"
  ],
  "ada:analysisType": "heating"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .

[] a ada:DSCHeatTabular ;
    ada:analysisType "heating" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DSC Instrument Detail
description: Differential Scanning Calorimetry heat tabular data
type: object
properties:
  '@type':
    type: array
    contains:
      const: ada:DSCHeatTabular
    minItems: 1
  ada:analysisType:
    type: string
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailDSC/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailDSC/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailDSC/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/detailDSC`

