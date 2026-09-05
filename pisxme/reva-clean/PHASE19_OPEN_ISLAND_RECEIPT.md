# Phase 19 open-acreage live-endpoint receipt

Status: `REJECTED_EXPERIMENT`

Candidate: U7 `(260,105)`, rotation `270`; J3 `(290,105)`, rotation `0`.

Native authoring path: `phase19_live_coordinated_open_island.py`.

Native DRC command:

```text
kicad-cli pcb drc --all-track-errors -o PHASE19_OPEN_ISLAND_LIVE-drc.rpt PHASE19_OPEN_ISLAND_LIVE.kicad_pcb
```

Latest result: `390` DRC violations and `478` unconnected items for the
consultant-reviewed legal 90-degree variant with U7 at `(240,105)` rotation
270 and J3 at `(270,145)` rotation 90. The candidate is rejected. It has candidate-introduced SATA/clock crossings and shorts; the
board-wide unconnected count also reflects that this disposable donor has no
inherited production copper. No clean-board artifact was modified or promoted.

The authoring path records placement, serializes a synchronization snapshot,
and uses native-reloaded endpoint coordinates for route generation. Ordinary
through-vias are used; no plane-layer signal routing or via-in-pad is authored.

Follow-up opposite-side placement: U7 `(260,105)` rotation `270`, C30-C33
west of U7, J3 `(200,140)` rotation `90`. Native DRC: `377` violations and
`476` unconnected items. Rejected because live SATA launch and clock fanout
still cross the U7/regulator pad field. This is evidence only; it is not a
Phase 19 closure claim.

Follow-up farther-outboard bridge: U7 `(280,105)` rotation `270`, J3
`(200,140)` rotation `90`, with C30-C33 between bridge and socket. Native DRC
measured `384` violations and `476` unconnected items. Rejected; clock/SATA
local escape crossings remain.

Topology-vs-integration fixture: the balanced S-expression preparation path
created a KiCad-loadable storage-only donor with `92` DRC violations / `78`
unconnected items before routing. The coordinated generator produced `322`
violations / `70` unconnected items after routing; candidate SATA/clock
crossings remain. This fixture is rejected and does not establish Phase 19
closure.
