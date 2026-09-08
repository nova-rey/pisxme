# RTL9210B support-fixture route experiments — 2026-09-07

## Current state and documentation hygiene

The JMS583 support network is already instantiated in the live authoritative
storage schematic and in the disposable support candidates. Any earlier note
in this record saying it still needs instantiation is historical/superseded,
not a current TODO. The current promoted rail/control disposable basis is V137
with V131/V122 support sub-primitives; V100 remains historical 1V1 evidence.
Path A and production CAD remain preserved.

## V132–V137 RTL_5V completion trials

V132–V136 are rejected route-allocation experiments. V132 reused an old
RTL_5V path and shorted retained RTL_1V1/CLKREQ fields; V133 co-authored the
rail above SPI but retained an RTL_1V1 short and PERST crossing; V134 hit
ground and CLKREQ vias; V135 entered the inherited CLKREQ corridor and C5
ground; V136 removed the PERST crossing but still contacted CLKREQ. These
reject those geometries only, not RTL9210B.

V137 starts from V131, keeps the validated CLKREQ overpass, and sends the C5
branch below the local control field before returning to C5.1. Native saved
connectivity joins C5.1/U1.17/U1.33. The focused audit and trace-removal
negative control pass, and the native report has no `shorting_items` or
`tracks_crossing`. Promote V137 only as the disposable RTL_5V
sub-primitive; inherited zone/manufacturing/open-support findings remain
unclosed.

V138 and V139 reapply the earlier U1.34 RTL_3V3 handoff on V137. Both join
U1.34 to C3/R2/R3/U1.20 in saved-board connectivity. V138 shorts the promoted
RTL_5V source field; V139 avoids that field but crosses SPISO3. Reject both as
route-allocation evidence. U1.34 remains an open endpoint.
V140 moves the U1.34 source left and raises its B.Cu corridor. It still
shorts SPISO and leaves a crossing in native DRC, so it is rejected. The
remaining U1.34 issue is allocation of the shared QFN source field on the
promoted V137 basis, not missing saved-board connectivity.

## V141 M.2 SSD_3V3 contact-row sub-primitive

V141 joins J1.2/J1.4/J1.6/J1.8 on the V137 basis using native pad-derived
F.Cu segments. Native DRC reports no `shorting_items` or `tracks_crossing`;
the saved-board audit and trace-removal negative control pass. This is only
the M.2 contact collector. It does not close the SSD_3V3 source, inrush,
power-budget, or complete Path-B power gate.

## V142–V143 U1.34 RTL_3V3 source-field allocation

V142 raised the U1.34 B.Cu corridor but contacted the retained SPICS via and
is rejected. V143 moves the source outside the V137 RTL_5V field and takes a
higher outer B.Cu path. Native DRC reports no `shorting_items` or
`tracks_crossing`; the native audit joins U1.34/C3/R2/R3/U1.20 and the
trace-removal negative control fails as required. Promote V143 only as the
U1.34 disposable sub-primitive; complete Path-B closure is still open.

## V144 combined support basis

V144 starts from V143 and reapplies the V141 socket-contact collector. Native
saved connectivity and the negative control pass for both U1.34 RTL_3V3 and
J1.2/J1.4/J1.6/J1.8; native DRC has no `shorting_items` or
`tracks_crossing`. Six intended high-speed endpoint opens remain, and the
SSD_3V3 source/power gate is not closed.

## V145 REFCLK lower-corridor trial — rejected

V145 attempted ordinary-via REFCLK pair corridors below U1. Native DRC found
contacts/crossings with inherited XTAL/1V1/CLKREQ fields and J1 sideband pads.
This is route-allocation evidence only; the V144 support basis and RTL9210B
REFCLK authority remain valid, and REFCLK remains open.

V146/V147 are retained rejected REFCLK trials. V146's lower F.Cu corridor
entered the J1 TX pad field; V147's outer F.Cu corridors still crossed the
U1 exposed GND pad despite separating the J1 drops. These results identify a
QFN lower-edge/RTL_1V1 source-field allocation problem. The next experiment
must move or reauthor that local support field before another REFCLK sweep.

V148/V149 are rejected local-support relocation trials. V148 moved the lower
RTL_1V1 collector to B.Cu but crossed XTAL_IN; V149 added an F.Cu overpass but
still contacted XTAL_IN and C1 ground. The next attempt must co-author the
XTAL_IN and lower 1V1 fields together.

V150/V151 refine the below-XTAL collector. V150 preserves clean signal DRC
but leaves the lower 1V1 pads disconnected from the existing handoff; V151
corrects that handoff and passes the native 1V1 audit and negative control.
V152/V153 are rejected REFCLK trials against V151 for XTAL_IN and 1V1
contacts. V154 moves only the 1V1 handoff outboard and passes native DRC's
signal gate plus the complete 1V1 audit. Promote V154 as the current local
support basis; REFCLK remains open.
V155 is rejected: the split REFCLK_N escape contacted U1 pad 65 and the
outboard 1V1 handoff, while REFCLK_P contacted the XTAL_IN endpoint. V154
remains the validated local-support basis; the next REFCLK attempt must
co-author the endpoint/sideband allocation.
V156 moves only the CLKREQ_N J1 launch outboard and passes native signal DRC.
V157 moves XTAL_IN to an outboard endpoint but crosses the retained XTAL_OUT
vertical span. Reject V157; the next support attempt must co-author the two
crystal nets.
V158 moves XTAL_IN's transition inward and passes the crystal connectivity
audit/negative control with no signal DRC classes. V160 removes the old F.Cu
1V1 handoff and joins the complete 1V1 pad group directly to the existing
B.Cu rail. V162 is rejected as the first REFCLK attempt on this basis because
its N transition contacts XTAL_OUT/legacy 1V1 and the source escapes cross.
V160/V158 remain the coordinated-support basis; REFCLK is open.
V163 co-authors XTAL_OUT on an upper B.Cu span and attempts upper REFCLK
escapes. Native DRC rejects it for an exposed-pad contact, REFCLK-N/CLKREQ_N
shorting, a REFCLK-P/N source-field contact, and J1 launch clearance.
V164 separates the source drops and moves the N launch, removing short
classes but leaving six native crossings involving the old 1V1 bridge,
XTAL_OUT, CLKREQ, PEDET, and the J1 sideband field. V165 removes the
superseded 1V1 bridge and tries P on F.Cu/N on B.Cu; native DRC still finds a
REFCLK-P contact with U1 pad 62 and XTAL_OUT crossings. V166 moves P to B.Cu
above the QFN, but the source via contacts exposed GND, its B.Cu span
contacts moved XTAL_OUT, and the J1-side N transition is too close to TXP.
Preserve V163-V166 as rejected route-allocation evidence. No Path-A asset,
production CAD, layer policy, or electrical authority changed; the remaining
task is one pad-aware QFN/XTAL/REFCLK/J1 allocation.
V167 uses the measured QFN pad gaps for narrow REFCLK dogbones, but its lower
B.Cu exits cross the unchanged crystal routes and its J1 vias occupy the
0.5-mm REFCLK contact row. V168 moves both J1 transitions outboard and
removes REFCLK-P/N shorts; it still collides with XTAL, SPI, RTL_5V, and the
old 1V1 collector. V169 moves the upper pair above the SPI fields and has no
REFCLK-P/N shorting, but its remaining lower support and corridor crossings
prevent promotion. V170 places the complete upper span on F.Cu and is
rejected by RTL_3V3, lane, and XTAL contacts. V171 adds short F.Cu
overpasses at the B.Cu trunk crossings and is rejected by XTAL/RTL_3V3/
SSD_3V3 contacts. V169 is retained as the best disposable topology, not a
pass; V158/V160 remain the promoted support basis.
V173 translates the local U1/U2/crystal/rail support island upward by 8 mm
and regenerates REFCLK from transformed native pads, but stale external
local-net copper remains. V174 globally scrubs those superseded local nets
before applying the same placement and REFCLK cell. Native DRC has zero
`shorting_items` and zero `tracks_crossing`; its saved-board audit and
trace-removal negative control pass both REFCLK mappings. Promote V174 only
as a disposable translated REFCLK placement/topology sub-primitive. It is
not full Path-B support closure.
V176/V177 retain the east-side translated crystal cluster and fail at the
XTAL/REFCLK source field. V178 is an authoring-negative because it stacked a
second REFCLK route on the V174 copper. V179 removes all superseded local
routes, moves Y1/C1/C2/R1 west of U1, and regenerates the crystal, RSET, and
REFCLK paths once. The board-wide REFCLK/XTAL corridor conflict disappears;
four localized crystal/RSET/QFN source defects remain. Preserve V179 as the
best translated-placement candidate, not a pass.
V175 restores the validated V158 XTAL_IN/XTAL_OUT copper translated onto
V174. Native DRC shows the expected local co-allocation defects: REFCLK-P
contacts the translated XTAL_IN transition and REFCLK-N crosses the
translated XTAL_OUT span. Reject V175 as route implementation evidence;
V174 remains the clean REFCLK-only basis and the next trial must co-author
the translated crystal and REFCLK lower exits.
V172 keeps the V169 pair topology but drops the lower exits below the crystal
row. Native DRC still reports U2/SPISI/RTL3V3/RTL1V1/PEDET conflicts and one
P/N endpoint crossing, so it is rejected. The V169 native saved-connectivity
audit passes both REFCLK mappings (U1.61→J1.55 and U1.62→J1.53) and its
trace-removal negative control fails as required. This confirms the remaining
problem is physical corridor ownership, not missing REFCLK net authority.

## V76–V78 U1.40 edge-group trials — rejected

V76 placed the U1.40 RTL_1V1 transition at (92.8,68.8), where the via
shorted the retained RTL_3V3 left escape; native DRC reported 9 violations /
24 opens. V77 moved the transition to (90.8,68.8), but its B.Cu collector
crossed the retained RTL_3V3 diagonal and still shorted its via; native DRC
reported 8 violations / 24 opens. V78 tried an upper-perimeter escape and is
rejected at 14 violations / 24 opens for RTL_3V3/SPICLK crossings and
clearance into adjacent U1 pads. Preserve all three as negative evidence.
They reject these route allocations only; V75 remains the promoted partial
RTL_1V1 basis and U1.40 remains open.

## V79–V80 3V3 reallocation trials — rejected

V79 reallocated the left RTL_3V3 escape and tested U1.40. Native DRC reports
8 findings / 25 opens; the former U1.40/3V3 short is gone, leaving a U1.40
dogbone clearance defect against pad 41 and a 3V3 clearance defect at the
no-net U1.35 field. V80 moved the 3V3 segment again, but its endpoint
authoring left a dangling track and did not remove the U1.40 pad-field
clearance defect; native DRC remains 8 findings / 25 opens. Preserve both as
negative evidence. The next attempt must derive the complete 3V3 replacement
path and a pad-aware U1.40 dogbone together.

V81 tested that dogbone at 0.15 mm. It remains rejected: native DRC reports
10 findings / 25 opens, including 0.1647-mm clearance to U1.41, 0.100-mm
clearance from the reallocated 3V3 segment to U1.35, and two minimum-width
violations. The board's 0.200-mm routing rule is retained; a finer trace is
not an acceptable workaround.

V82 tested a diagonal U1.40 escape against the V79 reallocated 3V3 field.
Native DRC reports 11 findings / 25 opens: the diagonal shorts/crosses the
U1.39 RTL_3V3 pad escape and violates the adjacent U1.38 solder-mask/clearance
envelope. Preserve it as evidence that the U1.40 departure and neighboring
3V3 source field must be authored as one QFN escape cell.

V83 is a diagnostic-only pad-width sensitivity trial. Shrinking the 68
perimeter pads in the V79 disposable footprint did not clear the two local
signal defects; native DRC remained 8 findings / 25 opens. No land-pattern
promotion or board-rule change follows from this test.

