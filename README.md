# ADA Geochemistry Building Blocks

Modular metadata schema components for the [Astromat Data Archive (ADA)](https://astromat.org), built using the [OGC Building Blocks](https://opengeospatial.github.io/bblocks/) pattern.

## Structure

### geochemProperties (31 schema components)

Property building blocks that define ADA-specific metadata elements: file types, instrument details, technique-specific data structures, spatial registration, and more.

Key building blocks that extend CDIF core BBs:
- **instrument** — extends core CDIF instrument (`schema:Product` with `nxs:BaseClass/NXinstrument` in `additionalType`)
- **laboratory** — extends core CDIF spatialExtent (`schema:Place` with `nxs:BaseClass/NXsource` in `additionalType`)

### adaProfiles (36 resource type profiles)

Metadata profiles that compose property building blocks with CDIF base schemas:

- **adaProduct** — base ADA product profile, composes via `allOf`:
  - `cdifCore` — core metadata properties
  - `cdifDataDescription` — variableMeasured with DDI-CDI extensions, `@id` requirement
  - `cdifArchiveDistribution` — archive distribution with `hasPart` component files
  - `cdifProvenance` — `prov:wasGeneratedBy` provenance activities
  - ADA-specific: technique types, instrument/lab/sample overlays, `ada:componentType`
- **35 technique profiles** — technique-specific constraints on `ada:componentType` values (e.g., adaSEM, adaXRD, adaICPMS, adaTEM)

## Cross-repo imports

This repository imports shared schema.org and CDIF property building blocks from [metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks) via the OGC Building Blocks import mechanism. All external references use absolute URLs (`https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/...`).

## Viewer

Browse the building blocks at: https://usgin.github.io/geochemBuildingBlocks/

## Tools

### Schema generation and resolution

- `tools/generate_profiles.py` — generates technique-specific profile building blocks from configuration data
- `tools/resolve_schema.py` — resolve all `$ref` into single resolvedSchema.json files
- `tools/regenerate_schema_json.py` — generate *Schema.json from schema.yaml sources (YAML→JSON + ref rewrite)

### Validation and auditing

- `tools/audit_building_blocks.py` — comprehensive audit: file completeness, schema consistency, resolvedSchema freshness, SHACL coverage
- `tools/audit_shacl_coverage.py` — check SHACL rules cover all schema.yaml properties; reports missing/extra shapes
- `tools/validate_examples.py` — validate example JSON files against resolved schemas
- `tools/validate_instance.py` — profile-aware validation of ADA metadata instances
- `tools/compare_schemas.py` — detect drift between schema.yaml and *Schema.json

### Build and deployment support

- `tools/augment_register.py` — add resolvedSchema URLs to build/register.json for the viewer
- `tools/generate_custom_report.py` — generate HTML validation report with granular SHACL severity breakdown
- `tools/cors_server.py` — local HTTP server with CORS headers for testing the viewer

### Tool provenance

`resolve_schema.py` and `regenerate_schema_json.py` are synced from the canonical copies in [metadataBuildingBlocks/tools/](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks/tree/main/tools). Do not edit locally — update the canonical copy and run `python tools/sync_resolve_schema.py --apply` from the metadataBuildingBlocks repo. The audit, validation, and report tools were also sourced from that repository.

## License

[Apache 2.0](LICENSE)
