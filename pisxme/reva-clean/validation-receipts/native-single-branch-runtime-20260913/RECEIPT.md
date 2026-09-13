# Native single-branch experiment — runtime result — 2026-09-13

Requested experiment: route only `12V_IN_B`, native `F2.1 (83.60,58.75)` to `U2.3 (21.45,96.45)`, with current MPA placement F2 `(90,60)` / D2 `(110,60)` and qualified KiCad 10.0.6 worker.

The disposable worker materialized the exact MPA placement and opened a native PCB editing context, but no native route artifact or per-segment collision evidence was produced during the bounded attempt. No `pcbnew` process remained when the attempt was interrupted and the workspace was released. This is a runtime/capability insufficiency for the native interactive experiment, not evidence of corridor infeasibility. Canonical CAD was unchanged.

Resume condition: a supported native PCB Editor routing capability must be available in a disposable worker; do not substitute coordinate scripting or stale placements.
