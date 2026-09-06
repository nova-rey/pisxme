# Native Ethernet ESD escape-cell audit

Board: `PHASE24_CORRECTED_MACRO_PLACEMENT.kicad_pcb` (KiCad 10 native load).

The audit uses transformed pad positions and native pad sizes. It scans cardinal dogbone centerlines at 0.25 mm increments out to 2.0 mm; it does not create copper or assert connectivity.

| pad | net | center (mm) | first clear F.Cu corridor | first clear B.Cu corridor |
|---|---|---:|---|---|
| U6.1 | `CM5_GBE_TD0_P` | (21.000,103.615) | E@0.25, N@0.25, S@0.25 | E@0.25, N@0.25, S@0.25 |
| U6.2 | `CM5_GBE_TD0_N` | (20.500,103.615) | W@2.00, E@1.00, N@0.25, S@0.25 | W@2.00, E@1.00, N@0.25, S@0.25 |
| U6.4 | `CM5_GBE_TD1_N` | (19.500,103.615) | W@1.00, E@2.00, N@0.25, S@0.25 | W@1.00, E@2.00, N@0.25, S@0.25 |
| U6.5 | `CM5_GBE_TD1_P` | (19.000,103.615) | W@0.25, N@0.25, S@0.25 | W@0.25, N@0.25, S@0.25 |
| U6.6 | `CM5_GBE_TD1_P` | (19.000,104.385) | W@0.25, N@0.25, S@0.25 | W@0.25, N@0.25, S@0.25 |
| U6.7 | `CM5_GBE_TD1_N` | (19.500,104.385) | W@1.00, E@2.00, N@0.25, S@0.25 | W@1.00, E@2.00, N@0.25, S@0.25 |
| U6.9 | `CM5_GBE_TD0_N` | (20.500,104.385) | W@2.00, E@1.00, N@0.25, S@0.25 | W@2.00, E@1.00, N@0.25, S@0.25 |
| U6.10 | `CM5_GBE_TD0_P` | (21.000,104.385) | E@0.25, N@0.25, S@0.25 | E@0.25, N@0.25, S@0.25 |
| U9.1 | `CM5_GBE_TD2_P` | (27.000,103.615) | E@0.25, N@0.25, S@0.25 | E@0.25, N@0.25, S@0.25 |
| U9.2 | `CM5_GBE_TD2_N` | (26.500,103.615) | W@2.00, E@1.00, N@0.25, S@0.25 | W@2.00, E@1.00, N@0.25, S@0.25 |
| U9.4 | `CM5_GBE_TD3_N` | (25.500,103.615) | W@1.00, E@2.00, N@0.25, S@0.25 | W@1.00, E@2.00, N@0.25, S@0.25 |
| U9.5 | `CM5_GBE_TD3_P` | (25.000,103.615) | W@0.25, N@0.25, S@0.25 | W@0.25, N@0.25, S@0.25 |
| U9.6 | `CM5_GBE_TD3_P` | (25.000,104.385) | W@0.25, N@0.25, S@0.25 | W@0.25, N@0.25, S@0.25 |
| U9.7 | `CM5_GBE_TD3_N` | (25.500,104.385) | W@1.00, E@2.00, N@0.25, S@0.25 | W@1.00, E@2.00, N@0.25, S@0.25 |
| U9.9 | `CM5_GBE_TD2_N` | (26.500,104.385) | W@2.00, E@1.00, N@0.25, S@0.25 | W@2.00, E@1.00, N@0.25, S@0.25 |
| U9.10 | `CM5_GBE_TD2_P` | (27.000,104.385) | E@0.25, N@0.25, S@0.25 | E@0.25, N@0.25, S@0.25 |

## Interpretation

A `none` result means the current ESD placement has no conservative cardinal departure cell at the chosen grid step; it is a placement/escape-template finding. A non-empty result is only a seed for the next obstacle-aware route and must still pass native DRC, connectivity, pair geometry, and reference continuity.
