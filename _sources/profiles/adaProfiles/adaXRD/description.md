# ADA XRD Profile

Technique-specific metadata profile for X-ray Diffraction (XRD) products in the Astromat Data Archive. XRD measures the diffraction pattern produced by X-rays interacting with crystalline materials to determine crystal structure, phase identification, and lattice parameters.

## Product Types
- **XRD Tabular** - Diffraction pattern data in tabular format (2-theta vs. intensity)

## Valid Component Types
- `ada:XRDTabular` - Tabular diffraction data with geometry and wavelength detail (xrd_detail)
- `ada:XRDDiffractionPattern` - Diffraction pattern images
- `ada:XRDIndexedImage` - Indexed diffraction pattern images
- `ada:instrumentMetadata` - Instrument metadata documents
- `ada:methodDescription` - Method description documents

## Detail Type
`xrd_detail` with properties: `geometry`, `sampleMount`, `stepSize`, `timePerStep`, `wavelength`
