# Phase 24 JMS_REXT local receipt

Candidate: `PHASE24_STORAGE_MKEY_USB3_REXT_LOCAL_20260912.kicad_pcb`

The current reset-local storage base was used. R80 was rehomed to `(148,130)`
and U11 pad 39 was routed to R80 pad 1 with a native-pad F.Cu path that stays
outside the accepted AVDD33, VCCO, and reset support channels. The existing
USB3 copper was not changed.

Native KiCad 10.0.5: JMS_REXT actual-connectivity audit PASS, trace-removal
negative control PASS, and the four-link CM5-to-U12 USB3 audit PASS. The
candidate has 544 inherited DRC violations / 416 unconnected items; this is a
support primitive and not a full-board closure result.

The REXT audit derives connectivity from saved pads/tracks and requires the
trace-removal negative control to fail as intended. No new short/crossing
claim is made from this primitive alone.
