
# Analytical Method Definition (Schema)

`ada.bbr.metadata.geochemProperties.methodDefinition` *v0.3*

A registered analytical method definition modeled as cdi:Activity + schema:Action + ada:MethodDefinition + bios:LabProtocol. Method identity (name, technique, instrument, laboratory, target material) at top level. Standard workflow encoded in schema:actionProcess as a schema:HowTo with ordered cdi:Activity + schema:Action steps. Each workflow step carries its own parameters, reagents, instruments. Uses bios:computationalTool for software, bios:reagent for reference materials, dqv:hasQualityMeasurement for quality metrics, ada:fieldScope (method/session/element) for parameter lifecycle.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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

## Examples

### EPMA Method Definition v3 Example
Electron Microprobe Analysis method definition for CU tephra glass,
modeled as cdi:Activity + schema:Action. Workflow in schema:actionProcess
with 5 ordered steps: sample preparation, calibration, WDS acquisition,
data processing, and quality control. Each step carries its own
parameters, reagents, and quality measurements.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "dqv": "http://www.w3.org/ns/dqv#",
    "prov": "http://www.w3.org/ns/prov#",
    "skos": "http://www.w3.org/2004/02/skos/core#"
  },
  "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:MethodDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "CU routine tephra glass version 1.0 with 6nA",
  "schema:version": "1.0.6",
  "schema:datePublished": "2011-10-20",
  "schema:measurementTechnique": {
    "@type": ["schema:DefinedTerm"],
    "schema:name": "EPMA-WDS",
    "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques"
  },
  "schema:object": [
    {
      "@type": ["schema:DefinedTerm"],
      "schema:name": "silicate glass",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    }
  ],
  "schema:instrument": {
    "@type": ["schema:Product", "schema:Thing"],
    "schema:name": "ARL SEMQ",
    "schema:additionalType": [
      "ada:EPMAInstrument"
    ],
    "schema:manufacturer": {
      "@type": ["schema:Organization"],
      "schema:name": "ARL"
    },
    "schema:model": {
      "@type": ["schema:ProductModel"],
      "schema:name": "SEMQ"
    },
    "schema:hasPart": [
      {
        "@type": ["schema:Thing"],
        "schema:name": "WDS Spectrometer Array",
        "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows"
      }
    ]
  },
  "ada:laboratory": {
    "@type": ["schema:Place"],
    "schema:name": "Concord University, Athens, West Virginia, USA"
  },
  "schema:agent": {
    "@type": ["schema:Organization"],
    "schema:name": "Concord University"
  },
  "bios:computationalTool": [
    {
      "@type": ["schema:SoftwareApplication"],
      "schema:name": "Probe for EPMA",
      "schema:version": "9.6.4",
      "ada:toolRole": "acquisition"
    }
  ],
  "ada:methodParameters": [
    {
      "@type": ["schema:PropertyValueSpecification"],
      "schema:name": "Additional Notes",
      "schema:valueName": "additionalNotes",
      "ada:fieldScope": "method",
      "ada:category": "General",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": false,
      "schema:defaultValue": "Water by difference included in x-ray matrix corrections for improved accuracy on hydrated glasses; offline multi-standard blank correction; offline standards-based normalization",
      "ada:tier": "O"
    }
  ],
  "schema:actionProcess": {
    "@type": ["schema:HowTo"],
    "schema:name": "EPMA WDS tephra glass analytical workflow",
    "schema:step": [
      {
        "@type": ["cdi:Activity", "schema:Action"],
        "schema:name": "Sample preparation",
        "schema:position": 1,
        "schema:additionalType": ["bios:LabProcess"],
        "schema:description": "Tephra glass grains mounted, polished, and carbon coated for EPMA.",
        "bios:reagent": [
          {
            "@type": ["schema:Thing"],
            "schema:name": "Carbon",
            "ada:reagentRole": "coatingMaterial"
          }
        ],
        "schema:result": {
          "@id": "#preparedMount"
        }
      },
      {
        "@type": ["cdi:Activity", "schema:Action"],
        "schema:name": "Instrument calibration",
        "schema:position": 2,
        "schema:description": "Calibrate WDS spectrometers on primary standards. Verify on secondary standards at start and end of session.",
        "schema:object": {"@id": "#preparedMount"},
        "bios:reagent": [
          {
            "@type": ["schema:Thing"],
            "schema:name": "Albite",
            "ada:reagentRole": "primaryStandard"
          },
          {
            "@type": ["schema:Thing"],
            "schema:name": "Kaersutite amphibole",
            "ada:reagentRole": "primaryStandard"
          },
          {
            "@type": ["schema:Thing"],
            "schema:name": "Lipari obsidian ID3506",
            "ada:reagentRole": "secondaryStandard"
          },
          {
            "@type": ["schema:Thing"],
            "schema:name": "USGS BHVO-2g",
            "ada:reagentRole": "secondaryStandard"
          },
          {
            "@type": ["schema:Thing"],
            "schema:name": "USGS NKT-1g",
            "ada:reagentRole": "secondaryStandard"
          }
        ]
      },
      {
        "@type": ["cdi:Activity", "schema:Action"],
        "schema:name": "WDS data acquisition",
        "schema:position": 3,
        "schema:description": "Quantitative WDS analysis at 15 kV / 6 nA. Si, Al, Na acquired first to minimize beam damage with TDI correction.",
        "ada:methodParameters": [
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Accelerating Voltage",
            "schema:valueName": "acceleratingVoltage",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": 15,
            "schema:unitText": "kV",
            "ada:tier": "M"
          },
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Beam Current",
            "schema:valueName": "beamCurrent",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": 6,
            "schema:minValue": 1,
            "schema:maxValue": 200,
            "schema:unitText": "nA",
            "ada:tier": "M"
          },
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Beam Diameter",
            "schema:valueName": "beamDiameter",
            "ada:fieldScope": "session",
            "ada:category": "Beam Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 10,
            "schema:minValue": 0,
            "schema:maxValue": 50,
            "schema:unitText": "um",
            "ada:tier": "M"
          },
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Beam Damage Minimization",
            "schema:valueName": "beamDamageMinimization",
            "schema:inDefinedTermSet": {
              "@id": "https://vocab.onegeochemistry.org/epma/beam-damage-methods"
            },
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": false,
            "schema:defaultValue": "Si, Al, Na acquired first; 6-7 time intervals for TDI correction",
            "ada:tier": "R"
          }
        ],
        "schema:result": {
          "@id": "#rawAnalyses"
        }
      },
      {
        "@type": ["cdi:Activity", "schema:Action"],
        "schema:name": "Data processing",
        "schema:position": 4,
        "schema:description": "Matrix correction, blank correction, and standards-based normalization using Probe for EPMA.",
        "schema:object": {"@id": "#rawAnalyses"},
        "bios:computationalTool": [
          {
            "@type": ["schema:SoftwareApplication"],
            "schema:name": "Probe for EPMA",
            "schema:version": "9.6.4",
            "ada:toolRole": "reduction"
          }
        ],
        "ada:methodParameters": [
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Matrix Correction Model",
            "schema:valueName": "matrixCorrectionModel",
            "schema:propertyID": "https://vocab.onegeochemistry.org/epma/matrix-correction",
            "schema:inDefinedTermSet": {
              "@id": "https://vocab.onegeochemistry.org/epma/matrix-correction-models"
            },
            "ada:fieldScope": "method",
            "ada:category": "Data Processing",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "Armstrong/Packwood-Brown 1981 MAS Phi(pz) with CITZMU MACs",
            "ada:enumeration": ["PAP", "XPP", "PhiRhoZ", "ZAF", "CITZAF", "Armstrong", "Other"],
            "ada:tier": "M"
          }
        ],
        "schema:result": {
          "@id": "#quantifiedResults"
        }
      },
      {
        "@type": ["cdi:Activity", "schema:Action"],
        "schema:name": "Quality control",
        "schema:position": 5,
        "schema:description": "Secondary standards analysed at start and end of every session. Drift correction by interpolation of primary standard calibrations.",
        "schema:object": {"@id": "#quantifiedResults"},
        "ada:methodParameters": [
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Drift Correction",
            "schema:valueName": "driftCorrection",
            "ada:fieldScope": "session",
            "ada:category": "Quality Control",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": false,
            "schema:defaultValue": "Primary reference materials at start/end of session; calibration interpolated",
            "ada:tier": "R"
          }
        ],
        "dqv:hasQualityMeasurement": [
          {
            "@type": ["dqv:QualityMeasurement"],
            "dqv:isMeasurementOf": "analytical precision (1-sigma)",
            "dqv:value": "Reported per element on secondary standards; see relatedLink publications"
          }
        ]
      }
    ]
  },
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Analysed Oxide/Element",
        "schema:valueName": "analysedOxide",
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "cdifVariableMeasured: cdi:name"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Beam Current (nA)",
        "schema:valueName": "beamCurrent",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:maxValue": 200,
        "schema:unitText": "nA",
        "ada:tier": "M"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Spectrometer",
        "schema:valueName": "spectrometer",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Sequence",
        "schema:valueName": "sequence",
        "ada:dataType": "integer",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Diffracting Crystal",
        "schema:valueName": "diffractingCrystal",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/diffracting-crystals"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:enumeration": ["PET", "PETJ", "LIF", "LIFH", "TAP", "RAP"],
        "ada:tier": "M"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Detector Type",
        "schema:valueName": "detectorType",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:enumeration": ["xenon", "P-10", "SDD", "Si(Li)", "Other"],
        "ada:tier": "R"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "X-ray Line",
        "schema:valueName": "xrayLine",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/xray-lines"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:enumeration": ["Ka", "Kb", "La", "Lb", "Ma"],
        "ada:tier": "M"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Peak Counting Time (s)",
        "schema:valueName": "peakCountingTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Background Method",
        "schema:valueName": "backgroundMethod",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/background-methods"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Background Counting Time (s)",
        "schema:valueName": "backgroundCountingTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "WDS PHA Setting",
        "schema:valueName": "phaSettings",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:enumeration": ["Integral", "Differential"],
        "ada:tier": "R"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Calibration Standard Name",
        "schema:valueName": "calibrationStandardName",
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Normalization Method",
        "schema:valueName": "normalizationMethod",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "O"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Normalization Standards",
        "schema:valueName": "normalizationStandards",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "O"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Detection Limit",
        "schema:valueName": "detectionLimit",
        "ada:dataType": "number",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Detection Limit Unit",
        "schema:valueName": "detectionLimitUnit",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Detection Limit Method",
        "schema:valueName": "detectionLimitMethod",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analysedOxide": "SiO2",
        "beamCurrent": 6,
        "spectrometer": "WDS 1",
        "sequence": 1,
        "diffractingCrystal": "PET",
        "detectorType": "P-10",
        "xrayLine": "Ka",
        "peakCountingTime": "12",
        "backgroundMethod": "high only",
        "backgroundCountingTime": 4,
        "phaSettings": "integral",
        "calibrationStandardName": "Albite or Lipari obsidian ID3506 or BHVO-2g",
        "normalizationMethod": "multi-standard weighted mean",
        "normalizationStandards": "Lipari obsidian ID3506, BHVO-2g",
        "detectionLimit": 0.0997,
        "detectionLimitUnit": "weight percent (%m/m)",
        "detectionLimitMethod": "Mean of WDS detection limits at 99% confidence"
      },
      {
        "analysedOxide": "TiO2",
        "beamCurrent": 6,
        "spectrometer": "WDS 1",
        "sequence": 3,
        "diffractingCrystal": "PET",
        "detectorType": "xenon",
        "xrayLine": "Ka",
        "peakCountingTime": "28",
        "backgroundMethod": "two backgrounds",
        "backgroundCountingTime": 20,
        "phaSettings": "integral",
        "calibrationStandardName": "Kaersutite amphibole",
        "normalizationMethod": "multi-standard weighted mean",
        "normalizationStandards": "Lipari obsidian ID3506, BHVO-2g",
        "detectionLimit": 0.0439,
        "detectionLimitUnit": "weight percent (%m/m)",
        "detectionLimitMethod": "Mean of WDS detection limits at 99% confidence"
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
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "dqv": "http://www.w3.org/ns/dqv#",
      "prov": "http://www.w3.org/ns/prov#"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/methodDefinition/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "dqv": "http://www.w3.org/ns/dqv#",
      "prov": "http://www.w3.org/ns/prov#",
      "skos": "http://www.w3.org/2004/02/skos/core#"
    }
  ],
  "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:MethodDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "CU routine tephra glass version 1.0 with 6nA",
  "schema:version": "1.0.6",
  "schema:datePublished": "2011-10-20",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "EPMA-WDS",
    "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "silicate glass",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Product",
      "schema:Thing"
    ],
    "schema:name": "ARL SEMQ",
    "schema:additionalType": [
      "ada:EPMAInstrument"
    ],
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "ARL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "SEMQ"
    },
    "schema:hasPart": [
      {
        "@type": [
          "schema:Thing"
        ],
        "schema:name": "WDS Spectrometer Array",
        "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows"
      }
    ]
  },
  "ada:laboratory": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Concord University, Athens, West Virginia, USA"
  },
  "schema:agent": {
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "Concord University"
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Probe for EPMA",
      "schema:version": "9.6.4",
      "ada:toolRole": "acquisition"
    }
  ],
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Additional Notes",
      "schema:valueName": "additionalNotes",
      "ada:fieldScope": "method",
      "ada:category": "General",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": false,
      "schema:defaultValue": "Water by difference included in x-ray matrix corrections for improved accuracy on hydrated glasses; offline multi-standard blank correction; offline standards-based normalization",
      "ada:tier": "O"
    }
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:name": "EPMA WDS tephra glass analytical workflow",
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Sample preparation",
        "schema:position": 1,
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:description": "Tephra glass grains mounted, polished, and carbon coated for EPMA.",
        "bios:reagent": [
          {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "Carbon",
            "ada:reagentRole": "coatingMaterial"
          }
        ],
        "schema:result": {
          "@id": "#preparedMount"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Instrument calibration",
        "schema:position": 2,
        "schema:description": "Calibrate WDS spectrometers on primary standards. Verify on secondary standards at start and end of session.",
        "schema:object": {
          "@id": "#preparedMount"
        },
        "bios:reagent": [
          {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "Albite",
            "ada:reagentRole": "primaryStandard"
          },
          {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "Kaersutite amphibole",
            "ada:reagentRole": "primaryStandard"
          },
          {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "Lipari obsidian ID3506",
            "ada:reagentRole": "secondaryStandard"
          },
          {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "USGS BHVO-2g",
            "ada:reagentRole": "secondaryStandard"
          },
          {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "USGS NKT-1g",
            "ada:reagentRole": "secondaryStandard"
          }
        ]
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "WDS data acquisition",
        "schema:position": 3,
        "schema:description": "Quantitative WDS analysis at 15 kV / 6 nA. Si, Al, Na acquired first to minimize beam damage with TDI correction.",
        "ada:methodParameters": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Accelerating Voltage",
            "schema:valueName": "acceleratingVoltage",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": 15,
            "schema:unitText": "kV",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Beam Current",
            "schema:valueName": "beamCurrent",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": 6,
            "schema:minValue": 1,
            "schema:maxValue": 200,
            "schema:unitText": "nA",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Beam Diameter",
            "schema:valueName": "beamDiameter",
            "ada:fieldScope": "session",
            "ada:category": "Beam Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 10,
            "schema:minValue": 0,
            "schema:maxValue": 50,
            "schema:unitText": "um",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Beam Damage Minimization",
            "schema:valueName": "beamDamageMinimization",
            "schema:inDefinedTermSet": {
              "@id": "https://vocab.onegeochemistry.org/epma/beam-damage-methods"
            },
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": false,
            "schema:defaultValue": "Si, Al, Na acquired first; 6-7 time intervals for TDI correction",
            "ada:tier": "R"
          }
        ],
        "schema:result": {
          "@id": "#rawAnalyses"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data processing",
        "schema:position": 4,
        "schema:description": "Matrix correction, blank correction, and standards-based normalization using Probe for EPMA.",
        "schema:object": {
          "@id": "#rawAnalyses"
        },
        "bios:computationalTool": [
          {
            "@type": [
              "schema:SoftwareApplication"
            ],
            "schema:name": "Probe for EPMA",
            "schema:version": "9.6.4",
            "ada:toolRole": "reduction"
          }
        ],
        "ada:methodParameters": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Matrix Correction Model",
            "schema:valueName": "matrixCorrectionModel",
            "schema:propertyID": "https://vocab.onegeochemistry.org/epma/matrix-correction",
            "schema:inDefinedTermSet": {
              "@id": "https://vocab.onegeochemistry.org/epma/matrix-correction-models"
            },
            "ada:fieldScope": "method",
            "ada:category": "Data Processing",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "Armstrong/Packwood-Brown 1981 MAS Phi(pz) with CITZMU MACs",
            "ada:enumeration": [
              "PAP",
              "XPP",
              "PhiRhoZ",
              "ZAF",
              "CITZAF",
              "Armstrong",
              "Other"
            ],
            "ada:tier": "M"
          }
        ],
        "schema:result": {
          "@id": "#quantifiedResults"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Quality control",
        "schema:position": 5,
        "schema:description": "Secondary standards analysed at start and end of every session. Drift correction by interpolation of primary standard calibrations.",
        "schema:object": {
          "@id": "#quantifiedResults"
        },
        "ada:methodParameters": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Drift Correction",
            "schema:valueName": "driftCorrection",
            "ada:fieldScope": "session",
            "ada:category": "Quality Control",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": false,
            "schema:defaultValue": "Primary reference materials at start/end of session; calibration interpolated",
            "ada:tier": "R"
          }
        ],
        "dqv:hasQualityMeasurement": [
          {
            "@type": [
              "dqv:QualityMeasurement"
            ],
            "dqv:isMeasurementOf": "analytical precision (1-sigma)",
            "dqv:value": "Reported per element on secondary standards; see relatedLink publications"
          }
        ]
      }
    ]
  },
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analysed Oxide/Element",
        "schema:valueName": "analysedOxide",
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "cdifVariableMeasured: cdi:name"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Beam Current (nA)",
        "schema:valueName": "beamCurrent",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:maxValue": 200,
        "schema:unitText": "nA",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Spectrometer",
        "schema:valueName": "spectrometer",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Sequence",
        "schema:valueName": "sequence",
        "ada:dataType": "integer",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Diffracting Crystal",
        "schema:valueName": "diffractingCrystal",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/diffracting-crystals"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:enumeration": [
          "PET",
          "PETJ",
          "LIF",
          "LIFH",
          "TAP",
          "RAP"
        ],
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Detector Type",
        "schema:valueName": "detectorType",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:enumeration": [
          "xenon",
          "P-10",
          "SDD",
          "Si(Li)",
          "Other"
        ],
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "X-ray Line",
        "schema:valueName": "xrayLine",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/xray-lines"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:enumeration": [
          "Ka",
          "Kb",
          "La",
          "Lb",
          "Ma"
        ],
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Peak Counting Time (s)",
        "schema:valueName": "peakCountingTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Background Method",
        "schema:valueName": "backgroundMethod",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/background-methods"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Background Counting Time (s)",
        "schema:valueName": "backgroundCountingTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "WDS PHA Setting",
        "schema:valueName": "phaSettings",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:enumeration": [
          "Integral",
          "Differential"
        ],
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Calibration Standard Name",
        "schema:valueName": "calibrationStandardName",
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Normalization Method",
        "schema:valueName": "normalizationMethod",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "O"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Normalization Standards",
        "schema:valueName": "normalizationStandards",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "O"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Detection Limit",
        "schema:valueName": "detectionLimit",
        "ada:dataType": "number",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Detection Limit Unit",
        "schema:valueName": "detectionLimitUnit",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Detection Limit Method",
        "schema:valueName": "detectionLimitMethod",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analysedOxide": "SiO2",
        "beamCurrent": 6,
        "spectrometer": "WDS 1",
        "sequence": 1,
        "diffractingCrystal": "PET",
        "detectorType": "P-10",
        "xrayLine": "Ka",
        "peakCountingTime": "12",
        "backgroundMethod": "high only",
        "backgroundCountingTime": 4,
        "phaSettings": "integral",
        "calibrationStandardName": "Albite or Lipari obsidian ID3506 or BHVO-2g",
        "normalizationMethod": "multi-standard weighted mean",
        "normalizationStandards": "Lipari obsidian ID3506, BHVO-2g",
        "detectionLimit": 0.0997,
        "detectionLimitUnit": "weight percent (%m/m)",
        "detectionLimitMethod": "Mean of WDS detection limits at 99% confidence"
      },
      {
        "analysedOxide": "TiO2",
        "beamCurrent": 6,
        "spectrometer": "WDS 1",
        "sequence": 3,
        "diffractingCrystal": "PET",
        "detectorType": "xenon",
        "xrayLine": "Ka",
        "peakCountingTime": "28",
        "backgroundMethod": "two backgrounds",
        "backgroundCountingTime": 20,
        "phaSettings": "integral",
        "calibrationStandardName": "Kaersutite amphibole",
        "normalizationMethod": "multi-standard weighted mean",
        "normalizationStandards": "Lipari obsidian ID3506, BHVO-2g",
        "detectionLimit": 0.0439,
        "detectionLimitUnit": "weight percent (%m/m)",
        "detectionLimitMethod": "Mean of WDS detection limits at 99% confidence"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> a cdi:Activity,
        schema1:Action,
        ada:MethodDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:name "EPMA WDS tephra glass analytical workflow" ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:description "Calibrate WDS spectrometers on primary standards. Verify on secondary standards at start and end of session." ;
                    schema1:name "Instrument calibration" ;
                    schema1:object <file:///github/workspace/#preparedMount> ;
                    schema1:position 2 ;
                    bios:reagent [ a schema1:Thing ;
                            schema1:name "USGS BHVO-2g" ;
                            ada:reagentRole "secondaryStandard" ],
                        [ a schema1:Thing ;
                            schema1:name "Lipari obsidian ID3506" ;
                            ada:reagentRole "secondaryStandard" ],
                        [ a schema1:Thing ;
                            schema1:name "USGS NKT-1g" ;
                            ada:reagentRole "secondaryStandard" ],
                        [ a schema1:Thing ;
                            schema1:name "Kaersutite amphibole" ;
                            ada:reagentRole "primaryStandard" ],
                        [ a schema1:Thing ;
                            schema1:name "Albite" ;
                            ada:reagentRole "primaryStandard" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Tephra glass grains mounted, polished, and carbon coated for EPMA." ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ;
                    schema1:result <file:///github/workspace/#preparedMount> ;
                    bios:reagent [ a schema1:Thing ;
                            schema1:name "Carbon" ;
                            ada:reagentRole "coatingMaterial" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:description "Quantitative WDS analysis at 15 kV / 6 nA. Si, Al, Na acquired first to minimize beam damage with TDI correction." ;
                    schema1:name "WDS data acquisition" ;
                    schema1:position 3 ;
                    schema1:result <file:///github/workspace/#rawAnalyses> ;
                    ada:methodParameters [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "Si, Al, Na acquired first; 6-7 time intervals for TDI correction" ;
                            schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/beam-damage-methods> ;
                            schema1:name "Beam Damage Minimization" ;
                            schema1:readonlyValue true ;
                            schema1:valueName "beamDamageMinimization" ;
                            schema1:valueRequired false ;
                            ada:category "Beam Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "method" ;
                            ada:tier "R" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 10 ;
                            schema1:maxValue 50 ;
                            schema1:minValue 0 ;
                            schema1:name "Beam Diameter" ;
                            schema1:readonlyValue false ;
                            schema1:unitText "um" ;
                            schema1:valueName "beamDiameter" ;
                            schema1:valueRequired true ;
                            ada:category "Beam Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 15 ;
                            schema1:name "Accelerating Voltage" ;
                            schema1:readonlyValue true ;
                            schema1:unitText "kV" ;
                            schema1:valueName "acceleratingVoltage" ;
                            schema1:valueRequired true ;
                            ada:category "Beam Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "method" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 6 ;
                            schema1:maxValue 200 ;
                            schema1:minValue 1 ;
                            schema1:name "Beam Current" ;
                            schema1:readonlyValue true ;
                            schema1:unitText "nA" ;
                            schema1:valueName "beamCurrent" ;
                            schema1:valueRequired true ;
                            ada:category "Beam Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "method" ;
                            ada:tier "M" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:description "Matrix correction, blank correction, and standards-based normalization using Probe for EPMA." ;
                    schema1:name "Data processing" ;
                    schema1:object <file:///github/workspace/#rawAnalyses> ;
                    schema1:position 4 ;
                    schema1:result <file:///github/workspace/#quantifiedResults> ;
                    ada:methodParameters [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "Armstrong/Packwood-Brown 1981 MAS Phi(pz) with CITZMU MACs" ;
                            schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/matrix-correction-models> ;
                            schema1:name "Matrix Correction Model" ;
                            schema1:propertyID "https://vocab.onegeochemistry.org/epma/matrix-correction" ;
                            schema1:readonlyValue true ;
                            schema1:valueName "matrixCorrectionModel" ;
                            schema1:valueRequired true ;
                            ada:category "Data Processing" ;
                            ada:dataType "string" ;
                            ada:enumeration "Armstrong",
                                "CITZAF",
                                "Other",
                                "PAP",
                                "PhiRhoZ",
                                "XPP",
                                "ZAF" ;
                            ada:fieldScope "method" ;
                            ada:tier "M" ] ;
                    bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Probe for EPMA" ;
                            schema1:version "9.6.4" ;
                            ada:toolRole "reduction" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:description "Secondary standards analysed at start and end of every session. Drift correction by interpolation of primary standard calibrations." ;
                    schema1:name "Quality control" ;
                    schema1:object <file:///github/workspace/#quantifiedResults> ;
                    schema1:position 5 ;
                    dqv:hasQualityMeasurement [ a dqv:QualityMeasurement ;
                            dqv:isMeasurementOf "analytical precision (1-sigma)" ;
                            dqv:value "Reported per element on secondary standards; see relatedLink publications" ] ;
                    ada:methodParameters [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "Primary reference materials at start/end of session; calibration interpolated" ;
                            schema1:name "Drift Correction" ;
                            schema1:readonlyValue false ;
                            schema1:valueName "driftCorrection" ;
                            schema1:valueRequired false ;
                            ada:category "Quality Control" ;
                            ada:dataType "string" ;
                            ada:fieldScope "session" ;
                            ada:tier "R" ] ] ] ;
    schema1:agent [ a schema1:Organization ;
            schema1:name "Concord University" ] ;
    schema1:datePublished "2011-10-20" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType "ada:EPMAInstrument" ;
            schema1:hasPart [ a schema1:Thing ;
                    schema1:description "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows" ;
                    schema1:name "WDS Spectrometer Array" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "ARL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "SEMQ" ] ;
            schema1:name "ARL SEMQ" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
            schema1:name "EPMA-WDS" ] ;
    schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/materials" ;
            schema1:name "silicate glass" ] ;
    schema1:version "1.0.6" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/background-methods> ;
                    schema1:name "Background Method" ;
                    schema1:valueName "backgroundMethod" ;
                    schema1:valueRequired true ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Detection Limit Unit" ;
                    schema1:valueName "detectionLimitUnit" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Sequence" ;
                    schema1:valueName "sequence" ;
                    schema1:valueRequired false ;
                    ada:dataType "integer" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/xray-lines> ;
                    schema1:name "X-ray Line" ;
                    schema1:valueName "xrayLine" ;
                    schema1:valueRequired true ;
                    ada:dataType "string" ;
                    ada:enumeration "Ka",
                        "Kb",
                        "La",
                        "Lb",
                        "Ma" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Detector Type" ;
                    schema1:valueName "detectorType" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:enumeration "Other",
                        "P-10",
                        "SDD",
                        "Si(Li)",
                        "xenon" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "WDS PHA Setting" ;
                    schema1:valueName "phaSettings" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:enumeration "Differential",
                        "Integral" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:maxValue 200 ;
                    schema1:minValue 1 ;
                    schema1:name "Beam Current (nA)" ;
                    schema1:unitText "nA" ;
                    schema1:valueName "beamCurrent" ;
                    schema1:valueRequired true ;
                    ada:dataType "number" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:minValue 1 ;
                    schema1:name "Background Counting Time (s)" ;
                    schema1:unitText "seconds" ;
                    schema1:valueName "backgroundCountingTime" ;
                    schema1:valueRequired true ;
                    ada:dataType "number" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Spectrometer" ;
                    schema1:valueName "spectrometer" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/diffracting-crystals> ;
                    schema1:name "Diffracting Crystal" ;
                    schema1:valueName "diffractingCrystal" ;
                    schema1:valueRequired true ;
                    ada:dataType "string" ;
                    ada:enumeration "LIF",
                        "LIFH",
                        "PET",
                        "PETJ",
                        "RAP",
                        "TAP" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Normalization Standards" ;
                    schema1:valueName "normalizationStandards" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "O" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Detection Limit Method" ;
                    schema1:valueName "detectionLimitMethod" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Normalization Method" ;
                    schema1:valueName "normalizationMethod" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "O" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Calibration Standard Name" ;
                    schema1:valueName "calibrationStandardName" ;
                    schema1:valueRequired true ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Detection Limit" ;
                    schema1:valueName "detectionLimit" ;
                    schema1:valueRequired false ;
                    ada:dataType "number" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:minValue 1 ;
                    schema1:name "Peak Counting Time (s)" ;
                    schema1:unitText "seconds" ;
                    schema1:valueName "peakCountingTime" ;
                    schema1:valueRequired true ;
                    ada:dataType "number" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Analysed Oxide/Element" ;
                    schema1:valueName "analysedOxide" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "cdifVariableMeasured: cdi:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ;
            ada:defaultAnalytes [ ],
                [ ] ] ;
    ada:laboratory [ a schema1:Place ;
            schema1:name "Concord University, Athens, West Virginia, USA" ] ;
    ada:methodParameters [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "Water by difference included in x-ray matrix corrections for improved accuracy on hydrated glasses; offline multi-standard blank correction; offline standards-based normalization" ;
            schema1:name "Additional Notes" ;
            schema1:readonlyValue true ;
            schema1:valueName "additionalNotes" ;
            schema1:valueRequired false ;
            ada:category "General" ;
            ada:dataType "string" ;
            ada:fieldScope "method" ;
            ada:tier "O" ] ;
    bios:computationalTool [ a schema1:SoftwareApplication ;
            schema1:name "Probe for EPMA" ;
            schema1:version "9.6.4" ;
            ada:toolRole "acquisition" ] .


