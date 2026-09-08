# RTL9210B package audit — V440

Audited from the saved native PCB `PHASE24_RTL9210B_CLKREQ_QFN_CLEARANCE_V431.kicad_pcb`
with KiCad 10 `pcbnew`, after transforms.

- Footprint: `RTL9210B-CG_QUALIFICATION`
- U1 orientation: 180 degrees
- Pads 61/62/60/63: SMD attribute, 0.9 x 0.2 mm, 0.4 mm pitch
- Exposed pad 69: SMD attribute, 4.8 x 4.8 mm
- REFCLK source pads: U1.61 at (109.95,61.60), U1.62 at (109.95,61.20)
- Adjacent source pads: U1.63 at (109.95,60.80), U1.60 at (109.95,62.00)

This confirms the imported object is an SMD QFN-style footprint, not a
through-hole footprint. The V439/V438 native DRC failures are caused by the
0.4-mm peripheral pitch, the 0.9-mm pad length, and the active 0.20-mm board
clearance/minimum-width rules. No rule relaxation or production-CAD change
is authorized by this audit.
