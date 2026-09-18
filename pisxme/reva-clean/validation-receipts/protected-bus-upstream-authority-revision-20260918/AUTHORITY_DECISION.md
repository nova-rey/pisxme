# Protected-bus upstream authority revision

- **Decision ID:** `PISXME-P24-PROTECTED-BUS-UPSTREAM-AUTHORITY-20260918-R2`
- **Package:** `P24-PROTECTED-BUS-UPSTREAM-AUTHORITY-REVISION`
- **Decision state:** `BINDING_DECISION`
- **Authority:** Product / Power Authority and Macro Placement Authority
- **Current reconciliation base:** `34576737e6d9cc1edd0749830f29c9b530b6797c`
- **CAD state:** no canonical CAD changed; no producer candidate emitted
- **HPQ basis:** Issue #6 `resolution-ready`, packet commit `13a9176696176719789572d35f2270e93590de69`

## Decision

HPQ Issue #6 demonstrated that the previous nine-branch R1 placement is
structurally contradictory. R1 is superseded for the local source/fuse
geography and must not be replayed. The selected nine-branch Molex architecture
and the conventional protected common bus remain valid.

The minimum upstream change is to move only the nine fuse-holder placements
north by 11.25 mm, preserve their 28 mm column spacing, and reserve a broad
pre-protection join field instead of the rejected narrow `x=104..106` tie. The
input headers, J1, board outline, package identities, schematic branch contract,
six-layer roles, and validated unrelated macro geography remain fixed.

This decision changes the local power-support macro geography. It does not
change product capability, source ratings, J1 contact assignments, or the
selected connector/fuse architecture.

## Fixed and superseded constraints

| Item | Binding disposition |
|---|---|
| 300 W sustained V100 envelope and 330 W / 100 ms design peak | **FIXED** |
| 40 A continuous / 45 A for 100 ms source contract | **FIXED** |
| 11.4--12.6 V source window; 11.05/11.00 V protected minima | **FIXED** |
| Complete source-to-J1 positive-plus-return hot resistance <=10.0 mOhm | **FIXED** |
| Three Molex `0039300060 / 39-30-0060` headers J5/J6/J9; nine positive/return branches | **FIXED** |
| Littelfuse `0297015.U` in `178.6165.0001` for F1--F9 | **FIXED** |
| Ordinary through-vias; six-layer roles F.Cu/In1 GND/In2 PWR/In3 PROTECTED_12V/In4 GND/B.Cu | **FIXED** |
| J1 `(150,90,0)` and J5/J6/J9 connector identity and service-facing entry edge | **FIXED** |
| R1 fuse rows `(26.25,51.25,76.25)` | **SUPERSEDED_BY_THIS_DECISION** |
| R1 claim of 3 mm row separation | **SUPERSEDED**; the actual 24.25 mm envelope on a 25 mm pitch gives 0.75 mm |
| R1 narrow `x=104..106` pre-protection join ties | **SUPERSEDED** |
| R1 no-change local power geography | **SUPERSEDED** only for F1--F9 and the protected-bus join |
| Any six-loop, precision-current, or equal-contact-current requirement | **NOT GOVERNING**; preserved historical evidence only |

The 0.75 mm inter-row gap is recorded honestly and is a DFM acceptance gate;
it is not described as the previously claimed 3 mm. If the released holder
envelope or the fabrication house requires a larger gap, the producer returns
that measured contradiction to MPA rather than silently compressing the
footprint or relaxing rules.

## Binding placement

All coordinates are board coordinates in millimetres, top side, rotation 0
degrees unless stated otherwise.

| Reference | Position | Disposition |
|---|---:|---|
| J1 | `(150,90,0)` | Fixed SXM2 anchor |
| J5 | `(12,25,0)` | Fixed external input anchor |
| J6 | `(12,50,0)` | Fixed external input anchor |
| J9 | `(12,75,0)` | Fixed external input anchor |
| F1/F2/F3 | `(36,15,0)`, `(64,15,0)`, `(92,15,0)` | Move from R1 row `y=26.25`; branch group J5 |
| F4/F5/F6 | `(36,40,0)`, `(64,40,0)`, `(92,40,0)` | Move from R1 row `y=51.25`; branch group J6 |
| F7/F8/F9 | `(36,65,0)`, `(64,65,0)`, `(92,65,0)` | Move from R1 row `y=76.25`; branch group J9 |
| D1/C3/U1/Q1 | `(108,10,0)`, `(108,29,0)`, `(108,34,0)`, `(111,42,0)` | Fixed R1 protection cohort |
| U2/Q2/C4/D2 | `(108,62,0)`, `(111,70,0)`, `(108,77,0)`, `(108,96,0)` | Fixed R1 support cohort; no unqualified parallel credit |
| TP2 | `(114,60,0)` | Fixed; source-bound probe only |

The three row bands are:

- J5/F1--F3: `y=3.0..27.0`;
- J6/F4--F6: `y=28.0..52.0`;
- J9/F7--F9: `y=53.0..77.0`.

