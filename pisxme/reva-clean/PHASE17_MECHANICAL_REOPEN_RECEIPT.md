# Phase 17 mechanical reopening receipt

Date: 2026-09-04
Status: IN PROGRESS — recoverable placement repair

## Decision

The project-authored `MECH_V100` rectangle is retained as a visible measured
top-side cooling datum on `Dwgs.User`; it is not treated as a universal hard
courtyard or underside keepout. Rev A assumes module-mounted cooling. Actual component courtyards,
connector bodies, mounting holes, and access constraints remain enforced.

This implements the user-authorized acreage interpretation: copper and
low-profile Ethernet support may pass beneath an elevated cooler, while the
tall MagJack must still be checked against real body and mating clearance.

## Independent review

Consultant `Crosscheck` classified the mixed-reservation interpretation as
`PROPOSED_UNBLOCK` and recommended a split source-proximate island: keep ESD
near CM5, move the tall MagJack to a legal edge, and use underside support
only where backplate/standoff/service checks permit.  It rejected historical
coordinates and the uniform rectangle as constraints.

## Evidence

Starting candidate: `ACREAGE_PHASE17_F1RIGHT40_ETH_GROUND_FIXED.kicad_pcb`.
It has zero Ethernet crossings/shorts, exact EDAC mapping, scoped regression
PASS, and pair skew 0.547–0.829 mm.  Native DRC before the mechanical change
reported 216 violations; the soft-envelope trial
`ACREAGE_PHASE17_SOFT_COOLER_TRIAL.kicad_pcb` reports 188 violations and only
four remaining courtyard overlaps, with no `MECH_V100` courtyard entries.
The remaining DRC/unconnected items are inherited acreage scaffold debt and
are not treated as proof of an Ethernet collision.

The scoped checks were rerun on the saved trial: Ethernet regression PASS;
route metrics PASS; pair skew was 0.547, 0.681, 0.688, and 0.829 mm for
TD2, TD0, TD3, and TD1 respectively.  The MDI paths remain F.Cu-only in this
candidate and no forbidden plane-layer signal was introduced.

## Next authorized experiment

Re-author the complete source-to-ESD fanout with the ESD/support island near
CM5 and place the tall MagJack at the most natural open board edge.  Preserve
the CM5IO topology, EDAC mapping, 100-ohm route basis, ground return, and
Phase 16 PCIe geometry.  Do not promote this receipt as Phase 17 closure until
the outboard MagJack candidate passes its mechanical, connectivity, native
DRC-scoped, and routing checks.

## Outboard translation trials

The generic transplant path was extended to translate only the Ethernet island
geometry while retaining J7 fixed. Two disposable acreage sweeps were run:

| Candidate | Placement | Native result | Decision |
|---|---|---|---|
| `ACREAGE_PHASE17_SPLIT_OUTBOARD_ETH_SOFT` | island +180,+40 mm | 336 violations, 13 crossings, 18 shorts | REJECTED |
| `ACREAGE_PHASE17_SPLIT_OUTBOARD_BOTTOM_SOFT` | island +180,+100 mm | 499 violations, 20 crossings, 26 shorts | REJECTED |

These failures are route-geometry failures of translated copper, not evidence
against the CM5IO electrical topology. The next trial must regenerate the
source-to-ESD fanout and connector launch for the selected placement rather
than translating finished copper blindly.

## Regenerated fanout trial

`phase17_regenerated_split_fanout.py` removes only the source-side MDI copper
from the +180,+40 mm island candidate and writes explicit J7-to-ESD lanes,
using ordinary through-vias for TD2/TD0. The resulting
`ACREAGE_PHASE17_REGENERATED_SPLIT_SOFT.kicad_pcb` was rejected by native DRC:
415 violations, including 22 `tracks_crossing`, 44 `shorting_items`, and six
hole-clearance findings. This rejects the lane implementation, not the CM5IO
topology; Phase 17 remains open.

The existing right-channel west-split authoring class was rerun against the
Phase 16 ancestor with the revised underside contract. Native DRC reported
458 violations, including 21 crossings, 8 shorts, and 449 unconnected items;
it was rejected. This confirms that simply enabling underside space does not
make the historical west-split route valid.

