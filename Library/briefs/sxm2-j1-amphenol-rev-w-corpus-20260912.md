# SXM2/J1 Amphenol Rev-W manufacturer corpus

Date: 2026-09-12
Scope: Manufacturer evidence supporting the package/footprint and assembly portions of the PiSXMe J1 contract. This brief does not assign SXM2 electrical functions.

## Sources

- `amphenol-74221-drawing-w`: [74221 Rev W drawing](https://cdn.amphenol-cs.com/media/wysiwyg/files/drawing/74221.pdf), released 4mm receptacle assembly, 10 x 40 = 400 positions, drawing EC ELX-V-40495-1, approved 2021-04-13.
- `amphenol-gs-12-100-rev-r`: [GS-12-100 Rev R](https://cdn.amphenol-cs.com/media/wysiwyg/files/documentation/gs-12-100.pdf), FCI product specification, authorized 2013-10-14.
- `amphenol-gs-20-033-rev-j`: [GS-20-033 Rev J](https://cdn.amphenol-cs.com/media/wysiwyg/files/documentation/gs-20-033.pdf), FCI application specification, verified 2016-04-27 and printed 2016-05-04.

The browser text extraction for all three documents was available on 2026-09-12. Direct `curl` from NYX returned HTTP 403 for each URL; therefore no local PDF bytes or SHA256 values are claimed. The Library retains URLs, revisions, extracted facts, and access/licensing disposition only.

## Cross-correlation

GS-12-100 identifies the 400-position 10 x 40, 4.0 mm mated-height pair as plug 84740 and receptacle 74221. Rev W independently identifies drawing 74221 as a released 4mm, 10 x 40 = 400-position receptacle assembly. GS-20-033 repeats the 74221/84740 pairing and supplies the application constraints: 0.584--0.635 mm copper-defined PCB lands, at least 0.15 mm solder-mask clearance around lands, no vias in BGA lands, covered connector-side vias, and a generally recommended 5.10 mm perimeter rework keepout. It also identifies A1 by a triangle and specifies that drawing/product specification precedence controls conflicts.

These manufacturer records corroborate PiSXMe J1's component identity, 400-contact geometry, orientation convention, and assembly/DFM constraints. They do not corroborate Benchoff's SXM2 contact electrical map, V100-specific auxiliary behavior, or the PiSXMe route. The Benchoff article/repository remain one reverse-engineered evidence family; the Xiaoyu repository remains insufficient at its pinned revision; CN108280004B remains topology/connector-use corroboration.

## Project linkage

The structured contact index is `Library/indexes/sxm2-benchoff-contact-map.json`. The active PiSXMe J1 footprint identity and coordinate cross-check are recorded in `Library/briefs/sxm2-j1-unblock-20260912.md`. Package/DFM authority may use this brief for the manufacturer portion of the gate, while electrical authority retains responsibility for the bounded J1 net contract and unknown-contact disposition.
