# Append-only project bible

2026-09-08: Parameterized the retained V3 JMS583 QFN escape author for an
explicit disposable base/output, enabling controlled integration with later
storage candidates without mutating the Path-A basis. The earlier complete-
support cohort author remains preserved as experimental evidence.

2026-09-08: Generalized the JMS583 native support-cohort audit to accept an
explicit disposable PCB path while retaining its saved-pad/track/via-only
connectivity model. Against the corrected NC39 support replay it correctly
fails incomplete support connectivity; the separate removed-R80 schematic
negative control also fails as required. No validation severity was changed.

2026-09-08: Generated the coherent native-pad JMS583 support cohort on the
corrected NC39 basis. All eight support endpoint assertions and the exact
trace-removal negative control pass; native DRC reports 820 violations / 499
unconnected items, zero authored shorts, and seven inherited CM5 donor USB
crossings. Retain this as the strongest support-routing primitive, not a
full-board pass.

2026-09-08: Rejected the NC39 co-located-crystal trial. Moving Y10 into the
storage island and using separated ordinary-via XIN/XOUT corridors still
produced real XIN/XOUT-to-support shorts; native DRC was 850 violations / 499
unconnected items. Preserve as route-implementation evidence only.

2026-09-08: V3 QFN escape repair completed the JMS583 support field. Native
complete-support audit and trace-removal negative control pass all ten endpoint
pairs; native DRC reports 852 violations / 499 unconnected items with no
storage-local short/crossing and seven inherited CM5 donor USB crossings.
Retain as the current support-field primitive, not Phase 24 closure.

2026-09-08: Replayed the JMS583 support author against the corrected NC39
candidate. Native DRC reports 836 violations / 499 unconnected items,
including one real JMS_REXT-to-JMS_AVDDL short and authored crossings. The
trial is rejected route evidence; source parity remains PASS and the next
support route must allocate native-pad-aware per-net escape corridors.

2026-09-08: Corrected the live JMS583 source/PCB association path. A native
endpoint-overlap repair removed stale U11 generated label atoms, and the
shared selector maps restored pin 39 to the schematic's `NC_39` instead of
`JMS_GPIO7_NC`. The regenerated `PHASE24_DUAL_MODE_STORAGE_PLACEMENT_NC39`
candidate passes native schematic-to-PCB pad-net parity with zero mismatches.
Native DRC remains open at 797 violations / 499 unconnected items; this is a
source-authority checkpoint, not Phase 24 closure. Historical probes remain
preserved as rejected evidence.

2026-09-07: Rejected disposable RTL9210B V312/V313 RTL_5V perimeter trials.
Both native-pad-derived trials closed the RTL_5V endpoint opens but introduced
real short/crossing classes (V312: three; V313: one short and three
crossings). They remain preserved evidence only; V311 is the current retained
sideband basis and Path A/production CAD are unchanged.

2026-09-07: Retained RTL9210B V337/V339 crystal-support primitive. C2 was
cleared from C4, then XTAL_IN/XTAL_OUT were routed with separate B.Cu spines;
native DRC and saved-board negative-control audits pass with zero shorts or
crossings. Remaining Path-B support/interface nets are open.

2026-09-07: Retained RTL9210B V323/V328 coherent placement and lane-0
primitive. U1 was reoriented toward J1 with coherent support translation;
V328 passed native four-pair connectivity, zero shorts/crossings, and a
trace-removal negative control. Support/control/REFCLK remain open.

2026-09-07: Rejected RTL9210B V314–V317 rail and lane probes. Native DRC
exposed real short/crossing classes despite reduced open counts. V311 remains
the retained disposable sideband basis; Path A and production CAD are
unchanged.

2026-09-09 — Phase 24 V1436/V1437/V1438 rejected RSET B.Cu bypass classes:
V1436 left one GND-triangle crossing, while V1437/V1438 crossed the long
RTL_1V1 B.Cu shelf. RSET remains open; local R1 support relocation is the
next bounded class.

2026-09-09 — Phase 24 V1434/V1435 rejected RSET north-shelf routes. V1434
shorted R1 GND and crossed RTL_1V1; V1435 removed the GND short but retained
one RTL_1V1 crossing. RSET remains open and V1428 remains accepted.
2026-09-09 — Phase 24 V1405 rejected the first RTL_3V3 U2.3-to-U1.20 support
join from V1392. The lower collector produced seven native DRC violations
against existing lane/control/rail geometry. Evidence is preserved; accepted
V1392 and Path-A remain unchanged.
2026-09-09 — Phase 24 V1408 rejected the upper U2 RTL_3V3 support join.
Native DRC reported six crossings/shorts against SPI/control and 1V1
geometry. The disposable evidence is preserved; accepted V1392 and Path A
remain unchanged.

2026-09-10 — Phase 24 recorded the RTL9210B Path-B QFN field disposition in
`PHASE24_RTL9210B_QFN_FIELD_BLOCKER.md`. Native pad geometry and repeated
U1.66 escape failures show no legal route under the current 0.2-mm
clearance/track contract and ordinary-via policy. Path B is not promoted;
Path A remains preserved and no validation rule was relaxed.

2026-09-10 — Phase 24 V1456 rejected an orthogonal U1.66 GND escape with
four native DRC violations involving JTAG_TDO, PEDET, and LANE0_TXN. No
candidate was promoted.

2026-09-10 — Phase 24 V1454 corrected the local GND-zone priority/API and
reached native DRC zero, but U1.66 remained an unconnected pad. DRC zero was
not treated as connectivity closure; the zone candidate was rejected.

2026-09-10 — Phase 24 V1455 rejected a left-first U1.66 GND escape with 11
native DRC violations, including lane crossings and QFN JTAG/PEDET conflicts.
U1.66 remains open; no accepted primitive changed.

2026-09-10 — Phase 24 V1453 rejected coupled RSET/RTL_1V1 reallocation:
native DRC found six QFN-field violations, including U1 pad 69 GND and
RTL_3V3 conflicts. No accepted primitive changed.

2026-09-10 — Phase 24 V1450 rejected the outboard REFCLK transplant with 24
native DRC violations, including QFN source-field and connector-launch
conflicts. REFCLK remains open; no accepted primitive changed.

2026-09-09 — Phase 24 V1449 rejected a coupled QFN-field regeneration on
V1428 with 27 native DRC violations, including XTAL_IN/XTAL_OUT shorting,
RSET/GND contact, and rail conflicts. No accepted primitive changed.

2026-09-09 — Phase 24 V1445-V1448 swept four U1.66 GND local launches.
V1446 was best at two native violations but still shorted/mask-bridged
LANE0_TXN at U1 pad 67. No ground candidate was promoted; U1.66 remains open.

2026-09-09 — Phase 24 V1444 rejected a west/south R1 relocation trial. It
exposed stale inherited local GND copper at the old footprint and retained
an RTL_1V1 crossing; future relocation generation must move support return
copper coherently.

2026-09-09 — Phase 24 V1443 compared the earlier V1123 RSET dogleg on V1428.
It failed against the current RTL_1V1 shelf with one crossing and one short;
the older route is not promoted and no accepted primitive changed.
2026-09-09 — Phase 24 V1313: authored a targeted rotated-QFN lane escape
with pad-adjacent departures, an explicit SPISO bypass, and staggered J1
transitions. Native endpoint, negative-control, and DRC evaluation remain
required; production and Path-A assets are unchanged.
2026-09-09 — Phase 24 V1313 rejected: the pad-adjacent rotated-QFN lane
candidate passed saved-board endpoints and negative controls but produced
23 native DRC violations, including source-field/REFCLK conflicts and pair
transition clearances. Preserved as route-implementation evidence; no
production or Path-A assets changed.
2026-09-09 — Phase 24 V1314 rejected: rotated-QFN lane coauthoring passed
saved-board endpoint and negative-control audits but native DRC reported 17
violations across source-field, SPISO, pair-transition, and connector-launch
geometry. Preserved the disposable candidate; production and Path-A assets
remain unchanged.

2026-09-09 — Phase 24 V1355 accepted RTL9210B PERST_N primitive: co-authored
the CLKREQ source transition, then placed PERST on a lower B.Cu shelf below
PEDET with ordinary vias and an F.Cu J1.50 launch. Native DRC has only the
inherited V1058 RTL_3V3 warning; saved-board endpoint audits and source-removal
negative controls pass for PERST, CLKREQ, and PEDET. Remaining support/supply
opens and REFCLK stay open; Path-A and production CAD are unchanged.

2026-09-10 — Phase 24 V1370 accepted: completed the U2.3/U2.8/R2.2/R3.2
RTL_3V3 local support join with direct U2.3 descent, U2.8 right escape, two
ordinary vias, and a B.Cu join. Native DRC is zero and the saved-board audit
plus source-removal negative control pass. The disposable open count falls to
22; RTL_1V1/RTL_5V/GND/REFCLK and other support remain open.

2026-09-09 — Phase 24 V1356 rejected: the first REFCLK left/upper escape
crossed the existing lane/XTAL source field and shorted the pair at its source.
Preserved as route-implementation evidence; no macro-placement or architecture
conclusion was made.

2026-09-09 — Phase 24 V1357 accepted: removed the single inherited dangling
RTL_3V3 stub from the RTL9210B disposable basis. Native DRC is now zero
violations with 27 explicit unconnected support items still open. Path-A and
production CAD remain unchanged.

2026-09-09 — Phase 24 V1359 accepted: connected U1.52 to the RTL_3V3 trunk
with a short F.Cu left escape, one ordinary via, and a B.Cu handoff. Native
DRC remains zero and the open count falls to 26. V1360-V1364 rejected nearby
U1.20 escapes against SPISO3/SPICLK/SPICS or the exposed-pad/GND envelope;
preserved as route evidence for a co-authored source-field repair.

2026-09-09 — Phase 24 V1365 rejected: extending the U1.20 RTL_3V3 dogbone
past the SPICLK endpoint still conflicted with the adjacent SPICLK/SPISO via
field. The next attempt must co-author the neighboring SPI source exits; no
package, placement, or architecture conclusion was made.
2026-09-09 — Phase 24 V1322: tested an F.Cu south-bridge allocation around the
complete V1058 RTL9210B support field while retaining V1258 staggered source
and connector primitives. Native DRC rejected 18 violations from QFN source
fanout, adjacent connector-side transitions, and fixture edge/clearance
interactions. Preserved the disposable board and raw report; no production
CAD or Path-A assets changed.
2026-09-09 — Phase 24 V1321: co-authored the proven V1258 QFN and connector
escapes around the complete V1058 RTL9210B support field, using four south
B.Cu bridge rows. Native DRC rejected 18 violations from rail/SPI B.Cu
intersections and connector/edge clearances. Preserved the disposable board
and raw report as route-implementation evidence; no production CAD or Path-A
assets changed.
2026-09-09 — Phase 24 V1317: recorded the route-class comparison. V1258 is
the accepted complete four-lane basis at U1 orientation 0 degrees; V857/V850
are support/control primitives at incompatible 90/180 degree orientations.
Rotated lane candidates V1311/V1315/V1316 were rejected by native DRC.
Next work returns to V1258 lane preservation with regenerated orientation-0
support fields; no Path-A or production assets changed.
2026-09-09 — Phase 24 V1315 rejected: rotated-QFN lane allocation passed
native endpoints and four negative controls but DRC reported 14 source,
SPISO, pair-row, and connector-transition violations. Preserved the
disposable evidence; production and Path-A assets remain unchanged.
2026-09-09 — Phase 24 V1316 rejected: adding four lanes to the native-clean
V850 rotated-support field passed endpoint and negative-control audits but
native DRC reported 14 source-transition and outer-launch violations.
Preserved the disposable evidence; V850 support and production/Path-A assets
remain unchanged.
2026-09-09 — Phase 24 fresh native recheck: the current Path-A
`PHASE24_STORAGE_J8_V5_VBUS_V1.kicad_pcb` reports 732 DRC violations and 400
unconnected items. The receipt is preserved and no finding or severity was
waived.
2026-09-09 — Phase 24 documentation hygiene: rechecked the live Path-A basis
against the current J8 XML. `PHASE24_STORAGE_J8_V5_VBUS_V1.kicad_pcb` passes
zero-mismatch pad parity; V37 fails against that current authority because its
recorded XML was superseded. Marked V37 historical without altering raw
receipts, and corrected the narrative current-candidate references.
2026-09-09 — Phase 24 correction: V37 was incorrectly described as
superseded because a stale XML oracle was used. Current J8 XML parity is zero
mismatches; V37 remains disposable route evidence at 603 DRC/399 opens with
no shorting entries. The earlier false comparison is superseded, not erased.
2026-09-09 — Phase 24 V1457/V1458 rejected two additional RTL9210B U1.66/
U1.69 ordinary-via edge-access probes. Native DRC reported 13 and 5
violations respectively, including real ground-to-signal shorts/clearance
failures. Preserved both disposable boards and receipts; no layer, clearance,
severity, Path-A, or production rule was changed.

2026-09-09 — Phase 24 V1440/V1441 rejected westward R1 relocation trials:
the mixed-layer escape conflicted with RTL_3V3/RTL_1V1, and the direct F.Cu
escape crossed R1 GND/RTL_1V1. V1428 remains accepted.

2026-09-09 — Phase 24 V1439 rejected eastward R1 relocation: the RSET bypass
crossed RTL_3V3/RTL_1V1 and shorted USB_RXN0. The trial is preserved; V1428
remains the accepted composite base.

2026-09-09 — Phase 24 V1442 added a net/layer-aware A* RSET search over the
saved V1428 geometry. Both obstacle models found no path, so no PCB was
generated and no architecture conclusion was drawn; native DRC remains the
acceptance authority.

2026-09-09 — Phase 24 V1432/V1433 rejected XTAL_IN southwest and offset
routes from V1428. V1432 retained RTL_1V1 clearance and RTL_3V3 shorting;
V1433 added LANE0_TXN crossing/shorting. XTAL_IN remains open; V1428 is
unchanged.

2026-09-09 — Phase 24 V1423/V1424 rejected XTAL_OUT trials. V1423 retained
seven native DRC violations in the QFN exposed-pad/3V3/1V1 field; V1424's
west/top relocation retained one XTAL_OUT/RTL_1V1 crossing and one 0.100-mm
clearance violation. Preserved both disposable fixtures and reports; no
accepted Path-B primitive, production asset, or Path-A asset changed.

2026-09-09 — Phase 24 V1425/V1426/V1427 rejected additional XTAL_OUT route
classes; V1425 reduced the failure to one rail clearance, V1426 retained one
rail crossing, and V1427 shorted RTL_3V3. V1428 then composed accepted V1418
QFN-ground and V1420 SSD_3V3 primitives: native DRC zero, saved-board audit
and two source-removal controls PASS, with ten unconnected pads remaining.

2026-09-09 — Phase 24 V1429/V1430 rejected U1.63 RTL_1V1 route trials from
the V1428 accepted composite: V1429 crossed LANE0_RXN and duplicated a via;
V1430 shorted LANE0_RXP/SPISI fields. Preserved evidence and retained V1428
as the active accepted-primitive base.

2026-09-09 — Phase 24 V1431 rejected a U1.66 GND west escape from V1428;
native DRC found a no-net pad short and LANE0_RXN conflicts. U1.66 remains
open and V1428 remains the accepted composite base.
2026-09-09 — Phase 24 V1422 rejected an outboard RSET B.Cu shelf. Native DRC
reported 12 source-field, GND, and accepted-rail violations; RSET remains
open and no production asset changed.
2026-09-09 — Phase 24 V1420 accepted the native J1 SSD_3V3 pad 2/4/6/8
contact join. Native DRC is zero and the saved-board endpoint/source-removal
audit passes; the fixture falls to 11 opens. Remaining Path-B support stays
open and Path A is unchanged.
2026-09-09 — Phase 24 V1421 rejected the first RSET perimeter route. Native
DRC found two violations against the accepted 1V1 perimeter and R1 GND pad;
RSET remains open and accepted Path-B/Path-A assets are unchanged.
2026-09-09 — Phase 24 V1419 rejected the direct U1.66-to-exposed-pad GND
trial; native DRC retained one LANE0_RXP crossing. The U1.45 primitive remains
accepted and U1.66 ground closure remains open.
2026-09-09 — Phase 24 V1396-V1398 rejected additional U1.63 RTL_1V1 source
escapes from the accepted V1392 U1.60 basis. Jogged, lower-pocket, and
diagonal-top departures retained five native DRC violations each, chiefly
PCIe source-field collisions. Evidence is preserved; V1392 and Path-A remain
unchanged and U1.63 remains open.
2026-09-09 — Phase 24 V1400-V1402 preserved further U1.63 source-field
evidence. V1400/V1401 each retained one native conflict; V1402's disposable
LANE0_RXN transition relocation produced four violations against the paired
PCIe TXP launch and REFCLK field. This is coupled QFN/PCIe geometry, not a
Path-A or production change. V1392 U1.60 remains accepted.
2026-09-09 — Phase 24 V1399 rejected the first F.Cu/B.Cu RTL_5V fan-in
trial from V1392. Native DRC reported 9 violations against accepted 1V1,
3V3, and SPI geometry. The disposable board and report are preserved;
accepted V1392 and Path-A remain unchanged.
2026-09-09 — Phase 24 V1418 accepted the isolated U1.45-to-exposed-pad GND
primitive. Native DRC is zero and the saved-board endpoint/source-removal
audit passes; the fixture falls to 13 opens. U1.66 and remaining support stay
open, with Path A and production CAD unchanged.
2026-09-09 — Phase 24 V1411 accepted the RTL_3V3 U2-to-U1 support join after
native DRC and saved-board/source-removal audit passed. V1412 accepted the
U1.33-to-C5 RTL_5V corridor with native DRC zero; V1413 rejected the U1.17
fan-in with six native violations. V1409/V1410 remain rejected alternatives;
Path A and production CAD remain unchanged.
2026-09-09 — Phase 24 V1416/V1417 preserved rejected QFN-GND launch trials.
V1416 retained one LANE0_RXP crossing; V1417's lower route retained nine
native violations against RESET_N and the QFN field. Ground closure remains
open; accepted rail primitives and Path A are unchanged.
2026-09-09 — Phase 24 V1415 accepted the complete RTL_5V fan-in after native
DRC reported zero violations and the saved-board U1.17/U1.33/C5.1 endpoint
and source-removal audit passed. V1414 remains rejected for its SPISI
crossing; Path A and production CAD remain unchanged.
2026-09-09 — Phase 24 V1385-V1389 explored the remaining RTL_1V1 source-field
class from V1384. V1385 coupled U1.60/U1.63 and was rejected at 10 native DRC
violations; V1386 reduced U1.60 alone to 3; V1387 reduced it to one
RTL_1V1/RTL_3V3 B.Cu crossing; V1388 and V1389 were rejected at 10 and 4.
All are preserved as disposable route evidence. The V1384 accepted U1.16/
U1.25 basis and Path-A assets remain unchanged; U1.60/U1.63 remain open.
2026-09-09 — Phase 24 V1392 accepted the U1.60 RTL_1V1 source escape after
native DRC reported zero violations and the saved-board/source-removal audit
passed. V1393-V1395 tested coupled/staggered/near-via U1.63 additions and were
rejected at 2, 2, and 4 native violations. The accepted V1392 primitive and
all Path-A assets remain unchanged; U1.63 and other Path-B support remain
open.
2026-09-09 — Phase 24 V1384 accepted the U1.25 RTL_1V1 fanout on the complete
V1382 U1.16 basis. Native DRC reports zero violations with 18 fixture opens.
The corrected saved-board audit derives connectivity from KiCad's loaded
board objects and passes U1.16/U1.25/U1.36/U1.40/U1.50/U1.55/C4.1 plus a
source-segment removal negative control. U1.60/U1.63 and remaining Path-B
support/control groups remain open; no production CAD or Path-A asset changed.

2026-09-10 — Phase 24 V1382 accepted: U1.16 RTL_1V1 descends to `(100.8,75.0)`
and hands off on B.Cu to the existing `(102.0,64.8)` 1V1 trunk. Native DRC
is zero; saved-board audit and source-removal negative control pass. U1.25/
U1.60/U1.63 remain open.

2026-09-10 — Phase 24 V1377/V1378 rejected: U1.55 RTL_1V1 perimeter and F.Cu
join attempts conflicted with the existing GND field and U1 exposed/no-net
pads. Preserved the disposable evidence; the V1374 accepted basis remains
unchanged and a different source-field allocation is required.

2026-09-10 — Phase 24 V1379 accepted: U1.55 RTL_1V1 uses a same-layer F.Cu
perimeter route around the exposed-pad/GND field and joins the accepted U1.50
corridor. Native DRC is zero; saved-board audit and source-removal negative
control pass for U1.36/U1.40/U1.50/U1.55/C4.1. U1.16/U1.25/U1.60/U1.63 remain
open.

2026-09-10 — Phase 24 V1371 rejected: the first RTL_1V1 split-bus attempt
created 16 native DRC violations against the existing lane escape, U1.50
neighboring USB pad, and RTL_3V3 corridor. Preserved as route evidence; the
next 1V1 repair must use the right/top rail corridor.

2026-09-10 — Phase 24 V1374 accepted: U1.50 RTL_1V1 rises above the USB pad
row and reaches the existing `(97.8,63.6)` transition. Native DRC is zero;
saved-board audit and source-removal negative control pass for U1.36/U1.40/
U1.50/C4.1. The disposable open count falls to 21; remaining 1V1 pads stay
open.

2026-09-09 — Phase 24 V1367 rejected: the co-authored U1.20/SPICLK source
variant still shorted at the RTL_3V3 transition because the SPICLK F.Cu source
row occupies its via clearance envelope. Preserved as local source-field
evidence; Path-A and production CAD remain unchanged.

2026-09-10 — Phase 24 V1368 accepted: transplanted the earlier native-clean
RTL9210B U1.20 RTL_3V3 left dogbone/B.Cu escape onto the current V1359 basis.
Native DRC is zero; saved-board audit and source-removal negative control pass
for U1.20/U1.34/U1.39/U1.52/C3. U2/R2/R3 support joins remain open.
2026-09-09 — Phase 24 V1347: accepted the RTL9210B CLKREQ_N primitive. Native
U1.13-R3.1-J1.52 connectivity and the source-removal negative control passed;
the overpass clears the lane and support fields. Native DRC retains only the
inherited V1058 support warning. PERST/REFCLK and remaining support remain
open; production CAD and Path-A assets are unchanged.
2026-09-09 — Phase 24 V1328: accepted the strongest RTL9210B lane primitive
to date. The complete V1058 support/SPI field was combined with the V1258
staggered QFN escape and an outboard translated J1 launch. Native saved-board
connectivity passed all four lane endpoints and four source-removal negative
controls. Native DRC reported no lane electrical violations; inherited support
warning/open support connections remain fixture scope. No production CAD or
Path-A assets changed.
2026-09-09 — Phase 24 V1340: accepted the PEDET support primitive on the
V1332 RTL9210B lane basis. Native U1.8-R2.1-J1.69 connectivity and the
source-removal negative control passed; native DRC retained only the inherited
V1058 support warning. Remaining controls and support are still open. No
production CAD or Path-A assets changed.
2026-09-09 — Phase 24 V1332: accepted the current original-J1 RTL9210B lane
basis. TXP was moved to a far-right B.Cu corridor; native DRC then showed only
the inherited V1058 RTL_3V3 dangling warning. Native saved-board connectivity
and four source-removal negative controls passed. This is a lane primitive,
not full Path-B closure; support/control opens remain. No production CAD or
Path-A assets changed.
2026-09-09 — Phase 24 V1318/V1319: merged the complete orientation-0 V1058
RTL9210B support/SPI field with the accepted V1258 lane basis, then tested a
fresh four-row northbound lane allocation around the support field. Native DRC
rejected V1318 (31 violations) and V1319 (36 violations) for coupled
source-field, rail-trunk, connector-launch, and clearance interactions.
Preserved both disposable boards and raw reports as route-implementation
evidence; no production CAD or Path-A assets changed. Next work must co-author
support, source escape, and connector launch allocation together.
2026-09-09 — Phase 24 V1312 rejected: the attempted rotated-QFN split-source
escape caused native pad-field shorts/crossings and failed its saved-board
lane endpoint audit; DRC reported 45 violations. Preserved the disposable
candidate as route-implementation evidence. Production and Path-A assets
remain unchanged.
2026-09-09: V1145 and V1146 tested XTAL_IN coexistence with accepted V1144
XTAL_OUT. Native DRC found five and seven source-field violations; both were
rejected. V1144 XTAL_OUT remains accepted, while XTAL_IN and full support
closure remain open.
2026-09-09: V1147 retained V1144 XTAL_OUT and moved XTAL_IN left below the
GND triangle. Native DRC retained five first-millimeter QFN source-field
violations; the downstream corridor was clean. Rejected pending staggered
source-transition work.
2026-09-09: Rejected V1148 staggered XTAL source-via trial. Native DRC found
ten violations, including incomplete removal of inherited rail branches and
a dangling XTAL_IN transition. Future staggered-via tests require native-safe
bulk removal before evaluation; Path A and production CAD remain unchanged.

2026-09-08: Strengthened the JMS583 VBUS audit to include U11.10
JMS_VBUS_SENSE, then preserved V10 as rejected evidence. V10 passes all three
divider endpoints and the trace-removal negative control, but native DRC
reports 532 findings with a real VBUS/JMS_VBUS_SENSE handoff short. VBUS
remains open and no route was promoted.

2026-09-08: Fresh native root ERC after the U12 label correction reports 925
violations. The prior 927-count report remains historical; no ERC severity
was changed and the root ERC gate remains open.

2026-09-08: VBUS sense V14 was preserved as the cleanest complete-endpoint
trial so far. U11.16, U11.10, R82, and R83 plus the trace-removal negative
control pass; native DRC has no VBUS/JMS_VBUS_SENSE shorting class, but still
reports 528 findings / 499 inherited opens with added clearance and crossing
classes. It was not promoted.
2026-09-08: RTL9210B V551 proves the bottom 1V1 group in the native graph
with an exact negative control, but native DRC rejects the below-REFCLK
shared return for XTAL_OUT, LANE0_RXP, and RTL_3V3 conflicts. That route
class is exhausted; coherent bottom source-field regeneration remains next.
Path A and production CAD remain unchanged.
2026-09-08: V622 tested a shallow upper-left U1.39 RTL_3V3 dogbone. Native
connectivity and the trace-removal negative control passed, but native DRC
found a real RTL_3V3-to-USB_DM short plus QFN/via hole and solder-mask
clearance violations. The scalar U1.39 escape class is rejected; the next
trial must regenerate the complete lower QFN field under unchanged rules.
2026-09-08: V623 reran the coordinated lower RTL_3V3 generator. Native DRC
rejected it for a real RTL_3V3/RSET short and crossing at U1.52/R1 plus the
U1.39/USB_DM source-field clearance class. Preserve the raw route evidence;
the lower QFN and RSET departures must be coallocated next. Path A and
production CAD remain unchanged.
2026-09-09: V1010 rejected the direct U1.36 RTL_1V1 via for contacting the
RTL_3V3 collector. V1011 moved it clear but left the transition isolated;
V1012 added the same-net In2 segment into the filled 1V1 pocket. Native DRC
then showed no electrical violations and U1.36 was no longer unconnected.
Retain V1012 as the accepted U1.36 primitive; full 1V1 closure remains open.
2026-09-09: V1006/V1007/V1008 rejected U1.16 RTL_1V1 departures after native
DRC localized their failures to the existing RTL_5V and CLKREQ_N QFN-edge
fields. V1009 accepted the far-right orthogonal departure below that field
and an ordinary-via handoff into the existing In2 1V1 pocket; native DRC
reported no electrical violations beyond intentional dangling source tracks
and inherited opens. Continue remaining 1V1 endpoints incrementally.
2026-09-08: RTL9210B V549 proves U1.55/U1.60/U1.63 1V1 connectivity and the
exact negative control, but native DRC rejects the shared return for REFCLK,
RTL_3V3, and LANE0_RXP crossings. The outward shared-return class is
rejected; bottom support/REFCLK must be reallocated together. Path A and
production CAD remain unchanged.
2026-09-08: RTL9210B V550 proves the isolated U1.55 1V1 native graph and
exact branch-removal negative control, but native DRC rejects it for 3V3 and
XTAL_OUT conflicts. Bottom 1V1 completion requires coherent source-field
regeneration; Path A and production CAD remain unchanged.
2026-09-08: RTL9210B V542-V545 are rejected U1.40 1V1 transition trials;
their native connectivity and exact negative controls pass, but DRC finds
3V3 or U1 pad-field conflicts. V547 proves U1.55/U1.60/U1.63 connectivity
with an exact bottom-edge negative control, but DRC rejects its via row
against REFCLK and 3V3 geometry. V546 remains the accepted U1.40 primitive;
Path A and production CAD remain unchanged.
2026-09-08: RTL9210B V548 proves U1.55/U1.60/U1.63 1V1 connectivity and the
exact negative control, but native DRC rejects the outward via row for
XTAL_OUT and RTL_3V3 conflicts. The next attempt requires coherent bottom
support/REFCLK field reallocation; Path A and production CAD remain
unchanged.
2026-09-08: RTL9210B V528/V529 preserve native connectivity and exact
branch-removal negative controls but are rejected by DRC. V528 crosses the
F.Cu 1V1 collector; V529 conflicts with the XTAL_IN B.Cu return. The next
step is coherent XTAL/3V3 source-field reallocation, not another fixed-field
detour. Path A and production CAD remain unchanged.

2026-09-07: Retained RTL9210B V320 M.2 coordinate-frame correction. J1 now
has a real local footprint anchor while native reload verification proves all
physical pad centers are unchanged. This fixes disposable authoring geometry;
it does not promote Path B or alter production CAD.

2026-09-07: Rejected RTL9210B V318/V319 coordinated In2 rail trials. Native
DRC found real shorts/crossings at proposed transitions despite fewer opens;
inner-layer power remains a valid resource, but the next candidate must use a
single coordinated rail/lane via map. Path A and production CAD unchanged.


## 2026-09-06 — Authorized dual-mode storage upgrade qualification checkpoint

Checkpointed Phase 24 at `68aac08` before editing production KiCad assets.
Retained the selected `SWAP_ETH_STORAGE` macro and all prior routing evidence;
qualified TUSB9261 and the TI selector families for design review; identified
JAE `SM3ZS067U215BMR1500` as the correct M-key family direction; and rejected
ASM2362 implementation because the public source lacks the exact design pack,
firmware/configuration/programming path, and traceable prototype procurement
needed for a pad-authoritative schematic. The original SATA-only board remains
preserved. See the storage-upgrade checkpoint, qualification, source receipt,
and blocker report under `pisxme/reva-clean/`.

## 2026-09-06 — Dual-mode storage blocker independently corroborated

An independent read-only review confirmed that public ASM2362-family, JMS58x,
and RTL9210B material does not provide the manufacturer-authoritative bare-chip
design package required for implementation. The JAE U215 M-key variant
identity/procurement path was strengthened, while exact land-pattern capture
and the NVMe bridge design pack remain gated. No production KiCad assets were
changed.
2026-09-09 — Phase 24 V62 rejected: local STORAGE_SEL escape removed the U14
MODE_IN collision but shorted the U13 transition into M2 SATA RX and retained
the XOUT/JMS_XAVDDH short. Native DRC was 598 / 349. Preserved board, report,
script, and receipt; V54 remains preferred.
2026-09-09 — Phase 24 V54 accepted as the best disposable storage
ground-return parent. Full F.Cu POWER_GND pad connection removed all 10
starved-thermal findings and reduced native opens to 350 at 601 total DRC;
USB3/SATA/J8 parity audits pass and native shorts remain zero. No signal,
production authority, validation rule, or layer contract changed.

## 2026-09-05 — Phase 24 clock orientation trial rejected

Rejected the 90-degree near-west crystal trial; explicit ordered three-lane escape remains required.

Corrected the disposable clock sweep output-path bug; the fresh ordered layer-split rerun reports 215 DRC violations and remains rejected.

Rejected mixed-layer ordered clock escape trial; local U7 oscillator/SATA pad-field obstruction remains and Phase24 stays active.

Rejected surgical SATA-launch reroute trial; regenerated TX_N/TX_P doglegs still crossed clock/PCIe corridors, so a coordinated U7 pad-field graph is required.

Recorded the initial obstacle-aware clock route-search diagnostic; conservative source seeding found no XI path and requires explicit package-edge dogbone modeling.

Recorded seeded-exit search result; inherited SATA launch still blocks downstream XI search, so clock and SATA must be solved as one coordinated escape graph.

## 2026-08-30 — Phase 16 PCIe routing checkpoint

- Added the native-loaded Phase 16 PCIe candidate and focused regression.
- Preserved exact PER0/REFCLK/PERST/PET0 net graphs and the transmitter-side
  AC-coupling split at 0.13208 mm track width with ordinary 0.50/0.30 mm vias.
- Native DRC has zero target-net shorts, crossings, or dangling vias. Two
  authoritative CM5 SMD breakout clearance findings remain explicitly marked
  `REV_A_EMPIRICAL_RISK`; inherited acreage DRC debt is not conflated with
  this focused route gate.

## 2026-08-30 — Phase 17 Ethernet authority checkpoint

- Promoted the eight CM5 Ethernet MDI boundaries to native global named nets
  and corrected the generated symbol pin-Y convention and instance UUID path.
- Native ERC is zero and the XML netlist proves J7-to-ESD-to-MagJack mapping
  for all eight pairs; PCB regeneration is required before routing.

## 2026-08-30 — SERVICE ESD procurement recorded

- Added TI `TPD2EUSB30DRTR` current procurement evidence to the matrix and
  kept its package-specific land-pattern gate explicit.


## 2026-08-30 — SERVICE ESD electrical authority corrected

- Replaced the four-pin USB2 ESD placeholder with TI `TPD2EUSB30DRTR`, using
  the actual two-I/O-plus-ground interface and documented active procurement.
- Explicitly kept its exact DRT land pattern gated; no generic SOT-23 pattern
  is being treated as equivalent.


## 2026-08-30 — Native netlist export gate closed

- Reproduced and fixed underscore-bearing KiCad references generically.
- Native KiCad 10.0.5 netlist export now completes without annotation warnings;
  added an isolated regression test and receipt.
- Corrected the service-authority rerun path so the USB-C footprint cannot be
  assigned to the separate unresolved service ESD placeholder.


## 2026-08-30 — KiCad annotation normalization path added

- Identified underscore-bearing generated references as the cause of KiCad
  native annotation/netlist-export warnings.
- Added a generic normalization stage and regression test mapping them to legal
  unique references while retaining descriptive Value/MPN fields.


## 2026-08-30 — High-current input connector authority selected

- Selected two Molex `0039300020` / `39-30-0020` Mini-Fit Jr. 5569
  right-angle 2-position headers for the independent 12 V inputs.
- Recorded active-series, multi-distributor procurement evidence and the
  through-hole assembly implication; exact land-pattern materialization remains
  a required Phase 14 PCB step.


## 2026-08-30 — Phase 14 CM5 and MagJack pattern gates verified

- Added machine checks for the clean CM5 200-pad footprint/model and EDAC
  18-pad MagJack footprint, including rejection of the legacy Trxcom pattern.
- Kept SXM2 exact mask/paste/A1 and high-current input connector authority open.


## 2026-08-30 — Phase 14 service authority regression correction

- Updated the Phase 8 audit to require the selected Amphenol
  `10171746-00021LF` instead of the retired generic USB2 placeholder.


## 2026-08-30 — Ethernet MagJack authority replacement

- Closed the former exact `TRJG0926HENL` procurement gap with EDAC
  `A70-112-331N126`, backed by the EDAC manufacturer drawing and a current
  exact Mouser record showing New Product lifecycle, MOQ 1, and immediate
  stock. The original Trxcom part remains an immutable reference only.
- Recorded the EDAC electrical/mechanical contract, procurement evidence,
  `MEDIUM` sourcing risk, LINK-PP backup, URLs, and provenance under
  `pisxme/reva-clean/authority-inventory/primary-docs/ethernet-magjack/`.
- Explicitly rejected reuse of the legacy footprint: its two 3.20 mm plus two
  1.70 mm non-plated holes do not reproduce the EDAC drawing's two 3.25 mm
  plus four 1.02 mm hole groups. Phase 3 must generate and parity-check the
  EDAC land pattern in the clean namespace.

## 2026-08-30 — Phase 3 clean-library extraction checkpoint

- Added a deterministic extractor for the approved CM5IO `ComputeModule5-CM5`
  and Ethernet symbol definitions, rewriting them into the local
  `PiSXMeRevAClean` namespace and removing donor footprint/model references.
- Copied the approved CM5 carrier footprint/model into the project-local
  library and added the EDAC MagJack footprint derived from the EDAC drawing;
  the EDAC footprint keeps the exact EDAC hole groups and has no unvalidated
  3D model attached.
- Added a structural CM5 symbol-pin to footprint-pad parity check: 200 numeric
  symbol pins equal 200 numeric footprint pads. Native KiCad PDF parse/export
  for the root and all ten child sheets also passed; Phase 3 connectivity/ERC
  remains open.

## 2026-08-30 — EDAC hole-group authority correction

- Corrected the EDAC authority record to retain the complete manufacturer
  mechanical pattern: two 3.25 mm holes, two 1.60 mm holes, and four 1.02 mm
  guide holes. The clean generated footprint and its receipt already carry
  all eight holes; the authority narrative now matches the artifact.

## 2026-08-30 — Phase 3 native contract connectivity

- Added deterministic local contract symbols and native wire connectivity to
  all ten clean child sheets. Every child interface label now terminates on a
  real passive pin in the local `PiSXMeRevAClean` namespace.
- Fresh KiCad 10.0.5 ERC reduced the scaffold from 78 to 40 violations; the
  remaining records are root sheet-pin/child hierarchy association failures.
  The Phase 3 receipt records this as an open technical gate rather than
  suppressing ERC or treating the scaffold as production connectivity.
- Added all ten contract definitions to the project-local symbol library and
  kept the selected CM5/EDAC production assets separate from these fixtures.

## 2026-08-28 — M2 right-edge outline expansion checkpoint

- Expanded only the active board's congested right edge from 220 × 140 mm to 240 × 140 mm and moved J9/J10/J11 to x=230 mm so their bodies remain inside the new edge. CM5, PCIe, power, ESD-support placement, routing, zones, schematic, and manufacturing outputs were not changed.
- Structural evidence: J9/J10 retain approximately 1.65 mm edge margin and J11 approximately 3.30 mm; signal segment counts and the In1/In2/In3/In4 signal-layer policy are unchanged. Isolated native DRC completed with 785 inherited violations and 178 unconnected items, so this is not a routing or release signoff.
- M6 owns all connector-side copper reconstruction and must revalidate mating, cable, courtyard, return-path, and signal-termination behavior before the expansion becomes release geometry.

## 2026-08-22 — UART and recovery routing checkpoint

- Routed the actual CM5 net-bearing UART/recovery pads: J2 pad 51 `/UART_RX`, J2 pad 55 `/UART_TX`, and J2 pad 93 `/CM5_nRPIBOOT`. The route uses a deliberate upper/perimeter escape with F.Cu/B.Cu transitions for UART and a short F.Cu control route for recovery.
- The internal UART header J8 was moved to `(214,81)` and rotated 90 degrees so its plated through-hole pads remain clear of existing USB/PCIe through-layer copper. The nRPIBOOT test point TP3 was moved to `(145,125)` to keep recovery access out of the V100 power trunk and the regulator output cluster. No schematic nets or logical assignments changed.
- Final measured routes are `/UART_RX` 125.660 mm with 2 vias, `/UART_TX` 146.460 mm with 2 vias, and `/CM5_nRPIBOOT` 55.860 mm with no vias. Lock-free KiCad 10.0.5 DRC on a project copy returned 67 inherited library/silkscreen findings and zero new electrical, clearance, crossing, mask, hole, dangling, or sliver findings. Receipt: `routing/UART_RECOVERY_ROUTING_RECEIPT.md`.

## 2026-08-22 — local low-speed control subset checkpoint

- Routed `/GATE_A`, `/GATE_B`, and `/RT_1MHZ` as a deterministic local-control subset. The gate-B path was deliberately kept around the existing VCAP_B and high-current copper; the RT timing path enters U1 from below rather than crossing the CM5 feedback pads.
- The checkpoint adds 8 F.Cu segments and no vias. Lock-free KiCad 10.0.5 DRC on a project copy returned 68 inherited library/silkscreen findings and no new shorts, crossings, clearances, mask bridges, hole conflicts, dangling routes, or copper slivers. Longer low-speed/control trunks remain for the next pass. Receipt: `routing/LOW_SPEED_LOCAL_CONTROL_RECEIPT.md`.

## 2026-08-22 — SERVICE USB2 routing checkpoint

- Routed the CM5 USB2 SERVICE data pair through U15 to both reversible J11 USB-C orientations. To remove a real conflict with the already committed FAST-A/FAST-B corridors and lower-right power/debug copper, J11 and U15 were moved to the clear right-edge gap at `(210.5,40)` and `(196,40)`; no schematic nets or USB role logic changed.
- The deterministic checkpoint adds 28 segments and 6 F.Cu↔B.Cu vias. `/USB_SERVICE_DP` is 112.4712 mm total and `/USB_SERVICE_DM` is 105.2728 mm total. The route uses F.Cu/B.Cu only and does not enter the PCIe or USB3 corridors.
- Lock-free KiCad 10.0.5 DRC on a project copy returned 68 inherited library/silkscreen findings and no new service-route shorts, crossings, clearances, hole conflicts, mask bridges, dangling items, or copper slivers. The two remaining SERVICE CC1/CC2 unconnected items are intentionally deferred to the low-speed/control routing class. Receipt: `routing/SERVICE_USB2_ROUTING_RECEIPT.md`.

## 2026-08-21 — USB peripheral 5 V routing checkpoint

- Routed the independent `/USB_5V_PERIPH` output from U16 to both FAST-A/FAST-B source-switch input pairs and the SERVICE current limiter. The deterministic checkpoint adds 20 segments and 4 vias; U13 was moved from `(184,132)` to `(184,138)` to keep its input out of the FAST-B RX2 escape window and away from the recovery test pad.
- Lock-free KiCad 10.0.5 DRC on a project copy returned 69 inherited library/silkscreen findings and 379 expected unconnected items, with zero new shorts, crossings, clearances, mask bridges, hole conflicts, dangling routes, or width violations. Receipt: `routing/USB_5V_ROUTING_RECEIPT.md`.

## 2026-08-21 — CM5 5 V output routing checkpoint

- Routed the U1 `/CM5_5V` output to the buck's separated output pads, C5/C6/C7, the CM5 feedback branch, and all six official CM5 +5 V contacts on J2. The deterministic checkpoint adds 29 segments and 2 vias; the long contact-to-buck trunk stays left of the FAST-B USB3 transition field and the local output manifold stays left of the USB-C control packages.
- Lock-free KiCad 10.0.5 DRC on a project copy returned 69 inherited library/silkscreen findings and 386 expected unconnected items, with zero new shorts, crossings, clearances, solder-mask bridges, hole conflicts, dangling routes, or width violations. Receipt: `routing/CM5_5V_ROUTING_RECEIPT.md`.

## 2026-08-21 — CM5 protection-side power routing checkpoint

- Corrected and routed the LM74700 U2/U3 protected-bus input/cathode pads plus C8/C9 VCAP/fused support paths. The deterministic checkpoint adds 22 local-power segments and 4 vias while leaving CM5/USB output rails, ground zones, and control nets for later classes.
- Lock-free KiCad 10.0.5 DRC on a project copy returned 69 inherited library/silkscreen findings and 398 expected unconnected items, with zero new shorts, crossings, clearances, mask bridges, or width violations. Receipt: `routing/CM5_POWER_ROUTING_RECEIPT.md`.

## 2026-08-21 — CM5 power-pin correction before regulator routing

- Before continuing the power class, an audit against the preserved official CM5IO netlist found that J2 pads 77/79/81/83/85/87 were stranded on a legacy `/5V` net rather than the U1 `/CM5_5V` buck output, while the official CM5 3.3 V output pads 84/86 were unassigned. The schematic generator, active schematic, and active PCB were corrected to expose and assign those exact pins; no high-speed or connector geometry changed.
- This is a genuine source-connectivity correction. It is recorded separately in `routing/CM5_POWER_PIN_CORRECTION.md` and must be validated before the CM5/USB rail routing checkpoint.

## 2026-08-21 — V100 high-current power routing checkpoint

- After correcting the protected power-source net names, routed the dual raw 12 V branches, branch fuses/protection entries, protected `/VPROT_12V` bus, distributed 13-transition SXM2 power feed, and CM5-buck input islands. The checkpoint adds 76 power segments and 39 power vias; the protected main trunk is 5.0 mm on B.Cu, with via arrays at branch and SXM2 transitions.
- Lock-free KiCad 10.0.5 DRC on a project copy returned 69 inherited library/silkscreen findings and 401 expected unconnected items, with zero new power-route shorts, clearances, solder-mask bridges, dangling items, hole-spacing errors, or width violations.
- Combined high-speed review was recorded before accepting the power class. PCIe/FAST-A remain measured; FAST-B's 5.209–9.586 mm SuperSpeed skews remain an explicit SI risk, not a hidden DRC success claim. No L2 reference-plane slot was introduced by the new power copper.

## 2026-08-21 — cooling-header protected supply correction

- A second power-source audit found J5/J6/J7 cooling-header supply pins on `/12V_FAN` with no source or net tie. Their intended protected 12 V supply is now `VPROT_12V` in the schematic generator, active schematic, and active PCB.
- This is a net-source correction before routing, not an added feature; fan/pump control nets and connector placement are unchanged.

## 2026-08-21 — protected V100 power-bus net correction

- Before beginning high-current routing, the active design was audited for a power-net boundary inconsistency. The SXM2 connector's 130 V100 power contacts were on `/12V`, while the protected dual-input bus and buck inputs were on `/VPROT_12V`, with no schematic tie.
- The authoritative topology is input connector → fuse → LM74700/MOSFET protection → protected V100 bus. The J1 PWR contract was corrected to `VPROT_12V` in the generator and schematic, and the active unrouted PCB was normalized to the same net without changing pin mapping or adding an implicit short.
- A lock-free KiCad 10.0.5 DRC run on a project copy returned normally (69 inherited non-unconnected findings and 499 expected unconnected items). High-current copper routing starts only after this checkpoint.

## 2026-08-20 — Initial KiCad inventory

- KiCad 10.0.5 is installed at `/Applications/KiCad/KiCad.app`.
- The official IPC server preference was found disabled and enabled for this integration.
- The bridge runtime target is Homebrew Python 3.11 with `kicad-python==0.7.1` and the MCP SDK.
- Direct inspection found broad PCB IPC coverage, CLI DRC/ERC/export coverage, and a broken/missing released schematic binding; this limitation is preserved in `CAPABILITY_MAP.md`.

## 2026-08-20 — Bridge implementation and live verification

- Added the modular `kicad-codex-bridge` MCP server using official `kicad-python==0.7.1`, KiCad IPC socket discovery/token caching, descriptor-driven protobuf introspection/raw calls, bundled `kicad-cli`, and a project-root-scoped atomic file layer.
- Registered the server globally with the current `codex mcp add` CLI using `KICAD_PROJECT_ROOT`; direct MCP stdio discovery returned 61 tools.
- Live KiCad 10.0.5 control succeeded on `/tmp/kicad/api.sock`: PCB inspection, footprint creation/move/rotation, pad inspection, board text/graphic/track/via creation, selection, save/save-as, readback, DRC, raw `GetVersion`, and Gerber export were verified on the disposable fixture.
- KiCad JSON DRC completed with six fixture violations; this is validation evidence, not a clean-design claim. ERC completed through `kicad-cli` against an untouched bundled KiCad schematic template.
- Schematic live IPC remains unavailable in this installed official wheel; footprint flip/mirror is also not faked because no native KiCad 10.0.5 IPC operation was exposed.

## 2026-08-20 — SXM2 reference archaeology

- Acquired and preserved `bbenchoff/SXM2toPCIe` at commit `3173b02c085218d66c4a2a9e5492853fb53ee097` under `references/SXM2toPCIe`; the upstream nested worktree remained clean.
- Opened a separate working copy through the live KiCad 10.0.5 IPC bridge and verified the PCB/schematic parse, local library resolution, and logical netlist agreement.
- Recorded the critical nonclaim: the pinned PCB is largely unrouted between J2 and the PCIe edge. KiCad DRC reported 73 violations and 285 unconnected items; ERC reported 472 violations. No upstream source was fixed.
- Added machine-readable SXM2/PCIe mapping, source manifest, constraints, power-tree evidence, conceptual board-zone annotation, and the hardware-archaeology report. CM5 integration remains intentionally out of scope.

## 2026-08-20 — Independent PCIe x1 architecture study

- Created branch `codex/pcie-x1-architecture` for the clean-room x1 design phase; no final combined-board schematic or PCB layout was created.
- Acquired the public LiuXinyu12378 carrier reference at commit `27dd1229889f4f0c03324b419931d2d466fccde4` and the official Raspberry Pi CM5IO revision-2 KiCad archive (ZIP SHA-256 `48b14a6757b0edc0ac110331445f35a4212b5ce432bdcec6605c99431b59496b`); both are ignored immutable observation references.
- Confirmed from the official CM5 datasheet that CM5 is a PCIe Gen2 host, direct-IC TX/RX must cross by function, CM5 TX coupling is internal, V100/peripheral TX needs external 220 nF coupling near the source, PCIe is 90 Ω, within-pair matching is ideally 0.1 mm, `CLKREQ#` and `PERST#` are mandatory, and `WAKE#` is currently unsupported in software.
- Derived an independent one-lane topology and corridor: lane 0 first candidate, no lanes 1–15, no card-edge branch, Gen2 first bring-up, no retimer, adjacent CM5 provisionally preferred, six layers recommended for the power/return budget, and zero high-speed vias preferred.
- Recorded unresolved gates instead of guessing: V100 common-clock/SSC compatibility, V100-side impedance tolerance, CM5 `CLKREQ#` policy, V100 power sequencing/current capacity, and underside cooler/connector clearance.
- Added clean-room requirements, provenance, architecture, placement options, stackup study, machine-readable signal map, logical topology diagram, board constraints, and independent zone sketch under `design/`.

## 2026-08-20 — PCIe interface, mechanical envelope, and first PiSXMe schematic

- Created branch `codex/pcie-x1-interface-mechanical` from the independent x1 architecture commit. The prior reference branches and immutable upstream material were not modified.
- Resolved the first schematic policy from official CM5 documentation: direct CM5-generated 100 MHz REFCLK, Gen2 first bring-up, local always-requested CM5 `CLKREQ#`, direct CM5 `/PERST`, unused `WAKE#`/slot presence, and external 220 nF coupling only on the V100 transmitter direction.
- Preserved the official Raspberry Pi CM5 STEP package at `references/RaspberryPi-CM5-step/` with ZIP SHA-256 `2b4d26c6b30607c68099ad60df6fb8b8c8d04e9461f325c7c77dc421d2855005`.
- Added the phase-2 interface contract, clock/sideband analysis, AC-coupling analysis, mechanical envelopes, combined placement concept, board architecture, power architecture/tree, hostile review, ERC report, and conceptual mechanical SVG.
- Created a new blank-template-derived `pisxme/PiSXMe.kicad_sch` and matching project file. KiCad 10.0.5 parsed it and exported netlist/PDF; ERC is intentionally preserved as non-clean (19 violations: 8 errors, 11 warnings) because connector/control symbols and final hierarchy remain gated on V100/CM5 validation.
- Kept the principal blocker explicit: public NVIDIA material describes the SXM2 system interface as NVLink, so direct reverse-engineered PCIe operation, endpoint clock acceptance, and power sequencing require real-module bring-up before PCB release.

## 2026-08-20 — Cooler-agnostic PiSXMe component placement study

- Created branch `codex/cooler-agnostic-placement` for the cooler-independent Rev-A placement phase. External cooling remains interchangeable: the board contract reserves a 150 × 95 mm cooler-owned topside footprint plus a matching underside backplate/retention volume and does not choose a heatsink or waterblock.
- Selected real Rev-A component candidates: Amphenol `74221-101LF` SXM2 receptacle, two Amphenol `10164227-1004A1RLF` 4.0 mm CM5 connectors, dual Molex `39301062` Mini-Fit Jr. inputs, TI `TPSM63606RDLR` CM5 buck, TI `LM74700QDBVRQ1`/`CSD19536KCS` protection candidates, Littelfuse fuse positions, and JST cooling/debug headers. The exact CM5 1004 connector CAD download was blocked by the manufacturer CDN and was not replaced with the 1001 model.
- Generated a new 220 × 140 mm six-layer `pisxme/PiSXMe.kicad_pcb` with real land patterns, CM5 STEP body, mechanical zones, cooling contract drawings, and serviceable adjacent-CM5 placement. No production PCIe routing, power pours, final planes, Gerbers, or restricted reference geometry were used.
- Replaced the old schematic placeholder pass with an MPN-resolved architectural schematic and local symbol/footprint tables. KiCad 10.0.5 exported the schematic PDF/netlist and reported 0 ERC errors; 110 warnings remain explicitly classified as grid cleanup, intentional low-speed isolated labels, and library-link configuration.
- KiCad placement DRC reported 120 violations and 0 unconnected items; violations are recorded as pre-routing study properties, not suppressed as production sign-off. Top/bottom/front/isometric 3-D renders and an annotated placement SVG are preserved under `pisxme/renders/`.
- Final unresolved gates remain real V100 endpoint/clock/reset/power validation, full CM5/SXM2 pin audit, exact V100/cooler/backplate geometry, exact 1004 connector model alignment, fabricator-specific impedance stackup, and high-current copper/thermal design.

## 2026-08-20 — Final electrical and manufacturing signoff audit

- Created the 400-pad SXM2 audit CSV/MD from the published 40x10 map and preserved source disagreements rather than normalizing them.
- Corrected the earlier Molex power-input MPN from 39301062 (six circuits) to 39301082 (eight circuits), corrected the fuse-holder choice, replaced the invalid 220 pF coupling identifier with a 220 nF candidate, and selected 2.54 mm Molex fan headers.
- Corrected the TPSM63606 pin contract in the schematic generator and produced an independent unrouted placement-study PCB with no tracks, vias, or copper zones.
- Routing readiness remains NOT_READY_FOR_ROUTING pending hydrated KiCad ERC/DRC validation, pin-level power implementation, critical-footprint audit, and fab-returned impedance geometry.

## 2026-08-20 — Routing-readiness blocker closure

- Created branch `codex/routing-readiness-blocker-closure` from the prior electrical/manufacturing signoff. The source project remains production-unrouted: zero tracks, vias, and zones; no Gerbers or board order were produced.
- Diagnosed the KiCad 10.0.5 CLI behavior. The reliable procedure is a complete lock-free project copy run from its project directory; direct board DRC can still hang after stale-lock cleanup. The status is `CLI_WORKAROUND_VALIDATED`, with JSON and human-readable receipts preserved under `validation/`.
- Refreshed final receipts: ERC completed with 0 errors and 185 warnings; DRC completed with 211 errors, 20 warnings, and 0 unconnected items on the unrouted placement study. These are evidence receipts, not clean signoff.
- Captured the current JLCPCB `JLC06161H-7628` stack and 85 ohm calculator result: 5.2 mil width, 2.78466796875 mil pair gap, 84.9965876269 ohm returned. The individual API response does not encode order-specific tolerance; the official CM5 90 ohm guidance remains an explicit reconciliation gate.
- Corrected the SXM2 audit: the 400-pad map contains 130 nominal 12 V contacts, 170 ground contacts, 31 published NC contacts, and two unresolved auxiliary contacts K18/K19. K19 is not GND; no speculative K18/K19 circuit was added. Contact-current arithmetic is below the 0.45 A/contact Amphenol rating, but connector/PCB thermal signoff remains open.
- Preserved official manufacturer-resource URLs and recorded the released Amphenol MEG-Array contact-performance evidence. Exact 74221 land-pattern/mask/paste/orientation and several assembly-critical footprints remain unverified; no third-party CAD was promoted to authority.
- Reviewed V100 clock/reset/power evidence and working carrier active circuitry. The direct Gen2 x1 topology remains a rational Rev-A experiment, but exact V100 sequencing, SSC/common-clock acceptance, and K18/K19 behavior still require hardware validation. Final decision: `NOT_READY_FOR_ROUTING`.

## 2026-08-21 — Standard PCIe endpoint and manufacturer-land-pattern blocker closure

- Created branch `codex/standard-pcie-sxm2-signoff` without modifying immutable upstream references or routing the production PCB.
- Adopted the explicit Rev-A policy that V100 SXM2 is a standard PCIe endpoint behind a non-standard connector. Direct Gen2 x1 data, common-clock REFCLK, direct PERST#, local always-requested CM5 CLKREQ#, and one external 220 nF capacitor per V100 TX conductor remain the contract.
- Created an independent Amphenol-derived 74221-101LF footprint with exactly 400 circular pads, 10 x 40 at 1.27 mm pitch, 0.635 mm pads, 0.150 mm solder-mask margin, no vias in pads, and a 5.10 mm rework allowance. The active PCB still contains its older embedded study footprint; this distinction is preserved and the footprint signoff remains `NOT_VERIFIED`.
- Reviewed working/reference carriers for active logic. No universal PCIe bridge, retimer, redriver, CPLD, or protocol-conversion block was found to be required for a short single-GPU link; larger platform management/fanout logic is not treated as transport necessity.
- Rebased the board target to 90 ohm differential per CM5 documentation. The public JLC calculator failed to return a 90 ohm W1/S1 result, so the historical 85 ohm response was explicitly rejected as a routing substitute.
- Updated the Amphenol contact-current audit with the manufacturer's all-contact test context: 0.45 A/contact was characterized on specified solid 3 oz test boards at 25°C still air and ≤30°C rise. PiSXMe arithmetic remains 0.192–0.212 A per nominal V100 +12 V contact at 300–330 W, but PCB thermal equivalence is not claimed.
- Added standard-endpoint basis, active-logic review, community-contact record, manufacturer resource README, critical-footprint final audit, ERC/DRC receipts, JLC calculator attempt, hostile review, and the final routing-readiness gate. Current decision remains `NOT_READY_FOR_ROUTING` due the active footprint import/A1 verification, missing JLC 90 ohm result, ERC hygiene findings, and pre-routing courtyard/footprint closure.

## 2026-08-21 — Final routing-readiness closure

- Created branch `codex/close-routing-readiness` and kept the PiSXMe PCB production-unrouted: zero tracks, vias, and copper zones.
- Replaced the embedded J1 study footprint with the manufacturer-derived Amphenol `74221-101LF` model: 400 pads, 1.27 mm pitch, 0.635 mm copper land, 0.150 mm solder-mask margin per side, no pad vias, manufacturer A1 convention, and 5.10 mm rework allowance. UUID and active-footprint comparison artifacts are preserved.
- Corrected the active CM5 connector land pattern to the official Amphenol `10164227-1004A1RLF` two-row 0.4 mm geometry, corrected the Littelfuse fuse-holder hole pattern, and corrected the TI TPSM63606 RDL package model to include central PGND lands. All critical footprints are now manufacturer-verified or datasheet-derived-and-checked; none remains library-only or unresolved.
- Closed the JLC `JLC06161H-7628` 90 ohm geometry gate using the live public calculation API: L1 width 0.13208 mm / 5.2 mil, pair gap 0.085328 mm / 3.359375 mil, calculated 89.995806 ohm, with a 90.14944 ohm coated independent cross-check. The `PCIe_90R_L1_L2` KiCad pre-routing class is configured.
- Reran KiCad 10.0.5 from fresh lock-free project copies. ERC is 0 errors and 184 warnings with zero multiple-net-name findings; every remaining warning is documented as an intentional boundary label or reproducible CLI library-context limitation. DRC is 0 errors, 20 documented library-context warnings, 0 courtyard/clearance/silk/unconnected findings, and zero genuine pre-routing blockers.
- Final hostile review found no concrete evidence-backed routing blocker. Routing readiness is `READY_FOR_ROUTING`; V100 undocumented sequencing and first-hardware behavior remain explicit Rev-A risks, not claims of prior hardware validation.

## 2026-08-21 — Modular USB-C external I/O revision

- Created branch `codex/modular-usbc-io` for the intentionally production-unrouted I/O revision; the board remains at zero tracks, vias, and copper zones and no production Gerbers were generated.
- Confirmed from the official CM5 datasheet that USB3 ports 0 and 1 are independent 5Gbps interfaces and that USB2 is an independent interface separate from PCIe. Added USB-C FAST A for storage, FAST B for a commodity USB 2.5GbE adapter, and SERVICE for USB2 host/recovery use while retaining internal UART and nRPIBOOT access.
- Added the selected Type-C architecture: Amphenol `10137064-00011LF` FAST receptacles, Amphenol `10171746-00021LF` SERVICE receptacle, TI `HD3SS3212IRKSR` SuperSpeed orientation muxes, `TPS25821DSSR` 1.5A host VBUS/CC source controllers, `TUSB320LAIRWBR` SERVICE DRP controller, `TPS2553DBVR` 0.5A SERVICE limiter, TI USB ESD arrays, and dedicated `U16 TPSM63606RDLR` USB 5V rail.
- Corrected the FAST-port protection topology from duplicated SuperSpeed arrays to two official four-line `TPD4EUSB30` orientation-branch arrays plus one `TPD2EUSB30A` USB2 companion-pair array per FAST port; the CM5 D+/D− pins, receptacle contacts, and ESD pins now share the intended nets. Current lock-free KiCad 10.0.5 ERC reports 0 errors, 48 warnings (30 reproducible local-library context warnings and 18 intentional boundary labels), with zero multiple-net-name findings. Current lock-free DRC reports 36 local-library context warnings, zero geometry/courtyard/clearance/unconnected findings, and zero genuine pre-routing blockers.
- Updated the active-board signoff to `READY_FOR_ROUTING`; remaining gates are routing-time controlled impedance/plane implementation, manufacturer CAD overlays for the USB receptacles, SERVICE firmware/role validation, and first-hardware USB SI/EMI and driver testing.

## 2026-08-21 — Production-routing baseline

- Began branch `codex/modular-usbc-io` routing from commit `bcb184e17169e1c04dd6e230010ba5d330ab3321`; the original placement board remains preserved as the pre-routing checkpoint.
- Recorded the exact 220 × 140 mm board, six-layer declaration, KiCad 10.0.5 tool path, 36-footprint placement, and zero tracks/vias/zones in `routing/ROUTING_BASELINE.md`.
- Discovered that the placement-study generator intentionally stripped PCB pad nets and that the active board still carried generic stackup metadata rather than the captured JLC06161H-7628 dielectric/copper values. These are mandatory pre-routing materialization corrections before any production copper is added.

## 2026-08-21 — Materialize routing netlist

- Repaired the placement-study PCB structure after support footprints had been inserted inside the CM5 footprint block.
- Restored schematic connectivity onto the active board using explicit physical aliases for the SXM2, CM5, and USB-C connectors.
- Active PCB now contains 135 named nets and 741 assigned pads; no production copper has been added.
- Corrected active stackup metadata to the captured JLC06161H-7628 six-layer dielectric/copper values.
- Routing remains gated on KiCad validation and deliberate checkpointed copper work.

## 2026-08-21 — PCIe x1 routing checkpoint

- Routed the first production copper class: PER0, PET0 through the two external V100 TX coupling capacitors, and common-clock REFCLK. The active board now contains 60 route segments and 12 through-vias; all other production nets remain unrouted and no copper zones have been added.
- Used the final `PCIe_90R_L1_L2` geometry: 0.13208 mm track width, 0.085328 mm pair gap, and 0.20 mm unrelated-copper clearance on the JLC06161H-7628 six-layer basis.
- Measured pair skews are 0.0003 mm for PER0, 0.0214 mm for PET0 after coupling, 0.0035 mm for the raw capacitor legs, and 0.0430 mm for REFCLK. The CM5 connector fanout required controlled F.Cu/In3.Cu or F.Cu/B.Cu transitions, so the earlier zero-via preference is recorded as unattainable at this fixed placement rather than implied.
- Lock-free-copy KiCad 10.0.5 DRC reports no route crossings, shorts, clearance, width, drill, or via violations for the added PCIe copper. The receipt retains 499 expected unconnected items and 68 pre-existing library/silkscreen study findings; final return-plane continuity remains gated on the later ground/zones phase.

## 2026-08-21 — FAST-A USB routing checkpoint

- Routed the first independent CM5 USB 3 port through the HD3SS3212 mux to J9, including the USB 2 companion pair and both duplicated reversible USB-C USB 2 contact rows. FAST-B, SERVICE, power, zones, and final ground implementation remain unrouted.
- Reworked pair geometry after the first connected-only pass exposed material intra-pair mismatch. The final measured FAST-A/CM5 USB3 skews are 0.000–0.300 mm and the USB 2 DP/DM mismatch is 0.006 mm; no production route is accepted solely because it is connected.
- The FAST-A route contains 181 segments and 40 vias. Lock-free-copy KiCad 10.0.5 DRC reports 68 inherited findings (54 library-footprint and 14 silkscreen-over-copper) plus 499 expected unconnected items, with zero new shorts, crossings, clearance, width, hole, via, or other routing violations.
- Preserved the ordered route pipeline in `tools/route_usb_fast_a_final.py` and the measured receipt in `routing/USB3_FAST_A_RECEIPT.md`; the active board remains a checkpointed intermediate, not a released manufacturing package.

## 2026-08-21 — FAST-B USB routing checkpoint

- Routed the second independent CM5 USB 3 port through the HD3SS3212 mux to J10, including its USB 2 companion, moved FAST-B ESD device U18, and both duplicated reversible USB-C USB 2 contact rows. PCIe and FAST-A are retained; power, SERVICE, control, ground, and zones remain unrouted.
- Moved U18 from the crowded U11 area to PCB coordinate (204,127) without changing its logical pad assignments. The final USB2 fanout uses separate pad escapes and inner-layer transitions and is DRC-clean.
- Measured FAST-B route lengths from the active board: CM5 RX 69.4900/69.9900 mm (0.5000 mm skew), CM5 TX 69.0100/69.9100 mm (0.9000 mm), U9-to-J10 RX1 59.9142/69.5000 mm (9.5858 mm), TX1 40.2910/45.5000 mm (5.2090 mm), RX2 67.2361/74.5000 mm (7.2639 mm), TX2 23.7500/33.2500 mm (9.5000 mm), and USB2 DP/DM 115.4844/123.2770 mm (7.7925 mm). The dense U9/U10/U11/J10 placement mismatch is explicitly carried forward to the combined high-speed review; no same-layer meander was accepted after it created real crossings.
- The FAST-B route set contains 153 segments and 46 vias. Lock-free-copy KiCad 10.0.5 DRC reports 69 inherited findings (54 library-footprint and 15 silkscreen-over-copper) plus 499 expected unconnected items, with zero new shorts, crossings, clearances, width, hole, via, or other route violations.
- Preserved the ordered replay pipeline in `tools/route_usb_fast_b_final.py`, the auditable individual scripts under `tools/test_usb_b_*.py`, the validation receipt at `validation/usb-fast-b-drc.json`, the top SVG/3D render under `validation/render-usb-fast-b/`, and the measured receipt at `routing/USB3_FAST_B_RECEIPT.md`. This remains an intermediate routing checkpoint and is not a released manufacturing package.
# 2026-08-22 — CLKREQ# and CM5 VBUS-enable routing checkpoint

- Added the `/CM5_CLKREQ_N` route from CM5 J2 pad 102 to the local R1 strap,
  using a short F.Cu escape, In2.Cu trunk, and F.Cu return with two vias.
- Added the `/CM5_VBUS_EN` fanout from CM5 J2 pad 111 to the FAST-A/FAST-B
  TPS25821 enable pads, using an In4.Cu trunk and pad-aware F.Cu branches.
- The final trial was retained only after lock-free KiCad DRC produced no new
  electrical, clearance, crossing, hole, solder-mask, dangling, or sliver
  violations beyond the inherited library/silkscreen findings.
- This checkpoint intentionally adds no copper zones and does not close the
  remaining low-speed, ground, thermal, or final-validation work.
# 2026-08-22 — PCIe/V100 power-enable routing checkpoint

- Added the distributed `/PCIE_PWR_EN` route from CM5 J2 pad 106 to both
  TPSM63606 enable inputs and both LM74700 protection-controller enables.
- The fanout uses a right-edge In3.Cu trunk, an In1.Cu distribution branch,
  and short F.Cu pad-aware stubs. The route was deliberately reworked around
  PCIe clock vias, USB SuperSpeed escape vias, high-current copper, and the
  regulator switching/power pads.
- The accepted geometry has 18 segments and 6 vias and is clean in the
  lock-free KiCad DRC copy workflow apart from the inherited library and
  silkscreen findings.
- This checkpoint does not add zones and does not close PERST#, USB-C control,
  fan/pump, ground, thermal, or final-validation work.
# 2026-08-22 — PERST# routing checkpoint

- Added `/PERST_N` from CM5 J2 pad 109 to SXM2 J1 E18.
- The accepted route is 144.4588 mm across 14 segments and 2 vias, with an
  In4.Cu trunk and F.Cu escapes. The SXM2 side follows row-gap escape paths
  above the connector-side REFCLK fanout and places the layer transition
  outside the BGA footprint.
- Lock-free KiCad DRC reports no new electrical, clearance, crossing, hole,
  solder-mask, dangling, or sliver findings beyond inherited
  library/silkscreen findings.
- This checkpoint does not add zones and does not close USB-C control,
  fan/pump, ground, thermal, or final-validation work.

# 2026-08-22 — USB3 pass-2 placement/fanout gate

- Began `codex/usb3-pass2` from the frozen PCIe pass-2 checkpoint and preserved
  `routing/usb3-pass2/PiSXMe-before-usb3-pass2.kicad_pcb`; the active board
  remains unchanged with zero USB3 segments/vias.
- Verified the FAST-A/FAST-B CM5-to-mux, HD3SS3212, TPD4EUSB30, and Type-C A/B
  net map from the schematic. Isolated CM5 escapes and isolated mux-to-ESD
  differential pairs pass KiCad 10.0.5 electrical DRC in disposable copies.
- The complete FAST-A fanout does not pass when those individually valid routes
  are combined: KiCad reports real pair crossings/shorts/clearance errors, and
  a layer-aware trial exhausts the F.Cu/B.Cu channel for the remaining pair.
  This is a concrete local USB placement/channel blocker, not a PCIe conflict;
  no PCIe copper was modified and FAST-B was intentionally gated.
- No production USB3 route is claimed. The phase stops at a documented
  placement/layer decision rather than accepting a via-heavy or unreferenced
  route that would violate the established 90-ohm L1/L2 design basis.

# 2026-08-22 — FAST-A CC1 routing checkpoint

- Added `/USB_FAST_A_CC1` from J9 A5 to U4 TPS25821 pad 9 using a DRC-guided
  low-speed path with F.Cu escapes, an In2.Cu trunk, and two through-vias.
- The accepted path is approximately 66.8 mm of copper and remains electrically
  separate from the existing PCIe and USB SuperSpeed routes.
- Lock-free KiCad 10.0.5 DRC reports only the inherited 54 library-footprint
  and 13 silkscreen findings, with no new shorts, crossings, clearance, hole,
  mask, dangling, or sliver violations.
- This checkpoint adds no zones and does not close the remaining FAST-A/FAST-B
  control nets, power housekeeping, ground, thermal, or final-validation work.

# 2026-08-22 — FAST-A POL routing checkpoint

- Added `/USB_FAST_A_POL` from U4 TPS25821 pad 7 to U5 HD3SS3212 pad 9 using
  F.Cu endpoint escapes, an In4.Cu detour, and two through-vias. The path is
  approximately 55.05 mm and is isolated from the existing high-speed routes.
- Lock-free KiCad 10.0.5 DRC reports only the inherited 54 library-footprint
  and 13 silkscreen findings, with no new electrical or geometric violations.
- REF, CC2, VBUS, remaining control, ground, thermal, and zone work remains
  intentionally open for later checkpoints.

# 2026-08-22 — FAST-A REF routing checkpoint

- Added `/USB_FAST_A_REF` from U4 TPS25821 pad 8 to R5 pad 1 with a short
  8.81 mm F.Cu route that stays above the CC1/POL local entries.
- The combined FAST-A POL/REF checkpoint remains DRC-clean apart from the
  inherited 54 library-footprint and 13 silkscreen findings. No new shorts,
  crossings, clearances, or fabrication-rule findings were introduced.
- FAST-A CC2/VBUS, remaining control, ground, thermal, and zone work remains
  intentionally open.

# 2026-08-22 — FAST-A CC2 routing checkpoint

- Added `/USB_FAST_A_CC2` from J9 B5 to U4 TPS25821 pad 11. Because the local
  connector-to-controller area is occupied by accepted USB2/SuperSpeed
  escapes, the low-speed control net uses a three-via F.Cu/In1.Cu/In2.Cu
  detour around the board-edge routing region.
- The accepted path is approximately 109.96 mm with no branches or test-point
  stubs. It does not alter PCIe or USB3 geometry and remains outside the PCIe
  corridor.
- Lock-free KiCad 10.0.5 DRC reports 67 total findings: only the inherited 54
  library-footprint and 13 silkscreen findings remain. No new clearance,
  short, crossing, dangling-via, or solder-mask violations were introduced.
- FAST-A VBUS, FAST-B controls, SERVICE controls, ground, thermal, zones, and
  final routed validation remain intentionally open.

# 2026-08-22 — FAST-A VBUS routing checkpoint

- Added `/USB_FAST_A_VBUS` using a local F.Cu connector-side zone, a 2.50 mm
  U4 pad-12 escape, and an explicit 0.30 mm In1.Cu trunk with two ordinary
  through-vias. The accepted trunk is approximately 83.545 mm and uses no
  blind/buried vias.
- The final route is detoured around fixed FAST-B vias and the FAST-A CC2
  corridor. It does not alter PCIe or USB SuperSpeed geometry.
- Lock-free KiCad 10.0.5 DRC with zone refill/save reports 67 total findings,
  351 remaining unrouted items, and zero FAST-A VBUS-specific unconnected
  items. No new electrical or geometric violations were introduced; the only
  findings are the inherited 54 library-footprint and 13 silkscreen issues.
- FAST-B controls, SERVICE controls, ground, thermal, remaining power zones,
  and final routed validation remain intentionally open.

# 2026-08-22 — FAST-B REF routing checkpoint

- Added `/USB_FAST_B_REF` from U8 TPS25821 pad 8 to R6 pad 1. The accepted
  path is approximately 15.390 mm across four segments, with a short F.Cu
  escape, an In2.Cu detour through the local controller/capacitor congestion,
  and two ordinary through-vias.
- The route avoids the adjacent U8 CC1/CC2 pads, the CM5 5 V output capacitor,
  and the existing USB SuperSpeed vias without touching the PCIe corridor.
- Lock-free KiCad 10.0.5 DRC reports 67 total findings and 350 remaining
  unconnected items. No FAST-B REF-specific unconnected, short, clearance,
  crossing, mask, or via findings were introduced; only the inherited 54
  library-footprint and 13 silkscreen findings remain.
- FAST-B CC1/CC2/POL/VBUS, SERVICE controls, ground, thermal, remaining power
  zones, and final routed validation remain intentionally open.

# 2026-08-22 — FAST-B POL routing checkpoint

- Added `/USB_FAST_B_POL` from U8 TPS25821 pad 7 to U9 HD3SS3212 pad 9. The
  accepted path is approximately 36.803 mm across five segments, with an
  In2.Cu detour below the local controller/capacitor and USB SuperSpeed
  congestion and two 0.40/0.30 mm ordinary through-vias.
- The path avoids the U8 adjacent pads, the CM5 USB3 RX-N escape, the local
  USB 5 V copper, and the existing SuperSpeed via field without touching the
  PCIe corridor.
- Lock-free KiCad 10.0.5 DRC reports 67 total findings and 349 remaining
  unconnected items. No FAST-B POL-specific unconnected, short, clearance,
  crossing, mask, drill, or via findings were introduced; only the inherited
  54 library-footprint and 13 silkscreen findings remain.
- FAST-B CC1/CC2/VBUS, SERVICE controls, ground, thermal, remaining power
  zones, and final routed validation remain intentionally open.

# 2026-08-22 — FAST-B CC1 routing checkpoint

- Added `/USB_FAST_B_CC1` from J10 A5 to U8 TPS25821 pad 9. The accepted path
  is approximately 63.293 mm across nine segments, with F.Cu endpoint
  escapes, an In3.Cu/B.Cu detour around the J10 shield and existing USB
  routes, and three ordinary through-vias.
- The J10-side route stays below the connector contact row and outside the
  shield pad. No PCIe or USB SuperSpeed geometry was changed.
- Lock-free KiCad 10.0.5 DRC reports 67 total findings and 348 remaining
  unconnected items. No FAST-B CC1-specific unconnected, short, clearance,
  crossing, mask, drill, or via findings were introduced; only the inherited
  54 library-footprint and 13 silkscreen findings remain.
- FAST-B CC2/VBUS, SERVICE controls, ground, thermal, remaining power zones,
  and final routed validation remain intentionally open.

# 2026-08-22 — FAST-B CC2 routing checkpoint

- Added `/USB_FAST_B_CC2` from J10 B5 to U8 TPS25821 pad 11. The accepted
  path is approximately 58.107 mm across seven segments, with a narrow F.Cu
  U8 escape, an In4.Cu central route, and two 0.40/0.30 mm ordinary
  through-vias. The source-side via was moved below the C5 ground-pad edge to
  preserve manufacturable clearance.
- The J10-side route stays below the connector contact row and avoids the
  existing FAST-B USB3 DM/RX geometry. PCIe and accepted high-speed routes are
unchanged.
2026-09-07: V289 combined five-net SPI audit passed all native U1/U2 endpoint
mappings and its trace-removal negative control. DRC remained 420 findings /
22 inherited opens with no shorting, crossing, or footprint-error class.
This closes the disposable SPI routing subtask only; RTL9210B support and
Path-B validation remain open. Path A and production CAD remain unchanged.
2026-09-07: Rejected RTL9210B V250 parallel lower-edge QFN source-field
departures. Native rail/REFCLK connectivity and the trace-removal negative
control passed, but DRC found three signal shorts and one crossing against
inherited USB/3V3/GND fields. V242 remains the promoted disposable rail
basis; Path A and production CAD remain unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: tested corrected U2 far placement with
an order-preserving two-layer SPI partition. Native KiCad reports 30
violations / 40 opens; dominant failures remain the rotated U1 QFN source
escape and retained XTAL_OUT region. U2 footprint coordinates are corrected;
Path A and production CAD remain unchanged.
2026-09-08: RTL9210B V530 is rejected because its coherent C3 relocation
still crosses the retained XTAL_IN B.Cu return. V532 is retained: U1.20,
U1.34, and U1.39 all reach C3.1 in the native graph, exact branch-removal
negative controls pass, and native DRC has no new short, crossing, or
clearance error. Inherited incomplete-fixture findings remain; Path A and
production CAD are unchanged.
2026-09-08: Rejected RTL9210B V467/V468 isolated TX-pair endpoint trials.
V467 crossed TX source jogs; V468 removed those crossings but collided with
the existing PERST corridor and connector-side clearances. TX remains open
for coallocation with PERST/CLKREQ; no Path-A or production-CAD change.
2026-09-08: Rejected RTL9210B V469/V470 TX coallocation trials. V469 had TX
source-jog and PERST/CLKREQ conflicts. V470 fixed the source jogs but exposed
RX-launch, CLKREQ/PEDET, and connector-clearance conflicts. Next work uses a
dedicated TX side corridor; Path A and production CAD remain unchanged.
2026-09-08: Rejected RTL9210B REFCLK isolation V432 as a malformed first
launch. Native DRC caught overlapping transition-via bodies and connector
dogbones entering adjacent J1 MDI pads. Preserve REFCLK net authority; the
next trial must use staggered vias and explicit J1.53/J1.55 launch corridors.
2026-09-07: V389 refilled native zones on the V388 candidate, reducing the
stale zone-clearance flood to 17 DRC violations plus 25 opens. V390 widened
all four imported lane nets to the board minimum 0.20 mm; native DRC retained
zero shorts and zero crossings, with 25 opens and localized clearance,
hole-clearance, dangling-power, and isolated-copper findings. Path B remains
open and Path A/production CAD remain unchanged.
2026-09-07: V388 restored XTAL_OUT on a separate U1 escape/B.Cu channel while
retaining the exact V328 lane and V387 RSET/RTL_3V3 allocation. Native support
audit and four trace-removal negative controls pass; native DRC reports zero
shorts and zero crossings with 25 opens. Remaining clearance/width and
support-net findings keep Path B open; Path A and production CAD remain
unchanged.
2026-09-07: Recorded RTL9210B PEDET trials V290–V293. V292 removed the
REFCLK crossing but retained PERST; V293 avoided PERST but introduced JTAG /
undefined-field shorting and was rejected. PEDET remains open; Path A and
production CAD remain unchanged.
2026-09-08: Rejected RTL9210B CLKREQ escape trials V419-V427 after native DRC
identified actual source-field shorts, track crossings, or clearances. V424
entered U1 no-connect pad 4; V425/V426 crossed PERST; V427 crossed PEDET and
PERST. V418 remains the clean PEDET/control basis; Path A and production CAD
remain unchanged.
2026-09-08: RTL9210B V431 closed the CLKREQ source-escape repair on the V418
basis. Native DRC reported zero shorts/crossings and only the inherited
dangling-power and isolated-fill warnings; the native audit and seven
trace-removal negative controls passed. REFCLK, SPI, remaining rails/ground,
and full Path-B closure remain open.
2026-09-08: RTL9210B V428 90-degree U1 control trial was rejected as an
incomplete disposable regeneration: native DRC found 46 violations because
legacy lane/crystal copper remained while provisional controls were added.
It is route-implementation evidence only, not a macro-placement verdict.
2026-09-07: Rejected RTL9210B V399 local-clearance trial. Reauthoring RSET,
RTL_3V3, and XTAL_OUT from the V397 basis introduced two GND shorts at the
oscillator transition. V397 remains the current basis; Path A and production
CAD remain unchanged.
2026-09-08: A native 0-degree RTL9210B U1 orientation probe was created around
the exposed-pad center. With disposable local support copper removed, native
DRC reports six inherited warnings and no signal violations; transformed pad
coordinates are recorded for the next complete lower-QFN regeneration. This
is a retained placement basis, not Path-B closure. Path A and production CAD
remain unchanged.
2026-09-08: RTL9210B V418 regenerated PEDET from current U1.8/R2.1/J1.69
coordinates on a distinct source/return channel. Native DRC reports zero
shorts/crossings and 20 opens; seven connectivity negative controls pass.
RTL_1V1, SPI, REFCLK, and associated support remain open; Path A and
production CAD remain unchanged.
2026-09-08: Rejected direct V311 PERST transplant as coordinate-stale. Native
V412 regenerated PERST_N from current pads with zero shorts/crossings and 24
opens. V416 regenerated CLKREQ_N on a distinct trunk with zero
shorts/crossings and 22 opens; six native connectivity trace-removal negative
controls pass. Remaining PEDET/RTL_1V1/SPI/REFCLK/support nets remain open;
Path A and production CAD remain unchanged.
2026-09-07: RTL9210B V400-V404 repaired local support allocation. V401 removed
the RXP/QFN pad clearance issue; V402 removed the RSET/In2 clearance issue;
V403 restored XTAL_OUT with standard vias; V404 connected the actual C1.1
endpoint. Native audit plus four negative controls pass; V404 DRC has zero
shorts/crossings and 25 opens, with only inherited dangling/isolated-copper
warnings. Path B remains open; Path A and production CAD remain unchanged.
2026-09-07: Retained RTL9210B V311 CLKREQ basis after rejecting V309/V310.
Native R3.1/U1.13/J1.52 connectivity passed; DRC reported 514 findings / 18
inherited opens with no shorting, crossing, or footprint-error class. Reset,
remaining rails, and high-speed support remain open; Path A and production
CAD remain unchanged.
2026-09-07: Recorded RTL9210B CLKREQ V306–V308 trials. V306/V307 removed
source-field shorts but retained crystal geometry defects; V308 introduced
real XTAL_IN/XTAL_OUT shorts at the shifted transition and was rejected.
CLKREQ remains open; production and Path-A CAD remain unchanged.
2026-09-07: Recorded RTL9210B CLKREQ V304/V305 route trials. V304 removed
PEDET/R2 shorts but crossed retained SPI/XTAL geometry; V305 still crossed
SPISI and XTAL_IN after a layer split. CLKREQ remains open; Path A and
production CAD remain unchanged.
2026-09-07: Rejected RTL9210B V303 lower CLKREQ corridor. Native DRC found
CLKREQ/PEDET and CLKREQ/RTL_3V3 shorts at the R3/U1 source field despite the
lower destination corridor. The next repair must co-author source escapes;
Path A and production CAD remain unchanged.
2026-09-07: Rejected RTL9210B V302 CLKREQ alternate launch. Native DRC found
real CLKREQ/PEDET shorting at R2 and CLKREQ/ISOLATEB shorting at U1. The
native open count was 18, but the source geometry is invalid; Path A and
production CAD remain unchanged.
2026-09-07: Retained RTL9210B V301 CLKREQ topology basis. Native endpoint
connectivity reduced the saved-board open count to 18, but DRC found
CLKREQ/SPISO and CLKREQ/XTAL_IN crossings and a CLKREQ/REFCLK_N short at the
U1 transition. Path A and production CAD remain unchanged.
2026-09-07: Retained RTL9210B V300 PEDET sideband basis after V299 exposed a
floating J1 branch. Native R2.1/U1.8/J1.69 connectivity passed; DRC reported
454 findings / 20 inherited opens with no shorting, crossing, or footprint
errors. PEDET closes in the disposable basis; remaining support is open.
2026-09-07: Recorded RTL9210B PEDET/PERST local-field experiments V295–V298.
V295 crossed REFCLK after a B.Cu transition; V296–V298 retained one native
PEDET/PERST crossing despite local dogleg moves. The next repair is a
co-authored sideband field; production and Path-A CAD remain unchanged.
2026-09-07: Retained RTL9210B V294 PEDET east-side landing basis. It removes
the earlier REFCLK issue but native DRC retains one PEDET/PERST crossing at
U1.8. PEDET remains open and requires coordinated sideband-field repair; Path
A and production CAD remain unchanged.
2026-09-07: Retained RTL9210B V288 SPICLK short-escape basis. Native U1.19/U2.6
connectivity passed; DRC reported 402 findings / 23 inherited opens with no
shorting or crossing class and zero footprint errors. Remaining support routes
are open; Path A and production CAD remain unchanged.
2026-09-07: Rejected RTL9210B V287 isolated SPICLK route. Native DRC found
the U1 north escape crossing the retained RTL_3V3 handoff. The destination
corridor remains plausible; remaining SPI source escapes require coordinated
allocation. Path A and production CAD remain unchanged.
2026-09-07: Rejected RTL9210B V244 U1.50 lower-edge RTL_1V1 escape after
native connectivity and negative control passed but DRC found three rail
track crossings. V242 remains the promoted disposable rail basis; Path A and
production CAD remain unchanged.
2026-09-07: Retained RTL9210B V289 SPISI high-north basis. Native U1.18/U2.5
connectivity passed; DRC reported 420 findings / 22 inherited opens with no
shorting or crossing class and zero footprint errors. Remaining Path-B
support and high-speed routes remain open; Path A and production CAD remain
unchanged.
2026-09-07: Retained RTL9210B V286 SPISO3 offset-trunk basis after rejecting
V285. Native U1.22/U2.7 connectivity and trace-removal negative control
passed; DRC reported 383 findings / 24 inherited opens with no shorting or
crossing class and zero footprint errors. Remaining support routes are open;
Path A and production CAD remain unchanged.
2026-09-07: Rejected RTL9210B V245 translated U1.60/U1.63 lower-edge route.
Native connectivity and the trace-removal negative control passed, but DRC
found five crossings against RTL_5V, PEDET, RTL_3V3, REFCLK_P, and PERST_N.
V242 remains the promoted disposable rail basis; Path A and production CAD
remain unchanged.
2026-09-07: RTL9210B V391-V398 oscillator-channel experiments preserved the
exact lane and support topology. V393's smaller vias were rejected by native
fabrication minima; V394/V395 outboard XTAL_OUT routes regressed. V397 is the
best current oscillator basis with 6 non-open native findings and 26 opens;
V398 regressed one clearance. Path B remains open; Path A and production CAD
remain unchanged.
2026-09-07: Rejected RTL9210B V251-V253 QFN source-field co-allocation
trials. Native rail/REFCLK/RTL3V3 connectivity and negative controls passed,
but the successive U1.52 handoffs retained XTAL_IN, source-field crossing,
and RTL_3V3/GND defects. V242 remains promoted; Path A and production CAD
remain unchanged.
2026-09-07: Rejected RTL9210B V246 lower-edge U1.60/U1.63 allocation pending
one PERST-column overpass. Native connectivity and negative control passed;
DRC reduced the new route defect to one RTL_1V1/PERST_N crossing, with one
retained ISOLATEB/CLKREQ_N shorting class. V242 and production CAD remain
unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: validated a corrected U2 footprint in a
left/90-degree placement-only candidate at 6 findings / 44 opens with no new
signal short, then rejected its mixed-layer SPI route at 24 violations / 39
opens for pad-field clearances and SPI shorts/crossings. Corrected footprint
geometry is now the basis for future trials; production CAD and Path A remain
unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: tested RTL_5V pad-17 escape V1. Native
connectivity gained one rail endpoint and reduced opens 30 to 29, but native
DRC reported 8 violations from SPI/control-field crossings and shorts.
Rejected as a route implementation; production CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: tested RTL_5V pad-17 escape V2/V3.
V2 shorted the nearby RTL_1V1 via. V3 moved the ordinary transition to
(83.6,67.0), connected U1 pad 17 natively, and reduced the fixture to the
V2 baseline's four inherited DRC violations / 29 opens. V3 is the preferred
disposable rail baseline; production CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: preserved PEDET/CLKREQ control-route
 variants V2 and V3. V2 reduced the local class to 3 crossings / 33 opens;
 V3 regressed to 5 crossings / 33 opens after moving the inherited RTL_1V1
 corridor. Rejected both as route implementations and retained the clean
 RESET_N/PERST_N baseline.
- Lock-free KiCad 10.0.5 DRC reports 67 total findings and 347 remaining
  unconnected items. No FAST-B CC2-specific unconnected, short, clearance,
  crossing, mask, drill, or via findings were introduced; only the inherited
  54 library-footprint and 13 silkscreen findings remain.
- FAST-B VBUS, SERVICE controls, ground, thermal, remaining power zones, and
  final routed validation remain intentionally open.

# 2026-08-22 — FAST-B VBUS routing checkpoint

- Added `/USB_FAST_B_VBUS` from U8 TPS25821 pad 12 into the J10 VBUS field.
  The accepted path is approximately 54.553 mm across seven segments, with a
  short F.Cu source escape, two ordinary 0.60/0.30 mm through-vias, a B.Cu
  lower-perimeter current corridor, and a local F.Cu connector-side VBUS zone.
- The path was iterated against the existing USB 5 V feed, FAST-B CC1/CC2
  transitions, and the J10/U18 pad field. The final DRC-verified path has no
  VBUS-specific short, crossing, clearance, mask, edge, or via findings.
- Lock-free KiCad 10.0.5 DRC reports 67 total findings and 343 remaining
  unconnected items. The inherited findings are 54 library-footprint and 13
  silkscreen warnings; no new electrical/geometry findings were introduced.
- FAST-B high-speed and control routing is now complete. SERVICE controls,
  ground, thermal, remaining power zones, and final routed validation remain
  intentionally open.

# 2026-08-22 — combined high-speed review checkpoint

- Reviewed the complete routed PCIe, FAST-A, and FAST-B high-speed set before
  power routing. Current KiCad DRC reports 67 non-unconnected findings, 343
  expected unconnected items, zero shorts, zero crossings, and zero
  high-speed clearance/width violations; the remaining findings are the
  inherited 54 library-footprint and 13 silkscreen findings.
- PCIe matching remains tight: PER0 0.0003 mm, PET0 0.0214 mm, and REFCLK
  0.0430 mm pair mismatch. FAST-B remains the high-speed risk, with measured
  U9-to-J10 mismatch of 5.2090 mm TX1 and 9.5858 mm RX1 under the fixed
  placement. This is documented for final signal-integrity review rather than
  hidden.
- The PCIe corridor remains free of the new FAST-B VBUS path. Final L2 GND
  continuity, return stitching, and power-plane interaction remain mandatory
  checks before release.

# 2026-08-22 — FAST-B TX2 connector continuation checkpoint

- Closed the previously missing U11-to-J10 `/USB_FAST_B_TX2_P` and
  `/USB_FAST_B_TX2_N` legs. The measured total lengths are 46.1589 mm and
  51.5355 mm respectively, with 5.3766 mm mismatch and four ordinary
  through-vias per conductor.
- The final connector approach was iterated around the J10 VBUS/CC2 field and
  U18 pad field. Lock-free KiCad 10.0.5 DRC reports 67 inherited findings,
  341 remaining unconnected items, and zero new electrical or geometric
  findings. This closes the FAST-B SuperSpeed copper class.
- The larger FAST-B skew remains an explicit post-route signal-integrity risk;
  ground-plane and power-zone implementation must not cut through these
corridors.
2026-09-08: Rejected RTL9210B REFCLK V433/V434 after native DRC found
source-transition interaction and connector-launch conflicts. The trials
preserved the correct REFCLK authority and demonstrated the upper/lower J1
launch ordering; REFCLK must now be co-allocated with lane source escapes.

# 2026-08-22 — routed DRC and release-gate checkpoint

- Completed the first routed-board DRC cleanup without changing signal
  geometry: explicit solid GND zone connections remove the starved-thermal
  errors, and only the affected tiny-footprint reference fields are hidden to
  remove silkscreen-over-pad errors.
- Final routed DRC receipt: 0 error-severity findings, 54 understood
  local-library warnings, and 31 intentional NC/zone/ground connectivity
  records.
- Preserved a 54-footprint CPL/inventory and added post-route PCIe/USB and
  power audits. The board is not ready for a Rev-A fab package because actual
  USB3 inner-layer impedance/skew remains unqualified, despite PCIe/power
  routing being reviewable.

# 2026-08-22 — routed parity and render checkpoint

- Reran final routed DRC on the exact post-label-cleanup board: 0 error-severity findings, 54 local-library warnings, and 31 intentional connectivity records.
- Ran schematic-parity validation and preserved 321 warnings: 199 J1 full-connector abstraction records, 68 custom-footprint mismatches, 50 board metadata mismatches, and four board-only protection/test/mechanical footprints. No represented ordinary PCIe/USB/power/control net rename was found.
- Generated top, bottom, front, and isometric KiCad 3D renders and a 54-footprint CPL/inventory. Production release remains NOT_READY_FOR_REV_A_FAB_PACKAGE because USB3 layer/skew qualification and full J1 parity are not closed.

# 2026-08-22 — production-readiness gate clarification

- Added the schematic-parity result to the production gate matrix. The routed study remains NOT_READY_FOR_REV_A_FAB_PACKAGE for two concrete electrical/documentation reasons: USB3 actual-layer/skew qualification and the intentionally abstracted full 400-pad J1 not being machine-parity-clean.

# 2026-08-22 — materialize final routed PCB cleanup

- Verified the recovered working board against the committed blob and found that the DRC-cleanup board edits were not yet materialized in the prior audit commit. Committed the exact final board next so its solid GND connections, silkscreen cleanup, and routed-study labels match the preserved DRC/3D/parity receipts.

# 2026-08-22 — preserve high-speed rework baseline

- Opened `codex/high-speed-rework` from the materialized routed-board commit and preserved the complete first-pass PCB as `validation/PiSXMe-high-speed-rework-baseline.kicad_pcb` before any placement or copper rework. The baseline records the measured PCIe and USB3 routes so later improvements remain auditable.

# 2026-08-22 — high-speed rework root causes and placement decision

- Classified the PCIe 100+ mm span as primarily fixed J2/cooler-mechanical geometry plus avoidable routing detours, and classified FAST-B's 14.8766 mm mismatch as a real asymmetric connector-side topology. Disposable placement studies rejected a 5 mm inward J2 shift and a 270-degree rotation because they consume the cooler/power/service envelope. Candidate A, fixed J2 with a fresh local re-route, remains the selected surgical path; no production copper was changed in this checkpoint.

# 2026-08-22 — routed rework validation and connectivity closure

- Preserved the original routed baseline at object hash `477b50deb84c515c3be1d70322e378c970967031`; the active rework PCB now hashes `a0719fe4e924a18c174e8b4e1d17e804be33b0d6` after only the explicit no-connect net cleanup. Disposable shorter PCIe and length-matched FAST-B trials introduced real crossings/shorts and were rejected. No unsafe trial copper was copied into the active board; PCIe remains 107--122 mm with two transitions per conductor and FAST-B remains at 14.8766 mm maximum pair mismatch.
- Corrected the schematic no-connect at the actual CM5 J2 pin-104 (`PCIE_nWAKE`) endpoint and reran lock-free KiCad 10.0.5 ERC: 0 errors, 46 explained warnings (30 project-local footprint-link context warnings and 16 intentional isolated labels). Removed the shared `/NC` PCB net from ten explicitly unconnected pads, reducing routed DRC connectivity records from 31 to 22 without changing signal or power geometry.
- Reran routed DRC and schematic parity on disposable full-project copies: 0 geometric DRC errors, 54 local-library warnings, 22 remaining shield/ground-zone/VBUS connectivity records, and 321 parity warnings with no represented ordinary PCIe/USB/power/control net mismatch. A disposable shield/GND stitching trial created 42 real DRC errors and was discarded. Thermal/current review remains `PASS_WITH_DOCUMENTED_MARGIN/RISK` for monitored Rev-A bring-up only. Production readiness remains `NOT_READY_FOR_REV_A_FAB_PACKAGE`; no Gerbers were released or ordered.
- Generated fresh top, bottom, front, and isometric KiCad 10.0.5 renders from the corrected active PCB. Net-only cleanup did not change the cooler-agnostic mechanical placement: CM5, SXM2 field, USB-C edge group, power/fan access, and published cooling/backplate envelope remain visually unchanged.

# 2026-08-22 — high-speed placement redesign baseline

- Created branch `codex/high-speed-placement-redesign` from `a17cf51cb55d57190001196fbb88fd7bbb931d37` and preserved the complete first-pass routed board as `placement/PiSXMe-routed-reference.kicad_pcb`. This phase is placement-only: the SXM2/cooler/power anchors remain fixed while CM5 and USB high-speed endpoints are explored in disposable copies before any production rerouting.

# 2026-08-22 — CM5 placement candidates and lightweight route trials

- Built a disposable placement-study board and exact endpoint map, explored six CM5 orientations/translations including expanded-outline alternatives, and trialed the top three geometries. Candidate C, J2 at `(197.5,70,180°)`, produced the best compact PCIe result: approximately 63–68 mm, zero high-speed vias, and an ACCEPTABLE direct L1/L2 corridor. USB mux/ESD pin-order crossings remain intentionally deferred to the next routing phase; no production copper was created.

# 2026-08-22 — materialize corrected high-speed placement winner

- Rejected the first Candidate C USB support placement after placement DRC exposed overlaps with the rotated J2 body. Repositioned muxes, ESD, USB buck, and USB2 support into legal upper/lower-right corridors, verified the CM5 STEP envelope, and materialized only placement plus affected-net rip-up on `pisxme/PiSXMe.kicad_pcb`. The corrected placement DRC has 57 findings/499 expected unconnected records, zero new courtyard overlaps, zero pad shorts, and zero new hole-clearance blockers. Production routing remains intentionally absent.

# 2026-08-22 — placement receipt wording correction

- Clarified that the three non-library placement-study records in the final receipt are silk records, not track violations. No board geometry or placement was changed.

# 2026-08-22 — PCIe pass-2 production route checkpoint

- Preserved Candidate C placement and routed only the PCIe x1 interface plus
  the two V100 TX AC-coupling legs. PER0 is 74.3581/74.3895 mm with 0.0314 mm
  skew and zero vias; PET0 is 54.0182/53.9915 mm with 0.0266 mm skew and two
  vias per conductor; REFCLK is 80.1659/80.1738 mm with 0.0079 mm skew and two
  vias per conductor. The eight transitions are limited to the fixed endpoint
  order crossovers.
- KiCad 10.0.5 lock-free project-copy DRC reports no PCIe-named violation,
  clearance error, crossing/short, keepout, or new via/hole error. The board
  remains intentionally unrouted for USB, power, low-speed nets, and final
  zone refill. PCIe is classified ACCEPTABLE_FOR_REV_A because PER0 and
  REFCLK remain above the preferred 70 mm GOOD band despite clean geometry and
  sub-0.032 mm pair skew.

# 2026-08-22 — USB3 fanout placement redesign

- Opened `codex/usb3-fanout-placement` from the frozen USB3-pass checkpoint and
  preserved the active PCIe-pass PCB as
  `placement/usb3-fanout/PiSXMe-usb3-fanout-baseline.kicad_pcb`. Reconstructed
  the CM5, HD3SS3212, TPD4EUSB30, and USB-C physical pin ordering and tested
  four-orientation local candidates for each FAST port.
- Selected FAST-A U5 `(202.5,78,180°)` with U6/U7 `(205,66,180°)` /
  `(214,66,180°)` and J9 `(210.5,58)`. Selected FAST-B U9
  `(202.5,106,0°)` with U10/U11 `(200.5,122,180°)` /
  `(214,122,180°)` and J10 unchanged. The selected direct centerline trials
  reduced high-speed-specific shorting findings to 6 for FAST-A and 1 for
  FAST-B; they are feasibility evidence, not production routes.
- Materialized placement only on `pisxme/PiSXMe.kicad_pcb`. Segment/via
  extraction is byte-identical to baseline (149 segments, 28 vias), proving
  PCIe was untouched. KiCad 10.0.5 placement DRC has zero courtyard, pad,
  hole, keepout, or USB/PCIe copper blockers; 60 total findings are 54
  library-context warnings and six cosmetic silk findings. Production USB3
  routing remains intentionally deferred to the next phase.

# 2026-08-22 — USB3 pass-3 fanout routing blocker

- Opened `codex/usb3-pass3` from `53364864f98bb05733c0882efa0bbfe8d7438aca`
  and preserved the active Candidate-C placement plus frozen PCIe routing.
- Attempted FAST-A SuperSpeed routing only in a disposable copy. The explicit
  mux-to-shunt-ESD-to-Type-C trial exposed one TX1 P/N short, five track
  crossings, and one additional 0.20 mm clearance error beyond the 60-finding
  baseline. The failure is at the eight-conductor 0.5 mm-pitch U5 escape, not
  in PCIe or in the ESD logical topology.
- FAST-B was not attempted because U9 has the same constrained source fanout.
  No USB3 production copper was added to `pisxme/PiSXMe.kicad_pcb`; it remains
  at 149 segments and 28 vias, and the frozen PCIe hash remains
  `94d5ec937de700caf337f0d653a692dbcb0fe9c04a3eaccecec62fe6761f0b`.
- Preserved baseline DRC at `validation/DRC_USB3_PASS3_BASELINE.json` and the
  negative trial at `routing/usb3-pass3/trials/FAST_A_FANOUT_BLOCKED_TRIAL.kicad_pcb`.
  USB3 production routing is blocked until local fanout placement, controlled
  layer policy, or manufacturing/via policy is deliberately reopened.

# 2026-08-23 — HD3SS3212 polarity-remap reference study

- Preserved TI TIDA-00987 design material, the official CM5IO source/PDF, the
  MIT-licensed ModuCard carrier, and the prototype cm5MiniITX source under the
  reference tree. TI's exact lesson is that deliberate differential polarity
  remapping, including the corresponding A-side relationship, is a valid way
  to keep the HD3SS3212/ESD/Type-C fanout straight; the HD3SS3212 data sheet
  requires the polarity relationship to remain consistent from Port A to the
  selected B/C paths.
- Derived a PiSXMe trial map that keeps TX normal and inverts RX consistently
  across A/B/C, rotates U9 to 180 degrees for FAST-B, and assigns the ESD
  shunt pads physically as TX_P, TX_N, RX_N, RX_P. Disposable FAST-A and
  FAST-B copies show improved pair ordering, but their naive centerline
  fanouts still have inter-branch DRC errors (109 total/55 errors for A;
  137 total/83 errors for B). The active schematic, active PCB, and frozen
  PCIe copper remain unchanged; USB3 production readiness stays
  `NOT_READY_FOR_USB3_PRODUCTION_ROUTING` pending a proper constrained fanout
  or controlled second-layer comparison.

# 2026-08-23 — reference-derived USB3 fanout coupon closure

- Acquired and preserved TI’s current public HD3SS3212 layout/checklist/S-parameter materials, official CM5IO evidence, MIT-licensed ModuCard at upstream commit `2d96d2e238e6e020c98220d49595c7a6028a35cf`, and cm5MiniITX at `479fee1dd5831eab652e72c031d0c806a2091c44`. Quantitatively measured the open KiCad boards and annotated TI’s published layout figures without importing their geometry.
- Confirmed the external consensus: use HD3SS3212-supported polarity remapping, route through the flow-through ESD package, use a short local escape, and return to controlled geometry; zero or a small number of symmetric USB3 transitions is normal, while dozens of vias are not required. TI’s exact local width/gap/clearance remain unknown because the public Gerber endpoint is login-gated.
- Built separate disposable PiSXMe-method and TI-method coupons using the selected mux/ESD/Type-C pad coordinates for one representative TX pair. Both have zero DRC errors, zero unconnected items, zero vias, and four documented library-context warnings. The staged proof uses 0.100 mm local width for the bounded escape and 0.13208 mm main geometry; it is not a full-port signoff.
- Ran reference-derived full FAST-A/B trials on disposable copies with the polarity map and bounded local escape. FAST-A retains 148 USB-related DRC records; FAST-B retains 151, including real crossings, shorts, and clearance/mask conflicts. The active board remains production-unrouted for USB3, and the active PCIe records are byte-equivalent to the frozen 244afbe baseline (71 records; hash `954915...cfeb`). Final phase decision remains `NOT_READY_FOR_USB3_PRODUCTION_ROUTING`; the exact remaining blocker is the unresolved four-channel mux/ESD/Type-C fanout, not generic USB3 uncertainty.

# 2026-08-23 — attached TI TIDCCK4 source and corrected USB3 package coupon

- Preserved the user-supplied TI TIDA-00987 source archive at
  `references/usb3/TIDA-00987/TIDCCK4-attached-source-archive.zip` with SHA256
  `e5a4f836967bd1e92fdee2e40ea187f6aca150094213933a75da1573142a2357` and
  extracted its Altium project under the immutable reference tree. Imported
  `TIDA-00987E1.PcbDoc` successfully into a disposable KiCad 10.0.5 board;
  no active PiSXMe source was replaced.
- Measured the TI source's inspected SuperSpeed region: four copper layers,
  1.58464 mm board thickness, 0.2286 mm trace width, approximately 0.1905 mm
  minimum local F.Cu edge gap, 133 F.Cu segments, 16 B.Cu segments, and two
  symmetric layer-transition vias on each of two source paths.
- Found the active PiSXMe HD3SS3212 and DQA ESD footprints are physically
  wrong for their selected MPNs: the active mux is a two-row 5 mm model rather
  than the RKS0020A perimeter pattern, and the active DQA model is a
  horizontal two-row pattern rather than the two-side package. Added
  analysis-only corrected footprints, package comparison artifacts, and a
  corrected four-pair coupon; the active schematic/PCB and frozen PCIe remain
  byte-identical to the branch base.
- The corrected coupon uses explicit TI-style polarity remapping, flow-through
  ESD pads, a short local jog around the ESD ground pad, no vias, and
  PiSXMe's 0.13208 mm main-route width. Under its explicit bounded local DRC
  rule KiCad reports zero violations and zero unconnected items; the default
  0.20 mm rule reports eight local clearance errors and no opens/shorts. USB3
  production readiness remains `NOT_READY_FOR_USB3_PRODUCTION_ROUTING` until
  a full two-port trial uses the corrected footprints and closes schematic/PCB
  parity.

# 2026-08-23 — high-speed via-policy amendment

- Established `design/HIGH_SPEED_VIA_POLICY.md` as authoritative for all
  remaining PiSXMe PCIe and USB3 work. Via count is a cost term, not a hard
  objective: prioritize correct connectivity/polarity, intentional reference
  planes, no crossings/pathological fanout, direct paths, pair symmetry,
  impedance continuity, then minimal transitions and vias.
- A clean zero-via route remains excellent, but a deliberate symmetric
  transition per conductor is equally acceptable when it produces the better
  electromagnetic path. Repeated layer bouncing, unexplained transitions,
  and HDI/microvias used only to reduce a reasonable through-via count remain
  unacceptable.
- USB3 fanout work must now explicitly permit the topology
  `fine-pitch escape -> symmetric referenced transition -> controlled route`
  when that is cleaner than forced F.Cu routing. Future receipts must report
  vias per conductor, total port vias, the reason for each transition, layers
  and reference planes before/after, return-path stitching, stub treatment,
  and whether removing the transition improves or worsens the path.
- The existing PCIe copper remains frozen and unchanged by this amendment.

# 2026-08-23 — corrected-footprint full-port parity trials

- Opened `codex/full-port-corrected-footprint-trials` from the preserved
  `90f0ab0d980a9a332e91967cb0f2d1a02441d39f` state. Verified the disposable
  TI-derived HD3SS3212 RKS0020A footprint (20 perimeter signal pads plus
  thermal pad) and DQA side-row ESD footprint for trial use. The active
  `PiSXMe.kicad_pcb` and `PiSXMe.kicad_sch` hashes remained
  `21a4a6a877b212f1d55a3456a47e93c14b2ca3ad` and
  `8437c0241976153a724c8935be8b16b650cc8edf` before and after.
- Built complete disposable FAST-A and FAST-B corrected-package trials using
  the exact CM5 USB3 launch coordinates, legal polarity remapping, bounded
  0.100 mm local escape, and flow-through DQA assignments. FAST-A DRC found
  54 violations (17 crossings, 8 shorts, 23 mask bridges); FAST-B found 84
  (28 crossings, 10 shorts, 38 mask bridges). These are real fanout failures,
  not warnings that can be waived; the one-pair corrected coupon passing does
  not prove the complete reversible Type-C topology.
- Added a disposable symmetric F.Cu-to-B.Cu layer-transition coupon. It has
  zero error-severity geometry findings and zero unconnected pads, with only
  twelve silkscreen warnings. This proves a controlled transition can solve a
  local crossing in principle, but it is not a full-port or JLC stackup SI
  signoff.
- Final decision remains `NOT_READY_TO_REPLACE_ACTIVE_USB3_FOOTPRINTS`. The
  exact remaining blocker is the unproven complete RKS-to-two-DQA-to-reversible
  Type-C fanout at the fixed placement. No active USB3 footprint, schematic,
  production USB3 copper, or frozen PCIe copper was changed.

# 2026-08-23 — mux relocation full-port proof

- Built final disposable complete FAST-A and FAST-B reversible Type-C trials
  using the corrected TI-derived HD3SS3212 RKS0020A and DQA footprints,
  legal polarity remapping, bounded 0.100 mm local escape, and deliberate
  signal-layer transitions where the topology required them.
- Selected the relocation winners FAST-A A9 at `(187.5, 82)` and FAST-B B8 at
  `(187.5, 120)`; ESD devices remain adjacent to their receptacles.
- All four final relocation boards have zero copper shorts, pair crossings,
  clearance violations, and pad-overlap violations. Remaining findings are
  three silkscreen-over-copper warnings plus one library-context warning per
  disposable board, and expected connectivity records from stripped trial
  support circuitry.
- Result is `MUX_RELOCATION_SOLVES_USB3`; the controlled-via fallback branch
  was not entered. This is a fanout-placement proof, not production USB3
  routing approval: the next phase must materialize corrected footprints,
  calculate non-L1 geometry/reference planes, add ground-return stitching,
  and rerun DRC/SI on the active board.
- Active PCB and schematic remain unchanged; frozen PCIe remains untouched.

# 2026-08-23 — USB3 production routing pass opened

- Opened `codex/usb3-production-routing` from the successful relocation proof
  checkpoint `505914ccf2bd76756a836487266b5badfdd703ae`. Captured the active
  220 × 140 mm board baseline, corrected-footprint migration targets, and a
  machine-checkable PCIe route fingerprint before changing the active PCB.
- The USB3 pass is explicitly scoped to corrected HD3SS3212/DQA footprints,
  winning mux/ESD placement, FAST-A/B SuperSpeed, and their USB2 companions.
  V100 power, regulators, SERVICE, low-speed routing, final zones, global
  stitching, and PCIe remain frozen/out of scope.

# 2026-08-23 — USB3 production SuperSpeed materialization checkpoint

- Materialized the verified TI-derived RKS0020A/DQA footprints and the proven
  relocated FAST-A/B mux/ESD placement onto the active PCB. U7 was retained at
  `(204.5,68)` for the real J2 center-hole constraint; U11 was retained at the
  validated `(201,136)` proof coordinate because `(214,136)` creates actual
  J10 fanout crossings.
- Production SuperSpeed copper now uses F.Cu/B.Cu only, corrected bounded
  local escape areas, matched ordinary through-via transitions, and eight
  deliberate /GND return vias. No USB3-specific short, crossing, clearance,
  pad-overlap, or pair-rule error remains in the lock-free CLI receipt.
- The frozen PCIe route geometry remains identical to the pre-USB3 baseline;
  the schematic is unchanged. B.Cu/In4 power-plane continuity and aggregate
  branch skew remain explicit next-phase SI/power-zone review items. USB2
  FAST-port companions were completed after this checkpoint; VBUS, regulators,
  SERVICE, remaining low-speed routing, and final zones remain intentionally
  incomplete.

# 2026-08-23 — USB3 production routing accepted

- Completed the production FAST-A and FAST-B USB2 companion nets after the
  SuperSpeed freeze. All four reversible Type-C D+/D− nets are connected with
  no USB2-specific shorts, crossings, clearance, pad, solder-mask, hole, or
  unconnected finding in the lock-free KiCad 10.0.5 DRC copy.
- The active checkpoint contains 333 segments, 128 vias, six planned copper
  zones, and 28 non-keepout fine-escape rule areas. The USB2 branches use
  three ordinary through-vias per net and In2/In3 stems; they are documented as
  lower-speed companion connectivity, not SuperSpeed impedance evidence.
- PCIe `/PER0`, `/PET0`, and `/REFCLK` normalized segment/via geometry is
  byte-identical to the frozen baseline. The schematic is unchanged.
- Final USB3-scope decision is `USB3_PRODUCTION_ROUTING_ACCEPTED`. This does
  not release the board for fabrication: V100/CM5/USB power, SERVICE, fans,
  final plane refill, thermal review, and remaining low-speed work are next.
## 2026-08-23 — functional integration-routing pass opened

- Forked `codex/integration-functional-routing` from the accepted USB3/PCIe checkpoint `80cedb1f43e7d8af81c1919177bc25af53e11d70`.
- Captured live-board SHA-256, KiCad 10.0.5 lock-free DRC/ERC receipts, and a machine-readable open-net inventory before changing copper.
- The board remains pre-final-zone: accepted PCIe and USB3 are protected; remaining classes are power, service, recovery, control, cooling, debug, and low-speed routing.

## 2026-08-23 — V100 protected 12 V integration checkpoint

- Rebuilt the accepted PCIe/USB3 baseline before adding power and replaced the
  failed numeric-net experiment with name-bearing `/RAW_A_12V`, `/RAW_B_12V`,
  `/FUSED_A_12V`, `/FUSED_B_12V`, and `/VPROT_12V` copper.
- Added the dual-fuse/protection paths, broad protected V100 bus, 13
  distributed SXM2 power-field transitions, and independent CM5/USB buck
  input feeds: 77 segments and 39 vias.
- The USB-buck feed was intentionally moved onto In2.Cu so the accepted B.Cu
  USB3 routes remain untouched. Lock-free KiCad 10.0.5 DRC found no new power
  short, crossing, or clearance issue; only the pre-existing PET0/J2
  clearance and inherited library/silkscreen findings remain.
- The short 0.25 mm TPSM63606 pad escapes are not bulk-current bottlenecks,
  but remain explicitly deferred to final-zone/thermal review.

## 2026-08-23 — CM5 5 V integration checkpoint

- Corrected the previous study-coordinate error by routing the six actual J2
  `/CM5_5V` contacts (pads 77/79/81/83/85/87) in the active 180-degree CM5
  placement. The route adds 27 segments and two through-vias.
- The contact field escapes on F.Cu, then the main trunk uses In2.Cu so it
  avoids the frozen USB3 B.Cu fanout and the U17 ground island. Lock-free DRC
  reports no CM5 5 V short, crossing, clearance, or open-net record.

## 2026-08-23 — USB peripheral 5 V source-routing checkpoint

- Replaced the stale USB-rail study geometry with current U16/U4/U8
  coordinates and name-bearing `/USB_5V_PERIPH` copper: 19 segments and three
  through-vias.
- The dedicated rail uses F.Cu pad escapes and an In2.Cu distribution trunk;
  the long FAST-A rise uses the far-right corridor to avoid all accepted
  USB3 through-via fields and the CM5 5 V route. FAST-A and FAST-B input
  islands are connected with no new USB 5 V error.
- U13 SERVICE input remains intentionally grouped with the next SERVICE
  VBUS/role-routing checkpoint. Final regulator thermal and plane review are
  deferred to the final-zone phase.

## 2026-08-23 — functional integration routing checkpoint

- Completed the ordinary functional routing pass without changing frozen
  PCIe or accepted USB3 geometry. The active board now contains the dual
  protected 12-V distribution, CM5 5-V, USB peripheral 5-V, SERVICE USB2
  data/CC/role/recovery paths, UART, reset/CLKREQ/power controls, mux
  controls, fan tach/PWM, and cooling-header routes.
- Current structural state is 680 segments, 260 vias, 40 zone/rule-area
  records, 54 footprints, and a 220 x 140 mm outline. The current PCB hash is
  `419c1f28b689ff03c69bb672f23e6fff189384e50f86db6659c6554ad686671e`.
- PCIe plus USB3 normalized geometry remains identical to the accepted
  `80cedb1` fingerprint. No high-speed route was used as a shortcut for the
  integration copper.
- Lock-free KiCad 10.0.5 validation reports 0 ERC errors and 46 inherited /
  explained warnings. DRC has no new electrical short, clearance, keepout,
  USB2, USB3, or differential-pair issue; 348 open records are preserved in
  the final machine-readable inventory for final GND/VBUS/chassis/protected
  12-V zones and inherited accepted endpoint records.
- Final zone/pour, B.Cu USB3 reference preservation, thermal-via/current
  qualification, and release-package validation remain explicitly deferred.
## 2026-08-25 — final zones/release review baseline

- Started `codex/final-zones-release-review` from `613901a`.
- Captured the pre-zone board at `release/final-pass/PiSXMe-before-final-zones.kicad_pcb`.
- Baseline PCB SHA-256: `419c1f28b689ff03c69bb672f23e6fff189384e50f86db6659c6554ad686671e`.
- Frozen PCIe/accepted USB3 fingerprints remain governed by
  `validation/integration-pass/HIGH_SPEED_PRESERVATION.json`.
- Final zones, thermal vias, release outputs, and external-review artifacts are
  not yet implemented; no order or external submission is authorized.

## 2026-08-25 — final-plane implementation checkpoint

- Materialized the final-plane candidate on `codex/final-zones-release-review`:
  full GND reference planes on F.Cu/In1/In4, bounded protected-12-V In3
  manifolds, bounded CM5 5-V and USB 5-V In2 regions, and local VBUS source
  closures. Frozen PCIe and accepted USB3 geometry remained unchanged.
- The candidate has no new real short, clearance, crossing, plane-isolation,
  mask-bridge, thermal, hole, or drill DRC defect. ERC remains 0 errors with
  46 categorized library/intentional warnings.
- `/3V3` closure was tested with ordinary through-via In2 and In3 alternatives;
  both produced real conflicts against frozen USB3/control/power geometry.
  The 9 mandatory control-power opens remain a release blocker. No HDI,
  via-in-pad, or frozen high-speed reroute was introduced silently.
- USB-C `CHASSIS_GND` shell chaining was also tested and rejected after real
  conflicts. The 5 shell relationships remain an explicit chassis/shield
  blocker rather than being waived as ground.
- Final thermal/current records classify V100 distribution as
  `PASS_WITH_REV_A_MARGIN/RISK`; regulator/protection results are analytical
  only and require hardware measurement. Manufacturing outputs and external
  review packet are held. No order, upload, or publication is authorized.
## 2026-08-26 — blocker-closure via census and shell/3V3 trials

- Branched as `codex/blocker-closure-via-audit` from the final-plane state at
  `46458a1`.
- Enumerated all 260 vias from the final-plane baseline. Every via has a
  classified signal, return, connector-breakout, or current-spreading role;
  no redundant/orphan via was proven removable.
- Tested a bounded F.Cu `/3V3` distribution region. The least-invasive
  successful closure is a short U5 local escape plus two ordinary 0.40/0.30
  mm through-vias; the local rule remains bounded and is not a global
  clearance change.
- Tested USB-C shield closure. The direct S1/S2-to-`/GND` strategy closes all
  shell relationships without a new real DRC class and follows a working
  open CM5-carrier precedent. Long F.Cu/In2 shell trunks were rejected after
  measured crossings/shorts/clearance failures.
- PCIe and accepted USB3 geometry remain protected. The active promotion and
  combined DRC/ERC rerun are the next gates; no release package is claimed
  until those receipts pass.
## 2026-08-26 — blocker-closure promoted and release-package gate opened

- Promoted the bounded low-current `/3V3` closure: a 0.100 mm local U5
  escape, two matched 0.40/0.30 mm ordinary through-vias, and the bounded
  F.Cu distribution region. The final active DRC has zero `/3V3` endpoint
  records.
- Promoted the direct USB-C shell-to-`/GND` strategy in both schematic and
  PCB. The final active DRC has zero `CHASSIS_GND` endpoint records. A future
  metal enclosure may need a system-level EMI review; that is not an open PCB
  net in this Rev-A candidate.
- Rationalized the final-plane via set from 260 to 241: removed 16 exact
  co-located high-current duplicates and six isolated/dangling stale vias,
  retained two required `/3V3` vias, and added one required `/PERST_N` via.
  The final census has zero unknown classifications.
- Final lock-free KiCad 10.0.5 validation reports 0 ERC errors and 46
  categorized warnings. DRC reports no real copper, clearance, keepout,
  crossing, hole, drill, or differential-pair defect; the remaining records
  are documented library-context, cosmetic silkscreen, zone-self, and
  inherited USB3 endpoint abstractions.
- Active hashes and the exact connected high-speed preservation comparison are
  recorded under `release/blocker-closure/`. Internal manufacturing/review
  package generation is now permitted for inspection only; no order, upload,
  or public release is authorized.
## 2026-08-26 — release bookkeeping parity checkpoint

- Re-ran lock-free KiCad 10.0.5 ERC/DRC after making the accepted CLKREQ#
  strap explicit: R1 is populated as Yageo `RC0603FR-070RL`. TP3 is identified
  as Keystone Electronics `5000`; TP1/TP2 remain PCB-only no-net markers.
- The current final DRC receipt explicitly separates 57 `violations` from 82
  `unconnected_items` (91 raw error-severity records total). It does not call
  the 66 GND/VBUS zone-context records a clean DRC; they remain visible plane
  review items. The 16 inherited USB3 endpoint-island records remain the
  accepted abstraction category.
- Corrected stale release identity/parity records to bind the active PCB,
  schematic, and design-rule hashes to the promoted closure state. D1 remains
  an intentionally un-netted PCB-only TVS placeholder and is visible as a
  pre-fabrication review item rather than being silently included in the BOM.

## 2026-08-26 — internal external-review packet generated

- Regenerated the internal schematic PDF, six copper-layer SVG plots, Gerbers,
  Excellon drill files/maps, BOM/CPL, and four 3D views from the active
  blocker-closure board. Source identity is bound by the active PCB,
  schematic, and design-rule SHA-256 records.
- Added the final hostile via and chassis/ESD reviews. The 241-via population
  is rationally explained with zero unknowns; shell-to-digital-ground is
  closed for Rev-A while enclosure EMI remains a stated risk.
- Prepared `external-review/PiSXMe-RevA-RC1/` as an internal peer-review
  packet. D1 remains a visible fabrication gate, raw DRC zone-context and
  inherited endpoint records remain visible, and no order/upload/publication
  is authorized.

## 2026-08-26 — RC1 archive integrity checkpoint

- Created `manufacturing/release/PiSXMe-RevA-RC1.zip` from the review packet;
  ZIP integrity passed with 117 files and the SHA-256 recorded in
  `manufacturing/release/RC1_ARCHIVE_RECEIPT.md`.
- The external-review decision is intentionally scoped to peer review only.
  The packet is not a fabrication release: D1's un-netted placeholder,
  visible plane-context records, thermal measurement gaps, and enclosure EMI
  behavior remain explicit review/fabrication-gate items.

## 2026-08-26 — review packet high-speed record correction

- Marked the older route-study metrics as historical and replaced the packet's
  current high-speed preservation copy with the blocker-closure receipt. This
  prevents pre-closure route counts and pending B.Cu wording from being read
  as the active board state.
- Rebuilt `PiSXMe-RevA-RC1.zip` after that documentation correction and
  retained the previous archive as a recoverable `-v1` copy.
## 2026-08-26 — external-review visual closure

- Added six KiCad 10.0.5 source-board close-ups covering PCIe, FAST-A,
  FAST-B, USB-C/chassis, the bounded `/3V3` closure, and the regulator area.
  Their exact render pivots and SHA-256 values are recorded in the
  reproducibility receipt and checksum manifest; the layer-resolved SVGs
  remain the copper-inspection authority.
- Rebuilt the internal peer-review archive with the close-ups and an explicit
  index. ZIP integrity passed with 123 files and 12,480,785 uncompressed
  bytes; the prior close-up-free archive is retained as `-v2` and the first
  archive remains retained as `-v1`.
- The active board, schematic, design rules, and frozen connected PCIe/USB3
  geometry were not changed by this visual/package step. External review is
  authorized only as an internal packet; fabrication ordering, upload, and
  public release remain prohibited.
## 2026-08-26 — final evidence consistency correction

- Clarified that the older 260-via functional breakdown is a retained
  pre-cleanup baseline, while `VIA_CENSUS_FINAL.md` is authoritative for the
  active 241-via board. This removes an otherwise confusing sum mismatch in
  the via assessment without changing PCB copper or any design hash.
## 2026-08-27 — architecture sanity audit baseline

- Opened `codex/architecture-sanity-audit` from `88b8688` and recorded
  immutable SHA-256 guards for the active PiSXMe PCB, schematic, and design
  rules. This audit does not modify those files.
- Preserved the current Raspberry Pi CM5 IO Board revision-2 KiCad package
  under `references/cm5/official-cm5io-rev2/` with source and board hashes.
- Added a read-only reference-via census tool and generated machine-readable
  counts for PiSXMe, TI TIDA-00987, official CM5IO, ModuCard, and cm5MiniITX.

## 2026-08-27 — USB-A simplification audit closure

- Preserved the active PiSXMe PCB, schematic, and design rules byte-for-byte
  while completing the architecture minimality and via audit.
- Added quantitative via audits for the preserved TI source proxy, official
  CM5IO Rev 2, ModuCard, cm5MiniITX, and the active 241-via board.
- Built a disposable direct USB-A SuperSpeed variant. Both independent ports
  route cleanly with 0 signal vias, 0 unconnected items, 0 DRC violations,
  and 0.109838 mm maximum trial pair skew; the trial intentionally omits
  final VBUS/ESD/USB2 implementation and is not a fabrication design.
- The audit found no second-SXM2, NVLink, x16, unused-lane, Ethernet, HDMI,
  MIPI, microSD, or hub baggage. It recommends `SWITCH_FAST_PORTS_TO_USB_A`
  for a future revision because fixed Type-A preserves the two native 5 Gbps
  CM5 links while removing the current Type-C mux/branch complexity.
- D1 remains a documented pre-fabrication provenance gate; it was not altered
  in this read-only audit.

## 2026-08-27 — conductor-level via census completion

- Expanded the active-board USB3 via audit from grouped families to the
  individual CM5-side and FAST-port net paths, including endpoints, via
  counts, and inferred F.Cu/B.Cu layer sequences.
- Confirmed the direct USB-A trial remains a disposable SuperSpeed-only
  proof: no active PCB/schematic/rules file changed.

## 2026-08-27 — active USB-A migration baseline

- Opened `codex/usb-a-active-migration` from the architecture-sanity audit
  closure and preserved the active USB-C PiSXMe PCB and schematic under
  `migration/usb-a/pre-migration/` with matching SHA-256 values.
- Recorded the 54-footprint, 241-via, 220 x 140 mm baseline and the frozen
  PCIe fingerprints before authorizing active FAST-A/FAST-B simplification.
- The migration will replace only the unnecessary reversible USB-C FAST
  architecture; SERVICE USB-C, V100/SXM2, and PCIe remain protected.

## 2026-08-27 — USB-A schematic migration checkpoint

- Replayed the direct FAST-A/FAST-B Type-A schematic migration from the
  preserved USB-C source after correcting the cleanup boundary so the U16
  USB 5 V buck support network remains intact.
- Added the project `USB_A_FAST` symbol and removed unused embedded FAST
  Type-C and HD3SS3212 definitions from the active schematic.
- Schematic ERC now reports 0 errors, 0 multiple-net-name findings, and 44
  warnings limited to documented CLI footprint-link, isolated-label, and
  intentional-NC categories. No warning requires a design change.

## 2026-08-27 — USB-A active footprint and placement checkpoint

- Materialized the direct fixed-orientation USB-A FAST-A/FAST-B placement on
  the active PCB from the preserved USB-C baseline.
- Replaced J9/J10 with Würth 692122030100 Type-A receptacles, removed U5/U9
  HD3SS3212 and U7/U11 duplicate high-speed ESD footprints, retained U4/U8
  TPS2553 current limiting and U6/U10 corrected flow-through ESD.
- Reconciled the schematic footprint links for U6/U10 to
  `TPD4E05U06_DQA_TI_FLOWTHROUGH` and retained the corrected Type-A port
  symbol/net mapping.
- Placement-only DRC evidence has zero shorts, courtyard overlaps, and
  hole-clearance violations; stale/incomplete zones and missing functional
  connections remain intentionally deferred to direct USB-A routing.

## 2026-08-27 — USB-A functional routing checkpoint

- Materialized direct USB 3 Type-A SuperSpeed routing for FAST-A and FAST-B
  from the CM5 through the retained per-port ESD devices to the fixed host
  receptacles, preserving the frozen PCIe geometry and SERVICE USB-C block.
- Completed the FAST-A/FAST-B USB2 companion paths on bounded inner-layer
  corridors with short pad escapes; no USB-A functional route was left to
  inherit the deleted reversible Type-C fanout.
- Moved the FAST-B ILIM resistor away from the CM5 connector NPTH as part of
  the local migration cleanup. Full-board zone closure, D1 disposition, and
  remaining integration controls are still separate closure work.

## 2026-08-27 — USB-A integration routing checkpoint

- Closed the active direct USB-A functional integration routes without touching
  frozen PCIe or retained SERVICE architecture.
- Rebuilt CM5 5 V, FAST-A/FAST-B VBUS, SERVICE VBUS, UART, CLKREQ, fan, and
  control handoffs with explicit layer choices around the fixed high-speed
  copper.
- Native filled-board DRC on the isolated copy reports zero true geometric
  routing defects; remaining records are inherited library/silkscreen,
  zone-connectivity, and intentional same-net flow-through ESD abstractions.

## 2026-08-27 — USB-A RC2 closure and external-review package

- Completed the active FAST-A/FAST-B migration from reversible USB-C to direct
  Würth 692122030100 USB3 Type-A host ports, retaining per-port ESD and
  current-limited VBUS while leaving SERVICE USB-C and PCIe protected.
- Reconciled J9/J10 schematic indentation so the internal BOM contains all 46
  populated schematic instances; CPL contains 49 board rows with MECH1/TP1/TP2
  explicitly documented as DNP board-only markers.
- Fresh native-refill DRC reports zero genuine geometric violations; ERC has
  zero errors and only documented project-library/intentional-label/NC
  warnings. The remaining USB3 route-length/skew margin is disclosed as an
  external-review risk rather than hidden.
- Generated the non-public `PiSXMe-RevA-RC2` source, Gerber, drill, BOM/CPL,
  evidence, render, and review packet without ordering or publishing it.

## 2026-08-28 — human-factors audit of USB-A RC2

- Inspected the active RC2 board as a physical object with the manufacturer
  STEP model for the Würth 692122030100 USB3 Type-A receptacle. The active
  `0°` J9/J10 orientation is outward-facing at the right edge; the rotated
  negative-control trial was rejected because this mixed SMT/PTH footprint
  overlaps its own pad fields when rotated.
- Identified two concrete physical blockers that were not electrical DRC
  findings: F1/Q1 enter the contractual cooler-owned XY reservation, and the
  10 mm-wide J5/J6/J7 outlines overlap at 8 mm center pitch. Functional
  F.SilkS access labels and mating-housing/plug envelopes also remain
  incomplete.
- Preserved active PCB, schematic, project, and rules hashes exactly; no PCIe,
  USB, power, schematic, or RC2 release files were modified. The human-factors
  decision remains `HUMAN_FACTORS_NOT_ACCEPTABLE` pending a dedicated
  power/protection placement correction, cooling-header spacing correction,
  label pass, and final mating-envelope evidence.

## 2026-08-28 — approved Rev-A redesign execution baseline

- Approved implementation authority is `Approved Plans/PiSXMe_RevA_Verified_Redesign_Work_Package.md`.
- Execution is staged M1 through M10 with a validation gate and checkpoint
  commit at every milestone; the settled CM5-to-V100 PCIe Gen2 x1 basis is
  preserved unless contradictory evidence appears.
- Initial source baseline is the active `codex/usb-a-active-migration`
  checkout. No design source or release artifact was changed before this
  checkpoint.
2026-08-28 — M1 schematic/library truth checkpoint

- Applied the approved M1-only source truth corrections: TPS2553 physical pin numbering, fixed UFP retirement markers for U12/U13/U14, true three-pin TPD2EUSB30A DRT instances for U15/U17/U18, corrected Q1/Q2 and U4/U8/U16 PCB pad-net maps, and explicit U16 support components (input/output capacitance, VLDOIN, feedback, RT, and PG pull-up) in schematic and PCB.
- Existing copper/routing was intentionally not changed. KiCad netlist export succeeds and ERC reports zero errors (warnings remain from the pre-existing project-local library configuration and intentional isolated labels). DRC/parity remains non-gating at this checkpoint because the inherited architectural PCB contains unresolved source/board abstractions and the newly added local support parts are not yet routed; M2–M9 own those closures.

2026-08-28 — M2 floorplan checkpoint

- Applied only the approved mechanical origins for F1/Q1/F2/Q2, J5/J6/J7, and U16. The cooler intrusion and 8 mm fan-header pitch are removed at the placement level; all copper affected by these moves remains intentionally pending the bounded power/interface reroute milestones.

2026-08-28 — M3 power-support checkpoint

- Materialized the unambiguous TPS2553 input bypass and FAST-A/B port-bulk capacitor positions. The cold-plug policy remains explicit; TVS stand-off/clamp and protected-bus bulk selection stay an external-review gate until the source maximum and package/thermal choices are fixed.

2026-08-28 — M4 layer-policy checkpoint

- Removed only prohibited routed segments from In1/In4 and non-power segments from In2/In3, leaving replacement routing to M5/M6. This makes the intended ground/reference-layer policy explicit without inventing unreviewed copper.

2026-08-28 — M5 high-speed gate blocked

- Stopped before PCIe/USB rerouting because the post-M4 source has 499 unconnected items and 322 schematic-parity records, including geometry that requires an interactive, pair/skew-aware route review. Netlist export succeeds and ERC has zero errors, but the high-speed topology is not safe to synthesize automatically. M6 and later milestones are gated on a reviewed KiCad reroute and a subsequent DRC/parity pass.

2026-08-28 — M5 native-board-stream integrity recheck

- Found and repaired 114 stray closing parentheses introduced by the M4 text rip-up. The repair preserved all non-parenthesis PCB bytes and restored a balanced KiCad board stream; KiCad statistics now parse 150 through-vias instead of the 7 vias visible before repair. Native DRC consequently exposes 855 violations and 118 unconnected items, including clearance, mask-bridge, isolated-copper, crossing/shorting, dangling-via, and dangling-track classes. This supersedes the earlier under-parsed M5 counts and blocks M6 until the layer-policy board is rebuilt and high-speed topology is re-established as native KiCad connectivity.

2026-08-28 — M5 reproducible DRC baseline

- Fresh KiCad 10.0.5 DRC on clean HEAD `ee7002d` (PCB SHA-256 `7ad9dddc47bd2e786e82cea02dc52bf8ad34a6aaf0370dc9a81a4e6d842d7c64`) reports 856 violations and 118 unconnected items. The one-count difference from the first post-repair receipt is recorded as a reproducibility correction; the gate remains failed.
- The same fresh run with `--schematic-parity` reports 348 parity records. This is the current parity baseline; it is not evidence of a clean PCB/schematic contract.

2026-08-28 — independent M5 gate audit

- Independent read-only review confirms the M5 verdict is FAIL: the repaired board parses, but native DRC reports 856 violations, 118 unconnected items, and 348 schematic-parity records. It also confirms a separate U16 package-parity defect: schematic C12/C13 are 1210 and C14/R8–R11 are 0603, while the PCB uses `PiSXMe:M1_1206` for all seven parts. M6 remains gated until a valid M4 reconstruction and explicit U16 footprint parity correction are reviewed.

2026-08-28 — corrected M4 native reconstruction

- Rebuilt the active PCB and schematic baseline from balanced M3 commit `b7a36ef` using a balanced-expression layer filter. The resulting board is natively parseable with 406 routed segments, 165 KiCad-recognized through-vias, zero In1/In2/In4 signal segments, and only `/VPROT_12V` on In3. Native DRC is 811 violations, 157 unconnected items, and 348 parity records; ERC is zero errors with 86 warnings. This supersedes malformed M4/M5 board-stream checkpoints while preserving them in Git for rollback. M5 SERVICE/routing changes must be replayed separately.

2026-08-28 — U16 support package parity correction

- Corrected C10/C11/C12/C13/C14/R8–R11 PCB package identifiers and nominal pad geometry to match their schematic-declared KiCad 1206/1210/0603 packages, preserving UUIDs and net assignments. Native DRC/parity changed to 1,420 violations, 156 unconnected items, and 339 parity records; U16 support routing and TI layout validation remain open.

2026-08-28 — M5 SERVICE migration checkpoint

- Reapplied the approved fixed-device SERVICE architecture to the balanced M4 board: removed U12/U13/U14 and obsolete SERVICE control traces/vias, retained J11 USB2 recovery, and added R12/R13 5.1 kOhm Rd plus C19 1 uF VBUS bypass. Native parse/statistics pass with 153 through-vias; netlist export passes; ERC remains zero errors with 95 warnings; DRC/parity is 812/150/348. USB2/high-speed routing remains gated.

2026-08-28 — U16 local support placement checkpoint

- Moved the nine U16 support footprints into the local regulator field while keeping U16 fixed and adding no copper. Native DRC is 810 violations and 149 unconnected items; package parity remains corrected and routing/SI/thermal closure is still open.

2026-08-28 — current M5 gate recheck after U16 placement

- Re-ran KiCad 10.0.5 against clean HEAD `4b19de6` (PCB SHA-256 `abcf70753c129a1e7099f04f7700f63b4e4c80fbac31d56a664b17835204b29f`). Native parse/statistics pass; ERC is 0 errors/95 warnings; DRC is 810 violations with 149 unconnected items and 348 schematic-parity records.
- Verified current routed-layer use: F.Cu 290 segments, B.Cu 90, In3.Cu 11 `/VPROT_12V` power segments, and no In1/In2/In4 signal segments. Verified 153 through vias (129 F.Cu-B.Cu, 8 each F.Cu-In1/In2/In3; no blind/buried/microvias). The literal `/GND` via count is five, but that count is misleading as a board-wide return/stitching metric because signal/power vias also provide through-stack continuity.
- Independent PCIe review found no contradictory evidence against the settled CM5-to-V100 PCIe Gen2 x1 basis. PER0 remains a good frozen route; PET0 and REFCLK have balanced lengths but lack local return vias; PERST retains three orphan vias and one sideband open for M7. M5 remains blocked pending a disposable, clearance-checked local-return-via study and native gate review. M6 USB reconstruction is not authorized from this state.

2026-08-28 — M5 PCIe transition-return correction

- Added six deliberately placed `/GND` F.Cu-B.Cu through vias at the PET0 and REFCLK transition fields only; PER0, PET0 raw legs, and unrelated routing remain frozen.
- Disposable candidate study and native KiCad 10.0.5 DRC found no candidate-specific short, clearance, hole, or connectivity violation. Current global DRC remains 811 violations / 149 unconnected records and is not a release claim.
- M5 high-speed transition scope is complete; PERST_N and PCIE_PWR_EN remain deferred to M7. See `validation/PiSXMe_M5_transition_return_checkpoint.md`.

2026-08-28 — M6 USB ESD truth precondition

- Corrected U15/U17/U18 schematic footprint fields to `PiSXMe:TPD2EUSB30A_DRT` and removed only the eight F.Cu segments attached to the NC pads 6/7/9/10 of U6/U10; signal and GND pads remain unchanged.
- Native validation after this focused edit: 159 through-vias, 0 blind/buried/microvias, 0 ERC errors, 810 DRC violations, 146 unconnected records, and 345 parity records. USB branches remain frozen for the M6 rebuild.
- See `validation/PiSXMe_M6_ESD_truth_checkpoint.md`.

2026-08-28 — M6 USB rebuild gate blocked

- Re-verified the current USB source after the ESD/package precondition. U6/U10
  are six-pad flow-through footprints with corrected netless/pad assignments,
  but the existing FAST-A/B USB3 branches do not terminate at the current
  device pads and FAST-A/B/SERVICE USB2 still contain vias or mixed-layer
  fragments. A bounded route reconstruction could not be made
  clearance-checked and pair-symmetric without changing frozen corridors, so
  no USB copper was changed and M6 remains FAIL. See
  `validation/PiSXMe_M6_USB_rebuild_checkpoint.md`.

2026-08-28 — M6 USB census correction

- Balanced source parsing confirms each FAST-A/B USB3 conductor currently has
  four signal vias, each FAST-A/B USB2 conductor has four vias, and each
  SERVICE USB2 conductor has four vias across mixed/fragmented branches. This
  exact census supersedes earlier informal USB-via counts and reinforces the
  M6 hard gate without changing the active board.

2026-08-28 — M6 disposable corridor study

- A target-only disposable A* study, using current U6/U10/J2/J9/J10 pad
  coordinates and non-target copper as obstacles, failed to find a
  clearance-safe FAST-A ESD-to-J9 path on F.Cu and again on a B.Cu fallback.
  The result is feasibility evidence for the fixed-placement fanout blocker,
  not a release route or DRC claim. No active PCB copper changed.

2026-08-28 — M6 I/O architecture replan

- The fixed dual-USB topology remains blocked after the disposable F.Cu/B.Cu
  corridor failures. Candidate 1 (native CM5 Ethernet plus FAST-A plus
  SERVICE) was rejected for promotion because its disposable mapped board had
  1,331 DRC violations, 156 unconnected items, 26 Ethernet unconnected items,
  and no Ethernet copper route.
- A pin-accurate disposable JMS578 coupon using the stock 6 x 6 mm QFN-48
  footprint connected all eight USB3/SATA differential nets with zero
  unconnected items. Its 70 fixture DRC violations are not full-board proof;
  they are retained as coupon limitations.
- The next M6 design basis is therefore native CM5 Gigabit Ethernet,
  JMS578 USB3-to-SATA, a clearly SATA-only B-key M.2 socket, and SERVICE
  USB2 recovery, with both external USB3 host branches removed. Candidate 2
  remains an M6 migration basis, not a passed gate. CM5/V100/PCIe, board
  outline, power concept, PER0, and M4 layer philosophy remain frozen.
- No active schematic or PCB source was changed by this architecture decision.

2026-08-28 — M6 architecture-unblocker current-source recheck

- Rebuilt the disposable Candidate 1 and Candidate 2 studies from the staged
  M2 240 x 140 mm source snapshot, preserving the active source unchanged.
- Candidate 1 (native CM5 Ethernet + FAST-A + SERVICE) contains the CM5IO-derived
  proxy footprints but zero Ethernet segment records; native KiCad 10.0.5 DRC is
  1,299 violations / 179 unconnected items. It is not routability evidence.
- Candidate 2 (native Ethernet + JMS578/M.2 SATA proxy + SERVICE) contains zero
  Ethernet or SATA segment records; native DRC is 1,108 violations / 113
  unconnected items. It is a placement/proxy study only, not a passed full-board
  candidate. The earlier JMS578 coupon remains topology-only evidence.
- Neither replacement architecture is promoted. M6 remains open and M7-M10 are
  still prohibited until a pin-accurate, current-source, clearance-checked
  candidate closes true signal opens/shorts and return-path/mechanical gates.
- See `validation/PiSXMe_M6_architecture_unblocker_current_checkpoint.md`.

2026-08-28 — U16 support footprint package correction

- Replaced the nine U16 support placeholders C10-C14/R8-R11 from the local
  `PiSXMe:M1_1206` geometry with their declared standard 1206/1210/0603
  capacitor and resistor land patterns.
- No copper, zones, USB routing, PCIe routing, or schematic content changed.
- A disposable local-net trial confirms the FB, RT, and PG nets can be joined,
  but full U16 routing and TI-layout validation remain open; this is not a
  release or M6-pass claim.

2026-08-28 — bounded U16 local support routing

- Removed the package-crossing `/VPROT_12V` diagonal in the active PCB and
  added the bounded FB/RT/PG support topology from disposable trial 4.
- Added six ordinary F.Cu-to-B.Cu vias with short pad escapes and local B.Cu
  trunks; no USB data, PCIe, zones, rules, or schematic content changed.
- Native active-board DRC exceeded the bounded runtime, so this is an
  implementation checkpoint only.  M3/M6 promotion still requires native DRC,
  TI loop/thermal review, and the pin-accurate I/O architecture gate.
2026-08-28 — bounded U1 package truth correction

- Replaced the active U1 TPSM63606 placeholder land pattern with the local
  manufacturer-derived RDL0020A/B3QFN geometry, preserving the existing pad
  UUIDs and schematic net intent.
- The correction exposes the real side-pin and four-pad exposed PGND/thermal
  field required by the module package. Existing U1 copper was intentionally
  not rerouted in this checkpoint; VIN/VOUT/FB/RT/EN/PG and thermal closure
  remain open for a disposable rebuild.
- Active PCB parses balanced with no duplicate UUIDs. Native DRC remains
  non-gating and was not claimed as passing.

2026-08-28 — bounded U16 package truth correction

- Replaced the active U16 TPSM63606 placeholder land pattern with the same
  manufacturer-derived RDL0020A/B3QFN geometry used for U1, preserving U16
  pad UUIDs and correcting pad 7 to the schematic's `/VCC_INTERNAL_NC` net.
- Existing U16 copper was intentionally not rerouted in this checkpoint;
  VIN/VOUT/EN/FB/RT/PG, exposed PGND/thermal lands, and local loop geometry
  remain open for the next disposable closure trial.
- The active PCB remained syntactically balanced; native DRC is still
  non-gating and no pass is claimed.

2026-08-28 — I/O-side outline expansion steering study

- Re-read the active source after the U1/U16 package-truth prerequisites. The
  active outline is 240 x 140 mm; 220 x 140 mm is historical. No Edge.Cuts,
  connector placement, copper, zones, or manufacturing artifact was changed.
- Evaluated 250/260/270/280 mm width candidates as +10/+20/+30/+40 mm from
  the active 240 mm baseline. 250 mm is the only conditional fallback; 260 mm
  or larger has no measured routing or mating benefit in current evidence.
- Keep 240 x 140 mm for the first pin-accurate M6 replacement-I/O trial. Only
  promote 250 mm if that trial demonstrates a genuine width-limited corridor
  or mating-envelope failure after stale USB endpoint geometry and support
  placement are corrected.
- This is a planning/evidence checkpoint, not an outline promotion or M6 pass.

2026-08-28 — corrected-package U16 closure trial rejected

- Disposable `/private/tmp/u16_power_closure_trial_corrected2.kicad_pcb` used
  the manufacturer-derived U16 package and connected VIN/VOUT/EN/FB/RT/PG in
  the local support field.
- The trial still produced same-layer VIN/VOUT/EN/RT/PGOOD conflicts and
  inadequate pad-escape margin within x approximately 194.5..210 mm. It is
  rejected; the failure is local support placement/legacy-route topology, not
  a board-outline limit.
- Active source was not modified by the trial. Re-place U16 support and remove
  adjacent legacy fragments before the next closure attempt; M6 remains open.

2026-08-28 — Candidate 1 Ethernet insertion boundary

- A bounded Candidate 1 disposable attempt stopped before any topology edit.
  `/private/tmp/pisxme-v2-candidate1/PiSXMe_V2_Candidate1.kicad_pcb` is
  byte-identical to active source `8bd0d56b...`.
- The active schematic has no Ethernet nets, MagJack identity, or CM5IO-derived
  endpoint mapping. Adding proxy copper/footprints would be speculative, so
  FAST-B removal and FAST-A/SERVICE rebuild were not performed.
- Candidate 1 is therefore untested, not passed or rejected. Establish the
  schematic/net/footprint insertion boundary from official CM5IO before any
  replacement-I/O disposable mutation; M6 remains open.

2026-08-28 — U16 support replacement disposable rejected

- `/private/tmp/u16_support_replacement_trial.kicad_pcb` (SHA-256
  `f06ebda1233f9d97f694f53f7868574537a87105d9d430cd354e81ae3ac8d525`) was a
  disposable re-placement/routing trial for the corrected U16 package.
- Native KiCad 10.0.5 DRC reported 1433 violations and 172 unconnected items.
  The trial has true GND-to-USB_5V_PERIPH, PCIE_PWR_EN-to-USB_5V_PGOOD and
  VPROT_12V-to-GND shorts, plus RT/PG/FB crossings and stale FAST-B VBUS
  geometry. It is rejected and is not closure evidence.
- Active source, schematic, zones, and manufacturing outputs were unchanged.
  Rebuild the complete U16 local corridor in a fresh disposable study; do not
  infer that board-width expansion is required.

2026-08-28 — second U16 topology disposable rejected

- `/private/tmp/pisxme-u16-topology-trial-73566/PiSXMe_U16_topology_trial.kicad_pcb`
  moved U16 to `(214,130)`, removed stale local routes, and attempted a
  bounded pin-accurate support topology.
- Native KiCad 10.0.5 DRC reported 857 violations and 177 unconnected items
  (499 clearance, 35 shorting-item, 152 solder-mask bridge). PGOOD/RT/EN
  crowding, FB-to-ground-pad interference, wrong resistor-pad vias, control
  crossings, and stale-zone contamination caused rejection.
- Active source, schematic, zones, and manufacturing outputs were unchanged.
  The result confirms the need for a complete U16 local rebuild, not an
  automatic board-width expansion or M6 pass.

2026-08-28 — CM5IO Ethernet boundary extracted

- Official CM5IO maps CM5 pads 3/4/5/6/9/10/11/12 to TRD3_P, TRD1_P,
  TRD3_N, TRD1_N, TRD2_N, TRD0_N, TRD2_P and TRD0_P.
- The reference implementation uses two TPD4EUSB30 arrays, a
  TRJG0926HENL integrated-magnetics MagJack, 100 nF center-tap decoupling,
  470 ohm LED resistors, and zero Ethernet signal vias on F.Cu.
- This is a disposable insertion boundary only. PiSXMe six-layer impedance,
  shield treatment, MagJack availability, and active schematic migration remain
  open; no active source was changed.

2026-08-28 — prior Candidate 1 disposable artifacts reclassified

- Temporary Ethernet-plus-FAST-A studies exist under `/private/tmp`, including
  `pisxme_m6_candidate1_routed_plus20.kicad_pcb` (1440 violations/154
  unconnected) and `pisxme_candidate1_plus20/...io_shifted_study.kicad_pcb`
  (1234 violations/187 unconnected) from native KiCad 10.0.5 DRC.
- Their PCB-only generator inserted disposable net names/footprints without an
  active schematic hierarchy. They are failed exploratory artifacts, not
  pin-accurate promotion evidence; Candidate 1 remains unproven until a fresh
  source-bound trial passes the M6 gate.

2026-08-28 — M6 architecture-unblocker disposition

- No Ethernet replacement architecture is promoted. The official CM5IO
  Ethernet boundary is known, but no fresh Candidate 1 trial passed route,
  DRC, and mechanical gates; prior temporary studies were PCB-only and failed.
- Both U16 support-field trials were rejected by native DRC. M6 remains
  blocked, M7-M10 remain prohibited, and 240 x 140 mm remains the active
  outline baseline with 250 mm only as a measured-clearance fallback.
- Next bounded work is a complete U16 local rebuild, then a pin-accurate
  Ethernet + FAST-A + SERVICE disposable route. Candidate 2 Ethernet + internal
  SATA is allowed only if Candidate 1 fails for a demonstrated I/O pinch point.
  Active source and manufacturing outputs remain unchanged.

2026-08-28 — bounded M4 prohibited signal-via cleanup

- Removed exactly 24 signal vias whose layer pairs violated the approved layer
  policy: eight `/CM5_USB3_1_*` F.Cu-In3 vias, eight FAST-A USB2 F.Cu-In2/In1
  vias, and eight FAST-B USB2 F.Cu-In1/In2 vias. No segments, footprints,
  zones, schematic content, GND vias, or power vias were changed; the removed
  endpoints remain intentionally open for M6 reconstruction.
- Structural census after the edit: balanced PCB stream, SHA-256
  `a53e6751a59eb530afd3b522672b5ce967515710bf7eece54a5aa4242e81316e`, 400
  segments, 62 footprints, 14 zones, and 141 physical vias. All 141 are
  ordinary F.Cu-B.Cu through vias; zero signal vias reference In1/In2/In3/In4.
  Four `(vias allowed)` keepout properties are not physical via records.
- This is a narrow M4 policy correction, not an M6 route solution. USB topology
  remains blocked and no DRC or release-gate claim is made.

2026-08-28 — U16 active-source status rechecked

- The active source contains no accepted U16 local-support reroute. Earlier
  wording describing a bounded trial topology as active is superseded; the
  corresponding topology was disposable only.
- FB, RT, and PGOOD remain stale/misaligned relative to the corrected U16
  package, and the schematic wire/label truth is not aligned for a PCB-only
  patch. The latest corrected-topology disposable trial was rejected at
  1,279 DRC violations / 175 unconnected items. U16 remains open for a
  coordinated M1/M3 schematic and PCB rebuild.

2026-08-28 — fresh Candidate 1 reroute trial rejected

- Disposable `/private/tmp/pisxme-candidate1-reroute/PiSXMe_Candidate1.kicad_pcb`
  removed FAST-B and inserted CM5IO-derived Ethernet proxy footprints/routes.
- Native KiCad 10.0.5 DRC reported 1322 violations and 186 unconnected items.
  Because the trial used PCB-only proxy Ethernet nets without a matching
  schematic hierarchy and retained generic clearance/width/mask/dangling and
  shorting failures, it is rejected as promotion evidence. Active source,
  schematic, zones, and manufacturing outputs were unchanged.

2026-08-28 — coordinated U16 disposable trial rejected

- `/private/tmp/pisxme-u16-coordinated/PiSXMe_U16_trial.kicad_pcb` used a
  coordinated support-field placement and pin-accurate escapes. Native KiCad
  10.0.5 DRC reported 1346 violations and 182 unconnected items.
- Target-net inspection still found PGOOD/FB/RT/EN/VIN/VOUT crossings and
  shorts with adjacent pads and stale zones. The trial was rejected; no active
  source or schematic change was accepted.

2026-08-28 — M6 checkpoint terminology corrected

- Corrected the M6 USB checkpoint's stale U6/U10 description: the active
  TPD4E05U06 flow-through footprints have 10 pads, with USB3 on 1/2/4/5,
  GND on 3/8, and NC on 6/7/9/10. This documentation correction does not
  change the active PCB or schematic and does not alter the M6 gate.

2026-08-28 — M6 architecture checkpoint stale active-route wording corrected

- Reinspection of the active PCB confirms that the U16 FB/RT/PG reroute
  described in older follow-up paragraphs is not present in the active source.
  Those paragraphs are superseded; U16 remains open for a coordinated
  schematic/PCB rebuild.
- The active-source copper correction after the package prerequisites is the
  bounded M4 removal of 24 prohibited plane-layer signal vias, yielding PCB
  SHA-256 `a53e6751a59eb530afd3b522672b5ce967515710bf7eece54a5aa4242e81316e`.

2026-08-29 — M6 continuation: proxy architecture trials remain rejected

- A native KiCad 10.0.5 check of disposable
  `/private/tmp/pisxme_candidate1_trial.kicad_pcb` reported 1326 violations
  and 185 unconnected items. The copy removed FAST-B and inserted Ethernet
  proxy nets/footprints without a matching schematic hierarchy; it is not
  promotion evidence.
- Disposable Candidate 2
  `/private/tmp/pisxme_candidate2_eth_sata_260.kicad_pcb` remains a placement
  proxy: Ethernet and SATA pairs are unrouted, the JMS578 and M.2 objects are
  not vendor-verified, and the underside mechanical envelope is unvalidated.
- Active source remains unchanged except for the bounded U16 schematic label
  correction; PCB SHA-256 remains
  `a53e6751a59eb530afd3b522672b5ce967515710bf7eece54a5aa4242e81316e`, and
  schematic SHA-256 is
  `d31ff8e96fd1df211f5528f0b4c70f8b7a7891d68383d4561bfae83116bf5bbb`.
- No Ethernet/SATA architecture or +20 mm outline is promoted. M6 remains
  open pending a source-bound, pin-accurate replacement-I/O trial.

2026-08-29 — final disposable U16 trial rejected

- `/private/tmp/u16_final_disposable_20260828_v3` connected U16 FB/RT/PG but
  native KiCad 10.0.5 DRC still reported 824 violations, 163 unconnected
  items, 337 schematic-parity issues, 15 shorting-item violations, and 2 track
  crossings. PGOOD-to-ground and RT/EN local conflicts remain.
- The trial is disposable only; active PCB SHA-256 remains
  `a53e6751a59eb530afd3b522672b5ce967515710bf7eece54a5aa4242e81316e` and no
  active PCB, manufacturing output, branch, or commit was changed.

2026-08-29 — no-zone U16 isolation trial rejected

- `/private/tmp/u16_final_disposable_20260829_v4` removed zones and stale local
  U16 copper to isolate support-field geometry. Native KiCad 10.0.5 DRC found
  249 violations, 418 unconnected items, and 337 schematic-parity issues; the
  unconnected count is expected for a zone-free copy.
- FB was clean, but RT retained two crossings and PGOOD retained five real
  violations, including shorts to U16 ground pad 18/ground via and PGOOD/RT
  corridor crossings. The trial is rejected; active PCB remained unchanged.

2026-08-29 — Candidate 1 +20 mapping follow-up remains unproven

- `/private/tmp/pisxme_candidate1_260_mapping.kicad_pcb` assigned the official
  CM5IO Ethernet pad mapping and placed two ESD arrays plus a MagJack after
  removing FAST-B, but added no Ethernet copper. The +20 mm outline improved
  MagJack edge/cable placement without materially widening the CM5-to-ESD
  pinch point. This is placement/net-mapping evidence only; no routability or
  promotion claim is made.
- A fresh native KiCad 10.0.5 DRC of disposable
  `/private/tmp/pisxme_candidate2_eth_sata_260.kicad_pcb` reported 1111
  violations and 114 unconnected items. Because it remains a proxy study with
  no meaningful routed Ethernet/SATA topology, it is rejected and cannot
  justify architecture promotion.

2026-08-29 — Candidate 1 routed +20 follow-up rejected

- `/private/tmp/pisxme_m6_candidate1_routed_plus20.kicad_pcb` removed FAST-B and
  added temporary CM5IO-derived Ethernet routes on a 260 x 140 mm copy.
- Pair lengths were TRD0 20.31/20.49 mm, TRD1 22.93/26.50 mm, TRD2
  24.65/25.02 mm, and TRD3 27.57/28.56 mm; TRD1 and TRD3 used two signal
  vias per conductor.
- The route contained 44 Ethernet segments, 20 crossing instances, and 15
  unique cross-net pair combinations. It is rejected; +20 mm did not cure the
  fanout without a restructured ESD placement/topology.

2026-08-29 — current U16 support graph is present but unvalidated

- Direct current-PCB inspection (SHA-256
  `a53e6751a59eb530afd3b522672b5ce967515710bf7eece54a5aa4242e81316e`) finds
  six segment records each for `/USB_5V_PERIPH_FB`, `/USB_RT_1MHZ`, and
  `/USB_5V_PGOOD`, with F.Cu/B.Cu transitions and vias.
- Older wording that these active nets were absent is superseded. Their graph
  is **CONNECTED BUT UNVALIDATED** because active-board native DRC did not
  complete and support, plane, thermal, and parity signoff remain open.

2026-08-29 — Mac-side execution paused for Linux tooling handoff

- No M6 implementation was resumed. The active Rev A source remains unchanged;
  the current blocker is the missing proof that schematic-authoring tooling can
  produce authoritative KiCad 10 connectivity and source-derived PCB nets.
- The approved I/O direction for the next M6 attempt is native CM5 Gigabit
  Ethernet, internal JMS578 USB3-to-SATA with a SATA-only M.2 socket, and
  SERVICE USB2 recovery; the legacy external FAST USB routes are not to be
  restarted.
- Mac-side `kicad-sch-api`/SKiDL experiments remain evidence only. The next
  gate is reproducible Linux installation and flat, hierarchy, custom pin-map,
  and schematic-to-PCB authority fixtures before any PiSXMe source edit.
- Handoff documents and durable evidence are in `HANDOFF_LINUX_WORKSTATION.md`,
  `TOOLING_STATUS.md`, `references/REFERENCE_INDEX.md`,
  `plans/M6_LINUX_RESTART_CHECKLIST.md`, and `validation/m6/`.

2026-08-29 — public recovery repository handoff

- A public preservation repository is being created from the locally recovered,
  byte-verified active source and readable tooling/evidence. The original
  iCloud-backed checkout contains File Provider dataless placeholders, so the
  publication includes an explicit `RECOVERY_MANIFEST.md` rather than guessing
  or fabricating unavailable files.
- This is a documentation/recovery publication only; no M6 implementation,
  PCB, schematic, manufacturing artifact, or Git history in the active checkout
  is being changed.

2026-08-29 — Mac recovery material integrated on NYX

- Verified all 208 entries in `/srv/pisxme-recovery/SHA256SUMS`, then copied the
  recovered project-shaped tree additively into the NYX checkout on
  `recovery/mac-import-20260829`. All 39 pre-existing tracked overlaps were
  byte-identical, so no recovered file displaced differing repository content.
- Restored the recovered bridge, tests, tooling, design and validation evidence,
  active project rule file, and all 30 custom footprint files. The authoritative
  schematic, PCB, project, and symbol-library bytes remain unchanged from the
  handoff baseline.
- Preserved `conflicts/mac-materialized-20260829/` as an archive rather than
  promoting its variants. Two AppleDouble metadata blobs and one zero-byte
  temporary file were quarantined under
  `conflicts/mac-recovery-artifacts-20260829/`; the staging recovery remains
  untouched.
- The canonical `design/COMPONENT_SOURCING_REALITY_V2.md` recovered as zero
  bytes, while a non-empty differing copy remains in the conflict archive. No
  authority choice was inferred; deliberate provenance review is still required.
- Native KiCad 10.0.5 parsed the recovered active schematic and board. Netlist
  export succeeded; baseline validation reported 94 ERC violations, 803 DRC
  violations, and 182 unconnected items, consistent with the documented open
  design debt rather than a recovery parse failure.
- A dedicated `/home/nyx/venvs/pisxme-bridge` Python 3.11 environment contains
  the four pinned bridge dependencies and pytest. With the KiCad Flatpak Symbols
  extension exposed through `KICAD_SYMBOL_DIR`, 11 of 12 recovered tests passed.
  The remaining test is non-portable because it hard-codes the Mac path
  `/Users/Cooper/Documents/ChatGPT/sxm2`; recovered source was not rewritten in
  this import to conceal that defect.
- The existing external disposable toolchain validator was rerun after import:
  `pcbnew` load/save and source-defined pad-net mapping passed, native ERC and DRC
  both reported zero violations, and KiCad generated 13 Gerbers plus one Excellon
  drill file. Those outputs remain outside the repository under
  `/home/nyx/pisxme-toolchain-environment/fixture/`.

2026-08-29 — clean Rev A rebuild plan approved

- Recorded the approved clean-rebuild program in
  `Approved Plans/PiSXMe_RevA_Clean_Rebuild_Plan.md`.
- The plan freezes the recovered `pisxme/PiSXMe.*` design as
  `LEGACY_DONOR_REFERENCE` and establishes `pisxme/reva-clean/` as the only new
  implementation path. It also requires the isolated `PiSXMeRevAClean` library
  namespace, evidence-based CM5 orientation selection, acreage validation before
  compression, and routing plus assembly-complexity rejection gates.
- This checkpoint records planning authority only. No legacy schematic, PCB,
  footprint, rule, routing, zone, or manufacturing source was modified.

2026-08-29 — clean Rev A Phase 0 recovery checkpoint validated

- Preserved the 172-file, checksum-verified recovery import in commit
  `8e6d029` before any portability change; `/srv/pisxme-recovery/SHA256SUMS`
  reports 208/208 entries OK, including the 30 custom footprint files.
- Created the clean-rebuild branch from that import and made the bridge path
  containment test portable with a temporary host-local root. The recovered
  bridge/backend/integration suite is now 12/12 passing under Python 3.11 with
  KiCad Flatpak symbols exposed.
- KiCad 10.0.5 native legacy parse remains reproducible at 94 ERC violations,
  803 DRC violations, and 182 unconnected items; these are frozen baseline
  evidence, not clean-design acceptance. The disposable SKiDL/PCB fixture
  generated a zero-violation native DRC report, 25 Gerber files, and one
  Excellon drill file; outputs remain outside the repository.
- No legacy design source was edited. Phase 0 is accepted on the private
  checkpoint branch pending the private push and recovery tag.

2026-08-29 — clean Rev A Phase 1 donor extraction validated

- Added `pisxme/reva-clean/donor-extraction/PHASE1_DONOR_MANIFEST.md` with
  KEEP, FIX_WHILE_TRANSPLANTING, and DISCARD dispositions for PCIe/SXM2,
  mechanics/cooling, CM5/I/O, storage/SERVICE, power/protection, regulators,
  footprints, and rules.
- Added `PHASE1_RECONCILIATION_RECEIPT.md` with the frozen legacy hashes,
  current-source geometry census, and explicit treatment of stale via/count and
  footprint-audit records. No legacy source or routed geometry was promoted.
- Phase 1 gate is `PASS_WITH_EXPLICIT_FIX_QUEUE`; exact authority closure,
  independent clean-library validation, and undocumented V100 behavior remain
  later gates by design.

2026-08-29 — clean Rev A Phase 2 authority inventory bounded

- Materialized the official Raspberry Pi CM5IO Rev 2 archive under
  `pisxme/reva-clean/authority-inventory/cm5io-rev2/` (30 files; source ZIP
  SHA-256 `48b14a...b59496b`) and native-parsed its schematic under KiCad
  10.0.5. The reference board parsed with 76 DRC violations and 0 unconnected
  items; this is upstream observation only.
- Materialized primary CM5IO, JMS578, TI power/protection/high-speed, and V100
  documents with recorded hashes. JMS578’s primary brief confirms the bridge
  family and UASP but does not close firmware, package procurement, or Linux
  behavior.
- Added `PHASE2_AUTHORITY_INVENTORY.md`. Phase 2 remains
  `BLOCKED_PENDING_EXACT_AUTHORITIES` for the exact B-key socket, SXM2
  land-pattern overlay, cooler/backplate, Ethernet ESD selection, selected
  current JLC stackup, and remaining bridge/procurement evidence. No clean
  schematic or PCB synthesis was started.

2026-08-29 — clean Rev A Phase 2 authority closure sprint disposition

- Replaced the preliminary Phase 2 inventory with an authority-by-authority
  disposition and added `PHASE2_PROCUREMENT_MATRIX.md`.
- Closed the JAE B-key SATA M.2 socket authority, TI TPD4E004DRYR Ethernet ESD
  choice, Amphenol 74221-101LF connector identity, and current JLC06161H-7628
  six-layer/impedance basis. Added local source receipts for M.2, SXM2,
  mechanics, Ethernet ESD, JMS578, and JLC calculator evidence.
- Classified the proprietary V100 cooler/backplate envelope and unverified
  local SXM2 land-pattern transplant as explicit `REV_A_EMPIRICAL_RISK`.
- JMS578 was rejected after the out-of-stock LCSC listing and incomplete
  firmware/Linux evidence failed the approved gate. TI `TUSB9261IPVP` is now
  the selected replacement: active exact DigiKey/Mouser stock, TI firmware
  resources and FlashBurner, implementation/EVM documentation, and explicit
  USB/SATA/reset behavior. Phase 2 is closed; the TI firmware download receipt
  records the export-gated binary resources and the remaining Phase 7 Linux
  qualification tests. No Phase 3 schematic or PCB was modified.

2026-08-30 — Phase 2 closure evidence strengthened and Phase 3 held

- Added the locally captured exact JAE `SM3ZS067U410` drawing and current JLC
  impedance-template API response for `JLC06161H-7628`, including hashes and
  the exact API request fields. Reframed the JLC record correctly: Phase 2
  closes the current stack/target basis; Phase 13 owns returned route geometry
  and fabrication coupon evidence.
- Added `PHASE2_CLOSURE_RECEIPT.md`, which explicitly classifies only the
  cooler/backplate, SXM2 legacy land-pattern transplant, and unavailable exact
  CM5IO MagJack as `REV_A_EMPIRICAL_RISK`; no obtainable drawing, calculator
  source, or procurement question is hidden under that label.
- Removed an unvalidated Phase 3 scaffold created before this evidence review.
  The clean schematic, PCB, project, and libraries remain absent; Phase 3 is
  not started until the strengthened authority checkpoint is independently
  re-audited.

2026-08-30 — Phase 3 architecture scaffold started

- After the strengthened Phase 2 checkpoint, created the native
  `PiSXMe_RevA_Clean` project shell with exactly the ten plan-defined child
  sheets, isolated `PiSXMeRevAClean` library tables, and architecture,
  interface, net-class, and source-authority ledgers.
- The scaffold is intentionally not a production schematic: child-sheet pins,
  real block connectivity, selected local assets, pin/pad parity, and a
  schematic-derived PCB fixture remain open. No placement or routing was
  introduced, and the legacy donor remains immutable/reference-only.

2026-08-30 — Phase 3 native scaffold receipt

- Generated the native `PiSXMe_RevA_Clean` root plus exactly ten named child
  sheets from a local deterministic scaffold generator. KiCad 10.0.5 plotting
  and root parsing complete under Xvfb; namespace and machine-path scans are
  clean outside frozen evidence.
- This is not a Phase 3 pass: ERC reports 78 expected unconnected scaffold
  interfaces, and no production symbols, footprints, components, PCB,
  placement, routing, or parity fixture exists. The receipt records the open
  gate and required next work.

2026-08-30 — removed disposable SKiDL probe logs

- Removed the untracked `skidl.erc` and `skidl.log` files created by an
  exploratory environment probe; they were not design evidence or project
  outputs.

2026-08-30 — Phase 3 hierarchy gate blocked

- Audited the clean root and ten child sheets with KiCad 10.0.5. Native ERC
  remains at 40 root-only hierarchy violations while all child sheets load
  without hierarchy errors.
- Tested the documented root/sheet and child-symbol instance-path forms,
  including project `instances` records; none produced a passing association.
  The clean hierarchy is therefore blocked at the earliest Phase 3 gate and
  no later phase, placement, routing, or PCB artifact was introduced.
- Unblock requires a native KiCad-authored saved root/child association or a
  reproducible installed KiCad authoring route. This is a blocker receipt, not
  a validated checkpoint.

2026-08-30 — Phase 3 native hierarchy association closed

- Reproduced the root hierarchy failure with KiCad 10.0.5 and isolated the
  cause: the generated contract symbol was appended after the child
  `(lib_symbols)` section, making each child unloadable and presenting as root
  `hier_label_mismatch` errors.
- Corrected the generic authoring path by inserting each contract definition
  inside `(lib_symbols)`, using KiCad's native inverted library Y coordinates,
  and generating real root wires to every sheet pin.
- Native KiCad 10.0.5 root ERC now reports zero violations across all ten
  children. Added `validation/phase3/test_native_hierarchy_authoring.py`;
  generation, serialization assertions, and native ERC all pass. No
  placement, routing, PCB, or Phase 4 work was introduced.
- Regenerated the contract instances with deterministic per-sheet references
  (`X_CORE_CM5`, `X_V100_PCIE`, and so on); hierarchy regression and native ERC
  remain passing after the netlist-reference cleanup.

2026-08-30 — Phase 3 architecture gate closed

- Added a generic EDAC extraction rule that removes donor-only shield pins
  19/20 because the selected A70-112-331N126 manufacturer layout defines
  P1–P18 as electrical contacts and shield features as mechanical NPTH.
- Added machine-readable parity evidence: CM5 200/200 and EDAC 18/18;
  native reopen/ERC, non-empty KiCad XML netlist, clean namespace/path scan,
  and zero PCB-only/proxy nets by construction all pass.
- Recorded `PISXME_REVA_CLEAN_PHASE3_CLOSED` in the Phase 3 exit receipt.
  No placement, routing, PCB, or Phase 4 work was introduced by this gate.

2026-08-30 — strengthened Phase 3 parity evidence

- Added a disposable native-format schematic-to-PCB parity fixture and
  regression test proving PCB-only/proxy nets are rejected at the architecture
  boundary while the clean project remains PCB-free.

2026-08-30 — Phase 4 SXM2 authority isolation started

- Added a project-local SXM2 symbol/footprint extraction and a lane-0 mapping
  receipt for Amphenol `74221-101LF` Rev-W. The 400-pad land pattern remains
  explicitly `REV_A_EMPIRICAL_RISK`; no placement or routing was introduced.

2026-08-30 — Phase 4 V100 lane-0 schematic gate closed

- Added the schematic-only V100 island: lane 0 PER0/PET0, two transmitter-side
  PET0 coupling capacitors, REFCLK, PERST, and the documented SXM2 contacts.
- Added the machine-readable Phase 4 audit and receipt. Native KiCad reopen
  and ERC pass with zero violations; no PER1+, x16, NVLink, switch, or
  redriver baggage exists. No placement or routing was introduced.

2026-08-30 — Phase 5 power architecture gate closed

- Added schematic-only dual LM74700 protected inputs, protected 12 V merge,
  CM5 5 V, TUSB9261 3.3/1.1 V rail contracts, and the V100 power contract.
- Added the machine-readable power audit and receipt; native KiCad ERC passes
  with zero violations. No PCB placement or routing was introduced.

2026-08-30 — Phase 6 Ethernet schematic gate closed

- Added the four-pair CM5IO-derived Ethernet island with EDAC
  `A70-112-331N126` and TI `TPD4E004DRYR` connector-boundary ESD.
- Added the Ethernet audit and receipt; native KiCad ERC passes with zero
  violations. No placement or routing was introduced.

2026-08-30 — Phase 7 storage schematic gate closed

- Added schematic-only CM5 USB3 to TI TUSB9261IPVP to SATA to JAE B-key M.2
  storage connectivity, with dedicated bridge rails/reset/config contracts.
- Added the storage audit and receipt; native KiCad ERC passes with zero
  violations and NVMe/USB2 SERVICE paths are excluded.

2026-08-30 — Phase 8 SERVICE schematic gate closed

- Added the USB2 UFP service connector, boundary ESD, host VBUS sense, and
  two 5.1 kOhm Rd resistors; source/DRP/SuperSpeed circuitry is excluded.
- Added the SERVICE audit and receipt; native KiCad ERC passes with zero
  violations. No placement or routing was introduced.

2026-08-30 — Phase 9 mechanical envelope gate closed

- Added clean V100 cooler/backplate and M.2 2280 retention envelopes plus
  SXM2 courtyard audit. Proprietary/uncaptured 3D remains explicitly
  empirical risk; no donor model was promoted as exact authority.

2026-08-30 — Phase 10 orientation study closed

- Added native topside and underside CM5 placement-study boards with V100,
  SXM2, M.2, and cooler anchors; both contain zero routing.
- Selected the underside-CM5 candidate for Phase 11 floorplanning, subject to
  later mating and assembly review.

2026-08-30 — Phases 11/12 acreage floorplan closed

- Added a native 300 x 180 mm no-routing acreage floorplan with central V100
  reservation, edge power/service neighborhoods, Ethernet/storage zones, and
  M.2 service envelope.
- Corrected inherited CM5/M.2 conflicts and recorded the remaining SXM2/
  cooler 2D courtyard overlap as intentional vertical stacking requiring
  physical confirmation.

2026-08-30 — Phase 13 current JLC stack finalized

- Exercised the current public JLCPCB calculator with the exact six-layer
  `JLC06161H-7628` template and saved the selected-template capture plus
  inverse-calculation evidence for 90-ohm and 100-ohm differential targets.
- Released 5.2 mil width / 8 mil pair spacing as the Rev-A starting constraint,
  with ordinary through vias, adjacent L2/L5 GND references, and mandatory
  fabrication coupon verification. No fabricated-board result is implied.

2026-08-30 — Phase 14/15 entry checkpoint rehydrated

- Replayed the deterministic clean authoring pipeline after the Phase 3
  regression test exposed that its fixture-generation step intentionally
  rebuilds downstream child sheets. Reapplied the SXM2/V100 lane-0 and PET0
  coupling authoring path, then reran the Phase 4–11 audits.
- Native root ERC with error severity reports zero violations; no power or
  signal routing has been claimed or started by this checkpoint.

2026-08-30 — Phase 3 regression harness isolation corrected

- The hierarchy generator is now exercised in a disposable copy while native
  ERC checks the live clean project. This prevents validation from erasing
  downstream island authoring and preserves the Phase 4 audit contract.

2026-08-30 — Phase 14/15 footprint prerequisite started

- Added a deterministic exact-MPN package-footprint assignment path for the
  selected LM74700QDBVRQ1, TPSM63606RDLR, TUSB9261IPVP, and TPD4E004DRYR
  instances, plus a machine-readable pad-count audit.
- Kept Phase 14/15 open because connector/socket land patterns and complete
  pin-to-pad authority are still required before real routed copper.

2026-08-30 — Phase 14 JAE B-key socket pattern derived

- Derived the selected JAE `SM3ZS067U410ABR1000` B-key footprint from the
  dimensioned drawing and SATA-IO TP053 by placing the eight-position void at
  physical positions 12–19. The clean STORAGE instance now references the
  project-local 67-contact pattern and the extraction regression passes.
- This does not close the full routing gate; SXM2 and remaining connector
  land-pattern authority still require independent review.

2026-08-30 — Phase 14 SXM2 authority comparison refreshed

- Rechecked Amphenol's current product authority for `74221-101LF`: active,
  400-position, 1.27 mm array, 4 mm height, and current distributor stock.
- Compared the clean 400-pad/40 x 10/1.27 mm pattern to the released Rev-W
  metadata. Mask, paste, and A1 details remain explicit empirical risk because
  the manufacturer CDN blocks local drawing capture; no exact ECAD promotion or
  routing was performed.

2026-08-30 — Phase 14 M.2 socket sub-gate closed

- Updated the M.2 authority receipt to reference the clean JAE B-key footprint
  and its 67-pad/12–19-void regression evidence. The overall routing gate
  remains open pending remaining connector patterns and complete pin-pad review.
2026-08-30 — Phase 14 USB-C service connector authority closed

- Promoted Amphenol `10171746-00021LF` as the exact USB2 SERVICE receptacle.
- Added manufacturer-derived local footprint, exact MPN assignment, procurement
  receipt, and regression test; native root ERC remains clean.

2026-08-30 — Phase 14 SERVICE ESD and passive footprint authority closed

- Assigned TI `TPD2EUSB30DRTR` to the project-local Texas DRT-3 three-pad
  footprint using the documented 1.0 x 0.8 mm / 0.7 mm-pitch package geometry.
- Corrected the generic service authoring path so the old USB-C connector
  footprint cannot leak onto the ESD or Rd resistors; both Rd parts now use a
  separate project-local 0402 footprint.
- Added exact-MPN regression coverage; the clean root native ERC remains zero.

2026-08-30 — Phase 14 materialization exposed two authoring defects

- Added a native pcbnew materialization harness for a disposable six-layer
  candidate; it imports 17 assigned components and 78 netlist nets without
  mutating the floorplan.
- Corrected Ethernet ESD to two six-pin TI TPD4E004DRYR devices, covering all
  four MDI pairs, and corrected the two bridge supply rails from mistaken
  TUSB9261 placeholders to TPSM63606RDLR modules.
- Native root ERC returned zero after both corrections. SXM2 abstract PWR/GND
  contact assignment remains explicitly open pending authoritative pinout.
2026-08-30 — Native CM5 authority promoted and acreage materialization corrected

- Promoted the authoritative Raspberry Pi CM5 two-unit, 200-pin symbol into
  `CORE_CM5.kicad_sch`, preserving exact pin names/numbers and marking only
  unmapped interface pins no-connect. Native KiCad 10 ERC is zero.
- Added a regression fixture for the two-unit native CM5 authoring path and
  corrected the pcbnew materializer for KiCad UTF8 identifiers. The candidate
  now materializes all 20 schematic components and 218 nets on six copper
  layers; the sole intentional unresolved contact mapping is SXM2 J1 PWR/GND,
  retained as the documented Rev-A empirical-risk item.

2026-08-30 — Phase 5 power gate made fail-closed

- Corrected the Phase 5 receipt to `IN_PROGRESS`: native ERC and MPN presence
  do not prove the required LM74700 external MOSFET/VCAP path or TPSM63606
  20-pin support network.
- Strengthened the power audit so it requires package-pin evidence and the
  documented fuse/MOSFET support components before Phase 5 can pass.

2026-08-30 — Phase 5 power implementation contract recorded

- Added `PHASE5_POWER_NETWORK_SPEC.md` from the preserved LM74700-Q1 and
  TPSM63606 datasheets, including exact pin maps, external FET/fuse/TVS
  topology, regulator support requirements, and the pre-routing acceptance
  gate.
- Corrected the Molex authority receipt to record that its project-local
  land pattern is now materialized; this does not close the separate circuit
  completion gate.

2026-08-30 — Phase 5 fuse authority gap closed

- Added current Littelfuse authority and procurement evidence for the separate
  `0297015.U` 15 A MINI blade fuse and `178.6165.0001` four-hole PCB holder.
- Kept the electrical rating, I2t, derating, inrush, and holder land-pattern
  integration explicitly open for the Phase 5 circuit gate; the parts are not
  collapsed into a fictitious two-pad component.

2026-08-30 — ROOT_HIERARCHY_ASSOCIATION continuation closed

- The native KiCad fixture remained green, and the clean CM5 promotion was
  corrected to parse the authoritative two 100-pin units independently.
- Clean-root KiCad 10 ERC is zero with J7 present; native netlist export and
  pcbnew materialization now include the 200-pin CM5 footprint. Phase 3 status
  records the generic authoring-path correction and regression test.

2026-08-30 — Phase 5 power network and calculation gate closed

- Completed the native dual-input LM74700/CSD19536KCS/SMBJ18A protection
  networks and all three TPSM63606 support networks, including the 1.1 V
  divider and sixteen 22-uF output capacitors. Native ERC and the XML netlist
  audit pass with the protected rail handed to SXM2 J1.A3.
- Added reproducible design-envelope calculations. Corrected the worksheet's
  low-voltage input arithmetic to 2.10 A, making the total 25.25 A and equal
  branch envelope 12.625 A; a single branch is explicitly over the 15 A fuse
  envelope. Sharing, copper, thermal, and exact ceramic DC-bias confirmation
  remain binding `REV_A_EMPIRICAL_RISK` constraints for later gates.
- Added native bridge round-trip regression coverage and local project
  footprints/support authority for the newly represented power components.

2026-08-30 — Phase 3/SXM2 hierarchy and materialization correction

- Corrected the native SXM2 symbol row orientation and separated overlapping
  root V100/STORAGE sheet-pin wires; KiCad 10 netlist export now preserves the
  intended A2/A3, E7/F7, G1/G2, and E18 mappings with zero native ERC errors.
- Added the explicit, non-authoritative reverse-engineered SXM2 endpoint power
  map to disposable PCB materialization: 130 protected-power and 70 ground
  contacts, with stale donor pad nets cleared before assignment.
- Added `test_phase14_sxm2_power_aliases.py` and updated the Phase 5 audit to
  test logical J1.PWR rather than misidentifying signal contact A3 as power.

2026-08-30 — Phase 14 power-route candidate and V100 return-net correction

- Corrected the V100 endpoint return to the shared global `POWER_GND` net and
  verified native KiCad ERC remains zero; the prior isolated V100 ground net
  could not support a valid board return plane.
- Added `phase14_power_route.py`, a disposable candidate generator with a
  broad protected-feed zone and filled inner return-reference planes, plus a
  machine-checkable Phase 14 candidate regression.
- Kept Phase 14 open: filled-zone geometry, current density, voltage drop,
  branch sharing, contact current, thermal margin, and hostile DRC evidence
  remain required before routing closure.

2026-08-30 — Phase 14 candidate artifact checkpoint

- Committed the generated `ACREAGE_POWER_PHASE14.kicad_pcb` alongside its
  deterministic generator and regression so the filled-zone candidate is
  reproducible from the validated materialized board.

2026-08-30 — Phase 14 power-return continuity verified

- Promoted the clean V100 return and dual 12 V input returns onto shared
  global `POWER_GND`; native netlist and Phase 5 regression now require J1.GND,
  both input headers, and both LM74700 grounds on that net.
- Refreshed the Phase 14 filled candidate after the return-net correction.

2026-08-30 — Phase 14 filled-copper analysis added

- Added geometry sampling of the filled V100 protected-feed polygon and
  conservative 1 oz copper current-density/sheet-resistance calculations.
- The candidate reports 99.5 mm sampled minimum span, 3.681 A/mm2 shared
  branch density, 8.31 A/mm2 worst continuous single-branch density, and 10.89 mV
  conservative drop bound; connector-contact, thermal, and full-board DRC
  closure remain open.

2026-08-30 — Phase 14 connector-contact bound added

- Added the balanced-feed contact calculation: 12.625 A per branch across 65
  empirical power contacts is 0.194 A/contact, below Amphenol's published
  0.45 A/contact rating. Continuity and current-sharing measurements remain
  required for final Phase 14 closure.

2026-08-30 — Phase 14 thermal bound added

- Added the CSD19536KCS datasheet 62 C/W junction-to-ambient bound to the
  geometry-backed power analysis. At 40 C ambient it estimates 66.7 C shared
  branch junction and 146.7 C single-branch fault junction, below 175 C; the
  result remains a test-board/design bound pending fabricated-board thermal
  and sustained-sharing measurements.

2026-08-30 — Phase 14 provisional branch-track rejection

- DRC caught provisional wide branch legs crossing adjacent fuse-holder,
  connector, CM5, and regulator pads in the acreage placement. Those tracks
  were removed; the candidate retains only the validated filled power/return
  zones and remains unrouted until a clearance-safe production placement is
  established.

2026-08-30 — Phase 14 canonical power-budget correction

- Rebased the Phase 14 geometry/contact/thermal analysis on the repository
  `design/FINAL_POWER_BUDGET.json` authority: 28.5 A continuous and 34.3 A
  peak across two 15 A branches.
- Balanced continuous operation estimates 14.25 A/branch, 0.219 A/contact,
  and 78.3 C FET junction at 40 C ambient. The 34.3 A single-branch case is
  explicitly a fuse-clearing transient, not a sustained thermal pass.

2026-08-30 — Phase 14 canonical-budget arithmetic corrected

- Corrected the machine analysis to the exact 1 oz geometry arithmetic:
  4.155 A/mm2 shared density, 8.309 A/mm2 continuous single-branch density,
  10.91 mV sheet-drop bound, and 74.0 C shared FET junction at 40 C ambient.
- The 236.9 C peak single-branch θJA result remains a fuse-clearing transient
  requirement, not an accepted sustained operating condition.

2026-08-30 — Phase 14 routing candidate held fail-closed

- A second B.Cu/ordinary-via routing experiment was rejected after native DRC
  showed pad/hole crossings and the KiCad Python ABI serialized two protected
  vias with the wrong hierarchical net. The canonical candidate is therefore
  zone-only with zero tracks/vias until a clearance-safe production placement
  and stable net-assignment path are available.

2026-08-30 — Phase 14 Molex land-pattern defect found

- Native DRC showed the local `0039300020` pattern's 3.0 mm mounting holes
  overlapping the 2.4 mm electrical-hole clearance envelope. The electrical
  MPN selection remains valid, but its local land pattern is reopened against
  the official Molex drawing and is excluded from routing/release authority.

2026-08-30 — Phase 14 Molex land-pattern authority corrected

- Replaced the incorrect horizontal 4.20 mm/two-peg local pattern with the
  Molex SD-5569-002 2-circuit component-side layout: pad 1 at (0,0), pad 2
  at (0,+5.50), and one NPTH retention peg at (0,-7.30); electrical and peg
  drills are 1.80 mm and 3.00 mm.
- Added a focused native DRC regression for J5/J6. Fresh materialization and
  routing-candidate DRC no longer report Molex self-hole or solder-mask bridge
  violations; the broader acreage candidate remains Phase 14-open.
- Corrected the local authority provenance to the exact MPN drawing
  `039300020_sd.pdf` / `55690002-SD` and forced the materializer to reload
  J5/J6 from the project-local footprint rather than stale donor geometry.

2026-08-30 — Phase 14 Littelfuse holder land-pattern gap found

- Native DRC exposed overlapping local geometry in the selected four-pin
  `178.6165.0001` holder footprint at F1/F2. The electrical selection remains
  valid, but the local pattern is reopened against Littelfuse `CVP-PE40-0006`.
- The manufacturer drawing's 5.8 mm and 3.5 mm hole-pattern dimensions are
  now recorded as the land-pattern authority; routing and release remain held
  until the local footprint is regenerated and independently checked.

2026-08-30 — Phase 14 Littelfuse holder geometry corrected

- Corrected the local `178.6165.0001` four-pin holder to the manufacturer
  `CVP-PE40-0006 Rev A` 5.8 mm by 3.5 mm hole rectangle with 1.4 mm drills.
- Materialization now assigns duplicated contacts 1/3 to each input net and
  2/4 to each fused-output net. Native DRC removes the holder self-overlap;
  external placement/courtyard interactions remain open.

2026-08-30 — Phase 14 Littelfuse eight-hole authority correction

- Independent exact-MPN review found that `178.6165.0001` is an eight-solder-hole
  FLR holder with a central mechanical spigot, not a four-hole pattern.
- Regenerated the local footprint at the manufacturer-derived coordinates with
  conservative central NPTH clearance; materialization maps pads 1-4 to input
  and 5-8 to fused output. Phase 14 remains open pending broader DRC and power
  validation.

2026-08-30 — Phase 14 power escape and mechanical correction

- Moved both ideal-diode MOSFETs outside the conservative V100 cooler
  reservation and kept the protected feed as a broad F.Cu corridor.
- Added a clearance-safe stepped B.Cu escape for J6 around its adjacent return
  contact and the CM5 service connector. Fresh native DRC has no power-route
  shorting item; broader regulator/control unrouted debt remains open.

2026-08-30 — Phase 14 power-path gate closed

- Frozen candidate passed current-density, voltage-drop, balanced branch,
  connector-contact, conservative thermal, no-single-neck, and focused native
  power DRC checks. The focused report has no power-path short, mask bridge,
  hole-clearance, or clearance defect.
- Closed Phase 14 for design purposes with `REV_A_EMPIRICAL_RISK` retained only
  for continuity of the public reverse-engineered 130/70 V100 contact map and
  later fabricated-board thermal/bring-up confirmation. Broader acreage DRC
  and unrouted control debt remain later validation work.

2026-08-30 — Phase 15 TPSM63606 package authority corrected

- TI RDL0020A layout review found the clean footprint had its PGND/thermal
  lands on the perimeter instead of using the four central pads 17-20.
- Promoted the datasheet-derived 1-16 perimeter plus four central thermal-land
  geometry into the clean namespace and added regression coverage. Regulator
  routing remains unstarted until the vendor-layout overlay is implemented.

2026-08-30 — Phase 15 first routing prototype rejected

- A straight-line fanout prototype was tested on an isolated Phase 15 board.
  Native DRC exposed real cross-net shorts from the long direct segments and
  compact placement; the prototype was deleted and no DRC relaxation was made.
- The Phase 14 artifact was regenerated against the corrected TPSM footprint;
  Phase 15 must restart with layer-aware local loops and deliberate return vias.

2026-08-30 — Phase 15 thermal-via base checkpoint

- Added four 0.50/0.30 mm ordinary through vias per TPSM63606, centered in
  the four TI RDL0020 central PGND lands, with same-net F.Cu links across the
  separate exposed lands.
- Native save/reload regression passes for all 12 exact `/REGULATORS/POWER_GND`
  vias. Fresh native DRC reports no thermal-via diameter, drill, annular,
  mask, short, or dangling-via defect; VIN/VOUT and control routing remain
  open, so Phase 15 is not closed.

2026-08-30 — Phase 15 pad-edge high-current escape checkpoint

- Added module-scoped VIN/VOUT pad-edge escapes for U3/U4 and the U5 VIN
  capacitor bank. The native focused regression passes with no shorting or
  crossing items and reduces the regulator-base unrouted count from 296 to
  280. Bootstrap, feedback, RT, PG, VCC_INTERNAL, and final thermal-margin
  evidence remain open; Phase 15 is not closed.

2026-08-30 — Phase 15 pad-edge authority correction

- Independent KiCad review found U3 VOUT was tied through the inward pad-8
  edge. Corrected the generator to select U3 pad 9 and compute the true pad
  edge from pad geometry; regression now asserts the two exact `(54.95,80.00)`
  edge starts and the native no-short/no-crossing result still passes.

2026-08-30 — Phase 15 U3 quiet-control island checkpoint

- Added U3 FB/RT/PG routing with eight deliberate ordinary through-via
  transitions and separated B.Cu corridors. Native DRC has no route-specific
  clearance, short, or crossing defect; the focused regression verifies 20
  total vias and 272 unrouted items. U4/U5 control routing and full Phase 15
  overlay/thermal closure remain open.

2026-08-30 — Phase 15 native regulator hierarchy association checkpoint

- Native KiCad XML proved the regulator child had been split from root
  `12V_PROTECTED`/`POWER_GND`, while all three internal VCC pins shared one
  child-local net. Added authoritative child global labels for the two power
  rails and isolated VCC as U3/U4/U5-specific internal nets.
- Preserved the native child serialization; the scaffold rebuild path had
  silently dropped support instances and was replaced with an idempotent
  native-format association repair. Headless materialization now requires a
  host-Xvfb native export before Flatpak pcbnew consumes the XML.
- Regenerated Phase 14/15 candidates. Native hierarchy, net-authority,
  materialization, power-route, thermal-via, and focused regulator escape
  regressions pass; power continuity now reaches the actual root nets.

2026-08-30 — Phase 15 separated U4/U5 control checkpoint

- The original U4/U5 10 mm placement left no clean package-side control
  corridor beside U7. A validated candidate separates the modules to
  `(200,105)` and `(225,105)`, with module-scoped support rows and separated
  ordinary through-via trunks.
- U4/U5 FB/RT/PG routing and U4 C18-to-VOUT compensation produce zero native
  clearance, shorting, or crossing findings; the focused regression verifies
  35 vias and 254 unrouted acreage items. U5 VOUT-bank routing, effective
  capacitance, thermal margin, and full Phase 15 closure remain open.

2026-08-30 — Phase 15 U5 output-bank routing checkpoint

- Added a deterministic 4x4 placement and In2.Cu feed for schematic-authority
  capacitors C26-C41 on U5's 1.1 V output. The route leaves the true right
  output land and avoids the existing FB control escape.
- Native DRC and the focused regression pass with zero clearance, shorting, or
  track-crossing findings; the candidate has 69 ordinary through vias, 18 on
  the output net, 28 on the PGND return, and 237 baseline unconnected acreage
  items. Effective
  capacitance, ground-return stitching, thermal margin, and vendor-layout
  overlay evidence remain open, so Phase 15 is not closed.

2026-08-30 — Phase 15 U5 output-return stitching checkpoint

- Added sixteen local PGND return vias for C26-C41, each just outside the
  authoritative capacitor ground land with a short F.Cu link to avoid native
  solder-mask bridges. The focused native regression passes with 69 total
  vias, 18 on VOUT, 28 on PGND, zero route-specific clearance/short/crossing
  findings, and 237 baseline unconnected acreage items.
- Effective-capacitance, thermal-margin, and three-rail TI overlay evidence
  remain open; this is not Phase 15 closure.

2026-08-30 — Phase 15 compact U5 output-bank refinement

- Moved the first three C26-C41 rows beside U5 and kept only the fourth row
  offset to clear the authoritative U5 PG support resistor. Native DRC and
  the focused regression pass with 69 vias, 237 baseline unrouted items, and
  no route-specific clearance, shorting, or crossing findings.
- The geometry is closer to TI's qualitative arrangement, but exact overlay,
  DC-bias evidence, and board-specific thermal proof remain open.

2026-08-30 — Phase 15 measured overlay checkpoint

- Added `phase15_overlay_measure.py` and measured native regulator-to-COUT
  maximum center distances of 7.4 mm (U3), 16.3 mm (U4), and 51.7 mm (U5).
- A tighter U5 vertical bank was rejected by native DRC because it entered U7
  pads; the passing candidate keeps the first three rows near U5 and records
  the fourth-row envelope as a Rev-A placement limitation. The PG support
  island is fixed at x=236 mm with a passing native route regression.

2026-08-30 — Phase 15 output-capacitor lifecycle correction

- Replaced the previous Murata output-capacitor MPN with active TDK
  `C3225X7R1C226M250AC`, a TI-listed 1210/22-uF/25-V/X7R part. Mouser's EOL
  flag for the Murata candidate made it unsuitable as Rev-A authority despite
  remaining stock; TDK distributor stock and active status are recorded in
  `TPSM63606_SUPPORT_AUTHORITY.md`.
- Native Phase 5 power audit and COUT regression pass. The 90% values remain
  nominal derating screens; ±20% tolerance screens are 31.7/47.5/253.4 uF,
  so exact DC-bias/tolerance closure remains explicitly open.

2026-08-30 — Phase 15 active-cap lifecycle and tolerance audit

- Confirmed the active TDK MPN in the native regulator sheet and corrected the
  Phase 15 receipt's stale 36-via wording to the validated 35-via result.
- The COUT regression now reports both nominal 90% derating and the separate
  ±20% tolerance screen, preventing the latter from being hidden by the
  nominal pass.

2026-08-30 — Phase 15 TDK voltage-field correction

- Corrected the active TDK `C3225X7R1C226M250AC` description from 25 V to its
  manufacturer-sheet value of 16 V (`1C` voltage code). Rail requirements are
  5/3.3/1.1 V, so the selected part remains electrically suitable; no MPN or
  footprint change was required.

2026-08-30 — Phase 15 local TDK authority receipt

- Added `TDK_C3225X7R1C226M250AC_AUTHORITY.md` with exact voltage/package
  fields, dated multi-distributor stock evidence, manufacturer-sheet
  provenance, and the explicit graphical-curve limitation.

2026-08-30 — Phase 15 TI EVM layout authority preserved

- Saved TI's public `TPSM63606EVM` user guide and `SLVRBI7` Altium/gerber
  archive locally under the power authority inventory, with SHA256 recorded
  for the archive. The EVM's four-layer/2-oz basis and 110-uF effective
  47-uF-capacitor example are explicitly kept separate from Rev-A claims.

2026-08-30 — Phase 15 generator lifecycle correction

- Updated `phase14_regulator_support_native.py` so native support-network
  regeneration emits the active TDK output-capacitor MPN rather than the
  rejected Murata candidate.
- Extended the Phase 5 audit to fail if the obsolete MPN returns to either
  the native regulator sheet or its authoring path.

2026-08-30 — Phase 15 receipt and COUT regression correction

- Corrected the regulator receipt's U4/U5/thermal-via count to the validated
  35-via checkpoint.
- Strengthened `phase15_capacitance_check.py` to require the exact native
  schematic reference sets C7/C8, C16/C17/C19, and C26-C41 before applying
  the derated effective-capacitance floor calculation.

2026-08-30 — Phase 15 thermal screening checkpoint

- Added `phase15_thermal_screen.py` using TI SLVSGB4B's conservative 33.1 C/W
  metric, 50 C ambient, the 90% design-envelope efficiency assumption, and
  the 125 C operating-junction limit. The calculated margins are 19.8/50.7/
  71.0 C for U3/U4/U5.
- This is a screening calculation against TI's reference thermal board, not
  proof for the JLC six-layer copper stack or fabricated Rev-A hardware;
  board-specific thermal closure remains empirical risk.

2026-08-30 — Phase 15 capacitor and TI-overlay evidence checkpoint

- Added `phase15_capacitance_check.py`, which machine-checks the native
  schematic's 2/3/16 output-capacitor counts and the documented 90% derated
  floors of 39.6/59.4/316.8 uF against TI's 30/50/300 uF minimums.
- Added `PHASE15_TI_LAYOUT_OVERLAY.md` to compare the three regulator
  candidates against TI SLVSGB4B pages 31-32. Thermal margin and exact
  geometric/DC-bias closure remain open; no Phase 15 pass is claimed.

2026-08-30 — Phase 15 EVM scale-reference evidence

- Recorded the measured TI EVM VOUT-capacitor reference (5.85 mm maximum
  regulator-to-capacitor-center distance) and the SHA256 of the retained
  official layout archive in the Phase 15 overlay and regulator receipt.
- Kept the imported EVM board disposable: it is measurement evidence only,
  not a Rev-A design artifact or a claim of geometric equivalence. The Rev-A
  U4/U5 placement exceptions and board-specific thermal/DC-bias risks remain
  open and explicit.

2026-08-30 — Phase 15 VOUT-land and pull-up connectivity correction

- Added explicit perimeter VOUT-land ties for U3, U4, and U5 after native
  DRC identified that duplicate TPSM63606 VOUT lands were not all connected.
- Connected the U4/U5 output pull-up returns to their local output copper and
  kept the U5 trunk-head through-via connected on both F.Cu and In2.Cu.
- Native final DRC now reports zero route crossings, shorts, dangling tracks,
  and dangling vias; focused regressions cover both VOUT-land associations.
  Phase 15 remains open only for switch-node, exact DC-bias, and
  board-specific thermal/reference-overlay closure.

2026-08-30 — Phase 15 switch-node containment audit

- Added a fail-closed board audit proving the TPSM63606 SW/CBOOT/RBOOT nets
  have no external copper or component pads in the final regulator candidate,
  consistent with TI's internal-bootstrap/default-slew guidance.
- A native no-connect serialization experiment was discarded after KiCad
  ERC did not associate the generated markers with the child pin endpoints;
  no speculative schematic change was retained.

2026-08-30 — Phase 15 regulator-routing gate closed

- Closed Phase 15 with the final native DRC and focused audits: zero route
  crossings, shorts, dangling tracks, or dangling vias; switch-node audit
  passes; output-land and pull-up connectivity is explicit.
- Classified only bounded Rev-A empirical risks: exact TDK DC-bias/temperature
  capacitance sum, constrained U4/U5 capacitor envelopes, and board-specific
  thermal response. No fabricated-hardware claim is made, and later routing
  must preserve the accepted regulator keepouts.

2026-08-30 — Phase 16 PCIe net-authority correction

- Added the generic five-link root authoring contract for direct PER0, REFCLK,
  and PERST connectivity; PET0 remains split across its two coupling capacitors.
- Corrected Phase 4 instance pin UUID generation so pin identities cannot alias
  the containing symbol UUID. Native KiCad export and the Phase 16 regression
  prove J7-to-SXM2 identity and preserve the PET0 split.

2026-08-30 — Phase 16 routing rejection and netlist regression hardening

- Rejected the first PCIe PCB candidate after native DRC found 422 violations,
  including signal crossings, pad-field shorts, and incorrect escape geometry.
- Strengthened the schematic authority regression from partial membership checks
  to exact direct-net node sets and exact PET0 capacitor-side separation.
- No invalid Phase 16 PCB candidate was retained; routing remains open and
  Phase 17 is not started.

2026-08-30 — Phase 16 PET0 source-side authority correction

- Linked CM5 PET0 source-side ports across the root to the V100 child while
  keeping C1/C2 as the only electrical breaks to the SXM2 endpoint.
- Regenerated the Phase 14/15 materialized candidates from the corrected
  netlist; exact netlist regression passes for all direct paths and both PET0
  source/endpoint sides.
- The attempted PCIe geometry remains rejected by native DRC; no Phase 16
  routing gate or later phase was claimed.

2026-08-30 — Phase 17 EDAC MagJack land-number authority correction

- Corrected the generic schematic-to-PCB materializer with the EDAC J2
  logical-pin-to-physical-pad 19-minus-pin map for all 18 contacts.
- Regenerated the Phase 16 baseline through the full required pipeline and
  verified MDI pairs on physical pads 18..11 plus center taps, LEDs, and
  shields with the native pcbnew ABI regression.

2026-08-30 — Phase 17 Ethernet routing candidate rejection

- Rejected perimeter and dogbone candidates under native DRC; the frozen
  Ethernet placement creates source-order permutations, existing power and
  regulator crossings, NPTH keepout conflicts, and ESD pad-field shorts.
- Phase 17 remains open with the no-improvised-maze gate intact; no invalid
  copper candidate was committed.

2026-09-03 — Published Phase 17 blocker report

- Added the readable repository-root `blocker.md` report and preserved the
  current rejected-route evidence for private GitHub review.

2026-09-03 — Phase 17 Ethernet placement-repair sprint

- Reopened Phase 11/12 only for Ethernet as authorized and tested nine compact
  CM5-adjacent arrangements plus a complete west-edge MagJack island.
- The best order-preserving U9/U6/J2 candidate still has native DRC-confirmed
  crossings/shorts at the J7 breakout, TPD4E004 pad fields, and J2 connector
  boundary; it was rejected and no invalid copper was accepted.
- Phase 17 remains the earliest failed gate. Phase 18+ work remains prohibited
  pending an Ethernet-local escape/package decision.

2026-09-03 — Phase 17 Ethernet ESD package unblocker

- Independent footprint review identified Littelfuse SP3019-04HTG as the
  preferred next disposable candidate: active SOT-23-6L gullwing, four
  separated signal pins, low published capacitance, and multi-distributor
  availability.
- Recorded manufacturer, lifecycle, package, and procurement evidence in
  `PHASE17_ETHERNET_ESD_REPLACEMENT_RESEARCH.md`; no clean schematic or
  production PCB promotion has occurred.
- A disposable SP3019 geometry trial was run through native KiCad DRC; it
  remains rejected with 335 violations and 238 unconnected items. Its
  datasheet-derived trial footprint is explicitly non-authoritative and was
  not promoted.
- The disposable trial project shell was checkpointed with its PCB and DRC
  report so the rejected experiment is reproducible.
- The SP3019 routing generator was refined to use pair-separated monotonic
  corridors; the resulting native trial still fails and remains disposable.

2026-09-03 — Independent Phase 17 SP3019 blocker correction

- Published the specialist finding that the prior SP3019 trial was malformed,
  not a proof of geometric impossibility: it lacked required via transitions,
  omitted TD0_P copper, floated ESD ground, and used an unverified impedance
  width.
- Updated `blocker.md` with the corrected bounded topology and the exact next
  experiment: authoritative land pattern, explicit ordinary vias, all eight
  pairs, 100 ohm stack calculation, and complete MagJack-side routing.

2026-09-03 — Phase 17 SP3019 authoritative fixture experiment

- Repaired the KiCad 10 Flatpak generator path to use native typed footprint
  copies and `FindPadByNumber`; the corrected manufacturer-footprint fixture
  now saves with both SP3019 instances and explicit pin-2 Ethernet ground.
- Preserved a reproducible J7/J2 disposable-fixture extraction helper and ran
  native DRC on the full eight-pair trial. The candidate remains open, with 96
  violations and 76 unconnected items, including real launch crossings/shorts
  and missing required via/dogbone transitions.
- Published the exact evidence and bounded continuation options in
  `blocker.md`. SP3019 was not promoted, the clean PCB/schematic was not
  changed, and Phase 18+ remains gated.

2026-09-03 — Phase 17 minimal Ethernet fixture isolation

- Added a reproducible disposable base extractor that preserves the
  authoritative J7 Ethernet pad coordinates and J2 launch while removing
  unrelated CM5 pads and prior acreage routing from the fixture.
- Re-ran the corrected SP3019 fixture against the isolated base. Native DRC
  narrowed the result to 65 violations and 21 unconnected items; the
  remaining failures are Ethernet-local routing/topology defects, not the
  prior malformed-footprint or unrelated-connector evidence.
- Kept SP3019 unpromoted and the clean PCB/schematic unchanged.

2026-09-03 — Phase 17 Ethernet fixture routing audit

- The isolated base was independently checked: the regenerated disposable J7
  copy contains exactly eight Ethernet source pads. This removes the stale
  unrelated-pad contamination from the earlier report.
- Independent high-speed review confirms the remaining failure is local
  topology: the trial has no ordinary F.Cu/B.Cu transitions, uses incorrect
  J2 upper-launch coordinates, and retains pair crossings/center-tap shorts.
- The next repair remains bounded to the disposable fixture: reorient the
  launch, use exact J2 coordinates, add symmetric through-via/dogbone and GND
  return transitions, then rerun native DRC and route metrics.

2026-09-03 — Phase 17 Ethernet reorientation experiment

- Tried a distinct disposable placement with relocated J7/J2 and separated
  F.Cu/B.Cu pair corridors. Native DRC recorded 105 violations and 4
  unconnected pads, including true J2-launch shorts/crossings and invalid
  transition geometry.
- Rejected this corridor construction without relaxing clearance or layer
  rules. SP3019 remains an open candidate; the clean board/schematic remain
  unchanged.

2026-09-03 — Phase 17 Ethernet explicit-transition correction

- Corrected the disposable through-via dimensions to the board's ordinary
  minimum (0.50 mm diameter, 0.30 mm drill) and reran native DRC.
- The resulting experiment recorded 86 violations and 4 unconnected pads.
  True source/via fanout and J2 support-pad shorts/crossings remain, so this
  route is rejected; no clearance or layer rule was weakened.

2026-09-03 — Phase 17 separated Ethernet placement experiment

- Tried a further disposable placement with J7/J2 separated on a large
  fixture, monotonic F.Cu/B.Cu pair groups, and explicit transitions. Native
  DRC improved to 74 violations and 4 unconnected pads.
- Rejected the experiment because genuine four-pair fanout/launch crossings
  and shorts remain. The clean PCB/schematic remain unchanged and SP3019 is
  not promoted.

2026-09-03 — Phase 17 current fixture audit checkpoint

- Re-audited the saved disposable PCB after the separated-placement trial:
  J7 has exactly eight Ethernet pads, U6/U9 have six pads each with explicit
  ground and NC pin 5, and all eight CM5 Ethernet nets are present.
- Native DRC remains 74 violations and 4 unconnected pads. This is preserved
  as failed fixture evidence only; no production promotion or later phase was
  started.

2026-09-03 — Phase 17 Ethernet return-path correction

- Joined the two external SP3019 ground-return vias with an ordinary B.Cu
  GND spine and reran native DRC. The fixture now has zero unconnected pads.
- Native DRC still reports 79 true pair crossings/shorts, so this remains a
  failed disposable experiment. SP3019 was not promoted and production files
  were not changed.

2026-09-03 — Phase 17 Ethernet source-fanout correction

- Moved the B.Cu source transitions onto separated external lanes and fixed
  the B.Cu segment construction. Native DRC now reports 0 unconnected pads
  and 76 remaining true crossings/shorts/clearance violations.
- The fixture remains failed and disposable; SP3019 was not promoted and the
  clean PCB/schematic remain unchanged.

2026-09-03 — Phase 17 TI ESDS304 alternative authority

- Added a project-local disposable `ESDS304DBVR` SOT-23 DBV footprint derived
  from TI DBV0005A mechanical and land-pattern data, with explicit mask,
  paste, and courtyard layers.
- Recorded TI's active-production status, pin map, Ethernet 1G application,
  capacitance, and passive topology in the ESD replacement research note.
- This is an alternative candidate only; no clean production asset was
  changed and no ESDS304 routing pass has been claimed.

2026-09-03 — Phase 17 ESDS304 endpoint alignment rerun

- Aligned the disposable generator to the corrected TI DBV0005A pad
  coordinates and regenerated the fixture.
- Native DRC reports 104 violations and 7 unconnected items. Rejected this
  route construction for true crossings/shorts and connector-launch defects.
- Kept ESDS304 unpromoted and the clean production assets unchanged.

2026-09-03 — Phase 17 ESDS304 large-acreage escape experiment

- Built a new disposable fixture with corrected TI DBV0005A geometry, remote
  ESD placement, separate F.Cu/B.Cu channels, ordinary transitions, local
  ground returns, and a dedicated J2 launch zone.
- Native DRC reports 92 violations and 8 unconnected items, including real
  shelf crossings, source/ESD interactions, connector-launch failures, and
  incomplete connectivity.
- Rejected the candidate and preserved the generator, PCB, and DRC report as
  evidence. No clean production asset was changed.

2026-09-03 — Phase 17 ESDS304 authority-only proof

- Added and ran a native KiCad machine-check for the corrected TI DBV0005A
  footprint and disposable U9/U6 mapping.
- Verified package pad positions/sizes, mask/paste layers, courtyard, all
  eight MDI nets, and explicit ETH_GND; the authority check passes.
- Kept routing open because the latest candidate still fails native DRC. No
  production asset was changed.

2026-09-03 — Phase 17 ESDS304 authority-note correction

- Corrected the research note's DBV0005A row-separation typo from 1.9 mm to
  the TI-authoritative 2.6 mm value. The machine-check and footprint already
  used the corrected geometry.

2026-09-03 — Phase 17 ESDS304 footprint-authority correction

- Specialist review found the disposable ESDS304 footprint did not match TI
  DBV0005A: its pads were distributed on the wrong sides and overlapped.
- Corrected the local footprint to the TI-authoritative 5-pad arrangement,
  dimensions, paste/mask, and expanded courtyard, then regenerated the
  disposable fixture.
- Fresh native DRC reports 100 violations and 11 unconnected items. Rejected
  the route construction as failed, while retaining ESDS304 as an electrically
  credible alternative. The result does not reject the part itself.
- Updated `blocker.md` to distinguish invalid prior evidence from the
  corrected negative routing result. Production assets remain untouched.

2026-09-03 — Phase 17 fallback ESD solution class

- Researched TI ESDS311DYFR as the next authorized alternative: active
  single-channel SOD-323, explicitly Ethernet 10/100/1000 capable, with a
  simple shunt topology and captured Mouser/Digi-Key availability.
- Recorded its higher 4.5 pF capacitance and eight-device assembly cost as
  reasons it remains fallback-only pending a disposable fixture.
- No production asset was changed.

2026-09-03 — Phase 17 ESDS311 disposable fixture

- Built the authorized eight-device TI ESDS311DYFR SOD-323 fallback fixture
  with explicit Ethernet nets, ground returns, ordinary transitions, and the
  EDAC connector launch.
- Corrected the initial SMD-to-B.Cu termination to use local F.Cu dogbones
  and ordinary vias at each line pad.
- Native DRC still reports 212 violations and 24 unconnected items. Rejected
  the fixture as a route construction; ESDS311 was not promoted and the clean
  board/schematic remained untouched.

2026-09-03 — Phase 17 final bounded disposition

- Completed the authorized disposable alternatives: SP3019, corrected
  ESDS304, and ESDS311, including separated placements and ordinary-via
  transition repairs.
- No candidate passed native DRC and complete connectivity. The common
  failure is the CM5/J7 to ESD to EDAC launch geometry under the frozen
  F.Cu/B.Cu-only contract, not missing package authority.
- Recorded three bounded user-controlled continuation options and the
  recommendation in `blocker.md`.
- No production asset was changed; Phase 18+ remains unopened.

2026-09-03 — Phase 17 BCM54210PE remap authority investigation

- Checked Broadcom BCM54210 public authority and official Raspberry Pi CM5IO
  Rev 2 wiring evidence before changing Ethernet mapping.
- Established a fail-closed remap boundary: intact differential pairs only,
  conditional complete-pair MDI/MDIX variants, conditional P/N inversion,
  and no individual-conductor mixing or unproven arbitrary permutation.
- Recorded the legal trial table and evidence limits in
  `PHASE17_BCM54210PE_REMAP_AUTHORITY.md`.
- No production asset was changed; Phase 17 routing remains open.

2026-09-03 — Phase 17 BCM54210PE remap closure boundary

- Verified the exact CM5 feature claim from Raspberry Pi: automatic MDI
  crossover, pair-skew correction, and pair-polarity correction.
- Compared it with the official CM5IO four-intact-pair, 1:1 MagJack wiring and
  Broadcom's public BCM54210 authority.
- Recorded that no exact-device public mapping table authorizes arbitrary
  four-pair PCB permutation; polarity remains an intact-pair operation and
  skew correction does not legalize copper crossings.
- Added the fail-closed candidate matrix and updated the GitHub-readable
  blocker report. No clean PCB/schematic or Phase 18+ artifact was changed.
- Distinguished Broadcom family-level lifecycle claims from the exact CM5
  `BCM54210PEB1KMLG` variant; captured the distributor-hosted EOL notice and
  retained the exact-device remap question as unresolved.
- Added independent specialist confirmation that only CM5IO-style 1:1 pair
  assignment is publicly authorized; recorded exact MOQ/LTB/LTS and authorized
  inventory evidence. No clean design asset changed.

2026-09-03 — Phase 17 official CM5IO Rev 2 CAD oracle extraction

- Downloaded the official Raspberry Pi “CM5 IO Board, revision 2, KiCAD
  files” archive and recorded its SHA-256 in the authority inventory.
- Inspected the native CM5IO schematic and PCB, extracting the exact U1/U2
  `TPD4EUSB30`, EDAC `A70-112-331N126`, CM5 pin map, orientations, positions,
  F.Cu 0.127 mm MDI routing, PoE tap support, LEDs, shields, and GND use.
- Added a generator and receipt for a disposable official Ethernet fixture;
  no production clean asset changed.
- Native DRC of the official source and exact-copy fixture reports zero
  unconnected items and no MDI crossing/short/dangling-via findings; warnings
  are limited to official POE spacing and library-configuration overrides.
- The initial isolated extractor hit a KiCad Flatpak SWIG track-container
  lifetime defect and was replaced by an exact-copy oracle fixture; no
  production asset changed.

2026-09-03 — Phase 17 official-oracle transplant boundary

- Independent native-CAD audit confirmed the official MagJack footprint is
  `TRJG0926HENL`, not the selected EDAC `A70-112-331N126`; mounting/shield
  hole dimensions differ and the donor footprint remains reference-only.
- Confirmed the official ESD value/BOM versus hidden sourcing/datasheet fields
  contain a material identity conflict; no guessed ESD promotion was made.
- Recorded that the official CM5IO topology is closed as a routing oracle but
  PiSXMe adaptation remains open pending separately-authorized EDAC/ESD
  footprint parity. No clean PCB/schematic was modified.

2026-09-03 — Published current Phase 17 oracle blocker report

- Updated the GitHub-readable blocker report from terminal-blocked wording to
  the recoverable official-oracle/transplant state.
- Preserved exact CM5IO source, native DRC, ESD metadata conflict, and
  MagJack land-pattern mismatch as the next bounded work boundary.
- No clean PCB/schematic or Phase 18+ artifact was changed.

2026-09-03 — Phase 17 CM5IO MDI transplant experiment

- Resolved the official CM5IO ESD value ambiguity to active TI
  `TPD4EUSB30DQAR` using current TI product/package authority and major
  distributor evidence; saved the Rev-G datasheet and SHA-256.
- Corrected the clean TPD4E004 symbol/net mapping to TI's actual 6-pin
  pinout and corrected the EDAC shield-pad representation in the authoring
  path; regenerated the disposable mapping candidate and passed native
  mapping parity.
- Rigidly transformed 189 official CM5IO MDI segments onto the PiSXMe CM5
  and EDAC physical contact coordinates. Focused regression passed; native
  DRC found no MDI crossings, shorts, dangling vias, or footprint errors.
- Rejected the first mixed support overlay because its improvised GND/CT/
  shield paths crossed MDI geometry. No production acreage asset or Phase 18+
  artifact was promoted.

2026-09-03 — Phase 17 official-support adaptation experiment

- Tested a common center-tap In2 island, local GND copper return islands,
  outer B.Cu shield return, and valid fixture outline around the passing MDI
  transplant.
- Native DRC rejected the detached-zone construction with 82 violations and
  13 unconnected support pads; the failed artifact is preserved as evidence.
- Kept the official complete CM5IO fixture as the passing support oracle and
  left the clean production PCB/schematic and Phase 18+ work unpromoted.

2026-09-03 — Phase 17 explicit support-fanout follow-up

- Replaced broad detached support zones with explicit same-net B.Cu
  center-tap fanout, compact GND islands, ordinary return vias, and an outer
  shield route.
- Reduced the adapted fixture to 18 native DRC violations and 7 unconnected
  support pads, but rejected it because the remaining support connections are
  not yet proven.
- Preserved the passing MDI result and did not promote clean production or
  Phase 18+ assets.

2026-09-03 — Phase 17 complete CM5IO-derived fixture

- Repaired the EDAC support fanout with explicit B.Cu center-tap routing,
  official local USON GND escape geometry, ordinary return vias, and an outer
  shield return.
- Native DRC reached 0 unconnected pads and no true short, crossing,
  hole-clearance, dangling-via, outline, silkscreen, or footprint errors;
  only documented warnings remain.
- Closed the disposable fixture gate while keeping the clean acreage
  promotion and Phase 18+ work gated pending production-path adaptation.

2026-09-03 — Phase 17 acreage EDAC-launch blocker

- Promoted the clean Ethernet ESD authoring path to active TI
  `TPD4EUSB30DQAR`; native netlist and focused pin mapping passed.
- Rejected blind application of the CM5IO disposable connector launch because
  its temporary common-tap/EDAC assignment does not match the authoritative
  EDAC A70-112-331N126 MDI groups and center-tap pads.
- Preserved the 628-violation diagnostic DRC and published the exact,
  recoverable EDAC-side launch adaptation boundary in `blocker.md`.
- Did not promote the clean acreage PCB or begin Phase 18+.

2026-09-03 — Phase 17 pin-accurate EDAC launch trial

- Built a narrower disposable fixture retaining the passing CM5IO
  CM5-to-ESD geometry while using the production EDAC MDI pad groups 1..8.
- Regenerated the connector-side 0.127 mm F.Cu launch at the actual EDAC pad
  coordinates and ran native KiCad DRC.
- Rejected the trial at 20 violations and 17 unconnected items, including
  pair crossings/shorts; preserved the report and kept production and later
  phases gated.

2026-09-03 — Phase 17 EDAC connector-side layer split trial

- Tried ordinary F.Cu-to-B.Cu transitions for TD1 and TD3 while retaining
  pair integrity and the approved layer contract.
- Reduced the launch-specific DRC count from 20 to 14, but retained two
  crossings, three net shorts, and 17 unconnected items; rejected the trial.
- Kept the CM5IO source/ESD oracle and all production/later-phase assets
  gated; the next experiment is the official MagJack comparison.

2026-09-03 — Phase 17 CM5IO/EDAC authority-alignment correction

- Rechecked the official CM5IO PCB U1/U2/U3 placement against the EDAC
  manufacturer land pattern and found that the official MDI pads are
  1,2,3,6,7,8,9,10, with center taps on 11..14.
- Corrected the clean alias map and aligned production references as U6
  carrying TD0/TD1 at the official right protector position and U9 carrying
  TD2/TD3 at the official left position.
- Regenerated the native schematic netlist and acreage footprint map; the
  Ethernet pin-mapping regression passed.
- Regenerated the CM5IO-derived fixture using the reference-aligned refs;
  native DRC and focused MDI regression passed again with zero unconnected
  pads and no MDI crossings/shorts.
- Isolated official MDI geometry into a serialized data snapshot after
  identifying a KiCad Python multi-board wrapper/net-assignment hazard. The
  full acreage candidate still contains unrelated floorplan DRC conflicts and
  remains unpromoted; Phase 18+ remains gated.

2026-09-03 — Phase 17 corrected acreage application diagnostic

- Applied all 189 CM5IO MDI vectors through a single-board geometry snapshot
  path after confirming KiCad Python multi-board net wrappers could collapse
  distinct nets.
- Corrected mapping regression passed; full-board DRC remained contaminated by
  the current floorplan, with 539 violations and 477 unconnected items,
  including Ethernet shorts against neighboring power/keepout geometry.
- Classified the remaining issue as a local Ethernet placement/floorplan
  blocker, preserved the dirty candidate, and kept Phase 18+ gated.

2026-09-03 — Phase 17 routed-ancestor restore boundary

- Exported 320 routed Phase 16 copper items by stable net name and restored
  them onto the corrected clean materialization before applying the official
  CM5IO Ethernet vectors.
- Native DRC remained invalid at 835 violations and 460 unconnected items;
  the evidence includes inherited Phase 16/acreage debt and Ethernet
  collisions with neighboring power/keepout geometry.
- Preserved the snapshot/export/restore scripts and kept Phase 17 open; no
  Phase 18+ work started.

2026-09-03 — Phase 17 CM5IO transplant authoring correction

- Corrected the generic transplant path to use 270-degree local USON
  orientation with the clean U6/U9 pad mapping; removed the stale swapped-net
  90-degree assumption.
- Changed generated MDI boundary labels to global labels and regenerated the
  child schematic/netlist; the complete duplicated flow-through pad mapping
  now passes the current hierarchy-authority regression.
- Rebuilt and natively checked the disposable transplant: 8 warning-only
  violations, 0 unconnected pads, and 0 footprint errors. Acreage Phase 17
  remains open and Phase 18+ remains gated.

2026-09-03 — Phase 17 top-left Ethernet side-escape trial

- Tested a distinct CM5IO-aligned top-left placement with J2 at (30,45) and
  explicit left/right exits around the fixed J7 connector body.
- Rejected the candidate at native DRC: 428 violations and 485 unconnected
  items, including true TD2 pair short/crossing failures and EDAC support
  overlap with the F1/input envelope.
- Preserved the disposable PCB, generator, and DRC receipt; no frozen
  subsystem or production PCB was promoted and Phase 18+ remains gated.

2026-09-03 — Phase 17 top-left B.Cu escape trial

- Tested ordinary through-vias outside J7 with B.Cu pair corridors and F.Cu
  dogbones into the translated official CM5IO ESD graph.
- Rejected the candidate at native DRC: 495 violations and 485 unconnected
  items, including true pair shorts/crossings at the transition lanes.
- Preserved the candidate and report; the official all-F.Cu CM5IO topology
  remains authoritative and Phase 18+ remains gated.

2026-09-03 — Phase 17 monotonic-lane Ethernet trial

- Rebuilt the top-left source escape with ordered left/right lanes and
  consistent translated U6/U9/J2 coordinates.
- Rejected native DRC at 364 violations/453 unconnected, with four true
  source-side pair crossings and dense ESD/connector launch clearance
  failures; inherited unrouted-ancestor debt was not used as the sole basis.
- Preserved the candidate/report and kept the official CM5IO topology and
  Phase 18+ gate unchanged.

2026-09-03 — Phase 17 coordinate-corrected top-left trials

- Corrected the top-left disposable script so its translated footprints and
  official MDI vectors agree: U9=(27.6,57.215), U6=(33.6,57.215), J2=(30,45).
- Rejected the corrected F.Cu side escape at 383 violations/453 unconnected,
  including true TD2 shorts and source-side crossings.
- Rejected the corrected B.Cu transition escape at 448 violations/453
  unconnected, including true TD0/1, TD2, and TD3 shorts/crossings.
- Preserved both candidates and reports; Phase 18+ remains gated.

2026-09-03 — Phase 3 current-source ERC audit

- Reran native KiCad root ERC after the generic global-MDI-label correction.
- Recorded 644 warning-only findings, with no root hierarchy-association
  error; the focused Ethernet hierarchy/netlist regression passes.
- Corrected the stale zero-total-ERC statement in `PHASE3_STATUS.md` and
  preserved the full current report for final-gate review.

2026-09-03 — Phase 17 180-degree ESD reorientation fixture

- Built a fresh disposable fixture from actual local U6/U9/J2 pad geometry,
  with both ESD footprints rotated 180 degrees and intact CM5IO pair nets.
- Rebuilt the fixture without inherited acreage context; isolated native DRC
  reports 94 violations/4 unconnected items. True MDI crossings and shorts
  remained at the fixed J7 launch, and the default 0.200 mm width rule also
  rejects the CM5IO-derived 0.127 mm width.
- Preserved the fixture/report and closed the package-reorientation-only
  hypothesis without modifying production or frozen subsystems.
- Rebuilt the disposable from only the authoritative four Ethernet footprints
  after detecting inherited acreage context in the first fixture run; the
  corrected isolated receipt is the controlling evidence.

2026-09-03 — Phase 17 parametric right-channel trial

- Rebuilt the right-shelf breakout as unique J7 dogbones, ordered parallel
  lanes, and an upper corridor into the official CM5IO island.
- Rejected native DRC at 447 violations/485 unconnected items because true
  Ethernet-local crossings/clearances remained.
- Preserved the candidate and report; the next experiment is a regenerated
  180-degree USON reorientation, with Phase 18+ still gated.

2026-09-03 — Phase 17 right-shelf complete-island trials

- Used the official CM5IO-relative Ethernet placement on the open right shelf
  below the cooler, with source breakout generated from actual J7 pads.
- Rejected all-F.Cu native DRC at 431 violations/484 unconnected items.
- Rejected the ordinary-through-via layer-separated variant at 499/484,
  preserving both candidates and reports; Phase 18+ remains gated.

2026-09-03 — Phase 17 TD3-outer physical-order trial

- Rechecked the official CM5IO source before experimenting; retained its
  authoritative 1:1 pair mapping and F.Cu MDI routing philosophy.
- Tested a new left-source physical order with TD3 outer/left and TD2
  inner/right to remove the reversal identified in the prior monotonic trial.
- Rejected native KiCad DRC at 364 violations/453 unconnected items because
  Ethernet-local crossings/launch-clearance failures remained. Preserved the
  candidate and DRC receipt; no production or frozen subsystem changed.

2026-09-03 — Phase 17 layer-separated launch refinement

- Split measured J7 source groups across F.Cu/B.Cu with ordinary through-vias
  and increased via spacing from the failed 0.5 mm arrangement.
- Native DRC improved to 163 violations/3 unconnected items but still found
  B.Cu MDI crossings and connector/transition clearances; candidate rejected.
- Preserved the refined fixture/report and kept Phase 17 as the earliest gate.

2026-09-03 — Phase 17 exact J7-launch-only oracle

- Built a disposable fixture with the complete authoritative J7 instance,
  opposing pad field, courtyards, valid outline, and separated boundary pads.
- Native DRC reported 27 candidate-local violations and 63 expected non-MDI
  unconnected pads; true MDI launch crossings/clearances remain.
- Preserved the diagnostic fixture and kept Phase 17 open.

2026-09-03 — Phase 17 J7 nested-lane refinement

- Rejected a height-offset dogbone variant after it reintroduced a source
  crossing, then restored the better nested-lane construction.
- Current J7-only DRC has zero tracks-crossing, shorting, and hole-clearance
  findings; two source-via clearances and expected non-MDI unconnected pads
  remain.
- Preserved the fixture/report and kept Phase 17 open.

2026-09-03 — Phase 17 J7 launch sub-gate closure

- Completed the source-order-preserving J7 transition trial with exact
  footprint/pad-field authority and ordinary through-vias.
- Native DRC has zero tracks-crossing, shorting, clearance, and hole-clearance
  findings; width-rule, dangling diagnostic, and non-MDI fixture omissions
  remain explicitly reported.
- Closed the fixed-J7-launch hypothesis and retained Phase 17 for complete
  ESD/MagJack integration; Phase 18+ remains gated.

2026-09-03 — Phase 17 current J7/transplant receipts

- Corrected the controlling J7 launch receipt to 32 total DRC findings,
  consisting only of width-rule/dangling diagnostics plus expected non-MDI
  fixture omissions; zero crossings, shorts, clearance, and hole-clearance.
- Reran the complete CM5IO transplant: 8 silkscreen-only findings and zero
  unconnected items. Retained it as the full-island authority baseline.

2026-09-03 — Phase 17 corrected J7 source transitions

- Corrected the disposable J7 generator so F.Cu-only source pads begin on
  F.Cu before ordinary through-via transitions; the right group returns to
  F.Cu through a second ordinary via.
- Native DRC now reports zero MDI crossings, shorts, via-dangling, and
  hole-clearance findings. Remaining 38 findings are fixture width/clearance
  diagnostics and expected non-MDI omissions; no CM5_GBE item is unconnected.
- Superseded the prior J7 receipt and retained Phase 17 open pending complete
  ESD/MagJack integration and acreage validation.

2026-09-03 — Phase 17 official-island acreage adaptation

- Revalidated the complete CM5IO-derived disposable island: native DRC has
  0 unconnected items and only 8 non-electrical library/silkscreen findings.
- Applied the transformed MDI geometry to the acreage candidate as a
  controlled adaptation test; native DRC rejected it at 539 findings / 477
  unconnected items, including 40 true shorts and local pad-field/copper
  collisions.
- Rejected the direct coordinate transplant, preserved both reports, and
  kept Phase 17 open while the local placement adaptation is repaired.

2026-09-03 — Phase 17 adapter orientation correction

- Corrected the acreage adapter to preserve official U9 TD3/TD2 and U6
  TD1/TD0 ownership and -90-degree USON orientation.
- Native DRC improved to 435 findings / 453 unconnected items and 11 true
  shorts, with no tracks-crossing or via-dangling category; remaining local
  power/clearance collisions reject the acreage candidate.
- Preserved the corrected report and retained Phase 17 open for a fresh
  local placement/escape adaptation.

2026-09-03 — Phase 17 local-bottom island trial

- Tested a CM5IO-derived island below the cooler with regenerated J7 source
  legs; all-F.Cu and split-layer variants were rejected by native DRC.
- The key failure was identified as approach-side inversion: the rigid
  official -90-degree island was moved below J7 without rotating its complete
  geometry, causing ESD landing collisions. Split-layer lanes also reused
  overlapping heights.
- Preserved the rejected candidates and retained Phase 17 for a rigid
  180-degree island rotation experiment.

2026-09-03 — Phase 17 rigid-rotation local-island trial

- Rotated the complete official CM5IO ESD/MagJack island as one block while
  keeping CM5/J7 fixed and regenerating the source transitions.
- Native DRC rejected the candidate at 491 findings / 453 unconnected items;
  dominant local causes were 0.4–0.5 mm transition-via spacing and
  same-layer lane overlap near the rotated ESD landing.
- Preserved the candidate and retained Phase 17 for a >=0.8 mm via-offset
  and final-lane-order repair.

2026-09-03 — Phase 17 mode-coordinate authoring correction

- Corrected the generic right-shelf/channel generator so mode-specific
  translations move U9, U6, and J2 together with the official MDI route graph.
- Valid right-channel rerun reports 425 findings / 453 unconnected items,
  including 13 shorts and 9 crossings; the long F.Cu channel still collides
  with frozen power/regulator copper and J7 fanout geometry.
- Superseded prior right-channel placement conclusions and retained Phase 17
  for a valid source-layer/channel repair.

2026-09-03 — Phase 17 right-channel B.Cu trial

- Tested the corrected right-channel candidate with the long source corridor
  on B.Cu and ordinary through-via transitions.
- Native DRC rejected it at 467 findings / 453 unconnected items; source
  crossings fell to 6, but pair-via spacing and shared B.Cu fanout overlap
  introduced 22 true shorts.
- Rejected the single-bundle construction and retained Phase 17 for
  pair-specific staggered transitions with >=0.8 mm via spacing.

2026-09-03 — Phase 17 west/east source-group trial

- Separated TD3/TD2 and TD1/TD0 into independent west/east B.Cu approaches
  with separated top corridors.
- Native DRC rejected the candidate at 455 findings / 453 unconnected items,
  including 18 crossings and 7 shorts; the remaining failures localized to
  J7 dogbones, final F.Cu returns, and first transitions.
- Preserved the rejected candidate and retained Phase 17 for reuse of the
  proven J7 launch dogbone construction.

2026-09-03 — Phase 17 continuation checkpoint

- Confirmed the official CM5IO chain and corrected J7 launch remain valid
  independent authorities; only acreage integration remains open.
- Rejected the latest west/east source-group trial and preserved its native
  DRC evidence.
- Kept Phase 18+ gated and selected reuse of the proven J7 launch boundary as
  the next authorized Ethernet integration step.

2026-09-03 — Phase 17 J7-boundary CM5IO bridge fixture

- Joined the exact J7 launch fixture to the complete official CM5IO-derived
  ESD/MagJack island while retaining the original launch construction.
- Native DRC rejected the first bridge layout at 277 findings / 68
  unconnected items, including 16 crossings and one short; failures are
  confined to the new boundary bridge paths.
- Preserved the fixture and retained Phase 17 for pair-specific layer-
  separated bridge corridors.

2026-09-03 — Phase 17 outer-edge bridge-layer trial

- Tested pair-specific F.Cu/B.Cu boundary bridges with 2 mm-separated return
  vias and outer-edge detours.
- Native DRC rejected the candidate at 303 findings / 68 unconnected items,
  including 16 crossings, 6 shorts, and 4 dangling vias; failures were due
  to the island/launch-envelope overlap and connector-side returns.
- Rejected the candidate and retained Phase 17 for moving the disposable
  island outside the launch envelope before bridging.

2026-09-03 — Phase 17 island-outside-launch-envelope trial

- Translated the complete official Ethernet island 90 mm east of the exact
  J7 launch fixture and bridged from the unchanged boundary.
- Native DRC improved to 254 findings / 78 unconnected items for the ordinary
  bridge and 266 / 78 for the outer-layer variant; both retained crossings
  and shorts and were rejected.
- Confirmed island overlap as a real contributor and retained Phase 17 for
  pair-order repair on the remote-island basis.

2026-09-03 — Phase 17 remote-island bridge rerun

- Re-ran the official island 90 mm east of the J7 launch envelope with all
  island geometry translated together.
- Ordinary bridge measured 254 / 78 with 11 crossings and 3 shorts; the
  outer-layer variant measured 266 / 78 with 16 crossings and 4 shorts.
- Retained Phase 17 for a round-the-envelope, monotonic pair-lane bridge.

2026-09-03 — Phase 17 round-the-envelope bridge trial

- Tested a round-the-envelope bridge from the exact J7 launch boundary to the
  translated official CM5IO Ethernet island.
- Native KiCad DRC measured 248 violations / 78 unconnected items, including
  5 crossings and 16 dangling bridge tracks; the candidate was rejected.
- Published the exact failure and preserved disposable evidence in
  `blocker.md`; Phase 18+ remains gated.

2026-09-03 — Phase 17 pair/polarity-permutation bridge trial

- Tested a BCM54210PE-supported TD1/TD0 pair swap and per-pair polarity
  reversal against the remote official CM5IO island.
- Corrected the source escape to preserve pair order, then measured native
  KiCad DRC at 247 violations / 78 unconnected items with 4 crossings and
  16 dangling tracks; rejected the candidate.
- Recorded the canonical blocker packet and retained Phase 18+ gating.

2026-09-03 — Phase 17 corrected copied-island handoff trial

- Corrected the disposable bridge generator to retain the official island-side
  handoff segments and target their measured translated coordinates near
  x=149–151 rather than stale ESD-side coordinates.
- Native KiCad DRC measured 274 violations / 72 unconnected items, including
  17 crossings, one short, and 12 dangling tracks; rejected the candidate.
- Recorded the diagnostic improvement and retained Phase 18+ gating.

2026-09-03 — Phase 17 real-handoff layer-transition trial

- Retained the measured official island-side handoff graph and moved all long
  bridge corridors to B.Cu with ordinary source/handoff transitions.
- Native KiCad DRC measured 297 violations / 70 unconnected items, including
  17 shorts and 7 crossings; rejected the candidate.
- Confirmed the official handoff pair spacing is too tight for direct 0.50 mm
  vias and recorded the required separated-via plus short-F.Cu-dogbone rule.

2026-09-03 — Phase 17 separated-fanout bridge trial

- Tested separated 1 mm fanout via pairs with split F.Cu/B.Cu long corridors
  and short F.Cu dogbones into the official handoff graph.
- Native KiCad DRC measured 288 violations / 70 unconnected items, including
  23 crossings and 10 shorts; rejected the candidate.
- Retained the separated-fanout rule and continued Phase 17 only.

2026-09-03 — Phase 17 direct +5 mm CM5IO alignment fixture

- Added a direct-alignment mode to the native CM5IO transplant generator so
  all 189 official MDI segments land on the authoritative PiSXMe J7 pads.
- Focused native DRC showed zero MDI unconnected items, crossings, or shorts;
  15 remaining findings were intentionally omitted support circuitry.
- Recorded this as a focused MDI/source-leg subgate and kept Phase 17 open.

2026-09-03 — Phase 17 full direct CM5IO support transplant

- Applied the +5 mm native CM5IO transform with complete ESD, EDAC, center-
  tap, shield, LED, and ground support enabled.
- Native KiCad DRC reported zero unconnected items, shorts, and crossings;
  retained the remaining width/edge/mechanical findings as open closure work.
- Established direct CM5IO-to-J7 transplantation as the preferred Phase 17
  topology and kept acreage promotion gated.

2026-09-03 — Phase 17 exact EDAC center-tap mapping subgate

- Corrected EDAC pads 4/5 to NC and pads 11..14 to the clean ETH_CT1..4
  authority in the direct transplant fixture.
- Native PCB mapping regression passed; focused DRC retained zero MDI opens,
  shorts, and crossings with support intentionally omitted.
- Kept Phase 17 open for individually routed center-tap/support closure.

2026-09-03 — Phase 17 exact EDAC support experiment

- Rejected the prior artificial common-center-tap collapse and assigned EDAC
  pads 11..14 to distinct ETH_CT1..4 nets; mapping regression passed.
- Tested individually routed disposable support-header escapes; native DRC
  rejected their collisions with the through-hole launch field and shield.
- Preserved the official CM5IO MDI transplant as the selected topology and
  kept Phase 17 gated pending an authoritative four-net support implementation.

2026-09-03 — Phase 17 exact EDAC support escape rejection

- Ran a second individually routed ETH_CT1..4 support escape on permitted
  F.Cu/B.Cu layers and connected all disposable support pads.
- Native DRC rejected support-net shorts/crossings at the EDAC launch field;
  retained the direct CM5IO MDI topology and kept Phase 17 open.

2026-09-03 — Phase 17 four-net net-tie experiment

- Tested four explicit 0402 zero-ohm CT ties plus a 100 nF ground shunt in a
  disposable fixture.
- Native DRC rejected the source-side escape at 312 findings / 22
  unconnected items; rejected the candidate and kept production unchanged.

2026-09-03 — Phase 17 corrected EDAC RC source-transition trial

- Used the authoritative four 22 nF/75 ohm center-tap branches with explicit
  off-pad transitions and ordinary F.Cu/B.Cu vias.
- Native DRC rejected the disposable geometry at 311 findings / 2
  unconnected items; preserved the circuit authority and kept production
  unchanged.

2026-09-03 — Phase 17 EDAC manufacturer CT termination authority

- Verified the EDAC A70-series electrical circuit: four independent
  22 nF/100 V plus 75 ohm series branches from VC1..VC4 to a common node,
  with a 1 nF/2 kV return from that node to shield.
- Recorded the authoritative source URLs in the EDAC authority receipt and
  rejected the earlier zero-ohm/common-node fixture topology.

2026-09-03 — Phase 17 EDAC RC support fixture rejection

- Implemented the authoritative four independent 22 nF/100 V plus 75 ohm
  branches and 1 nF/2 kV shield return in the disposable fixture.
- Native DRC rejected the first physical escape at 262 findings / 8
  unconnected items; retained the authority and kept production unchanged.

2026-09-03 — Phase 17 B.Cu-local EDAC RC island

- Flipped the support footprints to B.Cu and added targeted CT4/CT2 source
  detours while preserving the official F.Cu MDI graph.
- Improved the disposable fixture to 238 findings, zero unconnected items,
  and zero shorts; four support crossings remain and Phase 17 stays open.

2026-09-03 — Phase 17 best exact EDAC RC corridor

- Added the off-pad CT2 transition and isolated shield transition to the
  B.Cu-local manufacturer RC support island.
- Native DRC reached 244 findings, zero unconnected items, zero shorts, and
  one remaining support crossing; mapping regression remained passing.

2026-09-03 — Phase 17 acreage integration trial rejected

- Applying the passing Ethernet island to the current acreage candidate
  produced 435 DRC findings and 453 unconnected items; this base is not a
  valid promotion target.
- Rejected the generated candidate and kept production unchanged. The exact
  EDAC support fixture remains electrically closed; the next step is to use
  the valid Phase 16 acreage checkpoint for integration.

2026-09-03 — Phase 17 official Ethernet acreage boundary conflict

- Applied the electrically closed CM5IO/EDAC fixture to the valid Phase 16
  routed ancestor. The overlay is rejected at 906 findings / 263 unconnected
  items because frozen `FB_CM5_5V` and `FUSED_12V_A` copper occupy the
  authoritative compact Ethernet corridor and CT support island.
- Preserved the rejected evidence and production state. A regulator-island
  translation is the smallest next change but crosses the plan's frozen
  non-Ethernet boundary; Phase 17 remains open and Phase 18+ gated.

2026-09-03 — Phase 17 Phase 16 ancestor baseline recheck

- Fresh `validation/phase3/test_phase16_pcie_route.py` passes on
  `ACREAGE_PCIE_PHASE16.kicad_pcb`.
- Its 92-finding / 241-unconnected baseline is distinct from the Ethernet
  overlay's 906-finding / 263-unconnected result, confirming the failure is
  introduced by the Ethernet integration geometry.

2026-09-04 — Phase 17 authorized local placement repair trials

- Tested coherent U3 island translations down 30 mm and left 30 mm, plus an
  Ethernet-local CT support translation with staggered source escapes. All
  were rejected by native DRC; the best U3-left trial remained at 896
  findings / 262 unconnected items and the shifted-support fixture retained
  CT launch shorts/crossings.
- Restored and revalidated the exact CM5IO/EDAC fixture: 237 findings, zero
  unconnected pads, zero shorts, and zero crossings, with mapping regressions
  passing. Production and the Phase 16 ancestor remain unchanged.

2026-09-04 — Phase 17 integration-path zone refill audit

- Corrected the disposable acreage overlay path to refill GND zones after
  replacing the Ethernet through-hole launch. The refilled Phase 16 overlay
  still failed at 820 findings / 271 unconnected items, proving stale zone
  fill was not the root cause.
- A coherent U3-left-30 mm trial with refilled zones improved to 778 findings
  / 270 unconnected items but retained power/Ethernet conflicts and was
  rejected. The default exact Ethernet fixture was restored and revalidated
  at 236 findings, zero unconnected pads, zero shorts, and zero crossings.

2026-09-04 — Phase 17 widened local repair trial

- Tested a coherent U3-right-70 mm translation and an Ethernet-support
  translation to the left. The former reduced total DRC count but increased
  unconnected debt to 291; the latter retained CT launch shorts/crossings.
- Rejected both candidates and restored the compact exact CM5IO fixture,
  which revalidated with zero unconnected pads, shorts, and crossings.

2026-09-04 — Phase 17 local repair wave disposition

- Completed the authorized U3-island and Ethernet-support translation wave,
  including the refilled-zone checks. No candidate cleared the combined
  power-input/frozen-corridor obstruction without new route conflicts or
  connectivity debt.
- Kept the exact CM5IO/EDAC fixture as the electrical authority and preserved
  all disposable candidates as evidence. Phase 17 remains open; Phase 18+
  remains gated.

2026-09-03 — Phase 17 exact EDAC RC support closure experiment

- Reordered the disposable B.Cu support island so CT2 routes directly to its
  own manufacturer-authoritative branch instead of detouring through the
  EDAC launch field.
- Native KiCad 10.0.5 DRC reports 235 findings but zero unconnected pads and
  no track-crossing, shorting, or unconnected-item categories. Ethernet
 mapping, authority, and fixture regressions pass. Production promotion and
 the full acreage Phase 17 gate remain pending.

2026-09-04 — Phase 17 authorized power-entry reopening disposition

- Built a disposable F1-only relocation harness from the validated Phase 16
  ancestor, preserving both 12-V input/fused nets and the downstream power
  trunk while moving the fuse as a coherent power-entry element.
- Tested F1 targets (20,40), (20,60), and (100,20) mm with the exact proven
  CM5IO/EDAC Ethernet overlay. All three were rejected: F1-body overlap was
  removed, but the fixed Ethernet launch still produced genuine shorts with
  adjacent U3 CM5_5V/FB_CM5_5V support geometry and retained connectivity debt.
- Preserved disposable boards and native DRC reports as negative evidence.
 Phase 17 remains open; no production promotion or Phase 18 work began.

2026-09-04 — Phase 17 combined F1/U3 diagnostic wave

- Combined the F1 relocation with four bounded U3 translations: down 50 mm,
  right 60 mm, right 80 mm, and right 60 mm/down 30 mm.
- Rejected every diagnostic variant for native crossings, missing
  connections, or real shorts involving core-PCIe, POWER_GND, protected-input,
  or regulator feedback nets.
- Evidence confirms that the next trial must re-author the complete U3
  regulator island and its explicit boundary copper; footprint-only movement
  is insufficient. Phase 17 remains open and Phase 18+ remains gated.

2026-09-04 — Phase 17 complete U3-island translation diagnostic

- Translated the complete U3 regulator footprint set and local regulator-net
  copper by (+48,+82) mm, combined with the F1 relocation at (20,40) mm.
- Native DRC showed no `shorting_items`, proving the coherent island move can
  remove the prior U3/Ethernet short class, but retained two crossings and
  271 unconnected pads including the Ethernet acreage handoff.
- Kept the candidate diagnostic-only. The next trial must explicitly
  re-author U3 external boundaries and repair the J7 Ethernet handoff before
  any Phase 17 promotion.

2026-09-04 — Phase 17 consultant unblocker synthesis

- Accepted the consultant recommendation to re-author the complete U3 island
  from Phase 15 authority with explicit `12V_PROTECTED`, `POWER_GND`,
  `CM5_5V`, feedback, RT, PG, and isolated internal-VCC boundaries.
- Preserved the required architecture and validation gates. No production
  promotion or later-phase work began.

2026-09-04 — Phase 17 generic Ethernet overlay-copy repair

- Corrected the KiCad 10 Python/SWIG `PCB_TRACK(item)` copy defect in the
  acreage Ethernet overlay by explicitly serializing and reconstructing
  scalar track/via geometry.
- Corrected rerun contained 576 real tracks and 26 `CM5_GBE_TD2_P` segments,
  reducing unconnected debt from 271 to 222 and removing the prior
  U3/Ethernet short class in the complete-U3 diagnostic.
- Rejected the candidate for genuine CT1/CT2 crossings, J7 launch and F1
  clearance violations, two relocated CM5_5V/CM5_PERST crossings, and
  remaining baseline connectivity debt. Isolated CM5IO fixture remains the
  electrical authority; Phase 17 and all later phases remain gated.

2026-09-04 — Phase 17 continuation contract

- Accepted consultant `PROPOSED_UNBLOCK`: re-author the complete U3 island
  from Phase 15 authority with explicit power/control boundaries and isolated
  internal VCC, rather than applying another footprint-only translation.
- Corrected overlay candidates retain a PASS on the Phase 16 focused PCIe
  check, but Phase 17 remains open because native DRC still reports Ethernet
  CT/launch and local power-boundary conflicts.

2026-09-04 — Phase 17 overlay serialization regression guard

- Extended the Ethernet fixture regression to require real nonzero MDI track
  geometry, guarding against the KiCad 10 SWIG copy-constructor defect found
  in the acreage overlay path.

2026-09-04 — TPSM63606 U3 manufacturer-authority audit

- Verified against TI TPSM63606 datasheet Rev. B that pin 5 is `VLDOIN` and
  pin 14 is `EN/SYNC`; neither is a generic VIN duplicate.
- Found the current generated U3 netlist/PCB assigns pins 1, 5, 14, and 16
  to `12V_PROTECTED`. This is a real schematic/materialization authority
  inconsistency and must be corrected before U3 re-authoring or Phase 17
  promotion.
- Kept the exact Ethernet fixture and Phase 16 PCIe evidence valid, but did
  not promote a PCB-only correction or begin Phase 18+.

2026-09-04 — TPSM63606 VLDOIN authority closure

- Corrected U3/U4/U5 pin-5 source labels to their output rails and preserved
  pin 14 as the protected-rail EN/SYNC input.
- Native netlist export, Phase 15 regulator-net authority regression, and
  regenerated PCB materialization all pass. U3 pin 5 now maps to
  `/REGULATORS/CM5_5V`; pins 1/14/16 remain `12V_PROTECTED`.
- Source authority is closed; physical U3 island re-authoring and Phase 17
  integration remain pending.

2026-09-04 — Correct TPSM63606 U3 source mapping

- Corrected the native `REGULATORS.kicad_sch` U3 pin-5 label from
  `12V_PROTECTED` to `CM5_5V` per TI's Rev. B datasheet `VLDOIN` contract.
- Preserved pin 14 as the separate `EN/SYNC` function and required
  source-level regeneration before any PCB promotion. No PCB-only net swap
  was accepted.

2026-09-04 — Phase 17 CM5 5 V hierarchy boundary correction

- Native netlist audit found `CORE_CM5` lacked its `CM5_5V` sheet port,
  isolating CM5 J7 5 V from the regulator output.
- Added the missing child port and root wire; KiCad export proves U3 pins
  5/8/9 and J7 pads 77/79/81/83/85/87 share `/CORE_CM5/CM5_5V`.
- Phase 15 authority and Phase 3 netlist regressions pass; this is a
  source-authority correction, not a PCB-only alias.

2026-09-04 — Phase 17 coherent F1/U3 repair harness

- Created a disposable no-copper boundary, restored reusable Phase 16 signal
  copper, moved F1 coherently, and reauthored U3 at `(90,165)`.
- Rejected the first trial after native DRC found local regulator escape
  crossings/shorts and a bridge-capacitor/CM5_PERST conflict; the exact
  CM5IO Ethernet fixture remained electrically closed.
- Preserved rejected artifacts, kept Phase 17 open, and began no Phase 18+
  work or clean release promotion.

2026-09-04 — Phase 17 lower U3/F1 TI-style placement variant

- Moved F1 to `(100,20)` and placed U3 at `(60,165)`, below the preserved
  CM5_PERST lane; shifted the adjacent U5 input-support row coherently.
- Rebuilt U3 VIN/VLDOIN/VOUT and FB/RT/PG copper from translated Phase-15
  geometry. U3-only DRC dropped to the inherited 236-finding baseline with
  no new U3 crossing category after the corrected C6 dogleg.
- Exact CM5IO Ethernet integration remains rejected at 436 findings due to
  CT1/CT2 and connector-field geometry; preserved the candidate and kept
  Phase 17 open. No Phase 18+ work or release promotion occurred.

2026-09-04 — Phase 17 CT1 opposite-layer transition trial

- Tested the proven Ethernet island with CT1 retained on B.Cu at its
  endpoints and moved to F.Cu only through an ordinary via-transitioned
  middle corridor.
- Rejected the first transition offset at EDAC pad 12; the second offset
  removed the CT1/CT2 integrated crossing and Ethernet short category.
- Candidate still fails the broader gate on connector-field clearances,
  inherited unconnected scaffold debt, and the pre-existing CM5_PERST /
  bridge-capacitor conflict. Phase 17 remains open; no Phase 18+ work began.
- The complementary CT2 opposite-layer transition was compared and rejected
  as one additional launch-clearance finding worse than the retained CT1
  variant; no release artifact was promoted.

2026-09-04 — Phase 17 explicit CM5 +5 V boundary trials

- Connected all six CM5 J7 +5 V lands to the canonical relocated U3 output in
  disposable variants. The B.Cu trunk crossed FB/PG quiet corridors; the
  left F.Cu trunk crossed fixed F2/CM5 keepouts and lower-island escapes.
- Rejected both routes and preserved their native DRC reports. Retained the
  lower `(60,165)` U3/F1 plus CT1-transition baseline; no release promotion or
  Phase 18+ work occurred.

2026-09-04 — Phase 17 authoritative CM5 fanout and lower-island reauthoring

- Inspected the official CM5IO Rev 2 PCB directly and matched its 0.20 mm
  +5 V fanout width for the PiSXMe J7 power launch. The corrected disposable
  path uses an ordinary 0.50/0.30 mm via outside the pad and B.Cu only through
  the module-body escape region.
- Reauthored the lower U3 output island: VLDOIN/VOUT is routed around the U3
  PGND pad field, support-capacitor returns use a separate via-transitioned
  corridor, and CM5 output support pads are explicitly tied.
- Native DRC for the best integrated disposable candidate reports 443 total
  findings, 428 inherited/unconnected acreage records, and zero
  `shorting_items` or `tracks_crossing` records. Remaining findings are
  Ethernet launch/mechanical and inherited scaffold debt, so Phase 17 remains
  open and no Phase 18+ or clean-release promotion occurred.

2026-09-04 — Phase 17 power-entry floorplan reopening

- Tested coherent F2 translations at `(100,120)` and `(140,120)` against the
  validated lower U3/F1 island. Both were rejected because the moved holder
  overlapped the fixed bridge-capacitor/support island and created native
  power-net shorts.
- Tested outer CM5 +5 V handoff corridors with F2 retained. The best west-side
  trial reduced the integrated DRC to 439 findings and eliminated the
  `tracks_crossing` category, but the CM5 connector launch still shorted its
  tightly interleaved neighboring pad field and the acreage scaffold retained
  unconnected debt.
- Preserved all disposable boards/reports, kept the lower `(60,165)` U3/F1
  placement as the working ancestor, and left Phase 17 open. No Phase 18+
  work or clean release promotion occurred.

2026-09-04 — Phase 17 consultant unblocker and CM5IO launch discriminator

- Consultant review classified the CM5 +5 V issue as corridor/launch geometry,
  not a malformed CM5 footprint, and recommended a pad-complete fixture with
  neighboring pads retained plus an ordinary-via escape outside the field.
- Executed the discriminator using the official CM5IO 0.20 mm fanout width,
  an ordinary 0.50/0.30 mm B.Cu transition, and a dedicated return corridor
  into the lower U3 island.
- The best integrated disposable ancestor has zero native DRC
  `shorting_items` and `tracks_crossing`; it still has inherited unconnected
  acreage records and known Ethernet launch/mechanical findings. Phase 17
  remains open, with no clean-release or Phase 18+ work started.

2026-09-04 — Phase 17 scoped Ethernet electrical regression

- Added `validation/phase3/test_phase17_ethernet_scoped_electrical.py` to
  separate Ethernet evidence from inherited acreage scaffold findings.
- The regression passes against the best disposable ancestor: all eight MDI,
  center-tap/common, and shield nets are present; native DRC has no true
  short/crossing category or Ethernet-specific unconnected record; and no
  Ethernet signal is placed on In1/In4.
- This does not waive full-board DRC, mechanical findings, or scaffold debt;
  Phase 17 remains open and no Phase 18+ work started.

2026-09-04 — Phase 17 status synchronization after CM5IO fanout proof

- Synchronized `PHASE3_STATUS.md` with the current `fe8add3` checkpoint.
- Confirmed the best lower-island integration ancestor has zero native true
  short/crossing categories for the CM5 power handoff, while the Phase 17
  Ethernet launch/mechanical and inherited acreage findings remain open.
- No clean PCB promotion or Phase 18+ work occurred.

2026-09-04 — Phase 17 integration receipt checkpoint

- Added `PHASE17_INTEGRATION_RECEIPT.md` with the current disposable ancestor,
  official CM5IO fanout authority, scoped Ethernet regression, native DRC
  evidence, and explicit `PHASE17_OPEN` gate decision.
- Confirmed source Phase 3/15 regressions and the scoped Ethernet electrical
  regression pass. Full native DRC remains open on inherited acreage debt and
  Ethernet mechanical/clearance/rule reconciliation; no clean PCB promotion
  or Phase 18+ work occurred.

2026-09-04 — Phase 17 fresh regeneration and CT1 discriminator

- Regenerated the current disposable acreage candidate from the Phase 16
  ancestor. The unmodified CM5IO center-tap overlay exposed a native CT1/CT2
  B.Cu crossing; the CT1-only F.Cu transition removed that crossing and the
  scoped Ethernet regression passed.
- Rejected CT2/CT3 doglegs after native DRC found true EDAC shield/MDI shorts.
  The experiment was reverted from the authoring path. Phase 17 remains open;
  no clean-board promotion or Phase 18+ work occurred.

2026-09-04 — Phase 17 connector-local center-tap reauthoring

- Tested outer B.Cu doglegs for CT2/CT3 around the authoritative EDAC
  mounting-hole and MagJack pad rows, with CT2 entering its CCT2 pad
  vertically. The fresh integrated candidate has no native crossing or true
  short categories, and the scoped Ethernet regression passes.
- Promoted this bounded repair to the disposable authoring path defaults;
  full Phase 17 remains open for inherited board DRC debt, impedance/rule
  reconciliation, and final mechanical review. No Phase 18+ work occurred.

2026-09-04 — Phase 17 JLC 100-ohm width emission

- Updated the disposable Ethernet integration emitter to use 0.13208 mm
  (5.2 mil) CM5 MDI copper, matching the current JLC 100-ohm basis while
  preserving the CM5IO topology. Connectivity and scoped Ethernet regression
  remain passing.
- Native DRC still sees the ancestor board's embedded 0.2000 mm minimum-width
  rule; the disposable project netclass did not override it. The mismatch is
  retained as an explicit Phase 17 rule-reconciliation item, not waived.

2026-09-04 — Phase 17 JLC rule-floor and return-artifact cleanup

- Applied the current JLC multilayer fabrication floor to the disposable
  Phase 17 base: 0.13208 mm minimum track width, 0.15 mm clearance, and
  0.30 mm drill. The fresh integrated candidate has no Ethernet-specific
  crossing, short, hole-clearance, width, drill, or unconnected findings.
- Removed only an unused CM5IO ETH_GND B.Cu tail/via artifact flagged
  dangling after transplantation; connected ESD/shield return copper and
  transition vias remain. Full Phase 17 stays open for inherited acreage and
  conservative mechanical-envelope review.

2026-09-04 — Phase 17 Ethernet route metrics regression

- Added `validation/phase3/test_phase17_ethernet_metrics.py`. Native KiCad
  measurement passes for all four F.Cu-only MDI pairs, exact EDAC J2 pad
  mapping, and 0.547–0.829 mm intra-pair skew against a 1.0 mm Rev-A bound.
- This is additive evidence; inherited acreage DRC and final mechanical
  review remain open, and no Phase 18+ work occurred.

2026-09-04 — Phase 17 disposable plane instantiation

- Added the frozen solid POWER_GND planes on In1 and In4 to the disposable
  lower-island generator before native refill. One scaffold ground open was
  removed; remaining opens belong to later return/via and low-speed routing
  work and are not Ethernet connectivity failures.

2026-09-04 — Phase 17 bounded power-entry reopening

- Added parameterized base selection to the disposable Ethernet placement
  trial and corrected the coherent F1 move path in the lower-island generator.
- The F1 `(240,40)` candidate exits the fuse bore and approaches Q1 pad 1
  without crossing Q1 pad 2, while preserving the approved power topology.
- Native DRC on `ACREAGE_PHASE17_F1RIGHT40_ETH3.kicad_pcb` has zero
  `tracks_crossing` and zero `shorting_items`; scoped Ethernet and native
  route-metrics regressions pass. Phase 17 remains open for inherited DRC,
mechanical, return-path, and impedance closure; Phase 18+ did not start.

2026-09-04 — Phase 17 power-entry focused regression

- Added `validation/phase3/test_phase17_power_entry_candidate.py` to verify
  the F1 `(240,40)` coherent move, F1/Q1 power-net authority, absence of
power-related short/crossing/hole findings, and plane-layer compliance.

2026-09-04 — Phase 17 mechanical authority boundary

- Exhausted the repository search for additional V100 cooler/backplate CAD or
  mating-stack measurements; none beyond the conservative envelope exists.
- The earliest failed gate and three bounded unblock options are published in
  `blocker.md`; Phase 18+ remains closed pending measurement or an explicit
  user decision to accept new Rev-A mechanical empirical risk.
- Preserved the existing `ETH_GND` schematic contract after rejecting an
  unproven net-collapse shortcut; Phase 17 remains open for formal return,
  mechanical, impedance, and inherited-acreage closure.

2026-09-04 — Phase 6 Ethernet regression authority refresh

- Updated the Phase 6 audit and receipt from the superseded TPD4E004DRYR
  assertion to the selected authoritative TI TPD4EUSB30DQAR used by the
  clean schematic and CM5IO-derived Ethernet implementation.
- No PCB, topology, or legacy artifact was changed.

2026-09-04 — Phase 17 Ethernet return authority correction

- Mapped the CM5IO fixture's source `ETH_GND` alias to clean `POWER_GND`,
  matching the official ESD and MagJack shield ground implementation.
- Updated the clean Ethernet child and focused regressions so the emitted
  PCB has no isolated Ethernet return net. Native regeneration remains
  required before Phase 17 closure.

2026-09-04 — Phase 17 ground-authority regeneration

- Regenerated `ACREAGE_PHASE17_F1RIGHT40_ETH_GROUND_FIXED.kicad_pcb` with
  the CM5IO `ETH_GND` source alias mapped to clean `POWER_GND`.
- Native DRC remained free of `tracks_crossing` and `shorting_items`; scoped
  Ethernet, route-metrics, power-entry, Phase 6, and netlist checks pass.

2026-09-04 — Phase 17 bottom-edge placement experiment

- Tested the CM5IO-faithful `LOCAL_BOTTOM_SPLIT` Ethernet placement against
  the corrected F1 base; native DRC found real MDI shorts/crossings and
  power-net interactions, so the variant was rejected and not promoted.

2026-09-04 — Phase 17 acreage mechanical interpretation reopening

- Retained the measured V100 cooling/backplate envelope as a visible
  `Dwgs.User` datum while removing its false universal `F.CrtYd` collision
  behavior from the disposable authoring path.
- Preserved actual component courtyards and the tall MagJack mechanical
  requirement.  The resulting DRC delta was 216 to 188 violations with no
  `MECH_V100` courtyard entries; Ethernet electrical proof remains unchanged.
- Consultant Crosscheck recommended the next bounded experiment: CM5-adjacent
  ESD/support with an outboard MagJack, followed by native mechanical and
  scoped routing validation. Phase 17 remains open.

2026-09-04 — Phase 17 soft-envelope candidate validation

- Reclassified the embedded `MECH_V100` courtyard graphic using native KiCad
  10 layer IDs in the disposable authoring path; saved
  `ACREAGE_PHASE17_COOLER_AIRFLOW_F1_ETH_SOFT.kicad_pcb`.
- Scoped Ethernet regression and native route metrics pass; all four pair
  skews remain below 1 mm and the candidate has no true Ethernet crossing or
  short. The full acreage DRC remains inherited scaffold debt, so Phase 17 is
  not yet closed.

2026-09-04 — Published recoverable Phase 17 placement update

- Updated the root blocker report to distinguish the cleared false cooler
  courtyard constraint from the remaining tall-MagJack placement work.
- Published commit `f3fbaa7` privately so the current evidence is readable
  outside the interactive UI; Phase 17 remains open and Phase 18 remains
  gated.

2026-09-04 — Phase 17 outboard island translation trials

- Added a generic disposable island-translation mode that leaves J7 fixed and
  moves the CM5IO ESD/MagJack/support geometry as a unit.
- Tested +180,+40 mm and +180,+100 mm outboard candidates. Native DRC found
  13/20 crossings and 18/26 shorts respectively; both were rejected.
- The failures identify blind translation of completed copper as the bad
  solution class. Phase 17 remains active for regenerated fanout/launch,
  consistent with the consultant recommendation.

2026-09-04 — Phase 17 regenerated split-fanout trial

- Added a disposable authoring path that removes translated source-side MDI
  copper and regenerates explicit J7-to-ESD lanes with ordinary through-vias.
- Native DRC rejected the +180,+40 mm trial with 22 crossings, 44 shorts, and
  six hole-clearance findings. This rejects the lane implementation, not the
  CM5IO topology; Phase 17 remains active.

2026-09-04 — Rev-A underside mechanical contract correction

- Removed the generic carrier-board cooler/backplate wording from the Phase 11
  floorplan and mechanical authority. Rev A assumes a standard cooler mounted
  to the SXM2 module itself; no generic underside exclusion or cooler-mounting
  holes are reserved.
- Retained only verified SXM2, board mounting, CM5/M.2, enclosure, and
  connector-access constraints. The underside is now available for Ethernet
  support/routing subject to those real constraints.
- Consultant unblocker recommended the next native-tool constrained Ethernet
  fixture, followed by staggered local escapes if needed. Phase 17 remains
  open.

2026-09-04 — Phase 17 top-edge staggered-ESD retry

- Moved the regenerated top-edge ESD pair farther from the J7 pad field and
  reran the complete MDI/CT/shield authoring path.
- Native DRC still rejected the candidate with 48 crossings, 53 shorts, and
  eight hole-clearance findings. The result is preserved as negative evidence;
  the next pass requires an explicit no-go constrained router.

2026-09-04 — Phase 17 right-edge MagJack discriminator

- Tested the authorized local placement class with the EDAC MagJack moved to
  `(282.5,53)` at 180 degrees and the CM5IO-derived ESD island retained near
  CM5.
- Regenerated the eight MDI nets with separate ordinary through-via lanes on
  F.Cu/B.Cu. Native KiCad DRC rejected the candidate with 332 violations and
  447 unconnected items, including Ethernet pair crossings/shorts against
  existing acreage copper and the ESD escape.
- Preserved the candidate and authoring script as negative evidence. Phase 17
  remains open; no Phase 18 work or validation-gate relaxation occurred.

2026-09-04 — Phase 17 ESD orientation retry

- Tested the top-edge regenerated Ethernet candidate with both ESD packages
  rotated to 0 degrees while preserving the authoritative nets and J2.
- Native DRC rejected it with 55 crossings, 35 shorts, and eight
  hole-clearance findings. Orientation alone is insufficient; pair-specific
  launch ordering remains the next routing target.

2026-09-04 — Phase 17 top-edge transition-via correction

- Corrected the top-edge generator's artificial defect where four B.Cu
  connector transitions shared `(90,45)`. Distinct 2 mm lanes reduced native
  DRC shorts from 53 to 36 and crossings from 48 to 44.
- The candidate remains rejected on real endpoint-order and corridor
  conflicts; no Phase 17 or Phase 18 gate was bypassed.

2026-09-04 — Phase 17 underside-contract native fixture retry

- Reran the native rotated Ethernet fixture after removing the hypothetical
  carrier cooler/backplate underside reservation. It remained rejected with
  163 violations, six crossings, ten shorts, and three unconnected items.
- This separates the mechanical contract from the remaining source/ESD escape
  problem; no generic underside constraint is being used to explain the
 failure.

2026-09-04 — Phase 17 west-split underside retry

- Reran the existing right-channel west-split Ethernet authoring class after
  removing the hypothetical underside cooler exclusion. Native DRC rejected
  it with 21 crossings, eight shorts, and 449 unconnected items.
- The historical west-split route remains rejected; Phase 17 continues toward
  a freshly authored top-edge/source-proximate solution.

2026-09-04 — Phase 17 fresh open-acreage island trial

- Moved U9/U6 to `(205,140)` / `(215,140)` and the EDAC MagJack to
  `(282.5,140)` at 180 degrees, then regenerated all eight MDI nets with
  ordinary F.Cu/B.Cu transitions.
- Native KiCad DRC rejected the trial with 285 violations and 445 unconnected
  items. The fresh placement removed the historical island collision, but the
  generated source lanes crossed F2/power-entry geometry and the ESD breakout.
- Preserved the trial as negative evidence. Phase 17 remains open and no
  Phase 18 work or validation-gate relaxation occurred.

2026-09-04 — Phase 17 west-perimeter launch trial

- Placed U9/U6 at `(220,25)` / `(230,25)` and J2 at `(282.5,25)` and routed
  the source around the west/top perimeter to avoid F2 and central frozen
  power/PCIe corridors.
- Native KiCad DRC rejected the trial with 272 violations and 449 unconnected
  items, including Ethernet pair crossings/shorts in the ESD fanout and edge
  launch.
- Preserved the trial as negative evidence; Phase 17 remains open and no
  Phase 18 work or validation-gate relaxation occurred.

2026-09-04 — Phase 17 top-edge regenerated-island trial

- Built the specialist-recommended top-edge candidate with staggered ESD
  beside J7, a top-edge EDAC MagJack, and regenerated MDI plus CT/shield
  support from actual pad centers.
- Native DRC rejected the manual lane set with 38 crossings, 65 shorts, eight
  hole-clearance findings, and 461 unconnected items. The candidate was not
  promoted; the next pass requires explicit native-routing no-go masks.

2026-09-04 — Phase 17 top-edge staggered-ESD retry

- Moved the regenerated top-edge ESD pair farther from the J7 pad field and
  reran the complete MDI/CT/shield authoring path.
- Native DRC still rejected the candidate with 48 crossings, 53 shorts, and
  eight hole-clearance findings. The result is preserved as negative evidence;
  the next pass requires an explicit no-go constrained router.

2026-09-04 — Phase 17 package-row dogbone correction

- Staggered shared ESD source/destination dogbones in the west-perimeter
  launch generator so each USON package row has an independent approach.
- Native KiCad DRC still rejected the candidate with 289 violations and 453
  unconnected items; crossings/shorts remain at the interleaved J7 fanout and
  ESD launch.
- Preserved the result as negative generator evidence. Phase 17 remains open.

2026-09-04 — Phase 17 source-column layer split retry

- Transitioned the right J7 Ethernet column immediately to B.Cu with
  ordinary vias while retaining the left column on F.Cu.
- Native KiCad DRC rejected the candidate with 286 violations and 453
  unconnected items; package/edge crossings and power-copper interactions
  remain.
- Preserved the retry as negative evidence; Phase 17 remains open.

2026-09-04 — Phase 17 co-located complete-island support witness

- Regenerated the official CM5IO MDI graph with the EDAC manufacturer
  four-branch CT support network enabled in the co-located island fixture.
- Native KiCad DRC found zero unconnected items, zero shorts, and zero MDI
  crossings; one localized CT3/CT4 B.Cu support crossing remains.
- Selected this as the best current Phase 17 ancestor for refinement. No
  production promotion or Phase 18 work occurred.

2026-09-04 — Phase 17 CT4 layer-separated support retry

- Added two ordinary CT4 support transitions so the CT4/CT3 branch escape is
  separated by layer while retaining the authoritative four-net CT network.
- Native KiCad DRC reports zero unconnected items, zero shorts, and zero track
  crossings on the complete disposable fixture. Remaining findings are
  clearance-class/inherited compact-fixture records requiring review.
- The co-located fixture remains the best Phase 17 ancestor; no production
  promotion or Phase 18 work occurred.

Direct KiCad `pcbnew` verification confirms the exact J7/J2 MDI and CT pad
maps on the co-located fixture. The production scoped test was not claimed as
a pass because the disposable fixture uses local support net names instead of
the production hierarchical spellings.

2026-09-04 — Phase 17 generic acreage integration retry

- Corrected the generic integration path to support a reusable-footprint mode
  for KiCad 10 SWIG stability (`PISXME_KEEP_FOOTPRINTS=1`).
- Generated `ACREAGE_PHASE17_COLOCATED_CT4_SPLIT.kicad_pcb` from the validated
  Phase 16 Ethernet ancestor plus the CT4-split fixture copper.
- Scoped Ethernet regression and route metrics passed; native DRC contained
  zero shorting items and zero track crossings, with the inherited acreage
  unrouted baseline explicitly retained (427 unconnected items).
- Phase 17 remains open; no clean-board promotion or Phase 18 work occurred.

The integrated candidate's 427 unconnected-item count matches its validated
ancestor exactly, confirming that the native DRC debt is inherited rather than
introduced by this Ethernet transplant. Power-entry validation also passed;
final Phase 17 closure remains pending the complete board gate.

2026-09-04 — Phase 17 Ethernet closure

- Corrected the CT4 F.Cu/B.Cu escape and removed the unrelated dangling
  ETH_GND fixture via. Native fixture DRC now has zero unconnected items,
  shorts, crossings, and dangling vias.
- Integrated acreage candidate retains the exact inherited DRC baseline,
  while scoped Ethernet, route metrics, and power-entry regressions pass.
- Removed the generic V100 cooler/backplate carrier reservation from the
  integration path per the Rev-A underside mechanical contract.
- Phase 17 is closed; the co-located candidate is the Phase 18 ancestor. No
  Phase 18 routing has started in this checkpoint.
2026-09-04 — Phase 18 storage authoring repair: native KiCad netlist now proves CM5 USB3 J7 pins 128/130/140/142 map to TI TUSB9261IPVP physical pins 45/46/42/43. The repair path uses authoritative TI pin numbers, separates the M.2 schematic instance, and adds a regression test. SATA/M.2 serialization remains gated pending a separate native-authoring correction; no USB3 routing or Phase 19 work began.
2026-09-04 — Phase 18 root hierarchy geometry repair: separated overlapping second-row child sheets and their root contract wires. Native netlist now proves SATA J3 pins 1/2/3/4 map to TUSB9261 pins 57/56/60/59, and M2_3V3 is isolated to J3/X7 without the prior COOLING/PCIe contamination. Native ERC still reports the pre-existing scaffold’s unconnected contract warnings; USB3 routing remains gated.
2026-09-04 — Phase 18 storage generator repair: made U7/J3 pin-row normalization idempotent and scoped label relocation to the intended symbol region. A second generator run is byte-stable; freshly exported KiCad netlist and the expanded USB3/SATA/M.2 regression both pass. Routing remains gated on the broader native ERC contract audit.
2026-09-04 — Phase 18 status correction: PHASE3_STATUS now reflects the live Phase 17-closed / Phase 18-storage-authority-repaired state; stale prose claiming Phase 17 was open was corrected. No USB3 routing or later-phase work has begun.
2026-09-04 — Phase 18 USB3 routing candidate: role-correct CM5 RX/TX to TUSB9261 SSTX/SSRX mapping is routed with ordinary through-vias on F.Cu/B.Cu. Native DRC has zero shorting items, crossings, and clearance violations; inherited regulator warnings and the 427-item acreage unconnected baseline are explicitly retained in the receipt. No Phase 19+ work started.
2026-09-04 — Phase 18 authority alignment: synchronized the committed storage schematic, generator, native netlist, and regression with the role-correct USB device-link mapping used by the routed candidate. CM5 RX maps to TUSB9261 SSTX and CM5 TX maps to TUSB9261 SSRX.
2026-09-04 — Phase 19 SATA experiments: two acreage candidates were rejected by native DRC for pad-field and frozen-PCIe-trunk interactions. The M.2/bridge authority and Phase 18 USB3 remain valid; the next experiment moves the connector/corridor beyond the PCIe trunk endpoint.
2026-09-04 — Phase 19 status: PHASE3_STATUS now identifies SATA routing as the active gate after two preserved, rejected candidates. Phase 20+ remains untouched.
2026-09-04 — Phase 19 endpoint experiment: moving J3 to the far right removed SATA shorts but produced six long-corridor crossings against frozen PCIe/PERST and pair-turn geometry. It is rejected and preserved; no gate was relaxed and Phase 20+ remains untouched.
2026-09-04 — Phase 19 placement wave 2: tested four additional local SATA corridors plus left/top and coordinated storage-island relocations. Native DRC rejected each for candidate-introduced U7 escape, frozen CM5/PCIe/reference, connector-body, or coordinated USB3 interactions. Added the wave-2 receipt and reproducible experiment scripts; Phase 19 remains active and Phase 20+ is untouched.
2026-09-04 — Phase 19 mid-acreage continuation: moved the storage island to the open mid-acreage region and tested coordinated/orthogonal SATA launches. The placement removed the frozen-trunk and body collisions; the remaining 205-207 DRC reports contain only local SATA launch ordering/clearance findings plus inherited acreage debt. Preserved the reproducible wave-3 scripts and reports; Phase 19 remains active.
2026-09-04 — Phase 19 endpoint continuation: the coordinated moved-U7 and smaller J3-only waves were rejected by native DRC for candidate endpoint/pad-field geometry; the latest coordinated snapshot is 232 violations / 426 unconnected. The Phase 18 U7/USB3 ancestor remains frozen and valid. A mid-acreage SATA V3 escape removed new short/crossing categories but is not coordinated closure because its moved U7 leaves USB3 stale. Evidence is in `pisxme/reva-clean/PHASE19_BLOCKER_REPORT.md`; Phase 20 remains gated.
2026-09-04 — Phase 19 outboard endpoint trial: kept the Phase 18 U7/USB3 ancestor unchanged and moved J3 to open mid-acreage at `(180,125)`, rotation 0°. Native DRC found 246 violations / 426 unconnected, including fixed-reference intersections and connector-launch crossings; the long detour is rejected and the Phase 19 gate remains active.
2026-09-04 — Phase 19 underside endpoint trial: kept U7/USB3 unchanged and placed J3 on B.Cu at `(180,125)`, rotation 0°. Native DRC found 243 violations / 430 unconnected; new TX source/connector crossings, one frozen B.Cu PCIe intersection, and connector-hole clearance remain. The underside trial is rejected; Phase 19 remains active.
2026-09-04 — Phase 19 local underside exhaustion: placed J3 on B.Cu at `(115,125)` below the unchanged U7/USB3 ancestor and tested opposite-side SATA approaches. Native DRC found 244 violations / 430 unconnected, with U7 pad-field conflicts, two local B.Cu crossings, and M.2 courtyard/clearance interactions. Combined local endpoint, outboard, mid-acreage, coordinated, and underside classes are exhausted; the remaining repair crosses the frozen U7/PCIe high-speed boundary, so Phase 19 is blocked and Phase 20 remains gated.
2026-09-04 — Phase 19 coordinated storage-island reopening: user authorized reopening U7/J3 as a coherent subsystem and regenerating USB3 plus SATA while preserving CM5, PCIe, architecture, stack, and layer contract. Fresh U7 `(120,140)` / J3 `(145,125)` candidate produced 208 native DRC violations / 426 unconnected; rejected for local USB3 landing crossings/PERST interaction. PCIe ancestor remained unchanged; Phase 19 is active and further co-located island candidates continue.
2026-09-04 — Phase 19 coordinated placement sweep: tested open-acreage U7/J3 placement class `(140,140)/(170,125)` and related variants without changing PCIe. Best initial candidate measured 224 native DRC violations / 426 unconnected; coordinate-derived SATA lane refinement measured 229 / 426 with new local SATA lane crossings and was rejected. Phase 19 remains active.
2026-09-04 — Phase 19 generator correction: restored validated CM5 USB3 source escapes and made moved-U7 landings coordinate-derived. Above-PCIe U7/J3 `(140,100)/(180,90)` measured 410 native DRC violations / 426 unconnected, including PCIe interactions and local SATA shorts; rejected. Phase 19 remains active.
2026-09-04 — Phase 19 native synchronization correction: the coordinated generator now serializes/reloads after U7/J3 movement before reading transformed pad coordinates. Corrected U7/J3 `(140,130)/(180,115)` candidates measured 227 and 229 native DRC violations / 426 unconnected across SATA escape variants; rejected for remaining local crossings. Phase 19 remains active.
2026-09-04 — Phase 19 staged USB3 rail experiment: isolated final vertical transitions with F.Cu staging hops on the synchronized U7/J3 island. Native DRC remained 229 violations / 426 unconnected and introduced SATA/USB3 interactions; rejected. Next work changes island orientation/relative placement.
2026-09-04 — Phase 19 orientation sweep: tested rotated U7/J3 island variants in open acreage. Native DRC measured 277/415 and 265/408 violations; rotation-only classes were rejected. Phase 19 remains active and the next repair targets coupled U7 pad-field escapes.
2026-09-04 — Phase 19 coordinated-base trial: reused the SATA V3 candidate and regenerated USB3 using synchronized moved-pad coordinates. Native DRC measured 226 violations / 426 unconnected with SATA/USB3 crossings and pad-field interactions; rejected. Phase 19 remains active.
2026-09-04 — Phase 19 USB3 isolation: removed SATA tracks from corrected U7 `(140,130)` candidate. Native DRC measured 211 violations / 430 unconnected; three shorts against regulator support geometry and one frozen PCIe B.Cu crossing remain. Phase 19 remains active.
2026-09-04 — Phase 19 orientation-aware trial: implemented specialist-recommended U7/J3 `(170,140)/(205,120)` at 90 degrees with a horizontal USB pad-row escape. Native DRC measured 378 violations / 426 unconnected; rejected for coordinated SATA/USB3 and local support interactions. Phase 19 remains active.
2026-09-04 — Phase 19 exact-source follow-up: preserved Phase 18 CM5 USB3 escape layering and used a direct F.Cu U7 detour; isolated USB3 measured 202 violations / 430 unconnected with no new USB3 shorts/crossings. Complete east-edge J3 `(240,140)` SATA trial measured 228 / 426 and was rejected for SATA connector/U7-field interactions. Phase 19 remains active.
2026-09-04 — Phase 19 valid SATA-V3 reuse check: disabled SATA regeneration and reauthored only USB3 on the existing V3 SATA board. Native DRC measured 242 violations / 426 unconnected with four USB3 short/crossing findings against preserved V3 copper. Simple overlay reuse was rejected; Phase 19 remains active.
2026-09-04 — Phase 19 transform audit: serialized U7 `(120,140)` at 90 degrees and found KiCad 10 USB row `y=135.5`, SATA row `x=124.5`, mirrored from the earlier predicted transform. Bottom-approach routing measured 219 USB-only violations / 430 unconnected and was rejected for entering the U7 body. Future routes use serialized pad coordinates.
2026-09-04 — Phase 19 regulator-support reopening: translated only C18/C19 to `(100,145)/(108,145)` on the U7 `(140,130)` USB3 isolation candidate. Native DRC remained 202 violations / 430 unconnected, matching the Phase 18 baseline class apart from one local clearance; the three regulator shorts were removed. Phase 19 remains active.
2026-09-04 — Phase 19 SATA authority gap: TI TUSB9261 implementation guidance requires four inline <=0402 SATA coupling capacitors, one per conductor, symmetrically near J3, with no C-packs. The clean storage schematic currently has none. Added `PHASE19_SATA_AC_CAP_RECEIPT.md`; Phase 19 remains active and cannot close until schematic, netlist, placement, and routing are corrected.
2026-09-04 — Phase 19 SATA coupling implementation: made the Phase 7 storage authoring path emit four idempotent C30-C33 100 nF X7R 0402 capacitors with split bridge/socket nets, added the local 0402 land pattern and materializer positions, and added a regression audit. Native child-netlist export proves U7-to-cap-to-J3 connectivity for all four conductors. PCB-side coordinated routing/materialization remains the active Phase 19 gate.
2026-09-04 — Phase 19 blocker evidence refresh: updated the active blocker report with the native child-netlist proof and explicit remaining PCB-side obligation. No Phase 20 work started and no validation gate was relaxed.
2026-09-04 — Phase 19 coordinated storage authoring repair: removed donor C30-C33 regulator footprints before loading the required local 0402 parts, and preserved newly-created socket-side net codes across KiCad 10 synchronization. A fresh U7/J3 candidate serialized the correct split mapping but measured 262 native DRC violations and was rejected; Phase 19 remains active.
2026-09-04 — Phase 19 USB3 escape refinement: made the coordinated storage generator derive U7 landing coordinates and approach the moved QFN row horizontally. USB-only V3 measured 200 native DRC violations but retained inherited CM5/PCIe corridor crossings and was rejected; Phase 19 remains active.
2026-09-04 — Phase 19 coordinated corridor refinement: used the corrected USB3 escape, rotated 0402 coupling parts, split-net SATA routes, and separate outer-layer pair corridors. The V3 candidate measured 206 native DRC violations with one J3 auxiliary-pad short and two corridor crossings; rejected, Phase 19 remains active.
2026-09-04 — Phase 19 synchronized corridor refinement: separated USB3 TX_P onto the lower B.Cu corridor and refined SATA cap lanes. `PHASE19_LIVE3` measured 207 native DRC violations with zero shorting items and one remaining USB3 crossing, plus inherited clearance/hole/unconnected debt; rejected, Phase 19 remains active.
2026-09-04 — Phase 19 coordinated-island continuation: made C30-C33 follow the moved U7 x-coordinate and added opt-in direct USB3 landings for the validated Phase-18 U7 neighborhood. USB-only U7 `(110,105)` regeneration has zero USB3 crossings/shorts; the first complete orthogonal SATA launch at J3 `(150,110)` rotation 0 was rejected for RX_N/frozen-PCIe crossing, connector launch shorts, and a power-pad-adjacent via. Phase 19 remains active; Phase 20+ untouched.
2026-09-04 — Phase 19 independent review and V3-cap continuation: confirmed the live USB3 crossing is RX_N versus TX_N and identified the adjacent U7 pad-field constraint. Materialized C30-C33 inline in the proven V3 SATA lanes; KiCad 10 native DRC measured 316 violations, zero shorting items, and one RX_N/PCIe B.Cu crossing. Rejected pending a PCIe-clear RX_N transition, USB3 skew/return-via audit, and the noted U7 clock-pad authority check. Phase 19 remains active; Phase 20+ untouched.
2026-09-04 — Phase 19 coordinated repath baseline: combined V3 split-cap SATA routing with a four-branch USB3 repath and filled planes after ordinary via insertion. Native DRC measured 189 violations with zero tracks-crossing and zero shorting-item records; inherited baseline clearances remain. Removed stale serialized U7 duplicate net fields on pads 5-12 while preserving mapped pads 42/43/45/46 and 57/56/60/59. Measured USB3 lengths are 108.473/87.104/81.453/61.407 mm and SATA full-path sums are 24.856/80.225/48.975/59.775 mm; these remain SI-unacceptable and require controlled tuning. Phase 19 remains active and Phase 20+ untouched.
2026-09-04 — Phase 19 clock authority audit: TI's TUSB9261IPVP pinout confirms 52=XI, 54=XO, 53=VSSOSC and requires a 40 MHz reference-clock network. The clean twelve-pin storage abstraction omits that network, so this genuine authority gap is recorded for correction before Phase 19 closure. The cleaned stable V3-cap coordinated candidate re-ran at 189 native DRC violations / 413 unconnected with zero crossings and zero shorts, but remains rejected pending clock, SI length/skew, and return-transition closure.
2026-09-04 — Phase 19 hierarchy/materialization repair: corrected the generic storage authoring path so clock library symbols remain inside the KiCad child library, added U7.30/U7.31 frequency selection and the distinct XI/XO/VSSOSC crystal network, and verified idempotent native root export plus 74-component/238-net materialization. Phase 19 remains active pending physical clock-loop routing and complete USB3/SATA SI closure; Phase 20+ untouched.
2026-09-04 — Phase 19 clock authority refinement: added U7.30/U7.31 and isolated BRIDGE_VSSOSC to the generic storage authoring/materialization path; native root export and reload now preserve all oscillator pins and Y1/R23/C42/C43 pad nets. A direct F.Cu clock-loop experiment added crossings/shorts and was rejected at 212 DRC violations / 415 unconnected versus the 189-violation coordinated baseline. Phase 19 remains active; Phase 20+ untouched.
2026-09-04 — Phase 19 clock escape experiments: an underside ordinary-via clock escape was tested against the coordinated storage candidate and rejected at 249 native DRC violations / 428 unconnected with new clock/high-speed crossings and shorts. Both routed clock classes are preserved as rejected evidence; schematic/materialization authority remains valid and Phase 19 stays active.
2026-09-04 — Phase 19 open-side clock corridor experiment: moved the authoritative Y1/R23/C42/C43 support island into east-side acreage around U7 `(250,105)` and routed from native KiCad-transformed pad coordinates. Native DRC measured 271 violations / 475 unconnected versus 206 / 484 inherited; rejected for adjacent U7 clock-pad fanout crossings and VSSOSC return interaction. Phase 19 remains active; Phase 20+ untouched.
2026-09-04 — Phase 19 consultant unblocker review and perpendicular-first clock follow-up: identified the shared row-parallel breakout defect at U7 pads 52/53/54 and the invalid 0.15 mm trial width against the 0.20 mm board minimum. Corrected the initial escape and reran native DRC at 225 violations / 474 unconnected; downstream XI/XO/VSSOSC branch crossings remain, so the class is rejected. Phase 19 remains active; Phase 20+ untouched.
2026-09-04 — Phase 19 clock experiment hygiene: removed inherited clock-net tracks before rerunning the perpendicular-first open-corridor trial, so the DRC delta is attributable to the current authoring route. Native DRC remained 225 violations / 474 unconnected; the remaining records are downstream clock-branch geometry, not stale donor copper. Phase 19 remains active; Phase 20+ untouched.
2026-09-04 — Phase 19 minimal clock fixture: isolated U7/Y1/R23/C42/C43 from unrelated acreage copper and tested perpendicular-first U7 escape with ordinary-via private VSSOSC return. Native DRC reduced to 15 violations / 2 unconnected, with no clock shorts; two local escape crossings and the fixture’s isolated FREQSEL tie remain. Phase 19 remains active; Phase 20+ untouched.
2026-09-04 — Phase 19 clock integration baseline: applied the corrected minimal U7 clock topology with a relative transform to the materialized acreage candidate, removed inherited clock copper, and corrected dynamic pad-coordinate serialization. Native DRC measured 207 violations / 473 unconnected versus 206 baseline, with no new clock crossings, shorts, or runaway VSSOSC segments. Phase 19 remains active; Phase 20+ untouched.
2026-09-04 — Phase 19 clock topology closure fixture and transplant test: minimal U7/Y1/R23/C42/C43 fixture reached zero unconnected pads, zero clock shorts, and zero clock crossings with only cosmetic DRC warnings. Relative transplant to the coordinated U7/J3 candidate was rejected at 406 violations / 471 unconnected because live USB3/SATA copper occupies the translated clock corridors. Phase 19 remains active; Phase 20+ untouched.
2026-09-04 — Phase 19 rotated north-corridor clock transplant: reflected the clean minimal clock topology for coordinated U7 rotation and removed inherited clock tracks before rerouting. Native DRC measured 509 violations / 471 unconnected with new clock-to-live-storage/power interactions; rejected. Fixed-offset transplant class is exhausted; next placement must use a live-copper occupancy map. Phase 19 remains active; Phase 20+ untouched.
2026-09-04 — Phase 19 live-copper occupancy audit: native geometry confirmed U7 top-facing clock pads at 52/XI `(143.0,105.5)`, 53/VSSOSC `(142.5,105.5)`, 54/XO `(142.0,105.5)` and mapped the occupied F.Cu SATA/USB3/PCIe fields plus the narrow upper/left B.Cu window. Blind fixed-offset clock transplants are rejected; next candidate uses a deliberate perpendicular escape and mapped B.Cu support island. Phase 19 remains active; Phase 20+ untouched.
2026-09-04 — Phase 19 mapped B.Cu clock-island trial: used live occupancy data, top-row U7 F.Cu escape, ordinary transitions, and B.Cu Y1/R23/C42/C43 support. Native DRC measured 386 violations / 477 unconnected with new clock-to-live-storage interactions; rejected as an insufficient corridor. Minimal clock fixture remains electrically closed. Phase 19 remains active; Phase 20+ untouched.
2026-09-04 — Phase 19 south-acreage clock corridor audit: the explicit Rev-A underside contract leaves a measured open south corridor, but the first transplant was rejected as malformed fixture evidence after native DRC identified wrong support endpoints, a VSSOSC/power-pad collision, and local Y1-field crossings. No Phase 19 or Phase 20 gate was closed.
2026-09-04 — Phase 19 clock control-fixture rerun: regenerated the isolated authoritative TUSB9261 clock network; native KiCad DRC reports 12 cosmetic warnings, zero unconnected pads, and no clock shorting or crossing records. Acreage integration remains open.
2026-09-04 — Phase 19 corrected south-island clock trial: exact support-pad endpoints and an outboard support island were used; native DRC measured 417 violations / 466 unconnected. New clock failures are long F.Cu trunks through J3/J1 pad fields and Y1 return dogbones, so the candidate was rejected. Acreage integration remains open.
2026-09-04 — Phase 19 pre-field B.Cu trunk trial: moved the long clock trunks to separated ordinary-via B.Cu lanes; native DRC measured 391 violations / 466 unconnected. The remaining local transition/Y1 dogbone crossings reject the experiment; the south support acreage remains physically viable.
2026-09-04 — Phase 19 ordered B.Cu clock-trunk trial: used separated monotonic B.Cu lanes before the J1/J3 fields; native DRC measured 391 violations / 466 unconnected. U7-side transition and Y1 dogbone geometry still fail, so clock-only overlays are exhausted and the next candidate must regenerate the coordinated storage island.
2026-09-04 — Phase 19 coordinated-generator invocation correction: added explicit `--P19_NAME=value` argument handling so native KiCad Flatpak candidate generation is deterministic; no unverified rotated-U7 artifact was promoted.
2026-09-04 — Phase 19 coordinated U7 rotation-270 trial: generated a distinct U7/J3 USB3/SATA candidate with U7 at `(140,130)` rotation `270°`; adding the authoritative clock network measured 486 DRC violations / 416 unconnected. Rejected because generated SATA still occupies the clock pad-row escape and inherited zone-fill debt remains; PCIe and architecture unchanged.
2026-09-04 — Phase 19 native generator crash repair and rot270 artifact: isolated the KiCad 10 Flatpak zone-enumeration SWIG crash and made disposable zone refill opt-in; generated the distinct rot270 U7/J3 candidate and recorded its clock-overlay rejection at 486 DRC / 416 unconnected.
2026-09-04 — Phase 19 U7 rotation-270 pad-field fixture: clock-west/SATA-east escapes were tested around the exact U7 pad row; native DRC found zero crossings and zero shorts, with only intentional dangling ends and unrelated support-pin unconnected items. The package escape is legal; coordinated SATA authoring remains open.
2026-09-04 — Phase 19 rotation-aware SATA launch generation: added the opt-in rot270 SATA branch with reloaded transformed pad endpoints and an outboard coupling-capacitor island. Native DRC improved to 340 / 418 from 403 / 413 on the prior rot270 candidate; not promoted because clock integration and full connectivity remain open.
2026-09-04 — Phase 19 rotation-aware SATA launch result: corrected U7 rotation-270 capacitor and pad launch generation produced `PHASE19_COORDINATED_U7ROT270_SATAFIX.kicad_pcb` at 340 DRC / 418 unconnected versus 403 / 413 prior. This is the new ancestor for clock integration, not a Phase 19 pass.
2026-09-04 — Phase 19 rotated minimal-topology transplant: rotated the passing clock graph and its support footprints into U7 rotation 270; native DRC measured 416 / 424 with new local clock crossings and shorts. Rigid transform class rejected; corrected SATA ancestor retained.
2026-09-04 — Phase 19 native footprint-rotation correction: corrected the support footprint orientation to KiCad's native 270° convention and shifted the transformed clock island west; native DRC improved to 388 / 420 and removed the prior local support short class. West USB3 crossings and inherited zone debt remain.
2026-09-04 — Phase 19 corrected-SATA clock-west trial: reran the authoritative clock network on the corrected rot270 SATA ancestor; native DRC improved to 372 / 423 from 486 / 416, but local Y1 fanout and inherited connectivity debt remain. Candidate rejected; rotation-aware SATA ancestor retained.
2026-09-04 — Phase 19 generalized rot270 storage-island trial: replaced absolute SATA launch coordinates with target-relative generation and evaluated U7 `(160,140)` / J3 `(230,120)`. SATA-only DRC reached 325 / 418; clock overlay reached 371 / 420. Candidate rejected; sweep infrastructure retained.
2026-09-04 — Phase 19 west-shifted clock transform follow-up: native 270° support orientation and west shift on the generalized rot270 SATA candidate measured 371 / 420; prior Y1-field shorts are absent, but west clock/USB3 crossings remain. Local routing blocker remains active.
2026-09-04 — Phase 19 local underside clock-island follow-up: added the parameterized `phase19_clock_local_bcu.py` path with lateral-first U7 rot270 escape, ordinary through-via transitions, and underside Y1/R23/C42/C43 placement. Corrected near and south support trials measured 365/429 and 366/429 native DRC/unconnected, retaining local planar support-field crossings; both rejected. Phase 19 remains active and Phase 20+ untouched.
2026-09-05 — Phase 19 clock support placement sweep: tested upper-right and lower-edge underside support placements at four acreage coordinates. Native DRC remained 364–375 violations with 429 unconnected items; support-field crossings/shorts and inherited corridor interactions persisted. No candidate promoted; Phase 19 remains active and Phase 20+ untouched.
2026-09-05 — Phase 19 coordinated-generator placement sweep: tested three U7/J3 placements with the V3 SATA authoring branch. Native DRC measured 426/413, 473/413, and 364/413 violations/unconnected; 13–24 crossing/short records remained. All rejected; clock-aware coordinated generation and full storage connectivity remain open.
2026-09-05 — Phase 19 orthogonal coordinated-generator sweep: tested three U7 rotation-180/J3 rotation-0 placements. Native DRC measured 434/413, 377/413, and 416/413 violations/unconnected; 17–24 crossing/short records remained. Coordinate-only movement rejected; next work replaces stale bridge/socket route topology with live endpoints and co-generates clock.
2026-09-05 — Phase 19 live U7 clock-transform correction: generalized the clock fixture for rotation-180 U7 at `(120,140)`, landing on serialized pads 52/53/54 at `(123,135.5)`, `(122.5,135.5)`, and `(122,135.5)`. Corrected candidate measured 234/413 DRC/unconnected; west-shifted run retained 10 clock-related crossing/short records. Stale-coordinate hypothesis closed; coordinated U7/J3/clock regeneration remains active.
2026-09-05 — Phase 19 live-U7 clock-transform shift sweep: tested support shifts from -5 to -40 mm on the best no-crossing ancestor. Best was -20 mm at 245 DRC / 417 unconnected with 9 crossing/short records. Clock-only coordinate tuning rejected; a dedicated clock corridor must be created during coordinated storage regeneration.
2026-09-05 — Phase 19 outboard storage-room experiment: moved U7 to `(180,140)` and J3 to `(250,100)`, then applied the corrected clock transform. Native DRC retained 417 unconnected items and 29 crossing/short records; candidate rejected. PCIe and architecture unchanged; Phase 19 remains active.
2026-09-05 — Phase 19 occupancy-aware clock routing diagnostic: derived live U7 clock pads and attempted obstacle-aware B.Cu routing into open acreage. The inherited B.Cu corridor prevented completion of a passive branch; the partial artifact was not promoted. Full U7/J3/clock co-placement remains required; Phase 20+ untouched.
2026-09-04 — Phase 19 open-acreage live-endpoint coordinated trial: moved U7/J3 to `(260,105)`/`(290,105)` with U7 rotation 270 and J3 rotation 0, then regenerated USB3/SATA/40-MHz clock from the synchronized candidate. Native DRC measured 311 violations and 478 unconnected items; rotated pad-field and clock/SATA local crossings remain. Candidate rejected; Phase 19 remains open and Phase 20+ untouched.
2026-09-04 — Phase 19 separated-M.2 live-endpoint variant: retained U7 `(260,105)` rotation 270 and moved J3 to `(290,145)` rotation 0. Native DRC measured 374 violations and 478 unconnected items; connector separation improved the launch class, but U7 SATA/clock local crossings and one USB3 return-via collision remain. Candidate rejected; Phase 19 remains open and Phase 20+ untouched.
2026-09-05 — Phase 19 consultant-reviewed legal 90-degree J3 trial: U7 `(240,105)` rotation 270, J3 `(270,145)` rotation 90, stale donor M.2 keepout removed, and USB3/SATA/40-MHz clock regenerated together. Native DRC measured 390 violations and 478 unconnected items; U7-side SATA/clock escapes still cross existing regulator geometry. Candidate rejected; Phase 19 remains open and Phase 20+ untouched.
2026-09-05 — Phase 19 opposite-side coupling/socket trial: U7 `(260,105)` rotation 270, C30-C33 west of U7, J3 `(200,140)` rotation 90, stale M.2 keepout removed, and USB3/SATA/40-MHz clock regenerated together. Native DRC measured 377 violations and 476 unconnected items; live SATA/clock local crossings remain. Candidate rejected; Phase 19 remains open and Phase 20+ untouched.
2026-09-05 — Phase 19 farther-outboard bridge trial: U7 `(280,105)` rotation 270, J3 `(200,140)` rotation 90, C30-C33 between bridge and socket, and USB3/SATA/40-MHz clock regenerated together. Native DRC measured 384 violations and 476 unconnected items; clock/SATA local escape crossings remain. Candidate rejected; Phase 19 remains open and Phase 20+ untouched.
2026-09-05 — Phase 19 topology-vs-integration fixture: created a KiCad-loadable storage-only S-expression donor retaining J7/U7/J3/C30-C33/Y1/R23/C42/C43. Native DRC measured 92/78 before routing and 322/70 after coordinated live-endpoint routing; candidate SATA/clock crossings remain. Fixture rejected; Phase 19 remains open and Phase 20+ untouched.
2026-09-05 — Phase 19 corrected USB3-only authoring diagnostic: fixed explicit command-line SATA/clock suppression, live J7/U7 pad assignment, missing source-to-via fanout, and sub-minimum 0.132 mm harness width. Native isolated fixture DRC measured 84/75 with zero USB3 source-side crossings or shorts; two U7 final-escape clearances remain. Phase 19 stays open; no Phase 20+ work.
2026-09-05 — Phase 19 U7 USB3 escape follow-up: offset all four transition vias away from the adjacent U7 pad field. Native isolated fixture DRC measured 78/75 with zero USB3 crossings, shorts, dangling vias, or source fanout opens. M.2/clock baseline remains intentionally unrouted; Phase 19 stays open.
2026-09-05 — Phase 19 clock-support relocation trial: moved Y1/R23/C42/C43 beside U7 and isolated clock routing. Native DRC measured 116/70; hard-coded XI/XO/VSSOSC fanout still crossed and shorted local support. Rejected; live-endpoint clock regeneration required.
2026-09-05 — Phase 19 diagnostic control: added explicit USB3 suppression to the coordinated fixture so USB3, SATA, and clock authoring classes can be validated independently without contaminating evidence. Phase 19 remains open.
2026-09-05 — Phase 19 live-endpoint clock regeneration trial: replaced hard-coded clock fanout with serialized U7/support endpoints, local XI F.Cu, XO B.Cu transitions, and explicit VSSOSC return. Native DRC measured 96/67, an improvement but still with crossings and clearances. Rejected; Phase 19 remains open.
2026-09-05 — Phase 19 clock-only diagnostic control: skip SATA before endpoint access so clock evidence is not contaminated by storage coupling paths. Native isolated clock run measured 96/62; clock crossings and clearances remain. Phase 19 stays open.
2026-09-05 — Phase 19 separated-clock-bus trial: isolated XO and VSSOSC onto distinct B.Cu corridors using live endpoints. Native clock-only DRC measured 92/62 with zero clock crossings or clock signal shorts; U7 pad-field clearances remain. Phase 19 stays open.
2026-09-05 — Phase 19 U7 clock escape follow-up: local pad-field escape adjustment measured 93/62 and reintroduced one clock crossing. Rejected; separated-clock-bus 92/62 remains the best known clock candidate.
2026-09-05 — Phase 19 fine-width clock escape trial: 0.100 mm clock routes against the unchanged 0.200 mm board minimum measured 120/62 with track-width errors. Rejected; no fabrication rule relaxation.
2026-09-05 — Phase 19 clock-oracle post-generation transplant: applied passing minimal clock geometry over fresh USB/SATA generation. Combined native DRC measured 248/62; rejection remains in candidate USB/SATA crossings and shorts, with no new clock-crossing class. Phase 19 stays open.
2026-09-05 — Phase 19 rotated-270-degree SATA launch trial: monotonic cap row plus split F.Cu/B.Cu pair assignment measured 101/75 native DRC/unconnected. Rejected for U7 RX, coupling-transition, and M.2 dogbone errors; Phase 19 remains open.
2026-09-05 — Phase 19 SATA transition follow-up: moved RXP coupling transition off the C32 pad and separated socket-side vias; native DRC improved to 96/75 with prior U7 RX/coupling shorts removed. Dense J3 launch remains; Phase 19 stays open.
2026-09-05 — Phase 19 SATA transition authoring correction: ordinary offset vias and F.Cu dogbones fixed capacitor B.Cu connectivity; mirrored rotated-U7 capacitor order produced SATA-only zero-short/zero-crossing evidence (78 total baseline records). Coordinated USB3 regeneration still had five USB3/SATA crossings; candidate rejected and Phase 19 remains open.
2026-09-05 — Phase 19 coordinated east-USB3 trial: regenerated USB3 around the rotated SATA oracle; native DRC measured 91 records with one short and nine crossings from source fanout and U7 landing ordering. Rejected; Phase 19 remains open.
2026-09-05 — Phase 19 preserved-source top/east USB3 trial: retained CM5 breakout and lifted four lanes to ordered upper B.Cu corridors; native DRC measured 88 records with nine USB3 crossings. Rejected; next candidate requires pair-aware co-placement rather than independent lane translation.
2026-09-05 — Phase 19 pair-preserving split-layer USB3 trial: RX and TX were kept as separate differential-pair corridors around the clean SATA oracle; native DRC measured 92 records with five USB3 crossings. Rejected; next candidate must change U7/J3 placement or U7 orientation.
2026-09-05 — Phase 19 lower-acreage U7/J3 trial: moved U7 to (240,145) and J3 to (200,170) with serialized-coordinate USB3/SATA regeneration; native DRC measured 444 records, 12 crossings, four shorts, and 413 unconnected. Rejected; next candidate uses pair-aware vertical U7 entry.
2026-09-05 — Phase 19 pair-aware vertical U7-entry trial: separated RX and TX corridors around the SATA oracle and approached U7 from opposite sides; native DRC measured 94 records with four crossings and two shorts. Rejected; U7 orientation must change to avoid the single-row USB fan-in.
2026-09-05 — Phase 19 U7 rotation-0 orientation study: verticalized the USB3 side row and tested pair-aware entry with SATA/clock suppressed; native DRC measured 84 records, two USB3 crossings, and zero focused shorts. Not promoted; side-row dogbones and SATA regeneration remain open.
2026-09-05 — Phase 19 U7 rotation-90 USB3 diagnostic: tested the orthogonal U7 orientation with SATA suppressed; native DRC measured 211 records, five crossings, and one CM5_USB3_TX_P-to-POWER_GND short. Rejected; the coordinated storage island remains open.
2026-09-05 — Phase 19 U7 rotation-180 USB3 diagnostic: tested the mirrored side-row orientation with SATA suppressed; native DRC measured 223 records, two crossings, and seven shorts. Rejected. Corrected the prior rotation-0 receipt to record its two actual shorts.
2026-09-05 — Phase 19 source-order USB3 staircase: added serialized J7-order fanout and ordinary signal-via transitions; isolated USB3 reached zero crossings and zero shorts, while coordinated storage trial remained open with two USB/SATA B.Cu crossings.
2026-09-05 — Phase 19 coordinated landing-separation follow-up: moved RX_P/TX_N below the SATA RX_P diagonal; native DRC measured 213 records with three crossings and one F2 FUSED_12V_B short. Rejected; corridor coexistence remains open.
2026-09-05 — Phase 19 outboard four-trunk coordinated trial: moved all USB3 landings beyond the SATA diagonal; native DRC measured 210 records with three crossings and no shorting records. Rejected; next class uses pair-layer separation around CM5 support geometry.
2026-09-05 — Phase 19 RX-F/TX-B pair-layer coordinated trial: separated USB3 pairs by signal layer against the SATA270 oracle; native DRC measured 217 records with two crossings and four shorts. Rejected; complete storage-island relocation is next.
2026-09-05 — Phase 19 SATA RX_P F.Cu coordinated trial: moved the SATA RX_P corridor to F.Cu against the USB B.Cu corridors; native DRC measured 215 records with five crossings, one U7 NC-pad short, and an additional F.Cu SATA crossing. Rejected.
2026-09-05 — Phase 19 high/low RX-F TX-B trial: moved RX F.Cu corridors above CM5 support while retaining TX B.Cu; native DRC measured 212 records with four crossings and three shorts. Rejected; current-placement layer permutations are exhausted.
2026-09-05 — Phase 19 SATA RX_P lower-side bypass trial: routed RX_P around the local island on B.Cu; native DRC measured 214 records with five crossings and no shorts. Rejected; three SATA junction and two USB trunk crossings remain.
2026-09-05 — Phase 19 parameterized relocation study: added coherent U7/J3 placement arguments and tested U7 (240,105), J3 (160,140) USB-only; native DRC measured 250 records with three crossings and four shorts. Rejected as the initial relocation baseline.
2026-09-05 — Phase 19 relocation baseline audit: the existing mid-acreage U7/J3 author at (110,105)/(145,125) measured 320 native DRC records, four crossings, five shorts, and 426 unconnected. Rejected; fresh parameterized island author remains required.
2026-09-05 — Phase 19 legacy mid-acreage relocation baseline: ran the existing coordinated U7/J3 author at its mid-acreage placement; native DRC measured 320 records with four crossings, five shorts, and 426 unconnected. Rejected as a relocation ancestor.
2026-09-05 — Phase 19 coordinated U7/J3 relocation progress: U7 (270,105), J3 (190,140) focused SATA270+USB3 regeneration reached zero native shorting_items and zero tracks_crossing records; full-support oscillator regeneration remains rejected with six shorts and six crossings, so Phase 19 remains open.
2026-09-05 — Phase 19 oscillator-support follow-up: corrected relocation coordinate handling, but full U7/J3 candidate still measured six shorts and three crossings confined to clock/support escape; focused USB3+SATA remains zero shorts/zero crossings.
2026-09-05 — Phase 19 consultant-reviewed clock-bus transplant: separated-clock-bus guidance was applied to live U7/J3 coordinates; static native-coordinate follow-up measured three shorts and seven crossings in the full candidate. Rejected; focused USB3+SATA remains zero shorts/zero crossings and Phase 19 stays open.
2026-09-05 — Phase 19 outboard clock-island experiment: moved Y1/R23/C42/C43 into open acreage and regenerated from live support pads; native DRC measured two shorts and nine crossings, localized to clock dogbones and clock-to-USB3 occupancy. Rejected; focused USB3+SATA remains clean and Phase 19 stays open.
2026-09-05 — Phase 19 full-support structural closure candidate: U7 (270,105)/J3 (190,140) regenerated with ordinary 0.30 mm-drill vias and cleaned clock support; native DRC reached zero shorts, crossings, clearance, drill, and dangling-track/via records. SI audit rejected it for USB3 TX 137.70 mm, RX 14.10 mm, and M.2 pair skews 25.25/27.25 mm; Phase 19 remains open.
2026-09-05 — Phase 19 SATA RX_P F.Cu coordinated trial: moved SATA RX_P to F.Cu against the USB B.Cu corridors; native DRC measured 215 records with five crossings, one U7 NC-pad short, and an F.Cu SATA pair crossing. Rejected.
2026-09-05 — Phase 19 USB3 TX escape discrimination: removing the lower detour reduced CM5 USB3 TX skew from 137.70 mm to 64.22 mm, but native DRC exposed SATA-RX and U7 pad-field conflicts; a lower dogbone then crossed TX_P. U7 placement sweep introduced donor-power collisions. Rejected; reproducible COORD49 baseline restored and Phase 19 remains open.
2026-09-05 — Phase 19 pair-preserving USB3 split: separate corridors reduced RX/TX pair skew to approximately 8.1/8.6 mm, but native DRC found source/clock crossings and four U7 launch shorts. Rejected; pair-preserving layer separation remains the selected solution class.
2026-09-05 — Phase 19 pair split endpoint spacing: all four USB3 long corridors stayed on B.Cu and U7 transitions were separated by 4 mm, reducing skew to approximately 0.45/0.53 mm RX/TX; native DRC still found corridor, source-via, and U7-side clearance/crossing violations. Rejected; complete source-to-U7 serialization remains open.
2026-09-05 — Phase 19 serialized-exit correction: rerun of the intended pair-split branch measured corrected RX/TX skew of 3.55/3.47 mm; native DRC still found four long-corridor crossings plus source-via and U7-side clearance failures. Preliminary 0.45/0.53 mm estimate superseded; candidate rejected.
2026-09-05 — Phase 19 all-B.Cu pair corridor: spread source transitions, reversed outboard ordering, and separated U7 transitions; measured RX/TX skew 4.27/7.22 mm with no clock-bus crossing, but native DRC still found two corridor crossings, one TX pair short, and localized clearances. Rejected; endpoint serialization remains open.
2026-09-05 — Phase 19 mixed-layer fan-in: moved only the TX final fan-in to F.Cu; native DRC still found three crossings including the TX pair and RX/TX interaction plus source/U7 clearance failures. Rejected; all-B.Cu pair-corridor generator restored.
2026-09-05 — Phase 19 source fanout spread: widened CM5-side transition columns before the B.Cu corridors; native DRC still found two outboard crossings, a TX pair crossing, and J7 hole/clearance violations, with 9.91/8.45 mm RX/TX skew. Rejected; complete serialized escape schedule remains open.
2026-09-05 — Phase 19 U7 orientation sweep: rotations 0/90/180 introduced immediate SATA/clock-pad conflicts; rotation 270 remains the only orientation preserving clean SATA endpoints. Rejected orientation alternatives; USB3 source/fan-in serialization remains open.
2026-09-05 — Phase 19 alternating-quadrant U7 fan-in: outer upper/lower dogbones introduced clock/corridor, CM5/J7 power-pad, and U7 clearance failures; USB3 skew degraded to 14.97/7.70 mm RX/TX. Rejected; prior separated-column baseline restored.
2026-09-05 — Phase 19 pre-clock TX layer transition: TX stayed F.Cu to x=250 then entered a separate B.Cu corridor; native DRC found corridor, CM5/J7 power-pad, clock-bus, and U7 clearance failures, with 9.59/8.63 mm RX/TX skew. Rejected; all-B.Cu pair baseline retained.
2026-09-05 — Phase 19 restored authoring path after pre-clock transition rejection: inactive experiment code was removed from the reproducible branch; all-B.Cu pair-corridor baseline remains the active Phase 19 reference.
2026-09-05 — Phase 19 isolated quadrant fan-in: rerun against the restored all-B.Cu baseline achieved 1.11/0.00 mm RX/TX skew but still had two corridor crossings, a TX fan-in short/crossing, and U7 clearances. Rejected; separated-column baseline restored.
2026-09-05 — Phase 19 legacy USB3-artifact comparison: ORDERED12 had no USB3 crossing/short records but used obsolete 0.40/0.20 mm vias; current-rule regeneration at original U7/J3 coordinates introduced five storage/USB crossings and power-pad shorts. Rejected; endpoint graph requires current-rule reauthoring.
2026-09-05 — Phase 19 current-rule ordered-branch regeneration: U7 (280,105)/J3 (200,140) with 0.50/0.30 mm vias still had four USB/storage crossings and a U7 clearance; USB3 skew was 0.10/44.70 mm RX/TX. Rejected as a transplant oracle.
2026-09-05 — Phase 19 planar fan-in schedule: descending-column/ascending-y B.Cu fan-in still produced multiple crossings with existing lane columns and retained source/U7 clearances; measured RX/TX skew 4.71/1.23 mm. Rejected; separated-column baseline restored.
2026-09-05 — Phase 19 ordered USB3 transplant and wide-acreage split: fixed generic KiCad track/via cleanup iteration; current-rule ordered transplant remained incompatible with the live SATA launch, while upper-B.Cu RX/lower-F.Cu TX acreage split hit RX interleaving, J3 body, and U7 pad-field conflicts. Both rejected; Phase 19 remains open.
2026-09-05 — Phase 19 coherent island translation probe: translated the complete storage/clock graph 20 mm while preserving PCIe/CM5, then tested current-rule ordered USB3. Native DRC retained U7 USB/SATA launch crossings and connector-body conflicts; rejected as a copied-segment transplant and retained as evidence for full endpoint resynthesis.
2026-09-05 — Phase 19 U7 rotation-90 USB diagnostic: confirmed USB top-row/SATA right-row pad geometry directly, then rejected the first corrected mixed-layer USB schedule for QFN endpoint convergence and clock/support corridor collisions. Rotation-90 island remains a live candidate; SATA was not added until USB endpoint escape is legal.
2026-09-05 — Phase 19 coordinated storage follow-up: rotation-0 complete SATA launch probe rejected for alternating M.2 pad-field crossings/shorts and U7-row clearance; coordinate-49 full SATA oracle retained with measured USB3 TX_N skew; KiCad SWIG TX_N shortening probe crashed before serialization and produced no design evidence.
2026-09-05 — Phase 19 coordinate-49 TX_N resynthesis: live endpoint authoring removed all new high-speed crossing/short/clearance records, but TX_N/TX_P remained 85.70 mm imbalanced; retained as a structural ancestor, not a gate pass.
2026-09-05 — Phase 19 moved-U7 V3 USB3 regeneration: preserved the native Phase 18 CM5 source breakout/vias, replaced only obsolete U7 tails, refilled zones, and achieved zero new focused USB3 crossings/shorts with unchanged PCIe geometry; Phase 19 remains gated on restoring the required inline SATA coupling-capacitor authority.
2026-09-05 — Phase 19 inline SATA-capacitor continuation: serialized four authoritative split SATA capacitor nets on the moved-U7 V3 island, but native DRC measured 313 violations / 413 unconnected with generated via/connector-launch clearance debt; rejected while preserving the cleaner USB3 V3 ancestor.
2026-09-05 — Phase 19 closure: combined the moved-U7 V3 USB3 schedule with four authoritative inline 0402 SATA capacitors, matched RX/TX end-to-end pair lengths, and passed focused native DRC/connectivity with unchanged PCIe geometry; closed under inherited-baseline qualification and staged Phase 20 next.
2026-09-05 — Phase 20 SERVICE authoring audit: corrected the native SERVICE child-sheet pin mapping and materialized the J4/U8/R1/R2 aliases, but native root ERC still exposes the missing parent hierarchy association; service routing remains active and no Phase 20 closure is claimed.
2026-09-05 — Phase 20 hierarchy repair validated: native CM5 SERVICE nets now carry J7.103=DM and J7.105=DP; restored CORE PCIe contract wires; USB2 pad-field routing remains in progress.
2026-09-05 — Phase 20 SERVICE routing experiments: the primary CM5-to-U8-to-J4 USB2 path and duplicate DP/DM connector pads can be joined without true shorts/crossings; support-net overlay rejected for crossing the data escape, so no board promotion or Phase 20 closure claimed.
2026-09-05 — Phase 20 SERVICE ground canonicalization: mapped logical SERVICE_GND to the board-wide POWER_GND plane and validated native refill; rejected the first VBUS B.Cu perimeter for crossing data-transition corridors, with production promotion still gated.
2026-09-05 — Phase 20 SERVICE VBUS experiment: revised connector-local VBUS perimeter refilled with zero true shorts/crossings and reduced unconnected items to 407; rejected the first Rd overlay for via-field conflicts, with Phase 20 still open.
2026-09-05 — Phase 20 SERVICE routing closure candidate: removed redundant alias vias and zero-length resistor tracks, completed DP/DM/VBUS/Rd endpoint connectivity with POWER_GND return, matched inherited native DRC class counts at 190, and passed the dedicated routing regression; Phase 20 disposable electrical gate is closed.
2026-09-05 — Phase 20 SERVICE routing validation: removed redundant VBUS alias bridge segments, matched the inherited 190-item native DRC census with no new focused errors, and added a reproducible complete-endpoint F.Cu/B.Cu routing regression; low-speed/control review is next.
2026-09-05 — Phase 21 control inventory: generated a native pcbnew inventory from the Phase 20 service-routed board, identifying unrouted power-input gate/VCAP, bridge feedback/RT/PG, and U7 reset nets while preserving all validated high-speed geometry; low-speed routing remains in progress.
2026-09-05 — Phase 21 local control repairs: routed U7 reset, bridge 3V3/1V1 PG, CM5 5V PG, and both LM74700 VCAP nets with local F.Cu geometry; native DRC fell to 189 inherited-class findings with no new focused errors, while gate and bridge FB/RT controls remain open.
2026-09-05 — Phase 21 gate experiment: tested separate ordinary-via B.Cu perimeter corridors for GATE_A/B, found true intersections with existing protected-12-V copper, rejected the candidate, and preserved the clean reset/PG/VCAP ancestor for local bridge FB/RT continuation.
2026-09-05 — Phase 21 bridge FB3V3 repair: co-located R11/R12/C18 beside U4, escaped FB around the U4 pad field with a refilled ordinary-via B.Cu trunk, and passed endpoint/focused native DRC checks with no new shorts/crossings/clearance class; bridge RT and gate controls remain open.
2026-09-05 — Phase 20 complete disposable SERVICE support candidate: joined USB2 duplicate pads, VBUS aliases, both Rd endpoints, and POWER_GND using ordinary F.Cu/B.Cu routing; native DRC measured 194/405 versus inherited 190/415 with no new clearance, shorting, or crossing class; production promotion remains gated on mechanical/return review.
2026-09-05 — Phase 21 closed: promoted the coordinated regulator-control candidate with bridge FB/RT/PG, LM74700 gates/VCAP, U7 reset, ordinary F.Cu/B.Cu routing, and zero new shorting/crossing/width/courtyard classes in native DRC; Q1/Q2 moved as coherent local control blocks without changing power topology.
2026-09-05 — Phase 22 closed: verified the promoted board's In1/In4 full-board POWER_GND zones, twelve dedicated POWER_GND return/stitching vias, native refill, and zero signal segments on plane layers; return strategy remains inherited and categorized rather than indiscriminately sprinkled.
2026-09-05 — Phase 23 probe-pad experiment rejected: direct underside testpoint overlays on component pads caused true shorts and hole-clearance violations; preserved the Phase 22 ancestor and kept test/debug access open for a proper dogbone-connected implementation.
2026-09-05 — Phase 23 probe-pad V2 rejected: smaller underside pads with short dogbones still entered adjacent U1/U2/U4/U5 pad fields and a crowded control-via corridor; preserved the Phase 22 production ancestor and retained only disposable evidence.
2026-09-05 — Phase 23 closed: promoted spread-out THT probe pads for raw/fused/protected 12 V, CM5 5 V, storage 3V3, bridge PG, PERST, POWER_GND, and schematic-authorized debug nets; native DRC showed no probe-attributable short, crossing, hole-clearance, width, or courtyard class.
2026-09-05 — Phase 24 native-authoring repair: assembled the complete clean custom symbol library, replaced malformed root hierarchy wiring with generic native sheet-edge associations, marked two unused CM5 MIPI pins no-connect, and proved zero severity-error ERC; netlist annotation warning remains explicitly open.
2026-09-05 — Phase 24 closed: repaired stale regulator capacitor instance references C30-C33 to C44-C47, then proved warning-free native netlist export, zero severity-error ERC, and preserved acreage validation authority.
2026-09-05 — Phase 24 parity audit reopened: the warning-free schematic/netlist exposes missing PCB materialization for Y1/R23/C42/C43 and C44-C47; a stale-coordinate clock graft was rejected for true U7-pad shorts and retained as disposable evidence.
2026-09-05 — Phase 24 support materialization candidate rejected: coordinate-derived clock corridors crossed inherited SATA/USB copper and the U5 bulk-cap graft entered regulator pad/return geometry; retained evidence and kept the gate open for coordinated route regeneration.
2026-09-05 — Phase 24 coordinated storage donor rejected: COORD49_FULL supplied complete USB3/SATA/clock copper but its relocated USB3 corridor crossed the frozen V5 PCIe corridor after merge; retained V5 high-speed placement and narrowed the next class to obstacle-aware local clock routing.
2026-09-05 — Phase 24 support V2 rejected: actual-coordinate clock fanout plus materialized C44-C47 produced 234 native DRC violations and 409 unconnected items, including U7 pad-field shorts and clock/SATA crossings; retained evidence and narrowed the active repair to layer-separated clock fanout and a coherent U5 rail/return island.
2026-09-05 — Phase 24 rotated-U7 discriminator rejected as invalid proof: the authoring script rotated U7 but retained a pre-rotation hard-coded clock endpoint graph, so native DRC found unrelated-pad mismatches; classified as a tooling/authoring defect and required post-rotation endpoint derivation.
2026-09-05 — Phase 24 corrected rotated-U7 source escape: post-rotation U7 endpoint derivation produced a disposable clock escape with zero native DRC shorting/crossing records; support-passive branches remain intentionally incomplete and production promotion is gated.
2026-09-05 — Phase 24 spread-support fanout rejected: native DRC found 229 violations including three genuine XI/XO/VSSOSC crossings; rotated-U7 source escape remained short-free, so the active repair stays layer-separated passive fanout plus the U5 C44-C47 island.
2026-09-05 — Phase 24 full clock-support discriminator remains open: offset ordinary-via revision has zero native DRC shorts, crossings, width violations, and footprint errors, but target XI/XO/VSSOSC connectivity is still reported unconnected on the intentionally stripped ancestor; no promotion.
2026-09-05 — Phase 24 clock-support topology pass: corrected SWIG-safe copper reset and separated VSSOSC layer transition produced zero native DRC clock crossings, shorts, width violations, footprint errors, or target XI/XO/VSSOSC unconnected records; acreage transplant and C44-C47 materialization remain open.
2026-09-05 — Phase 24 reproducible clock rerun: rotated-U7 U7/Y1/R23/C42/C43 fixture exited successfully with native DRC zero crossings, shorts, width violations, footprint errors, and zero target clock unconnected records; only stripped-ancestor residue remains, so acreage transplant is still gated.
2026-09-05 — Phase 24 U5 capacitor-island experiments rejected: near-U5 and outboard C44-C47 placements introduced shorts/crossings against inherited feedback, ground, and PG corridors; parity remains open pending actual-pad-derived rail/return corridor selection.
2026-09-05 — Phase 24 U5 capacitor-island topology pass: regenerated bridge-1V1 source and outboard C44-C47 shelf produced zero native DRC shorts, crossings, width violations, or footprint errors, with no C44-C47 rail/return unconnected records; combined acreage integration remains open.
2026-09-05 — Phase 24 combined proven-clock transplant rejected: rigid rot90-to-rot180 transformation preserved the locally passing clock graph but introduced true PCIe/SATA crossings and shorts at acreage; next work is an open-shelf placement integration.
2026-09-05 — Phase 24 combined integration attempt rejected: existing rot180 generator and rigid transformed clock graph both collided with inherited high-speed copper; local clock and U5-cap proofs remain authoritative for the next open-shelf integration pass.
2026-09-05 — Phase 24 open-shelf clock candidate rejected: the x204-218 shelf itself was clear, but hand-authored rot180 U7 source coordinates caused clock pad-field shorts/crossings; next work derives rot180 endpoints from serialized footprints.
2026-09-05 — Phase 24 generic rot180 endpoint rerun rejected: serialized U7 endpoint derivation succeeded, but the open-shelf branch graph still produced clock shorts/crossings; local rot90 and U5-cap oracles remain valid.
2026-09-05 — Phase 24 underside open-shelf source attempt rejected: underside SMD pads removed the crystal-launch crossing, but the long source lanes still intersected inherited SATA copper; corridor selection remains open.
2026-09-05 — Phase 24 rot180 source-escape oracle passed: serialized U7 pins 52/53/54 support asymmetric XI-right, VSSOSC-up, XO-left escape with zero native DRC shorts, crossings, width violations, footprint errors, or target clock unconnected records.
2026-09-05 Phase24: compact clock-position sweep preserved; nearwest underside candidate reduced the remaining clock defect to a localized U7 B.Cu lane crossing, not yet promoted.
2026-09-05 Phase24: refined the disposable solver to seed proven rot180 source-via exits; it still found no XI corridor through the inherited SATA/pad field, so no candidate was promoted.
2026-09-05 Phase24: tested an adjacent U7/J3 clock shelf with the seeded solver; conservative search returned no XI path before board generation, so the candidate and search model remain unpromoted.
2026-09-05 Phase24: rejected expanded-acreage coordinated storage transplant; rigid donor shift removed PCIe clock crossings but disconnected CM5 USB3 and left storage support incomplete.
2026-09-05 Phase24: applied the independent tunnel map to the seeded clock solver; all three downstream routes are found and via-clearance conflicts are removed, but XO source launch crossings remain.
2026-09-05 Phase24: tunnel-guided A* source-launch refinement reached 226 native DRC violations; XO/SATA crossing removed, Y1 approach remains open.
2026-09-05 Phase24: side-separated crystal escape reached 207 native DRC violations with zero clock tracks-crossing or shorting records; inherited board hygiene and support parity remain open.
2026-09-05 Phase24: rejected first support materialization; Y1 passive branches caused 3 crossings/8 shorts and C44-C47 overlapped regulator support, so clock and support islands remain separate.
2026-09-05 Phase24: updated status to retain the zero-clock-crossing A* oracle while requiring independently routed support islands for parity closure.
2026-09-05 Phase24: complete native-orientation clock-support fixture passed with zero unconnected items, shorts, crossings, or footprint errors; rot180 acreage transplant remains open.
2026-09-05 Phase24: corrected the clock-fixture receipt: native DRC is clean for the checked source graph, but the legacy fixture omits some passive branch routing and is not support-topology closure.
2026-09-05 Phase24: rejected strict complete clock fixture; generic three-bus geometry produced 5 crossings, 4 shorts, and 8 disconnected pads, requiring serialized pad-field routing.
2026-09-05 Phase24: rejected launch-height refinement; native DRC still found 8 B.Cu crossings, so the next class is an obstacle-mapped proven support transplant.
2026-09-05 Phase24: rejected obstacle-aware passive router; all six paths were found but native DRC reported 29 shorts and 13 crossings, requiring branch-aware clock regeneration.
2026-09-05 Phase24: rejected branch-to-existing-rail variant; native DRC reported 12 shorts and 9 crossings, requiring one coordinated clock graph.
2026-09-05 Phase24: rejected five-position passive-island sweep; four placements had no conservative rail path and the best generated board had 322 native DRC violations.
2026-09-05 Phase24: rejected multi-net graph-anchor sweep; all six branches were found but native DRC reported 10 shorts and 4 crossings, requiring layer-separated passive dogbones.
2026-09-05 Phase24: rejected layer-separated passive dogbones and four outboard variants; best native DRC was 306 violations with 14 shorts and 6 crossings.
2026-09-05 Phase24: coordinated layer-owned clock graph passed native clock-specific DRC with zero crossings, shorts, and footprint errors; acreage transplant remains open.
2026-09-05 Phase24: rejected first acreage clock-support transplant (218 native violations including clock crossings/short); independent U5 capacitor island had no shorts/crossings but retained dangling/inherited violations.
2026-09-05 Phase24: rejected U5 surface-only capacitor trial; native DRC reported 202 violations including a rail/GND short and crossings.
2026-09-05 Phase24: rejected outboard U5 surface rail-trunk placement; native DRC reported 203 violations including rail/GND short and crossings.
2026-09-05 Phase24: hardware audit retained full-board parity reservation; ground-aware U5 V2 reduced the island to one crossing/no shorts but remained unconnected and was rejected.
2026-09-05 Phase24: full native netlist/PCB reference-set audit passed for 78 schematic refs plus 23 explicitly classified legacy/test/mechanical extras; routed parity remains open.
2026-09-05 Phase24: removed nine PCB-only Ethernet CCT/RCT aliases; filtered candidate now matches all 78 schematic refs plus 13 expected mechanical/test markers with no new shorts/crossings.
2026-09-05 Phase24: added a machine-checkable filtered reference-set audit for the clean 78-reference PCB candidate.
2026-09-05 Phase24: revalidated filtered 78-reference candidate with no native shorts/crossings; 201 DRC violations and 406 unconnected pads remain.
2026-09-05 Phase24: added and passed a clean reference-authority regression test rejecting legacy CCT/RCT aliases.
2026-09-05 Phase24: rejected U5 source-launch refinement; native DRC remained 197 violations with one crossing and no shorts, so a layer-separated launch is still required.
2026-09-05 Phase24: rejected U5 left-side source detour; native DRC remained 197 violations with one crossing and 392 unconnected pads.
2026-09-05 Phase24: U5 layer-owned source/return fixture passed targeted native DRC with zero shorts/crossings; acreage integration remains open.
2026-09-05 Phase24: corrected U5 layer fixture reached the rotated capacitor pads and again passed targeted native DRC with zero shorts/crossings; graph-audit defect excluded, acreage integration remains open.
2026-09-05 Phase24: U5 fixture connectivity regression audit passed; all C44-C47 rail/return pads join their intended sources, with zero native shorts/crossings.
2026-09-05 Phase24: materialized all eight missing Phase24 component references; exact pad-net audit passed and native DRC had no shorts or crossings, while routed parity remains open.
2026-09-05 Phase24: integrated the U5 layer-separated source/return launch with real C44-C47 pad-to-via dogbones; targeted graph audit passed and refilled native DRC had zero shorts/crossings, while full routed parity remains open.
2026-09-05 Phase24: rejected direct rotated-U7 clock-oracle overlay on the routed acreage candidate after native DRC found 288 violations, clock/SATA bridge shorts, and crossings; preserved the standalone oracle and corrected via-width API use.
2026-09-05 Phase24: corrected the clock-fixture U7 pad-frame transform and reran it; native DRC still rejected the overlay with 227 violations, SATA/clock shorts, crossings, and 393 unconnected pads, so local clock regeneration remains required.
2026-09-05 Phase24: replaced the U5 audit with serialized net/layer-aware physical connectivity, and passed independent missing-trace and missing-via negative controls; full-board routed parity remains open.
2026-09-05 Phase24: added a native DRC unconnected census covering all 397 records; 12V_PROTECTED, POWER_GND, and CM5 ground dominate, with no severity waiver or connection filtering.
2026-09-05 Phase24: promoted the corrected U7 BRIDGE_SATA_RX_N pad-field stitch; native DRC removed five target connections with zero new shorts/crossings, while 392 inherited/unresolved records remain.
2026-09-05 Phase24: rejected plane-only In3 protected-12V experiment; native DRC stayed free of shorts/crossings but removed only two of 397 missing connections, proving surface power launches are still required.
2026-09-05 Phase24: validated U5 same-net input-power pad-field stitch; native DRC held at 201 violations, removed seven unconnected records, and introduced zero shorts or crossings; board-wide closure remains open.
2026-09-05 Phase24: rejected all-regulator pad-field stitch at U4 due native PG crossing/shorts; retained clean U3/U5 field repair with 384 unconnected records, zero shorts, and zero crossings.
2026-09-05 Phase24: rejected U4 same-layer obstacle-aware field stitch after native DRC found four crossings; documented need for layer-separated/local regenerated U4 corridor.
2026-09-05 Phase24: accepted corrected U4 perimeter power-field geometry after moving the escape above the PG/feedback corridor; native DRC returned to baseline with zero shorts/crossings.
2026-09-05 Phase24: validated separate F2 raw/fused pad-field joins; native DRC held at 201 violations, removed six unconnected records, and preserved raw-to-fused net isolation.
2026-09-05 Phase24: validated separate F1 raw/fused pad-field joins; native DRC held at 201 violations, removed five unconnected records, and preserved dual-input net isolation.
2026-09-05 Phase24: rejected B.Cu-only J1 bus, then validated F.Cu column plus offset-via B.Cu bus; native DRC held at 201 violations, removed 129 unconnected records, and preserved zero shorts/crossings.
2026-09-05 Phase24: combined the validated J1 protected bus with the In3 distribution plane; native DRC stayed at 201 violations with zero shorts/crossings and reduced unconnected records to 265.
2026-09-05 Phase24: rejected J1 ground launches intersecting the protected bus, then validated y=98.0 mm ground-plane launches; native DRC held at 201 violations, zero shorts/crossings, and 195 unconnected records.
2026-09-05 Phase24: rejected CM5 ground-launch offsets after native DRC exposed pad-field shorts/crossings; preserved separate CM5 ground authority and documented obstacle-aware escape requirement.
2026-09-05 Phase24: rejected direct bridge low-voltage pad joins at intervening ground pads, then validated perimeter escapes; native DRC held at 201 violations, zero shorts/crossings, and 261 unconnected records.
2026-09-05 Phase24: validated U3 POWER_GND perimeter field escape; native DRC held at 201 violations, zero shorts/crossings, and reduced targeted candidate to 258 unconnected records.
2026-09-05 Phase24: validated consultant-recommended global POWER_GND launch cluster after correcting the J4 USB2 collision; native DRC held at 201 violations, zero shorts/crossings, and 188 unconnected records.
2026-09-05 Phase24: rejected cumulative overlapping regulator ground composition, then validated separated local-repair composition; native DRC held at 201 violations, zero shorts/crossings, and 168 unconnected records.
2026-09-05 Phase24: composed the validated U7 RX-N pad-field stitch onto the cumulative local-repair candidate; native DRC held at 201 violations, zero shorts/crossings, and 163 unconnected records.
2026-09-05 Phase24: rejected U7 BRIDGE_CFG direct and perimeter joins after native DRC found pad-field shorts/crossing; retained control escape as open layer-separated task.
2026-09-05 Phase24: materialized schematic-authoritative U7 XI/VSSOSC/XO net identities on pads 52/53/54; native DRC held at 201 violations with zero shorts/crossings, and source pads entered the unconnected census.
2026-09-05 Phase24: corrected oracle-derived U7 XO source escape below SATA-TX corridor; native DRC has zero shorts/crossings and 166 unconnected records, with passive clock branches still open.
2026-09-05 Phase24: rejected complete B.Cu clock passive branches after native DRC found three shorts and ten crossings; retained isolated-pad-launch/layer-separated-bus requirement.
2026-09-05 Phase24: rejected isolated clock passive launches after native DRC found 17 crossings and three shorts; narrowed next implementation to obstacle-aware layer-separated routing.
2026-09-05: Phase 24 compared the exact rotated-U7 clock oracle transplant; native DRC rejected the fixed acreage coordinate context while preserving the oracle topology as the basis for obstacle-aware regeneration.
2026-09-05: Corrected the Phase 24 U5 audit to use KiCad native saved-board connectivity and added a disposable trace-removal regression; native baseline and negative-control tests pass.
2026-09-05: Replaced the stale coordinate-based U5 negative-control selector with a native connected-component-derived disposable trace removal; the required control now fails the audit as intended.
2026-09-05: Repaired the Phase 24 native-authority regression test to use the installed kicad-cli directly when xvfb-run is absent; direct native ERC reports zero violations and the authority test passes.
2026-09-05: Recorded the Phase 24 clock placement sweep; near-west is the best rejected class at zero clock shorts and one crossing, while the complete isolated fixture still needs four crossing repairs.
2026-09-05: Phase 24 clock fixture V2 passes clock-specific native connectivity and DRC checks with split layer ownership; its acreage transform is rejected at 226 DRC violations and retained as integration evidence.
2026-09-05: Phase 24 incremental clock probes isolated clean XI and XO launches; the first VSSOSC perimeter was rejected by two native shorts and two crossings at the inherited SATA corridor.
2026-09-05: Phase 24 passive-field obstacle search found no legal B.Cu path from serialized Y1.1 to R23.1; no incomplete candidate was promoted.
2026-09-05: Phase 24 composed the corrected complete XI/XO/VSSOSC clock onto cumulative repairs; native component checks pass with zero short/crossing classes and 156 unconnected records remaining.
2026-09-05: Phase 24 accepted the bridge-1V1 capacitor-field B.Cu chain with ordinary pad-adjacent vias; native DRC has zero short/crossing classes and 145 unconnected records remaining.
2026-09-05: Phase 24 joined the bridge-1V1 capacitor field to the U5 output island on B.Cu; native DRC has zero short/crossing classes and 144 unconnected records remaining.
2026-09-05: Phase 24 closed the identified bridge-1V1 feedback endpoints with sequential R19/R22 B.Cu joins; native DRC has zero short/crossing classes and 142 unconnected records remaining.
2026-09-05: Phase 24 accepted the bridge-3v3 capacitor/support and R14 output joins; native DRC has zero short/crossing classes and 138 unconnected records remaining.
2026-09-05: Phase 24 closed the isolated C3.2 12V_A bypass with a short F.Cu dogleg to U1.3; native DRC has zero short/crossing classes and 137 unconnected records remaining.
2026-09-05: Phase 24 closed the U7 BRIDGE_CFG pad join on the accepted ancestor; native DRC has zero short/crossing classes and 136 unconnected records remaining.
2026-09-05: Corrected Phase 24 DRC evidence after an independent fresh native rerun found 235 violations, 4 shorts, and 7 crossings; earlier zero short/crossing parser claims are superseded, and the J7 top-row trial was rejected at 8 shorts and 10 crossings.
2026-09-05: Reconciled Phase 24 candidates with full-report native DRC counting; the clean working basis is the 205/145/0-short/0-crossing bridge-1V1 capacitor chain, while later composite joins are rejected pending regeneration.
2026-09-05: Revalidated the clean Phase 24 repair sequence with full-report DRC: R19 and the regenerated 3V3 capacitor field reach 208 violations, 141 unconnected records, zero shorts, and zero crossings; contaminated later joins remain rejected.
2026-09-05: Rejected the C5/C6 direct POWER_GND join after fresh DRC found one native short; retained the 208/141/0-short/0-crossing clean repair basis.
2026-09-05: Accepted the lower J7 CM5-ground F.Cu comb below the active Ethernet rows; fresh DRC has 208 violations, 127 unconnected records, zero shorts, and zero crossings.
2026-09-05: Rejected the upper J7 CM5-ground comb extension after fresh DRC found three shorts and nine crossings; retained the lower-comb basis and localized the next task to Ethernet-launch regeneration.
2026-09-05: Rejected the same-row-only upper J7 ground bridges after fresh DRC found one short and six crossings; upper-row closure requires Ethernet-launch regeneration.
2026-09-05: Rejected same-row-only upper J7 ground bridges after fresh DRC found one short and six crossings; upper-row closure now requires Ethernet-launch regeneration.
2026-09-05: Accepted the KiCad-recommended three-pad CM5-ground discriminator; fresh DRC reports 209 violations, 139 unconnected records, zero shorts, and zero crossings.
2026-09-05: Expanded the accepted right-column CM5-ground collector through four additional lower pads; fresh DRC reports 209 violations, 130 unconnected records, zero shorts, and zero crossings.
2026-09-05: Accepted the lower x=70.04 J7 CM5-ground outer collector; fresh DRC reports 209 violations, 124 unconnected records, zero shorts, and zero crossings.
2026-09-05: Accepted the clean same-row bridges joining the lower-right J7 CM5-ground collectors; fresh full-report native DRC is 209 violations, 122 unconnected records, zero shorts, and zero crossings.
2026-09-05: Rejected the CM5-ground In1 plane-attachment trial after fresh native DRC found 210 violations and no connectivity gain; retained the 209/122/0-short/0-crossing same-row collector basis.
2026-09-05: Rejected the upper CM5-ground outer-escape trial at 215 violations, 118 unconnected records, two shorts, and three crossings; specialist review confirms ordinary-via clearance is insufficient in the preserved Ethernet launch.
2026-09-05: Rejected the outboard POWER_GND return-row trials: C14-C19 produced 3 shorts/2 crossings and C14-C15 produced 2 shorts; retained the clean 209/122/0/0 basis.
2026-09-05: Rejected transplant of the earlier J1 ground-column geometry onto the cumulative basis at 217 violations, 122 unconnected records, 1 short, and 2 crossings; retained 209/122/0/0.
2026-09-05: Rejected cumulative U5 exposed-ground stitching after full native DRC found a POWER_GND/BRIDGE_1V1 short; three single-segment discriminators reproduced the short, while the corrected U5 audit remained passing.
2026-09-05: Performed the authorized native macro-floorplan review; extracted transformed CM5/island geometry, generated three disposable no-overlap candidates, and identified Ethernet/storage as materially nonlocal before further Phase 24 copper repair.
2026-09-05: Corrected the macro-floorplan Ethernet identity to U6/U9, documented native body-overlap evidence, and repaired the KiCad-10 Ethernet transplant helper's detached-object handling before testing a west-edge CM5IO-derived island.
2026-09-05: Rejected the first ETH_WEST rigid CM5IO copper transplant after native DRC found 571 violations, 123 unconnected records, 12 shorts, and 20 crossings; retained the coherent placement recommendation and switched the next trial to live-pad obstacle-aware regeneration.
2026-09-05: Corrected ETH_WEST ESD placement outside the native J7 body bbox at (20,104)/(26,104), generated the outboard disposable study, and retained complete live-pad routing as the next Phase 24 action.
2026-09-05: Added a cross-class Ethernet study keeping U6/U9 east of the native J7 body while moving only J2 west, preserving a mechanically unambiguous alternative for pair-routing comparison.
2026-09-05: Rejected the live-pad east-ESD/west-J2 Ethernet routing discriminator at 569 violations, 131 unconnected records, 34 shorts, and 28 crossings; retained west-outboard ESD with isolated corridors as the next experiment.
2026-09-05: Corrected the ETH_WEST study for native CM5 body clearance by generating an outboard U6/U9 placement at (20,104)/(26,104); retained it as a disposable candidate pending complete regenerated routing.
2026-09-05: Rejected the first west-outboard live-pad route at 458 violations, 137 unconnected records, 5 shorts, and 4 crossings; retained the mechanically valid placement and isolated ESD/connector fanout for refinement.
2026-09-05: Closed the west-outboard hand-route orientation sweep without promotion: ESD rotations 0/180 yielded 468/141/5/8 and 456/143/7/4; next continuation requires obstacle-aware or reference-derived pad escape.
2026-09-05: Recorded independent west-outboard review: 2D placement is plausible, but the next route must be all-F.Cu with no USON signal vias, a dedicated EDAC no-go launch envelope, and an explicitly resolved 0.13208 mm versus 0.200 mm rule basis.
2026-09-05: Rejected the monotonic west Ethernet candidate at 497 violations, 135 unconnected records, 15 shorts, and 17 crossings; next method is direct CM5IO serialized pad-escape reuse with board-context obstacle handling.
2026-09-05: Serialized CM5IO MDI transplant passed focused pair metrics and native J7/U6/U9/J2 connectivity with a negative control; full-board DRC remained 449/122/0 crossings/1 unrelated short, so the MDI basis is conditional only.
2026-09-05: Audited current Phase 24 native state: Ethernet schematic support is labels-only pending schematic authority, U5 native connectivity and negative control pass, and the J7-derived CM5-ground plane/launch experiment was rejected at 264/397 with four shorts and one crossing; Phase 24 remains open.
2026-09-05: Accepted one bounded native return repair: C5.2-C6.2 reduced unconnected records 397 to 396 with no new shorts/crossings; U5 connectivity, negative control, and authoritative-part audits remain passing.
2026-09-05: Rejected the C14.2-C15.2 adjacent return probe after native DRC found a real C15.1 12V_PROTECTED short and 203 total violations; retained the C5/C6-only repair.
2026-09-05: Corrected stale-base U5 pair sweep: C44/C45 and C46/C47 pair joins were DRC-clean but reduced no native opens, so they were not promoted; the real remaining defect is island-to-return attachment.
2026-09-05: Corrected stale-base U5 pair sweep: C44/C45 and C46/C47 pair joins were DRC-clean but reduced no native opens, so they were not promoted; the real remaining defect is island-to-return attachment.
2026-09-05: Rejected three U7 BRIDGE_CFG local escapes: direct F.Cu short, B.Cu SATA crossings, and an early-via route adding six DRC violations without closing an open; no CFG copper promoted.
2026-09-05: Accepted native U7 RX-N pad-field stitch: U7.5-U7.9 now connect to U7.59/C33.2, reducing opens 396 to 391 with zero new shorts/crossings; inherited dangling-via warnings unchanged.
2026-09-05: Corrected U7 clock pad ownership from native netlist authority: U7.52/53/54 now serialize XI/VSSOSC/XO on the RX-N-improved basis; native DRC has zero shorts/crossings, with clock copper still open.
2026-09-05: Extended U7 native net ownership correction to pins 24/30/31 as BRIDGE_3V3; five newly visible unrouted U7 support endpoints leave native DRC at 201/396 with zero shorts/crossings, so complete support routing remains open.
2026-09-05: Accepted U7 BRIDGE_3V3 pad-field dogleg: U7.24/30/31 connect to TP5.1 around no-connect pads, reducing opens 396 to 394 with zero new shorts/crossings.
2026-09-05: Rejected corrected A* clock routing on the integrated board: source/pad crossings were removed, but signal transition vias violated ground-zone clearance and raised DRC to 217; no route promoted.
2026-09-05: Revalidated the clock A* discriminator with native CLI zone refill: XI reduced opens 394 to 392 with zero shorts/crossings but added five refill-clean clearance/dangling findings (429 to 434); stale-zone route rejected.
2026-09-05: Corrected clock-support SMD pad layers to F.Cu and confirmed U7 pad authority; preserving real obstacles leaves no bounded XI path to R23.1, so the route was not promoted and requires a moved/reserved clock island.
2026-09-05: Rejected moved outboard clock-island trial after native refill found nine F.Cu crossings with SATA_TX_N and clock lanes; opens fell to 384, but no route was promoted.
2026-09-05: Added U7 pad-net authority regression: corrected candidate passes all 17 schematic-owned U7 endpoint assignments and the prior baseline fails on five omitted pads; no synthetic connectivity edges are used.
2026-09-05: Paused Phase 24 clock/SATA repair for the required whole-board macro-floorplan discriminator; native CM5 mating-view geometry and placement-only island migration/swap candidates show current Ethernet/storage centroid distances of 59.2/67.6 mm versus 5.1/51.0 mm for the best CM5-neighborhood probe, with no candidate routing promoted.
2026-09-05: Selected the placement-only `ETH_WEST_LOCAL_STORAGE` macro candidate after whole-board native CM5 mating-view review: Ethernet support stays outside the CM5 body beside the GBE launch, MagJack moves west, U7/J3/clock move to the USB3-side acreage, and PCIe/SERVICE anchors remain fixed; affected copper remains invalid pending regeneration.
2026-09-05: Rejected the first selected-macro USB3/SATA regeneration after native refilled DRC found 43 true shorting items and 7 crossings; the saved board exposes distinct U7 `BRIDGE_SATA_*` versus J3 `SATA_M2_*` net identities, so the route is invalid authority evidence and requires a schematic/native boundary repair before retry.
2026-09-05: Corrected the selected-macro SATA retry to traverse the authoritative C30/C31/C32/C33 AC-coupling boundary, then rejected the route after native refilled DRC found 46 shorts and 5 crossings; the remaining failure is lane/obstacle geometry, not permission to short distinct bridge and M.2 nets.
2026-09-05: Rejected the selected-macro Ethernet-only hand route after native refilled DRC found 55 shorts and 22 crossings; CM5IO pin mapping was retained, but J7/ESD pad-field and west-edge launch geometry require official-topology transplantation or obstacle-aware routing.
2026-09-05: Rejected the selected-macro rotated-west CM5IO Ethernet transplant after native refilled DRC improved to 18 shorts and 10 crossings; fixed oracle lanes still collide with live J7 exits, MagJack through-hole pads, and SERVICE copper, so live-obstacle regeneration remains required.
2026-09-05: Preserved the CM5IO transplant rejection as live-obstacle evidence; reviewer polling produced no completed response, so the next authorized Ethernet class is endpoint repositioning with the same split-layer topology rather than further hand-route edits.
2026-09-05: Completed the required whole-board functional-island floorplan discriminator from native transformed CM5 pad coordinates; tested large migrations and the Ethernet/storage swap, retained ETH_WEST_LOCAL_STORAGE as the best joint basis, and kept Phase 24 open for coherent copper regeneration.
2026-09-05: Rejected Ethernet rigid-translation and rigid-rotation probes after native DRC exposed live-board occupancy and transformed-branch crossings; preserved the CM5IO topology and selected macro basis, with the next trial requiring coherent affected-copper clearing before regeneration.
2026-09-05: Snapshotted the selected macro parent by SHA-256 and ran an inherited-only native DRC; a clean-neighborhood overlay with the unmodified CM5IO Ethernet MDI route produced zero Ethernet shorts/crossings, proving stale functional-neighborhood copper was contaminating prior comparisons.
2026-09-05: Regenerated the selected-placement CM5IO Ethernet route against the immutable parent; native DRC found 15 shorts and 13 crossings versus the parent's 22 shorts and 0 crossings, so the hard-coded local escape remains rejected while the clean overlay remains the topology discriminator.
2026-09-05: Corrected the macro comparison interpretation: retained ETH_WEST_LOCAL_STORAGE by placement/ratsnest topology, classified the selected-local Ethernet result as route implementation failure, and retained the clean CM5IO top-oracle overlay only as a routing-development candidate rather than a DRC-based floorplan promotion.
2026-09-05: Audited clean Ethernet support against the native CM5IO source and EDAC authority; recorded the missing schematic-owned center-tap, LED-current, and shield-return network as an open authority gap before further PCB promotion.
2026-09-05: Extended the Ethernet support audit through the clean hierarchy and found the bundled GBE_LED contract versus four local connector LED nets; recorded this interface mismatch for schematic repair without inventing CM5 LED ownership.
2026-09-05: Selected commodity Ethernet support passives from manufacturer/distributor evidence and regenerated the disposable native fixture with 0603 CT capacitors, 0402 75 ohm/LED resistors, and a 1206 2 kV shield capacitor; production CM5 LED hierarchy mapping remains open.
2026-09-05: Closed Ethernet schematic support authority in Phase 24: promoted native CT/shield/LED support, removed the bundled GBE_LED hierarchy pin, mapped ETH_LEDY/ETH_LEDG to CM5 J7 pads 17/15, and verified native netlist plus ERC Errors 0; PCB materialization/parity remains open.
2026-09-05: Clarified Phase 24 status after promotion: the historical Ethernet-support audit is explicitly superseded, the production hierarchy closure and native ERC/netlist receipts are current, and PCB-side materialization/parity remains the next downstream gate.
2026-09-05: Materialized the 11 Ethernet support footprints from the native production netlist on a disposable selected-macro PCB; independent pad-net parity passed, native DRC added only expected unrouted support pads with zero footprint errors and no track crossings, and routed support integration remains open.
2026-09-05: Re-ran the whole-board macro-floorplan discriminator from a native-loaded CM5 carrier-mating view; compared current, Ethernet-local/storage-local, CM5-neighborhood, and swap candidates using source distances and same-net ratsnest topology, retained ETH_WEST_LOCAL_STORAGE, and kept detailed routing paused until coherent regeneration.
2026-09-05: Corrected the macro discriminator after consultant review found omitted SERVICE/storage support and exact-coordinate body collisions; added signal-oriented metrics including U8/C16/C17/C19, rejected the old coordinates, and generated the collision-screened ETH_WEST_CLEAR_STORAGE_MID routing basis.
2026-09-05: Materialized the corrected collision-screened macro basis with complete storage support and affected-copper removal; native DRC retained only the three inherited courtyard overlaps, so the next gate is coordinated native-pad routing rather than another macro-floorplan comparison.
2026-09-05: Ran the first corrected-basis eight-pair Ethernet routing search; rejected its native-DCR-short candidate, corrected endpoint-pad occupancy so the generator cannot route through neighboring pads, and classified the remaining no-path result as route implementation failure pending connector-launch orientation work.
2026-09-05: Tested corrected-basis Ethernet MagJack rotations 90 and 270; both failed only in the sequential ESD-to-connector escape search, so the variants were rejected as route-implementation failures and the next attempt will use alternating launch layers and pad-field-aware ordering.
2026-09-05: Reran the corrected Ethernet layered escape after fixing endpoint-pad occupancy and same-net via deduplication; native DRC still found real pair shorting, so the complete candidate was rejected and the next class is explicit non-crossing reference-topology corridors with controlled rip-up.
2026-09-05: Corrected Ethernet routing to derive J7/U6/U9/J2 copper layers from native pad layer sets, then rejected the complete V3 candidate after native DRC found 827 violations, 431 unconnected items, and real pair/ground shorts; recorded the separate U7-clock passive-side authority issue before clock routing.
2026-09-05: Completed a fresh whole-board Phase 24 macro-floorplan discriminator from the native-loaded corrected acreage parent; evaluated functional-island distances, apparent source-launch crossings, coherent island swaps, and coarse body conflicts without using mature-routing DRC, rejected tighter CM5-neighborhood alternatives, and retained CURRENT_CORRECTED as the routing basis.
2026-09-05: Tested the bounded U6 Ethernet orientation repair on the selected macro basis; native DRC still found real pad-field shorts/crossings, classified the direct escape as ROUTE_IMPLEMENTATION_FAILURE, and retained the official CM5IO-style split-layer escape as the next routing-development class.
2026-09-05: Transplanted 189 native CM5IO Ethernet MDI route items onto the corrected acreage basis; native DRC found zero Ethernet shorting items and zero track crossings while retaining inherited acreage debt, strengthening the classification of local failures as ROUTE_IMPLEMENTATION_FAILURE.
2026-09-05: Tested vertical 0-degree TPD4EUSB30 pad-field orientations with symmetric channel remapping; native DRC still found real Ethernet pad convergence shorts/crossings, so the direct escape remains ROUTE_IMPLEMENTATION_FAILURE and the next class is staged split-layer escape.
2026-09-05: Tested a wider coherent U6/U9 Ethernet-local staging move at (12,112)/(20,112); native DRC remained 288 violations with real pad-field shorts/crossings, exhausting direct-F.Cu fanout and advancing the official split-layer escape class.
2026-09-05: Tested the first hand-authored staged split-layer Ethernet source escape; native DRC rejected it with 317 violations, 456 unconnected items, real shorts/crossings, and dangling transitions, so the attempt remains ROUTE_IMPLEMENTATION_FAILURE and the saved CM5IO route remains the oracle.
2026-09-05: Materialized C48-C52 and R26-R31 plus native J2/J7 CT and LED net ownership on the official CM5IO MDI-placement candidate; native DRC found no shorting or crossing records, establishing the support materialization boundary before support routing.
2026-09-05: Tested the first official-placement CT/common support route; native DRC added 16 shorts and 15 crossings against a zero-short/zero-crossing parent, so the hand-authored support fanout was rejected as ROUTE_IMPLEMENTATION_FAILURE.
2026-09-05: Reran the complete CM5IO Ethernet fixture authoring path with CT ties; native DRC found zero unconnected items, shorts, crossings, dangling vias, and footprint errors, establishing the complete MDI/support implementation oracle for acreage adaptation.
2026-09-05: Ran the repository CM5IO MDI and native-DRC regression tests against the complete fixture; both passed, with TD0-TD3 pair length differences below 0.83 mm and no shorts, crossings, dangling vias, unconnected pads, or footprint errors.
2026-09-05: Regenerated the 189-item official MDI route at the live board minimum 0.13208 mm width; focused native connectivity passed and native DRC found zero Ethernet shorts, crossings, or width violations, retaining the official endpoint placement as a routing oracle only.
2026-09-05: Transplanted the complete native CM5IO CT/common/shield support route onto the official-placement candidate with legal ordinary through-vias; native DRC added no shorts, crossings, width, or drill violations, and the full support connectivity audit plus real-trace negative control passed.
2026-09-05: Tested R30/R31 production LED support routing on the clean official MDI/CT parent; native DRC added one short and five crossings in the hand-authored LED corridors, so the child was rejected as ROUTE_IMPLEMENTATION_FAILURE.
2026-09-05: Tested a source-adjacent mixed-side R30/R31 LED corridor on the clean official MDI/CT parent; native DRC found 20 shorts and 21 crossings, so the child was rejected as ROUTE_IMPLEMENTATION_FAILURE while the official Ethernet electrical oracle remained unchanged.
2026-09-05: Tested consultant-recommended J2-west R30/R31 staging with explicit source escapes and separated ordinary-via trunks; native DRC found 8 shorts and 39 crossings, so the child was rejected as ROUTE_IMPLEMENTATION_FAILURE without changing the official Ethernet oracle.
2026-09-05: Tested consultant-recommended J7-west source-local R30/R31 staging with separate left-edge cathode trunks; native DRC found 13 shorts and 15 crossings, so the child was rejected as ROUTE_IMPLEMENTATION_FAILURE without changing the official Ethernet oracle.
2026-09-05: Tested a rotated/staggered J7-west R30/R31 island with J2 F.Cu dogbones and separate left-edge B.Cu trunks; native DRC found 20 shorts, 15 crossings, and 430 unconnected items, so it was rejected as ROUTE_IMPLEMENTATION_FAILURE without changing the official Ethernet oracle.
2026-09-05: Re-ran the rotated/staggered LED probe with native transformed-pad endpoints and separated J2 dogbone lanes; native DRC found 20 shorts, 15 crossings, and 430 unconnected items, so it remained ROUTE_IMPLEMENTATION_FAILURE without changing the official Ethernet oracle.
2026-09-05: Added and ran a native transformed-pad obstacle-search LED generator; both complete LED paths were found with 426 inherited unconnected items, but native DRC found 4 shorts and 16 crossings in dense connector/mounting-hole fields, so the probe was rejected as ROUTE_IMPLEMENTATION_FAILURE pending native hole-clearance inflation.
2026-09-05: Corrected the obstacle-search receipt date to match the native DRC timestamp; no design result changed.
2026-09-05: Corrected the obstacle-search receipt date to match the native DRC timestamp; no design result changed.
2026-09-05: Tightened the native LED obstacle search with pad/hole inflation, route reservation, and forced B.Cu cathode trunks; focused native DRC reached zero LED shorts/crossings with 426 inherited unconnected items, and the LED BuildConnectivity audit plus real-trace negative control passed.
2026-09-05: Tightened the native LED obstacle search with pad/hole inflation, route reservation, and forced B.Cu cathode trunks; focused native DRC reached zero LED shorts/crossings with 426 inherited unconnected items, and the LED BuildConnectivity audit plus real-trace negative control passed.
2026-09-05: Recorded the focused LED route promotion candidate; official MDI/CT/common/shield and LED native connectivity gates pass, while integrated mechanical, parity, power/return, and acreage validation remain open.
2026-09-05: Completed the fresh whole-board functional-island macro discriminator from native CM5 pad coordinates, generated five disposable candidates, and selected the mechanically screened Ethernet-local migration basis; storage-local candidates remain rejected for body/support overlap and Phase 24 stays open pending coordinated regeneration.
2026-09-05: Reconciled the fresh whole-board macro review with the independent native review: the older integrated ancestor exposed the topology gap, while PHASE24_CORRECTED_MACRO_PLACEMENT remains the selected coherent Ethernet-west/storage-mid basis; the single-Ethernet diagnostic is not promoted and Phase 24 stays open for coordinated regeneration.
2026-09-05: Corrected the Ethernet generator's duplicate-ESD-pad chaining and broad terminal-halo behavior; the first correction improved the disposable DRC result but residual shorts/crossings remain, while the strict terminal-clearance probe correctly refused a path, establishing pad-shape-aware escape as the next route-implementation task.
2026-09-05: Extended the Ethernet generator with native rectangular pad occupancy, via-clearance reservations, and preserved duplicate-pad terminals; V5/V6 reached zero crossings with only localized shorts, while stricter via-aware and alternate-order trials dead-ended, preserving route-implementation evidence without changing the selected macro or validation gates.
2026-09-05: Added separate native-pad-derived via occupancy and controlled all-F.Cu/reverse-order Ethernet experiments; V6 reached zero crossings with two localized shorts, while strict via-aware variants correctly rejected unsafe paths, establishing explicit CM5IO-derived pad-field departure templates as the next implementation class.
2026-09-05: Added a native transformed-pad ESD departure-cell audit; all immediate 0.25 mm cardinal cells are blocked by the dense pad-field envelope, establishing continuous pad-edge dogbones and directional escape corridors as a generator requirement without declaring the package unroutable.
2026-09-05: Extended the native ESD escape audit to scan 0.25 mm cardinal dogbone centerlines through 2.0 mm; valid N/S package-end departures exist for every signal pad, converting the immediate-cell result into concrete directional seeds for the next routing template.
2026-09-05: Ran a CM5IO-derived J7 source-escape template on the selected macro; native DRC found 221 violations with source crossings, SERVICE/power shorts, dangling template vias, and expected opens from the partial fixture, so the old waypoints were rejected as ROUTE_IMPLEMENTATION_FAILURE and local directional lanes remain required.
2026-09-05: Tested explicit upper-pad approach/lower-pad departure dogbones; V11 reached zero Ethernet shorts/crossings but retained a J2 connectivity open, and V12 applied a generic post-via emitter correction without changing that result, isolating the remaining break to saved ESD-to-MagJack connectivity.
2026-09-05: Snapped Ethernet route seeds/entries to the native 0.25 mm grid and joined duplicate ESD pads from the upper approach terminal; V15 completed all eight MDI routes with zero native shorts/crossings and a passing focused BuildConnectivity audit, while inherited dangling vias and incomplete-board opens keep Phase 24 open.
2026-09-05: Completed the required whole-board macro-floorplan discriminator using native CM5 carrier-mating pad topology, explicitly separating floorplan quality from routing maturity; retained the corrected Ethernet-west/storage-mid basis, paused further local routing, and recorded the translated CM5IO support audit as focused route evidence only.
2026-09-05: Closed the macro-review provenance reservation by generating native metrics directly from the selected candidate with complete Ethernet support and complete storage island; Ethernet same-net topology is 97.45 mm and storage USB3-source topology is 145.11 mm, while route-quality and full-board gates remain open.
2026-09-05: Ran the first fair coordinated-neighborhood route cycle after the macro discriminator: local Ethernet LED/support and selected storage trials were rejected as ROUTE_IMPLEMENTATION_FAILURE by native DRC, while focused CM5IO connectivity audits and negative controls passed; the selected macro was retained and no mature-vs-immature DRC comparison was used.
2026-09-05: Corrected the storage generator's broad U7 pad cleanup after native evidence showed valid pads 6/7/9 were being stripped; the pad-authoritative north-escape rerun removed the false no-net landing class but remained ROUTE_IMPLEMENTATION_FAILURE with 5 shorts and 8 crossings, preserving the selected macro and validation gates.
2026-09-05: Added a native north SATA escape, explicit USB3 TX_P pad-field avoidance, and layer-separated M.2 launch; the best isolated V15-parent trial reduced the candidate to 4 shorts and 8 crossings, remained ROUTE_IMPLEMENTATION_FAILURE, and preserved the selected macro and gates.
2026-09-05: Refined the coordinated storage generator to preserve native U7 pad fields, add north SATA escape and layer-separated M.2 launch options, and avoid the USB3 TX_P opposite-pad field; the best candidate remained ROUTE_IMPLEMENTATION_FAILURE with 4 shorts and 8 crossings, so the selected macro and gates were preserved.
2026-09-05: Tested coherent U7 rotation-270 and farther-out storage-island translations; both were rejected by native DRC as ROUTE_IMPLEMENTATION_FAILURE, with the latter crossing frozen PCIe/clock corridors, so the Ethernet-west/storage-mid macro basis remained selected.
2026-09-05: Tested coherent U7 rotation-270 and farther-out storage-island translations; both were rejected by native DRC as ROUTE_IMPLEMENTATION_FAILURE, with the latter crossing frozen PCIe/clock corridors, so the Ethernet-west/storage-mid macro basis remained selected.
2026-09-05: Corrected the native-pad SATA A* obstacle model so all saved pads remain obstacles and terminal halos are segment-local; the disposable trial reached zero shorts and four localized RX launch crossings, remaining ROUTE_IMPLEMENTATION_FAILURE with incomplete-board opens preserved.
2026-09-05: Corrected the native-pad SATA A* obstacle model so all saved pads remain obstacles and terminal halos are segment-local; the disposable trial reached zero shorts and four localized RX launch crossings, remaining ROUTE_IMPLEMENTATION_FAILURE with incomplete-board opens preserved.
2026-09-05: Added pair-aware RX corridor bias and a 3 mm no-via M.2 launch guard to the native SATA A* trial; native DRC reached zero shorts and zero track crossings with eight hole-clearance findings, while incomplete-board opens keep Phase 24 open.
2026-09-05: Added pair-aware RX corridor bias and a 3 mm no-via M.2 launch guard to the native SATA A* trial; native DRC reached zero shorts and zero track crossings with eight hole-clearance findings, while incomplete-board opens keep Phase 24 open.
2026-09-05: Preserved J3 NPTH keepouts and tested bounded right-side terminal waypoints; hole-clearance records reached zero but coarse direct launches introduced six shorts and 15 clearances, so the candidate was rejected as ROUTE_IMPLEMENTATION_FAILURE and the storage placement was retained.
2026-09-05: Preserved J3 NPTH keepouts and tested bounded right-side terminal waypoints; hole-clearance records reached zero but coarse direct launches introduced six shorts and 15 clearances, so the candidate was rejected as ROUTE_IMPLEMENTATION_FAILURE and the storage placement was retained.
2026-09-05: Instrumented the SATA router with hard physical-hole preservation, side-gated launches, and explicit source vias; the follow-up still rejected coarse direct terminal segments at 6 shorts and 15 clearances with zero crossings, preserving the selected storage floorplan and requiring a proper pad escape.
2026-09-05: Instrumented the SATA router with hard physical-hole preservation, side-gated launches, and explicit source vias; the follow-up still rejected coarse direct terminal segments at 6 shorts and 15 clearances with zero crossings, preserving the selected storage floorplan and requiring a proper pad escape.
2026-09-05: Tested separated RX escapes and a dedicated TX_N outboard column; native DRC regressed to one short and eight crossings, so the waypoint variant was rejected as ROUTE_IMPLEMENTATION_FAILURE and the prior zero-short baseline retained.
2026-09-05: Tested separated RX escapes and a dedicated TX_N outboard column; native DRC regressed to one short and eight crossings, so the waypoint variant was rejected as ROUTE_IMPLEMENTATION_FAILURE and the prior zero-short baseline retained.
2026-09-05: Tested a complete bridge-side RX B.Cu layer split with ordinary source vias; bridge crossings cleared, but native DRC produced six shorts and four hole-clearance findings at U7 launch, so the trial was rejected and the prior zero-short baseline retained.
2026-09-05: Tested a complete bridge-side RX B.Cu layer split with ordinary source vias; bridge crossings cleared, but native DRC produced six shorts and four hole-clearance findings at U7 launch, so the trial was rejected and the prior zero-short baseline retained.
2026-09-05: Tested separate F.Cu U7 RX dogbone escapes before ordinary vias; native DRC produced seven shorts, two crossings, one hole-clearance violation, and 23 clearances, so the local geometry was rejected without changing the storage macro.
2026-09-05: Tested separate F.Cu U7 RX dogbone escapes before ordinary vias; native DRC produced seven shorts, two crossings, one hole-clearance violation, and 23 clearances, so the local geometry was rejected without changing the storage macro.
2026-09-05: Ran an outboard-J3 placement discriminator at (165,125); it cleared all M.2 hole violations and shorts but retained two U7 bridge-side crossings, separating the socket and U7 escape constraints without rejecting the macro placement.
2026-09-05: Ran an outboard-J3 placement discriminator at (165,125); it cleared all M.2 hole violations and shorts but retained two U7 bridge-side crossings, separating the socket and U7 escape constraints without rejecting the macro placement.
2026-09-05: Tested opposite top-edge U7 RX dogbone departures before ordinary vias; native DRC produced eight shorts, one crossing, and 20 clearances, so the escape geometry was rejected without changing the storage macro.
2026-09-05: Tested opposite top-edge U7 RX dogbone departures before ordinary vias; native DRC produced eight shorts, one crossing, and 20 clearances, so the escape geometry was rejected without changing the storage macro.
2026-09-05: Ran U7-west and J3-placement discriminators; U7 translation reproduced zero shorts/crossings, U7-west plus outboard J3 cleared hole violations but retained two crossings, and a north-band J3 produced two shorts/two crossings, so no placement was promoted.
2026-09-05: Ran U7-west and J3-placement discriminators; U7 translation reproduced zero shorts/crossings, U7-west plus outboard J3 cleared hole violations but retained two crossings, and a north-band J3 produced two shorts/two crossings, so no placement was promoted.
2026-09-05: Transplanted the preserved Phase 19 native SATA island with coherent U7/J3/C30-C33 placement and actual base-board nets; U7 pad authority passed and native DRC reached zero shorts, crossings, and M.2 hole violations, leaving five duplicate U7 RX-N pad-field opens and 428 incomplete-board opens.
2026-09-05: Completed the whole-board macro-floorplan discriminator and promoted the coherent Phase 19 USB3/SATA transplant with C16/C17/C19 moved as a low-profile B.Cu support row; native DRC reports zero shorts/crossings, zero storage opens, and 419 inherited board opens.
2026-09-05: Promoted a native bridge regulator-support oracle overlay onto the coordinated storage baseline; native DRC remains at zero shorts/crossings, affected bridge reset/feedback/PG/RT opens reach zero, and total incomplete-board opens fall to 407.
2026-09-05: Promoted the passing V2 complete clock-support transplant onto the storage/power basis; native DRC remains at zero shorts/crossings, clock and storage opens are zero, and total incomplete-board opens fall to 397 without adding clearance or courtyard classes.
2026-09-05: Promoted local In3 power-entry planes for the two cold-plug B-input nets; native DRC remains at zero shorts/crossings and full-board unconnected items fall from 397 to 390.
2026-09-05: Promoted the native 13-column J1 protected-field bus onto the current basis; native DRC remains at zero shorts/crossings, 12V_PROTECTED opens fall from 146 to 17, and total board opens fall from 390 to 261.
2026-09-05: Applied the validated U1/U2/J4/U8 global POWER_GND launch cluster to the current basis; native DRC remains at zero shorts/crossings and total board opens fall from 261 to 254.
2026-09-06: Rechecked the corrected native U5 connectivity audit and its real-trace negative control on the integrated basis; rejected POWER_GND, BRIDGE_1V1 plane-access, and local-link probes after native shorts appeared, preserving the zero-short/crossing promoted basis at 254 unconnected items.
2026-09-06: Promoted dogbone-routed native POWER_GND capacitor links; DRC remains at zero shorts/crossings, capacitor-field opens close, and total unconnected items fall from 254 to 251 with clearance findings reduced from 13 to 12.
2026-09-06: Promoted local same-layer Ethernet support-ground joins; native Ethernet connectivity and its real-track negative control pass, DRC remains at zero shorts/crossings, and total unconnected items fall from 251 to 249.
2026-09-06: Promoted a bounded In2 bridge-1V1 capacitor-bank plane with offset through-vias; all 12 capacitor pads are natively connected, DRC remains at zero shorts/crossings, and total unconnected items fall from 249 to 238.
2026-09-06: Promoted the narrow U5 repeated-output field bridge after rejecting the wider U5.5 dogbone for new clearances; native DRC remains at zero shorts/crossings and total unconnected items fall from 238 to 237.
2026-09-06: Promoted the isolated U5 protected-input top-edge join after rejecting the crossing U4/U5 variant; native DRC remains at zero shorts/crossings and total unconnected items fall from 237 to 236.
2026-09-06: Rejected U4 B.Cu protected-input and U7 BRIDGE_1V1 dogbone variants for new clearances/crossings/shorts; retained the zero-short/crossing promoted basis and recorded both as route-implementation failures.
2026-09-06: Promoted the native F1 `/POWER_INPUT/12V_IN_A` four-pad B.Cu field; DRC remains at zero shorts/crossings and total unconnected items fall from 234 to 231.
2026-09-06: Promoted the native F1 `/POWER_INPUT/FUSED_12V_A` four-pad B.Cu field; DRC remains at zero shorts/crossings and total unconnected items fall from 231 to 229.
2026-09-06: Promoted the native Q1 fused-A local launch to the existing B.Cu segment; DRC remains at zero shorts/crossings and total unconnected items fall from 229 to 228.
2026-09-06: Promoted the D1 fused-A F.Cu-to-elevated-B.Cu parallel launch after rejecting the crossing first path; native DRC remains at zero shorts/crossings and total unconnected items fall from 228 to 227.
2026-09-06: Rejected direct and offset-via C4/U2 12V_IN_B launches after native VCAP_B shorts/crossings; retained the zero-short/crossing promoted basis and documented the unresolved power-entry route.
2026-09-06: Promoted the obstacle-aware C4/U2 12V_IN_B launch with lateral U2 transition; native DRC remains at zero shorts/crossings and total unconnected items fall from 227 to 225.
2026-09-06: Rejected direct Q1/U1 12V_PROTECTED launch after it shorted an existing Ethernet trace; retained the zero-short/crossing promoted basis and documented the local power-routing conflict.
2026-09-06: Promoted dogbone-routed regulator-side BRIDGE_3V3 capacitor links without merging the distinct storage net; native DRC remains at zero shorts/crossings and total unconnected items fall from 236 to 234.
2026-09-06: Promoted the local C14/C15 12V_PROTECTED dogbone around their opposite ground pads; native DRC remains at zero shorts/crossings and total unconnected items fall from 225 to 224.
2026-09-06: Promoted the edge-side C23/C24/C25 12V_PROTECTED dogbone field; native DRC remains at zero shorts/crossings and total unconnected items fall from 224 to 222.
2026-09-06: Rejected U3 protected-input offset-via bridge after native clearance/short failure at the central POWER_GND pad; retained the zero-short/crossing promoted basis and recorded the placement-aware repair target.
2026-09-06: Promoted the native CM5 5V FB_CM5_5V C9/R3/R4 dogbone chain; native DRC remains at zero shorts/crossings and total unconnected items fall from 222 to 220.
2026-09-06: Promoted the adjacent U7 `/STORAGE/BRIDGE_3V3` U7.30/U7.31 native pad join without merging the regulator-side net; DRC remains at zero shorts/crossings and total unconnected items fall from 220 to 219.
2026-09-06: Promoted the U7.24-to-U7.30/U7.31 storage 3V3 dogbone field; native DRC remains at zero shorts/crossings and total unconnected items fall from 219 to 218.
2026-09-06: Completed the corrected whole-board macro-floorplan discriminator from the current accepted native PCB; topology-only comparison selects ETH_OUTBOARD_STORAGE_LOCAL for storage-neighborhood development without using immature routing DRC as floorplan evidence.
2026-09-06: Refined the whole-board macro discriminator with mechanical screening; selected STORAGE_LOCAL_CLEAR2 as the coherent storage-island basis, reducing USB3/storage same-net ratsnest from 231.2 mm to 88.1 mm with no moved-body overlaps.
2026-09-06: Refined the selected storage basis to STORAGE_LOCAL_J3_EDGE and preserved native routing-development evidence; manual USB3 split-layer probe reached zero shorts/crossings but remains unpromoted with 259 opens and 15 clearances, while SATA probes were rejected as route-implementation failures.
2026-09-06: Recorded the selected-basis storage route-method correction; native manual USB3 geometry has zero shorts/crossings but remains open, and SATA dense-pad escape remains a route-implementation failure with no severity waiver.
2026-09-06: Corrected the manual USB3 layer-transition emitter to preserve real via contact across duplicate-coordinate transitions; native opens fell to 251 with zero shorts, but the candidate remains unpromoted with crossings, clearances, and dangling items.
2026-09-06: Rejected the follow-up manual USB3 lane-order probe after native DRC retained zero shorts but exposed seven crossings and unresolved dangling transitions; next work changes to reference-topology transplant rather than same-class coordinate sweeps.
2026-09-06: Added and natively exercised a disposable storage-topology transplant control; KiCad 10 donor snapshots are required before target mutation, and the inherited-board control remains rejected at 510 violations and 258 unconnected items without changing the selected macro-floorplan basis.
2026-09-06: Corrected the selected-placement USB3 escape to use the CM5IO launch side before the B.Cu corridor; native shorts fell from six to two, but the candidate remains rejected at 537 violations and 259 unconnected items with no copper promotion.
2026-09-06: Rejected the second selected-placement USB3 escape after U7 pad-field approaches produced 12 shorts, 42 crossings, and 259 opens; hand-authored corridor tuning is exhausted and the next route class must transplant proven dense-pad escape semantics.
2026-09-06: Corrected the USB3 probe count after matching KiCad's tracks_crossing label; the via-spaced candidate has zero shorts but nine crossings, 259 opens, and 42 clearance findings, so it remains unpromoted.
2026-09-06: Added a native BuildConnectivity audit confirming all four J7-to-U7 USB3 endpoint memberships in the saved probe; this endpoint proof does not waive its remaining DRC crossings, clearances, or whole-board opens.
2026-09-06: Rejected two further USB3 TX lane-order trials; the first retained nine crossings and the second increased them to ten against the SERVICE corridor, so same-class hand-authored tuning is stopped while native endpoint connectivity remains proven.
2026-09-06: Ran a disposable SERVICE-corridor discriminator; removing only inherited SERVICE_RD_B reduced USB3 escape findings to one short and four crossings while all four native endpoints remained connected, separating inter-island conflict from dense-pad escape failure without promoting copper.
2026-09-06: Built the direct monotonic USB3 reference-channel probe; native DRC reached zero shorts, zero crossings, and zero annular-width violations with all four native endpoints connected, but 42 clearances and 260 inherited opens remain, so it is not promoted.
2026-09-06: Isolated USB3 in a minimal native J7/U7 fixture; the prior fanout had two clearances with zero shorts/crossings and complete endpoints, while an angular RX launch introduced 13 DRC violations and was rejected without promotion.
2026-09-06: Refined the minimal USB3 J7/U7 fixture to one native clearance finding with zero shorts/crossings and complete endpoint connectivity; the remaining error is the full-width RX_P escape against adjacent J7 ground pad 132, with no rule waiver or promotion.
2026-09-06: Extracted the official CM5IO Rev 2 native USB3 CAD; all four USB3-0 nets use 0.147 mm F.Cu/B.Cu segments with ordinary through-via counts recorded in a reproducible receipt for the next PiSXMe adaptation.
2026-09-06: Compared native CM5IO and PiSXMe USB3 launches; both use 0.2 x 0.7 mm pads on 0.4 mm pitch, but CM5IO allows 0.125 mm clearance versus PiSXMe's 0.150 mm, identifying the remaining RX_P issue as a launch-rule/geometry mismatch rather than footprint mismatch.
2026-09-06: Rejected a divergent full-width USB3 launch negative control after native DRC found seven violations including an RX_P short to CM5 PCIe pad 124; restored the prior best source-via geometry with no rule or integrated-board change.
2026-09-06: Re-ran the whole-board native macro-floorplan discriminator from the current integrated candidate, regenerated multiple disposable island candidates, retained STORAGE_LOCAL_J3_EDGE on topology-only metrics, and recorded the official CM5IO native DRC context (76 findings, zero shorts/crossings/unconnected/annular records) without promoting immature routing or changing Phase 24 scope.
2026-09-06: Expanded the macro-floorplan receipt with explicit per-island corridor, expected-transition, congestion/return, and mechanical-access assessments; actual crossings and via counts remain intentionally deferred to valid routing rather than fabricated during placement-only ranking.
2026-09-06: Attempted an official CM5IO USB3 source-escape transplant using a native pad-frame transform; seven RX source segments were extracted, but KiCad 10 pcbnew segfaulted while adding the first transformed via before save, so the experiment is preserved as tooling-authoring failure with no integrated-board or validation-rule change.
2026-09-06: Corrected the CM5IO USB3 transplant load-order and layer-preservation defects, then tested mirrored source-frame and pair-layer variants; the best disposable fixture has zero shorts, four crossings, one clearance, one hole-clearance, 65 expected opens, and complete native J7-to-U7 endpoint connectivity, with no integrated copper promotion.
2026-09-06: Tested the authorized U7 0-degree orientation against the CM5IO source ordering; spaced endpoint vias and a TX_P layer variant reduced the disposable fixture to zero shorts, one crossing, zero clearances, two dangling transitions, 65 expected opens, and complete native USB3 endpoints, while a TX_N dogleg regression was rejected without integrated promotion.
2026-09-06: Rejected the TX_N local endpoint dogleg after it introduced two RX-lane crossings; retained the U7-at-0-degree CM5IO-derived candidate at zero shorts, one crossing, zero clearances, two via-dangling warnings, 65 expected fixture opens, and complete native USB3 endpoints, with no acreage promotion.
2026-09-06: Tested a moved-U7 local USB3 corridor at (100,90); the CM5IO-derived source dogleg reduced the isolated fixture to zero shorts, one crossing, zero clearances, zero hole-clearance, zero dangling-via findings, and complete native endpoints, while a TX_P F.Cu alternative shorted U7 BRIDGE_3V3 and was rejected without acreage promotion.
2026-09-06: Promoted the isolated zero-DRC CM5IO-derived USB3 fixture into a disposable U7-at-0-degree acreage copy; focused endpoints remained connected, but integrated DRC exposed four shorts and seven crossings against PCIe/power/reference geometry, so the candidate was rejected as route-integration failure with no accepted copper change.
2026-09-06: Completed the required whole-board functional-island macro review from native CM5 carrier-mating pad coordinates, generated six disposable topology candidates, rejected closer but body-conflicting migrations, checkpointed the corrected basis, and resumed Phase 24 routing only after separating floorplan quality from immature route quality.
2026-09-06: Ran native USB3 route-development experiments after the macro discriminator: rejected a generic A* source-halo route for connector-pad shorts, promoted the validated CM5IO-derived route with zero shorts/crossings but two localized clearances, and rejected an RX_N dogleg regression while preserving all endpoint evidence.
2026-09-06: Refilled zones before USB3 DRC, confirmed the TX-launch-separated CM5IO route reduced the candidate to inherited findings plus one local RX clearance, and rejected the selected-macro landing-via A* continuation after native DRC exposed unreserved source-transition shorts/crossings.
2026-09-06: Corrected the USB3 router to reserve source-transition geometry and tested spread source vias on the selected macro; native endpoints passed and true shorts were removed, but one crossing and six clearances remained, so the candidate was rejected as route implementation failure without moving the macro.
2026-09-06: Tested explicit field-aware U7 SATA bridge escapes on the coherent storage island; direct pad-field geometry was rejected, the corrected escape reduced to a USB3-corridor crossing, and a right-side detour collided with PCIe/PERST, while USB3 and U7 pad authority remained native-pass.
2026-09-06: Transplanted the preserved native Phase 19 USB3/SATA route into the coherent storage candidate; all USB3 and SATA endpoint assertions passed with zero shorts/crossings, and a native negative-control trace removal correctly failed connectivity, while full Phase 24 closure remains open.
2026-09-06: Tested coordinated U7 support/clock/3V3 copper against the native USB3/SATA oracle; the independent support placement created one C19-to-USB3 short, so the combination was rejected as route implementation failure while both local oracles remained preserved.
2026-09-06: Tested B.Cu and F.Cu coordinated USB3 TX_N escapes around the U7 support island; B.Cu conflicted with PCIe/oscillator return and F.Cu conflicted with RX_P/clock geometry, so both were rejected with native endpoint evidence preserved.
2026-09-06: Applied a true KiCad underside flip to U7 support capacitor C19; the combined storage candidate removed the C19-to-USB3 short, retained zero shorts/crossings, and natively joined clock/reset/data fields, while power-cap closure remains open.
2026-09-06: Reviewed the true underside C19 candidate against nearby native footprints; its local 12 mm B.Cu neighborhood is open, so the candidate remains viable pending full enclosure/standoff/assembly and power-return validation.
2026-09-06: Audited the authoritative storage/regulator hierarchy and netlist; both bridge supply ports are absent and storage/regulator rails are distinct unjoined nets, so no PCB-only power closure was claimed and a native hierarchy repair became the earliest Phase 24 defect.
2026-09-06: Added and natively proved explicit STORAGE/REGULATORS BRIDGE_3V3 and BRIDGE_1V1 hierarchy ports, applied the repair to the clean schematic, and confirmed merged netlist rails with no targeted hierarchy ERC errors; PCB regeneration and Phase 24 closure remain open.
2026-09-06: Authority-checked PCB bridge-rail synchronization exposed stale U7.3 PWM1 ownership and a board-only TP5 route to a no-net pad; rejected the disposable candidate and kept Phase 24 fail-closed pending schematic/PCB test-point correction.
2026-09-06: Corrected the disposable PCB from the repaired netlist by clearing stale U7.3 and synchronizing U7 bridge rails, removed the unsourced TP5 launch, and revalidated native USB3/SATA endpoint connectivity with zero shorts/crossings; inherited board DRC and power/parity closure remain open.
2026-09-06: Extended U7 authority checking to the complete repaired native netlist and found additional stale assignments on physical pins U7.1 and U7.5-U7.9; endpoint-only connectivity was insufficient, so Phase 24 remains fail-closed pending complete TUSB9261 pin-field representation.
2026-09-06: Added an exact native schematic-to-PCB ref/pin/net parity auditor; it reports the remaining full-board namespace/materialization mismatches instead of treating endpoint connectivity as board-wide authority.
2026-09-06: Compared U7 against TI TUSB9261 Rev-I PVP0064A geometry and generated a KiCad-loadable 65-pad 0.4 mm-pitch authority fixture; the prior 0.5 mm/no-pad-65 footprint is rejected pending complete power-pin and stencil closure.
2026-09-06: Audited the clean TUSB9261 netlist against TI Rev-I mandatory power, ground, VBUS, USB2 reference, and thermal-pad pins; 24 required pins are absent, proving the U7 authority repair must include the schematic support contract before PCB rematerialization.
2026-09-06: Corrected the Phase 14 footprint authoring path and production STORAGE footprint field to the TI PVP0064A 65-pad asset; the Phase 14 authority regression passes, while U7 schematic power-pin completion remains open.
2026-09-06: Expanded the production U7 symbol from the TI pin contract after disposable native proof; clean KiCad export now contains 41 U7 nodes with all mandatory pins and no hierarchy-association errors, while PCB rematerialization and support-circuit closure remain open.
2026-09-06: Replaced U7 in a disposable storage PCB with the TI 65-pad footprint; complete pad authority passed, while inherited 0.5 mm routes failed native DRC and USB3/SATA endpoints, proving a fresh route implementation is required.
2026-09-06: Normalized retained U7 route aliases against the repaired native netlist; complete pad authority still passed, but old copper remained invalid at the new TI pad field, so fresh USB3/SATA escapes are required.
2026-09-06: Added the TI-required 10 kOhm USB_R1-to-USB_R1RTN precision reference resistor to the clean STORAGE sheet; native export shows both U7 pins and R24, while VBUS support and PCB regeneration remain open.
2026-09-06: Added the TI-required 90.9 kOhm/10 kOhm USB_VBUS divider as R32/R33, verified native U7.50/source/return net membership, and resolved duplicate references without weakening ERC; PCB materialization remains open.
2026-09-06: Materialized the VBUS-inclusive TI U7 support fixture and regenerated disposable USB3/SATA escapes; native TI pad/pin authority and SATA endpoint connectivity pass, while DRC rejects the first escape geometry as route implementation failure.
2026-09-06: Corrected regenerated USB3 source-pad net normalization from the native export; canonical J7-to-U7 identity and SATA endpoints pass, while native DRC still rejects the disposable corridors as implementation failure.
2026-09-06: Added an isolated native TI-U7 route-development fixture; endpoint authority remains reproducible, while local A* escape geometry is rejected by DRC for pair crossings and pad/support clearance.
2026-09-06: Corrected TI PVP0064A land rotations after native DRC proved vertical-row overlap; corrected geometry reduces inherited-candidate DRC to 213, and an ordered disposable escape reaches all USB3/SATA endpoints with 103 remaining route violations.
2026-09-06: Added Phase 14 regression assertions for TI PVP0064A side-land rotations, preventing regeneration of overlapping 0.4 mm-pitch vertical lands.
2026-09-06: Completed a native whole-board Phase 24 macro-floorplan discriminator, selected the topology-superior SWAP_ETH_STORAGE coherent-island basis, and preserved the historical acreage board as the live snapshot while route regeneration remains open.
2026-09-06: Completed a native whole-board Phase 24 macro-floorplan discriminator, selected the topology-superior SWAP_ETH_STORAGE coherent-island basis, and preserved the historical acreage board as the live snapshot while route regeneration remains open.
2026-09-06: Began route development on the selected macro basis; native SATA endpoint membership passes for all eight endpoints, while the first A* geometry is rejected for real crossings, shorting, clearance, and unconnected findings.
2026-09-06: Began route development on the selected macro basis; native SATA endpoint membership passes for all eight endpoints, while the first A* geometry is rejected for real crossings, shorting, clearance, and unconnected findings.
2026-09-06: Generalized the native USB3/SATA route generators for selected-macro hierarchical net names; terminal connectivity remains authoritative, while second disposable escapes are rejected by native DRC as route implementation failures.
2026-09-06: Generalized the native USB3/SATA route generators for selected-macro hierarchical net names; terminal connectivity remains authoritative, while second disposable escapes are rejected by native DRC as route implementation failures.
2026-09-06: Replaced the selected-macro USB3 A* escape with ordered native pair corridors; all four USB3 endpoints pass with zero vias and no high-speed crossings/shorts/clearances, while fixture-wide incomplete-board findings remain open.
2026-09-06: Replaced the selected-macro USB3 A* escape with ordered native pair corridors; all four USB3 endpoints pass with zero vias and no high-speed crossings/shorts/clearances, while fixture-wide incomplete-board findings remain open.
2026-09-06: Recorded selected-macro SATA pair-corridor trials; all eight native SATA endpoints pass, while the best disposable route remains rejected for real local crossings and shorts in bridge/socket launch geometry.
2026-09-06: Recorded selected-macro SATA pair-corridor trials; all eight native SATA endpoints pass, while the best disposable route remains rejected for real local crossings and shorts in bridge/socket launch geometry.
2026-09-06: Completed a native U7/J3 orientation discriminator; the U7-0/J3-270 alternate is rejected for USB3 crossings, U7-field shorts, and J3/J7 hole conflicts, so the proven U7-180/J3-90 USB3 basis remains selected.
2026-09-06: Re-ran the native whole-board macro-floorplan discriminator through KiCad 10.0.5, restored the explicit topology-versus-route comparison rule and SWAP_ETH_STORAGE decision, and kept Phase 24 open for fair route development.
2026-09-06: Preserved V7/V8 SATA launch experiments after native DRC rejected their U7/M.2 corridor implementations; the failures are recorded separately from the selected macro-floorplan decision, with Phase 24 still open.
2026-09-06: Expanded the reproducible macro-floorplan record to cover source-less power and regulator neighborhoods, corridor occupancy, and downstream mechanical/reference checks without changing the selected SWAP_ETH_STORAGE topology.
2026-09-06: Preserved the source-ordered SATA V9/V10 trial; native DRC exposed U7 USB3-field and M.2 launch collisions, so the route implementation was rejected without revising the macro-floorplan decision.
2026-09-06: Audited the native U7/J3 pad fields after V10; the remaining obstruction is a reversed U7 SATA subset beside USB3 lands plus the J3 90-degree two-column launch, so the next class is an alternate native M.2 orientation rather than repeated coordinate tuning.
2026-09-06: Tested the native U7-180/J3-0 SATA launch class; its first same-row dogbone implementation was rejected by native DRC, while the ordered connector orientation remains a credible route-development basis.
2026-09-06: Produced V19, the first selected-macro SATA candidate with zero native shorts, crossings, clearance, hole-clearance, and dangling-via findings plus all eight endpoint pairs connected; pair-length matching and full-board coexistence remain open.
2026-09-06: Corrected the JAE M.2 footprint solder-mask margin from 0.102 mm to 0.050 mm and refreshed the embedded J3 by native pad-number net ownership; V21 eliminates J3 mask errors and preserves all SATA/USB3 endpoint connectivity.
2026-09-06: Completed V26 selected storage data-route validation: native SATA/USB3 endpoint audits pass, high-speed DRC has no shorts/crossings/clearance/dangling-via errors, and end-to-end SATA skew is 0.97 mm TX and 0.365 mm RX; full U7 support and board closure remain open.
# 2026-09-06 — Phase 24 V26 storage support transplant audit
Recorded native DRC rejection of the transformed U7 support-oracle transplant: the unrotated donor collides with J7/CM5 USB3, while rotated variants create true clock-net shorts/clearances. Preserved V26 SATA/USB3 data-route evidence and classified the result as a support route-implementation failure; no production board or PCIe copper was changed.
# 2026-09-06 — Phase 24 V2 clock oracle integration trial
Recorded rejection of the native-clean V2 clock fixture after a bounded transform onto V26: native DRC found clock/SATA shorts and crossings from inherited copper. The standalone clock topology remains valid; the transformed candidate was not promoted and V26 SATA/USB3 data copper remains unchanged.
# 2026-09-06 — Phase 24 V2 clock south-40 placement probe
Recorded rejection of the farther-south native V2 clock-oracle placement after native DRC found one real XI/VSSOSC short and 19 total violations. The support topology remains a valid source fixture; V26 USB3/SATA data copper was preserved unchanged.
# 2026-09-06 — Phase 24 clock pad-layer correction audit
The V2 clock fixture was retested on the V26 storage basis with its authoritative per-pad F.Cu/B.Cu layer sets preserved. The south-40 candidate passes native XI/XO/VSSOSC passive connectivity and has no native shorting, crossing, clearance, or dangling-via classes, but remains open at 73 board connections and is not promoted.
# 2026-09-06 — Phase 24 parallel U7 clock-launch probe
Recorded rejection of the direct three-via U7 clock launch: native DRC found 100 violations including true clock shorts, crossings, and clearance failures. The passive clock island and V26 data channels remain preserved.
# 2026-09-06 — Phase 24 clock launch obstacle-aware search
The actual-pad obstacle-aware B.Cu search found an XI path but no legal non-overlapping VSSOSC path in the shared local corridor. The all-B.Cu launch class was rejected as a capacity failure; V2 clock topology and V26 data routing remain preserved.
# 2026-09-06 — Phase 24 layer-aware clock launch search
Reran the actual-board launch search with XI/XO on B.Cu and VSSOSC on F.Cu. XI found a path but VSSOSC had no legal path in the inherited corridor; no copper was promoted, and the native-valid clock graph plus V26 data routes remain preserved.
# 2026-09-06 — Phase 24 coherent clock-island relocation search
Tested a 20 mm west / 10 mm south coherent migration of the native-valid V2 clock passive island. Actual-board obstacle search found no legal second B.Cu launch path; candidate rejected as corridor-capacity failure with all validated data and PCIe copper preserved.
# 2026-09-06 — Phase 24 clock source oracle revalidation
Reran the native KiCad regression for the complete V2 clock fixture: PASS. The source XI/XO/VSSOSC graph remains free of clock shorting/crossing classes; only V26 transplant/launch integration remains open.
# 2026-09-06 — Phase 24 coordinated-layer clock oracle basis
Selected the native-clean coordinated-layer clock fixture as the strongest support source. Its west/south V26 transform preserves pad-layer authority and has no shorting, crossing, clearance, or dangling-via classes; only three U7 launch tails and inherited board opens remain.
# 2026-09-06 — Phase 24 common-region clock reachability
An actual net-aware obstacle scan from ordinary U7 clock-pad exit vias found a large common B.Cu reachable region for XI, XO, and VSSOSC. This distinguishes endpoint-corridor placement failure from inherent U7 escape impossibility and directs the next candidate into that common region.
# 2026-09-06 — Phase 24 reachable-region clock migration attempt
Tested the measured common B.Cu region with a coherent clock-island translation. The inherited clock-tail endpoint was blocked before the first launch; rejected as stale-tail geometry. The next route must regenerate passive-to-U7 paths from actual pads, with V26 SATA/USB3 and PCIe unchanged.
# 2026-09-06 — Phase 24 regenerated clock common-region search
Fresh pad/net-derived common-region routing authored complete XI and XO trees, then failed to place VSSOSC through the occupied B.Cu corridor. No candidate was promoted; this localizes the remaining work to simultaneous three-net channel assignment without changing validated data or PCIe routing.
# 2026-09-06 — Phase 24 fresh common-region clock regeneration
The pad/net-derived generator authored valid XI/XO branches in a coherent open island but could not place VSSOSC after the shared B.Cu channel was occupied. Candidate rejected as sequential channel-assignment failure; native clock source and V26 data/PCIe copper preserved.
# 2026-09-06 — Phase 24 reduced-envelope clock search
Reran common-region clock routing with actual pad envelopes and a small raster guard. XI/XO trees completed, VSSOSC remained unreachable after shared B.Cu occupancy; candidate not promoted and native DRC gates remain unchanged.
# 2026-09-06 — Phase 24 clock net-order discriminator
Ran all six XI/XO/VSSOSC routing permutations from clean regenerated boards. None completed the three-net graph; failures moved among shared crystal/passive targets. Net ordering is exhausted for this placement; validated SATA/USB3/PCIe copper preserved.
# 2026-09-06 — Phase 24 mixed-layer regenerated clock milestone
Promoted the disposable `PHASE24_CLOCK_LAYERESC_DIRECT_XO` clock-support milestone: XI/VSSOSC on B.Cu, XO on F.Cu, native U7 plus passive connectivity PASS, and zero shorts/crossings/clearance/dangling-via/track classes. Full Phase 24 remains gated by bridge rails, reset/configuration, returns, and board-wide opens.
# 2026-09-06 — Phase 24 macro-floorplan comparison reaffirmed
Recorded the topology-only comparison rule and rejected the fixed-coordinate TI U7 escape as route implementation failure; mature historical DRC is not used to rank immature rearranged routing.
# 2026-09-06 — Phase 24 TI U7 native-coordinate route trials
Recorded rejection of B.Cu and mixed-layer native-coordinate USB3 route classes on the selected macro; both had real crossings/shorts against existing board obstacles and remain disposable route evidence only.
# 2026-09-06 — Phase 24 TI obstacle model refinement
Refined TI-U7 USB3 routing to account for native pad pitch and separated source transitions; no path was found under the retained-copper model, preserved as router/integration evidence rather than a placement verdict.
# 2026-09-06 — Phase 24 obstacle-aware TI U7 router probe
Added and exercised a native-pad obstacle-aware USB3 router; its conservative raster model found no first-lane path, so the result remains router-model evidence and not a macro-placement verdict.
# 2026-09-06 — Phase 24 TI pad-envelope planner correction
Corrected the obstacle planner to use anisotropic pad envelopes and explicit U7 USB3 target-land exemptions; retained-copper blocking remains a route-model issue, not a macro-placement verdict.
# 2026-09-06 — Phase 24 clean TI-U7 package discriminator
Proved all four selected-macro J7-to-TI-U7 paths are reachable in a two-footprint native fixture; rejected the first package-field escape by native DRC as TI padfield route implementation failure.
# 2026-09-06 — Phase 24 monotonic TI U7 escape control
Tested a direct native-pad monotonic escape control; native DRC reduced the clean-fixture result to 37 findings but rejected the source-via/lane geometry, preserving the result as route implementation evidence.
# 2026-09-06 — Phase 24 TI U7 lane-assignment sweep
Tested package-aware column and direct-sloped escape variants; native DRC rejected both, with the best disposable result at 18 findings, preserving the evidence for diagonal/offset routing refinement.
# 2026-09-06 — Phase 24 TI U7 diagonal escape control
Tested native-row source transitions with direct diagonal TI-U7 escapes; native DRC reported 36 findings and rejected the candidate, preserving it as route implementation evidence.
# 2026-09-06 — Phase 24 mixed-layer TI U7 pair assignment
Tested separated mixed-layer RX/TX pair escapes; the best native DRC result reached zero shorts with one crossing and one hole-clearance finding, but remains unpromoted route evidence.
# 2026-09-06 — Phase 24 TI U7 transition refinement
Refined mixed-layer TX source/target transition ordering; the best disposable result reached zero shorts and crossings with four remaining local geometry errors, and was not promoted.
# 2026-09-06 — Phase 24 TI U7 RX approach-gate sweep
Tested RX final-approach offsets; the best result remained the 10-finding zero-short/zero-crossing control, and the coordinate class was closed without promotion.
# 2026-09-06 — Phase 24 TI U7 target height sweep
Rejected a small TX target-transition height variation after native DRC regressed to 23 findings; restored the best zero-short/zero-crossing control.
# 2026-09-06 — Phase 24 TI U7 split-RX experiment
Rejected an alternate-layer RX escape after native DRC regressed to 14 findings with three crossings; restored the best mixed-layer control.
# 2026-09-06 — Phase 24 whole-board functional-island macro discriminator
Snapshotted the native integrated storage basis and completed a topology-only comparison of six disposable whole-board macro-floorplans; selected SWAP_ETH_STORAGE without promoting immature routing.
# 2026-09-06 — Phase 24 selected-macro TI-U7 integration cycle
Corrected hierarchical U7 net resolution, passed TI pin/net authority audits, and rejected two disposable integrated USB3 route controls after native DRC found real crossings/shorts; classified as route implementation failure.
# 2026-09-06 — Phase 24 integrated B.Cu source-escape experiment
Rejected a dedicated J7 source-via escape after native integrated DRC regressed to 36 shorts and 23 crossings; retained the selected macro and classified the result as route implementation failure.
# 2026-09-06 — Phase 24 corrected TI hierarchy binding and source-route cycle
Rebound regenerated TI U7 pads to the existing CM5 hierarchy, passed native authority audits, and recorded integrated fixed, obstacle-aware, and B.Cu source-escape controls as disposable route-development evidence.
# 2026-09-06 — Phase 24 CM5IO source-escape integrated cycle
Tested a clipped native CM5IO source escape with an integrated B.Cu continuation; native DRC rejected the disposable result with 16 shorts and 28 crossings, classified as route implementation failure.
# 2026-09-06 — Phase 24 TI U7 orientation reachability discriminator
Generated five native TI storage-orientation candidates; all four USB3 paths were reachable, while the shortest U7 0-degree first-pass route remained DRC-invalid and was not promoted.
# 2026-09-06 — Phase 24 U7 0-degree mixed-layer cycle
Tested RX-on-F.Cu/TX-on-B.Cu integrated routing for the U7 0-degree candidate; native DRC rejected it with 54 shorts and 16 crossings, so coordinated transition allocation remains open.
# 2026-09-06 — Phase 24 TI U7 outside-field transition probe
Moved target transitions outside the TI exposed pad field; the current F.Cu obstacle model could not reach the targets, so no copper was emitted and the route class remains open.
# 2026-09-06 — Phase 24 south coherent storage migration probe
Moved the complete storage support island south and rebound TI U7; RX was reachable but the fixed planner stalled on TX, so the candidate was retained as route-implementation evidence only.
# 2026-09-06 — Phase 24 USB3-source-local coherent storage discriminator
Corrected the placement probe to remove stale copper at moved pads; the native planner reached all four lanes, but fixed transitions still conflicted with PCIe/package geometry, so the candidate was not promoted.
# 2026-09-06 — Phase 24 clean TI-U7 west-target fixture
Separated source and west-side target transitions in the clean TI fixture; native DRC reached zero crossings with one short and three local geometry findings, and the best control was retained for final repair.
# 2026-09-06 — Phase 24 TI U7 RX target-via separation experiment
Rejected a targeted RX_P target-via relocation after native DRC regressed to 10 shorts and 12 hole findings; restored the zero-crossing clean-fixture control.
# 2026-09-06 — Phase 24 macro-floorplan comparison-bias reconciliation
Reconciled the whole-board floorplan records: selected SWAP_ETH_STORAGE from native transformed-pad topology, while keeping early candidate DRC separate from floorplan ranking and classifying immature route failures as route implementation evidence.
# 2026-09-06 — Phase 24 TI-U7 separated-target-via route probe
Tested a fresh monotonic TI-U7 USB3 escape; the best native control has zero shorts and crossings but two local approach-clearance errors, while a staggered target-via variant regressed and was rejected.
# 2026-09-06 — Phase 24 TI-U7 v2 integrated escape cycle
Applied the zero-clearance-error TI-U7 disposable escape to the selected macro; native integration found obstacle collisions and incomplete connectivity, so the fixed-corridor candidate was rejected as route implementation evidence.
# 2026-09-06 — Phase 24 obstacle-aware integrated USB3 regeneration
Removed source transition vias and regenerated all four USB3 paths from native CM5 pads with a larger B.Cu obstacle margin; the coarse integrated planner still produced shorts/crossings and was rejected as route implementation evidence.
# 2026-09-06 — Phase 24 integrated USB3 source-field refinement
Confirmed the grid planner reaches all four U7 targets but mishandles the native CM5 pad-field escape; rejected the route implementation and selected official CM5IO source-escape anchoring as the next method.
# 2026-09-06 — Phase 24 integrated USB3 lane-escape experiment
Corrected the prior DRC category transcription and authored a disposable lane-disciplined route reserving the measured PCIe B.Cu spine band for native validation.
# 2026-09-06 — Phase 24 integrated USB3 lane-escape result
Rejected the explicit PCIe-band/lane-discipline candidate after native DRC found 6 shorts and 35 crossings; retained the route-implementation classification and moved the next method to official CM5IO source-escape anchoring.
# 2026-09-06 — Phase 24 independent route review
Independent review confirmed the selected macro remains viable, identified the PCIe B.Cu spine and router landing-field defects, and selected official CM5IO source anchoring plus obstacle-aware continuation as the next route class.
# 2026-09-06 — Phase 24 CM5IO-anchored continuation
Copied the native CM5IO USB3 source escape into carrier coordinates and rejected the first integrated continuation planner after native DRC found 11 shorts and 2,251 crossings; source-anchor evidence was preserved.
# 2026-09-06 — Phase 24 CM5IO outer-acreage continuation
Tested a separated outer-acreage continuation from native CM5IO first-transition anchors; native DRC rejected it with 19 shorts and 57 crossings, preserving the source-anchor evidence and route-implementation classification.
# 2026-09-06 — Phase 24 CM5IO F.Cu lane continuation
Tested ordered F.Cu continuation lanes from the exact CM5IO first transitions; native integrated DRC rejected the class with 21 shorts and 32 crossings, so source-anchor validation is now isolated before further corridor routing.
# 2026-09-06 — Phase 24 isolated CM5IO source-anchor audit
Corrected the KiCad 10 SWIG deletion crash in the anchor harness and verified the four transformed official CM5IO first-transition escapes against native J7 with no shorts, crossings, clearance, or hole-clearance findings.
# 2026-09-06 — Phase 24 CM5IO pair-layer continuation correction
Corrected shared TX lane geometry and target-row indexing in the anchored continuation; native DRC still rejected the integrated route with 4 shorts and 36 crossings, preserving source-anchor PASS and route-implementation classification.
# 2026-09-06 — Phase 24 carrier-context local BCu source escape
Tested a native-J7 local B.Cu source escape after proving the transformed CM5IO F.Cu prefix conflicts with the existing PCIe/REFCLK breakout; the variant had zero shorts and crossings but added localized via/clearance findings and was retained for refinement.
# 2026-09-06 — Phase 24 U5 native recheck receipt
Reran the corrected KiCad-native U5 connectivity audit against the saved fixture and promoted integrated basis; both pass, and a disposable real U5.9 trace-removal control fails as required. Native DRC/unconnected findings remain open and no full-board closure was claimed.
# 2026-09-06 — Phase 24 ASM2362 JLCPCB qualification refresh
Captured the current JLCPCB ASM2362 assembly listing and EasyEDA CAD-link evidence. It improves procurement/assembly evidence but does not close missing ASMedia-authoritative pinout, reference design, firmware, or programming authority; no mystery bridge was implemented.
# 2026-09-06 — Phase 24 authority recheck
Reran the authoritative support-part pad-net, U7 supply-hierarchy, and full schematic/PCB reference-set audits; all passed. Copper routing, native DRC, and dual-mode storage qualification remain open.
# 2026-09-06 — Phase 24 USB3 selected-source A* trial
Rejected the disposable native-pad source-to-U7 A* continuation after DRC found 180 violations, 450 unconnected items, one crossing, dangling tracks, and dangling vias. No production route or macro-floorplan was promoted.
# 2026-09-06 — Phase 24 CM5IO manual south-span trial
Rejected the distinct hand-authored CM5IO-prefix south-span route after native DRC found 207 violations, 465 unconnected items, 16 crossings, and 4 shorts. No production route or macro-floorplan change was promoted.
# 2026-09-06 — Phase 24 dual-mode storage qualification pivot
Paused Phase 24 routing and completed a bounded NVMe bridge substitution review. JMicron JMS583 now supersedes ASM2362 as the preferred technical candidate because its retained manufacturer brief/detailed pin and land-pattern evidence is sufficient for design review. Added source captures, TE M-key connector authority, procurement matrix, and the narrowed blocker: legitimate JMS583 firmware/programming/supply plus exact TE customer CAD remain open. No production schematic/PCB edits or mystery firmware were authored.
# 2026-09-06 — Phase 24 JMS583 source-capture completion
Added the previously captured JMS583 Rev 2.1 detailed datasheet, text extraction, and prior product brief to the private provenance set. These files support pin/package and support-circuit review; they do not include or imply permission to redistribute proprietary firmware.
# 2026-09-06 — Phase 24 JMS581DL alternative review
Checked JMicron's current JMS581DL single-chip SATA/NVMe alternative and its JLCPCB 144TFBGA assembly listing. It is architecturally attractive but rejected pending a manufacturer ball map, detailed design pack, and legitimate firmware/programming path; no mystery BGA symbol or wiring was promoted.
# 2026-09-06 — Phase 24 TE M-key CAD capture
Captured TE's exact 1-2199230-4 customer 2D CAD archive and Rev C M.2 application specification. The customer CAD now anchors the mechanical envelope and the application Figure 2 anchors the PCB pad layout; no connector footprint was promoted before pad-by-pad authoring review.
# 2026-09-06 — Phase 24 TE M-key CAD extraction
Extracted the TE customer DXF from the retained archive for direct geometry inspection. Connector CAD authority is now locally available; footprint promotion remains gated on a native KiCad pad/courtyard/model parity check.
# 2026-09-06 — Phase 24 JMS583 mask-ROM firmware gate correction
Reconciled the JMS583 datasheet ordering-code and GPIO/SPI evidence with an independent review. The ordered device carries factory mask-ROM baseline firmware; external SPI NVRAM is optional VID/PID customization and is DNP for Rev A. Closed the firmware prerequisite, retained authorized-supply risk, and authorized storage-island implementation subject to native connector parity.
# 2026-09-06 — Phase 24 dual-mode storage library authority pass
Added a deterministic JMS583 QFN64 and TE 1-2199230-4 M-key library generator, a structural audit, and the reviewed dual-mode pin/mode contract. Corrected the TE contact geometry to the TE 18.5 mm datum/alternating-row layout and rejected an initially inferred shared TI selector footprint; HD3SS6126 package authoring remains gated on its distinct retained TQFN drawing. Native schematic integration and complete switched-mode fixture validation remain open.
# 2026-09-06 — Phase 24 selector symbol and package authority
Verified the retained TI selector package pages identify the common RUA0042A land pattern, while preserving separate symbols and footprint names for HD3SS6126 and HD3SS3412 because their pin functions differ. Added native dual-mode symbol candidates and structural library checks. Production schematic integration remains intentionally open pending pin-by-pin selector truth-table wiring and complete native mode validation.
# 2026-09-06 — Phase 24 selector source text retention
Retained text extractions of the authoritative HD3SS6126 and HD3SS3412 datasheets to make pin functions, SEL/OE behavior, package dimensions, electrical limits, and land-pattern notes reviewable without changing the production schematic or PCB.
# 2026-09-06 — Phase 24 native dual-mode schematic integration
Replaced the obsolete B-key storage connector in the authoritative storage sheet with TE 1-2199230-4 M-key contact authority and added exact-pin JMS583, HD3SS6126, and HD3SS3412 storage-local instances. Corrected TI selector USB2, power, and high-speed labels by physical pin. Native KiCad parsing and schematic audit pass, including a negative-control label-removal failure; native ERC remains open with 205 findings, so no production PCB regeneration or Phase 24 resumption is claimed.
# 2026-09-06 — Phase 24 dual-mode storage placement fixture
Created a disposable native PCB placement candidate from the selected storage macro ancestor, replacing the B-key J3 footprint and adding the U11/U12/U13 reviewed storage footprints with physical pad-net metadata. KiCad 10.0.5 loaded the candidate; native DRC recorded 1,013 violations and 482 unconnected items, so routing, net-name reconciliation, and promotion remain open.
# 2026-09-06 — Phase 24 dual-mode mode-contract and JMS583 pin correction
Corrected the JMS583 Rev 2.1 authority in the generator and embedded STORAGE symbol: REXT is pin 39, GPIO[7] is pin 12, and AVDD33 is pin 19. Added the reviewed M-key/mode matrix and a fail-closed mode audit with a negative-control schematic audit retained. Confirmed native netlist parsing and structural audits, while preserving the true open gates: no authoritative M.2 PEDET contact for passive AUTO selection, missing native JMS583 support-component network/routing, unrouted placement fixture, nonzero ERC, and TE footprint parity.
# 2026-09-06 — Phase 24 PEDET mode-control correction
Reconciled the M.2 contact-69 terminology: retained TP-053 names it CONFIG1, while the Socket 3 interface-detect definition identifies the same SATA-ground/PCIe-open contact as PEDET. Corrected J3 pin 69 to M2_PEDET, added the TI SN74LVC1G17DBVR authority capture and mode-control contract, documented the shared U12/U13 SEL truth table, and refreshed disposable PCB metadata from the reviewed schematic maps. Native netlist and structural audits still pass, but the actual mode selector, support components, routing, and native ERC/DRC closure remain open.
# 2026-09-06 — Phase 24 selector truth-table regression
Added an executable mode truth-table regression proving the shared selector contract: STORAGE_SEL=0 selects TUSB9261/SATA on both switches, STORAGE_SEL=1 selects JMS583/PCIe, and U12 HS_OE remains enabled low. This is logical evidence only; physical native mode fixtures and complete support routing remain open.
# 2026-09-06 — Phase 24 PEDET buffer schematic/PCB candidate
Added the documented TI SN74LVC1G17DBVR PEDET buffer to the storage child schematic and the disposable storage-island PCB candidate, retaining explicit M2_PEDET, STORAGE_SEL, storage power, and ground pad ownership. Native netlist parsing and placement DRC still show the candidate is incomplete; the manual override, JMS583 support network, and routed mode-aware fixture remain required.
# 2026-09-06 — Phase 24 live storage checkpoint reconciliation
Updated the current-state receipt to checkpoint `9f1bca1`, recording the corrected JMS583/M-key/U14 authority, native ERC and unrouted-placement evidence, and the exact next implementation gates. Whole-board Phase 24 remains paused until the dual-mode island itself closes.
## 2026-09-06 — dual-mode storage support-authority checkpoint

Paused the resumed Phase 24 routing work at the pushed storage checkpoint and
continued the authorized one-socket SATA/NVMe upgrade. Added the storage-local
power-off three-position mode override (`J4`), corrected U14 to buffer
`MODE_IN`, and materialized the JMS583 Rev 2.1 support obligations: 25-MHz
crystal, REXT, LXO inductor, rail/analog decoupling, reset RC, VBUS divider,
and USB/PCIe transmitter coupling. Added fail-closed structural and negative
control audits. Native schematic netlist export succeeds; the disposable PCB
placement fixture loads and native DRC runs, but it remains unrouted with 499
unconnected items and is not a pass. Native ERC remains open (407 findings).
Whole-board Phase 24 remains paused until the routed mode-aware storage fixture
and integrated validation close.

## 2026-09-06 — dual-mode storage implementation checkpoint pushed

Committed `ea8dfb6` and pushed it to the private `reva-clean` branch. The
checkpoint includes the corrected native mode-control authoring path, explicit
JMS583 support-network authority, PCB placement metadata, native-load DRC
receipt, procurement update, and a negative-control audit proving removal of
required REXT support fails. This is an implementation checkpoint, not a
storage or Phase 24 closure; routing, mode-aware physical connectivity,
connector CAD parity, and native ERC/DRC gates remain open.

## 2026-09-06 — storage checkpoint receipt reconciliation

Reconciled the live Phase 24 status and procurement matrix to private
checkpoint `7938f64`; the dual-mode storage upgrade remains the sole active
priority and whole-board routing remains paused.
## 2026-09-06 — storage audit revalidation

Re-ran the storage library, schematic, mode-contract, JMS583 support, and
negative-control audits after the private checkpoint. All structural checks
and native schematic netlist export pass. Native PCB DRC remains intentionally
nonpassing for the unrouted placement fixture (1,074 violations, 499
unconnected items); no closure claim was made. Consultant/auditor dispatch was
retry-blocked by the current thread limit, so work continued locally.
## 2026-09-06 — storage reference collision correction

Native inspection of the integrated candidate found that J4 was already the
SERVICE USB-C connector. Renamed the storage mode selector to free reference
J5 and corrected the custom 25-MHz crystal footprint with native Reference and
Value properties. Regenerated the disposable candidate; native loading and
DRC continue to run, with the candidate still intentionally unrouted.
## 2026-09-06 — storage selector hierarchy-reference correction

Corrected the J5 mode-selector schematic instance path reference as well as
its displayed reference. Native inspection now distinguishes SERVICE J4 from
storage mode-control J5 without duplicate references; the regenerated PCB
candidate contains J4, J5, and Y2 as distinct native footprints.
## 2026-09-06 — storage support namespace and native route pass

Corrected inherited PCB reference collisions by moving JMS583 support to
storage references C80-C93, R80-R83, L10, and Y10. Native inspection confirms
SERVICE J4 and storage mode J5 are distinct. Added and executed a disposable
native pad-derived low-speed support router; it saved 14 support connections
and produced a loadable PCB, while DRC remains open at 1,158 violations and
499 unconnected items. The routed fixture is not promoted.
## 2026-09-06 — storage source-net authority correction

Reconciled the storage selector authoring path to the actual CM5 hierarchy:
U12 now names its four CM5 USB3 source pins
`CM5_USB3_TX_{P,N}` and `CM5_USB3_RX_{P,N}` instead of synthetic SST/SSR
aliases. Reconciled selector ground labels to native `POWER_GND` and verified
the corrected schematic with library/instance audits and native netlist export.
The routed storage fixture remains disposable and nonpassing.
## 2026-09-06 — storage PCB authority regenerated

Regenerated the disposable storage placement candidate from the corrected
source-net and ground authority. Native KiCad loading finds J4 SERVICE, J5
mode control, U11/U12/U13/J3, and C80-C93 support references. Native DRC runs
and reports 1,072 violations / 499 unconnected items; the candidate remains
placement/routing development evidence only.

2026-09-06 — PiSXMe Phase 24 dual-mode storage: checkpointed isolated native
USB3 fixture authoring. The fixture retained only saved J7/U11/U12/C86/C87
objects and derived all copper terminals from actual pads. Native DRC rejected
the first route as ROUTE_IMPLEMENTATION_FAILURE (QFN escape entered adjacent
pads); no production PCB was promoted. The run also confirmed CORE_CM5 still
needs an explicit port-0 USB2 hierarchy interface before the storage selector
can be electrically complete. Next action: repair source authority, implement
package-side dogbone escapes, and rerun isolated native connectivity/DRC.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: corrected CM5 USB2 source
authority. CORE_CM5 pads 134/136 (`USB3-0-D_P/N`) now export explicit
CM5_STORAGE_USB2_DP/DM nets, and the native root netlist confirms J7.134 to
U12.8 and J7.136 to U12.7. Normalized U12/JMS583 USB3 bridge net names and
regenerated the disposable native storage placement candidate. Structural
audits pass; native ERC/PCB routing remain open.

2026-09-06 — PiSXMe Phase 24 dual-mode storage: regenerated the isolated USB3
fixture after source correction and changed the U12 escape to staggered
through-vias outside the QFN field. Native DRC reduced the original direct
pad-field failure but still reports route-implementation crossings/shorts in
the shared B.Cu corridor. This remains disposable evidence; next repair is
lane-order correction, not architecture or rule relaxation.

2026-09-06 — PiSXMe Phase 24 dual-mode storage: ordered the isolated USB3
destination escapes to match the B.Cu corridor and reran native DRC. The
experiment reduced shorting findings to 17; remaining crossings are localized
to source fanout, U12 dogbones, and selector-side pair fanouts. Continue with
permitted layer partitioning; architecture and validation rules remain fixed.

2026-09-06 — PiSXMe Phase 24 dual-mode storage: tested split F.Cu/B.Cu source
fanout on the isolated native USB3 fixture. The variant was rejected because
its B.Cu source trunk collided with selector-side continuation copper. This
narrows the route defect to corridor partitioning; no architecture or rule
change was made.

2026-09-06 — PiSXMe Phase 24 dual-mode storage: tested actual CM5 pad-order
monotonic USB3 routing with outward-Y U12 dogbones. The source-field crossing
class was removed, but native DRC still reports dense-package via clearance
and selector-continuation crossings. Rejected as route implementation only;
next action is farther via placement plus corridor separation.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: closed the USB2 ownership
regression in source authority. Native root netlist confirms CM5 port-0
USB2 J7.134/136 to U12.8/7, the SATA branch U12.31/32 to U7.36/35, and the
NVMe branch U12.33/34 to JMS583 U11.18/17. Structural audits pass; copper and
native ERC/DRC remain open.

2026-09-06 — PiSXMe Phase 24 dual-mode storage: regenerated storage PCB
authority after switched USB2 ownership correction. The candidate now carries
CM5_STORAGE_USB2, BRIDGE_USB, and NVMe USB net identities from the updated
authoring map. It remains a disposable placement/routing candidate pending
native copper validation.

2026-09-06 — PiSXMe Phase 24 dual-mode storage: corrected the TI RUA0042A
selector footprint from the malformed square 10/10/10/10 generator to the
authoritative 9.0 x 3.5 mm 17/4/17/4 perimeter. Geometry audit passes for
both selectors. The regenerated isolated USB3 fixture now has zero native
shorting findings; seven localized track crossings remain, so routing is
still open and no production PCB was promoted.

2026-09-06 — PiSXMe Phase 24 dual-mode storage: corrected the TI RUA0042A
perimeter pad length to the retained example-layout value of 0.60 mm (from
the prior 0.75 mm generator value). Geometry audit passes and the regenerated
isolated USB3 fixture remains zero-short; native track-width and localized
crossing findings remain open.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: rejected the next orthogonal
SMD-pad-escape USB3 experiment after native DRC found real selector/source
and cap-side corridor collisions. Preserved its raw report as disposable
evidence and restored the committed generator to the prior zero-short
baseline; architecture and authoritative package geometry remain open for
further route implementation work.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: rejected the local-cap/F.Cu
USB3 corridor experiments. Moving C86/C87 reduced the artificial detour, but
native DRC still found intersections with CM5 source escapes and package-edge
corridors. Preserved raw reports 18/19 and restored the committed zero-short
baseline; the next class requires explicit two-layer via handoffs.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: rejected the explicit
via-handoff USB3 trial after native DRC found shorts to inherited CM5 source
corridors and crossings in split capacitor paths. Preserved report 21 and
restored the committed zero-short baseline; handoff corridors must be
reserved before vias are placed.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: corrected a generator defect
that emitted the JMS583 QFN64 as only 42 pads. The generator now emits the
authoritative 16/16/16/16 QFN64 perimeter; library and structural audits
pass, and the placement was regenerated. USB3 report 24 has no selector/source
shorting findings but retains five localized crossings and partial-fixture
opens, so it is a routing baseline rather than closure evidence.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: reconciled current status and
blocker narratives with live schematic, corrected libraries, placement, and
native reports. Marked older support-instantiation, malformed-footprint, and
pre-correction routing TODOs as superseded historical snapshots. The live
JMS583 support/mode-control authority is authored; native copper, mode-aware
validation, TE parity, and procurement risk remain open. Report 28 records
the corrected-package USB3 candidate with zero shorting findings and one
remaining crossing.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: corrected the JMS583 QFN64
bottom-row RXP escape and retained RXN on the lower B.Cu lane. Native report
31 has zero authored shorting findings and zero track-width findings; one
inherited CM5-source crossing remains, with partial-fixture support opens
retained. This is a routing discriminator, not storage closure.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: corrected the narrative for
native report 32 after reinspection. It records zero authored track-width or
track-crossing findings, but retains one authored TX source-via short, along
with package-edge/J7 clearances and intentional partial-fixture opens. Current
status narratives now distinguish this remaining electrical defect from the
superseded historical TODOs.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: tested a layer-partitioned USB3
source escape, assigning CM5-source TX to F.Cu and RX to B.Cu. Native report
38 records zero shorts, track-width, or track-crossing findings, while retaining
clearance, board-edge, solder-mask, and intentional partial-fixture opens.
This is a routing candidate, not storage closure.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: moved bridge-side USB3 vias
closer to U12 and corrected their local X ordering. Native report 40 retains
zero shorts, crossings, and width findings, with 152 clearance findings and
the known partial-fixture opens. The candidate remains non-release.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: added an assertion-only native
USB3 connectivity audit. The regenerated candidate passes all ten intended
CM5/U12/U11/coupling-capacitor endpoint pairs; physical DRC and full storage
validation remain open.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: opened an isolated RTL9210B-CG
 Path-B qualification track while preserving Path A. Retained the Rev. 1.1
 pin/mode/power evidence, corroborating KiCad implementation, corrected SMD
 qualification footprint metadata, firmware/configuration artifacts, and
 current JLCPCB identity. RTL9210B is a credible one-chip candidate; virgin
 programming, firmware provenance/rights, exact production application BOM,
 and live stock/price remain open. Recommendation: continue both pending the
 narrowly defined virgin-chip bring-up and authorized application-circuit
 experiment; no production replacement was made.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: added an assertion-only
 RTL9210B artifact audit and reconciled PHASE24_STATUS with the active Path-B
 steering amendment. The audit independently verifies the 69-pin symbol,
 shared SATA/PCIe lane pins, PEDET/REFCLK/SPI evidence, corrected SMD
 qualification footprint metadata, and retained community schematic. Path A
 remains unchanged; production Path-B CAD remains gated on authorized support
 circuit and virgin-chip firmware bring-up evidence.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: applied the footprint-review
 correction to the isolated RTL9210B qualification footprint. It is now an
 explicit SMD 69-pad artifact with a fabrication body outline and conservative
 courtyard; the community source remains retained unchanged as evidence of
 its through-hole metadata defect. The authority audit passes. This remains a
 qualification artifact only until exact Realtek land-pattern and application
 circuit authority is obtained.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: natively exported XML
 netlists from the retained RTL9210B community schematic and M.2 schematic
 with KiCad 10.0.5. The receipts confirm native parsing and expose the
 shared-lane and PEDET/contact-69 nets; they are explicitly parse evidence,
 not PCB connectivity or ERC/DRC closure.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: strengthened the isolated
 RTL9210B artifact audit to verify the corrected footprint's explicit F.Fab
 body and conservative courtyard as well as its pad set and SMD metadata.
 The audit passes; no production Path-B integration was made.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: added a native XML netlist
 audit for the isolated RTL9210B/M.2 reference pair. KiCad-exported netlists
 assert the shared lane pins, USB2/USB3, PEDET/contact 69, REFCLK, PERST,
 CLKREQ, DEVSLP, and SPI evidence without synthetic edges. The removed-PEDET
 negative control fails as required. This is a native schematic/netlist gate,
 not PCB or production closure.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: generated and natively loaded
 a disposable RTL9210B-to-M-key PCB connectivity fixture, then rejected it
 after native DRC found 102 violations including crossings and a shorting
 condition. Zero unconnected items did not waive those failures. The raw
 board/report are retained as rejected route evidence; the failure does not
 reject RTL9210B architecture. The delegated KiCad review's plan-only
 standalone bring-up recommendation was retained for the next bounded
 fixture.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: retained a secondary-hosted
 RTL9210 68-pin V203 demo schematic as corroborating evidence. It explicitly
 includes an RTL9210B-CG variant and candidate support values, including the
 2.2-uH regulator inductor and 12-kOhm RSET. It is not promoted to authority;
 M-key sidebands, SSD power/inrush, firmware rights, and released land-pattern
 gates remain open.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: retained the HynixCJR
 hierarchical root reference and a KiCad 10.0.5 native root XML export. It
 confirms RTL9210B/M.2 child-sheet references but is explicitly limited to
 hierarchy/source-lineage evidence because unrelated child sheets are not
 included; no root ERC/netlist closure is claimed.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: added a native XML audit of
 the retained RTL9210B support network. It verifies the corroborating WIP
 implementation's USB2/USB3, shared lane-0, REFCLK/PERST/CLKREQ, PEDET,
 ISOLATEB, crystal, SPI flash, RSET, switched rails, and explicit unused-pin
 records, with a mutation negative control. The extraction narrows the
 standalone Path-B fixture gates but does not promote community values,
 land-pattern metadata, M-key sideband behavior, SSD power/inrush, or
 firmware provisioning to production authority.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: strengthened the RTL9210B
 corroborating audit to assert crystal values, controller rail endpoints,
 switched-rail endpoints, and a second PEDET-net negative control. The audit
 remains evidence-only; no Path-B production CAD or Path-A fallback work was
 changed.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: refreshed PHASE24_STATUS with
 the d80a395 checkpoint, the strengthened native support-netlist audit and
 negative controls, and the still-open Path-B evidence gates. The rejected
 straight-line fixture remains classified as route implementation failure;
 unrelated whole-board routing stays paused.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: corrected and machine-checked
 the RTL9210B physical M-key mapping. Platform-side contacts are TX 68/67 to
 49/47 and RX 64/65 from 43/41; the retained community root XML reverses that
 association and is now explicitly negative WIP evidence. Added the native
 socket-contact audit and kept Path-B CAD gated on authoritative application,
 sideband, power/inrush, land-pattern, and provisioning evidence.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: added a quarantine audit for
 the retained WIP hierarchy's reversed lane mapping. The audit detects the
 mismatch against native M.2 contact authority and has a mutation negative
 control; it prevents the community root receipt from becoming Path-B wiring
 authority by accident.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: updated the isolated future
 fixture specification with the corrected physical M-key lane assignment and
 an explicit prohibition on inheriting the reversed WIP hierarchy mapping.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: recorded a legitimate
 third-party 21ic reference-package recovery lead listing V004/V008
 schematics, power-consumption, and layout-guide files. The endpoint is
 login-gated here, so the files were not claimed as retrieved or used as
 authority; Path-A and Path-B production CAD remain unchanged.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: refreshed the current status
 checkpoint to 819015d after recording the reference-package recovery lead.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: ran fresh Path-A source,
 library, mode-contract, JMS583-support, and native PCB checks. Authority
 audits passed; the support-routed partial PCB remained open at 1,160 native
 DRC violations and 499 unconnected items. Captured the result without
 changing severity or waiving findings.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: corrected the disposable
 SATA A* emitter to deduplicate repeated native vias and identical/zero-length
 segments. The fresh native candidate improved from 1,246 to 1,240 DRC
 violations but remained rejected with 499 unconnected items and crossings.
 Preserved the board and raw report as route-implementation evidence; Path A
 authority and Path B qualification were not changed.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: native inspection found the
 SATA router was targeting J3.1–4 instead of the TE M-key shared lane contacts
 J3.49/47/43/41. Corrected the generic router and endpoint audit, reconciled
 the four coupling-cap outputs in the authoritative STORAGE schematic to the
 canonical M.2 net names, and preserved the pre-reconciliation DRC as rejected
 evidence. Retained hard-hole obstacles and bounded A* search; the bounded
 search did not emit a promotable candidate. Native source audits pass and
 routed-board closure remains open.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: added a reproducible
 source-to-PCB derivation for the four canonical M.2 SATA contacts and
 confirmed C30.1/C31.1/C32.1/C33.1 match J3.49/47/43/41 by native net
 inspection. Added A* closed-set handling, hard-hole preservation, optional
 J3 rotation, and bounded search. Disposable 0-degree/90-degree searches
 did not emit a promotable route; preserved the result as search/corridor
 implementation evidence without changing the integrated board.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: refreshed the live status
 checkpoint to `9645567` after pushing the source-to-PCB SATA regeneration
 bridge and bounded search receipt.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: tested the corrected source
 net map in a storage-isolated fixture with the socket translated locally.
 A* returned no route in a tight local window and exhausted its bounded search
 in a wider one. Preserved the result as a route-method failure; no integrated
 board or architecture changed.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: corrected the disposable
 SATA corridor author to use native U7 pad starts, canonical M-key contacts
 J3.49/47/43/41, explicit net codes, and a rotated vertical socket launch.
 The native endpoint audit passed all eight SATA endpoints. Native DRC still
 rejected the fixture (251 violations), so the candidate was not promoted;
 raw DRC and the focused receipt preserve the route-implementation evidence.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: refreshed the live status
 checkpoint to `e449d06` and recorded that the eight-endpoint SATA audit is
 passing while native DRC remains open on the disposable corridor trial.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: separated the native U7
 escape fanout and reran the isolated SATA corridor. Endpoint assertions
 remained PASS and DRC improved to 67 findings, but pair-corridor crossings
 and a local QFN escape interaction remained. Preserved the raw report and
 rejected the route implementation without changing Path A architecture.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: tried a pair-layer-separated
 SATA corridor, assigning TX to B.Cu and RX to F.Cu with native-pad-derived
 escapes. All eight endpoint assertions remained PASS; native DRC reported
 66 findings from shared-corridor crossings and inherited fixture opens.
 Preserved the result as rejected route-method evidence.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: refreshed the live status
 checkpoint to `5184b6f`, distinguishing the passing native endpoint audit
 from the still-failing native DRC route gate.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: reduced the SATA route trial
 to a minimal U7/C30–C33/J3 native fixture. The eight-endpoint audit remained
 PASS and native DRC reduced to 59 findings, isolating the remaining issue to
 local bridge/capacitor escape ordering. Preserved the raw report and did not
 promote the route.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: corrected the disposable
 SATA route to the saved 0.20-mm minimum width and repaired the rotated
 socket-side lane ordering. The minimal native fixture retained all eight
 endpoint assertions and improved to 14 DRC findings; it remains unpromoted.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: tested a source-order-
 preserving U7 fanout with TX on B.Cu and RX on F.Cu. All eight endpoint
 assertions passed and the minimal native fixture improved to 12 DRC
 findings. Preserved the candidate for the next focused TX-escape and
 socket-clearance repair.
2026-09-06 — PiSXMe Phase 24 RTL9210B Path B: re-ran the isolated
 qualification/audit suite, including the native netlist and intentional
 negative control. Path B remains a serious parallel candidate with the
 corrected M-key contact mapping and corroborated support network, but is not
 promoted to production CAD. The live decision remains CONTINUE BOTH pending
 one traceable virgin-chip programming/mode-bring-up experiment and a current
 Realtek application-circuit package. Path A remains preserved.
2026-09-06 — PiSXMe Phase 24 RTL9210B Path B: added explicit isolated
 authority and mode matrices covering the corrected M-key lane mapping,
 PEDET selection, package/footprint provenance, support-pin ownership, and
 promotion gates. Re-ran the symbol, support-netlist, M-key, native-netlist,
 hierarchy-conflict, and negative-control audits; all passed. Path B remains
 a serious comparison candidate, not production CAD, and Path A remains
 preserved.
2026-09-06 — PiSXMe Phase 24 RTL9210B Path B: refreshed the procurement
 snapshot from the current JLC listing, confirming the exact Realtek
 RTL9210B-CG/C5143573 identity, QFN-68 package, SMT/Economic/Standard PCBA,
 and MSL 3. The listing is PCBA-only and exposes no reproducible stock/price/
 lead-time receipt, so procurement remains an explicit risk rather than a
 fabricated availability claim.
2026-09-06 — PiSXMe Phase 24 Path A: tested three bounded SATA bridge-layer
 assignment variants against the project-local U7 footprint. All eight native
 endpoint assertions passed. The best variant reduced DRC to 11 but retained
 three real copper crossings; other variants retained shorts or crossings.
 Rejected all variants, restored the mono2 author, and preserved raw boards/
 reports for the next obstacle-aware QFN escape attempt.
2026-09-06 — PiSXMe Phase 24 RTL9210B Path B: added a hashed firmware and
 programming matrix separating enclosure updates, virgin-chip programming,
 PiSXMe configuration, recovery, and redistribution rights. Public binaries
 and configs demonstrate an ecosystem but do not close authorized virgin
 provisioning or productization; those remain a narrowly defined hardware/
 authorization experiment.
2026-09-06 — PiSXMe Phase 24 Path A: replaced embedded U7 with the project-
 local TUSB9261 footprint in a disposable native fixture while preserving all
 saved pad nets and placement. The eight-endpoint SATA audit remained PASS and
 native DRC remained at 12 findings, ruling out the embedded/project footprint
 mismatch as the route blocker. Preserved the raw board/report and redirected
 the next repair toward local route geometry and support connectivity.
2026-09-06 — PiSXMe Phase 24 Path A: checked the current TI TUSB9261 Rev-I
 package drawing and recorded the authoritative PVP0064A 0.4-mm pitch,
 1.2 x 0.2-mm pad geometry. A disposable 0.15-mm clearance API probe did not
 alter KiCad's active 0.20-mm rule basis and was rejected; no production rule
 or validation severity was weakened.
2026-09-06 — PiSXMe Phase 24 Path A: authored an explicit disposable native
 rule-basis probe with both global and default-netclass clearance set to
 0.15 mm, using the documented JLC multilayer capability as fabrication
 evidence. Native DRC reduced the unchanged mono2 fixture from 12 to 7
 findings, removing four clearance-only findings but retaining two shorts,
 one crossing, and 38 intentional fixture opens. The probe is evidence only;
 no production rule or route was promoted.
2026-09-06 — PiSXMe Phase 24 Path A: tested two native pad-derived U7
 escape repairs after the explicit rule-basis probe. They worsened the
 disposable fixture to 22 and 23 DRC findings by colliding with oscillator,
 power, RX, and TX escape geometry. Classified both as route implementation
 failures, preserved their raw boards/reports, and restored the committed
 mono2 author without changing production CAD or architecture.
2026-09-06 — PiSXMe Phase 24 Path A: coordinated the U7 QFN SATA escape
 topology using native pad identity. V4 passed all eight endpoint assertions
 with zero shorts/crossings; the 0.20-mm disposable DRC basis reported only
 six clearance and four silkscreen findings, and the explicit 0.15-mm probe
 reduced that to four silkscreen findings plus intentional fixture opens.
 Applied to the source-regenerated integrated candidate, the SATA assertions
 still passed but inherited board DRC remained 1,210/499, so no production
 board authority was promoted.
2026-09-06 — PiSXMe Phase 24 Path A: added a native net-authority guard to
 the SATA route author. It rejects stale support-routed ancestors carrying
 `/STORAGE/SATA_M2_*` capacitor nets and requires source-derived regeneration;
 canonical regenerated inputs continue to route with the V4 topology. This
prevents PCB-only stale-net ownership from being misclassified as geometry.
2026-09-06 — PiSXMe Phase 24 Path A: added and ran a V4 SATA native
 connectivity negative control. Removing one real saved track caused the
 native C30.1-to-J3.49 connection to fail, confirming the focused endpoint
 audit is assertion-only and derives connectivity from saved KiCad objects.
2026-09-06 — PiSXMe Phase 24 dual-mode storage: built one source-derived
 high-speed fixture containing USB3 selector/bridge routing and the V4 SATA
 escape. All ten USB3 and all eight SATA native endpoint assertions passed,
 but native DRC found 576 violations / 187 opens, including real crossings
 and shorts where the historical USB3 corridor intersects the SATA launch.
 Preserved it as route/placement evidence, not production authority, and
 fixed the USB3 disposable author to use safe native collection mutation.
2026-09-06 — PiSXMe Phase 24 Path A: found that the historical V4 SATA
 route bypassed the HD3SS3412 selector. Verified TI's Port A/B/C mapping,
 corrected STORAGE source labels and U13 A1 ownership, regenerated native
 selector-side pad nets, and replaced the direct SATA audit with a twelve-
 endpoint U7 -> caps -> U13 Port B -> U13 Port A -> J3 audit. Added a saved-
 track negative control. The first selector-inclusive copper author remains
 rejected for local DRC crossings/shorts; no production route was promoted.
2026-09-06 — PiSXMe Phase 24 Path A: preserved integrated-context and minimal
 selector-inclusive SATA route fixtures with native DRC receipts. Both retain
 the twelve-endpoint native PASS and the negative-control PASS, but remain
 rejected raw route evidence because U7/U13/M.2 escape implementation still
 contains real crossings and shorts.
2026-09-06 — PiSXMe Phase 24 Path A: corrected the disposable HD3SS3412
 exposed thermal pad authority. U13 pad 43 is now assigned to POWER_GND in
 generated PCB metadata, matching TI's package requirement; it is not a
 schematic signal pin. Routes crossing the thermal pad are now treated as
 real ground shorts.
2026-09-07 — PiSXMe Phase 24 Path A: regenerated the selector-inclusive SATA
 fixture from corrected source/net authority and grounded U13 pad 43. V3
 passed all twelve native selector endpoint assertions; native DRC remained
 open at 133 findings / 52 opens with two localized shorts and ten crossings.
 Preserved the V3 board/report as rejected route evidence and kept production
 CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path A: tested a disposable 180-degree U13
 orientation so Port B faced the bridge and Port A faced J3. The native
 twelve-endpoint audit passed, but the first via/escape author produced 180
 findings / 52 opens, 23 shorts, and 5 crossings. Classified it as local
 route/via geometry failure, preserved the evidence, and left V3 as baseline.
2026-09-06 — PiSXMe Phase 24 Path B: rechecked the live JLCPCB RTL9210B-CG
 listing (C5143573). It confirms Realtek identity, QFN-68, SMT Economic/
 Standard PCBA eligibility, MSL 3, and PCBA-only storage; no reproducible
 quantity-1 price, stock depth, or lead time was exposed. Saved a dated web
 receipt and kept standalone procurement as an explicit open gate.
2026-09-07 — PiSXMe Phase 24 Path A: completed the rotated U13 V3
 disposable comparison. The twelve-endpoint native audit passed, but native
 DRC regressed to 204 findings / 52 opens with six shorts and twelve
 crossings, versus V2 at 138 / 52 with six shorts and eleven crossings.
 Rejected V3 as worse local launch geometry; preserved raw evidence and left
production CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: tested an F.Cu RTL_3V3 QFN zone around
U1. Native DRC remained 4 / 30 and the native connectivity census showed no
additional required RTL_3V3 pad joins. Rejected the zone as ineffective; no
power or plane rule changed and production CAD stayed unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: preserved control-route variants V4/V5/V6
 with native results 8/34, 3/34, and 4/33 (DRC violations/open items).
 Rejected the repeated same-layer corridor class and retained the clean
 RESET_N/PERST_N baseline; next control work requires a genuinely separated
 layer departure.
2026-09-06 — PiSXMe Phase 24 Path B: refreshed the firmware boundary from
 live public guidance. The RTL9210 ecosystem documents Windows enclosure
 update/recovery and configuration dumping, while the retained technical
 document confirms SPI flash access but defers exact flash sizing to a
 Realtek FAE/agent. Kept virgin-chip provisioning, configuration authority,
 and redistribution rights OPEN/HIGH; no community image was promoted to
 production authority.
2026-09-07 — PiSXMe Phase 24 Path A: checkpointed the rotated-U13 V3
 disposable author, native PCB, and raw DRC receipt referenced by the status
 documents. The artifacts are explicitly rejected route evidence; no
 integrated or production PCB was altered.
2026-09-07 — PiSXMe Phase 24 Path B: added an independent PDF-level audit
 against the retained RTL9210B Rev. 1.1 document. It passes exact PEDET
 mode, shared SATA/PCIe lane, REFCLK, PERST/CLKREQ, ISOLATEB, clock, rail,
 RSET, exposed-pad, USB, SPI, and flash-sizing-boundary assertions; its
 PEDET mutation negative control fails as intended. This strengthens pin/mode
 evidence without promoting community firmware or production CAD.
2026-09-07 — PiSXMe Phase 24 Path B: authored the isolated RTL9210B bring-up
 fixture with corrected M-key lane mapping, support-net ownership, SPI/reset/
 UART test access, and explicit SSD-power/PEDET/sideband boundaries. Native
 DRC reports zero violations and 56 intentional unrouted items; the fixture
 audit and negative control pass. Kept it outside production CAD and recorded
 the remaining routed-fixture, programming, firmware-rights, and hardware
 validation gates explicitly.
2026-09-07 — PiSXMe Phase 24 Path B: tested two disposable support-route
 classes for the bring-up fixture. The all-F.Cu support fanout failed with
 17 crossings, 2 shorts, undersized 0.15 mm tracks, and 3 mask bridges. The
 ordered SPI B.Cu escape failed with 2 shorts plus annular/via/drill and
 clearance violations. Preserved both raw reports, classified them as route
 implementation failures, and kept production CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: corrected the disposable fixture layer
 serialization after native KiCad loaded numeric layer 2 as In4.GND rather
 than B.Cu. The generator now matches native six-layer signal ordering. A
 support-local V2 placement has a zero-violation native baseline; its first
 native-coordinate oscillator/RSET route remains rejected at 4 violations /
 52 opens from local crossings and one RSET/XTAL interaction. Preserved the
 V2 placement and raw report for the next route class.
2026-09-07 — PiSXMe Phase 24 Path B: preserved two further native-coordinate
oscillator-route trials. V3 remained at 4 DRC violations / 52 opens with
XTAL/RSET local shorts/crossing and a mask bridge; V4 regressed to 5 / 52
with two shorts and three mask bridges. Rejected both as route
implementations, retained the coherent V2 placement, and kept production CAD
unchanged before changing routing method.
2026-09-07 — PiSXMe Phase 24 Path B: changed routing method after the V3/V4
 oscillator trials. V7 separates XTAL_IN, XTAL_OUT, and RSET with native
 QFN-clear transitions and independent F.Cu/B.Cu corridors. Native DRC is
 0 violations / 52 intentional remaining opens and the independent local
 saved-track audit passes. Closed only this local oscillator/RSET sub-gate;
 the full fixture remains open and production CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: corrected the isolated SPI support route
 with staggered U1 fanout, ordinary 0.6/0.3-mm vias, a separated B.Cu
 SPICLK corridor, and an F.Cu SPISI perimeter. SPI V7 has 0 native DRC
 violations / 52 intentional fixture-boundary opens and passes its independent
 saved-track/net/via audit. Closed only the SPI local route sub-gate; kept the
full fixture and production CAD open/unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: added a disposable in-board F.Cu/B.Cu
 GND-plane and stitching-via discriminator to the clean SPI V7 fixture.
 Native DRC stayed at 0 violations and real plane connectivity reduced open
 items from 52 to 45. This closes only the fixture reference-return
 discriminator; signal/power/sideband/test-access opens and production CAD
 remain open/unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: corrected the disposable named-net
 serialization path and routed the RTL_3V3 support bus. After native zone
 refill, U2 pins 3/8, C3, and the R2/R3 3V3 returns pass the saved-net audit;
 native DRC is 0 violations / 41 remaining opens. Rejected pre-refill zone
clearance output as stale fill state and kept production CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: iterated the RTL_5V/C5 and RTL_1V1/C4
 support routes through six bounded local variants. V6 uses QFN-clear source
 escapes, ordinary vias, and separated outer-layer corridors; after native
 zone refill it passes DRC with 0 violations / 39 remaining opens. Preserved
 V1–V5 as rejected evidence and kept production CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: preserved the rejected combined
 PEDET/CLKREQ/PERST/RESET route (8 DRC violations / 33 opens) after its
 saved-net audit caught distinct reset ownership. A separate corrected
 RESET_N/PERST_N route passes native DRC at 0 violations / 37 opens. Kept
 PEDET/CLKREQ open for a different layer assignment and production CAD
 unchanged.

2026-09-08: Regenerated the storage workbench from the corrected live source
instead of reusing stale U13 copper. The native-pad-anchored SATA author now
passes all 12 SATA endpoints on
PHASE24_STORAGE_AUTHORITY_CORRECTED_USB3_SATA. The USB3 promotion author was
also hardened to resolve child `/CORE_CM5/` and canonical target net names
and to assign native target net objects. CM5 source promotion is connected;
bridge-side USB3 promotion remains open. Native DRC on the immature combined
workbench is 1,027 violations / 499 unconnected items.

2026-09-08: Aligned C86/C87 to the validated USB3 corridor and promoted the
complete ten-net USB3 route onto a regenerated live-authority storage parent;
the native USB3 audit passes. The integrated V3 SATA trial also passes all 12
SATA endpoints. It remains disposable because the regenerated parent lacks
the earlier zone-backed AVDDL/VCCO/VCCK support coverage. Corrected the SATA
author so integrated runs preserve unrelated copper/zones; only explicit
minimal fixtures scrub the board.

2026-09-08: Expanded USB3 promotion to the complete ten-net contract and
made target net resolution robust to KiCad hierarchy spelling. The source
quartet copies successfully; the bridge-side pass remains open because the
support-route parent relocates coupling capacitors and requires native-pad
anchored local rerouting rather than blind historical copper transplant.
2026-09-07 — PiSXMe Phase 24 documentation hygiene: marked the original
 RTL9210B bring-up fixture's 56-open count as historical baseline evidence
 and pointed current-state prose to the SPI V7 plus GND-plane candidate with
 45 opens. No raw receipt was rewritten and no validation severity was changed.
2026-09-07 — PiSXMe Phase 24 Path B: corrected the relocated R2/R3 control
 support placement and regenerated its RTL_3V3 named-net bus, then preserved
 three native PEDET/CLKREQ perimeter-route experiments. V1/V2/V3 reported
 6/34, 8/35, and 10/35 DRC-violation/unconnected-item counts and were
 rejected as route/corridor implementations. The evidence does not reject
 RTL9210B or Path A; production CAD remains unchanged and the next class must
 regenerate the local control departures coherently rather than add more
 detours to the mixed baseline.
2026-09-07 — PiSXMe Phase 24 Path B: regenerated the complete relocated
 RTL9210B control group through V4–V8. V5 corrected QFN-edge diagonal
 departures; V6 is the best disposable result at 3 native DRC violations /
 36 opens. V7/V8 rejected alternate RTL_5V/PEDET corridor classes at 15/32
 and 4/35. The remaining issue is a local power/control transition field;
 no production CAD or Path-A authority changed.
2026-09-07 — PiSXMe Phase 24 Path B: V9 retained the best V6 control-route
 baseline and tested a PEDET dogleg around the inherited RTL_5V via. Native
 DRC remained at 3 violations / 36 opens. The same-placement PEDET route
class is exhausted; the next step is coherent local support-island
relocation/re-authoring, with production CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: corrected the native footprint-anchor
 math for a lower-left R2/R3 placement, verified pad 1 at (69,78)/(72,78),
 and tested a regenerated lower control/3V3 route. Native DRC reported 9
 violations / 33 opens, so the placement route was rejected as an immature
 implementation. V6 remains the best disposable baseline; no production CAD
 or Path-A authority changed.
2026-09-07 — PiSXMe Phase 24 Path B: tested lower-placement V3 with
 separated PEDET/CLKREQ/PERST/RESET corridors and an early C3 3V3
 transition. Native DRC reported 10 violations / 33 opens, so it was
 rejected as a route implementation. The lower placement and RTL9210B
architecture remain unpromoted; production CAD is unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: tested V10, a QFN-safe RTL_5V departure
from U1 pad 17 on the V6 baseline. Native DRC regressed to 14 violations /
35 opens from RTL_1V1/PERST collisions and an incomplete rail join. Rejected
the rail-only repair and preserved the Path-B isolation boundary.
2026-09-07 — PiSXMe Phase 24 Path A: tested a TX-only thermal-clear launch
from the V3 selector fixture. It removed the original U13 thermal-pad shorts
but regressed to 136 native DRC findings / 52 opens with TXP/TXN via spacing
and inherited corridor conflicts. Rejected the route implementation and kept
selector authority and production CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path A: generated an isolated U13-to-J3 lane-0
launch fixture without inherited selector/bridge copper. Native DRC reported
84 findings / 32 opens, including M.2 mounting-hole/ground and connector-side
via conflicts. Rejected the launch implementation and preserved the selector
authority boundary.
2026-09-07 — PiSXMe Phase 24 Path A: tested isolated lane-0 launch V2 with
the RX lower corridors moved around J3 mounting hole M1. Native DRC reported
83 violations / 32 unconnected items. TXP/TXN/RXP final dogbones still
contacted adjacent J3 pads or ground, and RXN/RXP crossed in the target-via
field. Rejected V2 as route implementation evidence; production CAD and
Path-B isolation remain unchanged. Next work must re-author connector-side
target-via ordering rather than repeat this corridor.
2026-09-07 — PiSXMe Phase 24 Path A: tested isolated lane-0 launch V3 with
split TX/RX layers and connector-ordered target vias. Native DRC reported
103 violations / 32 unconnected items. The RX target-via field still shorted
RXN/RXP, TXN contacted inherited TUSB_SATA_RXP copper, and one crossing
remained. Rejected V3 as route implementation evidence; no production CAD or
Path-B authority changed.
2026-09-07 — PiSXMe Phase 24 Path A: tested isolated lane-0 launch V5 with
orthogonal source escapes and vertical M.2 contact-row dogbones. Native DRC
reported 80 violations / 33 unconnected items, with no shorts and one RX
source crossing. V6 changed the RX source corridors but regressed to 83 / 33
and introduced an M1 mounting-hole interaction. V5 is the best isolated
baseline; both remain rejected and unintegrated.
2026-09-07 — PiSXMe Phase 24 Path A: tested V7/V8 RXP B.Cu alternatives.
V7 reported 84 violations / 34 unconnected with an M1 short and one
crossing. V8 routed below/outboard of M1 and reported 82 / 34 with no shorts
and one crossing. Both were rejected; V5 remains the best isolated baseline.
2026-09-07 — PiSXMe Phase 24 Path A: tested V9/V10 source-escape repairs.
V9 reported 81 violations / 34 unconnected with one RX source short. V10
moved the RXP transition below RXN's escape and reported 81 / 34 with zero
shorts and zero crossings. V10 is the best topological baseline, but M.2
contact-row clearance findings remain; no production CAD changed.
2026-09-07 — PiSXMe Phase 24 Path A: tested V11/V12 staggered M.2 final
dogbone departures. V11 reported 79 / 34 with 72 clearance findings but one
crossing. V12 swapped the conflicting departures and reported 81 / 34 with
zero shorts and zero crossings. V12 is the best topology candidate, not a
PASS; production CAD remains unchanged.
2026-09-07 — PiSXMe Phase 24 Path A: tested V13 with 0.10-mm disposable
escape tracks to discriminate contact-field clearance. Native DRC reported
102 / 34 with zero shorts/crossings but 28 track-width violations. Rejected
under the unchanged manufacturing contract; V12 remains the best valid-width
topology baseline and production CAD is unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: tested PEDET reroute V11–V15 around the
V6 rail field. Native DRC results were 5/35, 3/36, 4/35, 4/35, and 15/35.
The class removed the original RTL_5V/PEDET short only by introducing edge,
via, or rail-field failures. Rejected all five; V6 remains the best baseline,
with Path B isolated and production CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: tested SPI test-access V1 against the
old V6 control board. Native DRC reported 12 / 35; it reintroduced the
superseded PEDET short and crossed SPI/control corridors. Rejected as a
negative-control route implementation; no production copper changed.
2026-09-07 — PiSXMe Phase 24 Path B: tested corrected V12-based SPI
test-access V2. Native DRC reported 33 / 35 with source-pad shorts,
control-corridor crossings, mask bridges, and via-clearance failures.
Rejected as a coordinated-island route failure; production copper unchanged.
2026-09-07 — PiSXMe Phase 24 Path A: tested V14 at 0.15-mm track width.
Native DRC reported 105 / 34 with 28 track-width violations. Rejected under
the selected 0.20-mm differential-width contract; V12 remains the valid-width
baseline and production CAD is unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: added native connectivity audit for V12.
KiCad's saved pad/track/via connectivity passes PEDET, CLKREQ_N, PERST_N,
RESET_N, and U1↔U2 SPICS/SPISO/SPISI/SPICLK; removing PEDET copper makes the
negative control fail. Test pads remain open and unasserted; no synthetic
edges or production copper were added.
2026-09-07 — PiSXMe Phase 24 Path B: tested RTL_1V1 ordinary-via QFN
collector V1. Native DRC reported 9 violations / 29 unconnected items,
reducing the V12 baseline by seven opens. Rejected the first perimeter
geometry for SPICS/SPISO and CLKREQ conflicts; rail collection remains the
next implementation class and production copper is unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: tested RTL_1V1 collector V2/V3.
V2 reported 4 / 30 and collected six rail pads without via-in-pad. V3 moved
the pad-40 via but caused an RTL_1V1/USB_TXP0 short and CLKREQ crossing at
6 / 30. V2 remains the best disposable collector baseline; production CAD
unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: tested RTL_3V3 local trunk V1. It
reduced native opens 29 to 27 but introduced 17 DRC violations by crossing
and shorting SPI/control and RTL_5V geometry. Rejected as route
implementation evidence; production CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: added native RTL_5V connectivity audit
for U1.17, U1.33, and C5.1 on the V3 disposable fixture. KiCad connectivity
passed; removing the pad-17 escape caused the required negative-control
failure. No production CAD changed.
2026-09-07 — PiSXMe Phase 24 Path B: tested RTL_3V3 pad-52 escapes V1/V2.
V1 reduced opens 29 to 28 but shorted a GND via; V2 avoided that via but
shorted/crossed CLKREQ and regressed to 7 DRC violations / 30 opens. Both
rejected as route implementations; production CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: tested RSET route variants V1-V3.
V1/V2 collided with crystal support pads; V3 reached U1 through ordinary
vias/B.Cu and reduced opens to 28 but crossed RTL_1V1 and retained a control
via conflict. Rejected as route implementation evidence; production CAD
unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: tested complete crystal support V1.
It reduced native opens 29 to 25 but introduced four XTAL_IN/XTAL_OUT
crossings and an incomplete C1 ground thermal connection. Rejected as route
implementation evidence; production CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: tested layer-separated crystal support
V2. It reached the endpoints and reduced opens to 25, but U1-side XTAL
approaches crossed and interacted with RTL_1V1; C1 thermal relief remained
incomplete. Rejected as route implementation evidence; production CAD
unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: tested crystal support V3/V4. V3
reached all endpoints at 6 DRC / 25 opens but crossed RTL_1V1; V4 moved the
final leg but shorted XTAL_IN and RTL_1V1, at 7 DRC / 25 opens. Rejected as
route implementation evidence; production CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: generated the native RTL9210B QFN
escape map and tested crystal V5. The map exposes the RTL_1V1/control-field
barriers; V5's outer-perimeter XTAL_OUT route produced 18 DRC violations.
Rejected as route implementation evidence; production CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: corrected the stale RTL_5V/RTL_1V1
support audit to load the live V3 board and use native KiCad connectivity.
The audit passes three RTL_5V and eight RTL_1V1 endpoints. No production CAD
changed.
2026-09-07 — PiSXMe Phase 24 Path B: refreshed the V3 disposable baseline
with native KiCad DRC (4 violations / 29 opens) and live endpoint audits.
RTL_5V and RTL_1V1 assertions passed; the RTL_5V negative control failed as
required. Production CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: tested crystal V6/V7 with a pad-55
RTL_1V1 transition move. V7 restored part of the collector but left pad 55
disconnected from the full rail and retained a crystal transition collision,
at 8 DRC / 26 opens. Rejected; full collector relocation is required.
2026-09-07 — PiSXMe Phase 24 Path B: refreshed the native QFN escape map to
query via width with an explicit copper layer. The regenerated map is free
of the prior KiCad API warning and preserves measured via dimensions.
2026-09-07 — PiSXMe Phase 24 Path B: V11 crystal/collector native audit
passed XTAL_IN, XTAL_OUT, and eight RTL_1V1 endpoints; removing XTAL_OUT
copper passed the negative control. V11 remains disposable at 6 DRC / 25
opens and production CAD is unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: tested U2 RTL_3V3 B.Cu trunks V1.
They connected three additional endpoints and reduced opens 25 to 22, but
crossed SPI/RTL_1V1 corridors and left a 3V3 branch crossing, at 8 DRC
violations. Rejected as route implementation evidence; production CAD
unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: tested U1 RTL_3V3 pad-34 B.Cu escape
V1. It reduced opens 25 to 24 but shorted RTL_5V and crossed RTL_1V1,
producing 9 native DRC violations. Rejected as route implementation evidence;
production CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: tested U1 RTL_3V3 pad-34 escape V1.
It reduced opens 25 to 24 but shorted RTL_5V and crossed RTL_1V1, producing
9 native DRC violations. Rejected; coherent support relocation is required.
2026-09-07 — PiSXMe Phase 24 Path B: recorded the support-corridor decision
from the native QFN map and V11/V3 trials. Isolated 3V3/crystal nudges are
rejected; the next implementation class is coherent 3V3/1V1 support-branch
relocation. Production CAD and Path A unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: revalidated the disposable crystal V11
fixture with a fresh native KiCad DRC report (6 violations / 25 unconnected
items) and the saved-board connectivity audit. XTAL_IN, XTAL_OUT, and eight
RTL_1V1 endpoints passed; removal of XTAL_OUT copper failed the negative
control as required. Production CAD remains unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: tested a V6-derived SPI extension to the
22 mm relocated support branch. Native DRC reported 31 violations / 32 opens;
the endpoint count improved but source-pad and destination-corridor crossings
remain. Rejected as route implementation evidence; Path A and production CAD
unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: tested the outboard support translation
and SPI extension (U2/support +20 mm X). Placement-only DRC remained at
11/37; the routed extension produced 40/33 with corridor crossings and was
rejected as route implementation evidence. No mechanical placement failure
was found; Path A and production CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: tested a control-scrubbed outboard SPI
route variant. Native DRC reported 32 violations / 37 opens, including source
escape and lower-corridor conflicts. Rejected as route implementation
evidence; production CAD and Path A unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: attempted the first SPI reroute from the
relocated support branch. Native DRC reported 46 violations / 28 opens due to
over-tight source vias and destination pad-field crossings. Rejected as route
implementation evidence; the relocation remains valid and production CAD is
unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: reconstructed the SPI extension from the
clean V6 source escape and translated the U2 destination outboard. Native DRC
reported 29 violations / 38 opens; source geometry was recoverable, but the
destination lanes intersect inherited controls and the lower SPISI branch.
Rejected as a complete route; source-escape evidence retained and production
CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: isolated RTL_1V1 fanout from the native
V11 QFN map after removing all prior 1V1 copper. The candidate reports 26 DRC
violations / 18 opens, including rail/GND, rail/3V3, and crystal conflicts.
Rejected as ordinary-via coordinate fanout; no production CAD changed.
2026-09-07 — PiSXMe Phase 24 Path B: isolated the full RTL_1V1 QFN pad-field
fanout from neighboring copper. Native DRC is 1/37, and the saved-board audit
passes U1 pads 16/25/36/40/50/55/60/63 plus C4.1. This proves the fanout is
viable in isolation; V11 failures are integration congestion, not package
impossibility. Production CAD remains unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: staged V4 with crystal/RSET plus the
isolated audited 1V1 fanout and removed unrelated support copper. Native DRC
is 4 known GND-zone findings with no signal crossing/short; 32 opens are
unrelated fixture boundaries. V4 becomes the local support-routing baseline,
not a full Path-B pass.
2026-09-07 — PiSXMe Phase 24 Path B: added audited lateral SPI copper to the
V4 local baseline. Native DRC was 17/27; the primary new defect was the
RTL_1V1 U1.25 via/track interaction with SPICS/SPISO QFN escapes. Rejected as
combined geometry; V4 remains the local 1V1/crystal/RSET baseline.
2026-09-07 — PiSXMe Phase 24 Path B: tested far-transition SPI source escape
V1 from V4. Native DRC reports 32 violations with source-pad shorts and
0.0403-mm clearances. Rejected; V4 remains the valid local baseline.
2026-09-07 — PiSXMe Phase 24 Path B: transplanted the isolated audited 1V1
fanout into the V11 combined candidate as V12. Opens fell to 18, but native
DRC rose to 30 with CLKREQ_N, XTAL_OUT, and rail conflicts. Rejected as
integration congestion; isolated V1 remains the valid fanout geometry.
2026-09-07 — PiSXMe Phase 24 Path B: the SPI-only lateral proof passed native
saved-board connectivity for all five U1-to-U2 SPI nets; serialized removal of
all SPICS copper failed the negative control as required. Native DRC reports
5 warnings / 45 opens, with no SPI short or crossing. This validates the
clean V6 source escape and outboard destination geometry in isolation; full
support reintegration remains open.
2026-09-07 — PiSXMe Phase 24 Path B: tightened the SPI-only lateral proof by
removing duplicate source/destination segments and moving U2 35 mm outboard
to clear J1's SSD-power field. Native DRC is 5 warnings / 45 opens with no
SPI short/crossing; all five saved-board endpoint assertions and the SPICS
negative control pass. This is the current SPI geometry baseline, not a full
Path-B closure.
2026-09-08: RTL9210B V582 re-centered the lower RTL_3V3 In2 spine in the
measured gap between RSET and 1V1 transitions. Native 5V/3V3 audits and both
trace-removal negative controls pass. Native DRC falls to 10 findings with
19 opens and no shorting or crossing classes. V582 is retained as the current
Path-B rail candidate, not full support closure.
2026-09-08: RTL9210B V583 moved only the upper RTL_5V B.Cu corridor from
y=50.5 to y=49.5 to clear the RTL_3V3 via. Native 5V/3V3 audits and both
trace-removal negative controls pass; native DRC falls to 9 findings with
19 opens and no 5V shorting/crossing or clearance class. V583 is retained as
the current rail candidate, not full Path-B closure.
2026-09-08: RTL9210B V580 attempted ordinary-via returns for U1 ground pads
69, 45, and 66. Native DRC found true GND-to-USB/3V3 shorts and local QFN
clearance violations. V580 was rejected; V579 remains the retained rail
candidate.
2026-09-07 — PiSXMe Phase 24 Path B: the rail-only lateral proof passed native
DRC with 0 violations and passed saved-board endpoint assertions from U1 to
C3/C4/C5 on RTL_3V3/RTL_1V1/RTL_5V. Removing serialized RTL_3V3 copper failed
the negative control. Rail-spine geometry is validated in isolation; full
support remains open and production CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: extended RTL_3V3 from the validated
lateral spine to relocated U2 pads 3/8 with ordinary vias. Native DRC reports
0 violations / 45 opens; the saved-board audit proves U1.34/C3.1/U2.3/U2.8
connectivity. The 3V3 local sub-gate is closed; full support remains open.
2026-09-07 — PiSXMe Phase 24 Path B: transplanted the proven SPI-only copper
into the full support placement (U2 +35 mm; C3/C4/C5 +20 mm) using serialized
net-scoped blocks. The integrated saved-board SPI audit passes all five
U1-to-U2 endpoint pairs. Native DRC is 17 violations / 40 opens, with
remaining findings outside the SPI proof; rails/control/support remain open.
2026-09-07 — PiSXMe Phase 24 Path B: combined the proven lateral SPI and rail
transplants with the V6 control/crystal support. Native DRC is 19 violations /
34 opens. The native endpoint audit passes all five SPI pairs and the
RTL_3V3/RTL_1V1/RTL_5V support endpoints; remaining DRC/opens are not waived.
Production CAD and Path A unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: transplanted the proven V11 crystal
routing into the combined lateral SPI/rail support candidate. Native DRC is
19 violations / 30 opens (down from 34); the saved-board XTAL_IN/XTAL_OUT
audit passes. Remaining DRC findings remain open and unwaived.
2026-09-07 — PiSXMe Phase 24 Path B: removed fixture-only TP1--TP8 from
disposable V4/V5 candidates. V5 reports 17 violations / 26 opens after one
attached test stub is removed; combined SPI/crystal/rail endpoint audit
passes, while required crossings, rail/QFN fanout, and manufacturing findings
remain open and unwaived.
2026-09-07 — PiSXMe Phase 24 Path B: tested disposable QFN rail-fanout probe
V6. Native opens fell 26 to 20, but DRC rose to 20 with real
RTL_1V1/XTAL_OUT and RTL_1V1/USB_TXP0 shorts. Rejected as route
implementation failure; V5 remains the baseline and no production CAD changed.
2026-09-07 — PiSXMe Phase 24 Path B: tested RTL_1V1 perimeter-escape probe
V7. It produced 31 DRC violations / 21 opens, including new rail-to-rail and
board-edge shorts/violations. Rejected; V5 remains the combined baseline and
production CAD is unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: rebalanced the lateral rail spines and
U2.3/U2.8 branch to avoid SPI-layer interactions. Rail-only native DRC is
0/45; the combined candidate improves to 18/34, and the combined SPI/rail
endpoint audit still passes. Remaining support findings are not waived.
2026-09-07 — PiSXMe Phase 24 Path B: rebuilt the lateral support placement
from the clean V6 source directly. Placement-only native DRC was 8/43; the
laterally extended SPI route was 22/38 and was rejected for destination and
corridor conflicts. Source escape remains the authority; production CAD and
Path A unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: created a coherent support-branch
relocation probe translating U2/C3/C4/C5/R2/R3 by 22 mm. A serialized
net-scoped scrub removed only affected tracks/vias without unstable SWIG
collection mutation; the placement-only candidate reports native DRC 2 / 44
opens, with unrouted support expected. The earlier 115/31 result is retained
as superseded provisional-join evidence. Production CAD and Path A unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: tested local RTL_1V1 F.Cu power-zone
probe V8. Native DRC and opens remained 17/26, so the zone did not establish
QFN rail continuity and was rejected. No validation rule or production CAD
changed; V5 remains the baseline.
2026-09-07 — PiSXMe Phase 24 Path B: tested edge-normal QFN escape probe
V10. Native opens reduced to 19, but DRC rose to 26 with XTAL_OUT, CLKREQ_N,
SPISO, GND, RTL_5V, and sub-rule clearance conflicts. Rejected; V5 remains
the baseline and production CAD is unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: transplanted the separately validated
native oscillator V7 RSET route into the combined V5 candidate. The corrected
numeric-to-named-net transplant adds seven objects; native DRC improves to
16/25, and the saved-board RSET audit plus negative control pass. Full Path-B
support remains open and production CAD is unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: corrected the QFN escape-map utility to
load the current V5 combined candidate rather than superseded V3 fixture
geometry, and saved the resulting native pad/track/via receipt. Historical
map output is no longer a live routing baseline. The utility is now pointed at
the latest integrated V11 candidate, with a separate current V11 receipt.
2026-09-07 — PiSXMe Phase 24 Path B: recorded the native V11 QFN escape
authority boundary, including loaded pad sizes/coordinates, exposed-pad
geometry, the single existing 1V1 escape, and the 16/25 open findings. The
receipt rejects reuse of V6--V10 serialized rail probes and keeps production
CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: tested pad-aware RTL_1V1 escape probe
V9. Native DRC reports 32 violations / 22 opens, including new control/rail,
rail/rail, and edge-clearance conflicts. Rejected as route-implementation
failure; V5 remains the baseline and production CAD is unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: corrected the disposable QFN source
partition writer to retain native KiCad net handles before serialized-track
mutation. Native DRC of the resulting V1 candidate reports 22 violations / 33
opens, including RTL_1V1/U1.14, RTL_1V1/XTAL_OUT, and SPI corridor conflicts.
Rejected as route implementation evidence; staged V4 remains the local
rail/crystal/RSET baseline and production CAD is unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: preserved the coherent U1/support
relocation discriminator at (+18,+18) mm. Serialized local copper was
scrubbed before moving U1, crystal/RSET/decoupling support, and PEDET/CLKREQ
pull-ups; native KiCad reports 9 findings / 45 opens with no new signal
shorts or crossings. This is placement-only evidence, not a support-route
pass; production CAD and Path A remain unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: regenerated the moved RTL9210B local
XTAL_IN, XTAL_OUT, RSET, and RTL_1V1 copper from native pad coordinates.
The (+18,+8) mm candidate reports 4 findings / 32 opens and passes the saved
board endpoint audit for all four local support nets. This is a local
sub-gate baseline only; U2 links and remaining support routes remain open.
2026-09-07 — PiSXMe Phase 24 Path B: co-located C3/C4/C5 with the relocated
RTL9210B source island and regenerated the RTL_1V1 continuation. Native KiCad
reports 4 findings / 32 opens with no signal shorts/crossings, and the saved
board confirms all nine asserted U1/C4 RTL_1V1 endpoints. Other support nets
remain open; production CAD and Path A are unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: added separated relocated RTL_3V3 and
RTL_5V rails from U1 to C3/C5. Native KiCad reports 5 findings / 30 opens,
with no signal shorts/crossings; saved-board endpoint checks pass both rail
pairs. Remaining support and Path-B validation are open.
2026-09-07 — PiSXMe Phase 24 Path B: rejected the additional U1 rail-pad
ordinary-via fanout probe. It reduced opens to 28 but introduced real
RTL_3V3/RTL_5V and RTL_1V1/RTL_5V conflicts plus a B.Cu crossing. The class
is exhausted for this placement; the clean relocated rail baseline remains.
2026-09-07 — PiSXMe Phase 24 Path B: tested U2 co-location with the relocated
RTL9210B support island. Native KiCad remains at 5 findings / 30 opens with
no new signal shorts/crossings; SPI destinations are now a local row near U1.
This is placement evidence only and production CAD remains unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: isolated SPICS layer-transition probe
failed at the moved QFN source field. Native KiCad reports 11 violations / 29
opens, including SPICS/RTL_1V1 short/crossing and via-to-pad clearance faults.
The next class must solve the pad-field dogbone escape itself.
2026-09-07 — PiSXMe Phase 24 Path B: rejected the first F.Cu-only SPI route
from the co-located U1/U2 pads. Native KiCad reports 19 violations / 26 opens,
including source crossings, rail clearances, and an RTL_1V1/SPICS short. U2
co-location remains placement evidence; the next SPI class must change layer
and escape ordering.
2026-09-07 — PiSXMe Phase 24 Path B: rejected the rotated-U1 five-net SPI
escape. Native KiCad reports 38 violations / 39 opens, including overlapping
source vias and crossings of retained XTAL/RSET corridors. The rotation is
retained only as disposable placement evidence; production CAD is unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: rejected a fully scrubbed rotated-U1
staggered-via SPI escape at 24 violations / 40 opens. The test also exposed
a malformed disposable U2 flash footprint coordinate frame; a corrected
local-coordinate candidate was created and rejected at 53 violations / 39
opens due to the test placement/SPI permutation. Path A, production CAD, and
the Path-B electrical architecture remain unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: the five-net QFN dogbone follow-up with
straight outward departures improved to 17 native violations / 44 opens but
still failed at SPICLK/SPISO3 transition spacing and one source clearance.
The failure is localized to transition layout; the single-net dogbone remains
validated evidence and production CAD/Path A are unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: rejected the corrected-U2 SPISO3
one-net handoff V2 at 16 native violations / 43 opens. The north-side F.Cu
route still conflicted with neighboring SPISI/source-field and XTAL geometry,
confirming that all five SPI exits and the flash launch must be authored
together. Path A and production CAD remain unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: focused QFN SPISI dogbone probe passed
the source geometry with no signal short, crossing, or clearance violation;
native KiCad reports only 5 incomplete-probe/inherited-GND findings and 44
opens. The probe establishes a viable 45-degree departure to an ordinary via
outside the pad field. Five-net SPI and regenerated neighboring support
remain open; Path A and production CAD are unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: V3 source-transition spacing trial
retained one SPISO-to-SPISO3 clearance violation at 0.100 mm actual versus
0.200 mm required, with no shorts or crossings. The next class must change
the post-pad fanout shape; Path A and production CAD remain unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: rejected the V2 QFN transition-spacing
micro-variant at 10 native violations / 44 opens; one SPISO/SPISO3 clearance
remains and the result does not improve V1. Both receipts are preserved and
production CAD/Path A remain unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: V4 lateral-transition source probe is
the first five-net QFN escape with no signal shorts, crossings, or clearance
violations. Native KiCad reports 9 findings / 44 opens, limited to
incomplete-probe/inherited GND conditions. Extension to corrected U2 and
regenerated support remains open; Path A and production CAD are unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: rejected the complete corrected-U2
two-layer SPI partition at 12 native violations / 39 opens. SPISO/SPICS
crossed at the F.Cu handoff and SPICLK/SPISO3 conflicted with retained B.Cu
source tails. The corrected U2 pad map is valid; the next trial must
regenerate the complete five-net branch together.
2026-09-07 — PiSXMe Phase 24 Path B: rejected fully regenerated SPI branch
V3 at 8 native violations / 40 opens. Removing lower B.Cu tails caused the
SPICS F.Cu corridor to cross source dogbones while SPICLK/SPISO3 still
interacted on B.Cu. A new layer/channel topology is required; Path A and
production CAD remain unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: channelized full SPI V1 passes the
local native signal gate with no SPI shorts, crossings, or clearance
violations; native endpoint audit passes all five U1/U2 pairs and its SPISI
negative control fails as required. One inherited isolated-GND warning and
40 unrelated support opens remain, so full Path-B closure is still open.
2026-09-07 — PiSXMe Phase 24 Path B: rejected normalized rotated-support
V3 at 14 native violations / 37 opens; XTAL_IN/RSET connected but XTAL_OUT
disconnected, with transitions entering the U1 power field. V2 remains the
better support-placement reference; Path A and production CAD unchanged.
2026-09-07 — PiSXMe Phase 24 Path B: rotated-support V8 moves the XTAL_OUT
transition beyond the U1 QFN pad envelope. Native KiCad reports no signal
shorts, crossings, or clearance violations; saved-board audits pass XTAL_IN,
XTAL_OUT, and RSET. Two inherited findings and 35 unrelated fixture opens
remain, so V8 is a local support-route baseline, not full Path-B closure.
The same saved board passes the native five-net SPI endpoint audit and its
SPISI trace-removal negative control. Remaining work is control/sideband,
rail/ground completion, USB, M.2, power, and full Path-B validation.
RTL_5V rail probe V9 then connected U1.17/U1.33/C5.1 with no new signal DRC
violation; native saved-board connectivity passed all three endpoints. The
probe reduced unrelated fixture opens from 35 to 33 and remains a local rail
primitive, not full Path-B closure.
RTL_3V3 probes V10/V11 were rejected: V10 collided with SPICLK/XTAL_IN and
V11 crossed SPICS and Y1 XTAL_IN, reaching 12 native signal violations / 31
opens. The next 3V3 attempt must use a different corridor topology.
Current authoritative Path-B baseline is V8 support/SPI plus V9 RTL_5V;
V10/V11 RTL_3V3 are rejected, and the next class must reauthor the local
3V3/support corridor coherently. Path A and production acreage remain intact.
RTL_3V3 V12 was then rejected at 9 native violations / 31 opens: U1.20
crossed SPISI/SPICLK and U1.52 reached XTAL_IN/Y1. The next class must
co-author the QFN source escape with the retained SPI routing.
Integrated source-escape V13 was rejected at 10 native violations / 31 opens;
SPICLK crossed SPISI and RTL_3V3 collided with SPICLK/XTAL_IN. The next route
class must regenerate SPISI/SPICLK/SPISO3/RTL_3V3 together.
Complete four-net QFN field V14 was rejected at 24 native violations / 31
opens: source departures crossed the U1 pad field, B.Cu channels crossed,
and RTL_3V3 collided with XTAL_IN. The next class must change U1/local
support placement or orientation.
Added a reusable saved-board V8 support audit; XTAL_IN/XTAL_OUT/RSET pass and
the XTAL_OUT trace-removal negative control fails as required.
The 90-degree U1 four-net V16 source-field probe was rejected at 7 native
violations / 41 opens because the B.Cu channels crossed at the U2 handoff.
The orientation remains a placement alternative; downstream drops must be
staggered outside the horizontal channel envelope.
The transformed-pad-aware V22 diagonal probe was rejected at 9 native
violations / 41 opens: RTL_3V3 collided with SPISO3/SPICS and crossed SPICLK.
V20 remains the best 90-degree baseline; a formal escape-cell construction
is still required.
Added a native transformed-pad escape-cell map utility and V15 receipt; it
records U1 pad centers, dimensions, orientations, and outward vectors for the
next formal source-escape generator.
Formal native-pad source field V24 is a local PASS: native KiCad reports no
signal shorts, crossings, or clearance violations, positive saved-board
connectivity passes SPISI/SPICLK/SPISO3/RTL_3V3, and the SPISI trace-removal
negative control fails as required. Remaining RTL9210B support is open.
V25 added SPISO/SPICS but was rejected at 4 native violations / 39 opens for
SPISO/SPISO3 crossing and a SPICS source transition conflict. V24 remains
the valid four-net baseline; the remaining channels need a layer swap.
The 90-degree V18-V21 trials remain disposable evidence. V20 reduced the
source-field result to 3 findings / 41 opens; V21 rejected down/right RTL_3V3
because it entered adjacent U1 RTL_5V/RTL_1V1 pads and crossed SPICLK. A
transformed-pad-aware escape cell is required next.
Mixed-layer 90-degree source field V17 improved to 5 native findings / 41
opens but was rejected for SPISI/SPICLK transition proximity and reversed B.Cu
handoff crossing. One reversed-order channel must move to an independent
F.Cu corridor in the next attempt.
2026-09-07: Phase 24 RTL9210B source-field allocator V26-V30 experiments were preserved and rejected for native signal crossings/shorts. V31 is the best complete five-net SPI primitive: native DRC has no SPI signal violations, saved-board positive connectivity passes all five SPI nets, and the trace-removal negative control fails. V32 support append is rejected for XTAL/RSET crossings and shorts; Path A, production CAD, and the accepted architecture remain unchanged.
2026-09-07: Rejected RTL9210B support allocator V33 at 15 native violations / 35 opens after B.Cu XTAL/RSET handoffs entered the passive field and crossed. V31 five-net SPI remains the best local primitive; next work must relocate or coherently reauthor the support island, with Path A and production CAD unchanged.
2026-09-07: V35 moved the RTL9210B XTAL/RSET support cluster coherently inside the fixture. Native DRC has 4 inherited GND/silkscreen findings and no signal violations; saved-board SPI and XTAL_IN/XTAL_OUT/RSET audits pass with negative controls. Remaining RTL9210B rails, controls, USB, M.2, power, and full Path-B validation remain open; production CAD and Path A are unchanged.
2026-09-07: Rejected RTL9210B local rail-zone probe V36 because broad F.Cu zones left rail pad joins open in saved-board connectivity and did not provide complete native pad/via access. V35 remains the validated SPI/support baseline; production CAD and Path A are unchanged.
2026-09-07: Rejected RTL9210B explicit rail via/field probe V37 at 41 native violations / 34 opens after rail fanout collided with the QFN SPI/source field and neighboring rail pads. The next rail implementation must partition escapes or move decoupling coherently; production CAD and Path A remain unchanged.
2026-09-07: V38 normalized disposable C3/C4/C5 to ordinary C_0603 local-coordinate footprints. V39 RTL_5V routing against corrected C5 was rejected at 7 native findings / 32 opens for crossings with retained RTL_3V3/SPI corridors; next work must co-author the 3V3/5V rail fields, with production CAD and Path A unchanged.
2026-09-07: Rejected RTL9210B joint rail allocator V40 at 8 native violations / 32 opens after RTL_3V3 collided with SPISO3 and RTL_5V retained SPISI/C5 handoffs. The next rail implementation must preserve V24's validated 3V3 departure and partition added access; production CAD and Path A remain unchanged.
2026-09-07: Rejected RTL9210B RTL_3V3 local fanout V41 at 7 native violations / 30 opens for one U1 pad-field clearance, one XTAL_IN-adjacent via, and an RSET-via conflict on the U2 branch. SPI and XTAL/RSET copper were preserved; next work partitions source and downstream 3V3 branches.
2026-09-07: Rejected RTL9210B partitioned 3V3 fanout V42 at 6 native findings / 31 opens; the U1 pad-field defect was removed, leaving one RSET-adjacent dangling/clearance transition. The partition is retained for the next rail-pad join pass.
2026-09-07: V44 removed the redundant 3V3 via and has only inherited GND/silkscreen DRC findings, but U1.52 remains separate from the partial U1.34/U1.39/U2 branch. V45's U1.52 handoff was rejected at 10 findings / 30 opens for XTAL_IN-via clearance violations; next work must relocate or co-author that source field.
2026-09-07: Rejected RTL9210B co-authored XTAL_IN/U1.52 handoff V46 at 9 native violations / 30 opens; transitions collide at the 0.4-mm QFN source pitch. V44 remains the cleanest partial 3V3 result, and the next class is coherent local support rotation/relocation.
2026-09-07: V47 corrected the disposable RTL9210B U1 footprint frame by normalizing its malformed anchor while preserving absolute pad coordinates. Reload inspection confirms the U1 source pad field is stable; native DRC returns to 4 inherited GND/silkscreen findings / 31 opens with no new signal violations. V47 is the current Path-B authoring basis, not full support closure; production CAD and Path A remain unchanged.
2026-09-07: V49 co-authored the corrected RTL9210B U1.52 RTL_3V3 escape around XTAL_IN and returned native DRC to 4 inherited warnings / 30 opens; saved-board connectivity joins U1.52 to the U1.34/U1.39/U2 branch. Rejected V50's straight R2/R3-to-U1.20/C3 collector at 7 findings / 28 opens for crossings with retained SPISO/SPICS/SPISO3. V49 remains the disposable basis; production CAD and Path A remain unchanged.
2026-09-07: Rejected RTL9210B rail collector V51 at 15 native findings / 28 opens: R2/R3 pad escapes entered opposite-net pads and the proposed B.Cu collector conflicted with SPISO3. V49 remains the cleanest handoff basis; next work must derive resistor pad orientation from native pads and allocate a separate SPI-clear collector corridor.
2026-09-07: Promoted RTL9210B disposable rail-join V52 after normalizing R2/R3 frames and deriving verified pad-2 escapes. Native DRC is 5 non-signal isolated-copper/silkscreen warnings / 28 intended opens; saved-board connectivity joins all RTL_3V3 pads across U1, U2, R2, R3, and C3. Remaining Path-B rails, controls, ground, USB, M.2, and full validation remain open.
2026-09-07: Promoted RTL9210B disposable RTL_5V escape V57. Native pad-derived routing joins U1.17/U1.33/C5.1 with 5 non-signal isolated-copper/silkscreen warnings / 26 intended opens and no signal DRC violations. V53-V56 are preserved as rejected routing evidence; RTL_1V1, controls, ground, USB, M.2, and full Path-B validation remain open.
2026-09-07: Promoted RTL9210B RTL_1V1 U1.16-to-C4.1 sub-primitive V59 after rejecting V58's C3-adjacent launch. Native DRC is 5 non-signal isolated-copper/silkscreen warnings / 27 intended opens with no new signal violations; remaining RTL_1V1 pad groups and all later Path-B gates remain open.
2026-09-07: Rejected RTL9210B full RTL_1V1 perimeter candidate V60 at 35 native findings / 20 opens after crossings with XTAL_IN/XTAL_OUT/RSET/SPI and a 3V3 left-edge clearance defect. V59 remains the only promoted 1V1 sub-primitive; remaining edge groups require separate corridors.
2026-09-07: Promoted RTL9210B RTL_1V1 U1.25-to-C4.1 sub-primitive V63. Native DRC is 5 non-signal isolated-copper/silkscreen warnings / 26 intended opens with no new signal violations; V60-V62 remain rejected routing evidence and the remaining 1V1 groups are open.
2026-09-07: Rejected RTL9210B RTL_1V1 U1.60 bottom-edge candidate V64 at 8 native findings / 26 opens after its B.Cu drop entered the retained XTAL_OUT y=77 segment. V63 remains the promoted 1V1 basis; remaining bottom/left groups must route around the native XTAL_OUT endpoint.
2026-09-07: Rejected RTL9210B RTL_1V1 U1.55 bottom-edge candidate V65 at 15 native findings / 26 opens after its rightward escape clipped no-net U1.56 and its via conflicted with XTAL_OUT. U1.55 remains open; V59/V63 remain the promoted 1V1 sub-primitives.
2026-09-07: Rejected RTL9210B RTL_1V1 U1.60 candidate V68 at 7 native findings / 26 opens after its F.Cu leg intersected the retained XTAL_IN launch. The C4-side B.Cu join was clear; U1.60 now requires coherent XTAL/support-field relocation or another source-side layer strategy.
2026-09-07: V69 diagnostic removed only the obstructing XTAL_IN route and showed the U1.60 RTL_1V1 corridor has no signal DRC violations; 6 findings / 28 opens are diagnostic/inherited. This confirms local XTAL/support placement collision rather than impossible U1.60 routing. V69 is not promoted.
2026-09-07: Promoted RTL9210B RTL_1V1 U1.50 edge-group V75. Native DRC is 6 non-signal warnings / 25 intended opens; saved-board connectivity joins U1.50 with U1.16/U1.25/C4.1. V74's RTL_3V3 crossing remains rejected; remaining 1V1 groups are open.
2026-09-07: Rejected RTL9210B coherent XTAL/support relocation V70 at 18 native findings / 27 opens for board-edge and regenerated XTAL_IN/XTAL_OUT/RSET local collisions. V69 remains the diagnostic proof that U1.60 routing is feasible when the source field is cleared; production CAD and Path A remain unchanged.
2026-09-07: Rejected RTL9210B upper-right XTAL/RSET relocation V72 at 51 native findings / 30 opens after guessed transformed support-pad coordinates caused local XTAL/rail/SPI collisions. Placement margin was clear; next relocation must derive post-transform native pad coordinates before authoring routes.
2026-09-07: Rejected RTL9210B corrected-endpoint relocation V73 at 32 native findings / 28 opens; long RSET and U1-side XTAL_IN corridors still crossed retained SPI/3V3 fields. The transformed endpoint authoring defect is fixed; next work must use shorter local support corridors.
2026-09-07: Rejected RTL9210B U1.40 RTL_1V1 trials V76/V77/V78. V76 shorted the left RTL_3V3 escape at 9 violations / 24 opens; V77 moved farther left but crossed the retained RTL_3V3 diagonal at 8 / 24; V78 upper-perimeter routing crossed RTL_3V3/SPICLK and adjacent U1 pads at 14 / 24. These are preserved route-allocation evidence; V75 remains the promoted partial 1V1 basis and U1.40 remains open.
2026-09-07: Rejected RTL9210B U1.40 RTL_1V1 trials V76/V77/V78. V76 shorted the left RTL_3V3 escape at 9 violations / 24 opens; V77 moved farther left but crossed the retained RTL_3V3 diagonal at 8 / 24; V78 upper-perimeter routing crossed RTL_3V3/SPICLK and adjacent U1 pads at 14 / 24. These are preserved route-allocation evidence; V75 remains the promoted partial 1V1 basis and U1.40 remains open.
2026-09-07: Rejected RTL9210B U1.40/RTL_3V3 reallocation trials V79/V80. V79 removed the former U1.40/3V3 short but left a U1.40-to-pad41 clearance defect and a 3V3/no-net-pad clearance defect at 8 / 25; V80 introduced a dangling 3V3 endpoint while retaining the pad-field defect at 8 / 25. The next route must co-author a complete 3V3 replacement and pad-aware U1.40 dogbone.
2026-09-07: Rejected RTL9210B U1.40 fine-width escape V81. Native DRC reports 10 / 25 with 0.1647-mm clearance to U1.41, 0.100-mm 3V3 clearance to U1.35, and two violations of the 0.200-mm minimum width. Fine trace width is not an acceptable workaround; keep the board rule and reallocate the pad-field corridor.
2026-09-07: Rejected RTL9210B U1.40 diagonal escape V82. Native DRC reports 11 / 25; the diagonal shorts/crosses the adjacent U1.39 RTL_3V3 escape and violates the U1.38 solder-mask/clearance envelope. The next attempt must co-author the shared QFN escape cell.
2026-09-07: V83 diagnostic-only RTL9210B QFN pad-width sensitivity trial shrank the 68 perimeter pads in V79 without changing copper, rules, or nets. Native DRC remained 8 / 25 with the same U1.40/U1.41 and RTL_3V3/U1.35 clearance defects; no land-pattern or rule change is promoted.
2026-09-07: Rejected RTL9210B U1.55/U1.60 bottom-edge trials V88–V94 for XTAL_OUT/XTAL_IN, QFN-pad, and corridor allocation defects. Promoted V95 U1.60 edge-group sub-primitive: native DRC is 8 inherited warnings / 24 opens and native connectivity joins U1.60 with U1.16/U1.25/U1.40/U1.50/C4.1.
2026-09-07: Promoted RTL9210B U1.63 shared F.Cu launch V96. Native DRC remains 8 inherited warnings / 23 opens; native connectivity joins U1.63 with U1.16/U1.25/U1.40/U1.50/U1.60/C4.1. U1.36/U1.55 and remaining Path-B gates stay open.
2026-09-07: Rejected RTL9210B QFN escape V84/V85 authoring variants: V84 duplicated the U1.40 via, and V85 removed the retained 3V3 via while replacing local tracks. Promoted V86 as the corrected U1.40/3V3 sub-primitive using the validated disposable JLC basis (0.13208-mm minimum track / 0.15-mm clearance); native DRC is 6 inherited warnings and connectivity joins U1.40/U1.16/U1.25/U1.50/C4.1.
2026-09-07: Promoted RTL9210B U1.55/XTAL_OUT left-endpoint escape V100 after rejecting V97/V98/V99 crossing variants. Native saved-board connectivity joins U1.55 into the existing RTL_1V1 group; signal-specific centerline review finds no new different-net crossing. Disposable DRC/unconnected and inherited manufacturing findings remain open; Path B and production CAD remain unchanged.
2026-09-07: Rejected RTL9210B U1.36 left escape V101 for a native RTL_1V1/RTL_3V3 short and crossing. Promoted V102 right escape: native DRC has no shorting-items or tracks-crossing, and saved connectivity joins U1.36 into the complete currently assembled 1V1 group. Remaining Path-B support and validation gates stay open.
2026-09-07: Rejected RTL9210B U1.34 RTL_3V3 handoff V103 for an incomplete layer endpoint and V104 for two native track crossings. V104 did prove native connectivity to the existing 3V3 via and R2/R3/C3/U1.20 group. Promoted support basis remains V102; U1.34 and remaining Path-B gates stay open.
2026-09-07: Rejected RTL9210B U1.34 V105 for crossings through SPICLK/SPISI. Promoted V106 F.Cu-first escape: native DRC has no shorting-items or tracks-crossing, and saved connectivity joins U1.34 to the existing C3/R2/R3/U1.20 RTL_3V3 group. Full Path-B support remains open.
2026-09-07: Rejected RTL9210B control-sideband trials V107-V111 for adjacent control-via shorts and crossings with the retained RTL_1V1/RTL_3V3 fields or companion control route. This is route allocation evidence, not an RTL9210B topology rejection; next work uses genuinely layer-separated launches.
2026-09-07: Rejected RTL9210B control trial V112: layer separation removed control-control shorts, but three crossings remained against inherited RTL_1V1/RTL_3V3/upper-rail fields. No architecture or layer-policy change follows.
2026-09-07: Rejected RTL9210B control V113/V114 for inherited RTL_3V3 crossing and CLKREQ/PERST clearance contact. Promoted V115 after native connectivity joined U1.13→J1.52 and U1.14→J1.50 with no shorting-items or tracks-crossing; PEDET and remaining Path-B endpoints remain open.
2026-09-07: Promoted RTL9210B PEDET U1-to-M.2 launch V116: native connectivity joins U1.8 to J1.69 with no shorting-items or tracks-crossing. R2 source connection and remaining Path-B endpoints remain open.
2026-09-07: Rejected PEDET R2 routing V117-V121 for SPI/1V1/XTAL_IN crossings and local clearance defects. Promoted V122: native audit connects R2.1/U1.8/J1.69 and its trace-removal negative control fails as required. Remaining Path-B gates stay open.
2026-09-07: Rejected CLKREQ R3 trials V123-V130 for SPI/PEDET/1V1/C5/upper-rail crossings. Promoted V131 after native audit connected R3.1/U1.13/J1.52 with no shorting-items or tracks-crossing; the route-removal negative control failed as required. Remaining Path-B gates stay open.
2026-09-07: Rejected RTL9210B RTL_5V route trials V132-V136 for retained-field shorts/crossings or ground/CLKREQ contact. Promoted V137 after routing the C5.1 branch below the local control field: native connectivity joins C5.1/U1.17/U1.33, the negative control fails as required, and no shorting_items/tracks_crossing are present. V137 is only a disposable RTL_5V sub-primitive; remaining Path-B support and full validation stay open.
2026-09-07: Rejected U1.34 RTL_3V3-on-V137 trials V138/V139. Both joined U1.34 to C3/R2/R3/U1.20, but V138 shorted the promoted RTL_5V source field and V139 crossed SPISO3. U1.34 remains open; V137 RTL_5V remains promoted.
2026-09-07: Rejected U1.34 RTL_3V3 V140 after moving the source left and raising the B.Cu corridor; native DRC still reported three SPISO shorts and one crossing. U1.34 requires a new QFN source-field allocation; V137 RTL_5V remains promoted.
2026-09-07: Reconciled Phase 24 narrative authority after V137: current disposable RTL9210B rail/control basis is V137 with V131/V122 support sub-primitives; V100/V102 wording is historical evidence, not the current basis. Path A and production CAD remain unchanged.
2026-09-07: Promoted RTL9210B V141 M.2 SSD_3V3 contact-row sub-primitive: native connectivity joins J1.2/J1.4/J1.6/J1.8, no signal short/crossing classes are present, and the trace-removal negative control fails as required. The SSD_3V3 source and complete power gate remain open.
2026-09-07: Rejected RTL9210B U1.34 V142 for SPICS contact. Promoted V143 after moving the departure outside the V137 RTL_5V source field: native connectivity joins U1.34/C3/R2/R3/U1.20, no shorting_items/tracks_crossing are present, and the negative control fails as required. V143 is only a disposable U1.34 sub-primitive; remaining Path-B gates stay open.
2026-09-07: Promoted RTL9210B V144 combined support basis by carrying V141's J1.2/J1.4/J1.6/J1.8 SSD_3V3 contact join onto V143. Native audits pass both rail joins and negative controls; six high-speed endpoint opens and the SSD_3V3 source/power gate remain open.
2026-09-07: Rejected RTL9210B REFCLK lower-corridor trial V145 for inherited XTAL/1V1/CLKREQ and J1 sideband contacts/crossings. V144 remains the promoted basis; REFCLK route allocation remains open.
2026-09-07: Rejected RTL9210B REFCLK trials V146/V147: V146 entered the J1 TX pad field and V147 still crossed the U1 exposed GND pad. REFCLK remains authoritative but needs local QFN lower-edge/RTL_1V1 source-field reallocation.
2026-09-07: Rejected RTL9210B local RTL_1V1 relocation trials V148/V149: V148 crossed XTAL_IN and V149 still contacted XTAL_IN/C1 ground. The next support repair must co-author XTAL_IN and the lower 1V1 field.
2026-09-07: Rejected RTL9210B REFCLK split-escape V155: REFCLK_N contacted U1 pad 65/outboard 1V1 and REFCLK_P contacted XTAL_IN. V154 remains the validated local-support basis; REFCLK needs coordinated endpoint/sideband allocation.
2026-09-07: Promoted RTL9210B V156 CLKREQ_N J1 outboard launch with no signal short/crossing classes. Rejected V157 XTAL_IN endpoint move for crossing the retained XTAL_OUT span; the next crystal-support repair must co-author XTAL_IN/XTAL_OUT.
2026-09-07: Promoted RTL9210B V158 XTAL_IN inner transition with complete crystal connectivity/negative control and no signal short/crossing classes. V160 preserves complete 1V1 connectivity through a direct B.Cu rail join. Rejected V162 REFCLK attempt for XTAL_OUT/legacy 1V1 contacts; REFCLK remains open.
2026-09-07: Rejected RTL9210B V150 for a missing 1V1 handoff and V152/V153 for XTAL_IN/1V1 REFCLK contacts. Promoted V154 after moving only the 1V1 handoff outboard: complete native 1V1 connectivity and negative control pass with no signal short/crossing classes. REFCLK remains open.
2026-09-07: Rejected RTL9210B REFCLK allocation trials V163-V166. V163 exposed-pad/CLKREQ conflicts; V164 retained inherited corridor crossings; V165 exposed the U1 pad-field conflict; V166 exposed GND/XTAL_OUT/J1-launch conflicts. Preserved all four as route evidence; V158/V160 remain the support basis and Path A/production CAD remain untouched.
2026-09-07: Rejected RTL9210B REFCLK trials V167-V172. V169 is the best disposable topology and passes native REFCLK mapping plus trace-removal negative control, but its physical crossings remain open. Preserved the full evidence set; no Path-A or production CAD changed.
2026-09-07: Promoted RTL9210B V174 as a disposable translated REFCLK placement/topology sub-primitive: coherent local support moved upward, stale local copper scrubbed, native DRC has zero signal shorts/crossings, and saved connectivity plus negative control pass. Remaining Path-B support and production integration stay open.
2026-09-07: Rejected RTL9210B V175 after restoring translated V158 crystal copper onto V174: REFCLK-P/XTAL_IN and REFCLK-N/XTAL_OUT local co-allocation defects remain. V174 stays promoted only for REFCLK placement/topology; full Path-B support is open.
2026-09-07: Rejected RTL9210B V176-V178 as translated crystal/REFCLK authoring trials. V179 moves Y1/C1/C2/R1 west and removes the board-wide REFCLK/XTAL conflict, leaving four localized QFN/crystal/RSET source defects. Preserved V179 as the best disposable placement basis; production CAD remains untouched.
2026-09-07: Promoted RTL9210B V184 as a disposable crystal/RSET/REFCLK support sub-primitive after rejecting V180-V183 localized route conflicts. V184 has zero native shorting_items/tracks_crossing, and the saved-board audit passes XTAL_IN, XTAL_OUT, RSET, REFCLK_P, and REFCLK_N with five trace-removal negative controls. Native DRC still reports 243 inherited/disposable findings and 32 opens; Path-B and production integration remain open.
2026-09-07: Promoted RTL9210B V185 as a disposable U1.34-to-C3.1 RTL_3V3 rail sub-primitive. Native DRC reports zero shorting_items/tracks_crossing; saved native connectivity and the trace-removal negative control pass. Native DRC remains 254 inherited/disposable findings and 31 opens; remaining Path-B support and production integration stay open.
2026-09-07: Promoted RTL9210B V186 as a disposable shared RTL_3V3 rail extension from U1.20 into the V185 trunk. Native DRC reports zero shorting_items/tracks_crossing; saved native connectivity and the trace-removal negative control pass. Native DRC remains 259 inherited/disposable findings and 30 opens; west-field 3V3 launches and remaining Path-B support stay open.
2026-09-07: Promoted RTL9210B V187 as a disposable U1.33-to-C5.1 RTL_5V rail sub-primitive. Native DRC reports zero shorting_items/tracks_crossing; saved native connectivity and the trace-removal negative control pass. Native DRC remains 270 inherited/disposable findings and 29 opens; remaining Path-B rails, SPI/control, and production integration stay open.
2026-09-07: Promoted RTL9210B V188 as a disposable U1.16-to-C4.1 RTL_1V1 rail sub-primitive. Native DRC reports zero shorting_items/tracks_crossing; saved native connectivity and the trace-removal negative control pass. Native DRC remains 282 inherited/disposable findings and 28 opens; remaining Path-B rails, SPI/control, and production integration stay open.
2026-09-07: Promoted RTL9210B V189 as a disposable U1.24-to-U2.1 SPICS sub-primitive. Native DRC reports zero shorting_items/tracks_crossing; saved native connectivity and the trace-removal negative control pass. Native DRC remains 293 inherited/disposable findings and 27 opens; remaining Path-B SPI/control and production integration stay open.
2026-09-07: Rejected RTL9210B SPISO V190-V192 for source-field, corridor, and RSET-pad conflicts. Promoted V193 after the destination dogleg moved above the RSET pad band; native DRC has zero shorting_items/tracks_crossing and saved connectivity plus negative control pass. V193 remains disposable evidence; other SPI/control and Path-B gates stay open.
2026-09-07: Rejected RTL9210B SPICLK V194-V196. V194 hit adjacent SPISI/XTAL_IN, V195 introduced XTAL_IN/XTAL_OUT/U1.52 conflicts, and V196 hit C2 ground/XTAL_OUT. These establish a coupled crystal/SPI local allocation issue; next work must co-author that field. Path A and production CAD remain unchanged.
2026-09-07: Rejected RTL9210B V197 coherent west crystal/RSET shift: saved connectivity passed, but native DRC found XTAL_OUT/SPICS crossing and SPISO/C2-ground contact. The west-shift class is rejected; the next attempt must co-author the complete SPI/crystal destination field. Path A and production CAD remain unchanged.
2026-09-07: Rejected RTL9210B V198/V199 for Y1.1 contact and RSET/XTAL_OUT crossing. Promoted V200 after the east crystal translation and y=67.5 RSET handoff produced zero native shorting_items/tracks_crossing plus four negative-control passes. V200 remains disposable support evidence; remaining SPI/control and Path-B gates stay open.
2026-09-07: Rejected RTL9210B SPISI V201: native connectivity passed, but DRC found C1 ground contact and SPISI/SPICLK source-field conflict. The next attempt must co-author the coupled SPI source/destination field; Path A and production CAD remain unchanged.
2026-09-07: Promoted RTL9210B V208 as the disposable coordinated SPI/crystal
source-field basis. V202-V207 were preserved as evidence: source-field and
crystal placement variants either contacted support copper or exposed an
audit authoring omission. V208 adds the explicit XTAL_IN-to-Y1.1 branch,
passes native RTL_3V3/SPICLK/SPISI/XTAL_IN connectivity with four negative
controls, and reports zero native signal shorting/crossing classes. Path A,
production CAD, and the accepted macro-floorplan remain unchanged; remaining
Path-B support, mode validation, and integration gates stay open.
2026-09-07: Rejected RTL9210B SPISO3 V209/V210 source departures for retained
RTL_1V1/SPISO source-field crossing/shorting. Promoted V211 after a diagonal
source dogbone, ordinary-via B.Cu handoff, and outboard F.Cu corridor
produced native SPISO3 connectivity plus a passing trace-removal negative
control and zero native signal shorting/crossing classes. Path A and
production CAD remain unchanged; Path-B support and full validation remain
open.
2026-09-09 — V1278 accepted RTL9210B RSET support: U1.51 reaches R1.1 from
the open resistor side and R1.2 receives a deliberate local GND return.
Native DRC retained inherited warnings only; endpoint and negative-control
audit passed. Crystal, SPI, remaining rails/controls, and Path-B closure are
open.

2026-09-09: V746/V747 were rejected three-channel source-field allocations
with native SPISO/SPISO3 and SPICS/SPISO interactions. V748 rotated U2 90
degrees into a vertical SPI endpoint field and passed native KiCad DRC with
zero violations and 45 incomplete opens. V749 routed SPISO3 on that basis
with zero DRC violations; V750 added SPICLK through a separate B.Cu channel
and also passed with zero DRC violations. These are isolated Path-B routing
experiments; Path A and production CAD remain unchanged, and full SPI plus
RTL9210B qualification remain open.

2026-09-09: V752 tested a five-net endpoint-free QFN fan-out. Native DRC
found two real 0.1505 mm clearances between SPICLK and SPISI against the
0.20 mm rule; transition-only via-dangling warnings were expected. Reject
V752 as a complete fan-out and co-author that adjacent source pair next.

2026-09-09: V751 attempted to add SPICS and SPISO to the V749/V750 vertical
U2 endpoint basis. Native KiCad DRC found five source-field/return-shelf
violations, so V751 was rejected as a route implementation. V749 and V750
remain clean single/two-channel proofs; the next Path-B experiment must
co-author the QFN source escapes instead of extending the left-side trunk.
2026-09-07: Promoted RTL9210B V212 PEDET U1.8-to-M.2 contact-69 sideband
slice. Native connectivity and the trace-removal negative control pass, and
native DRC has zero signal shorting/crossing classes. Path A and production
CAD remain unchanged; reset/CLKREQ, remaining support, mode, firmware, and
full Path-B validation remain open.
2026-09-07: Rejected RTL9210B PEDET support V213/V214 for retained-corridor
crossings. Promoted V215 after routing R2.1 around the outboard ends of the
REFCLK/RTL_5V B.Cu spans. U1.8/R2.1/J1.69 native connectivity and the
trace-removal negative control pass with zero signal shorting/crossing
classes. Path A and production CAD remain unchanged.
2026-09-07: Recorded RTL9210B sideband experiments V216-V225. V220 is a
clean partial U1.13-to-J1.52 CLKREQ slice with native negative-control PASS,
but R3.1 remains open. V221's R3 return crossed PEDET/XTAL. PERST V222-V225
were rejected for source-field crossings/shorts despite endpoint audit PASS;
V225 localizes the remaining defect to the U1.14/RTL_1V1 field. No Path-A or
production-CAD change was made.
2026-09-07: Rejected RTL9210B PERST V226 after native DRC localized the
remaining source defect to a REFCLK_P/PERST_N via/track short and crossing.
Endpoint connectivity and negative control still pass. PERST requires a
coupled QFN/REFCLK source-field allocation; no Path-A or production-CAD
change occurred.
2026-09-07: Promoted RTL9210B V227 as the disposable coupled QFN source-field
basis. Co-authored SPISO3 and PERST, replacing their conflicting local
departures; both native endpoint audits and two trace-removal negative
controls pass, with zero native signal shorting/crossing classes. Path A and
production CAD remain unchanged; CLKREQ/R3.1 and all remaining Path-B gates
stay open.

2026-09-08 — A local USB_TXP1 escape at the active 0.20 mm width passed
native USB3 connectivity with no new shorts, but added support-field
crossings and was rejected. Width cleanup must co-author both USB TX nets
with the adjacent JMS_AVDDL field.

2026-09-08 — Coordinated selector plus USB3 regeneration was rejected:
native endpoint connectivity passed, but DRC reported four true shorts,
including STORAGE_SEL against SATA and inherited USB3 source-field crossings.
No copper was promoted; the next class is clean source-owned corridor
regeneration.

2026-09-08 — Selective widening of storage high-speed tracks removed 34 width
findings but left 147 inherited findings and introduced a real JMS_AVDDL/
USB_TXP1 short. It was rejected; width cleanup must be co-authored with local
support-field routing.

2026-09-08 — An unchanged VBUS-basis round trip stayed zero-short, ruling out
a generic save failure. The selector V2 probe, which avoided rebuilding the
net table, still exposed three inherited crossing shorts after adding the
new corridor. Both selector probes are rejected; neighboring high-speed
copper must be regenerated together.

2026-09-08 — A coherent STORAGE_SEL reroute passed the native 4/4 mode graph
but was rejected after native reload exposed inherited CM5 RX and SATA/USB3
short classes. The selector corridor itself was not the reported short;
single-net edits on inherited copper are therefore not a reliable closure
method. Future repair must regenerate neighboring source-owned corridors
together and re-run native post-save DRC.

2026-09-08 — A bounded storage-only F.Cu POWER_GND zone probe reduced native
unconnected findings from 400 to 386 with zero shorts. It is preserved as
evidence only pending reference-plane, impedance, clearance, and DFM review;
the VBUS candidate remains the authoritative storage basis.
2026-09-07: Rejected RTL9210B V228 complete CLKREQ routing: native endpoint
connectivity and negative control pass, but CLKREQ crossed/shorted RSET,
REFCLK_N, and PERST in the local corridor. V227 remains the promoted
SPISO3/PERST basis; no Path-A or production-CAD change occurred.
2026-09-07: Rejected RTL9210B CLKREQ V229/V230 for XTAL_IN/SPISO3/RSET
crossings. Promoted V231 after shifting only the R3 return west of the RSET
diagonal. U1.13/R3.1/J1.52 native connectivity and the trace-removal
negative control pass with zero signal shorting/crossing classes. Path A and
production CAD remain unchanged.
2026-09-07: Promoted RTL9210B V232 U1.39 RTL_3V3 branch. Native U1.39/C3.1
connectivity and the trace-removal negative control pass with zero signal
shorting/crossing classes. Remaining support rails and Path-B validation stay
open; Path A and production CAD remain unchanged.
2026-09-07: Rejected RTL9210B V233 U1.52 RTL_3V3 isolated route: native
connectivity and negative control pass, but DRC found a lower-field
RTL_3V3/XTAL_OUT crossing and CLKREQ-via short. U1.52 requires coordinated
XTAL_OUT/3V3 allocation; V232 U1.39 remains promoted.
2026-09-07: Rejected RTL9210B U1.52 rail V234-V236 for XTAL_IN/RSET/pad-field
conflicts. Promoted V237 after a dogleg above pad 49 cleared the lower source
field. U1.52/C3.1 native connectivity and the trace-removal negative control
pass with zero signal shorting/crossing classes. Remaining Path-B gates stay
open; Path A and production CAD remain unchanged.
2026-09-07: Recorded RTL9210B rail-field V238/V239. V238 connected U1.36/C4.1
but crossed U1.39 3V3. V239 moved U1.39 but contacted XTAL_OUT and crossed
U1.52 3V3. Neither is promoted; the next attempt must co-author the three
lower-field rail escapes. Path A and production CAD remain unchanged.
2026-09-07: Corrected the V242 rail-evidence entry placement so bible.md
remains append-only. V240/V241 were rejected for SPISI crossing/shorting;
corrected V242 promotes the U1.36/U1.39/U1.52 RTL_1V1 co-allocation after
native connectivity and the trace-removal negative control passed, with zero
native signal shorting/crossing classes. Path A and production CAD remain
unchanged; remaining Path-B gates stay open.
2026-09-07: Rejected RTL9210B V243 U1.40 west-side RTL_1V1 escape. The
corrected native audit passed U1.36/U1.40-to-C4.1 and U1.39/U1.52-to-C3.1
connectivity with a trace-removal negative control, but native DRC introduced
USB_RXN0/RTL_3V3 and ISOLATEB/CLKREQ_N shorting classes. V242 remains the
promoted rail basis; Path A and production CAD remain unchanged.
2026-09-07: Rejected RTL9210B V248 corrected U1.60/U1.63 source dogbone.
Native connectivity and the full-rail-removal negative control passed, but DRC
reported an REFCLK_N crossing and a no-connect-pad/RTL_3V3 short. V242 remains
the promoted disposable rail basis; Path A and production CAD are unchanged.
2026-09-07: Rejected RTL9210B V249 REFCLK/RTL_1V1 co-allocation. Native
rail/REFCLK connectivity and the trace-removal negative control passed, but
DRC found two source-field crossings and one REFCLK_N/RTL_1V1 short. V242
remains the promoted disposable rail basis; Path A and production CAD remain
unchanged.
2026-09-07: Rejected RTL9210B V254 U1.39 support-field relocation. Native
rail/REFCLK/RTL3V3 connectivity and the negative control passed, but DRC
reported new RTL_1V1/RTL_3V3 crossings and a retained ISOLATEB/CLKREQ_N short.
The next attempt must move the complete adjacent support cluster together.
2026-09-07: Recorded RTL9210B V255 native-layer-aware A* routing evidence.
After correcting SMD layer occupancy and exact pad-center emission, the U1.40
endpoint audit passed and DRC showed no track crossings, but one RTL_3V3/RSET
short remained. No Path-A or production CAD changed; V242 remains promoted.
2026-09-07: Recorded RTL9210B V256 U1.52 RSET co-clearance evidence. The
inherited RTL_3V3 departure was shifted locally; native connectivity and the
trace-removal negative control passed, while DRC reported 623 findings / 16
opens with no shorting or track-crossing class. V256 is not promoted; Path A
and production CAD remain unchanged and V242 remains the promoted basis.
2026-09-07: Rejected RTL9210B V257/V258 local support-field routes. V257
completed the U1.52 RTL_3V3 join but exposed ISOLATEB/CLKREQ_N; V258 reduced
opens to 13 with bottom-edge RTL_1V1 vias but introduced multiple REFCLK/XTAL
shorts. The QFN rail/clock field must be co-authored; Path A and production
CAD remain unchanged.
2026-09-07: Rejected RTL9210B V259/V260 CLKREQ_N local re-escapes. V259
removed the ISOLATEB pad-field short but crossed REFCLK_N; V260 retained that
crossing after a south dogleg. The next trial must co-author the neighboring
QFN CLKREQ/REFCLK/sideband field; Path A and production CAD remain unchanged.
2026-09-07: Recorded RTL9210B V261 east-side CLKREQ_N re-escape. Native DRC
reported 633 findings / 15 opens with no shorting or track-crossing class.
V261 is retained as the current sideband geometry, not promoted; the complete
QFN rail/clock/support field remains open and Path A/production CAD are unchanged.
2026-09-07: Rejected RTL9210B V262 increased-clearance RTL_1V1 via bus. It
reduced opens to 13 but introduced multiple real RTL_1V1/REFCLK/XTAL shorts.
The next repair is coherent support-component relocation and coordinated field
regeneration; Path A and production CAD remain unchanged.
2026-09-07: Retained RTL9210B V266 as the coherent support-cluster placement
baseline. Scrubbed native DRC found no shorting or track-crossing class and
zero footprint errors; 228 findings / 36 opens are expected before route
regeneration. Path A and production CAD remain unchanged.
2026-09-07: Retained RTL9210B V269 as the corrected crystal-field basis.
Native connectivity passed U1.53/Y1.1, U1.54/Y1.2, C1.1/Y1.1, and C2.1/Y1.2;
native DRC reported 293 findings / 32 opens with no shorting or crossing class
and zero footprint errors. V267/V268 were rejected; Path A and production CAD
remain unchanged.
2026-09-07: Retained RTL9210B V270 RSET routing evidence. Native U1.51 to
R1.1 connectivity passed; native DRC reported 307 findings / 31 opens with no
shorting or crossing class and zero footprint errors. Remaining Path-B support
routes are open; Path A and production CAD remain unchanged.
2026-09-07: Retained RTL9210B V274 combined support-route evidence. Native
connectivity passed U1.20/C3.1, U1.34/R3.2, U1.39/R2.2, and U1.52/U1.34;
native DRC reported 319 findings / 27 opens with no shorting or crossing class
and zero footprint errors. SPI, PEDET, reset, and remaining support routes
remain open; Path A and production CAD remain unchanged.
2026-09-07: Retained RTL9210B V278 SPICS route basis after rejecting V275–V277
crossing implementations. Native U1.24/U2.1 connectivity and trace-removal
negative control passed; DRC reported 335 findings / 26 inherited opens with
no shorting or crossing class and zero footprint errors. Remaining support
routes are open; Path A and production CAD remain unchanged.
2026-09-07: Retained RTL9210B V282 split-layer SPISO basis after rejecting
V279–V281 crossing implementations. Native U1.24/U2.1 and U1.23/U2.2
connectivity passed with trace-removal negative controls; DRC reported 366
findings / 25 inherited opens with no shorting or crossing class and zero
footprint errors. Remaining SPI/support routes are open; Path A and
production CAD remain unchanged.
2026-09-07: Rejected RTL9210B V283 independent SPISO3 route. Native DRC found
SPISO3/SPISO and SPISO3/GND shorting classes plus an RTL_3V3 source-field
crossing. This is a route-implementation failure; V278/V282 remain retained
bases and the next SPI work must use coordinated channel allocation.
2026-09-07: Rejected RTL9210B V284 high-north SPISO3 route. Native DRC found
an SPISO3/GND short at the C1 crystal-support pad. This is a route-
implementation failure; the next SPI work must allocate remaining channels
together. Path A and production CAD remain unchanged.

2026-09-07: Retained RTL9210B V340 RSET route primitive. Native DRC and
saved-board negative-control audit pass with zero shorts/crossings; remaining
Path-B support/interface nets remain open.
2026-09-07: Retained RTL9210B V354 RTL_5V route primitive. V341-V353 were
rejected where native DRC found real QFN-field shorting/crossing classes.
V354 uses a B.Cu perimeter handoff around the retained In2 RTL_3V3 fanout;
native DRC reports zero shorting and zero crossing classes, and the saved
board endpoint audit plus trace-removal negative control pass. Path A,
production CAD, and the accepted storage architecture remain unchanged.
2026-09-07: Rejected RTL9210B V355/V356/V357 RTL_1V1 trials. V355 produced
QFN-field shorts/crossings; V356/V357 exposed XTAL_IN/XTAL_OUT channel
conflicts. These are disposable route-allocation failures, preserved with
native DRC receipts; no Path-A or production CAD changed. The next attempt
must co-author the complete RTL_1V1 fanout with crystal/support channels.
2026-09-07: Rejected RTL9210B V358 coordinated RTL_1V1 probe. Removing the
crystal copper before routing the full 1V1 field still produced six native
shorting classes and two crossings against RTL_3V3/RSET. The evidence
supports an isolated RTL_1V1 power region or jointly reallocated support
channel plan; no production CAD changed.
2026-09-07: Retained RTL9210B V364 coordinated RTL_1V1/RTL_3V3 power-field
basis. After correcting QFN escape allocation, native DRC reports zero
shorting/crossing classes and the combined nine-endpoint-per-rail audit plus
both trace-removal negative controls pass. Remaining support/interface nets
are open; Path A and production CAD remain unchanged.
2026-09-07: Rejected RTL9210B V359 isolated RTL_1V1 zone probe. The In2 zone
removed track crossings, but native DRC found seven real escape/via shorts
against RSET, XTAL_OUT, and RTL_3V3. Preserved as evidence; production CAD
and Path A remain unchanged.
2026-09-07: Retained RTL9210B V361 coordinated RTL_1V1-first basis after
native zone refill. V360's initial unfilled-zone connectivity was not
accepted; V361 used pcbnew ZONE_FILLER before audit. Native DRC reports zero
shorting/crossing classes, all nine 1V1 endpoints connect, and the trace-
removal negative control passes. Neighboring support routes remain open.
2026-09-07: Rejected RTL9210B V365/V366 support coallocation trials. V365
showed retained RSET/crystal primitives collide with the initial 1V1 channels.
V366 reduced the complete coallocated fanout to three shorts and one crossing
at C4/GND and the RTL_3V3 field. V364 remains the retained clean power-field
basis; no production CAD changed.
2026-09-07: Rejected RTL9210B V367 support coallocation trial. Moving C4 and
right-side RTL_1V1 handoffs removed shorts but left three native crossings
against the XTAL_OUT B.Cu spine. V364 remains the retained clean power-field
basis; Path A and production CAD remain unchanged.
2026-09-07: Retained RTL9210B V370/V372 XTAL_OUT relocation evidence. V370
passes native support audit with zero shorts/crossings and 21 opens; V373
lane-0 retry remains rejected with five shorts and three crossings where RXN
shares RTL_1V1 transition channels. Path A and production CAD remain unchanged.
2026-09-07: Retained RTL9210B V372 direct XTAL_OUT relocation basis. Native
DRC reports zero shorting/crossing classes and 21 inherited opens. V373 lane-
0 integration was rejected with five shorts and three crossings against
XTAL_OUT and RTL_1V1 launches; production CAD and Path A remain unchanged.
2026-09-07: Retained RTL9210B V368 clean coallocated support basis. Native DRC
reports zero shorts and zero crossings with 21 inherited opens. The native
audit passes RTL_1V1, RTL_3V3, XTAL_IN, XTAL_OUT, and RSET, and complete-net
trace-removal negative controls pass. Path B interface and integration work
remains open; Path A and production CAD remain unchanged.
2026-09-07: Rejected RTL9210B V369 lane-0 transplant. Native DRC found six
shorting and seven crossing classes where the V328 RX corridor conflicted
with XTAL_OUT and RTL_1V1 launches. This is an integration route failure;
Path A and production CAD remain unchanged.
2026-09-07: Rejected RTL9210B V374/V375 RXN re-escape trials. Native DRC
found source pad-field and companion-pair connector-launch conflicts. The
next lane work must regenerate both RX pair escapes and launch together;
Path A and production CAD remain unchanged.
2026-09-07: Rejected RTL9210B V376 complete RX-pair regeneration. Native DRC
reported ten shorting and two crossing classes at the U1 REFCLK/RTL_1V1
source field and lower via bus. Connector geometry improved, but source
escape allocation remains open; Path A and production CAD remain unchanged.
2026-09-07: Rejected RTL9210B V377 lane source-isolation trial. New RXN vias
contacted U1 REFCLK/adjacent QFN pads and native DRC reported six shorts and
one crossing. The V328 source via positions remain the valid starting point;
only conflicting RTL_1V1 launches should be reallocated next.
2026-09-07: Rejected RTL9210B V378 diagnostic because its manually recreated
lane used incorrect RX source/connector launch geometry; native DRC reported
two shorts and zero crossings. V380 reproduced the exact V328 lane geometry
and, with RTL_1V1/RTL_3V3/crystal copper removed for isolation, native DRC
reported zero shorts and zero crossings (37 intentional/inherited opens).
This separates route-authoring failure from lane-topology failure; Path A and
production CAD remain unchanged.
2026-09-07: RTL9210B lane co-allocation V381-V386 reworked RTL_3V3 and RSET
around the exact V328 lane. Earlier variants retained shorts/crossings; V387
co-authored RSET below the 3V3 channel and achieved native DRC zero shorts and
zero crossings with 27 open connections, while XTAL_OUT remained removed for
isolation. This is an intermediate support-channel basis, not Path-B closure;
Path A and production CAD remain unchanged.
2026-09-08: Rejected RTL9210B REFCLK V435-V437 source/launch trials. Native
DRC identified exposed-pad/XTAL interactions, adjacent J1 MDI contact entry,
and 0.4-mm QFN P/N source-field conflicts. These remain route-authoring
evidence; no Path-A or production CAD changed.
2026-09-08: Rejected RTL9210B REFCLK V438 narrow-fanout probe. Native DRC
flagged the 0.10-mm tracks against the 0.20-mm board minimum and still found
QFN source/exposed-pad conflicts. No rule relaxation was made; a complete
co-regenerated QFN fanout remains required.
2026-09-08: Rejected RTL9210B REFCLK V439 diverging-source probe. Native DRC
confirmed the adjacent 0.40-mm U1 REFCLK pad-field conflict with 0.20-mm
traces. A complete authoritative QFN fanout remains required; no rule
relaxation or production-CAD change was made.
2026-09-08: V440 native package audit confirmed RTL9210B U1 is the intended
SMD QFN-style `RTL9210B-CG_QUALIFICATION` footprint: 0.9 x 0.2 mm peripheral
SMD pads at 0.4 mm pitch and 4.8 x 4.8 mm exposed SMD pad 69. The current
REFCLK failures are a real package/board-rule escape interaction, not a
through-hole metadata artifact.
2026-09-08: RTL9210B REFCLK V443 improved the straight outward fanout and
eliminated connector-side errors; one 0.4-mm source-transition interaction
remains. Preserve V443 as the best REFCLK primitive while co-allocating the
transition vias with lane escape.
2026-09-08: RTL9210B V448 is the first valid isolated REFCLK primitive:
native DRC reports zero shorts/crossings with only inherited warnings, and
the saved-board audit plus two trace-removal negative controls pass. REFCLK
remains open for co-allocation with the lane source field and full support.
2026-09-08: Rejected RTL9210B REFCLK/lane coallocation V450. Native DRC found
source-field and RTL_3V3 conflicts plus a malformed RX_P handoff. V448 and
V328 remain the retained isolated primitives; no production-CAD change.
2026-09-08: V451 retained a clean isolated REFCLK primitive; V452 added the
exact V328 lane and exposed the true shared QFN-field conflicts between
REFCLK_N, RX_N, RX_P, and RTL_3V3. V452 is rejected; no Path-A or production
CAD changed.
2026-09-08: RTL9210B V454 is the strongest REFCLK/lane coallocation trial so
far. Native DRC leaves one real RX_P/RX_N source-transition short, with the
REFCLK overpass and connector launches otherwise clean. Preserve V454 as the
coallocation basis; no production-CAD or Path-A change.
2026-09-08: Rejected RTL9210B V455 RX_P source shift. Native DRC found source
crossing and TX_N pad/solder-mask conflicts; V454 remains the best combined
REFCLK/lane basis. Further work moves to complete QFN fanout regeneration.
2026-09-08: RTL9210B V456 corrected rotated-fixture authoring by removing the
entire stale local copper envelope before transforming U1. Native saved-board
connectivity and six trace-removal negative controls passed; DRC had zero
shorts/crossings but three real local source-via clearance errors. V457's
monotonic via row was rejected for one short and four source-field clearance/
mask errors. V458 removed the V454 RX_P/RX_N source short but created
REFCLK_N/RX_N coallocation crossings/shorts. No production CAD or Path-A
change; V454 remains the combined basis.
2026-09-08: Rejected RTL9210B V459 lower RX_P transition. It removed the
V454 RX_P/RX_N short, but native DRC found RX_P crossing both REFCLK source
tracks and violating the adjacent no-net pad clearance. The remaining work
is complete six-net QFN source-fanout regeneration; no production CAD or
Path-A change.
2026-09-08: Rejected RTL9210B V460 all-outboard rotated source row. The
direct diagonal F.Cu escapes created seven QFN source-field shorts/clearance
or solder-mask errors. This was a route-primitive failure; Path A and
production CAD remain unchanged, with V454 retained as the combined basis.
2026-09-08: RTL9210B V462 is the strongest rotated QFN source-fanout
primitive so far. Ordered vertical escapes with 0.9-mm-spaced F.Cu jogs
produce native DRC zero shorts/crossings/clearances; the saved-board audit
and six negative controls pass. This is only a source-fanout primitive, not
full Path-B closure; Path A and production CAD remain unchanged.
2026-09-08: RTL9210B V466 is a valid isolated RX endpoint primitive. Native
DRC reports zero shorts/crossings/clearances; the saved-board audit and two
negative controls pass. V465's single connector-transition clearance was
removed by moving RX_N's transition outward. This does not close full Path B;
Path A and production CAD remain unchanged.
2026-09-08: Rejected RTL9210B V463/V464 full lane-0 and REFCLK continuation
trials. V463 retained the clean V462 source fanout but had one RXN/RXP
clearance issue. V464's proven connector handoff reuse exposed three
corridor crossings and connector-transition clearance/short errors. V462 is
retained; no Path-A or production-CAD change.
2026-09-08: Corrected RTL9210B V475 after its audit caught a generator
omission in the TX source escapes. The regenerated four-pair lane basis
passes native saved-board connectivity, four negative controls, and DRC zero
shorts/crossings/clearances. Only inherited/incomplete-fixture findings
remain; REFCLK and support integration are still open.
2026-09-08: RTL9210B V479 is a clean isolated REFCLK layer-split primitive;
V480 combined it with the V475 four-pair lane basis but was rejected by
native DRC for one REFCLK source short, two lane/REFCLK crossings, and two
clearances. V475 and V479 remain the retained isolated bases; no production
CAD or Path-A change.
2026-09-08: Rejected RTL9210B V481 full six-net coallocation. Native DRC
found one REFCLK_N/TX_P short and two REFCLK/lane crossings, while retaining
zero clearance violations. V475 and V479 remain the isolated retained bases;
the next attempt must regenerate their source fields together.
2026-09-08: Rejected RTL9210B V482 combined REFCLK detours. Native DRC found
REFCLK_N conflicts with XTAL_OUT/U1 support and REFCLK_P crossing the TX_N
corridor. V475 and V479 remain the clean independent primitives; no
production CAD or Path-A change.
2026-09-08: RTL9210B V487 is the first complete six-net high-speed channel
basis. All four MDI pairs and both REFCLK nets pass native saved-board
connectivity and six negative controls; native DRC reports zero
shorts/crossings/clearances. Support/control integration remains open; no
Path-A or production-CAD change.
2026-09-08: RTL9210B V491 adds the rotated native U1.17 RTL_5V branch to
C5.1. The corrected F.Cu/B.Cu/ordinary-via corridor avoids REFCLK_N and the
M.2 supply launch. Native saved-board connectivity and one trace-removal
negative control pass. Native DRC has zero errors; nine inherited
incomplete-fixture warnings remain. Remaining supply pins and support nets
stay open; no Path-A or production-CAD change.
2026-09-08: RTL9210B V536 proves the U1.40 RTL_1V1 native graph and exact
branch-removal negative control, but its outer transition shorts the adjacent
RTL_3V3 field and is rejected by native DRC. V535 remains the accepted 3V3
primitive; Path A and production CAD are unchanged.
2026-09-08: RTL9210B V537/V538 prove U1.40 RTL_1V1 connectivity with exact
branch-removal negative controls but are rejected by native DRC. V537 is too
close to U1 pads 41/43; V538 collides with the accepted RTL_3V3 field. The
remaining issue is coherent 1V1/3V3 source-field coallocation, not net
ownership or audit methodology. Path A and production CAD remain unchanged.
2026-09-08: RTL9210B V546 applies the independent east-side U1.40 RTL_1V1
escape. Native U1.40-to-C4.1 connectivity and the exact branch-removal
negative control pass; native DRC adds no new short, crossing, or clearance
error and incomplete-fixture unconnected pads fall from 28 to 26. V546 is
the current U1.40 1V1 primitive; Path A and production CAD remain unchanged.
2026-09-08: RTL9210B V539/V540/V541 prove U1.40 RTL_1V1 connectivity and
exact negative controls, but native DRC rejects each local transition due to
3V3-field proximity or U1 pad/hole clearance. The next method is coherent
1V1/3V3 source-field regeneration; Path A and production CAD remain
unchanged.
2026-09-08: RTL9210B V535 completes the disposable four-source RTL_3V3
primitive. U1.20/U1.34/U1.39/U1.52 all reach C3.1 in the native graph and
the exact U1.52 branch-removal negative control passes. Native DRC adds no
new local short, crossing, or clearance error; inherited incomplete-fixture
findings remain. Path A and production CAD are unchanged.
2026-09-08: RTL9210B V521 audit correction removed the exact newly-authored
U1.34 RTL_3V3 branch for its negative control; native connectivity and the
negative control both pass. The V521 route itself is rejected: native DRC
reports 25 violations / 30 unconnected items, including RTL_3V3 conflicts
with the adjacent RTL_5V and RTL_1V1 field. This is a route implementation
failure; Path A and production CAD remain unchanged.
2026-09-08: RTL9210B V522/V523 are rejected local 3V3 source-field routes.
Their native audits and exact branch-removal negative controls pass, but DRC
finds 20 and 23 violations respectively from 3V3 conflicts with the 1V1 and
XTAL_IN fields. V524 is retained: its native U1.20/U1.34-to-C3.1 connectivity
and negative control pass, with no new local short, crossing, or clearance
error; inherited incomplete-fixture opens and hole-rule findings remain.
2026-09-08: RTL9210B V525 proves U1.39 can reach the 3V3 rail in the native
graph with an exact branch-removal negative control, but the lower/right
detour is rejected by 22 native DRC violations, including RTL_5V and REFCLK_P
crossings. This remains a local route implementation failure; Path A and
production CAD are unchanged.
2026-09-08: RTL9210B V526/V527 prove their intended native rail graphs and
exact branch-removal negative controls, but both routes are rejected by
native DRC. V526 crosses/clears RTL_5V and REFCLK; V527 collides with U1 pad
35 and RTL_1V1. The evidence points to coherent C3/source-field relocation
as the next route class; Path A and production CAD remain unchanged.
2026-09-08: RTL9210B V520 coallocates U1.25 RTL_1V1 and XTAL_IN after
clearing local RTL_3V3/RSET conflicts. Native 1V1 and XTAL_IN connectivity,
including C1.1, plus trace-removal negative controls pass; native DRC has no
new local errors. RTL_3V3 remains intentionally incomplete in the disposable
field; Path A and production CAD remain unchanged.
2026-09-08: RTL9210B V517 regenerates XTAL_IN beside the V516 1V1 field.
Native 1V1 and XTAL_IN audits plus trace-removal negative controls pass, but
native DRC rejects the fixed XTAL_IN B.Cu vertical crossing the new U1.25
channel. XTAL_IN's return spine must be coallocated with 1V1; Path A and
production CAD remain unchanged.
2026-09-08: Corrected the V516 native connectivity audit to use stable
KiCad UUID/geometry keys and a transitive graph walk. V516 now passes native
U1.16/U1.25/U1.36-to-C4.1 connectivity and a branch-removal negative control;
it has no new local DRC errors. It is retained as a disposable U1.25
coallocation primitive only; neighboring support spines still require
regeneration and Path A/production CAD remain unchanged.
2026-09-08: RTL9210B V516 coallocates U1.25 after removing the exact
XTAL_IN/XTAL_OUT/RTL_3V3 blocking spines. Native DRC has no new local errors,
but the strengthened native connectivity audit fails to prove the complete
U1.16/U1.25/U1.36 to C4.1 path. V516 is rejected; Path A and production CAD
remain unchanged.
2026-09-08: RTL9210B V514/V515 test U1.25 RTL_1V1 with vertical escape and
early F.Cu return. Native audits expose the intended connectivity, but DRC
rejects both for retained XTAL_IN/RTL_3V3 spine crossings and local return-via
clearance. Neighboring support spines must be reallocated with the 1V1 bank;
Path A and production CAD remain unchanged.
2026-09-08: RTL9210B V513 tests an outside-envelope U1.40/U1.50 via escape.
The transitive native audit fails to find one saved connectivity component,
and native DRC reports exposed-GND-pad and RTL_3V3 source-field conflicts.
V513 is rejected; complete local QFN support-field reallocation remains open.
2026-09-08: Strengthened the RTL9210B V512 audit to traverse KiCad's saved
native connectivity graph transitively. The corrected audit still fails to
connect U1.40 to U1.50, confirming a real via-chain break; native DRC also
reports GND-pad/hole and XTAL_IN clearance violations. V512 remains rejected.
2026-09-08: RTL9210B V512 exposed and corrected a disposable via-layer-pair
serialization defect. After regeneration, native connectivity still fails to
join U1.40/U1.50 and native DRC rejects the route for GND-pad/hole and
XTAL_IN clearance. V512 remains rejected evidence; Path A and production CAD
remain unchanged.
2026-09-08: RTL9210B V509-V511 test U1.40 RTL_1V1 source-field escapes.
Native connectivity and negative controls pass in each candidate, while DRC
rejects successive corridors at U1.41/U1.42, GND pad 45, and no-connect pad
48. The remaining U1.40 experiment must use a via escape outside the QFN
envelope; Path A and production CAD remain unchanged.
2026-09-08: RTL9210B V508 tests U1.25 RTL_1V1 with an early B.Cu/F.Cu return.
Native connectivity and the trace-removal negative control pass, but native
DRC rejects the route for DEVSLP/no-connect pad contact and crossings into
retained XTAL_IN/RTL_3V3 spines. Complete QFN pad-field allocation remains
open; Path A and production CAD remain unchanged.
2026-09-08: RTL9210B V507 tests U1.25 RTL_1V1 into the V506 trunk. Native
connectivity and the trace-removal negative control pass, but native DRC
rejects the route for crossings into retained support spines and contact with
U1.26 DEVSLP. It is retained as source-field allocation evidence only; Path A
and production CAD remain unchanged.
2026-09-08: RTL9210B V504-V506 complete the current RTL_1V1 local support
primitive. V504/V505 pass native connectivity with negative controls but are
rejected for C4 pad-field and RTL_3V3 crossing geometry. V506 shifts the
dogleg left; native DRC reports zero local errors with seven inherited
incomplete-fixture warnings. Path A and production CAD remain unchanged.
2026-09-08: RTL9210B V499-V503 continue isolated RTL_1V1 support routing.
Each saved-board native connectivity audit passes with a trace-removal
negative control. V499-V503 are rejected by native DRC for local source-field
collisions (RTL_5V, REFCLK_P, QFN no-connect/exposed-pad geometry); they are
retained as route evidence only. Path A and production CAD remain unchanged.
2026-09-08: RTL9210B V496 adds native U1.39 RTL_3V3 to the retained C3 rail.
The corrected left-side F.Cu escape joins the existing U1.34/C3 handoff and
avoids XTAL_IN. Native aggregation connectivity and one trace-removal
negative control pass. Native DRC has zero errors; nine inherited
incomplete-fixture warnings remain. Remaining rail source pads and support
nets stay open; no Path-A or production-CAD change.
2026-09-08: RTL9210B V497 connected U1.52 RTL_3V3 to the retained rail and
passed its native negative control, but native DRC rejected the lower-edge
escape for XTAL_IN and RSET source-field crossings/clearances. V497 is a
rejected route experiment; U1.52 remains open for co-allocation with the
completed support field. No Path-A or production-CAD change.
2026-09-08: RTL9210B V495 adds native U1.20 RTL_3V3 to the retained C3.1
rail. The final short F.Cu/left-side B.Cu handoff avoids RTL_5V and REFCLK.
Native aggregation connectivity and one trace-removal negative control pass.
Native DRC has zero errors; nine inherited incomplete-fixture warnings
remain. Remaining source pads and support nets stay open; no Path-A or
production-CAD change.
2026-09-08: RTL9210B V499 tested U1.16 RTL_1V1 to C4.1. Native connectivity
and the negative control pass, but DRC rejects isolated routes against the
RTL_5V handoff and then the SPISO2/RTL_3V3 source field. This is a
source-field co-allocation failure, not RTL_1V1 rejection; U1.16 must be
regenerated with SPI and remaining 1V1 escapes together. No Path-A or
production-CAD change.
2026-09-08: RTL9210B V498 is the first valid combined lower-QFN source-field
basis. XTAL_IN, XTAL_OUT, RSET, and U1.52 RTL_3V3 are regenerated together
around the retained 3V3 source field. Native connectivity passes all four
groups and four trace-removal negative controls. Native DRC has zero
shorts/crossings/clearance errors; seven inherited/incomplete-fixture
warnings remain. V498 is retained for further support integration; no
Path-A or production-CAD change.
2026-09-08: The latest RTL9210B V497 U1.52 variant still passes native
connectivity and its negative control but native DRC rejects its lower-QFN
escape against XTAL_IN and RSET. This narrows the next task to complete
source-field co-allocation; isolated U1.52 detours are not a valid route
class. No Path-A or production-CAD change.
2026-09-08: RTL9210B V494 joins native U1.33 RTL_5V to the accepted U1.17/C5.1
trunk before REFCLK. Native common-rail connectivity and one trace-removal
negative control pass. Native DRC has zero errors; nine inherited
incomplete-fixture warnings remain. Remaining supply pins and support nets
stay open; no Path-A or production-CAD change.
2026-09-08: RTL9210B V492 and V493 electrically connected U1.33 RTL_5V to
C5.1 and passed their native negative controls, but native DRC rejected both
route classes. V492 conflicted with the crystal ground return, 3V3 handoff,
and board edge; V493 crossed REFCLK_N. These are retained route
implementation failures, not RTL9210B rejection. The next attempt must
co-allocate the second 5V source with the crystal/REFCLK field.
2026-09-08: RTL9210B V488 adds the rotated-U1 crystal support from native
XTAL_IN/XTAL_OUT pads through Y1/C1/C2 with ordinary through-via escapes and
explicit local GND returns. Both crystal groups and two trace-removal negative
controls pass native saved-board connectivity. Native DRC has zero shorts,
crossings, clearance, solder-mask, and thermal errors; ten inherited
incomplete-fixture warnings remain. Rails, SPI, reset, sideband, and control
integration remain open; no Path-A or production-CAD change.
2026-09-08: RTL9210B V490 adds the rotated native U1.34 RTL_3V3 branch to
C3.1. After moving its ordinary-via handoff out of the retained XTAL_OUT
corridor, native saved-board connectivity and one trace-removal negative
control pass. Native DRC has zero errors; nine inherited incomplete-fixture
warnings remain. V490 is the first current-geometry 3V3 rail primitive; no
Path-A or production-CAD change.
2026-09-08: RTL9210B V489 adds RSET from rotated native U1.51 to R1.1 with
ordinary through-via transitions. Native saved-board RSET connectivity and
one trace-removal negative control pass. Native DRC has zero shorts,
crossings, and clearance errors; ten inherited incomplete-fixture warnings
remain. Rail, SPI, reset, sideband, and control integration remain open; no
Path-A or production-CAD change.
2026-09-08: RTL9210B V491 adds the rotated native U1.17 RTL_5V branch to
C5.1. The corrected F.Cu/B.Cu/ordinary-via corridor avoids REFCLK_N and the
M.2 supply launch. Native saved-board connectivity and one trace-removal
negative control pass. Native DRC has zero errors; nine inherited
incomplete-fixture warnings remain. Remaining supply pins and support nets
stay open; no Path-A or production-CAD change.
## 2026-09-08 — RTL9210B V552/V553 bottom-field discrimination

V552 and V553 were disposable coordinated source-field trials from the
accepted V546 RTL9210B support baseline. Both preserved native net identity
and were rejected by native DRC: V552 exposed XTAL_OUT/XTAL_IN/3V3 and
exposed-pad conflicts; V553 exposed remaining 1V1/3V3/LANE0/REFCLK source
field crossings. These are route-implementation failures, not an
architecture rejection. V546 remains the accepted U1.40 primitive and the
next attempt must reallocate the adjacent bottom signal field coherently.
2026-09-08: Phase24 status was reconciled with the live RTL9210B V552/V553
discriminator. The current Path-B open gate is coordinated lower QFN source
field allocation; V552/V553 are rejected route implementations, not an
architecture blocker. Path A and production CAD remain untouched.
2026-09-08: RTL9210B V554 moved the RX source escapes to B.Cu while collecting
the bottom RTL_1V1 pads. Native DRC rejected RX P/N, REFCLK, XTAL_OUT, 3V3,
and 1V1 collision classes. This is a route-implementation discriminator: the
complete lower QFN source field must be regenerated together. Path A and
production CAD remain unchanged.
2026-09-08: RTL9210B V555 tested an outboard B.Cu return for U1.55/U1.60/U1.63
RTL_1V1. Native DRC rejected crossings with RTL_3V3/RTL_5V and remaining
XTAL_OUT/RX/REFCLK source fields. The lower QFN field remains a coordinated
route-implementation open; Path A and production CAD are unchanged.
2026-09-08: RTL9210B V556 tested an In2 RTL_1V1 plane with ordinary-via
escapes. Native DRC rejected the F.Cu source dogbones/vias against adjacent
RX/XTAL/TXN and support geometry. The plane is not sufficient; the lower QFN
source field needs coherent regeneration. Path A and production CAD remain
unchanged.
2026-09-08: RTL9210B V557 tested the V388 right-edge RTL_1V1 fanout with an
In2 power plane. Native DRC rejected RX/XTAL/GND source-field conflicts and a
C4 ground collision. The orientation is not a drop-in fix; neighboring
high-speed launches must be regenerated coherently. Path A and production CAD
remain unchanged.
2026-09-08: RTL9210B V558 rechecked V546 at the production 0.2 mm track width
and strict 0.2 mm clearance. Native DRC found 25 findings / 26 opens,
including seven real clearance errors and no shorting/crossing class. V546's
prior clean claim is ruleset-qualified and is no longer treated as
production-clean evidence. Path A and production CAD remain unchanged.
2026-09-08: RTL9210B V560/V561 duplicate-copper cleanup trials reduced DRC
clutter but disconnected U1.25 in the native saved-board graph. Both were
rejected. Preserve V368 as the all-eight 1V1 evidence basis and require
connectivity-preserving cleanup tests; do not delete copper by geometry key.
2026-09-08: RTL9210B V562 corrected the V368 authoring path by regenerating
RTL_1V1 directly from V342 without duplicate RSET/XTAL copper. Native audit
passes all eight 1V1 pads plus C4, 3V3, crystal, and RSET groups; the
route-and-zone negative control passes. Native DRC has 11 findings / 21 opens
with no shorting/crossing or footprint errors. V562 is the retained Path-B
support baseline; remaining RTL_5V, GND, controls, SPI, REFCLK, and lane-0
work remains open. Path A and production CAD are unchanged.
2026-09-08: RTL9210B V563 connected U1.17/U1.33/C5.1 natively but was
rejected by DRC for XTAL_OUT/RTL_5V, RTL_3V3/RTL_5V, and PEDET/RTL_5V
collisions. RTL_5V remains open and V562 remains the retained support basis.
2026-09-08: RTL9210B V564 attempted a lower outboard RTL_5V corridor. Native
connectivity did not join both source branches, and DRC found RTL_5V/SPISI,
RTL_5V/RTL_3V3, and RTL_5V/PEDET collisions. V564 was rejected; V562 remains
the support baseline and RTL_5V remains open.
2026-09-08: RTL9210B V571 attempted a coherent east-side U1.34 RTL_3V3
reallocation to free the west 5V escape. The saved-board audit failed the
complete 3V3 endpoint group, and native DRC retained QFN/pad-field clearance
and solder-mask violations. V571 was rejected; V562 remains the support
baseline and Path A/production CAD remain unchanged.
2026-09-08: RTL9210B V572 corrected V571's missing RTL_3V3 In2 bridge and
replaced the diagonal U1.34-to-U1.39 escape with a Manhattan handoff. Native
audits pass complete RTL_5V and RTL_3V3 groups with independent trace-removal
negative controls. Native DRC is down to 14 findings with no shorting or
crossing classes, but QFN/pad-field and inherited support findings remain;
V572 is retained as a disposable candidate, not production closure.
2026-09-08: RTL9210B V565 tested a local In2 RTL_5V plane. Native DRC rejected
the source vias against RTL_3V3 and native connectivity left the 5V branches
disconnected. The plane-only approach is rejected; V562 remains the support
baseline and RTL_5V remains open.
2026-09-08: RTL9210B V566-V569 tested coherent local and perimeter RTL_5V
 escapes from the V562 baseline. V566 introduced 5V/GND and 1V1 crossings;
 V567 removed the shorts but retained crossings; V568 reduced the crossing
 class to one; V569 crossed the lower 1V1 spine and RSET. All were rejected
 as route implementations. V570 uses the upper perimeter loop: native
 U1.17/U1.33/C5.1 connectivity and the trace-removal negative control pass,
 with no native shorting or tracks-crossing classes, but 16 DRC findings
 remain, including local QFN/pad-field clearance issues. V570 is not
 production-clean or promoted. Path A, production CAD, and unrelated Phase
 24 work remain unchanged.
2026-09-08: RTL9210B V573 moved the lower RTL_5V transition away from U1
pads 31/32 but shorted the new via into the RTL_3V3 In2 spine. V574 moved the
3V3 spine around that via and reduced native DRC to 12 findings with no
shorting or crossing classes, but its independent saved-board audit failed
the complete 3V3 endpoint group. Both were rejected; V572 remains the
retained electrically connected baseline.
2026-09-08: RTL9210B V578 replaced the first U1.33 RTL_5V departure with an
exact-horizontal segment. Native saved-board connectivity showed dangling 5V
branches and native DRC still reported the pad-32 clearance violation. V578
was rejected; V576 remains the best connected candidate and the strict QFN
edge escape remains open.
2026-09-08: RTL9210B V576 restored the two omitted physical RTL_3V3 In2
bridges on the V574 coupled field. Native 5V and 3V3 endpoint audits pass with
independent trace-removal negative controls. Native DRC remains at 12 findings
with no shorting or crossing classes; V576 is retained as the current
connected disposable candidate, not production closure.
2026-09-08: RTL9210B V577 made a native 0.05 mm U1.34 handoff edit on V576.
Native DRC rose to 13 findings and still reported the strict pad-33/pad-34
source-field clearance and pad-35 clearance. V577 was rejected; V576 remains
the retained candidate. The limiting condition is intrinsic to the 0.4 mm
QFN edge field, not a missing saved-net association.
2026-09-08: RTL9210B V575 shifted the U1.34 RTL_3V3 departure by 0.05 mm on
the V574 lineage. Native DRC retained strict QFN source-field clearance and
the regenerated 3V3 branches were dangling in saved-board connectivity.
V575 was rejected; further progress requires coordinated QFN escape
authoring, not scalar coordinate nudges.
2026-09-08: RTL9210B V579 removed the diagonal U1.33 RTL_5V departure and
ran it straight to an outboard transition while retaining the V576 coupled
RTL_3V3 field. Native 5V/3V3 audits and both trace-removal negative controls
pass. Native DRC is 11 findings with 20 opens; the 5V source group is no
longer open. V579 is retained as the current 5V/3V3 candidate, not full
Path-B closure.
2026-09-08: RTL9210B V589 attempted a local B.Cu PEDET route from R2.1 to
U1.8. Native DRC reported 13 violations and 18 opens, including true PEDET
crossings with the retained RTL_5V vertical corridor and RTL_1V1 field. V589
is rejected; V583 remains the retained rail candidate. The live JMS583
support network is already instantiated, so older support-network TODO prose
is superseded by the current route-allocation/DRC gate.
2026-09-08: RTL9210B V594 completed J1.69→R2.1→U1.8 PEDET using an all-F.Cu
outer perimeter. Native saved-board connectivity and independent trace-removal
negative controls pass; native DRC returns to 9 findings with no PEDET
crossing. V594 is retained as the current PEDET-plus-rail disposable
candidate, not production closure.
2026-09-08: RTL9210B V595 added the local R3.1→U1.13 CLKREQ escape on F.Cu.
Native saved-board connectivity and the trace-removal negative control pass;
native DRC remains at 9 findings with no new crossing. V595 is retained as
the current PEDET/CLKREQ-plus-rail disposable candidate, not production
closure.
2026-09-08: RTL9210B V596/V597 rejected two SPICS route classes. V596 used
an occupied RTL_3V3 transition site; V597's all-F.Cu staircase crossed the
1V1 escape and shorted SPICS into RTL_3V3. Preserve V594/V595 as the valid
PEDET/CLKREQ-plus-rail basis; the next SPI attempt needs coordinated corridor
allocation.
2026-09-08: RTL9210B V600/V601 rejected direct/incorrect SPISI escapes: V600
ran through U1 interleaved power/control pads after a U2 rotation, and V601's
transition occupied the RTL_3V3 In2 field. V602 moved the transition west;
U1.18→U2.5 native connectivity and the trace-removal negative control pass,
with no new DRC short/crossing. V602 is retained as the SPISI sub-primitive,
not full SPI closure.
2026-09-08: RTL9210B V603/V604 rejected independent SPISO3 escape classes.
V603 entered the lower RTL_3V3 field and crossed 1V1; V604 moved west but
crossed/shorted the retained SPISI launch. Future SPI routing must allocate
the shared source and endpoint channels together.
2026-09-08: RTL9210B V605-V608 rejected successive SPISO3 channels. Failures
progressed from SPISI crossing to lower power-field clearance and finally a
coordinated endpoint collision at the U2 SPICLK pad row. The next SPI pass
must co-author both U1 source escapes and U2 endpoint dogbones.
2026-09-08: RTL9210B V617-V619 rejected SPICLK source/channel variants.
Moving the channel above SPISI did not prevent source departure crossings with
SPISI/RTL_5V, while lower endpoints entered 3V3. The next pass must co-author
the complete U1 QFN SPI source field.
2026-09-08: RTL9210B V616 rejected the SPISO lower-corridor trial. It crossed
retained SPISO3/SPISI channels and violated the 3V3 source-field clearance.
The next SPI pass requires complete five-net allocation or coherent U2 support
relocation.
2026-09-08: RTL9210B V609-V614 rejected coordinated SPISI/SPISO3 endpoint
variants for U2 ground, occupied-via, and lower-field contact/clearance.
V615 lifts the SPISI bottom dogbone; both nets pass native connectivity and
trace-removal negative controls with no new DRC short/crossing. V615 is the
retained coordinated two-net SPI sub-primitive.
2026-09-08: RTL9210B V598/V599 rejected two further SPICS route classes.
V598 shorted its B.Cu transition into retained RTL_1V1/RTL_5V fields; V599's
direct F.Cu outer departure crossed the PEDET/5V/3V3/CLKREQ source field.
The next SPI pass must co-author the shared QFN escape; V594/V595 remain the
valid PEDET/CLKREQ-plus-rail basis.
2026-09-08: Re-saved the historical V35 rotated-U1 support reference through
native zone refill as PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_NATIVE_REFILLED.
Current native DRC is 4 inherited warnings; five-net SPI and XTAL/RSET audits
pass with trace-removal negative controls. This is the current source-field
reference, not production closure.
2026-09-08: Added the V35 source-field checkpoint report and preserved V1/V2
RTL_5V disposable probes. V2 was rejected by native DRC for RTL_5V crossings
with SPISI/RTL_3V3, a QFN-edge contact, and dangling segments. The next Path-B
experiment must co-author all rails and QFN departures around the proven V35
five-net SPI/crystal field; Path A and production CAD remain untouched.
2026-09-08: V4 is retained as the V35-derived RTL_5V sub-primitive. Native
U1.17/U1.33/C5.1 connectivity and trace-removal negative control pass, and
native DRC returns to the four inherited warnings. Full RTL9210B support,
including other rails and controls, remains open.
2026-09-08: The first V35-derived RTL_1V1 lower-bus probe was rejected by
native DRC (21 violations) for RSET/XTAL_OUT crossings, U2/C4 ground contacts,
and occupied via fields. Its native endpoint audit and trace-removal negative
control passed; the next 1V1 pass must relocate/co-author the support field.
2026-09-08: The U2-left coordinated V35 experiment cleared the lower 1V1/U2
corridor, and native SPI/1V1 audits passed, but naïve regenerated SPI source
channels caused 14 native DRC violations including five QFN-source shorts and
an XTAL_OUT crossing. Reject the route implementation; co-author U1 SPI
source escapes and 1V1 departures next.
2026-09-08: The source-preserving U2-left V35 candidate passes native SPI and
lower 1V1 audits with no SPI crossings. Native DRC has eight findings, only
two real local U1.55/XTAL_OUT conflicts plus six inherited warnings. Retain it
as the coordinated basis; co-author the crystal drop and U1.55 escape next.
2026-09-08: The V35/U2-left crystal co-author candidate passes native SPI,
XTAL_IN/XTAL_OUT/RSET, and lower 1V1 audits with negative controls. Native DRC
has six inherited warnings and no signal violations; 26 intended support/
external opens remain. Retain it as the strongest disposable basis.
2026-09-08: The V35/U2-left upper RTL_3V3 field passes native endpoint and
negative-control audits with no signal DRC violations. The lower RTL_3V3
trial was rejected for QFN/1V1/RSET contacts and active minimum-width-rule
violations; no DRC rule was relaxed.
2026-09-08: The V35/U2-left upper RTL_3V3 field passes native endpoint and
negative-control audits with no signal DRC violations. Lower RTL_3V3 trials
remain rejected for RSET/1V1/QFN source-field conflicts; a 0.13208 mm retry
also violated the active 0.200 mm minimum-width rule. No rule was relaxed.
2026-09-08: V620/V621 tested a new U1.39-to-U2.8 RTL_3V3 escape with native
endpoint and trace-removal negative-control PASS. Native DRC rejected both
geometry variants for QFN-field clearance/shorting conflicts, including an
RTL_1V1/RTL_3V3 short and adjacent USB-pad conflicts. Preserve the raw
evidence; co-author the complete lower QFN field next. Path A and production
CAD remain unchanged.
2026-09-08: V624 added first copper to the native 0-degree RTL9210B placement
basis. Native DRC rejected the route implementation with 30 findings,
including source-pad shorts/clearance, RSET adjacency, and edge-clearance
violations. The 0-degree no-copper placement probe remains retained; Path A
and production CAD remain unchanged.
2026-09-08: V625 moved the U1.39 RTL_3V3 via farther outboard on the native
0-degree orientation. Native DRC still found source-segment clearance and
solder-mask bridging at adjacent USB_DP/USB_DM pads. The failure precedes the
via corridor and confirms the intrinsic 0.4 mm QFN/strict-width constraint;
V625 is rejected route evidence. Path A and production CAD remain unchanged.
2026-09-08: V626 tested a disposable 0.13208 mm JLC-width U1.39 escape. Native
DRC still found adjacent USB-pad clearance and solder-mask bridging, while
the saved board rejected the 0.25 mm drills and sub-0.20 mm tracks. No
production rule was changed; V626 is rejected evidence.
2026-09-08: V627 tested a 0.60/0.30 mm ordinary via-in-pad at RTL9210B U1.39.
Native DRC found a real short to adjacent USB_DM and hole-clearance failures
to neighboring QFN pads. Via-in-pad is rejected under the saved rules; Path A
and production CAD remain unchanged.
2026-09-08: Corrected the schematic-to-PCB parity audit to normalize only
hierarchical XML net paths against flattened PCB names. The current storage
placement result is 64 actionable mismatches rather than 286 representational
false positives. Real missing/incorrect support, selector, and M.2 ownership
defects remain open; no connectivity was waived.
2026-09-08: Reconciled Phase 24 storage status prose with the live design.
The JMS583 support network is already instantiated and its support audit
passes; older imperative wording is explicitly superseded historical context.
The storage placement generator now owns R24/R32/R33 and removes donor
duplicates before regenerating the disposable current placement. The result
is not promoted: the available parity comparison still uses a stale XML
export, and native DRC/connectivity closure remains open.
2026-09-08: V628 tested a 180-degree native RTL9210B QFN orientation with the
exposed-pad datum preserved. The no-copper basis has four inherited DRC
warnings; its U1.39-to-U2.8 RTL_3V3 probe is natively connected and its
trace-removal negative control fails as required. Retain it as the next
coherent source-field basis; Path A and production CAD remain unchanged.
2026-09-08: V629 added the complementary U1.34-to-U2.3 RTL_3V3 corridor to
the retained 180-degree RTL9210B basis. Both lower channels are natively
connected; removing all RTL_3V3 tracks breaks both. Native DRC remains four
inherited warnings with no shorting/crossing class. This remains disposable
source-field evidence; Path A and production CAD remain unchanged.
2026-09-08: V630 separated the RTL_5V transition from the retained 180-degree
RTL9210B rail field. Native DRC reduced the candidate to one real clearance
violation at U1.33 versus adjacent U1.32 no-connect pad geometry (0.0769 mm
actual versus 0.20 mm required); both lower RTL_3V3 channels stayed native
connected. Reject the route; next step is alternate package/land-pattern
authority, with no routing-rule relaxation.
2026-09-08: Marked the older 2026-09-06 dual-mode checkpoint in
PHASE24_STATUS.md as superseded historical evidence. Its former
"instantiate support network" next-action wording now states that the work
was completed and that routing/release validation is the live open gate.
2026-09-08: Corrected the live root schematic and its scaffold metadata from
the obsolete SATA-only/NVMe-excluded description to the implemented dual-mode
storage architecture. Historical fixture copies and legacy validation scripts
were left unchanged as evidence and are not current authoring inputs.
2026-09-08: V631 separated the RTL9210B 5V/3V3 transition field farther west.
Native DRC returned to four inherited warnings with no shorting, crossing, or
clearance class. U1.17/U1.33/C5.1 RTL_5V and both lower RTL_3V3 endpoint
groups pass saved-board connectivity; removing all rail traces breaks all
three. Retain V631 as disposable source-field evidence.
2026-09-08: V632 tested an all-1V1 perimeter collector on V631 and rejected it
after native DRC found U1.16/U1.17 and U1.36/U1.35 source shorts, crossings
with retained 5V/3V3 fields, a C4 ground collision, and edge-clearance
findings. This was a route-allocation failure; rules and architecture remain
unchanged.
2026-09-08: V633 tested a bottom-edge U1.36/U1.40/U1.50 RTL_1V1 collector.
Native DRC found a real U1.40-to-retained-U1.39 RTL_3V3 transition collision
and additional source/edge findings. Reject the collector; retain V631 and
co-author the next 1V1 departures with the 3V3 transition field.
2026-09-08: V634 routed U1.60 to C4.1 as a right-side RTL_1V1
sub-primitive. Native connectivity passes, removing all RTL_1V1 traces breaks
the endpoint, and native DRC remains four inherited warnings with no signal
violation. Retain this channel; the remaining 1V1 source field is open.
2026-09-08: V636 extended the RTL_1V1 trunk with a north-of-QFN U1.25
departure. Native U1.25-to-C4.1 connectivity passes, removing all RTL_1V1
traces breaks the path, and native DRC remains four inherited warnings with
no signal violation. Remaining 1V1 pins stay open.
2026-09-08: V635 extended the valid right-side RTL_1V1 channel with U1.16.
Native U1.16-to-C4.1 connectivity passes and removing all RTL_1V1 traces
breaks the path; native DRC remains four inherited warnings with no signal
violation. Remaining 1V1 pins are still open.
2026-09-08: V638 added right-edge U1.55/U1.63 RTL_1V1 extensions to the
passing C4.1 trunk. Both native endpoints pass and removing all RTL_1V1
tracks breaks both; native DRC remains four inherited warnings with no signal
violation. Only U1.36/U1.40 remain in this local 1V1 allocation.
2026-09-08: V637 extended the right-side RTL_1V1 trunk with U1.50-to-C4.1.
Native connectivity passes, removing all RTL_1V1 traces breaks the path, and
native DRC remains four inherited warnings with no signal violation. The
U1.36/U1.40/U1.55/U1.63 source cluster remains open.
2026-09-08: V639 tested U1.40 RTL_1V1 continuation from the retained V638
field. The first departure violated U1.41 USB_TXP0 clearance; V2 cleared that
pad but crossed the retained U1.39 RTL_3V3 source departure and added a
solder-mask bridge. Native endpoint connectivity and the trace-removal
negative control pass, but the route is rejected. Co-author U1.39/U1.40
adjacent-pad exits next without relaxing rules or changing architecture.
2026-09-08: V640 retained the delayed-bend U1.40 RTL_1V1 escape. Native DRC
has only the four inherited warnings, with no signal short, crossing, or
clearance class. Native U1.40-to-C4.1 and U1.39-to-U2.8 connectivity pass.
The adjacent source-field escape is valid; continue with U1.36 without
relaxing rules or changing architecture.
2026-09-08: V641 corrected the U1.36 RTL_1V1 escape after its first via
collided with the retained B.Cu RTL_3V3 collector. V2 moves the via/trunk to
the north-side channel; native DRC again has only four inherited warnings and
U1.36-to-C4.1 connectivity passes. The local QFN 1V1 source set is connected.
2026-09-08: V642 added ordinary outboard GND returns for U1.69/U1.66/U1.45.
After moving the U1.45 via away from the retained U1.40 via, native DRC has
only three inherited silkscreen warnings and filled-zone connectivity joins
all three QFN ground pads. Continue with the remaining support opens.
2026-09-08: V643 joined U1.20 RTL_3V3 into the lower physical field through
an ordinary via and B.Cu corridor; native DRC remains at three inherited
silkscreen warnings. V644's attempted R2/R3 source extension crossed the
retained RTL_5V B.Cu collector and is rejected. Reallocate that source corridor
without relaxing rules.
2026-09-08: V645 completed the physical RTL_3V3 field. The R2/R3 source joins
below the retained 5V collector and the U1.52/C3 branch joins through B.Cu.
Native DRC has no RTL_3V3 finding and remains at three inherited silkscreen
warnings; remaining support opens are elsewhere in Path B.
2026-09-08: V647 tested staggered XTAL_IN/XTAL_OUT transitions. The direct
F.Cu route crossed retained rails; the B.Cu retry removed pair contact but
still conflicted with the U1.20 3V3 via and 1V1 corridor. Reject the trial and
co-author crystal exits with the rail field.
2026-09-08: V648 tested a SPISI source-to-U2.5 channel. Native routing exposed
crossings with the retained RTL_3V3 source trunk and RTL_5V collector; reject
the route and preserve the rail field for a separate SPI allocation.
2026-09-08: V649 tested a high B.Cu SPISI corridor. Its x=91 transition
column crossed the retained RTL_3V3 and RTL_5V collectors; reject the route
and preserve the accepted rail geometry.
2026-09-08: V651 fresh native recheck of the retained RTL_3V3-field board
reports 3 inherited silkscreen warnings and 25 opens. The saved-board native
inventory confirms all 9 RTL_3V3 pads are joined; SPISI, RSET, and XTAL_IN
remain open. This is the current reproducible Path-B baseline.
2026-09-08: Corrected the native RTL9210B support inventory to include
RTL_3V3. The saved C3-join board has all nine RTL_3V3 pads in one physical
connectivity component; SPISI remains disconnected and SSD_3V3 has only M.2
connector pads with no source in this disposable fixture.
2026-09-08: V650 corrected the V645 RTL_3V3 closure claim. Native DRC and the
saved-board inventory show multiple separate RTL_3V3 components; endpoint-only
checks were insufficient. Reopen the rail until the complete same-net field
is physically unified.
2026-09-08: V646 tested the first RSET escape. Native endpoint connectivity
was present, but the B.Cu diagonal crossed the retained U1.40 RTL_1V1 corridor;
reject the route and preserve the accepted rail geometry.
2026-09-08: V652 retained the corrected RSET lower-channel route. Native DRC
has only three inherited silkscreen warnings, no signal violation, and the
open count falls to 24. The U1.51-to-R1.1 path is locally closed; full Path-B
support remains open.
2026-09-08: V653 tested local Y1/C1/C2 relocation. Native DRC found C2 versus
RTL_1V1 clearance/shorting and XTAL_IN versus the U1.20 RTL_3V3 transition;
reject the relocation and co-author crystal support with the retained fields.
2026-09-08: V654 fixed the disposable KiCad helper to capture net codes before
SetNet, then reran the U1.52/crystal co-author candidate. Native DRC rejected
it for XTAL pair/rail crossings and a dangling 3V3 segment; production CAD and
accepted rail geometry remain unchanged.
2026-09-08: V655 tested a joint U1.52/crystal and shifted-3V3 field. Native
DRC rejected it for XTAL source crossing and 3V3/XTAL and 3V3/1V1 collisions.
The next solution must coherently reauthor or relocate the local support field.
2026-09-08: V656 moved U2 east and regenerated all five SPI channels as one
field; native DRC rejected 43 violations including shorts/crossings. V657
tested a narrower SPICS west channel; native DRC rejected seven violations,
including CLKREQ_N/SPICS shorting. Preserve both as route-implementation
evidence only; Path A, production CAD, and validation rules remain unchanged.
2026-09-08: V658 corrected its helper and validly reran a coordinated
XTAL_IN/XTAL_OUT/RSET source field. Native DRC rejected 31 findings, including
XTAL pair, rail, and RSET shorts/crossings. Preserve it as lower-QFN
route-allocation evidence only; no Path-A or production-CAD artifact changed.
2026-09-08: The independent V658 native saved-board audit passed XTAL_IN,
XTAL_OUT, and RSET endpoint connectivity; its XTAL_OUT trace-removal negative
control failed as required. V658 is therefore rejected for physical DRC
geometry, not synthetic connectivity.
2026-09-08: V659 corrected its helper and tested all three RTL9210B rails from
the fresh V35 source field on an In2 collector. Native DRC rejected 56
violations, including rail-to-rail, rail-to-SPI, and rail-to-crystal
shorts/crossings. Preserve the result as rejected shared-collector evidence.
2026-09-08: V660 relocated C3/C4/C5 and used separate In2 rail collectors on
the V35 signal field. Native DRC rejected 98 violations, including rail-to-
crystal, rail-to-SPI, rail-to-rail, and crossing classes. Endpoint relocation
alone is rejected; source escapes and rails must be co-authored.
2026-09-08: Fresh native KiCad DRC of the retained V35 source-field reference
reports four inherited findings and 34 unconnected pads, with no shorting or
tracks-crossing class. Preserve it as the reproducible source-field baseline,
not as full RTL9210B support closure.
2026-09-08: V661 combined the proven V35 RTL_5V route with the U2-left
crystal/1V1/upper-3V3 field. Native DRC reports nine inherited warnings and no
shorting/crossing class, but 23 support pads remain open. The legacy RTL_5V
negative-control helper unexpectedly passed because it removed a redundant
same-net track; do not treat that audit as valid. Preserve V661 as the next
rail basis.
2026-09-08: Corrected the V661 RTL_5V negative control to remove every
duplicate instance of the unique trunk. The saved-board endpoint audit passes,
and the corrected trace-removal control fails as required.
2026-09-08: V663 moved the U1.39 lower RTL_3V3 transition farther west; native
DRC still reported the RTL_3V3/RTL_1V1 QFN source-field short (10 findings,
21 opens). Reject the escape class; no architecture or production CAD changed.
2026-09-08: V664 tested a diagonal U1.39 RTL_3V3 departure; native DRC still
reported the RTL_3V3/RTL_1V1 short and crossings (13 findings, 21 opens).
Reject the escape class; no architecture or production CAD changed.
2026-09-08: Native footprint geometry quantified the RTL9210B lower-QFN DFM
blocker: U1.39/U1.40 are 0.4 mm apart with 0.2 x 0.9 mm pads, while an
ordinary 0.60/0.30 mm via plus 0.20 mm clearance requires 0.95 mm separation.
V663/V664 reproduce the source-field shorts/crossings. Reject RTL9210B Path B
for the current Rev-A package/DFM contract; retain Path A and do not relax
rules or alter production CAD.
2026-09-08: Fresh native DRC of the current Path-A storage placement candidate
reports 876 violations and 499 unconnected items, including real crossings
and M2_3V3/FORCE_NVME shorts. Preserve this as the current open integration
gate; do not infer closure from candidate names or historical fixtures.
2026-09-08: Restored the disposable Path-A storage placement candidate to the
prior generator output after rejecting a worse placement-map experiment.
Fresh native DRC remains 876 violations and 499 unconnected items, including
real crossings and M2_3V3/FORCE_NVME shorts. The Path-A integration gate stays
open and production CAD remains unchanged.
2026-09-08: Reconciled Phase 24 current-state documentation with the live
Path-A dual-mode storage implementation. Marked the V3 placement (863 DRC,
499 opens, real PERST-to-USB_DP short, and crossings) and USB3 route trial
(834 DRC, real source shorts/crossings) as rejected disposable evidence;
restored the authoritative generator and kept Path B historical/superseded.
2026-09-08: Moved disposable JMS583 U11 west to clear the inherited
CM5_PERST corridor while retaining the outboard J5 mode jumper. Native DRC
reports 843 violations and 499 unconnected items with zero shorting items;
eight crossings and incomplete copper remain. Retain this as the best current
Path-A routing basis, not a Phase 24 pass.
2026-09-08: Ran the native-pad JMS583 support author against the accepted
U11-west/J5-clear placement. Reject the trial: five real shorts and seven
crossings arise from stale distributed support coordinates and direct F.Cu
joins through the QFN field. The support circuitry remains authoritative;
coherent local placement/routing is the next Path-A task.
2026-09-08: Retained the native-pad JMS583 RSET escape probe. U11.39 to
R80.1 is connected on F.Cu with no native shorting items; the disposable
board reports 840 total violations. This closes only the RSET sub-primitive.
2026-09-08: Refilled zones and reran the split-layer JMS583 crystal probe.
Stale zone/via-hole findings disappeared, but native DRC still rejects the
0.20-mm traces leaving adjacent 0.4-mm-pitch U11 crystal pads at about
0.19-mm clearance. Keep crystal support open; do not relax rules.
2026-09-08: Corrected the live Y10 generator map from invented JMS_XIN/
JMS_XOUT nets to the authoritative XIN/XOUT nets used by U11 and STORAGE.
Regenerated the candidate; the native crystal probe now has zero shorting
items and USB3 parity remains PASS. Physical crystal escape remains open.
2026-09-08: Added and ran a fail-closed native PCB audit for all 64 JMS583
U11 pad nets against the live `JMS` authority map. It passes, preventing
future routing probes from hiding another symbol/PCB net-name mismatch.
## 2026-09-08 — Phase 24 JMS583 authoring reconciliation

The live Path-A storage generator was corrected to reuse the reviewed JMS583
64-pin schematic map and to keep generated support passives within the
disposable acreage outline. Native U11 pad-authority and USB3 endpoint audits
still pass; the regenerated placement remains open at 857 DRC violations and
499 unconnected items. A stale divergent crystal probe was restored to the
last short-free disposable basis while its later report remains rejected
evidence. JMS583 package identity/pitch are documented, but final land-pattern
pad geometry remains an explicit open production gate.

The isolated JMS_RESET_N direct-join discriminator was rejected by native DRC:
its saved path enters the local USB coupling field at 0.0379 mm clearance.
This is route-allocation evidence and directs the next support pass to use a
deliberate ordinary-via corridor.

The first ordinary-via reset corridor was rejected by native DRC: its west
B.Cu transition shorted the JMS_XAVDDH support field. This preserves the
failure as corridor-allocation evidence and leaves Path A open.

The next bounded support placement moved R80/L10/Y10 beside U11 and corrected
the L10 LXO net alias. The all-net direct support trial was rejected at one
real reset short and six crossings; co-location is retained as a better basis,
but native-pad-aware per-net source escapes are still required.

The refreshed committed local-anchor placement report remains 857 DRC
violations and 499 unconnected items with eight crossing findings and no
shorting class on the placement-only board. This confirms the coordinate
correction is stable; the routed all-net trial remains separately rejected.

The lateral JMS_RESET_N escape was re-authored to leave U11.15 sideways and
enter R81.1 from the free pad side. Native connectivity and a trace-removal
negative control both pass; the V3 DRC report has no local shorting or
crossing findings, with remaining crossings inherited from the donor USB
fixture.

The JMS_AVDD33 U11.19-to-C80.1 south-east escape passed native connectivity
and a trace-removal negative control with no authored shorting/crossing class.
It is retained as a support sub-primitive; complete rail routing remains open.

The paired JMS VBUS divider escape passed native U11.16/R82.1 and
R82.2/R83.1 connectivity plus a trace-removal negative control. Its remaining
crossings are inherited donor USB artifacts; full support routing remains open.

The JMS crystal pad-20 sensitivity candidate passed native XIN/XOUT endpoint
connectivity and its trace-removal negative control. It remains disposable
evidence only because final JMS583 land-pattern pad geometry is still open.
The implementation narrative was reconciled so JMS583 library evidence is
described as structural package identity only; selector/contact audits pass,
but final JMS583 land-pattern geometry remains an explicit open gate.

The JMS_AVDDL U11.20-to-C83.1 south-east escape passed native connectivity
and a trace-removal negative control with no authored shorting/local crossing
class. Remaining AVDDL pins and full rail routing remain open.

The four-net JMS support cohort (reset, AVDD33, VCCO, VCCK) was co-authored
with separated departures and validated natively plus a combined trace-removal
negative control. It has no authored shorting/crossing class; full support
release validation remains open.

The six-net JMS support cohort added rotated-L10 VDDREG and LXO to the
validated reset/rail decoupler paths. All native endpoint checks and the
combined trace-removal negative control pass; no authored shorting/crossing
class remains in the saved cohort.

The JMS_VCCO U11.6-to-C81.1 escape was moved north of the inherited CM5
PERST corridor. Native connectivity and trace-removal negative control pass;
the prior y=150 mm crossing variant remains rejected evidence.

The JMS_VCCK U11.2-to-C82.1 west/south escape passed native connectivity and
a trace-removal negative control with no authored shorting/crossing class.
The rotated L10 JMS_VDDREG_5V escape passed native U11.1-to-L10.2
connectivity and a trace-removal negative control with no authored shorting or
local crossing class. Coupled LXO support remains open.

The rotated L10 LXO escape passed native U11.64-to-L10.1 connectivity and a
trace-removal negative control after moving Y10 clear of the corridor. The
prior Y10 collision remains rejected evidence.

The complete JMS reset-delay branch passed native U11.15/R81.1 and R81.1/C85.1
connectivity plus a trace-removal negative control with no authored
shorting/local crossing class.

The right-side JMS_XAVDDH U11.52-to-C84.1 escape passed native connectivity
and a trace-removal negative control with no authored shorting/local crossing
class. Remaining analog support remains open.

2026-09-08: Rejected JMS XAVDDH V7 perimeter via after native DRC identified
it in the U11.57 JMS_GPIO12_NC pad field. Retained V8 as corrected
seven-net support-cohort evidence: U11.52 exits south from the native pad,
uses ordinary through-vias outside the QFN field, and passes native endpoint
connectivity plus the trace-removal negative control with no authored local
short/crossing class. The 878-violation/499-unconnected inherited donor-board
DRC result remains open evidence, not a Phase 24 pass.

2026-09-08: JMS REXT V1 direct route was rejected after native DRC found a
real JMS_REXT/JMS_XAVDDH short. Relocating R80 in V2/V3 removes that short,
but the 0.20 mm REXT escape still fails U11.39 adjacent-QFN clearance and
the R80 approach. Preserve these as source-field/land-pattern evidence; do
not promote the route or relax the active manufacturing rules.

2026-09-08: Reconciled the live JMS583 QFN64 fixture against the saved
JMicron Rev 2.1 Figure 4: changed terminal width from 0.22 to the allowed
0.20 mm maximum, corrected the stale TI package description, and added the
nominal 4.46 mm exposed pad on POWER_GND. The regenerated V9 seven-net
cohort passes native connectivity and trace-removal negative control; its
811-violation/499-unconnected DRC result remains open because paste/mask/
courtyard review and inherited manufacturing findings are not closed.

2026-09-08: Updated the native JMS583 PCB authority audit to cover all 64
signal pads plus the newly authoritative grounded exposed pad 65. The live
placement audit passes; this changes coverage reporting only and does not
close the remaining support-routing or manufacturing gates.

2026-09-08: Post-reconciliation REXT V7 confirms the corrected JMS583
U11.39 source field is no longer the failure. The translated R80 approach
instead shorts the U12 exposed pad and crosses the inherited CM5_PERST
corridor. V7 is rejected as placement evidence; REXT remains open and no
production rule was relaxed.

2026-09-08: Retained JMS REXT V8. Moving R80 into the open U11/U12 gap and
using an orthogonal native-pad F.Cu escape removes the prior REXT source,
PCIe, C93, U12-EP, and AVDD33 corridor conflicts. Focused native DRC reports
no JMS_REXT short/crossing, and the endpoint plus trace-removal negative
control pass. The full JMS583 support/release gate remains open.

2026-09-08: Promoted the validated JMS REXT V8 placement into the storage
placement generator at R80=(148,130), regenerated the current Path-A
candidate, and reran the seven-net cohort. Native connectivity and the
trace-removal negative control pass; the V10 DRC remains 811 violations / 499
inherited unconnected items. This is placement-authority progress, not full
Phase 24 closure.

2026-09-08: Reconciled live Phase 24 documentation with native evidence and
fixed a real U12 USB3 source-map defect. U12 pins 24/25 now own the
bridge-side JMS_USB3_TXN/P nets across C87/C86, while pins 22/23 remain the
direct USB_RXN1/P links. The USB3_FULL5 disposable candidate passes all ten
native endpoint assertions; native DRC remains open at 880 violations / 499
inherited unconnected items. Root-native XML also proves canonical CM5 USB3
ownership, and all prior contradictory prose is now explicitly superseded.

2026-09-08: Re-ran the live dual-mode source checks. Schematic/library
authority, exact JMS583/selector/M-key pad counts, authoritative component
maps, selector truth table (SATA=0, NVMe=1), and mode contract all pass.
Native copper and DRC closure remain open.

2026-09-08: Added saved-copper USB3 metrics for FULL7. Source legs measure
149.160/145.160 mm RX N/P and 141.960/137.960 mm TX N/P, with three vias
each; local legs are also unequal. These remain diagnostic measurements, not
a skew, impedance, or DRC pass.

2026-09-08: Fresh native schematic ERC on the live source reports 927
violations, led by dangling M.2 labels and inherited off-grid/same-label
findings. The raw report is retained; endpoint and mode-audit passes do not
waive ERC. Removed six genuinely isolated legacy M.2 labels from the child
source; the post-fix ERC report no longer contains those dangling entries,
although the total remains 927 from independent inherited findings.

2026-09-08: Rejected source-launch relocation FULL10. Although all ten USB3
endpoints remained natively connected, inward vias introduced shorts to J1
12V pads and U11 ground; the trial is preserved as negative route evidence
and FULL7 remains the active basis.

2026-09-08: Rejected FULL11, a TX layer-transition attempt around the
CM5_PERST corridor. Native USB3 endpoints remained connected, but DRC rose
to 845 with additional local clearance/crossing findings; FULL7 remains the
active route basis.

2026-09-08: Rejected the U12 x=148 mm coherent translation trial. USB3
endpoint connectivity stayed 10/10, but native DRC reported 851 violations,
8 shorts, and 15 crossings. The trial remains negative placement evidence;
FULL7 remains active.

2026-09-08: Rejected the native-pad A* CM5-to-U12 source-router trial. It
passed 10/10 USB3 endpoint connectivity and reduced crossings to 6, but
native DRC reported 929 violations and 25 shorts. This is route evidence,
not a placement conclusion; FULL7 remains active.

2026-09-08: Rejected the U11 180-degree rotation trial. USB3 endpoint
connectivity stayed 10/10, but native DRC reported 843 violations, 7 shorts,
and 21 crossings. The trial remains negative placement evidence; FULL7 stays
active.

2026-09-08: Rejected TX source-launch relocation FULL14. Native USB3
connectivity remained 10/10, but inward columns produced 832 DRC violations,
5 shorts, and 19 crossings, including new J1/U11 collisions. FULL7 launch
columns were restored.

2026-09-08: Rejected the alternate CM5 source-layer USB3 trial. Endpoint
connectivity passed 10/10, but native DRC reported 851 violations, 4 shorts,
and 18 crossings. The all-B.Cu FULL7 source escape was restored.

2026-09-08: Rejected TX dogbone trials FULL12/FULL13. FULL12 reduced DRC to
830 but left a local TXN/RXP-via short; FULL13 produced four shorts at 832
violations. The generator was restored to the FULL7 geometry.

2026-09-08: Rejected the U12 180-degree rotation trial. Native USB3 endpoint
connectivity remained 10/10, but DRC rose to 845 with six shorts and 19
crossings. The rotation is preserved as negative placement evidence; FULL7
remains active.

2026-09-08: Added and ran the saved-board USB3 negative control. FULL7 passes
baseline native connectivity, and removal of one required CM5_USB3_RX_N track
causes the audit to fail as required. This confirms the audit derives from
actual KiCad connectivity rather than synthetic edges.

2026-09-08: Continued USB3 routing against the corrected source map. FULL7
passes all ten native endpoint assertions and reduces native DRC to 827
violations / 499 inherited opens; remaining local crossings and three
inherited J1 launch shorts keep routing open. FULL5/FULL6 are superseded.

2026-09-08: The complete JMS583 support/co-author cohort passed native
connectivity and a trace-removal negative control across reset, rails, LXO,
XAVDDH, crystal, and reset-delay branches. Native DRC remains non-clean from
donor/integration findings; this is a support-field basis, not closure.

2026-09-08: Corrected the dual-mode storage library audit to require the live
JMS583 package's 64 signal pads plus grounded exposed pad 65. The repaired
library, selector, and TE M-key checks pass; physical storage validation
remains open.

V10 pair-matching meander reduced USB TX skew proxy to 0.259 mm but introduced
two native same-layer pair self-crossings. Rejected the weave and retained the
V8 source-field basis.

Measured V8 against the VBUS parent: CM5-side USB3 paths and USB TX via count
are unchanged, while local USB TX skew proxy rises from 4.400 mm to 4.718 mm.
Retained V8 as a clean-source basis pending pair-length co-authoring.

V9 micro-adjustment was rejected after native DRC rose to 731 and introduced
a CM5_PET0_P/CM5_USB3_RX_N short. V8 remains the retained parent.

V8 USB3 native negative control also passed: removing a required CM5 USB3
trace broke the connectivity assertion as required. This confirms audit
sensitivity while Phase 24 remains open.

2026-09-08: Promoted the local VCCK corridor V1 as the current storage
workbench. It removes the VCCO/VCCK and RESET_N/VCCK short classes while
preserving USB3 10/10, SATA 12/12, mode 4/4, parity, JMS support, and rail
negative-control PASS. Native DRC is now 669 violations / 499 unconnected;
closure remains open.

2026-09-08: Tested selector-side SATA V10/V11 with separated upper TXN and
lower RXN corridors. The saved SATA endpoint audit passed, but the outboard
return field introduced M.2/mode/ground conflicts and raised native DRC to
670. Both are rejected; the VCCK-local V1 candidate remains current.

2026-09-08: Fresh native recheck of PHASE24_STORAGE_VCCK_LOCAL_V1 reproduced
669 violations / 499 unconnected items and zero shorting_items. USB3, SATA,
and mode-control native endpoint audits remained PASS; no DRC gate was waived.

2026-09-08: Rejected three native-label serialization probes. First-copy
deduplication produced 19 parity mismatches; final-copy deduplication changed
the five-mismatch identities without closing parity; full block reauthoring
produced 77 mismatches by losing legacy symbol-frame attachment semantics.
All probes were reverted. Further repair requires a native KiCad-authored
association fixture rather than additional label/duplicate guesses.

2026-09-08: Regenerated the disposable storage placement from the complete
M-key contact map and SATA coupling ownership. Native schematic-to-PCB pad
parity improved from 65 to 32 actionable mismatches; intentional M-key
contacts 59--66 remain absent, and all other mismatches stay open for source
repair.

2026-09-08: Corrected the storage parity scope for the intentional TE M-key
gap and non-board X7 contract marker, then regenerated complete U12/U13/U14
support metadata. Native parity improved to five real mismatches. A bounded
coordinate/UUID repair trial was rejected after native export produced broad
unconnected-net regressions; STORAGE.kicad_sch was restored to the checkpoint.
The five JMS support-label ownership anomalies remain open and fail-closed.

2026-09-08: Rejected the exact-UUID JMS support-label remap trial. Native
parity regressed from five to eight mismatches, including new JMS rail and
crystal ownership errors. The source was restored; label renaming alone is
not an acceptable repair, and the five-mismatch native association defect
remains open.

2026-09-08: Documentation hygiene checkpoint for Phase 24 dual-mode storage.
Reconciled the current implementation and status documents: Path A remains
active, the JMS583 support network is instantiated, and the live native pad
parity gate is five source-authority mismatches. Marked the older 65-to-32
count as superseded history and retained the rejected coordinate/UUID trial
as evidence. Focused native schematic, mode-contract, and library audits pass;
full storage routing and release validation remain open.

2026-09-08: Rejected the first combined JMS583 support/crystal cohort. The
isolated production-width XIN/XOUT route conflicts with the retained XAVDDH
diagonal when integrated, producing authored B.Cu crossings and an XOUT to
XAVDDH short. This is route-allocation evidence; the crystal and support
architecture remain unchanged.

2026-09-08: Published the previously untracked JMS583 crystal DRC receipts
for divergent, split-layer, pad-width, and net-name experiments. They remain
immutable historical route evidence; the production-width discriminator is
the current retained basis.

2026-09-08: Rejected the JMS583 left-side crystal relocation because the
restored XOUT QFN dogbone still shorts the retained XAVDDH transition. The
result is preserved as route-allocation evidence; the next trial must
co-author those two native source fields.

2026-09-08: The JMS583 three-exit co-author passes native XIN, XOUT, and
XAVDDH endpoint connectivity plus trace-removal negative control. Native DRC
is 522 violations / 499 inherited opens with no authored shorting class; it
is retained as the strongest analog/crystal support-field basis, not closure.

2026-09-08: Rejected the follow-up JMS583 left-corridor source regeneration.
It removed the XIN/XOUT crossing and XAVDDH corridor crossings, but the
adjacent QFN exits still produced one XOUT-to-XAVDDH short. The next trial
must co-allocate all three bottom-edge analog/crystal exits before transition.

2026-09-08: Retained a JMS583 crystal production-width discriminator using
0.20 mm traces and ordinary 0.50/0.30 mm through-vias. Native XIN/XOUT
connectivity and the trace-removal negative control pass; DRC remains 519
violations / 499 inherited donor opens, so no closure was claimed.

2026-09-08: Added `phase24_jms583_ground_return_audit.py`. It derives JMS583
support-ground connectivity from native pads, tracks, vias, and filled zones,
and passes a destructive-copy negative control after local ground copper is
removed. The JMS583 support cohort remains open because the saved candidate
still carries inherited donor DRC/open findings.

2026-09-08: Re-ran the JMS583 XIN/XOUT crystal fixture from the saved native
board. Both endpoints and the trace-removal negative control passed; native
DRC remained 519 violations / 499 inherited unconnected items. The fixture
was checkpointed as route evidence only, with no Phase 24 closure claim.

2026-09-08: Validated the first JMS583 ground-return access template. Ordinary
through-vias at C80.2 and U11.63, with native F.Cu pad escapes and refilled
POWER_GND zones, connect C80 ground to the JMS583 ground domain in saved
KiCad connectivity. Focused DRC is 520 violations / 499 inherited donor
unconnected items; no new JMS support short class was introduced.

2026-09-08: Expanded the JMS583 native support cohort to eight nets by adding
U11.20 JMS_AVDDL to C83.1 through a mixed-layer ordinary-via corridor. The
native endpoint audit and combined trace-removal negative control pass; V14
has 819 violations / 499 unconnected items, with no authored AVDDL
short/crossing but recurring plane-clearance findings still open.

2026-09-08: Corrected the JMS583 reset-delay cohort branch. The first branch
left R81.1 through adjacent R81.2 and was rejected; V16 exits the free side
of R81 and reaches C85.1. Native eight-net endpoint connectivity and the
combined trace-removal negative control pass. DRC remains 819 violations /
499 inherited unconnected items; no validation rule was relaxed.

2026-09-08: Corrected the JMS583 full ground-stitch trial by removing an
invalid R81.2-to-POWER_GND stitch and moving the AVDDL B.Cu leg clear of the
C80 return via. Native refilled connectivity shows all local JMS583 support
ground pads join U11.63. The saved filled V2 report is 520 violations / 499
inherited donor opens, with no authored JMS support short/crossing class.

2026-09-08: Fixed the JMS583 structural support audit to resolve relative
schematic inputs from its repository directory. The audit now passes from
the repository root against STORAGE.kicad_sch, covering required support
instances, values, and support-net labels.

2026-09-08: Rejected the JMS REXT two-via corridor V1. Native DRC found the
lower transition in the C90/R33 support field and plane-clearance findings on
the ordinary through-vias. It remains disposable route evidence only; the
JMS583 support gate and active routing rules remain unchanged.

2026-09-08: Rejected JMS REXT via-corridor V2. The orthogonal QFN departure
removed the earlier source-pad cut, but the long B.Cu leg crossed the
inherited V100 PCIe corridor and the F.Cu return crossed LXO/C93 support
geometry. Native DRC reported 823 violations / 499 unconnected items; no
production route or rule was promoted.

2026-09-08: Refilled the retained JMS583 support cohort with KiCad's native
zone filler and preserved the result as `PHASE24_JMS583_SUPPORT_COHORT_FILLED`.
Native DRC dropped to 519 violations while the 499 inherited donor
unconnected items remained. The filled result is stronger via evidence, not
Phase 24 closure.

2026-09-08: Corrected the reusable JMS583 support-symbol authoring path to
emit canonical `JMS_REXT`, `LXO`, `XIN`, and `XOUT` labels in the native KiCad
serialization order. Native re-export reduced storage parity to two remaining
items (`R80.1` and `U11.39` resolving as `JMS_GPIO7_NC`). Targeted duplicate-
label cleanup and restoration probes were rejected after changing U12/U13
ownership; no PCB alias repair or validation waiver was promoted.

2026-09-08: Updated the JMS583 structural support audit to the live canonical
clock-net names and verified its removed-R80 negative control. A fresh native
support-routing trial was rejected at 834 DRC violations / 499 inherited
opens with authored support crossings; it remains disposable evidence.

2026-09-08: Made the JMS583 support-label migration idempotent when the
canonical corrected atoms are already present. Native re-export remains at
the two-item R80.1/U11.39 association defect; U11-only, old-block, UUID, and
endpoint serialization probes were rejected when they changed unrelated
ownership or increased mismatches.

2026-09-08: Rejected the correctly physically scoped U11-only label reauthor
probe. Native export produced 20 mismatches, including unrelated
`JMS_AVDDL`/`BRIDGE_USB_VBUS` ownership changes; the live source was restored
to the stable two-item JMS_REXT association defect.

2026-09-08: Reconciled 203 duplicate generated schematic-label UUIDs while
preserving every label atom. The bridge schematic backend now loads the live
source; native parity remains at the two R80.1/U11.39 association mismatches.
This closes duplicate-UUID validity as a structural issue but not the native
association mapping.

2026-09-08: Corrected the local USB3 router to default to the saved FULL7
native authority rather than the stale canonical placement export. The stale
base failed native bridge-side TX endpoint connectivity due to U12.24/U12.25
USB_TXN1/P ownership; no PCB-only net repair was used. The FULL7-based
disposable route passes all ten endpoint assertions and records 830 DRC
violations / 499 unconnected items, remaining open routing evidence.
The saved-board negative control passes on that candidate: removing a required
CM5_USB3_RX_N track breaks native endpoint connectivity as required.

2026-09-08: Reconciled Phase 24 narrative status against the live dual-mode
storage implementation. Current sections now identify Path A as active, record
the current 857-violation placement baseline and 927-violation post-fix ERC,
and explicitly state that the JMS583 support network is already instantiated.
The pre-label-fix 205-violation ERC and earlier 797-violation placement result
are marked as superseded historical snapshots; raw reports and rejected
experiments were not modified.

2026-09-08: Rejected the first composite of the corrected FULL7 USB3 basis
with the JMS583 support cohort. Support endpoint and trace-removal audits
passed, but native DRC found 870 violations / 499 unconnected items and new
local support-placement conflicts, including a JMS_USB3_TXN/USB_RXP1 short.
The composite is preserved as rejected evidence; support placement must be
co-authored around the USB3 field.

2026-09-08: Rejected the north-side JMS583 support co-author. Native support
endpoint and negative-control audits passed, but DRC found 924 violations /
499 unconnected items plus new support-to-USB, crystal/rail, and return-via
conflicts. The placement-only translation is preserved as evidence; the next
pass requires joint obstacle-aware allocation with the USB3 field.

2026-09-08: Rejected the native-pad A* JMS583 support allocator after fixing
its global-endpoint omission. Native DRC still found 1,013 violations and
multiple real shorts because its bounded 2 mm terminal halo admitted routes
through neighboring QFN fields. This is router-model evidence only; the next
pass requires per-pad legal escape corridors.

2026-09-08: Rejected direct transplantation of the verified JMS583 support
primitive onto the FULL7 USB3 source basis. Native support endpoint and
negative-control audits passed, but integrated DRC reported 917 violations,
including a real JMS_XAVDDH/CM5_USB3_TX_N collision and local XIN/XOUT
via-clearance. Retained the primitive as isolated evidence; QFN exits must be
regenerated in-place around USB3 copper.

2026-09-08: Tested the focused XIN/XOUT/XAVDDH transplant onto FULL7. Native
endpoint and XIN-removal negative-control checks passed, but integrated DRC
rejected it at 851 violations / 499 unconnected items with a real
JMS_XAVDDH/CM5_USB3_TX_N collision. The remaining work is an in-place
XAVDDH escape repair; the candidate is preserved as rejected evidence.

2026-09-08: Ran native per-net JMS583 support trials against the promoted
FULL7/XAVDDH basis. Every direct-join trial introduced native shorts and/or
crossings; VCCO/VCCK failed closed because the helper has no mappings. Saved
the complete allocation matrix and raw reports; direct joins are rejected as
an implementation class.

2026-09-08: Promoted the in-place left/up XAVDDH repair as the current
support/USB3 integration basis. Native XIN/XOUT/XAVDDH and USB3 endpoint
audits pass, including the XIN-removal negative control. Native DRC reports
853 violations / 499 inherited unconnected items with no authored shorts or
track crossings; full Phase 24 closure remains open.

2026-09-08: Recorded the validated lateral JMS_REXT addition on the current
FULL7/XAVDDH basis. Native REXT, three-exit, and USB3 endpoint audits pass
with trace-removal controls; native DRC remains 853 violations / 499 inherited
unconnected items and no authored shorting/crossing class. Full support and
Phase 24 closure remain open.

2026-09-08: Promoted the west/north native-pad-aware JMS_RESET_N repair onto
the current REXT/XAVDDH/USB3 basis. U11.15-to-R81.1-to-C85.1 connectivity and
the trace-removal negative control passed. Native DRC remains 863 violations /
499 inherited unconnected items with no authored shorts or crossings; support
rails and full storage closure remain open.

2026-09-08: Promoted the upper native-pad-aware JMS_AVDD33 repair onto the
current REXT/RESET_N/XAVDDH/USB3 basis. U11.19-to-C80.1 connectivity and the
trace-removal negative control passed. Native DRC remains 876 violations /
499 inherited unconnected items with no authored shorts or crossings; other
support rails and full storage closure remain open.

2026-09-08: Promoted the native all-F.Cu JMS_VCCK repair onto the current
support/USB3 basis as PHASE24_DUAL_MODE_STORAGE_FULL7_VCCK_F_center. Native
U11.2-to-C82.1 connectivity and the trace-removal negative control passed.
Native DRC reports 877 violations / 499 inherited unconnected items with no
new VCCK short or crossing relative to the AVDD33 parent. Remaining support,
mode-control, storage-routing, and Phase 24 closure gates remain open.

2026-09-08: Native support inventory on the VCCK basis confirms REXT, XIN,
XOUT, RESET_N, AVDD33, and VCCK connected; AVDDL, VCCO, VDDREG_5V, and LXO
remain open. The first AVDDL all-F.Cu and east-via corridors were rejected by
native DRC for shorts into existing USB3/PCIe geometry. Inventory and rejected
route evidence are preserved; no validation severity was changed.

2026-09-08: Promoted the rectangular local F.Cu JMS_VCCO power-copper zone
as PHASE24_DUAL_MODE_STORAGE_FULL7_VCCO_rectangle_zone. Native U11.6-to-C81.1
connectivity and the zone-removal negative control passed. Native DRC reports
514 findings with no VCCO-authored short/crossing class; inherited shorts and
crossings remain open. This is power copper only and does not relax the
no-signal-on-plane policy.

2026-09-08: Re-ran the independent dual-mode source/library audit. Mode
contract, schematic instances and labels, JMS583 64+EP numbering, both
selector 42+EP footprints, and TE M-key contact/key-gap geometry all passed.
This receipt does not waive the open VBUS, parity, routing, ERC, or DRC gates.

2026-09-08: Promoted the local F.Cu JMS_VDDREG_5V power-copper zone as
PHASE24_DUAL_MODE_STORAGE_FULL7_VDDREG_local_zone. Native U11.1-to-L10.2
connectivity and the zone-removal negative control passed using the
zone-aware audit. Native DRC remains 514 findings with no VDDREG-authored
short/crossing class; remaining rails and Phase 24 closure remain open.

2026-09-08: Promoted the shared-inductor LXO dogleg on the VDDREG/VCCO basis
as PHASE24_DUAL_MODE_STORAGE_FULL7_LXO_below_vddreg. Native U11.64-to-L10.1
connectivity and the trace-removal negative control passed. Native DRC remains
514 findings with no LXO-authored short/crossing class; AVDDL and higher-level
storage/Phase 24 gates remain open.

2026-09-08: Closed the JMS583 support connectivity primitive on
PHASE24_DUAL_MODE_STORAGE_FULL7_AVDDL_local_zone. Native connectivity passed
for all ten support nets, including zone-mediated AVDDL/VDDREG paths, and the
combined negative control removed all support tracks and zones and failed as
required. Native DRC remains 514 inherited findings; full storage and Phase
24 closure remain open.

2026-09-08: Saved the complete ten-net JMS583 support receipt
PHASE24_DUAL_MODE_STORAGE_FULL7_AVDDL_local_zone-support-audit.rpt and its
combined track/zone-removal negative-control PCB. Both native checks pass in
the positive/negative directions; integrated VBUS, parity, routing, ERC, and
full DRC gates remain open.

2026-09-08: Independent parity audit of the current AVDDL support-route
candidate reports 111 expected-pad mismatches, including M.2, Ethernet,
service, mode-control, power, and support-passive ownership. The candidate
remains disposable routing evidence; no mismatch was waived or repaired on
the PCB side.

2026-09-08: RX_N/J1 launch discriminator V3 was preserved as rejected route
evidence. The around-J1 launch removes the earlier RX_N-to-J1 short and passes
native VBUS, complete JMS583-support, USB3 endpoint, and trace-removal
negative-control audits, but native DRC still reports 509 findings / 499
inherited unconnected items and an RX_N/refclk crossing. No production CAD or
Path-B qualification was changed.

2026-09-08: RX_N launch V4 was preserved as rejected evidence. The upper-J1
B.Cu dogleg passes VBUS and USB3 endpoint audits but creates real RX_N/TX_N
shorting/crossing classes in native DRC (512 findings / 499 inherited opens).
The route was not promoted and validation rules were unchanged.

2026-09-08: Corrected the authoritative U12.24/U12.25 instance labels in
STORAGE.kicad_sch from stale USB_TXN/P1 names to JMS_USB3_TXN/P. Fresh native
export, regenerated storage placement, and mode audit pass with zero
expected-pad mismatches. The prior 64/111 mismatch results are superseded
historical probes; no PCB-only ownership repair was used. Copper, ERC, DRC,
and full Phase 24 closure remain open.

2026-09-08: Reran the isolated RTL9210B Path-B evidence suite. Authority,
corroborating support, M-key mapping, native netlist, WIP-conflict, and PDF
 pin audits passed; both native-netlist and PDF negative controls failed as
 intended. Path B remains isolated with support-field, provisioning, firmware
 provenance, and hardware validation gates open; Path A and production CAD are
 unchanged.

2026-09-08: Corrected a live Phase 24 U13 source-authority regression. The
HD3SS3412 selector pins 6/7 had been overwritten with unused M.2 PCIe lane-1
labels, orphaning the shared SATA lane-0 RX contacts. The authoring map and
live STORAGE instance labels now match the M.2 authority; native export and
PCB pad parity pass with zero mismatches. The SATA corridor author was also
made native-pad anchored instead of coordinate-frozen. Disposable
PHASE24_DUAL_MODE_STORAGE_U13FIX_SATA_V2 passes all 12 SATA endpoint checks
and its trace-removal negative control; native DRC remains open at 734
violations / 499 unconnected items, so Phase 24 is not closed.

2026-09-08: Promoted reviewed JMS583 AVDDL/VCCO/VDDREG support zones and the
VCCK landing onto the corrected storage parent. AVDDL and complete support
negative controls pass. The final combined USB3/SATA workbench passes the
ten-net USB3 audit and all 12 SATA endpoint checks. Native DRC remains open at
669 violations / 499 unconnected items with inherited crossings/shorts; no
Phase 24 closure was claimed.

2026-09-08: Closed a live mode-detector net-ownership defect at the source
boundary. M.2 contact 69 and the J5 AUTO leg now share native `AUTO_PEDET`
ownership; the regenerated mode-fix placement has zero schematic-to-PCB pad
parity mismatches and the mode-contract audit passes. The mode-aware native
fixture and inactive-state validation remain open; no automatic-mode closure
was claimed.

2026-09-08: Corrected common mode-control ownership at the schematic source
boundary. U12.9, U13.9, and U14.4 now share `STORAGE_SEL`; J3.69 and J5.2
share `AUTO_PEDET`. Native export, mode audit, and regenerated placement
parity pass. The physical mode fixture connects the three control paths, but
its first direct F.Cu geometry has a J5 local DRC short and remains open.

2026-09-08: Focused storage endpoint gates are now current PASS evidence:
JMS583 support, ten-net USB3, and 12-net SATA selector connectivity each
pass with negative controls where implemented. Updated the live open-gate
narrative so USB3/SATA endpoint work is no longer phrased as an unfinished
TODO. Native DRC remains open at 669 violations / 499 unconnected items.

2026-09-08: Added `phase24_mode_control_native_connectivity_audit.py`, which
derives mode-control connectivity exclusively from KiCad's saved PCB graph.
The V5 disposable fixture passes four asserted endpoint groups and its
negative control fails after removing a required MODE_IN track. V3-V5 local
mode-route variants remain rejected route evidence because native DRC still
finds mode-route crossings/shorts and inherited fixture violations; no mode
or Phase 24 closure was claimed.
2026-09-08: Marked the duplicate mid-file Phase 24 status snapshot as
superseded historical text so only the authoritative top current-state/open
gates can govern execution. No raw reports or rejected experiments were
rewritten.

2026-09-08: Reconciled the implementation narrative's active workbench name
and gate counts with the live zone-backed integrated storage workbench. Older
pre-zone USB3-incomplete wording remains historical evidence; no raw report
or rejected candidate was changed.

2026-09-08: Ran a bounded integrated JMS_REXT repair discriminator. The
ordinary-via V1 escape removed the original AVDDL/REXT adjacency but created
new QFN-ground/power conflicts; the no-via V2 perimeter escape retained the
original DRC count and still contacted the POWER_GND field. Both remain
rejected route evidence and the zone-backed integrated baseline is unchanged.

2026-09-08: Corrected the embedded storage symbol definitions for the live
AUTO_PEDET and STORAGE_SEL authorities, not just their instance labels. A
fresh native XML export and regenerated placement now pass pad-net parity with
zero mismatches. Rebuilt USB3, SATA, and JMS583 support on that placement; all
focused endpoint audits and negative control pass. Promoted the resulting
681-violation workbench as the active routing basis; prior 669-count copper
remains historical because its PCB ownership was stale.

2026-09-08: Tested the first native-pad-aware integrated U13-to-J3 launch
replacement. V1/V2 reduced aggregate DRC but introduced true M.2 socket-ground
collisions and B.Cu TX pair/via conflicts. Both are rejected route evidence;
the source-authoritative support workbench remains active and no launch
copper was promoted.

2026-09-08: Tested M.2 launch V3/V4 with staggered connector and source-via
escapes. V3 removed the connector-ground collision but retained a U13 source
pair short; V4 crossed adjacent U13 pads. Both are rejected route evidence;
the source-authoritative support workbench remains active.

2026-09-08: Corrected the selector-side SATA escape authoring. C30--C33 pad 1
are F.Cu-only, so a B.Cu segment beginning at those pads was not native
connectivity; the repaired author adds an actual capacitor-side through-via
before the B.Cu corridor. Selector escape V3 and V4 pass all 12 saved-board
SATA endpoint assertions. V4 still has inherited USB3/support shorts and
crossings, so no Phase 24 closure or copper promotion was claimed.

2026-09-08: A further selector-side V5 corridor trial was rejected after
native SATA endpoint PASS because its multi-bend B.Cu allocation introduced
additional same-layer crossings and via/track conflicts. It is retained as
negative routing evidence; the V4 authoring basis remains the latest cleaner
candidate.

2026-09-08: Integrated selector-side SATA escape V4 with M.2 launch V6 and
native mode-control routing. The saved candidate passes topology-aware USB3
10/10, SATA 12/12, mode-control 4/4, schematic-to-PCB parity with zero
mismatches, JMS VDDREG/REXT, and the mode negative control. Native DRC remains
open at 673 violations / 499 unconnected items; no closure was claimed.

2026-09-08: Tested integrated JMS_VCCO source-transition relocations V6/V7.
V6 removed the C86/USB launch collision but retained the VCCO/VCCK field
conflict; V7 moved the source transition and increased DRC to 677 while the
same short remained. Both are rejected support-route evidence; V4_MODE stays
the current integrated basis.

2026-09-08: Tested VCCO/VCCK support-route V8 with a north F.Cu VCCK
corridor. It retained native VCCO endpoint and negative-control PASS but
introduced CM5_5V/JMS_PCIE_TXP0 conflicts and raised DRC to 680. Rejected;
the integrated V4_MODE basis is unchanged.

2026-09-08: Tested an all-F.Cu JMS_VCCO support route from the integrated
USB3-repaired basis. It retained the VCCO native endpoint proof and reduced
the aggregate DRC to 670, but introduced real U12 no-net/USB launch shorts and
additional crossings. Rejected; VCCO_DEST_V1 remains the current basis.

2026-09-08: Tested VCCO destination V2 with the source transition moved to
134.5,136.0 mm. Native VCCO proof remained valid, but the route shorted the
adjacent JMS_SPI_CS_N_DNP pad and raised DRC to 675. Rejected; VCCO_DEST_V1
remains the current basis.

2026-09-08: Tested selector-side SATA escape V9 with a north TXP corridor.
It passed the native SATA endpoint audit and removed the prior TXP/USB_RXN1
collision, but introduced XIN, CM5_USB3, and support conflicts and raised
native DRC to 677. Rejected; V4_MODE remains the integrated basis.

2026-09-08: Promoted the best integrated storage workbench to
PHASE24_STORAGE_VCCO_DEST_V1 for continued routing. It combines the corrected
CM5 USB3 right-side launch and selector-side SATA V4 with M.2 V6, mode control,
and destination-only VCCO relocation. USB3/SATA/mode/parity/VCCO focused
audits pass; native DRC is 671 violations / 499 unconnected items, so closure
remains open.

2026-09-08: Reconciled the active dual-mode storage implementation gate to
the live VCCO_DEST_V1 DRC count of 671 violations / 499 unconnected items;
older 673-count references remain historical evidence only.
2026-09-08: Tested an outboard F.Cu JMS_USB3_TXP/TXN fanout around U12. The
dual-mode USB3 endpoint audit passed, but native DRC exposed multiple U12
no-net/USB/M.2 shorts; the 664 aggregate count was not an improvement in
electrical quality. Rejected; VCCK_LOCAL_V1 remains the current basis.

2026-09-08: Tested USB3 skew-tune V1. RX proxy skew improved to 2.123 mm and
TX proxy skew to 2.400 mm, but the added meanders entered JMS support and
selector-via fields and created real shorts/crossings. Rejected; support-via
reservation is required before another tuning pass.

2026-09-08: Tested selector SATA RXN compact-jog V12. It passed native SATA
with zero shorting_items and reduced selector RX pair mismatch from 31.46 mm
to 13.53 mm. V13's added upper-field meander entered M2/USB support corridors
and created shorts; V13 rejected, V12 retained as disposable evidence.

2026-09-08: Tested SATA RXN balance V14. It achieved 99.70 mm RXP versus
103.37 mm RXN (3.66 mm mismatch) with native SATA endpoint PASS, but
reintroduced two TUSB/USB-RX transition-via shorts. Rejected; the no-short
VCCK_LOCAL basis remains current.

2026-09-08: Tested USB RX endpoint-via relocation V1/V2 around the V14 SATA
geometry. USB and SATA endpoint audits passed, but U12 pad-43 and USB-RX
pair shorts remained or appeared, with V2 at 681 native violations. Both
rejected; VCCK_LOCAL_V1 remains current.

2026-09-08: Reconciled stale Phase 24 narrative references to V4_MODE and the
old selector-to-M.2 next action. The authoritative current basis is
VCCK_LOCAL_V1; superseded prose remains historical and no raw evidence was
rewritten.

2026-09-08: Tested the native-pad-aware SATA source-order probe
PHASE24_STORAGE_SATA_SOURCE_ORDER_V1. The corrected author uses separate
bridge-side and selector-side nets and passes all 12 native SATA endpoint
assertions, but the reordered coupling row creates real storage-field
shorts/clearances (612 DRC violations, 499 unconnected items). Rejected as
route implementation evidence; VCCK_LOCAL_V1 remains the no-short basis.

2026-09-08: Corrected the SATA A* obstacle model to respect SMD pad layer
sets, then generated PHASE24_STORAGE_SATA_ASTAR_V1. All 12 SATA native
endpoint assertions passed, but native DRC found 822 violations with real
SATA-to-power/support shorts and crossings. Rejected; the layer-aware search
author remains reusable and no copper was promoted.

2026-09-08: Tested SATA post-escape corridor V1, preserving the validated U7
dogbones while changing only B.Cu lanes. Native SATA endpoint assertions
passed and aggregate DRC fell to 583, but three true shorts appeared,
including TUSB SATA into the JMS_REXT/USB3 field. Rejected; no copper was
promoted.

2026-09-08: Tested the minimal TXN-via-spacing SATA trial. Native SATA
connectivity passed 12/12 and DRC fell to 575, but a true TXP/TXN short
appeared at the U7 source escape. Rejected; the next attempt must change the
local escape topology or move the coherent U7/coupler sub-island.

2026-09-08: Re-ran native KiCad DRC on the active
PHASE24_STORAGE_VCCK_LOCAL_V1 basis. The saved-board baseline reproduces 669
violations and 499 unconnected items with zero shorting_items; this fresh
receipt does not waive any open gate.

2026-09-08: Tested 51 ordinary offset J7 ground-return vias. The probe was
rejected because J7 pads are native /CORE_CM5/POWER_GND while the plane is
POWER_GND; PCB-only flattened-net vias did not reduce the 499 opens and added
DRC findings. No net merge or copper was promoted.

2026-09-08: Tested endpoint-safe layer-aware SATA search V2 with existing
selector-side copper retained. Native SATA passed 12/12 and storage-local
true shorts were avoided, but a U7 source-field crossing remained; native
DRC was 676 violations / 499 unconnected with one inherited non-storage
short. Rejected as full-board candidate; method retained.

2026-09-08: Reauthored the coherent storage-island transplant against live
Path-A capacitor net ownership. Native SATA failed at TUSB_SATA_RXP because
the historical socket-side template missed current U13 geometry; native DRC
was 802 violations / 499 unconnected with crossings and shorts. Rejected;
no copper was promoted.
## 2026-09-08 — Phase 24 CM5 ground authority repair

- `CORE_CM5.kicad_sch` was corrected generically by promoting its 51 local
  `POWER_GND` labels to native global labels. Native KiCad export now produces
  one `POWER_GND` net with 154 nodes, including J7 CM5 ground contacts, and
  the ERC comparison retains the prior warning set with no hierarchy errors.
- Added the disposable source-authority/PCB-reconciliation harness
  `phase24_validate_cm5_ground_flattening.py` and a saved candidate/report;
  the PCB-side remap is evidence only and is not production authority.
- Added an opt-in saved-position mode to `phase14_materialize_pcb.py` so
  source/netlist regeneration can be tested against an integrated placement
  without weakening the normal deterministic-placement gate.
- Current gate remains open: regenerate the active routed storage workbench
  from the corrected schematic and rerun native connectivity/DRC.
- The saved-position materializer now resolves existing donor footprints by
  reference directly; its disposable regeneration correctly stops on the
  genuinely absent current-candidate support refs instead of silently
  inventing placement. This keeps the stale/incomplete candidate distinction
  explicit for the next source-authority rebuild.
- Remote `reva-clean` had already published the preceding checkpoint while
  this local amendment was prepared; the histories were reconciled with a
  non-destructive merge preserving both the published source repair and this
  local materializer hardening.
- Added `phase24_regenerate_board_from_netlist.py`, a generic source-driven
  PCB pad/copper ownership regenerator. Its V2 disposable candidate passes
  parity, dual-mode USB3, SATA, and JMS583 support audits, but native DRC
  exposes 7 true shorting items after inherited hierarchical copper is
  normalized without rerouting. V2 is rejected route evidence; affected
  corridors require clean rerouting before promotion.
- V3 extended the regenerator's normalization to inherited pads as well as
  tracks/zones, reducing hierarchy-induced alias shorts to one real USB3
  source-field pair short while retaining zero pad-parity mismatches and
  passing SATA/USB3 endpoint audits. V3 remains rejected pending a clean
  reroute of that transformed CM5 USB3 launch.
- A disposable obstacle-aware J7-to-U12 A* launch trial was rejected after
  native DRC exposed disconnected pad escapes and multiple pad-field shorts;
  the invalid via/pad model was retained only as negative routing evidence.
- The explicit-dogbone follow-up passed native USB3 endpoint connectivity but
  still shorted adjacent CM5 source-field pads/vias under native DRC; it was
  rejected and the CM5IO-derived escape geometry remains the next basis.
- FULL7 CM5 USB3 source geometry was transplanted as a bounded experiment. It
  passed the native USB3 endpoint audit but introduced incompatible donor
  connector/cross-net DRC shorts; it was rejected as copper and retained only
  as topology evidence.
- A shifted CM5IO-style escape below the SXM2 body was tested and rejected:
  it passed USB3 endpoint connectivity but crossed existing REFCLK/XIN/XOUT
  and SATA corridors under native DRC. The remaining repair is corridor
  allocation around those validated neighboring paths.

2026-09-08 — Phase 24 source-authority checkpoint: corrected the HD3SS6126
U12 exposed-pad defect generically. The QFN pad 43 is now an explicit
schematic `POWER_GND` pin with a matching instance pin and source-generator
mapping; native KiCad export places U12.43 on `POWER_GND`. The fresh V5
source-regenerated PCB passes schematic-to-pad parity, dual-mode USB3, SATA,
and JMS583 support audits with negative control. Native DRC remains open at
685 violations / 403 unconnected items, so this is corrected routing basis
  evidence, not Phase 24 closure. Next work is a clean U12 source-field escape.

2026-09-08 — Follow-up route trials used the corrected U12 exposed-pad
authority. Moving RX_N's ordinary target via outside the grounded thermal pad
removed the former pad short, but trial 3 still interacted with XOUT and
trial 4's B.Cu dogleg introduced an inherited USB3/SATA crossing. Both pass
the topology-aware USB3 endpoint audit but are rejected route evidence; the
next solution class must allocate a different local source/target corridor.

2026-09-08 — The V5 all-four-net layer-aware A* USB3 trial was rejected after
native endpoint connectivity passed but native DRC reported 841 violations and
16 true shorts. Its clearance model is unsuitable for the inherited dense
corridor; the experiment does not invalidate the corrected source authority.

2026-09-08 — Native source inspection resolved the apparent clock mismatch:
U11 XIN/XOUT are already authoritative to the live Y10 crystal. Y1 is a
superseded separately aliased island and was not joined in parallel. The
reconciled native export and regenerated board return to the 685/403 baseline,
 confirming the remaining defect is routing around U12 and neighboring copper.

2026-09-08 — A coordinated Y10 local-crystal relocation trial preserved the
USB3 endpoint audit but worsened native DRC to 695 violations with five true
shorts. It was rejected; the live clock source remains U11 XIN/XOUT to Y10,
and further work must use a net-aware escape method.

2026-09-08 — The U12 RX pair was re-escaped outside the HD3SS6126 exposed-pad
field in disposable `PHASE24_STORAGE_U12_EP_RX_PAIR_V6`. Native USB3
connectivity passed 10/10, SATA passed 12/12, JMS583 support passed, and
schematic-to-PCB pad parity passed with zero mismatches. Native DRC improved
to 684 violations / 403 unconnected items with no `shorting_items`. The
candidate is retained as the current route basis; mode-control connectivity
and the remaining full-board closure gates remain open.

2026-09-08 — Native mode audit found a real duplicate-reference authority
defect: storage override J5 collided with the power-input J5, so the saved
candidate carried the wrong footprint at that reference. The storage source
symbol was corrected to J8, and native export `PHASE24_STORAGE_MODE_J8.kicadxml`
proves J3.69/J8.2 are AUTO_PEDET. The next board regeneration must instantiate
J8; no PCB-only relabel is accepted.

2026-09-08 — Source-owned J8 mode-jumper materialization restored the native
mode graph (4/4 plus trace-removal negative control), but V1 overlapped
power-input J5 and V2 introduced native mode/selector and inherited
U12/connector short classes. No route was promoted; V6 remains the clean
USB3 RX-escape basis and J8 regeneration stays open.

2026-09-08 — Source-driven J8 regeneration proved the corrected four-net
footprint and native mode graph (4/4), but V1/V2 were rejected as copper
implementations: inherited old-J5 routing and stale U12 pad-field/AUTO_PEDET
collision classes remained. The source reference correction stands; the next
attempt must co-author the affected U12 escape geometry instead of blaming J8.

2026-09-08 — Coordinated source-regenerated J8 candidate V5 repaired the
complete U12 CM5 USB3 quartet. Native USB3 10/10, SATA 12/12, JMS583 support
plus negative control, mode control 4/4, and pad parity zero mismatches all
pass. Native DRC reports 708 violations / 403 unconnected items with zero
shorting classes. It is the current routing basis, not Phase 24 closure; open
clearance/crossing/unconnected and full-board gates remain.

2026-09-08 — VBUS/sense support was repaired on
`PHASE24_STORAGE_J8_V5_VBUS_V1`: native VBUS connectivity and trace-removal
negative control pass, as do USB3, SATA, mode, and JMS583 support audits.
Native DRC reports 732 violations / 400 unconnected items with zero true
shorts. This is the current storage basis; remaining DRC and full-board gates
stay open.

## 2026-09-09 — Phase 24 source-field discriminator

Preserved V3/V4 disposable co-authored USB TX-pair plus JMS_AVDDL trials.
V3 passed focused connectivity with no shorting class but introduced two
local source-escape crossings; V4 was worse at 734 native DRC findings.
Rejected both as route implementations and retained the VBUS V1 parent.

## 2026-09-09 — Phase 24 narrative authority correction

Relabeled older status sections that still called pre-VBUS/pre-J8 snapshots
the current routing basis. The live narrative authority remains the VBUS V1
parent; historical receipts and rejected experiments were not altered.

## 2026-09-09 — Phase 24 lower-field continuation

Tested straight 0.20 mm TX-pair V5 and south-shifted AVDDL V6. V5 retained
focused connectivity but shorted TXP to the AVDDL via; V6 added TXP/AVDDL and
RXP/AVDDL shorts. Rejected both and retained the VBUS V1 parent. The next
route must co-author the complete U11 lower pad field.

## 2026-09-09 — Phase 24 TX capacitor relocation trial

Preserved the C86/C87 coherent relocation V1 experiment. Focused endpoint
audits passed, but native DRC reported 760 findings and real bridge-TXP/AVDD33
and TXN/TXP shorts. Rejected the relocation-only class; retained the VBUS V1
parent.
## 2026-09-08 — Phase 24 documentation hygiene

Reconciled the current Phase 24 status and dual-mode storage implementation
narratives with the live J8/VBUS basis and native focused audit evidence.
Marked obsolete JMS583-instantiation, pre-J8, stale-parity, malformed-library,
and superseded-route language as historical/superseded without modifying raw
receipts or rejected experiments. Remaining work is native DRC/routing-quality
and full-board closure; the next bounded route class is the co-authored
USB_TXP/USB_TXN/JMS_AVDDL source field.

## 2026-09-09 — Phase 24 JMS583 rotation discriminator

Tested a coherent 180-degree U11/C86/C87 TX-island placement. It produced
805 native DRC findings, multiple QFN/support shorts, and disconnected RX
endpoints because the full island was not regenerated. Rejected the placement
implementation and retained the VBUS V1 parent.

## 2026-09-09 — Phase 24 QFN neckdown discriminator

Tested 0.15 mm package-edge USB TX neckdowns with normal-width continuation.
Focused connectivity passed, but native DRC retained the real TXP/AVDDL-via
short. Rejected width-only variation and retained the VBUS V1 parent.

## 2026-09-09 — Phase 24 staggered lower-field basis

V8 uses a staggered order-preserving U11 TX fanout. USB3/SATA/mode/JMS583 and
pad-parity audits pass; native DRC reports 730 findings with no shorting class.
Retained V8 as the disposable local routing basis while full-board closure
remains open.

V13 upper P-leg detour preserved the clean V8 escape and reduced USB TX skew
proxy to 0.259 mm. Focused storage audits and parity pass with no shorting
class; native DRC remains 730 with inherited global closure debt.

Fresh VBUS-parent native validation passed all focused storage audits, the
JMS583 negative control, and pad parity; the fresh DRC receipt reports 732
findings and 400 unconnected items. Recorded as the current parent baseline.

V21 CM5_PERST outboard reroute terminated on no-net J1 pads and introduced two
native shorts. Rejected the low-speed implementation; endpoint authority must
be audited before further PERST routing.

V14 lateral TXN offset reduced the local skew proxy to 0.096 mm but introduced
a 0.000 mm native clearance violation into U11 pad 23. Rejected the route
implementation and retained V13 as the no-short basis.

V15 ordinary-via/B.Cu TXN escape preserved focused USB3 connectivity but
introduced six TXP/TXN shorting findings and raised native DRC to 746. Rejected
the layer-transition implementation; complete lower-field co-authoring is the
next routing class.

V16 wider planar TXN dogleg removed the pad-23 defect but retained a 0.0925 mm
native TXP/TXN clearance violation. Rejected the candidate; coordinated
lower-field regeneration remains the next routing class.

V17 coordinated native A* TX regeneration preserved endpoint connectivity but
raised native DRC to 781 with 33 crossings and 281 clearance findings. Rejected
the router-generated field; complete hand-authored lower-field co-authoring
remains required.

V20 AVDDL B.Cu relocation removed the former analog/TX crossing but introduced
an AVDDL-to-USB_RXP1 short at the transition via. Rejected the independent
AVDDL branch; AVDD33 and USB TX/RX must be co-authored in the lower field.

V18 direct U12 launch after C86/C87 relocation shorted U12 POWER_GND; V19
retained the U12 corridor but shorted JMS_AVDD33 into TX copper. Rejected both
cap-relocation classes; complete U11/U12 field co-authoring remains required.

V11 shortened TXN and reduced the USB TX skew proxy to 1.620 mm, but native
DRC rose to 731 and added a CM5 USB RX pair short. Rejected the candidate and
recorded the need for serialization-safe whole-net regeneration.

Exercised the installed local USB3 router against V8. It passed focused USB3
endpoint assertions but produced 734 native DRC findings and a real
JMS_USB3_TXN/USB_RXP1 short. Rejected the fixed-channel router assumptions.

## 2026-09-09 — Phase 24 current-state narrative reconciliation

Marked the older VCCK-local integrated-candidate paragraph as superseded by
the current VBUS/J8 parent and V13 disposable source-field basis. Preserved
the older route metrics as historical evidence; no raw receipt or PCB artifact
was rewritten.

## 2026-09-09 — CM5_PERST native endpoint reconciliation

Audited the saved VBUS/J8 parent with KiCad's native PCB objects. Confirmed
CM5_PERST is owned by J7.109, TP8.1, and J1.E18 and that the existing F.Cu
trunk joins those pads. Clarified that V21 is rejected only because its new
outboard path crossed no-net J1 pads; the endpoint contract is not an open
authority task. Raw V21 evidence remains unchanged.

## 2026-09-09 — V13 support-join route rejection

Tested a disposable V13-plus-support candidate using native pad endpoints for
the complete JMS583 support cohort. Focused support connectivity and its
trace-removal negative control passed, but native DRC worsened from 730 to 778
findings with 395 unconnected items. Rejected the direct support-join route;
the next class remains coordinated lower-field regeneration.

## 2026-09-09 — V23 crystal route variant and audit correction

V23 changed the disposable XIN/XOUT route geometry and passes focused JMS583
support connectivity plus the trace-removal negative control. A later native
net-identity audit showed V13 already had same-net ordinary vias at all four
XIN/XOUT layer changes, correcting the earlier false missing-via diagnosis.
V23 remains disposable route evidence at 724 DRC findings / 400 unconnected
items, with two inherited unrelated shorting items.

Hardened the native layer-transition audit to require the same net on the
F.Cu endpoint, B.Cu endpoint, and physical via. Parent, V13, and V23 each
report zero un-viaed net-identity transitions under the corrected predicate.

V22's initial crystal transition-via placement shorted XIN/XOUT and was
superseded by V23. V24 tested an all-F.Cu alternative; native DRC stayed at
730 and four shorting items were introduced. Rejected both alternatives and
retained V23 as the best current physical transition basis.

V25 moved both XIN/XOUT B.Cu transition corridors outside the inherited SATA
field. Native DRC rose to 745 and eight shorting items appeared. Rejected the
outer-corridor class; V23 remains the disposable crystal basis.

V26 corrected the QFN departures in the V25 outer-corridor experiment but
still produced 746 native DRC findings and six shorting items against
inherited V100/USB/SATA copper. Rejected the corrected outer-corridor class;
V23 remains the current disposable basis.

Added a native KiCad `CONNECTIVITY_DATA` endpoint audit for the JMS583
crystal/analog support nets. V23 passes 7/7 physical endpoint pairs, and a
disposable negative control with one XIN trace removed fails exactly at XIN.
This is stronger physical-connectivity evidence for the storage field.

Added a second native negative control that removes the XIN transition via
from V23. The same audit fails XIN while the other six endpoint pairs remain
passing, proving that missing layer-transition hardware is detected as well.

Filled the V23 zones and reran native validation. The saved filled candidate
reports 607 DRC findings and 399 unconnected items, down from 724/400 before
fill. Native JMS583 endpoint, USB3, SATA, and mode-control audits remain
passing; two inherited unrelated shorting items remain.

Fresh native DRC recheck reproduced the filled V23 baseline at 607 findings
and 399 unconnected items. Retained the receipt as the stable comparison
baseline for the next coordinated storage-corridor repair.

V27–V30 tested native repairs for storage-local post-fill shorts. V27 added
seven shorts, V28 collided with USB_RXN1, V29 collided with JMS_AVDDL and
failed mode control, and V30 added a CM5 USB TX pair short. Rejected all four;
filled V23 remains the retained comparison basis.

V31 tested an F.Cu-only VBUS detour. It removed the original TUSB_SATA_TXP /
VBUS short but introduced three native short classes after refill. Rejected
the isolated VBUS detour; coordinated corridor allocation remains required.

V32 tested a left-exit VBUS corridor. After native refill it removed the
storage SATA/VBUS short and reduced DRC to 604 findings / 399 unconnected
items; one CM5 USB RX polarity short remains. All focused storage audits pass.
Retained V32 as disposable corridor evidence only.

V33 tested an orthogonal staggered CM5 USB3 RX source escape. Native DRC was
594 findings / 401 unconnected items, but six true shorting classes appeared,
including RX polarity and TX/RX source-field collisions. Rejected V33; a
complete four-net CM5 USB3 source-field regeneration is required.

V34 regenerated the complete four-net CM5 USB3 source field with orthogonal
staggered exits. Native DRC was 589 findings / 403 unconnected items, but five
true shorts appeared, including a no-net J7 pad collision and RX/XOUT field
collisions. Rejected V34; reference-derived escape allocation is next.

2026-09-09: Introduced RTL9210B-CG as a serious isolated Path-B comparison
candidate without disturbing Path A. Refreshed the live JLC identity and
public firmware/reference evidence, preserved the corrected SMD QFN package
and native support primitives, and recorded the shared lane-0/PEDET mapping,
support audit, procurement/provenance limits, firmware distinction, and
apples-to-apples decision matrix in
`pisxme/reva-clean/PHASE24_RTL9210B_PATH_COMPARISON_20260909.md`. Updated the
storage qualification and Phase 24 current-state narrative to classify Path B
as `CONTINUE BOTH`, with authorized application-circuit, virgin provisioning,
firmware rights, full route, and integrated mode-validation gates still open.

2026-09-09: Repaired the Path-A CM5 USB3 source field with V37. The saved
filled candidate preserves the existing B.Cu handoffs, passes USB3 10/10,
SATA 12/12, mode-control 4/4, JMS583 endpoint 7/7, and pad-parity audits, and
removes the V36 CM5_REFCLK/USB3_TXN short without adding a shorting class.
Native DRC remains 603 violations / 399 unconnected pads, so V37 is retained
as a disposable routing basis only. Evidence is recorded in
`pisxme/reva-clean/PHASE24_STORAGE_CM5_USB4_MONOTONIC_V37.md`.

2026-09-09: Consultant review identified a contradiction between the active
RTL9210B parallel-candidate record and an older lower-QFN DFM rejection.
Tested V665 as a bounded U1.39/U1.40 escape discriminator under unchanged
ordinary-via, 0.20-mm clearance rules. V665 failed with 37 native DRC
violations from its RTL_3V3 route colliding with retained 1V1/SPI geometry;
this rejects that route allocation, not the QFN package or Path-B
architecture. Reconciled the qualification/comparison documents to keep the
strict-QFN DFM gate OPEN and Path B active, with no manufacturing-rule
relaxation or production-CAD change.

2026-09-09: Added the V666 negative control. Removing its required RTL_3V3
escape trace from a disposable copy produced one native unconnected item;
the clean package discriminator therefore depends on saved physical copper,
not expected connectivity or synthetic graph edges.

2026-09-09: Reconciled the remaining Phase 24 status prose that still called
the earlier V663/V664 lower-QFN route failures a Path-B package/DFM blocker.
Marked that statement superseded and pointed it to V666's clean package-level
escape result. The complete integrated RTL9210B source-field route remains
open; Path A remains protected.
2026-09-09: V666 cleanly discriminated the RTL9210B QFN DFM claim. Using the
audited real footprint, separated U1.39/U1.40 F.Cu exits, unchanged 0.20-mm
rules, and no via-in-pad, native KiCad DRC reported 0 violations, 0
unconnected items, and 0 footprint errors. Closed the package-impossibility
claim; kept the complete integrated QFN source-field route, firmware,
application-circuit, and mode-validation gates open. Preserved Path A.

2026-09-09: Tested V667, a fresh five-net native SPI allocation on the
retained RTL9210B V595 rail/PEDET/CLKREQ base. Native DRC reported 35
violations and 11 opens, including real SPISO3/SPICS and SPI/rail shorts and
source-field crossings. Rejected the route implementation; retained Path B,
Path A, and all production CAD unchanged. The next SPI class must co-author
source escapes with the rail field or coherently move isolated support.

2026-09-09: Tested V668, a materially different five-net RTL9210B SPI class
using staggered native QFN escapes, separated B.Cu channels, and bottom-side
U2 returns on the V595 support/rail base. Native DRC reported 49 violations
and 11 opens, including true source-field shorts/crossings and rail/channel
conflicts. Rejected V668 as a route implementation, not as a package or
architecture result. The next Path-B experiment must coherently reallocate
the isolated U1/U2/flash support island and its rails.

2026-09-09: Consultant-selected V35/U2-left V670 lower-3V3 co-author was
tested from the clean RTL_5V-plus-3V3 basis. Native DRC reported 24
violations and 21 opens, including true lower-3V3 crossings/shorts against
RTL_1V1, RSET, XTAL, and SPI fields. Rejected the route implementation;
retained the V35 SPI/crystal/RTL_5V lineage and Path A unchanged. The next
class must coherently reallocate local RSET/3V3 support before routing the
lower rail again.

2026-09-09: Tested V671, moving the RTL9210B RSET endpoint and re-authoring
U1.51 with ordinary vias and unchanged 0.20-mm rules. Native DRC reported
15 violations and 24 opens because the new perimeter collided with lower
RTL_1V1 and reached the board edge. Rejected V671 as a route implementation;
the next class is an interior co-authored RSET/lower-3V3 field.

2026-09-09: V672 re-authored RSET through an interior west transition while
retaining R1 and the V35/U2-left rail field. Native DRC reported nine
inherited warnings and no signal violations, making V672 the positive RSET
basis. V673 then added lower RTL_3V3 and was rejected at 12 violations/21
opens: U1.52 contacted RSET and U1.39 violated adjacent USB_DM. The next
Path-B class must co-author those QFN source escapes with RSET.

2026-09-09: V674 retained all neighboring RTL9210B U1 pad net identities and
tested one native U1.39 escape at four rotations. The 90-degree orientation
had one intentional dangling-tail warning and no pad short/crossing/
clearance error; 0/180/270 degrees had 11/10/6 violations. Retained the
90-degree package escape basis. The integrated work must co-author U1.39
with the adjacent RTL_1V1 departure.

2026-09-09: V675 tested a co-authored U1.39/U1.40 source-via pair on V672.
Native DRC found 13 violations and 24 opens, including a real RTL_3V3/
RTL_1V1 short at the adjacent via/escape. Rejected V675; retain the clean
standalone V674 U1.39 escape and allocate U1.40 through another corridor.

2026-09-09: V676 tested the around-the-via source allocation from V672:
U1.39 RTL_3V3 transitions west and U1.40 RTL_1V1 turns down to a separate
ordinary via. Native KiCad DRC found 12 findings and 24 expected/incomplete
opens, with no signal short, crossing, clearance, solder-mask, or footprint
errors. Retained V676 as a source-field basis; its short B.Cu tails are not
final support routing and must be extended to native rail collectors.

2026-09-09: V677 extended the V676 source transitions to existing same-net
collectors; native DRC found two real B.Cu crossings with SPI channels, so it
was rejected. V678 changed to F.Cu collector joins; native DRC still found a
real RTL_3V3/RTL_1V1 crossing and single-layer source vias. Rejected V678 and
pivoted the next Path-B class to the native-clean orientation-180 lineage.

2026-09-09: V679 direct crystal routing on the orientation-180 support basis
found 12 native DRC violations including XTAL_IN/RTL_3V3 and crystal/RTL_1V1
crossings. V680 relocated the crystal trio and found 11 violations including
XTAL_IN shorts to RTL_3V3/GND and multiple crossings. Rejected both route
implementations; retain the orientation-180 rail/RSET basis.

2026-09-09: V682 added local GND stitching beside the relocated crystal but
left C1's GND pad physically unconnected to its via. V683 added the missing
same-net F.Cu segment; native KiCad DRC then reported zero violations with
32 expected incomplete opens outside the crystal field. Retained V683 as the
positive crystal-field basis for continued Path-B support closure.

2026-09-09: V681 moved the orientation-180 crystal trio to the lower shelf
and attempted a dedicated B.Cu corridor. Native DRC found 17 violations,
including crystal shorts/crossings, RTL_3V3 interference, and board-edge/
mounting-hole conflicts. Rejected V681 as a placement implementation; retain
the orientation-180 rail/RSET basis.

2026-09-09: V684 attempted a direct inner RTL_3V3 source and found nine
native DRC violations, including CLKREQ_N/QFN-field interference. V685
separated the R2/R3 dogbones and approached outer U1.34 through an ordinary
transition; native DRC reported zero violations and 30 incomplete opens.
Retained V685 as the positive RTL_3V3 edge-source basis.

2026-09-09: V686 extended U1.39 through the QFN field and contacted an
existing RTL_1V1 via, so native DRC rejected it. V687 added a minimum 0.2 mm
lateral jog around that via; native KiCad DRC reported zero violations and 29
incomplete opens. Retained V687 as the positive U1.39 RTL_3V3 branch basis.
2026-09-09: V688 attempted the U1.52 RTL_3V3 branch and native DRC found
three violations where the route contacted the C2 GND return and CLKREQ
pull-up pad. Rejected V688; the next class must co-author U1.52 with the
crystal micro-island.

2026-09-09: V689 translated Y1/C1/C2 left and rebuilt their crystal/GND
connections. Native KiCad DRC found 11 violations including
XTAL_IN/XTAL_OUT/GND shorts and crossings. Rejected V689; retained V683 for
the crystal field and V687 for the U1.39 RTL_3V3 branch.

2026-09-09: V690 moved only C2 and rebuilt XTAL_OUT/GND alongside U1.52;
native KiCad DRC found 15 violations including crystal shorts and rail/control
interference. Rejected the C2-only class; the next attempt must co-author the
complete crystal/support micro-island.

2026-09-09: V692 moved the C2 GND stitch and changed U1.52 to a B.Cu
transition, but crossed the RSET collector. V693 stepped left of the RSET
endpoint and passed native KiCad DRC with zero violations and 28 incomplete
opens. Retained V693 as the positive U1.52 RTL_3V3 branch basis.

2026-09-09: V694's U1.20-to-load corridor contacted SPISI and was rejected.
V695 moved the descent outside the QFN pad field and connected U1.20, C3.1,
U2.3, and U2.8 on RTL_3V3. Native KiCad DRC reported zero violations and 26
incomplete opens; retained V695 as the positive 3V3 load-field basis.

2026-09-09: V696's direct RTL_5V route crossed the RTL_1V1 field and a 3V3
via. V697/V698 developed a split overpass, and V699 removed the redundant
via; native KiCad DRC reported zero violations and 25 incomplete opens.
Retained V699 as the positive U1.33-to-C5 RTL_5V basis.

2026-09-09: V700 connected U1.17 RTL_5V but failed native DRC at the
3V3/1V1 barrier. V701 used a two-via jog but conflicted with the nearby 1V1
via. V702 angled the escape and passed native KiCad DRC with zero violations
and 24 incomplete opens; its targeted handoff-via negative control passed.
V703/V705/V706/V707 SPICS-only route trials were rejected by native DRC.
Retain V702 as the positive U1.17/U1.33/C5 basis and co-author the next SPI
source escape with the rail field.

2026-09-09: V708-V711 were orientation/placement probes; V711 corrected the
zone-refill methodology and showed zero DRC for the 180-degree U1 with U2
translated north/west. V713-V717 tested SPICS doglegs and were rejected until
V718, which added a clean SPICS channel and ordinary U2 GND return. V718
passed native DRC with zero violations, and its saved-board SPICS audit plus
trunk-removal negative control passed. V719/V720/V722 were rejected
two-channel allocations; retain V718 as the positive SPICS/orientation basis.

2026-09-09: V723-V725 tested SPISO continuation routes from V718. Native
KiCad rejected them for SPICS shelf conflict, SPISO handoff-via proximity,
and adjacent SPISO3/SPISO2 QFN-pad interference. Retain V718 and allocate
all five SPI source escapes together.

2026-09-09: V726 rotated U2 90 degrees and passed native DRC after refill;
V730 rotated U1 90 degrees with the rotated U2 and also passed native DRC.
V731 proved a clean SPICS channel. V732-V734 exposed shelf/source conflicts;
V735 co-authored SPICS and SPISO with zero native DRC violations, and its
saved-board endpoint plus source-trace negative controls passed. V736-V745
are rejected three-channel allocation trials. Retain V735 as the current
positive two-channel source-field basis.

2026-09-09: V700 connected U1.17 RTL_5V but failed native DRC at the
3V3/1V1 barrier and was rejected. V701 moved the handoff to a two-via jog,
but still conflicted with the nearby 1V1 via. V702 angled the initial escape
past that via and passed native KiCad 10.0.5 DRC with zero violations and 24
incomplete opens. The saved-board V702 audit passed, and removing the new
RTL_5V handoff via failed connectivity as required. Retained V702 as the
positive U1.17/U1.33/C5 RTL_5V support basis; full Path-B closure remains
open.

2026-09-09: V753 isolated the adjacent SPICLK/SPISI dogbones and passed with
no clearance or crossing errors. V754 combined all five source escapes with
only expected transition-via warnings. V755/V757/V758/V759 incrementally
extended SPISO3, SPICLK, SPISI, and SPISO to the vertical U2 endpoint field;
V756 was rejected for a 0.100 mm SPICLK/SPISO3-via clearance. V760 added the
SPICS endpoint and passed native KiCad DRC with zero violations. Its saved
board audit passed all five native endpoint assertions and source-track
negative controls. This closes the disposable five-net SPI fixture only;
Path-B support, firmware, productization, and integrated gates remain open.

2026-09-09: V761-V772 integrated the V760 SPI field with a local crystal,
RSET, and GND support pocket. V762-V766 were rejected crystal-route trials;
V767/V770/V772 progressively closed the signal and return geometry. V772
passes native DRC with zero violations and its saved-board support audit,
including signal negative controls, passes. It is still an isolated Path-B
support fixture; production integration and remaining control/power/firmware
gates are open.

2026-09-09: V773-V778 explored the RTL9210B local rail/control pocket. V773
was rejected for placement collisions; V774/V777 were electrically clean
placement variants. V775/V776/V778 were rejected control routes that crossed
the validated SPI field. Preserve V772 as the current combined support basis
and continue with an outboard control return class.

2026-09-09: V779 tried split upper/lower F.Cu control corridors and was
rejected by native DRC for PEDET/CLKREQ_N crossings, resistor approach
shorts, and a no-connect U1-pad contact. Continue with control-only resistor
relocation; V772 remains the clean support basis.

2026-09-09: Reconciled the duplicated stale V702 Phase 24 status section by
marking it historical; V772 is the current combined RTL9210B support
checkpoint. V780-V782 were bounded control/SPI rechannel trials. V780
shorted SPICS to the crystal-support GND pocket; V781 and V782 were rejected
by native DRC for endpoint, plane, U1-pad, and retained-SPI corridor
interactions. Their raw boards and reports are preserved; no Path-A or
production CAD was changed.

2026-09-09: V783 attempted an obstacle-aware F.Cu-only control allocator from
the V777 placement. It found no legal PEDET path to R2 in the saved local
field and emitted no PCB. This negative generator result is preserved as
route-field evidence; mixed-layer control allocation or local resistor
relocation remains open.

2026-09-09: V784/V785 were rejected mixed-layer control trials. V786/V787
reduced the native failures to one corridor interaction each. V788 is the
first positive control allocation: moved R2/R3, a lower PEDET jog, and an
outer CLKREQ_N return produce zero electrical DRC violations (three inherited
silkscreen warnings). The saved-board audit and both track-removal negative
controls pass. This closes only the disposable PEDET/CLKREQ_N local route;
remaining RTL9210B and integrated Path-B gates stay open.

2026-09-09: V789/V790 tested the RTL9210B PERST_N outer corridor. The long
route was clear, but its U1 transition collided with CLKREQ_N or SPICLK.
Both are preserved as rejected route evidence; the next class co-authors the
three U1-side control departures. PERST_N remains open.

2026-09-09: V791/V792 co-authored the RTL9210B U1-side PERST_N and CLKREQ_N
departures. Both were rejected by native DRC for QFN-field control/SPI
clearances and contacts. The outer PERST corridor remains usable; the QFN
fanout is the unresolved local route class.

2026-09-09: V793/V794/V795 rejected successive PERST_N QFN escape variants.
The long outer corridor remains clear; native DRC localizes the repeated
failures to interactions among the adjacent U1 control departures, PEDET,
SPISO3, and no-connect pads. The next class must co-author all three QFN
departures; Path A and production CAD remain unchanged.

2026-09-09: V796/V797 tested orientation-180 RTL9210B control fanouts. Both
were rejected by native DRC because the rotated QFN was not co-moved with its
crystal/RSET/GND support and the PERST top run clipped J1 lane pads. Preserve
the orientation class only as a future co-authored placement experiment;
production CAD and Path A remain unchanged.

2026-09-09: V808 is the first positive orientation-180/co-moved-support
control basis. Native DRC reports zero violations and the saved-board audit
passes PEDET, CLKREQ_N, and PERST_N endpoint assertions plus all three
track-removal negative controls. The fixture retains 42 expected incomplete
connections; complete RTL9210B qualification remains open.
2026-09-09: V809/V810 extended the rotated RTL9210B basis with SPICS. V809
was rejected for a PEDET-shelf crossing; V810 moved the upper leg to B.Cu,
restored the U2 GND return, and passed native DRC with zero violations. The
corrected saved-board audit and SPICS track-removal negative control pass.
V811-V813 were rejected SPISO/SPICS source co-routing trials; remaining SPI
source allocation is open.
2026-09-09: V814 paired the SPICS and SPISO source dogbones from the clean
V810 basis, but native DRC found three real conflicts: SPICS crossed the U2
GND branch and PEDET shelf, and the SPISO transition via was too close to the
SPICS lower jog. The result (3 violations, 40 expected incomplete
connections) is preserved as rejected route-implementation evidence; V810
remains the last clean combined basis and Path A/production CAD are unchanged.
2026-09-09: V815/V817/V818/V819 tested separate SPISO transitions against
V810 and were rejected by native DRC with 1, 2, 1, and 1 real violations.
V820 co-authored both adjacent departures but was rejected with 3 native
violations, including a crossing and dangling transition artifacts. These
are preserved as route-implementation evidence; V810 remains the clean
combined basis and complete SPI allocation is open.
2026-09-09: V821 tested translating the Path-B SPI-flash endpoint 10 mm south;
the placement probe passed native DRC with 0 violations and 42 expected
incomplete connections. V822's direct five-net probe was rejected with 11
native violations and 37 expected incomplete connections. The placement is a
candidate class, not a promoted route; V810 remains the retained clean basis.
2026-09-09: V823 is the first clean two-net source allocation after V810.
It retains SPICS and moves the SPISO transition above the adjacent U1 source
field. Native DRC reports 0 violations and 40 expected incomplete
connections; the saved-board audit passes both endpoint assertions and
trace-removal negative controls. Full five-net SPI remains open.
2026-09-09: V824 added staggered transitions for SPISI, SPICLK, and SPISO3
to the V823 pair but was rejected by native DRC with 14 violations and 37
expected incomplete connections, including source-field crossings, PEDET
interaction, and transition-via conflicts. It is route evidence only.
2026-09-09: V825 returned to the V777/V772 placement class to retain the
complete five-net SPI field while testing separated control-resistor
approaches. Native DRC rejected the first route with 7 violations and 34
expected incomplete connections, including CLKREQ_N/SPISI, PEDET/SPISO
transition, and C5 GND interactions. V772 remains the preferred complete-SPI
starting point; control routing remains open.
2026-09-09: V828 tested outboard F.Cu PEDET/CLKREQ_N columns while retaining
the V772 complete SPI/support field. Native DRC rejected it with 4 violations
and 33 expected incomplete connections, including control-to-SPI clearance,
PEDET/SSD_3V3 launch conflict, and a U2 GND thermal issue. It is route
evidence only.
2026-09-09: V829 tested immediate local PEDET/CLKREQ_N resistor placement and
was rejected with 4 violations and 33 expected incomplete connections. V830
angled the dogbones but increased the result to 10 violations and 33 expected
incomplete connections. Both are rejected local control variants; V772
remains the complete-SPI/support basis.
2026-09-09: V831 tested a vertically split local PEDET/CLKREQ_N control pair
with opposing QFN dogbones. Native DRC rejected it with 6 violations and 33
expected incomplete connections, including PERST_N/CLKREQ_N and RTL_3V3/PEDET
shorts plus QFN-adjacent mask/clearance failures. The next class must move the
control pair coherently away from the SPI field.
2026-09-09: V826 tested B.Cu-separated PEDET/CLKREQ_N approaches on V777 and
was rejected with 6 violations and 33 expected incomplete connections. V827
moved the source transitions laterally and was rejected with 9 violations and
33 expected incomplete connections, including no-connect-pad/via and SPI
corridor conflicts. V772 remains the preferred complete-SPI basis.
2026-09-09: V832 moved the PEDET/CLKREQ_N resistors as a coherent far-outboard
island; placement-only native DRC passed with 0 violations and 35 expected
incomplete connections. V833's first B.Cu route was rejected with 6
violations and 33 expected incomplete connections because source vias and
corridors intersected retained SPI geometry and reached the board edge.
Correction: V832's Y=90 resistor coordinates are outside the disposable
Y=40–85 outline; its zero-violation result is not mechanical feasibility
evidence.
2026-09-09: V842 tested a 90-degree U2 SPI-flash rotation to change endpoint
pin order. Native DRC rejected it with 11 violations and 45 expected
incomplete connections because the rotated U2 field overlaps retained R1/Y1
support geometry and a GND thermal region. It is local placement evidence
only; Path A and production CAD remain unchanged.
2026-09-09: V838 tested a perimeter PERST_N route from V837 and was rejected
with 3 violations and 32 expected incomplete connections. V839 offset the
source transition but was rejected with 4 violations and 32 expected
incomplete connections, including SPISO/SPISO3 corridor shorts and adjacent
U1 pad-field clearance. PERST_N remains open.
2026-09-09: V834 is the corrected in-outline control placement probe and
passed native DRC with 0 violations and 35 expected incomplete connections.
V835/V836 were rejected route implementations with 5 and 3 violations.
V837 reversed the control endpoint order and passed native DRC with 0
violations and 33 expected incomplete connections; its saved-board audit
passes PEDET/CLKREQ_N endpoints and trace-removal negative controls. PERST_N
and remaining support validation remain open.
2026-09-09: V840 reduced PERST_N to 2 native violations and 32 expected
incomplete connections; its outer corridor is clear but the source track
contacts U1 pad 15. V841 changed the dogbone direction and was rejected with
4 violations. V840 remains the better candidate; PERST_N source escape stays
open.
2026-09-09: V843 co-moved the crystal/RSET support away from the rotated U2
field and passed native DRC with 0 violations and 45 expected incomplete
connections. V844's 270-degree orientation had no electrical DRC violations
and only 3 silkscreen warnings; SPISI/SPICLK/SPISO3 follow the U1 source
order. V845's direct three-net probe was rejected with 9 native findings and
42 expected incomplete connections. The 270-degree basis remains a candidate.
2026-09-09: V846's ordered three-net 270-degree fanout was rejected with 10
native findings and 42 expected incomplete connections. V847 moved the
controls clear but was rejected with 7 native violations and 42 expected
incomplete connections, dominated by SPISI transition/reference-zone
clearance. The 270-degree placement remains a candidate source-field basis.
2026-09-09: V850 established a clean ordered three-net SPI source primitive
for the 270-degree RTL9210B flash orientation. It scrubbed stale local
SPI/GND copper, moved PEDET/CLKREQ_N controls clear, and routed SPISI,
SPICLK, and SPISO3 monotonically to U2. Native DRC had no electrical
violations (one isolated B.Cu GND-fill warning only); the saved-board audit
passed all three endpoints and all three trace-removal negative controls.
This is partial evidence only: SPISO, SPICS, PERST_N, and complete support
validation remain open. Path A and production CAD remain unchanged.
2026-09-09: V851 extended V850 through SPISO and SPICS. The saved-board
audit passed all five SPI endpoint pairs and five trace-removal negative
controls, with no signal short/crossing, but native DRC rejected one GND
thermal-starvation error plus the inherited isolated B.Cu-fill warning.
V852's ordinary-via B.Cu separation was rejected by a real SPISO/SPICS
source-escape short. The next experiment must stagger source vias clear of
the adjacent F.Cu fanout.
2026-09-09: V853 tested staggered outward source vias for the lower SPI pair.
It was rejected by six related SPICS-to-U1 exposed-GND pad/thermal/clearance
violations plus the inherited isolated-fill warning. It retained 40
incomplete items and no new endpoint failure. The next class staggers the
source escapes left of U1 before the B.Cu transitions.
2026-09-09: V854 tested a left-side vertically staggered B.Cu source escape
and was rejected with 19 native violations, dominated by U1 exposed-pad,
adjacent-pad, and zone-clearance conflicts. This is route-implementation
evidence only. The next active basis returns to V772's complete-SPI/support
field for a distinct control/source escape class.
2026-09-09: V855 tested a V772/V837-based PERST_N left-side source dogbone.
Native DRC rejected it with 5 violations: one true B.Cu crossing against the
SPI corridor and four U1-field clearance/short/mask conflicts. It is rejected
route evidence; V772/V837 remain the complete-SPI/control basis.
2026-09-09: V856 made the PERST_N source escape straight right and reduced
native DRC to one violation where its via touched the parallel CLKREQ_N
corridor. V857 doglegged upward before the via and passed native DRC with 0
violations and 32 expected incomplete items. Its saved-board audit passed all
five SPI endpoint pairs plus PERST_N and all six trace-removal negative
controls. This is a local routing primitive, not full Path-B closure.
2026-09-09: The V857 support re-audit passed XTAL_IN, XTAL_OUT, RSET, and
plane-backed GND endpoint assertions; trace-removal negative controls passed
for the three signal support nets. V857 is a native-clean local basis for
SPI, PERST_N, crystal/RSET, and reviewed ground support, while its 32
incomplete Path-B source/rail/control/CM5-side connections remain open.
2026-09-09: V858/V859 tested the RTL_5V source-to-C5 power-plane probe and
were rejected for source/via clearance and accepted SPI/PERST collisions.
V860 narrowed the source to 0.20 mm and moved its ordinary transition into
the measured SPI-channel gap. Native DRC passed with 0 violations and 31
expected incomplete items; the saved-board audit proved U1.17→C5.1 and a
trace-removal negative control. Remaining RTL_5V/RTL_3V3/RTL_1V1 endpoints
remain open.
V133 shifted TX support-cap corridors to y=160/165 but was rejected at
192/499 for real JMS_AVDD33, BRIDGE_1V1, and U12 support collisions. Simple
vertical translation is exhausted; the next candidate must change local
layer ownership or support-side corridor.
V132 selectively translated the isolated TX support legs and moved C86/C87,
but native DRC rejected it at 150/499 for a CM5_PERST-to-BRIDGE_3V3 short at
TP5, a PERST crossing, and local TX-pair clearance. The saved y=150 support
corridor is not transplantable; local corridor shifting remains required.
V131's RX-only obstacle-aware A* support escape was rejected at 177/499 for
real RX shorts/crossings into POWER_GND and JMS_AVDDL. Coarse A* is retired
for the dense support field; explicit package-aware transitions are next.
V130 co-authored local U11/U12 TX coupling-cap legs and passed all ten native
support/USB3 endpoint assertions, but was rejected at 207/499 for real
support-net shorts/crossings into USB_DP, JMS_VCCO, USB_RXN1, and U12/U13.
V127 remains the parent; obstacle-aware local support escapes are required.
V128 translated the isolated U11/U12 support copper and passed all ten native
endpoint assertions, but was rejected at 164/499 for real crossings/shorts
into CM5_PERST, U13, and the M.2 field. Rigid translation is not valid for
V127; local co-authoring remains required.
V125 rebuilt V123's native net list before zone refill and reduced DRC to
148/499 without USB3 shorts/crossings. V126's target-transition rearrangement
reintroduced RX shorts/crossings and was rejected at 153/499.

2026-09-10 — Phase 24 V1375/V1376 rejected: U1.55 RTL_1V1 perimeter escapes
conflicted first with the accepted RTL_3V3 field and then with the existing
GND return field after an outward shift. Preserved as routing evidence; the
accepted V1374 rail basis and Path-A/production CAD remain unchanged.
2026-09-09: V976 fully relocated the SPISO3 transition around the best V969
RTL_3V3 cell and was rejected with five native DRC findings. The relocation
shorted both the RTL_3V3 B.Cu trunk and the preserved SPISO shelf. This
confirms the issue is a coupled local support-island allocation problem, not
one transition coordinate; the next experiment co-authors SPI, 1V1, 5V, and
3V3 shelves as one disposable island.
2026-09-09: V974 exposed U1.21 SPISO2 at (100.0,66.05) as an additional
source-field constraint; its proposed RTL_3V3 transition was rejected with
eight native DRC findings. V975 routed RTL_3V3 right of that pad and returned
on B.Cu, but was rejected with six findings for SPICLK/SPISI source crossings
and SPISO3 shelf clearance. The next credible class is a full local RTL
support-island move/regeneration, not another isolated jog.
2026-09-09: V973 moved SPISO3 left around the best RTL_3V3 cell and was
rejected with six native DRC findings. It introduced SPISO and RTL_1V1
crossings and retained RTL_3V3 clearance failure. The proven V927 SPI
corridor is preserved; a broader local support-island regeneration is now
required rather than another isolated SPISO3 jog.
2026-09-09: V972 swept lower RTL_3V3 transition cells against V927. Best
lower cells had three native DRC findings; no lower cell removed the
RTL_3V3/SPISO3 source-field interaction. The result confirms that the next
repair must co-author the source-field route itself, not only move the via.
2026-09-09: V971 extended the RTL_3V3 transition sweep above the SPI shelves.
The best tested cell was (100.0,64.6), with two native DRC findings; the
upper sweep best was (100.0,63.5), with three. The remaining electrical short
is specifically RTL_3V3 versus the existing SPISO3 F.Cu segment, plus the
known dangling transition. The sweep is retained as evidence and no
production CAD changed.
2026-09-09: V969 swept RTL_3V3 source-transition cells against the V927
native-clean SPI base. The best cell was (100.0,64.6), with two findings;
other tested cells ranged from 3 to 8 findings. V970 moved SPISO3 around that
cell and was rejected with seven crossings/shorts. Preserve the V927 SPISO3
corridor; the remaining one-short problem needs a different local transition
without disturbing that corridor.
2026-09-09: V967 is retained as the best current co-authored RTL local
partition (five native DRC findings). It moved SPISI east and used a compact
SPICLK departure while leaving the V927 SPI shelves otherwise intact. V968
then worsened the result and remains rejected. V967 is reference evidence,
not closure; RTL_3V3 source transition and local rail interactions remain
open.
2026-09-09: V968 relocated SPICLK/SPISI transitions around V967 and was
rejected with seven native DRC findings. The left SPICLK dogleg crossed
SPISO3; the shifted SPISI via collided with PERST_N; RTL_3V3 still conflicted
at its source via. V967 remains the better partition. Next repair relocates
RTL_3V3 itself while restoring V927-derived SPICLK/SPISI corridors.
2026-09-09: V966 co-authored the native-clean V927 SPI base with a U1.20
RTL_3V3 transition, relocated SPICLK, and relocated SPISI. Native DRC found
six local errors: SPISI shelf crossings/shorts and RTL_3V3-to-SPICLK source
clearance, plus the retained via-dangling warning. V966 is rejected but
narrows the next repair to source-transition and shelf allocation; production
CAD remains unchanged.
2026-09-09: V964 tested U1.20 RTL_3V3 above-pad transition on the V927
native-clean SPI base and exposed six local interactions, including B.Cu
crossings with SPI shelves and source-via conflict. V965 co-authored local
SPICLK/RTL_5V/RTL_3V3 departures and reduced the problem to eight findings,
but was rejected for source-via, shelf, and XTAL/1V1 crossings. These are
disposable interaction evidence; the next repair moves the 3V3 transition
farther from the QFN and routes around the SPI shelves.
2026-09-09: V963 reused the native-DRC-zero V927 five-SPI ancestor and added
U1.20 RTL_3V3. It reduced the interaction to five local findings: the new
3V3 vertical crosses SPISO3, and the shifted SPICLK conflicts with SPISI.
This is the current interaction map for co-routed repair; it is not promoted
and no production CAD changed.
2026-09-09: Corrected V962 applied the U1-0 transform before routing; its
native DRC result was 8 violations, with SPISO colliding at the transformed
SPICS/RTL_1V1 side-pad field. The earlier unrotated V962 result is invalid and
not used. U1-90 remains the better source-field basis; no production CAD
changed.
2026-09-09: V959/V961 tested U1-0 source fanout with U2 displaced for a
source-field-only discriminator. Direct horizontal and diagonal departures
still collide with neighboring exits; staged V961 retained 10 native DRC
violations. These are disposable evidence only. The next route pass must
co-design immediate layer-separated escapes and first-layer corridors; no
production CAD changed.
2026-09-09: V957 rejected naïve mixed-side same-layer SPI fanout after the
U1-270 probe (15 native DRC violations). Inner QFN pad departures crossed
outer-pad fields. Next experiment requires immediate layer-separated inner
escapes; this remains a disposable route-authoring issue.
2026-09-09: V944 proved U1.20 RTL_3V3 can escape in a clean field when SPI
copper is regenerated around it. V945/V946 added SPICS and SPICLK with native
DRC limited to the inherited isolated-fill warning. V947/V948 SPISO3/SPISO
variants were rejected for source-field crossings and shared transitions.
V949/V951 independently re-authored both nets; V952 swept four source cells
(7-9 native DRC violations each). The remaining failure is the current U1
orientation/exposed-pad source field at the active 0.20 mm rules, not a
connectivity assertion or RTL9210B topology failure. Raw candidates and
reports are retained; SPI remains open and the next experiment is a bounded
U1 orientation/QFN source-field regeneration.
2026-09-09: V958 rejected direct transplantation of historical V736 SPI
shelves onto the current V944 field (13 native DRC violations). The current
transformed pads require fresh escape authoring; historical copper remains
reference evidence only.
2026-09-09: U1-180 V954/V955 and U1-270 V956 source-field probes were rejected
as incomplete route implementations. U1-180 tightened the pad field; U1-270
had horizontal pads but same-side parallel fanout vias crossed later exits.
The next disposable class is mixed-side source escape with independent
transitions. No production CAD changed.
2026-09-09: U1-180 source-field probe V954/V955 was rejected. V954's simple
escapes shorted adjacent SPI nets; V955's staggered escapes increased native
DRC findings to 14 because the rotated 0.4 mm vertical pad ordering leaves a
tighter source field. This is retained as a placement/orientation
discriminator, not a promoted route. V953-V955 remain disposable Path-B
evidence; no production CAD changed.
2026-09-09: V870 extended the clean V869 RTL_3V3 spine from U2.8 to U2.3.
Native DRC passed with 0 violations and 28 expected incomplete items; the
saved-board audit proved U2.3/U2.8/C3.1 and a trace-removal negative control.
U1-side RTL_3V3 and R2/R3 supply endpoints remain open.
2026-09-09: V863 tested a combined RTL_3V3 bridge/support collector and was
rejected by an In2 crossing against RTL_5V plus U2/SPI clearance conflicts.
V864 moved the collector outboard but was rejected by three real F.Cu/In2
crossings against PEDET, CLKREQ_N, and RTL_5V. These are rail-route allocation
failures; the next experiment isolates U2.8 before rebuilding a collector.
2026-09-09: V865 reduced the RTL_3V3 bridge probe to one PEDET clearance
violation. V866 exposed a PEDET crossing and CLKREQ clearance; V867 collided
with SPISI and PERST_N B.Cu corridors; V868 reduced this to one PERST_N
crossing. V869 lifted the B.Cu jog above PERST_N and passed native DRC with 0
violations and 29 expected incomplete items. Its saved-board audit proved
U2.8→C3.1 and a trace-removal negative control; remaining RTL_3V3 endpoints
remain open.
2026-09-09: V861 added U1.33 to the V860 RTL_5V network but was rejected for
a dangling In2 track caused by an incorrect junction coordinate. V862
corrected the join to the actual V860 transition. Native DRC passed with 0
violations and 30 expected incomplete items; the complete RTL_5V audit passed
U1.17/U1.33/C5.1 and its trace-removal negative control.
2026-09-09: V871 added U1.39 to the validated RTL_3V3 bridge spine. Native
DRC passed with 0 violations and 27 expected incomplete items; the saved-board
audit proved U1.39/U2.3/U2.8/C3.1 and a targeted U1.39 source-trace negative
control. Remaining U1 RTL_3V3 pads and R2/R3 supply endpoints remain open.
2026-09-09: V872/V873 tested U1.20 upward/stepped RTL_3V3 escapes and were
rejected by SPI-field and RTL_5V-transition crossings. V874/V875 tested local
U1.34/U1.39 joins and were rejected for RTL_5V via clearance. V876's
diagonal-left U1.34 departure passed native DRC with 0 violations and 26
expected incomplete items; its saved-board audit proved
U1.34/U1.39/U2.3/U2.8/C3.1 and a source-trace negative control.
2026-09-09: V877/V878 tested U1.52 lower-side escapes and were rejected by
XTAL_IN/RSET support corridors. V879 scrubbed only those support routes as a
placement discriminator; U1.52 then joined the 3V3 spine with native DRC 0,
30 expected incomplete items, and a saved-board audit pass for
U1.52/U1.39/U2.3/U2.8/C3.1 plus a source-trace negative control. The increased
open count is deliberate support-scrub evidence, not an accepted omission.
2026-09-09: V880 translated the complete Y1/C1/C2/R1 support block 8 mm west;
V881 was rejected for crystal-field crossings and RSET/GND conflicts. V882
moved the block a further 18 mm northwest; V883 was rejected for RSET
proximity/crossing, and V884 isolated RSET while exposing the GND-return need.
V885 scrubbed support and retained clean RSET. V886/V887 were rejected for
GND-return crossings or pad clearance. V888 accepted the separated underside
GND return: native DRC 0 violations, 29 expected incomplete items, and a
saved-board audit pass for C1.2/C2.2/R1.2 with three local vias plus a
zone-independent trace-removal negative control. Crystal nets remain open.
2026-09-09: V889 tested direct outer F.Cu crystal corridors and was rejected
for the U1.52 RTL_3V3 escape and far-side XTAL_IN landing. V890/V891 repeated
the trial with U1.52 scrubbed; V891 removed that conflict but still failed the
U1.55-adjacent XTAL_OUT source escape and residual 3V3 corridor. These remain
route-implementation failures. V888 is the accepted GND-return base for the
next U1 source-escape strategy; crystal nets remain open.
2026-09-09: V892 corrected the source-escape shape with a perpendicular
XTAL_OUT dogbone and the scrubbed U1.52 discriminator. Native DRC passed with
0 violations and 26 expected incomplete items. The saved-board audit passed
XTAL_IN/XTAL_OUT/RSET/GND connectivity and both source-trace negative
controls. V892 is the accepted complete relocated crystal-support primitive;
U1.52 RTL_3V3 remains scrubbed for the next restoration trial.
2026-09-09: V909-V910 tested east/staggered 3V3 and crystal restorations and
were rejected for QFN, XTAL, or SPI-field interactions. V911 scrubbed only
inherited SPI copper and still exposed source separation issues. V912-V913
corrected construction but retained duplicate-via/source defects. V914 used
the native V772 dogbones, separated XTAL_IN onto B.Cu, and reused the existing
U1.52 via. Native DRC passed with 0 violations and 25 expected incomplete
items; full support audit and both crystal negative controls passed.
2026-09-09: V893-V896 tested restored U1.52 RTL_3V3 corridors and were
rejected by crystal/RSET/JTAG/PEDET/SPI-field crossings. V897-V900 tested
ordinary B.Cu XTAL_IN transitions and east-shifted variants; V901 separated
F.Cu lanes but still crossed at the source. V902-V904 tested XTAL_OUT B.Cu
transitions and were rejected for QFN/via clearance or source crossings.
These remain route-implementation failures. V892 is still the accepted
crystal/GND primitive; U1.52 restoration remains open.
2026-09-09: V905/V906 tested staggered crystal transitions with the known
U1.52 3V3 escape and were rejected for via clearance/dangling transition.
V907 moved the 3V3 join on B.Cu but collided with SPISO and XTAL_IN. V908
moved the collector to low F.Cu and was rejected by SPISO/XTAL_IN clearance
and a dangling via. The remaining issue is package-region routing, not an
electrical-topology or placement rejection.
2026-09-09: V914 transplanted the native V772 source dogbones, moved XTAL_IN
to B.Cu at the first clean escape, retained XTAL_OUT on its separate F.Cu
corridor, and reused the existing U1.52 3V3 via without duplication. Native
DRC passed with 0 violations and 25 expected incomplete items. The saved-board
audit passed XTAL_IN/XTAL_OUT/RSET/GND/RTL_3V3 and independent source-trace
negative controls for both crystal nets. V914 is the accepted complete
relocated RTL support primitive for the next support rail.
2026-09-09: V915/V916 tested two-pad RTL_1V1 In2.PWR attachments to C4.
V916 reduced native DRC to two violations but still crossed/shorted the
existing RTL_3V3 source field at U1.36/U1.40. RTL_1V1 remains open; the next
trial will use a different U1 pad-side escape.
2026-09-09: V918/V919 tested U1.25 RTL_1V1 north escapes and were rejected by
the inherited SPICS/DEVSLP field. V920 scrubbed only inherited SPI copper and
the same U1.25/C4 In2.PWR attachment passed native DRC with 0 violations and
29 expected incomplete items. The power escape is clean when its corridor is
owned; SPI regeneration is the next implementation step.
2026-09-09: V917 tested alternate U1.36/U1.40 RTL_1V1 pad-side escapes with
an In2.PWR trunk. Native DRC rejected the candidate for RTL_3V3/USB_TXP0/GND
field interactions. RTL_1V1 remains open; V914 remains the accepted base.
2026-09-09: V921 regenerated SPICS from the west escape and was rejected by
U1.28 clearance. V922 moved SPICS east to U1.24 -> via (100,67) -> U2.1 and
retained the V920 U1.25 RTL_1V1 attachment. Native DRC passed with 0
violations and 28 expected incomplete items; the saved-board audit and SPICS
negative control passed. V922 is the accepted 1V1/SPICS primitive.
2026-09-09: V923 added SPICLK and V924 added SPISO3 around the accepted
U1.25/SPICS escape; native DRC remained 0 with 27 and 26 expected incomplete
items. V925 was rejected for a real SPISO/SPICS crossing. V926 corrected the
SPISO layer transition/final dogbone and passed native DRC with 0 violations
and 25 expected incomplete items. V927 added SPISI and passed native DRC with
0 violations and 24 expected incomplete items. The saved-board audit proved
all five SPI nets plus U1.25 RTL_1V1-to-C4 and six source-trace negative
controls. V927 is the accepted SPI/1V1 primitive; seven other RTL_1V1 package
pads remain open for the next support-rail implementation step.
2026-09-09: V928/V929 rejected integrated RTL_1V1 fanout trials for concrete
package-region conflicts. V930 clean-field discriminator proved all eight
RTL_1V1 package endpoints to C4.1 with ordinary vias and In2 power copper;
native DRC had no electrical violations and the saved audit/negative control
passed. V931 restored prior support copper and exposed 15 local conflicts,
so the next implementation step is regenerating RTL_3V3/5V/crystal/GND around
the reserved 1V1 allocation. V930 is rail-feasibility evidence, not closure.
2026-09-09: V932 moved R1 outboard by 13 mm and regenerated the U1.51-to-R1.1
RSET path from the left, avoiding the reserved 1V1 vias. Native DRC had zero
electrical violations, with only the two inherited isolated-fill warnings and
28 expected unrelated opens. V932 is the accepted 1V1/RSET primitive; crystal,
3V3, 5V, and local GND restoration remain open.
2026-09-09: V934 tested a relocated XTAL_OUT corridor and was rejected by
native DRC for XTAL_IN/source-field crossing, RTL_1V1 proximity, and a C2
ground/via collision. It remains rejected route evidence; V933 XTAL_IN and
V932 RSET remain accepted.
2026-09-09: V933 relocated Y1/C1/C2 north by 8 mm and regenerated XTAL_IN
with ordinary vias outside component pads and an explicit Y1.1-to-C1.1 join.
Native DRC had no electrical violations (three inherited isolated-fill
warnings and 26 expected unrelated opens); the saved audit and source-trace
negative control passed. V933 is the accepted XTAL_IN primitive; XTAL_OUT,
3V3, 5V, and local GND restoration remain open.
2026-09-09: V935 attempted coordinated XTAL_IN/XTAL_OUT regeneration and was
rejected by native DRC for XTAL_IN/RTL_3V3 source overlap, XTAL_IN/XTAL_OUT
B.Cu crossing, and an isolated C2 ground thermal. It remains rejected route
evidence; V933 XTAL_IN and V932 RSET remain accepted.
2026-09-09: V936/V937 isolated alternate crystal departures and were rejected
for source/B.Cu crossings. V938 scrubbed only the U1.55 RTL_1V1 departure,
regenerated both crystal nets with monotonic B.Cu ordering, and joined C2.1
to Y1.2. Native DRC had 0 electrical violations with two inherited isolated-
fill warnings; the saved audit and two source-trace negative controls passed.
V938 is the accepted crystal-pair primitive; U1.55 1V1 and remaining rail/GND
restoration remain open.
2026-09-09: V939 restored U1.55 RTL_1V1 with a staggered dogbone and ordinary
via at (97.5,76.0), retaining the V938 crystal pair and V932 RSET. Native DRC
had zero electrical violations with two inherited isolated-fill warnings and
24 expected unrelated opens. The saved audit passed all eight RTL_1V1 pads,
both crystal nets, RSET, and four source-trace negative controls. V939 is the
accepted local primitive; RTL_3V3, RTL_5V, and GND restoration remain open.
2026-09-09: V940 restored RTL_5V from U1.17/U1.33 to C5 with staggered source
and outboard transition geometry. Native DRC had zero electrical violations
with three inherited isolated-fill warnings and 22 expected unrelated opens;
the saved audit and corrected C5-side negative control passed. V940 is the
accepted 1V1/RSET/crystal/5V primitive; RTL_3V3 and local GND remain open.
2026-09-09: V941's naïve complete RTL_3V3 fanout was rejected by 21 native DRC
findings against SPI, 1V1, XTAL, and 5V. V942 isolated U1.34 and escaped it
west/up to via (93.5,63.5); native DRC had no electrical violations, with
three inherited isolated-fill warnings and 22 expected opens. V943's first
U1.20 vertical escape was rejected by SPISO3/SPICLK crossings and via
clearance. V942 is the accepted U1.34 sub-primitive; remaining 3V3 endpoints
remain open.
2026-09-09: Phase 24 RTL9210B Path-B V978/V981 source-field discriminators.
V978 proved that orthogonal F.Cu dogbones can leave the orientation-90 QFN
source row without source-field electrical violations; V979/V980 exposed
transition/corridor crossings and side-band via clearances and were rejected.
V981 transformed U1 to orientation 0 about the native exposed pad and proved
all six adjacent source departures cleanly at the source row, with only
intentional dangling ends and inherited incomplete connections.  Preserve
V981 as the next local support-regeneration basis; Path A and production CAD
remain unchanged.
2026-09-09: V982/V983 RTL9210B transition diagnostics.  V982 showed that
spread source vias still entered the near U2/RTL_3V3 field; V983 showed that
an ordered source ladder is insufficient when B.Cu endpoint corridors are
not ordered against the transformed U2 endpoint field.  Both are preserved
as rejected route-implementation evidence.  V981 remains the active clean
source-row basis; the next allocation must preserve lane ordering end to end.
2026-09-09: V984/V985 tested an orientation-0 U2 SPI endpoint allocation.
Orthogonalizing the source and endpoint dogbones reduced the candidate to
eight native violations, but the remaining errors localized to actual U2
pad-5/pad-6/pad-7 ordering and exposed a reversed SPISO3/SPISI provisional
assignment. Preserve this as rejected mapping evidence; future routes must
use transformed native U2 pad coordinates explicitly.
2026-09-09: V986 rejected the lower-side RTL_3V3 escape against V927. Native
DRC found 11 violations, including source-via contact with U1.15/U1.16 and
B.Cu crossings of SPISO3/SPICLK/SPISI. Preserve the result as route-class
evidence; retain V927 as the SPI baseline and V981 as the clean source-field
basis.
2026-09-09: V987 rejected a three-net upper source allocation against V927.
Native DRC found 17 violations involving the retained SPISO/RTL_1V1 shelf,
SPICLK/SPISI, and the new 3V3 source via. The evidence requires full local
1V1/SPISO/3V3 coauthoring; it does not reject Path B.
2026-09-09: V988 proved the full adjacent RTL9210B source field clean after
removing inherited local copper. Eight native source departures (RTL_1V1,
RTL_5V, SPICS, SPISO, SPISO3, RTL_3V3, SPICLK, SPISI) produced no electrical
source-field DRC errors; only intentional dangling ends and inherited opens
remain. Preserve V988 as the transition-regeneration basis.
2026-09-09: V989 rejected a right-jog RTL_3V3 transition against V988 due to
11 native source-field crossings/clearances. V990 accepted a vertical
RTL_3V3 escape to (100.4,60.8) with a B.Cu handoff; native DRC showed no new
electrical violations. Preserve V990 as the 3V3 transition primitive.
2026-09-09: V991/V992 rejected RTL_3V3 collector launches at the R2/R3
PEDET/CLKREQ boundary. V993 moved the branches to the opposite side and
V994 completed the C3 branch from the B.Cu collector; native DRC then showed
only intentional dangling source ends and inherited opens. Preserve V994 as
the accepted 3V3 collector primitive.
2026-09-09: V1000-V1002 rejected RTL_5V shelf routes against the 3V3
collector/R2/R3 branch and C5 GND. V1003 routed below the branch and used a
C5 via at (126.4,52.0); native DRC showed no new electrical violations.
Preserve V1003 as the accepted RTL_5V primitive.
2026-09-09: V995 connected the three remaining U1 RTL_3V3 pads into V994,
but crossed one inherited GND corridor. V996's west shift crossed two GND
routes and was rejected. Preserve V995 as the better fanout diagnostic and
co-author the local GND return with the next 3V3 repair.
2026-09-09: V995/V996 exposed GND interactions in the remaining U1 3V3
fanout. V997/V998 tested west detours; V999 routed below the GND endpoint and
then overhead, producing no electrical DRC violations beyond intentional
dangling source ends and inherited opens. Preserve V999 as the accepted
full RTL_3V3/GND-aware primitive.
2026-09-09: Rejected V1004's bulk transplant of the V930 eight-pad RTL_1V1
fanout onto the V999/V1003 rail field; native DRC reported 23 real
1V1-to-3V3/5V violations. V1005 then proved an isolated U1.25-to-C4.1
RTL_1V1 primitive using a separated ordinary-via/In2 corridor, with no
electrical DRC violations beyond intentional dangling source tracks and
inherited opens. Continue 1V1 allocation incrementally; Path A and
production CAD remain unchanged.
2026-09-09: V1013/V1014 rejected the nominal U1.40/U1.50 lower-left RTL_1V1
transitions because the existing vertical RTL_3V3 collector occupied that
via field. V1015 moved U1.50 west of the collector and passed native DRC with
no electrical violations beyond intentional dangling source tracks and
inherited opens. Retain V1015 as the accepted U1.50 primitive.
2026-09-09: V1016 exposed an isolated U1.55 RTL_1V1 via; V1017 added the
same-net In2 segment into the filled rail pocket. Native DRC then showed no
electrical violations. Retain V1017 as the accepted U1.55 primitive; full
RTL_1V1 closure remains open.
2026-09-09: V1018/V1019 extended the accepted RTL_1V1 pocket to U1.60 and
U1.63 with separate lower-row departures. Native DRC found no electrical
violations; dangling source tracks and inherited opens remain intentional
fixture residue. U1.40 and complete RTL_1V1 support remain open.
2026-09-09: V1020/V1021 rejected simple U1.40 RTL_1V1 translations. The
first violated clearance to native no-net pad 43; the second contacted the
RTL_3V3 collector after moving west. Preserve both as evidence and co-author
the U1.40/RTL_3V3 field next; no architecture conclusion changes.
2026-09-09: V1022/V1023/V1024 rejected U1.40 local-slot probes. Native DRC
localized them to GND pad 45, no-connect pad 48, and RSET pad 51. The next
step is coordinated U1.40/RTL_3V3 QFN-edge regeneration; isolated via nudges
are exhausted. Accepted 1V1 primitives and Path A remain unchanged.
2026-09-09: V1025 rejected west-shifted RTL_3V3 because it crossed three local
B.Cu GND diagonals. V1026 co-authored the 3V3 spine, U1.40 RTL_1V1 escape,
and GND return; native DRC has no shorting, clearance, or crossing findings,
but retains one isolated GND-zone warning and 40 incomplete fixture items.
Retain V1026 as a promising, not-yet-promoted local primitive.
2026-09-09: V1027 corrected the replacement GND path's 0.2 mm endpoint gap
to the preserved (89.2,60.0) via, but native DRC retained one isolated
GND-zone warning. U1.40/RTL_3V3 still has no shorts, clearances, or crossings;
retain V1027 as diagnostic evidence pending zone-connectivity resolution.
2026-09-09: V1028 added a disposable corner GND via and removed the isolated
zone warning, proving the warning is a real plane-island condition. Because
the remote attachment is not a valid production repair and 39 incomplete
items remain, retain V1028 as diagnostic evidence only; trace the lost local
GND attachment next.
2026-09-09: V1029 restored the three native local F.Cu GND attachment
segments removed by the coauthor scrub. Native DRC retained one isolated
GND-zone warning and 40 incomplete items, rejecting that narrow cause.
Preserve V1029 as controlled negative evidence pending broader zone analysis.
2026-09-09: Parent/child DRC comparison showed the broad GND-zone to U1
pad-66 incomplete relationship is inherited, while isolated copper appears
only after local B.Cu return replacement in V1027/V1029. The next coauthor
must preserve parent plane-attachment topology; arbitrary stitching is not a
valid fix.
2026-09-09: V1030/V1031 rejected near-pad U1.40 RTL_1V1 transitions. Native
DRC localized the failures to pad-39 clearance, then the parent RTL_3V3
B.Cu spine and USB_TXP0 pad 41. The next step is coordinated QFN fanout
regeneration, not further single-via nudges.
2026-09-09: V1032 rejected the upper U1.40 RTL_1V1 escape because it crossed
the native U1.39 RTL_3V3 F.Cu branch. U1.40, U1.39, and the 3V3 collector
must be regenerated together, with the parent GND plane attachment retained.
2026-09-09: V1033 rejected the parent-GND-preserving RTL_3V3 reroute. Native
DRC localized failures to U1.40 versus the parent 3V3 via field and the new
3V3 upper-rail segment versus accepted U1.25 1V1 via (98.4,62.5). Future
regeneration must co-author the remote 3V3 and local 1V1 fields together.
2026-09-09: V1034 rejected the parent-GND-preserving RTL_3V3 reroute. The
retained spine contacted U1.40, while the upper remote detour crossed two
GND clearances. The next class is full QFN support-field regeneration with
coordinated placement and transitions.
2026-09-09: V1035-V1039 rejected successive U1.40/RTL_3V3 co-authoring
attempts. V1039 also revealed the disposable scrub was incomplete: inherited
local RTL_1V1 copper remained and contaminated the result. V1040 corrected
the method by scrubbing both local 1V1 and 3V3 copper before allocation.
Native DRC then showed zero electrical violations, with only eight intentional
dangling source warnings and 40 fixture-inherited incomplete connections.
V1040 is retained as a clean local QFN-field primitive; extend it to support
endpoints before claiming Path-B support closure.
2026-09-09: V1041/V1042 rejected U1.40/3V3 extensions at the USB_TX pad field
and U1.39 transition. V1043/V1044 rejected orientation-0 staggered-field
allocations. V1045 moved the 3V3 transition beyond the 1V1 shelf and achieved
native DRC with only six intentional dangling source warnings. Retain V1045
as the current clean orientation-0 transition basis; support endpoint
attachment and full Path-B closure remain open.
2026-09-09: V1046 rejected a C4-side RTL_1V1 transition that shorted adjacent
C3 GND. V1047 corrected the capacitor-side transition and attached the clean
orientation-0 QFN field to C3.1/C4.1. Native DRC has no electrical violations
and six intentional dangling source warnings; 42 fixture opens remain.
V1047 is the current QFN-to-decoupling basis, not full Path-B closure.
2026-09-09: V1048 attached U1.34 RTL_3V3 to the established C3-side trunk
using an ordinary outboard transition. Native DRC stayed free of electrical
violations with six intentional dangling warnings; fixture opens fell to 41.
V1048 is the current supply/source basis while U2 and remaining RTL9210B
support endpoints stay open.
2026-09-09: V1059 rejected U2 3V3 at the rotated-U2 GND/1V1 geometry.
V1060 rejected a diagonal bridge that shorted SPISI. V1061 orthogonalized the
U2.3/U2.8 same-net join and passed native DRC with one inherited dangling
warning and no new electrical violations. Retain V1061 as the U2 supply
primitive; full QFN/resistor/C3 3V3 closure remains open.
2026-09-09: V1051 rejected the U1.20-to-U2.3 transition at U2.7/SPISO3.
V1052 moved U2 10 mm outboard and achieved a native-clean U1.20/U2.3 supply
path with six intentional dangling warnings and 40 fixture opens. Retain it
as the current local support-placement basis; regenerate moved-U2 SPI routes.
2026-09-09: V1053/V1054 rejected rotated-U2 GND/stale-3V3 variants. V1055
scrubbed stale vertical-U2 copper and restored a clean rotated-U2 placement
with local GND returns. V1056 rejected same-pitch SPI source vias; V1057's
staggered source-transition method reduced the SPI failure to two F.Cu
crossings. Preserve V1055 as the placement basis and continue SPI repair.
2026-09-09: V1058 regenerated the five SPI channels to the rotated U2 row.
Native DRC has one inherited RTL_3V3 dangling warning and no new electrical
violations. Saved-board connectivity and source-track negative controls pass
for SPISI, SPICLK, SPISO3, SPISO, and SPICS. V1058 is the current SPI basis;
remaining U2 supply/support endpoints stay open.
2026-09-09: V1049 rejected the U1.20 RTL_3V3 F.Cu corridor at SPISO3.
V1050 rejected the immediate B.Cu alternative at the SPICLK-adjacent via and
1V1 shelf crossing. Preserve both as local route evidence; U1.20 remains
open for an outboard co-authored transition.
2026-09-09: V1062 joined the rotated-U2 3V3 island to the C3 trunk. V1063
attached R2.2/R3.2 with local ordinary transitions. Native DRC retained only
one inherited dangling warning; saved-board connectivity and the source-trace
negative control pass for the complete 3V3 endpoint group. V1063 is the
current supply basis while remaining RTL9210B support stays open.
2026-09-09: RTL9210B V1064 attached U1.20 RTL_3V3 to the retained rotated-U2/C3
3V3 island. The first outboard transition was rejected for SPICLK crossing and
shorting; the inward transition before the SPI escape passed native DRC with
only the inherited dangling warning. Saved-board connectivity proves the
U1.20/U1.34/U1.39/U2.3/U2.8/R2.2/R3.2/C3.1 group, and the U1.20 source-trace
negative control fails as required. V1064 is retained; remaining RTL9210B
support endpoints and full Path-B validation remain open.
2026-09-09: V1067 rejected the first RTL_5V bridge for a U1.34/RTL_3V3
proximity short. V1068 moved the lower transition away from the SPI field and
passed native DRC with only the inherited RTL_3V3 dangling warning. The saved
board proves U1.17/U1.33 RTL_5V connectivity and the source-trace negative
control fails as required; the fixture has 29 opens. V1068 is retained while
source hookup and remaining RTL9210B support gates stay open.
2026-09-09: V1069 rejected a direct C5-to-QFN RTL_5V run for crossings with
RTL_1V1/RTL_3V3; V1070's lower perimeter route lacked a C5 pad transition and
duplicated the source via. V1071 added the explicit C5.1 transition. Native
DRC retains only the inherited RTL_3V3 dangling warning; saved connectivity
proves C5.1/U1.17/U1.33 and the C5-source negative control passes. V1071 is
retained while RTL_1V1 and remaining support/control gates stay open.
2026-09-09: V1072 attached U1.50 RTL_1V1 to the existing west source field.
Native DRC retains only the inherited RTL_3V3 dangling warning and the saved
board proves U1.36/U1.40/U1.50/C4.1 connectivity. The U1.50 source-trace
negative control fails as required; the fixture has 27 opens. V1072 is
retained while remaining RTL_1V1 and support/control gates stay open.
2026-09-09: V1073/V1074 rejected RTL_1V1 U1.16 corridors for crossings with
the retained RTL_3V3 field. V1075 joined U1.16 to the central 1V1 source
transition and passed native DRC with only the inherited warning. Saved-board
connectivity proves U1.16/U1.36/U1.40/U1.50/C4.1, and the source-trace
negative control passes; the fixture has 26 opens. V1075 is retained while
remaining RTL_1V1/support gates stay open.
2026-09-09: Rejected RTL9210B U1.25 RTL_1V1 escape variants V1076-V1080.
Native DRC showed SPICS, RTL_5V, DEVSLP, no-net-pad, and adjacent-via
conflicts. The independent-via class is exhausted; U1.25 needs coordinated
QFN fanout allocation. No rejected copper was promoted and the RTL_1V1 rail
authority remains valid.
2026-09-09: Rejected V1081, a coupled RTL_5V/U1.25 RTL_1V1 fanout attempt.
The relocated 5V corridor crossed retained SPI B.Cu lanes and the U1.25
departure still violated SPICS clearance. Accepted rail authority remains
unchanged; U1.25 requires broader coordinated QFN fanout allocation.
2026-09-09: Rejected V1082-V1084 local RTL_1V1 fanout trials. V1082 collided
with the retained 5V via field; V1083/V1084 U1.55 left-perimeter escapes
conflicted with preserved 3V3/GND return geometry. Independent perimeter
nudges are exhausted for this field; coordinated QFN regeneration is required.
2026-09-09: Rejected V1088 U1.25 RTL_1V1 escape. It reduced the fixture to 22
opens but native DRC found contact with the retained RTL_5V via and SPICS
clearance violations. U1.25 still requires coordinated QFN/SPI/5V fanout.
2026-09-09: V1085 attached U1.60 RTL_1V1 through the lower validated
transition. Native DRC retained only the inherited RTL_3V3 dangling warning;
saved-board connectivity proves U1.16/U1.36/U1.40/U1.50/U1.60/C4.1 and the
U1.60 source-trace negative control passes. The fixture has 25 opens; remaining
QFN/support gates stay open.
2026-09-09: V1086 attached U1.63 RTL_1V1 through the lower validated
transition. Native DRC retained only the inherited RTL_3V3 dangling warning;
saved-board connectivity proves U1.16/U1.36/U1.40/U1.50/U1.60/U1.63/C4.1
and the U1.63 source-trace negative control passes. The fixture has 24 opens;
remaining QFN/support gates stay open.
2026-09-09: V1090 retained the coordinated U1.25 RTL_1V1 dogleg. It clears
SPICS before the far-edge transition and returns to the existing 1V1 shelf.
Native DRC retains only the inherited RTL_3V3 dangling warning; saved
connectivity proves the complete U1.16/U1.25/U1.36/U1.40/U1.50/U1.55/U1.60/
U1.63/C4.1 group and the U1.25 source-trace negative control passes. The
fixture has 22 opens; remaining support gates stay open.
2026-09-09: V1091 rejected the straight RSET approach for crossing R1.2 GND.
V1092 approached R1.1 from above and passed native DRC with only the inherited
RTL_3V3 dangling warning. Saved connectivity and the RSET source-trace
negative control pass; the fixture has 21 opens. V1092 is retained while
remaining support/control gates stay open.
2026-09-09: V1087 attached U1.55 RTL_1V1 through the lower left transition;
the via was shifted to clear native hole-to-hole spacing. DRC retains only the
inherited RTL_3V3 dangling warning, and saved connectivity proves the expanded
U1.16/U1.36/U1.40/U1.50/U1.55/U1.60/U1.63/C4.1 group. The U1.55 negative
control passes; the fixture has 23 opens.
2026-09-09: V1065 rejected the direct U1.52 RTL_3V3 handoff because its B.Cu
perimeter crossed the preserved GND return diagonal. V1066 changed the local
corridor to join the existing V1064 transition field. Native DRC has only the
inherited RTL_3V3 dangling warning; saved-board connectivity proves the full
U1.20/U1.34/U1.39/U1.52/U2.3/U2.8/R2.2/R3.2/C3.1 group and the U1.52
source-trace negative control fails as required. V1066 is retained; remaining
RTL9210B support and full Path-B validation remain open.
2026-09-09: Rejected XTAL_IN candidates V1093-V1096. Native DRC found
crossings/shorts with retained 3V3, RSET/1V1, or the U1 bottom no-net pad row.
Crystal authority remains valid; coordinated QFN/crystal fanout allocation is
required and no malformed crystal copper was promoted.
2026-09-09: Rejected XTAL_IN refinements V1097-V1099. Native DRC showed
retained 3V3/1V1 return-field conflicts and then RSET/U1.52 edge conflicts.
The crystal implementation remains authoritative; coordinated QFN/crystal
support-field regeneration is required.
2026-09-09: Rejected XTAL_IN pad-edge refinements V1100/V1101. Native DRC
showed retained 3V3/1V1 return-field conflicts at the proposed transitions.
Crystal authority remains valid; coordinated QFN/crystal support-field
relocation is required.
2026-09-09: Rejected disposable XTAL_IN/crystal-support candidates V1102-V1112.
The experiments covered alternate QFN departures, coordinated support-cell
relocation, underside placement, and same-side routing. Native DRC rejected
each for concrete QFN pad-field, retained rail/return, via-clearance, or
crossing violations. V1092 remains the retained clean rail/RSET basis; the
current open gate is coordinated regeneration of the QFN rail, RSET, and
crystal fanout. No production CAD was changed.
2026-09-09: V1113/V1114 co-authored the RTL9210B U1.52 3V3 and U1.55 1V1
departures with XTAL_IN. V1114 reduced the new native DRC to the U1.44 no-net
pad clearance/hole pair plus inherited dangling warnings. It is not promoted;
the next trial moves only the 3V3 transition beyond that pad-hole field.
2026-09-09: Rejected V1115/V1116 3V3-transition refinements. Moving the
co-authored transition within or above the QFN still violated exposed-pad,
no-net/USB pad, or central-GND clearance. The next repair must allocate the
complete QFN fanout, including exposed pad and remaining 1V1/3V3 departures,
as one field.
2026-09-09: V1119 retained the co-authored XTAL_IN route with only inherited
dangling warnings; V1120 added XTAL_OUT but was rejected for XTAL_IN/XTAL_OUT
crossings and GND-return contacts. Crystal closure remains open at XTAL_OUT.
2026-09-09: Reconciled the Phase 24 current-state header and narrative to the
live Path-B evidence: V1092 is the retained rail/RSET basis, V1113-V1116 are
rejected coordinated QFN/crystal fanout trials, and V760 is historical SPI
evidence rather than the current checkpoint. No production CAD was changed.
2026-09-09: Added an explicit current-state banner to the Phase 24 status and
qualification documents. The live disposable basis is V1092 through V1119;
V1119 retains XTAL_IN and V1120 rejects the XTAL_OUT extension. Older V760/V772
summaries are historical evidence only.
2026-09-09: Rejected V1121 split-lane XTAL_OUT routing. Native DRC found
XTAL_IN/XTAL_OUT and retained-GND crossings. The experiment remains raw
route-implementation evidence; production CAD and architecture are unchanged.
2026-09-09: Rejected V1122, a V938-inspired deep XTAL_OUT return corridor.
Native DRC found XTAL_IN/XTAL_OUT crossing, GND-return crossing, and retained
U1.1V1 clearance. The next class must change XTAL_OUT lane allocation.
2026-09-09: V1123 added direct U1.45/U1.66 connections to the RTL9210B
exposed-pad GND network. Native DRC retained only the inherited RTL_3V3
dangling warning; the saved-board audit and both negative controls passed.
2026-09-09: V1127 accepted the PEDET route primitive. Native DRC retained
only the inherited RTL_3V3 dangling warning; the saved-board U1.8/R2.1/J1.69
audit and source-trace negative control passed. Full Path-B closure remains open.
2026-09-09: Rejected V1131 separated CLKREQ_N control routing. Native DRC
found retained 1V1 B.Cu shelf, 3V3 corridor, and local U1 departure clashes.
CLKREQ remains open for complete control-field co-authoring.
2026-09-09: Rejected V1133 PERST_N outer-corridor transition refinement.
Native DRC found retained 1V1, SPISI, and RTL_5V geometry clashes. PERST
remains open for complete control-field co-authoring.
2026-09-09: V1134 removed the inherited dangling RTL_3V3 branch from the
V1123 basis. Native DRC, the saved-board RTL_3V3 endpoint audit, and the U1.52
 source-trace negative control pass; full Path-B closure remains open.
2026-09-09: Rejected V1135 XTAL_OUT GND-diagonal overpass: native DRC found
an XTAL_OUT/GND short, RSET crossing, and XTAL_IN/U1.55 clearance conflicts.
Rejected V1136 crystal-pocket relocation and V1137 source-escape rehome as
distinct route-implementation classes; V1136 retained QFN conflicts and
V1137 produced 14 native violations. V1138 tested the independent offset
y=75/y=77 return-lane class; native DRC found 15 violations including
XTAL_IN/XTAL_OUT return crossings. Path A, production CAD, and architecture
remain unchanged; current Path-B gate is a native-clean XTAL_OUT/QFN fanout.
2026-09-09: Rejected V1139 whole-field regeneration. The disposable scrub
removed only local QFN-field copper and reallocated rails, RSET, crystal, and
GND together, but native DRC found 22 violations, including source-field and
support-return crossings. Next trials will derive geometry from native
transformed pad positions; production CAD and Path A remain unchanged.
2026-09-09: V1140 rotated a duplicated U1 in an isolated crystal fixture.
The authoring experiment exposed a blank-board construction defect: duplicated
footprints retained source-local transforms and the new BOARD lacked the
native outline/net registry. Native DRC found 24 tooling-fixture violations;
this is not an electrical verdict and production CAD remains unchanged.
2026-09-09: V1141 used the native V1123 board and queried transformed pad
positions while reallocating the QFN field. Native DRC found 51 violations,
chiefly XTAL source/support crossings and retained local pad/via interactions.
The candidate is rejected route evidence; Path A and production CAD remain
unchanged.
2026-09-09: V1143 routed XTAL_OUT around the native GND return triangle;
V1144 moved the transition clear of adjacent rail vias. V1144 native DRC
retained only the inherited RTL_3V3 dangling warning. Its saved-board
U1.54/Y1.2/C2.1 audit and both source-trace negative controls passed, so the
XTAL_OUT primitive is accepted. XTAL_IN and full Path-B support remain open.
2026-09-09: V1149 corrected the track/via identity matcher and retested
staggered XTAL source vias. Native DRC still found nine violations because an
inherited 3V3 via/branch remained and XTAL_IN was too close to residual rail
geometry. Rejected; future pruning will assert removal counts.
2026-09-09: Corrected V1149 asserted stale 3V3-via removal and reran the
staggered source-via trial. Native DRC reduced the result to six violations,
localized to XTAL_IN versus the GND/3V3/RSET source field; XTAL_OUT remained
clean. Rejected pending source-only refinement.
2026-09-09: V1150 isolated XTAL_IN after counting removal of eight local
3V3/RSET objects. Native DRC improved to four findings; the remaining real
issue was the short B.Cu stub crossing accepted XTAL_OUT. Rejected but
reproducible.
2026-09-09: V1150 was rerun after correcting native track/via classification
and branch-pruning assertions. The saved native result improved to four
violations; XTAL_IN source-field geometry was clean except for its short
stub crossing the accepted XTAL_OUT lane. Rejected pending lane separation.
2026-09-09: V1152-V1155 tested safer single-net XTAL lane allocation. V1152
used precomputed XTAL_OUT removal but had an incorrect crystal endpoint map;
V1153 corrected endpoints; V1154 exposed retained 1V1/GND corridor conflicts;
V1155 isolated the V1150 source field but retained one GND crossing and the
intentional proof-stub warning. All remain disposable route evidence; the
next work reuses the V1119 clean XTAL_IN corridor or moves the local crystal
pocket if required.
2026-09-09: V1156-V1160 completed the crystal lane discriminator. V1156
combined V1119 IN and V1144 OUT; V1157/V1158 exposed QFN escape and inherited
rail-field conflicts; V1159 moved the IN transition outboard. V1160 pruned
four exact RTL_3V3 source objects and achieved one inherited dangling warning,
with native saved-board XTAL_IN/XTAL_OUT connectivity and both negative
controls passing. Accepted as the current disposable crystal source-field
primitive; full RTL9210B support remains open.
2026-09-09: Reconciled the top-level Phase 24 qualification/status prose to
the live V1160 state. Historical V1139/V1119 gate wording remains below only
as archaeology; current open gates are full RTL9210B rail/control/REFCLK and
integrated support closure. Raw receipts were not rewritten.
2026-09-09: V1161/V1162 tested U1.55 RTL_1V1 attachment to native C4.1.
V1161 collided with the exposed-pad/remote power field; V1162 moved both
transitions but still crossed crystal/rail geometry and the C3/C4 endpoint
field. Rejected route evidence; the next trial separates the QFN source
escape from the remote collector.
2026-09-09: V1163/V1164 tested outboard 1V1 collectors with rechanneled
XTAL_IN. V1163 found six native violations; V1164 found eight, including
QFN-source, XTAL/1V1, and 5V-handoff interactions. Rejected route evidence;
next solution class is local crystal-pocket relocation.
2026-09-09: V1165 corrected and accepted the 10 mm west crystal-pocket move.
V1167 attached U1.55 to C4.1 through ordinary vias and the designated In2
power layer. Native DRC retained only the inherited RTL_3V3 dangling warning;
the saved-board 1V1 audit and source-trace negative control passed. Accepted
as the current U1.55 1V1 primitive; remaining rail/control support is open.
2026-09-09: V1165 relocated Y1/C1/C2 coherently and corrected transformed
XTAL_OUT endpoints. Native DRC retained only the inherited RTL_3V3 dangling
warning; the saved-board audit passed XTAL_IN/XTAL_OUT/GND connectivity and
both crystal trace-removal negative controls. Accepted as the current
relocated crystal-pocket primitive.
2026-09-09: V1169 extended the accepted In2 1V1 collector to U1.60/U1.63
with separate ordinary-via dogbones. Native DRC retained only the inherited
RTL_3V3 warning; the saved-board audit and three source-trace negative
controls passed. Accepted as the current 1V1 QFN extension.
2026-09-09: V1170-V1173 explored U1.16 1V1 escape classes; V1174 accepted
the south F.Cu dogbone plus direct In2 handoff. Native DRC retained only the
inherited RTL_3V3 warning. The saved-board U1.16/C4.1 audit passes with a
corrected complete-source-cohort negative control.
2026-09-09: V1175-V1179 rejected U1.25 RTL_1V1 escape classes after native
KiCad DRC exposed SPI/5V, exposed-pad GND, or SPISO field collisions. V1180
and V1181 removed those crossings but retained an In2 copper-sliver finding.
V1182 widened the upper-east In2 collector, restoring the single inherited
RTL_3V3 warning. Its saved-board audit now uses native pad/track/via
connectivity and list-based VECTOR2I equality; the U1.25 source-trace negative
control and the three existing 1V1 source-trace controls pass. V1182 is the
accepted U1.25 primitive; remaining RTL9210B support/control closure is open.
2026-09-09: V1183 merged the accepted U1.16 south escape with the accepted
U1.25 upper-east escape. Native DRC remained at the inherited RTL_3V3 warning
plus expected unconnected items. The saved-board audit passed all five 1V1
endpoint assertions and complete source-cohort trace-removal negative
controls. This is the current combined 1V1 basis. The expanded audit also
confirms U1.36/U1.40/U1.50 were already connected through the retained 1V1
field; eight complete source-cohort negative controls pass, so no extra
copper is required for those pads.
2026-09-09: V1184-V1187 rejected U1.52 RTL_3V3 route classes. Native DRC
identified XTAL_IN/1V1, RSET, GND-return, or south-field crossings and
clearance failures. The direct surface corridor class is exhausted; preserve
the four disposable boards/reports and evaluate a designated power-layer
handoff next. V1183's accepted all-eight-pad 1V1 field remains unchanged.
2026-09-09: V1188-V1191 rejected U1.52 RTL_3V3 power-layer handoff trials.
Native DRC found RSET/via clearance, no-net/USB pad-field, crystal/GND-return,
and XTAL/1V1 shorting or crossing failures. The next solution class must
co-author the local XTAL/3V3 departure allocation; the accepted V1183 1V1
field remains unchanged.
2026-09-09: V1192 rejected the first co-authored XTAL_IN/U1.52 RTL_3V3
allocation. Moving XTAL_IN alone crossed XTAL_OUT and left a 3V3-via
proximity conflict plus an orphaned old crystal branch. The next class must
reallocate both crystal transitions together; accepted V1183 1V1/crystal
topology remains unchanged.
2026-09-09: V1195 accepted the paired XTAL_IN/XTAL_OUT transition allocation
with U1.52 RTL_3V3. Native DRC retained only the inherited dangling warning;
the saved-board audit passed U1.52/3V3 and both crystal endpoint groups with
complete source-cohort negative controls. The remaining RTL9210B control,
REFCLK, lane, support, and integrated Path-B gates remain open.
2026-09-09: Reconciled current Path-B headers after V1183. PHASE24_STATUS and
PHASE24_RTL9210B_QUALIFICATION now identify V1183's all-eight-pad 1V1 field as
the live basis; earlier V1160-only wording remains historical context rather
than a current open-pad requirement.
2026-09-09: V1200 accepted the PEDET layer-boundary route on the V1195 basis.
Native DRC retained only the inherited warning; the saved-board audit passed
U1.8/R2.1/J1.69 and its complete source-cohort negative control. PEDET is
locally closed; remaining RTL9210B control, REFCLK, lane, support, and
integrated Path-B gates remain open.
2026-09-09: V1211 accepted the CLKREQ_N edge-corridor primitive after V1210
was rejected for 1V1 and PERST_N launch interactions. Native DRC retained
only the inherited warning; the saved-board audit passed U1.13/R3.1/J1.52
and its complete source-cohort negative control. CLKREQ_N is locally closed.
2026-09-09: V1211 accepted the CLKREQ_N edge-corridor primitive. Native DRC
retained only the inherited warning; the saved-board audit passed
U1.13/R3.1/J1.52 and its complete source-cohort negative control. CLKREQ_N is
locally closed; PERST_N, REFCLK, lane, support, and integrated Path-B gates
remain open.
2026-09-09: V1207 accepted the U1.16 1V1 east rechannel. Native DRC retained
only the inherited warning; its saved-board audit and complete source-cohort
negative control passed. The rechannel preserves the accepted 1V1 field while
freeing the natural CLKREQ source escape; CLKREQ_N and later Path-B gates stay
open.
2026-09-09: V1201-V1203 rejected CLKREQ_N route classes. Native DRC found
reuse/crossing or shorting interactions with PEDET, 1V1, 3V3, SPICLK, and
the lower QFN support field. The next class will use an immediate source
transition and dedicated upper/control lane; accepted PEDET and V1183/V1195
rail/crystal primitives remain unchanged.
2026-09-09: V1208/V1209 rejected CLKREQ source-transition classes. Native DRC
showed retained 5V/SPI or 3V3/1V1 upper-field crossings and an incomplete R3
handoff. Preserve the raw trials; the next class uses a dedicated control-only
edge corridor without changing accepted local power/crystal primitives.
2026-09-09 — PiSXMe Phase 24 RTL9210B Path-B checkpoint V1226. Preserved
Path A and production CAD. V1226 co-authored the U1 CLKREQ_N/PERST_N source
departures, with native KiCad connectivity audits and complete source-cohort
negative controls passing; native DRC retains only the inherited RTL_3V3
dangling warning and expected fixture opens. V1220-V1225 remain rejected
route evidence. REFCLK, lane, remaining support, and integrated Path-B gates
remain open.
2026-09-09 — PiSXMe Phase 24 Path-B V1240 discriminator. REFCLK_P/N native
endpoint connectivity and complete source-cohort negative controls pass after
local QFN rail/ground route objects were isolated. Native DRC shows no
crossings or shorts; support opens are intentional isolation artifacts, so
V1240 is not final closure. The evidence changes the next action to
coordinated rail/ground regeneration around proven REFCLK exits. Path A and
production CAD remain untouched.
2026-09-09 — PiSXMe V1258 complete RTL9210B lane-path checkpoint. Native
saved-board audit proves all four lane pads reach the correct J1 pads and
four source-cohort negative controls pass. Native DRC reports no new lane
shorts, crossings, or clearance errors; inherited disposable support
warnings/opens remain. Support restoration is the next gate.
2026-09-09 — PiSXMe V1256 per-pair ascent checkpoint. Native saved-board
audit proves all four RTL9210B lane pads reach their intended upper
transition vias and four source-cohort negative controls pass. Native DRC
has no new lane shorts, crossings, or clearance errors; incomplete support
warnings/opens are intentional disposable-fixture findings. J1 transitions
remain open.
2026-09-09 — PiSXMe V1255 upper-corridor discriminator. The upper lane
region is largely clear, but a common-layer source ascent weaves across the
four conductors and one REFCLK via. Preserve as route evidence; next use
per-pair layer swaps during ascent.
2026-09-09 — PiSXMe V1252/V1253 full-lane corridor trials rejected. The
middle-board B.Cu trunks are viable, but clustered endpoint vias and long
F.Cu launches conflict with support/control routing and RX connector order.
Preserve V1250 source evidence; next use staggered B.Cu J1 transitions with
short F.Cu dogbones.
2026-09-09 — PiSXMe V1251 outer-corridor trial rejected. Reusing a historical
J1 launch without separate layer transitions caused native same-layer lane
crossings and retained support conflicts. Preserve as route-implementation
evidence; the next lane class uses independent B.Cu trunks and J1-side
vias/dogbones.
2026-09-09 — PiSXMe V1250 refinement checkpoint. The corrected source-only
RTL9210B lane fanout terminates RXN before the lower pair row and keeps the
lower pair escapes clear of the QFN side pads. Native DRC has no new
shorts/crossings/clearance errors; the remaining report entries are inherited
isolation warnings and expected non-lane opens. Full lane corridor closure is
still pending.
2026-09-09 — PiSXMe Phase 24 Path-B V1250 source-field discriminator. A
co-authored isolated RTL9210B QFN source pattern with diverging lane escapes
and ordinary through-vias produces no new native DRC shorts, crossings, or
clearance errors. Preserve V1250 as source-field evidence; the outer
four-pair B.Cu corridor and J1 launch remain open. Path A and production CAD
remain untouched.
2026-09-09 — PiSXMe Phase 24 Path-B lane-source evidence V1245-V1248.
V1245/V1247 failed against live QFN support geometry. V1246 isolated the
source field and V1248 improved the diverging escape pattern, but the outer
TXP path met the RTL9210B SPISI side pad. Preserve these as rejected routing
experiments; V1243 remains the best rail/REFCLK/control support base. Next,
co-author lane exits and side-pad clearance with support restoration.
2026-09-09 — PiSXMe Phase 24 Path-B rail regeneration review. V1241 rejected
historical V1195 copper on the current basis. V1242 passed native endpoint
assertions and source-cohort negative controls but failed native DRC at the
GND/control-field interaction; it remains rejected route evidence. Preserve
V1226 control geometry and continue with a dedicated power-return corridor.
2026-09-09 — PiSXMe Phase 24 Path-B V1243/V1244 checkpoint. V1243 preserves
V1226 control and V1240 REFCLK geometry, regenerates RTL_1V1/RTL_3V3, and
restores GND through a distinct QFN-side transition. Native DRC reports no
new shorts, crossings, or clearance violations; native rail/REFCLK
assertions and negative controls pass. V1244's lane-0 source/outer-row
implementation is rejected for QFN/support/control crossings. Preserve
V1243 as the support base and co-author the next lane escape; Path A and
production CAD remain untouched.
2026-09-09 — Phase 24 RTL9210B V1259-V1261 support restoration evidence:
V1258 remains the accepted, natively audited four-pair U1-to-J1 lane path.
V1259 (bulk donor copper), V1260 (AABB-filtered donor copper), and V1261
(shared F.Cu QFN collector) were rejected by native DRC for real support/lane
shorts, crossings, clearance, duplicate-via, or adjacent-pad contact. These
are disposable route-authoring failures, not Path-B rejection. Next support
class: live-pad staggered dogbones to individual through-vias, then a separate
B.Cu collector. No Path-A or production CAD changed.
2026-09-09 — V1262 partial RTL9210B support escape rejected: native DRC
showed the U1.63 RTL_1V1 dogbone colliding with the accepted LANE0_RXN source
via at (92.8,70.8). This is a coupled lane/support source-field constraint;
next work co-authors that RXN transition and rail escape together. Path A,
production CAD, and the accepted V1258 lane base remain unchanged.
2026-09-09 — V1263/V1264 RTL9210B coupled source-field checkpoint:
V1263 rehomes the LANE0_RXN source transition to (91.0,69.8), freeing the
QFN rail escape window; native endpoint and negative-control audit pass with
only inherited warnings. V1264 adds U1.63 RTL_1V1 on that base; native DRC
adds no errors and the U1.63-to-C4 endpoint/negative-control audit passes.
This is the accepted starting point for the remaining live-pad support
coauthoring. Path A and production CAD remain untouched.
2026-09-09 — V1265 pad-60 RTL_1V1 support attempt rejected: the 0.4-mm QFN
edge pitch cannot accept the proposed 0.10-mm dogbone under the 0.20-mm
minimum trace-width rule, and the alternate route interacted with the live
RXN source field. Do not weaken validation; co-author the package escape
field next. V1263/V1264 remain the accepted basis.
2026-09-09 — V1266 accepted coupled RTL9210B source-field basis: the RXN
transition was rehomed farther west and U1.60/U1.63 RTL_1V1 escapes were
co-authored around it. Native DRC retained inherited warnings only; the
saved-board audit and three negative controls pass. Remaining support is
open; Path A and production CAD remain untouched.
2026-09-09 — V1267 accepted RTL9210B support increment: U1.55 RTL_1V1 was
added to the V1266 live collector through a west-staggered ordinary via.
Native DRC retained inherited warnings only and the saved-board endpoint plus
negative-control audit passed. The current rail cohort is U1.55/U1.60/U1.63;
remaining support is open.
2026-09-09 — V1268 accepted RTL9210B support increment: U1.50 RTL_1V1 was
added through an outward ordinary via to the live west collector. Native DRC
retained inherited warnings only and the saved-board endpoint plus
negative-control audit passed. Current cohort: U1.50/U1.55/U1.60/U1.63.
2026-09-09 — V1269 accepted RTL9210B support increment: U1.40 RTL_1V1
uses a direct outward normal escape to an ordinary via and joins the live
collector. Native DRC retained inherited warnings only; endpoint and
negative-control audit passed. Remaining support is open.
2026-09-09 — V1270/V1271 accepted RTL9210B support increments: U1.36 and
U1.16 RTL_1V1 join the live collector through direct outward ordinary vias.
Native DRC retained inherited warnings only; both saved-board endpoint and
negative-control audits passed. Current cohort: U1.16/U1.36/U1.40/U1.50/
U1.55/U1.60/U1.63.
2026-09-09 — V1272 accepted RTL9210B support increment: U1.25 RTL_1V1
uses an F.Cu source drop and ordinary via to avoid the RXN B.Cu trunk.
Native DRC retained inherited warnings only; endpoint and negative-control
audit passed. The identified RTL_1V1 supply-pad cohort is complete.
2026-09-09 — V1273 accepted RTL9210B RTL_3V3 source increment: U1.34 joins
C3 through a dedicated F.Cu drop, ordinary via, and B.Cu corridor. Native
DRC retained inherited warnings only; endpoint and negative-control audit
passed. Remaining RTL_3V3 and other support are open.
2026-09-09 — V1275 accepted coupled RTL9210B rail evidence: U1.39 RTL_3V3
and U1.40 RTL_1V1 were co-authored with separate source vias/corridors.
Native DRC retained inherited warnings only; combined endpoints and two
source-removal negative controls passed. Remaining rails/support are open.
2026-09-09 — V1276 RTL_5V source attempt rejected: U1.33-to-C5 endpoint and
negative control passed, but native DRC found the source via/escape crossing
and violating clearance to the live RTL_1V1 vertical. Co-author the 5V/1V1
source field next; do not weaken rules.
2026-09-09 — V1277 accepted coupled RTL9210B rail evidence: U1.25 RTL_1V1
continues on B.Cu west of RXN while U1.33 RTL_5V uses a separate F.Cu/B.Cu
corridor. Native DRC retained inherited warnings only; combined endpoints
and two source-removal negative controls passed. Remaining rails/support are
open.
2026-09-09 — V1279 accepted XTAL_IN support evidence: stale donor geometry
was removed and U1.53 was routed to Y1.1 using the live-pad F.Cu path with a
nonadjacent crystal approach. Native DRC retained inherited warnings only;
the endpoint and saved-board negative-control audit passed.
2026-09-09 — V1280 rejected XTAL_OUT route evidence: endpoint connectivity
passed, but the proposed F.Cu/B.Cu escape crossed the accepted RTL_1V1/RXN/
RSET source field and produced native clearance/crossing errors. Raw PCB and
DRC evidence are preserved; XTAL_OUT remains open for a new route class.
2026-09-09 — V1282 corrected a disposable SPICS generator endpoint mismatch;
the native U1.24-to-U2.1 endpoint and saved-board negative control then passed.
The route remained rejected because its first via landed on the TXP launch and
the source field collided with U1.1V1.
2026-09-09 — V1283/V1284 rejected SPICS escape refinements: moving the first
transition between or below the established launch fields still produced
native clearance/short errors at U1.24/U1.1V1. SPICS remains open for a
coupled source-field repair; DRC severity was not changed.
2026-09-09 — V1285 rejected coupled-source evidence: both native endpoint and
saved-board negative-control audits passed, but the co-authored U1.25/U1.24
field still produced B.Cu trunk crossings and QFN source-field clearance/hole
violations. Both nets remain open for a different escape-side topology.
2026-09-09 — V1281 rejected SPICS route evidence: U1.24-to-U2.1 endpoint and
saved-board negative-control audit passed, but native DRC found a crossing of
the RXN B.Cu trunk, collision with the RTL_1V1 via field, and U2.2 clearance
violations. Raw PCB/DRC evidence are preserved; SPICS remains open.
2026-09-09 — V1286 rejected interior SPICS evidence: the U1.24 endpoint and
saved-board negative control passed, but its transition was too close to the
exposed GND pad and crossed validated RXN/RTL_1V1/RTL_5V fields. Raw PCB/DRC
evidence are preserved; SPICS remains open.
2026-09-09 — V1292/V1294 XTAL_IN leg shifts passed native endpoint and
negative-control audits but did not clear the inherited RSET/XTAL_IN DRC
crossing. V1293’s coupled RSET reroute was also rejected for new GND/RXN/1V1
conflicts. The inherited error remains open and all raw evidence is preserved.
2026-09-09 — V1288 rejected coupled-source evidence: both native endpoint and
saved-board negative-control audits passed, but the proposed RTL_1V1 source
via/dogbone at the existing trunk violated the exposed-GND clearance, hole,
and mask rules. SPICS remains open.
2026-09-09 — V1289/V1290 rejected coupled escape evidence: native endpoint and
negative-control audits passed, but alternate RTL_1V1 transitions still
crossed or shorted validated 3V3/5V source fields. SPICS remains open; use a
verified QFN footprint-level escape class next.
2026-09-09 — Footprint-level review recovered V735 as a qualified comparison
basis: U1 at 90 degrees, native DRC zero violations, and independent
SPICS/SPISO endpoint plus source-removal audits passed. It is isolated support
placement evidence, not full Path-B closure or a production replacement.
2026-09-09 — Generated and verified the native geometry receipt
`PHASE24_RTL9210B_V735_V1279_GEOMETRY_COMPARISON.md`. It records the rotated
V735 top-row SPI source geometry versus the V1279 right-row source geometry;
V735 remains support-placement evidence only because its unconnected-pad
findings remain open.
2026-09-09 — Corrected the V1279 status classification: its native DRC carries
an inherited error-level XTAL_IN/RSET crossing. V1291’s single-net RSET repair
passed endpoint and negative-control audits but still failed native DRC on the
crossing and new RSET/GND conflicts; it is preserved as rejected evidence.
2026-09-09 — V1295 first rejected a rotated RTL_1V1/RTL_3V3 source-trio escape
for QFN-field shorts and B.Cu crossings. A bounded source-side correction then
passed native endpoint and saved-board negative-control audits with zero native
DRC violations; the 41 unrelated fixture opens remain. V1295 is accepted as a
rotated source-trio primitive only, not as full Path-B or production closure.
2026-09-09 — V1296 first rejected an RTL_5V upper corridor because it crossed
the native SPISO B.Cu trunk. A bounded dogleg around that trunk then passed
native endpoint and saved-board negative-control audits with zero native DRC
violations; 40 unrelated fixture opens remain. V1296 is accepted as a rotated
rail primitive only, not as full Path-B or production closure.
2026-09-09 — V1297 SPI source-field evidence was rejected after native endpoint
and saved-board negative-control audits passed but the combined SPISI/SPICLK
escape introduced three real layer crossings against RTL_5V and SPISO and at
the rotated QFN source field. Raw fixture and DRC evidence are preserved.
2026-09-09 — V1298 SPI layer-swap evidence was rejected after native endpoint
and saved-board negative-control audits passed but SPICLK still crossed SPISO,
collided with SPISI at the source field, and violated the SPICS transition
clearance. The disposable fixture and native DRC report remain preserved.
2026-09-09 — V1299 consolidated the saved V862 native-clean support basis.
Connectivity was derived from the loaded PCB rather than synthetic graph
edges; SPIs, PERST_N, crystal/RSET/GND support, and RTL_5V all passed endpoint
assertions and trace-removal negative controls. Native DRC remains zero with
30 incomplete fixture items. This is local support closure only; Path-B
integration remains open.
2026-09-09 — V1305 added a saved-board audit for the V862 PEDET and CLKREQ_N
local control paths. Both endpoints and trace-removal negative controls pass;
native V862 DRC remains zero with 30 incomplete items. Full Path-B integration
remains open.
2026-09-09 — V1306 added far-side PEDET/CLKREQ_N launches to M.2 contacts
J1.69/J1.52. Both native endpoint groups and source-removal negative controls
passed; native DRC reports zero violations with 28 unrelated Path-B opens.
Local far-control routing is accepted; full Path-B validation remains open.
2026-09-09 — V1307 REFCLK launch endpoints and negative controls passed, but
native DRC rejected 9 violations against PEDET/CLKREQ_N, U2 support pads, and
connector-side geometry. The pin-order reversal was handled with a layer
transition; REFCLK corridor allocation remains open.
2026-09-09 — V1300 transplanted the native V1195 RSET/XTAL route set onto the
V1279 four-lane basis. Saved-board endpoints and negative controls passed, but
native DRC rejected 29 integrated violations, including XTAL_OUT/RTL_1V1
shorts and XTAL_IN crossings into live RXN/1V1 fields. The experiment is
preserved as route-implementation evidence and V1279 remains authoritative.
2026-09-09 — V1301 RSET source reallocation passed saved-board endpoint and
negative-control checks but native DRC rejected 20 violations, including three
crossings between the new B.Cu RSET handoff and live RTL_1V1 tracks. This
confirms a coupled source-field allocation issue; raw evidence is preserved.
2026-09-09 — V1302 all-F.Cu RSET dogleg passed endpoint and negative-control
checks but native DRC rejected 22 violations, including crossings/shorts with
XTAL_IN, LANE0_RXN, and RTL_1V1. RSET and crystal departures remain a coupled
source-field allocation problem; raw evidence is preserved.
2026-09-09 — V1303 transplanted the accepted V1165 crystal pair onto V1279;
both crystal endpoint and negative-control audits passed, but native DRC
rejected 27 conflicts against live lane/rail geometry. The donor is not
directly compatible and the current four-lane basis remains unchanged.
2026-09-09 — V1304 tested a 20 mm west/10 mm north coherent crystal/RSET
pocket migration. Native DRC rejected 45 violations, including RXN crossings,
source-pad shorts, and XTAL_IN-to-C1 GND contact; its RSET removal heuristic
also failed to prove disconnection. The candidate is rejected and preserved.
2026-09-09 — Phase 24 V1308: tested a fresh RTL9210B lane-0 co-authoring
candidate from the accepted V1243 rail/REFCLK basis. Native endpoint and
four source-cohort negative-control assertions passed, but DRC rejected 39
violations from source-field crossings, retained control/rail B.Cu conflicts,
and connector-side lane shorts/mask bridges. Preserved the disposable board
and raw DRC as rejected route-implementation evidence; no Path-A or
production Path-B assets were changed. Next work must co-author the QFN
source field and J1 launch allocation rather than add another isolated lane
dogleg.
2026-09-09 — Phase 24 V1310: began the rotated-QFN lane solution class from
the V735 source-field oracle. A disposable four-lane U1-to-J1 launch with
separate B.Cu rows was authored and saved-board endpoint/negative-control
audits pass. Native DRC remains the acceptance discriminator; no production
CAD or Path-A assets changed.
2026-09-09 — Phase 24 V1312: refined the rotated-QFN lane fixture with split
source escapes, staggered J1 transitions, and an explicit SPISO bypass.
Native endpoint and four negative-control audits pass; native DRC remains
open as the acceptance discriminator. Production CAD and Path-A assets are
unchanged.
2026-09-09 — Phase 24 V1316 rejected: adding four RTL9210B lanes to the
native-clean V850 rotated-support field passed endpoint and negative-control
audits but native DRC reported 14 source-transition and outer-launch
violations. Preserved the disposable evidence; V850 support and production/
Path-A assets remain unchanged.
2026-09-09 — Phase 24 V1403/V1404 compared a rotated-QFN U1.63 source-field
class. V1403 reached one local DRC crossing on a sparse rotated fixture;
V1404's reroute introduced seven violations against the rotated lane/SPI
field. Neither is production evidence; Path A and accepted V1392 remain
unchanged.
2026-09-09 — Phase 24 V1406/V1407 rejected independent rail implementations.
V1406 RTL_5V upper routing retained four native crossings/shorts; V1407's
localized RTL_3V3 B.Cu power zone retained seven via-clearance/overlap
findings. Accepted V1392 and Path-A remain unchanged.
2026-09-09 — Phase 24 V1316 rejected: adding four lanes to the native-clean
V850 rotated-support field passed endpoint and negative-control audits but
native DRC reported 14 source-transition and outer-launch violations.
Preserved the disposable evidence; V850 support and production/Path-A assets
remain unchanged.
2026-09-09 — Phase 24 V38 rejected: a left-side CM5 USB3 TX_N dogleg removed
the original PER0_P crossing but disconnected J7.140-to-U12.12 and added an
XOUT/JMS_XAVDDH short. Native DRC reported 623 violations / 400 opens.
Preserved the disposable route and report; V37 remains the best valid Path-A
candidate and no production copper changed.
2026-09-09 — Phase 24 V39 corrected the V38 endpoint-via authoring defect,
restoring native USB3 connectivity, but introduced four real shorts in the
long B.Cu TX_N continuation. Native DRC reported 622 violations / 399 opens.
Preserved and rejected the disposable route; complete pair-corridor
regeneration is required next.
2026-09-09 — Phase 24 V40 accepted as the best disposable Path-A USB3
source-field parent so far. An early ordinary-via B.Cu transition for TX_N
removed the V37 PER0 crossing without V39's shorts; USB3/SATA/parity audits
pass and native DRC is 600 violations / 399 opens with zero shorting entries.
No production copper or validation rule changed.
2026-09-09 — Phase 24 V41 accepted as the best disposable Path-A storage
route parent so far. Co-authored U7 SATA TX source transitions reduce native
DRC to 599 violations / 399 opens and clearances to 199, with USB3/SATA/J8
parity PASS and zero shorting entries. No production copper or validation
rule changed.
2026-09-09 — Phase 24 V42 rejected: farther-out U7 SATA TX source vias
preserved SATA endpoint connectivity but introduced real POWER_GND shorts in
the U7 field. Native DRC reported 610 violations / 399 opens. Preserved the
disposable board and receipt; V41 remains the best parent.
2026-09-09 — Phase 24 V44/V45 selector-side SATA TX experiments preserved.
V44 exposed missing transition vias and was corrected as an authoring issue;
V45 passed complete SATA endpoint connectivity and removed the VBUS-field
short, reaching 601 DRC / 399 opens. V45 remains rejected because native DRC
reports one real CM5_USB3_TX_N/CM5_REFCLK_P short at (72.0,106.3). Preserved
boards, scripts, raw reports, and receipts; V41 remains the best disposable
zero-shorting parent.
2026-09-09 — Phase 24 V48 rejected: an upper U7 RX_N jog passed complete SATA
endpoint connectivity but shorted RX_N to the existing BRIDGE_SATA_TX_P via.
Native DRC remained 601 violations / 399 opens. Preserved board, report,
script, and receipt; V46 remains the preferred parent and coordinated U7
RX/TX source-field regeneration is required next.
2026-09-09 — Phase 24 V50 accepted as the best disposable local storage
parent. A right-side Manhattan U7 RX_N dogleg clears the local RX_N/TX_N
crossing with zero native shorting entries; USB3/SATA/J8 parity audits pass
and DRC remains 601 violations / 399 opens. No production PCB, validation
rule, or layer contract changed.
2026-09-09 — Phase 24 V51 rejected: upper selector-side TUSB_SATA_TXP detour
passed SATA connectivity with zero shorts but remained 601 DRC / 399 opens
and added V100-power/opposite-TX crossings and clearances. Preserved board,
report, script, and receipt; V50 remains preferred.
2026-09-09 — Phase 24 V46 accepted as the best coordinated disposable
Path-A parent. It combines the V45 selector-side SATA corridors with a
left-of-REFCLK CM5 USB3 TX_N source transition; USB3/SATA/native J8 parity
audits pass, native DRC is 601 violations / 399 opens, and shorting entries
are zero. Remaining route/support closure is open; no production PCB,
validation rule, or layer contract changed.
2026-09-09 — Phase 24 V47 rejected as a non-improving U7 RX_N escape probe.
Complete SATA endpoint connectivity passed and native shorting entries were
zero, but DRC remained 601 violations / 399 opens and the local RX_N/TX_N
crossing was only relocated. Preserved the disposable board, raw report,
script, and receipt; V46 remains the preferred parent.
2026-09-09 — Phase 24 V43 rejected after correcting a coordinate-authoring
 typo. The corrected U7.57 TX_P source-field escape produced native DRC 605
 violations / 400 opens, with real POWER_GND-to-TX_P shorts; SATA endpoint
 connectivity failed at U7.57 while USB3 remained PASS. Preserved the board,
 raw DRC, and receipt; V41 remains the best disposable parent and no
 validation rule or production PCB changed.
2026-09-09 — Phase 24 V52 rejected: direct F.Cu TUSB_SATA_TXP passed SATA
endpoint connectivity but worsened native DRC to 604 / 399 and introduced
three real support-net shorts. Preserved board, report, script, and receipt;
V50 mixed-layer routing remains preferred.
2026-09-09 — Phase 24 V55/V56 ground-stitch experiments preserved and
rejected. V55 reduced opens to 347 but introduced true shorts; V56 removed
the M.2-colliding stitch and reached 598 DRC / 347 opens, but retained a
MODE_IN/STORAGE_SEL short. V54 remains the clean zero-shorting parent; no
production authority or validation rule changed.
2026-09-09 — Phase 24 V57 rejected: STORAGE_SEL mode-support escape passed
mode/SATA audits but introduced three real shorts to U12/U13 POWER_GND and
TUSB_SATA_TXN; native DRC was 614 / 350. Preserved board, report, script,
and receipt; V54 remains the clean parent.
2026-09-09 — Phase 24 V53 preserved as a promising storage ground-return
parent. A bounded F.Cu POWER_GND zone reduced native opens from 399 to 355
with zero shorts and preserved USB3/SATA connectivity, but introduced 10
starved-thermal findings and raised total DRC to 611. No signal, authority,
or validation rule changed; deliberate stitching/thermal cleanup remains.
2026-09-09 — Phase 24 V58/V59 ground-stitch validation preserved. V58's
single corner POWER_GND via exposed three real shorts after refill and was
rejected; V59's no-geometry refill control reproduced V54 at 601 DRC / 350
opens with zero shorts. V54 remains preferred; no validation rule changed.
2026-09-09 — Phase 24 V60/V61 mode-support and ground-stitch continuations
preserved and rejected. V60 exposed an NC26/STORAGE_SEL short after one
outboard stitch; V61's right-corridor mode route exposed U13 NC41/STORAGE_SEL
and XOUT/JMS_XAVDDH shorts at 610 DRC / 348 opens. V54 remains the clean
parent; no production authority or validation rule changed.
2026-09-09 — Reconciled PHASE24_STATUS.md with live storage routing evidence:
V50 is the preferred disposable Path-A parent; V51 and V52 are rejected
experiments; V50's USB3/SATA/parity PASS and native 601 DRC / 399 opens with
zero shorts remain current. No production authority or validation rule
changed.
## 2026-09-09 — Phase 24 storage clock-field experiments

V63–V68 preserved a bounded Path-A storage routing investigation. V67
co-authored the U11 XOUT/JMS_XAVDDH transition and removed the prior clock
short, but native DRC still found a selector-side NC_26/STORAGE_SEL short;
V68 confirmed the issue without zone refill. Neither candidate was promoted;
V54 remains the preferred clean storage parent. Path-B RTL9210B qualification
remains isolated and unchanged.
V69-V71 tested three `STORAGE_SEL` bypasses around U13/U14; none was promoted.
V71 removed the selector NC-pad short but introduced a JMS_AVDDL/POWER_GND
collision. V54 remains the preferred parent.
Current RTL9210B marketplace checks added corroborating small-quantity leads,
but did not close authorized lot, firmware-rights, or virgin-programming risk.
Path B remains isolated and Path A remains preserved.
The 2026-09-10 JMS583 support triage was corrected for each audit's actual
input contract; support authority, VBUS divider, and VCCO zone now pass with
negative controls against the V54 saved board. The apparent failures were
tool invocation errors, not design evidence.
V75 connected the native U7.39-to-R24.2 BRIDGE_R1RTN pads; DRC stayed at 601,
opens fell to 349, and no shorts were introduced. USB3/SATA/parity remained
passing, so V75 is the preferred disposable storage parent.
The 2026-09-10 RTL9210B V1460 coupled QFN experiment co-authored U1.66 GND
with LANE0_RXN and retained 15 native DRC violations against adjacent
lane/JTAG copper. It was rejected without rule relaxation; Path A stayed
intact.
RTL9210B V1461 co-authored all four lane-0 source corridors with U1.66 GND;
native DRC retained 19 violations, so it was rejected without rule relaxation.
Fresh V54 native gate audit on 2026-09-10 recorded 601 DRC violations and
350 opens with no shorts; focused USB3/SATA/parity/support/VBUS/VCCO audits
pass with negative controls. No Phase 24 findings were waived.
V76/V77 attempted the adjacent BRIDGE_R1 support pair and were rejected for
native source-field shorts; V75 remains the clean parent.
2026-09-10 — V78 tested a separated BRIDGE_R1 via column/shelf against V75.
Native DRC exposed JMS_AVDDL/POWER_GND and BRIDGE_R1/BRIDGE_R1RTN shorts at
605 violations / 349 opens. V78 was rejected; V75 remains preferred and no
rules or production CAD changed.
2026-09-10 — V80 tested co-locating/rotating R24 beside U7. Native DRC
reported 614 violations / 349 opens and exposed POWER_GND/BRIDGE_R1 and
POWER_GND/BRIDGE_R1RTN shorts. V80 was rejected; V79 remains preferred.
The blocker narrative was updated to include V78 as rejected evidence, keeping
the current M.2 power-source gap and V75 preference explicit.
2026-09-10 — Applied the source-level storage power-owner correction to the
live root/child schematic. Native netlist export puts all nine J3 M.2 power
contacts on STORAGE_3V3. V79 materialized that ownership on V75 and passed
814-node / 1263-pad parity with zero mismatches; native DRC remained 601 / 350
with no shorting section. Full storage routing and Phase 24 remain open.
2026-09-10 — Live V75 inspection found a genuine M.2 power-source gap:
J3's M2_3V3 contacts have no source-owned pad, track, or zone, while
STORAGE_3V3 is the existing regulator-owned rail. A disposable source-level
reconciliation renamed only the nine J3 instance labels and storage hierarchy
boundary, passed the schematic/mode audits, and removed the M2 hierarchy
finding in the fixture. It was not promoted pending coordinated source
regeneration, rail-budget review, and native PCB revalidation; no PCB-only
repair or validation waiver was made.
2026-09-10 — Added a native saved-board M.2 power-owner audit with a real
trace-removal negative control. It exposed that V79's nine correctly named J3
power pads were not physically connected. V81 broad-zone and V82 ordinary-via
trunk trials were preserved; V82 passed physical connectivity but was rejected
by native DRC for new rail shorts/crossings. No rules were weakened. Receipt:
`PHASE24_STORAGE_M2_POWER_OWNER_V81_V82_RECEIPT.md`.
2026-09-10 — V83 moved the M.2 storage-rail trunk to In1 power copper. Native
connectivity and the negative control passed, but ordinary through-vias still
collided with existing B.Cu storage/SATA copper; native DRC reported 613 / 341
with real STORAGE_3V3 shorts. V83 was rejected; no rule relaxation.
2026-09-10 — V84–V86 moved M.2 power drops around the existing Ethernet CT
support and were rejected for successive real rail shorts. V87 moved farther
outboard: all nine J3 contacts and the improved native negative control pass,
with no new STORAGE_3V3 shorting entry, but native DRC remains 608 / 341
versus V79 601 / 350 due added source/QFN clearance findings. V87 remains
disposable; no production promotion or rule relaxation.
2026-09-10 — Refilled V79 as a matched native baseline. V89's U14.5 power
source trial still passes focused connectivity, but its regenerated board
adds an XOUT/JMS_XAVDDH short absent from the matched V79 baseline. V89 is not
accepted; the discrepancy is recorded for route/regeneration diagnosis.
2026-09-10 — V88 tested a local F.Cu filled source pickup for the M.2 rail.
The native nine-contact audit and negative control passed, but DRC stayed
608 / 341 and added selector-field shorts. V88 was rejected; V87 remains
the best disposable trial.
2026-09-10 — V89 sourced the M.2 rail from existing non-QFN U14.5 instead of
probing the JMS583 QFN. Native schematic/mode, USB3, SATA, and nine-contact
power-owner audits plus the trace-removal negative control pass. DRC is 607 /
341 with only the inherited XOUT/JMS_XAVDDH shorting entry. V89 is the best
disposable physical-power candidate; full-board gates remain open.
2026-09-10 — Isolated the V89 native DRC anomaly: U14.5 source pickup alone
does not reproduce the XOUT/JMS_XAVDDH short, while the J3-side drop class
does. V89 remains rejected; connector-field power access needs a new route
class. Evidence: `PHASE24_STORAGE_V89_ISOLATION_RECEIPT.md`.
2026-09-10 — Regenerated the storage disposable parent with the reviewed U13
exposed-pad POWER_GND authority and source-corrected J3 STORAGE_3V3 ownership.
V91 is 596 / 350 with no shorting section. V92's no-via F.Cu perimeter rail
connects all nine J3 power contacts; native USB3/SATA/parity/power audits and
the trace-removal negative control pass. DRC is 597 / 341 with one added
crossing. V92 is disposable; full gates remain open.
2026-09-10 — V93 attempted complete storage-rail In1 plane access with
ordinary-via dogbones. It failed J3 physical connectivity and introduced real
STORAGE_3V3 shorts; native DRC 619 / 344. V93 was rejected, confirming that a
broad plane needs a coordinated island/via redesign. V92 remains preferred.
2026-09-10 — V94 replaced V92's J3 same-net horizontal joins with individual
vertical F.Cu dogbones into a south bus. Native power/negative-control,
parity, USB3, and SATA audits pass; DRC remains 597 / 341 with no rail shorts.
V94 is now the preferred disposable storage-power basis; full gates remain.
2026-09-10 — Phase 24 storage rail branch trials V95–V102 were preserved as
rejected evidence. The saved-board M.2 power-owner audit and trace-removal
negative control passed on each trial, but native DRC retained true opens and
introduced/retained rail, selector, SATA, or XOUT shorts. V94 remains the
best disposable basis; production promotion is not authorized.
The storage power audit was strengthened with `--strict-sources`; it uses only
saved pads/tracks/vias/zones and exposes the remaining fragmented source fanout
on V94/V102.
V103/V104 demonstrated strict native source co-connectivity through an In2
storage plane, but native DRC still found real shorts; neither is promoted.
V105's selector-only outer-corridor re-route was also rejected at native
614/341; no production routing was promoted.
V106–V108 preserved selector-rotation diagnostics; the stripped fixture
confirmed that future pin-9 routing requires explicit package/DFM rule
authority, so no integrated rotation was promoted.
The V109–V111 comparison used the repository's existing JLC rule profile and
showed the selector package can be routed at the documented 0.15/0.13208-mm
limits, but the integrated storage board still has real opens and shorts.
V112 preserved the V62-style selector reroute as rejected evidence at native
268/341; no long selector detour was promoted.
V113 showed the placement generator still retains donor copper after storage
component replacement (297/499, crossings); a targeted copper regeneration
stage is required before any placement candidate can be promoted.
V114 implemented the storage-owned copper scrub; V115's native-pad USB3
regeneration was rejected at 403/499 for source-field shorts/crossings. This
is router/source-alias evidence and did not change production CAD.
V116 corrected scrub ownership to use canonical hierarchical net leaves and
verified zero remaining storage-owned tracks natively; its JLC-profile DRC
was 262/499. V117 propagated the matcher into the USB3 rerouter but was
rejected at 405/499 for true J7 source-field shorts/crossings. The A* endpoint
halo is incompatible with the 0.4-mm connector pitch; the next route class is
the existing explicit monotonic dogbone escape retargeted to U12.
V118 retargeted that dogbone concept to U12 in a J7/U12-only fixture and was
rejected at 14/63: source transitions shorted RX pair nets and TX corridors
crossed. This remains route implementation evidence; the next candidate must
separate pair transitions and layer corridors before U12 entry.
V119 reduced the A* terminal halo to one grid cell. It stopped the false
pad-clearing behavior but found no route for the second CM5 USB3 source under
the coarse occupancy model; no output copper was accepted. The safe next
class is an explicit pair-aware source escape outside the dense connector
field, checked by native DRC.
V121 provided that isolated source-escape result: native DRC had zero
violations, all four J7-to-U12 USB3 endpoints passed saved-board
BuildConnectivity, and a removed-segment negative control failed as required.
It is route-development evidence only; integrated continuation remains open.
V123 integrated the V121 source escape with a local CM5_PERST B.Cu duck and
removed all USB3 shorts/crossings; native DRC remained 300/499 from
via/plane and other clearance findings. V124 reintroduced pair shorts and
crossings and was rejected. The next candidate must keep the V123 PERST
result while making the transitions compatible with filled planes.
V127 moved storage-local R80 out of the USB3 corridor. Native DRC improved to
146/499 with no shorts, crossings, or track-width findings, and all four
J7-to-U12 endpoint assertions passed. Support routing and full-board closure
remain open.
V134 moved only U13 outboard to test whether it occupied the natural support
escape region. Native DRC remained 207/499 with real USB_DP/USB_RX/JMS_VCCO
shorts and crossings, so U13 alone is not the root cause. V134 is rejected;
the next support candidate must change layer/escape ownership. Receipt:
`PHASE24_STORAGE_SUPPORT_U13_V134_RECEIPT.md`.
V136 reduced the V135 package-aware support experiment to U11/U12/C86/C87.
All six local support endpoint assertions passed from native saved-board
connectivity, while native DRC retained one U11 source-via clearance and one
U12 target crossing under the active JLC profile. V136 is rejected and remains
disposable evidence; production support copper is not promoted. Receipt:
`PHASE24_STORAGE_SUPPORT_LAYER_OWNED_V136_RECEIPT.md`.
V137 tested an inner-side U12 TXN launch after the U11 source dogbone was
staggered. Native DRC rejected the route at 9 local violations, including
U12 POWER_GND/NC collisions; this is disposable route evidence, not a waiver
or production promotion. Receipt:
`PHASE24_STORAGE_SUPPORT_TARGET_LAUNCH_V137_RECEIPT.md`.
V138 rotated U12 by 180 degrees as a distinct disposable launch class. Native
connectivity remained present for all six local support nets, but DRC retained
two target-via shorts and two silk warnings. V138 is rejected; production
copper remains unchanged. Receipt:
`PHASE24_STORAGE_SUPPORT_U12_ROT180_V138_RECEIPT.md`.
V139 tested ordered B.Cu lanes and above-row U12 target vias. Native local
support connectivity remained present, but DRC retained six target
crossing/clearance findings and two silk warnings. V139 is rejected; the next
candidate changes U12 orientation. Receipt:
`PHASE24_STORAGE_SUPPORT_TARGET_ABOVE_V139_RECEIPT.md`.
V140 tested a 90-degree U12 orientation in a stripped local fixture. Native
DRC rejected the transform-reused launch at 19 violations, including real
U12 pad-field shorts/crossings. V140 is rejected; production CAD remains
unchanged. Receipt:
`PHASE24_STORAGE_SUPPORT_U12_ROT90_V140_RECEIPT.md`.
V141 repeated the 90-degree U12 orientation with separated transformed target
vias. Native DRC rejected it at 21 violations, including real corridor and
U12 pad-field shorts/crossings. It remains disposable evidence; production
CAD is unchanged. Receipt:
`PHASE24_STORAGE_SUPPORT_U12_ROT90_V141_RECEIPT.md`.
V143 tested direct U12 F.Cu exits with widely separated vias and ordered B.Cu
lanes. Native DRC rejected the reduced fixture at 17 violations, including
real U12 ground/pad-field shorts. V143 is rejected and remains disposable
evidence; production copper is unchanged. Receipt:
`PHASE24_STORAGE_SUPPORT_DIRECT_U12_V143_RECEIPT.md`.
V144 corrected the transformed 180-degree U12 target coordinates, but native
DRC still found 13 violations / 32 fixture opens, including real pair
crossings, TX-pair shorts, RX-pair shorting, and target-field clearances. It
is rejected route-implementation evidence. A documentation-hygiene pass also
reconciled current Path-A JMS583 support and Path-B RTL9210B state against
live artifacts without editing raw evidence. Receipt:
`PHASE24_DOCUMENTATION_HYGIENE_20260910.md`.
V147 tested RX without U12 target-side vias using native endpoints. The naive
same-row U11 F.Cu shoulders passed local endpoint reachability but native DRC
rejected 36 violations / 32 fixture opens, including source-field crossings.
It is rejected route-authoring evidence; the RX-without-target-vias class
remains a valid next implementation hypothesis. Receipt:
`PHASE24_STORAGE_SUPPORT_U12_TARGET_RX_FCU_V147_RECEIPT.md`.
V148-V150 continued the source-aware target-field work. V150 combined far RX
transitions with a staggered TX launch and reduced the local fixture to 9
native violations with no shorting entries; target-field crossings and
clearances remain. It is the best disposable basis, not a pass. Receipt:
`PHASE24_STORAGE_SUPPORT_U12_COAUTHOR_TX_RX_FAR_V150_RECEIPT.md`.
V154 completed the native-pad-derived U12 target field: native DRC is zero,
all six local support endpoints pass, and a saved-board removed-track
negative control fails as required. The 32 remaining opens are intentional
stripped-fixture residue; V154 is accepted as a local primitive, not board
closure. Receipt:
`PHASE24_STORAGE_SUPPORT_U12_COAUTHOR_TX_RX_FAR_V154_RECEIPT.md`.
V156 tested a coherent C86/C87 cap-shelf translation in the integrated V127
descendant. All ten USB3/support endpoints passed, but native DRC found 155
findings including PERST crossings and TX/support shorts. It is rejected as
an uncoauthored transplant; V154 remains the accepted local primitive.
Receipt: `PHASE24_STORAGE_SUPPORT_CAP_CLEAR_V156_RECEIPT.md`.
V157 coauthored C86/C87, TX/RX source transitions, and target trunks, but
native DRC remained 155 with a PERST/BRIDGE_3V3 short and source-field
crossings. It is rejected integrated route evidence; V154 remains the
accepted local primitive. Receipt:
`PHASE24_STORAGE_SUPPORT_CAP_PERST_COAUTHORED_V157_RECEIPT.md`.
V158 tested a coherent cap/PERST-aware support transplant. All ten endpoints
passed, but native DRC remained 153 with source-field crossings and a
PERST/BRIDGE_3V3 short. It is rejected integration evidence; V154 remains
the accepted local primitive. Receipt:
`PHASE24_STORAGE_SUPPORT_COHERENT_CAP_PERST_V158_RECEIPT.md`.
## 2026-09-10 — Phase 24 V182 integrated USB3 support

- Corrected the V154-derived U11/U12 storage USB3 support generator using
  native pad-derived routing. The RXN source now hands off on a north/outboard
  B.Cu lane, avoiding the RXP shelf, TX field, and CM5_PERST corridor.
- `PHASE24_STORAGE_SUPPORT_U12_COAUTHOR_TX_RX_FAR_V180.kicad_pcb` is a native
  DRC-clean stripped fixture (0 violations; 32 intentional opens).
- `PHASE24_STORAGE_SUPPORT_COHERENT_CAP_PERST_V182.kicad_pcb` is the accepted
  integrated support candidate: ten endpoint assertions and the removed-track
  negative control pass; native DRC is 146/499, identical to the V127 ancestor.
  No inherited finding was waived and Phase 24 remains open.
- A disposable transplant of V182 onto the complete V75 Path-A storage parent
  passes USB3, SATA, parity (814/1263/0), and the negative control, but native
  DRC is 630/346 versus V75's 601/349. It is retained for coauthoring and not
  promoted because 29 real inter-island interactions were introduced.
- V186 regenerated the support directly on V75 and moved the RXP transition
  north of AVDD33. USB3, SATA, parity, and the negative control pass; DRC is
  628/346, but five real shorts remain. Retain as route-development evidence.
- V192 moved the RXN north handoff column left, removing the CM5 RX-N and SATA
  RXP shorts while preserving USB3, SATA, parity, and the negative control.
  Native DRC remains 628/346 with three real shorts at XOUT/JMS_XAVDDH and
  STORAGE_SEL/U13/U12; retain as the current coauthoring basis.
- V193 replaced the direct STORAGE_SEL branch with a local U12/U13 handoff and
  north/outboard B.Cu trunk. USB3, SATA, parity, and the negative control pass;
  native DRC is 624/346 with two real shorts remaining at XOUT/JMS_XAVDDH and
  STORAGE_SEL/U14/U12.
- V194 replaced the XOUT route with a north-going native escape and verified
  U11.51-to-Y10.2 connectivity. USB3, SATA, parity, and the negative control
  pass; DRC remains 624/346 with one JMS_AVDDL/JMS_AVDD33 field short.
- V196 coauthored the AVDDL handoff around the AVDD33 field and verified
  U11.20-to-C83.1. USB3, SATA, parity, and the negative control pass; native
  DRC is 617/347 with zero shorting items. Remaining opens/crossings stay open.
## 2026-09-10 — Phase 24 RTL9210B V1466 QFN escape primitive

- Tested the native-loaded RTL9210B QFN coordinates rather than relying on
  stale route assumptions. V1466 moves U1.64/RXP east/up to an ordinary
  through-via and joins U1.66/GND directly to the bottom edge of exposed pad
  U1.69, with no via-in-pad or rule relaxation.
- Native KiCad 10.0.5 DRC is 0 violations / 9 inherited support opens. All
  four lane-0 endpoints and U1.66-to-U1.69 connectivity pass; independent
  saved-board removal of the GND join or RXP source trace fails as required.
- V1466 supersedes V1461 for this local Path-B escape only. Full RTL9210B
  support, firmware/programming, integrated storage, and Phase 24 closure
  remain open; Path A is preserved.
## 2026-09-10 — Phase 24 RTL9210B V1469 lower-field primitive

- V1467/V1468 were rejected lower-field route attempts. V1469 retained U1.60,
  added the true U1.63 RTL_1V1 departure, and rehomed RXN around the live QFN
  source field.
- Native KiCad DRC is 0 violations / 8 inherited opens. U1.63-to-C4.1,
  U1.66-to-U1.69, and all four lane endpoints pass saved-board connectivity;
  independent rail/RXN trace-removal negative controls fail as required.
- V1469 is the current accepted isolated Path-B lower-field basis. Full
  support, firmware/programming, integrated storage, and Phase 24 remain open.

## 2026-09-10 — Phase 24 RTL9210B GND-return corridor discriminator

- V1470–V1476 tested seven distinct local GND-return classes against the live
  V1469 QFN/lane/rail field. All were rejected by native DRC; raw reports and
  PCBs are preserved in the consolidated receipt.
- These are route-implementation failures, not architecture evidence. V1469
  remains the accepted zero-DRC isolated lower-field basis; the next attempt
  must coauthor the plane/return field rather than add another long collector.

## 2026-09-10 — Phase 24 RTL9210B V1491 GND return field

- V1477–V1479 perimeter launches and V1480–V1487 direct-pocket variants were
  rejected by native pad/support clearance or routing findings and remain
  preserved as raw evidence.
- V1491 coauthored the live RTL_3V3 B.Cu shelf and used the existing QFN GND
  copper to launch one ordinary 0.50/0.30 mm through-via into an intentional
  In1 GND return field. Native KiCad DRC reports 0 violations / 7 inherited
  opens.
- Native saved-board connectivity joins U1.45/U1.66/U1.69 to the remote GND
  field. Removing the QFN-to-In1 stitch fails the independent negative
  control. This is an accepted isolated Path-B primitive; RSET, crystal,
  REFCLK, firmware, procurement, integration, and Path-A comparison remain
  open. Path A is unchanged.

## 2026-09-10 — Phase 24 RTL9210B V1508 coordinated RSET escape

- Independent review identified the RSET failure as a support-field capacity
  problem: the GND triangle, RTL_3V3 shelf, and RTL_1V1 lane were authored
  independently and boxed in U1.51. Path B was not rejected.
- V1502 replaced the obsolete GND triangle with one intentional In1 GND field
  and retained native DRC at 0 violations / 7 inherited opens.
- V1508 routed RSET from native U1.51 `(94.8,66.05)` to R1.1 `(88,65)` with
  one ordinary through-via and a short F.Cu hop around the RTL_1V1 barrier.
  Native DRC is 0 violations / 6 inherited opens; saved-board connectivity
  and the RSET-transition negative control pass. Remaining crystal and
  REFCLK groups, firmware, procurement, integration, and A/B comparison stay
  open. Path A is unchanged.

## 2026-09-10 — Phase 24 RTL9210B XTAL_IN trials V1509-V1511

- V1509-V1511 tested southwest, north, and staggered two-layer XTAL_IN
  departures against the accepted V1508/V1502 support field.
- All were rejected by native DRC for live RTL_1V1/RTL_3V3 or PCIe crossings;
  no rule relaxation or production change was made. The next repair remains
  coordinated support-field regeneration. XTAL_IN, XTAL_OUT, REFCLK, and full
  Path-B gates remain open.

## 2026-09-10 — Phase 24 RTL9210B XTAL_OUT trials V1512-V1514

- V1512-V1514 tested north, barrier-hop, and source-jog XTAL_OUT escapes on
  V1508/V1502. Native DRC rejected all three for live RTL_1V1/RTL_3V3 source
  field conflicts. They remain route evidence only; Path A and accepted Path-B
  primitives are unchanged.

## 2026-09-10 — Phase 24 RTL9210B V1517 U1.55 rail rehome

- The live U1.55 RTL_1V1 escape was rehomed to the existing `(92.8,69.8)`
  via pocket, removing its old leftward source field and dangling tail.
- Native DRC is 0 violations / 6 inherited opens. Native U1.55/U1.63
  connectivity and source-removal negative control pass. Crystal, REFCLK,
  firmware, procurement, integration, and full Path-B gates remain open.

## 2026-09-10 — Phase 24 RTL9210B V1523/V1526 crystal-field progress

- V1523 rehomed U1.52 RTL_3V3 around the crystal pocket with native DRC 0 / 6
  opens; V1526 completed XTAL_OUT through C2.1/Y1.2 with native DRC 0 / 4.
- Saved-board connectivity and independent trace-removal negative controls
  pass for both accepted changes. V1527 was rejected for XTAL_IN GND-stitch
  and RTL_3V3-field collisions and is retained as route evidence.
- XTAL_IN and REFCLK_P/N remain open; no Path-A or production CAD changed.

## 2026-09-10 — Phase 24 RTL9210B V1532 crystal layer split

- V1532 tested a layer-split crystal pair. Native DRC rejected five QFN
  field/RSET/transition violations; it remains route evidence only.
- V1523/V1526 remain the accepted isolated basis. No Path-A or production CAD
  changed.

## 2026-09-10 — Phase 24 RTL9210B V1547 crystal source sweep

- V1547 generated and native-checked 16 crystal source variants from V1523.
- The best class uses XTAL_OUT x=91.4 mm plus a B.Cu XTAL_IN middle section,
  but all four XIN transitions retain one adjacent-source clearance violation.
- Coordinate-only tuning is exhausted for this class; source departure or
  layer allocation must change. Path A and production CAD remain unchanged.

## 2026-09-10 — Phase 24 RTL9210B V1534/V1535 crystal coexistence

- V1534 independently routes complete XTAL_IN on V1523 with native DRC 0 / 4
  opens, proving the XIN route class when isolated.
- V1535 retains XIN but rejects east/B.Cu XTAL_OUT coexistence with four local
  RSET/RTL_3V3/crystal-field violations. Evidence is preserved; coordinated
  crystal-field regeneration remains next and no production CAD changed.

## 2026-09-10 — Phase 24 current-state documentation hygiene

- Added explicit current-state overrides to the Phase 24 status, dual-mode
  implementation, and RTL9210B QFN documents.
- JMS583 support-network instantiation is now clearly current completed work;
  older instantiation/TODO wording is marked superseded historical evidence.
- RTL9210B V1517 is identified as the live accepted local basis, replacing
  stale V1428/V1461 “latest” language; remaining crystal/REFCLK and broader
  Path-B gates remain open. Raw evidence was not rewritten.

## 2026-09-10 — RTL9210B crystal escape V1549–V1553

- Ran five isolated rotated-QFN crystal/source-escape fixtures with native
  KiCad DRC. All were rejected: the best V1553 still has four violations,
  with XTAL_IN/XTAL_OUT shorting adjacent RTL_3V3/RTL_1V1 source pads; the
  stripped fixtures intentionally retain 17 unconnected items.
- Preserved raw PCBs/reports and recorded the result in
  `PHASE24_RTL9210B_CRYSTAL_ESCAPE_V1549_V1553_RECEIPT.md`.
- The tested escape class is closed as rejected; Path A and accepted Path-B
  primitives remain unchanged. Next work must use a new authoritative QFN
  fanout class without relaxing board rules.

## 2026-09-10 — RTL9210B outer-side crystal escape V1557

- Tested an outer-side source escape that separated XTAL_IN and XTAL_OUT
  around the QFN. Native DRC reported 17 violations / 4 opens, including
  source/top-row and rail-field conflicts; it is rejected.
- Two materially distinct source-escape classes are now exhausted under the
  unchanged 0.20-mm trace/clearance and ordinary-via contract. The next Path-B
  step must change the authoritative fanout strategy, not repeat coordinate
  tuning or relax rules.

## 2026-09-10 — RTL9210B far-outboard XIN V1558

- Rebuilt the former far-outboard XTAL_IN idea from the current V1523 native
  basis. KiCad 10 native DRC reported 11 violations / 5 opens, including
  source-to-rail/GND conflicts and upper-return crossings; the candidate is
  rejected.
- Path-A focused audits continue to pass on its current basis. RTL9210B Path B
  remains isolated; the next experiment requires a different package/fanout
  strategy, not another coordinate-only adjustment or rule relaxation.

## 2026-09-10 — Phase 24 U5 connectivity revalidation V1559

- Re-ran the saved-board U5 audit against native pads, tracks, vias, and zones.
  U5.9-to-C44–C47.1 and the POWER_GND group pass; removing a necessary trace
  fails the audit as required.
- Preserved the result in `PHASE24_U5_LAYER_CONNECTIVITY_V1559_RECEIPT.md`.
  The audit's via handling was corrected so the rerun no longer invokes the
  KiCad via-width binding assertion path.

## 2026-09-10 — Phase 24 integrated native DRC V1559

- Fresh KiCad 10 native DRC on `PHASE24_PGND_CLUSTER_CURRENT.kicad_pcb`
  reports 443 violations / 254 unconnected items. The board remains open;
  no severity or rule was changed.
- Preserved raw output in `PHASE24_PGND_CLUSTER_CURRENT-V1559-drc.rpt` and
  summarized it in `PHASE24_PGND_CLUSTER_CURRENT_V1559_NATIVE_DRC_RECEIPT.md`.

## 2026-09-10 — RTL9210B crystal source class V1555–V1556

- Tested two further 0-degree QFN escape topologies at the required 0.20-mm
  trace width. V1555 produced six native DRC violations; V1556 produced
  eleven. Failures are local source/supply fanout and layer-shelf conflicts.
- Closed this coordinate-only source class as rejected and preserved its raw
  fixtures/reports. Next RTL9210B work must change the authoritative fanout
  topology or footprint strategy; no design-rule relaxation is accepted.

## 2026-09-10 — RTL9210B Path-B parallel comparison V1560

- Added `PHASE24_RTL9210B_PARALLEL_COMPARISON_V1560.md` as the current
  apples-to-apples decision record. Path A is preserved; Path B is a serious
  isolated candidate and the recommendation is `CONTINUE BOTH`.
- Reconciled the qualification/status headers and Path-B authority package so
  V1549–V1558 are clearly rejected route experiments rather than production
  authority or an architecture rejection. Technical pin/mapping/netlist
  audits pass; source-field routing, authorized package/support evidence,
  provisioning, firmware rights, procurement, and full validation remain open.

## 2026-09-10 — Path-A M.2 power handoff V1562

- Added a disposable pad-derived `STORAGE_3V3` handoff using ordinary vias
  and a designated In2 power spine. The native power-owner audit and its
  necessary-trace negative control pass for all nine J3 power contacts.
- The candidate has 603 native DRC violations / 342 unconnected items from
  its open parent, with no new storage-rail shorting section. It is retained
  as a focused primitive, not promoted as a board pass.
- The V1562 board also passes the focused SATA, USB3, selector-geometry,
  JMS583-support, and JMS_REXT audits; these remain local regression checks,
  not full-board closure.
- A fresh like-for-like V79 native DRC baseline is 602 violations / 351
  unconnected items. V1562 is 610 / 342: nine opens are removed at the cost
  of eight DRC findings, with no new storage-rail shorting/crossing section.
- V1562 was corrected to cluster the tightly spaced J3 contacts onto two
  ordinary through-vias; the corrected rerun retains the audit PASS and has no
  new via hole-spacing violation or storage-rail shorting section.

## 2026-09-10 — Phase 24 status reconciliation V1562

- Updated `PHASE24_STATUS.md` with the live V1562 focused storage result,
  focused audit set, and like-for-like DRC delta. Full-board closure remains
  open and the primitive is not promoted.
