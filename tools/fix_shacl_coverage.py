#!/usr/bin/env python3
"""One-time script to add missing optional SHACL shapes and fix severity issues."""

from pathlib import Path

BB_ROOT = Path(__file__).resolve().parent.parent / "_sources"

# Missing optional properties: { bb_relative_path: { property: (xsd_type_or_None, message) } }
MISSING = {
    "geochemProperties/creativeWork": {
        "schema:description": ("xsd:string", "Creative work should have a description."),
    },
    "geochemProperties/detailBasemap": {
        "schema:description": ("xsd:string", "Basemap detail should have a description."),
        "ada:channel1": ("xsd:string", "Basemap detail should specify channel1."),
        "ada:channel2": ("xsd:string", "Basemap detail should specify channel2."),
        "ada:channel3": ("xsd:string", "Basemap detail should specify channel3."),
    },
    "geochemProperties/detailL2MS": {
        "ada:massGate": ("xsd:boolean", "L2MS detail should specify massGate."),
        "ada:plasmaShutter": ("xsd:boolean", "L2MS detail should specify plasmaShutter."),
        "ada:timeDelayUnits": ("xsd:string", "L2MS detail should specify timeDelayUnits."),
        "ada:wavelengthUnits": ("xsd:string", "L2MS detail should specify wavelengthUnits."),
    },
    "geochemProperties/detailLAF": {
        "ada:sampleType": ("xsd:string", "LAF detail should specify sampleType."),
    },
    "geochemProperties/detailQRIS": {
        "ada:calibrationFile": ("xsd:string", "QRIS detail should specify calibrationFile."),
        "ada:pipelineVersion": ("xsd:string", "QRIS detail should specify pipelineVersion."),
        "ada:illuminationColor": (None, "QRIS detail should specify illuminationColor."),
        "ada:illuminationLevel": ("xsd:integer", "QRIS detail should specify illuminationLevel."),
        "ada:target": ("xsd:string", "QRIS detail should specify target."),
    },
    "geochemProperties/detailSLS": {
        "ada:countScans": ("xsd:integer", "SLS detail should specify countScans."),
        "ada:version": ("xsd:integer", "SLS detail should specify version."),
        "ada:watertight": ("xsd:boolean", "SLS detail should specify watertight."),
    },
    "geochemProperties/detailVNMIR": {
        "ada:beamsplitter": ("xsd:string", "VNMIR detail should specify beamsplitter."),
        "ada:calibrationStandards": ("xsd:string", "VNMIR detail should specify calibrationStandards."),
        "ada:comments": ("xsd:string", "VNMIR detail should specify comments."),
        "ada:eMaxFitRegionMax": ("xsd:string", "VNMIR detail should specify eMaxFitRegionMax."),
        "ada:eMaxFitRegionMin": ("xsd:string", "VNMIR detail should specify eMaxFitRegionMin."),
        "ada:emissionAngle": (None, "VNMIR detail should specify emissionAngle."),
        "ada:emissivityMaximum": ("xsd:string", "VNMIR detail should specify emissivityMaximum."),
        "ada:environmentalPressure": (None, "VNMIR detail should specify environmentalPressure."),
        "ada:incidenceAngle": (None, "VNMIR detail should specify incidenceAngle."),
        "ada:measurement": ("xsd:string", "VNMIR detail should specify measurement."),
        "ada:measurementEnvironment": ("xsd:string", "VNMIR detail should specify measurementEnvironment."),
        "ada:phaseAngle": (None, "VNMIR detail should specify phaseAngle."),
        "ada:sampleHeated": ("xsd:boolean", "VNMIR detail should specify sampleHeated."),
        "ada:samplePreparation": ("xsd:string", "VNMIR detail should specify samplePreparation."),
        "ada:sampleTemperature": ("xsd:integer", "VNMIR detail should specify sampleTemperature."),
        "ada:spectralRangeMax": ("xsd:string", "VNMIR detail should specify spectralRangeMax."),
        "ada:spectralRangeMin": ("xsd:string", "VNMIR detail should specify spectralRangeMin."),
        "ada:spectralSampling": ("xsd:string", "VNMIR detail should specify spectralSampling."),
        "ada:spotSize": ("xsd:string", "VNMIR detail should specify spotSize."),
        "ada:uncertaintyNoise": (None, "VNMIR detail should specify uncertaintyNoise."),
        "ada:vacuumExposedSample": ("xsd:boolean", "VNMIR detail should specify vacuumExposedSample."),
    },
    "geochemProperties/detailXCT": {
        "ada:beamFilterMaterial": ("xsd:string", "XCT detail should specify beamFilterMaterial."),
        "ada:beamFilterThickness": (None, "XCT detail should specify beamFilterThickness."),
        "ada:dataRangeLower": ("xsd:integer", "XCT detail should specify dataRangeLower."),
        "ada:dataRangeUpper": ("xsd:integer", "XCT detail should specify dataRangeUpper."),
        "ada:detectorGain": ("xsd:string", "XCT detail should specify detectorGain."),
        "ada:detectorBinning": ("xsd:string", "XCT detail should specify detectorBinning."),
        "ada:detectorSize": ("xsd:string", "XCT detail should specify detectorSize."),
        "ada:detectorType": ("xsd:string", "XCT detail should specify detectorType."),
        "ada:imageExposure": (None, "XCT detail should specify imageExposure."),
        "ada:imageFPS": ("xsd:string", "XCT detail should specify imageFPS."),
        "ada:imageGain": (None, "XCT detail should specify imageGain."),
        "ada:imageSize": ("xsd:string", "XCT detail should specify imageSize."),
        "ada:instrumentType": ("xsd:string", "XCT detail should specify instrumentType."),
        "ada:nsiBeamHardening": (None, "XCT detail should specify nsiBeamHardening."),
        "ada:numberOfFramesAveragedPerProjection": ("xsd:integer", "XCT detail should specify numberOfFramesAveragedPerProjection."),
        "ada:pixelPitch": ("xsd:string", "XCT detail should specify pixelPitch."),
        "ada:reconstructedDataFormat": ("xsd:string", "XCT detail should specify reconstructedDataFormat."),
        "ada:reconstructionSoftware": ("xsd:string", "XCT detail should specify reconstructionSoftware."),
        "ada:rotationAngle": ("xsd:string", "XCT detail should specify rotationAngle."),
        "ada:rotationType": ("xsd:string", "XCT detail should specify rotationType."),
        "ada:sourceToDetectorDistance": ("xsd:string", "XCT detail should specify sourceToDetectorDistance."),
        "ada:sourceToObjectDistance": (None, "XCT detail should specify sourceToObjectDistance."),
        "ada:subPixGrid": ("xsd:string", "XCT detail should specify subPixGrid."),
        "ada:subPixShift": ("xsd:string", "XCT detail should specify subPixShift."),
        "ada:xraySource": ("xsd:string", "XCT detail should specify xraySource."),
        "ada:xrayTargetMaterial": ("xsd:string", "XCT detail should specify xrayTargetMaterial."),
        "ada:xrayTubeCurrent": (None, "XCT detail should specify xrayTubeCurrent."),
        "ada:xrayTubePower": (None, "XCT detail should specify xrayTubePower."),
    },
    "geochemProperties/detailXRD": {
        "ada:sampleMount": ("xsd:string", "XRD detail should specify sampleMount."),
        "ada:timePerStep": (None, "XRD detail should specify timePerStep."),
    },
    "geochemProperties/image": {
        "ada:acquisitionTime": ("xsd:string", "Image should specify acquisitionTime."),
        "ada:channel1": ("xsd:string", "Image should specify channel1."),
        "ada:channel2": ("xsd:string", "Image should specify channel2."),
        "ada:channel3": ("xsd:string", "Image should specify channel3."),
        "ada:pixelSize": ("xsd:string", "Image should specify pixelSize."),
        "ada:illuminationType": ("xsd:string", "Image should specify illuminationType."),
        "ada:imageType": ("xsd:string", "Image should specify imageType."),
    },
    "geochemProperties/imageMap": {
        "ada:acquisitionTime": ("xsd:string", "ImageMap should specify acquisitionTime."),
        "ada:channel1": ("xsd:string", "ImageMap should specify channel1."),
        "ada:channel2": ("xsd:string", "ImageMap should specify channel2."),
        "ada:channel3": ("xsd:string", "ImageMap should specify channel3."),
        "ada:illuminationType": ("xsd:string", "ImageMap should specify illuminationType."),
        "ada:imageType": ("xsd:string", "ImageMap should specify imageType."),
        "ada:numPixelsX": ("xsd:integer", "ImageMap should specify numPixelsX."),
        "ada:numPixelsY": ("xsd:integer", "ImageMap should specify numPixelsY."),
        "ada:spatialRegistration": (None, "ImageMap should specify spatialRegistration."),
    },
    "geochemProperties/collection": {
        "ada:componentType": ("xsd:string", "Collection should specify componentType."),
        "ada:memberTypes": (None, "Collection should specify memberTypes."),
        "ada:nFiles": ("xsd:integer", "Collection should specify nFiles."),
        "ada:filelist": (None, "Collection should specify filelist."),
    },
    "geochemProperties/document": {
        "schema:version": ("xsd:string", "Document should specify version."),
        "schema:isBasedOn": ("xsd:string", "Document should specify isBasedOn."),
    },
    "geochemProperties/supDocImage": {
        "ada:numPixelsX": ("xsd:integer", "Supplemental doc image should specify numPixelsX."),
        "ada:numPixelsY": ("xsd:integer", "Supplemental doc image should specify numPixelsY."),
    },
    "geochemProperties/spatialRegistration": {
        "ada:basemap": ("xsd:string", "Spatial registration should specify basemap."),
        "ada:originZ": (None, "Spatial registration should specify originZ."),
        "ada:coordUnits": ("xsd:string", "Spatial registration should specify coordUnits."),
    },
    "geochemProperties/otherFile": {
        "ada:formatDescription": ("xsd:string", "Other file type should specify formatDescription."),
    },
}


