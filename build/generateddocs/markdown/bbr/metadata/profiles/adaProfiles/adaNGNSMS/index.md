
# ADA NG-NS-MS Profile (Schema)

`ada.bbr.metadata.profiles.adaProfiles.adaNGNSMS` *v0.1*

Technique-specific profile for Noble Gas and Nitrogen Static Mass Spectrometry (NG-NS-MS) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA NG-NS-MS Profile

Technique-specific metadata profile for Noble Gas and Nitrogen Static Mass Spectrometry (NG-NS-MS) products in the Astromat Data Archive. Noble gas and nitrogen static mass spectrometry analysis.

## Product Types
- `ada:NGNSMSRaw`
- `ada:NGNSMSProcessed`

## Valid Component Types
- `ada:NGNSMSRaw`
- `ada:NGNSMSProcessed`
- `ada:analysisLocation`
- `ada:annotatedImage`
- `ada:areaOfInterest`
- `ada:basemap`
- `ada:calibrationFile`
- `ada:code`
- `ada:contextPhotography`
- `ada:contextVideo`
- `ada:inputFile`
- `ada:instrumentMetadata`
- `ada:logFile`
- `ada:methodDescription`
- `ada:other`
- `ada:plot`
- `ada:processingMethod`
- `ada:quickLook`
- `ada:report`
- `ada:samplePreparation`
- `ada:shapefile`
- `ada:supplementalBasemap`
- `ada:supplementaryImage`
- `ada:worldFile`

## Examples

