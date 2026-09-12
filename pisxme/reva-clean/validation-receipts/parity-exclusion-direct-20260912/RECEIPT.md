# Fresh native parity and exclusion audit — 2026-09-12

Source commit: `88085b3b`.
Toolchain: KiCad Light 10.0.6.

Native schematic netlist export used `--format kicadxml` and returned 0.
The instrumented audit reported 814 authoritative schematic nodes, 1262 PCB
pads, and 0 expected-pad mismatches. Explicit exclusions were
`nonphysical_x=65`, `j1_placeholder=2`, and `j3_key_gap=8`; alias contracts
were reported for J2, F1, F2, and J4. The parity comparison passed.

This closes only the bounded ownership/parity evidence scope; it does not
prove physical routed connectivity, power delivery, or integrated DRC closure.
