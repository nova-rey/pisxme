# Tier-2 R3 producer blocker

The exact R3 source-local geometry was produced from committed base `00380ada`; final candidate `2bb75c960a140260ace896ec119061e58a775d3b`, but native Light validation fails. Producer DRC reports `1256` violations and `431` unconnected items (`rc=5`), including `161` shorting items, `26` crossing tracks, `6` courtyard overlaps, `5` PTH-inside-courtyard findings, and `8` track / `7` via dangling findings. Baseline was `257/393`; the candidate is not electrically or mechanically ready.

The trace-only hot-neck estimate at authored 35 um copper is above the authority `0.65 mOhm` allocation for every branch before pad, fuse, via, field, and protection terms. Thermal evidence is `UNPROVEN_REQUIRES_PROTOTYPE_VALIDATION`. No alternate placement, topology, rule relaxation, J1 remap, six-loop, or canonical edit was attempted.

This is a candidate plus evidence packet for Root / Product-Power Authority review, not a DONE claim.
