# RTL9210B Path-B QFN field disposition

## CURRENT STATE — 2026-09-10 V1583

V1581 and V1582 are the latest fixed-orientation REFCLK trials and are both
rejected. V1581 produced 6 native DRC violations / 4 opens, including two
REFCLK shorts. V1582 produced 15 violations / 4 opens, including crossings
through RSET, RTL_3V3, RTL_1V1, and a REFCLK_N-to-RTL_1V1 short. Their raw
boards and reports are retained in the repository. These are source-field
implementation failures; they do not reopen the accepted Claude V1575
orientation decision.

V1583 also rejected an outer-board REFCLK overlay with 27 native DRC
violations, including source/lane crossings and J1-side launch conflicts.
The V1584–V1588 obstacle-aware source-field diagnostic then found individual
native paths but no complete six-net field: one pair-order found five paths
and no legal sixth path. It is diagnostic evidence, not a promoted route.
V1589 then removed the complete disposable local source-field rail/return
copper and still found only four of six paths before REFCLK_N had no legal
remaining path. This narrows the remaining issue to the combined QFN escape
and J1 launch topology, not merely inherited rail congestion.
V1590 isolates the package escape: all six U1 high-speed pads reach explicit
west handoff pads with native saved-board connectivity and six trace-removal
negative controls. Native DRC has no shorts or crossings; its remaining
warnings/opens are intentional stripped-support fixture findings. This local
primitive is accepted, but full support/J1 launch integration remains OPEN.
V1591 then searched from those handoffs to the actual J1/M.2 contacts and
placed four nets before no legal remaining launch existed. The residual issue
therefore follows the M.2/J1 launch field as well as the source-field
coauthoring; no complete candidate was promoted.
V1592 corrected the endpoint-pad model and found complete paths for all six
nets, but native DRC rejected the resulting centerline/via geometry with 594
clearance violations. The endpoint correction is retained; the planner's
multi-net separation remains open.
V1594 improved centerline spacing and generated all six launch paths, but
native DRC still reported 87 violations, including lane-0 P/N via shorting and
sub-0.2 mm clearances. The remaining planner defect is via-diameter and
connector-launch separation modeling; no route was promoted.
V1595 used deterministic monotonic channels and reduced the result to 34
violations, but native DRC still found source-handoff crossings/shorts and
J1-side via/clearance conflicts. Handoff-pad spacing and connector launch
must now be co-authored together; no route was promoted.
V1596 co-authored distinct-x handoffs with the connector launch but its
diagonal B.Cu transitions were rejected by native DRC with 50 violations,
including lane-pair shorts/crossings and support-net conflicts. The fixture
remains non-production and no route was promoted.
V1597 stripped unrelated support copper and tested six-net orthogonal launch
channels. Native DRC rejected it with 20 violations and 39 fixture opens;
the remaining defects are connector-side via clearance at the 0.5 mm J1
pitch plus offset dogbone/crossing geometry. No route was promoted.
The active accepted local basis remains V1517 at 0° top-side orientation.
The remaining technical task is a coordinated crystal/REFCLK/rail fanout
that is authored against the actual saved pads and ordinary-via rules.
Complete QFN support, firmware/programming, procurement, integration, and
Path-A/Path-B comparison remain OPEN. Receipt:
`PHASE24_RTL9210B_REFCLK_IMPLEMENTATION_REJECT_V1581_V1582_RECEIPT.md` and
`PHASE24_RTL9210B_REFCLK_OUTER_CORRIDOR_REJECT_V1583_RECEIPT.md`.
`PHASE24_RTL9210B_SOURCE_FIELD_ASTAR_DIAGNOSTIC_V1584_V1588_RECEIPT.md`.
`PHASE24_RTL9210B_SOURCE_FIELD_COAUTHOR_REJECT_V1589_RECEIPT.md`.
`PHASE24_RTL9210B_QFN_ESCAPE_HANDOFF_REJECT_V1590_RECEIPT.md`.
`PHASE24_RTL9210B_HANDOFF_J1_ASTAR_REJECT_V1591_RECEIPT.md`.
`PHASE24_RTL9210B_HANDOFF_J1_ASTAR_REJECT_V1592_RECEIPT.md`.
`PHASE24_RTL9210B_HANDOFF_J1_ASTAR_REJECT_V1594_RECEIPT.md`.
`PHASE24_RTL9210B_MANUAL_J1_MONOTONIC_REJECT_V1595_RECEIPT.md`.
`PHASE24_RTL9210B_COAUTHORED_LAUNCH_REJECT_V1596_RECEIPT.md`.
`PHASE24_RTL9210B_ORTHOGONAL_LAUNCH_REJECT_V1597_RECEIPT.md`.

