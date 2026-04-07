
# ADA Product Profile (Schema)

`ada.bbr.metadata.profiles.adaProfiles.adaProduct` *v0.1*

Top-level ADA product metadata profile composing all ADA building blocks

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA Product Profile

Top-level metadata profile for Astromat Data Archive (ADA) products. Composes all ADA building blocks into a complete product metadata schema. Each ADA product consists of one or more data files and supplemental files, each with an associated YAML metadata file.

The profile includes:
- Basic metadata (name, description, dates, status)
- Creator and contributor information
- Funding and licensing
- Measurement technique and provenance (instruments, laboratories, samples)
- Variable definitions
- Distribution with file-level metadata
- Metadata record information (subjectOf)

## Examples

### ADA Product Example
Example Astromat Data Archive (ADA) product metadata with all properties populated.
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
  "@id": "ex:adaProduct-example-001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "ADA Analysis of Meteorite ALH 84001 Fragment",
  "schema:description": "Example Astromat Data Archive (ADA) product metadata demonstrating all properties defined by the adaProduct profile. Contains mock data for testing and validation.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Image (EMPA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.99999/adaproduct-example-001",
    "schema:url": "https://doi.org/10.99999/adaproduct-example-001"
  },
  "schema:url": "https://astromat.org/products/adaproduct-example-001",
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
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Astromat Data Archive",
      "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/ADA",
      "schema:termCode": "ADA",
      "schema:inDefinedTermSet": "https://ada.astromat.org/vocabulary/techniques"
    },
    "meteorite",
    "astromaterials"
  ],
  "schema:creator": {
    "@list": [
      {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Analytica, Maria",
        "schema:identifier": "https://orcid.org/0000-0001-2345-6789",
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Lunar and Planetary Institute"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "analytica@example.org"
        }
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Researcher, John Q.",
        "schema:identifier": "https://orcid.org/0000-0002-9876-5432",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "researcher@example.org"
        },
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "NASA Johnson Space Center"
        }
      }
    ]
  },
  "schema:contributor": [
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "principalInvestigator",
      "schema:contributor": {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Leadscientist, Patricia",
        "schema:identifier": "https://orcid.org/0000-0003-1111-2222",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "leadscientist@example.org"
        }
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "award number",
        "schema:value": "NNX17AE48G"
      },
      "schema:name": "Astromaterials Curation and Analysis",
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:additionalType": [
          "schema:FundingAgency"
        ],
        "schema:name": "NASA - National Aeronautics and Space Administration"
      }
    }
  ],
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Astromat Data Archive (ADA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/ADA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-ada-20260110-001",
      "schema:startDate": "2026-01-10T09:30:00",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:ADAInstrument"
          ],
          "schema:name": "Example ADA Instrument",
          "schema:identifier": [
            "ex:instrument-ada-001"
          ]
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Analytical Sciences Laboratory",
        "schema:identifier": "https://ror.org/00hx57361",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
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
      "@id": "ex:adaProduct-var-001",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "measurement_value",
      "schema:alternateName": [
        "ADA primary measurement"
      ],
      "schema:description": "Primary measured quantity from Astromat Data Archive (ADA) analysis. This is example mock data for testing.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/ada_primary"
      ],
      "schema:unitText": "counts",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "counts"
    },
    {
      "@id": "ex:adaProduct-var-002",
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
      "schema:name": "adaProduct-ALH84001-archive.zip",
      "schema:description": "Archive containing ADA data files and supplementary materials",
      "schema:contentUrl": "https://astromat.org/downloads/adaproduct-example-001.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "schema:additionalType": [
        "RO-CRATE"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 15728640,
        "schema:unitText": "byte"
      },
      "schema:provider": [
        {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Astromat Data Archive"
        }
      ],
      "schema:hasPart": [
        {
          "@id": "ex:adaProduct-file-001",
          "@type": [
            "ada:image",
            "schema:ImageObject",
            "schema:MediaObject"
          ],
          "schema:name": "ALH84001_ADA_001.tif",
          "schema:description": "ADA data file for ALH 84001 thin section",
          "schema:additionalType": [
            "ada:EMPAImage"
          ],
          "schema:encodingFormat": [
            "image/tiff"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 10485760,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "@type": [
              "spdx:Checksum"
            ],
            "spdx:algorithm": "MD5",
            "spdx:checksumValue": "d41d8cd98f00b204e9800998ecf8427e"
          },
          "ada:componentType": "ada:EMPAImage"
        },
        {
          "@id": "ex:adaProduct-file-002",
          "@type": [
            "ada:document",
            "schema:DigitalDocument",
            "schema:MediaObject"
          ],
          "schema:name": "ALH84001_ADA_methods.pdf",
          "schema:description": "Method description document for this analysis",
          "schema:additionalType": [
            "ada:methodDescription"
          ],
          "schema:encodingFormat": [
            "application/pdf"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 524288,
            "schema:unitText": "byte"
          },
          "ada:componentType": "ada:methodDescription"
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
    "@id": "ex:adaProduct-metadata-001",
    "schema:about": {
      "@id": "ex:adaProduct-example-001"
    },
    "schema:dateModified": "2026-01-15",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-01-15T12:00:00Z",
    "schema:includedInDataCatalog": {
      "@type": [
        "schema:DataCatalog"
      ],
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
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaProduct/context.jsonld",
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
  "@id": "ex:adaProduct-example-001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "ADA Analysis of Meteorite ALH 84001 Fragment",
  "schema:description": "Example Astromat Data Archive (ADA) product metadata demonstrating all properties defined by the adaProduct profile. Contains mock data for testing and validation.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Image (EMPA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.99999/adaproduct-example-001",
    "schema:url": "https://doi.org/10.99999/adaproduct-example-001"
  },
  "schema:url": "https://astromat.org/products/adaproduct-example-001",
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
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Astromat Data Archive",
      "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/ADA",
      "schema:termCode": "ADA",
      "schema:inDefinedTermSet": "https://ada.astromat.org/vocabulary/techniques"
    },
    "meteorite",
    "astromaterials"
  ],
  "schema:creator": {
    "@list": [
      {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Analytica, Maria",
        "schema:identifier": "https://orcid.org/0000-0001-2345-6789",
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Lunar and Planetary Institute"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "analytica@example.org"
        }
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Researcher, John Q.",
        "schema:identifier": "https://orcid.org/0000-0002-9876-5432",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "researcher@example.org"
        },
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "NASA Johnson Space Center"
        }
      }
    ]
  },
  "schema:contributor": [
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "principalInvestigator",
      "schema:contributor": {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Leadscientist, Patricia",
        "schema:identifier": "https://orcid.org/0000-0003-1111-2222",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "leadscientist@example.org"
        }
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "award number",
        "schema:value": "NNX17AE48G"
      },
      "schema:name": "Astromaterials Curation and Analysis",
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:additionalType": [
          "schema:FundingAgency"
        ],
        "schema:name": "NASA - National Aeronautics and Space Administration"
      }
    }
  ],
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Astromat Data Archive (ADA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/ADA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-ada-20260110-001",
      "schema:startDate": "2026-01-10T09:30:00",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:ADAInstrument"
          ],
          "schema:name": "Example ADA Instrument",
          "schema:identifier": [
            "ex:instrument-ada-001"
          ]
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Analytical Sciences Laboratory",
        "schema:identifier": "https://ror.org/00hx57361",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
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
      "@id": "ex:adaProduct-var-001",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "measurement_value",
      "schema:alternateName": [
        "ADA primary measurement"
      ],
      "schema:description": "Primary measured quantity from Astromat Data Archive (ADA) analysis. This is example mock data for testing.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/ada_primary"
      ],
      "schema:unitText": "counts",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "counts"
    },
    {
      "@id": "ex:adaProduct-var-002",
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
      "schema:name": "adaProduct-ALH84001-archive.zip",
      "schema:description": "Archive containing ADA data files and supplementary materials",
      "schema:contentUrl": "https://astromat.org/downloads/adaproduct-example-001.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "schema:additionalType": [
        "RO-CRATE"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 15728640,
        "schema:unitText": "byte"
      },
      "schema:provider": [
        {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Astromat Data Archive"
        }
      ],
      "schema:hasPart": [
        {
          "@id": "ex:adaProduct-file-001",
          "@type": [
            "ada:image",
            "schema:ImageObject",
            "schema:MediaObject"
          ],
          "schema:name": "ALH84001_ADA_001.tif",
          "schema:description": "ADA data file for ALH 84001 thin section",
          "schema:additionalType": [
            "ada:EMPAImage"
          ],
          "schema:encodingFormat": [
            "image/tiff"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 10485760,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "@type": [
              "spdx:Checksum"
            ],
            "spdx:algorithm": "MD5",
            "spdx:checksumValue": "d41d8cd98f00b204e9800998ecf8427e"
          },
          "ada:componentType": "ada:EMPAImage"
        },
        {
          "@id": "ex:adaProduct-file-002",
          "@type": [
            "ada:document",
            "schema:DigitalDocument",
            "schema:MediaObject"
          ],
          "schema:name": "ALH84001_ADA_methods.pdf",
          "schema:description": "Method description document for this analysis",
          "schema:additionalType": [
            "ada:methodDescription"
          ],
          "schema:encodingFormat": [
            "application/pdf"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 524288,
            "schema:unitText": "byte"
          },
          "ada:componentType": "ada:methodDescription"
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
    "@id": "ex:adaProduct-metadata-001",
    "schema:about": {
      "@id": "ex:adaProduct-example-001"
    },
    "schema:dateModified": "2026-01-15",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-01-15T12:00:00Z",
    "schema:includedInDataCatalog": {
      "@type": [
        "schema:DataCatalog"
      ],
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

ex:adaProduct-example-001 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Electron Microprobe Analysis Image (EMPA)",
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
    schema1:description "Example Astromat Data Archive (ADA) product metadata demonstrating all properties defined by the adaProduct profile. Contains mock data for testing and validation." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:additionalType "RO-CRATE" ;
            schema1:contentUrl "https://astromat.org/downloads/adaproduct-example-001.zip" ;
            schema1:description "Archive containing ADA data files and supplementary materials" ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaProduct-file-001,
                ex:adaProduct-file-002 ;
            schema1:name "adaProduct-ALH84001-archive.zip" ;
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
            schema1:url "https://doi.org/10.99999/adaproduct-example-001" ;
            schema1:value "10.99999/adaproduct-example-001" ] ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/ADA" ;
            schema1:inDefinedTermSet "https://ada.astromat.org/vocabulary/techniques" ;
            schema1:name "Astromat Data Archive" ;
            schema1:termCode "ADA" ],
        "astromaterials",
        "meteorite" ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/ADA" ;
            schema1:name "Astromat Data Archive (ADA)" ] ;
    schema1:name "ADA Analysis of Meteorite ALH 84001 Fragment" ;
    schema1:subjectOf ex:adaProduct-metadata-001 ;
    schema1:url "https://astromat.org/products/adaproduct-example-001" ;
    schema1:variableMeasured ex:adaProduct-var-001,
        ex:adaProduct-var-002 ;
    schema1:version "1.0" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-ada-20260110-001" ;
            schema1:location [ a schema1:Place ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:identifier "https://ror.org/00hx57361" ;
                    schema1:name "Analytical Sciences Laboratory" ] ;
            schema1:mainEntity [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Thin section of Allan Hills 84001 martian meteorite" ;
                    schema1:identifier "igsn:10.60471/GSEEXAMPLE001" ;
                    schema1:name "ALH 84001,123" ] ;
            schema1:startDate "2026-01-10T09:30:00" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ada:ADAInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-ada-001" ;
                    schema1:name "Example ADA Instrument" ] ] .

