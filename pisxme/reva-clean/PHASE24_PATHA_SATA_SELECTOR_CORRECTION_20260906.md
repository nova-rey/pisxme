# Phase 24 Path-A SATA selector correction — 2026-09-06

Status: `SOURCE AUTHORITY CORRECTED; ROUTE IMPLEMENTATION OPEN`

## Finding

The earlier V4 SATA route connected C30–C33 directly to J3's shared lane-0
contacts. That route passed its old endpoint assertions but bypassed U13,
the approved HD3SS3412 SATA/PCIe selector. It is rejected as a topology
implementation, not retained as Path-A evidence of closure.

## Authoritative correction

TI's HD3SS3412 datasheet (`HD3SS3412-datasheet.pdf`, pp. 13–14) defines
Port A as the common side, Port B as the `SEL=L` side, and Port C as the
`SEL=H` side. The corrected source mapping is:

| Function | U13 pin(s) | Native net | Endpoint |
|---|---:|---|---|
| SATA TX+ / TX−, Port B | 38 / 37 | `TUSB_SATA_TXP/N` | C30.1 / C31.1 |
| SATA RX+ / RX−, Port B | 36 / 35 | `TUSB_SATA_RXP/N` | C32.1 / C33.1 |
| Shared M.2 SATA-A / PCIe-TX0 | 2 / 3 | `M2_SATA_A_*` | J3.49 / J3.47 |
| Shared M.2 SATA-B / PCIe-RX0 | 6 / 7 | `M2_SATA_B_*` | J3.41 / J3.43 |
| NVMe PCIe lane 0, Port C | 34/33 and 32/31 | `JMS_PCIE_TX/RX0` | U11 path |

The coupling-capacitor socket-side labels were changed from the M.2 nets to
the selector Port-B `TUSB_SATA_*` nets. U13 A1 was corrected from the stale
second-PCIe-TX names to the shared M.2 SATA-B/PCIe-RX0 names. The correction
is source-authoritative in `STORAGE.kicad_sch` and generated into the
disposable PCB by `phase24_integrate_dual_mode_storage.py` and
`phase24_place_dual_mode_storage_island.py`.

The TI package drawing also requires the exposed thermal pad to be soldered to
the PCB. The PCB generator now assigns U13 pad 43 to `POWER_GND`; it is not
invented as a schematic signal pin. Any F.Cu route over that pad is therefore
a real ground short and must be routed around or below it.

## Native evidence

`PHASE24_STORAGE_SATA_SELECTOR_CORRIDOR_20260906.kicad_pcb` passes the
selector-inclusive native audit:

* four U7-to-capacitor endpoints;
* four capacitor-to-U13 Port-B endpoints;
* four U13 Port-A-to-J3 endpoints;
* explicit rejection of direct capacitor-to-J3 reachability.

`phase24_sata_selector_native_connectivity_negative_control.py` removes a
real saved `TUSB_SATA_TXP` track in a disposable copy and observes the
expected C30.1-to-U13.38 disconnect. No expected edge is injected into the
graph.

The first selector-inclusive route still has local DRC crossings/shorts and
is not promoted. This is route implementation evidence only. The older direct
V4 route and its raw DRC/negative-control receipts remain immutable historical
evidence but are superseded for Path-A topology.

## Remaining gate

Re-author the four SATA pairs around the corrected U13 Port-B/A topology,
then rerun native DRC, pair geometry, and the combined USB3/SATA fixture.
No whole-board Path-A or Path-B decision is closed by this correction.
