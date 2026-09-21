# Protected Bus R3 Q1-Via Candidate

- Base: `df11bfaa`
- Worker: `root-mediated-gate-q1-via-20260921`
- Image/KiCad: `pisxme-kicad-light:v1` / `10.0.6`
- Method: remove GATE_A copper; F.Cu U1-pad-to-via at `(112.5,42)`; B.Cu via-to-Q1 gate pad.
- Producer DRC: 984 violations, 434 unconnected; exit code 5.
- Result: rejected bounded attempt; no candidate integration.
