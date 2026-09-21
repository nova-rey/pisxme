# Protected-bus R3 Macro Placement Authority decision

- Decision ID: `PISXME-P24-PROTOTYPE-POWER-BUS-MPA-R3-20260921`
- Base: `627ec337a28ce0c732df7744dc3ba360414464db`
- Trigger evidence: parent `f5e873b6` (997 DRC / 383 unconnected), B.Cu terminal attempt (989 / 383), F.Cu correction `14812360` (1013 / 364).
- Authority outcome: bind a staged corridor and local source/protection cohort; do not change system topology or J1 mapping.

## Fixed anchors

J1 `(150.00,90.00)` top 0 degrees; J5 `(12.00,25.00)` top 0 degrees; J6 `(12.00,45.00)` top 0 degrees; board outline, six-layer stack, high-speed/timing corridors, and existing return planes remain fixed.

## Binding local cohort

| Reference | Position | Rotation | Side |
|---|---:|---:|---|
| F1 | (32.00,22.00) | 0 | top |
| F2 | (32.00,54.00) | 0 | top |
| D1 | (49.00,8.00) | 0 | top |
| D2 | (49.00,70.00) | 0 | top |
| U1 | (49.00,22.00) | 0 | top |
| U2 | (49.00,54.00) | 0 | top |
| Q1 | (61.00,22.00) | 0 | top |
| Q2 | (61.00,54.00) | 0 | top |
| C3 | (47.00,24.00) | 0 | top |
| C4 | (47.00,56.00) | 0 | top |

## Corridor and layers

- Positive representative: J5.1 -> F1 -> D1/U1 -> Q1.2 -> J1 mapped 12V contacts.
- Escape Q1/Q2 on F.Cu to ordinary through-via arrays no earlier than x=66 mm; keep branches separate until x>=66 mm.
- Transition to `In3.Cu` protected plane; reserve approximately `(66,14)` through `(124,74)` and approach J1 from `(122,83)` through `(149,98)`.
- Use an F.Cu transition-via ladder outside the J1 SMD field; no B.Cu terminal, via-in-pad, or single-via 40 A path.
- Returns use local F.Cu plus distributed through-via arrays into `In1.Cu`/`In4.Cu`, then separate F.Cu fanout to mapped J1 `POWER_GND` contacts. No shared return neck or signal-as-return.
- B.Cu high-speed corridors remain protected; `In2.Cu` retains its existing PWR role.

## Contract and gate

Preserve R3: 11.4–12.6 V, 300 W sustained, 330 W/100 ms peak, 40 A continuous, 45 A/100 ms, complete 8.50 mOhm hot path. Producer must return changed-scope manifest, native targeted checks, branch/path extraction, and via/current/thermal evidence. This decision authorizes the isolated producer only; it does not authorize canonical integration.
