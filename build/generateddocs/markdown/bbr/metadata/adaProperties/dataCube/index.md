
# Data Cube Type (Schema)

`ada.bbr.metadata.adaProperties.dataCube` *v0.1*

CDI DimensionalDataStructure for multidimensional data. Defines properties: @type, componentType, dataComponentResource. Uses building blocks: detailL2MS (adaProperties), cdifDataCube (cdifProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Data Cube Type

Describes multidimensional data structures in ADA metadata. Typed as `ada:dataCube` and `cdi:DimensionalDataStructure`. Supports DimensionComponent, MeasureComponent, and AttributeComponent with value domain specifications and value mappings.

## Examples

### Data Cube Type Example
A multi-dimensional data cube for SEM-EDS elemental map cube data.
#### json
```json
{
  "@type": ["ada:dataCube", "cdi:StructuredDataSet"],
  "componentType": {
    "@type": "ada:SEMEDSElementalMapsCube"
  },
  "dataComponentResource": "cube_SEMEDS_001.hdf5"
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
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/dataCube/context.jsonld"
  ],
  "@type": [
    "ada:dataCube",
    "cdi:StructuredDataSet"
  ],
  "componentType": {
    "@type": "ada:SEMEDSElementalMapsCube"
  },
  "dataComponentResource": "cube_SEMEDS_001.hdf5"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .

[] a cdi:StructuredDataSet,
        ada:dataCube .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Data Cube Type
description: Multi-dimensional data cube structure using DDI-CDI. Typed as ada:dataCube
  and cdi:StructuredDataSet per CDIF 2026 alignment.
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
          const: ada:dataCube
      - contains:
          const: cdi:StructuredDataSet
    componentType:
      anyOf:
      - type: object
        properties:
          '@type':
            enum:
            - ada:GCMSCollection
            - ada:GCMSCube
            - ada:FTICRMSCube
            - ada:LCMSCollection
            - ada:SEMEBSDGrainImageMapCube
            - ada:SEMEDSElementalMapsCube
            - ada:SEMEDSPointDataCube
            - ada:SEMHRCLCube
            - ada:STEMEDSCube
            - ada:STEMEDSTomo
            - ada:STEMEELSCube
            - ada:VNMIRSpectralMap
        required:
        - '@type'
      - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailL2MS/schema.yaml
    dataComponentResource:
      type: string
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataCube/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/dataCube/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/dataCube/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/dataCube/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/adaProperties/dataCube`

