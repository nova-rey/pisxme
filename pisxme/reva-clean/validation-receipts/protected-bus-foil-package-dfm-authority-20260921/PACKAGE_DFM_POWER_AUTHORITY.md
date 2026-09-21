# PiSXMe C11000 foil Package/DFM/Power authority

- **Package:** `P24-PROTECTED-BUS-MATERIAL-SELECTION`
- **Construction workstream:** `P24-PROTECTED-BUS-CONSTRUCTION-CORRECTION`
- **Authority ID:** `PISXME-P24-FOIL-PACKAGE-DFM-POWER-20260921`
- **Status:** `SIGNED_CONDITIONAL_CONSTRUCTION_AUTHORITY`
- **Scope:** bounded local source-field construction; no CAD edit or canonical integration performed
- **Reviewed producer base:** `4e87f09d`
- **Retained mesh source:** `86568f8b`
- **Producer material candidate:** `1443bfda` / material census base `4e87f09d`

## Binding construction

The following construction is the single authorized foil definition for one
bounded producer attempt. It is a PiSXMe prototype construction requirement;
it is not a claim that a vendor has already qualified this assembly.

| Item | Binding value |
|---|---|
| Conductor | C11000 ETP copper foil/strap, one positive and one return element |
| Bare foil thickness | `1.00 mm nominal`; supplier tolerance must be recorded before fabrication and the finished part must not be below `0.90 mm` |
| Bare foil width | `8.00 mm nominal`, `7.90 mm minimum` finished width |
| Bare foil length | `82.00 mm nominal`, `81.75–82.25 mm` finished length |
| Positive field | `x=99..107 mm`, `y=5..87 mm` in the producer coordinate basis |
| Return field | `x=113..121 mm`, `y=5..87 mm` in the producer coordinate basis |
| Bare positive-to-return separation | `6.00 mm minimum` edge-to-edge after dimensional tolerance and assembly |
| Insulation | Polyimide film on both faces, `0.10 mm nominal` per face; finished coverage must be continuous over all foil faces and edges, with no exposed edge in the installed state |
| Insulation overhang | `>=1.00 mm` beyond every bare foil edge at cut edges, except at defined landing interfaces |
| Landing rows | `y=15, 40, 65, 82 mm` |
| Landing count | Four electrical transitions per polarity; eight total transitions |
| Board land | `2.40 mm` finished copper land with `1.20 mm` finished plated through-hole, subject to native package/fab capability verification |
| Foil landing aperture | `1.30 mm nominal`, `1.20 mm minimum` finished hole in each foil landing, concentric to the board PTH; no exposed foil may bridge adjacent landings |
| Electrical attachment | Copper-compatible plated pin/rivet or equivalent mechanically retained joint through each foil aperture and board PTH, soldered/welded/bonded only by a documented prototype process; adhesive alone is not an electrical connection |
| Mechanical retention | Secondary high-temperature insulating retainer/adhesive permitted only after Package/DFM review; it must not be the sole protection against movement or polarity contact |
| Rail landings | Positive to F.Cu/B.Cu/In2 power mesh; return to In1/In4 return mesh, preserving the existing polarity mapping |
| Field orientation | Positive and return elements remain separate, parallel, and outside signal corridors; no foil fold or edge may enter a connector, mounting-hole, heatsink, or high-speed keepout |

The `2.40 mm`/`1.20 mm` landing dimensions are design assumptions inherited
from the producer model and require native package/fabrication verification.
They are not a vendor qualification claim.

## Finished-edge and clearance contract

The following clearances apply after foil, insulation, attachment, tolerance,
warpage, and assembly are included:

1. Bare positive foil to bare return foil: `>=6.00 mm`.
2. Bare foil or conductive attachment to any unrelated copper, signal route,
   via, pad, mounting hole, connector body, or exposed chassis: `>=1.00 mm`.
3. Finished insulated foil edge to unrelated conductive feature: `>=0.50 mm`,
   with the `1.00 mm` insulation overhang preserved. A larger mechanical
   clearance governs wherever the connector, enclosure, or fab rule requires.
4. No foil or attachment may cross a high-speed differential corridor,
   controlled-impedance reference transition, connector courtyard, mounting
   hole keepout, heatsink envelope, or service-access path.
5. No positive/return foil may be routed over a signal-plane split or sever a
   required return-via path. The local source field must remain a DC power
   structure with an explicit return path.
6. Foil edges shall be rounded or deburred; burrs, sharp corners, exposed
   conductive cut edges, and loose strands are prohibited.
