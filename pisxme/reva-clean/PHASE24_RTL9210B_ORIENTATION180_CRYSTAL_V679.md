# RTL9210B Path-B V679 — rejected local crystal route

V679 tried direct F.Cu monotonic crystal and load-capacitor joins on the
native-clean orientation-180 support basis. Native DRC found 12 violations,
including an XTAL_IN/RTL_3V3 short, multiple crystal-to-1V1 clearance and
crossing failures, and 20 remaining incomplete opens.

Disposition: reject the route implementation. The orientation-180 rail/RSET
basis remains useful; this direct crystal placement is not promoted.