ex:adaProduct-file-001 a schema1:ImageObject,
        schema1:MediaObject,
        ada:image ;
    schema1:additionalType "ada:EMPAImage" ;
    schema1:description "ADA data file for ALH 84001 thin section" ;
    schema1:encodingFormat "image/tiff" ;
    schema1:name "ALH84001_ADA_001.tif" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 10485760 ] ;
    spdx:checksum [ a spdx:Checksum ;
            spdx:algorithm "MD5" ;
            spdx:checksumValue "d41d8cd98f00b204e9800998ecf8427e" ] ;
    ada:componentType "ada:EMPAImage" .

ex:adaProduct-file-002 a schema1:DigitalDocument,
        schema1:MediaObject,
        ada:document ;
    schema1:additionalType "ada:methodDescription" ;
    schema1:description "Method description document for this analysis" ;
    schema1:encodingFormat "application/pdf" ;
    schema1:name "ALH84001_ADA_methods.pdf" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 524288 ] ;
    ada:componentType "ada:methodDescription" .

ex:adaProduct-metadata-001 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct> ;
    schema1:about ex:adaProduct-example-001 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-01-15" ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:name "Astromat Data Archive" ;
            schema1:url "https://astromat.org" ] ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-01-15T12:00:00Z" .

ex:adaProduct-var-001 a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "counts" ;
    schema1:alternateName "ADA primary measurement" ;
    schema1:description "Primary measured quantity from Astromat Data Archive (ADA) analysis. This is example mock data for testing." ;
    schema1:name "measurement_value" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/variables/ada_primary" ;
    schema1:unitText "counts" .

