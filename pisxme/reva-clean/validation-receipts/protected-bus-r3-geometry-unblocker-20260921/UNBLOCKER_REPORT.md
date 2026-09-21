# Protected-bus R3 geometry method change

- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Outcome: `SELF_UNBLOCK`
- Clone evidence: baseline 937 DRC/435 opens; all-branch clone 1040 DRC/391 opens.
- Root cause: translated geometries overlap/cross on the same In2/In4 lanes and retain forbidden F.Cu return geometry. The 44-open reduction is illegal connectivity, not a valid route.
- Authorized next method: constraint-aware native route synthesis from current HEAD. Apply the MPA F.Cu corridor clip; reserve immutable copper; allocate unique noncrossing In2 fused lanes ending in the x=103.5..112 join field; allocate distinct In4 returns; use short F.Cu pad escapes and legal via arrays; derive geometry from the actual net graph rather than translating one branch.
- Invariants preserved: J1/J5/J6/J9 anchors, nine independent branches, corrected `B_i <= 5.850 mOhm` planning screen, complete `<=8.50 mOhm` path, six-layer contract, native fabrication rules.
- Required validation: exact-SHA fresh Light; zero branch shorts/crossings; nine-branch pad/net census; F.Cu clip proof; per-branch resistance/thermal extraction; complete source-to-J1 budget.
