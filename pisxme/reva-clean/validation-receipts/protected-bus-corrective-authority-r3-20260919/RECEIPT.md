# Protected-bus corrective authority R3 receipt

- **Package:** `P24-PROTECTED-BUS-AUTHORITY-R3`
- **Decision:** `PISXME-P24-PROTECTED-BUS-CORRECTIVE-20260919-R3`
- **Result:** `DONE_FOR_AUTHORITY_SCOPE; REQUIRES_PROTOTYPE_VALIDATION`
- **Canonical CAD changed:** no
- **Hardware operated:** no

R3 resolves HPQ #7 at the Product/Power Authority level by reallocating the
complete positive-plus-return source-to-J1 path to an 8.50 mOhm hot
implementation cap. It retains Q1 `CSD19536KCS` and explicitly prices its
2.7 mOhm 25 degC maximum at a 1.6 normalized hot factor as 4.32 mOhm at a
125 degC case design bound. The budget totals exactly 8.50 mOhm and leaves
the fixed 10.0 mOhm contract satisfied with a stricter implementation limit.

The receipt binds 11.4--12.6 V source voltage, 40 A continuous / 45 A for
100 ms source behavior, protected-voltage minima, nine independent Molex
positive/return branches, 7 A contact screens, branch current/balance
enforcement, fuse fault-isolation limits, Q1/TVS/LM74700 thermal and SOA
gates, all resistance terms, sequencing, reset/inhibit/brownout policy,
regulator rail screens, measurement points, and explicit producer scope.

The authority does not claim a CAD, PDN, load-step, package-inductance,
connector/harness, via-current, thermal, or fabricated-hardware pass. Those
items remain `REQUIRES_PROTOTYPE_VALIDATION`; adding capacitors is not used as
an analysis.

Machine-readable companion: `PROTECTED_BUS_AUTHORITY_R3.json`.