## V84–V86 coordinated QFN/JLC source-field trials

V84 is rejected because the first JLC-rule candidate duplicated the U1.40
via, and V85 is rejected because its cleanup removed the retained 3V3 via,
leaving two dangling endpoints. V86 corrects both authoring defects: it keeps
the native 3V3 via, replaces the local source tracks coherently, and persists
the validated disposable JLC defaults (0.13208-mm minimum track and 0.15-mm
clearance) in the default netclass. Native DRC reports only 6 inherited
isolated-GND/silkscreen warnings; native saved connectivity joins U1.40 with
U1.16/U1.25/U1.50/C4.1. Promote V86 only as the U1.40/3V3 edge-group
sub-primitive, not as full RTL9210B support closure.

## V88–V95 bottom-edge RTL_1V1 trials

V88–V94 are retained rejected experiments: V88 shorted U1.55 into XTAL_OUT;
V89–V91 placed U1.60 in or too near XTAL_IN; and V92–V94 successively
exposed QFN-pad, XTAL-via, and corridor-ordering defects. V95 is the first
clean U1.60 result: its F.Cu dogleg reaches an x103.0/y73.8 transition, its
B.Cu route passes above XTAL_IN, and it drops at x107.0. Native DRC reports
only 8 inherited isolated-GND/silkscreen warnings; native saved connectivity
joins U1.60 to U1.16/U1.25/U1.40/U1.50/C4.1. Promote V95 only as the U1.60
edge-group primitive; remaining U1.36/U1.55/U1.63 and full support gates are
unfinished.

## V96 U1.63 shared launch — promoted sub-primitive

V96 joins U1.63 to the promoted U1.60 F.Cu launch without a new via or
XTAL/support route. Native DRC reports only the eight inherited
isolated-GND/silkscreen warnings; native saved connectivity joins U1.63 with
U1.16/U1.25/U1.40/U1.50/U1.60/C4.1, reducing the fixture to 23 opens. This is
only the U1.63 edge-group primitive; U1.36/U1.55 and full Path-B closure are
unfinished.

## V97–V99 XTAL_OUT/U1.55 trials — rejected

V97 reauthored XTAL_OUT as a B.Cu span above the support field and added the
U1.55 RTL_1V1 launch. It restored U1.55 connectivity but crossed the retained
RTL_1V1 drop at x107.0. V98 moved that drop right and crossed the XTAL_OUT
vertical endpoint; V99 attempted a B.Cu overpass but still crossed the
XTAL_OUT horizontal at the first vertical segment. All three are retained
rejected route-implementation evidence.

## V100 left-endpoint escape — promoted disposable sub-primitive

V100 starts from V97, removes the crossing RTL_1V1 drop, travels on B.Cu below
the XTAL_OUT span to x94.8, then drops around the XTAL_OUT left endpoint into
the existing RTL_1V1 collector. Native saved-board connectivity joins U1.55
with U1.16/U1.25/U1.40/U1.50/U1.60/U1.63/C4.1. A native same-layer,
different-net centerline scan reports no new track crossing for the escape.
The direct CLI report retains the disposable fixture's inherited zone,
hole, mask, thermal, and unconnected findings; those are not waived or
represented as a full support PASS. V100 is promoted only as the current
U1.55/XTAL support sub-primitive.

## V101/V102 U1.36 completion trials

V101 attempted a left-side U1.36 RTL_1V1 handoff and is rejected by native
KiCad: its via/escape shorted and crossed the retained RTL_3V3 source field.
V102 returns to V100 and routes U1.36 rightward to a native through-via and
the existing RTL_1V1 collector. Native DRC reports no `shorting_items` or
`tracks_crossing`; saved-board connectivity joins U1.36 with the complete
currently assembled U1.16/U1.25/U1.40/U1.50/U1.55/U1.60/U1.63/C4.1 group.
V102 is promoted only as the disposable 1V1 edge-group basis; remaining
RTL9210B controls, grounds, USB, M.2, power, firmware, and full validation
remain open.

## V320 normalized M.2 footprint frame — retained authoring basis

V320 normalizes the disposable J1 M.2 footprint coordinate frame. The prior
fixture encoded its 13 pad locations as board-absolute positions while the
footprint anchor was `(0,0)`. The generator now assigns a real `(127,66)`
anchor and explicitly preserves the absolute pad centers; a native reload
assertion passes for every pad. This is a valid authoring correction, not a
routing or Path-B closure: native DRC remains the inherited V311 state with
18 opens and no new signal short/crossing class. Production CAD is unchanged.

## V314–V317 coordinated-field probes — rejected implementations

V314 tested RTL_1V1, V315 RTL_3V3, and V316/V317 lane-0 escapes from V311.
They reduced native open counts but introduced real shorts/crossings, so all
are rejected route-implementation attempts. V311 remains the retained
disposable basis; no Path-A or production CAD changed.

## V318/V319 coordinated In2 rail trials — rejected implementations

V318/V319 moved RTL_5V, RTL_1V1, and RTL_3V3 onto the contract-designated
In2.PWR layer from V311. Corrected native endpoints reduced the open count to
15, but the proposed vias and inner-layer corridors collided with retained
SPI/PEDET copper, U2 pads, and J1 SSD_3V3. Native DRC reported 7/11 real
shorting/crossing classes across the two trials. The experiment confirms
inner-layer power is available in principle, but does not provide a usable
append-only route. The next candidate must co-author rails and lane-0 with a
precomputed via map.

## V302 CLKREQ alternate launch — rejected implementation

V302 shifts the R3 launch west and transitions the U1-side branch below the
PERST launch. Native DRC finds real CLKREQ/PEDET shorting at R2 and
CLKREQ/ISOLATEB shorting at U1. It is rejected despite reducing the native
open count to 18; the next implementation must preserve adjacent net fields.

## V299/V300 PEDET sideband correction — retained, not promoted

V299 removes the PEDET/PERST crossing class with a U-shaped approach around
the PERST endpoint, but native connectivity exposed a floating J1 branch.
V300 adds the missing same-net join from the x=109 F.Cu dogleg to the existing
J1 branch via. Native connectivity joins R2.1, U1.8, and J1.69. Native DRC
reports 454 findings / 20 inherited opens with zero `shorting_items`, zero
`tracks_crossing`, and zero footprint errors. PEDET is closed for this
disposable sideband basis; CLKREQ, reset, remaining rails, and high-speed
support remain open.

## V294 PEDET east-side landing — retained, not promoted

V294 approaches U1.8 from an east-side F.Cu dogleg after the PEDET B.Cu trunk
transitions at x=106 mm. It avoids the earlier REFCLK crossing, but native
DRC retains one PEDET/PERST crossing at the U1 landing. The route is retained
as a local basis; PEDET is not closed until the PERST/PEDET field is coordinated.

## V289 combined five-net SPI audit — retained basis

Because V289 is chained from V278, V282, V286, and V288, its saved board
contains all five SPI routes. The native five-net endpoint audit passes all
five U1/U2 mappings, and the trace-removal negative control fails as required.
The board DRC summary is 420 findings / 22 inherited opens with zero
`shorting_items`, zero `tracks_crossing`, and zero footprint errors. This
closes the disposable five-net SPI routing subtask, but does not close the
RTL9210B support field or Path B.

## V289 SPISI high-north corridor — retained, not promoted

V289 routes actual U1.18=(101.2,58.05) to U2.5=(88.1,70.0) through a
separate high-north B.Cu corridor. Native connectivity passes. Native DRC
reports 420 findings / 22 inherited opens with zero `tracks_crossing`, zero
`shorting_items`, and zero footprint errors. V289 is retained as the SPISI
basis; remaining support and high-speed routes remain open.

## V288 SPICLK short-escape corridor — retained, not promoted

V288 uses the actual U1.19=(100.8,58.05) and U2.6=(89.3,70.0) endpoints,
placing the source via at (100.8,57.5) before the RTL_3V3 handoff and using
the retained high-north B.Cu destination corridor. Native connectivity
passes. Native DRC reports 402 findings / 23 inherited opens with zero
`tracks_crossing`, zero `shorting_items`, and zero footprint errors. V288 is
retained as the SPICLK basis; SPISI, PEDET, reset, remaining rails, and
high-speed support remain open.

## V287 SPICLK high-north trial — rejected implementation

V287 attempted an isolated SPICLK corridor from U1.19=(100.8,58.05) to
U2.6=(89.3,70.0). Its high-north B.Cu destination corridor did not add a
new lower-field crossing, but the source escape crossed the retained
RTL_3V3 handoff in the U1 pad field. It is rejected as a route-implementation
trial; remaining SPI source escapes require coordinated allocation.

## V284 SPISO3 high-north trial — rejected implementation

V284 moved the SPISO3 corridor above the lower SPI field, but its U1 north
escape crosses the C1 ground pad in the crystal-support field. Native DRC
reports a SPISO3/GND shorting class. This is a route-implementation failure;
the next experiment must allocate the remaining SPI channels together.

## V103/V104 U1.34 RTL_3V3 handoff trials — rejected

V103 attempted a left dogbone and B.Cu diagonal but targeted the wrong layer
endpoint, so native connectivity left U1.34 isolated. V104 corrected the
endpoint to the existing RTL_3V3 via at (100.4,60.8) and native connectivity
joined U1.34 to C3/R2/R3/U1.20, but native DRC reported two real track
crossings. Both are retained as route-authoring evidence; V102 remains the
promoted disposable basis and U1.34 remains open.

V105 kept the handoff above the SPI channels but its B.Cu vertical crossed
SPICLK and SPISI. V106 keeps the U1.34 departure on F.Cu until clear of those
channels, then transitions to the existing 3V3 via field. Native DRC reports
no `shorting_items` or `tracks_crossing`, and saved-board connectivity joins
U1.34 to the existing C3/R2/R3/U1.20 group. Promote V106 only as the
disposable U1.34 edge-group basis; full Path-B support remains open.

## V107–V111 control-sideband trials — rejected

V107 shorted adjacent CLKREQ_N/PERST_N vias. V108 and V109 moved the vias but
crossed the retained RTL_1V1/RTL_3V3 field. V110 used F.Cu monotonic paths but
the two control departures crossed each other at the QFN edge; V111 split the
transitions but still crossed the retained 1V1 field and companion control
route. Preserve these as route-allocation evidence only. The next trial must
use genuinely layer-separated launches.

V112 is the first genuinely layer-separated control attempt. It removes the
control-control shorts, but native DRC still reports three crossings against
the inherited RTL_1V1/RTL_3V3/upper-rail fields. It is rejected as a route
implementation trial; no architecture or layer-policy change follows.
V113 reduced the layer-separated trial to one RTL_3V3 crossing. V114 removed
that crossing but left CLKREQ_N/PERST_N clearance contact. V115 widens the
separation and passes the focused control-pair gate: native connectivity joins
U1.13 to J1.52 and U1.14 to J1.50, with no `shorting_items` or
`tracks_crossing`. Promote V115 only as the disposable control-pair
sub-primitive; PEDET and remaining Path-B endpoints stay open.
V116 adds the PEDET U1-to-M.2 launch on an independent F.Cu corridor. Native
connectivity joins U1.8 to J1.69 and native DRC reports no `shorting_items` or
`tracks_crossing`. Promote V116 only as the disposable U1-to-socket PEDET
sub-primitive; R2 source connection and remaining Path-B endpoints stay open.
V117 electrically joined R2 but crossed two SPI traces. V118 moved the source
outboard but crossed the 1V1 return wall; V119 moved below that wall but
introduced PEDET/ground and PEDET/1V1 defects. V120 removed the field crossings
but crossed XTAL_IN; V121 removed that crossing but left a 0.125-mm C2
clearance defect. V122 shifts the bottom return right and passes the focused
native PEDET audit: R2.1/U1.8/J1.69 are connected, and the trace-removal
negative control fails as required. Promote V122 only as the disposable
complete PEDET sub-primitive; remaining Path-B gates stay open.

