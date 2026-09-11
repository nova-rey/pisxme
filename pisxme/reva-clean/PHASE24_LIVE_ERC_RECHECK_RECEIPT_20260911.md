# Phase 24 live schematic ERC recheck — 2026-09-11

## Scope

Fresh native KiCad 10.0.5 full-severity ERC against the canonical clean root:
`PiSXMe_RevA_Clean.kicad_sch`. This is a live-source recheck, not a
disposable hierarchy fixture and not a severity-filtered pass.

Command:

```text
flatpak run --command=kicad-cli org.kicad.KiCad sch erc \
  --output PHASE24_CLEAN_SCHEMATIC_ERC_LIVE_RECHECK_20260911_v2.rpt \
  pisxme/reva-clean/PiSXMe_RevA_Clean.kicad_sch
```

## Result

Native KiCad reported **862 violations**. The report contains no ERC errors,
but its warnings remain open and unwaived; therefore this is not a Phase 24
pass.

| Class | Count |
|---|---:|
| `endpoint_off_grid` | 416 |
| `isolated_pin_label` | 232 |
| `unconnected_wire_endpoint` | 147 |
| `same_local_global_label` | 30 |
| `multiple_net_names` | 24 |
| `no_connect_dangling` | 11 |
| `lib_symbol_mismatch` | 2 |

Raw report SHA-256:
`d49840cb1f70c9f581560b1e0b3b8ee6dabda0175f45a64cbe32fb8c55b0efc3`.

## Disposition

The live schematic truth/ERC/netlist/parity gate remains OPEN. The focused
native hierarchy authoring regression is separately PASS, but does not prove
that the live source is warning-clean. The next implementation cycle must
address live contract/source authoring and then rerun native ERC, matching
netlist export, and parity against the exact integrated candidate.
