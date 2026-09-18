# Isolated worker baseline receipt

Worker base: `708a2ec9` (`reva-clean`)
KiCad CLI: `10.0.6`
Inspected: `pisxme/PiSXMe.kicad_sch`, `pisxme/PiSXMe.kicad_pcb`

The board is a six-layer, 1.6 mm nominal stackup with F.Cu, In1.Cu, In2.Cu,
In3.Cu, In4.Cu, and B.Cu; copper finish is ENIG. Rules are in
`PiSXMe.kicad_dru`. No Anderson/Powerpole footprint or reference is present.
Existing J5/J6 are Molex 22-23-2041 fan-header entries and were not edited.

Fresh pre-mutation KiCad Light checks:

```text
kicad-cli sch erc --format json .../PiSXMe.kicad_sch
Found 130 violations; status 0 without --exit-code-violations

kicad-cli pcb drc --format json .../PiSXMe.kicad_pcb
Found 803 violations and 182 unconnected items; status 0 without
--exit-code-violations
```

These are inherited project baseline findings, unrelated to the isolated audit.
No canonical board/schematic mutation was performed.
