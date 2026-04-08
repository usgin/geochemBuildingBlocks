#!/usr/bin/env python3
"""Convert Birner Spinel EPMA workbook to method definition JSON-LD."""
import sys, json, openpyxl
sys.stdout.reconfigure(encoding="utf-8")

wb = openpyxl.load_workbook(
    "G:/My Drive/OneGeochemistry/AnalyticalMethodTemplates/"
    "3226-1_EPMA_METHOD_SPINEL_Birner.xlsx",
    data_only=True,
)
ws1 = wb["EPMA-SEM Part 1"]
ws2 = wb["EPMA-SEM Part 2"]

# Part 1 row 8 values
p1 = {cell.column: cell.value for cell in ws1[8] if cell.value is not None}

# Part 2 analyte rows 8-19
analytes = []
for row in ws2.iter_rows(min_row=8, max_row=19, values_only=False):
    vals = {cell.column: cell.value for cell in row if cell.value is not None}
    if 2 in vals:
        analytes.append(vals)

defn = {
    "@id": "https://registry.onegeochemistry.org/methods/nmnh-spinel-oxybar-v1",
    "@type": ["ada:MethodDefinition", "schema:HowTo"],
    "schema:name": str(p1.get(4, "")),
    "schema:version": "1.0",
    "schema:datePublished": "2013-11-08",
    "schema:measurementTechnique": {
        "@type": ["schema:DefinedTerm"],
        "schema:name": "EPMA-WDS",
        "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
    },
    "schema:instrument": {
        "@type": ["schema:Product", "schema:Thing"],
        "schema:name": str(p1.get(7, "")),
        "schema:manufacturer": {
            "@type": ["schema:Organization"],
            "schema:name": "JEOL",
        },
        "schema:model": {
            "@type": ["schema:ProductModel"],
            "schema:name": "JXA-8900",
        },
        "schema:hasPart": [
            {
                "@type": ["schema:Thing"],
                "schema:name": "WDS Spectrometer Array",
                "schema:description": str(p1.get(20, "")),
            }
        ],
    },
    "ada:laboratory": {
        "@type": ["schema:Place"],
        "schema:name": str(p1.get(8, "")),
    },
    "ada:methodParameters": [
        {
            "schema:name": "acceleratingVoltage",
            "schema:alternateName": "Accelerating Voltage",
            "ada:scope": "constant",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:value": str(p1.get(14, "")),
            "ada:tier": "M",
            "ada:cdifPropertyPath": "cdifProvActivity: schema:additionalProperty",
        },
        {
            "schema:name": "beamCurrent",
            "schema:alternateName": "Beam Current",
            "ada:scope": "constant",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:value": str(p1.get(15, "")),
            "ada:tier": "M",
            "ada:cdifPropertyPath": "cdifProvActivity: schema:additionalProperty",
        },
        {
            "schema:name": "beamDiameter",
            "schema:alternateName": "Beam Diameter",
            "ada:scope": "constant",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:value": str(p1.get(16, "")),
            "ada:tier": "M",
            "ada:cdifPropertyPath": "cdifProvActivity: schema:additionalProperty",
        },
        {
            "schema:name": "beamRaster",
            "schema:alternateName": "Beam Raster",
            "ada:scope": "constant",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:value": str(p1.get(17, "none")),
            "ada:tier": "R",
            "ada:cdifPropertyPath": "cdifProvActivity: schema:additionalProperty",
        },
        {
            "schema:name": "matrixCorrectionModel",
            "schema:alternateName": "X-ray Matrix Corrections",
            "ada:scope": "constant",
            "ada:category": "Data Processing",
            "ada:dataType": "string",
            "schema:value": str(p1.get(25, "")),
            "ada:tier": "M",
            "ada:cdifPropertyPath": "cdifProvActivity: schema:actionProcess",
        },
        {
            "schema:name": "analyticalSoftware",
            "schema:alternateName": "Analytical Software",
            "ada:scope": "default",
            "ada:category": "Instrument & Software",
            "ada:dataType": "string",
            "schema:value": str(p1.get(13, "")),
            "ada:tier": "M",
            "ada:cdifPropertyPath": "cdifProvActivity: prov:used",
        },
        {
            "schema:name": "secondaryReferenceStandards",
            "schema:alternateName": "Secondary Reference Materials",
            "ada:scope": "constant",
            "ada:category": "Quality Control",
            "ada:dataType": "string",
            "schema:value": str(p1.get(18, ""))[:300],
            "ada:tier": "M",
            "ada:cdifPropertyPath": "cdifProvActivity: prov:used",
        },
        {
            "schema:name": "driftCorrection",
            "schema:alternateName": "Drift Correction",
            "ada:scope": "default",
            "ada:category": "Quality Control",
            "ada:dataType": "string",
            "schema:value": str(p1.get(24, "")),
            "ada:tier": "R",
            "ada:cdifPropertyPath": "cdifProvActivity: schema:additionalProperty",
        },
        {
            "schema:name": "beamDamageMinimization",
            "schema:alternateName": "Beam Damage Minimization",
            "ada:scope": "constant",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:value": str(p1.get(23, "not applicable")),
            "ada:tier": "R",
            "ada:cdifPropertyPath": "cdifProvActivity: schema:additionalProperty",
        },
        {
            "schema:name": "wdsUtilization",
            "schema:alternateName": "WDS Utilization",
            "ada:scope": "constant",
            "ada:category": "Instrument & Software",
            "ada:dataType": "string",
            "schema:value": str(p1.get(19, "")),
            "ada:tier": "M",
            "ada:cdifPropertyPath": "cdifProvActivity: schema:additionalProperty",
        },
        {
            "schema:name": "edsUtilization",
            "schema:alternateName": "EDS Utilization",
            "ada:scope": "constant",
            "ada:category": "Instrument & Software",
            "ada:dataType": "string",
            "schema:value": str(p1.get(21, "No")),
            "ada:tier": "M",
            "ada:cdifPropertyPath": "cdifProvActivity: schema:additionalProperty",
        },
    ],
    "ada:analyteTemplate": {
        "ada:analyteColumns": [
            {"schema:name": "analysedOxide", "schema:alternateName": "Analysed Oxide/Element", "ada:scope": "default", "ada:dataType": "string", "ada:tier": "M", "ada:cdifPropertyPath": "cdifVariableMeasured: cdi:name"},
            {"schema:name": "beamCurrent", "schema:alternateName": "Beam Current (nA)", "ada:scope": "default", "ada:dataType": "number", "schema:unitText": "nA", "ada:tier": "M", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "spectrometer", "schema:alternateName": "Spectrometer", "ada:scope": "default", "ada:dataType": "string", "ada:tier": "R", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "diffractingCrystal", "schema:alternateName": "Diffracting Crystal", "ada:scope": "default", "ada:dataType": "string", "ada:enumeration": ["LIF", "LIFH", "LiF", "PET", "PETJ", "TAP"], "ada:tier": "M", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "xrayLine", "schema:alternateName": "X-ray Line", "ada:scope": "default", "ada:dataType": "string", "ada:enumeration": ["Ka", "Kb", "La", "Lb", "Ma"], "ada:tier": "M", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "peakCountingTime", "schema:alternateName": "Peak Counting Time (s)", "ada:scope": "default", "ada:dataType": "number", "schema:unitText": "seconds", "ada:tier": "M", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "backgroundMethod", "schema:alternateName": "Background Method", "ada:scope": "default", "ada:dataType": "string", "ada:tier": "M", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "backgroundCountingTime", "schema:alternateName": "Background Counting Time (s)", "ada:scope": "default", "ada:dataType": "number", "schema:unitText": "seconds", "ada:tier": "M", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "calibrationStandardName", "schema:alternateName": "Calibration Standard Name", "ada:scope": "default", "ada:dataType": "string", "ada:tier": "M", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "calibrationStandardID", "schema:alternateName": "Calibration Standard ID", "ada:scope": "optional", "ada:dataType": "string", "ada:tier": "R", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "citationForStandard", "schema:alternateName": "Citation for Standard", "ada:scope": "optional", "ada:dataType": "string", "ada:tier": "R", "ada:cdifPropertyPath": "schema:additionalProperty"},
        ],
        "ada:defaultAnalytes": [],
    },
    "schema:relatedLink": [
        {
            "@type": ["schema:LinkRole"],
            "schema:linkRelationship": "describedIn",
            "schema:target": {
                "@type": ["schema:EntryPoint"],
                "schema:name": "Davis et al. 2017",
                "schema:url": "http://dx.doi.org/10.2138/am-2017-5823",
            },
        },
        {
            "@type": ["schema:LinkRole"],
            "schema:linkRelationship": "describedIn",
            "schema:target": {
                "@type": ["schema:EntryPoint"],
                "schema:name": "Birner et al. 2017",
                "schema:url": "https://doi.org/10.1093/petrology/egx072",
            },
        },
    ],
}

