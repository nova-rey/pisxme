# RTL9210B support-fixture route experiments — 2026-09-07

Status: **REJECTED ROUTE IMPLEMENTATIONS; PATH B ARCHITECTURE UNCHANGED**

These experiments operate only on disposable RTL9210B bring-up fixtures.
Neither changes `STORAGE.kicad_sch` nor the clean acreage PCB.

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
