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

Corrected USB3-only diagnostic: with explicit `--P19_SKIP_SATA=1
--P19_SKIP_CLOCK=1`, live J7/U7 pad assignment, 0.200 mm tracks, and a
complete source fanout, native DRC measured `80` violations / `75`
unconnected pads. No USB3 source-side crossings or shorts remained; two
U7-final-escape clearances remained at 0.150 mm. The diagnostic is retained
as authoring-path evidence and is not a Phase 19 pass.

U7 escape follow-up: transition vias were moved farther from the live pad
field. Native DRC measured `78` / `75`; USB3 had zero crossings, shorts,
dangling vias, and source fanout opens. The result remains fixture evidence,
not a Phase 19 pass.

Rotated-270-degree SATA launch trial: native DRC measured `101` / `75`.
The candidate improved the launch class but retained U7 RX escape,
coupling-transition, and M.2 dogbone shorts/clearances. Rejected and retained
as evidence for the next SATA correction.

Clock-only support relocation trial: Y1/R23/C42/C43 were moved beside U7
while USB3 and SATA routing were skipped. Native DRC measured `116` / `70`;
the inherited hard-coded XI/XO/VSSOSC fanout crossed and shorted the local
support pads. Rejected; a live-endpoint clock regeneration is required.

Live-endpoint clock regeneration trial: native DRC measured `96` / `67` with
fewer errors than the relocation trial, but clock crossings, support/via
clearances, and one return-via collision with the shared SATA coupling bank
remain. Rejected pending a corrected isolated return corridor.

Separated-clock-bus trial: XO uses a dedicated B.Cu bus and VSSOSC uses a
separate B.Cu return corridor. Clock crossings and clock net-to-net shorts
were eliminated; native DRC measured `92` / `62`. Three U7 pad-field
clearances and one shared-fixture return-via collision remain. Rejected as a
full pass, retained as the current best clock topology.

Follow-up U7 escape adjustment: native DRC measured `93` / `62` and
reintroduced a clock crossing. Rejected; the preceding `92` / `62`
separated-clock-bus candidate remains preferred.

Fine-width clock escape trial: 0.100 mm clock traces were tested without
changing the board minimum. Native DRC measured `120` / `62` with repeated
track-width errors. Rejected; the fabrication rule remains unchanged.

Clock-oracle post-generation transplant: applied the passing minimal clock
geometry over a freshly generated USB/SATA board. Native DRC measured `248` /
`62`; rejection is due to candidate USB/SATA crossings and shorts, while the
clock transplant introduced no new clock-crossing class.

SATA transition follow-up: native DRC measured `96` / `75`. Coupling-pad and
U7 RX pair shorts were removed; dense J3 launch/NC-pad clearances remain.
Rejected as a full SATA pass.
### 2026-09-05 — SATA transition oracle refinement

- `PHASE19_SATA270_LIVE24-drc.rpt`: SATA-only diagnostic, 78 total records,
  zero SATA shorting records and zero SATA crossing records.
- `PHASE19_COORDINATED_SATA270_USB1-drc.rpt`: coordinated diagnostic, 84
  total records, zero shorts, five USB3/SATA crossings.
- Authoring correction: capacitor B.Cu transitions now use ordinary offset
  vias with F.Cu dogbones; TX/RX capacitor rows mirror the rotated U7 pad
  order. No via-in-pad or plane-layer signal was introduced.
- Decision: retain the rotated SATA island as the storage-side oracle;
  reject coordinated candidate until USB3 corridors are regenerated around it.
### 2026-09-05 — coordinated east USB3 trial

- `PHASE19_COORDINATED_SATA270_USB_EAST1-drc.rpt`: 91 total records, one
  short and nine crossings; rejected.
- Failure class: altered source breakout and U7 landing dogbones crossed;
  SATA oracle was not the source of the failure.
### 2026-09-05 — preserved-source top/east USB3 trial

- `PHASE19_COORDINATED_SATA270_USB_TOP_EAST3-drc.rpt`: 88 total records,
  nine USB3 crossings; rejected.
- The CM5 source breakout was retained, but the source-to-upper-corridor lifts
  interleaved and the U7 landing dogbones crossed. No SATA-only failure was
  introduced.
### 2026-09-05 — pair-preserving split-layer USB3 trial

- `PHASE19_COORDINATED_SATA270_USB_PAIR_SPLIT2-drc.rpt`: 92 total records,
  five USB3 crossings; rejected.
- RX and TX were kept as separate differential-pair layer assignments, but
  source and U7 fan-in geometry still failed. SATA oracle remained clean.
