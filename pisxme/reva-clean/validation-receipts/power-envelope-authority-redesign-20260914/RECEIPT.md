# Power envelope redesign candidate receipt — 2026-09-14

The bounded architecture candidate is complete at base
`dd4b2c80785ca1fc82c84bd0da48ff612147690a`. It establishes a six-circuit,
independently current-limited 12-V input screen using the existing Molex
0039300020 contact family as the preferred low-risk implementation, with
three two-position headers replacing the incompatible two-header topology.

The candidate covers 300 W sustained and 330 W design peak, 11.4–12.6 V
input, 40 A continuous / 45 A bounded peak source capability, 6.4 A hard
branch limits, 38.4 A total derated branch capacity, drop budgets, branch
imbalance and fail-safe shutdown, transient/load-step bounds, and corridor
inputs. It makes no CAD change and does not duplicate HPQ Issue #2.

This is `CANDIDATE_READY_FOR_POWER_AUTHORITY_SIGNATURE`; it is not a claim of
connector/harness qualification or fabricated-hardware validation. Package
Authority must qualify mating parts, wire, crimp, length, thermal installation,
and exact footprint before implementation.
