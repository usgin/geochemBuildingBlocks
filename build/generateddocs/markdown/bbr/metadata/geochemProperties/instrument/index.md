
# ADA Analysis Instrument (Schema)

`ada.bbr.metadata.geochemProperties.instrument` *v0.1*

ADA analytical instrument extending the core CDIF instrument building block. Typed as schema:Thing + schema:Product with domain-specific classifications (e.g. nxs:BaseClass/NXinstrument) in schema:additionalType. Inherits hierarchical sub-components, manufacturer, model, calibration properties from core.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA Analysis Instrument

Extends the core CDIF [instrument](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/instrument/) building block for ADA analytical instruments. Instruments are typed as `schema:Thing` + `schema:Product` (from core) with domain-specific classifications in `schema:additionalType` (e.g. `nxs:BaseClass/NXinstrument`, `ada:AMSInstrument`).

Inherits all core instrument properties: hierarchical sub-components via `schema:hasPart`, manufacturer, model, ownership, calibration properties, and linked resources.

## Examples

### ADA Analysis Instrument Example
An analytical instrument extending the core CDIF instrument building block.
Typed as schema:Thing + schema:Product with NeXus and technique-specific
classifications in additionalType.
#### json
```json
{
  "@type": ["schema:Thing", "schema:Product"],
  "schema:name": "JEOL JXA-8530F Electron Microprobe",
  "schema:description": "Field-emission electron probe microanalyzer with 5 wavelength-dispersive spectrometers",
  "schema:identifier": "https://www.wikidata.org/wiki/Q116917974",
  "schema:additionalType": ["nxs:BaseClass/NXinstrument", "https://gcmd.earthdata.nasa.gov/kms/concept/76a947a3-4529-4fb7-87a7-f4b3a0a0de48"]
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
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/instrument/context.jsonld"
  ],
  "@type": [
    "schema:Thing",
    "schema:Product"
  ],
  "schema:name": "JEOL JXA-8530F Electron Microprobe",
  "schema:description": "Field-emission electron probe microanalyzer with 5 wavelength-dispersive spectrometers",
  "schema:identifier": "https://www.wikidata.org/wiki/Q116917974",
  "schema:additionalType": [
    "nxs:BaseClass/NXinstrument",
    "https://gcmd.earthdata.nasa.gov/kms/concept/76a947a3-4529-4fb7-87a7-f4b3a0a0de48"
  ]
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] a schema1:Product,
        schema1:Thing ;
    schema1:additionalType "https://gcmd.earthdata.nasa.gov/kms/concept/76a947a3-4529-4fb7-87a7-f4b3a0a0de48",
        "nxs:BaseClass/NXinstrument" ;
    schema1:description "Field-emission electron probe microanalyzer with 5 wavelength-dispersive spectrometers" ;
    schema1:identifier "https://www.wikidata.org/wiki/Q116917974" ;
    schema1:name "JEOL JXA-8530F Electron Microprobe" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA Analysis Instrument
description: ADA analytical instrument building block. Extends the core CDIF instrument
  building block with NeXus NXinstrument classification via additionalType. Instruments
  are typed as schema:Thing + schema:Product (from core) with domain-specific types
  (e.g. nxs:BaseClass/NXinstrument, ada:AMSInstrument) in additionalType.
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/instrument/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Domain-specific instrument type classifications. Should include
        a NeXus base class (e.g. nxs:BaseClass/NXinstrument) and/or technique-specific
        identifier (e.g. ada:AMSInstrument, GCMD instrument identifier).
      type: array
      items:
        type: string
      minItems: 1
  required:
  - schema:additionalType
x-jsonld-prefixes:
  schema: http://schema.org/
  nxs: http://purl.org/nexusformat/definitions/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/instrument/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/instrument/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/instrument/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/instrument`

