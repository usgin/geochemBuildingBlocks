
# Document Type (Schema)

`ada.bbr.metadata.geochemProperties.document` *v0.1*

Supplemental documents for calibration, methods, and analysis info. Defines properties: @type, componentType, schema:version, schema:isBasedOn. Uses building blocks: detailARGT (geochemProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Document Type

Describes supplemental documents in ADA metadata including calibration files, method descriptions, log files, processing descriptions, and other supplemental information. Typed as `ada:document` and `schema:DigitalDocument`.

## Examples

### Document Type Example
A calibration document associated with an analytical session.
#### json
```json
{
  "@type": ["ada:document", "schema:DigitalDocument"],
  "ada:componentType": {
    "@type": "ada:calibrationFile"
  },
  "schema:version": "1.0",
  "schema:isBasedOn": "calibration_original_20230415.pdf"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/document/context.jsonld"
  ],
  "@type": [
    "ada:document",
    "schema:DigitalDocument"
  ],
  "ada:componentType": {
    "@type": "ada:calibrationFile"
  },
  "schema:version": "1.0",
  "schema:isBasedOn": "calibration_original_20230415.pdf"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .

[] a schema1:DigitalDocument,
        ada:document ;
    schema1:isBasedOn "calibration_original_20230415.pdf" ;
    schema1:version "1.0" ;
    ada:componentType [ a ada:calibrationFile ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Document Type
description: Text or PDF/A documents providing supplemental information, typically
  related to calibration, instrument metadata details, analysis methods, or data representation.
  Typed as ada:document and schema:DigitalDocument.
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    minItems: 2
    allOf:
    - contains:
        const: ada:document
    - contains:
        const: schema:DigitalDocument
  ada:componentType:
    description: One of the supplemental document types if applicable
    anyOf:
    - type: object
      properties:
        '@type':
          enum:
          - ada:calibrationFile
          - ada:contextVideo
          - ada:instrumentMetadata
          - ada:logFile
          - ada:methodDescription
          - ada:peaks
          - ada:plot
          - ada:processingMethod
          - ada:QRISCalibrationFile
          - ada:report
          - ada:samplePreparation
          - ada:shapefile
          - ada:worldFile
    - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailARGT/schema.yaml
  schema:version:
    type: string
  schema:isBasedOn:
    description: same as ada/samis '_originalName'
    type: string
required:
- '@type'
- ada:componentType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/document/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/document/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/document/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/document`

