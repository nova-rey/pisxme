# Phase 24 storage V78 receipt — separated BRIDGE_R1 trial

V78 is a disposable continuation of accepted V75. It replaces only the
failed V76/V77 `BRIDGE_R1` route with a separate ordinary-via column at
`x=89.5` and a B.Cu shelf at `y=116`, leaving V75's `BRIDGE_R1RTN` route at
its established column/shelf. No net, footprint, layer policy, or rule was
changed.

Native KiCad DRC reports 605 violations / 349 unconnected items and exposes
two real shorting classes: `JMS_AVDDL` to `POWER_GND`, and `BRIDGE_R1` to
`BRIDGE_R1RTN`. It is rejected. V75 remains the preferred parent; no rule,
net, footprint, or production CAD change was made.
