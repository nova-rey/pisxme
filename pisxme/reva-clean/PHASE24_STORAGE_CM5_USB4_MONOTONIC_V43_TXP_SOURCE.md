# Phase 24 Path-A V43 TX_P source-field experiment

## Disposition

**REJECTED — route implementation experiment.** This disposable candidate
was generated from V41 after correcting an authoring typo that had passed a
`PAD` object where a coordinate was required. The corrected script authored
the intended U7.57 source escape, but the resulting F.Cu path enters the U7
power-pad field and creates real `POWER_GND` / `BRIDGE_SATA_TX_P` shorts and
mask/clearance conflicts.

## Native evidence

- Board: `PHASE24_STORAGE_CM5_USB4_MONOTONIC_V43_TXP_SOURCE.kicad_pcb`
- DRC: `PHASE24_STORAGE_CM5_USB4_MONOTONIC_V43_TXP_SOURCE-drc.rpt`
- Native DRC: **605 violations / 400 unconnected items**
- Shorting entries: present; the report identifies U7 pad 65 `POWER_GND`
  against the new TX_P F.Cu escapes near `(95.8,127.8)` and `(95.8,125.5)`.
- SATA endpoint audit: **FAIL** at `U7.57`.
- USB3 native connectivity audit: **PASS** for all audited endpoints.

The earlier V43 traceback was a tooling typo and is not engineering
evidence. After correction, the candidate was tested natively and rejected.
V41 remains the best disposable Path-A parent (599 DRC / 399 opens / zero
shorting entries). No production-authoritative PCB was changed.

## Next action

Preserve V41's source-field allocation and continue with a complete,
obstacle-aware SATA TX corridor regeneration on the selector side; do not
reuse the V43 U7 power-field escape.