The final band ends at `y=77.0`, ahead of the J7 top courtyard at `y=78.5`
and its mounting-hole clearance envelope. F7/F8 therefore no longer enter the
J7 holes at `(35,82)` and `(68,82)`. The top row leaves at least 2.875 mm from
the board edge using the 24.25 mm holder courtyard screen.

## Binding corridors and layer intent

1. **Raw branch lanes.** Each J5/J6/J9 positive pad uses a short F.Cu escape,
   then an ordinary through-via array to an ordered In2.Cu lane. The three
   group bands above are exclusive ownership regions. No F.Cu route crosses a
   neighboring connector pad, and pads 1--3 remain positive while pads 4--6
   remain dedicated returns.
2. **Fuse fanout.** Each raw lane terminates at its corresponding west fuse
   pad. Each east fuse pad remains a distinct fused lane until entering the
   join field. Fuse courtyards and the J7 keepout are hard obstacles; no route
   or copper clearance is obtained by a global rule change.
3. **Pre-protection positive join.** Replace the R1 `x=104..106` ties with a
   reserved `12V_BRANCH_JOIN` field on In2.Cu spanning `x=103.5..112.0`,
   `y=3.0..77.0`, clipped around the exact protection-package pads and their
   clearances. Local F.Cu pad escapes may stitch into this field. The field is
   a polygon/plane region with parallel ordinary through-via transitions; it
   is not nine narrow tie traces. The producer shall use at least four
   distributed positive transition columns and report actual drill, annulus,
   copper thickness, and current allocation.
4. **Protection.** U1/Q1 remains the selected common protection cohort under
   the existing source contract. U2/Q2 is not credited as passive parallel
   protection unless a new Product/Power decision authorizes it. No current
   equality is inferred from contact count.
5. **Protected positive bus.** Q1's post-protection transition enters In3.Cu
   at `x>=115`. Reserve an In3 field from approximately `(115,3)` through
   `(124,77)`, then the existing J1-side approach `(116.5,83)..(149,98)`;
   use only the already-authorized mapped J1 `12V_PROTECTED` contacts. No
   unknown contact, via-in-pad, or narrow F.Cu trunk is authorized.
6. **Return.** Reserve a matching POWER_RETURN_JOIN field on In4.Cu over
   `x=103.5..112.0`, `y=3.0..77.0`, with ordinary through-via stitching to
   the existing F.Cu POWER_GND/In1.Cu GND/In4.Cu GND hierarchy. The positive
   and return fields remain separate and are not joined through signal copper.
7. **Protected existing copper.** J1 signal/clock/USB3/Ethernet/storage/CM5
   copper, return fields, board outline, and J7 keepout remain protected. The
   old named input/fused/protected stubs are replaceable producer-era copper,
   but only those nets may be edited.

## Electrical, thermal, and DFM gates

The signed source allocations remain binding:

| Allocation | Maximum hot resistance |
|---|---:|
| Source harness/connector loop | 4.0 mOhm |
| Fuse and fault-isolation loop | 2.0 mOhm |
| PCB input positive plus return, including branch/join fields | 2.5 mOhm |
| J1 common-plane/spreading | 1.5 mOhm |
| Complete source-to-J1 positive plus return | 10.0 mOhm |

The producer must extract every branch, fuse/holder, protection device, via
array, plane, return, J1 contact field, and spreading contribution. The old
5.879 mOhm-per-tie result is rejected by construction: the new join is a
distributed plane field and may not be represented by a single 15.2 um tie.
The resistance gate remains an acceptance test; this authority packet does
not claim it passes.

The producer must also report:

- actual stackup copper thickness and equivalent positive/return cross-section;
- current and temperature-rise allocation for every branch neck and common
  field at 40 A continuous and 45 A for 100 ms;
- a distributed ordinary-through-via field at each common positive/return plane
  transition. The producer sizes the count from the actual released fab
  stackup, drill/annulus and via-current model; no single via may carry the
  40 A path and no arbitrary via-count credit is granted;
- fuse-holder courtyard/assembly clearance, connector mating and harness
  service access, annulus and mask checks;
- Q1/TVS/fuse SOA, inrush/shutdown, and thermal margins.

No passive-sharing, fabricated-hardware measurement, production AVL, or
undocumented SXM2 behavior is claimed by this decision. Prototype validation
remains required where the existing product contract says so.

## Producer handoff and stopping rule

The isolated producer may start only from the exact current committed base
specified by Root and may implement this one placement/corridor plan. It must
return a candidate, changed-scope manifest, native targeted DRC/connectivity,
positive/return via and copper census, full hot path extraction, and DFM/
thermal evidence. Root then performs serialized integration and fresh Light
validation.

A candidate failure returns concrete geometry/electrical evidence to this
authority. It does not authorize R1 replay, orientation sweeps, guessed
footprints, global rule relaxation, or another unrestricted route campaign.

**Authority result:** the HPQ-dependent protected-bus package is released to
the producer with this R2 plan. The only remaining gate is implementation and
independent integrated validation against the fixed Phase 24 acceptance rows.
