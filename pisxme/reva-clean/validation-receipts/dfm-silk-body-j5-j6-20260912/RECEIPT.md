# Integrated DFM silkscreen body repair

- Base candidate: `134e4c8a`.
- Scope: removed only the optional F.SilkS body rectangles for J5 and J6, each intersecting connector solder-mask pads. Reference fields, pads, nets, copper, vias, outline, schematic, and rules were unchanged.
- Producer/fresh Light: KiCad 10.0.6, image `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`.
- Fresh DRC: 358 violations / 499 unconnected items (from 364/499); no new electrical/connectivity classes observed.
- This candidate is ready for serialized integration review; remaining silk findings (Y10/TP1 and other classes) remain open.
