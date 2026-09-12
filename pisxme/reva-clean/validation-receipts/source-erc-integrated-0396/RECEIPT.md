# Integrated STORAGE USB3 label validation — 2026-09-12

- Candidate SHA: `0396a068`
- Toolchain: KiCad Light 10.0.6, qualified image `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`
- Native ERC: 351 findings, 0 errors. Classes: 126 isolated_pin_label, 121 endpoint_off_grid, 53 lib_symbol_issues, 26 same_local_global_label, 22 multiple_net_names, 3 footprint_link_issues.
- Native DRC: 433 violations, 499 unconnected items. No PCB geometry changed in this source-only candidate.
- Native netlist export: RC 0; integrated schematic parity warning remains because the schematic is not fully annotated for parity, recorded rather than waived.
- ERC SHA-256: `65c0f0051a9ec84552daf529871e9a6c2c0c343d40b587482bd57f1d267c34f5`
- DRC SHA-256: `c4d34548b0b847ae40aaec7c1c5e9d1fcdc5f34461d4c80446800e9bf0603a3f`
- XML SHA-256: `288ebbf60a7c4e30d9cadb66e03d0def47350d2c1e14feae0609116dd376e8ed`

Disposition: source-hygiene candidate is integrated and reproducibly validated; Phase 24 remains open because ERC/DRC and physical closure are not clean.
