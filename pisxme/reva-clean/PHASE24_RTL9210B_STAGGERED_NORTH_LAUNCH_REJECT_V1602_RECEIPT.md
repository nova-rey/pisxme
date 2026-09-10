# RTL9210B staggered north launch rejection — V1602

Date: 2026-09-10

V1602 started from the V1601 staggered handoff and attempted a reserved
north-channel launch to the native J1 contacts. Native KiCad DRC reported
**25 violations** and 30 unconnected items. The failure is implementation
geometry: source-side channel crossings/shorts, transition-via attachment
problems, and residual support-field conflicts. No candidate was promoted,
no rule was relaxed, and the V1601 handoff primitive remains the accepted
local source baseline.
