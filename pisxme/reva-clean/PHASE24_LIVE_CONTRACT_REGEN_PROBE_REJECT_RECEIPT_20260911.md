# Phase 24 live contract regeneration probe rejection — 2026-09-11

## Hypothesis

Use the live identity map and each child hierarchical label's actual Y
coordinate to regenerate the embedded contract-symbol pins and instance pin
list, without changing root sheets, circuit symbols, or net names.

## Disposable result

Probe: `.phase24_live_contract_probe_v2`.

Native KiCad 10.0.5 ERC reported 866 findings:

| Class | Count |
|---|---:|
| `endpoint_off_grid` | 416 |
| `isolated_pin_label` | 232 |
| `unconnected_wire_endpoint` | 144 |
| `same_local_global_label` | 30 |
| `multiple_net_names` | 24 |
| `no_connect_dangling` | 11 |
| `lib_symbol_mismatch` | 5 |
| `pin_not_connected` | 4 |

The four new errors are the sparse late support ports: `REGULATORS` pins
`BRIDGE_3V3`/`BRIDGE_1V1` and `STORAGE` pins `BRIDGE_3V3`/`BRIDGE_1V1`.
Their source wires exist in the child files, so this result demonstrates that
contract-symbol placement alone is not sufficient to reproduce KiCad's native
association for those sparse ports. The first probe's Y-sign error was fixed;
this remaining failure is a real serialization/association issue.

## Disposition

Rejected and not promoted. Canonical root/children and electrical intent were
unchanged. The script is retained as disposable implementation evidence; the
next regeneration must use native association semantics for the sparse ports,
not another blind coordinate perturbation.
