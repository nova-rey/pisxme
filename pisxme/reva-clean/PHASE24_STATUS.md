# Phase 24 acreage validation status

Status: IN PROGRESS — native ERC and netlist pass; schematic↔PCB component
parity remains open.

## Protected 12 V plane experiment

The candidate stack defines `In3.Cu` as `In3.PROTECTED_12V`, but the current
board had no protected 12 V fill. A disposable full-acreage In3 fill was
tested with native refill and DRC. It introduced no shorting or crossing
records and reduced missing connections only from 397 to 395: unresolved
surface regulator/capacitor pads still require explicit physical launches.
The plane-only candidate is rejected as insufficient; the layer role remains
available for a launch-mapped power repair.

## Closed in this checkpoint

- The clean project now resolves all 34 custom symbols through the assembled
  `PiSXMe_RevA_Clean_complete.kicad_sym` library.
- `phase24_repair_root_hierarchy.py` generically replaces the malformed root
  interior/diagonal wiring with outward sheet-edge stubs and named root
  associations, preserving child UUIDs and sheet instances.
- The CM5 sheet border is extended where the legacy final pin was outside its
  rectangle.
- Two unused MIPI1 D2 pins are explicitly marked no-connect; they are outside
  the Rev A interface contract.
- Native KiCad 10.0.5 ERC with `--severity-error` reports `Found 0 violations`.
- `validation/phase3/test_phase24_native_final_authority.py` passes.

## Netlist closure

The warning was caused by four regulator 22 uF capacitors retaining stale
`(instances)` references C30–C33 after their symbol properties were renumbered.
`phase24_repair_duplicate_refs.py` updates both serialized representations to
C44–C47.  KiCad 10.0.5 now exports a non-empty netlist with no annotation
warning.

Artifacts: `PHASE24_NATIVE_ERC_FINAL2.rpt`, `PHASE24_NETLIST_FINAL5.xml`, and
the Phase 24 native-authority regression.

## Remaining parity repair

Fresh comparison of `PHASE24_NETLIST_FINAL5.xml` against
`PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb` found schematic components with no PCB
footprint: `Y1`, `R23`, `C42`, `C43`, and `C44`–`C47`.  These are real storage
clock and regulator support components, not optional debug artifacts.  The
first disposable clock graft was rejected because its historical hard-coded
U7 clock-row coordinates produced true shorts; it is retained only as failed
evidence.  Phase 24 stays open until a coordinate-derived, native-DRC-clean
materialization and parity check are complete.

The next coordinate-derived candidate, `PHASE24_SUPPORT_MATERIALIZED`, was
also rejected.  Its clock corridors crossed inherited SATA/USB copper and its
U5-side bulk-cap graft entered existing regulator pad/return geometry.  This
establishes that the missing support must be integrated by regenerating the
coordinated storage/regulator local routes, not by overlaying support copper
onto the Phase 23 ancestor.

The `PHASE19_RELOC_U270J190_COORD49_FULL` storage-only donor was then tested
as a coordinated transplant.  It contains USB3, SATA, and clock copper, but
its relocated USB3 corridor crosses the frozen V5 PCIe corridor after merge.
It was rejected.  The valid next class is to retain V5's proven U7/J3
high-speed placement and add an obstacle-aware clock route locally, followed
by a separately coordinated U5 bulk-cap island.

## Latest bounded experiment

`phase24_materialize_support_v2.py` generated `PHASE24_SUPPORT_V2.kicad_pcb`
from actual U7 pad coordinates, with the clock parts in open acreage and the
four schematic-authoritative U5 capacitors materialized. It was rejected by
native DRC (`234` violations, `409` unconnected items): the attempted common
B.Cu clock surface still crossed inherited SATA copper, crossed between clock
branches, and produced U7 pad-field shorts. This is not evidence against the
storage architecture. The next valid class is layer-separated clock fanout
with vias outside the U7 pad field, then an independent coherent U5
rail/return island. See `PHASE24_BLOCKER_REPORT.md`.

The first rotated-U7 discriminator was rejected as an authoring/tooling proof:
it changed U7 orientation but used a pre-rotation hard-coded clock endpoint
graph, producing pad mismatches. It is not a valid architecture failure. Any
next rotated-U7 experiment must query the post-rotation footprint and support
pad coordinates before creating tracks or vias.

