# RTL9210B Path-B V671 — rejected RSET relocation

V671 moved the RSET resistor endpoint and re-authored the native U1.51 to
R1.1 connection to free the lower RTL_3V3 corridor. The experiment used the
V35/U2-left RTL_5V basis, ordinary 0.60/0.30-mm through-vias, 0.20-mm
tracks, and unchanged design rules.

Native KiCad 10.0.5 DRC found 15 violations and 24 unconnected items. The
new B.Cu RSET perimeter collided with the retained lower RTL_1V1 collector;
the moved endpoint also reached the board edge. The lower RTL_3V3 join was
not closed.

Disposition: reject V671 as a route implementation. It does not reject the
V35 lineage or Path-B architecture. The next credible class is an interior
RSET endpoint/field reallocation that co-authors RSET, lower 3V3, and the
existing 1V1/XTAL field; no rule relaxation or Path-A change is authorized.

Raw evidence: `PHASE24_RTL9210B_RSET_RELOCATED_V671.kicad_pcb`,
`PHASE24_RTL9210B_RSET_RELOCATED_V671-drc.rpt`, and
`phase24_rtl9210b_rset_relocate_v671.py`.
