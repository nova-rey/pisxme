# MPA R3 current-head reconciliation

- Decision: `PISXME-P24-PROTOTYPE-POWER-BUS-MPA-R3-20260921-R1`.
- Original authority base: `627ec337`; no CAD changes are imported.
- Current canonical HEAD checked: `c4478f70`.
- Reconciliation evidence: current-head probes in `protected-bus-r3-issue7-resume-20260921/` confirm J1/J5/J6/J9 anchors and the 3x3 F1-F9 grid remain at the authority coordinates; P2/P5 are unrouted and therefore remain producer scope.
- Scope: source-entry placement/corridor only. Product/Power R3 budget correction remains binding, including effective nine-branch neck <=0.650 mOhm, derived branch planning screen <=5.850 mOhm, complete hot path <=8.50 mOhm, and no global rules.
- Disposition: the existing MPA decision is current for geometry and is reconciled to HEAD; no stale CAD artifact is promoted. Resolve `authority:mpa-r3-corridor-20260921` and return the protected-bus producer to READY for a real isolated implementation.
