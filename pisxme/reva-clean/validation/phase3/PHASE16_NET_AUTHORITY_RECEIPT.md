# Phase 16 PCIe net-authority receipt

Checked: 2026-08-30. Status: `CLOSED` for schematic net authority; PCB
routing remains the active Phase 16 gate.

The clean root authoring path now declares five direct cross-sheet links:
PER0_P/N, REFCLK_P/N, and PERST. The links connect the `CORE_CM5` sheet pins
to the corresponding `V100_PCIE` CM5-side sheet pins with one native root wire
each. The V100 connector endpoints use the same canonical CM5 net names.

PET0_P/N are intentionally excluded from the direct-link table. Their CM5 and
V100 sides remain distinct and are connected only through C1 and C2.

The Phase 4 instance helper now assigns pin UUIDs distinct from the containing
symbol UUID; this prevents KiCad netlist pin-identity aliasing. Native KiCad
10 export proves J7-to-SXM2 identity for all five direct paths and preserves
the PET0 split. Regression: `test_phase16_pcie_net_authority.py`.

The generic authoring sources are `phase3_scaffold.py` and
`phase4_v100_lane0.py`; `phase16_pcie_net_authority.py` migrates the existing
later-phase root without regenerating child-sheet content.
