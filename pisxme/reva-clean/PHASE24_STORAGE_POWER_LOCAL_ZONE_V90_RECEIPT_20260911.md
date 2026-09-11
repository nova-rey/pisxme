# Storage M.2 power local-zone V90 experiment

V90 kept the V88 source pickup and J3 fanout but moved the long
`STORAGE_3V3` trunk to the designated `In2` low-voltage power layer. This
removes the V88 `In1.GND` policy violation while retaining ordinary
through-vias and saved-board physical connectivity.

Native connectivity passed for all nine J3 power contacts and the real
trace-removal negative control. Native KiCad DRC still reports 608 violations
and 341 unconnected items, including additional crossing/shorting and
clearance consequences relative to the V79 source. V90 is therefore rejected
as a route candidate, though its layer assignment is policy-compliant and its
connectivity result remains useful evidence. Canonical CAD was not changed.
