# Phase 24 storage orientation discriminator — 2026-09-06

Basis: `PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE.kicad_pcb`, loaded with
KiCad 10.0.5 `pcbnew`. These are disposable coherent storage-island probes;
existing production copper is not used as a quality comparator.

## Native pad-order comparison

| candidate | U7 | J3 | SATA relationship | USB3 relationship |
|---|---:|---:|---|---|
| selected | 180 deg | 90 deg | pair order reverses at the socket launch | native USB3 order is monotonic and already has a clean pair-corridor trial |
| `U7_0_J3_270` | 0 deg | 270 deg | pair order is monotonic from U7 to J3 | RX pair order reverses at U7; requires new escape treatment |
| `U7_270_J3_270` | 270 deg | 270 deg | requires separate bridge-side ordering review | USB3 source-to-U7 order is monotonic, but SATA exits the wrong side for the current J3 region |

## Tested alternate

`U7_0_J3_270` was isolated and given the existing native pair-corridor USB3
authoring method. Native endpoint connectivity passes for all four USB3
pairs, but DRC rejects the candidate with 128 findings including three real
track crossings, six true/field shorts involving the U7 SATA field, and
J3/J7 hole-clearance conflicts. This is a rejected orientation candidate;
the failures are concrete local geometry/mechanics, not a claim that the
storage architecture is impossible.

## Decision

Retain the selected `U7_180_J3_90` orientation as the active storage basis.
Its USB3 pair-corridor trial passes all four endpoint memberships with zero
high-speed crossings/shorts/clearances. SATA remains open and requires a
different local bridge/socket launch construction or a more carefully bounded
coherent rotation that preserves the proven USB3 neighborhood.

`STORAGE_ORIENTATION_DISCRIMINATOR = COMPLETE`
`SELECTED_STORAGE_ORIENTATION = U7_180_J3_90`
`PHASE24 = OPEN`
