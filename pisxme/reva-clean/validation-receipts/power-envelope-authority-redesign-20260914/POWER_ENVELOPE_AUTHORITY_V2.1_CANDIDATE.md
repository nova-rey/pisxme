# Power envelope authority V2.1 candidate

Status: `CANDIDATE_READY_FOR_POWER_AUTHORITY_SIGNATURE`; no CAD changed.

This corrected candidate defines **six physical 12-V/return loops** using six Molex `0039300020` 5569 two-position headers. The conservative 8 A/circuit manufacturer screen is derated to a 6.4 A hard limit, yielding 38.4 A aggregate against the 34.376 A low-voltage peak screen.

The applicable component specification is Molex `PS-5556-004-001` Rev B1. Exact mating terminal, wire, crimp, length, installation temperature, and source PDF hash remain Package Authority qualification items.

The source minimum is 11.4 V; protected-bus minima are 11.15 V sustained and 11.05 V peak after the 0.25/0.35 V total drop budgets. The drop budget is partitioned across harness (0.10 V), contacts (0.05 V), protection FET (0.05 V), PCB branch (0.05 V), and common bus (0.10 V peak allocation).

40 A continuous / 45 A bounded peak source capability is an internal PiSXMe requirement pending source/procurement authority. The 300 W/330 W product envelope is Class C; connector limits are Class B; six-loop topology, derating, drop, fault, and carrier transient screens are Class D; the missing V100 endpoint waveform is Class F.

This artifact supplies corridor inputs only. It does not qualify fabricated hardware, authorize routing, or duplicate HPQ Issue #2.
