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

## RTL_5V co-allocation result

V1 and V2 used only native V35 pad coordinates and ordinary through-vias and
were rejected: V2's native DRC found 15 violations, including RTL_5V
crossings with SPISI and RTL_3V3, a QFN-edge contact, and dangling segments.
V4 then used the clear upper source corridor, moved the U1.17 departure clear
of SPISI, and removed an unnecessary mid-corridor via. Its native endpoint
audit passes U1.17/U1.33/C5.1, and the trace-removal negative control passes.
Native DRC has four inherited warnings only; the board still has 32 intended
unconnected items because the remaining Path-B support is not yet authored.
V4 is promoted only as the RTL_5V sub-primitive, not as complete support or
production CAD.

The first RTL_1V1 lower-bus probe is rejected as a route implementation. Its
native endpoint audit and trace-removal negative control pass, but native DRC
reports 21 violations: the proposed bus crosses RSET and XTAL_OUT, contacts
U2 GND and C4 GND, and places several vias in occupied source-field areas.
The next 1V1 attempt must relocate the capacitor/support endpoint or
co-author the lower source field; another identical lower-bus sweep is not a
credible continuation.

The U2-left coordinated experiment moved U2 by 10 mm, regenerated all five
SPI channels from native U1/U2 pads, moved C4, and added the lower 1V1 fanout.
Its independent native SPI and 1V1 endpoint audits pass, but native DRC
reports 14 violations including five QFN-source SPI shorts and one XTAL_OUT
crossing. Reject this route implementation. The experiment does show that U2
migration clears the lower 1V1/U2 corridor; the next attempt must regenerate
the U1 source escapes and 1V1 departures as one field.

The source-preserving U2-left trial keeps V35's proven U1 SPI source escapes,
moves U2 10 mm left, regenerates only the SPI destination legs, moves C4, and
adds the lower 1V1 fanout. Native SPI and lower-1V1 audits both pass with
trace-removal controls. Native DRC reports eight findings: six inherited
ground/silkscreen warnings and two real U1.55/XTAL_OUT local conflicts. No
SPI crossing or short remains. Retain this as the current coordinated
placement basis; the next repair must co-author the XTAL_OUT transition and
U1.55 escape rather than abandon the U2 migration.

The crystal co-author candidate relocates XTAL_IN's source transition to
(93.8,76.5) mm and regenerates XTAL_IN/XTAL_OUT together around the U1.55
escape. Native SPI, XTAL_IN/XTAL_OUT/RSET, and lower 1V1 audits all pass with
negative controls. Native DRC reports six inherited warnings only, with no
signal violations; 26 intended external/support opens remain. Retain
`PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_U2_LEFT_CRYSTAL_COAUTHOR` as the
current strongest disposable basis, not as production closure.

On that basis, the upper RTL_3V3 field connects U1.20/U1.34/R2.2/R3.2/C3.1
with a native trace-removal negative control. Native DRC remains at six
inherited warnings and no signal violations. The first lower RTL_3V3 trial is
rejected: it caused QFN/1V1/RSET contacts, and its 0.13208 mm traces violate
the active 0.200 mm minimum-width rule. Lower 3V3 and remaining controls
remain open; no DRC rule was relaxed.

The upper RTL_3V3 candidate connects U1.20/U1.34/R2.2/R3.2/C3.1 and passes
its native trace-removal negative control. The lower RTL_3V3 candidate was
then tried with U1.39/U1.52 and the relocated U2 endpoints. Its native audit
does not pass; native DRC reports nine findings including RSET/1V1/QFN
contacts. A 0.13208 mm retry was also rejected because it still contacted the
source field and violated the active 0.200 mm minimum-width rule. These are
route-allocation failures, not grounds to weaken the board rules.

## Next implementation step

The 180-degree native orientation probe is now the preferred placement
discriminator. Its U1.39-to-U2.8 RTL_3V3 corridor passes saved-board native
connectivity and fails the trace-removal negative control; native DRC remains
at four inherited warnings before the rest of the field is authored. It is a
route sub-primitive, not a full-support or production pass.
V629 adds the complementary U1.34-to-U2.3 lower RTL_3V3 corridor. Both
channels pass saved-board native connectivity, and removing all RTL_3V3
tracks breaks both; native DRC remains at four inherited warnings with no
shorting or crossing class.
V630 attempted a separated U1.33 RTL_5V departure. It retained both lower
3V3 native connections and reduced the rail field to one real DRC violation,
but the U1.33 0.20-mm source track remains only 0.0769 mm from adjacent
U1.32 no-connect pad geometry. Reject this route and evaluate an alternate
authoritative land pattern/package; do not relax the active routing rule.
V631 then separated the transition field farther west. It retains native
connectivity for U1.17/U1.33/C5.1 RTL_5V and both lower RTL_3V3 endpoint
groups, with all-rail trace removal breaking all three groups. Native DRC is
four inherited warnings and has no shorting, crossing, or clearance class.
Retain it as the current disposable coordinated rail basis.
The bottom-edge U1.36/U1.40/U1.50 1V1 collector is rejected: native DRC
identified a U1.40-to-retained-U1.39 3V3 transition collision and additional
source/edge findings. The next 1V1 authoring must co-allocate departures with
the 3V3 field.
The first all-1V1 perimeter collector derived from V631 is rejected. Native
DRC found U1.16/U1.17 and U1.36/U1.35 source shorts, retained-rail crossings,
and a C4 ground collision. The next 1V1 attempt must use source-side channel
allocation around the proven rail field, not a global collector sweep.

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
- `PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_RTL5V_PROBE_V4-drc.rpt`
- `phase24_rtl9210b_v35_rtl5v_audit.py`
- `PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_RTL1V1_PROBE-drc.rpt`
- `phase24_rtl9210b_v35_rtl1v1_audit.py`
- `PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_U2_LEFT_REROUTE-drc.rpt`
- `phase24_rtl9210b_v35_u2_left_reroute.py`
- `PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_U2_LEFT_SOURCE_PRESERVED-drc.rpt`
- `phase24_rtl9210b_v35_u2_left_source_preserved.py`
- `PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_U2_LEFT_CRYSTAL_COAUTHOR-drc.rpt`
- `phase24_rtl9210b_v35_u2_left_crystal_coauthor.py`
