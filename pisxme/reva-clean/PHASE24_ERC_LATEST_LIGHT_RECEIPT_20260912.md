# Phase 24 latest fresh-Light ERC receipt

Date: 2026-09-12  
Validated ref: `4d31c1bc`  
Validator: fresh `kicad-light` workspace, KiCad 10.0.6

`kicad-cli sch erc` completed with exit code 0 and reported 367 findings.
The canonical warning classes match the local KiCad 10.0.5 census exactly:

| Class | Count |
|---|---:|
| `endpoint_off_grid` | 132 |
| `isolated_pin_label` | 126 |
| `same_local_global_label` | 30 |
| `multiple_net_names` | 23 |

The remaining count is the known KiCad 10.0.6 library/link and pin-type
classification difference (including 53 `lib_symbol_issues` and 3
`footprint_link_issues` in the raw report), not a change to the canonical
warning clusters. No schematic or PCB source was changed by this validation.
The native 10.0.5 311-warning / zero-error result remains the authoritative
local census; this receipt provides independent version-cross-check evidence.
