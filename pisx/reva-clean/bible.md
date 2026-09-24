
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

2026-09-24: A second Heavy v2 method-change attempt calibrated and dismissed the KiCad Setup modal, loaded the board, and exercised direct GUI routing, but saved no candidate; base hash remained unchanged. Evidence is retained in `protected-bus-heavy-waypoint-method-change-20260924`; producer remains parked for a capability-level escalation.

2026-09-24: A third Heavy v2 attempt explicitly cleared KiCad Setup and used direct xdotool-assisted Route Single Track control, reached the first MPA waypoint, then failed to advance and was undone. No candidate or canonical CAD change exists; receipt `protected-bus-heavy-direct-xdotool-20260924` is the capability-exhaustion evidence for HPQ escalation.

2026-09-24: MPA corrected the protected-bus corridor semantic conflict. The binding path is all-orthogonal F.Cu: J5.2 `(16.20,25.00)` -> `(16.20,27.40)` -> `(50.00,27.40)` -> `(50.00,13.75)` -> F2.1 `(57.60,13.75)`, with actual courtyard-based clearance. No CAD was edited; HPQ #8 remains the capability-resolution owner.

2026-09-24: HPQ #8 reached resolution-ready after the runner restart. Its authority-only MPA semantic correction is reconciled at current HEAD; the corrected protected-bus producer is claimed for isolated implementation and fresh Light validation. No CAD candidate or Phase 24 closure is claimed.
