# Phase 24 storage regeneration V114/V115 receipt

V114 is a disposable post-placement copper scrub of V113. It removes only
storage-owned tracks/vias/zones (`CM5_USB3_*`, storage bridge/selector/SATA/
M.2/support families and mode nets), leaving unrelated board copper intact.

- V114 removed 740 storage-owned copper objects.
- V114 native DRC under the repository JLC profile: 262 violations / 499 opens.
- V115 used the native-pad A* USB3 authoring path from V114 to U12.
- V115 native DRC: 403 violations / 499 opens, including real source-field
  shorts between USB3 P/N and CM5 ground/neighbor pads plus crossings.
- Decision: V115 rejected. It is router/source-alias evidence, not production
  routing.

The next implementation must normalize all transformed J7 source-pad aliases
and co-author the local U12 escape field before regenerating the USB3 pairs.
