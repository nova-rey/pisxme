# Protected Bus R3 Current-Head Baseline Receipt

- Base commit: `c7656c0e30b50600adf352c6f1aeb0544ebebc94`
- Worker: `pisxme-kicad-light:v1`
- KiCad: `10.0.6`
- Workspace: `root_mediated_cad_dispatch_20260921`
- Command: `kicad-cli pcb drc --format json --output current_head_drc.json PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- Result: 919 DRC violations; 435 unconnected items
- Purpose: fresh current-head baseline only; not producer closure
- Raw report SHA-256: `78bcd8ff817c237175ff8e569ae8c966eeedd8a5a6eff5c60966aae20fe9660e`
