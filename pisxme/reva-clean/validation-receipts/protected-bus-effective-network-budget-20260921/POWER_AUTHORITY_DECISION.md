# Protected-bus effective-network budget correction

- Decision: `PISXME-P24-PROTECTED-BUS-POWER-AUTHORITY-20260921-R2`
- Rejected candidate: `2bb75c9` (1256 DRC / 431 unconnected / 161 shorts)

The 8.50 mOhm complete hot-path budget is arithmetically valid. The prior 0.650 mOhm term was mis-scoped as a per-branch raw-neck limit and is superseded. It is retained only as the provisional effective nine-branch PCB-neck allocation pending a materially new, evidence-backed architecture/corridor plan. The derived 1.80 mOhm per-branch hot-loop rule is also superseded.

| Effective network term | mOhm |
|---|---:|
| Source harness/mating/crimps | 1.80 |
| Fuse/holder/contact | 0.55 |
| Nine-branch PCB neck network | 0.65 |
| Branch joins/transitions/vias | 0.45 |
| Q1 channel hot | 4.32 |
| Q1 leads/pads/positive transition | 0.15 |
| Protected copper/vias to J1 | 0.25 |
| J1 contact field/spreading | 0.25 |
| Residual | 0.08 |
| **Total** | **8.50** |

Retain: 11.4–12.6 V source, 300 W sustained, 330 W/100 ms peak, 40 A continuous, 45 A peak, 11.05/11.00 V protected minima, nine independent positive/return paths across three connectors, 7 A/contact screen, <=10% qualified branch imbalance, Q1 4.32 mOhm hot allocation, and no N-1/passive-sharing credit before prototype qualification.

The current candidate’s extracted three-group parallel trace-only equivalent is approximately 1.43 mOhm and therefore fails the provisional 0.65 mOhm effective allocation. Do not launch another same-geometry placement variant. Product/Power and MPA must issue one materially new effective-network architecture/corridor plan, with extraction and qualification method, before the package returns READY.
