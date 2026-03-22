
# ADA Analysis Laboratory (Schema)

`ada.bbr.metadata.geochemProperties.laboratory` *v0.1*

ADA laboratory/facility building block extending core CDIF spatialExtent (schema:Place). Adds nxs:BaseClass/NXsource classification via additionalType. Inherits place name, identifier, alternateName, geo coordinates from core.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA Analysis Laboratory

Extends the core CDIF [spatialExtent](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/spatialExtent/) building block for ADA laboratory/facility descriptions. Adds `nxs:BaseClass/NXsource` classification via `schema:additionalType`. Inherits place name, identifier, alternateName, geo coordinates, and GeoSPARQL geometry from core spatialExtent.

## Examples

### ADA Analysis Laboratory Example
A laboratory facility extending core spatialExtent (schema:Place) with
NeXus NXsource classification in additionalType.
#### json
```json
{
  "@type": ["schema:Place"],
  "schema:additionalType": ["nxs:BaseClass/NXsource"],
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
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/laboratory/context.jsonld"
  ],
  "@type": [
    "schema:Place"
  ],
  "schema:additionalType": [
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

[] a schema1:Place ;
    schema1:additionalType "nxs:BaseClass/NXsource" ;
    schema1:alternateName "LPL EMPA Lab" ;
    schema1:identifier "https://ror.org/03m2x1q45" ;
    schema1:name "Lunar and Planetary Laboratory Electron Microprobe Facility" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA Analysis Laboratory
description: ADA laboratory or facility building block. Extends the core CDIF spatialExtent
  (schema:Place) with NeXus NXsource classification via additionalType. Inherits place
  name, identifier, alternateName, geo coordinates, and geosparql geometry from spatialExtent.
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/spatialExtent/schema.yaml
- type: object
  properties:
    schema:additionalType:
      type: array
      items:
        type: string
      contains:
        const: nxs:BaseClass/NXsource
      description: Must include nxs:BaseClass/NXsource for NeXus facility classification.
x-jsonld-prefixes:
  schema: http://schema.org/
  nxs: http://purl.org/nexusformat/definitions/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/laboratory/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/laboratory/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/laboratory/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/laboratory`

