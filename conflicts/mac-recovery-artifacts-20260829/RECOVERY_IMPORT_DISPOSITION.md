# Mac recovery import disposition

The authoritative recovery staging tree remains:

`/srv/pisxme-recovery/raw-mac-recovery/`

The recovered project-shaped tree was copied additively into this repository on
2026-08-29. Existing repository files were retained because all 39 overlapping
files were byte-identical to their recovered counterparts. Conflict copies under
`conflicts/mac-materialized-20260829/` remain archival and were not promoted over
active paths.

Three non-source artifacts were moved into this quarantine instead of active
design paths, preserving their relative source paths:

- `pisxme/._footprints` — AppleDouble metadata.
- `pisxme/footprints/._PiSXMe.pretty` — AppleDouble metadata.
- `design/.FINAL_BLOCKER_REVIEW_V2.md.16iTtYy6ia` — zero-byte temporary file.

`SHA256SUMS.raw-mac-recovery` is an unchanged copy of
`/srv/pisxme-recovery/SHA256SUMS`. Its recorded paths are relative to
`/srv/pisxme-recovery/`, so verification of the original recovery set should be
run from that directory.

The exact recovered `bible.md` is retained at `recovered-originals/bible.md`.
The active root `bible.md` intentionally differs only because the repository's
append-only project log was extended with the NYX recovery integration record.

Do not silently replace `design/COMPONENT_SOURCING_REALITY_V2.md`: the recovered
canonical path is zero bytes, while a non-empty differing version is preserved at
`conflicts/mac-materialized-20260829/design/COMPONENT_SOURCING_REALITY_V2.md`.
Review provenance before choosing either version.
