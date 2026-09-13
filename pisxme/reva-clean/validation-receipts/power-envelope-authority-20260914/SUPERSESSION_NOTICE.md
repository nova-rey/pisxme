# Authority supersession notice

`POWER_ENVELOPE_AUTHORITY.md`, version `1.0.0`, was issued before the exact
Molex Mini-Fit application specification was brought into the review. It is
**superseded and non-controlling**.

The exact manufacturer application table in Molex `PS-43879-001-001`, section
4.3, rates the standard 5556 terminal wire-to-board system at 8 A per circuit
for a two-circuit 16/18-AWG assembly at the stated 30 C temperature-rise test.
It also says the Mini-Fit CPI system was not designed or tested for current
sharing. The generic `0039300020` product-page value of 13 A maximum per
contact does not qualify an unspecified mating terminal, wire, crimp, or
complete assembly.

The controlling decision is now:

- `POWER_ENVELOPE_AUTHORITY_V1.1.md`
- `POWER_ENVELOPE_AUTHORITY_V1.1.json`

Version 1.1 retains the A/B/C evidence and identifies only `continuous_current`
and `peak_current` as indispensable D fields. It does not bind a 250 W /
25.25 A product requirement to the unqualified selected two-contact harness.
