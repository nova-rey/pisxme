# Phase 17 Ethernet placement-repair trial receipt

Status: `PISXME_REVA_CLEAN_BLOCKED`

Scope: authorized Ethernet-only reopening of Phase 11/12. Frozen PCIe,
CM5/power placement, board stack, layer contract, and unrelated subsystems
were not changed.

Candidates trialed:

- `LEFT_A`, `LEFT_B`, `LEFT_C`
- `CM5_ADJACENT_D`, `D2`, `E`, `F`, `G`, `H`
- complete `ORDERED_WEST` island

The complete candidate used U9 `(25,100)` and U6 `(29,106)` at 180 degrees,
with J2 `(12,119)` at 180 degrees. This preserves the source/pair ordering at
the two ESD packages and moves the MagJack to the west service edge.

Native result: rejected. `ORDERED_WEST` produced 390 total DRC violations
and 237 unconnected items, including true Ethernet crossings/shorts in the
CM5-to-ESD breakout, WSON power/ground pad-field interference, and J2 NPTH/
pad-field collisions. Existing acreage DRC debt is included in the total;
the candidate-specific failures are not baseline-only.

Decision: no placement or copper from these trials is production material.
Phase 17 cannot close under the current TPD4E004/J2 two-signal-layer topology.
The next bounded choice is an Ethernet-local escape technology/fabrication
rule or an alternate protection/package land pattern. Phase 18+ remains
prohibited.
