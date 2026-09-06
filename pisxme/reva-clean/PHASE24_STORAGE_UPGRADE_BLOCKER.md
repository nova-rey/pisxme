# Phase 24 storage-island upgrade blocker

Status: `OPEN — implementation authorized; procurement evidence remains HIGH
risk` for the authorized SATA/NVMe upgrade only.
The prior SATA-only board is preserved.

## Exact unresolved items

`JMS583_AUTHORIZED_PROTOTYPE_SUPPLY`; TE M-key footprint authoring/parity is
the remaining local implementation gate.

ASM2362 is rejected, but it is no longer the only candidate. Bounded research
qualified JMS583's exact QFN64 pin assignment, land-pattern dimensions,
support values and power timing from JMicron's detailed Rev 2.1 datasheet.
JLCPCB lists exact `JMS583-QHFA3A` (`C25701682`, about $6.06 qty 1, minimum 1,
SMT), but currently reports zero stock; broker stock is corroborating only.

The firmware prerequisite is now closed for baseline operation: the
manufacturer ordering code includes a mask-ROM version, and the selected
device is factory programmed. External SPI NVRAM is documented for optional
VID/PID customization and is DNP in Rev A. Firmware update remains an
authorized future-maintenance path, not a design dependency. Authorized
prototype supply is still not demonstrated; JLC currently reports zero stock
and broker listings are not sufficient release evidence.

## Why production implementation stops

The NVMe bridge owns the USB and PCIe sides of the new path. JMS583's pads and
reference component values are now reviewable; baseline design may proceed
with factory mask-ROM operation. No mystery firmware or PCB-only repair is
permitted.

TE `1-2199230-4` is an eligible replacement: TE identifies it as Active, M
code, 67-position, 4.2-mm SMT and publishes application specification Rev C.
The exact TE customer CAD is now retained locally; native footprint pad,
courtyard and model parity must be completed before replacing J3. Existing
`SM3ZS067U410ABR1000` remains B-key-only.

## Sources checked

- JMicron official JMS583 product/solution page, official product brief,
  detailed Rev 2.1 datasheet, and official download center.
- JLCPCB exact JMS583-QHFA3A page and multiple broker stock snapshots.
- TE exact M-key product page, TE Rev C application/product specifications,
  and DigiKey exact MPN page.
- ASMedia ASM2362 official product page and JLCPCB assembly listing.
- JMicron's official JMS581DL product page/Product Brief and JLCPCB
  144TFBGA assembly listing were checked as a simpler one-chip alternative;
  its ball map/design pack/firmware path are not public.
- Realtek RTL9210B community firmware/reference ecosystem and searches for
  manufacturer documentation; no better authoritative bare-chip path found.
- TI TUSB9261/switch authorities and existing project firmware records.

All captures are retained under `authority-inventory/primary-docs/storage-upgrade/`.
No purchase was made.

## Shortest human action

Obtain an authorized prototype quote or traceable factory-programmed
`JMS583-QHFA3A` supply. The baseline design can proceed without a firmware
binary; external SPI NVRAM remains optional/DNP. Finish the native TE M-key
footprint parity check for `1-2199230-4` before replacing J3.

## Continuation options

1. Recommended: obtain JMS583 prototype supply confirmation and finish TE
   customer-CAD footprint parity, then implement the storage island and resume
   Phase 24.
2. Use a factory-programmed complete USB-to-NVMe module only if its exposed
   interfaces, firmware provenance and socket-side integration are documented.
3. Dropping dual-mode storage would retain the old SATA-only board, but that
   is a user architectural decision and is not assumed.

## Current implementation audit — 2026-09-06

The implementation path has since been advanced in the working tree:

- `STORAGE.kicad_sch` contains the TE M-key socket, JMS583-QHFA3A, and the two
  TI selectors. The JMS583 embedded symbol now reflects the detailed table,
  including REXT pin 39, AVDD33 pin 19, all AVDDL/VCCO/VCCK pins, GPIO/SPI
  optional pins, reset, crystal, and LXO.
- `phase24_dual_mode_storage_schematic_audit.py`, the library audit, and the
  mode-contract net-label audit pass. A removed-label negative control fails.
- Native KiCad netlist export parses successfully. Native ERC still reports
  201 violations, so this is not a release schematic.
- The native PCB candidate is placement-only and remains unrouted; its last
  native report recorded 1,013 violations and 482 unconnected items. It is not
  an integrated-board PASS.

The remaining engineering blockers are now explicit rather than generic
documentation objections:

1. The M.2 standard revision retained in the repository has no generic PEDET
   contact; IFDET/PRESENCE were removed. DAS/DSS cannot honestly be used as a
   universal SATA-versus-NVMe detector. AUTO therefore needs a real documented
   detector/sequencer or must remain open.
2. The JMS583 support network is represented as pin authority but still needs
   native component instances and physical support routing: 25-MHz crystal,
   REXT, AVDD33 capacitor, LXO inductor, reset RC, VBUS divider, decoupling,
   and the documented AC coupling capacitors.
3. The complete switched-mode native fixture, including inactive-state
   isolation and forced SATA/NVMe cases, has not yet passed DRC/connectivity.
4. TE customer CAD is retained, but its pad-by-pad native coordinate audit,
   courtyard, and 3D model release review remain open.

This report therefore remains `OPEN`; no Phase 24 resumption or completion is
claimed. The corrected JMS583 pin authority also supersedes any earlier
intermediate map that called pin 12 REXT.