### NG-NS-MS Product Example
Example Noble Gas and Nitrogen Static Mass Spectrometry (NG-NS-MS) product metadata with all properties populated.
Mock data for validation and testing.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "ex": "https://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:adaNGNSMS-example-001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "NG-NS-MS Analysis of Meteorite ALH 84001 Fragment",
  "schema:description": "Example Noble Gas and Nitrogen Static Mass Spectrometry (NG-NS-MS) product metadata demonstrating all properties defined by the adaNGNSMS profile. Contains mock data for testing and validation.",
  "schema:additionalType": [
    "Noble Gas and Nitrogen Static Mass Spectrometry (NGNSMS) Processed",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.99999/adangnsms-example-001",
    "schema:url": "https://doi.org/10.99999/adangnsms-example-001"
  },
  "schema:url": "https://astromat.org/products/adangnsms-example-001",
  "schema:dateModified": "2026-01-15",
  "schema:version": "1.0",
  "schema:conditionsOfAccess": [
    "Unrestricted access for research purposes"
  ],
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Published",
  "schema:keywords": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "NG-NS-MS",
      "schema:termCode": "NG-NS-MS",
      "schema:inDefinedTermSet": "https://ada.astromat.org/vocabulary/techniques"
    },
    "meteorite",
    "astromaterials"
  ],
  "schema:creator": {
    "@list": [
      {
        "@type": "schema:Person",
        "schema:name": "Analytica, Maria",
        "schema:identifier": "https://orcid.org/0000-0001-2345-6789",
        "schema:affiliation": {
          "@type": "schema:Organization",
          "schema:name": "Lunar and Planetary Institute"
        },
        "schema:contactPoint": {
          "@type": "schema:ContactPoint",
          "schema:email": "analytica@example.org"
        }
      },
      {
        "@type": "schema:Person",
        "schema:name": "Researcher, John Q.",
        "schema:identifier": "https://orcid.org/0000-0002-9876-5432",
        "schema:affiliation": {
          "@type": "schema:Organization",
          "schema:name": "NASA Johnson Space Center"
        },
        "schema:contactPoint": {
          "@type": "schema:ContactPoint",
          "schema:email": "researcher@example.org"
        }
      }
    ]
  },
  "schema:contributor": [
    {
      "@type": "schema:Role",
      "schema:roleName": "principalInvestigator",
      "schema:contributor": {
        "@type": "schema:Person",
        "schema:name": "Leadscientist, Patricia",
        "schema:identifier": "https://orcid.org/0000-0003-1111-2222",
        "schema:contactPoint": {
          "@type": "schema:ContactPoint",
          "schema:email": "leadscientist@example.org"
        }
      }
    }
  ],
  "schema:funding": [
    {
      "@type": "schema:MonetaryGrant",
      "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "award number",
        "schema:value": "NNX17AE48G"
      },
      "schema:name": "Astromaterials Curation and Analysis",
      "schema:funder": {
        "@type": "schema:Organization",
        "schema:additionalType": [
          "schema:FundingAgency"
        ],
        "schema:name": "NASA - National Aeronautics and Space Administration"
      }
    }
  ],
  "schema:measurementTechnique": {
    "@type": "schema:DefinedTerm",
    "schema:name": "Noble Gas and Nitrogen Static Mass Spectrometry (NG-NS-MS)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/NG-NS-MS"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-ng-ns-ms-20260110-001",
      "schema:startDate": "2026-01-10T09:30:00",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "prov:Entity",
            "nxs:BaseClass/NXinstrument"
          ],
          "schema:additionalType": [
            "ada:NG-NS-MSInstrument"
          ],
          "schema:name": "Example NG-NS-MS Instrument",
          "schema:identifier": "ex:instrument-ng-ns-ms-001"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place",
          "nxs:BaseClass/NXsource"
        ],
        "schema:name": "Analytical Sciences Laboratory",
        "schema:identifier": "https://ror.org/00hx57361"
      },
      "schema:mainEntity": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "ALH 84001,123",
          "schema:identifier": [
            "igsn:10.60471/GSEEXAMPLE001"
          ],
          "schema:description": "Thin section of Allan Hills 84001 martian meteorite"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaNGNSMS-var-001",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "measurement_value",
      "schema:alternateName": [
        "NG-NS-MS primary measurement"
      ],
      "schema:description": "Primary measured quantity from Noble Gas and Nitrogen Static Mass Spectrometry (NG-NS-MS) analysis. This is example mock data for testing.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/ng-ns-ms_primary"
      ],
      "schema:unitText": "counts",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "counts"
    },
    {
      "@id": "ex:adaNGNSMS-var-002",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "position_x",
      "schema:alternateName": [
        "X coordinate"
      ],
      "schema:description": "Horizontal position coordinate on sample surface.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/position_x"
      ],
      "schema:unitText": "micrometer",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "DimensionComponent",
      "cdi:simpleUnitOfMeasure": "um"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaNGNSMS-ALH84001-archive.zip",
      "schema:description": "Archive containing NG-NS-MS data files and supplementary materials",
      "schema:contentUrl": "https://astromat.org/downloads/adangnsms-example-001.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "schema:additionalType": [
        "RO-CRATE"
      ],
      "spdx:checksum": {
        "@type": "spdx:Checksum",
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
      },
      "schema:size": {
        "@type": "schema:QuantitativeValue",
        "schema:value": 15728640,
        "schema:unitText": "byte"
      },
      "schema:provider": [
        {
          "@type": "schema:Organization",
          "schema:name": "Astromat Data Archive"
        }
      ],
      "schema:hasPart": [
        {
          "@id": "ex:adaNGNSMS-file-001",
          "@type": [
            "ada:image",
            "schema:ImageObject"
          ],
          "schema:name": "ALH84001_NG-NS-MS_001.tif",
          "schema:description": "NG-NS-MS data file for ALH 84001 thin section",
          "schema:additionalType": [
            "ada:NGNSMSRaw"
          ],
          "schema:encodingFormat": [
            "image/tiff"
          ],
          "schema:size": {
            "@type": "schema:QuantitativeValue",
            "schema:value": 10485760,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "@type": "spdx:Checksum",
            "spdx:algorithm": "MD5",
            "spdx:checksumValue": "d41d8cd98f00b204e9800998ecf8427e"
          },
          "componentType": {
            "@type": "ada:NGNSMSRaw"
          }
        },
        {
          "@id": "ex:adaNGNSMS-file-002",
          "@type": [
            "ada:document",
            "schema:DigitalDocument"
          ],
          "schema:name": "ALH84001_NG-NS-MS_methods.pdf",
          "schema:description": "Method description document for this analysis",
          "schema:additionalType": [
            "ada:methodDescription"
          ],
          "schema:encodingFormat": [
            "application/pdf"
          ],
          "schema:size": {
            "@type": "schema:QuantitativeValue",
            "schema:value": 524288,
            "schema:unitText": "byte"
          },
          "componentType": {
            "@type": "ada:methodDescription"
          }
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaNGNSMS-metadata-001",
    "schema:about": {
      "@id": "ex:adaNGNSMS-example-001"
    },
    "schema:dateModified": "2026-01-15",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/adaProfiles/adaNGNSMS"
      }
    ],
    "schema:maintainer": {
      "@type": "schema:Organization",
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-01-15T12:00:00Z",
    "schema:includedInDataCatalog": {
      "@type": "schema:DataCatalog",
      "schema:name": "Astromat Data Archive",
      "schema:url": "https://astromat.org"
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "prov": "http://www.w3.org/ns/prov#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaNGNSMS/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcterms": "http://purl.org/dc/terms/",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "ex": "https://example.org/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:adaNGNSMS-example-001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "NG-NS-MS Analysis of Meteorite ALH 84001 Fragment",
  "schema:description": "Example Noble Gas and Nitrogen Static Mass Spectrometry (NG-NS-MS) product metadata demonstrating all properties defined by the adaNGNSMS profile. Contains mock data for testing and validation.",
  "schema:additionalType": [
    "Noble Gas and Nitrogen Static Mass Spectrometry (NGNSMS) Processed",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.99999/adangnsms-example-001",
    "schema:url": "https://doi.org/10.99999/adangnsms-example-001"
  },
  "schema:url": "https://astromat.org/products/adangnsms-example-001",
  "schema:dateModified": "2026-01-15",
  "schema:version": "1.0",
  "schema:conditionsOfAccess": [
    "Unrestricted access for research purposes"
  ],
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Published",
  "schema:keywords": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "NG-NS-MS",
      "schema:termCode": "NG-NS-MS",
      "schema:inDefinedTermSet": "https://ada.astromat.org/vocabulary/techniques"
    },
    "meteorite",
    "astromaterials"
  ],
  "schema:creator": {
    "@list": [
      {
        "@type": "schema:Person",
        "schema:name": "Analytica, Maria",
        "schema:identifier": "https://orcid.org/0000-0001-2345-6789",
        "schema:affiliation": {
          "@type": "schema:Organization",
          "schema:name": "Lunar and Planetary Institute"
        },
        "schema:contactPoint": {
          "@type": "schema:ContactPoint",
          "schema:email": "analytica@example.org"
        }
      },
      {
        "@type": "schema:Person",
        "schema:name": "Researcher, John Q.",
        "schema:identifier": "https://orcid.org/0000-0002-9876-5432",
        "schema:affiliation": {
          "@type": "schema:Organization",
          "schema:name": "NASA Johnson Space Center"
        },
        "schema:contactPoint": {
          "@type": "schema:ContactPoint",
          "schema:email": "researcher@example.org"
        }
      }
    ]
  },
  "schema:contributor": [
    {
      "@type": "schema:Role",
      "schema:roleName": "principalInvestigator",
      "schema:contributor": {
        "@type": "schema:Person",
        "schema:name": "Leadscientist, Patricia",
        "schema:identifier": "https://orcid.org/0000-0003-1111-2222",
        "schema:contactPoint": {
          "@type": "schema:ContactPoint",
          "schema:email": "leadscientist@example.org"
        }
      }
    }
  ],
  "schema:funding": [
    {
      "@type": "schema:MonetaryGrant",
      "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "award number",
        "schema:value": "NNX17AE48G"
      },
      "schema:name": "Astromaterials Curation and Analysis",
      "schema:funder": {
        "@type": "schema:Organization",
        "schema:additionalType": [
          "schema:FundingAgency"
        ],
        "schema:name": "NASA - National Aeronautics and Space Administration"
      }
    }
  ],
  "schema:measurementTechnique": {
    "@type": "schema:DefinedTerm",
    "schema:name": "Noble Gas and Nitrogen Static Mass Spectrometry (NG-NS-MS)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/NG-NS-MS"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-ng-ns-ms-20260110-001",
      "schema:startDate": "2026-01-10T09:30:00",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "prov:Entity",
            "nxs:BaseClass/NXinstrument"
          ],
          "schema:additionalType": [
            "ada:NG-NS-MSInstrument"
          ],
          "schema:name": "Example NG-NS-MS Instrument",
          "schema:identifier": "ex:instrument-ng-ns-ms-001"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place",
          "nxs:BaseClass/NXsource"
        ],
        "schema:name": "Analytical Sciences Laboratory",
        "schema:identifier": "https://ror.org/00hx57361"
      },
      "schema:mainEntity": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "ALH 84001,123",
          "schema:identifier": [
            "igsn:10.60471/GSEEXAMPLE001"
          ],
          "schema:description": "Thin section of Allan Hills 84001 martian meteorite"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaNGNSMS-var-001",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "measurement_value",
      "schema:alternateName": [
        "NG-NS-MS primary measurement"
      ],
      "schema:description": "Primary measured quantity from Noble Gas and Nitrogen Static Mass Spectrometry (NG-NS-MS) analysis. This is example mock data for testing.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/ng-ns-ms_primary"
      ],
      "schema:unitText": "counts",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "counts"
    },
    {
      "@id": "ex:adaNGNSMS-var-002",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "position_x",
      "schema:alternateName": [
        "X coordinate"
      ],
      "schema:description": "Horizontal position coordinate on sample surface.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/position_x"
      ],
      "schema:unitText": "micrometer",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "DimensionComponent",
      "cdi:simpleUnitOfMeasure": "um"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaNGNSMS-ALH84001-archive.zip",
      "schema:description": "Archive containing NG-NS-MS data files and supplementary materials",
      "schema:contentUrl": "https://astromat.org/downloads/adangnsms-example-001.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "schema:additionalType": [
        "RO-CRATE"
      ],
      "spdx:checksum": {
        "@type": "spdx:Checksum",
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
      },
      "schema:size": {
        "@type": "schema:QuantitativeValue",
        "schema:value": 15728640,
        "schema:unitText": "byte"
      },
      "schema:provider": [
        {
          "@type": "schema:Organization",
          "schema:name": "Astromat Data Archive"
        }
      ],
      "schema:hasPart": [
        {
          "@id": "ex:adaNGNSMS-file-001",
          "@type": [
            "ada:image",
            "schema:ImageObject"
          ],
          "schema:name": "ALH84001_NG-NS-MS_001.tif",
          "schema:description": "NG-NS-MS data file for ALH 84001 thin section",
          "schema:additionalType": [
            "ada:NGNSMSRaw"
          ],
          "schema:encodingFormat": [
            "image/tiff"
          ],
          "schema:size": {
            "@type": "schema:QuantitativeValue",
            "schema:value": 10485760,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "@type": "spdx:Checksum",
            "spdx:algorithm": "MD5",
            "spdx:checksumValue": "d41d8cd98f00b204e9800998ecf8427e"
          },
          "componentType": {
            "@type": "ada:NGNSMSRaw"
          }
        },
        {
          "@id": "ex:adaNGNSMS-file-002",
          "@type": [
            "ada:document",
            "schema:DigitalDocument"
          ],
          "schema:name": "ALH84001_NG-NS-MS_methods.pdf",
          "schema:description": "Method description document for this analysis",
          "schema:additionalType": [
            "ada:methodDescription"
          ],
          "schema:encodingFormat": [
            "application/pdf"
          ],
          "schema:size": {
            "@type": "schema:QuantitativeValue",
            "schema:value": 524288,
            "schema:unitText": "byte"
          },
          "componentType": {
            "@type": "ada:methodDescription"
          }
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaNGNSMS-metadata-001",
    "schema:about": {
      "@id": "ex:adaNGNSMS-example-001"
    },
    "schema:dateModified": "2026-01-15",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/adaProfiles/adaNGNSMS"
      }
    ],
    "schema:maintainer": {
      "@type": "schema:Organization",
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-01-15T12:00:00Z",
    "schema:includedInDataCatalog": {
      "@type": "schema:DataCatalog",
      "schema:name": "Astromat Data Archive",
      "schema:url": "https://astromat.org"
    }
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:adaNGNSMS-example-001 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Noble Gas and Nitrogen Static Mass Spectrometry (NGNSMS) Processed",
        "ada:DataDeliveryPackage" ;
    schema1:conditionsOfAccess "Unrestricted access for research purposes" ;
    schema1:contributor [ a schema1:Role ;
            schema1:contributor [ a schema1:Person ;
                    schema1:contactPoint [ a schema1:ContactPoint ;
                            schema1:email "leadscientist@example.org" ] ;
                    schema1:identifier "https://orcid.org/0000-0003-1111-2222" ;
                    schema1:name "Leadscientist, Patricia" ] ;
            schema1:roleName "principalInvestigator" ] ;
    schema1:creativeWorkStatus "Published" ;
    schema1:creator ( [ a schema1:Person ;
                schema1:affiliation [ a schema1:Organization ;
                        schema1:name "Lunar and Planetary Institute" ] ;
                schema1:contactPoint [ a schema1:ContactPoint ;
                        schema1:email "analytica@example.org" ] ;
                schema1:identifier "https://orcid.org/0000-0001-2345-6789" ;
                schema1:name "Analytica, Maria" ] [ a schema1:Person ;
                schema1:affiliation [ a schema1:Organization ;
                        schema1:name "NASA Johnson Space Center" ] ;
                schema1:contactPoint [ a schema1:ContactPoint ;
                        schema1:email "researcher@example.org" ] ;
                schema1:identifier "https://orcid.org/0000-0002-9876-5432" ;
                schema1:name "Researcher, John Q." ] ) ;
    schema1:dateModified "2026-01-15" ;
    schema1:description "Example Noble Gas and Nitrogen Static Mass Spectrometry (NG-NS-MS) product metadata demonstrating all properties defined by the adaNGNSMS profile. Contains mock data for testing and validation." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:additionalType "RO-CRATE" ;
            schema1:contentUrl "https://astromat.org/downloads/adangnsms-example-001.zip" ;
            schema1:description "Archive containing NG-NS-MS data files and supplementary materials" ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaNGNSMS-file-001,
                ex:adaNGNSMS-file-002 ;
            schema1:name "adaNGNSMS-ALH84001-archive.zip" ;
            schema1:provider [ a schema1:Organization ;
                    schema1:name "Astromat Data Archive" ] ;
            schema1:size [ a schema1:QuantitativeValue ;
                    schema1:unitText "byte" ;
                    schema1:value 15728640 ] ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2" ] ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:funder [ a schema1:Organization ;
                    schema1:additionalType "schema:FundingAgency" ;
                    schema1:name "NASA - National Aeronautics and Space Administration" ] ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "award number" ;
                    schema1:value "NNX17AE48G" ] ;
            schema1:name "Astromaterials Curation and Analysis" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:url "https://doi.org/10.99999/adangnsms-example-001" ;
            schema1:value "10.99999/adangnsms-example-001" ] ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://ada.astromat.org/vocabulary/techniques" ;
            schema1:name "NG-NS-MS" ;
            schema1:termCode "NG-NS-MS" ],
        "astromaterials",
        "meteorite" ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/NG-NS-MS" ;
            schema1:name "Noble Gas and Nitrogen Static Mass Spectrometry (NG-NS-MS)" ] ;
    schema1:name "NG-NS-MS Analysis of Meteorite ALH 84001 Fragment" ;
    schema1:subjectOf ex:adaNGNSMS-metadata-001 ;
    schema1:url "https://astromat.org/products/adangnsms-example-001" ;
    schema1:variableMeasured ex:adaNGNSMS-var-001,
        ex:adaNGNSMS-var-002 ;
    schema1:version "1.0" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-ng-ns-ms-20260110-001" ;
            schema1:location [ a <http://purl.org/nexusformat/definitions/BaseClass/NXsource>,
                        schema1:Place ;
                    schema1:identifier "https://ror.org/00hx57361" ;
                    schema1:name "Analytical Sciences Laboratory" ] ;
            schema1:mainEntity [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Thin section of Allan Hills 84001 martian meteorite" ;
                    schema1:identifier "igsn:10.60471/GSEEXAMPLE001" ;
                    schema1:name "ALH 84001,123" ] ;
            schema1:startDate "2026-01-10T09:30:00" ;
            prov:used [ a <http://purl.org/nexusformat/definitions/BaseClass/NXinstrument>,
                        schema1:Thing,
                        prov:Entity ;
                    schema1:additionalType "ada:NG-NS-MSInstrument" ;
                    schema1:identifier "ex:instrument-ng-ns-ms-001" ;
                    schema1:name "Example NG-NS-MS Instrument" ] ] .

