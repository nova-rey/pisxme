# Phase 24 integrated U14 silkscreen repair — 2026-09-13

- Base: `21012812` (physical candidate `d7a8ddfa`)
- Scope: removed two U14 `F.SilkS` outline segments clipping its pad 1 (`JMS_VDDREG_5V`); regulator pads, nets, copper, footprint anchor, rules, and schematic unchanged.
- Producer Light DRC: `370 violations / 499 unconnected` versus base `372 / 499`; no new violation class.
- Fresh integrated validation is required before acceptance.
- Fresh Light checkout from integrated commit `b17f7f2d`: DRC `370 / 499`, reproducing the producer result. Raw fresh report and stdout are retained here.
- Toolchain: KiCad Light 10.0.6, image `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`.
