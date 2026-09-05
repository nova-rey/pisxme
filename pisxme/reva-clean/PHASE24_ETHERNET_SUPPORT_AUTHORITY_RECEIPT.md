# Phase 24 Ethernet support-authority receipt

Date: 2026-09-05

## Finding

The production Ethernet schematic now owns the complete support network. Its
serialized authority contains the EDAC J2, ESD U6/U9, four CT capacitor/resistor
branches, shield capacitor, and the two CM5IO-authoritative LED resistors.

This closes the schematic-authority gap; the CM5IO-derived MDI placement and
routing topology remain independently validated. PCB support materialization
must still be regenerated from these saved schematic nets.

## Evidence checked

- Clean source: `ETHERNET.kicad_sch`.
- Official native CM5IO source: `authority-inventory/cm5io-rev2/CM5_GPIO.kicad_sch`.
- EDAC authority: `authority-inventory/primary-docs/ethernet-magjack/EDAC_A70-112-331N126_AUTHORITY.md`.
- Reproducible audits: `phase24_ethernet_support_authority_audit.py` and
  `validation/phase24/test_ethernet_support_production.py`.

The original audit established the omission. The repaired sheet now contains
the four `22 nF / 100 V` to `75 ohm` branches, common node, `1 nF / 2 kV`
shield capacitor, and CM5IO-authoritative `470R` LED current resistors.

The hierarchy mismatch is resolved by removing the bundled `GBE_LED` port and
using the two actual CM5IO LED outputs (`ETH_LEDY`/`ETH_LEDG`) at J7 pads 17/15.

## Decision

`PHASE24_ETHERNET_SUPPORT_AUTHORITY = CLOSED`

The promoted implementation adds native symbols, values, footprints,
MPN/provenance fields, and net ownership for the EDAC CT network, LED current
limiting, and shield return. It removes the bundled LED hierarchy pin and
connects `ETH_LEDY`/`ETH_LEDG` to the native CM5 pad endpoints for J7 pads 17/15.
The dedicated production regression is
`validation/phase24/test_ethernet_support_production.py`.

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

The disposable fixture closed the authoring/topology discriminator. The
production candidate and promoted hierarchy now pass native netlist/ERC
validation; PCB support materialization and board-wide Phase 24 closure remain
separate downstream work.
No historical PCB-only `ETH_CT_BRANCH_*`, `ETH_CT_COMMON`, `CCT*`, or `RCT*`
objects are promoted as production authority.

## Classification

`ROUTE_IMPLEMENTATION_FAILURE`: prior immature Ethernet routing probes.

`CLOSED`: the support-network omission and bundled LED hierarchy mismatch are
resolved. Any remaining Phase 24 failures are downstream PCB parity/routing
work, not this schematic-authority gap.
