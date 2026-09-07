# RTL9210B support-fixture route experiments — 2026-09-07

## Current authoritative baseline

V8 is the current combined support/SPI baseline and V9 is the retained
RTL_5V rail primitive. V10/V11 RTL_3V3 trunks are rejected because they
intersect retained high-speed/support corridors. The next experiment must
change the 3V3/support corridor or coherently reauthor that local island.

The 90-degree mixed-layer V18/V19/V20/V21 trials remain disposable evidence.
V20 reduced the source-field result to 3 findings / 41 opens; V21 rejected a
down/right RTL_3V3 departure after it entered adjacent U1 RTL_5V/RTL_1V1 pads
and crossed SPICLK. The next implementation requires a transformed-pad-aware
escape cell.

Status: **REJECTED ROUTE IMPLEMENTATIONS; PATH B ARCHITECTURE UNCHANGED**

These experiments operate only on disposable RTL9210B bring-up fixtures.
Neither changes `STORAGE.kicad_sch` nor the clean acreage PCB.

## Latest source-field experiments

The fully scrubbed rotated-U1 staggered-via candidate
`PHASE24_RTL9210B_ROTATE_U1_STAGGERED_SPI_V1.kicad_pcb` was tested with
ordinary 0.6/0.3-mm vias and source transitions spaced 1.2 mm apart. Native
KiCad reports 24 violations / 40 unconnected items, including SPI net
shorts, crossings, and source-field clearances. It is rejected as a route
implementation; no production or Path-A asset changed.

That trial also exposed a real disposable-library defect in U2. The
`BRINGUP_W25Q128_SPI_FLASH` footprint had `(at 20 18)` but pad coordinates
that were authored as absolute-looking board coordinates. Consequently,
moving U2 did not move its pads. A corrected local-coordinate test was
created as `PHASE24_RTL9210B_U2_CORRECTED_FOOTPRINT_V1.kicad_pcb`. Its native
DRC result is 53 violations / 39 opens because the selected placement and
SPI permutation still collide with the rotated U1 field; it is rejected as
an implementation candidate, while the coordinate-frame correction is
retained as the basis for future placement tests. The defect does not alter
the Path-B electrical decision or production CAD.

The corrected-footprint left/90-degree placement
`PHASE24_RTL9210B_U2_CORRECTED_LEFT_ROT90_PLACEMENT_V1.kicad_pcb` was then
checked without copper. Native KiCad reports 6 findings / 44 opens, with no
new signal short; the inherited findings are the known GND/footprint
conditions. A mixed-layer SPI trial against its actual transformed pads,
`PHASE24_RTL9210B_U2_CORRECTED_LEFT_ROT90_SPI_V1.kicad_pcb`, reports 24
violations / 39 opens, including SPISI/SPICLK and SPICS/SPISO conflicts and
pad-field clearances. It is rejected as a route implementation. The
placement remains valid evidence that further trials must use corrected
transformable geometry, but this coordinate/orientation plus simple
two-layer escape is not promotable.

## Far placement and order-preserving layer partition

`PHASE24_RTL9210B_U2_CORRECTED_FAR_PARTITION_SPI_V1.kicad_pcb` placed the
corrected U2 at `(86,90)` with 90-degree orientation and assigned the
order-preserving SPI subsets to F.Cu and B.Cu. Native KiCad reports 30
violations / 40 opens. The dominant findings are actual SPISI/SPICLK,
SPICS/SPICLK, SPISO3/SPICS, and SPISO/SPICS conflicts, plus source-field
clearances and crossings. The report shows the failure is at the rotated
U1 source escape and retained XTAL_OUT region, not the U2 footprint's
coordinate frame. This route class is rejected; the next trial must solve
the QFN source breakout itself or change the U1 source-facing orientation.

## Focused QFN dogbone probe

`PHASE24_RTL9210B_U1_QFN_SINGLE_DOGBONE_V1.kicad_pcb` scrubbed retained
XTAL_IN/XTAL_OUT/RSET/local SPISI copper and tested only the rotated-U1
SPISI departure. The route leaves the pad at 45 degrees, reaches a
0.6/0.3-mm ordinary-via transition outside the QFN field, and continues on
B.Cu. Native KiCad reports 5 findings / 44 opens with no signal short,
crossing, or clearance violation from the dogbone. Remaining findings are
the intentionally incomplete probe and inherited GND conditions. This
validates the local departure geometry; it does not close the five-net SPI
branch.

The SPISO3 corrected-U2 handoff V2
`PHASE24_RTL9210B_SPISO3_CORRECTED_U2_V2.kicad_pcb` moved the handoff to a
north-side F.Cu corridor after recreating the validated source dogbone.
Native KiCad reports 16 violations / 43 opens, including SPISI/SPISO3 and
SPISO3/XTAL_IN conflicts plus crossings. It is rejected as a one-net route
implementation. The result establishes that the complete five-net source
escape and downstream flash launch must be authored together.

