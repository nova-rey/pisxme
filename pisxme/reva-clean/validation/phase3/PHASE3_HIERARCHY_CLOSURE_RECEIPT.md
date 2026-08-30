# Phase 3 hierarchy closure receipt

Checked: 2026-08-30 with KiCad 10.0.5.

## Defect and correction

The child generator appended each `PiSXMeRevAClean:*_Contract` definition
after the closing `(lib_symbols ...)` expression. KiCad therefore loaded the
child as an incomplete screen, and root ERC misleadingly reported
`hier_label_mismatch` for every sheet pin.

The generic authoring path now:

- inserts the contract definition before the child library block closes;
- negates library-pin row Y coordinates to match KiCad schematic placement;
- places hierarchical labels with the native left-edge orientation; and
- creates root wires terminating at every hierarchical sheet pin.

## Native evidence

`validation/phase3/test_native_hierarchy_authoring.py` regenerates the ten
children, checks the serialized library-block and coordinate invariants, and
runs:

```text
xvfb-run -a kicad-cli sch erc --exit-code-violations --severity-error
```

Result: `Found 0 violations`, exit code 0.

Additional native checks passed:

- root PDF export through KiCad 10.0.5;
- KiCad XML netlist export through KiCad 10.0.5;
- clean CM5 symbol/footprint parity: 200 pins = 200 pads;
- clean-source namespace/path scan: no legacy `PiSXMe:` IDs or machine-local
  model paths.

This closes `ROOT_HIERARCHY_ASSOCIATION`. It does not claim production
placement, routing, fabricated-hardware operation, or completion of later
production-island parity work.
