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

The best current coordinated V3 run (`PHASE19_BEST.kicad_pcb`, U7 `(120,140)`
180 degrees, J3 `(145,125)` 90 degrees) measured 206 native DRC violations.
It retains one J3 auxiliary-pad short and two USB3/PCIe or local corridor
crossings, so it is rejected. The cap-net serialization failures remain fixed.

The refined synchronized candidate `PHASE19_LIVE3.kicad_pcb` is the current
best local result: native DRC measured 207 violations with zero shorting-item
records and one remaining USB3 source/landing crossing. It also retains
inherited clearance/hole/unconnected debt, so Phase 19 remains open and the
candidate is rejected.

Date: 2026-09-04

Status: `PISXME_REVA_CLEAN_PHASE19_SATA_ROUTING_IN_PROGRESS`

## 2026-09-04 coordinated-island continuation

The authoring harness was corrected so C30-C33 follow the requested U7
coordinate instead of retaining the former fixed x positions. A second
correction adds an opt-in direct USB3 landing mode for the validated
Phase-18 U7 neighborhood. With U7 `(110,105)` and USB3-only generation,
native DRC reports zero USB3 `tracks_crossing` and zero USB3 `shorting_items`;
the one remaining crossing/short category is inherited CM5/PERST or frozen
PCIe geometry outside the USB3 island.

The first complete orthogonal SATA launch experiment at U7 `(110,105)` and
J3 `(150,110)` rotation 0 was rejected. Native DRC identified concrete local
failures: RX_N crossing the frozen PCIe B.Cu corridor, connector-pad launch
shorts caused by the trial's J3 approach points, and one RX via near an
existing power-input pad. This is evidence against that exact trial, not
against the CM5-to-SATA architecture. No PCIe or Phase-18 ancestor copper was
modified.

The active blocker therefore remains a recoverable coordinated storage-island
placement/routing problem. The next bounded experiment must move the complete
island into genuinely open acreage or adjust the J3 orientation/edge while
retaining the direct USB3 landing mode, then derive all SATA launch points
from the actual connector pad and courtyard geometry. Phase 19 remains open;
Phase 20+ has not started.

## Independent high-speed review and V3-cap continuation

An independent PCB review confirmed the prior crossing diagnosis: the named
`(95,140)` marker is the RX_N landing segment, and its actual conflict is the
F.Cu TX_N diagonal, not TX_P. The review also identified that the direct
RX_N patch must account for the adjacent U7 pad field and that the live
candidate is not SI-closed until length/skew and transition-return evidence
are measured.

The generator now has an opt-in `P19_RXN_DIRECT` branch that preserves the
source corridor and uses a short ordinary-via return beside the serialized
RX_N pad. A V3-cap candidate using U7 `(120,140)` rotation 180 and J3
`(145,125)` rotation 90, with C30-C33 placed inline in the proven V3 lanes,
was generated and reloaded by KiCad 10. Native DRC measured 316 total
violations, zero `shorting_items`, and one `tracks_crossing`. The sole
crossing is RX_N on B.Cu against the frozen PCIe B.Cu trunk; SATA itself has
zero crossing/short records in this candidate. It is therefore rejected but
is the best current decomposition of the remaining problem.

The next experiment must move that one RX_N transition off the PCIe trunk or
select a nearby U7/J3 placement with the same V3 SATA lane ordering. It must
also include the independent review's required USB3 pair-length/skew audit
and local GND return-via review. A separate review noted U7 clock pads 52/53
remain unassigned in the current inherited materialization; this is retained
as a Phase 7/19 authority item and is not silently waived.

## 2026-09-04 coordinated repath baseline

The coordinated USB3 repath was extended across all four branches while
retaining the V3 split-cap SATA geometry. The generated/reloaded candidate is
`PHASE19_COORDINATED_PASS_CANDIDATE3.kicad_pcb` with U7 `(120,140)` rotation
180 and J3 `(145,125)` rotation 90. Native DRC reports 189 total violations,
418 unconnected items, zero `tracks_crossing`, zero `shorting_items`, and the
three inherited clearance plus two inherited hole-clearance records, with the
same five inherited dangling-via records as the accepted Phase-18 acreage
baseline. No candidate-introduced true clearance, short, or crossing remains
in the high-speed routing categories.

