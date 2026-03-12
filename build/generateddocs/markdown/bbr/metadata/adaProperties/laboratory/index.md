
# Analysis Laboratory Type (Schema)

`ada.bbr.metadata.adaProperties.laboratory` *v0.1*

Laboratory/facility definition combining NXsource and schema:Place. Defines properties: @type, schema:identifier, schema:name, schema:alternateName.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Analysis Laboratory Type

Defines the laboratory or facility where analysis was performed. Combines NeXus NXsource typing with schema:Place for location semantics. Supports URI-based identifiers for facility lookup.

## Examples

### Laboratory Type Example
A laboratory facility described as a NeXus NXsource with schema:Place typing.
#### json
```json
{
  "@type": ["schema:Place", "nxs:BaseClass/NXsource"],
  "schema:name": "Lunar and Planetary Laboratory Electron Microprobe Facility",
  "schema:alternateName": "LPL EMPA Lab",
  "schema:identifier": "https://ror.org/03m2x1q45"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "nxs": "http://purl.org/nexusformat/definitions/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/laboratory/context.jsonld"
  ],
  "@type": [
    "schema:Place",
    "nxs:BaseClass/NXsource"
  ],
  "schema:name": "Lunar and Planetary Laboratory Electron Microprobe Facility",
  "schema:alternateName": "LPL EMPA Lab",
  "schema:identifier": "https://ror.org/03m2x1q45"
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] a <http://purl.org/nexusformat/definitions/BaseClass/NXsource>,
        schema1:Place ;
    schema1:alternateName "LPL EMPA Lab" ;
    schema1:identifier "https://ror.org/03m2x1q45" ;
    schema1:name "Lunar and Planetary Laboratory Electron Microprobe Facility" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Analysis Laboratory Type
description: Laboratory or facility definition combining NeXus NXsource with schema:Place.
  Used to identify the location where analysis was performed.
type: object
properties:
  '@type':
    const:
    - schema:Place
    - nxs:BaseClass/NXsource
  schema:identifier:
    type: string
    format: uri
  schema:name:
    type: string
  schema:alternateName:
    type: string
x-jsonld-prefixes:
  schema: http://schema.org/
  nxs: http://purl.org/nexusformat/definitions/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/laboratory/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/laboratory/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/adaProperties/laboratory/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/adaProperties/laboratory`

