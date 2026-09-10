# RTL9210B XTAL_IN trials: V1509-V1511

These disposable trials were run against the current V1508 RSET and V1502
single-In1-GND-field basis. V1509 used the prior southwest corridor; V1510
staggered the departure north of the lower PCIe shelves; V1511 added a second
layer hop through the native pad-field gap. All were rejected by native KiCad
DRC for real crossings/clearance against the live RTL_1V1 field, RTL_3V3
field, or PCIe launch. No accepted design rule or authority was changed.

V1509-V1511 are route-implementation evidence, not proof that XTAL_IN or the
RTL9210B architecture is impossible. The current accepted basis remains
V1508; XTAL_IN, XTAL_OUT, REFCLK, and all full Path-B gates remain OPEN.
