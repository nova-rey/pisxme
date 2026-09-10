# Phase 24 USB3 corrected-halo A* V119 receipt

V119 is a disposable reroute attempt from the alias-clean V116 board to U12.
The endpoint halo was reduced from eight grid cells (approximately 2 mm) to
one cell so the search cannot erase neighboring 0.4-mm-pitch CM5 connector
pads. The run authoritatively resolved J7.128 to U12.16, then correctly
reported no legal route for J7.130 to U12.15 under the two-layer occupancy
model.

Decision: rejected as an incomplete route implementation. Unlike V117, it
does not produce source-field shorts; the corrected obstacle model exposes
that a coarse grid search cannot solve the dense source escape. No production
CAD or Phase 24 gate is closed. The next route class remains an explicit
pair-aware/native source escape, with each transition placed outside the
connector pad field and independently checked by native DRC.
