# Phase 24 JMS_XAVDDH local V3 receipt

Candidate: `PHASE24_STORAGE_MKEY_USB3_XAVDDH_LOCAL_V3_20260912.kicad_pcb`

This candidate starts from the validated REXT base and uses a 0.15 mm local
F.Cu escape from U11.52 to the first open point, then 0.20 mm copper and
ordinary 0.60/0.30 mm through-vias to rehomed C84.1. The local exception is
limited to the immediate QFN escape.

Native KiCad 10.0.5 endpoint connectivity and trace-removal negative control
pass, but this is not sufficient for promotion. Fresh KiCad Light 10.0.6
validation finds a real XAVDDH-to-XIN short at the QFN pad field, a B.Cu
crossing of an accepted USB3 route, and local clearance/mask findings; total
census is 562 violations / 415 unconnected items. The candidate is rejected.

The local exception was limited to the immediate QFN escape, but the escape
geometry itself is invalid. The failure is route implementation, not evidence
against the JMS_XAVDDH circuit or frozen RTL9210B placement.
