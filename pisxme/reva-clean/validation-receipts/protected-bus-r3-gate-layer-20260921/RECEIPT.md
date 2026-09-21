# Protected Bus R3 Layer-Aware Gate Candidate

- Base source commit: `6428197f`
- Producer: `root-mediated-gate-layer-20260921`
- Image: `pisxme-kicad-light:v1`
- KiCad: `10.0.6`
- Input artifact: `protected-bus-r3-support-local-links-20260921/PHASE24_PROTECTED_BUS_R3_SUPPORT_LOCAL_LINKS.kicad_pcb`
- Method: remove only existing `GATE_A` copper; add a short F.Cu pad escape from U1 gate pad 5 to a through-via, then an In2 segment to Q1 gate pad 3. No source/J1/high-speed geometry was edited.
- Native Light DRC: `981` violations, `434` unconnected items, `0` footprint errors, exit code `5` (violations present).
- Comparison: prior support-local checkpoint `986/434`; improvement is five fewer violations with unchanged unconnected count.
- Result: candidate evidence only; not canonical integration and not a Phase 24 acceptance pass.
- Command: `python3 /workspace/project/apply_gate_layer.py`; `kicad-cli pcb drc --severity-all --exit-code-violations -o /workspace/output/gate-layer/gate-layer-drc.rpt /workspace/project/pisxme/reva-clean/PHASE24_PROTECTED_BUS_R3_GATE_LAYER.kicad_pcb`
Fresh Light validation result: FAIL (983 DRC violations, 434 unconnected; candidate is not an integrated acceptance result).
