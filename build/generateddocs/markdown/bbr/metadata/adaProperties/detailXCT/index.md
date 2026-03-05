
# XCT Instrument Detail (Schema)

`ada.bbr.metadata.adaProperties.detailXCT` *v0.1*

X-ray Computed Tomography images with detailed scan parameters. Defines properties: @type, beamFilterMaterial, beamFilterThickness, dataRangeLower, dataRangeUpper, detectorGain, detectorBinning, detectorSize, detectorType, imageExposure, imageFPS, imageGain, imageSize, instrumentType, nsiBeamHardening, numberOfFramesAveragedPerProjection, numberOfProjections, numberOfSlices, pixelPitch, reconstructedDataFormat, reconstructedVoxelSize, reconstructionSoftware, rotationAngle, rotationType, sourceToDetectorDistance, sourceToObjectDistance, subPixGrid, subPixShift, xraySource, xrayTargetMaterial, xrayTubeCurrent, xrayTubeEnergy, xrayTubePower.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# XCT Instrument Detail

X-ray Computed Tomography images with detailed scan parameters. (Extension type, not in v3 source schema.)

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: XCT Instrument Detail
description: X-ray Computed Tomography images with detailed scan parameters. (Extension
  type, not in v3 source schema.)
type: object
properties:
  '@type':
    const: ada:XCTImageCollection
  beamFilterMaterial:
    type: string
  beamFilterThickness:
    type: number
  dataRangeLower:
    type: integer
  dataRangeUpper:
    type: integer
  detectorGain:
    type: string
  detectorBinning:
    type: string
  detectorSize:
    type: string
  detectorType:
    type: string
  imageExposure:
    type: number
  imageFPS:
    type: string
  imageGain:
    type: number
  imageSize:
    type: string
  instrumentType:
    type: string
  nsiBeamHardening:
    type: number
  numberOfFramesAveragedPerProjection:
    type: integer
  numberOfProjections:
    type: integer
  numberOfSlices:
    type: integer
  pixelPitch:
    type: string
  reconstructedDataFormat:
    type: string
  reconstructedVoxelSize:
    type: string
  reconstructionSoftware:
    type: string
  rotationAngle:
    type: string
  rotationType:
    type: string
  sourceToDetectorDistance:
    type: string
  sourceToObjectDistance:
    type: number
  subPixGrid:
    type: string
  subPixShift:
    type: string
  xraySource:
    type: string
  xrayTargetMaterial:
    type: string
  xrayTubeCurrent:
    type: number
  xrayTubeEnergy:
    type: number
  xrayTubePower:
    type: number
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailXCT/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailXCT/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailXCT/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/adaProperties/detailXCT`

