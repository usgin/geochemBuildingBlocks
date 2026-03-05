# ADA ICP-MS Profile

Technique-specific metadata profile for Inductively Coupled Plasma Mass Spectrometry (ICP-MS) products in the Astromat Data Archive. ICP-MS measures elemental and isotopic concentrations by ionizing samples in an argon plasma and separating ions by mass-to-charge ratio. This profile covers HR-ICP-MS (high resolution), Q-ICP-MS (quadrupole), and MC-ICP-MS (multi-collector) variants.

## Product Types
- **HR-ICP-MS Processed/Raw** - High-resolution ICP-MS data
- **Q-ICP-MS Processed/Raw** - Quadrupole ICP-MS data
- **MC-ICP-MS Raw/Processed** - Multi-collector ICP-MS data

## Valid Component Types
- `ada:HRICPMSProcessed` - HR-ICP-MS processed tabular data
- `ada:HRICPMSRaw` - HR-ICP-MS raw tabular data or documents
- `ada:QICPMSProcessedTabular` - Q-ICP-MS processed tabular data
- `ada:QICPMSRawTabular` - Q-ICP-MS raw tabular data
- `ada:MCICPMSTabular` - MC-ICP-MS tabular data
- `ada:MCICPMSCollection` - MC-ICP-MS data collections
- `ada:MCICPMSRaw` - MC-ICP-MS raw documents (e.g., Neptune Plus .exp files)
- `ada:methodDescription` - Method description documents
- `ada:instrumentMetadata` - Instrument metadata documents
- `ada:calibrationFile` - Calibration documents

## Detail Type
No ICP-MS-specific detail type; component types are enum-only.
