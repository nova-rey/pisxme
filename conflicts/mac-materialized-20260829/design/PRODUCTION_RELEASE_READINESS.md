# Production release readiness

Date: 2026-08-22  
Board: `pisxme/PiSXMe.kicad_pcb`

## Decision

**NOT_READY_FOR_REV_A_FAB_PACKAGE**

This phase deliberately preserved the routed board after rejecting shorter
PCIe and lower-skew FAST-B trial geometries that introduced real DRC errors.
The current board is therefore not a silently changed release candidate; it
remains the auditable first-pass routed study.

The first production-quality routing pass is materially complete and
reviewable, but the board is not ready to package for fabrication.

## Gate matrix

| Gate | Result | Evidence |
|---|---|---|
| PCIe x1 routed | POOR PHYSICAL ROUTE | `routing/HIGH_SPEED_FINAL_METRICS.md`, `routing/PCIE_REWORK_RECEIPT.md` |
| USB3 FAST-A/B routed | FAST-A reviewable; FAST-B NOT ACCEPTABLE | `routing/HIGH_SPEED_FINAL_METRICS.md`, `routing/USB3_FAST_B_REWORK_RECEIPT.md` |
| 12 V V100 distribution | PASS WITH DOCUMENTED THERMAL RISK | `routing/THERMAL_CURRENT_ANALYSIS.md` |
| CM5/USB power | PASS TO THERMAL REVIEW | power-route receipts and current budget |
| Routed DRC | PASS WITH DOCUMENTED CONTEXT | 0 geometric errors; 54 local-library warnings; 22 remaining intentional connectivity records |
| Routed ERC | PASS WITH DOCUMENTED WARNINGS | 0 errors; 46 explained warnings in `validation/ERC_ROUTED_REWORK_RECEIPT.md` |
| PCB/schematic parity | NOT MACHINE-CLEAN | 321 warnings, including 199 intentional J1 full-connector abstraction records; see `validation/PCB_SCHEMATIC_PARITY_RECEIPT.md` |
| Mechanical contract | PASS | cooler/backplate keepouts remain preserved |
| BOM/CPL/release files | NOT RELEASED | this phase does not generate release Gerbers or send files externally |

## Concrete blockers

1. FAST-B SuperSpeed pair matching and connector-side breakout are not
   sufficiently demonstrated for a conservative USB3 production release.
2. PCIe remains in the project's POOR band: 107--122 mm with two transitions
   per conductor. The fixed J2/cooler relationship must be reconsidered before
   a controlled-impedance production route can be called deliberate.
3. The routed board still contains 22 DRC connectivity records across the
USB shield net, F.Cu GND-zone islands, and USB VBUS zones, plus 54
project-local library warnings. The shared `/NC` net defect is fixed; the
remaining records need a deliberate shield/zone copper disposition rather
than a blanket waiver or treating DRC exit code 0 as a clean release.
4. The 400-pad J1 connector is electrically assigned on the PCB but is
   intentionally abstracted in the schematic; full machine parity must be
   resolved or explicitly waived in the release review.
5. Thermal qualification of the 300 W-class SXM2 feed and regulator regions
   is still a hardware/fab-build validation task.

## Accepted prototype risks

The standard PCIe endpoint assumption, V100 sequence behavior, hidden-joint
reflow quality, and exact cooler implementation remain Rev-A prototype risks.
They are not being represented as proven production facts.

## Next gated work

Rework or field-solve the USB3 layer strategy, rerun the high-speed audit,
rerun KiCad ERC/DRC on the exact board, then regenerate a fabrication-only
package review. Do not order this revision from the current state.