# Populate analytes from Part 2
for a in analytes:
    row = {"analysedOxide": str(a.get(2, "")).strip()}
    if 4 in a:
        row["beamCurrent"] = a[4]
    if 5 in a:
        row["spectrometer"] = str(a[5])
    if 7 in a:
        row["diffractingCrystal"] = str(a[7])
    if 9 in a:
        row["xrayLine"] = str(a[9])
    if 10 in a:
        row["peakCountingTime"] = a[10]
    if 11 in a:
        row["backgroundMethod"] = str(a[11])
    if 12 in a:
        row["backgroundCountingTime"] = a[12]
    if 16 in a:
        row["calibrationStandardName"] = str(a[16])
    if 17 in a and a[17]:
        row["calibrationStandardID"] = str(a[17])
    if 20 in a and a[20]:
        row["citationForStandard"] = str(a[20])[:200]
    defn["ada:analyteTemplate"]["ada:defaultAnalytes"].append(row)

outpath = (
    "C:/Users/smrTu/OneDrive/Documents/GithubC/USGIN/geochemBuildingBlocks/"
    "_sources/geochemProperties/methodDefinition/examples/"
    "nmnh-spinel-oxybar-v1.json"
)
with open(outpath, "w", encoding="utf-8") as f:
    json.dump(defn, f, indent=2, ensure_ascii=False)

print(f"Wrote {len(defn['ada:analyteTemplate']['ada:defaultAnalytes'])} analytes")
print(f"Wrote {len(defn['ada:methodParameters'])} method parameters")