The corrected rotated-U7 source-escape discriminator now derives post-rotation
U7 endpoints and produces zero native DRC `shorting_items` and
`tracks_crossing` records for the clock escape. It remains a disposable oracle
because the Y1/R23/C42/C43 branches and U5 C44-C47 island are not yet complete.

The latest bounded sweep (`phase24_clock_position_sweep.py`) improved the
clock-support search to a compact near-west underside candidate, but it still
has one localized B.Cu clock-lane crossing at the U7 escape. It remains an
unpromoted experiment; Phase 24 is still open.

The subsequent side-separated A* clock oracle reached zero clock-specific
crossing/shorting records in native DRC. A follow-on support materialization
was rejected at 240 native violations because the added Y1 passive branches
entered the crystal pad field and the C44--C47 placement overlapped existing
regulator support. The clock oracle is retained as evidence; support networks
must be placed and routed as independently bounded islands.

The native-orientation disposable fixture reports zero unconnected items,
shorts, crossings, and footprint errors, but it is not a complete support
topology: inspection shows that all passive branches are not routed to
R23/C42/C43. It remains a source-escape/footprint discriminator only. The
remaining work is a genuinely complete rot180 coordinate transplant plus a
separate U5 capacitor island.

The first strict complete-fixture implementation was rejected by native DRC
(24 violations: 5 crossings, 4 shorts, 8 disconnected pads). It is retained
as evidence that the next implementation must derive and reserve the actual
Y1 pad field rather than assume a generic three-bus geometry.

The subsequent launch-height refinement remained invalid (9 native DRC
violations, including 8 crossings). It is rejected; the next candidate must
use an obstacle-mapped proven support template.

The first obstacle-aware passive router found all six passive paths but was
rejected by native DRC (380 violations: 29 shorts and 13 crossings). The
remaining repair must regenerate the clock topology with branch reservations
before adding passive fanout.

The multi-net graph-anchor sweep found all six branch paths but was rejected
by native DRC (271 violations: 10 shorts and 4 crossings). The next repair
class is layer-separated passive dogbones with offset vias and short rail
joins.

A five-position coordinated-island sweep was also rejected: four placements
had no conservative route to a rail anchor and the best generated board had
322 native DRC violations. No candidate was promoted.

The rail-attachment variant was rejected by native DRC (268 violations: 12
shorts and 9 crossings). The remaining valid implementation class is a
single coordinated clock graph containing source escape, Y1, R23, C42, and
C43 before materialization.

