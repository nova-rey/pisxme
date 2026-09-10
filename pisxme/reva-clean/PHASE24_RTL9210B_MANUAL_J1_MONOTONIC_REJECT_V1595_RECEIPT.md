# RTL9210B deterministic monotonic J1 launch rejection — V1595

Date: 2026-09-10

V1595 started from the accepted V1590 west QFN handoffs and used explicit
staggered F.Cu handoff transitions, separated B.Cu channels, and staggered
J1-side F.Cu exits. Native KiCad 10.0.5 DRC rejected the candidate with **34
violations**, including six source-handoff crossings/shorts, B.Cu crossings
through existing RTL_1V1/RTL_3V3/CLKREQ_N geometry, and J1-side clearance and
via conflicts. Thirty unconnected items remain from the intentionally stripped
support fixture. No candidate was promoted and no rule was relaxed.

The trial reduces the prior planner failure but shows that monotonic J1
channels alone are insufficient while the west handoff pads remain tightly
co-located. A valid next implementation must co-author handoff-pad spacing
and the connector launch together, or use a verified alternate launch
footprint/topology.
