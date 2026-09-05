# Phase 20 status — SERVICE USB2

Date: 2026-09-05
Status: IN PROGRESS — hierarchy repaired; board-side SERVICE routing remains open

Phase 19 remains accepted at commit `42d3654` with the moved-U7 coordinated
storage artifact. Phase 20 has not passed.

## Proven in this continuation

The native KiCad netlist exported from `PiSXMe_RevA_Clean.kicad_sch` now gives
the corrected SERVICE island mapping:

| Net | Native endpoints |
|---|---|
| `/CORE_CM5/SERVICE_USB2_DP` | J4.1, J7.105, U8.1 |
| `/CORE_CM5/SERVICE_USB2_DM` | J4.2, J7.103, U8.2 |
| `/SERVICE/SERVICE_VBUS_SENSE` | J4.3 |
| `/SERVICE/SERVICE_RD_A` | J4.5, R1.1 |
| `/SERVICE/SERVICE_RD_B` | J4.6, R2.1 |
| `/SERVICE/SERVICE_GND` | J4.4, U8.3, R1.2, R2.2 |

The board-side materialization script applies the manufacturer footprint alias
map to J4 and assigns J7.103 = USB2_DM and J7.105 = USB2_DP. The mapping is
reproducible in `phase20_apply_service_authority.py` and the corrected native
export is `phase20-production.net`.

## Current failed proof

The inherited board had all J4/U8/R1/R2 signal pads incorrectly assigned to
SERVICE_GND and J7 USB2 pads as no-connect. Directly routing over that board
would therefore have been invalid. After pad repair, the native DRC still
contains the inherited acreage debt and the first routing trials add
source/pad-field crossings. Those trials are rejected and are not Phase 20
evidence.

Native schematic ERC still reports inherited root-side and unconnected-sheet
pin debt, but the specific SERVICE hierarchy association is now represented
correctly and carries the service nets to J7 in the native export.

## Next bounded continuation

Complete the board-side SERVICE island from the corrected hierarchy. The
current best primary escape is
`PHASE20_SERVICE_PADFIELD_DETOUR.kicad_pcb`: it has no SERVICE USB2
`shorting_items` or `tracks_crossing` entries in the primary escape, but the
USB-C duplicate A/B pads, VBUS aliases, RD resistors, and GND return still
need explicit completion. No PCIe, storage, stack, or validation gate is
relaxed.
