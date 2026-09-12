# Phase 24 retained-board zone-refill probe

Date: 2026-09-12  
Base: `b3684300` / `PHASE24_JMS583_FINE_QFN_ESCAPE.kicad_pcb`  
Validator: fresh KiCad Light `pcbnew` + `kicad-cli`

## Result

The disposable board was loaded with native `pcbnew`, refilled with
`ZONE_FILLER.Fill`, saved separately, and checked with native DRC. Native DRC
changed from 612 violations / 409 unconnected items to 472 violations / 409
unconnected items.

| Class | Saved baseline | Refilled probe |
|---|---:|---:|
| `clearance` | 191 | 117 |
| `track_width` | 181 | 188 |
| `unconnected_items` | 409 | 409 |
| `via_dangling` | 6 | 7 |
| `tracks_crossing` | 2 | 2 |
| Total | 612 | 472 |

## Disposition

REJECTED as a Phase 24 closure candidate: refill does not address the
connectivity gate and creates additional track-width/via-dangling findings.
The result is retained as implementation evidence: future board comparisons
must state whether zones were freshly refilled. No canonical PCB or
validation severity was changed.
