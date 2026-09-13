# Phase 24 clean Light baseline reproduction — current head

- Package: `P24-BASELINE-REPRODUCE`
- Base/source SHA: `61b45be32abf27fccbc70f37abe246a711861428`
- Worker: `p24-baseline-reproduce-61b45be3`, qualified `kicad-light`, 1 CPU / 1 GiB / 256 PIDs
- Image: `pisxme-kicad-light:v1`, ID/digest: `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`
- KiCad CLI: `10.0.6`
- Worker checkout: clean detached checkout of `/home/nyx/PiSXMe` at the base SHA
- Scope: untouched baseline reproduction only; no CAD, project, library, or rule mutation.

## Selected context

- Schematic: `pisxme/reva-clean/PiSXMe_RevA_Clean.kicad_sch`
- PCB: `pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- Project/routing settings: `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pro`
- Board rules: `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_dru`
- Symbol table: `sym-lib-table`; footprint table: `fp-lib-table`; project symbols: `PiSXMe_RevA_Clean_complete.kicad_sym`
- Exact input hashes, raw commands, return codes, and artifact hashes are in `raw/`.

## Native results

| Check | Command family | Result | RC |
|---|---|---:|---:|
| Version | `kicad-cli version --format plain` | KiCad 10.0.6 | 0 |
| ERC | `kicad-cli sch erc --severity-all --format json --exit-code-violations` | 293 findings; command reports violations | 5 |
| Native netlist | `kicad-cli sch export netlist --format kicadxml` | 290280-byte XML generated | 0 |
| DRC | `kicad-cli pcb drc --severity-all --format json --exit-code-violations` | 300 violations; 499 unconnected items; 0 reported shorting-items | 5 |
| Live hierarchy contract | `phase24_live_contract_map.py` | 10 children; PASS | 0 |
| Structural hierarchy | `validation/phase3/phase24_hierarchy_structure_audit.py` | PASS | 0 |
| Schematic/pad ownership parity | `phase24_schematic_pcb_pad_parity_audit.py` | 814 authoritative nodes, 1,262 PCB pads, 0 mismatches; PASS | 0 |
| Path-A native connectivity census | `phase24_patha_native_storage_census.py` | 26 required pairs: 11 PASS / 15 OPEN; 292 storage pads | 0 |
| Power/return object census | `validation/phase24_power_return_census.py` | JSON census generated; no CAD mutation | 0 |

ERC and DRC nonzero return codes are expected baseline findings, not worker/tool failure. The three KiCad `PROPERTY_ENUM` assertions emitted by pcbnew-based parity/census tools are retained in `raw/*.stdout`; both tools completed their stated audits with RC 0.

## Interpretation

This is the selected integrated **baseline**, not a producer candidate, integration candidate, validation result, or Phase 24 closure. The 15 open Path-A endpoint pairs and DRC/ERC findings remain acceptance work. The clean worker proves the current exact-head source/rule/library context reproduces under the pinned Light image; it does not waive any physical, connectivity, power, SI, mechanical, firmware, or manufacturing requirement.
