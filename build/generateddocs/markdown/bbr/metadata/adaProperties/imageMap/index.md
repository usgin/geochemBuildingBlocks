
# Image Map Type (Schema)

`ada.bbr.metadata.adaProperties.imageMap` *v0.1*

Spatially registered image map with pixel coordinates and component types. Defines properties: @type, acquisitionTime, componentType, channel1, channel2, channel3, illuminationType, imageType, numPixelsX, numPixelsY, spatialRegistration. Uses building blocks: detailEMPA (adaProperties), spatialRegistration (adaProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Image Map Type

Describes spatially registered image maps with pixel coordinates, component type classification (including EMPA details), and spatial registration metadata. Extends the basic image type with pixel dimensions and spatial registration.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Image Map Type
description: Spatially registered image maps with pixel coordinates, component type
  classification, and spatial registration metadata.
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    minItems: 2
    allOf:
    - contains:
        const: ada:imageMap
    - contains:
        const: schema:ImageObject
  acquisitionTime:
    type: string
  componentType:
    anyOf:
    - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailEMPA/schema.yaml
    - type: object
      properties:
        '@type':
          enum:
          - ada:basemap
          - ada:supplementalBasemap
          - ada:L2MSOverviewImage
          - ada:NanoIRMap
          - ada:LITImage
          - ada:UVFMImage
          - ada:VLMImage
          - ada:SEMEBSDGrainImageMap
          - ada:SEMEDSElementalMap
          - ada:SEMHRCLMap
          - ada:SEMImageMap
          - ada:STEMImage
          - ada:TEMImage
          - ada:TEMPatternsImage
          - ada:NanoSIMSMap
          - ada:XANESimage
          - ada:VNMIROverviewImage
      required:
      - '@type'
  channel1:
    type: string
  channel2:
    type: string
  channel3:
    type: string
  illuminationType:
    type: string
    description: Type of illumination used to create the image.
  imageType:
    type: string
    description: Specifies the nature of the sample's response to the illumination.
  numPixelsX:
    type: integer
  numPixelsY:
    type: integer
  spatialRegistration:
    $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/spatialRegistration/schema.yaml
required:
- '@type'
- componentType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/imageMap/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/imageMap/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/imageMap/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/adaProperties/imageMap`

