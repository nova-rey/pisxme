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
