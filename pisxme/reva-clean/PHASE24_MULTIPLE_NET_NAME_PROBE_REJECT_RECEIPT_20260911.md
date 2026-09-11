# Phase 24 multiple-net-name probe — rejected

The disposable probe removed one co-located `NC_*` label from `STORAGE` and
ran native KiCad 10.0.5 ERC. It reduced `multiple_net_names` from 24 to 23,
but the copied project produced 115 `footprint_link_issues` findings that are
absent from the canonical source. Total native findings therefore increased
from 777 to 891.

## Evidence

- Probe: `.phase24_multiple_net_name_probe/`
- Native report: `.phase24_multiple_net_name_probe/no-nc-alias-erc.rpt`
- Report SHA-256: `3474deabf292158a812eb0ce51f76b73f66164e727f0c0aca576ee8b03f88dd1`
- Canonical baseline: `PHASE24_CLEAN_SCHEMATIC_ERC_PROMOTED_20260911.rpt`
- Baseline: 777 warnings / 0 errors
- Probe: 891 warnings / 0 errors

## Disposition

**REJECTED.** The alias removal itself was not promoted. The probe did not
preserve the canonical library/footprint resolution environment, so its one-
warning reduction cannot establish a safe electrical or netlist-preserving
repair. The remaining multiple-name findings require a correctly reproduced
native project copy and explicit net-name/node parity before any label is
removed or renamed.
