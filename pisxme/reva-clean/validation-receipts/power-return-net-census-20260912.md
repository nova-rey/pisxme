# Power/return net census — 2026-09-12

Source: `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb` at canonical head
`e1850a9e` (board content inherited from physical candidate `fc2b79f8`).

A bounded parser counted named copper segments and vias by net. Selected
power/return nets currently have the following physical objects:

| Net | Segments | Vias |
|---|---:|---:|
| `12V_PROTECTED` | 6 | 1 |
| `POWER_GND` | 47 | 17 |
| `STORAGE_3V3` | 22 | 4 |
| `JMS_AVDD33` | 3 | 2 |
| `JMS_AVDDL` | 7 | 4 |
| `JMS_VCCO` | 4 | 0 |
| `JMS_VDDREG_5V` | 4 | 2 |
| `CM5_5V` | 38 | 9 |
| `FUSED_12V_A` | 7 | 1 |
| `12V_IN_A` | 3 | 1 |

This is an object census only. It does not prove continuity, current capacity,
voltage drop, thermal margin, or closure of unconnected pads. Native DRC and
rail-specific connectivity/PI evidence remain required.
