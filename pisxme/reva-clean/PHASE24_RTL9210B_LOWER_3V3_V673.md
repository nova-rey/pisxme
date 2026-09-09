# RTL9210B Path-B V673 — rejected lower-3V3 join on V672

V673 added native U1.39→U2.8 and U1.52→U2.3 RTL_3V3 joins to the positive
V672 RSET basis. Native DRC found 12 violations and 21 opens. Three new
signal failures remain: the U1.52 via contacts the relocated RSET source,
and the U1.39 departure violates/bridges the adjacent USB_DM pad. The
remaining opens are expected incomplete Path-B support.

Disposition: reject V673 as an implementation. V672 remains the RSET basis;
the next class must co-author the U1.39 escape and U1.52/RSET source field,
not add lower-rail channels independently.
