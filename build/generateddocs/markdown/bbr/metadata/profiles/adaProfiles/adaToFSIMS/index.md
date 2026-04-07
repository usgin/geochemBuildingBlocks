
# ADA ToF-SIMS Profile (Schema)

`ada.bbr.metadata.profiles.adaProfiles.adaToFSIMS` *v0.1*

Technique-specific profile for Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA ToF-SIMS Profile

Technique-specific metadata profile for Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS) products in the Astromat Data Archive. Time-of-flight secondary ion mass spectrometry surface analysis.

## Product Types
- `ada:TOFSIMSCollection`

## Valid Component Types
- `ada:TOFSIMSCollection`
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

### ToF-SIMS Product Example
Example Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS) product metadata with all properties populated.
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
    "@id": "ex:adaToFSIMS-example-001",
    "@type": [
        "schema:Dataset",
        "schema:Product"
    ],
    "schema:name": "ToF-SIMS Analysis of Meteorite ALH 84001 Fragment",
    "schema:description": "Example Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS) product metadata demonstrating all properties defined by the adaToFSIMS profile. Contains mock data for testing and validation.",
    "schema:additionalType": [
        "Time-of-flight secondary ion mass spectrometry (TOFSIMS)",
        "ada:DataDeliveryPackage"
    ],
    "schema:identifier": {
        "@type": [
            "schema:PropertyValue"
        ],
        "schema:propertyID": "https://registry.identifiers.org/registry/doi",
        "schema:value": "10.99999/adatofsims-example-001",
        "schema:url": "https://doi.org/10.99999/adatofsims-example-001"
    },
    "schema:url": "https://astromat.org/products/adatofsims-example-001",
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
            "schema:name": "ToF-SIMS",
            "schema:termCode": "ToF-SIMS",
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
                "schema:affiliation": {
                    "@type": [
                        "schema:Organization"
                    ],
                    "schema:name": "NASA Johnson Space Center"
                },
                "schema:contactPoint": {
                    "@type": [
                        "schema:ContactPoint"
                    ],
                    "schema:email": "researcher@example.org"
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
        "schema:name": "Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS)",
        "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/ToF-SIMS"
    },
    "prov:wasGeneratedBy": [
        {
            "@type": [
                "prov:Activity",
                "schema:Action"
            ],
            "schema:identifier": "session-tof-sims-20260110-001",
            "schema:startDate": "2026-01-10T09:30:00",
            "prov:used": [
                {
                    "@type": [
                        "schema:Thing",
                        "schema:Product"
                    ],
                    "schema:additionalType": [
                        "nxs:BaseClass/NXinstrument",
                        "ada:ToF-SIMSInstrument"
                    ],
                    "schema:name": "Example ToF-SIMS Instrument",
                    "schema:identifier": "ex:instrument-tof-sims-001"
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
            "@id": "ex:adaToFSIMS-var-001",
            "@type": [
                "schema:PropertyValue",
                "cdi:InstanceVariable"
            ],
            "schema:name": "measurement_value",
            "schema:alternateName": [
                "ToF-SIMS primary measurement"
            ],
            "schema:description": "Primary measured quantity from Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS) analysis. This is example mock data for testing.",
            "schema:propertyID": [
                "https://ada.astromat.org/vocabulary/variables/tof-sims_primary"
            ],
            "schema:unitText": "counts",
            "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
            "cdi:role": "MeasureComponent",
            "cdi:simpleUnitOfMeasure": "counts"
        },
        {
            "@id": "ex:adaToFSIMS-var-002",
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
            "schema:name": "adaToFSIMS-ALH84001-archive.zip",
            "schema:description": "Archive containing ToF-SIMS data files and supplementary materials",
            "schema:contentUrl": "https://astromat.org/downloads/adatofsims-example-001.zip",
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
                    "@id": "ex:adaToFSIMS-file-001",
                    "@type": [
                        "ada:image",
                        "schema:ImageObject",
                        "schema:MediaObject"
                    ],
                    "schema:name": "ALH84001_ToF-SIMS_001.tif",
                    "schema:description": "ToF-SIMS data file for ALH 84001 thin section",
                    "schema:additionalType": [
                        "ada:TOFSIMSCollection"
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
                    "ada:componentType": "ada:TOFSIMSCollection"
                },
                {
                    "@id": "ex:adaToFSIMS-file-002",
                    "@type": [
                        "ada:document",
                        "schema:DigitalDocument",
                        "schema:MediaObject"
                    ],
                    "schema:name": "ALH84001_ToF-SIMS_methods.pdf",
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
        "@id": "ex:adaToFSIMS-metadata-001",
        "schema:about": {
            "@id": "ex:adaToFSIMS-example-001"
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
                "@id": "https://w3id.org/geochem/metadata/profiles/adaToFSIMS"
            },
            {
                "@id": "https://w3id.org/cdif/data_description/1.0"
            },
            {
                "@id": "https://w3id.org/cdif/provenance/1.0"
            },
            {
                "@id": "https://w3id.org/cdif/manifest/1.0"
            },
            {
                "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
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
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaToFSIMS/context.jsonld",
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
  "@id": "ex:adaToFSIMS-example-001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "ToF-SIMS Analysis of Meteorite ALH 84001 Fragment",
  "schema:description": "Example Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS) product metadata demonstrating all properties defined by the adaToFSIMS profile. Contains mock data for testing and validation.",
  "schema:additionalType": [
    "Time-of-flight secondary ion mass spectrometry (TOFSIMS)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.99999/adatofsims-example-001",
    "schema:url": "https://doi.org/10.99999/adatofsims-example-001"
  },
  "schema:url": "https://astromat.org/products/adatofsims-example-001",
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
      "schema:name": "ToF-SIMS",
      "schema:termCode": "ToF-SIMS",
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
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "NASA Johnson Space Center"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "researcher@example.org"
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
    "schema:name": "Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/ToF-SIMS"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-tof-sims-20260110-001",
      "schema:startDate": "2026-01-10T09:30:00",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:ToF-SIMSInstrument"
          ],
          "schema:name": "Example ToF-SIMS Instrument",
          "schema:identifier": "ex:instrument-tof-sims-001"
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
      "@id": "ex:adaToFSIMS-var-001",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "measurement_value",
      "schema:alternateName": [
        "ToF-SIMS primary measurement"
      ],
      "schema:description": "Primary measured quantity from Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS) analysis. This is example mock data for testing.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/tof-sims_primary"
      ],
      "schema:unitText": "counts",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "counts"
    },
    {
      "@id": "ex:adaToFSIMS-var-002",
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
      "schema:name": "adaToFSIMS-ALH84001-archive.zip",
      "schema:description": "Archive containing ToF-SIMS data files and supplementary materials",
      "schema:contentUrl": "https://astromat.org/downloads/adatofsims-example-001.zip",
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
          "@id": "ex:adaToFSIMS-file-001",
          "@type": [
            "ada:image",
            "schema:ImageObject",
            "schema:MediaObject"
          ],
          "schema:name": "ALH84001_ToF-SIMS_001.tif",
          "schema:description": "ToF-SIMS data file for ALH 84001 thin section",
          "schema:additionalType": [
            "ada:TOFSIMSCollection"
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
          "ada:componentType": "ada:TOFSIMSCollection"
        },
        {
          "@id": "ex:adaToFSIMS-file-002",
          "@type": [
            "ada:document",
            "schema:DigitalDocument",
            "schema:MediaObject"
          ],
          "schema:name": "ALH84001_ToF-SIMS_methods.pdf",
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
    "@id": "ex:adaToFSIMS-metadata-001",
    "schema:about": {
      "@id": "ex:adaToFSIMS-example-001"
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
        "@id": "https://w3id.org/geochem/metadata/profiles/adaToFSIMS"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
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

ex:adaToFSIMS-example-001 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Time-of-flight secondary ion mass spectrometry (TOFSIMS)",
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
    schema1:description "Example Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS) product metadata demonstrating all properties defined by the adaToFSIMS profile. Contains mock data for testing and validation." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:additionalType "RO-CRATE" ;
            schema1:contentUrl "https://astromat.org/downloads/adatofsims-example-001.zip" ;
            schema1:description "Archive containing ToF-SIMS data files and supplementary materials" ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaToFSIMS-file-001,
                ex:adaToFSIMS-file-002 ;
            schema1:name "adaToFSIMS-ALH84001-archive.zip" ;
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
            schema1:url "https://doi.org/10.99999/adatofsims-example-001" ;
            schema1:value "10.99999/adatofsims-example-001" ] ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://ada.astromat.org/vocabulary/techniques" ;
            schema1:name "ToF-SIMS" ;
            schema1:termCode "ToF-SIMS" ],
        "astromaterials",
        "meteorite" ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/ToF-SIMS" ;
            schema1:name "Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS)" ] ;
    schema1:name "ToF-SIMS Analysis of Meteorite ALH 84001 Fragment" ;
    schema1:subjectOf ex:adaToFSIMS-metadata-001 ;
    schema1:url "https://astromat.org/products/adatofsims-example-001" ;
    schema1:variableMeasured ex:adaToFSIMS-var-001,
        ex:adaToFSIMS-var-002 ;
    schema1:version "1.0" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-tof-sims-20260110-001" ;
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
                    schema1:additionalType "ada:ToF-SIMSInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-tof-sims-001" ;
                    schema1:name "Example ToF-SIMS Instrument" ] ] .

ex:adaToFSIMS-file-001 a schema1:ImageObject,
        schema1:MediaObject,
        ada:image ;
    schema1:additionalType "ada:TOFSIMSCollection" ;
    schema1:description "ToF-SIMS data file for ALH 84001 thin section" ;
    schema1:encodingFormat "image/tiff" ;
    schema1:name "ALH84001_ToF-SIMS_001.tif" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 10485760 ] ;
    spdx:checksum [ a spdx:Checksum ;
            spdx:algorithm "MD5" ;
            spdx:checksumValue "d41d8cd98f00b204e9800998ecf8427e" ] ;
    ada:componentType "ada:TOFSIMSCollection" .

