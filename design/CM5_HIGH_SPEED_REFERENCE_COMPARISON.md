# CM5 high-speed reference comparison

Date: 2026-08-23

## Official Raspberry Pi CM5IO

The official CM5IO project is the highest-authority CM5 carrier evidence in
this set. It uses Type-A connectors rather than a Type-C orientation mux, so it
does not provide a direct mux fanout template. It does provide two important
facts:

* `CM5_HighSpeed.kicad_sch` explicitly says `USB 3 Pairs P/N swapped to help
  routing`.
* Its USB3 footprint mapping visibly assigns the physical Type-A pad order to
  swapped P/N net names, confirming that physical polarity remapping is part of
  the official CM5 carrier layout practice.

A read-only PCB inspection found a small number of USB3 layer transitions: the
two ports use F.Cu/B.Cu as needed, with roughly one or two vias per conductor
depending on the path. This is evidence that a via is acceptable when needed,
not a target for PiSXMe’s short local fanout.

## ModuCard CM5 Module

Source: MIT-licensed `references/cm5/moducard-cm5-module/`, commit
`2d96d2e238e6e020c98220d49595c7a6028a35cf`. The README reports fabrication,
assembly and bring-up completion.

Read-only PCB metrics for the USB SuperSpeed nets:

| Group | Observation |
|---|---|
| `USB_SS_0` | F.Cu only, zero vias, approximately 8.3–9.9 mm paths in the local CM5-to-connector/hub region |
| `USB_SS_1` | F.Cu/B.Cu, one via per net, approximately 31–45 mm paths |

This is useful working-hardware evidence that direct CM5 USB3 routing can be
short and simple, but its connector and board geometry differ from PiSXMe.

## cm5MiniITX

Source: `references/cm5/cm5MiniITX/`, commit
`479fee1dd5831eab652e72c031d0c806a2091c44`. The checkout describes itself as a
prototype and has no clear project-level license, so it is reference-only.

Read-only metrics show longer USB3 paths, with some F.Cu/B.Cu transitions and
several vias on one port. This demonstrates that a working-looking carrier can
trade length/vias for board-level placement, but it is not a justification for
PiSXMe’s former 40–46-via Type-C fanout.

## Lessons applied to PiSXMe

1. CM5 physical escape order must be treated as a first-class constraint.
2. P/N labels are not sacred physical order; the official CM5IO itself records
   swaps for routing.
3. A zero-via or low-via local route is plausible when mux/ESD/connector order
   is designed together.
4. A second layer is an allowed fallback, not a substitute for fixing an
   avoidable polarity/order mismatch.
5. No CM5 reference justifies altering the frozen PCIe routing in this phase.