V123/V124 joined R3.1 electrically but crossed existing SPI/PEDET/1V1 fields.
V125/V126 moved the return right but contacted C5/RTL_3V3; V127/V128/V129
reduced the defect to the PERST elbow, and V130 reduced it to one upper-rail
crossing. V131 overpasses that rail and passes the focused CLKREQ audit:
R3.1/U1.13/J1.52 are connected, with no `shorting_items` or
`tracks_crossing`; the route-removal negative control fails as required.
Promote V131 only as the disposable complete CLKREQ sub-primitive; RESET_N,
RTL_5V, high-speed links, and full Path-B validation remain open.

## Current authoritative baseline

V31 is the current best complete five-net SPI source/target primitive. It
uses native saved-pad coordinates and separates SPISO3, SPISO, and SPICS from
the retained V24 SPISI/SPICLK/RTL_3V3 field. Native DRC reports only inherited
GND-fill/silkscreen findings (4 total), with no SPI signal violations; the
saved-board positive and trace-removal negative-control audits pass all five
SPI nets. This does not close support because the V24 base has no XTAL/RSET
joins. V32 is retained as a rejected support implementation (11 violations /
35 opens): its F.Cu support paths crossed each other and the local passive
pad field. The next candidate must allocate support and rails coherently
around V31 rather than append the V32 paths.

V33 tested B.Cu long-span XTAL/RSET handoffs with local F.Cu dogbones. It is
rejected at 15 native violations / 35 opens: the handoff vias and local
dogbones entered the C1/Y1 passive field and crossed one another. This is a
support-island placement/authoring failure, not a rejection of the V31
five-net SPI primitive or the RTL9210B architecture.

V35 is the first combined V31-support candidate with a clean local result.
The coherent +4/+3-mm move keeps Y1/C1/C2/R1 inside the fixture outline and
separates the U1-side handoffs. Native DRC has only four inherited
GND/silkscreen findings; the five-net SPI audit and XTAL_IN/XTAL_OUT/RSET
support audit both pass, and both trace-removal negative controls fail. This
does not close the remaining RTL9210B rail, control, USB, M.2, or power gates.

V36 broad F.Cu rail-zone probe is rejected. It leaves RTL_3V3/RTL_5V/RTL_1V1
pad joins open in the saved-board connectivity report and adds no acceptable
replacement for explicit rail access; native DRC reports five findings,
including the inherited GND thermal warning. The zone shortcut is not
promoted, and V35 remains the support/SPI baseline.

V38 corrected the malformed C3/C4/C5 footprints using ordinary local
SMD-coordinate CAD and introduced no DRC regression. V39 added a native
RTL_5V route to corrected C5, but native DRC reports two real crossings with
the retained RTL_3V3/SPI corridor. It is rejected as a route implementation;
the next attempt must co-author the 3V3 and 5V fields.

V41 added a local RTL_3V3 fanout without changing the validated SPI or
XTAL/RSET paths. Native DRC reports 7 findings / 30 opens. It is rejected for
one U1 pad-field clearance, one XTAL_IN-adjacent via, and an RSET-via conflict
on the U2 branch; the next attempt must partition the source and downstream
3V3 branches.

V42 partitioned the RTL_3V3 source and U2 branches and restored the validated
U1.20/C3 trunk. Native DRC reports 6 findings / 31 opens; the prior U1
pad-field defect is gone, but one RSET-adjacent via remains dangling/too
close. It is not promoted; the partition is retained as the next rail-pad
join basis.

V44 removes the redundant same-layer V43 via and has only the inherited
GND/silkscreen DRC findings. The saved-board 3V3 connectivity is partial:
U1.34/U1.39/U2.3/U2.8 are joined, U1.20/C3 remains a separate trunk, and
U1.52 is open. V45's attempted U1.52 handoff is rejected at 10 findings /
30 opens for XTAL_IN-via clearances. Further work must relocate the handoff
or regenerate the U1.52/XTAL_IN source field together.

V46 co-authored XTAL_IN and U1.52 from V44 but is rejected at 9 native
violations / 30 opens. The new transitions collide at the 0.4-mm QFN pitch,
including XTAL_IN/RTL_3V3 shorts and crossings. V44 remains the cleanest
partial 3V3 result; further work must rotate or coherently relocate the local
support field.

V47 is a successful authoring-path correction, not a routing closure. The
disposable U1 footprint had a malformed transformed frame: its anchor was at
(36,150) while its pads were physically authored near (98,70). The V47
generator records the saved absolute pad locations, normalizes the footprint
anchor, and restores those pad locations after the transform. Reloaded native
coordinates match the pre-transform pad field for U1.18/U1.20/U1.22 and
U1.51-U1.54. Native DRC returns to 4 inherited GND/silkscreen findings / 31
opens with no new signal violations. Use V47 as the stable basis for the next
coherent rail/support authoring pass; do not treat its intended opens as a
complete RTL9210B support PASS.

V49 is the cleanest follow-on handoff from the corrected frame. It routes
U1.52 around the existing XTAL_IN lower-left field and joins U1.52 to the
U1.34/U1.39/U2 branch with native DRC at the inherited 4-warning / 30-open
baseline. V50 attempted to join the R2/R3 rail taps and U1.20/C3 with a
straight F.Cu collector; it is rejected at 7 findings / 28 opens for real
crossings with retained SPISO, SPICS, and SPISO3. This is a route allocation
failure, not evidence against the corrected footprint or the RTL_3V3 net.

V51 is rejected at 15 native findings / 28 opens. Its R2/R3 escapes ran into
the opposite-net pads because the resistor pad orientation was not respected,
and its B.Cu collector conflicted with the retained SPISO3 transition. Keep
this as negative evidence; V49 remains the cleanest handoff basis. The next
rail pass must derive resistor pad sides from the saved footprint and allocate
a collector corridor that is clear of SPI.

V52 is the first successful complete RTL_3V3 rail join in this series. It
normalizes the R2/R3 footprint frames, escapes their verified RTL_3V3 pad 2
sides, and uses a B.Cu collector clear of the retained SPI transitions. Native
DRC reports 5 non-signal isolated-copper/silkscreen warnings / 28 intended opens; saved-board connectivity
joins U1.20/U1.34/U1.39/U1.52, U2.3/U2.8, R2.2, R3.2, and C3.1. Promote V52 as
the current disposable 3V3 basis, while retaining the remaining rail/control
opens as unfinished work.

V59 corrects the V58 1V1 launch by routing U1.16 through a B.Cu dogleg below
the 3V3 handoff and entering C4.1 from the right, clear of C3. Native DRC
reports 5 non-signal isolated-copper/silkscreen warnings / 27 intended opens
and no new signal violations. V59 is promoted only as the U1.16/C4.1
sub-primitive; the other RTL_1V1 pad groups remain unfinished.

V60 is rejected at 35 native findings / 20 opens. Its full perimeter collector
crossed retained XTAL_IN/XTAL_OUT/RSET and SPI fields and violated the local
3V3 clearance at a left-edge via. Keep it as negative evidence only; V59 is
the current promoted U1.16/C4.1 sub-primitive, and the remaining 1V1 groups
must be allocated in separate native corridors.

V63 validates the U1.25 RTL_1V1 top-edge sub-primitive. Its F.Cu escape is
offset left of SPICS before entering the upper B.Cu perimeter, which joins the
existing C4.1 right-side route. Native DRC reports 5 non-signal
isolated-copper/silkscreen warnings / 26 intended opens and no new signal
violations. Promote V63 only as this U1.25/C4.1 sub-primitive; remaining 1V1
groups are unfinished.

V75 validates the U1.50 RTL_1V1 left-edge sub-primitive. Moving the collector
below the RTL_3V3 handoff removes V74's only signal crossing; native DRC is 6
non-signal isolated-copper/silkscreen warnings / 25 intended opens, and saved
connectivity joins U1.50/U1.16/U1.25/C4.1. Promote V75 only as this edge-group
primitive; the remaining RTL_1V1 groups are unfinished.

V64 is rejected at 8 native findings / 26 opens. The U1.60 bottom-edge drop
entered the retained XTAL_OUT B.Cu segment at y=77 and did not clear the local
XTAL/RSET corridor. Preserve it as negative evidence; V63 remains the current
promoted 1V1 basis and future bottom-edge routes must avoid XTAL_OUT entirely.

V65 is rejected at 15 native findings / 26 opens. The U1.55 rightward escape
entered adjacent no-net U1.56 and its transition violated clearance to the
XTAL_OUT via/segment. Preserve it as negative evidence; U1.55 needs a new
local source-field allocation rather than another direct bottom drop.

V68 is rejected at 7 native findings / 26 opens. The U1.60 F.Cu leg was
clear of XTAL_OUT but intersected the retained XTAL_IN launch near x=107.5;
the C4-side B.Cu join was otherwise clear. U1.60 therefore needs a coherent
XTAL/support-field relocation or a different source-side layer escape.

V69 is a diagnostic discriminator, not a support PASS. Removing only the
obstructing XTAL_IN copper permits the U1.60 RTL_1V1 corridor with no signal
DRC violations; its 6 findings / 28 opens are the deliberately disconnected
XTAL_IN/support path, one dangling diagnostic endpoint, and inherited
non-signal warnings. The result confirms a local XTAL/support placement
collision and supports coherent relocation.

V70 is rejected at 18 native findings / 27 opens. The moved Y1/C1/C2/R1
island was placed too close to the board edge, while its regenerated
XTAL_IN/XTAL_OUT/RSET paths had local clearance/short issues. Preserve this
as a relocation failure; V69 remains the diagnostic proof that U1.60 routing
is feasible after clearing XTAL_IN.

V72 is rejected at 51 native findings / 30 opens. The upper-right support
placement had usable board-edge margin, but regenerated XTAL/RSET paths were
based on guessed transformed pad coordinates and collided with local
XTAL/rail/SPI geometry. Preserve it as authoring evidence; future relocation
work must inspect post-transform native pad positions before routing.

V73 used the extracted post-transform endpoints, but is rejected at 32 native
findings / 28 opens. Its long RSET perimeter crosses retained SPI/3V3 fields,
and the U1-side XTAL_IN departure is too close to RTL_3V3. The endpoint
authoring defect is fixed; the next class must split support routes into
shorter local corridors.

V57 completes the RTL_5V disposable rail primitive. Its U1.33-to-U1.17
F.Cu escape passes above the native SPI source endpoints, then uses the
SPI-clear B.Cu dogleg and a right-side C5.1 launch. Native DRC reports 5
non-signal isolated-copper/silkscreen warnings / 26 intended opens, and
saved-board connectivity joins U1.17/U1.33/C5.1. Promote V57 as the current
RTL_5V basis; the remaining rail/control opens are unfinished.

V40 jointly reauthored the 3V3/5V rail spines. Native DRC reports 8 findings,
including a new RTL_3V3/SPISO3 source collision and retained RTL_5V/SPISI and
C5-handoff conflicts. It is rejected; the next rail class must keep the V24
3V3 source departure and add partitioned access around it.

V37 added explicit rail pad-to-via dogbones and shaped B.Cu rail fields. It is
rejected at 41 native violations / 34 opens because the via fanout enters the
QFN SPI/source field and neighboring rail pads. The result is preserved as
rail-access evidence; V35 remains the validated local baseline.

V8 is the current combined support/SPI baseline and V9 is the retained
RTL_5V rail primitive. V10/V11 RTL_3V3 trunks are rejected because they
intersect retained high-speed/support corridors. The next experiment must
change the 3V3/support corridor or coherently reauthor that local island.

