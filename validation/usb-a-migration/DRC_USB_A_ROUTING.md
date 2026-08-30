# USB-A targeted DRC receipt

Date: 2026-08-27  
Tool: KiCad 10.0.5 `pcb drc --refill-zones --save-board --format json`

Source report: `DRC_FULL_BOARD_RC2_FINAL.json`

## Targeted result

| Check | FAST-A | FAST-B |
|---|---:|---:|
| USB3 short/crossing errors | 0 | 0 |
| USB3 clearance errors | 0 | 0 |
| differential-pair rule errors | 0 | 0 |
| pad/hole/keepout errors | 0 | 0 |
| USB2 companion errors | 0 | 0 |

The full native-refill report contains no `shorting_items`, `tracks_crossing`,
`clearance`, `track_width`, `diff_pair_*`, `padstack`, `hole_clearance`, or
`keepout` violation. The two FAST ports are therefore clean under the
targeted USB-A filter.

The report's 49 warnings are standalone `lib_footprint_issues` records from
the CLI validation copy not loading the project-local `PiSXMe` footprint
library. They are context warnings, not USB-A geometry failures.
