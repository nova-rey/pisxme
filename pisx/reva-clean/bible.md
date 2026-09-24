
2026-09-24: Click-on-via candidate 5acf732e completed GUI/save/reopen but fresh Light found 926 DRC versus 919 baseline (+7); rejected and returned to producer method queue.

2026-09-24: Compared rejected click-via candidate to a fresh same-HEAD baseline: +6 clearance and +1 shorting_items (PWR_SRC_J9_P1 versus 12V_PROTECTED); unconnected improved by one. Evidence confirms local geometry is not acceptable.

2026-09-24: MPA rejected the tested (24.514048,24.273596) waypoint after fresh Light showed +6 clearance and +1 short; replacement corridor remains required before another producer attempt.

2026-09-24: Parked protected-bus producer on explicit MPA replacement-waypoint authority dependency; only tested waypoint is rejected.

2026-09-24: Parked protected-bus producer on explicit MPA replacement-waypoint authority dependency; only tested waypoint is rejected.

2026-09-24: Removed transient work-queue lock from tracked files; queue state remains in work-queue.json.

## 2026-09-24 — Protected-bus replacement corridor authority

Macro Placement Authority rejected the failed J5.2-to-F2.1 via route and bound one
replacement top-side F.Cu corridor: `(16.20,25.00) -> (18.35,27.15) -> (50.00,27.15) -> (50.00,13.75) -> (57.60,13.75)`, with no via or raw In2 lane. The decision preserves fixed 12V_PROTECTED geometry, In1/In4 returns, and all R3 resistance/current/DFM/DRC gates. The producer may resume only through one isolated Heavy v2 candidate and fresh Light validation.

Queue state: `authority:protected-bus-mpa-replacement-waypoint-20260924` resolved by the MPA receipt; only the protected-bus producer subtree is eligible to resume, subject to the isolated Heavy v2 producer and fresh Light validation gates.

2026-09-24: Qualified Heavy v2 replacement-corridor attempt launched from `9bda92d4` and produced route screenshots but no saved candidate before bounded GUI control stalled; no CAD was integrated. Receipt `protected-bus-heavy-v2-replacement-timeout-20260924` parks only the producer for Tier-2 method change while preserving the MPA corridor.
