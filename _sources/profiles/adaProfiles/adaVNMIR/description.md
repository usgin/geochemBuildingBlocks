# ADA VNMIR Profile

Technique-specific metadata profile for Very-Near Mid-Infrared (VNMIR) and FTIR spectroscopy products in the Astromat Data Archive. VNMIR/FTIR measures the infrared absorption and emission of materials to determine molecular composition and structure, used extensively for mineral identification in planetary and terrestrial samples.

## Product Types
- **VNMIR Point** - Single-point spectral measurements
- **VNMIR Overview Image** - Overview image maps with spectral registration
- **VNMIR Spectral Map** - Hyperspectral data cubes

## Valid Component Types
- `ada:VNMIRSpectralPoint` - Point spectral measurements in tabular format (vnmir_detail)
- `ada:VNMIROverviewImage` - Overview image maps with spectral context (vnmir_detail)
- `ada:VNMIRSpectralMap` - Hyperspectral data cubes (vnmir_detail)
- `ada:VNMIRSpectraPlot` - Spectral plot images or documents
- `ada:analysisLocation` - Analysis location images
- `ada:instrumentMetadata` - Instrument metadata documents
- `ada:methodDescription` - Method description documents

## Detail Type
`vnmir_detail` with 20+ properties including: `detector`, `beamsplitter`, `calibrationStandards`, `comments`, `numberOfScans`, `eMaxFitRegionMin/Max`, `emissionAngle`, `emissivityMaximum`, `environmentalPressure`, `incidenceAngle`, `measurement`, `measurementEnvironment`, `phaseAngle`, `sampleHeated`, `samplePreparation`, `sampleTemperature`, `spectralRangeMin/Max`, `spectralResolution`, `spectralSampling`, `spotSize`, `uncertaintyNoise`, `vacuumExposedSample`
