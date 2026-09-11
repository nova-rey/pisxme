# Phase 24 PWR_FLAG repair probe rejection — 2026-09-11

## Scope

Disposable probe `.phase24_power_flag_probe_v3` replaced every embedded
`power:PWR_FLAG` definition in `CORE_CM5`, `POWER_INPUT`, and `V100_POWER`
with the installed KiCad 10.0.5 authority. The helper was corrected first
because `CORE_CM5` contains two embedded definitions, not one.

## Result

The source substitution itself completed for four definitions, but native ERC
rejected the candidate at 1,054 findings:

| Class | Count |
|---|---:|
| `endpoint_off_grid` | 416 |
| `isolated_pin_label` | 232 |
| `unconnected_wire_endpoint` | 147 |
| `footprint_link_issues` | 115 |
| `lib_symbol_issues` | 75 |
| `same_local_global_label` | 30 |
| `multiple_net_names` | 24 |
| `no_connect_dangling` | 11 |
| `power_pin_not_driven` | 2 |
| `pin_to_pin` | 2 |

The original two `lib_symbol_mismatch` records disappear, but the candidate
creates real unit/pin and library-link defects. It is rejected and was not
promoted to canonical sources. The disposable directory is retained as raw
negative evidence.

## Disposition

The canonical embedded PWR_FLAG definitions remain authoritative. Any future
repair must preserve the project’s embedded unit serialization or perform a
complete native-compatible symbol migration with netlist comparison; a text
replacement is not sufficient.
