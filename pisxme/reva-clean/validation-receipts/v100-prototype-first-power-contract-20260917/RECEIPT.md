# Receipt — V100 prototype first-power contract

- **Package:** `P24-V100-PROTOTYPE-FIRST-POWER-CONTRACT`
- **Contract:** `PISXME-P24-V100-FIRST-POWER-20260917` revision 1.0
- **Assigned base:** `c2e0194c432e712d6f8386b9682f038dd06188e6`
- **Result:** `DONE` for the delegated design-artifact scope
- **CAD changed:** no
- **Hardware operated:** no
- **Production qualification:** not claimed

## Work performed

The contract binds a staged, current-limited prototype bring-up procedure to
the signed protected common 12 V architecture. It covers unpowered inspection,
resistance/diode checks, source/protected-bus checks, local rails, EN/PG/reset/
PERST#/inhibit observations, CM5-only operation, inhibited V100 installation,
incremental low-load enable, mandatory shutdown criteria, thermal/contact
checks, run-record fields, and fault recovery.

The procedure retains 300 W sustained and 330 W bounded peak as product
requirements. It does not claim those values were measured. It explicitly
marks undocumented SXM2 sequencing, installed contact-field distribution,
load-step behavior, thermal installation, shutdown/restart, and PCIe/GPU
operation as `REQUIRES_PROTOTYPE_VALIDATION`.

## Validation

- JSON parses successfully with Python's standard `json` parser.
- The JSON and Markdown were inspected for matching contract ID, package ID,
  base SHA, product envelope, stage ceilings, and no-hardware-claim boundary.
- No `.kicad_sch`, `.kicad_pcb`, footprint, rule, configuration, or private
  Library file was modified.
- `SHA256SUMS` covers the contract and receipt files.

This receipt is design-validation evidence only. A future hardware run must
return raw measurements and hashes before any prototype stage can be marked
`PASS`.