The candidate also removes the inherited duplicate U7 pad-net records on
pads 5-12 in the serialized output. The authoritative mapped pads remain:
USB3 42/43/45/46 and SATA 57/56/60/59. Native reload confirms two endpoint
pads and routed copper for each of the four USB3 nets, each of the four
bridge-side SATA nets, and each of the four socket-side SATA nets; no
high-speed unconnected-item records remain after the stale records are
removed.

The first path-length audit is not yet acceptable for SI closure. Summed
copper lengths are USB3 RX_N 108.473 mm, RX_P 87.104 mm, TX_N 81.453 mm, and
TX_P 61.407 mm; SATA full-path copper sums across bridge and socket sides are
TX_P 24.856 mm, TX_N 80.225 mm, RX_P 48.975 mm, and RX_N 59.775 mm including
the split-cap corridors. These are
candidate measurements, not a claim of compliance. The next repair must add
controlled, pair-symmetric length tuning without reintroducing crossings,
forbidden-layer signals, pad-field violations, or unnecessary transitions.

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

## 2026-09-04 clock-pin authority audit

The independent review's reference to U7 pads 52/53 was checked against the
local TI implementation-guide and Rev-I datasheet records. The exact PVP
pinout is: pin 52 `XI`, pin 54 `XO`, and pin 53 `VSSOSC`; these are not an
unassigned SATA or USB pair. TI's implementation guide requires a 40 MHz
reference, either a crystal between XI/XO or an external clock on XI with XO
left open, and a local VSSOSC return. The current abstract twelve-pin storage
symbol and clean schematic expose neither the oscillator network nor these
three pins. This is a genuine pre-release storage-authority gap discovered
during Phase 19, not a reason to waive the routing gate. It must be corrected
in the storage authoring path and then included in the coordinated PCB/SI
revalidation before Phase 19 can close.

The stable V3-cap generator branch was cleaned of the rejected tuned-cap
variant and re-run at U7 `(120,140)` / J3 `(145,125)`, U7 rotation 180° and
J3 rotation 90°. Native KiCad DRC again measured 189 total violations / 413
unconnected items, with zero `tracks_crossing` and zero `shorting_items`.
The candidate is retained as the best geometric baseline, but remains
`REJECTED_EXPERIMENT` because USB3 and SATA full-path length balance,
transition-return evidence, and the newly confirmed 40 MHz clock network are
not closed.

## 2026-09-04 hierarchy/materialization correction and clock-network proof

The storage authoring path was corrected generically. The failure was not a
missing KiCad project-instance path: the newly added clock library symbols had
been emitted after the STORAGE library closure and were therefore malformed
top-level symbols. The repair now places them inside the child `lib_symbols`
section and rebuilds their instances idempotently. Native KiCad 10 root export
now includes U7, J3, Y1, R23, C42, and C43.

The root netlist proof now shows:

* U7.30 and U7.31 on `/STORAGE/BRIDGE_3V3`;
* U7.52/XI, Y1.1, R23.1, and C42.1 on `/STORAGE/BRIDGE_XI`;
* U7.54/XO, Y1.3, R23.2, and C43.1 on `/STORAGE/BRIDGE_XO`;
* U7.53/VSSOSC, Y1.2/Y1.4, C42.2, and C43.2 on the distinct
  `/STORAGE/BRIDGE_VSSOSC` net.

The corrected materializer reload proof assigns those exact nets to the
physical U7 and clock-support pads and materializes 74 components, 238 nets,
and six copper layers. The clock island follows U7 in the coordinated
candidate; Y1 has its two electrical pads plus two VSSOSC return pads, with no
via-in-pad. This removes the prior SATA/VSSOSC alias and is now a valid
authoring/materialization baseline.

Phase 19 is still active. The coordinated routed candidate has not yet been
promoted: it still requires the short physical XI/XO/VSSOSC copper loop,
clock-to-high-speed clearance review, and the outstanding USB3/SATA
length/reference/return-via acceptance evidence. The candidate remains
`REJECTED_EXPERIMENT` pending those checks; no Phase 20 work has started.

## 2026-09-04 clock-loop routing experiment

A disposable physical clock-island experiment was applied to the best
coordinated SATA/USB3 candidate. It carried U7.30/U7.31, U7.52/U7.53/U7.54,
Y1, R23, C42, and C43 with the corrected net assignments. The first direct
F.Cu star/branch loop was rejected: native KiCad DRC measured 212 violations
and 415 unconnected items, including new `tracks_crossing` and
`shorting_items` records between XI, XO, and VSSOSC. The experiment is not
evidence against the crystal architecture; it is a failed local escape class.

