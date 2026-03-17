
# Spatial Registration Type (Schema)

`ada.bbr.metadata.adaProperties.spatialRegistration` *v0.1*

Pixel coordinate system registration for images and maps. Defines properties: basemap, originX, originY, originZ, coordDef, coordUnits, pixelUnits, pixelScaleX, pixelScaleY, originLocation.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Spatial Registration Type

Defines the pixel coordinate system registration for spatially registered images and maps. Includes origin coordinates (X, Y, Z), pixel scales, coordinate units, and the coordinate definition type (stage-defined or pixel-defined).

## Examples

### Spatial Registration Example
Pixel coordinate system registration for a spatially registered image map.
#### json
```json
{
  "ada:basemap": "basemap_BSE_001.tif",
  "ada:originX": 0.0,
  "ada:originY": 0.0,
  "ada:originZ": 0.0,
  "ada:coordDef": "pixel-defined",
  "ada:coordUnits": "micrometer",
  "ada:pixelUnits": "micrometer",
  "ada:pixelScaleX": 0.125,
  "ada:pixelScaleY": 0.125,
  "ada:originLocation": "upperLeft"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/spatialRegistration/context.jsonld"
  ],
  "ada:basemap": "basemap_BSE_001.tif",
  "ada:originX": 0.0,
  "ada:originY": 0.0,
  "ada:originZ": 0.0,
  "ada:coordDef": "pixel-defined",
  "ada:coordUnits": "micrometer",
  "ada:pixelUnits": "micrometer",
  "ada:pixelScaleX": 0.125,
  "ada:pixelScaleY": 0.125,
  "ada:originLocation": "upperLeft"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] ada:basemap "basemap_BSE_001.tif" ;
    ada:coordDef "pixel-defined" ;
    ada:coordUnits "micrometer" ;
    ada:originLocation "upperLeft" ;
    ada:originX 0e+00 ;
    ada:originY 0e+00 ;
    ada:originZ 0e+00 ;
    ada:pixelScaleX 1.25e-01 ;
    ada:pixelScaleY 1.25e-01 ;
    ada:pixelUnits "micrometer" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Spatial Registration Type
description: Defines pixel coordinate system registration including origin coordinates,
  pixel scales, and coordinate definition type for spatially registered images and
  maps.
type: object
properties:
  ada:basemap:
    type: string
    description: link to appropriate basemap image map
  ada:originX:
    type: number
  ada:originY:
    type: number
  ada:originZ:
    type: number
  ada:coordDef:
    type: string
    description: Whether coordinates are stage-defined or pixel-defined. If pixel-defined,
      are coordinates from stage, upperleftPixel, or centerPixel.
  ada:coordUnits:
    type: string
  ada:pixelUnits:
    type: string
  ada:pixelScaleX:
    type: number
  ada:pixelScaleY:
    type: number
  ada:originLocation:
    type: string
    description: 'The location of the origin pixel of an image. Range: upperLeft,
      upperRight, lowerLeft, lowerRight, center'
required:
- ada:originX
- ada:originY
- ada:pixelScaleX
- ada:pixelScaleY
- ada:pixelUnits
- ada:originLocation
- ada:coordDef
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

