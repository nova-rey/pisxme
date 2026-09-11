# Phase 24 root-repair probe rejection — 2026-09-11

The existing `phase24_repair_root_hierarchy.py` was run only in the disposable
workspace probe `.phase24_root_repair_probe_current`. It rebuilt root sheet
stubs from the legacy coordinate model and did not modify production CAD.

Native KiCad 10.0.5 ERC rejected the probe with 997 findings. The dominant
416 `endpoint_off_grid` findings were unchanged; `isolated_pin_label` rose to
252 and native `footprint_link_issues` appeared (115). This is a route/source
authoring implementation failure, not evidence against the closed hierarchy
authority or RTL9210B design.

Disposition: **REJECTED**. Do not run this rewriter against the canonical
schematic. Continue with the coherent native-grid generator path, which must
move root sheet geometry, contract pins, labels, and wires as one serialized
unit and then undergo native ERC/netlist validation.
