# RTL9210B GND-return corridor trials — V1470–V1476

Date: 2026-09-10
Base for all trials: `PHASE24_RTL9210B_U163_RXN_REHOME_V1469.kicad_pcb`

These disposable trials attempted to connect the internally joined
U1.45/U1.66/U1.69 GND island to the remote GND return while preserving the
approved QFN, 0.20 mm routing, ordinary-through-via, and layer rules.

- V1470: bottom/right edge via; rejected, 14 violations from RTL_3V3,
  RTL_1V1, and CLKREQ interactions.
- V1471: farther outboard via/trunk; rejected, 7 violations from SPI,
  CLKREQ, and local rail interactions.
- V1472: north U1.45 departure; rejected, one RTL_1V1 via short.
- V1473: exposed-pad top-right launch; rejected, 6 B.Cu/support crossings.
- V1474: outer top-right corridor; rejected, 9 QFN/right-pad and rail
  conflicts.
- V1475: right shelf; rejected, 3 remaining rail/corridor interactions.
- V1476: short F.Cu overpass; rejected, 6 QFN/support-field violations.

These are route-implementation results, not architecture rejection. V1469
remains the accepted lower QFN/lane/rail basis with zero native DRC; the next
credible work is coordinated GND-plane/return-field regeneration, not a
validation-rule relaxation. No production CAD or Path A asset changed.
