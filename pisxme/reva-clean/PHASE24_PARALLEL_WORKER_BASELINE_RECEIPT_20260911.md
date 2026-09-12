# Phase 24 isolated worker baseline — 2026-09-11

## Scope

Three independent read-only workstreams were prepared from committed ref
`70bbb8f1` using `/home/nyx/pisxme-eda-workers/scripts/pisxme-worker`:

| Workstream | Worker | Result |
|---|---|---|
| ERC grid | `erc-grid-20260911` / KiCad Light | Native ERC completed: 539 warnings, 0 errors |
| ERC labels | `erc-labels-20260911` / KiCad Light | Native ERC completed: 539 warnings, 0 errors |
| DFM/full-board | `phase24-dfm-20260911` / KiCad Light | Native DRC completed: 180 violations, 468 unconnected items |

The two ERC reports were independently generated in separate workspaces and
have different hashes (`2abae4817e660a34fb0e8d92654f88c281fd9136ecc15b154c363761c2477042`
and `29b255de9c363a56c287bd1847c435430128063946aa8575a35b7ab79003c0e7`),
but the same result. The DRC report hash is
`2ddb531f73849a96d0ce30e1842d65a796ffda8267e6ee396e18ec4281d94393`.

## Interpretation

The live dirty worktree's 483/0 ERC census and 477 unconnected DRC count are
not reproducible from committed ref `70bbb8f1`; they depend on additional
uncommitted state. This is a provenance distinction, not evidence that either
result is correct or incorrect. Canonical integration must first identify and
validate the uncommitted delta. No worker edited canonical sources and no
worker candidate was promoted.

## Next action

Keep ERC grid, ERC labels, ERC aliases, storage power, and DFM as concurrent
workstreams. Reconcile the 483/0 live report against the committed 539/0
worker baseline before promoting further schematic changes; run authoritative
ERC/netlist/parity only after that reconciliation.
