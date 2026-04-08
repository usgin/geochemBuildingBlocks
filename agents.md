# ADA Geochemistry Building Blocks -- Agent Guide

Technical reference for AI coding agents working in this repository.

## Repository purpose

Modular metadata schema components for the Astromat Data Archive (ADA), built on the OGC Building Blocks pattern. Defines JSON Schema building blocks for geochemistry analytical technique metadata, extending shared CDIF base schemas.

## Directory layout

```
_sources/
  geochemProperties/       31 property building blocks (instrument, laboratory, file types, technique details)
  profiles/adaProfiles/    36 metadata profiles (adaProduct base + 35 technique profiles)
build/                     Generated outputs (register.json, annotated schemas, RDF exports, reports)
tools/                     Python tooling for generation, validation, and auditing
.github/workflows/         CI: OGC postprocess, viewer deployment
```

## Building block structure

Each building block directory contains a standard set of files:

- `schema.yaml` -- canonical JSON Schema source (Draft 2020-12)
- `*Schema.json` -- generated JSON equivalent of schema.yaml (via `regenerate_schema_json.py`)
- `bblock.json` -- OGC Building Block metadata (name, status, version, tags)
- `description.md` -- human-readable documentation
- `examples.yaml` -- usage examples for validation testing
- `context.jsonld` -- JSON-LD context for RDF mapping
- `resolvedSchema.json` -- fully inlined schema (all $refs resolved, via `resolve_schema.py`)
- `rules.shacl` -- SHACL validation shapes

Profiles additionally compose base schemas via `allOf` references.

## Schema composition pattern

- Property blocks define ADA-specific metadata elements
- `adaProduct` profile composes four CDIF base schemas (`cdifCore`, `cdifDataDescription`, `cdifArchiveDistribution`, `cdifProvenance`) plus ADA overlays via `allOf`
- 35 technique profiles extend `adaProduct` with technique-specific `ada:componentType` constraints
- External schemas are referenced via full HTTP URLs to `cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/`
- Local schemas use relative `$ref` paths (e.g., `../stringArray/schema.yaml`)

## Key identifiers

- **Identifier prefix:** `ada.bbr.metadata.`
- **Import source:** `https://usgin.github.io/metadataBuildingBlocks/build/register.json`
- **Viewer URL:** `https://usgin.github.io/geochemBuildingBlocks/`

## Tools

### Schema generation and resolution

| Tool | Purpose |
|------|---------|
| `generate_profiles.py` | Generate technique profile building blocks from config data. Run with `--list` to see all profiles, or pass a profile name to regenerate one. |
| `regenerate_schema_json.py` | Sync `*Schema.json` from `schema.yaml` sources. Use `--dry-run` to preview. |
| `resolve_schema.py` | Resolve all `$ref` into single `resolvedSchema.json`. Supports `--all`, `--structured`, `--flatten-allof`. Canonical copy from metadataBuildingBlocks. |

### Validation and auditing

| Tool | Purpose |
|------|---------|
| `audit_building_blocks.py` | Comprehensive audit: file completeness, schema.yaml vs JSON consistency, resolvedSchema freshness, example validation, SHACL coverage. Run with `--filter <name>` or `--json -o report.json`. |
| `audit_shacl_coverage.py` | Check SHACL rules cover all schema.yaml properties. Reports missing/extra shapes and severity mismatches. Use `--verbose` for detail. |
| `validate_examples.py` | Validate example JSON files against resolved schemas. Use `--filter` to target specific blocks. |
| `validate_instance.py` | Profile-aware validation of metadata instances. Auto-detects profile from `dcterms:conformsTo`. Supports `--dir`, `--profile`, `--termcode-fallback`. |
| `compare_schemas.py` | Detect drift between schema.yaml and *Schema.json (missing properties, type mismatches). |

### Data collection

| Tool | Purpose |
|------|---------|
| `download_ecl_methods.py` | Download analytical method Excel workbooks from the EarthChem Library. Reads the methods list from a Google Sheet, scrapes ECL record pages for filenames, and POSTs to `dl_multi.php` to download. Supports `--dry-run`, `--output-dir`, `--delay`. Skips already-downloaded files. |

