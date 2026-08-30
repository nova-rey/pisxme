# Hostile review — final pre-routing gate

Date: 2026-08-21
Question: is there a concrete evidence-backed reason not to route the board?

## Findings

| Attack area | Result | Evidence |
|---|---|---|
| SXM2 pad count/orientation | PASS | active J1 is the 400-pad Amphenol-derived model; A1, 1.27 mm pitch, 0.635 mm pad, 0.150 mm mask margin, no pad vias, and rework courtyard are recorded. |
| CM5 connector orientation | PASS | official 10164227 drawing-derived two-row 100-pad model is active on J2A/J2B; both are deliberate 90° placements, not mirrored. |
| TX/RX and polarity | PASS AS REV-A BASIS | standard endpoint contract remains internally consistent: CM5 TX→V100 RX and V100 TX→CM5 RX; V100 TX has two external 220 nF capacitors. |
| REFCLK/PERST/CLKREQ | PASS AS REV-A BASIS | direct common-clock REFCLK, direct active-low PERST#, local CM5 CLKREQ# assertion; no mandatory V100-side CLKREQ or WAKE route identified. |
| Impedance definition | PASS | live JLC calculation for JLC06161H-7628 gives 90 Ω at W1 0.13208 mm and S1 0.085328 mm; independent coated calculation is 90.14944 Ω. |
| ERC | PASS WITH EXPLANATIONS | 0 errors, 184 warnings; 0 multiple-net names; every remaining warning is grouped and documented as tool limitation or intentional boundary labeling. |
| DRC placement | PASS | 0 errors, 0 courtyard/clearance/silk/unconnected findings; 20 local-library warnings only. |
| Power path | PASS FOR ROUTING | contact-current arithmetic remains below the Amphenol all-contact test rating under nominal and 330 W V100 scenarios; copper spreading and thermal design remain routing tasks. |
| Cooler/backplate contract | PASS | no fixed placement violates the published topside or underside reserved volume; final cooler remains user-defined. |
| Manufacturability | PASS FOR ROUTING | critical footprints are manufacturer-verified or datasheet-derived-and-checked; hidden joints/X-ray and selective solder are production controls. |

## Residual risks, not blockers

- V100-specific power sequencing is supported by working-carrier empirical
  evidence and the standard-endpoint policy, but has not been exercised on the
  user's hardware.
- Private NVIDIA timing documentation is unavailable; Rev-A uses conservative
  common-clock/reset behavior and records that limitation.
- U1 thermal-via/paste implementation and high-current copper geometry still
  require the next routing phase.
- KiCad CLI reports 12 PCB footprint-link warnings and 12 corresponding
  schematic link warnings because of project-local library resolution in the
  isolated CLI context. These are reproducible and explicitly classified.

## Decision

No concrete unresolved design defect was found. The board is ready for
controlled-impedance routing, subject to the explicit “no Gerbers/order” stop
condition of this phase.
