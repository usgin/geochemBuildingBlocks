
# Image Map Type (Schema)

`ada.bbr.metadata.geochemProperties.imageMap` *v0.1*

Spatially registered image map with pixel coordinates and component types. Defines properties: @type, acquisitionTime, componentType, channel1, channel2, channel3, illuminationType, imageType, numPixelsX, numPixelsY, spatialRegistration. Uses building blocks: detailEMPA (geochemProperties), spatialRegistration (geochemProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Image Map Type

Describes spatially registered image maps with pixel coordinates, component type classification (including EMPA details), and spatial registration metadata. Extends the basic image type with pixel dimensions and spatial registration.

## Examples

### Image Map Type Example
A spatially registered SEM elemental map image with pixel coordinates and spatial registration.
#### json
```json
{
  "@type": ["ada:imageMap", "schema:ImageObject"],
  "ada:componentType": {
    "@type": "ada:SEMEDSElementalMap"
  },
  "ada:acquisitionTime": "2024-03-15T14:35:00Z",
  "ada:channel1": "Fe Ka",
  "ada:illuminationType": "Electron beam",
  "ada:imageType": "X-ray intensity map",
  "ada:numPixelsX": 1024,
  "ada:numPixelsY": 768,
  "ada:spatialRegistration": {
    "ada:originX": 0.0,
    "ada:originY": 0.0,
    "ada:pixelScaleX": 0.25,
    "ada:pixelScaleY": 0.25,
    "ada:pixelUnits": "micrometer",
    "ada:originLocation": "upperLeft",
    "ada:coordDef": "pixel-defined"
  }
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
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/imageMap/context.jsonld"
  ],
  "@type": [
    "ada:imageMap",
    "schema:ImageObject"
  ],
  "ada:componentType": {
    "@type": "ada:SEMEDSElementalMap"
  },
  "ada:acquisitionTime": "2024-03-15T14:35:00Z",
  "ada:channel1": "Fe Ka",
  "ada:illuminationType": "Electron beam",
  "ada:imageType": "X-ray intensity map",
  "ada:numPixelsX": 1024,
  "ada:numPixelsY": 768,
  "ada:spatialRegistration": {
    "ada:originX": 0.0,
    "ada:originY": 0.0,
    "ada:pixelScaleX": 0.25,
    "ada:pixelScaleY": 0.25,
    "ada:pixelUnits": "micrometer",
    "ada:originLocation": "upperLeft",
    "ada:coordDef": "pixel-defined"
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a schema1:ImageObject,
        ada:imageMap ;
    ada:acquisitionTime "2024-03-15T14:35:00Z" ;
    ada:channel1 "Fe Ka" ;
    ada:componentType [ a ada:SEMEDSElementalMap ] ;
    ada:illuminationType "Electron beam" ;
    ada:imageType "X-ray intensity map" ;
    ada:numPixelsX 1024 ;
    ada:numPixelsY 768 ;
    ada:spatialRegistration [ ada:coordDef "pixel-defined" ;
            ada:originLocation "upperLeft" ;
            ada:originX 0e+00 ;
            ada:originY 0e+00 ;
            ada:pixelScaleX 2.5e-01 ;
            ada:pixelScaleY 2.5e-01 ;
            ada:pixelUnits "micrometer" ] .


```

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
  ada:acquisitionTime:
    type: string
  ada:componentType:
    anyOf:
    - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailEMPA/schema.yaml
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
  ada:channel1:
    type: string
  ada:channel2:
    type: string
  ada:channel3:
    type: string
  ada:illuminationType:
    type: string
    description: Type of illumination used to create the image.
  ada:imageType:
    type: string
    description: Specifies the nature of the sample's response to the illumination.
  ada:numPixelsX:
    type: integer
  ada:numPixelsY:
    type: integer
  ada:spatialRegistration:
    $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/spatialRegistration/schema.yaml
required:
- '@type'
- ada:componentType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/imageMap/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/imageMap/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/imageMap/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/imageMap`

