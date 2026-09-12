# Phase 24 JMS AVDD33 rehome receipt

Candidate: `PHASE24_STORAGE_MKEY_USB3_AVDD33_REHOME_20260912.kicad_pcb`

C80 was moved into the storage island at (150,146), and U11 pad 19 escapes
outward before a short local F.Cu path reaches the decoupler. This avoids the
superseded north-west route and its CM5 USB3 corridor crossings. The selected
RTL9210B/JMS583 orientation, USB3 topology, and VCCK/VDDREG primitives are
unchanged.

Native KiCad 10.0.5: AVDD33 audit PASS, trace-removal negative control PASS,
USB3 ten-link audit PASS, and 431 DRC violations / 419 unconnected items.
No shorting or track-crossing finding is introduced by the AVDD33 primitive.
It remains a support primitive pending full support-cohort integration and
board-level DRC closure.
