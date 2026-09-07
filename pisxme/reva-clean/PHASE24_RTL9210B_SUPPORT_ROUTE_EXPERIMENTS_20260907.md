# RTL9210B support-fixture route experiments — 2026-09-07

Status: **REJECTED ROUTE IMPLEMENTATIONS; PATH B ARCHITECTURE UNCHANGED**

These experiments operate only on disposable RTL9210B bring-up fixtures.
Neither changes `STORAGE.kicad_sch` nor the clean acreage PCB.

## Attempt 1 — all-F.Cu support fanout

`PHASE24_RTL9210B_BRINGUP_SUPPORT_ROUTED.kicad_pcb`

The crystal, RSET, and SPI support nets were routed directly on F.Cu using
the fixture's first placement. Native DRC found 58 violations and 46
unconnected items:

```text
17 tracks_crossing
2 shorting_items
36 track_width
3 solder_mask_bridge
```

The author used 0.15 mm tracks below the board's 0.20 mm minimum and forced
long support corridors through one another. Rejected as route implementation
failure.

## Attempt 2 — SPI B.Cu ordinary-via escape

`PHASE24_RTL9210B_SPI_BCU_FIXTURE.kicad_pcb`

The five SPI nets were re-authored with pad dogbones, ordinary F.Cu/B.Cu
transitions, and ordered B.Cu channels. The saved-track/via audit passes and
confirms no via-in-pad coordinates, but native DRC still finds:

```text
2 shorting_items
14 clearance
10 annular_width
10 via_diameter
10 drill_out_of_range
51 unconnected_items
```

This rejects the specific via geometry and remaining pad-field interaction.
It does not reject RTL9210B or the support topology. The next valid route
class must use the ordinary-via dimensions allowed by the selected JLC stack,
move transitions farther from the QFN/flash pad fields, and then revalidate
the full support group.

## Generator correction and support-local V2

Native KiCad inspection found a fixture serialization defect: the generated
layer table declared inner layers as `power` and ordered `B.Cu` before the
inner layers, so numeric layer 2 was loaded as `In4.GND` rather than `B.Cu`.
The generator now matches native KiCad's six-layer `signal` serialization and
layer order. This was a fixture-authoring defect, not evidence against the
route topology.

The support-local V2 placement then moved the crystal, RSET, flash,
decoupling, and pull-ups into a coherent local neighborhood. Its unrouted
native baseline has zero DRC violations. A native-coordinate oscillator/RSET
route against that placement improves to 4 DRC violations / 52 opens, with
three local crossings and one RSET/XTAL interaction; no via, drill, or track
width violations remain. It is still rejected as a route implementation, but
 the placement variant remains a credible next baseline.

## Attempts 3 and 4 — oscillator/RSET local variants

Two further variants were generated from the same native-coordinate support
placement. V3 remained at 4 native DRC violations / 52 opens, including one
XTAL_IN/XTAL_OUT crossing, two shorts (XTAL_IN/XTAL_OUT and XTAL_OUT/GND), and
one solder-mask bridge. V3 is rejected as a route implementation while the
support-local V2 placement remains retained.

V4 changed the local dogbone ordering but regressed to 5 violations / 52
opens, including two shorts and three solder-mask bridges. V4 is rejected as
worse than V3. These experiments do not reject RTL9210B or its support
topology; they establish that another routing method is required rather than
another fixed-coordinate oscillator trial.

## Attempt 5 — V7 separated-layer oscillator route

V7 changed the method rather than another local dogbone ordering: XTAL_IN
escapes to B.Cu at a transition clear of the adjacent QFN pads, XTAL_OUT
uses a separate transition below the XTAL_IN escape, and RSET uses an
independent B.Cu corridor. Native KiCad DRC reports **0 violations / 52
unconnected items**. The local saved-track audit passes and confirms that the
three intended nets are actually authored; the 52 opens are the remaining
unrouted support-fixture boundary and are not waived. V7 is therefore a local
route PASS, not a full RTL9210B fixture PASS.

## Attempts 6 and 7 — SPI support route

SPI V2/V3/V4/V5/V6 were retained as routing-development evidence. They
progressively removed undersized-via, source-pad clearance, dangling-via, and
same-layer crossing defects. The final V7 uses ordinary 0.6/0.3-mm vias for
the three monotonic B.Cu channels, a separated B.Cu SPICLK corridor, and a
F.Cu perimeter corridor for SPISI. Native KiCad DRC reports **0 violations /
52 unconnected items**, and the saved-track/net/via audit passes. This closes
the SPI local route sub-gate only; remaining fixture support and intentional
boundary opens are still open.