The 90-degree mixed-layer V18/V19/V20/V21 trials remain disposable evidence.
V20 reduced the source-field result to 3 findings / 41 opens; V21 rejected a
down/right RTL_3V3 departure after it entered adjacent U1 RTL_5V/RTL_1V1 pads
and crossed SPICLK. The next implementation requires a transformed-pad-aware
escape cell.

## 90-degree transformed diagonal V22 — rejected

V22 moved the RTL_3V3 source through a diagonal transformed-pad-aware probe.
Native KiCad reports 9 violations / 41 opens: the departure collides with
SPISO3/SPICS and crosses the SPICLK B.Cu channel. V20 remains the best
implementation baseline; a formal escape-cell construction is still needed.

## 90-degree formal source field V24 — local PASS

V24 moves the SPISI transition outside the measured SPICLK clearance envelope
while retaining the mixed-layer channel plan. Native KiCad reports 2 inherited
findings / 41 opens and no signal shorts, crossings, or clearance violations.
Saved-board native checks pass SPISI, SPICLK, SPISO3, and RTL_3V3 endpoints;
removing a required SPISI segment fails the negative control. V24 is a local
source-field baseline, not full RTL9210B fixture closure.

## Complete SPI from V24 V25 — rejected

V25 added SPISO and SPICS to the V24 source baseline. Native KiCad reports 4
violations / 39 opens: SPISO crosses the SPISO3 F.Cu escape and SPICS enters
that source corridor. V24 remains the valid four-net source baseline; the
remaining channels require a source-field-aware layer swap.

The native escape-cell map utility now records the transformed U1 pad centers,
orientations, dimensions, and package-center outward vectors in
`PHASE24_RTL9210B_ESCAPE_CELL_MAP_NATIVE_V15.txt`. This map is the source for
the next generator iteration.

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

## V180–V184 crystal/RSET local repair

V180–V183 were rejected as localized route implementations: V180 had an
RSET/XTAL_OUT crossing and RTL_1V1 source short; V181/V183 moved the
conflict onto the XTAL_IN or XTAL_OUT transition; V182 removed the short
but retained an F.Cu crossing. V184 moves the RSET transition into the gap
above XTAL_OUT and keeps the RSET trunk on B.Cu below the crystal island.
Native KiCad DRC reports zero `shorting_items` and zero `tracks_crossing`.
The saved-board V184 audit passes XTAL_IN, XTAL_OUT, RSET, REFCLK_P, and
REFCLK_N, with five trace-removal negative controls. V184 is promoted only
as a disposable support sub-primitive; inherited manufacturing/clearance/
open findings and the remaining Path-B support gates remain open.

## V186 RTL_3V3 shared U1.20 launch

Consultant review of V185 identified U1.20 as the next clean same-net
extension and warned that U1.39/U1.52 are in the west-field crystal/RSET
placement conflict. V186 adds only a vertical F.Cu stub from native U1.20
pad coordinates `(100.4,58.05)` to `(100.4,56.5)` and a 0.6/0.3-mm via
onto the existing V185 B.Cu RTL_3V3 rail. Native DRC reports 259 findings /
30 unconnected items, with zero `shorting_items` and zero
`tracks_crossing`. The saved-board audit joins U1.20/U1.34/C3.1 and its
trace-removal negative control fails as required. V186 is promoted as a
disposable shared-rail sub-primitive; U1.39/U1.52/U2.3/U2.8/R2.2/R3.2 and
the remaining Path-B support gates remain open.

## V189 SPICS U1.24-to-U2.1 handoff

V189 adds the SPICS route from native U1.24 to U2.1 through an upper
F.Cu/B.Cu/F.Cu outer corridor. Native KiCad reports 293 findings / 27
unconnected items, with zero `shorting_items` and zero `tracks_crossing`.
The saved-board audit joins U1.24/U2.1 and its trace-removal negative
control fails as required. V189 is promoted as a disposable SPI
sub-primitive; the remaining SPI nets, rail branches, controls, and full
Path-B validation remain open.

## V188 RTL_1V1 U1.16-to-C4.1 handoff

V188 adds a separate right-edge RTL_1V1 corridor from native U1.16 to C4.1
on the V187 basis, between the previously promoted upper rail corridors.
Native KiCad reports 282 findings / 28 unconnected items, with zero
`shorting_items` and zero `tracks_crossing`. The saved-board audit joins
U1.16/C4.1 and its trace-removal negative control fails as required. V188
is promoted as a disposable rail sub-primitive; the remaining RTL_1V1
collector, west-field RTL_3V3, SPI/control, and full Path-B validation remain
open.

## V187 RTL_5V U1.33-to-C5.1 handoff

V187 adds the separate upper RTL_5V corridor from native U1.33 to C5.1 on
the V186 basis. Native KiCad reports 270 findings / 29 unconnected items,
with zero `shorting_items` and zero `tracks_crossing`. The saved-board audit
joins U1.33/C5.1 and its trace-removal negative control fails as required.
V187 is promoted as a disposable rail sub-primitive; the remaining RTL_5V
branch, RTL_1V1, west-field RTL_3V3, SPI/control, and full Path-B validation
remain open.

## V185 RTL_3V3 U1.34-to-C3.1 handoff

V185 adds only the native-pad-derived U1.34-to-C3.1 RTL_3V3 rail slice to
the promoted V184 support basis. It exits the rotated QFN on F.Cu, changes
to B.Cu outside the pad field, and returns at C3.1. Native KiCad reports
254 findings / 31 unconnected items, with no `shorting_items` or
`tracks_crossing`; the increase in total findings is inherited
clearance/zone/open reporting from the added copper, not a signal short or
crossing. The saved-board audit joins U1.34 to C3.1 and its trace-removal
negative control fails as required. V185 is a promoted disposable rail
sub-primitive; the remaining 3V3 branches, support rails, SPI/control, and
full Path-B validation remain open.

## V201 SPISI route — rejected

V201 tested U1.18 SPISI to U2.5 from the promoted V200 basis. Native
connectivity and the trace-removal negative control passed, but native DRC
found SPISI contact to C1 ground at the destination and SPISI/SPICLK source
shorting/crossing at the QFN escape. This is a coupled SPI source/destination
allocation failure; no production CAD or Path-A architecture changed.

## V198–V200 SPICLK/crystal allocation

V198 retained the V193 support placement and moved XTAL_IN left, but the
straight SPICLK column contacted Y1.1. V199 translated Y1/C1/C2/R1 east by
2 mm and regenerated all crystal/RSET routes; it removed the shorts but
left an RSET/XTAL_OUT crossing. V200 corrected only the RSET transition to
the validated y=67.5 gap. Native KiCad reports 318 findings / 26
unconnected items for V200, with zero `shorting_items` and zero
`tracks_crossing`. The saved-board audit passes XTAL_IN, XTAL_OUT, RSET,
and SPICLK, with four trace-removal negative controls. V200 is promoted as
the disposable crystal/SPICLK basis; remaining SPI/control and Path-B gates
remain open.

## V283 SPISO3 trial — rejected implementation

V283 attempted a split-layer SPISO3 corridor from actual U1.22 to U2.7.
Native DRC found SPISO3/SPISO and SPISO3/GND shorting classes plus a
source-field crossing with RTL_3V3. This is a route-implementation failure
from independently adding a third channel to the V278/V282 corridors; it is
not evidence against the support placement. The next SPI experiment must
allocate all remaining channels together.

## V197 coherent crystal/SPI west shift — rejected

V197 moved Y1/C1/C2/R1 west as one support cluster, regenerated XTAL_IN,
XTAL_OUT, RSET, and retried SPICLK. The native saved-board audit passed all
four asserted net groups with negative controls, but native DRC reported
315 findings / 27 unconnected items including an XTAL_OUT/SPICS crossing,
SPISO contact to C2 ground, and a new SPICS/XTAL_OUT collision at the moved
C2 pads. This placement class is rejected; it does not justify changing the
accepted Path-B architecture. The next attempt must co-author the complete
SPI/crystal destination field rather than shifting only the crystal cluster.

## SPICLK V194–V196 route allocation — rejected

V194 shorted adjacent U1.18 SPISI and crossed XTAL_IN. V195 attempted the
consultant-recommended source reshape plus XTAL_IN via relocation, but the
new crystal transition contacted XTAL_OUT and U1.52 and still crossed the
SPICLK corridor. V196 retained the validated V193 crystal geometry and
doglegged SPICLK around the XTAL_IN via; native DRC still found C2 ground
contact and an XTAL_OUT crossing. All three are rejected route
implementations. The evidence now supports a coordinated local
crystal/SPI-field relocation or co-authored escape; no production CAD or
Path-A architecture changed.

## SPISO V190–V193 route allocation

V190 and V191 were rejected after native DRC found source-field and
destination-corridor shorts/crossings. V192 cleared the source field but
hit the RSET support pad at `(83.4,66.0)`. V193 moved the destination
dogleg above that pad band while retaining the threaded source escape.
Native KiCad reports 308 findings / 26 unconnected items for V193, with zero
`shorting_items` and zero `tracks_crossing`. The saved-board audit joins
U1.23/U2.2 and its trace-removal negative control fails as required. V193 is
promoted as a disposable SPISO sub-primitive; the other SPI/control nets and
full Path-B validation remain open.
## V202–V208 coordinated SPI/crystal source-field allocation

V202 co-authored SPICLK, SPISI, RTL_3V3, and XTAL_IN from the V200 basis.
Native DRC reported 338 findings / 25 unconnected items; the remaining
signal-specific defect was XTAL_IN contacting C1 ground. V203's east C1 move
was rejected after 352 DRC findings exposed multiple XTAL field conflicts.
V204/V205 moved C1 downward; V205 corrected the omitted Y1.1 branch in the
audit, but native DRC still found an XTAL_IN/XTAL_OUT conflict. V206 retained
the source-field approach but still contacted Y1.1/C1 ground. V207 removed
the signal-specific DRC defects, while its first audit correctly exposed that
the intentional XTAL_IN branch to Y1.1 had not been authored in the test
fixture.

V208 adds that explicit branch and reruns the saved-board audit. Native DRC
reports 337 findings / 25 unconnected items with zero `shorting_items` and
zero `tracks_crossing`. Native connectivity passes the asserted RTL_3V3,
SPICLK, SPISI, and XTAL_IN groups; four trace-removal negative controls fail
as required. V208 is promoted as the current disposable coordinated
SPI/crystal source-field basis. The remaining RTL9210B support/control nets,
full mode validation, and production integration remain open. Path A,
production CAD, and the accepted macro-floorplan are unchanged.
## V209–V211 SPISO3 U1.22-to-flash allocation

V209 attempted a direct F.Cu outboard SPISO3 departure and failed at the U1
source field, crossing the retained RTL_1V1/SPISO escape. V210 moved the
departure through an ordinary-via B.Cu handoff and preserved native endpoint
connectivity, but native DRC still found one real SPISO3/SPISO source-field
short. V211 changed only the local dogbone to a diagonal departure before
the via. Native connectivity and the trace-removal negative control pass;
native DRC reports 357 findings / 24 unconnected items with no
`shorting_items` or `tracks_crossing`. V211 is promoted as a disposable
SPISO3 sub-primitive. Remaining RTL9210B support/control, high-speed,
mode-aware, firmware, and production gates remain open.
## V212 PEDET U1.8-to-M.2 contact 69

V212 adds the RTL9210B PEDET sideband from native U1.8 to the M-key socket's
contact 69 using a short F.Cu source dogbone, an ordinary-via B.Cu trunk, and
a connector-side F.Cu return. Native KiCad DRC reports 370 findings / 23
unconnected items with zero `shorting_items` and `tracks_crossing`. The
saved-board audit joins U1.8/J1.69 and its trace-removal negative control
fails as required. V212 is promoted as disposable PEDET evidence only;
remaining reset/clock-request, support, high-speed, mode, firmware, and
production gates remain open.
## V213–V215 complete PEDET support return

