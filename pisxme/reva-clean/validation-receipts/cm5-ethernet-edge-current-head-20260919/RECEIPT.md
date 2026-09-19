# CM5/Ethernet edge DFM current-head verification

Current canonical SHA: `f90e7a7566dc80960fdb6fcbf23e418cbe5315ea`.

Fresh detached KiCad Light 10.0.6 validation returned the expected DRC exit code 5: 257 violations and 393 unconnected items. Scoped results are PASS: zero shorts, zero copper-edge-clearance violations, zero C7/C8 courtyard overlap, and no C48–C51 edge-clearance violations. Remaining courtyard overlaps are J7/C14 and C5/C6, outside this package.

The scoped CM5/Ethernet 2D geometry is byte-identical to the prior integrated r3 candidate. Full 3D assembly/service closure remains UNPROVEN under the shared mechanical model-envelope dependency; no CAD edits or waiver are claimed.
