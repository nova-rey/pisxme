# Architecture sanity audit baseline

Date: 2026-08-27
Branch at audit start: `codex/architecture-sanity-audit`
Starting commit: `88b8688be5b13d687551be46f25249867dbbe00c`

The active PiSXMe design is intentionally out of scope for mutation during
this audit. These hashes are the before/after guard for that promise.

| Active file | SHA-256 before audit |
|---|---|
| `pisxme/PiSXMe.kicad_pcb` | `de3f3ff6e375029b62e4f4cd4285d9477d88a7dbf1137c34498adb9a6b580f4e` |
| `pisxme/PiSXMe.kicad_sch` | `b9ba4290d6274e85caf82b1111fd5f1badba00299a08014cec9e36bdbce92406` |
| `pisxme/PiSXMe.kicad_dru` | `681a9397b053ed62c006af1e01f83fb4994368c1022a30ac9f2760edb727afd9` |

The audit may add disposable reference copies, reports, and experiment boards;
it must not rewrite any of the three active files above.

