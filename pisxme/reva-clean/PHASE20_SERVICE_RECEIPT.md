# Phase 20 SERVICE receipt

Date: 2026-09-05
Status: IN PROGRESS

## Native hierarchy authority

KiCad 10 native export of the disposable hierarchy candidate and the promoted
clean source proves J7.103 = `USB2_N` and J7.105 = `USB2_P`:

| Net | Endpoints |
|---|---|
| `/CORE_CM5/SERVICE_USB2_DM` | J4.2, J7.103, U8.2 |
| `/CORE_CM5/SERVICE_USB2_DP` | J4.1, J7.105, U8.1 |

The corrected source and export are retained under
`phase20-hierarchy-candidate/` and `phase20-production.net`.

## Routing experiments

Rejected candidates are retained for comparison: `PHASE20_SERVICE_COHERENT`,
`PHASE20_SERVICE_ALIAS_VIA`, and `PHASE20_SERVICE_OUTER_ESCAPE`. They added
USB-C pad-field crossings or invalid via clearances.

The current best primary escape is
`PHASE20_SERVICE_PADFIELD_DETOUR.kicad_pcb`. Native DRC reports 192
violations versus 190 in the inherited base and 411 versus 415 unconnected
items. It has no focused SERVICE USB2 shorting or crossing entries before
duplicate alias completion. It is not yet a Phase 20 pass.

## Open work

Complete J4 A/B duplicate USB2 pads, VBUS aliases, RD_A/RD_B resistor
connections, and deliberate GND return. Native schematic ERC remains
non-clean because of broader inherited scaffold unconnected-sheet-pin debt;
that is not claimed as passed.

The board materializer now canonicalizes logical `SERVICE_GND` to the existing
board-wide `POWER_GND` plane net, consistent with the storage ground alias.
After refill, the separate SERVICE ground island no longer appears as a
service-local unconnected cluster.

The first VBUS perimeter experiment is rejected: its B.Cu segments crossed
the existing data-transition corridors. VBUS still requires a separated local
support route before the candidate can be promoted.

## Latest bounded experiment

`PHASE20_SERVICE_ALIAS_FINAL_CANDIDATE.kicad_pcb` joined all four USB-C DP/DM
duplicate pads and retained zero native `shorting_items` and
`tracks_crossing` entries for the USB2 data topology. Its two ordinary data
alias transitions are outside the connector pad field, but the candidate is
not promoted: the VBUS/Rd/GND support network is not yet complete and the
unfilled inherited ground zones still produce native DRC debt. The subsequent
`PHASE20_SERVICE_SUPPORT_CANDIDATE` overlay is rejected because its support
routes cross the data escape and connector/shield clearances.
