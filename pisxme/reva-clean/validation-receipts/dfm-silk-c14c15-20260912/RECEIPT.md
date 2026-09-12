# Integrated C14/C15 reference-text DFM repair

- Base candidate: `c1d995eb`.
- Scope: moved only C14 reference to local X=4 mm and C15 reference to local X=6 mm, away from adjacent pads. No pads, nets, copper, vias, outline, schematic, rules, or footprint geometry changed.
- Toolchain: KiCad Light 10.0.6, qualified image.
- Fresh DRC: 340 violations / 499 unconnected items; zero shorting items.
- Two silk findings removed; remaining DFM/electrical findings remain open.
