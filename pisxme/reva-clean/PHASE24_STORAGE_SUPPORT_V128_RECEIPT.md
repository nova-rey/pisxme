# Phase 24 storage support V128 receipt

V128 translated the saved isolated dual-mode U11/U12/C86/C87 support copper
by (-10, -15) onto the V127 board and moved C86/C87 to the translated
coordinates. Native endpoint auditing passed all ten declared USB3/support
connections.

The candidate is rejected by native DRC: 164 violations / 499 opens,
including real crossings against CM5_PERST and shorts from translated
support traces into U13 ground and M.2-area objects. The isolated fixture's
coordinates are therefore not a rigidly transplantable island for V127.
This is a placement/route-transplant failure, not a failure of the six-net
support topology or endpoint authority.

The next implementation must co-author the support capacitors and routes at
V127's actual U11/U12/U13 geometry, preserving the V127 CM5 USB3 and PERST
results.