## Revised underside contract

The Rev-A contract was subsequently narrowed: a cooler/backplate mounted to
the V100 SXM2 module is outside the carrier-board mechanical envelope. No
generic underside keepout or carrier mounting holes are reserved. The native
Phase 9 and Phase 11/12 audits pass with the floorplan label
`V100 MODULE / TOP COOLING DATUM`; underside Ethernet routing is therefore
permitted except at verified board hardware and connector/access geometry.

The rotated native-tool fixture was rerun under this contract. Its result was
still negative (163 violations, 6 crossings, 10 shorts, 3 unconnected), so
removing the hypothetical underside reservation does not by itself solve the
source/ESD escape. It remains a disposable rejected fixture, not an authority
change or a Phase 17 pass.

## Top-edge regenerated-island trial

Following the specialist recommendation, `phase17_top_edge_regenerated.py`
placed U9/U6 beside J7 at `(24,97)` and `(28,103)`, placed J2 at the top edge
`(150,12.5,180°)`, and regenerated all eight MDI paths plus CT/common/shield
support. Native DRC rejected the result with 351 violations, 38 crossings,
65 shorts, 8 hole-clearance findings, and 461 unconnected items. The manual
lanes intersect existing power/PCIe and connector fields; this candidate is
rejected and no clean-board authority was promoted.

A second top-edge iteration moved the ESD pair to `(50,110)` / `(60,115)` to
clear the J7 pad field and regenerated the local lanes again. It reduced some
shorts but still failed native DRC with 350 total violations, 48 crossings,
53 shorts, and 8 hole-clearance findings. It was also rejected; the next
iteration must use a constrained router/no-go mask for the actual frozen
power and PCIe copper rather than hand-selected corridor lines.

An ESD-orientation variant was also tested at 0° with the same top-edge J2
placement. Native DRC reported 338 violations, 55 crossings, 35 shorts, 8
hole-clearance findings, and 461 unconnected items. It was rejected; rotation
alone does not resolve the pair-specific launch ordering.

The follow-up audit identified a separate authoring error: the first top-edge
generator placed all four B.Cu connector-side transitions at `(90,45)`,
creating artificial stacked-via shorts. The corrected generator gives each
transition a distinct 2 mm lane. Native DRC improved to 319 violations, 44
crossings, 36 shorts, and 8 hole-clearance findings, but the candidate remains
rejected because real pair endpoint ordering and board-corridor conflicts
remain.

## Right-edge MagJack discriminator

The next bounded placement class moved only the EDAC MagJack to the open right
edge at `(282.5,53)` with its authoritative 180-degree orientation, while
retaining the accepted CM5IO-derived U9/U6 ESD island. The authoring path was
implemented in `phase17_right_edge_mdi_trial.py`; it captures actual pad
centers, regenerates the eight MDI nets, uses distinct ordinary through-via
lanes for TD2/TD0, and keeps all signals on F.Cu/B.Cu.

Native KiCad DRC rejected the first right-edge discriminator with 332
violations and 447 unconnected items. The Ethernet-specific failures include
pair crossings and shorts at the existing acreage copper/ESD escape. This is
rejected as a routing-generator trial: the right-edge placement has not been
promoted, and the CM5IO electrical authority remains unchanged. The next
credible class is a genuinely fresh source-to-ESD island authoring pass in an
open acreage region, with a constrained no-go mask for frozen PCIe and power
copper rather than adding long manual lanes to the existing copper field.

## Fresh open-acreage island trial

The complete ESD pair was moved to `(205,140)` / `(215,140)` and the EDAC
MagJack to `(282.5,140)` at 180 degrees, using the newly available underside
contract and lower-right acreage. All eight MDI nets were regenerated from
actual J7, ESD, and MagJack pad centers, with TD2/TD0 using ordinary F.Cu to
B.Cu transitions and no internal-plane signals.

Native KiCad DRC rejected this first fresh-island authoring pass with 285
violations and 445 unconnected items. The failures are now localized to the
generated source corridors crossing the existing F2/power-entry geometry, the
package-aware ESD breakout, and the connector-boundary support pads. The
placement class itself is retained for refinement; the trial is not promoted
and Phase 17 remains open.
