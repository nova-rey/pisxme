# Product/Power corrected source and complete-path budget — signed v2.0.0

Status: `SIGNED_NUMERICAL_CONTRACT_DOWNSTREAM_QUALIFICATION_GATED`
Decision: `PISXME-P24-POWER-BUDGET-HPQ4`
Base: `cb2cebf525dbb6fbe29f3bed8d7762ead0b2b831`
Authority: Product/Power Authority, 2026-09-14
CAD changed: no

## Binding disposition

The 300 W sustained / 330 W 100-ms peak product envelope, six independent
loops, no passive-sharing credit, and protected-bus minima of 11.05 V
sustained / 11.00 V peak are preserved. The 90% efficiency floor is now
explicitly located between the protected bus (`P0`) and the V100 plus 22.7 W
functional-load plane (`L0`); source-to-bus conduction loss is separate.

The source plane (`S0`) shall remain 12.05–12.60 V sustained and
12.10–12.60 V for the bounded peak, with at least 40 A continuous and 45 A
peak capability. The former 11.40 V and ambiguous 12.00 V minima are
superseded.

At the protected-bus minima, the required currents are 32.448466566 A
sustained and 35.626262626 A peak, or 5.408077761 A and 5.937710438 A per
independent loop. Every loop A–F shall independently guarantee at least
6.000 A and shall not exceed 6.400 A under full operational tolerance and
temperature. Another loop's unused capacity is not admissible proof.

`MAX17527AATP+T` with 6.25 kΩ, 0.1% SETI is rejected as the production
current-contract basis: its 5.754245754 A guaranteed floor misses the 6.000 A
requirement by 0.245754246 A. A 6.20 kΩ workaround is not authorized outside
the documented 6 A programming range. A different limiter must meet the full
6.000–6.400 A window and its hot resistance allocation.

## Complete hot resistance contract

These are allocation maxima and downstream qualification gates, not claims
that an existing component or installation already passes.

| Series term, including stated return scope | Hot cap |
|---|---:|
| Limiter | 57.000 mΩ |
| Fuse and holder | 20.000 mΩ |
| External nFET | 15.625 mΩ |
| Connector and crimp complete loop | 20.000 mΩ |
| Harness wire-only complete loop | 20.000 mΩ |
| PCB branch positive and dedicated return | 15.625 mΩ |
| **Per-branch subtotal** | **148.250 mΩ** |
| Shared common positive and return at aggregate current | **1.333333333 mΩ** |

For balanced accounting, the complete-path equivalent is 156.250 mΩ and
`Vdrop = Ibranch*0.148250 + Itotal*0.001333333333333`.
The JSON's `_ohm_exact` strings control calculation; mΩ numbers are rounded
displays, and the common-bus cap is exactly 1/750 Ω.

| Point | Sustained | Peak |
|---|---:|---:|
| Total current | 32.448466566 A | 35.626262626 A |
| Per-loop current | 5.408077761 A | 5.937710438 A |
| Branch drop | 0.801747528 V | 0.880265572 V |
| Common-bus drop | 0.043264622 V | 0.047501684 V |
| Complete static drop | 0.845012150 V | 0.927767256 V |
| P0 lower bound | 11.204987850 V | 11.172232744 V |
| Margin over protected-bus minimum | 0.154987850 V | 0.172232744 V |

At the 6.4 A per-loop derated ceiling (38.4 A aggregate), the complete static
drop is exactly 1.0000 V. The peak static margin leaves at most 0.172232744 V
for additional dynamic droop while S0 remains at or above 12.10 V. The
corresponding 3.177796060 A load step gives a 0.054198803 Ω dynamic-impedance
ceiling and 1 ms recovery screen; measured/extracted L, ESR, ESL, control
response, and ground bounce remain mandatory.

## Downstream gates

No CAD producer is released by this decision. Normal Phase 24 flow must still:

1. select a full-temperature limiter meeting 6.000–6.400 A and 57 mΩ hot;
2. qualify exact fuse/holder, nFET, and TVS with I²t, clamp, VDS, reverse and
   SOA evidence;
3. qualify all six connector/crimp and harness schedules at their separate
   20 mΩ hot caps, with 16-AWG, bundling, ambient and thermal evidence;
4. prove each PCB branch/return and the shared common positive/return caps;
5. close return continuity, PDN/load-step, FLAG aggregation, brownout,
   V100 inhibit/reset, and controlled restart;
6. close MPA, thermal, provenance, and exact-component gates; and
7. perform serialized CAD integration followed by independent current-HEAD
   ERC, DRC, opens/shorts, return-path, DFM, and qualified KiCad Light checks.

The machine-readable JSON is controlling. `POWER_BUDGET_CALC.py` independently
recomputes the signed arithmetic. Source hashes in the JSON preserve the
HPQ3, provisional, prior-authority, Library, and manufacturer-derived inputs.
