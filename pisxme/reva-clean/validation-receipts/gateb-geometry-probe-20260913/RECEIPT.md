# GATE_B overlap geometry probe

Current integrated PCB geometry was inspected in a disposable Light worker.
The GATE_B network has a via at `(12.54,108.0)` directly coincident with Q2
pad 3, plus a B.Cu route from `(12.54,108.0)` to `(12.54,98.5)` and then to a
via at `(14.0,98.5)`, with F.Cu continuation to U2 support geometry.

The overlap is therefore a real via-in-PTH condition, not a duplicate same-net
via. It cannot be removed or waived by the duplicate-via method. A valid repair
would require a pad-aware GATE_B relocation/reroute and fresh DRC; the prior
relocation/removal attempt introduced a real USB_TXP1/JMS_AVDDL short and remains
rejected.