ex:adaNGNSMS-file-001 a schema1:ImageObject,
        ada:image ;
    schema1:additionalType "ada:NGNSMSRaw" ;
    schema1:description "NG-NS-MS data file for ALH 84001 thin section" ;
    schema1:encodingFormat "image/tiff" ;
    schema1:name "ALH84001_NG-NS-MS_001.tif" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 10485760 ] ;
    spdx:checksum [ a spdx:Checksum ;
            spdx:algorithm "MD5" ;
            spdx:checksumValue "d41d8cd98f00b204e9800998ecf8427e" ] .

ex:adaNGNSMS-file-002 a schema1:DigitalDocument,
        ada:document ;
    schema1:additionalType "ada:methodDescription" ;
    schema1:description "Method description document for this analysis" ;
    schema1:encodingFormat "application/pdf" ;
    schema1:name "ALH84001_NG-NS-MS_methods.pdf" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 524288 ] .

ex:adaNGNSMS-metadata-001 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/profiles/adaProfiles/adaNGNSMS>,
        <https://w3id.org/cdif/core/1.0/>,
        <https://w3id.org/cdif/discovery/1.0/> ;
    schema1:about ex:adaNGNSMS-example-001 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-01-15" ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:name "Astromat Data Archive" ;
            schema1:url "https://astromat.org" ] ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-01-15T12:00:00Z" .