## Ground/reference closure discriminator

The isolated V2 fixture had no copper zones, so every GND return remained an
open even after local signal routes passed. An in-board disposable F.Cu/B.Cu
GND pair with ordinary 0.6/0.3-mm stitching vias was added to the SPI V7
candidate. Native DRC remains **0 violations** and unconnected items fall from
52 to 45. This closes reference-plane connectivity for the disposable
fixture only; it does not synthesize signal edges or promote the fixture into
production CAD.

## RTL_3V3 support bus

The first power-support route exposed a generator assumption: after native
KiCad saved the filled fixture, net identities were serialized by name rather
than through the old numeric net table, and the first DRC was run before
refilling zones. The generator now emits native named-net segments. The
refilled candidate connects U2 pins 3/8, C3, and the R2/R3 3V3 returns;
native DRC reports **0 violations / 41 unconnected items**, and the saved-net
audit passes. This is a local support sub-gate, not full fixture closure.

## RTL_5V/C5 and RTL_1V1/C4 support

Five local route variants were rejected for QFN pad-field, corridor, via, or
adjacent-GND geometry. V6 changes the route class: RTL_5V reaches its B.Cu
outboard corridor through an F.Cu transition and approaches C5 from above;
RTL_1V1 escapes from the QFN top row before its B.Cu transition. Native DRC
after zone refill reports **0 violations / 39 unconnected items**. This closes
the two local rail-support sub-gate only; control/sideband, USB, M.2, and
test-access connectivity remain open.

## RESET/PERST and PEDET/CLKREQ control routing

The first combined PEDET/CLKREQ/PERST/RESET author was rejected at **8 DRC
violations / 33 opens**. Its saved-net audit correctly caught distinct
RESET_N versus PERST_N ownership, but the PEDET/CLKREQ B.Cu corridors crossed
the rail/SPI corridors and one J1 transition was too close to PERST. A
corrected separate RESET_N/PERST_N route was then authored from the V6 rail
baseline and passes native DRC at **0 violations / 37 opens**. PEDET/CLKREQ
remain the next control-routing gate and are not waived. V2 reduced the
combined PEDET/CLKREQ class to 3 crossings / 33 opens; V3 changed the
RTL_1V1 corridor but regressed to 5 crossings / 33 opens. Both are retained
as rejected route evidence, not current fixture candidates.

V4/V5/V6 continued the control experiments with layer/detour changes but did
not close the class: their native results were respectively 8 violations /
34 opens, 3 / 34, and 4 / 33. The residuals are same-layer crossings between
PEDET, CLKREQ_N, RTL_5V, and inherited support corridors. This coordinate-only
class is rejected; further work must use a genuinely layer-separated source
and endpoint departure.

## Relocated R2/R3 control-island placement and perimeter routes

The disposable placement `PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL.kicad_pcb`
was corrected after an initial coordinate-frame error. Native inspection
confirms R2 pad 1 at `(71,48)` and R3 pad 1 at `(74,48)`; the only baseline
findings after relocation were stale RTL_3V3 tracks to the former positions.
The 3V3 bus was regenerated from saved named nets before testing controls.

Three new route classes were then tested and rejected without changing Path A
or production CAD:

* `PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V1.kicad_pcb`: 6 native DRC
  violations / 34 unconnected items. PEDET/CLKREQ crossed the inherited
  RTL_5V/RTL_1V1/RTL_3V3 corridors and CLKREQ approached REFCLK too closely.
* `PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V2.kicad_pcb`: 8 violations / 35
  unconnected items. The upper/lower layer split still crossed inherited rail
  corridors and placed the CLKREQ via inside the PERST clearance field.
* `PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V3.kicad_pcb`: 10 violations / 35
  unconnected items. The lower-perimeter class collided with inherited
  RESET/PERST and crystal/support geometry and produced a PEDET pad-field
  interaction.

These are valid native KiCad experiments, not synthetic graph results. They
show that the current local placement plus inherited support escape does not
yet provide a legal PEDET/CLKREQ corridor. They do not reject RTL9210B. The
next authorized class is a coherent local control/support-island regeneration
that includes RESET/PERST departures, rather than adding more perimeter
detours to the current mixed baseline. The fixture remains isolated and Path
A remains preserved.
