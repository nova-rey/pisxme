# HPQ4 power-budget calculator replacement receipt

Package: `P24-POWER-BUDGET-CALCULATOR-REPLACEMENT`

This receipt records a **new replacement artifact**, not recovery of the
historical HPQ4 `POWER_BUDGET_CALC.py`. The historical path is still absent;
its expected hash remains recorded in the original `SHA256SUMS` and in the
replacement manifest. No attempt was made to claim that the missing HPQ runner
source was recovered.

## Input and scope

The replacement reads only the imported signed
`POWER_BUDGET_CORRECTION.json` (Product/Power Authority decision
`PISXME-P24-POWER-BUDGET-HPQ4`, version `2.0.0`). It uses Python `Decimal`
with precision 50 and preserves the signed 300 W sustained / 330 W peak,
six-independent-loop, protected-bus, and complete-path resistance contracts.
It does not change CAD, footprints, rules, connectivity, or product-envelope
values.

## Reproduction

```text
python3 validation-receipts/power-budget-correction-20260914/POWER_BUDGET_CALC_REPLACEMENT.py --json \
  > validation-receipts/power-budget-correction-20260914/POWER_BUDGET_CALC_REPLACEMENT_OUTPUT.json
```

The command completed with **26/26 assertions PASS**. The replacement also pins the SHA-256 of the signed input at runtime, fails closed under `python3 -O`, and derives the balanced complete-path resistance as `R_branch + 6*R_common` before comparing it with the signed field. The report reproduces the
signed load-accounting, source-current-margin, static IR/drop, full-derated
ceiling, and transient-PDN numeric assertions. It includes the source JSON
hash, base SHA, explicit missing/recovered flags, exact method, and preserved
downstream gates.

## Authority status

The replacement identity and manifest were reviewed and accepted by Product/Power Authority as a **new replacement artifact**. This does not recover or replace the historical `POWER_BUDGET_CALC.py`, and it does not release nFET, protection, harness, or CAD work.

See `POWER_BUDGET_CALC_REPLACEMENT_MANIFEST.json` for the candidate base SHA,
artifact hashes, historical missing-source disposition, reproduction command,
and signed review status. The signed disposition is
`POWER_BUDGET_CALC_REPLACEMENT_AUTHORITY_DISPOSITION.md`.
