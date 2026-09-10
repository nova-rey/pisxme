# Phase 24 storage USB3 support V140 receipt

V140 is a disposable local fixture with U12 rotated 90 degrees and a
regenerated support-route attempt. It tests a distinct selector orientation;
the fixture contains only U11, U12, C86, and C87 plus the authored USB3
support copper.

Native DRC reports 19 violations, including real U12 pad-field shorts,
crossings, and corridor collisions. The experiment is rejected. It does not
alter the accepted V127 parent or production CAD. Orientation changes require
transform-aware regeneration of both CM5 source and bridge-side launches.
