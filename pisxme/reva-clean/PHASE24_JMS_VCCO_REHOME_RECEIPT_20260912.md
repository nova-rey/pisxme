# Phase 24 JMS VCCO rehome receipt

Candidate: `PHASE24_STORAGE_MKEY_USB3_VCCO_REHOME_20260912.kicad_pcb`

C81 was moved to (150,148) inside the storage island. U11 pad 6 leaves by a
short outward F.Cu escape, then routes along a local y=145 corridor to C81.
The y=148 endpoint avoids the frozen CM5_PERST trunk at y=150; the earlier
y=150 trial is retained as rejected evidence.

Native KiCad 10.0.5: VCCO audit PASS, trace-removal negative control PASS,
USB3 ten-link audit PASS, and 430 DRC violations / 419 unconnected items.
No shorting or track-crossing finding is introduced by this primitive.

Fresh EDA Light validation from committed ref `c8833d56` reports 432
violations / 419 unconnected items under KiCad 10.0.6, reproducing the VCCO
and USB3 connectivity results; the DRC delta is retained as a tool-version
difference.
