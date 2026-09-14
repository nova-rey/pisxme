# Product/Power corrected source and drop budget — provisional authority candidate

Status: `PROVISIONAL_CANDIDATE_PENDING_POWER_AUTHORITY_SIGNATURE`
Base SHA: `3af770b9`
Source: HPQ Issue #3 Sol resolution, `HPQ3_SOL_RESOLUTION.json`.

## Binding product constraints

- 300 W V100 sustained and 330 W bounded peak remain unchanged.
- Six independent 12-V/return loops remain required; passive current sharing is prohibited.
- Protected-bus minima remain 11.05 V sustained and 11.00 V peak.

## Corrected source and branch contract

The source contract shall guarantee 12.00 V minimum at the six-loop input, 12.60 V maximum, and 40 A continuous / 45 A bounded 100-ms peak capability. At the 12.00-V minimum, the six-loop system must deliver the low-voltage-screen currents without relying on redistribution.

The MAX17527A 6.25-kOhm SETI arrangement is retained only as a capacity screen: 5.754245754 A minimum and 6.24625 A maximum per loop. Six minima provide 34.5254745 A, exceeding the 34.37621832-A 330-W low-voltage screen by 0.14925618 A (0.434%). This is the corrected guaranteed branch allocation; the former 5.8-A per-loop assertion is removed because it was not guaranteed by the selected limiter.

## Complete path resistance/drop budget

The former 0.350/0.400-V allocations were incomplete. The corrected contract reserves complete source-to-protected-bus path loss, including controller/limiter, fuse/holder, nFET, connector/crimp, harness, PCB branch, and common bus:

| Term | Sustained max | Peak max | Basis |
|---|---:|---:|---|
| MAX17527A/controller and limiter | 0.356 V | 0.388 V | 57 mOhm max screen at 6.24625 A; bounded hot allowance |
| Fuse/holder | 0.116 V | 0.128 V | provisional cold screen; must be replaced by exact qualified assembly value |
| nFET | 0.100 V | 0.100 V | reserved until exact MPN and hot RDS(on) qualification |
| Connector/crimp | 0.116 V | 0.128 V | complete pair allocation |
| Harness | 0.116 V | 0.128 V | complete hot-loop allocation |
| PCB branch | 0.100 V | 0.100 V | derived copper allocation |
| Common bus/returns | 0.047 V | 0.056 V | six-loop aggregate allocation |
| **Complete-path reserve** | **0.951 V** | **1.028 V** | sum of all terms |

At 12.00 V source minimum, these reserves yield 11.049 V sustained and 10.972 V peak, which do not meet the protected-bus minima. Therefore the source minimum must be raised to at least 12.001 V sustained and 12.028 V peak for these provisional reserves. The authority shall bind practical rounded requirements of 12.05 V minimum sustained and 12.10 V minimum during the bounded peak, or reduce qualified path resistance with evidence. The 12.60-V maximum remains.

Equivalent complete-path resistance limits are 0.951/5.754245754 = 165.27 mOhm sustained and 1.028/6.24625 = 164.58 mOhm peak. These are complete-path limits, not permissions to omit any component term.

## Required authority closure

Power Authority must replace provisional terms with guaranteed hot values, sign the source range and branch allocation, and close nFET gate/VDS/SOA, fuse/TVS, harness, thermal, and FLAG/reset evidence. No CAD or footprint change is authorized until signature.
