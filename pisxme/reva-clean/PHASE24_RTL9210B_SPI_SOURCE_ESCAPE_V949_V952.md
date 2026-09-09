# RTL9210B SPI source-escape evidence — V949–V952

## Current state

Path B remains disposable and isolated. No production schematic/PCB asset was
changed. The clean-field V944 candidate remains the comparison base.

V948 was rejected because SPISO and SPISO3 shared a via, crossed in F.Cu, and
the SPISO3 launch entered U1 pad 2. V949 rebuilt both nets with independent
source transitions, B.Cu corridors, and right-side U2 launches. V949 reduced
the result to two errors: one SPISO source crossing and one B.Cu clearance.

V951 moved the SPISO transition below the pad field. It removed the
SPISO/SPISO3 crossing but placed the via inside the 4.8 mm U1 exposed pad;
native DRC reported the resulting clearance error. V952 swept four alternate
transition cells. The best candidates still fail at the U1 source field:

| candidate | native DRC violations | unconnected items | result |
|---|---:|---:|---|
| A | 9 | 25 | rejected |
| B | 8 | 25 | rejected |
| C | 7 | 25 | rejected |
| D | 7 | 25 | rejected |

The remaining errors are real geometry failures, not synthetic connectivity
or a topology objection. The present U1 orientation exposes SPISO3
(99.6,66.05), SPISO (99.2,66.05), and SPICS (98.8,66.05) immediately above a
4.8 mm exposed pad. At the active 0.20 mm track / 0.20 mm clearance rules,
the available source escape field is saturated by pad clearance and the
existing RTL_1V1/RTL_5V corridors.

## Decision

Do not promote V949–V952. Do not relax rules, add synthetic graph edges, or
claim SPI closure. The next bounded experiment is to regenerate the source
field with a different U1 orientation or a co-designed QFN escape primitive,
then re-run native DRC and the saved negative-control connectivity audit.

Raw boards, scripts, and DRC reports are retained as rejected evidence.

V953–V956 tested U1 orientation as the next solution class. U1-180 placed
the SPI pads in a tighter 0.4 mm vertical source field (V954: 9 DRC findings;
V955 staggered: 14). U1-270 restored a horizontal field but a same-side
parallel fanout still crossed later transitions (V956: 9 findings). The next
candidate will use mixed-side source escapes and independent transitions;
these probes do not alter production CAD.
V958 attempted to transplant the older V736 separated-shelf routing onto the
current V944 clean field. It was rejected with 13 native DRC violations,
including SPISO/SPICLK and SPISO3/SPISO source crossings plus downstream
SPICS/SPISO shelf crossings. Historical copper is therefore not being
restored; current transformed pads require a fresh escape authoring pass.
V957 tested mixed-side same-layer fanout after U1-270 rotation. It was
rejected (15 native DRC violations): inner pad departures still cross
outer-pad fields before reaching their side-specific transitions. The next
escape class must separate inner departures by layer immediately at the QFN
field; same-layer fanout is not sufficient.
