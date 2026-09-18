# Local rail overlay evidence receipt

- Package: `P24-LOCAL-RAIL-OVERLAY-EVIDENCE`
- Base requested by dispatch: `45f78de58ff43d3d074c62d95a973cbf4419a17d`
- Queue recorded base: `2d6e3ea4cfd08f587d42be66cc37a77838e5641a`
- Reviewed HEAD: `168998cb570cf4dbaaa1857c0f52d62d023fb500`
- Board SHA-256: `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c`
- Result: `EVIDENCE_READY; INTEGRATED_REGULATOR_OVERLAY_REMAINS_OPEN`
- CAD changed: no
- Protected bus touched: no
- Producer candidate: none
- Integration candidate: none

## Scope and evidence

The packet audits U3/U4/U5 TPSM63606 support cohorts, native schematic
capacitance/value contracts, current serialized geometry, local routes/returns,
TI layout guidance, and thermal-evidence boundaries. The package did not edit
the board, schematic, rules, libraries, source topology, or protected-bus
region.

The full machine-readable result is `LOCAL_RAIL_OVERLAY_EVIDENCE.json`; the
human-readable result is `LOCAL_RAIL_OVERLAY_EVIDENCE.md`. `geometry.json` and
`support-census.json` are read-only exact-board measurements. `native-netlist.xml`
is regenerated from the current root schematic with KiCad CLI.

Current integrated findings:

- U3 input/output bypass is physically nearby, but the current serialized board
  has no local POWER_GND via within 4 mm of U3 and its FB/control cohort is not
  locally closed.
- U4 input/output support is 147.763–155.724 mm / 118.207–130.188 mm from
  the regulator; BRIDGE_3V3, FB, RT, and PG have zero serialized routes/vias.
- U5 input/output support is 118.431–132.098 mm / 27.459–105.802 mm from
  the regulator; BRIDGE_1V1, FB, RT, and PG have zero serialized routes/vias.
- The board-wide POWER_GND zones exist, but board-wide segments/vias do not
  prove the required per-module local PGND thermal-via arrays.
- Nominal COUT sums are U3 44 uF, U4 66 uF, and U5 352 uF. The 90% screen is
  not a DC-bias/temperature or load-step proof; 1.1 V has no direct TI table row.

## Validation

Two exact-source checks report the same integrated census:

- qualified fresh Light receipt, KiCad 10.0.6: 300 violations / 499
  unconnected items (`validation-receipts/si-power-reference-current-head-61085fe0`);
- host read-only cross-check, KiCad 10.0.5: 300 violations / 499
  unconnected items (`drc-host-10.0.5.json`).

This package closes the evidence census only. The Phase 24 integrated
`regulator_reference_overlays`, power-rail, thermal, and connectivity rows
remain open. Root must route any CAD implementation through the serialized
producer/integration path after protected-bus dependency resolution, followed
by fresh Light validation at the integrated SHA.

No fabricated-hardware, vendor-approval, production-qualification, or board
thermal-measurement claim is made.
