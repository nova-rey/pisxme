# Phase 24 JMS VCCK local receipt

Candidate: `PHASE24_STORAGE_MKEY_USB3_VCCK_LOCAL_20260912.kicad_pcb`

The storage-local VCCK primitive connects U11 pad 2 to C82 pad 1 using an
outward F.Cu escape, ordinary through-vias, and a B.Cu vertical segment. It
does not alter U12, the accepted USB3 topology, or the frozen RTL9210B
orientation.

Native KiCad 10.0.5 DRC reports 426 violations / 420 unconnected items. The
dedicated VCCK actual-connectivity audit and trace-removal negative control
pass. The complete ten-link USB3 audit passes. No new shorting or track-crossing
class is introduced; remaining board findings remain unwaived.

Fresh EDA Light validation from committed ref `fe36fb10` reports 428
violations / 420 unconnected items under KiCad 10.0.6, reproducing the VCCK
connectivity result; the DRC delta is retained as a tool-version difference.
