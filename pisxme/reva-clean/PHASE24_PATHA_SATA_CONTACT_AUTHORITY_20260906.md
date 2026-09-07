# Phase 24 Path-A SATA contact-authority correction

## Finding

The live TE M-key footprint maps the shared SATA/PCIe lane to J3 contacts
49/47 and 43/41. J3 contacts 1/2/3/4 are configuration and power contacts.
The earlier disposable A* route incorrectly targeted 1/2/3/4; native DRC
therefore reported direct shorts into `M2_CONFIG3`, `M2_3V3`, and adjacent
connector geometry.

## Source correction

The SATA route generator now targets 49/47/43/41, preserves the actual hard
drilled-hole obstacle map, deduplicates emitted native objects, and bounds A*
search expansion. The SATA native endpoint audit uses the same canonical
contacts.

The authoritative child schematic was also reconciled: the four coupling-cap
outputs now use the same canonical M.2 net names as the connector:

| bridge-side function | M.2 net | J3 contact |
|---|---|---:|
| TX+ | `M2_SATA_A_P_PCIE_TXP0` | 49 |
| TX- | `M2_SATA_A_N_PCIE_TXN0` | 47 |
| RX+ | `M2_SATA_B_N_PCIE_RXP0` | 43 |
| RX- | `M2_SATA_B_P_PCIE_RXN0` | 41 |

Source audits still pass after this reconciliation.

## Disposable validation

The first corrected-contact board was generated before the source net-name
reconciliation and consequently failed the native net-ownership check; its
raw DRC is retained as evidence in
`PHASE24_PATHA_SATA_NATIVE_ASTAR_M2CONTACTS_20260906-drc.rpt`.

The hard-obstacle/tight-launch run was bounded at 250,000 A* expansions and
did not produce a candidate for promotion. This is a routing-search/corridor
failure, not evidence against the corrected M.2 contact mapping.

`PATH_A_SATA_CONTACT_AUTHORITY = CORRECTED`
`PATH_A_SATA_NATIVE_ROUTING = OPEN`
`PHASE24 = OPEN`
