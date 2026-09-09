# RTL9210B Path-B V668 — rejected source-field allocation

Date: 2026-09-09

V668 is a disposable native-pad experiment based on the V595 support,
rail, PEDET, and CLKREQ field. It tested a materially different class from
V667: five staggered QFN source dogbones, distinct B.Cu channels, and bottom
endpoint returns to the native U2 flash pads. It used ordinary through vias,
0.20 mm tracks, and the existing unrelaxed design rules.

Native KiCad 10.0.5 DRC found 49 violations and 11 unconnected items,
including true SPISO/SPISO3/SPICS source-field shorts/crossings and B.Cu
channel conflicts with retained RTL_5V/RTL_1V1/RTL_3V3 fields.

Disposition: reject V668 as a route implementation. This is not evidence
against the RTL9210B package or Path-B topology. It shows that staggering
channels around the unchanged V595 source/rail field is insufficient. The
next credible class must move the isolated U1/U2/flash support island
coherently, or regenerate its complete source field, so SPI escapes and
local rails are allocated together. Path A and production CAD remain
unchanged.

Raw evidence: `PHASE24_RTL9210B_SPI_CHANNELIZED_NATIVE_V668.kicad_pcb`,
`PHASE24_RTL9210B_SPI_CHANNELIZED_NATIVE_V668-drc.rpt`, and
`phase24_rtl9210b_spi_channelized_v668.py`.
