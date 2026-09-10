# Phase 24 storage support V129/V130 receipt

V129 tested a fresh local U11-to-U12 support escape from native pads. The
direct four-net candidate passed the four CM5 USB3 endpoint assertions and
the two direct RX support assertions, but TX coupling-cap endpoints remained
unconnected.

V130 moved C86/C87 into the storage acreage and added both TX capacitor legs.
All ten native support/USB3 endpoint assertions passed, but native DRC
rejected the candidate at 207 violations / 499 opens with real shorts and
crossings into USB_DP, JMS_VCCO, USB_RXN1, and the U12/U13 pad fields.

Decision: reject V130. This is a local support escape implementation failure;
the storage topology and V127 CM5 USB3 route remain unchanged. The next
candidate must use obstacle-aware pair escapes around the U12/U13 fields and
must not use direct F.Cu runs through their pad columns.