```


### NMNH Spinel Oxybarometry Method Definition v3
Spinel oxybarometry method at NMNH Smithsonian, modeled as
cdi:Activity + schema:Action. Workflow with 5 steps including
calibration with Smithsonian reference standards carrying
catalog identifiers and citations. Multiple target materials
(spinel, olivine, orthopyroxene) via schema:object.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "dqv": "http://www.w3.org/ns/dqv#",
    "prov": "http://www.w3.org/ns/prov#",
    "skos": "http://www.w3.org/2004/02/skos/core#"
  },
  "@id": "https://registry.onegeochemistry.org/methods/nmnh-spinel-oxybar-v1",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:MethodDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Spinel oxybarometry version 1",
  "schema:version": "1.0",
  "schema:datePublished": "2013-11-08",
  "schema:measurementTechnique": {
    "@type": ["schema:DefinedTerm"],
    "schema:name": "EPMA-WDS",
    "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques"
  },
  "schema:object": [
    {
      "@type": ["schema:DefinedTerm"],
      "schema:name": "spinel",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    },
    {
      "@type": ["schema:DefinedTerm"],
      "schema:name": "olivine",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    },
    {
      "@type": ["schema:DefinedTerm"],
      "schema:name": "orthopyroxene",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    }
  ],
  "schema:instrument": {
    "@type": ["schema:Product", "schema:Thing"],
    "schema:name": "JEOL JXA-8900 Superprobe; JEOL JXA-8530F Hyperprobe",
    "schema:manufacturer": {
      "@type": ["schema:Organization"],
      "schema:name": "JEOL"
    },
    "schema:model": {
      "@type": ["schema:ProductModel"],
      "schema:name": "JXA-8900"
    },
    "schema:hasPart": [
      {
        "@type": ["schema:Thing"],
        "schema:name": "WDS Spectrometer Array",
        "schema:description": "5 WDS spectrometers with TAPx2, LiFx2, PETJ, LiFH."
      }
    ]
  },
  "ada:laboratory": {
    "@type": ["schema:Place"],
    "schema:name": "National Museum of Natural History, Smithsonian Institution"
  },
  "schema:agent": {
    "@type": ["schema:Organization"],
    "schema:name": "Smithsonian Institution, Department of Mineral Sciences"
  },
  "bios:computationalTool": [
    {
      "@type": ["schema:SoftwareApplication"],
      "schema:name": "Probe for EPMA",
      "ada:toolRole": "acquisition"
    }
  ],
  "ada:methodParameters": [
    {
      "@type": ["schema:PropertyValueSpecification"],
      "schema:name": "WDS Utilization",
      "schema:valueName": "wdsUtilization",
      "ada:fieldScope": "method",
      "ada:category": "Instrument & Software",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": true,
      "schema:defaultValue": "Yes",
      "ada:enumeration": ["Yes", "No"],
      "ada:tier": "M"
    },
    {
      "@type": ["schema:PropertyValueSpecification"],
      "schema:name": "EDS Utilization",
      "schema:valueName": "edsUtilization",
      "ada:fieldScope": "method",
      "ada:category": "Instrument & Software",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": true,
      "schema:defaultValue": "No",
      "ada:enumeration": ["Yes", "No"],
      "ada:tier": "M"
    }
  ],
  "schema:actionProcess": {
    "@type": ["schema:HowTo"],
    "schema:name": "EPMA WDS spinel oxybarometry workflow",
    "schema:step": [
      {
        "@type": ["cdi:Activity", "schema:Action"],
        "schema:name": "Sample preparation",
        "schema:position": 1,
        "schema:additionalType": ["bios:LabProcess"],
        "schema:description": "Spinel-bearing peridotite samples mounted in epoxy, polished, and carbon coated.",
        "schema:result": {
          "@id": "#preparedMount"
        }
      },
      {
        "@type": ["cdi:Activity", "schema:Action"],
        "schema:name": "Instrument calibration",
        "schema:position": 2,
        "schema:description": "Calibrate WDS spectrometers on primary Smithsonian standards. Verify with secondary spinel standards from Wood & Virgo (1989), Bryndzia & Wood (1990), and Ionov & Wood (1992).",
        "schema:object": {"@id": "#preparedMount"},
        "bios:reagent": [
          {
            "@type": ["schema:Thing"],
            "schema:name": "San Carlos olivine",
            "schema:identifier": {
              "@type": ["schema:PropertyValue"],
              "schema:propertyID": "Smithsonian catalog",
              "schema:value": "NMNH 111312/444"
            },
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43–47."
          },
          {
            "@type": ["schema:Thing"],
            "schema:name": "Tiebaghi Mine chromite",
            "schema:identifier": {
              "@type": ["schema:PropertyValue"],
              "schema:propertyID": "Smithsonian catalog",
              "schema:value": "NMNH 117075"
            },
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43–47."
          },
          {
            "@type": ["schema:Thing"],
            "schema:name": "Kakanui Hornblende",
            "schema:identifier": {
              "@type": ["schema:PropertyValue"],
              "schema:propertyID": "Smithsonian catalog",
              "schema:value": "NMNH 143965"
            },
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43–47."
          },
          {
            "@type": ["schema:Thing"],
            "schema:name": "Spinel",
            "schema:identifier": {
              "@type": ["schema:PropertyValue"],
              "schema:propertyID": "Smithsonian catalog",
              "schema:value": "NMNH 136041"
            },
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Davis et al. (2017), American Mineralogist."
          },
          {
            "@type": ["schema:Thing"],
            "schema:name": "Manganite",
            "schema:identifier": {
              "@type": ["schema:PropertyValue"],
              "schema:propertyID": "Smithsonian catalog",
              "schema:value": "NMNH 114887"
            },
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Davis et al. (2017), American Mineralogist."
          },
          {
            "@type": ["schema:Thing"],
            "schema:name": "Wollastonite (synthetic, F.R. Boyd)",
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Davis et al. (2017), American Mineralogist."
          },
          {
            "@type": ["schema:Thing"],
            "schema:name": "IO-5657, PS-216, Vi314-5, IM8703, DB8803-3, BAR8601-10, MO4334-14, KLB8320",
            "schema:description": "Secondary spinel standards for Fe3+/ΣFe calibration",
            "ada:reagentRole": "secondaryStandard",
            "schema:citation": "Wood & Virgo (1989); Bryndzia & Wood (1990); Ionov & Wood (1992)."
          }
        ]
      },
      {
        "@type": ["cdi:Activity", "schema:Action"],
        "schema:name": "WDS data acquisition",
        "schema:position": 3,
        "schema:description": "Quantitative WDS analysis at 15 kV / 40 nA, focused beam. 5 spectrometers measuring SiO2, TiO2, Al2O3, Cr2O3, FeOT, MnO, MgO, CaO, NiO simultaneously.",
        "ada:methodParameters": [
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Accelerating Voltage",
            "schema:valueName": "acceleratingVoltage",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": 15,
            "schema:unitText": "kV",
            "ada:tier": "M"
          },
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Beam Current",
            "schema:valueName": "beamCurrent",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": 40,
            "schema:minValue": 1,
            "schema:maxValue": 200,
            "schema:unitText": "nA",
            "ada:tier": "M"
          },
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Beam Diameter",
            "schema:valueName": "beamDiameter",
            "schema:inDefinedTermSet": {
              "@id": "https://vocab.onegeochemistry.org/epma/beam-modes"
            },
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "Focused beam",
            "ada:enumeration": ["Focused", "Defocused", "Raster"],
            "ada:tier": "M"
          },
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Beam Raster",
            "schema:valueName": "beamRaster",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": false,
            "schema:defaultValue": "none",
            "ada:tier": "R"
          },
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Beam Damage Minimization",
            "schema:valueName": "beamDamageMinimization",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": false,
            "schema:defaultValue": "not applicable",
            "ada:tier": "R"
          }
        ],
        "schema:result": {
          "@id": "#rawAnalyses"
        }
      },
      {
        "@type": ["cdi:Activity", "schema:Action"],
        "schema:name": "Data processing",
        "schema:position": 4,
        "schema:description": "Matrix correction using CITZAF. Fe3+/ΣFe calculated from spinel stoichiometry using flank method calibrated against secondary spinel standards with known Mössbauer Fe3+/ΣFe ratios.",
        "schema:object": {"@id": "#rawAnalyses"},
        "bios:computationalTool": [
          {
            "@type": ["schema:SoftwareApplication"],
            "schema:name": "Probe for EPMA",
            "ada:toolRole": "reduction"
          }
        ],
        "ada:methodParameters": [
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Matrix Correction Model",
            "schema:valueName": "matrixCorrectionModel",
            "schema:propertyID": "https://vocab.onegeochemistry.org/epma/matrix-correction",
            "schema:inDefinedTermSet": {
              "@id": "https://vocab.onegeochemistry.org/epma/matrix-correction-models"
            },
            "ada:fieldScope": "method",
            "ada:category": "Data Processing",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "CITZAF",
            "ada:enumeration": ["PAP", "XPP", "PhiRhoZ", "ZAF", "CITZAF", "Armstrong", "Other"],
            "ada:tier": "M"
          }
        ],
        "schema:result": {
          "@id": "#quantifiedResults"
        }
      },
      {
        "@type": ["cdi:Activity", "schema:Action"],
        "schema:name": "Quality control",
        "schema:position": 5,
        "schema:description": "Primary and secondary standards run at start and end of session; subset run regularly during session.",
        "schema:object": {"@id": "#quantifiedResults"},
        "ada:methodParameters": [
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Drift Correction",
            "schema:valueName": "driftCorrection",
            "ada:fieldScope": "session",
            "ada:category": "Quality Control",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": false,
            "schema:defaultValue": "Primary and secondary standards at start/end; subset run regularly during session.",
            "ada:tier": "R"
          }
        ],
        "dqv:hasQualityMeasurement": [
          {
            "@type": ["dqv:QualityMeasurement"],
            "dqv:isMeasurementOf": "analytical reproducibility",
            "dqv:value": "Davis et al. (2017) report reproducibility on spinels PS211, PS212, OC231350, KLB8304"
          }
        ]
      }
    ]
  },
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Analysed Oxide/Element",
        "schema:valueName": "analysedOxide",
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "cdifVariableMeasured: cdi:name"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Beam Current (nA)",
        "schema:valueName": "beamCurrent",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:maxValue": 200,
        "schema:unitText": "nA",
        "ada:tier": "M"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Spectrometer",
        "schema:valueName": "spectrometer",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Diffracting Crystal",
        "schema:valueName": "diffractingCrystal",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/diffracting-crystals"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:enumeration": ["LIF", "LIFH", "LiF", "PET", "PETJ", "TAP"],
        "ada:tier": "M"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "X-ray Line",
        "schema:valueName": "xrayLine",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/xray-lines"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:enumeration": ["Ka", "Kb", "La", "Lb", "Ma"],
        "ada:tier": "M"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Peak Counting Time (s)",
        "schema:valueName": "peakCountingTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Background Method",
        "schema:valueName": "backgroundMethod",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/background-methods"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Background Counting Time (s)",
        "schema:valueName": "backgroundCountingTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Calibration Standard Name",
        "schema:valueName": "calibrationStandardName",
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Calibration Standard ID",
        "schema:valueName": "calibrationStandardID",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Citation for Standard",
        "schema:valueName": "citationForStandard",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analysedOxide": "SiO2",
        "beamCurrent": 40,
        "spectrometer": "WDS 4",
        "diffractingCrystal": "TAP",
        "xrayLine": "Ka",
        "peakCountingTime": 30,
        "backgroundMethod": "two backgrounds, high and low sides",
        "backgroundCountingTime": 30,
        "calibrationStandardName": "San Carlos olivine",
        "calibrationStandardID": "NMNH 111312/444",
        "citationForStandard": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43–47."
      },
      {
        "analysedOxide": "TiO2",
        "beamCurrent": 40,
        "spectrometer": "WDS 3",
        "diffractingCrystal": "PETJ",
        "xrayLine": "Ka",
        "peakCountingTime": 40,
        "backgroundMethod": "two backgrounds, high and low sides",
        "backgroundCountingTime": 40,
        "calibrationStandardName": "Kakanui Hornblende",
        "calibrationStandardID": "NMNH 143965",
        "citationForStandard": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43–47."
      },
      {
        "analysedOxide": "Al2O3",
        "beamCurrent": 40,
        "spectrometer": "WDS 4",
        "diffractingCrystal": "TAP",
        "xrayLine": "Ka",
        "peakCountingTime": 40,
        "backgroundMethod": "two backgrounds, high and low sides",
        "backgroundCountingTime": 40,
        "calibrationStandardName": "Spinel",
        "calibrationStandardID": "NMNH 136041",
        "citationForStandard": "Davis et al. (2017), American Mineralogist."
      },
      {
        "analysedOxide": "Cr2O3",
        "beamCurrent": 40,
        "spectrometer": "WDS 2",
        "diffractingCrystal": "LiFH",
        "xrayLine": "Ka",
        "peakCountingTime": 30,
        "backgroundMethod": "two backgrounds, high and low sides",
        "backgroundCountingTime": 30,
        "calibrationStandardName": "Tiebaghi Mine chromite",
        "calibrationStandardID": "NMNH 117075",
        "citationForStandard": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43–47."
      },
      {
        "analysedOxide": "FeOT",
        "beamCurrent": 40,
        "spectrometer": "WDS 2",
        "diffractingCrystal": "LiFH",
        "xrayLine": "Ka",
        "peakCountingTime": 30,
        "backgroundMethod": "two backgrounds, high and low sides",
        "backgroundCountingTime": 30,
        "calibrationStandardName": "San Carlos olivine",
        "calibrationStandardID": "NMNH 111312/444",
        "citationForStandard": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43–47."
      },
      {
        "analysedOxide": "MnO",
        "beamCurrent": 40,
        "spectrometer": "WDS 1",
        "diffractingCrystal": "LiF",
        "xrayLine": "Ka",
        "peakCountingTime": 30,
        "backgroundMethod": "two backgrounds, high and low sides",
        "backgroundCountingTime": 30,
        "calibrationStandardName": "Manganite",
        "calibrationStandardID": "NMNH 114887",
        "citationForStandard": "Davis et al. (2017), American Mineralogist."
      },
      {
        "analysedOxide": "MgO",
        "beamCurrent": 40,
        "spectrometer": "WDS 1",
        "diffractingCrystal": "TAP",
        "xrayLine": "Ka",
        "peakCountingTime": 30,
        "backgroundMethod": "two backgrounds, high and low sides",
        "backgroundCountingTime": 30,
        "calibrationStandardName": "San Carlos olivine",
        "calibrationStandardID": "NMNH 111312/444",
        "citationForStandard": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43–47."
      },
      {
        "analysedOxide": "CaO",
        "beamCurrent": 40,
        "spectrometer": "WDS 3",
        "diffractingCrystal": "PETJ",
        "xrayLine": "Ka",
        "peakCountingTime": 30,
        "backgroundMethod": "two backgrounds, high and low sides",
        "backgroundCountingTime": 30,
        "calibrationStandardName": "Wollastonite (synthetic, F.R. Boyd)",
        "citationForStandard": "Davis et al. (2017), American Mineralogist."
      },
      {
        "analysedOxide": "NiO",
        "beamCurrent": 40,
        "spectrometer": "WDS 5",
        "diffractingCrystal": "LiF",
        "xrayLine": "Ka",
        "peakCountingTime": 40,
        "backgroundMethod": "two backgrounds, high and low sides",
        "backgroundCountingTime": 40,
        "calibrationStandardName": "San Carlos olivine",
        "calibrationStandardID": "NMNH 111312/444",
        "citationForStandard": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43–47."
      }
    ]
  },
  "schema:relatedLink": [
    {
      "@type": ["schema:LinkRole"],
      "schema:linkRelationship": "describedIn",
      "schema:target": {
        "@type": ["schema:EntryPoint"],
        "schema:name": "Davis et al. 2017",
        "schema:url": "http://dx.doi.org/10.2138/am-2017-5823"
      }
    },
    {
      "@type": ["schema:LinkRole"],
      "schema:linkRelationship": "describedIn",
      "schema:target": {
        "@type": ["schema:EntryPoint"],
        "schema:name": "Birner et al. 2017",
        "schema:url": "https://doi.org/10.1093/petrology/egx072"
      }
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/methodDefinition/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "dqv": "http://www.w3.org/ns/dqv#",
      "prov": "http://www.w3.org/ns/prov#",
      "skos": "http://www.w3.org/2004/02/skos/core#"
    }
  ],
  "@id": "https://registry.onegeochemistry.org/methods/nmnh-spinel-oxybar-v1",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:MethodDefinition",
    "bios:LabProtocol"
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
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "spinel",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "olivine",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "orthopyroxene",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Product",
      "schema:Thing"
    ],
    "schema:name": "JEOL JXA-8900 Superprobe; JEOL JXA-8530F Hyperprobe",
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
    },
    "schema:hasPart": [
      {
        "@type": [
          "schema:Thing"
        ],
        "schema:name": "WDS Spectrometer Array",
        "schema:description": "5 WDS spectrometers with TAPx2, LiFx2, PETJ, LiFH."
      }
    ]
  },
  "ada:laboratory": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "National Museum of Natural History, Smithsonian Institution"
  },
  "schema:agent": {
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "Smithsonian Institution, Department of Mineral Sciences"
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Probe for EPMA",
      "ada:toolRole": "acquisition"
    }
  ],
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "WDS Utilization",
      "schema:valueName": "wdsUtilization",
      "ada:fieldScope": "method",
      "ada:category": "Instrument & Software",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": true,
      "schema:defaultValue": "Yes",
      "ada:enumeration": [
        "Yes",
        "No"
      ],
      "ada:tier": "M"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "EDS Utilization",
      "schema:valueName": "edsUtilization",
      "ada:fieldScope": "method",
      "ada:category": "Instrument & Software",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": true,
      "schema:defaultValue": "No",
      "ada:enumeration": [
        "Yes",
        "No"
      ],
      "ada:tier": "M"
    }
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:name": "EPMA WDS spinel oxybarometry workflow",
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Sample preparation",
        "schema:position": 1,
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:description": "Spinel-bearing peridotite samples mounted in epoxy, polished, and carbon coated.",
        "schema:result": {
          "@id": "#preparedMount"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Instrument calibration",
        "schema:position": 2,
        "schema:description": "Calibrate WDS spectrometers on primary Smithsonian standards. Verify with secondary spinel standards from Wood & Virgo (1989), Bryndzia & Wood (1990), and Ionov & Wood (1992).",
        "schema:object": {
          "@id": "#preparedMount"
        },
        "bios:reagent": [
          {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "San Carlos olivine",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "Smithsonian catalog",
              "schema:value": "NMNH 111312/444"
            },
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43\u201347."
          },
          {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "Tiebaghi Mine chromite",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "Smithsonian catalog",
              "schema:value": "NMNH 117075"
            },
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43\u201347."
          },
          {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "Kakanui Hornblende",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "Smithsonian catalog",
              "schema:value": "NMNH 143965"
            },
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43\u201347."
          },
          {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "Spinel",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "Smithsonian catalog",
              "schema:value": "NMNH 136041"
            },
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Davis et al. (2017), American Mineralogist."
          },
          {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "Manganite",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "Smithsonian catalog",
              "schema:value": "NMNH 114887"
            },
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Davis et al. (2017), American Mineralogist."
          },
          {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "Wollastonite (synthetic, F.R. Boyd)",
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Davis et al. (2017), American Mineralogist."
          },
          {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "IO-5657, PS-216, Vi314-5, IM8703, DB8803-3, BAR8601-10, MO4334-14, KLB8320",
            "schema:description": "Secondary spinel standards for Fe3+/\u03a3Fe calibration",
            "ada:reagentRole": "secondaryStandard",
            "schema:citation": "Wood & Virgo (1989); Bryndzia & Wood (1990); Ionov & Wood (1992)."
          }
        ]
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "WDS data acquisition",
        "schema:position": 3,
        "schema:description": "Quantitative WDS analysis at 15 kV / 40 nA, focused beam. 5 spectrometers measuring SiO2, TiO2, Al2O3, Cr2O3, FeOT, MnO, MgO, CaO, NiO simultaneously.",
        "ada:methodParameters": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Accelerating Voltage",
            "schema:valueName": "acceleratingVoltage",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": 15,
            "schema:unitText": "kV",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Beam Current",
            "schema:valueName": "beamCurrent",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": 40,
            "schema:minValue": 1,
            "schema:maxValue": 200,
            "schema:unitText": "nA",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Beam Diameter",
            "schema:valueName": "beamDiameter",
            "schema:inDefinedTermSet": {
              "@id": "https://vocab.onegeochemistry.org/epma/beam-modes"
            },
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "Focused beam",
            "ada:enumeration": [
              "Focused",
              "Defocused",
              "Raster"
            ],
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Beam Raster",
            "schema:valueName": "beamRaster",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": false,
            "schema:defaultValue": "none",
            "ada:tier": "R"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Beam Damage Minimization",
            "schema:valueName": "beamDamageMinimization",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": false,
            "schema:defaultValue": "not applicable",
            "ada:tier": "R"
          }
        ],
        "schema:result": {
          "@id": "#rawAnalyses"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data processing",
        "schema:position": 4,
        "schema:description": "Matrix correction using CITZAF. Fe3+/\u03a3Fe calculated from spinel stoichiometry using flank method calibrated against secondary spinel standards with known M\u00f6ssbauer Fe3+/\u03a3Fe ratios.",
        "schema:object": {
          "@id": "#rawAnalyses"
        },
        "bios:computationalTool": [
          {
            "@type": [
              "schema:SoftwareApplication"
            ],
            "schema:name": "Probe for EPMA",
            "ada:toolRole": "reduction"
          }
        ],
        "ada:methodParameters": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Matrix Correction Model",
            "schema:valueName": "matrixCorrectionModel",
            "schema:propertyID": "https://vocab.onegeochemistry.org/epma/matrix-correction",
            "schema:inDefinedTermSet": {
              "@id": "https://vocab.onegeochemistry.org/epma/matrix-correction-models"
            },
            "ada:fieldScope": "method",
            "ada:category": "Data Processing",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "CITZAF",
            "ada:enumeration": [
              "PAP",
              "XPP",
              "PhiRhoZ",
              "ZAF",
              "CITZAF",
              "Armstrong",
              "Other"
            ],
            "ada:tier": "M"
          }
        ],
        "schema:result": {
          "@id": "#quantifiedResults"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Quality control",
        "schema:position": 5,
        "schema:description": "Primary and secondary standards run at start and end of session; subset run regularly during session.",
        "schema:object": {
          "@id": "#quantifiedResults"
        },
        "ada:methodParameters": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Drift Correction",
            "schema:valueName": "driftCorrection",
            "ada:fieldScope": "session",
            "ada:category": "Quality Control",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": false,
            "schema:defaultValue": "Primary and secondary standards at start/end; subset run regularly during session.",
            "ada:tier": "R"
          }
        ],
        "dqv:hasQualityMeasurement": [
          {
            "@type": [
              "dqv:QualityMeasurement"
            ],
            "dqv:isMeasurementOf": "analytical reproducibility",
            "dqv:value": "Davis et al. (2017) report reproducibility on spinels PS211, PS212, OC231350, KLB8304"
          }
        ]
      }
    ]
  },
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analysed Oxide/Element",
        "schema:valueName": "analysedOxide",
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "cdifVariableMeasured: cdi:name"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Beam Current (nA)",
        "schema:valueName": "beamCurrent",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:maxValue": 200,
        "schema:unitText": "nA",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Spectrometer",
        "schema:valueName": "spectrometer",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Diffracting Crystal",
        "schema:valueName": "diffractingCrystal",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/diffracting-crystals"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:enumeration": [
          "LIF",
          "LIFH",
          "LiF",
          "PET",
          "PETJ",
          "TAP"
        ],
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "X-ray Line",
        "schema:valueName": "xrayLine",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/xray-lines"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:enumeration": [
          "Ka",
          "Kb",
          "La",
          "Lb",
          "Ma"
        ],
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Peak Counting Time (s)",
        "schema:valueName": "peakCountingTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Background Method",
        "schema:valueName": "backgroundMethod",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/background-methods"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Background Counting Time (s)",
        "schema:valueName": "backgroundCountingTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Calibration Standard Name",
        "schema:valueName": "calibrationStandardName",
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Calibration Standard ID",
        "schema:valueName": "calibrationStandardID",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Citation for Standard",
        "schema:valueName": "citationForStandard",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analysedOxide": "SiO2",
        "beamCurrent": 40,
        "spectrometer": "WDS 4",
        "diffractingCrystal": "TAP",
        "xrayLine": "Ka",
        "peakCountingTime": 30,
        "backgroundMethod": "two backgrounds, high and low sides",
        "backgroundCountingTime": 30,
        "calibrationStandardName": "San Carlos olivine",
        "calibrationStandardID": "NMNH 111312/444",
        "citationForStandard": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43\u201347."
      },
      {
        "analysedOxide": "TiO2",
        "beamCurrent": 40,
        "spectrometer": "WDS 3",
        "diffractingCrystal": "PETJ",
        "xrayLine": "Ka",
        "peakCountingTime": 40,
        "backgroundMethod": "two backgrounds, high and low sides",
        "backgroundCountingTime": 40,
        "calibrationStandardName": "Kakanui Hornblende",
        "calibrationStandardID": "NMNH 143965",
        "citationForStandard": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43\u201347."
      },
      {
        "analysedOxide": "Al2O3",
        "beamCurrent": 40,
        "spectrometer": "WDS 4",
        "diffractingCrystal": "TAP",
        "xrayLine": "Ka",
        "peakCountingTime": 40,
        "backgroundMethod": "two backgrounds, high and low sides",
        "backgroundCountingTime": 40,
        "calibrationStandardName": "Spinel",
        "calibrationStandardID": "NMNH 136041",
        "citationForStandard": "Davis et al. (2017), American Mineralogist."
      },
      {
        "analysedOxide": "Cr2O3",
        "beamCurrent": 40,
        "spectrometer": "WDS 2",
        "diffractingCrystal": "LiFH",
        "xrayLine": "Ka",
        "peakCountingTime": 30,
        "backgroundMethod": "two backgrounds, high and low sides",
        "backgroundCountingTime": 30,
        "calibrationStandardName": "Tiebaghi Mine chromite",
        "calibrationStandardID": "NMNH 117075",
        "citationForStandard": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43\u201347."
      },
      {
        "analysedOxide": "FeOT",
        "beamCurrent": 40,
        "spectrometer": "WDS 2",
        "diffractingCrystal": "LiFH",
        "xrayLine": "Ka",
        "peakCountingTime": 30,
        "backgroundMethod": "two backgrounds, high and low sides",
        "backgroundCountingTime": 30,
        "calibrationStandardName": "San Carlos olivine",
        "calibrationStandardID": "NMNH 111312/444",
        "citationForStandard": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43\u201347."
      },
      {
        "analysedOxide": "MnO",
        "beamCurrent": 40,
        "spectrometer": "WDS 1",
        "diffractingCrystal": "LiF",
        "xrayLine": "Ka",
        "peakCountingTime": 30,
        "backgroundMethod": "two backgrounds, high and low sides",
        "backgroundCountingTime": 30,
        "calibrationStandardName": "Manganite",
        "calibrationStandardID": "NMNH 114887",
        "citationForStandard": "Davis et al. (2017), American Mineralogist."
      },
      {
        "analysedOxide": "MgO",
        "beamCurrent": 40,
        "spectrometer": "WDS 1",
        "diffractingCrystal": "TAP",
        "xrayLine": "Ka",
        "peakCountingTime": 30,
        "backgroundMethod": "two backgrounds, high and low sides",
        "backgroundCountingTime": 30,
        "calibrationStandardName": "San Carlos olivine",
        "calibrationStandardID": "NMNH 111312/444",
        "citationForStandard": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43\u201347."
      },
      {
        "analysedOxide": "CaO",
        "beamCurrent": 40,
        "spectrometer": "WDS 3",
        "diffractingCrystal": "PETJ",
        "xrayLine": "Ka",
        "peakCountingTime": 30,
        "backgroundMethod": "two backgrounds, high and low sides",
        "backgroundCountingTime": 30,
        "calibrationStandardName": "Wollastonite (synthetic, F.R. Boyd)",
        "citationForStandard": "Davis et al. (2017), American Mineralogist."
      },
      {
        "analysedOxide": "NiO",
        "beamCurrent": 40,
        "spectrometer": "WDS 5",
        "diffractingCrystal": "LiF",
        "xrayLine": "Ka",
        "peakCountingTime": 40,
        "backgroundMethod": "two backgrounds, high and low sides",
        "backgroundCountingTime": 40,
        "calibrationStandardName": "San Carlos olivine",
        "calibrationStandardID": "NMNH 111312/444",
        "citationForStandard": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43\u201347."
      }
    ]
  },
  "schema:relatedLink": [
    {
      "@type": [
        "schema:LinkRole"
      ],
      "schema:linkRelationship": "describedIn",
      "schema:target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "schema:name": "Davis et al. 2017",
        "schema:url": "http://dx.doi.org/10.2138/am-2017-5823"
      }
    },
    {
      "@type": [
        "schema:LinkRole"
      ],
      "schema:linkRelationship": "describedIn",
      "schema:target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "schema:name": "Birner et al. 2017",
        "schema:url": "https://doi.org/10.1093/petrology/egx072"
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://registry.onegeochemistry.org/methods/nmnh-spinel-oxybar-v1> a cdi:Activity,
        schema1:Action,
        ada:MethodDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:name "EPMA WDS spinel oxybarometry workflow" ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Spinel-bearing peridotite samples mounted in epoxy, polished, and carbon coated." ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ;
                    schema1:result <file:///github/workspace/#preparedMount> ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:description "Calibrate WDS spectrometers on primary Smithsonian standards. Verify with secondary spinel standards from Wood & Virgo (1989), Bryndzia & Wood (1990), and Ionov & Wood (1992)." ;
                    schema1:name "Instrument calibration" ;
                    schema1:object <file:///github/workspace/#preparedMount> ;
                    schema1:position 2 ;
                    bios:reagent [ a schema1:Thing ;
                            schema1:citation "Davis et al. (2017), American Mineralogist." ;
                            schema1:name "Wollastonite (synthetic, F.R. Boyd)" ;
                            ada:reagentRole "primaryStandard" ],
                        [ a schema1:Thing ;
                            schema1:citation "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43–47." ;
                            schema1:identifier [ a schema1:PropertyValue ;
                                    schema1:propertyID "Smithsonian catalog" ;
                                    schema1:value "NMNH 143965" ] ;
                            schema1:name "Kakanui Hornblende" ;
                            ada:reagentRole "primaryStandard" ],
                        [ a schema1:Thing ;
                            schema1:citation "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43–47." ;
                            schema1:identifier [ a schema1:PropertyValue ;
                                    schema1:propertyID "Smithsonian catalog" ;
                                    schema1:value "NMNH 117075" ] ;
                            schema1:name "Tiebaghi Mine chromite" ;
                            ada:reagentRole "primaryStandard" ],
                        [ a schema1:Thing ;
                            schema1:citation "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43–47." ;
                            schema1:identifier [ a schema1:PropertyValue ;
                                    schema1:propertyID "Smithsonian catalog" ;
                                    schema1:value "NMNH 111312/444" ] ;
                            schema1:name "San Carlos olivine" ;
                            ada:reagentRole "primaryStandard" ],
                        [ a schema1:Thing ;
                            schema1:citation "Wood & Virgo (1989); Bryndzia & Wood (1990); Ionov & Wood (1992)." ;
                            schema1:description "Secondary spinel standards for Fe3+/ΣFe calibration" ;
                            schema1:name "IO-5657, PS-216, Vi314-5, IM8703, DB8803-3, BAR8601-10, MO4334-14, KLB8320" ;
                            ada:reagentRole "secondaryStandard" ],
                        [ a schema1:Thing ;
                            schema1:citation "Davis et al. (2017), American Mineralogist." ;
                            schema1:identifier [ a schema1:PropertyValue ;
                                    schema1:propertyID "Smithsonian catalog" ;
                                    schema1:value "NMNH 114887" ] ;
                            schema1:name "Manganite" ;
                            ada:reagentRole "primaryStandard" ],
                        [ a schema1:Thing ;
                            schema1:citation "Davis et al. (2017), American Mineralogist." ;
                            schema1:identifier [ a schema1:PropertyValue ;
                                    schema1:propertyID "Smithsonian catalog" ;
                                    schema1:value "NMNH 136041" ] ;
                            schema1:name "Spinel" ;
                            ada:reagentRole "primaryStandard" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:description "Matrix correction using CITZAF. Fe3+/ΣFe calculated from spinel stoichiometry using flank method calibrated against secondary spinel standards with known Mössbauer Fe3+/ΣFe ratios." ;
                    schema1:name "Data processing" ;
                    schema1:object <file:///github/workspace/#rawAnalyses> ;
                    schema1:position 4 ;
                    schema1:result <file:///github/workspace/#quantifiedResults> ;
                    ada:methodParameters [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "CITZAF" ;
                            schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/matrix-correction-models> ;
                            schema1:name "Matrix Correction Model" ;
                            schema1:propertyID "https://vocab.onegeochemistry.org/epma/matrix-correction" ;
                            schema1:readonlyValue true ;
                            schema1:valueName "matrixCorrectionModel" ;
                            schema1:valueRequired true ;
                            ada:category "Data Processing" ;
                            ada:dataType "string" ;
                            ada:enumeration "Armstrong",
                                "CITZAF",
                                "Other",
                                "PAP",
                                "PhiRhoZ",
                                "XPP",
                                "ZAF" ;
                            ada:fieldScope "method" ;
                            ada:tier "M" ] ;
                    bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Probe for EPMA" ;
                            ada:toolRole "reduction" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:description "Quantitative WDS analysis at 15 kV / 40 nA, focused beam. 5 spectrometers measuring SiO2, TiO2, Al2O3, Cr2O3, FeOT, MnO, MgO, CaO, NiO simultaneously." ;
                    schema1:name "WDS data acquisition" ;
                    schema1:position 3 ;
                    schema1:result <file:///github/workspace/#rawAnalyses> ;
                    ada:methodParameters [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "none" ;
                            schema1:name "Beam Raster" ;
                            schema1:readonlyValue true ;
                            schema1:valueName "beamRaster" ;
                            schema1:valueRequired false ;
                            ada:category "Beam Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "method" ;
                            ada:tier "R" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 40 ;
                            schema1:maxValue 200 ;
                            schema1:minValue 1 ;
                            schema1:name "Beam Current" ;
                            schema1:readonlyValue true ;
                            schema1:unitText "nA" ;
                            schema1:valueName "beamCurrent" ;
                            schema1:valueRequired true ;
                            ada:category "Beam Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "method" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "not applicable" ;
                            schema1:name "Beam Damage Minimization" ;
                            schema1:readonlyValue true ;
                            schema1:valueName "beamDamageMinimization" ;
                            schema1:valueRequired false ;
                            ada:category "Beam Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "method" ;
                            ada:tier "R" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "Focused beam" ;
                            schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/beam-modes> ;
                            schema1:name "Beam Diameter" ;
                            schema1:readonlyValue true ;
                            schema1:valueName "beamDiameter" ;
                            schema1:valueRequired true ;
                            ada:category "Beam Conditions" ;
                            ada:dataType "string" ;
                            ada:enumeration "Defocused",
                                "Focused",
                                "Raster" ;
                            ada:fieldScope "method" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 15 ;
                            schema1:name "Accelerating Voltage" ;
                            schema1:readonlyValue true ;
                            schema1:unitText "kV" ;
                            schema1:valueName "acceleratingVoltage" ;
                            schema1:valueRequired true ;
                            ada:category "Beam Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "method" ;
                            ada:tier "M" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:description "Primary and secondary standards run at start and end of session; subset run regularly during session." ;
                    schema1:name "Quality control" ;
                    schema1:object <file:///github/workspace/#quantifiedResults> ;
                    schema1:position 5 ;
                    dqv:hasQualityMeasurement [ a dqv:QualityMeasurement ;
                            dqv:isMeasurementOf "analytical reproducibility" ;
                            dqv:value "Davis et al. (2017) report reproducibility on spinels PS211, PS212, OC231350, KLB8304" ] ;
                    ada:methodParameters [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "Primary and secondary standards at start/end; subset run regularly during session." ;
                            schema1:name "Drift Correction" ;
                            schema1:readonlyValue false ;
                            schema1:valueName "driftCorrection" ;
                            schema1:valueRequired false ;
                            ada:category "Quality Control" ;
                            ada:dataType "string" ;
                            ada:fieldScope "session" ;
                            ada:tier "R" ] ] ] ;
    schema1:agent [ a schema1:Organization ;
            schema1:name "Smithsonian Institution, Department of Mineral Sciences" ] ;
    schema1:datePublished "2013-11-08" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:hasPart [ a schema1:Thing ;
                    schema1:description "5 WDS spectrometers with TAPx2, LiFx2, PETJ, LiFH." ;
                    schema1:name "WDS Spectrometer Array" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "JXA-8900" ] ;
            schema1:name "JEOL JXA-8900 Superprobe; JEOL JXA-8530F Hyperprobe" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
            schema1:name "EPMA-WDS" ] ;
    schema1:name "Spinel oxybarometry version 1" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/materials" ;
            schema1:name "spinel" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/materials" ;
            schema1:name "orthopyroxene" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/materials" ;
            schema1:name "olivine" ] ;
    schema1:relatedLink [ a schema1:LinkRole ;
            schema1:linkRelationship "describedIn" ;
            schema1:target [ a schema1:EntryPoint ;
                    schema1:name "Birner et al. 2017" ;
                    schema1:url "https://doi.org/10.1093/petrology/egx072" ] ],
        [ a schema1:LinkRole ;
            schema1:linkRelationship "describedIn" ;
            schema1:target [ a schema1:EntryPoint ;
                    schema1:name "Davis et al. 2017" ;
                    schema1:url "http://dx.doi.org/10.2138/am-2017-5823" ] ] ;
    schema1:version "1.0" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/diffracting-crystals> ;
                    schema1:name "Diffracting Crystal" ;
                    schema1:valueName "diffractingCrystal" ;
                    schema1:valueRequired true ;
                    ada:dataType "string" ;
                    ada:enumeration "LIF",
                        "LIFH",
                        "LiF",
                        "PET",
                        "PETJ",
                        "TAP" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/background-methods> ;
                    schema1:name "Background Method" ;
                    schema1:valueName "backgroundMethod" ;
                    schema1:valueRequired true ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/xray-lines> ;
                    schema1:name "X-ray Line" ;
                    schema1:valueName "xrayLine" ;
                    schema1:valueRequired true ;
                    ada:dataType "string" ;
                    ada:enumeration "Ka",
                        "Kb",
                        "La",
                        "Lb",
                        "Ma" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Spectrometer" ;
                    schema1:valueName "spectrometer" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:minValue 1 ;
                    schema1:name "Background Counting Time (s)" ;
                    schema1:unitText "seconds" ;
                    schema1:valueName "backgroundCountingTime" ;
                    schema1:valueRequired true ;
                    ada:dataType "number" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Citation for Standard" ;
                    schema1:valueName "citationForStandard" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:minValue 1 ;
                    schema1:name "Peak Counting Time (s)" ;
                    schema1:unitText "seconds" ;
                    schema1:valueName "peakCountingTime" ;
                    schema1:valueRequired true ;
                    ada:dataType "number" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Calibration Standard Name" ;
                    schema1:valueName "calibrationStandardName" ;
                    schema1:valueRequired true ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Calibration Standard ID" ;
                    schema1:valueName "calibrationStandardID" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Analysed Oxide/Element" ;
                    schema1:valueName "analysedOxide" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "cdifVariableMeasured: cdi:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:maxValue 200 ;
                    schema1:minValue 1 ;
                    schema1:name "Beam Current (nA)" ;
                    schema1:unitText "nA" ;
                    schema1:valueName "beamCurrent" ;
                    schema1:valueRequired true ;
                    ada:dataType "number" ;
                    ada:tier "M" ] ;
            ada:defaultAnalytes [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ] ] ;
    ada:laboratory [ a schema1:Place ;
            schema1:name "National Museum of Natural History, Smithsonian Institution" ] ;
    ada:methodParameters [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "Yes" ;
            schema1:name "WDS Utilization" ;
            schema1:readonlyValue true ;
            schema1:valueName "wdsUtilization" ;
            schema1:valueRequired true ;
            ada:category "Instrument & Software" ;
            ada:dataType "string" ;
            ada:enumeration "No",
                "Yes" ;
            ada:fieldScope "method" ;
            ada:tier "M" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "No" ;
            schema1:name "EDS Utilization" ;
            schema1:readonlyValue true ;
            schema1:valueName "edsUtilization" ;
            schema1:valueRequired true ;
            ada:category "Instrument & Software" ;
            ada:dataType "string" ;
            ada:enumeration "No",
                "Yes" ;
            ada:fieldScope "method" ;
            ada:tier "M" ] ;
    bios:computationalTool [ a schema1:SoftwareApplication ;
            schema1:name "Probe for EPMA" ;
            ada:toolRole "acquisition" ] .


```


