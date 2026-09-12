# SXM2 J1 package/net authority reassessment — 2026-09-12

Authority basis: private Library refresh `01326bd8b6a3190ea07b2504405ea8696e55e858`, including `Library/briefs/sxm2-j1-unblock-20260912.md`, `Library/indexes/sxm2-benchoff-contact-map.json`, and `Library/provenance/sources.json`; manufacturer identity remains Amphenol/FCI `74221-101LF` and Rev-W drawing authority in `SXM2_74221-101LF_AUTHORITY.md`.

Mechanical result: PiSXMe J1 contains exactly 400 pads named `A1..K40`. Parsed pad identifiers and relative coordinates match the Benchoff 74221 implementation by identity transformation (zero coordinate error), including A1, A2, B1, B2, and K40. This is a parsed correspondence, not visual inference.

Electrical contract decision: the existing bounded contract is sufficient and remains approved:

- 130 contacts assigned to `12V_PROTECTED`.
- 170 contacts assigned to `POWER_GND`.
- Selected x1 PCIe/reference/reset contacts retained: A2/A3, G1/G2, E7/F7, E18.
- Other published PCIe lanes remain intentionally unassigned for the x1 product.
- 31 source-declared NC/project-unknown contacts and K18/K19 auxiliary/protection unknown contacts remain unassigned.

Cross-correlation found no contact-level conflict. Benchoff article and KiCad implementation are reverse-engineering evidence, not NVIDIA-official documentation; the pinned Xiaoyu repository contains only a README and does not independently provide a pin map. The manufacturer and patent corroborate connector identity/topology, not contact assignments.

Disposition: **SUFFICIENT for the bounded PiSXMe J1 package/net contract; no schematic, footprint, or net correction is required.** Preserve unknown contacts as unknown/NC. Reopen only on concrete contradictory package geometry or electrical evidence. This decision does not prove fabricated-hardware behavior, procurement readiness, or full-board connectivity.
