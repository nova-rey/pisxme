# Phase 24 U5 native recheck

Date: 2026-09-06
KiCad: 10.0.5 (Flatpak Python bindings and `kicad-cli`)

## Evidence

The corrected `phase24_u5_layer_connectivity_audit.py` was run against the
saved `PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb` fixture and the promoted
`PHASE24_PGND_CLUSTER_CURRENT.kicad_pcb` integrated basis. Both passed after
`board.BuildConnectivity()`, using only KiCad's serialized pads, tracks,
vias, and filled-zone connectivity. The target table is assertion-only; it
does not create graph edges.

The regression negative control removed a real serialized U5.9-connected
track in a disposable saved copy. The audit failed as required. This proves
that the focused audit is sensitive to missing copper rather than merely
asserting the expected component membership.

Commands:

```text
flatpak run --command=python3 org.kicad.KiCad \
  pisxme/reva-clean/test_phase24_u5_layer_connectivity.py
flatpak run --command=python3 org.kicad.KiCad \
  pisxme/reva-clean/phase24_u5_layer_connectivity_audit.py \
  pisxme/reva-clean/PHASE24_PGND_CLUSTER_CURRENT.kicad_pcb \
  --negative-controls
```

Observed result: focused U5 audit PASS; negative control PASS with removed
member `U5.9`.

## Boundary

This is focused U5 connectivity evidence only. It is not a full-board DRC or
Phase 24 closure. Native DRC/unconnected findings remain open and are not
waived, severity-adjusted, or converted into synthetic connectivity.
