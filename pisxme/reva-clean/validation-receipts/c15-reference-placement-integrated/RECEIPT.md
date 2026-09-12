# Phase 24 integrated C15 reference placement repair — 2026-09-13

- Base: `59c8f9fc` (physical candidate `d7a8ddfa`)
- Scope: moved only the C15 `F.SilkS` reference field from local `(0,0)` to `(2,0)` mm to clear the C14 reference; no pads, vias, nets, copper, footprint anchors, rules, or schematic changed.
- Producer Light DRC: `377 violations / 499 unconnected` versus base `379 / 499`; remaining silk-overlap family reduced to zero, with no new class.
- Fresh integrated validation is required before acceptance.
