# Protected-bus source-topology authority

- **Package:** `P24-PROTECTED-BUS-SOURCE-TOPOLOGY-AUTHORITY`
- **Decision:** `PISXME-P24-PROTECTED-BUS-SOURCE-TOPOLOGY-20260918-R2`
- **Status:** `DONE` / `BINDING_DECISION`
- **Decision owners:** Product / Power Authority and Macro Placement Authority
- **Canonical base:** `02bb6e639e58ae74b92baecfaf5a68e3e1ad4622`
- **Producer base:** a new isolated candidate must start from that canonical base after Root's queue transition; no rejected producer candidate is an allowed base.

## Decision

The authoritative source lineage for R2 is the current canonical Rev-A source at
the package base above:

| Source | Path | SHA-256 |
|---|---|---|
| PCB | `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb` | `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c` |
| schematic | `PiSXMe_RevA_Clean.kicad_sch` | `6eef63bd3d2b0b9fafc0150d3c34f636ce24a48b2ecbd3d28a5f0bfec167e9f1` |

The source is authoritative for J1, the unrelated macro geography, the six-layer
stack roles, and all existing non-power connectivity. It is **not electrically
R2-complete**: the committed producer receipt proves that it contains only J5/J6
and F1/F2 for this source path. The rejected nine-branch producer files are
non-authoritative and must not be adopted or used as a lineage shortcut.

Because the missing objects are required by the already binding nine-branch
contract, the minimum correction is authorized. This is a topology/source
correction gate for the next isolated producer; this package makes no schematic,
PCB, footprint, routing, or rule edit.

## Exact authorized correction

1. Replace the existing two-pin J5 and J6 source connectors with exactly one
   six-circuit header each, and add exactly one six-circuit J9 header. Use
   `39-30-0060 / 0039300060` and the audited project footprint
   `Molex_5569-06A2_2x03_P4.20mm_Horizontal`. Keep J1 at `(150,90,0)`, J5 at
   `(12,25,0)`, J6 at `(12,50,0)`, and J9 at `(12,75,0)`.
2. Use exactly nine Littelfuse `0297015.U` fuse symbols, F1 through F9, each in
   `PiSXMeRevAClean:ATO_FuseHolder_17861650001`. Place them at:
   `(36,15)`, `(64,15)`, `(92,15)`, `(36,40)`, `(64,40)`, `(92,40)`,
   `(36,65)`, `(64,65)`, `(92,65)`, all top-side at 0 degrees.
3. Bind the nine positive/return pairs exactly as follows. J5/J6/J9 pads 1/2/3
   are positive and pads 4/5/6 are return, paired 1-4, 2-5, 3-6:

| Branch | Positive net | Return net | Fused positive | Fuse |
|---|---|---|---|---|
| B1 | `PWR_SRC_J5_P1` | `PWR_RET_J5_P4` | `PWR_FUSED_J5_P1` | F1 |
| B2 | `PWR_SRC_J5_P2` | `PWR_RET_J5_P5` | `PWR_FUSED_J5_P2` | F2 |
| B3 | `PWR_SRC_J5_P3` | `PWR_RET_J5_P6` | `PWR_FUSED_J5_P3` | F3 |
| B4 | `PWR_SRC_J6_P1` | `PWR_RET_J6_P4` | `PWR_FUSED_J6_P1` | F4 |
| B5 | `PWR_SRC_J6_P2` | `PWR_RET_J6_P5` | `PWR_FUSED_J6_P2` | F5 |
| B6 | `PWR_SRC_J6_P3` | `PWR_RET_J6_P6` | `PWR_FUSED_J6_P3` | F6 |
| B7 | `PWR_SRC_J9_P1` | `PWR_RET_J9_P4` | `PWR_FUSED_J9_P1` | F7 |
| B8 | `PWR_SRC_J9_P2` | `PWR_RET_J9_P5` | `PWR_FUSED_J9_P2` | F8 |
| B9 | `PWR_SRC_J9_P3` | `PWR_RET_J9_P6` | `PWR_FUSED_J9_P3` | F9 |

4. Join the nine fused positives only at `12V_BRANCH_JOIN`, then use the
   existing U1/Q1/D1/C3 cohort (`LM74700QDBVRQ1`, `CSD19536KCS`, `SMBJ18A`,
   `100 nF`) into `12V_PROTECTED`. Join the nine distinct returns only at
   `POWER_RETURN_JOIN`, then `POWER_GND`. U2/Q2/D2/C4 may remain physically
   present but receive no parallel-bus or N-1 credit unless Product/Power issues
   a new signed decision.

## Frozen constraints and producer gates

The correction preserves 300 W sustained, 330 W for 100 ms, 40 A continuous,
45 A peak, 11.4–12.6 V source window, 11.05 V sustained / 11.00 V peak
protected minimums, and the complete hot-path maximum of 10 mOhm. It preserves
`F.Cu / In1.Cu GND / In2.Cu PWR / In3.Cu PROTECTED_12V / In4.Cu GND / B.Cu`,
J1, high-speed corridors, and unrelated macro placement. Ordinary through-vias
only; no single via carries the 40 A path; no global rule relaxation; no passive
sharing; no invented symbols, aliases, footprints, or alternate reference
assignments.

The next producer must return a fresh native schematic/netlist/ERC/DRC and exact
symbol-pad-footprint census before any routing claim. Root owns serialized
integration and fresh Light validation. Resistance, thermal, fuse I²t/SOA,
harness, and fabricated-hardware acceptance remain open gates.

## Evidence and disposition

- `validation-receipts/protected-bus-r2-producer-blocked-20260918/RECEIPT.md`
  and `raw/topology-census.json`: committed at `02bb6e63`; proves the assigned
  source has J5/J6 and F1/F2 only and that no producer candidate exists.
- `validation-receipts/protected-bus-upstream-authority-revision-20260918/AUTHORITY_DECISION.json`:
  binds the R2 source contract, coordinates, layers, and 10 mOhm allocation.
- `validation-receipts/power-input-nine-branch-contract-20260918/NINE_BRANCH_SCHEMATIC_CONTRACT.md`:
  binds exact branch names, protection components, and ownership.
- `validation-receipts/molex-mpa-nine-branch-revision-20260918/MPA_DECISION.md`:
  binds J5/J6/J9 pin mapping, placement, corridors, and no-alternate rule.
- Library brief `high-current-input-connector-reassessment-20260918.md`:
  records the released Molex 5569 six-circuit geometry and the 7 A loaded-circuit
  screen; it does not claim final thermal or hardware qualification.

**Return:** `DONE`. Root should transition this package through normal candidate
and validation handling, then release the corrected source-topology producer.
