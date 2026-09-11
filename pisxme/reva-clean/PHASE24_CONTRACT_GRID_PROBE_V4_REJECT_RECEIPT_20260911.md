# Phase 24 complete-grid probe v4 — rejected — 2026-09-11

## Scope

Disposable only. The probe rewrites the legacy hierarchy contract geometry to
native 2.54 mm spacing while deriving port order from the live labels and
parent-sheet pins. Circuit symbols, footprints, and electrical names were not
changed.

## Native result

KiCad 10.0.5 reported 770 findings. The probe reduced the canonical v3
endpoint-off-grid class from 416 to 280, but introduced four
`label_dangling` errors and three `pin_not_connected` errors, including sparse
`CM5_POWER` and `BRIDGE_1V1_3V3` associations. It therefore fails the native
hierarchy acceptance gate and is rejected.

## Classification

This is a route/authoring-transform failure, not evidence against the
2.54 mm hierarchy approach. The failed result demonstrates that port-order
mapping alone is insufficient: every sparse root label, parent pin, child
label/wire, contract pin, and direct link must be transformed by identity.
The canonical source was not changed.

The disposable raw report is retained in
`.phase24_coherent_contract_grid_probe4/coherent-grid-erc-v4.rpt` in the local
working tree. No production candidate may use this output.
