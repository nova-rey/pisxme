# Bidirectional surplus-pad coverage audit

- Source commit: `3cb079bb`
- Worker: `pisxme-kicad-light:v1`, KiCad 10.0.6
- Expected schematic pad keys: 814
- Actual PCB pad keys: 1,262
- Surplus actual pads: 448
- Surplus with assigned net: 313
- Surplus with no net: 135

Most surplus assigned pads are J1's 12V_PROTECTED/POWER_GND field, which is outside the schematic's two placeholder pins and must be covered by the approved J1 contact contract. The 135 no-net pads and all surplus classes require explicit classification before bidirectional acceptance can close. This audit does not invent assignments.
