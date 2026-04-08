# Analytical Method Definition

A registered analytical method description that can be referenced by metadata records. Methods are typed as `ada:MethodDefinition` and `schema:HowTo`.

## Structure

A method definition contains:

- **Identity** -- name, DOI/URI, version, measurement technique (DefinedTerm), instrument specification (via CDIF instrument building block), laboratory
- **`ada:methodParameters`** -- array of operating parameters, each carrying:
  - `ada:scope`: `constant` (fixed for all sessions), `default` (editable with default value and constraints), or `optional` (available on demand)
  - `ada:category`: grouping label for form layout (e.g. "Beam Conditions", "Data Processing")
  - `schema:value`: the constant or default value
  - `schema:minValue` / `schema:maxValue` / `ada:enumeration`: constraints for validation
  - `ada:cdifPropertyPath`: mapping to CDIF JSON-LD output path
  - `ada:tier`: M/R/O validation strictness
- **`ada:analyteTemplate`** -- per-analyte column definitions and pre-populated analyte rows. Each analyte row becomes a `schema:variableMeasured` / `cdi:InstanceVariable` entry in metadata records. Analyte-specific parameters (X-ray line, crystal, counting time, calibration standard) are serialised as `schema:additionalProperty` within each variableMeasured entry.

## Form integration

When a user selects a method in the ada_metadata_forms (Tab 3):
1. Constant parameters render as a read-only summary
2. Default parameters render as editable fields pre-filled with defaults
3. Optional parameters are available via an "Add property" picker
4. The analyte template pre-populates the variables measured table
5. Method-level parameters serialise into `prov:wasGeneratedBy` activity `schema:additionalProperty`

## Dependencies

- [instrument](../instrument/) -- instrument specification
- [laboratory](../laboratory/) -- laboratory/facility
- CDIF [definedTerm](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/definedTerm/) -- measurement technique classification
- CDIF [identifier](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/identifier/) -- method DOI
- CDIF [person](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/person/) -- method creator
- CDIF [labeledLink](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/labeledLink/) -- method references
- CDIF [monetaryGrant](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/monetaryGrant/) -- funding