## Complete corrected-U2 partition trial

`PHASE24_RTL9210B_COMPLETE_SPI_PARTITION_V1.kicad_pcb` used the corrected U2
footprint at 0 degrees and connected all five source tails toward the flash
row using a proposed two-layer partition. Native KiCad reports 12 violations
/ 39 opens. SPISO/SPICS cross at the F.Cu handoff, and SPICLK/SPISO3 conflict
with existing B.Cu source tails. The corrected U2 pad map itself is valid;
this append-style route is rejected, and the next trial must regenerate the
complete five-net branch together.

## Rotated support relocation V3 — rejected

The normalized Y1/C1/C2/R1 support relocation was re-authored with ordinary
transitions outside the QFN field. Native KiCad reports 14 violations / 37
opens. XTAL_IN and RSET pass saved-board connectivity, but XTAL_OUT is
disconnected and the source transitions conflict with U1 power-field pads.
V3 is rejected as a route implementation; V2 and the original support
placement evidence remain preserved.

## Rotated support relocation V8 — local PASS

`PHASE24_RTL9210B_ROTATED_SUPPORT_RELOCATION_V8.kicad_pcb` preserves the
compact relocated support placement and moves the XTAL_OUT transition beyond
the U1 QFN pad envelope. Native KiCad reports 2 inherited findings only:
isolated B.Cu GND fill and a silkscreen overlap. There are no signal shorts,
crossings, or signal-clearance violations. A saved-board native audit passes
XTAL_IN (U1.53/Y1.1/C1.1), XTAL_OUT (U1.54/Y1.2/C2.1), and RSET
(U1.51/R1.1). The fixture still reports 35 unrelated unconnected items, so
this is a local support-route PASS rather than full Path-B closure. Path A
and production CAD are unchanged.

The same V8 saved board passes the native five-net SPI endpoint audit for
SPISI, SPICLK, SPISO3, SPISO, and SPICS. Its SPISI trace-removal negative
control fails as required, confirming no synthetic connectivity edge was
introduced by the support relocation.

## RTL_5V rail V9 — local PASS

`PHASE24_RTL9210B_RTL5V_RAIL_V9.kicad_pcb` adds a bottom-side RTL_5V trunk
from U1.17/U1.33 to C5.1 through ordinary vias outside the QFN pad field.
Native KiCad reports 4 inherited findings / 33 unconnected items and no new
signal violation. Saved-board connectivity passes U1.17, U1.33, and C5.1.
This is a local rail primitive, not full support closure.

## RTL_3V3 rail V10/V11 — rejected

The V10 local 3V3 trunk reduced the fixture to 31 opens but produced real
SPICLK/RTL_3V3 and XTAL_IN/RTL_3V3 shorts. V11 moved the source transitions
but its lower B.Cu trunk crossed SPICS and the Y1 XTAL_IN launch, reporting
12 native signal violations / 31 opens. Both are rejected route
implementations; the next 3V3 trial must change corridor topology.

The top/outer RTL_3V3 V12 probe is rejected at 9 native violations / 31
opens. U1.20 crosses the validated SPISI/SPICLK source escapes and U1.52's
transition reaches the XTAL_IN/Y1 launch. The next attempt must co-author 3V3
with the QFN source escape and preserved SPI.

## Complete four-net QFN field V14 — rejected

V14 regenerated SPISI, SPICLK, SPISO3, and RTL_3V3 as one source-field
topology. Native KiCad reports 24 violations / 31 opens: direct departures
cross the U1 pad field, B.Cu channels cross, and RTL_3V3 collides with
XTAL_IN. This route class is rejected; the next class must change U1 or
local-support placement/orientation.

## 90-degree U1 four-net field V16 — rejected

V16 tested the rotated U1 top-row source field with separated SPISI, SPICLK,
SPISO3, and RTL_3V3 channels. Native KiCad reports 7 violations / 41 opens;
the B.Cu channels cross during the U2 handoff. The placement remains useful
evidence, but the simple parallel-drop implementation is rejected.

## 90-degree mixed-layer source field V17 — rejected

V17 kept SPISO3 on F.Cu and placed SPICLK/SPISI on separated B.Cu channels,
with RTL_3V3 on its own upper bus. Native KiCad reports 5 findings / 41
opens; SPISI/SPICLK transition proximity and the reversed B.Cu handoff still
produce real shorts/crossing. This improves over V16 but is not promotable.

## Integrated 3V3/SPICLK source escape V13 — rejected

V13 regenerated SPICLK with RTL_3V3 but still reports 10 native violations /
31 opens. SPICLK crosses the retained SPISI departure, and RTL_3V3 collides
with SPICLK and XTAL_IN. The next candidate must regenerate the
SPISI/SPICLK/SPISO3/RTL_3V3 QFN source field together.

