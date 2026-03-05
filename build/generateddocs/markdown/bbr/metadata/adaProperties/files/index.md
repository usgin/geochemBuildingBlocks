
# Files Type (Schema)

`ada.bbr.metadata.adaProperties.files` *v0.1*

DataDownload with checksum, size, encoding format, and file detail. Defines properties: schema:additionalType, schema:description, schema:size, resultTarget, schema:relatedLink. Uses building blocks: dataDownload (schemaorgProperties), stringArray (adaProperties), image (adaProperties), imageMap (adaProperties), tabularData (adaProperties), collection (adaProperties), dataCube (adaProperties), document (adaProperties), supDocImage (adaProperties), otherFile (adaProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Files Type

Describes properties for any file in an ADA product. Includes file metadata (name, description, checksum, size, encoding format), file detail classification (image, imageMap, tabularData, collection, dataCube, document, supDocImage, otherFile, or Metadata), and inter-file relationships via `schema:relatedLink`.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Files Type
description: Properties for any file in an ADA product distribution. GeneralType provides
  info based on broad categories of file format (tabular, image, dataCube, document).
  Type constraints (e.g. DataDownload) are applied at the composition level in profiles.
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/dataDownload/schema.yaml
- type: object
  description: properties added for geochemical datasets
  properties:
    schema:additionalType:
      type: array
      description: other classifier for the file. ada componentTypes are specified
        in the specific file type schema attached by $refs
      items:
        type: string
    schema:description:
      type: string
    schema:size:
      type: object
      properties:
        '@type':
          const: schema:QuantitativeValue
        schema:value:
          type: integer
        schema:unitText:
          type: string
          default: byte
    resultTarget:
      $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/stringArray/schema.yaml
    schema:relatedLink:
      type: array
      description: 'Links between files in the product. Use schema:name for path to
        target in product, or use #id JSON-LD links. Used to link metadata files in
        bundle to the data or supplementary files they document.'
      items:
        type: object
        properties:
          '@type':
            type: string
            const: schema:LinkRole
          schema:linkRelationship:
            type: string
          schema:target:
            type: object
            properties:
              '@type':
                type: string
                const: schema:EntryPoint
              schema:encodingFormat:
                type: string
              schema:name:
                type: string
              schema:url:
                type: string
- anyOf:
  - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/image/schema.yaml
  - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/imageMap/schema.yaml
  - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/tabularData/schema.yaml
  - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/collection/schema.yaml
  - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/dataCube/schema.yaml
  - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/document/schema.yaml
  - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/supDocImage/schema.yaml
  - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/otherFile/schema.yaml
  - type: object
    properties:
      '@type':
        const:
        - Metadata
    required:
    - '@type'
  - type: object
    description: DataDownload distribution (archive or direct download without specific
      file type)
    properties:
      '@type':
        type: array
        contains:
          const: schema:DataDownload
    required:
    - '@type'
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  spdx: http://spdx.org/rdf/terms#

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/files/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/files/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "spdx": "http://spdx.org/rdf/terms#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/files/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/adaProperties/files`

