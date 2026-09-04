# Phase 19 SATA AC-coupling implementation receipt

Date: 2026-09-04  
Status: `SCHEMATIC_IMPLEMENTED_PCB_PENDING`

## Authority

The checked-in TI TUSB9261 implementation guide (`authority-inventory/primary-docs/tusb9261/TUSB9261-implementation-guide-revE.pdf`, SATA section) requires one inline coupling capacitor on each SATA conductor. It limits the package to 0402 or smaller, requires symmetric placement close to the SATA connector signal pins, and disallows capacitor packs.

## Current clean-design finding

The generic Phase 7 storage authoring path now emits C30-C33. Each is
`GRM155R71C104KA88D`, 100 nF X7R, `PiSXMeRevAClean:C_0402_1005Metric`, with
distinct bridge-side and socket-side net labels. Native child-netlist export
shows the four split paths; the clean PCB materializer now has the matching
0402 footprint and deterministic M.2-launch positions.

## Required correction

Add four ordinary 0402 capacitors, one in each of:

| Conductor | Required path |
| --- | --- |
| SATA TX+ | U7 `BRIDGE_SATA_TX_P` → capacitor → J3 pad 1 |
| SATA TX− | U7 `BRIDGE_SATA_TX_N` → capacitor → J3 pad 2 |
| SATA RX+ | U7 `BRIDGE_SATA_RX_P` → capacitor → J3 pad 3 |
| SATA RX− | U7 `BRIDGE_SATA_RX_N` → capacitor → J3 pad 4 |

The selected MPN, footprint, values, reference designators, schematic
connectivity, placement, and native netlist must be recorded before the SATA
routing gate can be re-evaluated. No C-pack substitution is permitted. The
PCB routing generator still must be updated to route each bridge-side net to
the correct capacitor pad and each socket-side net from the other pad.

## Decision

Phase 19 remains active pending PCB-side routing/materialization and full
native DRC. This is an obtainable manufacturer implementation requirement,
not `REV_A_EMPIRICAL_RISK` and not a reason to relax the routing gate.
