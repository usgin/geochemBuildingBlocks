
# Tabular Data Type (Schema)

`ada.bbr.metadata.adaProperties.tabularData` *v0.1*

CDI PhysicalDataSet for tabular/structured data files. Defines properties: @type, componentType, xCoordCol, yCoordCol, zCoordCol, coordUnits, spatialRegistration. Uses building blocks: detailDSC (adaProperties), detailEAIRMS (adaProperties), detailEMPA (adaProperties), detailLAF (adaProperties), detailNanoSIMS (adaProperties), detailNanoIR (adaProperties), detailPSFD (adaProperties), detailVNMIR (adaProperties), detailXRD (adaProperties), spatialRegistration (adaProperties), cdifTabularData (cdifProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Tabular Data Type

Describes tabular/structured data files in ADA metadata. Typed as `cdi:PhysicalDataSet` and `ada:tabularData`. Supports DDI-CDI WideDataStructure for column layout description, spatial registration, and various analytical technique-specific component types.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Tabular Data Type
description: Tabular data type aligned with CDIF 2026 schema using DDI-CDI and CSVW
  properties. Typed as cdi:TabularTextDataSet and ada:tabularData.
allOf:
- type: object
  properties:
    '@type':
      type: array
      items:
        type: string
      minItems: 2
      allOf:
      - contains:
          const: cdi:TabularTextDataSet
      - contains:
          const: ada:tabularData
    componentType:
      anyOf:
      - type: object
        properties:
          '@type':
            type: string
            enum:
            - ada:AMSRawData
            - ada:AMSProcessedData
            - ada:DSCResultsTabular
            - ada:FTICRMSTabular
            - ada:GPYCProcessedTabular
            - ada:GPYCRawTabular
            - ada:HRICPMSProcessed
            - ada:HRICPMSRaw
            - ada:ICPOESIntermediateTabular
            - ada:ICPOESProcessedTabular
            - ada:ICPOESRawTabular
            - ada:ICTabular
            - ada:MCICPMSTabular
            - ada:NGNSMSRaw
            - ada:NGNSMSProcessed
            - ada:QICPMSProcessedTabular
            - ada:QICPMSRawTabular
            - ada:RAMANRawTabular
            - ada:RITOFNGMSTabular
            - ada:RITOFNGMSCollection
            - ada:SEMEDSPointData
            - ada:SIMSTabular
            - ada:STEMEDSTabular
            - ada:STEMEELSTabular
            - ada:SVRUECTabular
            - ada:XANESRawTabular
            - ada:XANESProcessedTabular
        required:
        - '@type'
      - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailDSC/schema.yaml
      - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailEAIRMS/schema.yaml
      - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailEMPA/schema.yaml
      - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailLAF/schema.yaml
      - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailNanoSIMS/schema.yaml
      - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailNanoIR/schema.yaml
      - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailPSFD/schema.yaml
      - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailVNMIR/schema.yaml
      - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailXRD/schema.yaml
    xCoordCol:
      description: The column names are redundant, they are lists in the hasPhysicalMapping
        array. Include here for convenience.
      type: string
    yCoordCol:
      type: string
    zCoordCol:
      type: string
    coordUnits:
      type: string
    spatialRegistration:
      $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/spatialRegistration/schema.yaml
  required:
  - '@type'
  - componentType
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifTabularData/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/tabularData/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/tabularData/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/tabularData/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/adaProperties/tabularData`