Layer-separated passive dogbones with offset through-vias were also rejected
by native DRC (306 violations: 14 shorts and 6 crossings); four outboard
variants had no conservative path. A fresh coordinated clock graph is now
required for support integration.
The coordinated layer-owned disposable fixture now proves the complete
Y1/R23/C42/C43 clock-support graph: XI is carried on B.Cu, XO on F.Cu, and
VSSOSC on a separate B.Cu perimeter. Native DRC reports no clock crossings,
shorts, footprint errors, or clock unconnected records. Its eight remaining
unconnected records are deliberately isolated non-clock U7 pads in the
stripped fixture; acreage transplant and full Phase 24 parity remain open.
The first acreage support transplant was rejected: native DRC reported 218
violations, including clock-net crossings and a VSSOSC/XO short caused by
placing passive branches into inherited USB3 and clock corridors. This does
not invalidate the coordinated disposable topology. A separate U5 C44-C47
island trial has no shorting or crossing records, but retains inherited
unconnected/dangling cleanup and is not yet promoted.
The follow-up surface-only U5 support trial was also rejected: native DRC
reported 202 violations, including a rail/ground short and crossings. It is
not promoted; the U5 rail must be regenerated with a real return strategy and
clearance-aware source launch.
All eight previously missing schematic-authoritative references are now
materialized in the disposable `PHASE24_ALL_AUTHORITATIVE_PARTS` baseline.
The exact pad-net audit passes for Y1/R23/C42/C43/C44-C47. Native DRC reports
187 inherited violations and 406 unconnected pads, but no shorting or crossing
records; this closes the component-materialization discriminator only, not
routed Phase 24 closure.
The outboard U5 surface placement was rejected as the same failed solution
class: native DRC reported 203 violations, including a bridge-1V1/POWER_GND
short and crossings. Two surface-only placements have now failed; the next
repair must use a clearance-mapped ground-aware island rather than another
surface rail trunk.
The independent hardware audit confirms the eight-part materialization is
narrow evidence only: full-board parity, routing connectivity, source
ownership, and footprint-filter parity remain unproven. The ground-aware U5
V2 trial reduced the new problem to one localized rail/return crossing with
no new shorting record, but still has unconnected/inherited failures and is
not promoted. The next U5 repair must separate the source and return lanes by
layer or use a mapped return launch.
The latest U5 V2 source-escape refinement was rerun after moving the rail
launch around the regulator feedback corridor. Native DRC remains at 197
violations and 392 unconnected pads, with one source/return crossing and no
shorting record. It is retained as a rejected disposable result; the
ground-aware U5 island still needs a layer-separated source/return launch.
The current U5 V2 rerun uses a left-side source detour to avoid the feedback
segment, but native DRC still reports one crossing at the separate return
trunk and 392 unconnected pads. It remains a disposable negative result; no
production geometry has changed.
The stripped U5 layer fixture now proves the C44-C47 source/return topology:
ordinary through-vias launch 1V1 and POWER_GND, with separate B.Cu rail and
return corridors. Native DRC reports zero `shorting_items` and zero
`tracks_crossing`; its 499 unconnected records are deliberate non-target
fixture/U5 pads. This is a reusable topology oracle, not an acreage promotion.
The corrected U5 layer fixture was rerun after extending both layer-owned
trunks to the rotated capacitor pad rows. Native DRC still reports zero
shorting and zero crossing records; 499 unconnected pads are deliberate
non-target fixture/U5 pads. The separate graph-audit script exposed a
coordinate-join defect and is not used as closure evidence; acreage U5
integration remains open.
The U5 fixture regression audit now passes after correcting its serialized
via/track coordinate joins: all four C44-C47 rail pads connect to U5.9 and
all four return pads connect to R20.2. Native DRC remains zero shorts and zero
crossings for the fixture. This strengthens the topology proof only; acreage
integration and full-board parity remain open.
The PCB-only Ethernet alias filter removed CCT/CCT1-CCT4 and RCT1-RCT4 from
the materialized parity candidate. The candidate now contains all 78 native
schematic references plus only MECH_M2_2280 and TP1-TP13; the exact reference
set audit passes. Native DRC introduces no shorting or crossing records.
Electrical Ethernet return/support routing must still be reconciled before
this candidate can be promoted.
The filtered clean-reference candidate was revalidated after the alias removal:
the 78-reference audit still passes, and native DRC reports no shorting or
track-crossing records. It retains 201 DRC violations and 406 unconnected
pads, so it remains a parity/source candidate rather than a routed production
artifact.

## Integrated U5 layered launch

`phase24_u5_integrate_layered.py` applies the reviewed source/return topology
to the filtered acreage candidate using the existing authoritative C44-C47
footprints, ordinary through-vias, and refilled In1/In4 ground zones.
`phase24_u5_layer_connectivity_audit.py` passes: U5.9 joins C44-C47.1 and
R20.2 joins C44-C47.2. Native DRC reports 201 violations and 397 unconnected
pads, with zero `shorting_items` and zero `tracks_crossing`. This closes the
integrated U5 topology discriminator only; full Phase 24 routed parity remains
open.

## Rejected clock-oracle acreage transplant

`phase24_integrate_clock_oracle.py` attempted to transplant the proven
rotated-U7 clock copper from `PHASE19_PASS_CLOCK_ROT180_S20.kicad_pcb` onto
the integrated acreage candidate while reusing the existing Y1/R23/C42/C43
authoritative footprints. Native DRC rejected the overlay: 288 violations,
400 unconnected pads, multiple track crossings, and shorts between clock
nets and existing SATA/bridge copper. The standalone oracle remains valid;
its unmodified coordinate context cannot be overlaid onto this already-routed
acreage candidate. The experiment is retained as negative evidence, and its
KiCad via-width API call was corrected for reproducible reruns.

## Corrected clock-fixture transform rerun