V213 correctly joined U1.8, R2.1, and J1.69 but crossed the retained SPISI
and REFCLK/RTL_5V corridors. V214 moved the branch above the SPI field but
still crossed the long B.Cu REFCLK_P and RTL_5V spans. V215 carried the R2
return around those outboard corridor ends. Native DRC reports 381 findings /
22 unconnected items with zero `shorting_items` and `tracks_crossing`.
Native connectivity joins U1.8/R2.1/J1.69 and its trace-removal negative
control fails as required. V215 is promoted as the complete disposable PEDET
support slice; remaining Path-B controls, rails, high-speed, mode, firmware,
and production gates remain open.
## V216–V221 CLKREQ allocation

V216 connected U1.13 to J1.52 but crossed SPISO3 and entered J1 PERST pad
50. V217 moved the connector dogleg but retained a PEDET/source-field
crossing. V218 moved the source transition early, but crossed REFCLK_N.
V219 moved below the REFCLK corridor and hit the adjacent RTL_1V1 launch.
V220 is the clean partial slice: native U1.13-to-J1.52 connectivity and the
trace-removal negative control pass, with native DRC reporting 402 findings /
21 opens and no signal shorting/crossing classes. V221 added R3.1 but
reintroduced PEDET/XTAL conflicts. V220 is retained only as partial evidence;
the complete CLKREQ support return remains open.

## V222–V225 PERST allocation

V222 connected U1.14 to J1.50 but crossed SPISO3. V223 moved the transition
left but shorted REFCLK_N and ISOLATEB. V224 moved above the adjacent field
but contacted the no-connect pad 15. V225 moved horizontally before rising;
native connectivity and the negative control pass, but native DRC still
reports a PERST/RTL_1V1 source crossing. All four are rejected route
implementations. The PERST source field requires a coordinated local
allocation with the adjacent QFN control/rail escapes; no Path-A or
production-CAD change is justified.
## V226 PERST upper B.Cu detour — rejected

V226 kept the U1.14 horizontal exit clear of the adjacent RTL_1V1 launch and
used an upper B.Cu detour, but the transition via and first B.Cu segment
landed on the retained REFCLK_P horizontal. Native endpoint connectivity and
the trace-removal negative control pass; native DRC reports a real
REFCLK_P/PERST_N short/crossing. This confirms that PERST requires a coupled
REFCLK/QFN source-field allocation. It is rejected as a route
implementation; no Path-A or production-CAD change occurred.
## V227 coordinated SPISO3/PERST QFN source-field repair

V227 removed the prior disposable SPISO3 and PERST route implementations and
co-authored both source fields. SPISO3 moves to an outboard F.Cu column;
PERST exits U1.14 through the newly cleared F.Cu lane, transitions below the
PEDET trunk, and launches to J1.50. Native connectivity passes both
SPISO3/U1.22-to-U2.7 and PERST/U1.14-to-J1.50 assertions. Both trace-removal
negative controls fail as required. Native DRC reports 392 findings / 21
unconnected items with zero `shorting_items` and zero `tracks_crossing`.
V227 is promoted as a disposable coupled-source-field basis. R3.1/CLKREQ,
remaining rails, high-speed paths, mode, firmware, and production gates
remain open.
## V228 CLKREQ completion attempt — rejected

V228 added U1.13, R3.1, and J1.52 to the V227 coupled basis. Native
connectivity and the trace-removal negative control pass, but native DRC
reports 426 findings / 19 opens with CLKREQ crossing/shorting the retained
RSET, REFCLK_N, and PERST corridors. This is a three-net local sideband
allocation failure; V227 remains the promoted SPISO3/PERST basis and no
production or Path-A change occurred.
## V229–V231 complete CLKREQ corridor

V229 separated CLKREQ by transitioning from B.Cu to F.Cu around PERST, but
the R3 return crossed XTAL_IN and the F.Cu run crossed SPISO3. V230 moved the
R3 join below XTAL/RSET and added a short F.Cu overpass, leaving one RSET
crossing. V231 moved only the R3 vertical farther west. Native connectivity
joins U1.13/R3.1/J1.52; the trace-removal negative control fails as required.
Native DRC reports 435 findings / 19 unconnected items with zero
`shorting_items` and zero `tracks_crossing`. V231 is promoted as the
disposable complete CLKREQ basis. Remaining rails, high-speed paths, mode,
firmware, and production gates remain open.
## V232 RTL_3V3 U1.39 branch

V232 joins native U1.39 into the promoted RTL_3V3 trunk at the existing
3V3 support field using an F.Cu left escape and B.Cu handoff. Native
connectivity joins U1.39/C3.1 and the trace-removal negative control fails as
required. Native DRC reports 448 findings / 18 unconnected items with zero
`shorting_items` and zero `tracks_crossing`. V232 is promoted as disposable
rail evidence; remaining RTL_3V3/RTL_1V1 branches and all other Path-B gates
remain open.
## V233 RTL_3V3 U1.52 branch — rejected

V233 connected U1.52 to C3.1 in saved-board native connectivity and passed
its trace-removal negative control, but native DRC found an RTL_3V3/CLKREQ
via short and an RTL_3V3/XTAL_OUT crossing in the lower QFN/crystal field.
It is rejected as an isolated rail route. The next U1.52 attempt must
co-author XTAL_OUT and the local CLKREQ return; V232 remains the promoted
U1.39 rail basis.
## V234–V237 RTL_3V3 U1.52 allocation

V234 crossed XTAL_IN and RSET. V235/V236 moved the transition but still
contacted RSET or pad 49. V237 doglegged above pad 49 before the layer
transition. Native connectivity joins U1.52/C3.1 and the trace-removal
negative control fails as required. Native DRC reports 466 findings / 17
unconnected items with zero `shorting_items` and zero `tracks_crossing`.
V237 is promoted as the disposable U1.52 RTL_3V3 basis; remaining rail
branches and all other Path-B gates remain open.
## V238–V239 RTL_1V1 U1.36 / RTL_3V3 co-allocation

V238 joins U1.36 to C4.1 with native connectivity and a passing
trace-removal negative control; native DRC reports 475 findings / 16 opens
with one RTL_1V1/RTL_3V3 crossing at the existing U1.39 vertical. V239 moved
the U1.39 vertical west, but that co-allocation introduced XTAL_OUT contact
and a new crossing with the promoted U1.52 3V3 vertical. Both are retained
as route evidence, not promoted. The next attempt must co-author U1.36,
U1.39, and U1.52 together; Path A and production CAD remain unchanged.

## V240–V242 RTL_1V1 U1.36/U1.39/U1.52 co-allocation

V240 added U1.36-to-C4.1 but crossed SPISI. V241 removed that crossing but
introduced a native SPISI/RTL_1V1 via short. V242 moves the handoff via to
x=104.0 and explicitly extends the B.Cu trunk from x=102.5 to that via. The
first V242 run exposed a generator omission of that extension; the corrected
script now passes native U1.36/U1.39/U1.52 connectivity and the trace-removal
negative control. Native DRC is 484 findings / 16 unconnected items with zero
`shorting_items` or `tracks_crossing`. V242 is promoted as disposable rail
evidence; remaining RTL_1V1 branches and full Path-B gates remain open.

## V243 RTL_1V1 U1.40 west-side escape — rejected

V243 tested U1.40 from the V242 basis using a west-side F.Cu departure,
ordinary via at (91.0,60.8), and B.Cu return to the promoted 1V1 trunk.
The corrected native audit joins U1.36/U1.40 to C4.1 and U1.39/U1.52 to
C3.1; its trace-removal negative control fails as required. Native DRC,
however, reports 493 findings / 15 unconnected items and three signal
shorting classes: USB_RXN0/RTL_3V3 twice and ISOLATEB/CLKREQ_N. Reject V243
as a route implementation. V242 remains the promoted basis; Path A and
production CAD remain unchanged.

V381-V386 explored reallocation of the U1.52 RTL_3V3 escape and the RSET
return while keeping the exact V328 lane primitive. V381-V383 were rejected
for crossings or shorts against the retained RSET/XTAL channels. V384-V386
showed that simply moving the transition closer to the RX via field still
causes clearance/short conflicts; these are retained as route-implementation
evidence.

V387 co-authors the RSET return below the 3V3 channel and terminates RTL_3V3
on In2 at the existing power trunk, avoiding the RX B.Cu corridor. Native DRC
reports 0 shorting items and 0 tracks-crossing items, with 27 unconnected
items and remaining ordinary clearance/width findings. XTAL_OUT is still
removed for this discriminator, so V387 is an intermediate support-channel
basis, not a Path-B closure. Path A and production CAD remain unchanged.

V388 restores XTAL_OUT on a separate U1 escape and B.Cu vertical channel,
while retaining the V387 RSET/RTL_3V3 allocation and exact V328 lane. The
native V388 audit passes all four lane nets plus RTL_3V3, XTAL_IN, XTAL_OUT,
and RSET; four trace-removal negative controls fail as required. Native DRC
reports 0 shorting items, 0 tracks-crossing items, and 25 unconnected items.
Remaining findings include ordinary clearance/width/manufacturing issues,
so V388 is the first complete lane/support co-allocation basis but is not
yet Path-B closure. Path A and production CAD remain unchanged.
## V244 RTL_1V1 U1.50 lower-edge escape — rejected

V244 tested U1.50 from the V242 basis with a lower-edge F.Cu departure at
(94.05,64.8), an ordinary via at (96.0,64.8), and B.Cu return to the
promoted 1V1 trunk. Native connectivity and the corrected trace-removal
negative control pass for U1.36/U1.39/U1.50/U1.52. Native DRC reports 496
findings / 15 unconnected items and three track crossings: the new B.Cu
vertical crosses RTL_5V and RTL_3V3, and the source leg crosses RTL_3V3.
Reject V244 as a route implementation; V242 remains promoted.

## V245 RTL_1V1 U1.60/U1.63 translated lower-edge topology — rejected

V245 translated the historical V95/V96 lower-edge route class onto the V242
pad field and terminated it at the promoted 1V1 trunk. Native connectivity
and the trace-removal negative control pass for U1.36/U1.60/U1.63. Native
DRC reports 502 findings / 14 unconnected items and five track crossings:
the new B.Cu vertical crosses RTL_5V, PEDET, and RTL_3V3, while its F.Cu
source field crosses REFCLK_P and PERST_N. Reject V245 as a route
implementation; V242 remains promoted and no Path-A or production-CAD change
occurred.

## V246 RTL_1V1 U1.60/U1.63 co-allocation — rejected, narrowed

V246 co-authored the lower-edge source escape around the REFCLK/PEDET fields
and preserved the V242 trunk. Native U1.36/U1.60/U1.63 connectivity and the
trace-removal negative control pass. Native DRC reports 511 findings / 14
unconnected items. The prior lower-edge crossings were reduced to one
RTL_1V1/PERST_N B.Cu crossing at the horizontal handoff near (104.5,65.8);
the report also contains one ISOLATEB/CLKREQ_N shorting class in the retained
sideband field. Reject V246 pending a PERST-column overpass; it is useful
allocation evidence and does not alter V242 or production CAD.

## V248 RTL_1V1 U1.60/U1.63 source-dogbone correction — rejected

V248 corrected V247's U1.60 source departure around no-connect pad 59 and
used the split F.Cu/B.Cu handoff. Native U1.36/U1.60/U1.63 connectivity and
the full-rail-removal negative control pass. Native DRC reports 527 findings
/ 14 unconnected items, including an REFCLK_N crossing at the corrected
source field and a no-connect-pad/RTL_3V3 short. Reject V248; the next trial
must move the source escape farther from the REFCLK and no-connect fields.