## SUPERSEDED CURRENT-STATE HEADER — V1558

V1549–V1558 are bounded, isolated crystal/source-escape experiments and are
all rejected. Native DRC remains the authority: V1553 reports four source-row
shorts/mask failures, V1556 reports eleven local violations, and V1557
reports seventeen local violations including source/top-row and rail-field
collisions; V1558 reports eleven local violations / five opens at a far-
outboard XIN transition; none is a production layout. The stripped fixtures' two to 17
unconnected items are fixture limitations, not passes.

Path A and the accepted Path-B support primitives remain preserved. Two
materially distinct source-escape classes have now been exercised without
changing rules; the next experiment must change the authoritative fanout
strategy or package escape assumption. No board-rule relaxation is accepted.


## CURRENT STATE OVERRIDE — 2026-09-10

The active accepted local Path-B basis is now
`PHASE24_RTL9210B_U155_REHOME_V1517.kicad_pcb`; the older V1428 composite and
V1461 coupled-field descriptions below are historical baselines, not the
current candidate. V1517 is native DRC clean at 0 violations / 6 inherited
opens and passes U1.55↔U1.63 connectivity plus the saved-board source-removal
negative control. The six remaining opens are XTAL_IN, XTAL_OUT, and REFCLK
P/N endpoint groups. Complete QFN support, firmware/programming, procurement,
integration, and Path-A/Path-B comparison remain OPEN.

The earlier statement that Path B is not promoted because U1.66 cannot be
escaped is superseded by V1466/V1469/V1491 and the V1517 continuation. The
remaining issue is coordinated crystal/REFCLK support routing, not an
unresolved U1.66 escape. Historical DRC reports and rejected trials remain
immutable evidence.

## Current evidence

The active saved-board base is `PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb`.
Native DRC is 0 violations for the accepted composite V1418/V1420 primitives,
and its saved-board audit passes two source-removal negative controls. Ten
unconnected pad groups remain.

The remaining U1.66 GND connection is a package-field problem. Native pad
geometry is:

| pad | net | center | size |
|---|---|---|---|
| U1.65 | LANE0_RXN | (94.05, 72.0) | 0.9 x 0.2 mm |
| U1.66 | GND | (94.05, 72.4) | 0.9 x 0.2 mm |
| U1.67 | LANE0_TXN | (94.05, 72.8) | 0.9 x 0.2 mm |
| U1.68 | LANE0_TXP | (94.05, 73.2) | 0.9 x 0.2 mm |
| U1.69 | GND exposed pad | (98.0, 70.0) | 4.8 x 4.8 mm |

The pad pitch is 0.4 mm with 0.2 mm pad-to-pad gap. The active local DRC
contract requires 0.2 mm clearance and 0.2 mm track width. A standard
through-via outside the pad cannot be reached from U1.66 without crossing or
shorting U1.65/U1.67/U1.68 or the existing JTAG/PEDET/PCIe field.

## Experiments checked

Direct, west, left-first, orthogonal, local-zone, R1-relocation, coupled
RSET/RTL_1V1, coupled QFN regeneration, and REFCLK-adjacent field trials
were preserved in `PHASE24_STATUS.md` and their native DRC reports. The best
U1.66 direct trial still failed; the priority-corrected GND zone had native
DRC zero but left U1.66 unconnected. No severity or validation rule was
relaxed.

## Disposition

Path B is not promoted to production CAD under the current RTL9210B footprint,
clearance, and ordinary-through-via contract. The shortest credible technical
unblock is a manufacturer-verified alternate RTL9210B land-pattern/package
escape that provides a legal U1.66 fanout, followed by complete regeneration
and revalidation of the lane/REFCLK/support field. A second option is a
controlled local package/clearance rule change, which requires explicit user
approval and manufacturing review. Leaving U1.66 open is not acceptable.

Path A remains preserved and available as the fallback architecture. This
report is a Path-B disposition, not a waiver of the overall Phase 24 gate.

## Follow-up native probes — V1457/V1458

Two additional ordinary-through-via edge-access probes were run from the
accepted V1428 composite and rejected on native KiCad 10.0.5 evidence. V1457
used a near-bottom U1.66/U1.69 join and produced 13 violations, including
lane/ground shorts and no-net pad clearance failures. V1458 moved the via
farther below the field and produced 5 violations, including a RESET_N short,
LANE0_RXN contact, and a source-field crossing. Neither probe changes the
Path-B disposition or the approved clearance/layer contract. Their raw PCBs,
generators, and DRC receipts are retained as route-implementation evidence.

## Coupled corridor probe — V1460

