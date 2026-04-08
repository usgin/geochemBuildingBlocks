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

### Data collection

- `tools/download_ecl_methods.py` — download analytical method Excel workbooks from the EarthChem Library. Reads methods list from Google Sheets, downloads available workbooks. Supports `--dry-run`, `--output-dir`.

### Build and deployment support

- `tools/augment_register.py` — add resolvedSchema URLs to build/register.json for the viewer
- `tools/generate_custom_report.py` — generate HTML validation report with granular SHACL severity breakdown
- `tools/cors_server.py` — local HTTP server with CORS headers for testing the viewer

### Tool provenance

`resolve_schema.py` and `regenerate_schema_json.py` are synced from the canonical copies in [metadataBuildingBlocks/tools/](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks/tree/main/tools). Do not edit locally — update the canonical copy and run `python tools/sync_resolve_schema.py --apply` from the metadataBuildingBlocks repo. The audit, validation, and report tools were also sourced from that repository.

## Planned: Method Definition Building Block

A new `methodDefinition` building block is planned to support a **registry of analytical method definitions** that metadata forms can consume at runtime. The full design is in [`G:\My Drive\OneGeochemistry\MethodDefinitionDesign.md`](MethodDefinitionDesign.md) and summarized here.

### Problem

Analytical methods (EPMA, LA-ICP-MS, XRD, etc.) have dozens of operating parameters. Today these live in Excel templates and prose documents. The existing `detail*` blocks (e.g. `detailEMPA` with only `ada:spectrometersUsed` and `ada:signalUsed`) describe file-type metadata, not method configuration. There is no machine-actionable method definition that a form can consume.

### Design

A `methodDefinition` building block typed as `ada:MethodDefinition` + `schema:HowTo` containing:

1. **Identity** — name, DOI, version, `schema:measurementTechnique` (DefinedTerm), instrument spec (reusing CDIF instrument BB), laboratory.

2. **`ada:methodParameters`** — array of parameter objects, each carrying:
   - `ada:scope`: `constant` | `default` | `optional` — controls form rendering
   - `ada:category` — grouping label for form layout
   - `schema:value` — constant or default value
   - `schema:minValue`/`schema:maxValue`/`ada:enumeration` — constraints
   - `ada:cdifPropertyPath` — mapping to CDIF JSON-LD output path
   - `ada:tier` — M/R/O validation strictness

3. **`ada:analyteTemplate`** — per-element column definitions and pre-populated analyte rows. These become `schema:variableMeasured` entries in metadata records.

### Scope tiers

| Scope | Form behaviour |
|-------|---------------|
| `constant` | Read-only summary text, fixed for all sessions |
| `default` | Editable field, pre-filled with default, validated against min/max/enum |
| `optional` | Available via "Add property" picker, not shown by default |

### Integration with ada_metadata_forms

Selecting a technique on Tab 3 populates a Method dropdown from the registry. Selecting a method auto-generates: a read-only summary of constants, editable fields for defaults, an analyte table from the template. JSON-LD export references the method by `@id` in `schema:actionProcess`.

### Implementation phases

1. **Building block schema** — `geochemProperties/methodDefinition/` in this repo
2. **Registry backend** — PostgreSQL table + API in amds-ldeo/metadata
3. **Form integration** — Tab 3 updates in ada_metadata_forms
4. **Seed data** — Convert OneGeochemistry EPMA workbooks to method definition instances

### Source analysis

The design was informed by analysis of:
- OneGeochemistry EPMA-SEM Excel templates (40+ filled method workbooks)
- EPMA Metadata Profile v1.0 (docx, 73-field reference profile with M/R/O tiers)
- SMRTable (xlsx, scope annotations per field: technique/method/session/event)
- CDIF metadataBuildingBlocks (cdifProvActivity, instrument, qualityMeasure, etc.)
- Existing geochemBuildingBlocks detail* schemas

An integrated EPMA template (`EPMA_Integrated_Method_Template_v1.xlsx`) with CDIF/geochem BB mapping columns was produced as part of this analysis; it lives in `G:\My Drive\OneGeochemistry\AnalyticalMethodTemplates\`.

## License

[Apache 2.0](LICENSE)
