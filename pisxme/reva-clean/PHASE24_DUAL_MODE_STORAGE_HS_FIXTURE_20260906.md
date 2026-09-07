# Phase 24 dual-mode storage high-speed fixture — 2026-09-06

## Classification

`ROUTE_IMPLEMENTATION_FAILURE` for the combined fixture; source and endpoint
authority remain valid. No integrated production PCB was changed.

## Construction

The fixture starts from the source-derived SATA net-authority board, retains
the CM5 source, U7/U11/U12/U13, U14/J5, J3, coupling capacitors, and local
clock/support footprints, removes inherited copper/zones, emits the native
USB3 selector/bridge routes, then emits the promoted V4 SATA QFN escape.
Only ordinary F.Cu/B.Cu signals and through-vias are used.

## Native connectivity

`phase24_dual_mode_storage_usb3_native_connectivity_audit.py`: PASS for all
ten USB3 endpoint pairs (CM5→U12, U11↔C86/C87→U12, and U11↔U12 RX).

`phase24_sata_native_connectivity_audit.py`: PASS for all eight SATA endpoint
pairs, including U7→coupling capacitors and C30/C31/C32/C33→J3.49/47/43/41.

These audits derive connectivity from saved pads/tracks/vias; their assertion
lists do not add graph edges.

## Native DRC

The combined fixture reports 576 findings and 187 unconnected items. The
report contains genuine SATA/USB3 crossings and shorts, not merely the local
0.20 mm clearance findings. The largest observed cause is that the current
historical source-to-storage corridor crosses the newly co-located SATA
launch; a combined high-speed placement/routing repair is therefore still
required. This is not evidence against the dual-mode architecture.

The raw board and DRC report are preserved as
`PHASE24_DUAL_MODE_STORAGE_HS_ISOLATED_SATA_V4_20260906.*`.

## Tooling correction

`phase24_usb3_dual_mode_isolated_fixture.py` now accepts explicit base/output
paths and retains the complete storage high-speed neighborhood. The simpler
USB3 author now uses `RemoveNative()` and rebuilds the native net list before
saving; this fixed a KiCad 10 Python-wrapper exit-139 mutation failure. Its
first rerun exposed disconnected local support paths, so it was not promoted.
