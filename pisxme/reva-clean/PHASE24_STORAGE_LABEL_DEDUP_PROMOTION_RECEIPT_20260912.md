# Phase 24 STORAGE duplicate-label repair — promoted

## Hypothesis

The repeated `isolated_pin_label` findings were caused by duplicate ordinary
label records with the same name and exact sheet coordinate in
`STORAGE.kicad_sch`, rather than by distinct electrical contracts.

## Controlled proof

The generic transform in `phase24_deduplicate_identical_labels.py` was first
run in a disposable copy. It removed 289 duplicate records across 146 exact
name/coordinate keys. Native KiCad 10.0.5 ERC changed from 483 warnings / 0
errors to 377 warnings / 0 errors:

| class | before | after |
|---|---:|---:|
| endpoint_off_grid | 197 | 197 |
| isolated_pin_label | 232 | 126 |
| same_local_global_label | 30 | 30 |
| multiple_net_names | 24 | 24 |

No new ERC class appeared. The exported semantic netlist comparison was exact:
338 nets, zero missing names, zero extra names, and zero changed node sets.

## Promotion

The same transform was applied to the canonical `STORAGE.kicad_sch` source.
Fresh native ERC reproduced 377 warnings / 0 errors. Raw evidence:

- baseline ERC: `PHASE24_CURRENT_LIVE_erc.rpt`, SHA-256
  `6d75a67ceafe454dc6f1ee21eec82a22cd328c70df3d37fc1b8cd9fab869fac0`
- promoted ERC: `PHASE24_CURRENT_LIVE_AFTER_LABEL_DEDUP_erc.rpt`, SHA-256
  `073595a9a51df1c97033d917000143c35e3330468ca4e378ba786729d058e698`
- baseline netlist: `PHASE24_CURRENT_LIVE.net`, SHA-256
  `0dbc18b62cd9c6ed9d6523df397fba4af0092508cd8646b678ad22fc4872df90`
- promoted netlist: `PHASE24_CURRENT_LIVE_AFTER_LABEL_DEDUP.net`, SHA-256
  `9b7bcc34744c3185706743331c52a044d8786a83ec5b4de74fb59996ba0ba40b`

The raw netlist files differ in serialization, but the semantic comparison is
exact as stated above. This closes one root-cause repair, not Phase 24: the
remaining 377 warnings are still open and unwaived.
