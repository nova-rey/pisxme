# Phase 24 clean-worker baseline reproduction

- Base/source commit: `d0af3cc8`
- Worker: `kicad-light`, image `pisxme-kicad-light:v1`
- KiCad CLI: `10.0.6`
- Command: `kicad-cli pcb drc --format json --severity-all --exit-code-violations -o baseline-drc.json PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- Return code: `5` (violations present)
- Result: **314 violations; 499 unconnected items**.
- Scope: untouched committed baseline reproduced in a clean disposable worker. This is baseline evidence only and does not close any acceptance row.
- Raw output and checksum: `baseline-drc.json`, `SHA256SUMS`.
