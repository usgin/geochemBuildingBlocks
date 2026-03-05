
# Collection Type (Schema)

`ada.bbr.metadata.adaProperties.collection` *v0.1*

Set of related files with identical information models or composite datasets. Defines properties: @type, componentType, memberTypes, nFiles, filelist. Uses building blocks: stringArray (adaProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Collection Type

Describes a collection of related files in ADA metadata. Can represent a set of files with identical information models and serialization (a collection), or a heterogeneous set of files constituting a composite dataset. Typed as `ada:collection` and `schema:Collection`.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Collection Type
description: A collection can be a set of files with identical information model and
  serialization/formatting, or a heterogeneous set of files that together constitute
  a dataset (a composite dataset).
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    minItems: 2
    allOf:
    - contains:
        const: ada:collection
    - contains:
        const: https://schema.org/Collection
    description: GeneralType for collections
  componentType:
    type: object
    properties:
      '@type':
        type: string
        enum:
        - ada:AIVAImageCollection
        - ada:ARGTCollection
        - ada:EAIRMSCollection
        - ada:EMPAImageCollection
        - ada:GCMSCollection
        - ada:GCGCMSCollection
        - ada:LCMSCollection
        - ada:LCMSMSCollection
        - ada:LIT2DDataCollection
        - ada:LITPolarDataCollection
        - ada:MCICPMSCollection
        - ada:NanoIRMapCollection
        - ada:NanoIRPointCollection
        - ada:NanoSIMSCollection
        - ada:NanoSIMSImageCollection
        - ada:QRISCalibratedCollection
        - ada:QRISRawCollection
        - ada:RITOFNGMSCollection
        - ada:SEMEDSElementalMaps
        - ada:SEMEDSPointDataCollection
        - ada:SEMImageCollection
        - ada:SIMSCollection
        - ada:TEMEDSImageCollection
        - ada:TOFSIMSCollection
        - ada:UVFMImageCollection
        - ada:VLMImageCollection
        - ada:XANESCollection
        - ada:XCTImageCollection
  memberTypes:
    description: List of the component types in the collection
    $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/stringArray/schema.yaml
  nFiles:
    type: integer
    description: Number of files in the collection, including metadata files
  filelist:
    type: array
    items:
      type: object
      properties:
        fileName:
          type: string
          description: Full path to file in container object
        fileNamePattern:
          type: string
          description: Pattern for collection members with differentiating suffix
            at '*'
        componentType:
          description: The component type for the file(s)
          type: string
        schema:encodingFormat:
          type: string
          description: MIME type with extension
      oneOf:
      - required:
        - fileName
      - required:
        - fileNamePattern
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/collection/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/collection/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/collection/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/adaProperties/collection`

