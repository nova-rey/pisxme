# Phase 21 control inventory

Generated from `PHASE20_SERVICE_RD_OUTER_REFILLED.kicad_pcb` with KiCad pcbnew.

| Net | Pads | Existing tracks |
|---|---|---:|
| `/CORE_CM5/CM5_PERST` | J1.E18, J7.109 | 5 |
| `/POWER_INPUT/GATE_A` | Q1.3, U1.5 | 0 |
| `/POWER_INPUT/GATE_B` | U2.5, Q2.3 | 0 |
| `/POWER_INPUT/VCAP_A` | C3.1, U1.1 | 0 |
| `/POWER_INPUT/VCAP_B` | U2.1, C4.1 | 0 |
| `/REGULATORS/FB_BRIDGE_1V1` | U5.10, R20.1, R19.2 | 0 |
| `/REGULATORS/FB_BRIDGE_3V3` | R11.2, R12.1, C18.1, U4.10 | 0 |
| `/REGULATORS/FB_CM5_5V` | R3.2, C9.1, U3.10, R4.1 | 6 |
| `/REGULATORS/PG_BRIDGE_1V1` | U5.13, R22.2 | 0 |
| `/REGULATORS/PG_BRIDGE_3V3` | R14.2, U4.13 | 0 |
| `/REGULATORS/PG_CM5_5V` | R6.2, U3.13 | 4 |
| `/REGULATORS/RT_BRIDGE_1V1` | U5.12, R21.1 | 0 |
| `/REGULATORS/RT_BRIDGE_3V3` | R13.1, U4.12 | 0 |
| `/REGULATORS/RT_CM5_5V` | R5.1, U3.12 | 3 |
| `/STORAGE/BRIDGE_RESET` | U7.2, U7.4 | 0 |

## Progress

The reset tie, three PG nets, and both VCAP nets are now routed in
`PHASE21_CONTROLS_VCAP.kicad_pcb`. The remaining zero-track control classes
are the two power-input gate nets and the bridge FB/RT nets.
