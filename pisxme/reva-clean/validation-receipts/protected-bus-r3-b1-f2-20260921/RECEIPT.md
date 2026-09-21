# R3 B1 F2 Branch Extension Candidate

- Base: `dd8496c1`
- Worker/image: `root-mediated-r3-b1-f2-20260921`, `pisxme-kicad-light:v1`, KiCad `10.0.6`
- Input: retained corridor-aware B1 candidate.
- Scope: add J5.2→F2 positive source path and J5.5 return escape/via; preserve existing B1 and J1/high-speed copper.
- Producer DRC: 947 violations, 434 unconnected items, exit code 5.
- Result: producer checkpoint only; exact-SHA fresh validation required.
