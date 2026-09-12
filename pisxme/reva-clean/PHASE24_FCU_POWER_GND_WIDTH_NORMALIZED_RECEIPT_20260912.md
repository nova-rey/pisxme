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
