# PiSXMe Rev A prototype power architecture authority decision

- **Package:** `P24-POWER-ARCHITECTURE-AUTHORITY-DECISION`
- **Decision ID:** `PISXME-P24-POWER-ARCH-20260917`, revision `1.0`
- **Assigned base:** `cb066de9` (provenance-audit dispatch base)
- **Decision review state:** current `reva-clean` HEAD `0dba84d3`; no CAD files were changed
- **Evidence:** provenance audit `cb066de9`; SXM2 authority audit `1056ba6c`; carrier sanity Library brief `c882dfe3`; current foundational contract `c06876d2`
- **Assurance level:** PiSXMe Rev A is a prototype/open-hardware carrier. This decision contains no fabricated-hardware measurement or production-qualification claim.
- **Signature:** **SIGNED_SELECTED_PROTOTYPE_ARCHITECTURE — Product / Power Authority — 2026-09-17**

## Binding decision

Select **Architecture B with the ordinary protection refinement described as C**:

> An adequately rated external 12-V input assembly (one input or multiple separately protected and independently qualified input paths as the mechanical design requires) feeds an ordinary protected common/distributed 12-V V100 power plane. Use source/input fuse or equivalent fault isolation, reverse-polarity or ideal-diode protection, TVS/over-voltage and under-voltage policy, bounded inrush/shutdown behavior, and optional current sensing. Do not require precision current regulation or equal-current control for each SXM2 contact group. Do not claim passive current sharing until the exact parallel input assembly is qualified.

This is the minimum architecture that directly addresses the governing product requirements and the safety/physics checks while preserving a practical prototype path. It does not copy any public carrier's expressive CAD or placement.

The architecture preserves the **300 W sustained V100 product requirement** and the existing **330 W bounded design-peak allowance**. The source, connector/harness, protection, copper, return, thermal and drop budgets remain required closure work. The previous 40 A continuous / 45 A bounded-peak source screen may be retained as a conservative starting budget for the replacement source contract; it is a Class-D engineering screen, not a six-loop product invariant and not a claim that the installed assembly is qualified.

The selected architecture distributes the mapped 12-V and GND contacts as a common low-impedance plane/field. Contact multiplicity is used for current distribution only after the exact contact, copper and thermal conditions are checked. Unknown SXM2 contacts remain unknown/no-connect unless a separate authority record establishes them. Undocumented standalone SXM2 auxiliary/sequence behavior remains **`REQUIRES PROTOTYPE VALIDATION`**.

## Why the six-loop precision architecture is not governing

The bounded provenance audit found the six-loop, no-sharing, 6.000–6.400 A, precision-limiter and 57 mOhm requirements first in internal PiSXMe implementation records. The NVIDIA V100 material establishes a 300 W maximum-power fact and the NVLink/SXM2 product identity; it does not establish six input loops, per-group current, precision regulation, or the stated limiter allocation. The Amphenol record establishes connector geometry/rating under its conditions, not a six-loop current contract. The public carrier corpus shows common high-capacity 12-V entry/distribution and ordinary protection; it contains no independent six-loop mandate.

Repeating an internal assumption in later signed budgets, limiter decisions, or HPQ packets does not create a new authority source. The prior two-branch caution remains valid only as a scoped safety observation: an unqualified small connector/harness assembly must not be credited with carrying the full product load. It does not imply six precision-regulated SXM2 branches.

## Architecture comparison

