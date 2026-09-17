# Corrective protected-bus producer blocker

- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Base: `2388c9b13175c32ee503c519237acac28aec1d57`
- Worker: `power-bus-corrective-20260918`
- Toolchain: KiCad Light 10.0.6
- Time: 2026-09-17T23:40:42Z
- State: `BLOCKED_PACKAGE_GEOMETRY_AND_MATING_ASSEMBLY_EVIDENCE`

## Scope inspected

The committed base was loaded with KiCad's `pcbnew` bindings in the qualified
Light worker. The selected board is six-layer
`PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`. The source region contains:

- J5: Molex `0039300020` / `Molex_0039300020_5569_2P_RA`, at (12.000, 25.000) mm,
  pad 1 `12V_IN_A`, pad 2 `POWER_GND`.
- J6: the same two-position Molex footprint at (12.000, 45.000) mm, pad 1
  `12V_IN_B`, pad 2 `POWER_GND`.
- F1/F2, U1/U2, Q1/Q2, D1/D2, and the existing protected-bus copper remain
  downstream of these source pads. J1's 12-V/GND map is outside this package.

The current exact Molex pair has one positive and one return contact per
connector. The private manufacturer evidence rates the exact 2-circuit
application at 8 A/circuit (13 A is a generic family maximum), so the pair
cannot receive the 40 A continuous / 45 A 100-ms source credit.

## Why no CAD candidate was produced

The private Library identifies Samtec PowerStrip/40 as the strongest bounded
candidate: `PET-08-02-T-VT-LC` / `PES-08-02-T-VT` with a `PESS` 10-AWG cable
family. The indexed Samtec test evidence screens two powered contacts at
48.5 A/contact after its cited 20% derating and 30 C-rise basis. It does not
provide an authorized PiSXMe footprint, exact cable-side MPN/length, contact
assignment, or a complete mechanical envelope for this board.

The official Samtec product page exposes a footprint link, but the linked
recommended footprint drawing is marked confidential/proprietary and states
that reproduction or incorporation requires written consent. Its bytes were
not copied into this workspace or repository, and no footprint was synthesized
from it. The public page alone is insufficient to establish the exact pad,
NPTH, keepout, connector-envelope, mating, and cable geometry needed for a
safe KiCad footprint.

The Anderson PP15/45 fallback (`ASMPR45-1X2-RK`) likewise has no authorized
local footprint, exact board-entry geometry, or bound harness/crimp assembly in
the private Library. Retaining the existing Molex footprint would silently
preserve the disqualified 8-A-per-circuit input and would not implement the
authority-selected replacement.

No `.kicad_pcb`, schematic, rules, library, or canonical file was mutated in
this attempt. No connector MPN or footprint was invented. No six-loop
precision-regulation circuitry was restored.

## Exact dependency required to resume

Package/Power Authority must provide one of the following bounded inputs:

1. an authorized Samtec PET/PES footprint package or written permission and
   exact mechanical drawing/license for use, plus the exact cable-side
   assembly and energized two-contact assignment; or
2. an authorized Anderson PP15/45 board footprint/package and exact
   cable/crimp/harness assembly; or
3. another authority-selected high-current assembly with a licensed,
   mechanically verified KiCad footprint and complete mating/harness data.

After that evidence arrives, the producer can replace J5/J6 only in the source
region, route complete positive and return paths, and run the required native
source-connectivity, targeted DRC, resistance, and thermal screen. Until then,
any CAD mutation would be a guessed package and cannot be promoted.

## Retained evidence

- `base-drc.json`, `base-drc.rpt`, `base-drc.stdout`, `base-drc.stderr`, and
  return-code files: untouched-base Light DRC, 300 violations and 499
  unconnected items; command completed with return code 0.
- `REGION_INSPECTION.txt`: KiCad-aware J5/J6/source-region footprint, pad/net,
  and geometry inspection.
- Private Library evidence: `high-current-gpu-input-assembly-20260917`,
  Library commit `82c760b4`, represented in public receipt
  `validation-receipts/power-input-assembly-evidence-20260918/`.
- Manufacturer records used by Librarian:
  `https://www.samtec.com/products/pet-08-02-t-vt-lc`,
  `https://www.samtec.com/products/pes-08-02-t-vt`,
  `https://www.samtec.com/products/pess`, and the Samtec test report URL
  recorded in the private brief. No restricted vendor bytes are retained here.