## V249 RTL_1V1/REFCLK co-allocation — rejected

V249 moved the local REFCLK transitions outward and co-authored U1.60/U1.63
lower-edge rail escapes. Native rail/REFCLK endpoint connectivity and the
trace-removal negative control pass. Native DRC reports 525 findings / 14
unconnected items, with two REFCLK/source-field crossings and one
REFCLK_N/RTL_1V1 short at the QFN pad launches. Reject V249; the next trial
must separate the first F.Cu departures before either layer transition.

## V250 QFN source-field parallel departures — rejected

V250 tested 0.13-mm parallel lower-edge departures for REFCLK_P, REFCLK_N,
U1.60, and U1.63, with relocated local REFCLK transitions and the V242 rail
trunk preserved. Native rail/REFCLK connectivity and the trace-removal
negative control pass. Native DRC reports 541 findings / 14 unconnected
items, including three signal shorts (USB_RXN0/RTL_3V3 twice and RTL_3V3/GND)
and one remaining source-field crossing. Reject V250; the adjacent inherited
USB/3V3/GND fields must be co-relocated before another parallel escape.
negative control pass. Native DRC reports 541 findings / 14 unconnected
items, including three signal shorts (USB_RXN0/RTL_3V3 twice and RTL_3V3/GND)
and one remaining source-field crossing. Reject V250; the adjacent inherited
USB/3V3/GND fields must be co-relocated before another parallel escape.

## V251–V253 QFN source-field co-allocation — rejected

V251 co-authored the U1.52 RTL_3V3 branch with the V250 field; native rail,
REFCLK, and RTL_3V3 connectivity plus the trace-removal negative control
passed, but DRC reported an XTAL_IN/RTL_3V3 short and one crossing. V252
moved that handoff again and retained two source-field short/crossing classes.
V253 moved it farther west; native connectivity and the negative control still
passed, while DRC reported 541 findings / 14 unconnected items, three
crossings, and one RTL_3V3/GND short. Reject V251–V253 as route
implementations; no Path-A or production-CAD change occurred.

## V255 native A* U1.40 escape — rejected

The native-layer-aware A* search was corrected to honor SMD pad layers and
preserve exact native pad-center endpoints. It found a 131-node U1.40 route;
the native endpoint audit passed. Native DRC reported 628 findings / 15
unconnected items with no track-crossing class, but retained one
RTL_3V3/RSET short in the local QFN field. V255 is rejected as a route
promotion, but the search method now produces reproducible topology evidence.

## V254 U1.39 support-field relocation — rejected

V254 moved only the U1.39 RTL_3V3 escape around the C2 ground pad on the
V253 basis. Native rail/REFCLK/RTL_3V3 connectivity and the trace-removal
negative control pass, but native DRC reports 546 findings / 14 unconnected
items with new RTL_1V1/RTL_3V3 crossings and a retained ISOLATEB/CLKREQ_N
short. Reject V254; the complete adjacent support cluster must move together.

## V256 U1.52 RSET co-clearance — rejected

V256 applies a narrow local repair to the inherited U1.52 RTL_3V3 escape,
moving its short departure and vertical trunk from x=94.5 mm to x=94.7 mm so
the rail clears U1.51 RSET. Native DRC reports 623 findings / 16 unconnected
items, with no `shorting_items` or `tracks_crossing` class. Native U1.36/U1.40
connectivity passes, and removing a required RTL_1V1 trace fails the negative
control as expected. The remaining unconnected support and manufacturing-rule
findings prevent promotion; V256 is retained as evidence for the next
co-authored support-field repair.

## V257 U1.52 rail join — rejected

V257 completed the short V256 RTL_3V3 branch into the existing upper rail
field. Native DRC reports 626 findings / 15 unconnected items. The U1.52
branch is connected, but the inherited ISOLATEB/CLKREQ_N pad-field short is
exposed. Reject as a route promotion.

## V258 bottom-edge RTL_1V1 via bus — rejected

V258 attempted ordinary F.Cu-to-B.Cu escapes for U1.55/U1.60/U1.63 and a
local B.Cu RTL_1V1 bus. It reduced the unconnected count to 13, but native
DRC reports 668 findings and multiple real RTL_1V1 shorts into REFCLK_P,
REFCLK_N, and XTAL_OUT. Reject; the QFN support field must be co-authored
with those neighboring analog/clock escapes rather than populated with
independent vias.

## V265–V266 coherent support-cluster placement — V266 retained

The first scrubbed placement (V265) put Y1/C1 too close and produced one
XTAL_OUT/GND pad overlap. V266 translated C1 to clear that overlap. The
scrubbed V266 board has no `shorting_items`, no `tracks_crossing`, and zero
footprint errors; native DRC reports 228 findings / 36 opens because all
affected support copper was intentionally removed. V266 is retained as the
placement baseline for coordinated route regeneration; it is not yet a
routed or promoted RTL9210B implementation.

## V259–V260 CLKREQ local re-escape — rejected

V259 escaped U1.13 CLKREQ_N to an ordinary via west of the adjacent U1.12
ISOLATEB pad. It removed the pad-field short but crossed the existing B.Cu
REFCLK_N corridor. V260 moved the B.Cu dogleg farther south; native DRC still
reported the REFCLK_N crossing. Reject both as local route implementations;
CLKREQ_N and REFCLK_N departures must be co-authored as one QFN side-field.

## V261 CLKREQ east-side re-escape — retained, not promoted

V261 routes U1.13 CLKREQ_N east on F.Cu, then drops at x=103.4 mm and joins
the existing B.Cu continuation from a south dogleg. Native DRC reports 633
findings / 15 unconnected items with no `shorting_items` or `tracks_crossing`
class. This is the best current CLKREQ local geometry, but the remaining
rail, clock, support, and high-speed connectivity failures prevent promotion.

## V262 bottom-edge RTL_1V1 bus at increased clearance — rejected

V262 repeated the U1.55/U1.60/U1.63 bottom-edge bus with the escape row moved
to y=68.8 mm. It reduced the unconnected count to 13, but native DRC reported
652 findings with real RTL_1V1 shorts into RTL_3V3, REFCLK_P/N, and XTAL_OUT.
Reject; independent via placement cannot safely coexist with the existing
clock field.

## V267–V268 crystal escape trials — rejected

V267 and V268 attempted first-pass crystal routes from the scrubbed V266
placement. Their diagonal QFN exits and capacitor dogbones produced real
XTAL/rail/ground conflicts or crossings and were rejected as implementations.

## V269 corrected crystal field — retained, not promoted

V269 preserves the corrected straight-out QFN exits, uses separated ordinary
through-via corridors, and fixes the capacitor pad-side dogbones. Native
connectivity confirms U1.53→Y1.1, U1.54→Y1.2, C1.1→Y1.1, and C2.1→Y1.2.
Native DRC reports 293 findings / 32 opens with no `shorting_items` or
`tracks_crossing` class and zero footprint errors. Rail, reset, SPI, and
remaining support connections are still open, so V269 is retained as the
crystal-field basis rather than promoted as a complete Path-B board.

## V270 RSET route on retained support placement — retained, not promoted

V270 adds the moved RSET path from U1.51 to R1.1 using a short F.Cu escape,
one ordinary via, and a local F.Cu landing. Native connectivity confirms the
join. Native DRC reports 307 findings / 31 opens with no `shorting_items` or
`tracks_crossing` class and zero footprint errors. The remaining rail,
control, SPI, and high-speed support paths remain open.

## V271–V273 rail escape trials — rejected

V271 and V272 exposed, then corrected, U1.20/U1.18 pad-field interactions in
the RTL_3V3 departure. V273 uses the corrected U1.20 north escape and direct
local branches to C3.1, R3.2, and R2.2. It has no shorting or crossing class,
but the U1.52-to-U1.34 endpoint remained open.

## V274 completed RTL_3V3 local joins — retained, not promoted

V274 adds the final short same-net join between the U1.52 branch and U1.34.
Native connectivity confirms U1.20→C3.1, U1.34→R3.2, U1.39→R2.2, and
U1.52→U1.34. Native DRC reports 319 findings / 27 opens with no
`shorting_items` or `tracks_crossing` class and zero footprint errors. SPI,
PEDET, reset, remaining rail branches, and high-speed paths remain open.

## V275–V277 SPICS corridor trials — rejected implementations

V275 adds native U1.24→U2.1 SPICS connectivity, but its B.Cu horizontal
corridor crosses both retained XTAL_IN and XTAL_OUT B.Cu trunks. V276 moves
the corridor to F.Cu and crosses two retained RTL_3V3 branches. V277 moves
below the crystal trunks but crosses the retained B.Cu REFCLK corridor. These
are route-implementation failures; the support placement and existing
crystal/RSET/rail basis remain valid.

## V278 SPICS outer lower corridor — retained, not promoted

V278 routes the actual U1.24=(98.8,58.05) to U2.1=(83.3,70.0) endpoints via
an offset B.Cu corridor that avoids the retained crystal and REFCLK trunks,
with ordinary through-vias and short F.Cu pad dogbones. Native KiCad DRC
reports 335 findings / 26 unconnected items, with zero `tracks_crossing`,
zero `shorting_items`, and zero footprint errors. The unconnected count is
the inherited unfinished support field, not a SPICS failure. The native
endpoint audit and its trace-removal negative control both pass. V278 is
retained as the SPICS route basis; SPISO, SPISO3, SPICLK, SPISI, PEDET,
reset, remaining rail branches, and high-speed paths remain open.

## V279–V281 SPISO corridor trials — rejected implementations

V279 attempted a lower B.Cu SPISO lane but crossed the V278 SPICS source and
return lanes and also crossed at the U1 adjacent-pad escape. V280 moved the
lane but still crossed the SPICS horizontal branch and had a pad-field
crossing. V281 fixed the U1 north escape and endpoint dogbone but retained a
single SPISO/SPICS B.Cu crossing. These are route-implementation failures.

## V282 SPISO split-layer corridor — retained, not promoted

V282 retains V278 and adds SPISO from actual U1.23=(99.2,58.05) to
U2.2=(84.5,70.0). It transitions from the U1 north escape to B.Cu, crosses
to F.Cu before the SPICS endpoint, and returns to a lower B.Cu lane with
ordinary through-vias. Native KiCad DRC reports 366 findings / 25 unconnected
items, zero `tracks_crossing`, zero `shorting_items`, and zero footprint
errors. Native endpoint audits and trace-removal negative controls pass for
both SPICS and SPISO. V282 is retained as the two-net SPI corridor basis;
SPISO3, SPICLK, SPISI, PEDET, reset, remaining rails, and high-speed paths
remain open.

## V285 SPISO3 trunk trial — rejected implementation

V285 moved the SPISO3 escape to B.Cu before the crystal field, but its
vertical trunk crossed the retained XTAL_IN branch. It is rejected as a
route-implementation failure.

## V286 SPISO3 offset trunk — retained, not promoted

V286 shifts that B.Cu trunk laterally around XTAL_IN while preserving the
V278/V282 bases and actual U1.22=(99.6,58.05) to U2.7=(90.5,70.0) endpoint
mapping. Native DRC reports 383 findings / 24 inherited opens, with zero
shorting or crossing class and zero footprint errors. Native endpoint and
trace-removal negative-control audits pass. V286 is retained as the SPISO3
basis; SPICLK, SPISI, PEDET, reset, remaining rails, and high-speed paths
remain open.

## V312/V313 RTL_5V perimeter trials — rejected implementations

V312 and V313 were tested from the saved V311 board using native pad-derived
endpoints and ordinary F.Cu/B.Cu through-vias. Each reduced the native
unconnected count from 18 to 16 by joining U1.17/U1.33/C5.1. V312 introduced
three short/crossing classes at the upper QFN field; V313 moved the escape to
a lower perimeter but retained one short and three crossings. Both are
rejected as route-implementation failures. No Path-A or production CAD
changed, and V311 remains the retained sideband basis.