The coordinate transform was corrected from the footprint-origin frame to the
serialized U7 pad frame: fixture U7.52 `(97,104.5)` maps to acreage U7.52
`(123,135.5)` under `x'=220-x, y'=240-y`. The rerun places the reused clock
footprints consistently and reproduces the fixture copper. It is still
rejected for acreage promotion: native DRC reports 227 violations, 393
unconnected pads, multiple crossings, and shorts between the clock return/XI
nets and existing SATA copper. This establishes that the proven clock topology
needs a locally regenerated corridor around the existing storage routes, not a
blind copper overlay.

## U5 physical-audit correction and negative controls

`phase24_u5_layer_connectivity_audit.py` was corrected to invoke KiCad's
native connectivity rebuild over serialized pads, tracks, vias, layers, nets,
and filled zones. Expected target membership is assertion-only; no synthetic
edges or XY-only nodes are used.
Against `PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb` it passes for U5.9 to
C44-C47.1 and R20.2 to C44-C47.2. The disposable negative-control harness
removes an actually required C44 rail dogbone trace in a copied board; the
control correctly makes the audit fail. This native component has no
necessary via, so no via-removal claim is made. Native DRC has no
target C44-C47 unconnected finding, while the remaining 397 unconnected pads
are outside this local proof and keep full Phase 24 open.

## Native unconnected census

`phase24_native_unconnected_census.py` parses the native DRC report without
changing severity or filtering the gate. The 397 records are dominated by
146 `12V_PROTECTED`, 128 `POWER_GND`, and 50 `/CORE_CM5/POWER_GND` records;
smaller groups include bridge 1V1/3V3, input/fused 12 V, SATA RX-N, and the
clock nets. The complete table is in
`PHASE24_NATIVE_UNCONNECTED_CENSUS.md`. This identifies the next repair
classes while retaining every native connection as mandatory.

## U7 SATA RX-N pad-field repair

The U7 `BRIDGE_SATA_RX_N` repeated-pad group was repaired with four same-net
F.Cu pad-field links, an offset F.Cu/B.Cu via at `(127.5,140.5)`, a B.Cu
dogleg around the existing SATA-TX trunk, and an offset return via at
`(119.5,134.5)`. Native DRC on the resulting candidate reports 201
violations, zero `shorting_items`, zero `tracks_crossing`, and 392
unconnected pads versus 397 before the repair. No `BRIDGE_SATA_RX_N`
unconnected record remains. This is targeted storage evidence; full-board
parity remains open.

## U5 input-power field stitch experiment

`phase24_u5_input_power_stitch.py` tested the serialized U5 exposed-pad field
using only same-net F.Cu tracks. The 12V_PROTECTED chain joins U5 pads 1, 16,
and 14; its pad-14 leg doglegs around the explicit NC pad 15. The POWER_GND
chain joins the central exposed row and side pads. Native KiCad 10.0.5 DRC
reports 201 violations and 390 unconnected items, compared with 201 and 397
for the integrated-layered baseline; there are zero `shorting_items` and zero
`tracks_crossing`, and no remaining U5 12V_PROTECTED or POWER_GND unconnected
record. This is a valid targeted physical repair, not full Phase 24 closure:
the remaining missing connections are dominated by board-wide protected-12V,
global/CM5 ground, input/fused-12V, low-voltage, and clock/storage groups.

## Regulator-field follow-up

`phase24_regulator_power_field_stitch.py` generalized the serialized
TPSM63606 exposed-pad repair. The all-regulator trial was rejected: U4's
existing PG_BRIDGE_3V3 corridor occupies the direct 12V escape and native DRC
reported one crossing and three shorts. A bounded U3+U5 trial was then run
without U4. It reports the inherited 201 DRC violations, zero shorts, zero
crossings, and 384 unconnected items (down from 397). This promotes only the
U3/U5 local field evidence; U4 requires an obstacle-aware escape and the
board-wide power/ground distribution is still unresolved.

## B-side input fuse pad-field experiment

`phase24_f2_padfield_stitch.py` joins the four raw-side F2 pads and four
fused-side F2 pads as two separate same-net F.Cu fields. Native DRC remains at
the inherited 201 violations with zero shorts and zero crossings; unconnected
items fall from 397 to 391. The candidate is retained as targeted input
geometry evidence, but the F2 fields still need named connections to J6/U2/Q2
and the rest of the protected distribution.

