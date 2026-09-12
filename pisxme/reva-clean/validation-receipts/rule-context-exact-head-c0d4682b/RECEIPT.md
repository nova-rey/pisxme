# Exact-head rule-context validation

- Candidate/source commit: `c0d4682b`
- Worker: `pisxme-kicad-light:v1`; KiCad CLI `10.0.6`
- Board: `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- Project context: clean detached checkout; board-local `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_dru` present and loaded by native DRC.
- Native command: `kicad-cli pcb drc --format json --severity-all -o drc.json PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- Result: 314 violations, 499 unconnected items (expected non-clean baseline; RC 5 when `--exit-code-violations` is used).
- Rule-scope evidence: the board-local rule file contains the authorized XIN/XOUT 0.10-mm width/clearance rule; the retained focused scope audit records 7 XIN/XOUT tracks inside the approved window with no fine-net vias. Ordinary board-wide constraints remain active outside that rule.
- This receipt proves exact-head context loading only; it does not waive physical violations or close acceptance.
- Raw DRC and checksum retained in this directory.
