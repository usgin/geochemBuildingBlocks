
# ICP-OES Instrument Detail (Schema)

`ada.bbr.metadata.geochemProperties.detailICPOES` *v0.1*

Inductively Coupled Plasma Optical Emission Spectrometry detail properties. Defines properties: @type, mass, dissolutionFactor.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ICP-OES Instrument Detail

Inductively Coupled Plasma Optical Emission Spectrometry. (Extension type, not in v3 source schema.)

## Examples

### ICP-OES Instrument Detail Example
Inductively Coupled Plasma Optical Emission Spectrometry processed data detail.
#### json
```json
{
  "@type": "ada:ICPOESProcessedTabular",
  "ada:mass": "50.2 mg",
  "ada:dissolutionFactor": 100.0
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailICPOES/context.jsonld"
  ],
  "@type": "ada:ICPOESProcessedTabular",
  "ada:mass": "50.2 mg",
  "ada:dissolutionFactor": 100.0
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a ada:ICPOESProcessedTabular ;
    ada:dissolutionFactor 1e+02 ;
    ada:mass "50.2 mg" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ICP-OES Instrument Detail
description: Inductively Coupled Plasma Optical Emission Spectrometry. (Extension
  type, not in v3 source schema.)
type: object
properties:
  '@type':
    anyOf:
    - const: ada:ICPOESIntermediateTabular
    - const: ada:ICPOESProcessedTabular
    - const: ada:ICPOESRawTabular
  ada:mass:
    type: string
  ada:dissolutionFactor:
    type: number
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailICPOES/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailICPOES/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailICPOES/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/detailICPOES`

