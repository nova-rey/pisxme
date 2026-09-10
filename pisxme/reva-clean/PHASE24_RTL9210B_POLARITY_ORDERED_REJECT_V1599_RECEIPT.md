# RTL9210B polarity-ordered launch rejection — V1599

Date: 2026-09-10

V1599 tested a disposable RX/REFCLK polarity-remap hypothesis intended to
make the U1-to-J1 endpoint ordering monotonic. Native KiCad DRC rejected the
fixture with **43 violations** and 41 unconnected items. The trial also
exposed blank/incorrect connector net ownership in the disposable pad-remap
implementation, so it is not evidence for a production polarity change.

No pad remap, architecture change, or validation-rule relaxation was
promoted. The accepted U1 orientation and V1590 source escape remain the
baseline. Any future polarity experiment must first preserve exact native
connector pad ownership, then validate polarity from authoritative PCIe
definitions independently of routing geometry.
