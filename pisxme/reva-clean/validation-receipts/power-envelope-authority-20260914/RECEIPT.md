# Power-envelope authority receipt — 2026-09-14

`PISXME-REV-A-POWER-ENVELOPE-001` version `1.1.0` is the controlling
signed/versioned Power Authority decision for the Branch-B reassessment.
Version `1.0.0` is retained only as superseded provenance. The controlling
decision does **not** bind the Rev-A 12-V protected-input design envelope to
250 W / 25.25 A total / dual 13 A branches: the exact Molex
`PS-43879-001-001` application specification rates the standard 5556
two-circuit 16/18-AWG assembly at 8 A per circuit before application derating
and rejects an assumed current-sharing qualification.

The Librarian and Researcher packets were reviewed first, then reconciled
against the exact manufacturer application table. Seven requested fields are
A/B/C; `continuous_current` and `peak_current` remain indispensable D fields
because the current selected contact/harness assembly cannot carry the
requested total by arithmetic, and no authoritative V100/SXM2 transient
contract was found. The artifact sets internal requirements for harness
selection, branch fault handling, shutdown, surge support boundary, thermal
acceptance, and load-step validation without claiming vendor V100 waveform
data or fabricated-hardware results.

Files:

- `POWER_ENVELOPE_AUTHORITY_V1.1.md` — controlling review, equations, field
  matrix, rail rules, legacy-value disposition, and resume conditions.
- `POWER_ENVELOPE_AUTHORITY_V1.1.json` — machine-readable controlling decision
  and calculations.
- `SUPERSESSION_NOTICE.md` — explicit v1.0 supersession and source conflict.
- `POWER_ENVELOPE_AUTHORITY.md` and `.json` — v1.0 superseded artifacts,
  retained for provenance only.
- `SHA256SUMS` — hashes of all receipt artifacts except the manifest itself.

Read-only checks performed:

```text
python3 -m json.tool POWER_ENVELOPE_AUTHORITY_V1.1.json
sha256sum POWER_ENVELOPE_AUTHORITY.md POWER_ENVELOPE_AUTHORITY.json RECEIPT.md \
  SUPERSESSION_NOTICE.md POWER_ENVELOPE_AUTHORITY_V1.1.md \
  POWER_ENVELOPE_AUTHORITY_V1.1.json
git diff --check
```

No schematic, PCB, library, rule, or configuration file was edited. The
current integrated board remains physically open for Branch-B copper,
protected-rail continuity, return connectivity, regulator support, and
thermal/load-step validation.
