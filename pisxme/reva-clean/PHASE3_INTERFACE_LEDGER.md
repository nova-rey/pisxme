# PiSXMe Rev A Clean — Phase 3 interface ledger

This ledger is the root-to-sheet contract. Signal names are stable interfaces;
local implementation names may not bypass them.

| Owner | Interface | Direction / class | Authority and constraint |
|---|---|---|---|
| CORE_CM5 | `CM5_PCIE_PER0/PET0`, `CM5_REFCLK`, `CM5_PERST#` | CM5 <-> V100 | Gen2 x1 only; Phase 1 PCIe donor and CM5 authority |
| CORE_CM5 | `CM5_USB3_TX/RX` | CM5 -> STORAGE | one USB3 path only; no USB2 SERVICE dependency |
| CORE_CM5 | `CM5_GBE_MDI[0..3]`, LED, center-tap rails | CM5 <-> ETHERNET | official CM5IO mapping; selected ESD authority |
| CORE_CM5 | `SERVICE_USB2_DP/DM`, `SERVICE_VBUS_SENSE` | CM5 <-> SERVICE | USB2 UFP; no VBUS source |
| V100_PCIE | `V100_PER0/PET0`, `V100_REFCLK`, `V100_PERST#` | high speed/control | SXM2 `74221-101LF`; lane 0 only; raw PET AC coupling |
| V100_POWER | `V100_12V_A/B`, `V100_GND_*` | power/return | distributed power; cooler envelope authority |
| POWER_INPUT | `12V_IN_A/B`, `12V_PROTECTED`, `PG/FAULT` | power/control | dual cold-plug regulated inputs |
| REGULATORS | `CM5_5V`, `STORAGE_3V3`, `BRIDGE_1V1/3V3` | power | vendor circuits; TUSB9261 requires 1.1 V and 3.3 V |
| ETHERNET | `GBE_MDI[0..3]`, `GBE_LED[0..1]`, `GBE_SHIELD` | high speed/control/return | `TPD4E004DRYR`; MagJack risk explicit |
| STORAGE | `USB3_TO_BRIDGE`, `BRIDGE_SATA`, `M2_SATA_*`, `M2_3V3` | high speed/power | TUSB9261IPVP; SATA-IO Socket 2/B-key mapping |
| SERVICE | `SERVICE_USB2_DP/DM`, `SERVICE_VBUS_SENSE`, `SERVICE_Rd_A/B` | USB2/control | UFP-only; connector ESD; no source VBUS |
| COOLING | `FAN/PUMP_12V`, `TACH`, `PWM`, `THERMAL_ALERT` | power/control | conservative cooler/backplate envelope |
| DEBUG | `UART`, `RECOVERY`, `PG/FAULT_TEST`, `GND_TEST` | low speed/test | accessible probes; no high-speed stubs |

Any interface not listed here is local to its owning sheet and must not appear
as an accidental root-level net.
