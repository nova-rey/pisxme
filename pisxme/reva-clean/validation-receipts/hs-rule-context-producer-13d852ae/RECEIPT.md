# Scoped high-speed netclass producer candidate

- Producer base: `4eaf2ab8`; producer commit: `13d852ae` (project-rule context only)
- Integrated source currently contains the previously validated C7/C25 silk repair; no copper, schematic, storage, power, J1, or global minimum edits were made.
- Added project-local netclasses: `HS_PCIE_90R` (eight CM5/V100 PCIe/REFCLK/PET0 nets), `HS_USB3_90R` (four CM5 USB3 nets), and `PCIE_PERST_CONTROL` (CM5_PERST). Each uses 0.13208-mm width; ordinary `Default` remains 0.20 mm. Differential gap is 0.2032 mm for HS classes.
- Netclass patterns: 13 exact net names; no wildcard patterns.
- Producer DRC: 201 violations / 499 unconnected items; the 72 high-speed width findings are removed under the scoped classes.
- Negative control: retained reference run still reports ordinary 0.100-mm tracks against the normal floor, demonstrating scoped context does not globally permit undersized ordinary routing.
- This is a producer/integration candidate, not Phase 24 closure. Return-path, skew, SI, and remaining DRC/connectivity evidence remain open.
- Raw outputs and checksums retained here.
