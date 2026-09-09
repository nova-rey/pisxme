# RTL9210B Path-B V692 — rejected U1.52 B.Cu route

V692 moved the C2 GND stitch and changed U1.52 to a B.Cu transition, but the
vertical leg crossed the existing RSET B.Cu collector. Native KiCad DRC found
one real crossing and 28 incomplete opens. Reject this route.
