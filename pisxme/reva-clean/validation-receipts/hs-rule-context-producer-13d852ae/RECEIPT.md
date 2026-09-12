# Phase 24 scoped high-speed netclass context producer receipt

Date: 2026-09-13

## Four-state identity

- Baseline source: committed `4eaf2ab8` (untouched project sidecar `{}`).
- Producer candidate: `13d852aeb6423add9583cbd6f4fc40934327732c` in the
  disposable `scoped_hs_rule_context_producer` worker.
- Integration candidate: none; Root owns serialized promotion.
- Validation result: fresh Light detached checkout of the producer candidate,
  KiCad `10.0.6`, qualified image `pisxme-kicad-light:v1`.

## Scoped context

`PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pro` now defines the existing
Default class at 0.20 mm and three named classes:

- `HS_PCIE_90R`: 0.13208 mm track/differential width, 0.2032 mm pair gap;
  `CM5_PER0_P/N`, `CM5_REFCLK_P/N`, `CM5_PET0_P/N`, and `V100_PET0_P/N`.
- `HS_USB3_90R`: 0.13208 mm track/differential width, 0.2032 mm pair gap;
  `CM5_USB3_RX_N/P` and `CM5_USB3_TX_N/P`.
- `PCIE_PERST_CONTROL`: 0.13208 mm single-ended track width;
  `CM5_PERST`.

The sidecar contains no `board.design_settings.rules` override, so the board
wide minimum remains 0.20 mm. The existing JMS583 `.kicad_dru` is unchanged.
No copper, storage, power, J1, schematic, library, or stackup content changed.

## Fresh Light validation

Command:

```text
kicad-cli pcb drc --format json --severity-all --exit-code-violations \
  -o /workspace/output/drc.json \
  /workspace/project/pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb
```

The command returned RC 5 because the integrated board remains open. It
reported 312 DRC violations and 499 unconnected items. Counts by relevant
class were 118 `track_width`, 138 `clearance`, 2 `tracks_crossing`, and 0
`shorting_items`. The 72 scoped track-width findings are labeled by native
KiCad as `HS_USB3_90R`, `HS_PCIE_90R`, or `PCIE_PERST_CONTROL`; this records
class application while retaining the real board-wide minimum finding.

The required ordinary negative control is present: `SERVICE_VBUS_SENSE`
has 0.13208 mm tracks, remains in native `Default`, and is reported as a real
`track_width` violation against the 0.20 mm board minimum. This demonstrates
that the context does not globally exempt 0.13208 mm geometry.

The fresh pcbnew audit found 72 scoped track segments, 23 scoped vias, every
scoped segment exactly 132080 nm, and only F.Cu/B.Cu signal layers. The board
retains In1/In4 ground reference layers and 17 POWER_GND stitching vias. No
scoped via is within 2 mm of a POWER_GND via (nearest measured distance
33.3135 mm), so the audit records reference-plane availability but does not
claim local return-via closure or SI closure.

Raw files in this receipt directory are the producer baseline and fresh
Light outputs. The fresh validation is context evidence only; it does not
close native DRC, physical connectivity, power, or acceptance rows.
