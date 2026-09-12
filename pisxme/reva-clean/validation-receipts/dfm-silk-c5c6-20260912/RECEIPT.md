# Integrated C5/C6 reference-text DFM repair

- Base candidate: `098a4219`.
- Scope: moved only C5 reference to X=-3.0 mm and C6 reference to X=+3.0 mm, preserving identification. Pads, nets, copper, vias, outline, schematic, rules, and footprint geometry were unchanged.
- Toolchain: KiCad Light 10.0.6, qualified image.
- Fresh DRC: 344 violations / 499 unconnected items; zero shorting items.
- Four silk findings removed; remaining DFM/electrical findings remain open.
