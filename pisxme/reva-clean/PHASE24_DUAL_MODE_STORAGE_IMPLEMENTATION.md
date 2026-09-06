# Phase 24 dual-mode storage implementation

Status: `IN PROGRESS — library authority landed; native schematic integration
and routed mode fixture remain open` (2026-09-06).

The active implementation is the storage-local two-bridge topology:

`CM5 USB -> HD3SS6126RUAR -> {TUSB9261 SATA | JMS583-QHFA3A NVMe}
-> HD3SS3412RUAR -> TE 1-2199230-4 M-key Socket 3`.

The selected JMS583 is factory mask-ROM qualified for baseline use. Its
optional SPI NVRAM remains DNP. This does not close procurement: JLC's exact
part listing currently reports zero stock and broker listings are not an
authorized source.

## Land-pattern artifacts

`phase24_generate_dual_mode_storage_libraries.py` emits three native
footprints from retained authorities:

- `JMS583_QFN64_8x8.kicad_mod`: QFN64, 0.4-mm pitch, 8-mm body, 64 pads.
- `HD3SS_RUA0042A_WQFN42.kicad_mod`: TI RUA0042A, 42 pads plus exposed pad
  43, shared by the two selected TI switches.
- `TE_1-2199230-4_MKEY.kicad_mod`: 67 contacts with the TP-053 M-key gap.

The generated files are review candidates until native pad-by-pad comparison
against the TE DXF/application drawing and TI/JMicron package pages is signed
off. The library audit is intentionally structural; it does not assert PCB
connectivity.

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
