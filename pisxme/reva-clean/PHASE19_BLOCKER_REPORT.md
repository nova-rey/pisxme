# Phase 19 SATA routing blocker (active, non-terminal)

Date: 2026-09-04

Status: `PISXME_REVA_CLEAN_PHASE19_SATA_ROUTING_IN_PROGRESS`

## Current evidence

The closed Phase 18 CM5-to-U7 USB3 route remains valid at U7 `(110,105)`.
The coordinated moved-U7 experiment was rejected because regenerated USB3
escapes crossed the frozen PCIe field and U7 support pads. The J3-only trial
was also rejected: the selected rotated M.2 endpoint arrangement interleaved
the SATA groups with the fixed U7 launch and existing copper.

Native KiCad 10 DRC receipts:

| Candidate | Result | New failure class |
| --- | ---: | --- |
| `ACREAGE_PHASE19_STORAGE_MIDACREAGE_COORDINATED.kicad_pcb` | 232 violations / 426 unconnected | USB3/SATA endpoint crossings and pad-field shorts; inherited baseline separate |
| `ACREAGE_PHASE19_SATA_J3_ONLY.kicad_pcb` | 234 violations / 426 unconnected | J3 launch/endpoint crossings and shorts; inherited baseline separate |
| `ACREAGE_PHASE19_SATA_OUTBOARD_MONOTONIC.kicad_pcb` | 246 violations / 426 unconnected | fixed-board PCIe/reference intersections plus M.2 launch crossings; inherited baseline separate |
| `ACREAGE_PHASE19_STORAGE_MIDACREAGE_SATA_LAUNCH_V3.kicad_pcb` | 198 violations / 430 unconnected | no new short/crossing category; SATA-only proof, not coordinated-board closure |

The V3 result is useful evidence for a local SATA corridor, but is not
promoted because its moved U7 leaves the already-closed USB3 route stale.

The outboard trial kept U7 and USB3 unchanged and moved J3 to `(180,125)` at
rotation 0°. It still introduced crossings against the fixed reference field
and connector launch geometry, so it is rejected rather than treated as a
passing long detour.

## Next authorized continuation

Keep U7 and the Phase 18 USB3 route frozen. Continue with a bounded M.2
endpoint placement/orientation search, using the proven SATA V3 escape as the
starting geometry. Candidates must pass focused native DRC for all four SATA
nets, preserve 100-ohm ordinary F.Cu/B.Cu routing, and avoid plane-layer
signals, stubs, shorts, crossings, and connector/mechanical conflicts.

This is a recoverable progress packet, not terminal `BLOCKED`; Phase 20+ has
not started.
