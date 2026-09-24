# Heavy GUI-control qualification import

- Capability: `pisxme-kicad-heavy:v2`
- Image digest: `sha256:39fdae0176135aec42a0dacc8fb250bf8cbf915e01ad67a342e8f8bb2de44344`
- Interfaces: `/usr/local/bin/pisxme-heavy-session`, `/usr/local/bin/pisxme-heavy-gui`
- Source: `/home/nyx/pisxme-eda-workers/docs/QUALIFICATION.md` and `HEAVY_GUI_CONTROL.md`
- Scope: isolated Heavy producer only; canonical CAD remains untouched

Qualification evidence records GUI-routed `ROUTE_A` around an obstacle and
`ROUTE_B` to completion, fresh Light validation with zero unconnected items and
no DRC-count increase, and a separate named-via fixture. Heavy use is limited
to cases where Light/scripted edits are exhausted. The protected-bus producer
may resume through the normal isolated candidate, fresh Light validation, and
serialized integration gates.
