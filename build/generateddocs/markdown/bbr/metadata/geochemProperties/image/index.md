
# Image Type (Schema)

`ada.bbr.metadata.geochemProperties.image` *v0.1*

ADA image with componentType classification for analytical images. Defines properties: @type, acquisitionTime, componentType, channel1, channel2, channel3, pixelSize, illuminationType, imageType.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Image Type

Describes image objects in ADA metadata with acquisition details and component type classification. Typed as `ada:image` and `schema:ImageObject`. Supports various analytical image types including EMPA, SEM, TEM, STEM, and spectroscopic images.

## Examples

### Image Type Example
An SEM backscattered electron image with component type and acquisition details.
#### json
```json
{
  "@type": ["ada:image", "schema:ImageObject"],
  "ada:componentType": {
    "@type": "ada:SEMImageCollection"
  },
  "ada:acquisitionTime": "2024-03-15T14:30:00Z",
  "ada:channel1": "BSE",
  "ada:pixelSize": "0.5 micrometer",
  "ada:illuminationType": "Electron beam",
  "ada:imageType": "Backscattered electron"
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
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/image/context.jsonld"
  ],
  "@type": [
    "ada:image",
    "schema:ImageObject"
  ],
  "ada:componentType": {
    "@type": "ada:SEMImageCollection"
  },
  "ada:acquisitionTime": "2024-03-15T14:30:00Z",
  "ada:channel1": "BSE",
  "ada:pixelSize": "0.5 micrometer",
  "ada:illuminationType": "Electron beam",
  "ada:imageType": "Backscattered electron"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .

[] a schema1:ImageObject,
        ada:image ;
    ada:acquisitionTime "2024-03-15T14:30:00Z" ;
    ada:channel1 "BSE" ;
    ada:componentType [ a ada:SEMImageCollection ] ;
    ada:illuminationType "Electron beam" ;
    ada:imageType "Backscattered electron" ;
    ada:pixelSize "0.5 micrometer" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Image Type
description: Image objects with acquisition details and component type classification.
  Typed as ada:image and schema:ImageObject.
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
        const: schema:ImageObject
    description: GeneralType for images
  ada:acquisitionTime:
    type: string
  ada:componentType:
    type: object
    properties:
      '@type':
        enum:
        - ada:AIVAImage
        - ada:EMPAImage
        - ada:LITImage
        - ada:STEMImage
        - ada:TEMImage
        - ada:TEMPatternsImage
        - ada:UVFMImage
        - ada:VLMImage
        - ada:SEMEBSDGrainImage
        - ada:SEMEDSElementalMap
        - ada:SEMHRCLImage
        - ada:SEMImageCollection
        - ada:TEMEDSImageCollection
        - ada:NanoSIMSImage
        - ada:XANESImageStack
        - ada:XANESStackOverviewImage
        - ada:XRDDiffractionPattern
        - ada:ShapeModelImage
    required:
    - '@type'
  ada:channel1:
    type: string
  ada:channel2:
    type: string
  ada:channel3:
    type: string
  ada:pixelSize:
    type: string
  ada:illuminationType:
    type: string
    description: Type of illumination used to create the image. Examples include Visible
      light, Cross-polarized visible light, ultraviolet light, Electron beam, X-ray.
  ada:imageType:
    type: string
    description: Specifies the nature of the sample's response to the illumination
      that was detected and measured.
required:
- '@type'
- ada:componentType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/image/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/image/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/image/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/image`

