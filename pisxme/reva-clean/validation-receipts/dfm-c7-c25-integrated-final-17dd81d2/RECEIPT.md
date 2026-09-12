# Integrated validation after residual C7/C25 silk repair

- Integrated candidate/source commit: `17dd81d2`
- Fresh validator: `pisxme-kicad-light:v1`, KiCad 10.0.6
- Command: `kicad-cli pcb drc --format json --severity-all --exit-code-violations -o integrated-drc.json PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- Result: 312 DRC violations, 499 unconnected items; no acceptance closure.
- Change scope: C7 and C25 F.SilkS reference placement only; no copper, pads, nets, rules, storage, power, or J1 changes.
- The two residual silk-over-copper findings are removed; all remaining physical and connectivity findings remain subject to Phase 24 acceptance.
- Raw output/checksum retained here.
