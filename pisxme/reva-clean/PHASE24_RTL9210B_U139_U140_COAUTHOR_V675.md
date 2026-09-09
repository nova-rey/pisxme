# RTL9210B Path-B V675 — rejected adjacent source-via pair

V675 started from the positive V672 interior-RSET basis, removed the old
U1.40 departure, and tested parallel 0.20-mm F.Cu dogbones from native U1.39
(RTL_3V3) and U1.40 (RTL_1V1) to staggered ordinary through-vias. The final
source-only run retained native pad identities and unchanged rules.

Native KiCad 10.0.5 DRC found 13 violations and 24 opens. The key failure is
a real RTL_3V3/RTL_1V1 short: the U1.39 via remains too close to the
adjacent U1.40 departure at the required 0.20-mm clearance. The standalone
U1.39 V674 escape is clean, but this integrated pair is not.

Disposition: reject V675 as a route implementation. The next class must
take U1.40 through a different escape corridor/layer allocation before
placing the U1.39 via; no width or clearance relaxation is allowed.
