# Protected-bus R3 Macro Placement Authority revision

- **Decision ID:** `PISXME-P24-PROTOTYPE-POWER-BUS-MPA-R3-20260921-R1`
- **Originating work package:** `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- **Base:** `627ec337a28ce0c732df7744dc3ba360414464db`
- **Producer evidence:** `894fa433` exposed the omitted F3-F9 geometry
- **State:** `BINDING_DECISION`
- **CAD changed by this decision:** no

## Bounded correction

The Product/Power R3 contract requires three source headers (`J5`, `J6`,
`J9`) and nine independently fused positive/return branches (`F1`–`F9`).
The preceding R3 corridor record defined only `J5/J6` and `F1/F2`; that
record is superseded only for the source-entry placement scope. The signed
nine-branch contract and the existing nine-branch MPA record remain the
architecture authority. No branch, connector, protection topology, J1 map,
or product requirement is changed.

## Fixed anchors

All are top-side, zero degrees:

| Reference | Position | Status |
|---|---:|---|
| `J1` | `(150.00, 90.00)` | fixed SXM2 anchor |
| `J5` | `(12.00, 25.00)` | fixed source header |
| `J6` | `(12.00, 50.00)` | fixed source header |
| `J9` | `(12.00, 75.00)` | fixed source header |

The board outline, six-layer stack, validated signal/timing corridors,
connector geography, J1 pad/net mapping, and existing return hierarchy remain
fixed. `J7/J8` remain reserved for their existing functions.

## Binding fuse and protection placement

All references are top-side, zero degrees.

| Reference | Position | Branch ownership |
|---|---:|---|
| `F1` | `(36.00, 26.25)` | `J5.1/J5.4` |
| `F2` | `(64.00, 26.25)` | `J5.2/J5.5` |
| `F3` | `(92.00, 26.25)` | `J5.3/J5.6` |
| `F4` | `(36.00, 51.25)` | `J6.1/J6.4` |
| `F5` | `(64.00, 51.25)` | `J6.2/J6.5` |
| `F6` | `(92.00, 51.25)` | `J6.3/J6.6` |
| `F7` | `(36.00, 76.25)` | `J9.1/J9.4` |
| `F8` | `(64.00, 76.25)` | `J9.2/J9.5` |
| `F9` | `(92.00, 76.25)` | `J9.3/J9.6` |

Fuse pads 1–4 are the raw branch side; pads 5–8 are the fused branch side.
The three 28 mm fuse columns and 25 mm row spacing are the sole local fuse
grid. No fuse courtyard may overlap a connector, neighboring fuse, return
via field, or unrelated component.

The common protection/support cohort is fixed as follows:

| Reference | Position | Role |
|---|---:|---|
| `D1` | `(108.00, 10.00)` | Branch/common TVS support |
| `C3` | `(108.00, 29.00)` | VCAP support |
| `U1` | `(108.00, 34.00)` | primary LM74700 stage |
| `Q1` | `(111.00, 42.00)` | primary pass FET; protected output faces J1 |
| `U2` | `(108.00, 62.00)` | retained physical cohort; no parallel-stage credit |
| `Q2` | `(111.00, 70.00)` | retained physical cohort; no parallel-stage credit |
| `C4` | `(108.00, 77.00)` | retained physical cohort; no parallel-stage credit |
| `D2` | `(108.00, 96.00)` | retained physical cohort; no parallel-stage credit |
| `TP2` | `(114.00, 60.00)` | probe only after its net is authority-bound |

`U2/Q2/D2/C4` do not receive passive-sharing, N-1, or second-common-stage
credit. Any DNP/removal or schematic reassignment remains a separate source
and Product/Power authority action; this placement revision does not decide it.

## Branch corridors and layer ownership

- `J5/J6/J9` positive pads escape briefly on F.Cu, then use ordinary
  through-via arrays to ordered `In2.Cu` raw lanes.
- Branches are ordered by header row and contact number: `J5.1-.3` to
  `F1-F3`, `J6.1-.3` to `F4-F6`, and `J9.1-.3` to `F7-F9`.
- Fused outputs remain nine distinct ordered `In2.Cu` lanes to the
  pre-protection `12V_BRANCH_JOIN` region at approximately `x=104..106`.
- Returns from pads 4–6 of each header use distinct ordinary through-vias and
  ordered `In4.Cu` lanes to a broad `POWER_RETURN_JOIN` at `x>=104`.
- F.Cu is limited to pad escapes, local protection/control loops, and probe
  access. No F.Cu star fanout or long raw/fused trunk is permitted.
- The primary common stage is the `U1/Q1/D1/C3` cohort. Q1 protected output
  transitions through a parallel ordinary-via field at `x>=115` to `In3.Cu`.
- `In3.Cu` is the sole post-protection `12V_PROTECTED` plane. It approaches
  the mapped J1 power field from approximately `x=116.5..124`, then uses an
  outside-SMD transition ladder and F.Cu fanout to mapped contacts only.
- No B.Cu terminal may terminate at J1. No via-in-pad, unknown-contact
  assignment, or single-via high-current path is allowed.
- Preserve J1 signal/high-speed copper, CM5 timing corridors near
  `y=76/80/82`, USB3/Ethernet/storage corridors, existing GND zones, and
  unrelated footprints.

## Contract and implementation gate

The producer must preserve the R3 contract: 11.4–12.6 V source, 300 W
sustained, 330 W/100 ms peak, 40 A continuous, 45 A/100 ms, nine branch
pairs, no passive-sharing credit, and complete hot path `<=8.50 mOhm`.

The producer must assert all nine branch/pad/fuse identities, return native
connectivity and targeted DRC, extract every positive/return branch and
transition-via path, and provide current/thermal/resistance evidence. This is
an isolated producer decision only; it does not authorize canonical
integration or close validation.

**Authoritative baseline declaration:** The sole current source-placement
baseline is the fixed `J1/J5/J6/J9` anchor set, the 3x3 `F1-F9` grid above,
the fixed protection cohort, ordered `In2.Cu` positive lanes, ordered
`In4.Cu` return lanes, and post-protection `In3.Cu` transition at `x>=115`.
The earlier two-header/F1-F2 R3 placement is superseded for this scope.