`phase24_rtl9210b_support_v8_audit.py` records the same check as a reusable
regression: all three V8 support nets pass from saved-board native
connectivity, and removal of an XTAL_OUT track fails the audit.

The fully regenerated V3 branch
`PHASE24_RTL9210B_FULL_REGENERATED_SPI_V3.kicad_pcb` removed the lower
SPISO/SPICS B.Cu source tails and routed those nets directly on F.Cu. Native
KiCad reports 8 violations / 40 opens: SPICS crosses the regenerated source
dogbones and SPICLK/SPISO3 still conflict on the upper B.Cu departure. The
class is rejected; source and downstream channels must be planned together.

## Channelized full SPI V1 — local PASS

`PHASE24_RTL9210B_CHANNELIZED_FULL_SPI_V1.kicad_pcb` regenerates all five
U1-to-U2 SPI nets from a scrubbed base. It preserves the validated lateral
QFN departures, keeps SPISI/SPICLK/SPISO3 on separated B.Cu orthogonal
columns, gives SPISO an independent F.Cu corridor, and routes SPICS below
the upper channels on B.Cu. Native KiCad reports 1 inherited isolated-GND
warning / 40 unrelated support opens, with no SPI signal violation. The
saved-board native audit passes all five endpoint pairs; removing a necessary
SPISI track makes the audit fail. This is a local SPI sub-gate PASS, not a
full fixture or production-CAD PASS.

The follow-up five-net probe changed the departure to straight outward
segments before the staggered diagonals. Native KiCad improved to 17
violations / 44 opens, but SPICLK and SPISO3 still short/collide at the
0.6-mm transitions and one source clearance remains. This is rejected as a
transition-layout implementation; the diagonal single-net departure remains
validated evidence.

The V3 source-transition spacing trial
`PHASE24_RTL9210B_U1_QFN_FIVE_DOGBONES_V3.kicad_pcb` increased the lower-row
separation but still reports 10 violations / 44 opens. The only signal
violation is the same SPISO-to-SPISO3 clearance (0.100 mm actual versus
0.200 mm required); there are no shorts or crossings. V3 is rejected and
the next class must change the post-pad fanout shape.

The V4 lateral-transition source probe
`PHASE24_RTL9210B_U1_QFN_FIVE_DOGBONES_V4.kicad_pcb` moves SPISO3's
transition laterally away from the SPISO departure. Native KiCad reports 9
findings / 44 opens with no shorts, crossings, or signal-clearance errors;
the remaining findings are incomplete-probe dangling items and inherited
GND conditions. This closes the local five-net QFN source-escape sub-gate,
not the full SPI branch.

The V2 transition-spacing micro-variant
`PHASE24_RTL9210B_U1_QFN_FIVE_DOGBONES_V2.kicad_pcb` was rejected at 10
violations / 44 opens. It leaves one SPISO/SPISO3 clearance violation and
the expected incomplete-probe/inherited findings, so it does not improve
the V1 source-field result. The V1 and V2 results are retained separately;
production CAD and Path A are unchanged.

## Attempt 1 — all-F.Cu support fanout

`PHASE24_RTL9210B_BRINGUP_SUPPORT_ROUTED.kicad_pcb`

The crystal, RSET, and SPI support nets were routed directly on F.Cu using
the fixture's first placement. Native DRC found 58 violations and 46
unconnected items:

```text
17 tracks_crossing
2 shorting_items
36 track_width
3 solder_mask_bridge
```

The author used 0.15 mm tracks below the board's 0.20 mm minimum and forced
long support corridors through one another. Rejected as route implementation
failure.

## Attempt 2 — SPI B.Cu ordinary-via escape

`PHASE24_RTL9210B_SPI_BCU_FIXTURE.kicad_pcb`

The five SPI nets were re-authored with pad dogbones, ordinary F.Cu/B.Cu
transitions, and ordered B.Cu channels. The saved-track/via audit passes and
confirms no via-in-pad coordinates, but native DRC still finds:

```text
2 shorting_items
14 clearance
10 annular_width
10 via_diameter
10 drill_out_of_range
51 unconnected_items
```

This rejects the specific via geometry and remaining pad-field interaction.
It does not reject RTL9210B or the support topology. The next valid route
class must use the ordinary-via dimensions allowed by the selected JLC stack,
move transitions farther from the QFN/flash pad fields, and then revalidate
the full support group.

## Generator correction and support-local V2

Native KiCad inspection found a fixture serialization defect: the generated
layer table declared inner layers as `power` and ordered `B.Cu` before the
inner layers, so numeric layer 2 was loaded as `In4.GND` rather than `B.Cu`.
The generator now matches native KiCad's six-layer `signal` serialization and
layer order. This was a fixture-authoring defect, not evidence against the
route topology.

