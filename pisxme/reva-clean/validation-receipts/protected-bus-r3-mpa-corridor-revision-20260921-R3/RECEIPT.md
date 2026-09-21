# R3 MPA decision receipt

This packet is a binding placement/corridor decision only. No CAD was edited and
no hardware was operated.

- Work package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Decision: `PISXME-P24-PROTECTED-BUS-MPA-20260921-R3`
- Placement: source-local fuse banks F1-F3 at y=15, F4-F6 at y=40, F7-F9 at y=65;
  J1/J5/J6/J9 and the protection cohort remain fixed.
- Authority basis: Product / Power Authority superseded the R1 grid and long
  In2 raw lanes because of the 0.65 mOhm hot raw branch-neck allocation.
- Implementation: short ordered F.Cu local raw escapes, distributed In2 fused
  join, ordered In4 return field, In3 protected J1 transition.
- Status: `BINDING_DECISION_FOR_PRODUCER; REQUIRES_PROTOTYPE_VALIDATION`.
