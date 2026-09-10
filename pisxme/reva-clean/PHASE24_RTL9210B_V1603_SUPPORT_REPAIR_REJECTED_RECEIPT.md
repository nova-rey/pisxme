# Rejected support repair after V1603/V1517 integration

Date: 2026-09-10  
Status: REJECTED — disposable implementation evidence only

The attempted local RTL_1V1 and XTAL_IN/XTAL_OUT reclosure connected all
previously open endpoints, but native KiCad DRC rejected the geometry with
13 errors: XTAL/RTL_3V3 and XTAL/GND shorts, RTL_1V1/RSET clearance and
shorting, source-field crossings, and solder-mask/hole-clearance conflicts.

This does not invalidate the accepted V1603 high-speed launch. The clean
authoritative checkpoint remains `21b6c1f0`, whose V1603/V1517 candidate has
zero high-speed DRC errors, native six-net connectivity, and six negative
controls. Support must be regenerated around the existing RSET/RTL_3V3/GND
geometry; no DRC rule was relaxed and this candidate is not promoted.
