# Phase 24 multiple-net-name probe — rejected

The corrected disposable probe removed one co-located `NC_*` label from
`STORAGE` and ran native KiCad 10.0.5 ERC with the project footprint library
included. It reduced `multiple_net_names` from 24 to 23 and native ERC from
777 to 776, but it failed exact netlist parity.

## Evidence

- Probe: `.phase24_multiple_net_name_probe/`
- Native report: `.phase24_multiple_net_name_probe/no-nc-alias-erc.rpt`
- Report SHA-256: `d00e06ce197fa3f014ae532e2d76151604c09fa2e6fc829d3e7af4c991802170`
- Canonical baseline: `PHASE24_CLEAN_SCHEMATIC_ERC_PROMOTED_20260911.rpt`
- Baseline: 777 warnings / 0 errors
- Probe: 776 warnings / 0 errors
- Native netlist comparison: 338 canonical nets versus 339 probe nets; one
  extra `/STORAGE/NC_1` net and one changed `/STORAGE/JMS_VDDREG_5V` node set.
- The initial run without the footprint library was invalid and is not used
  for disposition.

## Disposition

**REJECTED.** The alias removal itself was not promoted. Even with the
corrected library environment, removing the label changed net ownership and
created an extra net, so it is not electrically/netlist safe. The remaining
multiple-name findings require per-label intent analysis; warning reduction
alone is insufficient.
