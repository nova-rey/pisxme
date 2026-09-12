# Phase 24 M-key USB3 east handoff receipt

## Decision

`ACCEPTED_SOURCE_HANDOFF_BASELINE`: U12 is moved 15 mm east from the
U12-left/R80 baseline into the open storage pocket. The accepted RTL9210B
orientation and all non-storage anchors remain unchanged. All four J7-to-U12
USB3 lanes use a reserved B.Cu funnel after the source escape, then ordinary
through-vias and short F.Cu dogbones into the actual U12 pads.

## Native evidence

Candidate: `PHASE24_STORAGE_MKEY_USB3_U12_EAST_COORDINATED_20260912.kicad_pcb`

* Actual-pad audit with negative control: PASS for all four J7/U12 endpoint
  pairs; removed RX_N copper disconnects the endpoint.
* Native KiCad 10.0.5 DRC after refill: 418 violations / 427 unconnected.
  No USB3 `tracks_crossing` or USB3 shorting findings remain. Full-board DRC
  remains open because the unrelated `STORAGE_SEL`/`STORAGE_3V3` short and
  inherited unconnected items remain.
* Broader ten-link storage USB3 audit: four CM5 source links pass; six
  U11/C86/C87/U12 support links remain disconnected and are the next gate.

This is an accepted local source-handoff primitive, not Phase 18 or Phase 24
closure. The six-link support network must be routed and validated next.
