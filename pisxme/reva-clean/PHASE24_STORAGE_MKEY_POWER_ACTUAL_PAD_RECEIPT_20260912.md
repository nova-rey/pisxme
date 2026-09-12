# Phase 24 storage M-key power handoff — actual-pad probe

Starting candidate:
`PHASE24_STORAGE_MKEY_PAD_AUTHORITY_FRESH_20260912.kicad_pcb`

The disposable `phase24_storage_mkey_power_actual_pad_probe.py` derives all
launch coordinates from the saved J3 and U14 pads, then adds only
`STORAGE_3V3` copper and ordinary through vias. It does not use guessed
coordinates or synthetic graph edges.

Resulting candidate:
`PHASE24_STORAGE_MKEY_POWER_ACTUAL_PAD_PROBE_20260912.kicad_pcb`

Validation:

- Native M.2 power-owner audit: **PASS**, all nine J3 power contacts reach a
  native STORAGE_3V3 source.
- Trace-removal negative control: **PASS**, removing an actual required
  STORAGE_3V3 track makes the native audit fail.
- Native DRC: 544 violations / 431 unconnected items. This remains an
  isolated partially routed storage candidate and is not full-board closure.

The candidate is promoted only as the next disposable storage-routing basis;
canonical acreage copper remains unchanged.