### LA-ICP-MS Volcanic Glass Trace Elements (UoC v1)
Laser ablation ICP-MS method for trace elements in volcanic glass
from the University of Cologne. Demonstrates a non-EPMA technique
with a different workflow: sample prep, ICP-MS tuning, laser
calibration with NIST612/610/ATHO-G/StHs6/80-G standards, laser
ablation acquisition (193 nm excimer, point mode, 15-20 um spots),
Iolite 4 data reduction, and QC. Shows compound instrument
(laser + mass spec as schema:hasPart), isotope-based analyte
template, and method-level funding/references.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "dqv": "http://www.w3.org/ns/dqv#",
    "prov": "http://www.w3.org/ns/prov#",
    "skos": "http://www.w3.org/2004/02/skos/core#"
  },
  "@id": "https://registry.onegeochemistry.org/methods/uoc-laicpms-glass-v1",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:MethodDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "UoC volcanic glass trace elements v.1",
  "schema:identifier": "http://doi.org/10.60520/IEDA/114187",
  "schema:version": "1.0",
  "schema:datePublished": "2022-04-22",
  "schema:measurementTechnique": {
    "@type": ["schema:DefinedTerm"],
    "schema:name": "LA-ICP-MS",
    "schema:description": "Laser Ablation Inductively Coupled Plasma Mass Spectrometry",
    "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques"
  },
  "schema:object": [
    {
      "@type": ["schema:DefinedTerm"],
      "schema:name": "volcanic glass",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    }
  ],
  "schema:instrument": {
    "@type": ["schema:Product", "schema:Thing"],
    "schema:name": "ESI imageGEO193 laser + Thermo Fischer iCAP Q ICP-MS",
    "schema:hasPart": [
      {
        "@type": ["schema:Thing"],
        "schema:name": "ESI imageGEO193",
        "schema:description": "193 nm ArF excimer laser ablation system",
        "schema:manufacturer": {
          "@type": ["schema:Organization"],
          "schema:name": "Elemental Scientific Lasers (ESI)"
        }
      },
      {
        "@type": ["schema:Thing"],
        "schema:name": "Thermo Fischer iCAP Q",
        "schema:description": "Single-quadrupole ICP-MS",
        "schema:manufacturer": {
          "@type": ["schema:Organization"],
          "schema:name": "Thermo Fisher Scientific"
        }
      }
    ]
  },
  "ada:laboratory": {
    "@type": ["schema:Place"],
    "schema:name": "Geo-/Cosmochemistry lab, Institute of Geology and Mineralogy, University of Cologne, Germany"
  },
  "schema:agent": {
    "@type": ["schema:Organization"],
    "schema:name": "University of Cologne, Institute of Geology and Mineralogy"
  },
  "bios:computationalTool": [
    {
      "@type": ["schema:SoftwareApplication"],
      "schema:name": "Iolite",
      "schema:version": "4",
      "schema:url": "https://iolite-software.com/",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:methodParameters": [
    {
      "@type": ["schema:PropertyValueSpecification"],
      "schema:name": "Internal Standard",
      "schema:valueName": "internalStandard",
      "ada:fieldScope": "method",
      "ada:category": "Calibration",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": true,
      "schema:defaultValue": "Si analyzed by EPMA or EDS",
      "schema:description": "Internal standard element and how its concentration is derived for each unknown.",
      "ada:tier": "M"
    },
    {
      "@type": ["schema:PropertyValueSpecification"],
      "schema:name": "Element Fractionation Correction",
      "schema:valueName": "elementFractionationCorrection",
      "ada:fieldScope": "method",
      "ada:category": "Data Processing",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": false,
      "schema:defaultValue": "No correction other than measurement relative to NIST612 and use of Si as internal standard",
      "ada:tier": "R"
    },
    {
      "@type": ["schema:PropertyValueSpecification"],
      "schema:name": "Calibration/QC/Unknown Sequence",
      "schema:valueName": "analysisSequenceRatio",
      "schema:description": "Ratio of calibration standard / QC standard / unknown analyses in a repeating block.",
      "ada:fieldScope": "session",
      "ada:category": "Quality Control",
      "ada:dataType": "string",
      "schema:readonlyValue": false,
      "schema:valueRequired": false,
      "schema:defaultValue": "2/4/15",
      "ada:tier": "R"
    },
    {
      "@type": ["schema:PropertyValueSpecification"],
      "schema:name": "Detection Limit Method",
      "schema:valueName": "detectionLimitMethod",
      "ada:fieldScope": "method",
      "ada:category": "Quality Control",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": false,
      "schema:defaultValue": "Sample individual LOD calculation according to Pettke et al. (2012)",
      "ada:tier": "R"
    }
  ],
  "schema:funding": [
    {
      "@type": ["schema:MonetaryGrant"],
      "schema:identifier": "DFG INST 216/1019-1 FUGG no. 665508",
      "schema:funder": {
        "@type": ["schema:Organization"],
        "schema:name": "Deutsche Forschungsgemeinschaft (DFG)"
      }
    }
  ],
  "schema:relatedLink": [
    {
      "@type": ["schema:LinkRole"],
      "schema:linkRelationship": "methodology",
      "schema:target": {
        "@type": ["schema:EntryPoint"],
        "schema:name": "Pettke et al. (2012)",
        "schema:url": "https://doi.org/10.1016/j.oregeorev.2011.11.001"
      }
    }
  ],
  "schema:actionProcess": {
    "@type": ["schema:HowTo"],
    "schema:name": "LA-ICP-MS volcanic glass trace element workflow",
    "schema:step": [
      {
        "@type": ["cdi:Activity", "schema:Action"],
        "schema:name": "Sample preparation",
        "schema:position": 1,
        "schema:additionalType": ["bios:LabProcess"],
        "schema:description": "Volcanic glass shards or tephra grains mounted in epoxy, polished to expose flat surfaces, and carbon coated for prior EPMA analysis of major elements (Si used as internal standard).",
        "schema:result": {
          "@id": "#preparedMount"
        }
      },
      {
        "@type": ["cdi:Activity", "schema:Action"],
        "schema:name": "ICP-MS tuning and optimization",
        "schema:position": 2,
        "schema:description": "Tune ICP-MS using auto-tune function on line scan of NIST612. Optimize for maximum sensitivity while minimizing oxide production (ThO/Th ~0.7%).",
        "ada:methodParameters": [
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "RF Power",
            "schema:valueName": "rfPower",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 1200,
            "schema:unitText": "W",
            "ada:tier": "M"
          },
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Carrier Gas (He) Flow Rate",
            "schema:valueName": "carrierGasHeFlowRate",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 0.9,
            "schema:unitText": "L/min",
            "ada:tier": "M"
          },
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Carrier Gas (Ar) Flow Rate",
            "schema:valueName": "carrierGasArFlowRate",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 0.8,
            "schema:unitText": "L/min",
            "ada:tier": "M"
          },
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Signal Smoothing",
            "schema:valueName": "signalSmoothing",
            "ada:fieldScope": "method",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": false,
            "schema:defaultValue": "Glass smoothing device",
            "ada:tier": "R"
          },
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Oxide Production (ThO/Th)",
            "schema:valueName": "oxideProduction",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": "ca. 0.7%",
            "ada:tier": "M"
          }
        ]
      },
      {
        "@type": ["cdi:Activity", "schema:Action"],
        "schema:name": "Laser ablation calibration",
        "schema:position": 3,
        "schema:description": "Calibrate using NIST612 as primary reference material. Verify with secondary standards NIST610, ATHO-G, and StHs6/80-G.",
        "bios:reagent": [
          {
            "@type": ["schema:Thing"],
            "schema:name": "NIST SRM 612",
            "schema:description": "Trace Elements in Glass (nominal 50 ppm)",
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Jochum et al. (2011), Geostandards and Geoanalytical Research, 35(4): 397–429."
          },
          {
            "@type": ["schema:Thing"],
            "schema:name": "NIST SRM 610",
            "schema:description": "Trace Elements in Glass (nominal 500 ppm)",
            "ada:reagentRole": "secondaryStandard",
            "schema:citation": "Jochum et al. (2011), Geostandards and Geoanalytical Research, 35(4): 397–429."
          },
          {
            "@type": ["schema:Thing"],
            "schema:name": "ATHO-G",
            "schema:description": "MPI-DING Icelandic rhyolite glass",
            "ada:reagentRole": "secondaryStandard",
            "schema:citation": "Jochum et al. (2006), Geochemistry Geophysics Geosystems, 7(2)."
          },
          {
            "@type": ["schema:Thing"],
            "schema:name": "StHs6/80-G",
            "schema:description": "MPI-DING St. Helens dacite glass",
            "ada:reagentRole": "secondaryStandard",
            "schema:citation": "Jochum et al. (2006), Geochemistry Geophysics Geosystems, 7(2)."
          }
        ]
      },
      {
        "@type": ["cdi:Activity", "schema:Action"],
        "schema:name": "Laser ablation data acquisition",
        "schema:position": 4,
        "schema:description": "Ablate sample in point mode with 15–20 um spot. 30 s gas blank followed by 40 s ablation. Helium carrier gas transports aerosol to ICP-MS via signal smoothing device.",
        "schema:object": {"@id": "#preparedMount"},
        "ada:methodParameters": [
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Laser Wavelength",
            "schema:valueName": "laserWavelength",
            "ada:fieldScope": "method",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "193 nm (ArF excimer)",
            "ada:tier": "M"
          },
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Laser Spot Width",
            "schema:valueName": "laserSpotWidth",
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": "15; 20",
            "schema:description": "Spot width in um; multiple values if varied during session.",
            "schema:unitText": "um",
            "ada:tier": "M"
          },
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Laser Spot Path Geometry",
            "schema:valueName": "laserSpotPathGeometry",
            "schema:inDefinedTermSet": {
              "@id": "https://vocab.onegeochemistry.org/laicpms/spot-geometries"
            },
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": "point",
            "ada:enumeration": ["Point", "Transect", "Area", "Map"],
            "ada:tier": "M"
          },
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Laser Energy",
            "schema:valueName": "laserEnergy",
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 0.001,
            "schema:unitText": "mJ",
            "ada:tier": "M"
          },
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Laser Pulse Time",
            "schema:valueName": "laserPulseTime",
            "ada:fieldScope": "method",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "7 ns",
            "ada:tier": "M"
          },
          {
            "@type": ["schema:PropertyValueSpecification"],
            "schema:name": "Repetition Rate",
            "schema:valueName": "repetitionRate",
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 5,
            "schema:unitText": "Hz",
            "ada:tier": "M"
          }
        ],
        "schema:result": {
          "@id": "#rawSignals"
        }
      },
      {
        "@type": ["cdi:Activity", "schema:Action"],
        "schema:name": "Data reduction",
        "schema:position": 5,
        "schema:description": "Process raw time-resolved signals in Iolite 4. Background subtraction using 30 s pre-ablation gas blank. Normalize to NIST612 with Si as internal standard. Calculate concentrations and sample-individual detection limits per Pettke et al. (2012).",
        "schema:object": {"@id": "#rawSignals"},
        "bios:computationalTool": [
          {
            "@type": ["schema:SoftwareApplication"],
            "schema:name": "Iolite",
            "schema:version": "4",
            "ada:toolRole": "reduction"
          }
        ],
        "schema:result": {
          "@id": "#quantifiedConcentrations"
        }
      },
      {
        "@type": ["cdi:Activity", "schema:Action"],
        "schema:name": "Quality control",
        "schema:position": 6,
        "schema:description": "Secondary standards (NIST610, ATHO-G, StHs6/80-G) analysed interspersed with unknowns in ratio 2 calibration / 4 QC / 15 unknowns. Drift monitored via repeated NIST612 analyses throughout session.",
        "schema:object": {"@id": "#quantifiedConcentrations"},
        "dqv:hasQualityMeasurement": [
          {
            "@type": ["dqv:QualityMeasurement"],
            "dqv:isMeasurementOf": "oxide production",
            "dqv:value": "ThO/Th ca. 0.7%"
          },
          {
            "@type": ["dqv:QualityMeasurement"],
            "dqv:isMeasurementOf": "detection limit method",
            "dqv:value": "Sample-individual LOD per Pettke et al. (2012)"
          }
        ]
      }
    ]
  },
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Measured Isotope",
        "schema:valueName": "measuredIsotope",
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "schema:description": "Element symbol with mass number (e.g. Si29, Ba138, U238).",
        "ada:tier": "M"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Spectrometer Dwell Time",
        "schema:valueName": "spectrometerDwellTime",
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "schema:description": "Dwell time per isotope per sweep in seconds.",
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Analysis Count Time",
        "schema:valueName": "analysisCountTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:description": "Total signal integration time during ablation in seconds.",
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Background Count Time",
        "schema:valueName": "backgroundCountTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:description": "Gas blank measurement time before ablation in seconds.",
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Detection Limit",
        "schema:valueName": "detectionLimit",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "schema:description": "Typical detection limit at 99% confidence (3-sigma).",
        "ada:tier": "R"
      },
      {
        "@type": ["schema:PropertyValueSpecification"],
        "schema:name": "Detection Limit Unit",
        "schema:valueName": "detectionLimitUnit",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:enumeration": ["ppm", "ppb", "weight percent (%m/m)"],
        "ada:tier": "R"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "measuredIsotope": "Si29",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "internal standard",
        "detectionLimitUnit": ""
      },
      {
        "measuredIsotope": "Ca43",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Rb85",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Sr88",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Y89",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Zr90",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Nb93",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Ba138",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "La139",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Ce140",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Nd146",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Sm147",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Eu153",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Gd157",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Dy163",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Er166",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Yb172",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Lu175",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Hf178",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Th232",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "U238",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      }
    ]
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/methodDefinition/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "dqv": "http://www.w3.org/ns/dqv#",
      "prov": "http://www.w3.org/ns/prov#",
      "skos": "http://www.w3.org/2004/02/skos/core#"
    }
  ],
  "@id": "https://registry.onegeochemistry.org/methods/uoc-laicpms-glass-v1",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:MethodDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "UoC volcanic glass trace elements v.1",
  "schema:identifier": "http://doi.org/10.60520/IEDA/114187",
  "schema:version": "1.0",
  "schema:datePublished": "2022-04-22",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "LA-ICP-MS",
    "schema:description": "Laser Ablation Inductively Coupled Plasma Mass Spectrometry",
    "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "volcanic glass",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Product",
      "schema:Thing"
    ],
    "schema:name": "ESI imageGEO193 laser + Thermo Fischer iCAP Q ICP-MS",
    "schema:hasPart": [
      {
        "@type": [
          "schema:Thing"
        ],
        "schema:name": "ESI imageGEO193",
        "schema:description": "193 nm ArF excimer laser ablation system",
        "schema:manufacturer": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Elemental Scientific Lasers (ESI)"
        }
      },
      {
        "@type": [
          "schema:Thing"
        ],
        "schema:name": "Thermo Fischer iCAP Q",
        "schema:description": "Single-quadrupole ICP-MS",
        "schema:manufacturer": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Thermo Fisher Scientific"
        }
      }
    ]
  },
  "ada:laboratory": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Geo-/Cosmochemistry lab, Institute of Geology and Mineralogy, University of Cologne, Germany"
  },
  "schema:agent": {
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "University of Cologne, Institute of Geology and Mineralogy"
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Iolite",
      "schema:version": "4",
      "schema:url": "https://iolite-software.com/",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Internal Standard",
      "schema:valueName": "internalStandard",
      "ada:fieldScope": "method",
      "ada:category": "Calibration",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": true,
      "schema:defaultValue": "Si analyzed by EPMA or EDS",
      "schema:description": "Internal standard element and how its concentration is derived for each unknown.",
      "ada:tier": "M"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Element Fractionation Correction",
      "schema:valueName": "elementFractionationCorrection",
      "ada:fieldScope": "method",
      "ada:category": "Data Processing",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": false,
      "schema:defaultValue": "No correction other than measurement relative to NIST612 and use of Si as internal standard",
      "ada:tier": "R"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Calibration/QC/Unknown Sequence",
      "schema:valueName": "analysisSequenceRatio",
      "schema:description": "Ratio of calibration standard / QC standard / unknown analyses in a repeating block.",
      "ada:fieldScope": "session",
      "ada:category": "Quality Control",
      "ada:dataType": "string",
      "schema:readonlyValue": false,
      "schema:valueRequired": false,
      "schema:defaultValue": "2/4/15",
      "ada:tier": "R"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Detection Limit Method",
      "schema:valueName": "detectionLimitMethod",
      "ada:fieldScope": "method",
      "ada:category": "Quality Control",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": false,
      "schema:defaultValue": "Sample individual LOD calculation according to Pettke et al. (2012)",
      "ada:tier": "R"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:identifier": "DFG INST 216/1019-1 FUGG no. 665508",
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "Deutsche Forschungsgemeinschaft (DFG)"
      }
    }
  ],
  "schema:relatedLink": [
    {
      "@type": [
        "schema:LinkRole"
      ],
      "schema:linkRelationship": "methodology",
      "schema:target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "schema:name": "Pettke et al. (2012)",
        "schema:url": "https://doi.org/10.1016/j.oregeorev.2011.11.001"
      }
    }
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:name": "LA-ICP-MS volcanic glass trace element workflow",
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Sample preparation",
        "schema:position": 1,
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:description": "Volcanic glass shards or tephra grains mounted in epoxy, polished to expose flat surfaces, and carbon coated for prior EPMA analysis of major elements (Si used as internal standard).",
        "schema:result": {
          "@id": "#preparedMount"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "ICP-MS tuning and optimization",
        "schema:position": 2,
        "schema:description": "Tune ICP-MS using auto-tune function on line scan of NIST612. Optimize for maximum sensitivity while minimizing oxide production (ThO/Th ~0.7%).",
        "ada:methodParameters": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "RF Power",
            "schema:valueName": "rfPower",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 1200,
            "schema:unitText": "W",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Carrier Gas (He) Flow Rate",
            "schema:valueName": "carrierGasHeFlowRate",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 0.9,
            "schema:unitText": "L/min",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Carrier Gas (Ar) Flow Rate",
            "schema:valueName": "carrierGasArFlowRate",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 0.8,
            "schema:unitText": "L/min",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Signal Smoothing",
            "schema:valueName": "signalSmoothing",
            "ada:fieldScope": "method",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": false,
            "schema:defaultValue": "Glass smoothing device",
            "ada:tier": "R"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Oxide Production (ThO/Th)",
            "schema:valueName": "oxideProduction",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": "ca. 0.7%",
            "ada:tier": "M"
          }
        ]
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Laser ablation calibration",
        "schema:position": 3,
        "schema:description": "Calibrate using NIST612 as primary reference material. Verify with secondary standards NIST610, ATHO-G, and StHs6/80-G.",
        "bios:reagent": [
          {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "NIST SRM 612",
            "schema:description": "Trace Elements in Glass (nominal 50 ppm)",
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Jochum et al. (2011), Geostandards and Geoanalytical Research, 35(4): 397\u2013429."
          },
          {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "NIST SRM 610",
            "schema:description": "Trace Elements in Glass (nominal 500 ppm)",
            "ada:reagentRole": "secondaryStandard",
            "schema:citation": "Jochum et al. (2011), Geostandards and Geoanalytical Research, 35(4): 397\u2013429."
          },
          {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "ATHO-G",
            "schema:description": "MPI-DING Icelandic rhyolite glass",
            "ada:reagentRole": "secondaryStandard",
            "schema:citation": "Jochum et al. (2006), Geochemistry Geophysics Geosystems, 7(2)."
          },
          {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "StHs6/80-G",
            "schema:description": "MPI-DING St. Helens dacite glass",
            "ada:reagentRole": "secondaryStandard",
            "schema:citation": "Jochum et al. (2006), Geochemistry Geophysics Geosystems, 7(2)."
          }
        ]
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Laser ablation data acquisition",
        "schema:position": 4,
        "schema:description": "Ablate sample in point mode with 15\u201320 um spot. 30 s gas blank followed by 40 s ablation. Helium carrier gas transports aerosol to ICP-MS via signal smoothing device.",
        "schema:object": {
          "@id": "#preparedMount"
        },
        "ada:methodParameters": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Wavelength",
            "schema:valueName": "laserWavelength",
            "ada:fieldScope": "method",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "193 nm (ArF excimer)",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Spot Width",
            "schema:valueName": "laserSpotWidth",
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": "15; 20",
            "schema:description": "Spot width in um; multiple values if varied during session.",
            "schema:unitText": "um",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Spot Path Geometry",
            "schema:valueName": "laserSpotPathGeometry",
            "schema:inDefinedTermSet": {
              "@id": "https://vocab.onegeochemistry.org/laicpms/spot-geometries"
            },
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": "point",
            "ada:enumeration": [
              "Point",
              "Transect",
              "Area",
              "Map"
            ],
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Energy",
            "schema:valueName": "laserEnergy",
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 0.001,
            "schema:unitText": "mJ",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Pulse Time",
            "schema:valueName": "laserPulseTime",
            "ada:fieldScope": "method",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "7 ns",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Repetition Rate",
            "schema:valueName": "repetitionRate",
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 5,
            "schema:unitText": "Hz",
            "ada:tier": "M"
          }
        ],
        "schema:result": {
          "@id": "#rawSignals"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
        "schema:position": 5,
        "schema:description": "Process raw time-resolved signals in Iolite 4. Background subtraction using 30 s pre-ablation gas blank. Normalize to NIST612 with Si as internal standard. Calculate concentrations and sample-individual detection limits per Pettke et al. (2012).",
        "schema:object": {
          "@id": "#rawSignals"
        },
        "bios:computationalTool": [
          {
            "@type": [
              "schema:SoftwareApplication"
            ],
            "schema:name": "Iolite",
            "schema:version": "4",
            "ada:toolRole": "reduction"
          }
        ],
        "schema:result": {
          "@id": "#quantifiedConcentrations"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Quality control",
        "schema:position": 6,
        "schema:description": "Secondary standards (NIST610, ATHO-G, StHs6/80-G) analysed interspersed with unknowns in ratio 2 calibration / 4 QC / 15 unknowns. Drift monitored via repeated NIST612 analyses throughout session.",
        "schema:object": {
          "@id": "#quantifiedConcentrations"
        },
        "dqv:hasQualityMeasurement": [
          {
            "@type": [
              "dqv:QualityMeasurement"
            ],
            "dqv:isMeasurementOf": "oxide production",
            "dqv:value": "ThO/Th ca. 0.7%"
          },
          {
            "@type": [
              "dqv:QualityMeasurement"
            ],
            "dqv:isMeasurementOf": "detection limit method",
            "dqv:value": "Sample-individual LOD per Pettke et al. (2012)"
          }
        ]
      }
    ]
  },
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Measured Isotope",
        "schema:valueName": "measuredIsotope",
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "schema:description": "Element symbol with mass number (e.g. Si29, Ba138, U238).",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Spectrometer Dwell Time",
        "schema:valueName": "spectrometerDwellTime",
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "schema:description": "Dwell time per isotope per sweep in seconds.",
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analysis Count Time",
        "schema:valueName": "analysisCountTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:description": "Total signal integration time during ablation in seconds.",
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Background Count Time",
        "schema:valueName": "backgroundCountTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:description": "Gas blank measurement time before ablation in seconds.",
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Detection Limit",
        "schema:valueName": "detectionLimit",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "schema:description": "Typical detection limit at 99% confidence (3-sigma).",
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Detection Limit Unit",
        "schema:valueName": "detectionLimitUnit",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:enumeration": [
          "ppm",
          "ppb",
          "weight percent (%m/m)"
        ],
        "ada:tier": "R"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "measuredIsotope": "Si29",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "internal standard",
        "detectionLimitUnit": ""
      },
      {
        "measuredIsotope": "Ca43",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Rb85",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Sr88",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Y89",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Zr90",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Nb93",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Ba138",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "La139",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Ce140",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Nd146",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Sm147",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Eu153",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Gd157",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Dy163",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Er166",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Yb172",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Lu175",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Hf178",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "Th232",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      },
      {
        "measuredIsotope": "U238",
        "spectrometerDwellTime": "1e-8",
        "analysisCountTime": 40,
        "backgroundCountTime": 30,
        "detectionLimit": "sample individual LOD",
        "detectionLimitUnit": "ppm"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://registry.onegeochemistry.org/methods/uoc-laicpms-glass-v1> a cdi:Activity,
        schema1:Action,
        ada:MethodDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:name "LA-ICP-MS volcanic glass trace element workflow" ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:description "Ablate sample in point mode with 15–20 um spot. 30 s gas blank followed by 40 s ablation. Helium carrier gas transports aerosol to ICP-MS via signal smoothing device." ;
                    schema1:name "Laser ablation data acquisition" ;
                    schema1:object <file:///github/workspace/#preparedMount> ;
                    schema1:position 4 ;
                    schema1:result <file:///github/workspace/#rawSignals> ;
                    ada:methodParameters [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 5 ;
                            schema1:name "Repetition Rate" ;
                            schema1:readonlyValue false ;
                            schema1:unitText "Hz" ;
                            schema1:valueName "repetitionRate" ;
                            schema1:valueRequired true ;
                            ada:category "Laser Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 1e-03 ;
                            schema1:name "Laser Energy" ;
                            schema1:readonlyValue false ;
                            schema1:unitText "mJ" ;
                            schema1:valueName "laserEnergy" ;
                            schema1:valueRequired true ;
                            ada:category "Laser Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "15; 20" ;
                            schema1:description "Spot width in um; multiple values if varied during session." ;
                            schema1:name "Laser Spot Width" ;
                            schema1:readonlyValue false ;
                            schema1:unitText "um" ;
                            schema1:valueName "laserSpotWidth" ;
                            schema1:valueRequired true ;
                            ada:category "Laser Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "point" ;
                            schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/laicpms/spot-geometries> ;
                            schema1:name "Laser Spot Path Geometry" ;
                            schema1:readonlyValue false ;
                            schema1:valueName "laserSpotPathGeometry" ;
                            schema1:valueRequired true ;
                            ada:category "Laser Conditions" ;
                            ada:dataType "string" ;
                            ada:enumeration "Area",
                                "Map",
                                "Point",
                                "Transect" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "193 nm (ArF excimer)" ;
                            schema1:name "Laser Wavelength" ;
                            schema1:readonlyValue true ;
                            schema1:valueName "laserWavelength" ;
                            schema1:valueRequired true ;
                            ada:category "Laser Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "method" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "7 ns" ;
                            schema1:name "Laser Pulse Time" ;
                            schema1:readonlyValue true ;
                            schema1:valueName "laserPulseTime" ;
                            schema1:valueRequired true ;
                            ada:category "Laser Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "method" ;
                            ada:tier "M" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:description "Process raw time-resolved signals in Iolite 4. Background subtraction using 30 s pre-ablation gas blank. Normalize to NIST612 with Si as internal standard. Calculate concentrations and sample-individual detection limits per Pettke et al. (2012)." ;
                    schema1:name "Data reduction" ;
                    schema1:object <file:///github/workspace/#rawSignals> ;
                    schema1:position 5 ;
                    schema1:result <file:///github/workspace/#quantifiedConcentrations> ;
                    bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Iolite" ;
                            schema1:version "4" ;
                            ada:toolRole "reduction" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Volcanic glass shards or tephra grains mounted in epoxy, polished to expose flat surfaces, and carbon coated for prior EPMA analysis of major elements (Si used as internal standard)." ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ;
                    schema1:result <file:///github/workspace/#preparedMount> ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:description "Secondary standards (NIST610, ATHO-G, StHs6/80-G) analysed interspersed with unknowns in ratio 2 calibration / 4 QC / 15 unknowns. Drift monitored via repeated NIST612 analyses throughout session." ;
                    schema1:name "Quality control" ;
                    schema1:object <file:///github/workspace/#quantifiedConcentrations> ;
                    schema1:position 6 ;
                    dqv:hasQualityMeasurement [ a dqv:QualityMeasurement ;
                            dqv:isMeasurementOf "detection limit method" ;
                            dqv:value "Sample-individual LOD per Pettke et al. (2012)" ],
                        [ a dqv:QualityMeasurement ;
                            dqv:isMeasurementOf "oxide production" ;
                            dqv:value "ThO/Th ca. 0.7%" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:description "Calibrate using NIST612 as primary reference material. Verify with secondary standards NIST610, ATHO-G, and StHs6/80-G." ;
                    schema1:name "Laser ablation calibration" ;
                    schema1:position 3 ;
                    bios:reagent [ a schema1:Thing ;
                            schema1:citation "Jochum et al. (2011), Geostandards and Geoanalytical Research, 35(4): 397–429." ;
                            schema1:description "Trace Elements in Glass (nominal 50 ppm)" ;
                            schema1:name "NIST SRM 612" ;
                            ada:reagentRole "primaryStandard" ],
                        [ a schema1:Thing ;
                            schema1:citation "Jochum et al. (2006), Geochemistry Geophysics Geosystems, 7(2)." ;
                            schema1:description "MPI-DING St. Helens dacite glass" ;
                            schema1:name "StHs6/80-G" ;
                            ada:reagentRole "secondaryStandard" ],
                        [ a schema1:Thing ;
                            schema1:citation "Jochum et al. (2011), Geostandards and Geoanalytical Research, 35(4): 397–429." ;
                            schema1:description "Trace Elements in Glass (nominal 500 ppm)" ;
                            schema1:name "NIST SRM 610" ;
                            ada:reagentRole "secondaryStandard" ],
                        [ a schema1:Thing ;
                            schema1:citation "Jochum et al. (2006), Geochemistry Geophysics Geosystems, 7(2)." ;
                            schema1:description "MPI-DING Icelandic rhyolite glass" ;
                            schema1:name "ATHO-G" ;
                            ada:reagentRole "secondaryStandard" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:description "Tune ICP-MS using auto-tune function on line scan of NIST612. Optimize for maximum sensitivity while minimizing oxide production (ThO/Th ~0.7%)." ;
                    schema1:name "ICP-MS tuning and optimization" ;
                    schema1:position 2 ;
                    ada:methodParameters [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 1200 ;
                            schema1:name "RF Power" ;
                            schema1:readonlyValue false ;
                            schema1:unitText "W" ;
                            schema1:valueName "rfPower" ;
                            schema1:valueRequired true ;
                            ada:category "ICP-MS Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 9e-01 ;
                            schema1:name "Carrier Gas (He) Flow Rate" ;
                            schema1:readonlyValue false ;
                            schema1:unitText "L/min" ;
                            schema1:valueName "carrierGasHeFlowRate" ;
                            schema1:valueRequired true ;
                            ada:category "ICP-MS Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "Glass smoothing device" ;
                            schema1:name "Signal Smoothing" ;
                            schema1:readonlyValue true ;
                            schema1:valueName "signalSmoothing" ;
                            schema1:valueRequired false ;
                            ada:category "ICP-MS Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "method" ;
                            ada:tier "R" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "ca. 0.7%" ;
                            schema1:name "Oxide Production (ThO/Th)" ;
                            schema1:readonlyValue false ;
                            schema1:valueName "oxideProduction" ;
                            schema1:valueRequired true ;
                            ada:category "ICP-MS Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 8e-01 ;
                            schema1:name "Carrier Gas (Ar) Flow Rate" ;
                            schema1:readonlyValue false ;
                            schema1:unitText "L/min" ;
                            schema1:valueName "carrierGasArFlowRate" ;
                            schema1:valueRequired true ;
                            ada:category "ICP-MS Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ] ] ] ;
    schema1:agent [ a schema1:Organization ;
            schema1:name "University of Cologne, Institute of Geology and Mineralogy" ] ;
    schema1:datePublished "2022-04-22" ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:funder [ a schema1:Organization ;
                    schema1:name "Deutsche Forschungsgemeinschaft (DFG)" ] ;
            schema1:identifier "DFG INST 216/1019-1 FUGG no. 665508" ] ;
    schema1:identifier "http://doi.org/10.60520/IEDA/114187" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:hasPart [ a schema1:Thing ;
                    schema1:description "193 nm ArF excimer laser ablation system" ;
                    schema1:manufacturer [ a schema1:Organization ;
                            schema1:name "Elemental Scientific Lasers (ESI)" ] ;
                    schema1:name "ESI imageGEO193" ],
                [ a schema1:Thing ;
                    schema1:description "Single-quadrupole ICP-MS" ;
                    schema1:manufacturer [ a schema1:Organization ;
                            schema1:name "Thermo Fisher Scientific" ] ;
                    schema1:name "Thermo Fischer iCAP Q" ] ;
            schema1:name "ESI imageGEO193 laser + Thermo Fischer iCAP Q ICP-MS" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:description "Laser Ablation Inductively Coupled Plasma Mass Spectrometry" ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
            schema1:name "LA-ICP-MS" ] ;
    schema1:name "UoC volcanic glass trace elements v.1" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/materials" ;
            schema1:name "volcanic glass" ] ;
    schema1:relatedLink [ a schema1:LinkRole ;
            schema1:linkRelationship "methodology" ;
            schema1:target [ a schema1:EntryPoint ;
                    schema1:name "Pettke et al. (2012)" ;
                    schema1:url "https://doi.org/10.1016/j.oregeorev.2011.11.001" ] ] ;
    schema1:version "1.0" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:description "Gas blank measurement time before ablation in seconds." ;
                    schema1:minValue 1 ;
                    schema1:name "Background Count Time" ;
                    schema1:unitText "seconds" ;
                    schema1:valueName "backgroundCountTime" ;
                    schema1:valueRequired true ;
                    ada:dataType "number" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:description "Typical detection limit at 99% confidence (3-sigma)." ;
                    schema1:name "Detection Limit" ;
                    schema1:valueName "detectionLimit" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Detection Limit Unit" ;
                    schema1:valueName "detectionLimitUnit" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:enumeration "ppb",
                        "ppm",
                        "weight percent (%m/m)" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:description "Element symbol with mass number (e.g. Si29, Ba138, U238)." ;
                    schema1:name "Measured Isotope" ;
                    schema1:valueName "measuredIsotope" ;
                    schema1:valueRequired true ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:description "Dwell time per isotope per sweep in seconds." ;
                    schema1:name "Spectrometer Dwell Time" ;
                    schema1:unitText "seconds" ;
                    schema1:valueName "spectrometerDwellTime" ;
                    schema1:valueRequired true ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:description "Total signal integration time during ablation in seconds." ;
                    schema1:minValue 1 ;
                    schema1:name "Analysis Count Time" ;
                    schema1:unitText "seconds" ;
                    schema1:valueName "analysisCountTime" ;
                    schema1:valueRequired true ;
                    ada:dataType "number" ;
                    ada:tier "M" ] ;
            ada:defaultAnalytes [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ] ] ;
    ada:laboratory [ a schema1:Place ;
            schema1:name "Geo-/Cosmochemistry lab, Institute of Geology and Mineralogy, University of Cologne, Germany" ] ;
    ada:methodParameters [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "2/4/15" ;
            schema1:description "Ratio of calibration standard / QC standard / unknown analyses in a repeating block." ;
            schema1:name "Calibration/QC/Unknown Sequence" ;
            schema1:readonlyValue false ;
            schema1:valueName "analysisSequenceRatio" ;
            schema1:valueRequired false ;
            ada:category "Quality Control" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "Sample individual LOD calculation according to Pettke et al. (2012)" ;
            schema1:name "Detection Limit Method" ;
            schema1:readonlyValue true ;
            schema1:valueName "detectionLimitMethod" ;
            schema1:valueRequired false ;
            ada:category "Quality Control" ;
            ada:dataType "string" ;
            ada:fieldScope "method" ;
            ada:tier "R" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "No correction other than measurement relative to NIST612 and use of Si as internal standard" ;
            schema1:name "Element Fractionation Correction" ;
            schema1:readonlyValue true ;
            schema1:valueName "elementFractionationCorrection" ;
            schema1:valueRequired false ;
            ada:category "Data Processing" ;
            ada:dataType "string" ;
            ada:fieldScope "method" ;
            ada:tier "R" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "Si analyzed by EPMA or EDS" ;
            schema1:description "Internal standard element and how its concentration is derived for each unknown." ;
            schema1:name "Internal Standard" ;
            schema1:readonlyValue true ;
            schema1:valueName "internalStandard" ;
            schema1:valueRequired true ;
            ada:category "Calibration" ;
            ada:dataType "string" ;
            ada:fieldScope "method" ;
            ada:tier "M" ] ;
    bios:computationalTool [ a schema1:SoftwareApplication ;
            schema1:name "Iolite" ;
            schema1:url "https://iolite-software.com/" ;
            schema1:version "4" ;
            ada:toolRole "reduction" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Analytical Method Definition v3
description: A registered analytical method definition modeled as a cdi:Activity and
  schema:Action. The method identity (name, technique, instrument, laboratory) lives
  at the top level. The standard workflow is encoded in schema:actionProcess as a
  schema:HowTo containing an ordered sequence of cdi:Activity + schema:Action steps
  (sample preparation, calibration, acquisition, data processing, quality control).
  Each workflow step carries its own parameters, reagents, and instruments. Method-level
  parameters that apply across all steps remain at the top level in ada:methodParameters.
  Integrates Bioschemas vocabulary for computational tools and reagents, DDI-CDI for
  activity sequence, and dqv:hasQualityMeasurement for quality metrics.
type: object
properties:
  '@context':
    type: object
    description: JSON-LD context declaring the namespace prefixes used in a method
      definition. Required for the document to be a valid JSON-LD instance. Bound
      prefixes must include schema (always), cdi (DDI-CDI), and ada (ADA vocabulary).
      Additional prefixes (bios, dqv, prov, skos) are recommended when those vocabularies
      are used in the body of the definition.
    properties:
      schema:
        const: http://schema.org/
      ada:
        const: https://ada.astromat.org/metadata/
      cdi:
        const: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
      bios:
        const: https://bioschemas.org/
      dqv:
        const: http://www.w3.org/ns/dqv#
      prov:
        const: http://www.w3.org/ns/prov#
      skos:
        const: http://www.w3.org/2004/02/skos/core#
    required:
    - schema
    - ada
    - cdi
  '@id':
    type: string
    description: Persistent URI for this method definition in the registry.
  '@type':
    type: array
    items:
      type: string
    minItems: 4
    allOf:
    - contains:
        const: cdi:Activity
    - contains:
        const: schema:Action
    - contains:
        const: ada:MethodDefinition
    - contains:
        const: bios:LabProtocol
    description: Must include cdi:Activity, schema:Action, ada:MethodDefinition, and
      bios:LabProtocol.
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
    description: ISO 8601 date when this method configuration was first used.
  schema:dateModified:
    type: string
    description: ISO 8601 date of last update to this definition.
  schema:additionalType:
    description: Further classification of the activity type (e.g. schema:CreateAction
      for a production method).
    type: array
    items:
      type: string
  schema:measurementTechnique:
    description: The analytical technique this method implements. Must be a DefinedTerm
      from a controlled vocabulary of techniques.
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
  schema:object:
    description: Target material(s) this method is designed to analyse (e.g. silicate
      glass, olivine, spinel). Modeled as DefinedTerm(s) or free text.
    type: array
    items:
      anyOf:
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
      - type: string
  schema:instrument:
    description: Primary instrument specification for this method. Use schema:hasPart
      for instrument sub-components (spectrometers, detectors).
    $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/instrument/schema.yaml
  bios:computationalTool:
    description: Software tools used for data acquisition, reduction, and processing.
      Each tool carries name, version, and optional URL.
    type: array
    items:
      $ref: '#/$defs/ComputationalTool'
  bios:reagent:
    description: Reference materials, calibration standards, and chemical reagents
      used across this method. Reagents specific to a single workflow step should
      be placed on that step instead.
    type: array
    items:
      $ref: '#/$defs/Reagent'
  ada:laboratory:
    description: Laboratory where this method was developed. Optional; omit for methods
      that are instrument-generic.
    $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/laboratory/schema.yaml
  schema:agent:
    description: Person or organisation who defined or is responsible for this method.
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/person/schema.yaml
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/organization/schema.yaml
    - type: object
      properties:
        '@id':
          type: string
  schema:actionProcess:
    description: The standard workflow for this method, expressed as a schema:HowTo
      containing an ordered sequence of workflow steps. Each step is a cdi:Activity
      + schema:Action describing a distinct phase (sample preparation, calibration,
      acquisition, data processing, quality control). Steps carry their own parameters,
      reagents, instruments, and sub-steps.
    $ref: '#/$defs/WorkflowHowTo'
  ada:methodParameters:
    type: array
    description: Method-level parameters that apply across all workflow steps (e.g.
      method-scoped constants like matrix correction model). Step-specific parameters
      should be placed on the appropriate workflow step instead.
    items:
      $ref: '#/$defs/MethodParameter'
  ada:analyteTemplate:
    description: Template for per-analyte (element-specific) parameters. Defines the
      columns that appear in the element table, each with scope, datatype, and constraints.
      Analyte rows become schema:variableMeasured entries in metadata records. Typically
      associated with the acquisition workflow step.
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
  dqv:hasQualityMeasurement:
    description: Quality measurements that characterize the method's expected performance
      (e.g. analytical precision, accuracy, counting statistics error). Uses the CDIF
      qualityMeasure building block.
    type: array
    items:
      $ref: '#/$defs/QualityMeasure'
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
- '@context'
- '@type'
- schema:name
- schema:measurementTechnique
$defs:
  WorkflowHowTo:
    type: object
    description: The method's standard workflow expressed as a schema:HowTo. Contains
      an ordered array of workflow steps in schema:step, where each step is a cdi:Activity
      + schema:Action.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: schema:HowTo
        minItems: 1
      '@id':
        type: string
      schema:name:
        type: string
        description: Name of the workflow (e.g. "EPMA WDS analytical workflow").
      schema:description:
        type: string
        description: Overview of the workflow.
      schema:url:
        type: string
        format: uri
        description: URL to a published protocol document.
      schema:step:
        type: array
        description: Ordered sequence of workflow steps. Each step is a cdi:Activity
          + schema:Action describing a distinct phase of the analytical procedure.
        items:
          $ref: '#/$defs/WorkflowStep'
    required:
    - '@type'
    - schema:step
  WorkflowStep:
    type: object
    description: A single step in the analytical workflow, modeled as a cdi:Activity
      + schema:Action. Each step describes a distinct phase such as sample preparation,
      instrument calibration, data acquisition, data processing, or quality control.
      Steps carry their own parameters, instruments, reagents, and may contain sub-steps
      via schema:actionProcess.
    properties:
      '@type':
        type: array
        items:
          type: string
        minItems: 2
        allOf:
        - contains:
            const: cdi:Activity
        - contains:
            const: schema:Action
      '@id':
        type: string
      schema:name:
        type: string
        description: Name of this workflow step (e.g. "Sample preparation").
      schema:description:
        type: string
        description: Detailed description of what this step involves.
      schema:position:
        type: integer
        description: Ordinal position in the workflow sequence (1-based).
      schema:additionalType:
        description: Further classification of this step (e.g. bios:LabProcess for
          wet-lab steps, schema:CreateAction for production steps).
        type: array
        items:
          type: string
      schema:instrument:
        description: Instrument or equipment used in this step.
        anyOf:
        - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/instrument/schema.yaml
        - type: object
          properties:
            '@id':
              type: string
          required:
          - '@id'
      bios:computationalTool:
        description: Software tools used in this step.
        type: array
        items:
          $ref: '#/$defs/ComputationalTool'
      bios:reagent:
        description: Reference materials, standards, or reagents used in this step.
        type: array
        items:
          $ref: '#/$defs/Reagent'
      prov:used:
        description: Input entities consumed or referenced by this step (e.g. prepared
          sample from a prior step).
        type: array
        items:
          anyOf:
          - type: string
          - type: object
            properties:
              '@id':
                type: string
      schema:result:
        description: Output entity produced by this step (can be referenced as input
          by a subsequent step).
        anyOf:
        - type: string
        - type: object
          properties:
            '@id':
              type: string
      schema:object:
        description: Reference to a prior step whose result is the input for this
          step (action chaining).
        anyOf:
        - type: string
        - type: object
          properties:
            '@id':
              type: string
      schema:additionalProperty:
        description: Step-specific parameters (e.g. beam conditions for the acquisition
          step, matrix correction settings for the data processing step).
        type: array
        items:
          $ref: '#/$defs/StepParameter'
      ada:methodParameters:
        description: Step-specific method parameters with scope and tier metadata.
          These are parameters that belong to this particular workflow phase.
        type: array
        items:
          $ref: '#/$defs/MethodParameter'
      schema:actionProcess:
        description: Sub-workflow for this step, expressed as a nested schema:HowTo
          with its own ordered steps. Use for steps that have a multi-phase internal
          procedure (e.g. sample preparation with mount, grind, polish, coat).
        $ref: '#/$defs/WorkflowHowTo'
      dqv:hasQualityMeasurement:
        description: Quality measurements specific to this workflow step.
        type: array
        items:
          $ref: '#/$defs/QualityMeasure'
    required:
    - '@type'
    - schema:name
    - schema:position
  MethodParameter:
    type: object
    description: 'A parameter specification for the method, typed as schema:PropertyValueSpecification.
      Uses schema.org properties for value constraints (defaultValue, minValue, maxValue,
      readonlyValue, valueRequired) and ada: extensions for analytical method semantics
      (fieldScope, category, tier). Link to a controlled vocabulary via schema:inDefinedTermSet.'
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: schema:PropertyValueSpecification
        minItems: 1
      schema:name:
        type: string
        description: Human-readable display label (e.g. "Accelerating Voltage").
      schema:valueName:
        type: string
        description: Machine-readable parameter name for serialization (e.g. "acceleratingVoltage").
      schema:description:
        type: string
        description: Guidance text shown to the user in the form.
      schema:propertyID:
        description: URI identifying this parameter type in a formal vocabulary. Links
          to a skos:Concept or similar term definition.
        anyOf:
        - type: string
          format: uri
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
      schema:inDefinedTermSet:
        description: SKOS ConceptScheme providing the controlled vocabulary for allowed
          values of this parameter. When present, form renders a dropdown/select populated
          from the vocabulary. Can be an object reference (@id URI), a labeled link
          (LinkRole with name and URL), or a plain URI string.
        anyOf:
        - type: string
          format: uri
        - type: object
          description: Object reference to a vocabulary defined elsewhere.
          properties:
            '@id':
              type: string
              format: uri
          required:
          - '@id'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.yaml
      schema:defaultValue:
        description: The default value for this parameter. For constant parameters
          (readonlyValue=true), this is the fixed value. For editable parameters,
          this is the pre-filled default.
        anyOf:
        - type: string
        - type: number
        - type: boolean
      schema:readonlyValue:
        type: boolean
        description: true = constant, fixed for every session (read-only in form).
          false = editable (default or optional depending on valueRequired).
      schema:valueRequired:
        type: boolean
        description: 'true = must be provided (mandatory). false = optional. Combined
          with readonlyValue: readonly+required = constant mandatory; !readonly+required
          = editable mandatory; !readonly+!required = optional.'
      schema:minValue:
        type: number
        description: Minimum allowed numeric value. Defines the lower bound of a valid
          range at the method level; specific values within this range may be set
          per element in the analyteTemplate.
      schema:maxValue:
        type: number
        description: Maximum allowed numeric value. Upper bound of valid range.
      schema:stepValue:
        type: number
        description: Granularity expected of the value (e.g. 0.1 for nA).
      schema:valuePattern:
        type: string
        description: Regex pattern for validating string values.
      schema:multipleValues:
        type: boolean
        description: Whether multiple values are allowed (default false).
      ada:fieldScope:
        type: string
        enum:
        - method
        - session
        - element
        description: Whether this parameter is fixed at the method level, varies per
          analytical session, or is element-specific.
      ada:category:
        description: Grouping label for form layout (e.g. "Beam Conditions", "Data
          Processing", "Quality Control"). String for simple cases; DefinedTerm to
          link to a controlled vocabulary of parameter categories.
        anyOf:
        - type: string
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
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
      ada:enumeration:
        type: array
        items:
          anyOf:
          - type: string
          - type: number
        description: Inline list of allowed values. Fallback when no SKOS vocabulary
          exists yet. If inDefinedTermSet is also present, this list is ignored in
          favour of the vocabulary.
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
        description: The CDIF building block property path this parameter maps to.
          Used for JSON-LD serialisation.
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
    - ada:fieldScope
    - ada:dataType
  StepParameter:
    type: object
    description: "A schema:PropertyValue carrying a parameter setting for a workflow
      step. Simpler than MethodParameter \u2014 just name, value, and optional unit."
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: schema:PropertyValue
        minItems: 1
      schema:name:
        type: string
      schema:value:
        anyOf:
        - type: string
        - type: number
        - type: boolean
      schema:unitText:
        type: string
    required:
    - '@type'
    - schema:name
  AnalyteColumn:
    type: object
    description: Definition of one column in the per-analyte parameter table, typed
      as schema:PropertyValueSpecification. Each column defines what values are expected
      per element/oxide row. Analyte rows become schema:variableMeasured entries;
      columns become schema:additionalProperty within each.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: schema:PropertyValueSpecification
        minItems: 1
      schema:name:
        type: string
        description: Human-readable column label (e.g. "Diffracting Crystal").
      schema:valueName:
        type: string
        description: Machine-readable column identifier (e.g. "diffractingCrystal").
      schema:description:
        type: string
        description: Guidance text for this column.
      schema:propertyID:
        description: URI identifying this column's parameter type in a formal vocabulary.
        anyOf:
        - type: string
          format: uri
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
      schema:inDefinedTermSet:
        description: SKOS ConceptScheme providing the controlled vocabulary for allowed
          values in this column.
        anyOf:
        - type: string
          format: uri
        - type: object
          description: Object reference to a vocabulary defined elsewhere.
          properties:
            '@id':
              type: string
              format: uri
          required:
          - '@id'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.yaml
      schema:defaultValue:
        description: Default value for this column (pre-filled per row).
        anyOf:
        - type: string
        - type: number
        - type: boolean
      schema:readonlyValue:
        type: boolean
        description: true = constant across all analytes (read-only column).
      schema:valueRequired:
        type: boolean
        description: true = must be provided for every analyte row.
      schema:minValue:
        type: number
      schema:maxValue:
        type: number
      schema:valuePattern:
        type: string
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
        description: Inline allowed values list (fallback when no SKOS vocabulary
          exists).
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
        description: How this column maps into the variableMeasured JSON-LD structure.
    required:
    - schema:name
    - ada:dataType
  ComputationalTool:
    type: object
    description: Software application used for data acquisition, reduction, or processing.
      Follows Bioschemas ComputationalTool pattern.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: schema:SoftwareApplication
      '@id':
        type: string
      schema:name:
        type: string
        description: Name of the software (e.g. "Probe for EPMA").
      schema:version:
        type: string
        description: Software version string (e.g. "12.9.5").
      schema:description:
        type: string
        description: Role or purpose of this tool in the method.
      schema:url:
        type: string
        format: uri
        description: URL to the software product or documentation.
      ada:toolRole:
        type: string
        enum:
        - acquisition
        - reduction
        - processing
        - visualization
        description: Role this software plays in the analytical workflow.
    required:
    - schema:name
  Reagent:
    type: object
    description: A reference material, calibration standard, or chemical reagent.
      Follows Bioschemas reagent pattern with extensions for geochemistry reference
      materials.
    properties:
      '@type':
        type: array
        items:
          type: string
        minItems: 1
      '@id':
        type: string
        description: Persistent identifier (e.g. IGSN, GeoReM URL).
      schema:name:
        type: string
        description: Name of the material (e.g. "San Carlos olivine").
      schema:description:
        type: string
      schema:identifier:
        description: Formal identifier (IGSN, catalog number, GeoReM ID).
        anyOf:
        - type: string
        - type: object
          properties:
            '@type':
              type: array
              items:
                type: string
              minItems: 1
            schema:propertyID:
              type: string
            schema:value:
              type: string
      ada:reagentRole:
        type: string
        enum:
        - primaryStandard
        - secondaryStandard
        - interferenceStandard
        - blankMaterial
        - coatingMaterial
        - reagent
        description: Role of this material in the method.
      schema:citation:
        description: Publication reference for the standard's accepted values.
        anyOf:
        - type: string
        - type: object
          properties:
            '@type':
              type: array
              items:
                type: string
            schema:name:
              type: string
            schema:url:
              type: string
              format: uri
    required:
    - schema:name
  QualityMeasure:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/qualityProperties/qualityMeasure/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  prov: http://www.w3.org/ns/prov#
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  bios: https://bioschemas.org/
  dqv: http://www.w3.org/ns/dqv#
  skos: http://www.w3.org/2004/02/skos/core#

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
    "bios": "https://bioschemas.org/",
    "dqv": "http://www.w3.org/ns/dqv#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
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
* [Bioschemas LabProtocol Profile](https://bioschemas.org/profiles/LabProtocol)
* [DDI-CDI 1.0 Process Model](https://ddialliance.org/Specification/DDI-CDI/1.0/)
* [W3C Data Quality Vocabulary (DQV)](https://www.w3.org/TR/vocab-dqv/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/methodDefinition`

