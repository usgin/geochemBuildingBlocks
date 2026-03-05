
# Spatial Registration Type (Schema)

`ada.bbr.metadata.adaProperties.spatialRegistration` *v0.1*

Pixel coordinate system registration for images and maps. Defines properties: basemap, originX, originY, originZ, coordDef, coordUnits, pixelUnits, pixelScaleX, pixelScaleY, originLocation.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Spatial Registration Type

Defines the pixel coordinate system registration for spatially registered images and maps. Includes origin coordinates (X, Y, Z), pixel scales, coordinate units, and the coordinate definition type (stage-defined or pixel-defined).

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Spatial Registration Type
description: Defines pixel coordinate system registration including origin coordinates,
  pixel scales, and coordinate definition type for spatially registered images and
  maps.
type: object
properties:
  basemap:
    type: string
    description: link to appropriate basemap image map
  originX:
    type: number
  originY:
    type: number
  originZ:
    type: number
  coordDef:
    type: string
    description: Whether coordinates are stage-defined or pixel-defined. If pixel-defined,
      are coordinates from stage, upperleftPixel, or centerPixel.
  coordUnits:
    type: string
  pixelUnits:
    type: string
  pixelScaleX:
    type: number
  pixelScaleY:
    type: number
  originLocation:
    type: string
    description: 'The location of the origin pixel of an image. Range: upperLeft,
      upperRight, lowerLeft, lowerRight, center'
required:
- originX
- originY
- pixelScaleX
- pixelScaleY
- pixelUnits
- originLocation
- coordDef
x-jsonld-prefixes:
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/spatialRegistration/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/spatialRegistration/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "ada": "https://ada.astromat.org/metadata/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/spatialRegistration/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/adaProperties/spatialRegistration`

