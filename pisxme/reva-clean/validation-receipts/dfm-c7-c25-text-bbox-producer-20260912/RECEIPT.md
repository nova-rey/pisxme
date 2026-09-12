# Phase 24 residual C7/C25 silkscreen repair producer receipt

Date: 2026-09-12

## State and scope

- Producer base commit: `09c15cf8f18c82e2a2a47aeddd33df4da774385d`
- Producer candidate: this workstream's commit (recorded after commit)
- Integrated canonical promotion: Root-owned; this receipt is not an integration claim.
- Changed file: `pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- Changed scope: only the F.SilkS `Reference` properties for C7 and C25.
- No schematic, pads, nets, copper, vias, outline, stackup, rules, footprints, J1, storage, or power objects were changed.

The starting integrated candidate had two remaining `silk_over_copper` findings:

- C7 reference at global `(62.0,168.5)` intersecting C7 pad 1 at `(63.65,168.5)`.
- C25 reference at global `(139.0,170.0)` intersecting C25 pad 2 at `(137.1,170.0)`.

This attempt derives placement from the actual footprint anchor, pad extents, and courtyard. Both references use the available top-side clearance pocket, local `(0,-2.5)`:

- C7 footprint anchor `(65.0,168.5)`, F.CrtYd global box `[63.3,66.7] x [167.15,169.85]`; reference center `(65.0,166.0)`, nominal 1.27-mm text height, leaving the text below its lower edge at approximately `166.635`, above the courtyard by approximately `0.515` mm and clear of both pads.
- C25 footprint anchor `(136.0,170.0)`, F.CrtYd global box `[134.5,137.5] x [168.85,171.15]`; reference center `(136.0,167.5)`, nominal 1.27-mm text height, leaving the text lower edge at approximately `168.135`, above the courtyard by approximately `0.715` mm and clear of both pads.

No text was placed over copper or into the neighboring C7/C8, U3, R5, C24, or C34 component envelopes. The method is a geometric relocation, not a rule change or DRC exclusion.

## Fresh Light validation

Qualified image: `pisxme-kicad-light:v1`
Image digest: `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`
KiCad: `10.0.6`
Command:

```text
kicad-cli pcb drc --format json --severity-all --output /workspace/output/top-drc.json --exit-code-violations pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb
```

The command returned exit code `5` because unresolved DRC findings remain. Raw output is retained as `producer-drc.json`; stdout and the candidate board checksum are retained beside this receipt.

- Base DRC: `314` violations / `499` unconnected items.
- Producer candidate DRC: `312` violations / `499` unconnected items.
- Candidate violation classes: `clearance 138`, `track_width 118`, `copper_edge_clearance 16`, `holes_co_located 9`, `track_dangling 9`, `via_dangling 7`, `courtyards_overlap 6`, `pth_inside_courtyard 5`, `tracks_crossing 2`, `lib_footprint_issues 2`.
- Candidate `silk_over_copper`: `0`.
- No new violation class or unconnected item was introduced by this text-only change.

This is a producer result. Root must cherry-pick or otherwise integrate the candidate serially and run a fresh detached Light validation against the integrated SHA before reusing the result for acceptance closure.
