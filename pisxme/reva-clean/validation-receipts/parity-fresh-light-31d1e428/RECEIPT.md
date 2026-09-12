# Fresh isolated Light schematic-parity attempt

- Source commit: `31d1e428`
- Worker: `pisxme-kicad-light:v1`, KiCad 10.0.6
- Command: `kicad-cli pcb drc --schematic-parity --severity-all --format json`
- Native parity preflight: **failed to fetch schematic netlist; schematic parity requires a fully annotated schematic**
- DRC fallback result: 312 violations / 499 unconnected items
- Disposition: parity row remains open; no CAD changes.
