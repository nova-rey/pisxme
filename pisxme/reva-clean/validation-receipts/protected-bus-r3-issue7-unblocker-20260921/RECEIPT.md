# Protected-bus R3 Issue #7 producer Unblocker receipt

- **Package:** `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- **Outcome:** `SELF_UNBLOCK`
- **Classification:** `IMPLEMENTATION`
- **Blocker:** Straight raw F.Cu escapes in the R3 B1/B2 native micro-batches did not advance the branch acceptance gate.

## Root cause

The failure is in the raw-escape implementation method. The corrected source
candidate has the complete signed topology: J5/J6/J9, F1-F9, and all 27
branch nets have native pad ownership. The R3 MPA decision fixes the source-
local banks and requires short ordered F.Cu local escapes, distinct ordinary
through-via return arrays, distributed In2 fused joins, and ordered In4 returns.
The attempted four-segment straight raw escapes do not implement that corridor
allocation and are therefore not evidence of a topology or authority
contradiction.

## Evidence

- Corrected source topology: all 27 required nets present; source-stage baseline
  `1039` violations / `499` unconnected items.
- B1 straight raw micro-batch: `1055` violations / `499` unconnected items.
- B2 straight raw micro-batch: `1090` violations / `499` unconnected items;
  `shorting_items` increased from 38 to 42 between B1 and B2.
- R3 MPA decision: `PISXME-P24-PROTECTED-BUS-MPA-20260921-R3`, binding
  source-local placement and layer/corridor ownership.
- R3 MPA reassessment: no geometric contradiction demonstrated; B1/B2 are
  implementation failures and unrestricted straight replay is rejected.

## Chosen alternative

Use **corridor-aware native KiCad Light authoring of one complete branch pair
at a time**, restarting from the corrected source-topology candidate. For the
next branch, derive pad-edge geometry from the loaded board, use the R3 short
ordered F.Cu local positive escape (direct pad entry where legal, otherwise an
ordinary through-via array and short In2 transition), and route its paired
connector return through a distinct ordinary-via array into the ordered In4
return field. Save and reload before targeted validation; do not retain or
extend the B1/B2 straight candidates, add a long raw In2 trunk, or use bulk
nearest-neighbor mutation.

## Why safe and validation

This preserves the signed nine-branch topology, fixed R3 placement, native
design rules, ordinary-via requirement, protected/high-speed corridors, and
the `8.50 mOhm` hot-path acceptance gate. The owner must prove after the first
branch checkpoint that the board reloads, the exact branch nets and endpoints
are connected, no branch-local short/crossing/clearance/width violation was
introduced, and the open-branch census changes as expected. Continue the same
serialized method only after that receipt; complete validation still requires
all branches, targeted native DRC/connectivity, resistance, thermal, and DFM
evidence. A concrete geometric contradiction under this R3 corridor goes to
Macro Placement Authority; it does not authorize a straight replay.

## Resume point

Resume the owned producer at the corrected source-topology candidate with a
fresh Light worker and the single corridor-aware branch-pair micro-batch. No
user approval or authority re-selection is required. Independent work remains
available for source/net census and acceptance-evidence preparation.