The J1 bus was then combined with a full `In3.PROTECTED_12V` zone in
`phase24_j1_protected_plane.py`. Native DRC remains at 201 violations with
zero shorts and zero crossings; unconnected items improve 268 to 265. The
plane is therefore electrically compatible with the validated connector bus,
but does not replace explicit surface launches for the remaining regulators,
capacitors, input branches, and SXM2/ground populations.

The J1 POWER_GND field was then connected as seven serialized vertical F.Cu
columns, each entering the existing In1/In4 ground planes through an ordinary
via below the protected B.Cu bus. The first y=96.5 mm launch trial was
rejected for six native POWER_GND-to-12V_PROTECTED shorts at the bus. Moving
only those launches to y=98.0 mm removes the shorts: native DRC returns to 201
inherited violations with zero shorts/crossings and 195 unconnected items.
This is accepted J1 ground-field evidence; local ground launches elsewhere
and the separate CM5 ground net remain open.

## CM5 ground-launch experiment (rejected)

The CM5 connector ground net was tested with a dedicated local In1 plane
island and serialized J7 pad-to-via launches. A 0.85 mm outward offset
shorted adjacent signal pads; widening to 1.8 mm still produced new
clearance/short records, and a 3.0 mm perimeter variant reduced the native
unconnected count to 176 but produced 17 shorts, eight crossings, and 422
violations. All variants are rejected. CM5 ground must not be copper-bridged
to global POWER_GND; an obstacle-aware escape or authority correction is
required.

## Bridge low-voltage pad-field experiment

The first direct U4/U5 low-voltage joins crossed the intervening POWER_GND
pad and were rejected with two shorts. The corrected
`phase24_bridge_lv_padfields.py` exits each pad field around that ground pad,
then joins the bridge rail pads on F.Cu. Native DRC is 201 inherited
violations with zero shorts and zero crossings; the plane-based candidate's
unconnected count falls from 265 to 261. This is accepted targeted evidence;
remaining bridge capacitor distribution and control/clock connectivity still
require complete named routing.

## J1 protected-12V field bus experiment

The first J1 B.Cu-only bus was rejected because the saved connector pads are
surface pads and native DRC worsened to 214 violations. The corrected
`phase24_j1_protected_bus.py` derives all 13 protected-pad columns from the
serialized J1 footprint, joins each column on F.Cu, transfers each column
through one ordinary offset via below the final row, and joins the B.Cu bus.
Native DRC returns to the inherited 201 violations with zero shorts and zero
crossings; unconnected items fall from 397 to 268. This is strong targeted
evidence for the J1 protected field, but named attachment to the rest of the
protected distribution and the remaining ground/CM5/rail groups are still
required.

The analogous F1 A-side pad-field trial joins its raw and fused four-pad
groups independently. Native DRC remains at 201 violations with zero shorts
and zero crossings; unconnected items fall from 397 to 392. This is retained
as targeted evidence and preserves the dual-input architecture. The existing
F1/J5/Q1/U1 branch still needs complete named routing and plane launches.

The U4-specific left-side dogbone was rejected as well. It removed the U4
short class, but native DRC found four F.Cu crossings against the existing
PG_BRIDGE_3V3 corridor and U4 ground escape, leaving 390 unconnected items.
U4 therefore needs a layer-separated or locally regenerated corridor rather
than another same-layer coordinate tweak.

A later U4 perimeter reroute was also tested. The initial layer-separated
trial crossed the existing B.Cu feedback trunk; the corrected perimeter
variant moved the escape to y=100.5 mm and avoids that trunk. Native DRC is
back to the inherited 201 violations with zero shorts and zero crossings. It
is retained as a clean U4 local geometry experiment, but the remaining 390
native unconnected items are board-wide and still prevent Phase 24 closure.

The U3 POWER_GND exposed field was tested with a right-side perimeter escape
around the central thermal row and a lower side-pad rail. Native DRC remains
at 201 inherited violations with zero shorts and zero crossings; the prior
bridge candidate's unconnected count falls from 261 to 258. This is accepted
targeted regulator-return evidence; full ground-plane attachment remains
open.

The combined U4/U5 ground-field trial was rejected for two crossings against
the existing U4 PG_BRIDGE_3V3 corridor. A bounded U5-only follow-up retains
the clean U3 ground result and adds the U5 perimeter field: native DRC is 201
inherited violations with zero shorts/crossings and 255 unconnected items.
U4 remains intentionally excluded from this promoted local candidate until
its control corridor is regenerated.

