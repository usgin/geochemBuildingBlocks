
# EA-IRMS Instrument Detail (Schema)

`ada.bbr.metadata.geochemProperties.detailEAIRMS` *v0.1*

Elemental Analysis Isotope Ratio Mass Spectrometry collection. Defines properties: @type, massConsumed, elementType.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# EA-IRMS Instrument Detail

Elemental Analysis Isotope Ratio Mass Spectrometry collection.

## Examples

### EA-IRMS Instrument Detail Example
Elemental Analysis Isotope Ratio Mass Spectrometry collection detail.
#### json
```json
{
  "@type": "ada:EAIRMSCollection",
  "ada:massConsumed": "2.5 mg",
  "ada:elementType": "carbon"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailEAIRMS/context.jsonld"
  ],
  "@type": "ada:EAIRMSCollection",
  "ada:massConsumed": "2.5 mg",
  "ada:elementType": "carbon"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .

[] a ada:EAIRMSCollection ;
    ada:elementType "carbon" ;
    ada:massConsumed "2.5 mg" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: EA-IRMS Instrument Detail
description: Elemental Analysis Isotope Ratio Mass Spectrometry collection
type: object
properties:
  '@type':
    const: ada:EAIRMSCollection
  ada:massConsumed:
    type: string
  ada:elementType:
    type: string
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailEAIRMS/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailEAIRMS/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailEAIRMS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/detailEAIRMS`

