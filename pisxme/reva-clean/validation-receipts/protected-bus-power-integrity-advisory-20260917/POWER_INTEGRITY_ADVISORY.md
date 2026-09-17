# Protected-bus Power Integrity advisory

- Package: `P24-PROTOTYPE-POWER-BUS-PRODUCER`
- Canonical basis: `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- Basis SHA-256 prefix: `75d2d370...181bf7c`
- Read-only; no CAD or queue edits

## Contract screens

At 11.4 V source, 90% efficiency, and 22.7 W auxiliary load:

- 300 W sustained: `(300+22.7)/(0.9*11.4) = 31.452 A`.
- 330 W for 100 ms: `(330+22.7)/(0.9*11.4) = 34.376 A`.
- Source margins are 8.548 A continuous and 10.624 A peak against 40/45 A.
- A 10 mOhm complete path gives 314.5 mV sustained and 343.8 mV peak drop.
- Protected-bus minima at this corner are 11.085 V and 11.056 V against 11.05/11.00 V contractual limits.

Allocation: 4.0 mOhm harness/connector, 2.0 mOhm fuse/protection,
2.5 mOhm PCB input, and 1.5 mOhm J1 spreading. Copper/via extraction must
screen at least 39.315 A continuous and 37.814 A peak; this is not a generic
trace-width waiver.

## Current-geometry findings

- `12V_IN_A`: 8 pads, 3 segments, 1 via; includes a 222 mm, 2.0 mm segment
  estimated at 54.6 mOhm (1 oz), 27.3 mOhm (2 oz), 13.6 mOhm (4 oz), or
  9.1 mOhm (6 oz) before return/via/contact effects.
- `12V_IN_B`: 7 pads, zero segments/vias.
- `FUSED_12V_A`: 8 pads, 7 segments, 1 via; incomplete branch.
- `FUSED_12V_B`: 7 pads, zero segments/vias.
- `12V_PROTECTED`: 151 pads, 6 segments, 1 via; no bus zone, only narrow
  tracks. `In3.Cu` is declared as protected but has no corresponding zone.
- `POWER_GND`: ground zones exist, but native return connectivity and impedance
  are not closed.
- `BRIDGE_3V3` and `BRIDGE_1V1`: zero segments/vias; physical opens.

The two existing J5/J6 footprints each expose one 12-V contact and one return.
Equal splitting would require 15.73 A sustained or 17.19 A peak per branch,
so 40/45 A credit requires exact connector/terminal/harness qualification or an
authority-approved source-topology change. Passive-sharing credit is forbidden
without a complete resistance and thermal model.

## Required MPA plan content

Resolve source assembly capacity, replace the long input geometry, create a
low-impedance protected positive bus and return to the J1 field, route the two
open bridge rails with local switch/decoupling loops, and preserve validated
high-speed corridors and anchors. Include Kelvin points and complete positive /
return resistance, current-density, via, and thermal extraction before the
producer is promoted. Undocumented transient and SXM2 endpoint behavior remains
prototype validation work; no hardware measurements are claimed.