## Global POWER_GND launch cluster

Following the independent PI review, `phase24_pgnd_launch_cluster.py` adds
short F.Cu dogbones and ordinary through-vias for U1.2, U2.2, J4's four
POWER_GND pads, and U8.3, feeding the existing In1/In4 planes. The first J4
bottom-left launch was rejected because its via hit the existing USB2 B.Cu
track; moving that one via to `(40.5,103.0)` corrected the collision. The
final native DRC candidate reports 201 inherited violations, zero shorts,
zero crossings, and 188 unconnected items versus 195 before the cluster.
CM5 `/CORE_CM5/POWER_GND` remains separate and untouched.

## Cumulative local-repair composition

`phase24_integrate_local_repairs.py` composes the validated J1 protected bus
and In3 plane, J1 ground columns, global U1/U2/J4/U8 returns, bridge
low-voltage perimeter escapes, U3/U5 protected-field escapes, U4's perimeter
protected escape, and separate F1/F2 raw/fused pad fields. The first
composition also added U3/U4/U5 ground-field copper and was rejected for
three native crossings between 12V and ground field routes. Removing those
overlapping ground additions yields a clean cumulative candidate: native DRC
201 inherited violations, zero shorts, zero crossings, and 168 unconnected
items. Ground-field additions remain separately validated and must be
reintegrated only with obstacle-aware layer separation.

## Cumulative U7 RX-N integration

`phase24_compose_u7_rxn.py` applies the previously validated U7
BRIDGE_SATA_RX_N pad-field stitch to the cumulative local-repair candidate.
Native DRC remains at 201 inherited violations with zero shorts and zero
crossings; unconnected items fall from 168 to 163. The storage correction
therefore composes cleanly with the accepted power/rail repairs. Clock and
the remaining SATA/control groups remain open.

## U7 clock-pad authority correction

Inspection of the cumulative candidate found U7 pads 52, 53, and 54
serialized without net assignments, despite the schematic mapping to
`BRIDGE_XI`, `BRIDGE_VSSOSC`, and `BRIDGE_XO`. The disposable
`phase24_assign_u7_clock_pads.py` materializes those exact net identities.
Native DRC remains at 201 violations with zero shorts and zero crossings;
the unconnected count changes from 163 to 166 because the now-authoritative
source pads correctly enter the native gate. Clock copper fanout remains
unresolved and will be routed from these real source pads.

## U7 BRIDGE_CFG join experiment (rejected)

The direct CFG pad join crossed U7 pad 24 (`BRIDGE_3V3`) and was rejected.
The attempted perimeter reroute around the pad field still introduced two
shorts and one crossing in native DRC. The CFG control net remains open and
must use a layer-separated, pad-frame-derived escape.

## U7 oracle-derived clock source escape

`phase24_u7_clock_source_escape.py` adds the rotated-U7 oracle's XI and
VSSOSC escapes plus a corrected XO dogleg below the SATA-TX corridor. The
first XO path was rejected for one crossing; the corrected disposable
candidate has zero shorts and zero crossings. Native DRC reports 204 total
inherited/placement violations and 166 unconnected items. This closes the
source-escape discriminator only; support-passive branches and end-to-end
clock connectivity remain open.

## Complete clock passive-branch trial (rejected)

`phase24_clock_passive_branches.py` attempted full XI/XO/VSSOSC branches on
B.Cu from the clean U7 source escape to Y1/R23/C42/C43. The candidate reduced
the unconnected census to 156, but native DRC found three shorts and ten
crossings where the branches entered adjacent passive pads and existing
storage copper. It is rejected; the useful result is that clock closure needs
isolated pad launches and layer-separated buses, not direct B.Cu pad-field
approaches.

## Isolated clock-launch trial (rejected)

`phase24_clock_isolated_launches.py` added offset through-vias at every
clock-support passive pad and separate F.Cu buses. Native DRC rejected the
candidate with 17 crossings and three shorts, including long XI/XO corridors
through existing SATA/USB copper and an XO approach into an unassigned U7
pad. The next valid class must use obstacle-aware layer-separated routing
from the serialized U7 pad field.

## Exact clock-oracle transplant comparison (rejected)

