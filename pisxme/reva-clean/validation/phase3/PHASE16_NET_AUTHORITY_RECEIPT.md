# Phase 16 PCIe net-authority receipt

Checked: 2026-08-30. Status: `CLOSED` for schematic net authority; PCB
routing remains the active Phase 16 gate.

The clean root authoring path now declares five direct cross-sheet links:
PER0_P/N, REFCLK_P/N, and PERST. It also links the two CM5-side PET0 ports to
the V100 child before C1/C2. The V100 connector endpoints use the same
canonical CM5 net names for direct paths.

PET0_P/N are intentionally excluded from the direct-to-connector set. Their
CM5/source and V100/endpoint sides remain distinct and are connected only
through C1 and C2.

The Phase 4 instance helper now assigns pin UUIDs distinct from the containing
symbol UUID; this prevents KiCad netlist pin-identity aliasing. Native KiCad
10 export proves J7-to-SXM2 identity for all five direct paths and preserves
the PET0 split. Regression: `test_phase16_pcie_net_authority.py`.

The generic authoring sources are `phase3_scaffold.py` and
`phase4_v100_lane0.py`; `phase16_pcie_net_authority.py` migrates the existing
later-phase root without regenerating child-sheet content.
