# Phase 24 Path-A SATA local-corridor discriminator

Using the source-regenerated disposable board, the SATA A* router was tested
with the M.2 socket translated into local storage acreage. The isolated board
contains the CM5/U7/J3/coupling neighborhood and no unrelated board copper.

- 0-degree J3 at `(138,95)`, local bounds `(90,75)`–`(155,140)`: no legal
  path for the first socket launch.
- Wider local bounds `(75,65)`–`(185,155)`: bounded search exhausted without
  emitting a candidate.

These are route-search failures. They do not reject the corrected source
mapping, the TE footprint, or the Path-A architecture. The next method must
allocate explicit pair corridors or use a native/manual obstacle-aware
router; unconstrained grid expansion is not a sufficient proof of placement
impossibility.

`SATA_SOURCE_NET_AUTHORITY = PASS`
`SATA_LOCAL_CORRIDOR_ASTAR = REJECTED`
`PHASE24 = OPEN`