The support-local V2 placement then moved the crystal, RSET, flash,
decoupling, and pull-ups into a coherent local neighborhood. Its unrouted
native baseline has zero DRC violations. A native-coordinate oscillator/RSET
route against that placement improves to 4 DRC violations / 52 opens, with
three local crossings and one RSET/XTAL interaction; no via, drill, or track
width violations remain. It is still rejected as a route implementation, but
 the placement variant remains a credible next baseline.

## Attempts 3 and 4 — oscillator/RSET local variants

Two further variants were generated from the same native-coordinate support
placement. V3 remained at 4 native DRC violations / 52 opens, including one
XTAL_IN/XTAL_OUT crossing, two shorts (XTAL_IN/XTAL_OUT and XTAL_OUT/GND), and
one solder-mask bridge. V3 is rejected as a route implementation while the
support-local V2 placement remains retained.

V4 changed the local dogbone ordering but regressed to 5 violations / 52
opens, including two shorts and three solder-mask bridges. V4 is rejected as
worse than V3. These experiments do not reject RTL9210B or its support
topology; they establish that another routing method is required rather than
another fixed-coordinate oscillator trial.

## Attempt 5 — V7 separated-layer oscillator route

V7 changed the method rather than another local dogbone ordering: XTAL_IN
escapes to B.Cu at a transition clear of the adjacent QFN pads, XTAL_OUT
uses a separate transition below the XTAL_IN escape, and RSET uses an
independent B.Cu corridor. Native KiCad DRC reports **0 violations / 52
unconnected items**. The local saved-track audit passes and confirms that the
three intended nets are actually authored; the 52 opens are the remaining
unrouted support-fixture boundary and are not waived. V7 is therefore a local
route PASS, not a full RTL9210B fixture PASS.

## Attempts 6 and 7 — SPI support route

SPI V2/V3/V4/V5/V6 were retained as routing-development evidence. They
progressively removed undersized-via, source-pad clearance, dangling-via, and
same-layer crossing defects. The final V7 uses ordinary 0.6/0.3-mm vias for
the three monotonic B.Cu channels, a separated B.Cu SPICLK corridor, and a
F.Cu perimeter corridor for SPISI. Native KiCad DRC reports **0 violations /
52 unconnected items**, and the saved-track/net/via audit passes. This closes
the SPI local route sub-gate only; remaining fixture support and intentional
boundary opens are still open.

## Ground/reference closure discriminator

The isolated V2 fixture had no copper zones, so every GND return remained an
open even after local signal routes passed. An in-board disposable F.Cu/B.Cu
GND pair with ordinary 0.6/0.3-mm stitching vias was added to the SPI V7
candidate. Native DRC remains **0 violations** and unconnected items fall from
52 to 45. This closes reference-plane connectivity for the disposable
fixture only; it does not synthesize signal edges or promote the fixture into
production CAD.

## RTL_3V3 support bus

The first power-support route exposed a generator assumption: after native
KiCad saved the filled fixture, net identities were serialized by name rather
than through the old numeric net table, and the first DRC was run before
refilling zones. The generator now emits native named-net segments. The
refilled candidate connects U2 pins 3/8, C3, and the R2/R3 3V3 returns;
native DRC reports **0 violations / 41 unconnected items**, and the saved-net
audit passes. This is a local support sub-gate, not full fixture closure.

## RTL_5V/C5 and RTL_1V1/C4 support

Five local route variants were rejected for QFN pad-field, corridor, via, or
adjacent-GND geometry. V6 changes the route class: RTL_5V reaches its B.Cu
outboard corridor through an F.Cu transition and approaches C5 from above;
RTL_1V1 escapes from the QFN top row before its B.Cu transition. Native DRC
after zone refill reports **0 violations / 39 unconnected items**. This closes
the two local rail-support sub-gate only; control/sideband, USB, M.2, and
test-access connectivity remain open.

## RESET/PERST and PEDET/CLKREQ control routing

The first combined PEDET/CLKREQ/PERST/RESET author was rejected at **8 DRC
violations / 33 opens**. Its saved-net audit correctly caught distinct
RESET_N versus PERST_N ownership, but the PEDET/CLKREQ B.Cu corridors crossed
the rail/SPI corridors and one J1 transition was too close to PERST. A
corrected separate RESET_N/PERST_N route was then authored from the V6 rail
baseline and passes native DRC at **0 violations / 37 opens**. PEDET/CLKREQ
remain the next control-routing gate and are not waived. V2 reduced the
combined PEDET/CLKREQ class to 3 crossings / 33 opens; V3 changed the
RTL_1V1 corridor but regressed to 5 crossings / 33 opens. Both are retained
as rejected route evidence, not current fixture candidates.

