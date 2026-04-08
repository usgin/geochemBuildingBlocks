#!/usr/bin/env python3
"""Convert Concord Glass EPMA workbook to method definition JSON-LD."""
import sys, json, openpyxl
sys.stdout.reconfigure(encoding="utf-8")

wb = openpyxl.load_workbook(
    "G:/My Drive/OneGeochemistry/AnalyticalMethodTemplates/"
    "2088-1_ConcordEPMA_Glass_METHOD_1-0_6_final_.xlsx",
    data_only=True,
)
ws1 = wb["EPMA-SEM Part 1"]
ws2 = wb["EPMA-SEM Part 2"]

p1 = {cell.column: cell.value for cell in ws1[8] if cell.value is not None}

analytes = []
for row in ws2.iter_rows(min_row=8, max_row=30, values_only=False):
    vals = {cell.column: cell.value for cell in row if cell.value is not None}
    if 2 in vals and str(vals[2]).strip():
        analytes.append(vals)

defn = {
    "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6",
    "@type": ["ada:MethodDefinition", "schema:HowTo"],
    "schema:name": str(p1.get(4, "")),
    "schema:version": "1.0.6",
    "schema:datePublished": str(p1.get(5, ""))[:10] if p1.get(5) else "",
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
            "schema:name": "ARL",
        },
        "schema:model": {
            "@type": ["schema:ProductModel"],
            "schema:name": "SEMQ",
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
            "ada:dataType": "number",
            "schema:value": p1.get(14, 15),
            "schema:unitText": "kV",
            "ada:tier": "M",
            "ada:cdifPropertyPath": "cdifProvActivity: schema:additionalProperty",
        },
        {
            "schema:name": "beamCurrent",
            "schema:alternateName": "Beam Current",
            "ada:scope": "constant",
            "ada:category": "Beam Conditions",
            "ada:dataType": "number",
            "schema:value": p1.get(15, 6),
            "schema:unitText": "nA",
            "ada:tier": "M",
            "ada:cdifPropertyPath": "cdifProvActivity: schema:additionalProperty",
        },
        {
            "schema:name": "beamDiameter",
            "schema:alternateName": "Beam Diameter",
            "ada:scope": "default",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:value": str(p1.get(16, "")),
            "ada:tier": "M",
            "ada:cdifPropertyPath": "cdifProvActivity: schema:additionalProperty",
        },
        {
            "schema:name": "matrixCorrectionModel",
            "schema:alternateName": "X-ray Matrix Corrections",
            "ada:scope": "constant",
            "ada:category": "Data Processing",
            "ada:dataType": "string",
            "schema:value": str(p1.get(25, ""))[:200],
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
            "schema:name": "beamDamageMinimization",
            "schema:alternateName": "Beam Damage Minimization",
            "ada:scope": "constant",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:value": str(p1.get(23, ""))[:300],
            "ada:tier": "R",
            "ada:cdifPropertyPath": "cdifProvActivity: schema:additionalProperty",
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
            "schema:name": "additionalNotes",
            "schema:alternateName": "Additional Notes",
            "ada:scope": "constant",
            "ada:category": "General",
            "ada:dataType": "string",
            "schema:value": str(p1.get(26, ""))[:500],
            "ada:tier": "O",
            "ada:cdifPropertyPath": "cdifProvActivity: schema:additionalProperty",
        },
    ],
    "ada:analyteTemplate": {
        "ada:analyteColumns": [
            {"schema:name": "analysedOxide", "schema:alternateName": "Analysed Oxide/Element", "ada:scope": "default", "ada:dataType": "string", "ada:tier": "M", "ada:cdifPropertyPath": "cdifVariableMeasured: cdi:name"},
            {"schema:name": "beamCurrent", "schema:alternateName": "Beam Current (nA)", "ada:scope": "default", "ada:dataType": "number", "schema:unitText": "nA", "ada:tier": "M", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "spectrometer", "schema:alternateName": "Spectrometer", "ada:scope": "default", "ada:dataType": "string", "ada:tier": "R", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "sequence", "schema:alternateName": "Sequence", "ada:scope": "default", "ada:dataType": "integer", "ada:tier": "R", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "diffractingCrystal", "schema:alternateName": "Diffracting Crystal", "ada:scope": "default", "ada:dataType": "string", "ada:tier": "M", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "detectorType", "schema:alternateName": "Detector Type", "ada:scope": "default", "ada:dataType": "string", "ada:tier": "R", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "xrayLine", "schema:alternateName": "X-ray Line", "ada:scope": "default", "ada:dataType": "string", "ada:tier": "M", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "peakCountingTime", "schema:alternateName": "Peak Counting Time (s)", "ada:scope": "default", "ada:dataType": "string", "schema:unitText": "seconds", "ada:tier": "M", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "backgroundMethod", "schema:alternateName": "Background Method", "ada:scope": "default", "ada:dataType": "string", "ada:tier": "M", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "backgroundCountingTime", "schema:alternateName": "Background Counting Time (s)", "ada:scope": "default", "ada:dataType": "number", "schema:unitText": "seconds", "ada:tier": "M", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "phaSettings", "schema:alternateName": "WDS PHA Setting", "ada:scope": "default", "ada:dataType": "string", "ada:tier": "R", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "calibrationStandardName", "schema:alternateName": "Calibration Standard Name", "ada:scope": "default", "ada:dataType": "string", "ada:tier": "M", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "normalizationMethod", "schema:alternateName": "Normalization Method", "ada:scope": "optional", "ada:dataType": "string", "ada:tier": "O", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "normalizationStandards", "schema:alternateName": "Normalization Standards", "ada:scope": "optional", "ada:dataType": "string", "ada:tier": "O", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "detectionLimit", "schema:alternateName": "Detection Limit", "ada:scope": "optional", "ada:dataType": "number", "ada:tier": "R", "ada:cdifPropertyPath": "qualityMeasure: dqv:QualityMeasurement"},
            {"schema:name": "detectionLimitUnit", "schema:alternateName": "Detection Limit Unit", "ada:scope": "optional", "ada:dataType": "string", "ada:tier": "R", "ada:cdifPropertyPath": "schema:additionalProperty"},
            {"schema:name": "detectionLimitMethod", "schema:alternateName": "Detection Limit Method", "ada:scope": "optional", "ada:dataType": "string", "ada:tier": "R", "ada:cdifPropertyPath": "schema:additionalProperty"},
        ],
        "ada:defaultAnalytes": [],
    },
}

