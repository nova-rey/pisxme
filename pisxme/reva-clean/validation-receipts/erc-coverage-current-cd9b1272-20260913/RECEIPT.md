# P24-ERC-COVERAGE current-head result

- Package: `P24-ERC-COVERAGE`
- Candidate/base actually tested: `cd9b127223e987ade64b39680ce14d74e79d18be`
- Qualified validator: `pisxme-kicad-light:v1`
- KiCad: `10.0.6`
- Image digest: `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`
- CAD mutation: none; selected schematic and PCB hashes are recorded in `validation.json`.

## Commands and raw results

The run used a fresh detached Light checkout of the exact tested head:

```text
kicad-cli version
kicad-cli sch erc --severity-all --format json --output /workspace/output/current-erc.json --exit-code-violations PiSXMe_RevA_Clean.kicad_sch
kicad-cli sch export netlist --format kicadxml --output /workspace/output/current-native.xml PiSXMe_RevA_Clean.kicad_sch
python3 phase24_schematic_pcb_pad_parity_audit.py PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb /workspace/output/current-native.xml
```

Return codes and stdout are retained beside this receipt. Native ERC returned RC `5` and reported `293` findings / `0` error-severity findings. The finding classes were `endpoint_off_grid=121`, `isolated_pin_label=126`, `same_local_global_label=24`, and `multiple_net_names=22`. Native netlist export returned RC `0`.

The parity audit returned RC `0`: `814` authoritative schematic nodes against `1,262` PCB pads, `0` expected-pad mismatches, exclusions `nonphysical_x=65`, `j1_placeholder=2`, `j3_key_gap=8`, and aliases `J2=18`, `F1=2`, `F2=2`, `J4=6`. Three nonfatal `PROPERTY_ENUM` assertions were emitted while loading the PCB.

## Disposition

`P24-ERC-COVERAGE` is **DONE as a bounded evidence package with FAIL/OPEN acceptance results**. No safe source repair candidate was produced. The previous guarded NC repair remains rejected because it split the native `U11.62 ↔ J3.62` node and worsened the ERC count; no source changes are promoted.

The native ERC acceptance row remains `OPEN`: zero full-severity findings has not been achieved. The schematic↔PCB coverage row remains `OPEN`: expected-pad ownership passes within scope, but surplus-pad correctness and full bidirectional disposition remain separate requirements. The parity result does not prove physical routing, DRC, power delivery, SI, or manufacturing readiness, and it does not unblock Issue `#2`.