ex:adaNGNSMS-var-001 a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "counts" ;
    schema1:alternateName "NG-NS-MS primary measurement" ;
    schema1:description "Primary measured quantity from Noble Gas and Nitrogen Static Mass Spectrometry (NG-NS-MS) analysis. This is example mock data for testing." ;
    schema1:name "measurement_value" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/variables/ng-ns-ms_primary" ;
    schema1:unitText "counts" .

ex:adaNGNSMS-var-002 a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "DimensionComponent" ;
    cdi:simpleUnitOfMeasure "um" ;
    schema1:alternateName "X coordinate" ;
    schema1:description "Horizontal position coordinate on sample surface." ;
    schema1:name "position_x" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/variables/position_x" ;
    schema1:unitText "micrometer" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA NG-NS-MS Product Profile
description: Technique-specific profile for Noble Gas and Nitrogen Static Mass Spectrometry
  (NG-NS-MS) products. Extends the base ADA product profile with constraints on valid
  NG-NS-MS component types.
allOf:
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a NG-NS-MS product type identifier.
      contains:
        enum:
        - Noble Gas and Nitrogen Static Mass Spectrometry (NGNSMS) Processed
        - Noble Gas and Nitrogen Static Mass Spectrometry (NGNSMS) Raw
        - Noble gas and Nitrogen Static Mass Spectrometry
    schema:distribution:
      items:
        oneOf:
        - required:
          - componentType
          properties:
            componentType:
              anyOf:
              - properties:
                  '@type':
                    enum:
                    - ada:NGNSMSRaw
                    - ada:NGNSMSProcessed
              - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaProduct/schema.yaml#/$defs/universalComponentType
        - required:
          - schema:hasPart
          properties:
            schema:hasPart:
              items:
                properties:
                  componentType:
                    anyOf:
                    - properties:
                        '@type':
                          enum:
                          - ada:NGNSMSRaw
                          - ada:NGNSMSProcessed
                    - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaProduct/schema.yaml#/$defs/universalComponentType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  csvw: http://www.w3.org/ns/csvw#
  prov: http://www.w3.org/ns/prov#
  spdx: http://spdx.org/rdf/terms#
  nxs: http://purl.org/nexusformat/definitions/
  dcterms: http://purl.org/dc/terms/
  geosparql: http://www.opengis.net/ont/geosparql#

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaNGNSMS/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaNGNSMS/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaNGNSMS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/profiles/adaProfiles/adaNGNSMS`

