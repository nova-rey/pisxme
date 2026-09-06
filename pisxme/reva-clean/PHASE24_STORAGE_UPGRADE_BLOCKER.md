# Phase 24 storage-island upgrade blocker

Status: `PISXME_REVA_CLEAN_BLOCKED` for the authorized SATA/NVMe upgrade only.
The prior SATA-only board is preserved.

## Exact unresolved items

`JMS583_FIRMWARE_PROGRAMMING_AND_AUTHORIZED_SUPPLY`; TE M-key customer CAD
parity is open but independently tractable.

ASM2362 is rejected, but it is no longer the only candidate. Bounded research
qualified JMS583's exact QFN64 pin assignment, land-pattern dimensions,
support values and power timing from JMicron's detailed Rev 2.1 datasheet.
JLCPCB lists exact `JMS583-QHFA3A` (`C25701682`, about $6.06 qty 1, minimum 1,
SMT), but currently reports zero stock; broker stock is corroborating only.

The remaining external artifact is a legitimate JMS583 firmware/configuration
and programming path. JMicron says firmware is downloaded through USB and
external SPI NVRAM holds vendor information, but its public download center
does not publish a generic firmware image, matching programmer, supported SPI
flash/config format, or redistribution rights. No third-party binary may be
copied into the design. Authorized prototype supply or factory-programmed
parts is also not demonstrated.

## Why production implementation stops

The NVMe bridge owns the USB and PCIe sides of the new path. JMS583's pads and
reference component values are now reviewable, but a board without approved
firmware/configuration would not be a validated storage device. No mystery
firmware, symbol promotion, selector wiring, or PCB-only repair was authored.

TE `1-2199230-4` is an eligible replacement: TE identifies it as Active, M
code, 67-position, 4.2-mm SMT and publishes application specification Rev C.
The exact TE customer CAD/pad drawing still must be imported and compared
before replacing J3. Existing `SM3ZS067U410ABR1000` remains B-key-only.

## Sources checked

- JMicron official JMS583 product/solution page, official product brief,
  detailed Rev 2.1 datasheet, and official download center.
- JLCPCB exact JMS583-QHFA3A page and multiple broker stock snapshots.
- TE exact M-key product page, TE Rev C application/product specifications,
  and DigiKey exact MPN page.
- ASMedia ASM2362 official product page and JLCPCB assembly listing.
- Realtek RTL9210B community firmware/reference ecosystem and searches for
  manufacturer documentation; no better authoritative bare-chip path found.
- TI TUSB9261/switch authorities and existing project firmware records.

All captures are retained under `authority-inventory/primary-docs/storage-upgrade/`.
No purchase was made.

## Shortest human action

Obtain from JMicron or an authorized design partner: the approved JMS583
firmware image, matching programming utility/use rights, SPI flash/config
format, and an authorized prototype quote or factory-programmed
`JMS583-QHFA3A` supply. Separately obtain TE's exact customer CAD/drawing for
`1-2199230-4`. With those artifacts, the storage island can be implemented and
validated without reopening the board macro-floorplan.

## Continuation options

1. Recommended: obtain the JMS583 firmware/programming/supply package and TE
   customer CAD, then implement the storage island and resume Phase 24.
2. Use a factory-programmed complete USB-to-NVMe module only if its exposed
   interfaces, firmware provenance and socket-side integration are documented.
3. Dropping dual-mode storage would retain the old SATA-only board, but that
   is a user architectural decision and is not assumed.
