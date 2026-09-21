# R1 protected-bus Product/Power Authority decision

- Decision: `PISXME-P24-PROTOTYPE-POWER-BUS-POWER-AUTHORITY-20260921`
- Evidence: R3/R1 isolated candidates `f5e873b6`, `14812360`, `894fa433`, `426bc7e`; fresh Light counts 997/383, 1013/364, 679/390, and 1220/391.

The nine-branch protected-bus topology remains valid. The exact R1 3x3 fuse grid and mandatory long ordered In2 raw lanes are superseded because they contradict the R3 allocation of **0.65 mOhm total hot resistance for each raw branch positive-plus-return PCB neck**. A 2 mm-wide 1 oz outer-copper conductor is approximately 2.46 mOhm for 20 mm; its positive-plus-return pair is about 4.93 mOhm for 20 mm and about 19.7 mOhm for 80 mm. Inner 0.5 oz copper is higher resistance.

## Retained invariants

Retain 11.4–12.6 V source, 300 W sustained, 330 W for 100 ms, 40 A continuous, 45 A peak, protected minima 11.05/11.00 V, complete hot path <=8.50 mOhm, three source headers, nine independent fused positive/return pairs, no passive-sharing or N-1 credit, J1 mapping, unknown/no-connect assignments, six-layer roles, ordinary through-vias, protected/high-speed corridors, and native connectivity/current/via/thermal/resistance closure.

## Superseded implementation constraints

Supersede only the exact F1–F9 coordinates, long ordered In2 raw lanes, prohibition on relocating the fuse bank within the source-entry region, and the R1 no-alternate-placement clause. MPA must issue one revised local plan placing each fuse bank close enough to its source header to satisfy the 0.65 mOhm branch allocation while preserving branch identity and the protection/J1 transition unless evidence proves that insufficient.

No global rule relaxation, J1 remap, topology reduction, or six-layer change is authorized.