| Candidate | Governing requirement satisfied | Complexity / area | Loss / heat | Failure and test behavior | Evidence and decision |
|---|---|---|---|---|---|
| **A — six independent precision loops** | Satisfies the old internal six-loop contract, whose premise is E/F rather than A–D | Six limiter/control paths, shunts/FETs, fault aggregation, source nets and return corridors; highest routing and DFM burden | Repeated limiter/shunt/FET loss and thermal hotspots; complete installed hot path remains unproven | Many coordination and fault states; production calibration/fixture demands are inappropriate as a prototype prerequisite | Retained as historical evidence only; **SUPERSEDED as governing Rev A architecture** |
| **B — conventional protected/distributed 12 V** | Directly supports the 300 W sustained / 330 W bounded peak objective when the exact source, connector, copper, protection and thermal budgets close | Lowest component and routing burden; uses the existing 12-V contact field and ordinary protection | One protected bus and a bounded source/drop budget; no duplicated precision limiter loss | Simple first-power measurements and fault checks; unknown V100 sequence is explicitly a prototype validation item | **Selected**; conventional high-capacity V100 carrier practice supports the architecture at a high level |
| **C — protected input paths into one common bus** | Same product objective, while allowing separate connector fuses/ORing/sense where mechanical input assembly requires it | Slightly more parts than B but far less than A; boundaries follow actual input assemblies | Each entry path is independently rated/protected; no equal-current credit without qualification | Fault isolation and current observation are straightforward; exact parallel-path behavior is a source-contract task | **Selected refinement of B**, only where the chosen input assembly needs it; it is not six-loop precision control |

Benchoff's public SXM2-to-PCIe reference uses two 2x3 PCIe power headers and direct high-current delivery; the broader indexed carrier set likewise shows ordinary high-capacity 12-V entry/distribution. These are sanity-check references, not NVIDIA approval or permission to copy CAD. Their value is architectural: they make the six precision paths an implementation choice requiring a PiSXMe-specific reason, not a default.

## Real requirements and prototype assurance

| Requirement | Binding status | Closure evidence still required |
|---|---|---|
| 300 W sustained V100 operation | Product requirement plus NVIDIA 300 W product fact | Source/bus budget, voltage drop, copper/via rise, connector/harness rating, protection and thermal closure |
| 330 W bounded peak allowance | Retained product design allowance | Peak/transient source and protection budget with stated duration and margin |
| Safe input and distribution | Physics/safety and component contracts | Exact source, connectors, conductors/crimps, fuse/TVS/reverse/inrush policy, return path and thermal calculations |
| Required rails and logic/interface behavior | External component/interface contracts where documented | Schematic/net/sequence review; unsupported standalone SXM2 auxiliary behavior is `REQUIRES PROTOTYPE VALIDATION` |
| First power and thermal behavior | Prototype validation | Defined current-limited bring-up, voltage/temperature/current measurements, shutdown checks and stop limits after fabrication |
| Production guarantees, lifetime calibration and population statistics | Not a prerequisite for Rev A prototype fabrication | May remain a later release concern; no production claim is made here |

## Corrected six-loop constraint ledger

`HARD` means it has A–D authority and may constrain architecture. `SOFT` means a useful engineering preference or bounded implementation screen that may yield to a safer equivalent. `SUPERSEDED` means the old six-loop contract no longer governs this Rev A decision. `UNPROVEN` means evidence is insufficient and it has no foundational veto.

