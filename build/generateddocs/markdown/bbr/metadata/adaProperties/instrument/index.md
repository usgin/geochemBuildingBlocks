
# Analysis Instrument Type (Schema)

`ada.bbr.metadata.adaProperties.instrument` *v0.1*

Analytical instrument definition combining NXinstrument and prov:Entity. Defines properties: @type, schema:additionalType, schema:name, schema:description, schema:identifier.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Analysis Instrument Type

Defines analytical instruments used in analysis events. Combines the NeXus NXinstrument base class with PROV-O Entity typing. Supports GCMD instrument identifiers via `schema:additionalType`.

## Examples

### Instrument Type Example
An analytical instrument described as a NeXus NXinstrument with PROV-O Entity typing.
#### json
```json
{
  "@type": ["schema:Thing", "prov:Entity", "nxs:BaseClass/NXinstrument"],
  "schema:name": "JEOL JXA-8530F Electron Microprobe",
  "schema:description": "Field-emission electron probe microanalyzer with 5 wavelength-dispersive spectrometers",
  "schema:identifier": "https://www.wikidata.org/wiki/Q116917974",
  "schema:additionalType": ["https://gcmd.earthdata.nasa.gov/kms/concept/76a947a3-4529-4fb7-87a7-f4b3a0a0de48"]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "prov": "http://www.w3.org/ns/prov#",
      "nxs": "http://purl.org/nexusformat/definitions/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/instrument/context.jsonld"
  ],
  "@type": [
    "schema:Thing",
    "prov:Entity",
    "nxs:BaseClass/NXinstrument"
  ],
  "schema:name": "JEOL JXA-8530F Electron Microprobe",
  "schema:description": "Field-emission electron probe microanalyzer with 5 wavelength-dispersive spectrometers",
  "schema:identifier": "https://www.wikidata.org/wiki/Q116917974",
  "schema:additionalType": [
    "https://gcmd.earthdata.nasa.gov/kms/concept/76a947a3-4529-4fb7-87a7-f4b3a0a0de48"
  ]
}
```

#### ttl
```ttl
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .

[] a <http://purl.org/nexusformat/definitions/BaseClass/NXinstrument>,
        schema1:Thing,
        prov:Entity ;
    schema1:additionalType "https://gcmd.earthdata.nasa.gov/kms/concept/76a947a3-4529-4fb7-87a7-f4b3a0a0de48" ;
    schema1:description "Field-emission electron probe microanalyzer with 5 wavelength-dispersive spectrometers" ;
    schema1:identifier "https://www.wikidata.org/wiki/Q116917974" ;
    schema1:name "JEOL JXA-8530F Electron Microprobe" .


```

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