7. The finished insulation shall remain continuous after cutting, attachment,
   rework, and service. A cut edge may not rely on solder mask as its sole
   insulation.

The `6.00 mm` spacing is a PiSXMe design requirement. It is not being claimed
as a universal external safety standard; Package/DFM must still check the
actual operating environment and enclosure.

## Resistance and joint acceptance

The retained R3 model uses `rho=1.724e-5 ohm-mm2/mm` at 20 C and reports:

```text
bare foil model                         0.17671 mOhm
foil plus four modeled bonds             0.33671 mOhm
effective PCB neck                      0.498645 mOhm
required effective PCB neck             0.650000 mOhm
neck margin                              0.151355 mOhm
complete modeled hot path                8.098645 mOhm
required complete hot path               8.500000 mOhm
complete-path margin                     0.401355 mOhm
```

These figures are analytical only. The release acceptance is:

- Every foil polarity path and every landing joint is represented explicitly
  in the four-wire resistance model; no bond, pad, via, or spreading term may
  be hidden in residual.
- Each individual landing joint shall model and then measure, when hardware
  exists, `<=0.040 mOhm` at the declared reference condition and `<=0.060
  mOhm` at the declared hot condition. If the selected joining process cannot
  meet those numbers, Power Authority must reissue the budget before release.
- The complete four-landing network per polarity shall not exceed the
  producer model's `0.33671 mOhm` foil-plus-bond term at the hot design point.
- The integrated effective PCB neck shall be `<=0.650 mOhm` and the complete
  source-to-J1 hot path `<=8.500 mOhm`, with the fixed Q1, protected-bus, J1,
  and residual terms still visible.
- No passive-sharing or N-1 credit is applied until all nine source branches,
  their foil transitions, and their returns are independently extracted and
  qualified.

The `0.040 mOhm` and `0.060 mOhm` joint limits are PiSXMe budget allocations,
not manufacturer data. They are intentionally narrow because the prior
`0.499 mOhm` model has only `0.151 mOhm` neck margin.

## Thermal model assumptions

The analytical model shall be rerun with the exact constructed geometry and
these declared assumptions:

