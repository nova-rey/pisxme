# Exact-head fresh Light validation

- Candidate: `17dd81d2`
- Worker image: `pisxme-kicad-light:v1`, KiCad 10.0.6
- Inputs: canonical schematic/PCB/project/rules from that committed head

Fresh isolated checks report:

- Native DRC: 312 violations, 499 unconnected items, no shorting-items class.
- Native ERC: 351 findings.
- Native netlist export: completed; retained as `native.xml`.
- DRC explicit violation-exit run recorded `DRC_RC=5` in `returncodes.txt`.

These are validation results, not closure. The exact-head reports supersede
older candidate references for final acceptance binding; open crossings,
opens, ERC findings, and all other acceptance gaps remain.