def build_property_shape(prop, xsd_type, message):
    """Build a SHACL property shape block."""
    lines = [
        f"    sh:property [",
        f"        sh:path {prop} ;",
    ]
    if xsd_type:
        lines.append(f"        sh:datatype {xsd_type} ;")
    lines.extend([
        f"        sh:severity sh:Warning ;",
        f'        sh:message "{message}" ;',
        f"    ] ;",
    ])
    return "\n".join(lines)


def main():
    updated = 0
    total_shapes = 0

    for bb_path, props in MISSING.items():
        shacl_path = BB_ROOT / bb_path / "rules.shacl"
        if not shacl_path.exists():
            print(f"SKIP (no rules.shacl): {bb_path}")
            continue

        content = shacl_path.read_text(encoding="utf-8")
        new_shapes = []

        for prop, (xsd_type, msg) in props.items():
            # Skip if property already has a shape
            if f"sh:path {prop}" in content:
                continue
            new_shapes.append(build_property_shape(prop, xsd_type, msg))

        if not new_shapes:
            continue

        # Insert before the final .\n (the closing dot of the NodeShape)
        # Find the last occurrence of the shape-closing pattern
        stripped = content.rstrip()
        if stripped.endswith("."):
            stripped = stripped[:-1].rstrip()

        shapes_text = "\n".join(new_shapes)
        new_content = stripped + "\n" + shapes_text + "\n    .\n"

        shacl_path.write_text(new_content, encoding="utf-8")
        updated += 1
        total_shapes += len(new_shapes)
        print(f"Updated {bb_path}: added {len(new_shapes)} shapes")

    # Fix otherFile componentType severity: Warning -> Violation
    other_shacl = BB_ROOT / "geochemProperties/otherFile/rules.shacl"
    if other_shacl.exists():
        content = other_shacl.read_text(encoding="utf-8")
        # The componentType shape currently has no explicit severity (defaults to Violation)
        # but the audit says it's Warning. Let me check and fix.
        # Actually the audit said "required in schema but Warning in SHACL"
        # The encodingFormat has sh:severity sh:Warning but componentType doesn't have severity
        # so it defaults to Violation. The audit might be confused. Let me verify.
        if "sh:path ada:componentType" in content and "sh:severity" not in content.split("ada:componentType")[1].split("]")[0]:
            print("otherFile/ada:componentType already defaults to Violation (no explicit severity)")
        else:
            print("Note: check otherFile componentType severity manually")

    print(f"\nTotal: {updated} files updated, {total_shapes} shapes added")


if __name__ == "__main__":
    main()