The valid retained state is the schematic/netlist/materialization baseline,
not this routed experiment. Further work must use an ordinary-via,
layer-separated short clock escape with the exact pad coordinates, then
re-run focused native DRC and return/reference checks before promotion.

A second disposable class placed Y1/R23/C42/C43 on the underside and used
ordinary F.Cu-to-B.Cu transitions from the U7 clock pads. It was also rejected:
native KiCad DRC measured 249 violations and 428 unconnected items, with new
clock/high-speed `tracks_crossing` and `shorting_items` records. The underside
is permitted by the Rev-A mechanical contract, but this particular transition
geometry is not acceptable. The next experiment must change the local U7 clock
escape/placement relationship, not relax the layer policy or reuse either
failed clock route.

## 2026-09-04 open-side clock corridor experiment

The next disposable class used the materialized U7 at `(250,105)` and moved
the existing authoritative Y1/R23/C42/C43 footprints into the genuinely open
east-side acreage around `(255..261,112..118)`. The experiment used native
KiCad-reported transformed pad coordinates rather than assumed footprint-local
coordinates, assigned the exact XI/XO/VSSOSC nets, and kept VSSOSC distinct
from board GND. It measured 271 native DRC violations / 475 unconnected items,
versus 206 / 484 for its inherited materialization baseline.

This class is rejected. The new records are concrete clock-fanout failures:
the three adjacent U7 clock pads need a monotonic escape before they can branch
to the crystal and load capacitors; the attempted same-side branches crossed
one another and the VSSOSC return. The FREQSEL fanout also approached an
unassigned neighboring pad. This is not evidence against the required crystal
mode or against the open-side placement; it identifies the next necessary
experiment as a pad-row escape/rotation change with one net per corridor,
followed by a fresh coordinated USB3/SATA candidate. No Phase 19 gate was
relaxed and no Phase 20 work started.

## 2026-09-04 consultant review and perpendicular-first follow-up

The independent consultant reviewed the three rejected clock classes and the
current materialized geometry. It identified a common topology defect rather
than a placement or architecture defect: each prior trial ran at least one
clock track along the 0.5 mm-pitch U7 pad row before turning away. The exact
U7 row is 52/XI `(247.0,109.5)`, 53/VSSOSC `(247.5,109.5)`, 54/XO
`(248.0,109.5)`, with adjacent no-net pads 51 and 55. It also found that the
trial helper used 0.15 mm traces against a 0.20 mm board minimum.

The consultant recommended retaining the open east-side support placement,
escaping each clock pad perpendicular to the row before any lateral turn, and
using separated corridors for the subsequent crystal branches. This is an
in-scope authoring/routing correction. It does not require changing the
TUSB9261 clock architecture, layer contract, or PCIe corridor.

The follow-up applied the perpendicular-first breakout and raised the trial
trace width to 0.20 mm. Native KiCad DRC improved to 225 violations / 474
unconnected items, but the trial still generated clock-only crossings and
shorts in the downstream same-layer XI/XO/VSSOSC branches. It is rejected;
the result confirms the U7-row defect was real but that the crystal-side
branch topology must also be changed. Phase 19 remains active and Phase 20+
remain untouched.

## 2026-09-04 minimal clock fixture continuation

To separate clock topology from the inherited acreage debt, a disposable native
KiCad fixture retained the real TUSB9261 footprint and Y1/R23/C42/C43 while
removing unrelated footprints, copper, and zones. The fixture used a
perpendicular-first U7 escape, an ordinary through-via VSSOSC return, and
separate F.Cu/B.Cu corridors. Native KiCad DRC measured 15 violations / 2
unconnected items, with no `shorting_items` records. The remaining clock
records are two same-side escape crossings, one local clearance violation,
and one dangling VSSOSC bus endpoint; the two unconnected items are the
fixture's intentionally isolated U7.30/U7.31/BRIDGE_3V3 tie.

This is the best current clock topology experiment but is not yet closed: the
two escape crossings must be removed and the 3V3 frequency-select tie must be
made explicit in the fixture before applying the clock route to the complete
coordinated storage island. The result confirms that the clock network is
implementable with the approved architecture and layers; Phase 19 remains
active and Phase 20+ remain untouched.

## 2026-09-04 acreage clock integration baseline