| ID | Constraint | Earliest authority | Corrected status | Reason |
|---|---|---|---|---|
| `PWR-LOOP-001` | Six independent 12-V loops | Internal candidate `937fac20` | **SUPERSEDED** | Architecture choice; no NVIDIA, safety or user requirement establishes six loops |
| `PWR-LOOP-002` | No passive sharing between the six loops | Internal six-loop candidate `937fac20`; scoped Phase-5 two-branch caution is separate | **SUPERSEDED** as six-loop contract; **HARD** only for any exact parallel input assembly until qualified | Preserve safety against unqualified input-path sharing without preserving six regulators |
| `PWR-LOOP-003` | ≥6.000 A per loop | Downstream HPQ4 budget `0a97f3e4` | **SUPERSEDED** | Derived from the abandoned loop allocation, not the V100 contract |
| `PWR-LOOP-004` | ≤6.400 A per loop | Internal branch screen `937fac20` | **SUPERSEDED** | Internal derating screen, not an SXM2 requirement |
| `PWR-LOOP-005` | Precision current regulation/limiting on every loop | Internal candidate/limiter lineage `937fac20` / `454de823` | **SUPERSEDED** | Protection may be ordinary and system-level; precision equalization is unjustified |
| `PWR-LOOP-006` | ≤57 mOhm hot limiter allocation | Candidate limiter fact `454de823`, later budget `0a97f3e4` | **SUPERSEDED** | Candidate loss allocation cannot become a system architecture requirement |
| `PWR-LOOP-007` | Prescribed current independently through each SXM2 power-contact group | No authoritative origin found | **UNPROVEN** | Contact map and multiplicity do not establish group current; preserve unknowns |
| `PWR-BUS-001` | Common protected 12-V bus must carry the declared product envelope with margin | Product requirement + physics/safety + component contracts | **HARD** | Replacement source/bus contract must close voltage, current, fault and thermal limits |
| `PWR-BUS-002` | No passive sharing credit across parallel external input paths without exact qualification | Derived safety requirement | **HARD** | Applies only if multiple input paths are selected; each path must be rated/protected |
| `PWR-BUS-003` | Undocumented standalone SXM2 sequencing/auxiliary behavior | No complete public contract | **UNPROVEN / REQUIRES PROTOTYPE VALIDATION** | Do not fabricate a sequence; define first-power checks |

## HPQ #5 disposition

HPQ Issue #5 and its no-go calculations remain retained historical engineering evidence. Its original six-loop limiter problem is **reframed and superseded** by this authority decision; it is no longer a governing dependency for Rev A source architecture, exact nFET selection, or prototype fabrication. Do not continue limiter-family searches, precision-comparator design, current-servo qualification, supplier-assurance work, or six-loop production qualification under that issue.

The issue must remain auditable and must not be deleted. The queue should remove `hpq:nova-rey/codex-config-backup#5` from the superseded limiter subtree, record `SUPERSEDED_BY PISXME-P24-POWER-ARCH-20260917`, and retain the issue URL/receipt as historical evidence. A future HPQ resolution must not resurrect the six-loop contract without a new A–D authority source.

## Replacement queue packages

Root should create/activate these coherent packages, preserving the existing queue's package history:

1. `P24-PROTOTYPE-SOURCE-BUS-CONTRACT` — **READY after this decision**. Bind exact source voltage/tolerance, continuous/peak input capability, input connector/harness/crimp assembly, common bus, ordinary protection, return strategy, drop/thermal budgets and first-power limits. No precision six-loop requirement; no CAD edits.
2. `P24-PROTOTYPE-POWER-BUS-PRODUCER` — **WAITING on `package:P24-PROTOTYPE-SOURCE-BUS-CONTRACT`**. Produce the minimum schematic/PCB/net corrections for the selected protected bus in one isolated CAD worker, respecting current anchors/corridors and current J1 contract. Return candidate only.
3. `P24-PROTOTYPE-POWER-BUS-INTEGRATION-VALIDATION` — **WAITING on producer candidate**. Serialize integration and run fresh KiCad Light ERC/DRC/connectivity, power/return/drop extraction, and focused DFM/thermal checks at the exact integrated SHA.
4. `P24-V100-PROTOTYPE-FIRST-POWER-CONTRACT` — **READY in parallel**. Define current-limited bring-up, rails/enables/reset observations, voltage/current/temperature measurements, stop limits and explicit empirical-risk records. No claim of fabricated-hardware success.

Existing six-loop producer/qualification packages should be marked `SUPERSEDED_BY` this decision rather than silently left as HPQ dependencies. Independent Phase 24 storage, SI, mechanics, firmware-provenance and validation work remains in scope.

## Validation and limits

- Read and reconciled the provenance audit, NVIDIA/SXM2 audit, private Library carrier brief, foundational invariant contract and retained limiter no-go.
- Compared architecture classes without copying reference CAD or restricted bytes.
- No schematic, PCB, footprint, rule, configuration, or external Library source was changed.
- This authority record is a design-validation decision for a prototype. It is not a fabricated-hardware measurement, vendor approval, production release, or claim that undocumented SXM2 behavior has passed.
