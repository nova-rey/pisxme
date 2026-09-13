# Phase 24 regulator reference-layout overlay audit

Date: 2026-09-13
Status: `MISMATCH_REQUIRES_MPA_PLACEMENT_CORRIDOR_DECISION`
Scope: read-only geometry and native serialization audit of the selected
integrated acreage candidate. No schematic, PCB, library, rule, or zone was
edited by this audit.

## Exact source and provenance

| Item | Value |
|---|---|
| Git source commit inspected | `2ae2664ffeb21e759099dfc02b0244a002fce503` |
| Board | `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb` |
| Board SHA-256 | `9938f35c69c9f314fe91498a4858022a4b4d75611d89c68a79c48fd09a11856e` |
| Project footprint | `PiSXMe_RevA_Clean.pretty/TPSM63606RDLR_RDL0020.kicad_mod` |
| Footprint SHA-256 | `be0541e2a1de26e301ebdc9e1e42930a0ee16e5e6f43a7b515753d0a7bd7c152` |
| Reference authority | `authority-inventory/primary-docs/power/TPSM63606_SUPPORT_AUTHORITY.md` |
| Overlay record | `PHASE15_TI_LAYOUT_OVERLAY.md` |
| Prior regulator receipt | `PHASE15_REGULATOR_LAYOUT_RECEIPT.md` |
| Geometry artifact | `geometry.json` |
| Geometry artifact SHA-256 | `2567b775d86b13b5c8aee3ed7d112af72c5e1a8e010cb43b7927de0aa3e54868` |
| Geometry reader | host `pcbnew` 10.0.5, read-only load; no DRC or save |

The Phase 15 authority is TI TPSM63606 revision B, SLVSGB4B, pages 31-32,
plus the retained TI EVM guide/layout archive. It requires local VIN and VOUT
bypass, localized top-side PGND return copper, a lower-layer VOUT feed, short
feedback routing, a solid ground plane below the module, PGND thermal vias,
and sufficient copper for the junction-temperature limit. The EVM's 5.85 mm
maximum regulator-to-output-capacitor center distance is a quantitative
reference measurement, not a project hard limit or a dimensioned overlay.

## Current package and layer observations

U3, U4, and U5 all use `TPSM63606RDLR_RDL0020`, are on F.Cu at 0 degrees, and
have 20 pads. The footprint serialization matches the local package authority:
perimeter pads 1-16 and four central 1.58 x 0.50 mm PGND thermal pads 17-20.
The central PGND pad centers are at local y = -1.125, -0.375, 0.375, and
1.125 mm. No footprint/package correction is identified by this audit.

The board declares the six signal layers as F.Cu, In1.Cu (`In1.GND`), In2.Cu
(`In2.PWR`), In3.Cu (`In3.PROTECTED_12V`), In4.Cu (`In4.GND`), and B.Cu. The
serialized board contains global POWER_GND zones on F.Cu, In1.Cu, and In4.Cu.
It contains no local regulator VOUT plane or regulator-specific stackup overlay
record. The project default netclass is 0.20 mm track / 0.20 mm clearance;
the only board-local rule file exception is the JMS XIN/XOUT 0.10 mm rule and
is unrelated to these regulator modules.

## Native geometry measurements

Distances below are footprint-center distances, matching the prior Phase 15
measurement convention. They are evidence of the current candidate's
placement, not claims that a center-distance threshold is itself an acceptance
rule.

| Module / rail | Current component set | Current center-distance range | Overlay disposition |
|---|---|---:|---|
| U3 VIN / `12V_PROTECTED` | C5, C6 | 8.004-8.246 mm | Local placement exists; copper/return closure still requires integrated validation |
| U3 VOUT / `CM5_5V` | C7, C8 | 6.103-7.433 mm | Local placement exists; current local output copper is present |
| U4 VIN / `12V_PROTECTED` | C14, C15 | 147.763-155.724 mm | MISMATCH: support bank is remote from U4 |
| U4 VOUT / `BRIDGE_3V3` | C16, C17, C19 | 118.207-130.188 mm | MISMATCH: output bank is remote from U4 |
| U5 VIN / `12V_PROTECTED` | C23, C24, C25 | 118.431-132.098 mm | MISMATCH: input bank is remote from U5 |
| U5 VOUT / `BRIDGE_1V1` | C26-C29, C34-C41, C44-C47 | 27.459-105.802 mm | MISMATCH: nearest four are remote and the C26-C41 bank is far west |

