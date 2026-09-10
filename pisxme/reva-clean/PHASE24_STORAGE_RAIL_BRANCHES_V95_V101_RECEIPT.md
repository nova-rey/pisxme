# Phase 24 storage-rail branch trials V95–V101 — rejected evidence

These are disposable tests from the source-corrected V94 board. They are not
production PCB authority.

| Trial | Change | Native power audit | Native DRC | Decision |
|---|---|---|---:|---|
| V95 | U13.30 to U14.5, north F.Cu branch, full refill | PASS, negative control PASS | 600 / 340 | REJECT: NC_27/STORAGE_SEL and MODE_IN/STORAGE_SEL shorts |
| V96 | U13.30 to U14.5, B.Cu north perimeter | PASS, negative control PASS | 607 / 340 | REJECT: crossings and latent shorts |
| V97 | U13.30 to U14.5, high F.Cu perimeter | PASS, negative control PASS | 607 / 340 | REJECT: crossings and latent XOUT short |
| V98 | U13 local fanout to B.Cu east trunk | PASS, negative control PASS | 611 / 337 | REJECT: STORAGE_3V3/TUSB_SATA_RXP shorts |
| V99 | U12/U13/U14/R81 vias into local In4 rail plane | PASS, negative control PASS | 617 / 334 | REJECT: via/pad and rail-to-signal shorts |
| V100 | Exact V95 branch without zone refill | PASS, negative control PASS | 603 / 340 | REJECT: branch still crosses and exposes NC/selector shorts |
| V101 | U13/U14 safe-offset vias into local In4 rail plane | PASS, negative control PASS | 606 / 337 | REJECT: storage-selector, SATA, and latent XOUT shorts |
| V102 | U13.30 around outer B.Cu/F.Cu perimeter to U14.5 | PASS, negative control PASS | 619 / 340 | REJECT: crossings and latent selector/XOUT findings |
| V103 | U12/U13/U14/R81 into local In2 power plane | PASS, strict-source PASS | 612 / 333 | REJECT: rail-to-signal/via shorts |
| V104 | U13/U14-only local In2 plane with revised escapes | PASS, focused PASS | 610 / 337 | REJECT: NC_26/STORAGE_SEL and latent XOUT shorts |
| V105 | Removed existing selector copper; outer F.Cu re-route U12/U13/U14 | not applicable | 614 / 341 | REJECT: crossings and recurring XOUT/JMS_XAVDDH short |
| V106 | Rotate U12/U13 selector footprints 90 degrees | not applicable | geometry probe | REJECT as direct-board candidate: inherited copper is stale after rotation |
| V107 | Rotated selectors with local pin-9 stubs | not applicable | 738 / 353 | REJECT as integrated candidate: stale copper/zone conflicts |
| V108 | Stripped rotated-selector pin-9 escape fixture | not applicable | 275 / 489 | DIAGNOSTIC: package has intrinsic sub-0.2-mm pad clearances; no route-width error, but local rule treatment is unresolved |

The focused audit proves the nine J3 contacts reach at least one
`STORAGE_3V3` source through saved native copper. It does not waive the
remaining requirement that every regulator/support pad assigned to that net
must physically join the rail. The trials therefore remain evidence only.

The audit now also supports `--strict-sources`, requiring all listed source
pads to share one native saved-board connectivity component. Current V94 and
V102 fail this stricter assertion, while V103/V104 pass it; V103/V104
nevertheless fail native DRC and remain rejected.

V106–V108 show that selector rotation changes the affected copper rather than
proving the complete board. The stripped fixture confirms the pin-9 escape
geometry needs an explicit manufacturer/DFM rule decision; no integrated
rotation has been promoted.

The next repair must address the fragmented source fanout with pad-aware
clearance and a hardened `STORAGE_SEL` escape. No synthetic graph edges,
severity changes, or stale V94 route promotion are permitted.
