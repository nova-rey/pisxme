# Phase 24 storage USB3 support-graft receipt

Candidate: `PHASE24_STORAGE_MKEY_USB3_EAST_SUPPORT_20260912.kicad_pcb`

The east-pocket U12 source-handoff baseline was retained and C86/C87 were
co-located at the storage island. Native saved-board connectivity passes all
ten expected USB3 links, including both U11-to-capacitor legs, both
capacitor-to-U12 legs, and the direct U11-to-U12 RX pair. However, native DRC
after refill reports 452 violations / 421 unconnected items, including real
new USB3 shorts/crossings at the U11 TX escape, the F.Cu CM5_PERST crossing,
U12 support-pad launches, and RX pair convergence. It is rejected as a route
implementation, not as an electrical-topology failure.

The next implementation must keep the accepted east source handoff and use
an obstacle-aware local support route: fan out U11’s adjacent TX/RX pads with
short local dogbones, transition support legs to B.Cu before CM5_PERST, and
return through ordinary vias near the U12 support pads. Do not promote this
candidate or treat its ten-link connectivity PASS as DRC closure.
