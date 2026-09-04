# Phase 19 SATA routing blocker (active, non-terminal)

## 2026-09-04 coordinated storage authoring repair

The coordinated-island generator was corrected after a KiCad 10 serialization
audit. The Phase 18 donor reuses C30-C33 for unrelated regulator capacitors;
the generator now removes those donor footprints and loads the project-local
0402 footprints. It also assigns explicit net codes and attaches the new
socket-side nets before synchronization reload, preserving the intended
C30-C33/J3 split mapping.

Disposable candidate U7 `(150,140)` / J3 `(180,125)` completed generation and
serialized the expected four SATA socket nets, but native DRC measured 262
violations. Candidate-introduced SATA launch crossings/shorts and inherited
CM5/PERST interactions remain, so this candidate is rejected. Evidence is in
`PHASE19_COORDINATED_STORAGE_REPAIR_RECEIPT.md`; Phase 19 remains active and
no Phase 20+ work has started.

Follow-up USB3 escape refinement reduced the USB-only V3 disposable report to
200 native DRC violations by approaching the moved U7 row horizontally, but
it still crosses inherited CM5/PCIe source-corridor geometry and is rejected.
This remains a coordinated storage-island routing experiment, not a Phase 19
closure claim.

Date: 2026-09-04

Status: `PISXME_REVA_CLEAN_PHASE19_SATA_ROUTING_IN_PROGRESS`

## Current evidence

### 2026-09-04 continuation: SATA coupling network implemented

The earlier missing-implementation finding has been corrected generically in
`phase7_storage.py` and checkpointed at `db574ab`. Native KiCad 10 child-netlist
export now proves four separate paths:

| Bridge-side | Part | Socket-side |
| --- | --- | --- |
| `BRIDGE_SATA_TX_P` | C30 `GRM155R71C104KA88D`, 100 nF, 0402 | `SATA_M2_TX_P` → J3 pad 1 |
| `BRIDGE_SATA_TX_N` | C31 `GRM155R71C104KA88D`, 100 nF, 0402 | `SATA_M2_TX_N` → J3 pad 2 |
| `BRIDGE_SATA_RX_P` | C32 `GRM155R71C104KA88D`, 100 nF, 0402 | `SATA_M2_RX_P` → J3 pad 3 |
| `BRIDGE_SATA_RX_N` | C33 `GRM155R71C104KA88D`, 100 nF, 0402 | `SATA_M2_RX_N` → J3 pad 4 |

The PCB materializer loads four matching footprints and native DRC confirms
they are represented as physical pads. This closes the schematic/netlist
implementation gap, but not the Phase 19 routing gate: the coordinated PCB
generator still needs to route both sides of every capacitor and then prove
the full U7→C30-C33→J3 channel.

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

Cross-class coordinated trial: used the SATA V3 candidate as the input board
and regenerated USB3 after the native pad-coordinate synchronization fix.
`ACREAGE_PHASE19_STORAGE_V3_USB_REGEN.kicad_pcb` measured 226 native DRC
violations / 426 unconnected, with SATA/USB3 crossings and pad-field
interactions. Rejected; the SATA V3 geometry cannot simply be combined with
the regenerated USB3 path.

Orientation sweep continuation: U7/J3 rotations at `(150,140)/(190,140)`
and `(145,135)/(190,135)` measured 277/415 and 265/408 native DRC
violations respectively. Rotation-only classes are rejected; the coupled
U7 pad-field escape remains the active engineering issue.

Direct-F.Cu USB3 isolation trial: with SATA tracks removed from the corrected
U7 `(140,130)` candidate, native DRC measured 211 violations / 430
unconnected. Three candidate-introduced failures were shorts against the
regulator support island and one crossing against the frozen PCIe B.Cu field.
This identifies the next local repair target; no PCIe architecture change is
implied.

Exact-source USB3 follow-up: preserving the Phase 18 CM5 escape layering and
using a direct local F.Cu detour to U7 `(140,130)` reduced the isolated USB3
candidate to 202 violations / 430 unconnected, with no new USB3 short or
crossing category. The complete east-edge SATA trial at J3 `(240,140)` was
then rejected at 228 violations / 426 unconnected because its SATA launch
still crosses/shorts at the connector and U7 field. Phase 19 remains active.

Specialist-recommended orientation trial: U7 `(170,140)`, rotation `90°`,
with J3 `(205,120)`, rotation `90°`, was implemented with an orientation-aware
horizontal USB pad-row escape. Native DRC measured 378 violations / 426
unconnected and was rejected. The recommendation remains useful: its
placement clears the C19/PERST area, but the current SATA launch and remaining
local support interactions require another coordinated route.

Valid reuse check: SATA regeneration was disabled and only USB3 was reauthored
on the existing V3 SATA board. The resulting candidate measured 242 native DRC
violations / 426 unconnected and retained four USB3 short/crossing findings
against preserved V3 copper. Simple overlay reuse is rejected; a fresh
coordinated route remains required.

The TI implementation-guide review also found an open implementation gap:
four inline SATA AC-coupling capacitors (one per conductor, 0402 or smaller,
symmetrically close to J3; no C-pack) are absent from `STORAGE.kicad_sch`.
This is recorded in `PHASE19_SATA_AC_CAP_RECEIPT.md`. Phase 19 cannot close
until the authoritative schematic/netlist and routed capacitor network exist.

Transform audit: the unblocker-recommended U7 `(120,140)` `90°` candidate
was serialized and inspected. KiCad 10 actually places its USB row at
`y=135.5` and SATA row at `x=124.5`; the earlier predicted transform was
mirrored. The bottom-approach branch therefore entered the U7 body and
measured 219 USB-only DRC violations / 430 unconnected. It is rejected;
subsequent routing must use serialized pad coordinates directly.

Regulator-support reopening: translating only C18/C19 to `(100,145)/(108,145)`
on the U7 `(140,130)` USB3 isolation candidate removed the three prior
`BRIDGE_3V3` shorts. Native DRC remained 202 violations / 430 unconnected,
matching the Phase 18 baseline class apart from one local clearance. This
confirms the authorized coherent support move is electrically safe in the
disposable proof; complete Phase 19 remains gated by SATA launch geometry.
