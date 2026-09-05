# Phase 24 acreage validation status

Status: IN PROGRESS — native ERC authority repaired; netlist annotation
warning remains under audit.

## Closed in this checkpoint

- The clean project now resolves all 34 custom symbols through the assembled
  `PiSXMe_RevA_Clean_complete.kicad_sym` library.
- `phase24_repair_root_hierarchy.py` generically replaces the malformed root
  interior/diagonal wiring with outward sheet-edge stubs and named root
  associations, preserving child UUIDs and sheet instances.
- The CM5 sheet border is extended where the legacy final pin was outside its
  rectangle.
- Two unused MIPI1 D2 pins are explicitly marked no-connect; they are outside
  the Rev A interface contract.
- Native KiCad 10.0.5 ERC with `--severity-error` reports `Found 0 violations`.
- `validation/phase3/test_phase24_native_final_authority.py` passes.

## Remaining gate

Native netlist export writes a non-empty artifact but emits:
`Warning: schematic has annotation errors, please use the schematic editor to
fix them`.  The remaining investigation is to identify the exporter’s
annotation source and prove a warning-free export without weakening schematic
or PCB parity.  Phase 24 is not marked closed until that evidence is resolved.

Artifacts: `PHASE24_NATIVE_ERC_FINAL2.rpt`,
`PHASE24_NETLIST_FINAL3.xml`, and the Phase 24 native-authority regression.
