# Phase 24 F.Cu ground-plane width-normalized candidate

Date: 2026-09-12  
Base: `PHASE24_FCU_POWER_GND_PLANE_PROBE.kicad_pcb`  
Candidate: `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`

The candidate widens only 32 pre-existing undersized `POWER_GND` tracks to
the ordinary 0.20 mm minimum, refills the native zones, and leaves all signal
tracks and footprints unchanged. Producer native DRC reports 440 violations
/ 265 unconnected items, down from 472/265. It has zero shorts and the same
two inherited crossings.

This is a repair basis, not a Phase 24 pass. Fresh validator, power/SI,
manufacturing, and remaining connectivity checks are required before any
promotion decision.

Fresh KiCad Light validation from `fc44ebca` reproduces 440 violations / 265
unconnected items. Fresh native XML source-to-pad parity also passes with 814
authoritative schematic nodes, 1,262 PCB pads, and 0 mismatches. The candidate
is the current bounded repair basis; it is not closure.
