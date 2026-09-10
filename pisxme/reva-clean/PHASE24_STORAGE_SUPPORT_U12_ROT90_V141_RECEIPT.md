# Phase 24 storage USB3 support V141 receipt

V141 is a disposable local fixture that rotates U12 by 90 degrees and uses
explicitly separated target-via coordinates above its transformed pad row.
It was intended to test whether a transform-aware orientation could remove
the vertical bridge-side funnel.

Native DRC reports 21 violations, including real B.Cu corridor crossings,
U12 pad-field shorts, target-launch crossings, and two silk warnings. The
fixture remains a local support experiment and omits the full support/power
cohort.

V141 is rejected. The transformed footprint did not produce a valid launch;
no DRC rule or validation severity was relaxed and no production copper was
promoted.
