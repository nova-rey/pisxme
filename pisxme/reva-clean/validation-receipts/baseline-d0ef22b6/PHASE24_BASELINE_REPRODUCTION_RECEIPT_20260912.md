# Phase 24 untouched baseline reproduction receipt

Date: 2026-09-12
Workstream: `phase24-baseline-exec`
Workspace: `/home/nyx/eda-workspaces/phase24-baseline-exec`
Repository: `nova-rey/pisxme`
Base SHA: `d0ef22b6076c5ceb43cba5024e4b27f192ec8b27`
Worker: qualified `kicad-light`, 1 CPU, 1 GiB, 256 PIDs
KiCad: `10.0.6`
Image: `pisxme-kicad-light:v1`
Image ID/digest: `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`

## Selected inputs

- Schematic: `pisxme/reva-clean/PiSXMe_RevA_Clean.kicad_sch`
- PCB: `pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- Project: `pisxme/reva-clean/PiSXMe_RevA_Clean.kicad_pro`
- Rules: `pisxme/reva-clean/PiSXMe_RevA_Clean.kicad_dru`
- Symbols: `pisxme/reva-clean/PiSXMe_RevA_Clean_complete.kicad_sym`

Input hashes are recorded in `output/source-input-sha256sums.txt`.

## Commands and results

All commands ran in `/workspace/project/pisxme/reva-clean` inside the worker;
raw stdout and return-code files are retained under `output/`.

| Check | Command | Result | RC |
|---|---|---:|---:|
| Version | `kicad-cli version` | `10.0.6` | 0 |
| Native ERC | `kicad-cli sch erc --severity-all --exit-code-violations --output /workspace/output/baseline-erc.rpt /workspace/project/pisxme/reva-clean/PiSXMe_RevA_Clean.kicad_sch` | 355 findings; no error count reported by summary | 5 |
| Native DRC | `kicad-cli pcb drc --severity-all --exit-code-violations --output /workspace/output/baseline-drc-severity-all.rpt /workspace/project/pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb` | 440 violations; 265 unconnected pads; no `shorting_items`; 2 `tracks_crossing` | 5 |
| Native XML | `kicad-cli sch export netlist --format kicadxml --output /workspace/output/baseline-native.xml /workspace/project/pisxme/reva-clean/PiSXMe_RevA_Clean.kicad_sch` | XML written, 290178 bytes | 0 |
| Live contract | `python3 phase24_live_contract_map.py --root /workspace/project/pisxme/reva-clean/PiSXMe_RevA_Clean.kicad_sch --output /workspace/output/live-contract.json` | PASS; 10 children | 0 |
| Structural hierarchy | `python3 validation/phase3/phase24_hierarchy_structure_audit.py` | PASS; balanced native expressions | 0 |
| Narrow parity | `python3 phase24_schematic_pcb_pad_parity_audit.py /workspace/project/pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb /workspace/output/baseline-native.xml` | PASS; 814 authoritative nodes, 1262 PCB pads, 0 mismatches | 0 |

The diagnostic `output/baseline-drc.rpt` additionally records the first
run with `--all-track-errors`: 469 violations / 265 unconnected, RC 5. It is
retained separately and is not the canonical 440-count baseline command.

The parity run emitted three KiCad `PROPERTY_ENUM` assertions while still
completing with the stated PASS; these are retained in `parity.stdout`.
The baseline is open and does not authorize repair or a completion claim.

## Artifact hashes

| Artifact | SHA-256 |
|---|---|
| `output/baseline-erc.rpt` | `a5a88d3c0a4f2685f0e0e2d908a936edc49f7a7368a02a0aa52baa14aaa622c4` |
| `output/baseline-drc-severity-all.rpt` | `c4b86ef1b1de601319094257600851c482b38b96f73471bff709c13c2505d2ca` |
| `output/baseline-native.xml` | `6b3a2fac2185359491861820202f34237ff7fa5b603f5c01439bef840f715594` |
| `output/live-contract.json` | `3431baaf04f5fbb7ead4554abe62767c0bfa28c1458e6c9f38393be177487b91` |