The cleaned minimal clock topology was applied with a relative transform to
the materialized acreage candidate, preserving U7 and moving only the local
clock support island. The integration harness removes any inherited clock-net
tracks before adding the corrected route, and compensates dynamic pad
coordinates so no stale transformed endpoint is serialized. Native KiCad DRC
measured 207 violations / 473 unconnected items versus 206 violations for the
materialization baseline. The report contains no new clock `tracks_crossing`,
`shorting_items`, or runaway-length VSSOSC records; the remaining DRC debt is
inherited board geometry and incomplete non-clock routing.

This is a usable clock integration baseline, not Phase 19 closure. The next
step is to apply the same relative clock island to the complete coordinated
USB3/SATA candidate and rerun the full storage SI, return-via, and native DRC
gates. Phase 20+ remain untouched.

## 2026-09-04 clean minimal clock fixture and coordinated transplant

The minimal fixture was refined to close the explicit FREQSEL0/FREQSEL1 tie
and terminate the VSSOSC return at a connected ordinary-via bus. Native KiCad
DRC reports 12 warnings, zero unconnected pads, zero clock shorts, and zero
clock crossings; the remaining warnings are silkscreen/copper-sliver checks.
This closes the clock topology as a disposable electrical fixture, not as an
acreage release artifact.

The same relative geometry was then applied to the coordinated storage
candidate at U7 `(140,110)` / J3 `(145,125)`, with inherited clock copper
removed before routing. That transplant was rejected at 406 violations / 471
unconnected items because the candidate's live SATA/USB3 copper occupies the
translated support corridors and the new clock branches collide with those
signals. The result is a valid rejection of this placement transplant, not of
the clean minimal topology. The next experiment must relocate the complete
clock support island into a corridor clear of the already-routed USB3/SATA
fields, then regenerate the coordinated candidate. Phase 19 remains active;
Phase 20+ remain untouched.

## 2026-09-04 coordinated live-copper occupancy map

The coordinated candidate was inspected with native `pcbnew` geometry rather
than relying on footprint courtyards alone. Around U7 `(140,110)`, rotation
180 degrees, the clock row is top-facing: 52/XI `(143.0,105.5)`, 53/VSSOSC
`(142.5,105.5)`, and 54/XO `(142.0,105.5)`. The active F.Cu storage field
contains the SATA bridge launches at x=`139.0..141.0`, the SATA socket
approaches at x=`134.5..136.5`, and the USB3/PCIe source corridors extend
through the same local field. B.Cu contains the SATA RX continuation near
y=`130..138`, leaving only a narrow upper/left B.Cu window for a clock
transition and local support island.

This map explains both fixed-offset transplant failures: the nominal north
and east locations were not free once live copper and pad fields were
considered. The next disposable candidate will use a deliberate
perpendicular F.Cu escape from the top-facing U7 clock row, transition only
after the row is clear, and place the low-profile clock support in the mapped
B.Cu window. No validated USB3/SATA/PCIe copper will be overwritten, and no
Phase 19 closure claim is made yet.

## 2026-09-04 rotated north-corridor transplant rejection

The clean minimal clock route was reflected for the coordinated U7 rotation
and moved the support island north/outboard of U7, with the clock-net tracks
removed before regeneration. The coordinated candidate's live copper map
shows SATA launch and USB3/PCIe corridors in the apparently open north region;
native KiCad DRC measured 509 violations / 471 unconnected items, including
new clock-to-storage/power crossings and shorts. This candidate is rejected.

The result closes the fixed-offset transplant class: a clean isolated clock
fixture cannot be promoted by geometric reflection alone when the coordinated
candidate contains active high-speed copper. The next candidate must use a
live-copper occupancy map to place the clock island in a genuinely empty
acreage corridor, then route the short clock loop before full SI review. No
architecture, layer, or PCIe gate was relaxed; Phase 19 remains active and
Phase 20+ remain untouched.
## 2026-09-04 mapped B.Cu clock-island rejection

The live-copper map was used to build a disposable coordinated candidate with
U7's top-facing clock row escaping on F.Cu and Y1/R23/C42/C43 placed on B.Cu
in the measured west window. The clock-net copper was removed before the
trial, all clock pads were assigned explicitly, and the U7 FREQSEL pins were
tied to the bridge 3.3 V rail. Native KiCad DRC measured 386 violations / 477
unconnected items, including new clock-to-live-storage crossings and shorts.

