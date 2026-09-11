# Storage M.2 power local-zone V89 experiment

V89 preserved the V88 source-to-J3 power topology but changed both long
trunk transitions from `In1.GND` to `B.Cu`, obeying the no-signal-on-plane
layer contract. Native saved-board connectivity still passed for all nine J3
power contacts and the actual trace-removal negative control.

Native KiCad DRC reported 609 violations and 341 unconnected items, versus
608/341 for V88 and 601/350 for the V79 source. The B.Cu correction therefore
does not produce a promotable candidate and is rejected as a route
implementation. It does, however, establish that the V88 connectivity win
does not depend on synthetic graph edges; the remaining work is physical
clearance/corridor repair. No canonical CAD was changed.
