# Phase 24 STORAGE USB3 label-scope candidate

- Producer base: `19a1390a2bca36515b6cc1a08a9d5c0b7e6d88d8` (assigned base 19a1390a)
- Candidate scope: four existing STORAGE fanout labels only; local `label` records for CM5_USB3_RX_N, CM5_USB3_RX_P, CM5_USB3_TX_N, and CM5_USB3_TX_P become global labels. No symbols, wires, pin UUIDs, coordinates, or net names changed.
- Generator: `phase24_promote_storage_usb3_global_labels.py`; clean regeneration from base is byte-equal to candidate.
- Candidate STORAGE SHA-256: `c647b404c03e7e8e57aa2ccf93bd38950200ab100414989003b73b328f392776`
- Native producer tool: KiCad Light 10.0.6 (qualified image pinned by campaign)
- ERC: 351 total findings, 0 errors; 121 endpoint_off_grid, 126 isolated_pin_label, 22 multiple_net_names, 26 same_local_global_label, plus 53 lib_symbol_issues and 3 footprint_link_issues. Baseline same-source Light report was 355 total; four same-local/global warnings were removed.
- Semantic netlist comparison: 361 net names in both exports; zero name delta and zero changed node sets. XML bytes differ only in native export metadata.
- Raw hashes: producer ERC `875becd73bda5774fafd34d340faeb113fc05b6ae8b3e4dcecf1b9e690b9c5bb`; baseline XML `d434175efbe8cd20a6d66b03076fc58e1821bc597cb631770a8a692a232c97ad`; candidate XML `321292978f31694757f602079bee742da6fe794e8b163f83417d6496b70feb2a`.

Fresh Light validation workspace: `validation-source-erc-label-validate2-20260912T185524Z`; native ERC reproduced 351 findings / 0 errors with the same class counts. Fresh netlist semantic comparison against `baseline.xml`: 361 names, zero name delta, zero changed node sets. Fresh ERC SHA-256: `48ff15efe676fa9a0a1ea1836e4549bbf096146a3ab4c7cc55291f9eeb3cd8dd`; fresh XML SHA-256: `6adffde32686f0d6ce5ebdaa4499adf2c00e3aa8c8dc686147c7d7f572cccc3`.

Disposition: candidate passes its bounded source-hygiene validation and is ready for serialized Root integration review. This is source hygiene evidence only; it does not close integrated ERC or Phase 24.