## V323/V328 coherent reorientation and lane-0 closure primitive

V323 moves U1 to `(106,62)` at 180 degrees and translates the RTL9210B local
support components together, clearing the J1 SSD-power field that invalidated
V322. Its unrouted native DRC has no shorting or crossing class. V328 routes
the four transformed lane-0 nets using TX on F.Cu and RX with explicit outer-
layer transitions outside both pad fields. Native DRC reports zero shorting
and zero crossing classes; the saved-board endpoint audit and trace-removal
negative control pass. Support/control/REFCLK remain open.

## V337/V339 crystal relocation and route primitive

V337 clears C2 from C4 while retaining the coherent V323 support placement.
V339 routes XTAL_IN and XTAL_OUT using separate B.Cu spines and short native
capacitor handoffs. Native DRC reports zero shorting and zero crossing
classes, and the saved-board crystal audit plus trace-removal negative control
pass. This closes only the local crystal primitive; remaining RTL9210B
support and interface nets are still open.

## V340 RSET route primitive

V340 routes U1.51 RSET to R1.1 on the V339 crystal/lane placement using a
short F.Cu departure, a B.Cu corridor, and an F.Cu resistor handoff. Native
DRC reports zero shorting and zero crossing classes; the saved-board
connectivity audit and trace-removal negative control pass. RSET is retained;
remaining rails, controls, SPI, REFCLK, USB, and M.2 support remain open.

## V341-V354 rail-field follow-up

V341-V345 RTL_3V3/RTL_5V trials were rejected as route-implementation
failures because they introduced real shorting or crossing classes in the
QFN support field. V342 remains the clean RTL_3V3 base. V346-V353 tested
alternate RTL_5V handoffs; V354 is retained as the first clean candidate.
V354 routes U1.17/U1.33/C5.1 to the RTL_5V support field using a short
F.Cu escape and a B.Cu perimeter trunk. Native DRC reports 0 shorting
items, 0 tracks-crossing items, and 24 unconnected items (the base V342
had 26). The native endpoint audit and trace-removal negative control pass.
This does not close the RTL9210B support rail or Path B: RTL_1V1, USB,
REFCLK, reset, remaining control, lane, and M.2 integration work remain open.

V355 RTL_1V1 is rejected as an initial placement/escape trial. It produced
8 shorting and 4 crossing classes, including collisions with the retained
RTL_3V3 and crystal fields. No authority or Path-A asset changed; further
RTL_1V1 work must use coordinated pad-field channel allocation.

V356/V357 are rejected partial RTL_1V1 channel trials. V356 attempted a
direct B.Cu U1.16-to-C4 trunk and collided with the retained XTAL_OUT spine.
V357 moved the C4 handoff to F.Cu, but collided with C3/GND and crossed the
retained XTAL_IN B.Cu route. These are implementation/channel-allocation
failures. The next RTL_1V1 candidate must co-author the complete 1V1 fanout
with the crystal and adjacent support fields; no production or Path-A CAD
was changed.

V358 is rejected as a coordinated 1V1 probe. It removed the retained
XTAL_IN/XTAL_OUT copper before adding a complete U1/C4 1V1 field; native DRC
reported 6 shorting classes and 2 crossing classes, primarily against the
retained RTL_3V3 and RSET fields. It reduced the inherited open count to 23,
but does not establish a valid route. The result confirms that the next
attempt must use an explicitly isolated RTL_1V1 power region or a jointly
reallocated 3V3/RSET/1V1 channel plan.
 
V359 tested an In2 RTL_1V1 zone with native F.Cu pad escapes, rather than
synthetic connectivity. The zone eliminated track-crossing classes but the
chosen escapes/via locations still produced 7 native shorting classes against
RSET, XTAL_OUT, and RTL_3V3. It is rejected; the result supports using a
power-region approach only after the package escapes and neighboring support
channels are co-allocated with verified clearance.

V362/V363/V364 are the coordinated power-field follow-up. V362 restored the
authoritative V342 RTL_3V3 tracks onto the refilled V361 1V1 region and found
two genuine 3V3/1V1 contacts. V363 corrected one QFN escape but was superseded
after exposing a USB-pad contact. V364 rebuilt the 1V1 field with a
down-then-out U1.40 escape and restored RTL_3V3 after removing only disposable
neighbor routes. Native DRC reports 0 shorting items, 0 tracks-crossing items,
and 26 unconnected items. A combined native endpoint audit passes all nine
1V1 and nine 3V3 endpoints; independent trace-removal negative controls fail
as required. V364 is retained as the coordinated power-field basis. RSET,
crystal, USB, REFCLK, reset, lane, and M.2 work remain open.

V360/V361 are retained as a coordinated 1V1-first basis. V360 removed only
the disposable RTL_3V3/RSET/XTAL copper and authored native U1/C4 escapes plus
an In2 RTL_1V1 region. Its first saved board had an unfilled zone, so its
connectivity count was not accepted. V361 refilled that saved zone with the
native `ZONE_FILLER` and was then audited from actual pads/tracks/vias/zones.
Native DRC reports 0 shorting items, 0 tracks-crossing items, and 34
unconnected items; all nine asserted 1V1 endpoints connect, and the
trace-removal negative control fails as required. This closes the 1V1-first
allocation hypothesis only, not the neighboring support routes or Path B.

V365 transplanted the retained RSET/crystal primitives onto V364 and is
rejected with 5 shorting and 4 crossing classes; it demonstrates that those
primitives must be reallocated together with 1V1. V366 is the first complete
coallocated 1V1 fanout trial with the retained neighboring primitives. It
reduced the problem to 3 shorting and 1 crossing class: a C4/GND handoff and
one right-side 1V1 trunk at the RTL_3V3 field. V366 is rejected as a route
implementation, while V364 remains the retained clean power-field basis.
V367 is a follow-up coallocation trial that moves the C4 and right-side
handoffs outward. It removes all shorting classes but retains three native
tracks-crossing classes, all against the retained XTAL_OUT B.Cu spine. It is
rejected pending either moving that crystal spine or assigning those 1V1
branches to a different layer/channel.
V372 removes the unnecessary XTAL_OUT intermediate via and routes directly
from U1 to an outboard B.Cu riser. Native DRC reports 0 shorting items, 0
tracks-crossing items, and 21 unconnected items; this restores the V368
support audit basis while freeing the former XTAL_OUT channel.

V373 transplants the V328 lane-0 primitive onto V372. It is rejected as an
integration route: native DRC reports 5 shorting and 3 crossing classes,
including lane RXN against the outboard XTAL_OUT riser and lane TXN/RXN
against RTL_1V1 right-side launches. The next candidate must co-author the
lane escape and 1V1 right-side channels; no Path-A or production CAD changed.
V370 is retained as a clean XTAL_OUT reallocation candidate: native DRC
reports 0 shorting items, 0 tracks-crossing items, and 21 unconnected items,
and the coallocated support audit plus RTL_1V1/XTAL_OUT negative controls
pass. V371 transplants V328 lane-0 onto the older V370 transition and is
rejected with 6 shorting and 7 crossing classes. V372 removes the unnecessary
XTAL_OUT intermediate via and is retained as the direct-riser basis; V373
retries lane-0 against it and is rejected with 5 shorting and 3 crossing
classes. The remaining problem is lane RXN/RTL_1V1 transition-channel sharing.
V368 is retained as the first clean coallocated support basis. It keeps the
retained RSET and XTAL_IN/XTAL_OUT primitives, routes the RTL_1V1 right-side
branches on In2, and routes the top/left branches on B.Cu to avoid RTL_3V3.
After native zone refill, DRC reports 0 shorting items, 0 tracks-crossing
items, and 21 unconnected items. A native endpoint audit passes RTL_1V1,
RTL_3V3, XTAL_IN, XTAL_OUT, and RSET; negative controls remove every route
for RTL_1V1 and RSET and fail as required. This is a support-field basis,
not Path-B closure; USB, REFCLK, reset, SPI, lane, and M.2 remain open.
V369 attempted to transplant the current-orientation V328 lane-0 primitive
onto V368. It is rejected as an integration route failure: native DRC found
6 shorting and 7 crossing classes, chiefly between RX B.Cu, XTAL_OUT, and
the 1V1 launches. The next high-speed pass must co-author lane-0, XTAL_OUT,
and the 1V1 right-side channels; no authority or Path-A CAD changed.
V370/V372 provide the retained XTAL_OUT relocation basis: direct U1-to-riser
F.Cu handoff, outboard B.Cu riser, and native endpoint continuity. V373
transplant of V328 lane-0 was rejected with 5 shorts and 3 crossings. V374
and V375 below-band RXN experiments were also rejected after native pad-field
and connector-launch conflicts. The remaining work is a joint RX-pair and
1V1 launch allocation; no production or Path-A CAD changed.
V376 regenerated both lane-0 RX pair escapes and their connector launches
together. It is rejected: native DRC reports 10 shorting and 2 crossing
classes, including RXN/U1 REFCLK and RXN/RTL_1V1 lower-via contacts. The
connector crossing was reduced, but the source escape still requires a
co-authored U1 pad-field channel plan.
V377 isolated the lane-0 source/corridor by removing RTL_1V1 copper, but its
new RXN vias still contacted U1 REFCLK and adjacent QFN pad rows. Native DRC
reported 6 shorts and 1 crossing. This candidate is rejected; the next pass
retains the proven V328 source via positions and reallocates only the
conflicting RTL_1V1 launches.

V378 was a diagnostic lane-only regeneration, but it did not faithfully
reproduce V328: the RXP connector launch was routed through J1.41/RXN and the
RX source vias were placed at the U1 pad-field exits rather than at V328's
staggered transition points. Native DRC therefore reported 2 shorts and 0
crossings. It is rejected as a route-authoring error, not as evidence against
the lane topology.

V380 repeats the diagnostic with the exact V328 lane geometry: RXP source
transition at (110.6,66.5), RXN source transition at (111.5,64.5), connector
returns at (132,66.5)/(132,64.5), and the authoritative J1 RXN/RXP launches
to pads 41/43. RTL_1V1, RTL_3V3, XTAL_IN, and XTAL_OUT copper was removed only
to isolate the lane from known support-channel conflicts. Native DRC reports
0 shorting items and 0 tracks-crossing items, with 37 unconnected items from
the intentionally incomplete support base. This proves the exact lane
primitive remains geometrically valid; the remaining task is joint
allocation of support rails/crystal and the lane source channels. Path A and
production CAD remain unchanged.
V389 refilled all native zones on V388 before comparing DRC. This removed the
stale zone-clearance flood and left 17 violations, including 25 unconnected
items counted separately by the report. V390 applied the board minimum 0.20 mm
width to all four lane nets and removed the four imported 0.13 mm width
errors. V390 retains 0 shorts and 0 crossings, with 25 opens and localized
clearance/hole-clearance, dangling-power, and isolated-copper findings. These
remain open manufacturing/layout findings; no Path-A or production CAD
changed.
V391-V392 reallocated oscillator transitions with standard vias. V392 reduced
the complete co-allocated candidate to 7 non-open native findings while
retaining zero shorts/crossings; V393's smaller 0.40/0.20 mm vias were
rejected by the native 0.50/0.30 mm fabrication minima. V394-V395 outboard
XTAL_OUT routes introduced new conflicts and were rejected. V396/V397 moved
XTAL_IN beyond the exposed-pad edge; V397 is the better basis with 6 native
non-open findings and 26 opens. V398 moved XTAL_OUT rightward and regressed
one local clearance, so it is rejected. All remain disposable Path-B work;
Path A and production CAD are unchanged.
V399 co-authored RSET/RTL_3V3 and XTAL_OUT from the V397 basis but introduced
two GND shorts at the XTAL_OUT transition, so it is rejected. V397 remains the
current basis for the next repair; Path A and production CAD are unchanged.
V409 direct PERST_N import from V311 was rejected: the historical source used
different U1 coordinates and produced two shorts plus an RTL_3V3 conflict.
V410 regenerated from the actual U1.14/J1.50 pads but used a crowded source
via and sub-minimum 0.50/0.25 via geometry, so it was rejected. V411 moved
the PERST source escape above the U1 row; V412 moved its B.Cu trunk outside
the RTL_3V3 via field. V412 has 0 shorts/crossings and 24 opens.

