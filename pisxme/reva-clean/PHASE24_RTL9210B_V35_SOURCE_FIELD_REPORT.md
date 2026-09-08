# RTL9210B V35 source-field checkpoint — 2026-09-08

## Current decision

The native-refilled V35 board is retained as the rotated-U1 source-field
reference. It is not a complete Path-B candidate and must not be promoted to
production CAD. Path A and the current V595/V615 work remain preserved.

## Revalidated evidence

`PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_NATIVE_REFILLED.kicad_pcb` was
loaded and refilled with KiCad's native zone filler before DRC. The resulting
native DRC receipt contains four inherited warnings only: three isolated GND
zone warnings and one C1/R1 silkscreen overlap. The native audits pass all
five SPI endpoints (SPISI, SPICLK, SPISO3, SPISO, SPICS) and XTAL_IN,
XTAL_OUT, and RSET. Removing a necessary SPI or XTAL_OUT trace in disposable
copies breaks the corresponding native connectivity, so the checks do not
use synthetic graph edges.

## V35 versus the current co-allocated field

V35 has U1's saved pad field at approximately x=94.05–101.95 mm,
y=66.05–73.95 mm, with U2 below it and the crystal/RSET support moved as a
coherent cluster. V595 has U1 at approximately x=102.05–109.95 mm,
y=58.05–65.95 mm, with extensive rail/PEDET/CLKREQ copper already allocated.
V35 therefore supplies a clean five-net SPI/crystal source-field oracle, but
does not contain the complete current rail/control implementation.

## RTL_5V co-allocation result

V1 and V2 used only native V35 pad coordinates and ordinary through-vias and
were rejected: V2's native DRC found 15 violations, including RTL_5V
crossings with SPISI and RTL_3V3, a QFN-edge contact, and dangling segments.
V4 then used the clear upper source corridor, moved the U1.17 departure clear
of SPISI, and removed an unnecessary mid-corridor via. Its native endpoint
audit passes U1.17/U1.33/C5.1, and the trace-removal negative control passes.
Native DRC has four inherited warnings only; the board still has 32 intended
unconnected items because the remaining Path-B support is not yet authored.
V4 is promoted only as the RTL_5V sub-primitive, not as complete support or
production CAD.

The first RTL_1V1 lower-bus probe is rejected as a route implementation. Its
native endpoint audit and trace-removal negative control pass, but native DRC
reports 21 violations: the proposed bus crosses RSET and XTAL_OUT, contacts
U2 GND and C4 GND, and places several vias in occupied source-field areas.
The next 1V1 attempt must relocate the capacitor/support endpoint or
co-author the lower source field; another identical lower-bus sweep is not a
credible continuation.

The U2-left coordinated experiment moved U2 by 10 mm, regenerated all five
SPI channels from native U1/U2 pads, moved C4, and added the lower 1V1 fanout.
Its independent native SPI and 1V1 endpoint audits pass, but native DRC
reports 14 violations including five QFN-source SPI shorts and one XTAL_OUT
crossing. Reject this route implementation. The experiment does show that U2
migration clears the lower 1V1/U2 corridor; the next attempt must regenerate
the U1 source escapes and 1V1 departures as one field.

The source-preserving U2-left trial keeps V35's proven U1 SPI source escapes,
moves U2 10 mm left, regenerates only the SPI destination legs, moves C4, and
adds the lower 1V1 fanout. Native SPI and lower-1V1 audits both pass with
trace-removal controls. Native DRC reports eight findings: six inherited
ground/silkscreen warnings and two real U1.55/XTAL_OUT local conflicts. No
SPI crossing or short remains. Retain this as the current coordinated
placement basis; the next repair must co-author the XTAL_OUT transition and
U1.55 escape rather than abandon the U2 migration.

The crystal co-author candidate relocates XTAL_IN's source transition to
(93.8,76.5) mm and regenerates XTAL_IN/XTAL_OUT together around the U1.55
escape. Native SPI, XTAL_IN/XTAL_OUT/RSET, and lower 1V1 audits all pass with
negative controls. Native DRC reports six inherited warnings only, with no
signal violations; 26 intended external/support opens remain. Retain
`PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_U2_LEFT_CRYSTAL_COAUTHOR` as the
current strongest disposable basis, not as production closure.

On that basis, the upper RTL_3V3 field connects U1.20/U1.34/R2.2/R3.2/C3.1
with a native trace-removal negative control. Native DRC remains at six
inherited warnings and no signal violations. The first lower RTL_3V3 trial is
rejected: it caused QFN/1V1/RSET contacts, and its 0.13208 mm traces violate
the active 0.200 mm minimum-width rule. Lower 3V3 and remaining controls
remain open; no DRC rule was relaxed.

