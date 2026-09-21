# Macro Placement Authority R3 — source-local nine-branch fuse banks

- **Originating work package:** `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- **Decision ID:** `PISXME-P24-PROTECTED-BUS-MPA-20260921-R3`
- **Authority:** Macro Placement Authority, implementing Product / Power Authority decision `PISXME-P24-PROTOTYPE-POWER-BUS-POWER-AUTHORITY-20260921`
- **Status:** `BINDING_DECISION_FOR_PRODUCER; REQUIRES_PROTOTYPE_VALIDATION`
- **CAD changed by this decision:** no
- **Hardware operated:** no

## Binding decision

The R1 fuse grid at y=26.25/51.25/76.25 and its mandatory long ordered In2
raw lanes are superseded. The sole replacement is three source-local fuse banks,
with one bank associated with each fixed input header. The bank bands move north
by 11.25 mm to y=15/40/65, retaining 28 mm column spacing and the exact branch
identity. This is a physical placement decision, not another route variant.

The source-local geometry is selected because Product / Power Authority allocates
at most 0.65 mOhm hot to each branch's raw PCB positive-plus-return neck. The
prior long inner-layer raw lanes cannot meet that allocation on the released
stackup. The producer must extract the actual cross-section, via construction,
length, and hot resistance; this decision claims no measured pass.

## Fixed anchors and exact component positions

All positions are board coordinates in millimetres. All components are top side,
rotation 0 degrees unless stated otherwise.

| Reference | Position | Disposition |
|---|---:|---|
| J1 | `(150,90,0)` | fixed SXM2 anchor and mapped contact field |
| J5 | `(12,25,0)` | fixed source header; branches B1-B3 |
| J6 | `(12,50,0)` | fixed source header; branches B4-B6 |
| J9 | `(12,75,0)` | fixed source header; branches B7-B9 |
| F1/F2/F3 | `(36,15,0)`, `(64,15,0)`, `(92,15,0)` | J5 bank; B1/B2/B3 |
| F4/F5/F6 | `(36,40,0)`, `(64,40,0)`, `(92,40,0)` | J6 bank; B4/B5/B6 |
| F7/F8/F9 | `(36,65,0)`, `(64,65,0)`, `(92,65,0)` | J9 bank; B7/B8/B9 |
| D1/C3/U1/Q1 | `(108,10,0)`, `(108,29,0)`, `(108,34,0)`, `(111,42,0)` | fixed primary protection cohort |
| U2/Q2/C4/D2 | `(108,62,0)`, `(111,70,0)`, `(108,77,0)`, `(108,96,0)` | fixed non-credited support cohort |
| TP2 | `(114,60,0)` | fixed source-bound probe |

Each fuse bank is the row nearest its source header. The released holder
courtyard screen is 24.25 mm on the relevant envelope, leaving 0.75 mm between
25 mm bank pitches; that gap is a DFM acceptance gate. The top bank envelope is
within the board edge screen, and the bottom bank remains clear of the J7
keepout. The producer shall report the actual released footprint envelope and
mating/service clearance; it may not silently compress the holder or relax
courtyard rules.

## Branch identity and local escape ownership

The electrical contract remains:

- J5/J6/J9 pads 1-3 are positive and pads 4-6 are return.
- Pair pads 1-4, 2-5, and 3-6 per header.
- F1/F4/F7 are branch 1; F2/F5/F8 are branch 2; F3/F6/F9 are branch 3.
- Each fuse is one series `0297015.U` path; no passive sharing or N-1 credit.
- Source window 11.4-12.6 V; 300 W sustained; 330 W for 100 ms; 40 A
  continuous and 45 A peak; complete hot path <=8.50 mOhm.

For each header, the three positive pads route monotonically to the west raw
pads of the three fuses in that header's bank. Use short, ordered F.Cu local
escapes and direct pad entry where clearances permit; no long mandatory In2
raw lane is authorized. The three positive paths must not cross one another or
enter a neighboring fuse courtyard. Use the pad geometry and available copper
width to maximize cross-section; the producer sizes any ordinary through-via
array from the released stackup and returns the extracted positive-plus-return
resistance against the 0.65 mOhm allocation.

Each connector return pad 4-6 escapes into its own local ordinary-through-via
array and reaches the matching ordered In4 return lane/field. Returns never
pass through a fuse pad, a signal corridor, or a shared single neck. The source
locality applies to the return transition as well as the positive branch neck.

Each fuse east pad group remains an independent fused net until entering the
reserved distributed `12V_BRANCH_JOIN` field. No branch identity is collapsed
at the local bank.

## Layer intent and exact corridor reservations

1. **F.Cu source-local corridors:** reserve the three monotonic positive paths
   from each connector to its bank's west fuse pads, plus short connector-return
   pad escapes to their return-via arrays. F.Cu is also permitted for local
   fuse-east pad escapes and protection/control loops. No F.Cu global return
   fill may bridge the branch pads; the R2 zone release remains in force.
2. **In2.Cu raw/fused field:** raw positive is not a mandatory long lane. In2
   is reserved for short local transitions where a via is required and for the
   distributed fused `12V_BRANCH_JOIN` field spanning approximately
   `x=103.5..112.0, y=3.0..77.0`, clipped around exact pads and clearances.
   Fused nets stay separate until that field and use multiple ordinary
   through-via transition columns.
3. **In4.Cu return field:** reserve a distributed `POWER_RETURN_JOIN` field
   over approximately `x=103.5..112.0, y=3.0..77.0`, with distinct branch
   arrivals and ordinary through-via stitching. In1.Cu remains the continuous
   POWER_GND reference/return plane. Positive and return fields remain separate.
4. **Protection:** the J5/J6/J9 fused field feeds U1/Q1 in the fixed primary
   cohort. U2/Q2/D2/C4 remain physically separate and receive no passive
   parallel or N-1 credit. Their disposition cannot be used to shorten or
   merge a branch.
5. **Post-protection:** Q1's protected output uses a distributed ordinary-via
   field beginning at `x>=115` and enters the sole In3.Cu `12V_PROTECTED` field.
   In3 approaches the already mapped J1 12-V contacts from approximately
   `x=116.5..124`; no B.Cu J1 terminal, via-in-pad, unknown contact, or narrow
   F.Cu trunk is authorized.
6. **Protected copper:** preserve J1 high-speed/clock/USB3/Ethernet/storage/
   CM5 copper, validated return structures, board outline, and J7 keepout.
   Only named obsolete power stubs and the replacement source-local power
   corridors may be changed.

## Why this placement is binding

The retained failures (997/383, 1013/364, 679/390, and 1220/391) exercised
R1's exact fuse grid or its immediate corridor variants. Product / Power
Authority identified the governing contradiction: long raw lanes consume more
than the 0.65 mOhm hot branch allocation before the common path is counted.
Moving each entire bank to the source-header band removes that long raw neck
while preserving fixed connectors, the nine-branch contract, the protection
cohort, and the J1 transition. The 24.25 mm holder envelope and 25 mm bank
pitch are explicitly a DFM gate; no cosmetic gap claim is made.

This decision does not authorize another orientation sweep, alternate grid,
common passive bus, global rule relaxation, connector remap, J1 remap, or six-
layer change. If the producer cannot satisfy the 0.65 mOhm branch allocation
with this geometry and released copper/via construction, it must return the
measured contradiction to Product / Power Authority; it may not replay R1.

## Producer handoff

The isolated producer shall begin from Root's exact committed base and implement
only this placement/corridor plan. It shall return:

- exact footprint positions/orientations and branch/pad census;
- local positive/return trace and via geometry per branch;
- fuse-holder courtyard, connector mating, installation and service DFM;
- targeted native DRC/connectivity;
- extracted per-branch hot resistance, current density and thermal evidence;
- complete R3 source-to-J1 resistance and protection/thermal evidence.

The candidate then requires serialized canonical integration and fresh KiCad
Light validation. This authority packet is `REQUIRES_PROTOTYPE_VALIDATION`; it
contains no fabricated measurement or hardware-operating claim.

**AUTHORITATIVE BASELINE DECLARATION:** For
`P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`, the sole local placement is the
source-local three-bank arrangement at y=15/40/65 with fixed J1/J5/J6/J9 and
fixed protection cohort above. Raw branches use ordered short F.Cu local
escapes, fused branches use the distributed In2 join field, returns use
ordered In4 fields, and post-protection uses In3 to mapped J1 contacts. No
alternate placement or same-class route variant is authorized.
