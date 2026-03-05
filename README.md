# ADA Geochemistry Building Blocks

Modular metadata schema components for the [Astromat Data Archive (ADA)](https://astromat.org), built using the [OGC Building Blocks](https://opengeospatial.github.io/bblocks/) pattern.

## Structure

### adaProperties (31 schema components)

Property building blocks that define ADA-specific metadata elements: file types, instrument details, technique-specific data structures, spatial registration, and more.

### adaProfiles (36 resource type profiles)

Metadata profiles that compose property building blocks with CDIF base schemas:

- **adaProduct** — base ADA product profile (composes cdifMandatory + cdifOptional + ADA properties)
- **35 technique profiles** — technique-specific constraints (e.g., adaSEM, adaXRD, adaICPMS, adaTEM)

## Cross-repo imports

This repository imports shared schema.org and CDIF property building blocks from [metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks) via the OGC Building Blocks import mechanism.

## Viewer

Browse the building blocks at: https://usgin.github.io/geochemBuildingBlocks/

## Tools

- `tools/generate_profiles.py` — generates technique-specific profile building blocks from configuration data

## License

[Apache 2.0](LICENSE)
