# Exact-head rule-context validation

- Candidate/source commit: \
- Worker: \; KiCad CLI \
- Board: \
- Project context: clean detached checkout; board-local \ present and loaded by native DRC.
- Native command: \
- Result: 314 violations, 499 unconnected items (expected non-clean baseline; RC 5 when \ is used).
- Rule-scope evidence: the board-local rule file contains the authorized XIN/XOUT 0.10-mm width/clearance rule; the retained focused scope audit records 7 XIN/XOUT tracks inside the approved window with no fine-net vias. Ordinary board-wide constraints remain active outside that rule.
- This receipt proves exact-head context loading only; it does not waive physical violations or close acceptance.
- Raw DRC and checksum retained in this directory.
