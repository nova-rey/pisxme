# PiSXMe Phase 24 power-constraint provenance audit

- **Package:** `P24-POWER-CONSTRAINT-PROVENANCE-AUDIT`
- **Base:** `668807f0167f31ab0a3dd9f0764fbea1a574d980`
- **Date:** 2026-09-17
- **Status:** `CANDIDATE_READY_FOR_PRODUCT_POWER_AUTHORITY_REVIEW`
- **CAD/configuration changed:** no
- **Architecture selected:** no; this receipt only audits authority lineage

## Result

The 300 W sustained V100 product envelope is a governing product requirement,
and the cached NVIDIA V100 datasheet supplies an external 300 W maximum-power
fact. Neither source requires six independent 12 V loops, precision current
regulation on every loop, a 6.000--6.400 A per-loop window, or a prescribed
current for each SXM2 power-contact group.

The earliest record of the **six-loop architecture** is the internal Phase 24
candidate `937fac206fb63ad16923f244af15100ee0dfe472`, not an NVIDIA/SXM2
specification, safety law, or user product decision. The later conditional
signoff, HPQ4 signed budget, limiter authority packets, and HPQ #5 packet repeat
and formalize that candidate; they are not independent origins. Those records
therefore cannot give the six-loop implementation a foundational veto by
repetition alone.

A separate earlier Phase 5 calculation does justify refusing to rely on an
unqualified two-branch connector path to carry the complete load. That is a
scoped engineering/safety conclusion about the selected input assembly. It does
not establish six precision-regulated loops or a per-SXM2-contact current
contract.

## Requirement lineage and authority classification

Classes are A: NVIDIA/SXM2 external requirement; B: physics/safety or other
external contract; C: explicit user product requirement; D: valid derived
engineering requirement needed by A--C; E: architecture/implementation choice;
F: historical or agent-created assumption with insufficient provenance.

| ID | Current requirement audited | Earliest located source | Later repetitions (not independent authority) | Class | Authority conclusion |
|---|---|---|---|---|---|
| `PWR-LOOP-001` | Six independent 12 V power loops | `937fac20` (`POWER_ENVELOPE_AUTHORITY_V2.2_CANDIDATE.json`: `proposed_input_architecture.circuits=6`, `dc_power_loops=6`, `return_loops=6`; `branch_policy.topology_note`), an internal candidate | `daaf6d3b` conditional six-loop signoff; `0a97f3e4` HPQ4 contract; `66ea28f4` replacement calculator; `dd2e7eed` no-go | **E** | A topology selected by internal engineering. Total 300/330 W does not determine six loops. No foundational veto until Product/Power Authority independently justifies it. |
| `PWR-LOOP-002` | No passive current-sharing credit between the six loops | Six-loop form first appears at `937fac20` (`branch_policy.passive_sharing_allowed=false`). A narrower two-branch precursor is in `8387a587` `PHASE5_POWER_CALCULATIONS.md`, which says the two-branch envelope must not rely on one branch carrying the full load because of the selected assembly limits. | `daaf6d3b`, `0a97f3e4`, `66ea28f4`, `dd2e7eed` | **E** for the six-loop contract; **D-scoped precursor** for the earlier two-branch safety conclusion | The earlier safety conclusion is reusable for the selected connector/harness until qualified. It does not prove six loops or precision regulation. |
| `PWR-LOOP-003` | Every loop guarantees at least 6.000 A | First exact numeric contract located at `0a97f3e4` (`POWER_BUDGET_CORRECTION.json`: `independent_loop_contract.guaranteed_delivery_floor_a_per_loop=6.0`), derived after the six-loop candidate existed | `66ea28f4`, `1a39f6b2`, `22018346`, `dd2e7eed` | **E** | The corrected budget's own protected-bus calculation requires about 5.408 A sustained and 5.938 A peak per loop at its stated minima; the 6.000 A floor is an implementation allocation/qualification window, not an NVIDIA requirement. |
| `PWR-LOOP-004` | Every loop stays at or below 6.400 A in full operational tolerance | A 6.4 A hard branch screen first appears at `937fac20`, derived from an internal 8 A connector screen times a 0.8 derating factor. The exact `full_tolerance_operational_ceiling_a_per_loop=6.4` is formalized at `0a97f3e4`. | `66ea28f4`, `1a39f6b2`, `22018346`, `dd2e7eed` | **E** | The 6.4 A number is a selected architecture/derating screen. The connector evidence can bound an assembly when applicable, but does not require six branches or this exact per-loop window. |
| `PWR-LOOP-005` | Independent precision current regulation/limiting on every loop | `937fac20` (`branch_policy.topology_note` says each loop is independently current-limited and fault isolated); the first exact controller candidate is `454de823` (`POWER_CURRENT_LIMITER_AUTHORITY.json`, six `MAX17527AATP+T` instances) | `0a97f3e4`, `1a39f6b2`, `4794c361`, `b3edd1fb`, `dd2e7eed`, HPQ #5 | **E** | This is a protection/control architecture chosen to implement the six-loop contract. No NVIDIA/SXM2 source located in the current corpus requires precision branch regulation. |
| `PWR-LOOP-006` | Limiter allocation no greater than 57 mOhm hot | Underlying 57 mOhm part fact first appears with the selected MAX17527A candidate at `454de823` (`ron_max_specified_mohm=57`). The project-level generic hot allocation is first made explicit in `0a97f3e4` (`static_ir_budget` limiter cap 57.0 mOhm). | `66ea28f4`, `da8760ff`, `1a39f6b2`, `dd2e7eed` | **E** for the PiSXMe allocation; **B** only for the cited candidate's component data | A candidate component's specified resistance does not create a system requirement, and it does not prove a complete installed hot path. The allocation has no independent product/SXM2 provenance. |
| `PWR-LOOP-007` | Each SXM2 power-contact group must receive a prescribed current independently | No authoritative source located. The NVIDIA V100 datasheet in `authority-inventory/primary-docs/NVIDIA-Tesla-V100-datasheet.pdf` records 300 W maximum power but no branch/group current. The J1 reverse-engineering/contact corpus maps contacts and the Amphenol record supplies connector/contact facts; neither specifies a PiSXMe group-current allocation. | `0a97f3e4` `branch_path` and `dd2e7eed` six-loop contract refer to loops, not an external J1 group-current requirement | **F** | No foundational requirement has been established. Contact count/field presence is not a current-sharing or per-group regulation specification. Preserve unknown behavior as unknown and require an explicit authority decision before imposing a group-current contract. |

