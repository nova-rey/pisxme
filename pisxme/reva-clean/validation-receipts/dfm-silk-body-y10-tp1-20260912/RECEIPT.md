# Integrated DFM silkscreen body repair 2

- Base candidate: `4a712b69`.
- Scope: removed only the optional F.SilkS body rectangle for Y10 and circle for TP1, each intersecting solder-mask pads. References, pads, nets, copper, vias, outline, schematic, and rules were unchanged.
- Toolchain: KiCad Light 10.0.6, qualified image.
- Fresh DRC: 353 violations / 499 unconnected items (from 358/499); no electrical/connectivity change.
- Remaining silk, clearance, width, courtyard, edge, and model findings remain open.
