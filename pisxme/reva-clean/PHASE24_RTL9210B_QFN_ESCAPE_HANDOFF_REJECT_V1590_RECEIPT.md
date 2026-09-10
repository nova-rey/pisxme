# RTL9210B QFN escape handoff fixture — V1590

Date: 2026-09-10

V1590 is a disposable package-escape discriminator on the fixed Claude V1575
orientation and V1517 U1 footprint. It removes only the local source-field
copper and connects all six U1 high-speed source pads monotonically west to
explicit F.Cu handoff pads. It does not claim full J1/M.2 launch closure or
support-circuit closure.

Native saved-board connectivity links every U1 endpoint to its matching JH1
handoff pad. The audit also removes one necessary trace in each of six
disposable copies and requires the link to fail; all six negative controls
pass.

Native KiCad 10.0.5 DRC reports **11 warnings, 36 unconnected items, and 0
footprint errors**. The warnings/opens are expected because the fixture
intentionally strips rail, control, crystal, SPI, and distant endpoint
copper. Crucially, it reports no `shorting_items`, no `tracks_crossing`, and
no padstack errors for the six handoff pads. The source-escape geometry is
therefore accepted as a local primitive, while the overall Path-B field
remains OPEN.