- C11000 resistivity at 20 C: `0.01724 ohm-mm2/m` (or the selected released
  material's tighter manufacturer value).
- Resistance temperature coefficient: `0.00395/K` unless the selected
  material record gives a more conservative value.
- Electrical hot screen: evaluate at `125 C` conductor/joint temperature for
  resistance and loss; this is a design screen, not a claimed operating
  temperature.
- Continuous ambient screen: `40 C` declared ambient, still-air/no-forced-air
  credit unless the mechanical authority supplies a defined airflow.
- Continuous temperature-rise limit: `<=30 C` above declared ambient or the
  lower limit of the selected insulation, attachment, connector, or board
  material.
- Current screen: calculate both the producer's modeled `23.679 A` per foil
  polarity and the no-sharing worst case of `40 A` continuous through one
  foil. Evaluate `45 A` for `100 ms` as a bounded pulse.
- At 40 A, the 8 mm2 foil screen is `5.00 A/mm2`; at 45 A it is `5.625
  A/mm2`. At 125 C, the ideal homogeneous foil is approximately `0.247 mOhm`
  for 82 mm, before joints and spreading.
- Heat paths shall include foil convection/radiation, conduction through each
  landing/joint, the polyimide thermal barrier, and the PCB copper/board path.
  The polyimide film shall not be credited as a heatsink.
- The model shall report foil, joint, pad, via, and nearby PCB temperatures
  separately. "Add more insulation" is not a thermal solution.

The existing producer's `2.960 A/mm2`, `0.1888 W`, and `0.030 K` pulse values
are retained as an informational model under its current split assumptions;
they do not close the no-sharing or continuous thermal requirements.

## SI, return, package, and DFM constraints

- The selected six-layer signal stack remains unchanged. The foil is a local
  DC reinforcement and must not require inner-layer signal routing.
- F.Cu/B.Cu/In2 positive mesh and In1/In4 return mesh remain explicit. The
  authority does not permit a return through signal copper, shields, mounting
  hardware, or an unqualified chassis path.
- SI authority must inspect foil proximity to every high-speed corridor,
  reference transition, return via, and connector field. Any change to plane
  continuity or controlled impedance requires re-analysis.
- The custom foil/landing construction must be represented in the mechanical
  and 3D/assembly review, including film thickness, edge overhang, rivet/pin
  height, solder fillet, bend radius (if any), retainer, service access, and
  cooler/backplate/connector envelopes.
- Native KiCad DRC must be run with the project libraries/rules after the
  construction is represented. The existing candidate's clearance, shorting,
  solder-mask, hole, courtyard, and co-location failures remain open and may
  not be waived by the foil authority.
- DFM must verify the `1.20 mm` finished holes, `2.40 mm` lands, annular ring,
  pad-to-foil overlap, plating, solder-mask opening, paste/assembly process,
  edge clearance, copper burr control, and rework/service sequence.
- No global rule relaxation, synthetic connectivity, or hidden mechanical
  contact is permitted.
- The attachment method must be producible with ordinary prototype tooling or
  have a documented local assembly procedure. Supplier/production AVL
  qualification is outside the prototype gate.

## Prototype-validation dispositions

| Item | Pre-fabrication state | Prototype disposition |
|---|---|---|
| C11000 identity and bulk material properties | `PROVEN` at material-property level by indexed evidence | Verify received material and retain certificate/marking if available |
| Exact foil thickness/width/length tolerance | `UNPROVEN` for selected supplier/part | Measure incoming foil and record; fabrication may proceed only within the bound dimensions |
| Exact 0.10 mm polyimide grade and finished thickness | `UNPROVEN` | Select a released film with manufacturer dielectric/temperature data; measure finished coverage |
| Landing and joint process | `UNPROVEN` PiSXMe prototype process | First article joint coupon or sacrificial sample; four-wire each joint and inspect cross-section/retention |
| Continuous temperature rise | `UNPROVEN` | Current-limited 40 A run with thermocouples at foil center, each joint, pad/via field, PCB neck, and connector; stop at 30 C rise or lower component limit |
| 45 A / 100 ms pulse heating | `ANALYTICAL` only | Capture source/J1 voltage, current waveform, joint/foil temperature and post-pulse inspection |
| Static resistance and voltage drop | `ANALYTICAL` only | Four-wire source-to-J1 and polarity-specific branch measurements at cold and hot conditions |
| Current balance | `UNPROVEN` | Measure all nine branch currents; accept only within the existing `10%` limit with no open-branch credit |
| Insulation integrity and movement | `UNPROVEN` | Visual/continuity inspection before and after thermal/current cycling; verify no exposed edge or polarity contact |
| SI/return impact | `UNPROVEN` | Native route/return review before fab; post-fab coupon or appropriate SI evidence where applicable |
| Fabricated hardware and SXM2 operation | `REQUIRES_PROTOTYPE_VALIDATION` | First-power staged bring-up under external current limiting; no pre-fab pass claim |

## Narrow unresolved fields

No irreducible external blocker remains for generating prototype CAD. The
following are deliberately `UNPROVEN` and must be closed by the bounded
Package/DFM producer or prototype validation:

1. selected supplier and tolerance for the 1.00 mm C11000 foil;
2. exact released 0.10 mm polyimide product/adhesive/edge treatment;
3. qualified pin/rivet/solder/bond process and actual joint resistance;
4. mechanical retention, bend/warpage, service and rework sequence;
5. continuous thermal rise and current sharing in the assembled source field;
6. final native DRC/DFM/3D clearance and SI/return review.

These are prototype engineering evidence gaps, not user-owned product decisions.
They can be carried as explicit `REQUIRES_PROTOTYPE_VALIDATION` dispositions,
provided the analytical limits above are met before fabrication.

## Queue result

- `P24-PROTECTED-BUS-MATERIAL-SELECTION`: **DONE** — this authority artifact
  binds the construction and acceptance limits.
- `P24-PROTECTED-BUS-CONSTRUCTION-CORRECTION`: **READY** for one bounded
  construction-only producer attempt from the current canonical base. The
  producer must implement this exact foil/landing contract, preserve signal
  corridors and J1 mapping, and return fresh Light DRC/connectivity plus the
  resistance/thermal/DFM evidence listed above.
- Existing candidate `1443bfda`: **REJECTED/VALIDATION_FAILED**; its modeled
  resistance is reusable evidence, but its `1555` DRC / `426` unconnected
  result is not a release.
- No unrestricted routing variants, fuse-only substitutions, global rule
  changes, or canonical integration are authorized.

**Signature:** PiSXMe Package / DFM / Product-Power Authority —
`SIGNED_CONDITIONAL_CONSTRUCTION_AUTHORITY` — 2026-09-21