`phase24_clock_oracle_coordinated.py` moved the existing Y1/R23/C42/C43
footprints into the proven rotated-U7 oracle coordinates and copied only the
oracle's XI/XO/VSSOSC tracks and ordinary vias. The transplant is valid as a
reference comparison but is rejected on the cumulative acreage board: native
KiCad DRC reports 288 violations, including clock/SATA crossings and
clock-to-J3 shorts/clearances. This confirms the oracle topology is sound but
its fixed coordinate context must be locally regenerated around the current
storage launch.
## Exact coordinated oracle transplant — rejected

`phase24_clock_oracle_coordinated.py` moved Y1/R23/C42/C43 to the exact
rotated-U7 oracle positions/orientations and copied only clock-net tracks and
ordinary vias onto the current U7 authority candidate. Native KiCad DRC
reported 288 violations and 166 unconnected items, including clock/SATA
crossings, clock/J3 interactions, and shorts/clearance failures. Rejected for
acreage integration; the oracle topology remains valid and must be regenerated
around the current serialized U7/storage geometry.

## U5 connectivity audit corrected

`phase24_u5_layer_connectivity_audit.py` now uses KiCad's native connectivity
rebuild over the saved PCB and checks asserted target pads against native
connected-item components. It no longer creates graph edges from expected
connectivity. The saved U5 board passes, and the regression negative control
removes an actually connected U5.9 trace in a disposable board object; the
audit then fails as required. No validation severity was changed.

## Clock fixture V2 and acreage transform

`phase24_complete_clock_fixture_v2.py` produces a complete clock-specific
fixture with XI/XO on B.Cu and VSSOSC on an F.Cu perimeter. Its native
connectivity and clock-short/crossing regression passes. The transformed
acreage experiment is rejected at 226 DRC violations, including seven clock
shorts and 16 crossings; the fixture topology is retained, but the fixed
transform is not promoted.

## Incremental XI/XO/VSSOSC probes

The XI-only and XI+XO probes each have zero native short/crossing classes and
reduce the unconnected census from 166 to 165 and 164 respectively. The first
VSSOSC addition is rejected at 163 unconnected records because its F.Cu path
crosses the inherited SATA-TX-N corridor and shorts the XI launch and a
POWER_GND pad. The next repair is a layer-separated VSSOSC obstacle crossing;
XI/XO are retained unchanged.

The subsequent passive-field B.Cu search could not find a path from the
serialized Y1.1 launch to R23.1 within the current local bounds, so no
candidate was emitted. This further localizes the open work to coordinated
passive-field routing/placement.

## Complete clock composed on cumulative repairs

`phase24_apply_complete_clock.py` composed the complete native-clean clock
source (`PHASE24_CLOCK_COMPLETE_ASTAR_V2.kicad_pcb`) onto
`PHASE24_LOCAL_REPAIRS_U7_RXN.kicad_pcb`. Native pad-component checks pass for
XI (Y1.1/R23.1/C42.1), XO (Y1.3/R23.2/C43.1), and VSSOSC
(Y1.2/Y1.4/C42.2/C43.2). Native DRC reports 205 violations and 156
unconnected records, with zero `[shorting_items]` and zero
`[tracks_crossing]`. The clock is therefore promoted into the cumulative
ancestor; Phase 24 remains open for the unrelated board-wide connectivity
census.

## Bridge 1V1 capacitor-field continuation

`phase24_bridge_1v1_cap_chain.py` adds adjacent ordinary-via escapes from the
left-side rail pad of the spaced C26/C27/C28/C29 and C34-C41 fields, then joins
the escapes on B.Cu. Native DRC holds at 205 violations with zero
`[shorting_items]` and zero `[tracks_crossing]`; the unconnected census falls
from 156 to 145. The candidate is accepted as the next cumulative ancestor.
The remaining BRIDGE_1V1 records are isolated R19, R22, and C41 endpoints and
will be handled separately rather than assuming this field route closed them.

## Bridge 1V1 field joined to U5

`phase24_bridge_1v1_field_join.py` adds a B.Cu perimeter join from the
field's existing ordinary via to the C46.1/U5.5/U5.8/U5.9 output island.
Native DRC remains at 205 violations with zero `[shorting_items]` and zero
`[tracks_crossing]`; unconnected records fall to 144. Native connectivity
confirms the complete capacitor field and U5 output pads are one component.
R19.1 and R22.1 remain isolated endpoints for a separate local repair.
