# Product/Power Authority disposition — HPQ4 calculator replacement

Package: `P24-POWER-BUDGET-CALCULATOR-REPLACEMENT`  
Campaign: `phase24-phase25-acreage`  
Candidate base SHA: `4cead01ea4f89b4f4a89a1bdef365062ea4df4ad`

## Binding input and provenance

The reviewed input is the retained Product/Power Authority decision
`PISXME-P24-POWER-BUDGET-HPQ4`, version `2.0.0`, at:

`validation-receipts/power-budget-correction-20260914/POWER_BUDGET_CORRECTION.json`

Its SHA-256 is
`321e4d14c3696d1d24c9ccb54c17526e339786b527e73b54b1ebd0100c501eae`.
The historical HPQ source
`validation-receipts/power-budget-correction-20260914/POWER_BUDGET_CALC.py`
with expected SHA-256
`82a3f904dfecf5773b26202c77d10fe9e177d6d7bb42aaf8c67a8cd17e0f3e8b` remains
absent and unrecovered. This disposition accepts a new replacement identity;
it makes no recovery claim.

## Review performed

The reviewed replacement is:

- `POWER_BUDGET_CALC_REPLACEMENT.py`, SHA-256
  `3fe4e0b416b0eba10044baf1b1dd4e2b55457cc5a0d64e30ff84bf556ba4d5d2`;
- `POWER_BUDGET_CALC_REPLACEMENT_OUTPUT.json`, SHA-256
  `1b1ce2d71431a3924826e26452068749a1529715c939d12e93c7bcdfd2ee03b7`;
- `POWER_BUDGET_CALC_REPLACEMENT_RECEIPT.md`;
- `POWER_BUDGET_CALC_REPLACEMENT_MANIFEST.json`;
- this authority disposition.

The implementation was independently executed with both normal and optimized
Python execution. Both runs produced the retained report with 26/26 assertions
passing. The implementation now:

1. pins and checks the signed input SHA-256 at runtime;
2. uses explicit fail-closed checks that remain active under `python3 -O`;
3. calculates load accounting, six independent loop current, source current
   margin, branch/common/static drop, full-derated ceiling, and transient PDN
   values from the signed JSON; and
4. derives the balanced complete-path resistance as
   `R_branch + 6 * R_common = 0.148250 + 6 * 0.001333333333333333333333333333
   = 0.156250 ohm`, then checks it against the signed authority field.

The output reproduces the signed contract values: 32.448466566 A sustained
source current, 35.626262626 A bounded-peak source current, 5.408077761 A and
5.937710438 A per-loop requirements, and a 1.000000000 V full-derated complete
path drop. These are contract calculations, not physical qualification results.

A tamper test changed the signed input in a disposable copy and ran the
replacement with `python3 -O`; it failed closed on the input-hash mismatch.

## Disposition and limits

**ACCEPTED_AS_NEW_REPLACEMENT_ARTIFACT.** The replacement is mathematically
faithful to the retained signed HPQ4 JSON within its documented Decimal
precision and assertion tolerances. It is authorized as the reproducible
calculation artifact for the numerical contract only.

The following remain open and are preserved as downstream gates: exact limiter,
fuse/holder, nFET, TVS/clamp, connector/crimp and harness qualification, PCB
branch and common-bus resistance, PDN/load-step behavior, sequencing and
fault handling, thermal qualification, provenance, MPA, ERC/DRC, connectivity,
DFM, and fresh integrated KiCad Light validation. No CAD release or product
-envelope change is authorized by this disposition.

Authority: `Product/Power Authority`  
Authority level: `BINDING_WITHIN_DELEGATED_SCOPE`  
Signed at: `2026-09-17`  
Disposition identity: `PISXME-P24-POWER-BUDGET-CALCULATOR-REPLACEMENT-AUTHORITY-ACCEPTED`
