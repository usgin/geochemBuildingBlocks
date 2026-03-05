
# Analysis Instrument Type (Schema)

`ada.bbr.metadata.adaProperties.instrument` *v0.1*

Analytical instrument definition combining NXinstrument and prov:Entity. Defines properties: @type, schema:additionalType, schema:name, schema:description, schema:identifier.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Analysis Instrument Type

Defines analytical instruments used in analysis events. Combines the NeXus NXinstrument base class with PROV-O Entity typing. Supports GCMD instrument identifiers via `schema:additionalType`.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Analysis Instrument Type
description: Analytical instrument definition combining NeXus NXinstrument base class
  with PROV-O Entity. Used to describe instruments involved in analysis events.
type: object
properties:
  '@type':
    const:
    - schema:Thing
    - prov:Entity
    - nxs:BaseClass/NXinstrument
  schema:additionalType:
    description: Identifier for an instrument or component in the analytical instrumentation,
      e.g. GCMD instrument identifier.
    type: array
    items:
      type: string
  schema:name:
    type: string
  schema:description:
    type: string
  schema:identifier:
    type: string
x-jsonld-prefixes:
  schema: http://schema.org/
  prov: http://www.w3.org/ns/prov#
  nxs: http://purl.org/nexusformat/definitions/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/instrument/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/instrument/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/instrument/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/adaProperties/instrument`

