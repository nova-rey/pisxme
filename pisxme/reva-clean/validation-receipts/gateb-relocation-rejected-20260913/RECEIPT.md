# Rejected GATE_B via relocation

Base: `3ff559fd`. The target GATE_B via was moved from Q2 pad 3 `(12.54,108)`
to `(10,110)`, with a short F.Cu handoff and the existing upper route
preserved. Fresh Light DRC reported **310 violations / 499 unconnected**,
including one real `GATE_B`↔`12V_PROTECTED` short plus new clearance,
hole-clearance, and solder-mask findings. Candidate rejected; canonical PCB
unchanged.
