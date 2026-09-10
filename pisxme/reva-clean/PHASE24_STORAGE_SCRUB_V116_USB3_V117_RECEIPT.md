# Phase 24 storage scrub V116 / USB3 reroute V117 receipt

## Scope

Disposable evidence only. Path A and the accepted macro-floorplan are
unchanged. V114 remains immutable historical evidence; V116 is a fresh
rerun from `PHASE24_STORAGE_REGEN_JLC_V113.kicad_pcb`.

## V116 — hierarchical-alias-safe scrub

`phase24_storage_copper_scrub_v116.py` removes storage-owned tracks and zones
using the canonical leaf of the native net name. This catches serialized
aliases such as `/CORE_CM5/CM5_USB3_RX_N`, which the original V114 matcher
missed. Native inspection found zero remaining storage-owned tracks after the
scrub, including zero USB3 tracks on any layer. Under the repository JLC
profile (0.15 mm clearance / 0.13208 mm minimum track), native DRC is 262
violations / 499 unconnected items. This is a clean donor-copper boundary, not
a closed storage route.

## V117 — rerouter regression

`phase24_reroute_storage_usb3_native.py` now uses the same canonical leaf
matching when excluding/removing USB3 copper. It was run from V116 for the
native endpoints J7.128/130/140/142 to U12.16/15/12/11. Native DRC is 405
violations / 499 unconnected items. The report contains true source-field
shorts and crossings at the dense J7 connector field, so V117 is rejected.

The failure is a route-authoring defect, not evidence against the U12
placement: the A* implementation clears an approximately 2 mm halo around
endpoints on a 0.25 mm grid, which erases neighboring 0.4 mm-pitch connector
pad obstacles. The next route class is the existing explicit monotonic
dogbone/source-escape method, retargeted to U12 and then checked natively.

## Decision

V116 is retained as the honest storage regeneration base. V117 is rejected;
no production CAD, Phase 18 closure, or Phase 24 closure is claimed.
