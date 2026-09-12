# Phase 24 integrated resistor reference text-height repair — 2026-09-13

- Base integrated candidate: `d7887899`
- Scope: reference fields of exactly 28 resistors (`R1-R6`, `R11-R14`, `R19-R24`, `R26-R33`, `R80-R83`) changed from 0.70 mm to 0.80 mm text size.
- No pads, vias, nets, copper, footprints, rules, or schematic files changed.
- Producer Light DRC: `395 violations / 499 unconnected` versus base `423 / 499`; the reduction equals the 28 text-height findings and introduced no new class.
- Fresh integrated validation is required before acceptance.
- Fresh Light checkout from integrated commit `75f8a101`: DRC `395 / 499`, reproducing the producer result. Raw fresh report and stdout are retained here.
- Toolchain: KiCad Light 10.0.6, image `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`.
