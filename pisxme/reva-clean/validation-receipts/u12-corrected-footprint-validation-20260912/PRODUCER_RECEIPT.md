# U12 corrected footprint producer receipt — 2026-09-12

Base source SHA: 48ff2c48439ca911c144a7c6b5392bb0b1659337

Scope: footprint-only geometry for U12 HD3SS6126_RUA0042A; no schematic, rules, routes, U11, power, or J1 edits.

TI QFND142D geometry applied to perimeter pads: 0.50 mm pitch, 0.60 x 0.25 mm pads, 42 perimeter pads. Existing pad 43 exposed-pad number, net, size, and layers preserved because this candidate does not alter the thermal-pad contract.

Local coordinate transformation (board placement/orientation unchanged):
- Pads 1–17: x=-1.5, y=-4.0..4.0 in 0.5 mm steps.
- Pads 18–21: y=+4.4, x=+0.75..-0.75 in 0.5 mm steps, rotation 90.
- Pads 22–38: x=+1.5, y=+4.0..-4.0 in 0.5 mm steps.
- Pads 39–42: y=-4.4, x=-0.75..+0.75 in 0.5 mm steps, rotation 90.

Mechanical caution: exact TI exposed-pad copper/paste segmentation and courtyard were not changed; this is a bounded perimeter geometry producer candidate for authority review.

Changed files: PiSXMe_RevA_Clean.pretty/HD3SS6126_RUA0042A.kicad_mod and PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb.
