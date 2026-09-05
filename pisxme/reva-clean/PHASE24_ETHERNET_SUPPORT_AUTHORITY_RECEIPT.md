# Phase 24 Ethernet support-authority receipt

Date: 2026-09-05

## Finding

The clean Ethernet schematic is not yet support-complete. Its serialized
authority contains J2, U6, and U9, plus labels for `ETH_CT1..4`, the four LED
nets, and `GBE_SHIELD`, but no center-tap termination components, LED-current
resistors, or explicit shield/ground return component.

This is a schematic-authority gap, not evidence that the CM5IO-derived MDI
placement or routing topology is wrong. PCB-only support additions remain
unpromoted until the schematic owns the same references and nets.

## Evidence checked

- Clean source: `ETHERNET.kicad_sch`.
- Official native CM5IO source: `authority-inventory/cm5io-rev2/CM5_GPIO.kicad_sch`.
- EDAC authority: `authority-inventory/primary-docs/ethernet-magjack/EDAC_A70-112-331N126_AUTHORITY.md`.
- Reproducible audit: `phase24_ethernet_support_authority_audit.py`.

The audit reports no `CCT*`/`RCT*` component references in the clean sheet.
Each center-tap and LED label is currently a dead-end local net at the
connector-side symbol. The donor schematic contains real CM5IO LED current
resistors `R2`/`R3` at `470R`; its center taps are exposed as tap nets for the
PoE header rather than a local EDAC termination network. The EDAC authority
specifies four `22 nF / 100 V` to `75 ohm` series branches into a common node,
with a `1 nF / 2 kV` shield/ground termination capacitor.

The hierarchy adds a second authority mismatch: the child exposes one bundled
`GBE_LED` port, while its four connector LED labels are local and the root has
no four-net LED contract. The support repair must resolve that interface
explicitly; it must not invent four CM5 LED nets or silently leave the LED
pins floating.

## Decision

`PHASE24_ETHERNET_SUPPORT_AUTHORITY = OPEN_SCHEMATIC_REPAIR_REQUIRED`

The next implementation must add real native schematic symbols, values,
footprints, MPN/provenance fields, and net ownership for the EDAC CT network,
LED current limiting, and shield return, while reconciling the bundled LED
hierarchical contract. After native ERC/netlist/parity validation, the PCB
support island may be regenerated from those saved nets.

## Disposable native schematic proof

`phase24_ethernet_support_fixture.py` creates a disposable child/root pair
without editing production sources. The fixture uses ordinary `C48-C52` and
`R26-R31` references. Its selected passive MPNs are recorded in
`authority-inventory/primary-docs/ethernet-support-passives/ETHERNET_SUPPORT_PASSIVES_AUTHORITY.md`.

Native KiCad 10.0.5 root ERC reports `Errors 0`. The exported netlist proves
all four J2 center taps reach their own capacitor, each capacitor reaches its
own 75 ohm resistor, all four resistors meet at `ETH_CT_COMMON`, C52 reaches
the J2 shield net, and both LED cathodes have 470 ohm series resistors. The
regression is `validation/phase24/test_ethernet_support_schematic_fixture.py`.

This fixture closes the authoring/topology discriminator only. The LED source
nets still require production hierarchy mapping to the authoritative CM5
Ethernet LED pads 15 and 17; no PCB promotion is implied by this fixture.
No historical PCB-only `ETH_CT_BRANCH_*`, `ETH_CT_COMMON`, `CCT*`, or `RCT*`
objects are promoted as production authority.

## Classification

`ROUTE_IMPLEMENTATION_FAILURE`: prior immature Ethernet routing probes.

`SCHEMATIC_AUTHORITY_GAP`: the current support-network omission. It is not a
`MACRO-PLACEMENT_FAILURE` and is not terminally blocked.
