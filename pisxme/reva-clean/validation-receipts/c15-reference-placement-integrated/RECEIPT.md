# Phase 24 integrated C15 reference placement repair — 2026-09-13

- Base: `59c8f9fc` (physical candidate `d7a8ddfa`)
- Scope: moved only the C15 `F.SilkS` reference field from local `(0,0)` to `(2,0)` mm to clear the C14 reference; no pads, vias, nets, copper, footprint anchors, rules, or schematic changed.
- Producer Light DRC: `377 violations / 499 unconnected` versus base `379 / 499`; remaining silk-overlap family reduced to zero, with no new class.
- Fresh integrated validation is required before acceptance.
- Fresh Light checkout from integrated commit `6bdc15f9`: DRC `377 / 499`, reproducing the producer result. Raw fresh report and stdout are retained here.
- Toolchain: KiCad Light 10.0.6, image `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`.