## Independent product and external facts retained

| Fact | Class | Evidence | Scope |
|---|---|---|---|
| V100/SXM2 maximum power consumption is 300 W | B (external product fact) | Cached NVIDIA datasheet, SHA-256 `ca694a4789eae7feb9ce9090f2207cbe82f5da1448922d4855e346680c59d3`, indexed in the private Librarian brief | Total product power fact only; it does not define source voltage, transient, branch allocation, contact-group current, or current-limiter topology. |
| PiSXMe Rev A shall support 300 W sustained and retain 330 W peak allowance | C | User product decision recorded in `PROJECT_INVARIANTS.json` / `PRODUCT_POWER_INVARIANT_PACKET.md` and carried into HPQ4 | Governing product behavior; topology remains an engineering decision constrained by safety and interface evidence. |
| Selected connector/harness limits and protection ratings | A/B | Phase 5 records, Molex/TI/Littelfuse authority records and private Library evidence | Apply to the exact selected assembly and operating conditions; do not extrapolate to six-loop precision control. |

## Disposition for Product/Power Authority

This package makes no replacement architecture decision. It establishes the
following bounded authority correction for review:

1. Keep the 300 W sustained / 330 W bounded-peak product requirements in force.
2. Treat `PWR-LOOP-001` through `PWR-LOOP-006` as implementation-derived
   constraints (`E`) pending the separate Product/Power architecture comparison.
3. Treat `PWR-LOOP-007` as `F/UNPROVEN`; do not infer it from contact count or
   assign current merely to obtain parity.
4. Retain the Phase 5 two-branch no-single-branch-load conclusion only within
   its exact connector/harness/protection scope; it is not evidence for six
   precision loops.
5. Preserve HPQ #5, its calculations, and its issue packet as historical
   engineering evidence. This audit neither admits, closes, nor deletes HPQ
   state, and it does not authorize CAD edits.

The Product/Power Authority must decide whether a simpler prototype power
architecture satisfies the real product, interface, and safety requirements.
Until that decision is made, downstream six-loop limiter work must not be
represented as a foundational necessity merely because its records are signed.

## Evidence boundary and checks

- Search covered current reva-clean source records, commit history for the
  cited artifacts, the private Library power/SXM2 briefs and source index, and
  the authority inventory. No CAD file was read or changed by this package.
- Git ancestry verified the origin order: `8387a587` Phase 5 two-branch
  calculation; `937fac20` first six-loop candidate; `454de823` first exact
  limiter candidate/57 mOhm candidate datum; `0a97f3e4` first exact
  6.000--6.400 A and generic 57 mOhm contract; later records repeat or reject
  those assumptions.
- “No source located” means no source in the bounded corpus and history listed
  above; it is not a claim that no future external document could exist.
- No architecture, CAD, rules, configuration, HPQ issue, or queue state was
  changed here.
