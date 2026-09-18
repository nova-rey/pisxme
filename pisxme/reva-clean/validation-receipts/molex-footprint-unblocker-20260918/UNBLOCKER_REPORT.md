# Molex footprint authority unblocker report

Outcome: INTERNAL_ROUTE.

The released 39301082 footprint geometry is internally non-overlapping: 4.20 mm contact pitch, contact rows at +/-6.30 mm, NPTHs at +/-3.65 mm, 2.60 mm lands, and 3.60 mm NPTH keepouts. The producer DRC collision is caused by existing J5/J6 placement and protected-bus copper routing through the J5 NPTH at (15.65,25.00), with equivalent connector-region conflicts at J6.

This is an implementation placement/corridor problem. Macro Placement Authority and the protected-bus producer must preserve the released footprint, reserve NPTH keepouts, and relocate/reroute affected copper in one isolated current-HEAD candidate. Canonical CAD remains unchanged.
