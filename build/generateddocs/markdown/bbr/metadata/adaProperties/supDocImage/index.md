
# Supplemental Document Image Type (Schema)

`ada.bbr.metadata.adaProperties.supDocImage` *v0.1*

Supplemental document images including analysis locations and context photos. Defines properties: @type, componentType, numPixelsX, numPixelsY, _original_name.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Supplemental Document Image Type

Describes supplemental document images such as analysis location images, annotated products, context photography, areas of interest, instrument metadata images, supplemental basemaps, plots, quick-look images, reports, and visual images.

## Examples

### Supplemental Document Image Example
A context photography image used as supplemental documentation.
#### json
```json
{
  "@type": ["ada:image", "schema:DigitalDocument"],
  "ada:componentType": {
    "@type": "ada:contextPhotography"
  },
  "ada:numPixelsX": 2048,
  "ada:numPixelsY": 1536,
  "_original_name": "sample_context_photo_001.jpg"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/supDocImage/context.jsonld"
  ],
  "@type": [
    "ada:image",
    "schema:DigitalDocument"
  ],
  "ada:componentType": {
    "@type": "ada:contextPhotography"
  },
  "ada:numPixelsX": 2048,
  "ada:numPixelsY": 1536,
  "_original_name": "sample_context_photo_001.jpg"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a schema1:DigitalDocument,
        ada:image ;
    ada:componentType [ a ada:contextPhotography ] ;
    ada:numPixelsX 2048 ;
    ada:numPixelsY 1536 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Supplemental Document Image Type
description: Supplemental document images including analysis location images, annotated
  products, context photography, and other supplemental visual materials.
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    minItems: 2
    allOf:
    - contains:
        const: ada:image
    - contains:
        const: schema:DigitalDocument
    description: GeneralType for supplemental document images
  ada:componentType:
    type: object
    properties:
      '@type':
        enum:
        - ada:analysisLocation
        - ada:annotatedProduct
        - ada:contextPhotography
        - ada:areaOfInterest
        - ada:instrumentMetadata
        - ada:supplementalBasemap
        - ada:other
        - ada:plot
        - ada:quickLook
        - ada:report
        - ada:visImage
    required:
    - '@type'
  ada:numPixelsX:
    type: integer
  ada:numPixelsY:
    type: integer
  _original_name:
    type: string
required:
- '@type'
- ada:componentType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/supDocImage/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/supDocImage/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/supDocImage/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/adaProperties/supDocImage`

