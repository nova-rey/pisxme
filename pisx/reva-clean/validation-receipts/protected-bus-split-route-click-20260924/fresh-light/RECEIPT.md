# Fresh Light validation — protected-bus click-via candidate

- Candidate SHA: `5acf732e30a7379eec73a7348150a277d8db0bb6`
- Base SHA: `f27f892b74c940c3d36b9c6f933bd535ccc16f85`
- Toolchain: KiCad Light 10.0.6
- Baseline: 919 DRC violations / 435 unconnected items (`protected-bus-r3-current-head-baseline-20260921`)
- Candidate: 926 DRC violations / 434 unconnected items
- Result: **FAIL** native targeted DRC; +7 DRC violations. Candidate is rejected and not integrated.
- No claim of complete path-budget or thermal/DFM closure is made from this rejected candidate.
