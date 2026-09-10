# RTL9210B Path-B QFN field disposition

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
