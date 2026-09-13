# Power envelope authority V2.2 candidate

Status: `CANDIDATE_READY_FOR_POWER_AUTHORITY_SIGNATURE`; no CAD changed.

This revision preserves six physical 12-V/return loops, the 6.4 A hard branch limit, and the 38.4 A aggregate derated capacity. It applies Molex PS-5556-004-001 Rev B1 (2026-03-24), the 5569 header family specification, with a phosphor-bronze 5556 terminal class and tin-plated selected interface. The PDF byte hash is pending Librarian acquisition and is explicitly not claimed.

Drop budgets are now separate and internally consistent: sustained 0.350 V at 5.8 A/branch (0.116 harness + 0.116 connector loop + 0.030 FET + 0.030 PCB branch + 0.058 common bus), and peak 0.400 V at 6.4 A/branch (0.128 + 0.128 + 0.040 + 0.040 + 0.064 V). With a 11.4 V source minimum, protected-bus minima are 11.05 V sustained and 11.00 V peak. These are internal Class-D screens pending Package/Power qualification.

The product envelope remains Class C, connector limits Class B, topology/derating/drop/fault/carrier screens Class D, and the missing V100 endpoint waveform Class F. 40 A continuous / 45 A bounded peak source capability remains an internal PiSXMe requirement pending procurement authority.


## Conditional authority signature

Power Authority conditionally signed the corrected numerical architecture. Librarian indexed Molex PS-5556-004-001 Rev B1 (ECM 851282, 2026-03-24) and selected 5556 phosphor-bronze tin-plated terminals `39000079`/`39000080` in private Library commit `c27ee33f`. The exact PDF byte hash is unavailable because the direct fetch returned a non-equivalent response; no substitute hash is claimed. Package Authority qualification of the exact mating assembly remains a separate required package before CAD implementation.
