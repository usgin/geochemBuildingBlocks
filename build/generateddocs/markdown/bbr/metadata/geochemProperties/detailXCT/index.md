
# XCT Instrument Detail (Schema)

`ada.bbr.metadata.geochemProperties.detailXCT` *v0.1*

X-ray Computed Tomography images with detailed scan parameters. Defines properties: @type, beamFilterMaterial, beamFilterThickness, dataRangeLower, dataRangeUpper, detectorGain, detectorBinning, detectorSize, detectorType, imageExposure, imageFPS, imageGain, imageSize, instrumentType, nsiBeamHardening, numberOfFramesAveragedPerProjection, numberOfProjections, numberOfSlices, pixelPitch, reconstructedDataFormat, reconstructedVoxelSize, reconstructionSoftware, rotationAngle, rotationType, sourceToDetectorDistance, sourceToObjectDistance, subPixGrid, subPixShift, xraySource, xrayTargetMaterial, xrayTubeCurrent, xrayTubeEnergy, xrayTubePower.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# XCT Instrument Detail

X-ray Computed Tomography images with detailed scan parameters. (Extension type, not in v3 source schema.)

## Examples

### XCT Instrument Detail Example
X-ray Computed Tomography image collection with detailed scan parameters.
#### json
```json
{
  "@type": "ada:XCTImageCollection",
  "ada:instrumentType": "micro-CT",
  "ada:xraySource": "sealed tube",
  "ada:xrayTargetMaterial": "tungsten",
  "ada:xrayTubeEnergy": 120.0,
  "ada:xrayTubeCurrent": 0.1,
  "ada:xrayTubePower": 12.0,
  "ada:beamFilterMaterial": "copper",
  "ada:beamFilterThickness": 0.5,
  "ada:sourceToDetectorDistance": "500 mm",
  "ada:sourceToObjectDistance": 200.0,
  "ada:detectorType": "flat panel",
  "ada:detectorSize": "2048x2048",
  "ada:detectorBinning": "1x1",
  "ada:numberOfProjections": 1440,
  "ada:numberOfSlices": 2000,
  "ada:numberOfFramesAveragedPerProjection": 4,
  "ada:rotationAngle": "360 degrees",
  "ada:rotationType": "step-and-shoot",
  "ada:imageExposure": 0.5,
  "ada:imageSize": "2048x2048",
  "ada:reconstructedVoxelSize": "5.0 micrometer",
  "ada:reconstructedDataFormat": "16-bit TIFF",
  "ada:reconstructionSoftware": "Nikon CT Pro 3D"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailXCT/context.jsonld"
  ],
  "@type": "ada:XCTImageCollection",
  "ada:instrumentType": "micro-CT",
  "ada:xraySource": "sealed tube",
  "ada:xrayTargetMaterial": "tungsten",
  "ada:xrayTubeEnergy": 120.0,
  "ada:xrayTubeCurrent": 0.1,
  "ada:xrayTubePower": 12.0,
  "ada:beamFilterMaterial": "copper",
  "ada:beamFilterThickness": 0.5,
  "ada:sourceToDetectorDistance": "500 mm",
  "ada:sourceToObjectDistance": 200.0,
  "ada:detectorType": "flat panel",
  "ada:detectorSize": "2048x2048",
  "ada:detectorBinning": "1x1",
  "ada:numberOfProjections": 1440,
  "ada:numberOfSlices": 2000,
  "ada:numberOfFramesAveragedPerProjection": 4,
  "ada:rotationAngle": "360 degrees",
  "ada:rotationType": "step-and-shoot",
  "ada:imageExposure": 0.5,
  "ada:imageSize": "2048x2048",
  "ada:reconstructedVoxelSize": "5.0 micrometer",
  "ada:reconstructedDataFormat": "16-bit TIFF",
  "ada:reconstructionSoftware": "Nikon CT Pro 3D"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a ada:XCTImageCollection ;
    ada:beamFilterMaterial "copper" ;
    ada:beamFilterThickness 5e-01 ;
    ada:detectorBinning "1x1" ;
    ada:detectorSize "2048x2048" ;
    ada:detectorType "flat panel" ;
    ada:imageExposure 5e-01 ;
    ada:imageSize "2048x2048" ;
    ada:instrumentType "micro-CT" ;
    ada:numberOfFramesAveragedPerProjection 4 ;
    ada:numberOfProjections 1440 ;
    ada:numberOfSlices 2000 ;
    ada:reconstructedDataFormat "16-bit TIFF" ;
    ada:reconstructedVoxelSize "5.0 micrometer" ;
    ada:reconstructionSoftware "Nikon CT Pro 3D" ;
    ada:rotationAngle "360 degrees" ;
    ada:rotationType "step-and-shoot" ;
    ada:sourceToDetectorDistance "500 mm" ;
    ada:sourceToObjectDistance 2e+02 ;
    ada:xraySource "sealed tube" ;
    ada:xrayTargetMaterial "tungsten" ;
    ada:xrayTubeCurrent 1e-01 ;
    ada:xrayTubeEnergy 1.2e+02 ;
    ada:xrayTubePower 1.2e+01 .


```

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
  ada:beamFilterMaterial:
    type: string
  ada:beamFilterThickness:
    type: number
  ada:dataRangeLower:
    type: integer
  ada:dataRangeUpper:
    type: integer
  ada:detectorGain:
    type: string
  ada:detectorBinning:
    type: string
  ada:detectorSize:
    type: string
  ada:detectorType:
    type: string
  ada:imageExposure:
    type: number
  ada:imageFPS:
    type: string
  ada:imageGain:
    type: number
  ada:imageSize:
    type: string
  ada:instrumentType:
    type: string
  ada:nsiBeamHardening:
    type: number
  ada:numberOfFramesAveragedPerProjection:
    type: integer
  ada:numberOfProjections:
    type: integer
  ada:numberOfSlices:
    type: integer
  ada:pixelPitch:
    type: string
  ada:reconstructedDataFormat:
    type: string
  ada:reconstructedVoxelSize:
    type: string
  ada:reconstructionSoftware:
    type: string
  ada:rotationAngle:
    type: string
  ada:rotationType:
    type: string
  ada:sourceToDetectorDistance:
    type: string
  ada:sourceToObjectDistance:
    type: number
  ada:subPixGrid:
    type: string
  ada:subPixShift:
    type: string
  ada:xraySource:
    type: string
  ada:xrayTargetMaterial:
    type: string
  ada:xrayTubeCurrent:
    type: number
  ada:xrayTubeEnergy:
    type: number
  ada:xrayTubePower:
    type: number
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailXCT/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailXCT/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailXCT/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/detailXCT`

