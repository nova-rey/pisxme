# Hostile human-factors review

Review date: 2026-08-28  
Scope: active RC2 PCB, current manufacturer-backed USB-A render, enclosure and
service assumptions.  
Independent reviewer: Euclid read-only review, supplemented by root-agent
model inspection and footprint geometry checks.

## Findings and disposition

| Finding | Evidence | Disposition |
|---|---|---|
| FAST-A/B could be backwards | Würth STEP shows both active 0° apertures facing +X/right; right-edge crop confirms it | Closed; retain current orientation |
| Rotating J9/J10 would improve access | 90°/270° negative-control trial creates mixed SMT/PTH pad-field overlap and DRC shorts | Rejected; not a manufacturable option |
| Two USB-A plugs may collide | Centers are 38 mm apart; nominal connector width is 16.66 mm; provisional independent 22 x 12 mm panel openings do not overlap | Pass with enclosure/plug-envelope assumption |
| F1/Q1 are inside cooler-owned XY reservation | F1 at `(80,116)` and Q1 at `(110,116)`; cooler rectangle ends at `y=117.5`; F1 body is 22 x 8 mm and Q1 body is 10 x 6 mm | Open pre-review blocker; move the power/protection row or amend the cooler contract with evidence |
| Cooling headers are physically colliding | J5/J6/J7 outlines are 10 x 4 mm at 8 mm center pitch | Open pre-review blocker; spread to at least 12--14 mm or use a wider horizontal arrangement |
| Functional labels are missing | Current functional annotations are primarily `Dwgs.User`; visible port, power, cooling, recovery, and test-point labels are not yet complete on F.SilkS | Open pre-review blocker; add concise F.SilkS labels |
| SERVICE access is unproven | J11 is recovery-critical, but the mating model/axis is not present in the render set | Open serviceability reservation; verify part drawing/model before release |
| Power cable latch/bend access is unproven | J3/J4 are edge-adjacent, but Mini-Fit Jr housing model is absent | Enclosure integration reservation; require a housing and cable exit envelope |
| UART/recovery access is weak | J8 is at `(214,81)` near FAST-A; TP3 is interior at `(145,125)` | Keep as debug-only, add label/access guidance; consider a future internal service cutout |

## Review conclusion

The initial USB-A orientation suspicion was false for the selected receptacle.
The board is nevertheless not human-factors-ready because the cooler/protection
conflict and cooling-header collision are concrete physical problems, not
generic prototype uncertainty. Missing visible labels and unverified
recovery/power mating envelopes prevent a release-quality usability claim.
