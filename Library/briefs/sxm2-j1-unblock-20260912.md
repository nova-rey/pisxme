# SXM2/J1 authority research brief

Date: 2026-09-12
Question: Does public evidence establish a usable contact contract for PiSXMe J1, and how does it map to the active footprint?

## Finding

The Benchoff article and its complete KiCad repository provide a strong public reverse-engineering precedent for a 40 x 10 SXM2 contact map. They are one evidence family, not independent sources, and are explicitly not NVIDIA-official documentation. The manufacturer drawing independently establishes that 74221-101LF is a 400-position, 10 x 40, 1.27-mm-pitch, 4-mm receptacle assembly, but does not assign SXM2 electrical functions. CN108280004B independently corroborates use of FCI 74221-101LF in an SXM2 test-board context and PCIe/NVLink topology, but publishes no detailed contact map. The pinned `xiaoyu9733/sxm2-pinout-definition` commit contains only a README and supplies no usable second map.

## Mechanical correspondence

The active PiSXMe J1 footprint is `PiSXMeRevAClean_SXM2_74221_101LF`, at (150,90), with exactly 400 pads named A1..K40. Its pad coordinates match the Benchoff 74221 footprint convention exactly: A1=(24.765,-5.715), A2=(23.495,-5.715), B1=(24.765,-4.445), B2=(23.495,-4.445), K40=(-24.765,5.715), all relative to the footprint anchor. This establishes an identity transformation by coordinate and pad-name inspection; it does not establish that PiSXMe's existing net assignments are correct.

## Classification

The indexed map has 130 published 12V contacts (rows 22,23,25,26,28,29,31,32,34,35,37,38,40), 155 published GND contacts including the signal-region grounds and rows 21/24/27/30/33/36/39, PCIe receive/transmit contacts in rows 1-13, REFCLK E7/F7, PERST E18, and special K18/K19 protection/cathode labels. Published NC entries in rows 15-20 remain source-declared NC/project-unknown rather than a blanket electrical assignment; Benchoff states 31 contacts were still unmapped/probably unconnected.

## Conflicts and limits

No direct contact-level conflict was found because the only fetched second repository has no data. The identity mapping conflicts with neither manufacturer geometry nor the patent, but neither manufacturer nor patent supplies electrical functions. The published map is suitable as an authority input for package/footprint review and a narrow contract decision; it cannot by itself prove V100-specific undocumented auxiliary behavior, power-current adequacy, or routing/DRC closure. Keep unknown contacts unknown until the package authority and electrical authority accept the evidence.

## Project implications

Package authority should compare the indexed contact IDs mechanically against J1, then classify each PiSXMe net assignment. Any promotion must be a minimal, reviewable net-contract correction; do not copy the reference PCB or its routed geometry, do not assign all 400 contacts merely to obtain parity, and do not infer undocumented contacts from labels.

References: `Library/indexes/sxm2-benchoff-contact-map.json`; `Library/provenance/sources.json`; project-derived `design/PCIE_X1_PROVENANCE.md`; active PiSXMe PCB SHA `1f9e01dd10eacf94de803bee3191a24af20c44a43602f4cf72cc80af60234bd0`.
