# Protected Bus R3 Via-in-Pad Gate Candidate

- Base source commit: `84fb8ebb`
- Producer: `root-mediated-gate-via-pad-20260921`
- Image: `pisxme-kicad-light:v1`; KiCad `10.0.6`
- Input: prior layer-aware candidate `protected-bus-r3-gate-layer-20260921`
- Method: remove all existing `GATE_A` copper, place one through-via at U1 gate pad 5 `(107.5,35.45)`, and route one B.Cu segment directly to Q1 gate pad 3 `(113.54,42.0)`.
- Producer DRC: 980 violations, 434 unconnected items; 0 footprint errors; exit code 5.
- Result: bounded candidate awaiting fresh exact-SHA validation; no canonical integration claim.
