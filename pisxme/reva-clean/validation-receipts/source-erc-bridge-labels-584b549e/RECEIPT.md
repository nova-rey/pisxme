# Phase 24 STORAGE bridge USB label-scope candidate

- Producer base: `584b549e` (`584b549e` resolves to the exact committed base;
  full SHA is recorded in the workspace metadata and candidate commit).
- Candidate scope: exactly two existing `STORAGE.kicad_sch` local labels,
  `BRIDGE_USB_DP` at `(120,152.935)` and `BRIDGE_USB_DM` at `(120,151.665)`,
  promoted to global labels. No symbols, wires, pin UUIDs, coordinates, or
  net names changed. No PCB file was touched.
- Generator: `phase24_promote_storage_bridge_usb_global_labels.py`; exact
  UUID/coordinate guards prevent a broad replacement.
- Toolchain: qualified `pisxme-kicad-light:v1`, KiCad 10.0.6. Version output
  and all raw command return codes are retained.

## Baseline and candidate evidence

Both runs used the same root schematic and project source from the committed
base/candidate with these native commands:

```
kicad-cli sch erc --severity-all --format json --exit-code-violations \
  --output /workspace/output/{baseline,candidate}-erc.json PiSXMe_RevA_Clean.kicad_sch
kicad-cli sch export netlist --format kicadxml \
  --output /workspace/output/{baseline,candidate}-native.xml PiSXMe_RevA_Clean.kicad_sch
```

The producer baseline reports 351 findings / 0 errors. The candidate reports
349 findings / 0 errors. ERC classes are:

| class | baseline | candidate |
|---|---:|---:|
| `same_local_global_label` | 26 | 24 |
| `multiple_net_names` | 22 | 22 |
| `isolated_pin_label` | 126 | 126 |
| `endpoint_off_grid` | 121 | 121 |
| `lib_symbol_issues` | 53 | 53 |
| `footprint_link_issues` | 3 | 3 |

The two removed warnings are the exact `BRIDGE_USB_DP/DM` local/global
collisions. No new ERC class or severity-error finding appeared.

The native netlist exports contain 361 nets each. Semantic comparison of net
names and sorted node attribute sets reports zero missing names, zero extra
names, zero changed node sets (`semantic_equal True`). XML byte differences,
if present, are serialization metadata only. The candidate source SHA-256 and
all retained artifact hashes are in `SHA256SUMS`.

Disposition: bounded source-hygiene candidate passes its identity-preserving
producer validation and is ready for Root's serialized integration review.
It remains source-only evidence; it does not close integrated ERC or Phase 24.
