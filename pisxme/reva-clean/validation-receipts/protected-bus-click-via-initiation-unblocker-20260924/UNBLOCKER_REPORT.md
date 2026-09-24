# Tier-2 Unblocker — click-on-via route initiation

- Prior failure: pressing `x` after net verification routed from cursor-adjacent `12V_IN_A` copper.
- Root cause: KiCad `x` starts at cursor, not the inspected object; adjacent B.Cu copper is 1.5 mm from the confirmed via.
- Method change: keep `In2.PWR` active and Vias-only selection; move cursor to exact via center `(24.514048,24.273596)` and left-click the via to start the native route. Require status `Routing Track: PWR_SRC_J5_P2` at 0.2 mm before continuing.
- Abort on any other net. No placement/rule/topology changes.
