# Current-head direct native DRC check

- Source commit: `28ab8fc1`
- PCB: `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- Command: `kicad-cli pcb drc --severity-all --format json --output drc.json <pcb>`
- Return code: 0
- Observed: 310 violations, 499 unconnected items
- Classes: clearance 138; track_width 118; copper_edge_clearance 16; track_dangling 9; holes_co_located 9; via_dangling 7; courtyards_overlap 6; pth_inside_courtyard 5; tracks_crossing 2
- No shorting_items reported.
- DRC JSON SHA256: `5545e6329f5c35f485fa99262eea0a5343da2531bedcfc684f7666181c283525`

This is a direct current-host check. It is not a substitute for the required fresh isolated Light validation; the difference from the retained 312-count Light receipt must be reconciled as a context/tool invocation difference before acceptance.
