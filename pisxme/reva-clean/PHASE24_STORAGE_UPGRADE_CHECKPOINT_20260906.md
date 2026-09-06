# Phase 24 storage-island upgrade checkpoint

Checked 2026-09-06 on `reva-clean`, before any production schematic or PCB
edit for the SATA/NVMe upgrade.

## Interrupted state

- Git HEAD: `68aac08d57a06efcab02b704d0a0e3aa16043336` (`phase24 test local
  BCu CM5 source escape`).
- Accepted macro decision: `SWAP_ETH_STORAGE`.
- Current Phase 24 state: `OPEN`.
- Current storage development basis: TI `TUSB9261IPVP` with JAE
  `SM3ZS067U410ABR1000` B-key socket and the existing clock/support island.
- The working tree contains user-owned generated fixtures and modified
  candidates. No conflicting long-running routing process was found; none was
  stopped. No unrelated file was reverted or cleaned.

## Evidence preserved

The selected macro, Phase 16 PCIe ancestor, Ethernet/reference source escape
receipts, TI U7 package audit, clock oracle, storage placement/routing trials,
and rejected candidates remain untouched. The current integrated storage route
is not Phase 18/19 closed; Phase 24 still has native DRC/open/connectivity
debt documented in `PHASE24_STATUS.md`.

## Upgrade interruption and resume point

Interrupted task: continue Phase 24 route development and whole-board closure.
The authorized task inserts a qualification and implementation gate for one
M-key socket supporting SATA and NVMe through the existing CM5 USB path.

Resume point: after the NVMe bridge, selectors, M-key socket, mode-control,
power, firmware/configuration, and mode-aware validation authorities are
closed. At that point update the authoritative clean schematic/library and
regenerate only the storage island, then rerun the affected Phase 24 checks
and continue the original whole-board closure.

## Decision at this checkpoint

Do not modify the production schematic or PCB yet. The available ASM2362
authority is insufficient for a safe pad-map or reference-circuit edit. The
accepted SATA-only board is preserved while a precise qualification blocker is
recorded in `PHASE24_STORAGE_UPGRADE_BLOCKER.md`.
