# R3 B1 F2 In2-Handoff Candidate

- Base: `0ed85cca`
- Worker/image: `root-mediated-r3-b1-f2-in2-20260921`, `pisxme-kicad-light:v1`, KiCad `10.0.6`
- Input: retained corridor-aware B1 candidate.
- Scope: J5.2 short F.Cu escape, PWR_SRC_J5_P2 In2 handoff to F2 source, distinct J5.5 return-via escape; no J1/high-speed edits.
- Producer DRC: 969 violations, 434 unconnected items, exit code 5.
- Result: candidate awaiting exact-SHA fresh validation.
- Fresh exact-SHA Light: 971 violations, 434 unconnected items, exit code 5; candidate rejected for integration.
