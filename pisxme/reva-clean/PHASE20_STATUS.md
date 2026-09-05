# Phase 20 status — SERVICE USB2

Date: 2026-09-05
Status: IN PROGRESS — authoring-path repair required

Phase 19 remains accepted at commit `42d3654` with the moved-U7 coordinated
storage artifact. Phase 20 has not passed.

## Proven in this continuation

The native KiCad netlist exported from `PiSXMe_RevA_Clean.kicad_sch` now gives
the corrected SERVICE island mapping:

| Net | Native endpoints |
|---|---|
| `/SERVICE/SERVICE_USB2_DP` | J4.1, U8.1 |
| `/SERVICE/SERVICE_USB2_DM` | J4.2, U8.2 |
| `/SERVICE/SERVICE_VBUS_SENSE` | J4.3 |
| `/SERVICE/SERVICE_RD_A` | J4.5, R1.1 |
| `/SERVICE/SERVICE_RD_B` | J4.6, R2.1 |
| `/SERVICE/SERVICE_GND` | J4.4, U8.3, R1.2, R2.2 |

The board-side materialization script applies the manufacturer footprint alias
map to J4 and assigns J7.103 = USB2_DM and J7.105 = USB2_DP. The mapping is
reproducible in `phase20_apply_service_authority.py` and the corrected native
export is `phase20-materialize.xml`.

## Current failed proof

The inherited board had all J4/U8/R1/R2 signal pads incorrectly assigned to
SERVICE_GND and J7 USB2 pads as no-connect. Directly routing over that board
would therefore have been invalid. After pad repair, the native DRC still
contains the inherited acreage debt and the first routing trials add
source/pad-field crossings. Those trials are rejected and are not Phase 20
evidence.

Native schematic ERC also reports root-side hierarchical sheet-pin and
dangling-wire errors. The root contains separate `CORE_CM5` and `SERVICE`
hierarchical pins but no valid parent wiring that joins the SERVICE contract;
the native netlist consequently does not carry the service net to J7. This is
the next authoring-path defect to fix before another acreage route is promoted.

## Next bounded continuation

Repair the root hierarchy generically so the CORE_CM5 `SERVICE_USB2` contract
and SERVICE sheet `SERVICE_USB2` pin are connected in native KiCad, then export
again and require the J7 103/105 mapping to be represented by the normal
materialization path. Only after that proof will a short open-acreage USB2
route be attempted. No PCIe, storage, stack, or validation gate is relaxed.
