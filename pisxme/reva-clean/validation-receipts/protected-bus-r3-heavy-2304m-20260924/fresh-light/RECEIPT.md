# Fresh Light validation — Heavy 2304m protected-bus candidate

- Candidate SHA: `a19c403ac13897fc7515ed8d57461add61329400`
- Light image/tool: qualified PiSXMe Light worker, KiCad 10.0.6
- Result: `REJECTED`
- Native DRC: 927 violations, 434 unconnected items
- Same fresh baseline: 919 violations, 435 unconnected items
- Delta: +8 DRC violations, -1 unconnected item

The candidate is not integrated. The added defects include the co-located F2.1 via and related clearance/hole findings recorded in the Heavy report. Source connectivity for the selected branch is not sufficient to close the integrated acceptance row.
