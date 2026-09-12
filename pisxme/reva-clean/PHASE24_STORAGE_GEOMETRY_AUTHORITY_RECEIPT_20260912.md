# Phase 24 storage geometry authority receipt — 2026-09-12

The private Library was updated at commit `6ec7505f` with provenance and indexed
source notes for JLCPCB capabilities, the JLC six-layer capability page, and
TI HD3SS6126 datasheet SLAS975A / RUA0042A.

Sources:

- https://jlcpcb.com/capabilities/Capabilities (retrieved 2026-09-12)
- https://jlcpcb.com/6-layer-pcb (retrieved 2026-09-12)
- https://www.ti.com/lit/ds/symlink/hd3ss6126.pdf (SLAS975A)
- https://www.ti.com/product/HD3SS6126 (retrieved 2026-09-12)

The indexed fabrication bounds support 0.09/0.09 mm multilayer trace/space,
0.15/0.25 mm via hole/diameter, and 0.20 mm via-to-track as published limits;
these are evidence inputs, not an automatic project-rule waiver.

The unresolved package-authority issue is that PiSXMe U12's retained footprint
uses 0.40 mm pad-center pitch while the TI RUA0042A package documentation states
0.50 mm pitch. Pad and thermal-pad dimensions otherwise match the documented
examples. U12 geometry and any local clearance exception remain blocked pending
package/footprint authority reconciliation. No USB3 route variant was promoted.
