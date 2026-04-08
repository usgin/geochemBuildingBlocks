# Analytical Method Definition v3

A registered analytical method definition modeled as a `cdi:Activity` + `schema:Action`. The method itself is the activity; its standard workflow is encoded in `schema:actionProcess`.

## Changes from v2

- **Root type**: `cdi:Activity` + `schema:Action` + `ada:MethodDefinition` + `bios:LabProtocol` (replaces `schema:HowTo` at root)
- **Target material**: `schema:object` carries the material(s) the method analyses (e.g. silicate glass, olivine)
- **Method author**: `schema:agent` replaces `schema:creator`
- **Workflow**: `schema:actionProcess` holds a `schema:HowTo` with ordered `cdi:Activity` + `schema:Action` steps
- **Sample preparation**: now a workflow step, not a separate property
- **Parameters distributed**: step-specific parameters live on their workflow steps; only method-wide parameters remain at top level

## Structure

### Method identity (top level)
- `schema:name`, `schema:identifier`, `schema:version`, `schema:datePublished`
- `schema:measurementTechnique` — DefinedTerm from controlled vocabulary
- `schema:object` — target material(s) as DefinedTerm or text
- `schema:instrument` — primary instrument with manufacturer, model, sub-components
- `bios:computationalTool` — software tools (method-wide)
- `bios:reagent` — reference materials used across multiple steps
- `ada:laboratory` — laboratory/facility
- `schema:agent` — method author (person or organisation)

### Standard workflow (`schema:actionProcess`)
A `schema:HowTo` containing `schema:step` — an ordered array of `cdi:Activity` + `schema:Action` items. Typical steps:

1. **Sample preparation** (`bios:LabProcess`) — mounting, polishing, coating
2. **Instrument calibration** — primary/secondary standards, spectrometer setup
3. **Data acquisition** — beam conditions, per-element parameters (linked to `ada:analyteTemplate`)
4. **Data processing** — matrix correction, TDI, blank/normalization corrections
5. **Quality control** — drift monitoring, precision/accuracy assessment

Each workflow step can carry:
- `ada:methodParameters` — typed parameters with scope, fieldScope, tier
- `schema:additionalProperty` — simple PropertyValue parameters
- `bios:reagent` — step-specific standards and materials
- `bios:computationalTool` — step-specific software
- `schema:instrument` — step-specific equipment
- `prov:used` / `schema:result` / `schema:object` — input/output chaining
- `schema:actionProcess` — nested sub-workflow
- `dqv:hasQualityMeasurement` — step-specific quality metrics

### Per-analyte parameters (`ada:analyteTemplate`)
Unchanged from v1/v2. Defines columns and default rows for the element table.

### Quality metrics (`dqv:hasQualityMeasurement`)
Method-level quality metrics using CDIF qualityMeasure building block. Step-specific metrics can also appear on workflow steps.

## Dependencies

- [instrument](../instrument/) — instrument specification
- [laboratory](../laboratory/) — laboratory/facility
- CDIF [definedTerm](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/definedTerm/) — technique, target material
- CDIF [identifier](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/identifier/) — method DOI
- CDIF [person](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/person/) — method author
- CDIF [labeledLink](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/labeledLink/) — method references
- CDIF [monetaryGrant](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/monetaryGrant/) — funding
- CDIF [qualityMeasure](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/qualityProperties/qualityMeasure/) — quality metrics
- CDIF [bioschemasProperties](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/bioschemasProperties/cdifBioschemasProperties/) — Bioschemas vocabulary
- DDI-CDI [Activity](https://docs.ddialliance.org/DDI-CDI/1.0/model/FieldLevelDocumentation/DDICDILibrary/Classes/Process/Activity.html) — activity model
