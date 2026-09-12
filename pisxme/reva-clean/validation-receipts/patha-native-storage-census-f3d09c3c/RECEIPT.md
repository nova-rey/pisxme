# Phase 24 Path-A native storage census endpoint correction

Date: 2026-09-13
Source commit: `f3d09c3cb84e9d7bfe76ffc4acf2de84afa7aa77`
Selected integrated PCB: `pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
Canonical schematic: `pisxme/reva-clean/PiSXMe_RevA_Clean.kicad_sch`
Validator: `phase24_patha_native_storage_census.py`
Worker: `patha-census-endpoint-f3d09c3c` from the committed source ref
Tool image: qualified `pisxme-kicad-light:v1`
KiCad CLI: `10.0.6` (`kicad-cli.version`)

## Scope

This is a validation-tool correction only. The required Path-A endpoint tuple
for `STORAGE_SEL` now checks `U14.4` to `U13.9`. The previous `U13.12` check
was incorrect for the current schematic/PCB contract. No CAD, footprint, net
assignment, routing, rule, or acceptance status changed.

The prior receipt at
`validation-receipts/patha-native-storage-census-19a1390a/` remains retained
as historical evidence and is not overwritten.

## Reproduction

```text
cd /workspace/project/pisxme/reva-clean
python3 phase24_patha_native_storage_census.py \
  PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb \
  /workspace/output/patha-native-storage-census.json
```

The command completed with exit code `0`. KiCad emitted three native
`PROPERTY_ENUM` assertion lines to stderr while loading the board; they are
retained verbatim in `patha-native-storage-census.stderr` and did not prevent
JSON generation.

## Result

- Storage-island pads covered: `292`
- Required endpoint checks: `26`
- Open required endpoints: `15`
- `STORAGE_SEL` `U14.4 -> U12.9`: `OPEN`
- `STORAGE_SEL` `U14.4 -> U13.9`: `OPEN`
- `AUTO_PEDET` `J3.69 -> U14.2`: included in the 26 checks

The corrected endpoint is still open in the integrated candidate. This is an
open-route inventory and does not close the Path-A storage, DRC, or Phase 24
acceptance rows.

Raw JSON, stdout, stderr, tool version, return-code marker, and hashes are
retained in this directory. The raw JSON is identical between two runs from
the same committed worker checkout; the second run was used for the retained
artifacts.
