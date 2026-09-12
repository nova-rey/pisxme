# Integrated C7/C8 reference-text DFM repair

- Base candidate: `5d73ca2a`.
- Scope: moved only F.SilkS reference fields for C7 and C8 by +2.5 mm in Y, away from their own pads. Pads, nets, copper, vias, outline, schematic, rules, and reference identities were unchanged.
- Toolchain: KiCad Light 10.0.6, qualified image.
- Fresh DRC: 351 violations / 499 unconnected items; zero shorting items.
- Remaining silk, clearance, width, courtyard, edge, and model findings remain open.
