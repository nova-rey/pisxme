# Phase 24 Macro Placement Authority decision — storage/power congestion

MPA reclassified the unresolved integrated storage/power work as physical
corridor congestion under the current local placement. The approved Path-A
topology and six-layer contract remain unchanged. Further speculative routing
variants are frozen pending the single producer implementation below.

## Binding placement

- Keep U13 at `(180,135)`, top side, rotate to `180°`.
- Move and rotate the top-side coupling cohort to `180°`: C30 `(103.5,116)`,
  C32 `(103.5,120)`, C33 `(103.5,128)`, C31 `(103.5,132)`.
- Move F2 to `(18,145)` and D2 to `(35,145)`, rotations unchanged.
- Keep J1, J3, J5, J6, J7, U7, U11, U12, U14, U1, U2, Q2, C4, Q1, and F1
  fixed. U2/Q2/C4/GATE_B remain a coherent switch cohort.

## Binding corridor and protection rules

- U7-to-capacitor escapes use short F.Cu pad-field routes; transition only
  outside pad fields.
- Capacitor-to-U13 Port-B TX uses separated upper F.Cu channels; RX uses
  separated lower B.Cu channels below U11/U12 and clear of CM5_PERST.
- U13 Port-A to J3 uses ordered eastward differential corridors with
  F.Cu/B.Cu separation and vias outside J3 keepouts.
- STORAGE_SEL and mode control use the east/lower U14 corridor, outside the
  USB3 return field.
- Branch-B raw input uses the outer-left J6-to-F2 corridor; fused output uses
  a separate west-side route to Q2/U2/D2. Keep J6.2 POWER_GND isolated.
- Protect existing CM5 USB3, V100_PET0_N, CM5_PERST, U11/U12 support, J3
  STORAGE_3V3, J1 PCIe/reference copper, and power/ground zones.
- Use ordinary through-vias. The fine-pitch rule is local only; normal
  net-class width, clearance, mask, hole, impedance, and DFM rules apply
  elsewhere. No synthetic connections or permissive global rules.

The producer must use native U13.9 for the second STORAGE_SEL endpoint; the
older census spelling U13.12 is stale. A structural contradiction must return
to MPA with evidence rather than trigger another placement search.

Evidence basis: `PHASE24_BLOCKED_ROUTING_AUTHORITY_20260913.md`,
`validation-receipts/patha-native-storage-census-19a1390a/`,
`validation-receipts/power-return-census-20260913/`, rejected route receipts,
and the private Library storage/power/reference-layout briefs.
