# P24-POWER-CURRENT-LIMITER-AUTHORITY

Status: `CONDITIONALLY_SIGNED_SELECTION`

## Binding selection

Power Authority conditionally signs the existing limiter selection for the
V2.2 six-loop source architecture:

- six `Analog Devices MAX17527AATP+T`, one per independent 12-V loop A--F;
- one `6.25 kOhm`, `0.1%` SETI resistor per limiter;
- nominal regulated branch limit `6.000 A`;
- guaranteed calculated regulated range `5.75425--6.24625 A` per branch,
  using the device `+/-4%` limit accuracy and resistor tolerance;
- `CLMODE` latch-off with the vendor-prescribed `220 kOhm` resistor to GND;
- one open-drain FLAG per loop, aggregated into a fail-safe V100 inhibit/reset
  function before controlled restart;
- PLIM is disabled only as documented in the candidate and must not replace
  the branch current-limit proof.

The calculated maximum is below the V2.2 `6.400 A` branch screen by
`0.15375 A`; the six-branch calculated minimum is `34.52547 A`, above the
V2.2 low-voltage peak screen `34.37622 A` by `0.14925 A`. The narrow margin
must be retained at full precision and is not bench evidence, load-sharing
evidence, or authorization to redistribute one branch's load to another.

## Fast-trip interpretation

The `6.400 A` invariant is signed here as the **post-blanking regulated branch
limit**. It does **not** include the MAX17527A's sub-3-us fault transient. The
device evidence gives a `20--32 A` internal fast-trip threshold and `3 us`
typical response, with the external reverse-protection nFET remaining on
during that event. That transient is a separate system energy/SOA requirement;
it must be covered by the exact nFET, fuse, TVS/clamp, harness-inductance and
PCB-copper coordination calculation. No claim is made that instantaneous
fault current is <= `6.400 A`.

## Dependency disposition

This receipt resolves the queue dependency
`authority:power-current-limiter-signature`: the MPN, SETI, regulated-limit
interpretation, latch-off mode and FLAG intent are now binding authority
inputs for the remaining qualification work. It does **not** resolve the
whole source-contract dependency or authorize CAD insertion.

The following remain required before the six-loop source/net/component
contract can return to `READY`:

1. Select and qualify an exact external reverse-protection nFET at the
   MAX17527A guaranteed `4.45--4.95 V` gate-drive range, including reverse
   polarity/current SOA. Existing `CSD19536KCS` evidence is not guaranteed at
   that gate voltage.
2. Select the exact fuse and TVS/clamp and retain worst-case I2t/SOA
   coordination across the `20--32 A` fast-trip event, blanking/latch behavior,
   harness inductance and PCB copper.
3. Close the six FLAG aggregation, V100 inhibit/reset, EN timing and
   controlled-restart truth table; any branch fault must fail safe.
4. Qualify six actual harness loops and the MPA/thermal installation,
   including the signed `<=20 mOhm` hot complete-loop requirement where that
   is the declared scope.
5. Librarian retains the official ADI source provenance in the private
   Library. The current indexed transient retrieval hash is
   `dc96bb134570f41409d3b1ff6f8d6ea128c035eecc2944a4eaa95950469b59cd`; no
   local vendor PDF copy is claimed.

## Evidence reviewed

- `validation-receipts/power-current-limiter-authority-20260914/POWER_CURRENT_LIMITER_AUTHORITY.{md,json}` (`454de823`)
- `validation-receipts/power-envelope-authority-redesign-20260914/POWER_ENVELOPE_AUTHORITY_V2.2_CANDIDATE.{md,json}` (`daaf6d3b`)
- `validation-receipts/protection-dossier-20260914/PROTECTION_DOSSIER.json`
  (private Library `989e7b8c4e101f9d5a4be7841de2078aba8c9624`)
- `validation-receipts/power-authority-signoff-20260914/POWER_AUTHORITY_SIGNOFF.{md,json}`

CAD changed: **no**. Product envelope reduced: **no**. This is a conditional
limiter-selection authority receipt, not integrated design validation.