V4/V5/V6 continued the control experiments with layer/detour changes but did
not close the class: their native results were respectively 8 violations /
34 opens, 3 / 34, and 4 / 33. The residuals are same-layer crossings between
PEDET, CLKREQ_N, RTL_5V, and inherited support corridors. This coordinate-only
class is rejected; further work must use a genuinely layer-separated source
and endpoint departure.

## Relocated R2/R3 control-island placement and perimeter routes

The disposable placement `PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL.kicad_pcb`
was corrected after an initial coordinate-frame error. Native inspection
confirms R2 pad 1 at `(71,48)` and R3 pad 1 at `(74,48)`; the only baseline
findings after relocation were stale RTL_3V3 tracks to the former positions.
The 3V3 bus was regenerated from saved named nets before testing controls.

Three new route classes were then tested and rejected without changing Path A
or production CAD:

* `PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V1.kicad_pcb`: 6 native DRC
  violations / 34 unconnected items. PEDET/CLKREQ crossed the inherited
  RTL_5V/RTL_1V1/RTL_3V3 corridors and CLKREQ approached REFCLK too closely.
* `PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V2.kicad_pcb`: 8 violations / 35
  unconnected items. The upper/lower layer split still crossed inherited rail
  corridors and placed the CLKREQ via inside the PERST clearance field.
* `PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V3.kicad_pcb`: 10 violations / 35
  unconnected items. The lower-perimeter class collided with inherited
  RESET/PERST and crystal/support geometry and produced a PEDET pad-field
  interaction.

These are valid native KiCad experiments, not synthetic graph results. They
show that the current local placement plus inherited support escape does not
yet provide a legal PEDET/CLKREQ corridor. They do not reject RTL9210B. The
next authorized class is a coherent local control/support-island regeneration
that includes RESET/PERST departures, rather than adding more perimeter
detours to the current mixed baseline. The fixture remains isolated and Path
A remains preserved.

## Coherent four-control regeneration — V4 through V8

V4 removed the inherited RESET/PERST/PEDET/CLKREQ copper and regenerated all
four controls together, but its diagonal QFN departures crossed adjacent
no-net pads and produced 16 violations / 34 opens. V5 corrected the source
departures to vertical QFN-safe escapes and reduced the result to 6 / 35.

V6 corrected the remaining 3V3 branch transitions and moved only the local
PEDET/rail interaction. Native DRC reports **3 violations / 36 opens**. V7
moved the inherited RTL_5V transition into a nominally clear B.Cu channel,
but that channel intersects RTL_1V1 and drives the rail through the QFN-side
pad field; it regresses to **15 / 32**. V8 restores V6's rail geometry and
moves only PEDET to a B.Cu dogleg; it reports **4 / 35**, including a
dogleg/3V3 transition conflict.

V6 is retained as the current disposable baseline, not a pass. The remaining
implementation task is the local RTL_5V/3V3/PEDET transition field; further
long perimeter detours are not justified. All results are native KiCad DRC
after zone refill, and Path A/production CAD remain unchanged.

V9 retained V6 and added a local PEDET dogleg around the inherited RTL_5V
via. It remains at **3 violations / 36 opens** because the dogleg intersects
the RTL_5V vertical departure. This closes the current same-placement route
class for evidence; the next class must relocate or coherently re-author the
small RTL_5V/3V3/control support island rather than add more PEDET detours.

## Lower-left support placement discriminator

The first lower-placement helper incorrectly used global pad coordinates as
the footprint anchor and placed R2/R3 at the wrong coordinates. That variant
is retained only as tooling evidence. The corrected helper uses the native
pad-to-footprint local offset and produces R2 pad 1 at `(69,78)` and R3 pad 1
at `(72,78)`.

The first regenerated lower-placement route uses a separate bottom 3V3
collector and lower PEDET/CLKREQ/PERST corridors. Native DRC reports **9
violations / 33 opens**, including RESET/3V3 crossings, PEDET/CLKREQ
crossings, a GND-via collision, and a QFN-edge departure clearance. It is
rejected as a route implementation and not ranked above V6 merely because it
has fewer opens. Production CAD and Path A remain unchanged.

Lower V3 re-authored the corrected lower placement with separated PEDET,
CLKREQ, PERST, RESET, and 3V3 corridors. Native DRC reports **10 violations
/ 33 opens**, including SPI/3V3 interference, lower control crossings, and a
GND-via collision. It is rejected as a route implementation; the lower
placement remains disposable and no Path-B architecture decision changes.

V10 attempted a QFN-safe RTL_5V departure from U1 pad 17 while preserving
V6 controls and 3V3. Native DRC regressed to **14 violations / 35 opens**;
the new rail transition collided with RTL_1V1 and PERST geometry and did not
complete the source join. It is rejected. Moving only the rail departure is
insufficient; the support island remains isolated and Path A is preserved.

