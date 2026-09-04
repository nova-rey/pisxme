# Phase 17 mechanical reopening receipt

Date: 2026-09-04
Status: IN PROGRESS — recoverable placement repair

## Decision

The project-authored `MECH_V100` rectangle is retained as a visible measured
cooling/backplate datum on `Dwgs.User`; it is not treated as a universal hard
courtyard.  The authoritative mechanical note already classifies the public
cooler CAD gap as `REV_A_EMPIRICAL_RISK`.  Actual component courtyards,
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
