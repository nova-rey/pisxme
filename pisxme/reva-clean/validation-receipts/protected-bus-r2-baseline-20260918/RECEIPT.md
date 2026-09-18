# Protected-bus R2 fresh baseline receipt

- Source base: `34dbf5dcc9a22faf398ca2ed20722a1cd31bc7e1`
- Selected PCB: `pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- Tool: qualified `pisxme-kicad-light:v1`, KiCad `10.0.6`
- Command: `kicad-cli pcb drc --output selected-baseline-drc.rpt PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- Result: native checker returned RC 0; 300 DRC violations and 499 unconnected items.
- Scope: untouched baseline reproduction before R2 producer edits; this is not an acceptance pass.
- Raw report: `selected-baseline-drc.rpt`
