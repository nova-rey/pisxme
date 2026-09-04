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
| `ACREAGE_PHASE19_SATA_UNDERSIDE_ENDPOINT.kicad_pcb` | 243 violations / 430 unconnected | TX source/connector crossings, one frozen PCIe B.Cu intersection, and connector-hole clearance; inherited baseline separate |
| `ACREAGE_PHASE19_SATA_LOCAL_UNDERSIDE.kicad_pcb` | 244 violations / 430 unconnected | U7 pad-field conflicts, two local B.Cu pair crossings, and M.2 courtyard/clearance interactions; inherited baseline separate |
| `ACREAGE_PHASE19_STORAGE_MIDACREAGE_SATA_LAUNCH_V3.kicad_pcb` | 198 violations / 430 unconnected | no new short/crossing category; SATA-only proof, not coordinated-board closure |
| `ACREAGE_PHASE19_STORAGE_COORDINATED_FRESH.kicad_pcb` | 208 violations / 426 unconnected | regenerated USB3 source/landing crossings and local PERST/USB3 interactions; SATA V3 corridor retained |

The V3 result is useful evidence for a local SATA corridor, but is not
promoted because its moved U7 leaves the already-closed USB3 route stale.

The outboard trial kept U7 and USB3 unchanged and moved J3 to `(180,125)` at
rotation 0°. It still introduced crossings against the fixed reference field
and connector launch geometry, so it is rejected rather than treated as a
passing long detour.

The underside trial kept the same U7/USB3 ancestor and placed J3 on B.Cu at
`(180,125)`, rotation 0°. It reduced the top-side obstruction but its current
split-layer source/connector escape still crosses the frozen B.Cu field and
violates connector-hole clearance, so it is also rejected.

## Next authorized continuation

Keep U7 and the Phase 18 USB3 route frozen. Continue with a bounded M.2
endpoint placement/orientation search, using the proven SATA V3 escape as the
starting geometry. Candidates must pass focused native DRC for all four SATA
nets, preserve 100-ohm ordinary F.Cu/B.Cu routing, and avoid plane-layer
signals, stubs, shorts, crossings, and connector/mechanical conflicts.

Phase 20+ has not started. The authorized local endpoint/underside classes are
now exhausted. The user has explicitly authorized reopening the coherent U7/J3
storage island, including regeneration of both USB3 and SATA routing. The fresh
coordinated candidate at U7 `(120,140)` / J3 `(145,125)` is rejected as an
experiment, but demonstrates that the remaining failure is local USB3 landing
geometry rather than a reason to preserve the former U7 coordinate. Phase 19
remains active; further co-located island candidates will keep the PCIe
ancestor unchanged.

Generator-correction experiment: the USB3 source-side escapes were restored
to the validated Phase 18 geometry and the moved-U7 landing was made
coordinate-derived. An above-PCIe placement at U7 `(140,100)` / J3 `(180,90)`
was rejected by native DRC at 410 violations / 426 unconnected, including
PCIe interactions and local SATA shorts. This class is not promoted; the next
search remains in open acreage beside/below the validated PCIe corridor.

Placement-sweep continuation: U7/J3 `(140,140)/(170,125)` was the best
tested open-acreage class at 224 violations / 426 unconnected, but retained
real USB3/PERST and pair crossings. A coordinate-derived SATA-lane refinement
measured 229 / 426 and introduced local SATA lane crossings/shorts; it is
rejected. No PCIe geometry changed.

Native synchronization correction: after moving U7/J3, the generator now
serializes and reloads the board before reading transformed pad coordinates.
The corrected U7 `(140,130)` / J3 `(180,115)` candidate measured 227 native
DRC violations / 426 unconnected before SATA escape refinement; the next
escape refinement measured 229 / 426 and reintroduced SATA/USB3 crossings.
Both are rejected experiments. This closes the stale-pad-coordinate defect
in the experiment harness, not Phase 19.

Staged USB3 rail experiment: kept the synchronized U7 `(140,130)` / J3
`(180,115)` placement and moved each final vertical transition onto B.Cu
after an F.Cu staging hop. Native DRC remained 229 violations / 426
unconnected and reported new SATA/USB3 pair interactions; rejected. The next
continuation changes island orientation/relative placement rather than adding
another same-geometry rail variant.

Orientation sweep continuation: U7/J3 rotations at `(150,140)/(190,140)`
and `(145,135)/(190,135)` measured 277/415 and 265/408 native DRC
violations respectively. Rotation-only classes are rejected; the coupled
U7 pad-field escape remains the active engineering issue.
