# Phase 24 Path-A focused audit — 2026-09-06

Input authority:

- schematic: `STORAGE.kicad_sch`
- PCB candidate: `PHASE24_DUAL_MODE_STORAGE_SUPPORT_ROUTED.kicad_pcb`
- Path A: CM5 USB → HD3SS6126 → TUSB9261/JMS583 → HD3SS3412 → TE M-key

## Native/source audits

```text
python3 phase24_dual_mode_storage_schematic_audit.py
PASS dual-mode schematic instances, footprints, and required net labels

python3 phase24_dual_mode_storage_library_audit.py
PASS JMS583 has 64 pads
PASS JMS583 numbering is 1..64
PASS HD3SS6126_RUA0042A.kicad_mod has 42 signal pads plus EP
PASS HD3SS3412_RUA0042A.kicad_mod has 42 signal pads plus EP
PASS TE M-key has 67 contacts plus four mechanical pads
PASS TE M-key preserves key gap 59..66

python3 phase24_dual_mode_storage_mode_audit.py --allow-auto-open
PASS dual-mode mode contract

python3 phase24_jms583_support_audit.py STORAGE.kicad_sch
PASS JMS583 required support network authority
```

## Native PCB result

`kicad-cli pcb drc --severity-all` exits zero as a tool invocation and writes
`PHASE24_PATHA_SUPPORT_ROUTED_NATIVE_20260906-drc.rpt`, but the design result
is not a pass: **1,160 violations and 499 unconnected items**. This is a
partial route-development fixture, not full-board closure. No severity was
changed and no findings were waived.

The source/mode/library audits therefore close only the corresponding Path-A
authority claims. They do not close native connectivity, routing, ERC/DRC,
mode-state isolation, mechanical parity, or Phase 24.

