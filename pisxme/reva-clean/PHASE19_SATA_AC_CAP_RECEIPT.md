# Phase 19 SATA AC-coupling implementation receipt

Date: 2026-09-04  
Status: `OPEN_IMPLEMENTATION_GAP`

## Authority

The checked-in TI TUSB9261 implementation guide (`authority-inventory/primary-docs/tusb9261/TUSB9261-implementation-guide-revE.pdf`, SATA section) requires one inline coupling capacitor on each SATA conductor. It limits the package to 0402 or smaller, requires symmetric placement close to the SATA connector signal pins, and disallows capacitor packs.

## Current clean-design finding

`STORAGE.kicad_sch` currently exposes the four bridge SATA nets directly from
U7 to J3 and contains no four-cap inline network. The current PCB experiments
therefore cannot close Phase 19, even when their copper is geometrically clean.

## Required correction

Add four ordinary 0402 capacitors, one in each of:

| Conductor | Required path |
| --- | --- |
| SATA TX+ | U7 `BRIDGE_SATA_TX_P` → capacitor → J3 pad 1 |
| SATA TX− | U7 `BRIDGE_SATA_TX_N` → capacitor → J3 pad 2 |
| SATA RX+ | U7 `BRIDGE_SATA_RX_P` → capacitor → J3 pad 3 |
| SATA RX− | U7 `BRIDGE_SATA_RX_N` → capacitor → J3 pad 4 |

The selected MPNs, footprints, values, reference designators, schematic
connectivity, placement, and native netlist must be recorded before the
SATA routing gate can be re-evaluated. No C-pack substitution is permitted.

## Decision

Phase 19 remains active. This is an obtainable manufacturer implementation
requirement, not `REV_A_EMPIRICAL_RISK` and not a reason to relax the routing
gate.