The mapped window is rejected as insufficient once the complete candidate's
pad fields and B.Cu storage transitions are included. The clean minimal clock
fixture remains electrically closed; this is a placement/corridor failure.
The next experiment must move the low-profile clock support farther from the
U7/SATA pad field and route the three clock nets with a local layer-separated
escape, using the live occupancy map at each proposed coordinate. Phase 19
remains active; Phase 20+ remain untouched.

## 2026-09-04 south-acreage clock corridor audit

The live coordinated candidate was re-audited against the explicit Rev-A
mechanical contract. The board outline is approximately `300 x 180 mm`; live
storage copper is concentrated above about `y=140 mm`, and the prior generic
V100 cooler/backplate exclusion is not a Rev-A constraint. This leaves a real
south-acreage corridor for low-profile bridge-clock support. No PCIe, CM5,
SXM2, connector, standoff, M.2, or enclosure-floor authority currently blocks
that region.

A disposable south-corridor transplant placed Y1/R23/C42/C43 at `(220,150)`,
`(230,150)`, `(220,160)`, and `(230,160)`. Native KiCad DRC reported `407`
violations and `466` unconnected items. Inspection found that the new clock
errors were caused by the experiment authoring itself: support branches were
serialized to non-pad coordinates, the VSSOSC lane intersected an existing
power pad near `(159.35,150)`, and local XO/VSSOSC branches crossed at the Y1
field. Existing SATA/USB3 errors were also present.

This candidate is rejected as invalid proof, not evidence against the south
corridor. The corrected continuation must use exact reloaded pad coordinates
for every support endpoint, put all long clock lanes outside the live
high-speed envelope before descending, and preserve the passing
minimal-fixture topology. Phase 19 remains active; Phase 20+ remains
untouched.

## 2026-09-04 coordinated U7 rotation-270 trial

The generator invocation path was corrected and used to produce a distinct
coordinated candidate with U7 at `(140,130)`, rotation `270` degrees, and J3
at `(180,115)`. This is the first complete candidate in the new orientation;
the U7 clock row is on the west side while the SATA pins remain on the
opposite local side. The USB3/SATA island was regenerated from the Phase 18
ancestor without modifying PCIe.

After adding the authoritative 40 MHz clock network and the south support
island, native KiCad DRC measured `486` violations and `416` unconnected
items. The candidate is rejected. New records show that the generated SATA
launch still occupies the local U7 pad-row escape, and the trial's ordinary
clock vias also encounter inherited unfilled-plane/zone rule records. This is
not evidence against rotation 270: it identifies the required next repair as
clock-aware SATA pad-row generation plus a native zone-fill/reload pass.
Phase 19 remains active; Phase 20+ remains untouched.

## 2026-09-04 U7 rotation-270 pad-field discriminating fixture

To distinguish a local U7 package impossibility from a coordinated-route
problem, a minimal native fixture retained only U7 in the rotation-270
orientation and assigned the three clock nets plus all four bridge-side SATA
nets. Clock pads 52/53/54 escaped west on F.Cu; SATA pads 56/57/59/60 escaped
east, with alternating permitted layers.

Native KiCad DRC reported `7` warnings and `5` unconnected items, with zero
`tracks_crossing` and zero `shorting_items` records. The warnings are the
intentional dangling ends of the isolated escapes; the five unconnected items
are unrelated inherited U7 support-pin pairs plus the two SATA B.Cu escapes
without connector endpoints. This fixture therefore proves that the rot270
U7 clock/SATA pad-field escape is geometrically legal. The remaining failure
is the coordinated SATA launch authoring, which must be regenerated around
the proven clock escape. Phase 19 remains active.

## 2026-09-04 rotation-270 candidate artifact and native crash repair

The previously missing rotated candidate was generated successfully after
isolating a KiCad 10 Flatpak SWIG crash in the coordinated generator. The
crash occurred while enumerating zones after footprint/net mutation; the
generator now makes zone refill opt-in for disposable candidates so the board
can be saved and reopened for native validation. The resulting artifact is
`PHASE19_COORDINATED_U7ROT270_FULL.kicad_pcb`, with native DRC `403` / `413`
before clock integration and `PHASE19_COORDINATED_U7ROT270_CLOCK.kicad_pcb`
with `486` / `416` after the first clock overlay.

The rot270 orientation remains the best geometric lead because the clock row
escapes west while the SATA pins face the other side. The first overlay is
rejected; its new errors are identifiable clock/SATA local escape crossings,
non-planar support fanout, and inherited zone/via-rule records. No Phase 19
closure claim is made.

