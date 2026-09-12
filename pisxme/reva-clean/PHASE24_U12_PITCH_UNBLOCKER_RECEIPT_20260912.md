# Phase 24 U12 pitch unblocker receipt — 2026-09-12

The bounded Unblocker review classifies the retained U12 footprint discrepancy as
an internal domain-authority issue. Direct source inspection confirms 0.40 mm
pad increments; the indexed TI RUA0042A evidence specifies 0.50 mm pitch.
Local land sizes and the thermal pad match the TI examples, so the pitch issue
cannot be waived as a harmless measurement difference.

Required next authority packet: exact per-pad coordinates, pad 43, paste/mask,
courtyard, and via treatment from the retained footprint versus the TI datasheet
(SHA256 `ce9c29d4c051738737e76a24ca40202e926db58a8b4665581bf905a4bd11b2ee`) or
authoritative TI CAD. Until then, freeze U12 routing/fanout edits. If 0.50 mm is
confirmed, create a corrected producer footprint and revalidate integrated;
if a package-specific 0.40 mm variant is proven, record that authority rationale.
