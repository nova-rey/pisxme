# Schematic-parity context probe

- Source commit: `57bb50bf`
- Worker: writable qualified `pisxme-kicad-light:v1`, KiCad 10.0.6
- Validation-only context operation: copied canonical `PiSXMe_RevA_Clean.kicad_sch` to the PCB stem expected by KiCad parity, without modifying canonical files.
- Result: 312 native DRC violations, 499 unconnected items, **528 schematic parity issues**.
- Conclusion: the earlier “fully annotated schematic” preflight was a filename/context lookup failure. With matching stem, parity runs and exposes real mismatches; this is not a waiver or closure.
