# Exact-head native ERC reproduction

- Candidate/source commit: `70248ce8`
- Worker/image: fresh detached `pisxme-kicad-light:v1`; KiCad 10.0.6
- Schematic: `PiSXMe_RevA_Clean.kicad_sch`
- Command: `kicad-cli sch erc --format json --severity-all -o erc.json PiSXMe_RevA_Clean.kicad_sch`
- Result: 351 warnings, 0 errors reported by the native checker.
- Scope: exact-head source/toolchain reproduction. The 351 findings remain open; no blanket waiver or severity downgrade is implied.
- Raw output and checksum are retained here.
