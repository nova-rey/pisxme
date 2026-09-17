# P24 corrected power-budget current-head validation receipt

Package: `P24-POWER-BUDGET-CORRECTION`
Assigned base: `66ea28f4509e6027a479e0b4dd5d823fca22dc99`
Validated current HEAD: `a08371b50c8d827ccad2c4089f523e47f352bacc`
Campaign: `phase24-phase25-acreage`

## Scope

This is a current-head reconciliation of the already signed Product/Power
Authority contract and its accepted replacement calculator. It is a validation
receipt only. It does not recover the historical HPQ4 calculator, change CAD,
change the product envelope, release physical power qualification, or release
any CAD producer.

The assigned base is an ancestor of current HEAD. The only paths changed from
the assigned base to current HEAD are the Main Work Queue and `bible.md`;
there are no schematic, PCB, project, rule, footprint, model, or
`PROJECT_INVARIANTS*` changes.

## Authority and artifact identity

- Signed decision: `PISXME-P24-POWER-BUDGET-HPQ4`, version `2.0.0`.
- Signed input:
  `POWER_BUDGET_CORRECTION.json`, SHA-256
  `321e4d14c3696d1d24c9ccb54c17526e339786b527e73b54b1ebd0100c501eae`.
- Replacement status:
  `ACCEPTED_AS_NEW_REPLACEMENT_ARTIFACT`.
- Replacement calculator:
  `POWER_BUDGET_CALC_REPLACEMENT.py`, SHA-256
  `3fe4e0b416b0eba10044baf1b1dd4e2b55457cc5a0d64e30ff84bf556ba4d5d2`.
- Replacement output:
  `POWER_BUDGET_CALC_REPLACEMENT_OUTPUT.json`, SHA-256
  `1b1ce2d71431a3924826e26452068749a1529715c939d12e93c7bcdfd2ee03b7`.
- Replacement manifest:
  `POWER_BUDGET_CALC_REPLACEMENT_MANIFEST.json`, SHA-256
  `67739ee0c5f9bd3f0142151e098557996c9084894457a612f4265f8147381f9a`.
- Authority disposition:
  `POWER_BUDGET_CALC_REPLACEMENT_AUTHORITY_DISPOSITION.md`, SHA-256
  `b1540095bf8fda4c0555133897669d81502f812756f7d13fd3290dd1461b0bfe`.

All listed present artifacts match the manifest and `SHA256SUMS`. The
historical `POWER_BUDGET_CALC.py` remains absent, with expected SHA-256
`82a3f904dfecf5773b26202c77d10fe9e177d6d7bb42aaf8c67a8cd17e0f3e8b`; this is
the documented missing historical source, not a failed replacement check.

## Reproduction performed at current HEAD

From the project root:

```text
python3 validation-receipts/power-budget-correction-20260914/POWER_BUDGET_CALC_REPLACEMENT.py --json > /tmp/power-budget-current-head-normal.json
python3 -O validation-receipts/power-budget-correction-20260914/POWER_BUDGET_CALC_REPLACEMENT.py --json > /tmp/power-budget-current-head-optimized.json
cmp -s /tmp/power-budget-current-head-normal.json /tmp/power-budget-current-head-optimized.json
```

Results:

- normal execution: return code `0`;
- optimized execution: return code `0`;
- output comparison: byte-identical;
- assertion count: `26`;
- assertion status: `PASS`;
- signed input hash pin: `PASS`;
- complete-path resistance derivation: `PASS`;
- historical-source recovery claim: `false` as required.

The retained repository output is byte-identical to the normal current-head
reproduction. The signed numerical contract remains unchanged: 300 W sustained,
330 W bounded peak, six independent 6.000–6.400 A loops, 12.05/12.10–12.60 V
source windows, and downstream physical qualification gates.

## Result

`DONE — CURRENT_HEAD_VALIDATED`

This package is complete at the authority/calculation-contract scope. Root may
resolve `P24-POWER-BUDGET-CORRECTION` and unlock downstream packages. Exact
limiter, fuse/holder, nFET, TVS, harness, PCB resistance, PDN, thermal,
sequencing, MPA, ERC/DRC, connectivity, DFM, and fresh integrated KiCad Light
validation remain separate required gates.
