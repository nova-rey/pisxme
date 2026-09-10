# Phase 24 storage USB3 support V139 receipt

V139 tested staggered target vias above the U12 bridge-side pad row, with
ordered B.Cu corridors and the V136 source escape. The intent was to prevent
the right-side four-pad funnel from forcing a crossing.

Results:

- Native saved-board support connectivity remained present for all six local
  U11/U12 USB3 support nets.
- Native DRC: 6 violations, including target-side crossings and via/track
  clearances between the staggered launch corridors; two silk warnings are
  also present.
- The reduced fixture omitted the CM5 source and support power cohort, so its
  32 unconnected pads are fixture omissions, not a production assertion.

V139 is rejected. No design-rule or severity relaxation is permitted. The
next experiment changes the selector orientation and regenerates its local
launch rather than continuing coordinate tweaks on the same U12 funnel.
