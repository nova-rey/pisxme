# Phase 24 integrated-routing blocker reassessment

Current canonical candidate is the validated exact integrated CAD lineage at
`f4711172` (later commits in this lineage retain only receipts/metadata). The
latest bounded candidates were:

- one Path A SATA pair dogleg: rejected at 309 DRC / 499 unconnected after
  adding four width and two dangling-track findings;
- one branch-B `12V_IN_B` route: rejected after a real J6.2 `POWER_GND` to
  `12V_IN_B` short;
- one second `CM5_5V` dangling-track removal: neutral trade of one track
  dangling for one via dangling;
- one `FUSED_12V_A` dangling-track removal: no change.

Safe exact duplicate-hole cleanup and validation-context corrections have been
integrated. Remaining integrated blockers are structural: 15 required Path A
storage endpoint pairs remain open, branch-B delivery remains unrouted, 138
clearance and 118 width findings remain, and the GATE_B via-in-PTH overlap
requires a pad-aware reroute. No rule relaxation, synthetic connectivity, or
waiver is authorized.

Next permitted discriminator: an authority-reviewed, pad-aware local reroute
for one storage or power net that demonstrably preserves all existing copper,
followed by fresh Light DRC/connectivity validation. If that route class again
fails, escalate the physical corridor to the relevant authority/Unblocker
rather than replaying the same geometry.
