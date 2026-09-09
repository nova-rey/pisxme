# RTL9210B Path-B V672 — interior RSET basis

V672 retains the V35/U2-left RTL_5V support field and R1 placement, removes
the old RSET copper, and re-authors U1.51 to R1.1 through an interior west
transition and lower B.Cu return. Native KiCad 10.0.5 DRC reports nine
inherited warnings only, with no signal violations. This is a positive RSET
placement basis, not complete Path-B closure; lower RTL_3V3, controls,
REFCLK, lane-0, and other support remain open.

V673 layered the lower-3V3 joins on this basis and exposed the remaining
source-field conflicts; see its separate rejection receipt.
