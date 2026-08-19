# ADA Geochemistry Building Blocks

> **⚠ Superseded — development has moved to [amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks).**
> This repository is archived and read-only. The active, self-contained home for the geochemistry
> building blocks and the TAPP schema-generation pipeline is now the amds-ldeo copy; the TAPP source
> tables live in [amds-ldeo/tapp](https://github.com/amds-ldeo/tapp). Please open issues and PRs
> there. This repo is retained for history only.

Modular metadata schema components for documenting geochemical analytical Methods and Datasets.  Built using the [OGC Building Blocks](https://opengeospatial.github.io/bblocks/) pattern.

The scheme involves three components:

1. A Technique-Aligned protocol (TAPP) that defines a analytical procedure, including kinds of samples used, target analytes, instruments used, sample preparation, analysis workflow and data reduction.  In the TAPP definition, some of these might be specified as fixed, some might have default values, and some are expected to be specified a the individual session level.  The fixed properties are the necessary properties that define the TAPP.  There are also properties that apply as the analytical session (or 'analysis event') level, and properties that are specific to the description of individual analytes. The authoritative protocol definition is in an Excel workbook.  For discussion purposes, the label 'property' is used for properties in the TAPP that are fixed, and 'parameter' for properties that may be adjusted at the session level. Parameters may have default values specified in the TAPP definition.

2. A building block JSON schema specific to the protocol. This protocol definition object is registered in a protocol registry and accessible via its URI. The TAPP definition is referenced as a measurementTechnique in dataset metadata. 

3. A technique-specific 'detail' building block JSON schema that defines the parameters that may be assigned values at the individual dataset level. There is one detail block per technique under `_sources/analysisSpecificDetails/` (e.g. `detailEMPA`), not a single 'details' file. The content of this schema is included in the schema for dataset instances to create a metadata schema for Datasets conforming to the profile. Session-level and per-analyte parameters are defined once in a registered parameter registry (`parameterValues`) and referenced from the detail blocks by URI, so a parameter can be reused across detail definitions; the references are resolved inline into the published resolved schema.

## Structure

### techniqueProtocols (TAPP definitions + shared catalogs)

```
_sources/techniqueProtocols/
  analyteColumns/        ← registered BB: schema:PropertyValueSpecification $defs per analyte column
  parameterTemplates/    ← registered BB: PropertyValueSpecification $defs (readOnly:true params)
  parameterValues/       ← registered BB: schema:PropertyValue $defs (readOnly:false params)
  vocab/                 ← catalog: schema:DefinedTermSet files (referenced by @id, not $ref)
  tappDefinition/        ← base TAPP definition (JSON-LD class ada:TAPPDefinition)
  empaTAPP/              ← concrete TAPP profile (EMPA)
  laicpmsTAPP/           ← concrete TAPP profile (LA-ICP-MS)
  <future>TAPP/          ← additional TAPPs `$ref` the catalogs above
```

`analyteColumns`, `parameterTemplates`, and `parameterValues` are each a **registered type-library building block** (`bblock.json` with `isTypeLibrary: true`): every entry lives as a named `$def` in the catalog's `schema.yaml`, and TAPP / detail blocks reference them by URI fragment (`$ref: …/<catalog>/schema.yaml#/$defs/<name>`). Because they are registered, the OGC bblocks `annotate` step resolves those refs **locally via the register** and inlines them into `resolvedSchema.json`. This matters: a *loose* helper file (a plain `<name>.json` not inside a registered BB) is instead fetched from the published gh-pages URL, which 404s on moved or unpublished paths (`process-bblocks.yml` sets `skip-pages: true`, so gh-pages never auto-updates) — that fragility is why the catalogs were promoted to registered BBs. `vocab/` is the exception: it stays a plain catalog of `schema:DefinedTermSet` files because it is referenced only by JSON-LD `@id` (`schema:inDefinedTermSet`), never by `$ref`, so the `annotate` step never fetches it.

The catalog dirs are **shared dictionary resources** — multiple TAPP profiles `$ref` the same files when their definitions match. The tooling's `share_or_write_catalog` helper lets a TAPP regen overwrite its own entries (matched by `$id` ownership) but errors out on a collision with an entry originated by a different TAPP, so a new TAPP either reuses identical catalog entries or surfaces a renaming requirement.

- `tappDefinition` — base TAPP. Defines the `WorkflowHowTo` / `WorkflowStep` / `MethodParameter` / `AnalyteColumn` / `AnalyteIdentifierColumn` `$defs` that concrete TAPP profiles extend.
- `empaTAPP` — Electron Microprobe Analysis. Extends `tappDefinition` via `allOf` with EPMA top-level properties + `ada:methodParameters` / `ada:analyteTemplate.ada:analyteColumns` constraints referencing the shared catalogs. Generated from `docs/TAPP_EPMA_filled.xlsx` (the canonical TAPP template). 11 examples ship with the BB (10 publication-derived instances + a comprehensive synthetic example).
- `laicpmsTAPP` — LA-ICP-MS. Built from `docs/TAPP_LAICPMS_filled.xlsx` (reshaped from the `LA-ICPMS_TAPP_v8.xlsx` source workbook).

### analysisSpecificDetails detail blocks (per-dataset values)

The 16 technique-specific detail blocks live under `_sources/analysisSpecificDetails/` (`detailEMPA`, `detailXRD`, `detailARGT`, …). Each pairs with a TAPP definition and carries the per-instance values. (The old `details` umbrella BB — an `anyOf` over the detail blocks — was unused and has been removed.)

- `detailEMPA` — paired with `empaTAPP`. Carries `readOnly:false` parameter values as `schema:additionalProperty[]` PropertyValue entries. The `schema:additionalProperty` constraint is inline in detailEMPA's `allOf` (no separate `parametersConstraint.yaml`), with `anyOf` branches `$ref`ing the `parameterValues` registry `$defs`. References the empaTAPP definition via `schema:measurementTechnique` `anyOf` (by `@id` ref or inline). 11 paired examples (`exampledetailEMPA-P1.json` … `-P10.json` + `-all.json`).

The split was made on 2026-04-28: parameters in the TAPP spreadsheet route to `empaTAPP/methodParameters[]` (readOnly:true) or `detailEMPA/schema:additionalProperty[]` (readOnly:false). Method-level constants (the `ada:xxxDefault` top-level properties) stay on the TAPP.

### profiles/geochemProfiles (technique-specific dataset profiles)

`profiles/geochemProfiles/` (alongside `profiles/adaProfiles/`) holds technique profiles that compose a TAPP definition + detail block on top of `adaProduct`:

- `empaProfile` — extends `adaProduct` with `schema:measurementTechnique` `anyOf` pointing at empaTAPP and a `schema:distribution.schema:hasPart` branch that lets `detailEMPA` appear.
- `LA-ICPMS` — extends `adaProduct` with `schema:measurementTechnique` wired to laicpmsTAPP.

### geochemProperties (property building blocks)

Property building blocks that define ADA-specific metadata elements: file types, instrument details, technique-specific data structures, spatial registration, and more. (The technique-specific `detail<XXX>` blocks that previously lived here now reside under `analysisSpecificDetails/`.)

Key building blocks that extend CDIF core BBs:
- **instrument** — extends core CDIF instrument (`schema:Product` with `nxs:BaseClass/NXinstrument` in `additionalType`)
- **laboratory** — extends core CDIF spatialExtent (`schema:Place` with `nxs:BaseClass/NXsource` in `additionalType`)

### adaProfiles (36 resource type profiles)

Metadata profiles that compose property building blocks with CDIF base schemas:

- **adaProduct** — base ADA product profile, composes via `allOf`:
  - `cdifCore` — core metadata properties
  - `cdifDataDescription` — variableMeasured with DDI-CDI extensions, `@id` requirement
  - `cdifManifest` — archive distribution with `hasPart` component files (was `cdifArchiveDistribution` in CDIF ≤1.0)
  - `cdifProvenance` — `prov:wasGeneratedBy` provenance activities
  - ADA-specific: technique types, instrument/lab/sample overlays, `ada:componentType`
- **35 technique profiles** — technique-specific constraints on `ada:componentType` values (e.g., adaSEM, adaXRD, adaICPMS, adaTEM)

## componentType architecture

Each archive `hasPart` item carries an `ada:componentType` (a single string like `ada:EMPAImageMap`) that classifies the file. The architecture enforces a two-level constraint:

1. **File type ↔ componentType mapping** — each file-type building block (`image`, `imageMap`, `tabularData`, `collection`, `dataCube`, `document`, `supDocImage`, `otherFile`) declares a sealed `enum` of valid componentType values. The enum is derived from the **Components worksheet** of `amds-ldeo/metadata/ADA-AnalyticalMethodsAndAttributes.xlsx` (the canonical mapping). E.g. `ada:EMPAImageMap` is valid only on parts whose `@type` includes `ada:imageMap`.

2. **Profile-level constraint** — a technique profile's `schema:hasPart.items` uses a schema-level `anyOf` with three kinds of branch: (a) `$ref` to `adaProduct/$defs/universalComponentTypeBranch` (factored once, used everywhere) for universal componentTypes; (b) inline string-enum for technique-specific componentTypes that have no detail block; (c) `$ref` to a technique-specific *detail* schema (e.g. `detailEMPA`) which pins `ada:componentType` to its technique consts and contributes detail-specific sibling properties (e.g. `ada:spectrometersUsed`, `ada:signalUsed`) flat on the hasPart item — not nested inside componentType.

### Refreshing the mapping

After editing the Components worksheet:

```
python tools/apply_componentType_enums.py --refresh \
    --xlsx ../../amds-ldeo/metadata/ADA-AnalyticalMethodsAndAttributes.xlsx
python tools/regenerate_schema_json.py
python tools/resolve_schema.py --all
python tools/validate_examples.py
```

The cached mapping at `tools/componentType_enum_cache.json` is committed so the apply step works on a fresh clone without spreadsheet access.

## Cross-repo imports

This repository imports shared schema.org and CDIF property building blocks from [metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks) via the OGC Building Blocks import mechanism. All external references use absolute URLs (`https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/...`).

## Viewer

Browse the building blocks at: https://usgin.github.io/geochemBuildingBlocks/

## Tools

### TAPP / detail / profile generation pipeline (4 scripts)

The end-to-end pipeline for adding a new technique profile from a filled-in TAPP template spreadsheet. See [docs/TAPP_TEMPLATE_GUIDE.md](docs/TAPP_TEMPLATE_GUIDE.md) for what to put in the spreadsheet.

```
python tools/build_TAPP_from_spreadsheet.py [TAPP_NAME]  [XLSX_PATH] [--pub Pn]…  # 1. TAPP BB + catalogs
python tools/build_detail_BB.py             [TAPP_NAME]  [XLSX_PATH] [--pub Pn]…  # 2. detail BB + parameterValues
python tools/build_profile_BB.py            [TAPP_NAME]                            # 3. profile BB scaffold
python tools/build_dataset_template.py      <tapp-instance.json>                   # 4. xlsx data-entry template
                                            [<out.xlsx>]
```

All four scripts default to `empaTAPP` / `docs/TAPP_EPMA_filled.xlsx` for back-compat. The shared library at `tools/_tapp_lib.py` does the heavy lifting (parser, catalog emit helpers, scaffolders); the four drivers are thin wrappers. The library is parameterized for multiple TAPPs via a `TAPP_PROFILES` / `CFG` mechanism, so `empaTAPP` and `laicpmsTAPP` share the same generator (it was previously EMPA-hardcoded).

`--pub <code>` (repeatable) on scripts 1 and 2 limits which publication-derived examples get regenerated — useful when migrating pub columns one at a time.

### Publication migration helper

```
python tools/interpret_pub_analytes.py            # preview only (review files)
python tools/interpret_pub_analytes.py --apply    # also rewrite source xlsx
```

Reads publication columns whose analyte axis isn't explicitly populated and infers it from rows 48 / 59 / 64 (Halogen Correction / Primary Calibration Standard / Typical Detection Limit). Default-mode outputs:
- `docs/TAPP_EPMA_filled-interp.xlsx` — side workbook with each `<pub>-interp` column inserted right after its source pub for side-by-side review.
- `build/interp-review/example<empaTAPP|detailEMPA>-<pub>-interp.json` — paired review JSON instances built from the inferred data.

With `--apply`, additionally rewrites rows 32 / 40 / 59 / 64 of each inferred pub column in `docs/TAPP_EPMA_filled.xlsx` to the pipe-delim convention. After migration, the regular pipeline (`build_TAPP_from_spreadsheet.py` etc.) reproduces the same rich examples directly from the source — no interp loop needed.

Detection-limit values keep their full text per element (e.g. `"SiO2: 0.02 wt%"`, `"<0.03 wt% for TiO2"`) so context isn't lost in the migration.

### Schema generation and resolution

- `tools/generate_profiles.py` — generates technique-specific profile building blocks from configuration data
- `tools/resolve_schema.py` — resolve all `$ref` into a structured `resolvedSchema.json` (`$defs` + internal `$ref`, recursion-safe and ~88–90% smaller than the old fully-inlined form, which is no longer emitted; `--structured` is now a no-op)
- `tools/regenerate_schema_json.py` — generate *Schema.json from schema.yaml sources (YAML→JSON + ref rewrite)

### Validation and auditing

- `tools/audit_building_blocks.py` — comprehensive audit: file completeness, schema consistency, resolvedSchema freshness (via the structured resolver), SHACL coverage. `isTypeLibrary` BBs (reusable `$defs` libraries with no instantiable root class, e.g. `stringArray`, `parameterValues`) are exempt from the standalone-example and SHACL-NodeShape requirements.
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

## TAPP Definition Building Block

The `tappDefinition` building block at `techniqueProtocols/tappDefinition/` defines a registry-backed Technique-Aligned Protocol Profile (TAPP) definition schema (v3). Was previously `methodDefinition`. A TAPP definition is modeled as a `cdi:Activity` + `schema:Action` + `ada:TAPPDefinition` + `bios:LabProtocol`.

### Structure

- **TAPP identity** (top level) — name, DOI, version, `schema:measurementTechnique`, `schema:object` (target materials), instrument, `schema:location` (laboratory/facility), software (`bios:computationalTool`), reagents (`bios:reagent`), agent
- **Standard workflow** (`schema:actionProcess`) — a `schema:HowTo` containing ordered `cdi:Activity` + `schema:Action` steps: sample preparation, calibration, data acquisition, data processing, quality control
- **Parameters** — typed as `schema:PropertyValueSpecification` with `schema:readonlyValue`, `schema:valueRequired`, `schema:defaultValue`, `schema:minValue`/`maxValue`, `schema:inDefinedTermSet` (SKOS vocabulary link), and `ada:fieldScope` (method/session/element)
- **Analyte template** (`ada:analyteTemplate`) — per-element column definitions (also `PropertyValueSpecification`) and default analyte rows
- **Quality metrics** (`dqv:hasQualityMeasurement`) — at method level and on workflow steps

### Examples

Example files use the sibling `example<bbName>-<variant>.json` pattern (validated by `tools/validate_examples.py`):

- `exampletappDefinition-concord-glass-v1-0-6.json` — EPMA WDS tephra glass (Concord University)
- `exampletappDefinition-nmnh-spinel-oxybar-v1.json` — EPMA WDS spinel oxybarometry (Smithsonian NMNH)
- `exampletappDefinition-uoc-laicpms-glass-v1.json` — LA-ICP-MS volcanic glass trace elements (University of Cologne)

For the empaTAPP profile: 10 publication-derived examples (`exampleempaTAPP-P1.json` … `exampleempaTAPP-P10.json`) plus `exampleempaTAPP-all.json`, a hand-authored comprehensive synthetic instance that exercises every property allowed by the resolved schema. Use the latter as a structural reference when authoring new TAPP profiles or onboarding new authors.

### Vocabularies used

- [Bioschemas](https://bioschemas.org/) — `bios:LabProtocol`, `bios:LabProcess`, `bios:computationalTool`, `bios:reagent`
- [DDI-CDI](https://ddialliance.org/Specification/DDI-CDI/1.0/) — `cdi:Activity` for workflow steps
- [W3C DQV](https://www.w3.org/TR/vocab-dqv/) — `dqv:hasQualityMeasurement` for quality metrics
- [schema.org](https://schema.org/) — `PropertyValueSpecification` for parameter definitions, `Action`/`HowTo`/`HowToStep` for workflow

## License

[Apache 2.0](LICENSE)
