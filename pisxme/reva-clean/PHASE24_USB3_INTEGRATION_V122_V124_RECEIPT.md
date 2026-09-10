# Phase 24 USB3 integration V122–V124 receipt

These are disposable integrated candidates from V116 using the V121 source
escape template.

V122 retained the original PERST F.Cu trunk and therefore had no shorts but
four crossings at the U12 final-mile segments. V123 locally ducked the
single-ended CM5_PERST trunk to B.Cu. Native DRC then reported 300 findings
/ 499 opens, but no `shorting_items` or `tracks_crossing`; the remaining
findings are via/filled-plane clearance, hole-clearance, inherited clearance,
and incomplete-board opens. The four-endpoint U12 native connectivity audit
passes. V123 is not a production candidate because the complete native DRC
gate is not clean.

V124 moved the endpoint transitions and refilled zones. Native DRC reported
153 findings including RX pair shorts and crossings, so it is rejected.

The evidence separates the problems: V121 proves the pair-aware route in
isolation; V123 proves the PERST crossing can be removed without USB3 shorts;
the next candidate must use a via/plane-compatible local transition and then
revalidate the affected PERST/PCIe corridor.