ex:adaProduct-var-002 a cdi:InstanceVariable,
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
$id: https://w3id.org/adaJSONLD/schema/3.0
title: Astromat Archive Product Metadata
description: Schema for JSON metadata documenting products in Astromat Data Archive
  (ADA). Each project consists of one or more data files and 0 to many supplemental
  files. Each file MUST have an associated YAML metadata file, with the same name,
  but '.yaml' as the file extension. Version 3.0 aligned with CDIF 2026 schema for
  DDI-CDI variable types and CSVW tabular data properties.
type: object
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifCore/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataDescription/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifArchiveDistribution/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifProvenance/schema.yaml
- type: object
  properties:
    '@type':
      type: array
      items:
        type: string
        enum:
        - schema:Dataset
        - schema:Product
    schema:additionalType:
      type: array
      description: Should have the ada product type and 'ada:DataDeliveryPackage'
      items:
        type: string
      contains:
        enum:
        - 40Ar/39Ar Geochronology and Thermochronology (ARGT)
        - 40Ar/39Ar geochronology and thermochronology
        - Accelerator Mass Spectrometry (AMS)
        - Accelerator Mass Spectrometry
        - Advanced Imaging and Visualization of Astromaterials (AIVA)
        - Analysis Advanced Imaging and Visualization of Astromaterials (AIVA)
        - Basemap
        - Differential Scanning Calorimetry (DSC)
        - Differential Scanning Calorimetry
        - Electron Microprobe Analysis (EMPA) Collection
        - Electron Microprobe Analysis Image (EMPA)
        - Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)
        - Electron Microprobe Analysis (EMPA)
        - Electron microprobe analysis
        - Elemental Analysis-Isotope Ratio Mass Spectrometry (EA-IRMS)
        - Elemental analysis - isotope ratio mass spectrometry
        - Fluorescence Microscopy (UVFM) Image
        - UV Fluorescence Microscopy
        - Fourier Transform Ion Cyclotron Resonance Mass Spectrometry (FTICRMS) Cube
        - Fourier Transform Ion Cyclotron Resonance Mass Spectrometry (FTICRMS) Tabular
        - Fourier Transform Ion Cyclotron Resonance Mass Spectrometry
        - Gas Chromatography-Mass Spectrometry (GCMS)
        - Gas Chromatography-Mass Spectrometry
        - Gas Pycnometry (GPYC) Processed
        - Gas Pycnometry (GPYC) Raw
        - Gas pycnometry
        - High-resolution Inductively Coupled Plasma Mass Spectroscopy (HRICPMS) Processed
        - High-resolution Inductively Coupled Plasma Mass Spectroscopy (HRICPMS) Raw
        - High-resolution inductively coupled plasma mass spectrometry
        - Inductively Coupled Plasma - Optical Emission Spectroscopy (ICPOES) Intermediate
        - Inductively Coupled Plasma - Optical Emission Spectroscopy (ICPOES) Processed
        - Inductively Coupled Plasma - Optical Emission Spectroscopy (ICPOES) Raw
        - Inductively coupled plasma - optical emission spectrometry
        - Ion Chromatography (IC)
        - Ion Chromatography
        - Laser Assisted Fluorination (LAF) Processed
        - Laser Assisted Fluorination (LAF) Raw
        - Liquid Chromatography - Mass Spectrometry (LCMS) Collection
        - Liquid Chromatography-Mass Spectrometry
        - Lock-In Thermography (LIT) Collection
        - Lock-In Thermography (LIT) image
        - Lock-In Thermography
        - Microprobe Two-Step Laser Mass Spectrometry (L2MS)
        - Microprobe Two-Step Laser Mass Spectrometry
        - Multi-Collector Inductively Coupled Plasma Mass Spectrometry (MCICPMS) processed
        - Multi-Collector Inductively Coupled Plasma Mass Spectrometry (MCICPMS) Raw
        - Multi-Collector Inductively Coupled Plasma Mass Spectrometry
        - Nanoscale Infrared Mapping (NanoIR) Background
        - Nanoscale Infrared Mapping (NanoIR) MapCollection
        - Nanoscale Infrared Mapping (NanoIR) Point Data
        - Nanoscale Infrared Mapping
        - Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) Image
        - Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) Raw
        - Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) Tabular
        - Nanoscale secondary ion mass spectrometry
        - Noble Gas and Nitrogen Static Mass Spectrometry (NGNSMS) Raw
        - Noble Gas and Nitrogen Static Mass Spectrometry (NGNSMS) Processed
        - Noble gas and Nitrogen Static Mass Spectrometry
        - Particle Size Frequency Distribution (PSFD)
        - Particle Size Frequency Distribution
        - Quadrupole Inductively Coupled Plasma Mass Spectrometry (QICPMS) Processed
        - Quadrupole Inductively Coupled Plasma Mass Spectrometry (QICPMS) Raw
        - Quadrupole Inductively Coupled Plasma Mass Spectrometry
        - Quantitative Reflective Imaging System (QRIS)
        - Quantitative Reflective Imaging System (QRIS) Calibrated
        - Raman vibrational spectroscopy
        - Resonance ionization time of flight noble gas mass spectrometry (RITOFNGMS)
          Processed
        - Resonance ionization time of flight noble gas mass spectrometry (RITOFNGMS)
          Spectra
        - Resonance ionization time of flight noble gas mass spectrometry
        - Scanning Electron Microscopy (SEM) Image
        - Scanning Electron Microscopy Electron Backscatter Diffraction (SEMEBSD)
          Grain Image
        - Scanning Electron Microscopy Energy Dispersive X-ray Spectroscopy (SEMEDS)
          Point Data
        - Scanning Electron Microscopy Energy Dispersive X-ray Spectroscopy (SEMEDS)
          image
        - Scanning Electron Microscopy High Resolution Cathodoluminescence (SEMHRCL)
          image
        - Scanning electron microscopy
        - Focused ion beam-scanning electron microscopy
        - Scanning Transmission Electron Microscopy (STEM) Image
        - Scanning Transmission Electron Microscopy Electron Energy-loss Spectra (STEMEELS)
          Cube
        - Scanning Transmission Electron Microscopy Electron Energy-loss Spectra (STEMEELS)
          Tabular
        - Scanning Transmission Electron Microscopy Energy Dispersive X-ray Spectroscopy
          (STEMEDS) Cube
        - Scanning Transmission Electron Microscopy Energy Dispersive X-ray Spectroscopy
          (STEMEDS) Tabular
        - Scanning Transmission Electron Microscopy Energy Dispersive X-ray Spectroscopy
          (STEMEDS) Tomography
        - Secondary Ion Mass Spectrometry (SIMS) Tabular
        - Secondary ion mass spectrometry
        - Seismic Velocities and Rock Ultrasonic Elastic Constants (SVRUEC)
        - Seismic Velocities and Rock Ultrasonic Elastic Constants
        - Structured Light Scanning (SLS) Individual Scan Collection
        - Structured Light Scanning (SLS) Shape Model
        - Structured Light Scanning
        - Time-of-flight secondary ion mass spectrometry (TOFSIMS)
        - Transmission Electron Microscopy (TEM) Image
        - Transmission Electron Microscopy (TEM) Patterns Image
        - Transmission Electron Microscopy
        - Visible Light Microscopy (VLM) Image
        - Visible Light Microscopy
        - Visible, near-infrared, and mid-infrared Spectroscopy (VNMIR) Point
        - Visible, near-, and mid-infrared spectroscopy
        - X-ray Absorption Near Edge Structure Hyperspectral Image Stack (XANES)
        - X-ray absorption near edge structure (XANES) spectroscopy
        - X-ray Computed Tomography (XCT) Image Collection
        - X-ray computed tomography
        - X-ray Diffraction (XRD) Tabular
        - X-ray diffraction
      minItems: 2
    submissionType:
      type: string
    schema:license:
      description: Legal statement of conditions for use and access
      type: array
      minItems: 0
      items:
        anyOf:
        - type: string
        - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/creativeWork/schema.yaml
    schema:relatedLink:
      type: array
      description: Links to related resources at the product level
      items:
        type: object
        properties:
          '@type':
            type: array
            items:
              type: string
            contains:
              const: schema:LinkRole
            minItems: 1
          schema:linkRelationship:
            type: string
          schema:target:
            type: object
            properties:
              '@type':
                type: array
                items:
                  type: string
                contains:
                  const: schema:EntryPoint
                minItems: 1
              schema:encodingFormat:
                type: string
              schema:name:
                type: string
              schema:url:
                type: string
    schema:creativeWorkStatus:
      type: string
    schema:measurementTechnique:
      type: object
      description: Text description of the measurement method
      properties:
        '@type':
          type: array
          items:
            type: string
          contains:
            const: schema:DefinedTerm
          minItems: 1
        schema:name:
          type: string
        schema:identifier:
          type: string
    prov:wasGeneratedBy:
      description: ADA analysis events. Extends cdifProvActivity (from cdifProvenance)
        with ADA-specific instrument, laboratory, and sample properties.
      type: array
      items:
        type: object
        properties:
          prov:used:
            type: array
            description: Instruments used in the analysis
            items:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/instrument/schema.yaml
          schema:location:
            $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/laboratory/schema.yaml
          schema:mainEntity:
            type: array
            description: Samples analyzed
            items:
              type: object
              properties:
                '@type':
                  type: array
                  items:
                    type: string
                  allOf:
                  - contains:
                      const: schema:Thing
                  - contains:
                      const: https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample
                  minItems: 2
                schema:additionalType:
                  type: array
                  items:
                    type: string
                schema:identifier:
                  type: array
                  items:
                    type: string
          schema:startDate:
            type: string
        required:
        - prov:used
    schema:variableMeasured:
      description: ADA variable definitions. Extends cdifVariableMeasured (from cdifDataDescription)
        with additional ADA properties. Requires description with minLength 10.
      type: array
      items:
        type: object
        properties:
          schema:description:
            type: string
            minLength: 10
          schema:alternateName:
            type: array
            items:
              type: string
              description: Human intelligible name for variable that conveys semantics
          schema:measurementTechnique:
            anyOf:
            - type: string
            - type: object
              properties:
                '@id':
                  type: string
            - type: object
              properties:
                '@type':
                  type: array
                  items:
                    type: string
                  contains:
                    const: schema:DefinedTerm
                  minItems: 1
                schema:name:
                  type: string
              required:
              - '@type'
              - schema:name
          schema:unitText:
            type: string
          schema:unitCode:
            anyOf:
            - type: string
            - type: object
              properties:
                '@id':
                  type: string
            - type: object
              properties:
                '@type':
                  type: array
                  items:
                    type: string
                  contains:
                    const: schema:DefinedTerm
                  minItems: 1
                schema:name:
                  type: string
              required:
              - '@type'
              - schema:name
          schema:minValue:
            type: number
          schema:maxValue:
            type: number
          schema:url:
            type: string
            format: uri
        required:
        - schema:description
    schema:spatialCoverage:
      description: Geographic extent of resource content.
      type: array
      items:
        $ref: '#/$defs/SpatialExtent'
    schema:temporalCoverage:
      description: Temporal extent of resource content.
      type: array
      items:
        $ref: '#/$defs/TemporalExtent'
    dqv:hasQualityMeasurement:
      description: Quality measurements reported to assess the resource.
      type: array
      items:
        $ref: '#/$defs/QualityMeasure'
    schema:distribution:
      description: Distribution inherits from cdifCore (DataDownload, WebAPI) and
        cdifArchiveDistribution (archive with hasPart). ADA file-type classification
        uses ada:componentType on hasPart items.
      type: array
      items:
        type: object
        properties:
          schema:hasPart:
            items:
              allOf:
              - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/files/schema.yaml
              - type: object
                properties:
                  ada:componentType:
                    type: string
                    description: ADA file type classification. Values are restricted
                      by technique-specific profiles. Universal types (e.g. ada:calibrationFile,
                      ada:report) are valid across all techniques.
    schema:subjectOf:
      properties:
        dcterms:conformsTo:
          contains:
            type: object
            properties:
              '@id':
                const: https://w3id.org/geochem/metadata/profiles/adaProduct
$defs:
  SpatialExtent:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/spatialExtent/schema.yaml
  TemporalExtent:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/temporalExtent/schema.yaml
  QualityMeasure:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/qualityProperties/qualityMeasure/schema.yaml
  universalComponentType:
    description: Component type values valid across all ADA techniques. Used in ada:componentType
      on hasPart items.
    enum:
    - ada:analysisLocation
    - ada:annotatedImage
    - ada:areaOfInterest
    - ada:basemap
    - ada:calibrationFile
    - ada:code
    - ada:contextPhotography
    - ada:contextVideo
    - ada:inputFile
    - ada:instrumentMetadata
    - ada:logFile
    - ada:methodDescription
    - ada:other
    - ada:plot
    - ada:processingMethod
    - ada:quickLook
    - ada:report
    - ada:samplePreparation
    - ada:shapefile
    - ada:supplementalBasemap
    - ada:supplementaryImage
    - ada:worldFile
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

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaProduct/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaProduct/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xas": "https://xas.org/dictionary/",
    "time": "http://www.w3.org/2006/time#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaProduct/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/profiles/adaProfiles/adaProduct`