The upper RTL_3V3 candidate connects U1.20/U1.34/R2.2/R3.2/C3.1 and passes
its native trace-removal negative control. The lower RTL_3V3 candidate was
then tried with U1.39/U1.52 and the relocated U2 endpoints. Its native audit
does not pass; native DRC reports nine findings including RSET/1V1/QFN
contacts. A 0.13208 mm retry was also rejected because it still contacted the
source field and violated the active 0.200 mm minimum-width rule. These are
route-allocation failures, not grounds to weaken the board rules.

## Next implementation step

The 180-degree native orientation probe is now the preferred placement
discriminator. Its U1.39-to-U2.8 RTL_3V3 corridor passes saved-board native
connectivity and fails the trace-removal negative control; native DRC remains
at four inherited warnings before the rest of the field is authored. It is a
route sub-primitive, not a full-support or production pass.
V629 adds the complementary U1.34-to-U2.3 lower RTL_3V3 corridor. Both
channels pass saved-board native connectivity, and removing all RTL_3V3
tracks breaks both; native DRC remains at four inherited warnings with no
shorting or crossing class.
V630 attempted a separated U1.33 RTL_5V departure. It retained both lower
3V3 native connections and reduced the rail field to one real DRC violation,
but the U1.33 0.20-mm source track remains only 0.0769 mm from adjacent
U1.32 no-connect pad geometry. Reject this route and evaluate an alternate
authoritative land pattern/package; do not relax the active routing rule.
V631 then separated the transition field farther west. It retains native
connectivity for U1.17/U1.33/C5.1 RTL_5V and both lower RTL_3V3 endpoint
groups, with all-rail trace removal breaking all three groups. Native DRC is
four inherited warnings and has no shorting, crossing, or clearance class.
Retain it as the current disposable coordinated rail basis.
The bottom-edge U1.36/U1.40/U1.50 1V1 collector is rejected: native DRC
identified a U1.40-to-retained-U1.39 3V3 transition collision and additional
source/edge findings. The next 1V1 authoring must co-allocate departures with
the 3V3 field.
V634 provides a clean right-side U1.60-to-C4.1 1V1 sub-primitive on F.Cu.
Native connectivity and the all-RTL_1V1 trace-removal negative control pass;
native DRC remains at four inherited warnings with no signal violation.
V637 extends the right-side 1V1 trunk with U1.50-to-C4.1. Native connectivity
and the all-RTL_1V1 trace-removal negative control pass; native DRC remains at
four inherited warnings with no signal violation. The remaining source
cluster is U1.36/U1.40/U1.55/U1.63.
V638 resolves the U1.55/U1.63 portion with right-edge F.Cu extensions to the
passing C4.1 trunk. Both native endpoints and the all-RTL_1V1 trace-removal
negative controls pass; native DRC remains four inherited warnings with no
signal violation. U1.36/U1.40 remain open.
V639 is rejected. Its first U1.40 route was too close to adjacent U1.41
USB_TXP0; the V2 departure clears that pad field but crosses the retained
U1.39 RTL_3V3 source departure and creates a solder-mask bridge. Native DRC
reports six findings total, with the crossing and mask bridge as the new
signal/mechanical classes; the saved-board U1.40-to-C4.1 endpoint audit and
trace-removal negative control pass. This is a route implementation failure,
not evidence against the 180-degree placement or the RTL9210B architecture.
The next experiment must jointly allocate the adjacent U1.39/U1.40 exits
while preserving the already passing U1.34/U1.39 3V3 and U1.16/U1.25/U1.50/
U1.55/U1.60/U1.63 1V1 channels.
V640 is the passing delayed-bend implementation of that joint allocation.
U1.39 retains its proven F.Cu-to-B.Cu exit; U1.40 stays on F.Cu until below
the QFN pad-body envelope before turning to its own ordinary through-via and
B.Cu corridor. Native DRC remains at four inherited warnings and has no new
signal class. Native U1.40-to-C4.1 and U1.39-to-U2.8 connectivity pass. Retain
this local sub-primitive and continue with the remaining U1.36 departure.
V641's first U1.36 via collided with the retained B.Cu RTL_3V3 collector and
is rejected. V2 moves the via to x=92.5 mm, y=74.3 mm and uses a separate
north-side B.Cu channel. Native DRC returns only the four inherited warnings;
U1.36-to-C4.1 connectivity passes. The full local QFN RTL_1V1 source set is
now connected without relaxing width, clearance, layer, or via rules.
V642 adds ordinary outboard GND returns from U1.69 exposed-pad edge, U1.66,
and U1.45. The first U1.45 via position conflicted with the U1.40 1V1 via and
was rejected; the corrected via at (99.5,76.0) leaves native DRC with only
three inherited silkscreen warnings. Native zone connectivity connects all
three U1 ground pads. Retain this return sub-primitive and continue with the
remaining control, clock, SPI, and external support opens.
V643 adds the missing U1.20 RTL_3V3 branch to the lower field through an
ordinary via at (92.0,67.6) and B.Cu; native DRC remains at three inherited
silkscreen warnings. V644's R2/R3 source extension is rejected because its
west-side B.Cu corridor crosses the retained RTL_5V segment at x=89.0. The
source join must be co-authored around that collector.
V645 completes the shared RTL_3V3 physical component. The R2/R3 source route
joins below the retained 5V collector, and the U1.52/C3 branch joins through
the B.Cu field to the U1.20 branch. Native DRC has no RTL_3V3 short, crossing,
or unconnected finding and remains at three inherited silkscreen warnings.
This is a rail-field closure only; controls, clocks, SPI, USB, lane 0, M.2,
power, firmware, and integrated Path-B validation remain open.
V647's crystal-pair trials are rejected. The direct F.Cu path crosses the
retained rail field; the staggered B.Cu retry removes XTAL_IN/XTAL_OUT contact
but still conflicts with the U1.20 3V3 via and U1 1V1 corridor. The crystal
source exits require coordinated allocation with those rails.
V648's first SPISI route is rejected because its B.Cu source corridor crosses
the retained RTL_3V3 and RTL_5V collectors. The endpoint route class remains
open; allocate SPI separately from the rail field.
V649's high B.Cu SPISI corridor is rejected because its x=91 transition column
crosses the retained RTL_3V3 source route and RTL_5V collector. The next SPI
escape must place the transition west of both rails or co-author the source
field with them.
V651 freshly reloads the retained C3-join board through native KiCad. The
saved-board DRC is 3 inherited silkscreen warnings / 25 unconnected items;
the native inventory confirms all 9 RTL_3V3 pads are joined, while SPISI,
RSET, and XTAL_IN remain open. Use this as the reproducible next-pass baseline.
V652 retains the lower-channel RSET route. The source and resistor-side
transitions are outboard of the QFN and crystal/power fields; native DRC is
three inherited silkscreen warnings with no signal class, and the open count
falls from 25 to 24. RSET is locally closed; remaining support gates stay open.
V650 is a documentation correction: the native C3-join board still has
multiple RTL_3V3 physical components. Endpoint checks alone did not prove the
same-net field; native DRC and the saved-board component inventory reopen this
rail until every assigned pad and support endpoint is physically joined.
V646's first RSET route is rejected. The U1.51-to-R1.1 endpoint path is
physically connected, but its B.Cu diagonal crosses the retained U1.40 1V1
corridor. A separate RSET channel is required; no routing rule is relaxed.
V636 extends the passing 1V1 trunk with a north-of-QFN U1.25 departure.
Native U1.25-to-C4.1 connectivity and the trace-removal negative control
pass; native DRC remains at four inherited warnings with no signal violation.
V635 extends the passing U1.60-to-C4.1 1V1 channel with a north U1.16
departure. Native connectivity and the trace-removal negative control pass;
native DRC remains at four inherited warnings with no signal violation.
The first all-1V1 perimeter collector derived from V631 is rejected. Native
DRC found U1.16/U1.17 and U1.36/U1.35 source shorts, retained-rail crossings,
and a C4 ground collision. The next 1V1 attempt must use source-side channel
allocation around the proven rail field, not a global collector sweep.

