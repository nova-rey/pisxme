# Phase 24 fresh KiCad Light DFM validation — 2026-09-12

The committed ref `5148df63` was validated in a fresh detached KiCad Light
workspace (`dfm-validate-20260912`) using the read-only project mount:

```text
kicad-cli pcb drc --severity-all \
  --output /workspace/output/acreage-validate-drc.rpt \
  /workspace/project/pisxme/reva-clean/ACREAGE_CANDIDATE.kicad_pcb
```

Result: **180 violations / 468 unconnected items**. This confirms the
committed candidate's DFM result independently of the producer workspace.
It is not a Phase 24 pass: the candidate is not yet the fully integrated,
parity-closed acreage board, and manufacturing findings remain open.