Current module positions are U3 `(60,165)`, U4 `(225,105)`, and U5
`(235,105)`. The retained Phase 15 overlay record measured a different
candidate, reporting U3/U4/U5 maximum output-bank distances of 7.4/16.3/51.7
mm. Those historical values cannot be transferred to this board: the current
U4/U5 positions and support-bank coordinates differ, and this board's
serialized geometry must be treated as the active evidence.

## Copper and return observations

The read-only native net census in `geometry.json` reports:

- U3 has local `12V_PROTECTED` and `CM5_5V` F.Cu/B.Cu routing. The board-wide
  `CM5_5V` net has 37 segments and 9 vias; this is not by itself proof of
  regulator transient or thermal closure.
- U4 and U5 have zero serialized segments and zero vias on
  `BRIDGE_3V3`/`BRIDGE_1V1`. Their output capacitors therefore have no current
  integrated output feed in this candidate.
- The board has six `12V_PROTECTED` segments and one via. The local source
  escape is at U3; no local U4/U5 input escape is present in the selected board.
- The board has 47 `POWER_GND` segments and 11 vias, plus the global F.Cu/In1.Cu/
  In4.Cu ground zones. No POWER_GND via lies within 4 mm of the center of U3,
  U4, or U5. The one POWER_GND via nearest U5 is at `(247,114)`, outside the
  module thermal-pad field; it is not the four-via central PGND array required
  by the package authority.
- `FB_CM5_5V`, `FB_BRIDGE_3V3`, and `FB_BRIDGE_1V1` each have zero serialized
  tracks and zero vias on this candidate. `RT_BRIDGE_3V3`, `RT_BRIDGE_1V1`,
  `PG_BRIDGE_3V3`, and `PG_BRIDGE_1V1` likewise have no serialized routing.
  This leaves U4/U5 control and feedback closure open. The absence of copper
  is a current-board observation; it does not prove the net contract is wrong.

The current board therefore does not satisfy the TI-derived local placement,
VOUT feed, local PGND return, thermal-via, or control-route overlay evidence for
U4/U5. U3's local placement and partial copper remain useful evidence but do
not close the integrated acceptance row.

## Required authority action

This is a physical placement/corridor mismatch, not evidence that the
TPSM63606 architecture or package is impossible. Macro Placement Authority
must issue one binding local plan before further speculative routing. The plan
must decide the positions/orientations of U3/U4/U5 and their support cohorts,
reserve VIN/VOUT/FB/RT/PG corridors and layer intent, protect the existing U3
copper and high-speed corridors, and place the four ordinary PGND thermal vias
per module. At minimum, the affected support cohorts are:

- U3: C5/C6 VIN, C7/C8 VOUT, C9 feedback, R3/R4/R5/R6 controls;
- U4: C14/C15 VIN, C16/C17/C19 VOUT, C18 feedback, R11/R12/R13/R14 controls;
- U5: C23/C24/C25 VIN, C26-C29/C34-C41/C44-C47 VOUT, and R19/R20/R21/R22
  controls.

The producer must implement that one authority plan in an isolated committed
worker, then run targeted native connectivity/DRC and a fresh KiCad Light
validation. If a structural contradiction appears, return the measured
collision and affected immutable corridor to MPA for one bounded revision.
Do not use this receipt to authorize arbitrary component moves, rule
relaxation, deletion of required capacitors, synthetic connectivity, or another
unbounded route sweep.

## Acceptance disposition

`regulator_reference_overlays` remains `OPEN` on the selected integrated
candidate. This audit provides the missing current-board overlay evidence and
identifies the MPA handoff; it is not a Phase 24 pass, a thermal simulation,
a PDN/load-step result, or fabricated-hardware evidence. Exact capacitor
DC-bias/temperature derating, board-specific thermal response, current
crowding, and transient/impedance measurements remain the documented
`REV_A_EMPIRICAL_RISK` boundary until separately evidenced.