Re-author the complete current support field from native pad coordinates on a
fresh V35-derived disposable board: first allocate all three rails and the
QFN power/control departures around the proven five-net SPI/crystal field,
then add REFCLK, lane 0, USB, and external controls. Do not append another
scalar RTL_5V route to V595. The source-field reference has been proven; the
remaining work is coordinated route allocation and full Path-B validation.

## Receipts

- `PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_NATIVE_REFILLED-drc.rpt`
- `PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35-spi-audit.txt`
- `PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35-support-audit.txt`
- `PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_RTL5V_PROBE_V2-drc.rpt`
- `PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_RTL5V_PROBE_V4-drc.rpt`
- `phase24_rtl9210b_v35_rtl5v_audit.py`
- `PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_RTL1V1_PROBE-drc.rpt`
- `phase24_rtl9210b_v35_rtl1v1_audit.py`
- `PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_U2_LEFT_REROUTE-drc.rpt`
- `phase24_rtl9210b_v35_u2_left_reroute.py`
- `PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_U2_LEFT_SOURCE_PRESERVED-drc.rpt`
- `phase24_rtl9210b_v35_u2_left_source_preserved.py`
- `PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_U2_LEFT_CRYSTAL_COAUTHOR-drc.rpt`
- `phase24_rtl9210b_v35_u2_left_crystal_coauthor.py`
