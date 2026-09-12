# Phase 24 storage USB3 support V2 receipt

Candidate: `PHASE24_STORAGE_MKEY_USB3_EAST_SUPPORT_V2_20260912.kicad_pcb`

The candidate preserves the accepted east U12 source handoff and places C86
and C87 in the storage island. Native saved-board connectivity passes all ten
USB3 assertions, including both capacitor legs and the direct RX pair.

It is rejected as a route implementation: native KiCad 10.0.5 DRC after
refill reports 464 violations / 421 unconnected, with new USB3 defects at the
U11 fine-pitch TX/RX escape, U12 support returns, and support-pair crossings.
No production rule was relaxed and no architecture or closed placement
decision was changed. The next support implementation must use a pad-escape-
aware local fanout at U11, separately planned B.Cu channels, and return vias
at U12.
