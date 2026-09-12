# Phase 24 storage USB3 support V4 receipt

Candidate: `PHASE24_STORAGE_MKEY_USB3_EAST_SUPPORT_V4_20260912.kicad_pcb`

Native saved-board connectivity passes all ten USB3 links. V4 retains the
accepted east U12 source handoff, uses directional 0.10 mm local U11 escape
segments, and separates the U12 returns to the right of its exposed pad.

It is rejected as a route implementation: native KiCad 10.0.5 DRC after
refill reports 459 violations / 421 unconnected. The decisive new findings
are U11 fine-pitch escape contact with adjacent/no-net pads, RX support-pair
return convergence at U12, and a same-layer support-channel crossing. The
remaining unrelated board findings are inherited. No architecture, closed
orientation, layer contract, or accepted source handoff changed.

Next work remains confined to a genuinely pad-escape-aware local U11 fanout
and separately reserved U12 support return channels.
