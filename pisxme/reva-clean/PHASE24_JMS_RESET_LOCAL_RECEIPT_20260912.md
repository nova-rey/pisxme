# Phase 24 JMS reset local receipt

Candidate: `PHASE24_STORAGE_MKEY_USB3_RESET_LOCAL_20260912.kicad_pcb`

The reset branch leaves U11 pad 15 through a short left-edge jog, transitions
with ordinary through-vias into a dedicated B.Cu channel, and returns on F.Cu
to C85 and R81 without crossing the accepted VCCO/VCCK or USB3 paths.

Native KiCad 10.0.5: reset actual-connectivity audit PASS, trace-removal
negative control PASS, USB3 ten-link audit PASS, and 437 DRC violations / 417
unconnected items. No shorting or track-crossing finding is introduced by the
corrected reset primitive. The earlier straight north-bound reset route is
rejected evidence only.