ex:adaToFSIMS-file-002 a schema1:DigitalDocument,
        schema1:MediaObject,
        ada:document ;
    schema1:additionalType "ada:methodDescription" ;
    schema1:description "Method description document for this analysis" ;
    schema1:encodingFormat "application/pdf" ;
    schema1:name "ALH84001_ToF-SIMS_methods.pdf" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 524288 ] ;
    ada:componentType "ada:methodDescription" .

ex:adaToFSIMS-metadata-001 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct>,
        <https://w3id.org/geochem/metadata/profiles/adaToFSIMS> ;
    schema1:about ex:adaToFSIMS-example-001 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-01-15" ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:name "Astromat Data Archive" ;
            schema1:url "https://astromat.org" ] ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-01-15T12:00:00Z" .

ex:adaToFSIMS-var-001 a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "counts" ;
    schema1:alternateName "ToF-SIMS primary measurement" ;
    schema1:description "Primary measured quantity from Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS) analysis. This is example mock data for testing." ;
    schema1:name "measurement_value" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/variables/tof-sims_primary" ;
    schema1:unitText "counts" .

ex:adaToFSIMS-var-002 a cdi:InstanceVariable,
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
title: ADA ToF-SIMS Product Profile
description: Technique-specific profile for Time-of-Flight Secondary Ion Mass Spectrometry
  (ToF-SIMS) products. Extends the base ADA product profile with constraints on valid
  ToF-SIMS component types.
allOf:
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a ToF-SIMS product type identifier.
      contains:
        enum:
        - Time-of-flight secondary ion mass spectrometry (TOFSIMS)
        - Time-of-Flight Secondary Ion Mass Spectrometry
    schema:distribution:
      description: Distribution items for adaToFSIMS. Archive hasPart items must have
        ada:componentType from technique-specific or universal values.
      type: array
      items:
        type: object
        properties:
          schema:hasPart:
            items:
              type: object
              properties:
                ada:componentType:
                  anyOf:
                  - enum:
                    - ada:TOFSIMSCollection
                  - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaProduct/schema.yaml#/$defs/universalComponentType
    schema:subjectOf:
      properties:
        dcterms:conformsTo:
          contains:
            type: object
            properties:
              '@id':
                const: https://w3id.org/geochem/metadata/profiles/adaToFSIMS
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

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaToFSIMS/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaToFSIMS/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaToFSIMS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/profiles/adaProfiles/adaToFSIMS`

