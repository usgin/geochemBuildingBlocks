
# Analytical Method Definition (Schema)

`ada.bbr.metadata.geochemProperties.methodDefinition` *v0.1*

A registered analytical method description containing identity, instrument specification, scope-tagged operating parameters (constant/default/optional), and per-analyte parameter templates. Typed as ada:MethodDefinition and schema:HowTo. Defines properties: @type, schema:name, schema:identifier, schema:version, schema:measurementTechnique, schema:instrument, ada:laboratory, ada:methodParameters, ada:analyteTemplate, schema:creator, schema:relatedLink, schema:funding.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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

## Examples

### EPMA Method Definition Example (abbreviated)
Electron Microprobe Analysis method definition for spinel oxybarometry
at NMNH Smithsonian. Shows constant beam conditions, default software,
and an analyte template with two default analytes.
#### json
```json
{
  "@id": "https://registry.onegeochemistry.org/methods/nmnh-spinel-oxybar-v1",
  "@type": ["ada:MethodDefinition", "schema:HowTo"],
  "schema:name": "Spinel oxybarometry version 1",
  "schema:version": "1.0",
  "schema:datePublished": "2013-11-08",
  "schema:measurementTechnique": {
    "@type": ["schema:DefinedTerm"],
    "schema:name": "EPMA-WDS",
    "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques"
  },
  "schema:instrument": {
    "@type": ["schema:Product", "schema:Thing"],
    "schema:name": "JEOL JXA-8900 Superprobe",
    "schema:manufacturer": {
      "@type": ["schema:Organization"],
      "schema:name": "JEOL"
    },
    "schema:model": {
      "@type": ["schema:ProductModel"],
      "schema:name": "JXA-8900"
    }
  },
  "ada:methodParameters": [
    {
      "schema:name": "acceleratingVoltage",
      "schema:alternateName": "Accelerating Voltage",
      "ada:scope": "constant",
      "ada:category": "Beam Conditions",
      "ada:dataType": "number",
      "schema:value": 15,
      "schema:unitText": "kV",
      "ada:tier": "M",
      "ada:cdifPropertyPath": "cdifProvActivity: schema:additionalProperty"
    },
    {
      "schema:name": "beamCurrent",
      "schema:alternateName": "Beam Current",
      "ada:scope": "constant",
      "ada:category": "Beam Conditions",
      "ada:dataType": "number",
      "schema:value": 40,
      "schema:unitText": "nA",
      "ada:tier": "M",
      "ada:cdifPropertyPath": "cdifProvActivity: schema:additionalProperty"
    },
    {
      "schema:name": "matrixCorrectionModel",
      "schema:alternateName": "X-ray Matrix Corrections",
      "ada:scope": "constant",
      "ada:category": "Data Processing",
      "ada:dataType": "string",
      "schema:value": "CITZAF",
      "ada:tier": "M",
      "ada:cdifPropertyPath": "cdifProvActivity: schema:actionProcess"
    },
    {
      "schema:name": "analyticalSoftware",
      "schema:alternateName": "Analytical Software",
      "ada:scope": "default",
      "ada:category": "Instrument & Software",
      "ada:dataType": "string",
      "schema:value": "Probe for EPMA",
      "ada:tier": "M",
      "ada:cdifPropertyPath": "cdifProvActivity: prov:used"
    },
    {
      "schema:name": "samplePreparationMethod",
      "schema:alternateName": "Sample Preparation Method",
      "ada:scope": "optional",
      "ada:category": "Samples",
      "ada:dataType": "string",
      "ada:tier": "R",
      "ada:cdifPropertyPath": "cdifProvActivity: schema:actionProcess"
    }
  ],
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "schema:name": "analysedOxide",
        "schema:alternateName": "Analysed Oxide/Element",
        "ada:scope": "default",
        "ada:dataType": "string",
        "ada:tier": "M",
        "ada:cdifPropertyPath": "cdifVariableMeasured: cdi:name"
      },
      {
        "schema:name": "xrayLine",
        "schema:alternateName": "X-ray Line",
        "ada:scope": "default",
        "ada:dataType": "string",
        "ada:enumeration": ["Ka", "Kb", "La", "Lb", "Ma", "Mb"],
        "ada:tier": "M",
        "ada:cdifPropertyPath": "schema:additionalProperty"
      },
      {
        "schema:name": "diffractingCrystal",
        "schema:alternateName": "Diffracting Crystal",
        "ada:scope": "default",
        "ada:dataType": "string",
        "ada:enumeration": ["LIF", "LIFH", "PET", "PETJ", "TAP", "RAP"],
        "ada:tier": "M",
        "ada:cdifPropertyPath": "schema:additionalProperty"
      },
      {
        "schema:name": "peakCountingTime",
        "schema:alternateName": "Peak Counting Time",
        "ada:scope": "default",
        "ada:dataType": "number",
        "schema:unitText": "seconds",
        "ada:tier": "M",
        "ada:cdifPropertyPath": "schema:additionalProperty"
      },
      {
        "schema:name": "calibrationStandardName",
        "schema:alternateName": "Calibration Standard Name",
        "ada:scope": "default",
        "ada:dataType": "string",
        "ada:tier": "M",
        "ada:cdifPropertyPath": "schema:additionalProperty"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analysedOxide": "SiO2",
        "xrayLine": "Ka",
        "diffractingCrystal": "TAP",
        "peakCountingTime": 30,
        "calibrationStandardName": "San Carlos olivine"
      },
      {
        "analysedOxide": "FeOT",
        "xrayLine": "Ka",
        "diffractingCrystal": "LiFH",
        "peakCountingTime": 30,
        "calibrationStandardName": "San Carlos olivine"
      }
    ]
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/",
      "schema": "http://schema.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/methodDefinition/context.jsonld"
  ],
  "@id": "https://registry.onegeochemistry.org/methods/nmnh-spinel-oxybar-v1",
  "@type": [
    "ada:MethodDefinition",
    "schema:HowTo"
  ],
  "schema:name": "Spinel oxybarometry version 1",
  "schema:version": "1.0",
  "schema:datePublished": "2013-11-08",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "EPMA-WDS",
    "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques"
  },
  "schema:instrument": {
    "@type": [
      "schema:Product",
      "schema:Thing"
    ],
    "schema:name": "JEOL JXA-8900 Superprobe",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "JXA-8900"
    }
  },
  "ada:methodParameters": [
    {
      "schema:name": "acceleratingVoltage",
      "schema:alternateName": "Accelerating Voltage",
      "ada:scope": "constant",
      "ada:category": "Beam Conditions",
      "ada:dataType": "number",
      "schema:value": 15,
      "schema:unitText": "kV",
      "ada:tier": "M",
      "ada:cdifPropertyPath": "cdifProvActivity: schema:additionalProperty"
    },
    {
      "schema:name": "beamCurrent",
      "schema:alternateName": "Beam Current",
      "ada:scope": "constant",
      "ada:category": "Beam Conditions",
      "ada:dataType": "number",
      "schema:value": 40,
      "schema:unitText": "nA",
      "ada:tier": "M",
      "ada:cdifPropertyPath": "cdifProvActivity: schema:additionalProperty"
    },
    {
      "schema:name": "matrixCorrectionModel",
      "schema:alternateName": "X-ray Matrix Corrections",
      "ada:scope": "constant",
      "ada:category": "Data Processing",
      "ada:dataType": "string",
      "schema:value": "CITZAF",
      "ada:tier": "M",
      "ada:cdifPropertyPath": "cdifProvActivity: schema:actionProcess"
    },
    {
      "schema:name": "analyticalSoftware",
      "schema:alternateName": "Analytical Software",
      "ada:scope": "default",
      "ada:category": "Instrument & Software",
      "ada:dataType": "string",
      "schema:value": "Probe for EPMA",
      "ada:tier": "M",
      "ada:cdifPropertyPath": "cdifProvActivity: prov:used"
    },
    {
      "schema:name": "samplePreparationMethod",
      "schema:alternateName": "Sample Preparation Method",
      "ada:scope": "optional",
      "ada:category": "Samples",
      "ada:dataType": "string",
      "ada:tier": "R",
      "ada:cdifPropertyPath": "cdifProvActivity: schema:actionProcess"
    }
  ],
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "schema:name": "analysedOxide",
        "schema:alternateName": "Analysed Oxide/Element",
        "ada:scope": "default",
        "ada:dataType": "string",
        "ada:tier": "M",
        "ada:cdifPropertyPath": "cdifVariableMeasured: cdi:name"
      },
      {
        "schema:name": "xrayLine",
        "schema:alternateName": "X-ray Line",
        "ada:scope": "default",
        "ada:dataType": "string",
        "ada:enumeration": [
          "Ka",
          "Kb",
          "La",
          "Lb",
          "Ma",
          "Mb"
        ],
        "ada:tier": "M",
        "ada:cdifPropertyPath": "schema:additionalProperty"
      },
      {
        "schema:name": "diffractingCrystal",
        "schema:alternateName": "Diffracting Crystal",
        "ada:scope": "default",
        "ada:dataType": "string",
        "ada:enumeration": [
          "LIF",
          "LIFH",
          "PET",
          "PETJ",
          "TAP",
          "RAP"
        ],
        "ada:tier": "M",
        "ada:cdifPropertyPath": "schema:additionalProperty"
      },
      {
        "schema:name": "peakCountingTime",
        "schema:alternateName": "Peak Counting Time",
        "ada:scope": "default",
        "ada:dataType": "number",
        "schema:unitText": "seconds",
        "ada:tier": "M",
        "ada:cdifPropertyPath": "schema:additionalProperty"
      },
      {
        "schema:name": "calibrationStandardName",
        "schema:alternateName": "Calibration Standard Name",
        "ada:scope": "default",
        "ada:dataType": "string",
        "ada:tier": "M",
        "ada:cdifPropertyPath": "schema:additionalProperty"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analysedOxide": "SiO2",
        "xrayLine": "Ka",
        "diffractingCrystal": "TAP",
        "peakCountingTime": 30,
        "calibrationStandardName": "San Carlos olivine"
      },
      {
        "analysedOxide": "FeOT",
        "xrayLine": "Ka",
        "diffractingCrystal": "LiFH",
        "peakCountingTime": 30,
        "calibrationStandardName": "San Carlos olivine"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://registry.onegeochemistry.org/methods/nmnh-spinel-oxybar-v1> a schema1:HowTo,
        ada:MethodDefinition ;
    schema1:datePublished "2013-11-08" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "JXA-8900" ] ;
            schema1:name "JEOL JXA-8900 Superprobe" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
            schema1:name "EPMA-WDS" ] ;
    schema1:name "Spinel oxybarometry version 1" ;
    schema1:version "1.0" ;
    ada:analyteTemplate [ ada:analyteColumns [ schema1:alternateName "X-ray Line" ;
                    schema1:name "xrayLine" ;
                    ada:cdifPropertyPath "schema:additionalProperty" ;
                    ada:dataType "string" ;
                    ada:enumeration "Ka",
                        "Kb",
                        "La",
                        "Lb",
                        "Ma",
                        "Mb" ;
                    ada:scope "default" ;
                    ada:tier "M" ],
                [ schema1:alternateName "Calibration Standard Name" ;
                    schema1:name "calibrationStandardName" ;
                    ada:cdifPropertyPath "schema:additionalProperty" ;
                    ada:dataType "string" ;
                    ada:scope "default" ;
                    ada:tier "M" ],
                [ schema1:alternateName "Analysed Oxide/Element" ;
                    schema1:name "analysedOxide" ;
                    ada:cdifPropertyPath "cdifVariableMeasured: cdi:name" ;
                    ada:dataType "string" ;
                    ada:scope "default" ;
                    ada:tier "M" ],
                [ schema1:alternateName "Diffracting Crystal" ;
                    schema1:name "diffractingCrystal" ;
                    ada:cdifPropertyPath "schema:additionalProperty" ;
                    ada:dataType "string" ;
                    ada:enumeration "LIF",
                        "LIFH",
                        "PET",
                        "PETJ",
                        "RAP",
                        "TAP" ;
                    ada:scope "default" ;
                    ada:tier "M" ],
                [ schema1:alternateName "Peak Counting Time" ;
                    schema1:name "peakCountingTime" ;
                    schema1:unitText "seconds" ;
                    ada:cdifPropertyPath "schema:additionalProperty" ;
                    ada:dataType "number" ;
                    ada:scope "default" ;
                    ada:tier "M" ] ;
            ada:defaultAnalytes [ ],
                [ ] ] ;
    ada:methodParameters [ schema1:alternateName "X-ray Matrix Corrections" ;
            schema1:name "matrixCorrectionModel" ;
            schema1:value "CITZAF" ;
            ada:category "Data Processing" ;
            ada:cdifPropertyPath "cdifProvActivity: schema:actionProcess" ;
            ada:dataType "string" ;
            ada:scope "constant" ;
            ada:tier "M" ],
        [ schema1:alternateName "Accelerating Voltage" ;
            schema1:name "acceleratingVoltage" ;
            schema1:unitText "kV" ;
            schema1:value 15 ;
            ada:category "Beam Conditions" ;
            ada:cdifPropertyPath "cdifProvActivity: schema:additionalProperty" ;
            ada:dataType "number" ;
            ada:scope "constant" ;
            ada:tier "M" ],
        [ schema1:alternateName "Sample Preparation Method" ;
            schema1:name "samplePreparationMethod" ;
            ada:category "Samples" ;
            ada:cdifPropertyPath "cdifProvActivity: schema:actionProcess" ;
            ada:dataType "string" ;
            ada:scope "optional" ;
            ada:tier "R" ],
        [ schema1:alternateName "Analytical Software" ;
            schema1:name "analyticalSoftware" ;
            schema1:value "Probe for EPMA" ;
            ada:category "Instrument & Software" ;
            ada:cdifPropertyPath "cdifProvActivity: prov:used" ;
            ada:dataType "string" ;
            ada:scope "default" ;
            ada:tier "M" ],
        [ schema1:alternateName "Beam Current" ;
            schema1:name "beamCurrent" ;
            schema1:unitText "nA" ;
            schema1:value 40 ;
            ada:category "Beam Conditions" ;
            ada:cdifPropertyPath "cdifProvActivity: schema:additionalProperty" ;
            ada:dataType "number" ;
            ada:scope "constant" ;
            ada:tier "M" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Analytical Method Definition
description: A registered analytical method description that can be referenced by
  metadata records. Contains constant parameters, required parameters with defaults
  and constraints, optional extension properties, and per-analyte parameter templates.
  Methods are typed as ada:MethodDefinition and schema:HowTo.
type: object
properties:
  '@id':
    type: string
    description: Persistent URI for this method definition in the registry.
  '@type':
    type: array
    items:
      type: string
    minItems: 2
    allOf:
    - contains:
        const: ada:MethodDefinition
    - contains:
        const: schema:HowTo
    description: Must include ada:MethodDefinition and schema:HowTo.
  schema:name:
    type: string
    description: Short descriptive name with version (e.g. "JEOL-8530F WDS Major Element
      Glass v2.1").
  schema:identifier:
    description: DOI or other persistent ID for this method definition.
    anyOf:
    - type: string
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
  schema:description:
    type: string
    description: Human-readable summary of the method, may be auto-generated from
      constant parameters at registration time.
  schema:version:
    type: string
    description: Semantic version string (e.g. "2.1.0").
  schema:datePublished:
    type: string
    description: ISO 8601 date when this method definition was first registered.
  schema:dateModified:
    type: string
    description: ISO 8601 date of last update to this definition.
  schema:measurementTechnique:
    description: The analytical technique this method implements. Must be a DefinedTerm
      from a controlled vocabulary of techniques.
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
  schema:instrument:
    description: Instrument requirements/specification for this method.
    $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/instrument/schema.yaml
  ada:laboratory:
    description: Laboratory where this method was developed. Optional; omit for methods
      that are instrument-generic.
    $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/laboratory/schema.yaml
  ada:methodParameters:
    type: array
    description: All operating, processing, and quality parameters for this method.
      Each parameter carries a scope tag (constant / default / optional) that controls
      form rendering behaviour.
    items:
      $ref: '#/$defs/MethodParameter'
  ada:analyteTemplate:
    description: Template for per-analyte (element-specific) parameters. Defines the
      columns that appear in the element table, each with scope, datatype, and constraints.
      Analyte rows become schema:variableMeasured entries in metadata records.
    type: object
    properties:
      ada:analyteColumns:
        type: array
        items:
          $ref: '#/$defs/AnalyteColumn'
      ada:defaultAnalytes:
        type: array
        description: Pre-populated analyte rows for this method. Each entry is an
          object keyed by analyteColumn names.
        items:
          type: object
          additionalProperties: true
    required:
    - ada:analyteColumns
  schema:creator:
    description: Person(s) who defined this method.
    type: array
    items:
      anyOf:
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/person/schema.yaml
      - type: object
        properties:
          '@id':
            type: string
  schema:relatedLink:
    type: array
    description: Publications, Zenodo records, or other references documenting this
      method.
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.yaml
  schema:funding:
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/monetaryGrant/schema.yaml
required:
- '@type'
- schema:name
- schema:measurementTechnique
- ada:methodParameters
$defs:
  MethodParameter:
    type: object
    description: A single parameter in the method definition. Carries metadata about
      how the parameter behaves across method instantiations.
    properties:
      schema:name:
        type: string
        description: Machine-readable parameter name (e.g. "acceleratingVoltage").
      schema:alternateName:
        type: string
        description: Human-readable display label (e.g. "Accelerating Voltage").
      schema:description:
        type: string
        description: Guidance text shown to the user in the form.
      ada:scope:
        type: string
        enum:
        - constant
        - default
        - optional
        description: constant = fixed for every session, shown as read-only. default
          = required, editable, pre-filled with default value. optional = available
          but not shown unless user adds it.
      ada:category:
        type: string
        description: Grouping label for form layout (e.g. "Beam Conditions", "Data
          Processing", "Quality Control").
      schema:value:
        description: The constant value (scope=constant) or the default value (scope=default).
          Type matches ada:dataType.
        anyOf:
        - type: string
        - type: number
        - type: boolean
      ada:dataType:
        type: string
        enum:
        - string
        - number
        - integer
        - boolean
        - date
        - uri
        description: Expected data type for the parameter value.
      schema:minValue:
        type: number
        description: Minimum allowed numeric value (scope=default only).
      schema:maxValue:
        type: number
        description: Maximum allowed numeric value (scope=default only).
      ada:enumeration:
        type: array
        items:
          anyOf:
          - type: string
          - type: number
        description: Allowed values list. If present, the form renders a dropdown/select
          instead of free text.
      schema:unitText:
        type: string
        description: Unit of measure label (e.g. "kV", "nA", "um").
      schema:unitCode:
        description: URI for unit of measure (QUDT preferred).
        anyOf:
        - type: string
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
      ada:cdifPropertyPath:
        type: string
        description: 'The CDIF building block property path this parameter maps to
          (e.g. "cdifProvActivity: schema:additionalProperty"). Used for JSON-LD serialisation.'
      ada:tier:
        type: string
        enum:
        - M
        - R
        - O
        description: Mandatory / Recommended / Optional tier from the metadata profile.
          Informs validation strictness.
    required:
    - schema:name
    - ada:scope
    - ada:dataType
  AnalyteColumn:
    type: object
    description: Definition of one column in the per-analyte parameter table. Controls
      what fields appear for each measured element/oxide. Each analyte row becomes
      a schema:variableMeasured entry; analyte columns become schema:additionalProperty
      within that variableMeasured entry.
    properties:
      schema:name:
        type: string
        description: Column identifier (e.g. "diffractingCrystal").
      schema:alternateName:
        type: string
        description: Display label (e.g. "Diffracting Crystal").
      schema:description:
        type: string
        description: Guidance text.
      ada:scope:
        type: string
        enum:
        - constant
        - default
        - optional
      ada:dataType:
        type: string
        enum:
        - string
        - number
        - integer
        - boolean
        - date
        - uri
      ada:enumeration:
        type: array
        items:
          anyOf:
          - type: string
          - type: number
      schema:unitText:
        type: string
      ada:tier:
        type: string
        enum:
        - M
        - R
        - O
      ada:cdifPropertyPath:
        type: string
        description: How this column maps into the variableMeasured JSON-LD structure
          (e.g. "schema:additionalProperty", "schema:measurementTechnique").
    required:
    - schema:name
    - ada:scope
    - ada:dataType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  prov: http://www.w3.org/ns/prov#
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/methodDefinition/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/methodDefinition/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "prov": "http://www.w3.org/ns/prov#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/methodDefinition/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)
* [OneGeochemistry EPMA Metadata Profile v1.0](https://github.com/usgin/geochemBuildingBlocks)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/methodDefinition`

