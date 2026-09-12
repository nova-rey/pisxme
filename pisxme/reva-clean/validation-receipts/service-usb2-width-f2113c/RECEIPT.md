# SERVICE USB2 width producer candidate — 2026-09-13

- Producer base: `bf056be3`
- Candidate PCB SHA-256: `f2113cff03eb222351072a77d7776f8297619838667026ea8891c18fd549f0aa`
- Scope: widened 30 F.Cu/B.Cu? `SERVICE_USB2_DP`/`SERVICE_USB2_DM` track segments below the normal 0.20 mm minimum to exactly 0.20 mm. No high-speed PCIe/USB3 tracks, footprint geometry, rules, or net ownership changed.
- KiCad Light 10.0.6 native DRC: 431 violations / 499 unconnected items, versus 433 / 499 integrated baseline.
- DRC JSON SHA-256: `efee99f1327810ad04e02bbbacd43b0f7e56fa706467e0853cb1e1c1044fa44c`
- Decision: promote for serialized integration and fresh validation; Phase 24 remains open.
