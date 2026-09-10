# RTL9210B connector-offset launch rejection — V1598

Date: 2026-09-10

V1598 used connector-pad-order handoffs, a 1 mm-spaced connector via row, and
direct offset dogbones to the native J1 contacts. Native KiCad DRC reported
**16 violations** and 39 unconnected items in the intentionally incomplete
fixture. Connector pitch clearance was improved, but the single-layer source
to via-row diagonals shorted/crossed TX/RX and REFCLK nets and conflicted with
the retained J1 control pads. No candidate was promoted and no rule was
relaxed.

The evidence narrows the next implementation class to mixed source-side
F.Cu/B.Cu assignment or explicit orthogonal channel reservation. The accepted
RTL9210B 0-degree orientation and V1590 QFN escape remain unchanged.
