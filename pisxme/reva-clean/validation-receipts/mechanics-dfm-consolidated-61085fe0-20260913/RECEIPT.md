# Phase 24 mechanics / 3D / assembly / DFM consolidated package

- **Package state:** `DONE_PACKAGE_EVIDENCE_OPEN_ACCEPTANCE`
- **Scope:** current canonical PCB mechanical, 3D-model, assembly/service, and fabrication-input census. This package did not edit routing, outline, anchors, footprints, schematic, rules, or configuration.
- **Source:** `nova-rey/pisxme`, branch `reva-clean`, documentation HEAD `61085fe0`.
- **Selected PCB:** `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- **Selected PCB SHA-256:** `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c`
- **Schematic SHA-256:** `6eef63bd3d2b0b9fafc0150d3c34f636ce24a48b2ecbd3d28a5f0bfec167e9f1`
- **Rules SHA-256:** `d5473e6262fdf3b53d5de051626f0ed76dedf7257ba591f79ab8ad55f5b411ec`

## Fresh current-head checker result

A fresh detached qualified `pisxme-kicad-light:v1` checkout validated the selected board with KiCad 10.0.6. The launcher receipt and raw outputs are retained in this directory.

Command:

```text
kicad-cli pcb drc --format json --severity-all --exit-code-violations --output /workspace/output/current-drc.json PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb
```

The native checker returned `5` because unresolved findings remain. It reported **300 violations**, **499 unconnected items**, and **0 `shorting_items`**. The exact class census is:

| Class | Count | Package disposition |
|---|---:|---|
| `clearance` | 138 | Open; route/net-class owner must resolve. No blanket rule relaxation. |
| `track_width` | 118 | Open; preserve controlled-impedance and approved fine-escape scope. |
| `copper_edge_clearance` | 15 | Open; requires coordinated edge/routing decision. |
| `track_dangling` | 9 | Open physical connectivity requirement. |
| `via_dangling` | 7 | Open physical connectivity requirement. |
| `courtyards_overlap` | 6 | Open mechanical placement/assembly disposition. |
| `pth_inside_courtyard` | 5 | Open; explicit M.2 envelope is not shrunk to hide the finding. |
| `tracks_crossing` | 2 | Open physical routing requirement. |

Raw `current-drc.json`, stdout, return code, and hashes are retained. The machine-readable details are in `mechanics-dfm-census.json`.

## Mechanical and envelope dispositions

The six native courtyard overlaps are:

- `C5/C6` and `C7/C8`: placement/assembly clearance remains open.
- `J3/MECH_M2_2280` and `J8/MECH_M2_2280`: the explicit 2280 SSD envelope intersects the connector/header geometry; the envelope must not be silently reduced.
- `J7/C14`: CM5 body/underside and service clearance requires exact assembly/access disposition.
- `L10/U11`: local power/storage support placement requires coordinated disposition and is adjacent to the blocked integrated geometry.

The five PTH/courtyard findings are J3 M2 and J8 pads 1–4 against `MECH_M2_2280`. They remain open findings. No waiver or severity change was applied.

The current board edge envelope is approximately `(-0.05,-0.05)` to `(300.05,180.05)` mm. The retained envelope census records positions, orientations, and bounding boxes for J1, J3, J5, J6, J7, J8, `MECH_M2_2280`, U1, U7, U13, and U14. Existing connector and interface anchors remain protected by this package.

The prior native model census is byte-applicable to this exact selected PCB SHA (the source board at its basis commit hashes identically): 131 footprints total, 3 with 3D model records, and 128 without. The missing-model list includes the major connectors, ICs, passives, test points, and the M.2 mechanical envelope. Required exact model acquisition and geometry verification remain open. `CM5_J7` has a retained model record; the other model records are insufficient for full assembly signoff.

The complete lists are retained as `mechanical-census.txt` and `mechanics-envelope.txt`. Source receipts: `mechanical-model-census-3a811eac-20260913/` and `mechanics-envelope-current-0b65731e-20260913/`.

## Assembly, service, and fabrication evidence

The applicable authority records establish the following constraints:

- Amphenol/FCI `74221-101LF` J1 identity and manufacturer authority are closed, while hidden-joint SMT access, exact local land-pattern overlay, and an exact connector model remain required for assembly signoff.
- JAE `SM3ZS067U410ABR1000` J3 is the selected B-key 2280 socket; its retention datum, cable/SSD access, and exact package model must be included in final assembly evidence.
- Molex `0039300020` J5/J6 and Littelfuse `178.6165.0001` fuse holders are through-hole, serviceable parts. Their documented assembly path requires a second selective/wave/hand solder operation; current routing and thermal evidence does not sign this operation off.
- The V100 cooler/backplate authority closes a conservative Rev-A collision contract and explicitly provides no proprietary carrier-mounted cooler CAD. No unverified cooler or backplate fit is claimed.
- The selected six-layer `JLC06161H-7628` stack is the fabrication basis. Order-time impedance coupon, tolerance, and fab-return evidence remain required.

A current production release package is absent from the canonical tree. The audit found no current Gerbers, drill package, CPL/position file, assembly drawings, panelization, fab-job/package, or complete revision-linked model set. The regenerated BOM and exclusion disposition receipts are useful scoped evidence, but they are not a final release package; `TP1`–`TP13` and `MECH_M2_2280` still require explicit final assembly/DFM disposition on the final integrated SHA.

## Acceptance disposition

| Acceptance row | Status | Evidence and remaining gate |
|---|---|---|
| `mechanical_3d_assembly_service` | `OPEN` | Geometry and model census retained; courtyard/PTH/edge findings, exact models, cooler/SSD/cable envelope, assembly sequence, and service access remain unresolved. |
| `dfm` | `OPEN` | Native DRC and release-input inventory retained; 300 violations, 499 unconnected items, missing release outputs, and assembly/model gaps remain. |

This package is a completed evidence work package, not a Phase 24 acceptance PASS. It creates no authorized disposition for native violations and no fabricated-hardware claim. The acceptance rows remain open until a later valid integrated candidate is mechanically and DFM validated.

## Authority and next action

Authority basis is retained at:

- `authority-inventory/PHASE2_AUTHORITY_INVENTORY.md`
- `authority-inventory/primary-docs/sxm2/SXM2_74221-101LF_AUTHORITY.md`
- `authority-inventory/primary-docs/m2-jse/M2_SOCKET_AUTHORITY.md`
- `authority-inventory/primary-docs/power/MOLEX_0039300020_AUTHORITY.md`
- `authority-inventory/primary-docs/power/LITTELFUSE_0297015U_17861650001_AUTHORITY.md`
- `authority-inventory/primary-docs/mechanics/V100_COOLER_BACKPLATE_AUTHORITY.md`
- `authority-inventory/primary-docs/jlc/JLC06161H-7628_IMPEDANCE_BASIS.md`

Next action is for the owning integrated CAD/authority workstreams to resolve the blocked corridor and remaining physical findings, then regenerate current BOM/CPL/fabrication/assembly artifacts and run a fresh Light DFM/mechanical gate against that exact integrated SHA. This package must not be used to start Phase 25.

## Artifact manifest

`SHA256SUMS` covers this receipt, the machine-readable census, raw DRC, Light validation identity, mechanical and envelope lists, and checker metadata.