# Populate analytes
for a in analytes:
    row = {"analysedOxide": str(a.get(2, "")).strip()}
    if 4 in a: row["beamCurrent"] = a[4]
    if 5 in a: row["spectrometer"] = str(a[5])
    if 6 in a: row["sequence"] = a[6]
    if 7 in a: row["diffractingCrystal"] = str(a[7])
    if 8 in a: row["detectorType"] = str(a[8])
    if 9 in a: row["xrayLine"] = str(a[9])
    if 10 in a: row["peakCountingTime"] = str(a[10])
    if 11 in a: row["backgroundMethod"] = str(a[11])
    if 12 in a: row["backgroundCountingTime"] = a[12]
    if 13 in a: row["phaSettings"] = str(a[13])
    if 16 in a: row["calibrationStandardName"] = str(a[16])
    if 24 in a: row["normalizationMethod"] = str(a[24])
    if 25 in a: row["normalizationStandards"] = str(a[25])
    if 27 in a: row["detectionLimit"] = a[27]
    if 28 in a: row["detectionLimitUnit"] = str(a[28])
    if 29 in a: row["detectionLimitMethod"] = str(a[29])
    defn["ada:analyteTemplate"]["ada:defaultAnalytes"].append(row)

outpath = (
    "C:/Users/smrTu/OneDrive/Documents/GithubC/USGIN/geochemBuildingBlocks/"
    "_sources/geochemProperties/methodDefinition/examples/"
    "concord-glass-v1-0-6.json"
)
with open(outpath, "w", encoding="utf-8") as f:
    json.dump(defn, f, indent=2, ensure_ascii=False)

print(f"Wrote {len(defn['ada:analyteTemplate']['ada:defaultAnalytes'])} analytes")
print(f"Wrote {len(defn['ada:methodParameters'])} method parameters")
