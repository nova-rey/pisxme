# Phase 24 dual-mode storage implementation

Status: `IN PROGRESS — native symbol/connector integration landed; mode
control, copper fixture, and full electrical validation remain open`
(2026-09-06).

The active implementation is the storage-local two-bridge topology:

`CM5 USB -> HD3SS6126RUAR -> {TUSB9261 SATA | JMS583-QHFA3A NVMe}
-> HD3SS3412RUAR -> TE 1-2199230-4 M-key Socket 3`.

The selected JMS583 is factory mask-ROM qualified for baseline use. Its
optional SPI NVRAM remains DNP. This does not close procurement: JLC's exact
part listing currently reports zero stock and broker listings are not an
authorized source.

## Land-pattern artifacts

`phase24_generate_dual_mode_storage_libraries.py` emits native
footprints from retained authorities:

- `JMS583_QFN64_8x8.kicad_mod`: QFN64, 0.4-mm pitch, 8-mm body, 64 pads.
- `HD3SS6126_RUA0042A.kicad_mod` and `HD3SS3412_RUA0042A.kicad_mod`: TI
  RUA0042A, 42 pads plus exposed pad 43. Separate names preserve distinct
  pin ownership despite the common package drawing.
- `TE_1-2199230-4_MKEY.kicad_mod`: 67 contacts with the TP-053 M-key gap.

The generated files are review candidates until native pad-by-pad comparison
against the TE DXF/application drawing and TI/JMicron package pages is signed
off. The library audit is intentionally structural; it does not assert PCB
connectivity.

## Current evidence

`STORAGE.kicad_sch` now contains U7 plus native U8 JMS583, U9 HD3SS6126,
U10 HD3SS3412, and J3 TE 1-2199230-4. The B-key J3 is removed. The saved
sheet parses under KiCad 10.0.5, and `phase24_dual_mode_storage_schematic_audit.py`
passes; its negative-control copy fails when a required M-key label is removed.
Native ERC currently reports 205 violations, so this is not an ERC pass. The
report is retained as evidence and includes inherited abstract-sheet issues,
off-grid generated symbol endpoints, and isolated labels requiring cleanup.

## Remaining implementation gates

1. Add native symbols whose pin numbers exactly match the retained TI tables,
   JMS583 datasheet, and TP-053 socket table.
2. Replace the old B-key J3 in the authoritative `STORAGE.kicad_sch`; do not
   patch a PCB-only connector.
3. Add the two selector truth tables and a latched AUTO/FORCE SATA/FORCE NVMe
   control circuit. Validate inactive-state isolation and PEDET-empty safety.
4. Complete the JMS583 reference circuit: rails, 25-MHz crystal, REXT, reset,
   VBUS detect, USB/PCIe AC coupling, internal-regulator inductor, and DNP
   optional SPI NVRAM.
5. Recalculate the storage 3.3-V budget for NVMe inrush/transient and both
   bridges before PCB regeneration.
6. Build and route a complete native fixture, then integrate only after forced
   SATA, forced NVMe, AUTO, empty, reset, and inactive-state audits pass.

No production PCB change is claimed by the footprint generation alone.
