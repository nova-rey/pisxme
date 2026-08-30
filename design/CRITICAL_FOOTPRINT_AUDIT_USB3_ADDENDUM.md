# Critical USB3 footprint audit addendum

Date: 2026-08-23

This addendum supersedes any earlier “library-only” or “usable with
reorientation” conclusion for the two local USB3 fanout packages.

| Reference family | Active footprint | Evidence | Final status |
|---|---|---|---|
| HD3SS3212IRKSR | `PiSXMe:HD3SS3212_RKS` | TI HD3SS3212 RKS0020A package drawing and imported TIDA-00987 source | **NOT_VERIFIED — geometry mismatch** |
| TPD4EUSB30 | `PiSXMe:TPD4EUSB30_DQA` | TI TPD4EUSB30 official DQA package drawing | **NOT_VERIFIED — geometry mismatch** |

The mismatch is physical pad placement, not merely a missing 3D model or
silkscreen detail. These two footprints are fabrication-critical and must be
replaced/verified before USB3 copper is authorized.

The other previously closed footprint audits are not reopened by this
addendum. PCIe, SXM2, power, CM5, and board-edge mechanical anchors were not
changed.

## Source-archive closure update — 2026-08-23

The attached TI source archive was imported and the corrected analysis-only
footprints were checked in a disposable coupon. The coupon passes with zero
violations and zero unconnected items under its explicit bounded local escape
rule. This validates the corrected package model and flow-through ESD
experiment; it does not reclassify the active footprints. The active board
remains unchanged and the two active USB3 footprints remain `NOT_VERIFIED`.
