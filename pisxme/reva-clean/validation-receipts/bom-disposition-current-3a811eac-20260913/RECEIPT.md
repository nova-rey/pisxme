# Current BOM-only reference disposition

- Board source: `3a811eac`.
- Native PCB serialization confirms all 14 PCB-only references are intentional exclusions: `TP1`–`TP13` carry `exclude_from_pos_files exclude_from_bom`; `MECH_M2_2280` carries `board_only exclude_from_pos_files exclude_from_bom`.
- Values and exact attributes are retained in `bom-disposition.json`.
- This resolves the BOM-only reference ambiguity for this scoped DFM check. It does not close courtyard, edge-clearance, model, assembly, or full DFM acceptance.
