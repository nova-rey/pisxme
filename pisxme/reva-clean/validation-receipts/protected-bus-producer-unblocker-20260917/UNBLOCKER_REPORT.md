# Protected-bus producer Unblocker report

- Package: `P24-PROTOTYPE-POWER-BUS-PRODUCER`
- Base: `31b30dc0ccb28fe341f9bffb26005b5f50cd7641`
- Classification: `INTERNAL_ROUTE / DOMAIN_AUTHORITY`
- Date: 2026-09-17

## Evidence

The selected PCB has an incomplete protected-bus topology. `12V_IN_B` and
`FUSED_12V_B` have zero routed segments, `12V_PROTECTED` has no bus-wide
copper or zone, and only `POWER_GND` zones are present. A fresh KiCad Light
baseline reports 300 DRC violations and 499 unconnected items. The initial
producer attempt stopped at this census; the capability-changed direct KiCad
attempt produced only baseline/render/SVG artifacts and no candidate or CAD
mutation.

## Required route

This is a placement/corridor authority problem. Macro Placement Authority,
with Power Integrity advisory, must issue one binding current-HEAD plan for
J5/J6, F1/F2, D1/D2, U1/U2, Q1/Q2, the J1 power field, protected-bus plane
and layer use, returns, reserved corridors, and protected existing copper.
The plan must satisfy the signed conventional protected 12-V source-bus
contract, including the 10 mOhm complete positive-plus-return source-to-J1
budget, ampacity, and thermal constraints. The superseded six-loop MPA plan
must not be reused.

## Queue disposition

Only this producer is parked on `authority:protected-bus-mpa`; its dependent
integration package remains waiting on the producer. Unrelated Phase 24 work
is not made blocked by this route.