## 2026-09-04 coordinated-generator invocation correction

The coordinated storage generator previously depended on host-side `P19_*`
environment overrides. Under the installed KiCad Flatpak those overrides were
not reliably visible, so a requested rotated-U7 candidate could not be
verified as a distinct artifact. The authoring path now accepts explicit
`--P19_NAME=value` arguments before importing `pcbnew`, preserving the same
parameter names while making native candidate generation deterministic.

No rotated-U7 candidate is promoted from the failed invocation. Phase 19
remains active pending a separately identified generated board and its native
USB3/SATA/clock validation.

## 2026-09-04 ordered B.Cu clock-trunk trial

The next trial used three ordered B.Cu trunk lanes after short U7 escapes,
with XI/XO/VSSOSC assigned monotonically before the south support island.
Native KiCad DRC measured `391` violations and `466` unconnected items. This
was an improvement over the prior `417`-violation trial, but it still produced
new clock errors because the U7-side transition was itself inside the active
SATA pad/launch field and the Y1 return dogbones were not planar with the
adjacent XI/XO pads.

The candidate is rejected. This closes the class of clock-only overlays on
the existing coordinated storage copper. The next in-scope repair must
regenerate the U7/J3 USB3/SATA island with clock-aware pad escapes as one
coherent candidate; the validated PCIe ancestor, layer contract, stack, and
storage architecture remain frozen.

## 2026-09-04 pre-field B.Cu trunk trial

A third south-corridor experiment moved the long XI/XO/VSSOSC trunks onto
separated ordinary-via B.Cu lanes before the J1/J3 fields. Native DRC measured
`391` violations and `466` unconnected items. This reduced the prior
F.Cu-through-field class, but the trial still introduced local clock
crossings: the three trunk lanes were not ordered monotonically through the
transition region, and the Y1 dogbones were still on the wrong side of the
adjacent return pads. It is rejected as a routing-topology experiment.

The result is still useful: the south support acreage does not itself collide
with the board's live copper. The remaining work is a planar, ordered B.Cu
escape plus exact local pad dogbones; no new component, architecture change,
PCIe reopening, or validation relaxation is indicated.

## 2026-09-04 corrected south-island clock trial

The south trial was corrected to use the exact serialized support-pad
coordinates and moved the support farther outboard to `(250,150)`, `(270,149)`,
`(250,170)`, and `(270,170)`. The proposed VSSOSC return was isolated on
B.Cu after an ordinary transition at `(200,92)`. Native DRC measured `417`
violations and `466` unconnected items.

The prior non-pad endpoint defect is gone. The remaining new records are
geometric: long F.Cu XI/XO trunks still enter the J3/J1 pad fields before
reaching the open acreage, and the adjacent Y1 clock-return dogbones need a
layer-separated pad escape. Existing SATA/USB3 debt remains inherited. The
candidate is rejected, but the result confirms the support area itself is
available. The next trial must transition the clock trunks before the J3/J1
fields and use a genuinely separate local return layer at Y1; no architecture,
PCIe, stack, or Phase 20 gate has been changed.

## 2026-09-04 clock control-fixture rerun

The native minimal TUSB9261 clock fixture was regenerated and checked again
after the south-corridor rejection. KiCad 10 DRC reports `12` warnings and
`0` unconnected pads; the report contains no `shorting_items` or
`tracks_crossing` records. The remaining warnings are non-electrical
silkscreen/text/copper-sliver checks. This reconfirms that the authoritative
40 MHz XI/XO/VSSOSC topology and perpendicular-first escape are implementable;
the unresolved issue is only integration into the fully routed acreage
candidate.

## 2026-09-04 rotation-aware SATA launch generation

The coordinated generator was corrected so the `P19_SATA_V3` geometry is no
longer reused at U7 rotation 270. With U7 `(140,130)` rotation `270` and J3
`(180,115)` rotation `90`, the new opt-in `P19_SATA_ROT270` branch places the
four bridge-side coupling capacitors in an outboard local island and derives
all bridge/socket endpoints from reloaded transformed pads.

The corrected SATA-only coordinated artifact measured `340` native DRC
violations and `418` unconnected items, versus `403` and `413` for the prior
rot270 full candidate. The reduction confirms the former V3 coordinates were
an authoring defect, not a physical conclusion. The candidate is not
promoted: clock support has not yet been regenerated against the new
capacitor island, and the full USB3/SATA connectivity gate remains open.