## PEDET reroute V11–V15

V11–V15 tested bounded PEDET return relocations around the V6 rail field:
native DRC results were 5/35, 3/36, 4/35, 4/35, and 15/35 respectively.
V12 removed the original RTL_5V/PEDET short but introduced an RTL_3V3
crossing; V13/V14 moved the transition to B.Cu but retained via/rail-field
conflicts; V15 regressed with multiple shorts and crossings. The route class
is rejected. V6 remains the current baseline and no Path-B authority or
production CAD changed.

## SPI test-access V1 — rejected

The first test-access author connected four SPI test-pad targets from the V6
control fixture, but native DRC reported 12 violations / 35 unconnected
items. It reintroduced the superseded PEDET short and crossed SPI, RESET,
PERST, and CLKREQ corridors; B.Cu routes also lacked a valid F.Cu pad
transition. The candidate is preserved as negative-control evidence and is
not a current baseline.

V2 was regenerated from corrected V12 control geometry, but native DRC
reported 33 violations / 35 unconnected items. The four B.Cu lanes caused
source-pad shorts, RESET/PERST/CLKREQ crossings, mask bridges, and via
clearance failures. V2 is rejected; no test-access copper is promoted.

## RTL_1V1 QFN collector V1

The first ordinary-via perimeter collector for U1 RTL_1V1 pads reduced native
unconnected items from 36 to 29, but DRC reported 9 violations from SPICS/
SPISO pad-field conflicts, a CLKREQ crossing, and duplicate-via geometry.
It is rejected as a route implementation; the open-count reduction confirms
that coherent rail collection is preferable to individual signal detours.

## RTL_3V3 zone V1 — rejected

The local F.Cu RTL_3V3 zone did not reduce the required open count: native
DRC remained 4 violations / 30 unconnected items and U1 RTL_3V3 pads did not
gain native connectivity. It is rejected as ineffective; V2 remains the
RTL_1V1 collector baseline.

V2 removed the duplicate transition, omitted the SPI-conflicting pad-25
branch, and jogged the bottom rail around CLKREQ: native DRC 4/30, with six
RTL_1V1 pads collected. V3 moved the pad-40 via left but caused a
USB_TXP0 short and CLKREQ crossing at 6/30. V2 is the preferred disposable
collector baseline; no rail copper is promoted.

## Native connectivity audit

`phase24_rtl9210b_control_connectivity_audit.py` uses KiCad's actual saved
connectivity data and passes PEDET, CLKREQ_N, PERST_N, RESET_N, and all four
U1↔U2 SPI endpoint assertions on V12. Its negative control removes PEDET
copper and fails as required. Test pads remain deliberately outside the
assertion set until a coordinated access route is authored.

## RTL_5V pad-17 escape V1 — rejected

Starting from the preferred RTL_1V1 collector V2, a direct F.Cu side escape
was attempted for U1 RTL_5V pad 17 into the existing pad-33/C5 rail bus.
Native connectivity gained one real rail endpoint and reduced unconnected
items from 30 to 29, but native DRC reported 8 violations: the escape
crossed/shorted the SPISO, SPISI, and SPICLK field and retained the inherited
PEDET/RTL_3V3 and RTL_1V1/CLKREQ conflicts. This is rejected as a route
implementation; the V2 collector remains the current disposable baseline and
production copper is unchanged.

## RTL_3V3 local trunk V1 — rejected

From the V3 RTL_5V baseline, a direct F.Cu trunk was added from U1 pad 34
through pad 20 and toward the existing C3-side RTL_3V3 branch. Native DRC
reported 17 violations / 27 unconnected items: the trunk crossed and shorted
SPICS, SPISO, the RTL_5V transition, and nearby pad-field geometry. Although
the open count fell by two, the geometry is not manufacturable and is
rejected. The clean V3 RTL_5V baseline remains preferred.

## RTL_5V pad-17 escape V2/V3

V2 moved the transition below the QFN but placed the 0.6-mm via too close to
the existing RTL_1V1 via at (82.8,67.5), producing an RTL_1V1/RTL_5V short
and six clearance violations; it is rejected. V3 moved the ordinary via to
(83.6,67.0) and retained the B.Cu corridor to the existing bus. Native DRC
reported 4 violations / 29 unconnected items, with pad 17 absent from the
unconnected set. The remaining violations are inherited from the V2 baseline
(RTL_3V3/PEDET, CLKREQ/RTL_1V1, and unfinished support/test geometry). V3 is
the preferred disposable RTL_5V collector baseline; no production copper is
promoted.
## RTL_3V3 pad-52 escape V1/V2 — rejected

