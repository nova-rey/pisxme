# Phase 24 integrated C14 reference placement repair — 2026-09-13

- Base: `769eb0b5` (physical candidate `d7a8ddfa`)
- Scope: moved only the C14 `F.SilkS` reference field from local `(0,0)` to `(6,0)` mm, placing it outside the J7 CM5 outline; no pads, vias, nets, copper, footprint anchors, rules, or schematic changed.
- Producer Light DRC: `379 violations / 499 unconnected` versus base `382 / 499`; silk-over-copper reduced 67→66 and silk-overlap reduced 3→1, with no new class.
- Fresh integrated validation is required before acceptance.
- Fresh Light checkout from integrated commit `be2fc476`: DRC `379 / 499`, reproducing the producer result. Raw fresh report and stdout are retained here.
- Toolchain: KiCad Light 10.0.6, image `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`.