### Build and deployment support

| Tool | Purpose |
|------|---------|
| `augment_register.py` | Add `resolvedSchema` URLs to `build/register.json`. Uses `ada.bbr.metadata.` prefix. Run during CI before viewer deployment. |
| `generate_custom_report.py` | Generate HTML validation report with granular SHACL severity breakdown from OGC postprocess `report.json`. |
| `cors_server.py` | Local HTTP server with CORS headers for testing the viewer. Default port 8090. |

### Tool provenance

`resolve_schema.py` and `regenerate_schema_json.py` are synced from the canonical copies in [metadataBuildingBlocks/tools/](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks/tree/main/tools). Do not edit locally. The audit, validation, and report tools were also sourced from that repository.

## CI/CD pipeline

1. **`process-bblocks.yml`** -- On push to main: runs OGC `bblocks-postprocess` validation, generates `build/register.json`, annotated schemas, RDF exports, `tests/report.json`
2. **`deploy-viewer.yml`** -- After postprocess completes: sets up Python 3.11, runs `augment_register.py` and `generate_custom_report.py`, generates viewer config, deploys to GitHub Pages

## Cross-repo relationships

- **metadataBuildingBlocks** (CDIF) -- upstream source for shared CDIF schemas and canonical tool copies. Schemas imported via OGC building blocks import mechanism.
- **CDIF profile release repos** (`cdif-core`, `discovery`, `codelist`, `dataDescription`) -- standalone repos with schemas, SHACL rules, and validated examples for each CDIF conformance class. Conformance URIs (e.g. `https://w3id.org/cdif/core/1.0`) redirect to profile BBs in metadataBuildingBlocks via w3id.org.
- **ada_metadata_forms** (amds-ldeo) -- Django app that validates ADA metadata. Uses a standalone monolithic JSON Schema (`adaMetadata-SchemaOrgSchema-v3.json`), NOT the modular building blocks. No direct dependency on this repo's build outputs.
- **w3id.org/cdif** -- persistent identifier redirects for CDIF building blocks and conformance URIs. Maintained in smrgeoinfo/w3id.org fork.

## methodDefinition building block (v3)

The `geochemProperties/methodDefinition/` building block defines analytical method definitions as `cdi:Activity` + `schema:Action` + `ada:MethodDefinition` + `bios:LabProtocol`.

- **Workflow:** `schema:actionProcess` contains a `schema:HowTo` with ordered `cdi:Activity` + `schema:Action` steps (sample prep, calibration, acquisition, data processing, QC)
- **Parameters:** typed as `schema:PropertyValueSpecification` with `readonlyValue`, `valueRequired`, `defaultValue`, `minValue`/`maxValue`, `inDefinedTermSet` (SKOS vocabulary), `ada:fieldScope` (method/session/element). Parameters live on their workflow steps; method-wide parameters at top level.
- **Analyte template:** `ada:analyteTemplate` with `PropertyValueSpecification`-typed columns and default analyte rows
- **Vocabularies:** Bioschemas (`bios:computationalTool`, `bios:reagent`, `bios:LabProcess`), DDI-CDI (`cdi:Activity`), DQV (`dqv:hasQualityMeasurement`), SKOS (vocabulary references)
- **Examples:** EPMA glass (Concord), EPMA spinel oxybarometry (NMNH Smithsonian), LA-ICP-MS glass trace elements (U. Cologne)
- **Form integration:** Tab 3 of ada_metadata_forms consumes method definitions from the registry

## Common tasks

**Add a new technique profile:**
```bash
# Edit PROFILES dict in tools/generate_profiles.py, then:
python tools/generate_profiles.py adaNewTechnique
python tools/regenerate_schema_json.py
python tools/resolve_schema.py adaNewTechnique
```

**Audit all building blocks:**
```bash
python tools/audit_building_blocks.py _sources/
python tools/audit_shacl_coverage.py --verbose
python tools/validate_examples.py
```

**Check schema consistency after edits:**
```bash
python tools/compare_schemas.py
python tools/resolve_schema.py --all
```

**Run the viewer locally:**
```bash
python tools/cors_server.py 8090 build/
```
