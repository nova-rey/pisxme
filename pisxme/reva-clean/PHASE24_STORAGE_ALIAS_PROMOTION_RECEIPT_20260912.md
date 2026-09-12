# Phase 24 STORAGE alias promotion receipt

## Current result

Two exact STORAGE label aliases were promoted to the authoritative child
schematic:

- `TME` -> `POWER_GND` at `(70,130.075)`
- `M2_CONFIG1` -> `AUTO_PEDET` at `(240,125.63)`

The disposable probe changed only those two exact records. Local native KiCad
10.0.5 ERC reports 311 violations with zero errors. Exported schematic
netlist comparison is exact: 361 nets, zero missing names, zero extra names,
and zero changed node sets.

Fresh `kicad-light` validation from committed ref `820c71b1` reproduced the
probe successfully under KiCad 10.0.6 and reported 367 violations. The count
is retained as a tool-version delta, not merged with the local 10.0.5 census.

## Explicit non-promotion

`M2_3V3` -> `STORAGE_3V3` at `(240,210.72)` remains rejected. Its disposable
probe reduced the warning count but changed net ownership, splitting eight
M.2 power pads into `/STORAGE/M2_3V3`; it is not an identity-preserving alias.

## Validation scope

This closes only the two alias-authoring defects. It does not close Phase 24,
does not waive remaining ERC warnings, and does not alter PCB authority.
