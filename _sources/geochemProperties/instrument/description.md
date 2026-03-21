# ADA Analysis Instrument

Extends the core CDIF [instrument](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/instrument/) building block for ADA analytical instruments. Instruments are typed as `schema:Thing` + `schema:Product` (from core) with domain-specific classifications in `schema:additionalType` (e.g. `nxs:BaseClass/NXinstrument`, `ada:AMSInstrument`).

Inherits all core instrument properties: hierarchical sub-components via `schema:hasPart`, manufacturer, model, ownership, calibration properties, and linked resources.