V413/V414 regenerated CLKREQ_N from the current U1.13/R3.1/J1.52 pads;
V414 still shared/crossed the PERST trunk. V415 moved CLKREQ to a distinct
y=76 trunk, and V416 moved its vertical leg outside PERST. V416 has 0
shorts/crossings and 22 opens. The V416 native audit passes the existing
lane/support nets plus PERST_N and CLKREQ_N, with six trace-removal negative
controls passing. Remaining opens are PEDET, RTL_1V1, SPI, REFCLK, and other
support connections; Path A and production CAD remain unchanged.
V400 moved only the RSET endpoint and reduced the native non-open findings by
one. V401 shifted the RXP source vertical and removed the remaining QFN-pad
clearance error without changing pair ordering or connector launch. V402
lowered the RSET return and removed its In2 clearance error. V403 restored the
oscillator with standard vias and had only three warnings plus 26 opens. V404
connected the actual C1.1 endpoint; native support audit and four negative
controls pass, and native DRC reports 0 shorts, 0 crossings, 25 opens, and
only the inherited dangling/isolated-copper warnings. This is the current
best Path-B local basis, not full closure; Path A and production CAD remain
unchanged.
V417 PEDET regeneration used current U1.8/R2.1/J1.69 coordinates but shared
older trunks and was rejected. V418 moved PEDET to a distinct y=54.5 source
channel and lower return. Native DRC reports 0 shorts/crossings and 20 opens;
the V418 audit passes lane/support/control/PEDET connectivity with seven
trace-removal negative controls. Remaining opens are RTL_1V1, SPI, REFCLK,
and associated return/power support; Path A and production CAD remain
unchanged.

V419-V423 are rejected CLKREQ source-escape experiments. V419 introduced a
PEDET/CLKREQ short; V420 introduced JTAG/XTAL conflicts; V421 crossed the
PERST source; and V422/V423 each introduced a real RTL_1V1 or PERST conflict.
V424 entered U1's no-connect pad-4 field and crossed XTAL_IN, so it is also
rejected. V425 avoided pad 4 but crossed the PERST source and approached the
RTL_5V pad too closely. V426 has the same PERST crossing and an RTL_5V
clearance error. V427 crosses the PEDET source and existing PERST trunk.
These are route-implementation failures; V418 remains the best clean
PEDET/control basis and no Path-A or production CAD was changed.
V430 raised the V416 CLKREQ dogleg but still left a 0.15 mm clearance to
U1.12. V431 raised it to y=57.10 mm. Native DRC then reported only the two
inherited warnings (dangling RTL_3V3 and isolated GND fill) plus the 20
intentional/inherited opens; it reported zero shorts and zero crossings. The
V431 native audit passes all lane/support/PERST/CLKREQ/PEDET groups and seven
trace-removal negative controls. This closes the CLKREQ source-escape repair
on the V418 basis; REFCLK and remaining power/SPI support are still open.
V428 changed solution class by rotating U1 90 degrees and regenerating
PEDET/CLKREQ/PERST from the transformed native pads. It is rejected as an
early disposable trial: stale lane/crystal copper was not co-regenerated,
and the provisional control corridors themselves crossed existing lane,
REFCLK, and each other. Native DRC reported 46 violations. This result is
not a macro-placement verdict; it shows that a rotation trial must be
regenerated as a complete local support/lane island before comparison.
V432 isolated REFCLK but is rejected as a malformed first launch: its
0.40-mm-separated transition vias violated the 0.60-mm via body clearance,
and its straight connector dogbones contacted adjacent J1 MDI pads. The
source/endpoint choice is not evidence against REFCLK; the next fixture must
stagger both transitions and approach J1.53/J1.55 from clear connector-side
corridors.
V433/V434 regenerated REFCLK_P/REFCLK_N with separated upper/lower J1
approaches. V433 still crossed the two B.Cu diagonals and contacted the
adjacent REFCLK connector pad; V434 spread the trunks but retained a source
escape/via interaction and a J1.53 launch conflict. Both are rejected as
route-implementation failures. They establish the needed monotonic
connector ordering; the next pass must co-allocate REFCLK with the lane
source transitions and use a clearance-aware source escape.
V435-V437 continued REFCLK co-allocation. V435/V436 showed that leftward
transitions enter the exposed pad or XTAL_OUT; V437 separated the outer J1
launches but still hit the adjacent MDI pad and the 0.4-mm U1 REFCLK P/N
source spacing. These are valid native-D RC failures of the current broad
escape primitives, not Path-B closure. The next source allocation must use a
complete co-regenerated QFN fanout (including lane/XTAL) with verified local
clearance; no production CAD changed.
V439 isolated only the REFCLK source fanout with diverging 0.20-mm traces.
Native DRC still found the adjacent U1.61/U1.62 source-field conflict at the
0.40-mm pitch. This confirms the package/rule interaction quantitatively;
the next candidate must be a complete QFN fanout with authoritative escape
geometry, not another isolated trunk adjustment.
V438 tested a 0.10-mm reduced-width REFCLK fanout from the native U1 pads,
widening after the proposed transitions. Native DRC still rejected it: the
QFN P/N source separation remained below clearance, the N transition entered
U1's exposed-pad region, and the board's 0.20-mm minimum-width rule flagged
both fanout tracks. This confirms that a reduced-width exception would be a
design-rule relaxation, not an acceptable closure. The next effort remains a
complete rotated/co-regenerated QFN fanout or another documented footprint
escape solution; no Path-A or production CAD changed.
V443 used straight outward U1.61/U1.62 fanouts and separated upper/lower
connector launches. Native DRC removed the prior connector and source-pad
crossings; only one source-transition interaction remained, with the
REFCLK_P via 0.4 mm from the REFCLK_N fanout. The result is the strongest
REFCLK primitive so far, but not closure. The remaining work is co-allocation
of the two transitions with the lane escape under the active rule basis.
V444-V447 explored REFCLK_N left-side staggering; each retained a local
clearance or crystal/no-connect interaction. V448 removed both XTAL nets for
a valid isolation test and moved REFCLK_N below the U1 no-connect field.
Native DRC reports zero shorts/crossings with only the inherited dangling
RTL_3V3 and isolated-GND warnings; the V448 audit passes both REFCLK endpoint
groups and two trace-removal negative controls. V448 is the retained REFCLK
primitive pending full lane/REFCLK co-allocation.
V450 attempted early RX_P transition plus a lower REFCLK_N trunk. Native DRC
rejected it with RX_P/RX_N source-field contact, REFCLK_N/RTL_3V3 conflicts,
and a malformed RX_P handoff that left a dangling transition. It is rejected
as a route-authoring/coallocation trial; V448 remains the clean REFCLK
primitive and V328 remains the authoritative lane primitive.
V451 retained the clean V443-style REFCLK_P launch and moved REFCLK_N's
transition upward before its lower B.Cu corridor. Native DRC reported zero
shorts/crossings with only inherited warnings and 26 inherited opens. V452
added the exact V328 lane primitive; native DRC exposed the real shared-field
conflicts: RX_N intersects the REFCLK_N source/transition, RX_P approaches
U1 RTL_3V3, and the lower REFCLK trunk approaches the RX_P transition. V452
is rejected as a coallocation candidate, while V451 remains the clean
REFCLK basis and V328 remains the lane authority.
V453 added an upper REFCLK_N overpass but retained RX-source conflicts. V454
coordinated the source and connector corridors: REFCLK_N descends outside
the REFCLK_P B.Cu corridor, RX_N moves to the outer source transition, and
RX_P uses an early ordinary-via transition. Native DRC reduced the candidate
to one real RX_P/RX_N source-transition short, two inherited warnings, and
22 inherited opens. V454 is retained as the current coallocation basis while
that single RX transition is repaired.
V455 moved the RX_P transition upward from V454. Native DRC rejected it with
an RX_P/RX_N source crossing, RX_P clearance to TX_N, and solder-mask bridge
errors. V454 therefore remains the best combined basis. The source-field
gate has now been tested with straight, staggered, early-via, upper, lower,
and diverging allocations; the next credible class is a complete
rotated/re-authored QFN fanout, not another single-net coordinate tweak.
V456 corrected the rotated-package fixture authoring path by removing the
complete local copper envelope before applying the 90-degree U1 transform.
Its saved-board audit proves all six transformed source pads reach their
local transition vias, and six trace-removal negative controls fail as
expected. Native DRC has zero shorts/crossings but retains three real local
clearance errors in the staggered source-via fanout, so V456 is not closure.
V457 tested a monotonic row of source vias. Native DRC rejected it with one
source short plus four QFN source-field clearance/solder-mask errors; this is
another route-implementation failure, not evidence against the RTL9210B
pin map. V458 moved RX_P's V454 source transition beyond the RX_N endpoint.
It removed the original V454 RX_P/RX_N transition short but crossed/shorted
the existing REFCLK_N and RX_N transitions, so it is rejected. V454 remains
the strongest combined basis while a complete clearance-aware QFN fanout is
developed; no Path-A or production CAD changed.
V459 kept V454's REFCLK/RX_N launches and moved only RX_P's source transition
below the QFN edge. Native DRC removed the V454 source short, but the RX_P
escape crossed both REFCLK source tracks and violated the adjacent no-net pad
clearance. It is rejected as a local source-field implementation failure;
the next attempt must regenerate all six source escapes as one clearance-aware
fanout. No Path-A or production CAD changed.
V460 tested the rotated package with all six source transitions moved to a
1-mm-spaced outboard row in source order. Native DRC rejected the direct
diagonal fanout with seven source-field shorts/clearance and solder-mask
errors. This is an invalid escape primitive, not a rejection of the package
pin map; the retained basis remains V454 while a proper layer-aware fanout
must be authored.
V461 used a planar rotated fanout with ordered vertical escapes and decreasing
F.Cu jog heights. It eliminated shorts and crossings but retained five
0.5-mm-adjacent via/jog clearances. V462 widened those jog heights to 0.9 mm.
Native DRC reports zero shorts, crossings, and clearance violations; the
saved-board audit proves all six source pads connect to their transition vias,
and six trace-removal negative controls pass. V462 is the strongest source
fanout primitive, but it is not a complete Path-B route or support closure.
V465 isolated the RX pair endpoint corridor from the other high-speed nets.
Native DRC reduced the pair trial to one 0.134-mm connector-transition
clearance, with zero shorts/crossings. V466 moved RX_N's transition 0.5 mm
outboard and achieved native DRC zero shorts/crossings/clearances; the saved
board audit confirms U1.64/J1.43 and U1.65/J1.41 connectivity, and two
trace-removal negative controls pass. V466 is a valid RX-pair endpoint
primitive, not full RTL9210B closure.
V463 connected the six V462 source transitions to the J1 endpoints using
distinct B.Cu horizontal rows and F.Cu endpoint launches. Native DRC found
one real RXN/RXP clearance issue; V464 reused the proven V448/V328 connector
handoff positions, but introduced three corridor crossings and multiple
connector-transition clearances/shorts. Both are rejected route
implementations. V462 remains the clean source primitive; the next full route
must allocate endpoint corridors by layer and connector ordering rather than
sharing a single row family.
