# Storage/power blocker reclassification — 2026-09-13

Outcome: `INTERNAL_ROUTE`; classification `DOMAIN_AUTHORITY` (physical congestion / placement-corridor decision). This is not a campaign or external blocker.

Baseline: integrated candidate `acdc52c47d520b053e791b030945d6fa95d5348a` (GATE_B repair candidate follows as `47364e6d`); PCB SHA-256 `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c`; fresh result 300 DRC violations, 499 unconnected, zero reported shorts, two inherited crossings, 15 open Path-A pairs.

Branch-B remains physically open: `12V_IN_B` and `FUSED_12V_B` each have seven pads with zero segments/vias; `12V_PROTECTED` has six segments and one via. The corrected control contract is `AUTO_PEDET J3.69↔J8.2`; `U14.2↔J8.4` is `MODE_IN`.

The exact endpoint list, geometry, anchors, movable cohorts, layers, protected corridors, constraints, and rejected hypotheses are supplied to Macro Placement Authority in the workstream packet. No speculative routing is authorized before one binding MPA placement/corridor plan. Crossings remain MPA-owned because they intersect the JMS_AVDDL/USB_RXN1 high-speed corridor.

Next action: MPA binding plan → isolated qualified KiCad producer → targeted native connectivity/DRC → fresh KiCad Light validation. A structural contradiction may return once to MPA for one bounded revision; only then may a genuinely frozen constraint be escalated.

Independent lanes continue: ERC/source, coverage, SI/return, regulator/power analysis, firmware/provenance, DFM/mechanics, and evidence preparation. Path B RTL9210B remains isolated and unpromoted.
