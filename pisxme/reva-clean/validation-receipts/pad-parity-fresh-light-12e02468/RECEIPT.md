# Fresh Light schematic-to-PCB pad-net parity audit

- Source commit: `12e02468`
- Worker: `pisxme-kicad-light:v1`, KiCad 10.0.6
- Native schematic nodes: 814
- PCB pads: 1,262
- Excluded contract nodes: nonphysical_x=65, j1_placeholder=2, j3_key_gap=8
- Alias contracts: J2=18, F1=2, F2=2, J4=6
- Expected-pad mismatches: 0
- Result: schematic-to-PCB pad-net parity PASS within the script's stated scope.
- Scope limit: this does not prove surplus-pad correctness, physical routing, or full bidirectional acceptance by itself. Native KiCad parity still reports separate metadata/net conflicts.
