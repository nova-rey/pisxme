# Product/Power Authority — Protected-Bus Resistance Budget Correction

- Decision ID: `PISXME-P24-PROTECTED-BUS-POWER-AUTHORITY-20260921-R3`
- Status: `SIGNED_CONDITIONAL_PRODUCT_POWER_AUTHORITY`
- Qualification: `REQUIRES_PROTOTYPE_VALIDATION`
- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`

The prior interpretation that 0.650 mOhm applied to each raw branch neck is superseded. The 0.650 mOhm term is the effective nine-branch PCB-neck network allocation within the unchanged 8.500 mOhm source-to-J1 hot-path cap:

`R_neck_eff = 1 / sum(1 / B_i) <= 0.650 mOhm`, for all nine positive-plus-return branch resistances `B_i`.

A symmetric planning screen is `B_i <= 5.850 mOhm` per branch, with a nominal 2.925 mOhm positive/return split. Every branch must be extracted; no branch omission, passive-sharing credit, or N-1 credit is allowed. Current balance remains a separate <=10% screen.

The retained complete hot budget remains: source harness/mating/crimps 1.80 mOhm; fuse/holder/contact 0.55 mOhm; effective nine-branch PCB neck 0.65 mOhm; branch joins/transitions/vias 0.45 mOhm; Q1 hot channel 4.32 mOhm; Q1 leads/pads 0.15 mOhm; protected copper/vias to J1 0.25 mOhm; J1 field/spreading 0.25 mOhm; residual 0.08 mOhm; total 8.50 mOhm.

Product invariants remain: 11.4–12.6 V source, 300 W sustained, 330 W/100 ms peak, 40 A continuous, 45 A bounded peak, J1/J5/J6/J9 anchors, nine independent branches, six-layer stack, protected corridors, no passive-sharing/N-1 credit, and complete source-to-J1 hot path <=8.50 mOhm.

At equal loading, branches carry 4.444 A at 40 A and 5.000 A at 45 A; with a 10% imbalance screen, maxima are 4.889 A and 5.500 A. These are calculations only. The 42.9 mm J5.2-to-F2 geometry rejects only the erroneous per-branch 0.650 mOhm interpretation; exact branch extraction, DFM, thermal, source/contact, PDN, sequencing, and prototype validation remain open.
