# RTL9210B RSET receipt: V1508

`PHASE24_RTL9210B_RSET_WEST_V1508.kicad_pcb` is the accepted isolated RSET
repair from the V1502 single In1 GND-field basis. U1.51 `(94.8,66.05)` exits
on F.Cu to an ordinary 0.50/0.30 mm through-via, crosses the former RTL_1V1
B.Cu barrier on a short F.Cu hop, and terminates at R1.1 `(88,65)` without
touching R1.2/GND. The obsolete GND triangle is not restored.

Native KiCad DRC: **0 violations**, 6 inherited support opens. The native
saved-board audit verifies U1.51↔R1.1 connectivity and the R1.2 GND net. Its
negative control removes the RSET B.Cu transition and confirms the endpoint
connection fails. No expected graph edges are used.

This closes only the isolated RSET primitive. XTAL_IN, XTAL_OUT, REFCLK,
firmware/configuration, procurement, full mode validation, integration, and
Path-A/Path-B comparison remain open.
