# RTL9210B Path-B V670 — rejected lower-3V3 co-author

V670 starts from the V35/U2-left `RTL_5V_PLUS_3V3_PROBE` basis identified by
the consultant as the strongest current lineage. It adds U1.39→U2.8 and
U1.52→U2.3 RTL_3V3 channels using native pads, ordinary 0.60/0.30-mm
through-vias, 0.20-mm tracks, and the standing layer contract.

Native KiCad 10.0.5 DRC found 24 violations and 21 unconnected items. The
new lower-3V3 source tracks cross or short the retained 1V1/RSET/XTAL/SPI
fields; both U2 endpoint joins remain incomplete.

Disposition: reject V670 as a route implementation. The V35
SPI/crystal/RTL_5V basis remains valid evidence. The next credible class is
coherent local relocation or re-authoring of the RSET/3V3 support endpoint
field, followed by native-pad lower-3V3 routing. No Path-A or production CAD
was changed and no design rule was relaxed.

Raw evidence: `PHASE24_RTL9210B_LOWER_3V3_V670.kicad_pcb`,
`PHASE24_RTL9210B_LOWER_3V3_V670-drc.rpt`, and
`phase24_rtl9210b_lower_3v3_v670.py`.
