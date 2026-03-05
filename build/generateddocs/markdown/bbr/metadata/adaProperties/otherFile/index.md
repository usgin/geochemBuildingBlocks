
# Other File Type (Schema)

`ada.bbr.metadata.adaProperties.otherFile` *v0.1*

Non-standard file formats approved for ADA submission. Defines properties: @type, componentType, schema:encodingFormat, formatDescription. Uses building blocks: detailSLS (adaProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Other File Type

Describes files in non-standard formats that have been approved for submission to the Astromat Archive. Supports EMSA spectral data, OBJ 3D models, STL files, XLSX workbooks, and Neptune Plus exports.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Other File Type
description: Files in other widely-used formats approved for submission to the Astromat
  Archive. Includes EMSA, OBJ, STL, XLSX, and Neptune Plus export formats.
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    minItems: 1
    contains:
      const: ada:otherFileType
  componentType:
    anyOf:
    - type: object
      properties:
        '@type':
          enum:
          - ada:other
      required:
      - '@type'
    - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailSLS/schema.yaml
  schema:encodingFormat:
    description: 'One of the approved non-standard file formats: ''Spectral Data Exchange
      File (.emsa)''-->text/plain; ''3D model file (.obj)''-->model/obj; ''Standard
      Triangle Language (.stl)''-->model/stl; ''Open XML workbook (.xlsx)''-->application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;
      ''Neptune Plus export (.exp)''-->application/octet-stream'
    enum:
    - text/plain
    - model/obj
    - model/stl
    - application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
    - application/octet-stream
  formatDescription:
    type: string
    description: Free text explanation of file format, or a link to a publicly accessible
      specification for the format.
required:
- '@type'
- componentType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/otherFile/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/otherFile/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/otherFile/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/adaProperties/otherFile`

