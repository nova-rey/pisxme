# Protected Bus R3 F.Cu-only Gate Loops

- Base: `bf3038cc`
- Method authority: support-cohort routing review 20260921
- Worker/image: `root-mediated-fcu-gate-loop-20260921`, `pisxme-kicad-light:v1`, KiCad `10.0.6`
- Scope: remove GATE_A/GATE_B copper and add clearance-aware F.Cu-only local loops, routing U1/U2 gate pads around the cohort to Q1/Q2 gate pads; no B.Cu/In2 gate trunk, no via-in-pad, no source/J1 corridor edits.
- Producer DRC: 980 violations, 434 unconnected; exit code 5.
- Result: candidate awaiting exact-SHA fresh validation.
- Fresh exact-SHA Light: 982 violations, 434 unconnected items, exit code 5; candidate rejected for integration.
