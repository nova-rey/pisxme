# Phase 24 F.Cu POWER_GND plane probe

Date: 2026-09-12  
Base: `PHASE24_JMS583_FINE_QFN_ESCAPE.kicad_pcb` at `c1ec1520`  
Candidate: `PHASE24_FCU_POWER_GND_PLANE_PROBE.kicad_pcb`

## Result

A disposable native `pcbnew` candidate added one full-acreage F.Cu
`POWER_GND` zone with 0.20 mm local clearance and full pad connection, then
refilled all zones. Producer native DRC reported 472 violations and 265
unconnected items, versus the saved baseline's 612 and 409.

| Class | Baseline | Probe |
|---|---:|---:|
| `unconnected_items` | 409 | 265 |
| `clearance` | 191 | 117 |
| `track_width` | 181 | 188 |
| `starved_thermal` | 0 | 0 |
| `via_dangling` | 6 | 7 |
| `tracks_crossing` | 2 | 2 |
| Total | 612 | 472 |

This is a candidate for fresh-validator review, not a Phase 24 pass. The
remaining opens and manufacturing findings must be resolved, and the plane's
signal-integrity, thermal, and manufacturability effects must be reviewed
before promotion. The retained board was not modified.