V1 routed U1 pad 52 to the existing west-side 3V3 trunk and reduced native
opens from 29 to 28, but its F.Cu trunk shorted the verified GND via at
(75.0,54.0). V2 jogged west around that via, but collided with the CLKREQ
pull-up at (74.0,48.0) and regressed to 7 DRC violations / 30 opens. Both
are rejected as route implementations; the V3 RTL_5V board remains the
preferred disposable baseline and production CAD is unchanged.
## RSET V1/V2/V3 — rejected

RSET V1 reached U1 but shorted the C1 ground pad. V2 jogged around C1 but
shorted the Y1 XTAL_IN pad. V3 moved both endpoints through ordinary vias and
B.Cu, reducing native opens to 28, but crossed the RTL_1V1 B.Cu corridor and
exposed an inherited RTL_1V1/CLKREQ via conflict. The route class is
rejected; no production copper is changed.
## Crystal support V1 — rejected

The complete XTAL_IN/XTAL_OUT candidate used explicit dogbones around the
collinear capacitor pads and reached the U1 crystal pads, reducing native
opens 29 to 25. Native DRC nevertheless found four real XTAL_IN/XTAL_OUT
crossings and an incomplete C1 ground thermal connection. It is rejected;
the next attempt must separate the two crystal nets by layer/transition.
## Crystal support V2 — rejected

XTAL_IN was moved to B.Cu immediately after Y1 while XTAL_OUT remained on
F.Cu. The candidate still reduced native opens to 25, but the U1-side
approaches crossed at the transition, crossed RTL_1V1, and retained the
incomplete C1 ground thermal connection. It is rejected; future work must
change the U1-side approach geometry rather than repeat the capacitor escape.
## Crystal support V3/V4 — rejected

V3 separated both crystal nets through B.Cu and reached all endpoints at
6 DRC violations / 25 opens; the only new error was the XTAL_OUT approach
crossing an existing RTL_1V1 pad escape. V4 moved that final leg, but native
DRC found seven violations including XTAL_OUT shorts to the XTAL_IN via and
RTL_1V1 via. Both remain disposable negative evidence; no production copper
is promoted.
## QFN escape map and crystal V5 — rejected

`phase24_rtl9210b_qfn_escape_map.py` records native U1 pad coordinates and
all existing track/via corridors in the x=73..87, y=56..68 window. It shows
that the RTL_1V1 collector and control transitions form a real local barrier.
Crystal V5 routed XTAL_OUT around the outer perimeter, but native DRC found
18 violations including RTL_5V crossing/shorts, PEDET/PERST/CLKREQ conflicts,
and a GND-pad clearance failure. V5 is rejected; the map is retained as the
authoritative basis for the next escape attempt.
## Crystal V6/V7 with pad-55 RTL_1V1 move — rejected

The coherent pad-55 transition move was tested with the dual-layer crystal
routes. V6 exposed a broken lower RTL_1V1 collector and 9 DRC violations;
V7 restored the lower segment but left pad-55 disconnected from the complete
collector and collided with the relocated transition, at 8 DRC violations /
26 opens. This proves that a single-via move is insufficient: the next class
must relocate the full RTL_1V1 collector or move the local support island.
## U2 RTL_3V3 B.Cu trunks V1 — rejected

Moving the two U2-side 3V3 trunks below the PEDET corridor connected three
additional native endpoints, reducing opens from 25 to 22. The long B.Cu
trunks crossed SPISO3, SPICLK, and RTL_1V1 corridors and retained a 3V3
pull-up crossing; native DRC increased to 8 violations. The candidate is
rejected as route implementation evidence and V11 remains the baseline.
## U1 RTL_3V3 pad-34 B.Cu escape V1 — rejected

The measured offset escape reached one additional native endpoint, reducing
opens from 25 to 24. Its F.Cu jog was 0.0472 mm from the RTL_5V bus and
shorted it; the B.Cu trunk also crossed the RTL_1V1 bus. Native DRC reported
9 violations. Rejected; this indicates coherent 3V3 support relocation is
needed rather than further local trace nudging.
## U1 RTL_3V3 pad-34 B.Cu escape V1 — rejected

The pad-34 offset escape reached one additional native endpoint, reducing
opens 25 to 24. Native DRC reported 9 violations: the short F.Cu jog was
0.0472 mm from the RTL_5V bus and shorted it, while the B.Cu trunk crossed
the RTL_1V1 bus. This route class is rejected; the measured result requires
coherent 3V3/1V1 support relocation.

## Coherent relocation route V2 — local sub-gate positive

The in-board (+18,+8) mm relocation was regenerated from the native moved
pads. XTAL_IN, XTAL_OUT, and RSET copper was translated from the staged
source-authority routes; RTL_1V1 was translated locally and given a new
outboard continuation to C4. Native KiCad reports 4 findings / 32 opens,
with no signal shorts or crossings. `phase24_rtl9210b_relocation_route_audit.py`
passes XTAL_IN, XTAL_OUT, RSET, and all eight asserted RTL_1V1 endpoints.
This is a positive local route baseline, not full Path-B closure: U2/C3-C5
links, controls, and remaining support paths are still open.

