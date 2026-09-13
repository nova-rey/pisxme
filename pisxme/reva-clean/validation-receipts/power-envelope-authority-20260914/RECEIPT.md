# Power-envelope authority receipt — 2026-09-14

`PISXME-REV-A-POWER-ENVELOPE-001` version `1.0.0` is the signed/versioned
Power Authority decision for the Branch-B reassessment. It binds the Rev-A
12-V protected-input design envelope to **250 W V100 allowance / 25.25 A total
/ 13 A maximum per branch**, with equal-share target 12.625 A per branch.

The Librarian and Researcher packets were reviewed first. All nine requested
fields classify as A, B, or C; no indispensable D field remains. The prior
Issue #2 `external-blocker` premise is therefore unsupported. The artifact
sets internal requirements for harness selection, branch sharing, shutdown,
surge support boundary, thermal acceptance, and load-step validation without
claiming vendor V100 waveform data or fabricated-hardware results.

Files:

- `POWER_ENVELOPE_AUTHORITY.md` — review, equations, field matrix, rail rules,
  legacy-value disposition, and resume conditions.
- `POWER_ENVELOPE_AUTHORITY.json` — machine-readable decision and calculations.
- `SHA256SUMS` — hashes of the two decision files and this receipt.

Read-only checks performed:

```text
python3 -m json.tool POWER_ENVELOPE_AUTHORITY.json
sha256sum POWER_ENVELOPE_AUTHORITY.md POWER_ENVELOPE_AUTHORITY.json RECEIPT.md
git diff --check
```

No schematic, PCB, library, rule, or configuration file was edited. The
current integrated board remains physically open for Branch-B copper,
protected-rail continuity, return connectivity, regulator support, and
thermal/load-step validation.
