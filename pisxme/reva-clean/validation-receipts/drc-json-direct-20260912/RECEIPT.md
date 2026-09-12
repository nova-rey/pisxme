# Exact-head native DRC JSON validation — 2026-09-12

Validated source commit: `ebcf9fdb`.
Toolchain: KiCad Light 10.0.6.
Command: `kicad-cli pcb drc --format json --severity-all --exit-code-violations`

Result: **340 violations / 499 unconnected items**, with return code 5 due to
violations. Violation classes are retained in the JSON report. The checker
reports five ignored checks: missing courtyard, track endpoint not centered on
via, tuning-profile geometries, footprint-filter mismatch, and footprint-type
mismatch. These exclusions remain subject to explicit acceptance disposition.