Following independent review, V1460 regenerated `LANE0_RXN` together with the
U1.66 GND escape instead of adding another isolated via. Native DRC reported
15 violations / 10 opens: the GND path avoided the original U1.66 direct
failure but collided with LANE0_TXP, LANE0_TXN, and JTAG_TCK geometry. It is
rejected under the unchanged rules. The coupled source-field class is the
next required Path-B work; no production CAD or Path-A asset changed.
V1461 then co-authored the U1.66 GND escape with all four lane-0 source
corridors. Native DRC reported 19 violations / 14 opens, including an RXP/RXN
transition collision and exposed-pad GND conflicts with RTL_1V1/RTL_3V3. It
is rejected under the unchanged rules. The coupled source-field experiment
and disposition are recorded in `PHASE24_RTL9210B_COUPLED_V1461_RECEIPT.md`.

## GND-return corridor follow-up — V1470–V1476

The V1470–V1476 edge, outboard, north, top-right, shelf, and F.Cu-overpass
GND-return trials were rejected under the unchanged rules. Their native DRC
results are preserved in the raw reports and
`PHASE24_RTL9210B_GND_RETURN_V1470_V1476_RECEIPT.md`. These are
route-implementation failures against the live support field, not evidence
against RTL9210B or the accepted V1469 lower-field basis. The next GND work
must coauthor the actual plane/return field; no severity or layer rule is
waived.

## Follow-up native escape — V1466

V1466 supersedes that local trial as the current QFN escape basis. It uses the
actual native pad centers, moves U1.64/RXP east and then north before its
ordinary through-via transition, and joins U1.66/GND directly to the bottom
edge of exposed pad U1.69. Native KiCad DRC reports 0 violations / 9 inherited
support opens. All four lane-0 endpoints and U1.66-to-U1.69 pass saved-board
native connectivity; separate saved-board GND/RXP trace-removal negative
controls fail as required. Receipt:
`PHASE24_RTL9210B_U166_JOIN_RXP_EAST_UP_V1466_RECEIPT.md`.

This closes the specific U1.66 local escape experiment, not the full Path-B
gate. Remaining QFN support, REFCLK/control, firmware/programming,
procurement, integrated storage, and productization checks remain open.

## Lower-field continuation — V1467/V1468/V1469

V1467 and V1468 were rejected because their first U1.63 RTL_1V1 departure
interacted with the existing U1.60/RXN source field. V1469 co-authored that
field instead: it retained U1.60, added the true U1.63 pad departure, and
rehomed RXN below the TXP transition. Native DRC is 0 violations / 8 inherited
opens; U1.63-to-C4.1, all four lane endpoints, and U1.66-to-U1.69 pass native
saved-board connectivity. Rail and RXN source-removal negative controls pass.
Receipt: `PHASE24_RTL9210B_U163_RXN_REHOME_V1469_RECEIPT.md`.

V1469 supersedes V1466 as the current isolated QFN/lane/rail basis. This
closes the lower-field primitive only; full Path-B support and integration
remain open.

## Current override — V1491

The V1470–V1476 GND-return failures are historical rejected evidence, not the
current implementation. V1491 is the current accepted isolated basis:
`PHASE24_RTL9210B_GND_REROUTE_RTL3V3_V1491.kicad_pcb`. It has 0 native DRC
violations, joins the QFN GND field to the remote return through an intentional
In1 GND field, and passes a saved-board negative control. Remaining RSET,
crystal, and REFCLK opens are genuine current work. Receipt:
`PHASE24_RTL9210B_GND_RETURN_V1488_V1491_RECEIPT.md`.

## Current override — V1508 RSET

V1508 is the current accepted RSET primitive on the coordinated V1502 ground
field. Native DRC is 0 violations / 6 inherited opens, and native RSET
connectivity plus the saved-board transition-removal negative control pass.
Receipt: `PHASE24_RTL9210B_RSET_V1508_RECEIPT.md`.
## CURRENT STATE — 2026-09-10 V1556

V1549–V1556 are bounded, isolated crystal/source-escape experiments and are
all rejected. Native DRC remains the authority: V1553 reports four source-row
shorts/mask failures, while V1556 reports eleven local violations including
the RTL_3V3 transition conflict; neither is a production layout. The stripped
fixtures' two or 17 unconnected items are fixture limitations, not passes.
Path A and the accepted Path-B support primitives remain preserved. Next
action is a new authoritative QFN source-escape class, not another
coordinate-only tweak or a DRC-rule relaxation.

See `PHASE24_RTL9210B_CRYSTAL_ESCAPE_V1549_V1553_RECEIPT.md` and the native
reports beside each fixture for raw evidence.
