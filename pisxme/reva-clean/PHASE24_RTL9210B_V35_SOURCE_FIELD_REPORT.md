# RTL9210B V35 source-field checkpoint — 2026-09-08

## Current decision

The native-refilled V35 board is retained as the rotated-U1 source-field
reference. It is not a complete Path-B candidate and must not be promoted to
production CAD. Path A and the current V595/V615 work remain preserved.

## Revalidated evidence

`PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_NATIVE_REFILLED.kicad_pcb` was
loaded and refilled with KiCad's native zone filler before DRC. The resulting
native DRC receipt contains four inherited warnings only: three isolated GND
zone warnings and one C1/R1 silkscreen overlap. The native audits pass all
five SPI endpoints (SPISI, SPICLK, SPISO3, SPISO, SPICS) and XTAL_IN,
XTAL_OUT, and RSET. Removing a necessary SPI or XTAL_OUT trace in disposable
copies breaks the corresponding native connectivity, so the checks do not
use synthetic graph edges.

## V35 versus the current co-allocated field

V35 has U1's saved pad field at approximately x=94.05–101.95 mm,
y=66.05–73.95 mm, with U2 below it and the crystal/RSET support moved as a
coherent cluster. V595 has U1 at approximately x=102.05–109.95 mm,
y=58.05–65.95 mm, with extensive rail/PEDET/CLKREQ copper already allocated.
V35 therefore supplies a clean five-net SPI/crystal source-field oracle, but
does not contain the complete current rail/control implementation.

## Rejected implementation probe

`PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_RTL5V_PROBE_V2.kicad_pcb` used
only native V35 pad coordinates and ordinary through-vias to test an RTL_5V
co-allocation. Native DRC found 15 violations, including RTL_5V crossings
with SPISI and RTL_3V3, an RTL_5V-to-RTL_3V3 contact at the QFN edge, and
dangling RTL_5V segments. V1 is also preserved and was rejected for the
same route-implementation class. Neither probe changes the retained V35
reference or production design.

## Next implementation step

Re-author the complete current support field from native pad coordinates on a
fresh V35-derived disposable board: first allocate all three rails and the
QFN power/control departures around the proven five-net SPI/crystal field,
then add REFCLK, lane 0, USB, and external controls. Do not append another
scalar RTL_5V route to V595. The source-field reference has been proven; the
remaining work is coordinated route allocation and full Path-B validation.

## Receipts

- `PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_NATIVE_REFILLED-drc.rpt`
- `PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35-spi-audit.txt`
- `PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35-support-audit.txt`
- `PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_RTL5V_PROBE_V2-drc.rpt`
