# Replacement calculator authority-review packet

Package: `P24-POWER-BUDGET-CALCULATOR-REPLACEMENT`
Decision input: `PISXME-P24-POWER-BUDGET-HPQ4` v2.0.0

## Review request

Product/Power Authority is asked to review and sign the **new replacement
identity and manifest** below. This packet does not claim that the missing
historical `POWER_BUDGET_CALC.py` was recovered, and it does not alter the
signed HPQ4 numerical contract.

## Candidate evidence

- `POWER_BUDGET_CALC_REPLACEMENT.py`: new Python Decimal implementation;
  SHA-256 `6854dd01dc756356b527fa69af7f2827f41b4be28a589f7f62e691dee4ce6149`.
- `POWER_BUDGET_CALC_REPLACEMENT_OUTPUT.json`: 25/25 numeric assertions PASS;
  SHA-256 `b81a8665991de05e296b5d58c652c9be63fb28a9c53424bccf7c39fbfeabbc7a`.
- `POWER_BUDGET_CALC_REPLACEMENT_MANIFEST.json`: source/missing-source
  provenance and artifact manifest;
  SHA-256 `36f04b80846822678a23821aec7f2246c0397e4aac60670840804faa0245caa8`.
- `POWER_BUDGET_CALC_REPLACEMENT_RECEIPT.md`: reproduction receipt;
  SHA-256 `502842f8054ddfe2fd364409196048f9c3b277f9e717d7bc82aa8bb5403b11e4`.
- `POWER_BUDGET_CORRECTION.json`: signed input;
  SHA-256 `321e4d14c3696d1d24c9ccb54c17526e339786b527e73b54b1ebd0100c501eae`.

## Scope checks

The calculator reads only the signed JSON, uses Decimal precision 50, and
reproduces load accounting, source current margin, static branch/common/total
drops, protected-bus lower bounds, full-derated ceiling, and transient-PDN
assertions. The historical missing path and its expected hash are retained as
missing and unrecovered. No CAD, footprint, rule, connectivity, or product
load-envelope field is modified.

## Authority disposition

`PENDING_PRODUCT_POWER_AUTHORITY_SIGNATURE`

A Power Authority must append or replace this disposition with a signed
review before the queue package can be marked complete or downstream work can
be released. The implementing Supervisor does not self-authorize this binding
review.