## Rail-cap co-location V1 — positive local baseline

C3/C4/C5 were moved coherently by (-10,+18) mm beside the relocated U1.
Stale external RTL_1V1 copper was scrubbed and a new B.Cu continuation was
connected to the moved C4 pad. Native KiCad reports 4 findings / 32 opens,
with no signal shorts or crossings. The saved-board check confirms all nine
asserted RTL_1V1 endpoints. This is a local routing baseline only; the other
rails, SPI/control links, and full Path-B validation remain open.

## QFN source partition V1 — rejected

`phase24_qfn_spi_power_partition_v1.py` first exposed a KiCad Python API
failure: calling `FindNet()` after removing serialized tracks returned an
opaque invalid handle. The script was corrected to capture native net objects
before mutation. The resulting `PHASE24_RTL9210B_QFN_SPI_POWER_PARTITION_V1`
was checked by native KiCad 10.0.5 and produced 22 violations / 33
unconnected items. It introduced an RTL_1V1 clearance conflict at U1.14,
an RTL_1V1/XTAL_OUT short at the left transition, and SPICS/SPISO corridor
conflicts. The experiment is rejected as route implementation evidence; no
production CAD was changed. The API correction is retained in the script for
future disposable writers.

## Coherent U1/support relocation V1 — placement discriminator

Because the source-partition route class remained congested, a separate
placement-only candidate moved U1, C1/C2, R1, Y1, and R2/R3 by (+18,+18) mm
after serialized removal of their old local support copper. Native KiCad
reports 9 findings / 45 opens. The findings are one deliberately dangling
old RTL_1V1 trunk, an isolated legacy zone, and non-production silkscreen
overlaps; no new signal short or crossing was introduced. This does not pass
the support route gate. It establishes the moved native pad coordinates as a
candidate source for complete regenerated support routing; U2/C3-C5 remain at
their existing outboard positions and production CAD is unchanged.

## Relocated 3V3/5V rail slice V1 — positive

The moved U1-to-C3/C5 rail slice uses F.Cu source escapes, separated B.Cu
transitions, and dogbones outside the capacitor pads. Native KiCad reports 5
findings / 30 opens, with no signal shorts or crossings. Saved-board checks
pass U1.20/C3.1 on RTL_3V3 and U1.17/C5.1 on RTL_5V. Remaining QFN rail-pad
parity, SPI/control, and full support validation are open.

## Additional U1 rail-pad fanout V1 — rejected

The probe attempted U1.34/U1.33 escapes to the existing relocated 3V3/5V
trunks. Native KiCad reduced opens to 28 but reported real 3V3/5V and
1V1/5V shorts or clearances and a B.Cu crossing. It is rejected as the second
failure in this ordinary-via additional-pad-fanout class. No production CAD
was changed; the clean rail baseline remains the prior rails candidate.

## U2 co-location V1 — placement discriminator

U2 was translated by (-15,+18) mm into the relocated U1/C3-C5 island. Native
KiCad reports 5 findings / 30 opens, matching the prior rail baseline and
adding no signal short or crossing. The five SPI destination pads now occupy
a local row near the moved source, providing the next source/target geometry
for routed SPI regeneration. No production CAD was changed.

## Co-located SPI V1 — rejected

The first explicit F.Cu-only SPI regeneration from the moved U1/U2 pads
produced 19 native violations / 26 opens, including multiple source-pad
crossings, rail interactions, and an RTL_1V1/SPICS short. It is rejected as a
route implementation. The U2 co-location remains a valid placement
discriminator; the next SPI class must use layer transitions and a deliberate
escape ordering.

## Rotated-U1 SPI V1 — rejected

After rotating U1 180 degrees about its exposed-pad center, a five-net SPI
escape was tested from the new left-side source field to the co-located U2.
Native KiCad reports 38 violations / 39 opens, including overlapping source
transition vias, SPICS/SPISO3 conflicts, and crossings of retained XTAL/RSET
copper. It is rejected as a route implementation. The rotation remains a
disposable placement alternative only.

## Isolated SPICS layer probe V1 — rejected

A single-net SPICS route was tested from the moved U1 source to the moved U2
destination using an ordinary 0.6/0.3-mm through-via. Native KiCad reports
11 violations / 29 opens, including a SPICS/RTL_1V1 short and crossing at the
source field, plus pad/hole-clearance failures. The near-transition variant
is rejected; the prior far-transition variant is also retained as negative
evidence. The next attempt must solve the QFN pad-field escape itself.
