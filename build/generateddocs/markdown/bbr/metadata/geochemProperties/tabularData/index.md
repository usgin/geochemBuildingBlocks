
# Tabular Data Type (Schema)

`ada.bbr.metadata.geochemProperties.tabularData` *v0.1*

CDI PhysicalDataSet for tabular/structured data files. Defines properties: @type, componentType, xCoordCol, yCoordCol, zCoordCol, coordUnits, spatialRegistration. Uses building blocks: detailDSC (geochemProperties), detailEAIRMS (geochemProperties), detailEMPA (geochemProperties), detailLAF (geochemProperties), detailNanoSIMS (geochemProperties), detailNanoIR (geochemProperties), detailPSFD (geochemProperties), detailVNMIR (geochemProperties), detailXRD (geochemProperties), spatialRegistration (geochemProperties), cdifTabularData (cdifProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Tabular Data Type

Describes tabular/structured data files in ADA metadata. Typed as `cdi:PhysicalDataSet` and `ada:tabularData`. Supports DDI-CDI WideDataStructure for column layout description, spatial registration, and various analytical technique-specific component types.

## Examples

### Tabular Data Type Example
A tabular data file containing MC-ICP-MS isotope ratio results.
#### json
```json
{
  "@type": ["cdi:TabularTextDataSet", "ada:tabularData"],
  "ada:componentType": {
    "@type": "ada:MCICPMSTabular"
  },
  "cdi:isDelimited": true,
  "ada:xCoordCol": "X_um",
  "ada:yCoordCol": "Y_um",
  "ada:coordUnits": "micrometer"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/tabularData/context.jsonld"
  ],
  "@type": [
    "cdi:TabularTextDataSet",
    "ada:tabularData"
  ],
  "ada:componentType": {
    "@type": "ada:MCICPMSTabular"
  },
  "cdi:isDelimited": true,
  "ada:xCoordCol": "X_um",
  "ada:yCoordCol": "Y_um",
  "ada:coordUnits": "micrometer"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a cdi:TabularTextDataSet,
        ada:tabularData ;
    cdi:isDelimited true ;
    ada:componentType [ a ada:MCICPMSTabular ] ;
    ada:coordUnits "micrometer" ;
    ada:xCoordCol "X_um" ;
    ada:yCoordCol "Y_um" .


```

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
    ada:componentType:
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
      - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailDSC/schema.yaml
      - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailEAIRMS/schema.yaml
      - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailEMPA/schema.yaml
      - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailLAF/schema.yaml
      - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailNanoSIMS/schema.yaml
      - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailNanoIR/schema.yaml
      - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailPSFD/schema.yaml
      - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailVNMIR/schema.yaml
      - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailXRD/schema.yaml
    ada:xCoordCol:
      description: The column names are redundant, they are lists in the hasPhysicalMapping
        array. Include here for convenience.
      type: string
    ada:yCoordCol:
      type: string
    ada:zCoordCol:
      type: string
    ada:coordUnits:
      type: string
    ada:spatialRegistration:
      $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/spatialRegistration/schema.yaml
  required:
  - '@type'
  - ada:componentType
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/cdifProperties/cdifTabularData/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/tabularData/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/tabularData/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/tabularData/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/tabularData`

