# PiSXMe Phase 24 completion → Phase 25 acreage freeze

Status: **APPROVED — EXECUTION NOT STARTED**

Approved by Rey on 2026-09-12, incorporating the execution clarifications below. The latest instruction authorizes saving this document only: **do not begin campaign work yet**. Commissioning, baseline reproduction, repairs, validation, commits, pushes, and tagging await a subsequent instruction to start. This approval does not resume the legacy whole-product goal.

## 1. Objective, authority, and verified starting state

Complete the selected integrated acreage design, validate every applicable Phase 24 requirement, perform the exact Phase 25 freeze, and end the campaign. Do not begin Phase 26, compression, miniaturization, packing experiments, edge moves, or final-size optimization.

This plan preserves the applicable acceptance requirements of `PiSXMe_RevA_Clean_Rebuild_Plan.md`, reconciled against later approved architecture and current Root Foreman instructions. It supersedes the legacy handoff's prohibition on Phase 25 only after Phase 24 passes. It does not revive obsolete SATA-only/B-key architecture, single-writer orchestration, or cross-machine shared-workload experiments.

### Planning-time observations

These are the observations from the approved planning turn, not new execution validation:

- Local `reva-clean` and live `origin/reva-clean` resolved to succession commit `d0ef22b6076c5ceb43cba5024e4b27f192ec8b27`.
- Design checkpoint `772b342c3107340abcfcc381ac83031d90f8035d` is an ancestor. The intervening changes contain handoff documentation and bible entries only.
- Git status was clean. This establishes checkout state, not archive completeness or general host cleanliness.
- `origin` is public `nova-rey/pisxme`; `private` is private `nova-rey/pisxme-private`. The handoff's repository-name prose is incorrect.
- Private `reva-clean` resolved to `aca13b100c1b4cc59d8f6345d13a73db0d1af700`, an ancestor of the succession tip. Neither inspected remote advertised `ACREAGE_REFERENCE_VALIDATED`.
- Publication policy explicitly selected by Rey: **private-only campaign pushes and tagging**. Leave public origin unchanged; do not push to `main`.

At execution start, refresh refs and checkout state without resetting over newer work. Inspect any new delta before proceeding.

### Selected candidate lineage

Use `pisxme/reva-clean/PiSXMe_RevA_Clean.kicad_sch` and `pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`.

Distinguish four states in every receipt:

1. **Baseline:** unchanged succession source and selected repair PCB.
2. **Producer candidate:** isolated, scoped changes from a recorded committed base.
3. **Integration candidate:** Root's serialized combination of accepted changes.
4. **Validation result:** evidence tied to one integration SHA and its complete artifact identities.

Retain this PCB filename throughout the campaign. Historical boards remain evidence, not interchangeable current targets. The selected manifest must name the schematic and all children, PCB, project, rules, libraries, models, source commit, launcher identity, and toolchain/image digest.

### Verify storage authority once

Planning inspection found Path A selected: CM5 USB → HD3SS6126 → TUSB9261 SATA / JMS583 NVMe → HD3SS3412 → shared M-key socket. SATA/NVMe are operating modes; Path A/B are alternative implementations.

At execution start, record exact Git revisions and file hashes for the existing decisions, including:

- `pisxme/reva-clean/PHASE24_DUAL_MODE_STORAGE_PIN_MATRIX.md`.
- `pisxme/reva-clean/PHASE24_RTL9210B_PARALLEL_COMPARISON_V1560.md`.
- The existing `authority-inventory/rtl9210b/RTL9210B_PATHB_AUTHORITY.md` at its actual repository location.
- `pisxme/reva-clean/PHASE24_RTL9210B_QUALIFICATION.md`, including its live override.

If the records agree, explicitly dispose handoff area 5, Path-B production integration, as **out of scope: unpromoted alternative; isolated evidence retained**. Do not reopen architecture selection or develop both alternatives. If the records actually conflict, report the precise conflict and pause only dependent storage-selection work; do not silently choose a convenient source.

Preserve SWAP_ETH_STORAGE, CM5/V100/SXM2/connector anchors, six-layer roles, ordinary through-vias, accepted PCIe/USB3/Ethernet topology, U11/support geography, and RTL orientation. Escalate only demonstrated contradictions to the relevant authority.

### Retained evidence and archive

The named final validator exists at `/home/nyx/eda-workspaces/validation-phase24-successor-freeze-validation-20260912T153259Z`. It retains ERC/DRC reports and logs, native XML, netlist log, live-contract JSON, and a source/image receipt. Logs report **355 ERC findings and 440 DRC violations / 265 unconnected items**. Complete historical commands, per-command return codes, and rule-loading provenance were not established by those files.

Baseline ERC findings remain 299 electrical warnings (121 endpoint-off-grid, 126 isolated-pin-label, 30 same-local/global-label, 22 multiple-net-name) plus 53 library-symbol and 3 footprint-link findings. No finding is waived merely as environment-related. The selected PCB's reported absence of a shorting-items class does not excuse its two inherited crossings or prove connectivity.

The succession archive exists at `/home/nyx/PiSXMe-succession-archive-20260912`:

| Artifact | SHA-256 |
|---|---|
| `untracked-files.tar` | `99aa058e6795bb6e41dd904aedb104bddc9e84a030c058fd3a2317e0202bf11b` |
| `tracked-worktree.patch` | `aac6232db24e9574ed3a4bf0e225d22b0fd00480e9b71fd5fd77689c319040c1` |

The tar has 107,259 entries; the patch affects 91 files. Unique uncommitted geometry includes HD3SS3412/HD3SS6126 pad-position changes and TUSB9261 pad rotations. Their intended approval status is unproven. No separate succession manifest was found in the bounded inspection.

Preserve the archive. Assess these identified deltas only where they affect authority or correctness, against actual package authority and selected geometry. Import an individual change only after that assessment. Do not restore the archive wholesale, delete it, claim completeness, or reconstruct the entire experimental history.

## 2. Bounded commissioning and effective validation context

Installed Root instructions, registry, Supervisor, Librarian, Unblocker, Macro Placement Authority, specialist definitions, and `pisxme-eda-workers` skill were inspected during planning. Reuse functioning infrastructure.

| Capability | Planning evidence | Execution action |
|---|---|---|
| Agent capacity | Config specifies 24 subordinate threads; session advertises 25 total slots. Two Root-dispatched research roles worked. | Record configured, advertised, and observed capacity separately. Do not claim 24 load-verified slots. |
| Configuration reload | App-server started at 08:34; config modification time was 11:08. | Do not infer reload from a new chat or restart the shared server. |
| Nesting | No Supervisor→contractor runtime test performed. | Run one harmless read-only nesting probe. |
| Models | Relevant inspected role files contain no model override; config names `gpt-6-astra`. | Record actual inheritance/model/effort metadata where exposed; preserve deliberately selected role models. |
| CAD tooling | Launcher and Light/SKiDL/Heavy images exist; no Docker containers were running. | Reuse them; no rebuild, upgrade, or replacement orchestrator. |

The nesting probe asks a Supervisor to assign one contractor a read-only hash calculation. Record parent/child IDs, supported depth, completion, and available model metadata. If nested delegation is unavailable, Supervisor owns its work package while Root launches requested contractors. Do not claim nesting occurred. Do not bypass runtime restrictions or restart the shared app-server.

Pin Light to `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`, matching the retained validator receipt and installed image. Capture native `kicad-cli version`; the qualified target is 10.0.6. The launcher resolves tags, so enforce the pinned identity before and after each run and reject a mismatch.

### First execution stage: untouched baseline, then rule binding

Reproduce the untouched selected baseline **once** in fresh Light workers before repairs. Use succession source unless inspection establishes a newer authoritative delta requiring reconciliation. Run full native ERC/DRC, fresh XML export, hierarchy, and existing parity checks. Compare with retained checkpoint outputs and distinguish source, library, project/rules, version, and execution-environment differences.

The selected PCB has no matching `.kicad_pro` or `.kicad_dru`; the fine-escape rule resides beside another PCB. After the untouched replay, bind the selected PCB to its correct explicit project, libraries, and approved rules as a separately recorded context correction.

**Prove effective native rule application, not file presence.** Use bounded disposable native-checker probes inside the authorized U11/Y10 escape window and outside it. Demonstrate that permitted local geometry is accepted, below-limit geometry is detected, normal/net-class constraints apply outside the window, and genuine shorts/manufacturing violations remain detected. Record rule attribution in raw checker outputs. Reject a net-name-only global relaxation.

Report context corrections separately from physical design repairs. Neither authorizes hiding shorts, opens, manufacturing defects, or required circuitry. Once baseline, nesting, targeted archive, and tool-context checks are complete, move into substantive source and copper repair; do not continue commissioning indefinitely.

### Existing worker interface and resource policy

Use `/home/nyx/pisxme-eda-workers/scripts/pisxme-worker`:

```sh
pisxme-worker prepare /home/nyx/PiSXMe BASE_SHA WORKSTREAM
pisxme-worker start kicad-light WORKSTREAM /home/nyx/eda-workspaces/WORKSTREAM 1 1g -- COMMAND...
pisxme-worker validate /home/nyx/PiSXMe CANDIDATE_SHA WORKSTREAM COMMAND...
pisxme-worker status WORKSTREAM
pisxme-worker cleanup WORKSTREAM
pisxme-worker release WORKSTREAM
```

`pisxme-worker` above denotes the absolute launcher path, not an assumed PATH installation. Read the installed skill/interface before allocating or releasing. Producers start from committed refs; validators use fresh detached read-only project mounts. Preserve candidates, outputs, and receipts before release. SKiDL is used for circuit generation where its ownership/parity contract is qualified; native authored islands are not casually regenerated. Heavy requires a demonstrated GUI need.

Planning measured 3,912 MiB total RAM, approximately 2,501 MiB available, with swap already used. Start with **one active CAD container**, 1 CPU/1 GiB/256 PIDs, and reserve at least 1 GiB available host headroom. Measure before admission. Fresh validation receives the CAD slot ahead of the next producer job. Research and host-side analysis continue concurrently.

## 3. Adaptive concurrent ownership and serialized integration

Four concurrent subordinate agents and sixteen reusable sessions are **initial operating budgets, not completion barriers**. Increase useful parallelism within actual supported runtime limits when independent runnable work would otherwise wait and measured host resources permit. Do not spawn to fill slots. Count managers and nested children; reserve room for contractors rather than filling capacity with waiting Supervisors. Agent and CAD-process concurrency are separate budgets, both with local overhead. Never change role models silently to schedule work.

Root owns the goal, integration, resource admission, and one compact `PHASE24_CAMPAIGN.json` record. It contains acceptance rows, authorities, owners/session/job IDs, base/candidate SHAs, edit boundaries, dependencies, start/end state, waiting reasons, evidence, and next actions. Avoid redundant pointer documents and status-only commit chains.

| Workstream | Accountable owner and edit boundary | Dependencies |
|---|---|---|
| A. Source/ERC/export | Source Supervisor and source KiCad contractor. One root-sheet writer; child tasks partitioned by file, not warning class. Own hierarchy/generator contracts and export hygiene. | Starts with B/C/F after baseline capture. Storage electrical changes require B's contract. |
| B. Integrated storage | Storage Supervisor and storage KiCad contractor. U11/Y10/support, U12–U14 selectors, TUSB9261, J3, selected SATA/NVMe channels, local supply branches. | Analysis starts early; critical footprint verification precedes geometry-dependent repairs. Local branches use C's agreed feed endpoints. |
| C. Power/returns/thermal | PI specialist directs a KiCad contractor; thermal specialist supplies bounded analysis. Own input/protection, regulators, SXM2 distribution, global rail/GND zones and stitching. | Starts with A/B/F. Storage pad-field copper stays B-owned. |
| D. Residual board repair | Root dispatches general KiCad contractor for residual net/region sets. C/D may reuse the contractor sequentially. | Classify early; exclude B/C scope before edits and obey channel/rule constraints. |
| E. Footprints/DFM/mechanics | Footprint specialist owns library recommendations/generator consistency; DFM specialist owns mechanical/assembly review. Corrections go through region writers. | Critical packages/archive deltas start early; final review requires integrated geometry. |
| F. SI/reference/readiness | Librarian supplies private briefs; SI/PCIe specialists assess channels/references; one hardware auditor performs final hostile review. | Discovery starts early; final conclusions require integrated geometry and power results. |

Initial simultaneous assignments: Source Supervisor, Storage Supervisor, PI specialist, and Librarian. Dispatch source/storage contractors and footprint/SI reviews as briefs and dependencies permit, adjusting the initial agent budget when useful. Queue CAD operations separately. Supervisors retain work-package ownership even under Root-mediated dispatch.

### Shared-file and copper control

- Root owns selected `.pro/.dru`, manifests, and integration.
- Source Supervisor owns `phase3_scaffold.py` changes. Its old generator writes root and all ten children; do not run it over current authored sheets.
- One library writer owns `phase24_generate_dual_mode_storage_libraries.py` and generated assets. Do not overwrite later footprint refinements by casual regeneration.
- Actual symbol resolution uses `PiSXMe_RevA_Clean_complete.kicad_sym` and `Storage_DualMode.kicad_sym`; preserve explicit project-local resolution.
- Assign physical edits by footprint/UUID, net set, and region. C owns global zones even where they cross another region. Agree local storage rail/return handoffs before either writer edits boundary copper.
- Workers return base SHA, candidate commit/patch, changed scope, tests, artifacts, and remaining findings. Root rebases overlapping candidates against the latest integrated baseline and reruns affected checks. Never concurrently merge whole-board files as if textual independence proved geometric independence.

### Integration dependency order

1. Reconciled project/rules/libraries and source-contract fixes.
2. Verified footprints and affected-region adaptation.
3. Power feed/return contracts and storage local implementation.
4. Residual routing and mechanical/DFM corrections.
5. Integrated SI/PI/thermal evidence and closure validation.

Independent patches need not wait for unrelated lanes. Every commit carries its concise append-only `bible.md` update; milestone status reflects closed requirements, not commit counts or warning percentages.

### Bounded progress and escalation

After two materially different failures in one solution class, or 45 minutes without a new artifact, discriminating result, or reduced blocker, require a focused method change. Emit the registry blocker packet with evidence, class, attempts, assumptions, oracle, independent work, and unblock condition. Root may invoke Unblocker once per eligible distinct blocker. A placement change requires a structural-contradiction packet to its authority. Do not replay rejected JMS ground variants or reopen orientation because immature routing is difficult.

Keep blockers scoped. Continue independent work and resume dependent work when inputs arrive. Do not use Unblocker to waive audit findings, bypass approval/runtime restrictions, or manufacture a passing milestone. Optional suggestions do not extend the goal.

## 4. Phase 24 acceptance matrix and focused validation

Every required row must resolve against one integration SHA and one complete source/toolchain manifest. Existing scoped passes remain reusable only within their tested scope and unchanged dependencies.

| Acceptance row | Required closure |
|---|---|
| Native ERC | Clean full-severity result; account for all 299 electrical and 56 library/link findings. No severity filtering or environmental blanket waiver. |
| Native DRC and physical connectivity | Clean integrated DRC; zero unintended shorts and zero unresolved required connections. Resolve inherited crossings and actual remaining REFCLK clearance defects. |
| Bidirectional source/pad/reference coverage | Fresh native XML; expected and surplus references/pads/nets classified; duplicate keys detected; no concealed hierarchical-net collisions. |
| Placeholder/alias coverage | Audit every excluded `X*` ref, J1 PWR/GND, J3 59–66 key-gap placeholders, and J2/F1/F2/J4 aliases. Independently cover every required physical CM5/SXM2/M-key power contact. |
| Libraries and pin mapping | Zero legacy namespace leakage or unresolved links; verified package-to-pad mapping, project-local library census, explicit official dependencies. |
| Layers, routes and returns | Six-layer role census; ordinary through-vias; no ordinary plane-layer signals; actual width/gap/length/skew/via and transition/reference evidence. |
| Impedance | Resolve the recorded same 5.2-mil/8-mil geometry for 90 Ω and 100 Ω against frozen stack and actual geometry. State calculation/fabricator tolerances and limits. |
| Power/protection/thermal | All required contacts physically supplied; sharing, bottlenecks, voltage drop, inrush, protection, effective capacitance, transient and thermal margins verified analytically or through applicable evidence. |
| Regulator overlays | Compare current integrated copper/support geometry with exact vendor references. Existing risk dispositions do not waive new physical defects. |
| Storage/JMS583 | Selected SATA/NVMe modes, switches, inactive-state isolation, M-key mapping, all required support branches and returns pass integrated checks and meaningful negative controls. |
| Fine escape | Effective native local 0.10-mm XIN/XOUT rule is proven in the authorized window; appropriate normal/net-class geometry resumes outside. No global relaxation. |
| Authority/firmware/procurement | Required package/configuration/programming/traceable-supply evidence present or covered by an existing applicable disposition. Agreed unpromoted Path B remains outside production gate. |
| Mechanics/DFM/serviceability | Actual models/envelopes, holes, mating, cooler/backplate, SSD/cables, mask/paste, courtyards, silk, assembly sequence, tool and probe access verified. |
| Independent hostile review | One focused hardware audit of integrated candidate and evidence. Material unresolved findings block Phase 24; optional suggestions do not extend the campaign. |

No new waivers are authorized. Preserve exact applicable `REV_A_EMPIRICAL_RISK` records and distinguish design evidence from deferred hardware tests. Do not demand fabricated-hardware testing where the approved gate explicitly defers it, and never claim enumeration, bench thermal response, licensing rights, or vendor approval that was not obtained.

The existing 814 expected-node / 1,262-pad / zero-mismatch result is narrow ownership evidence. It does not prove physical connectivity, surplus-pad correctness, power delivery, or SI. Extend coverage without invalidating the scoped pass without cause.

### Existing commands and minimal tool changes

Run existing checks in the selected project directory, always supplying the exact candidate and fresh outputs:

```sh
kicad-cli sch export netlist --format kicadxml --output OUTPUT/current.xml SCHEMATIC
python3 phase24_live_contract_map.py --root SCHEMATIC --output OUTPUT/live-map.json
python3 phase24_schematic_pcb_pad_parity_audit.py PCB OUTPUT/current.xml
python3 phase24_u5_layer_connectivity_audit.py PCB --negative-controls
python3 phase24_dual_mode_storage_usb3_native_connectivity_audit.py PCB
python3 phase24_storage_m2_power_owner_audit.py PCB --strict-sources --connector=J3
python3 phase24_integrated_support_audit.py PCB --negative-output OUTPUT/support-negative.kicad_pcb
python3 phase24_jms583_fine_escape_scope_audit.py PCB
python3 phase24_dual_mode_storage_schematic_audit.py STORAGE.kicad_sch
python3 phase24_mode_truth_table_test.py
```

Native ERC/DRC must include all severities and retained exclusions; capture supported CLI arguments during baseline execution. Never use `--severity-error` as the clean gate. The old checked-in root XML is stale SATA-era output and is never a parity authority.

Make only changes needed to establish the matrix:

- Use a thin modular `phase24_validate_candidate.py --manifest MANIFEST --output OUTPUT` entrypoint around existing checks if needed for repeatable execution. This is orchestration of existing checks, not a replacement validation framework.
- Record commands, return codes, raw outputs, source/image/rule/library identities and hashes; fail if any required row fails or lacks evidence.
- Extend parity for duplicate keys, surplus pads, exclusions and full-hierarchy collisions, preserving its original narrow result separately.
- Parameterize stale reference audits using `FINAL5.xml` or unrelated PCBs.
- Separate `phase14_power_analysis.py` read-only analysis from generator side effects and fixed historical geometry.
- Replace historical-board assumptions in return/mechanical checks with selected-candidate inputs and real geometry evidence.
- Expand JMS coverage beyond the existing five-join support audit; reject missing expected M-key power sources.
- Keep logic truth tables distinct from physical switch-isolation and eventual hardware-operation evidence.

Use targeted tests during repair, fresh Light validation for material integrated batches, and one complete fresh-checkout closure run. Do not repeatedly rerun unchanged green fixtures instead of closing open requirements. Documentation-only changes need manifest/diff checks, not every historical CAD test.

The launcher emits its standard validation receipt only after successful completion. Independently capture identity and host-side exit status so failed runs also retain complete evidence.

### External dependencies and private Library

Start discovery early:

- JMS583 baseline firmware is documented as factory-mask-ROM; traceable factory-programmed procurement remains open.
- TUSB9261 firmware/programming downloads require authorized TI access; required binaries were not retained.
- Resolve exact impedance evidence and critical model/package gaps using authorized sources.

Librarian retrieves existing material first from `/home/nyx/PiSXMe-Library/Library`. Preserve private `Library` branch `b13bdb28c23c138670c63a05875061a0280fce4a` as observed during planning; use explicit refs because its configured upstream is misleading. Do not copy restricted reference material into public development history, change visibility, or overwrite mirror/Library history.

If vendor authorization, traceable supply, firmware, or a mandatory model is genuinely unavailable, report the missing evidence and block only its dependent acceptance row while independent work continues. Ask Rey only for a genuinely user-owned decision or authorization that existing instructions do not supply.

## 5. Closed milestones, Phase 25 freeze, and hard stop

**M0 — Reproducible baseline and effective context:** untouched selected source replayed once; differences reconciled; exact storage authorities recorded; targeted archive evidence indexed; runtime limits recorded; native rule-loading and local/outside behavior proven.

**M1 — Coherent integration basis:** project/rules/libraries explicit, source/export coverage sound, critical footprints verified, region ownership and feed boundaries fixed.

**M2 — Integrated engineering closure:** required routes, storage, returns, power, mechanics and reference evidence satisfy their acceptance rows.

**M3 — Phase 24 passed:** complete fresh-checkout validation and focused hostile review close every required row, with only already-authorized applicable dispositions. Root alone declares completion. A clean isolated fixture cannot close an integrated counterpart.

**M4 — Phase 25 frozen and privately backed up:**

1. Let `C` be the exact validated source commit. Freeze schematic/PCB, outline, placements/orientations, routes/vias, stack/rules, libraries/models, margins, power results, assembly sequence, accepted-risk records, commands and raw closure artifacts by hash.
2. Package a machine-readable freeze manifest naming `validated_source_sha=C`, complete closure receipts, reproducible commands/toolchain identities, and artifact hashes. Restricted artifacts stay in private storage with hashes and access references.
3. Commit freeze documentation and one concise append-only bible milestone as freeze commit `F`. Earlier campaign commits also include their required concise bible entries.
4. Prove validated design inputs are unchanged between `C` and `F`; rerun affected validation if any design input changed. Avoid a self-referential manifest SHA: the manifest names validated `C`, while the tag identifies freeze `F`.
5. Recheck remote identities, private visibility, ancestry and tag conflicts. Fetch during execution; never reset, force-push, mirror-push, or alter `Library`. If private branch ancestry has diverged, preserve both histories and resolve the narrow integration issue before pushing.
6. Use explicit destinations, substituting the actual commit and message-file path:

   ```sh
   git push private F:refs/heads/reva-clean
   git tag -a ACREAGE_REFERENCE_VALIDATED F -F FREEZE_TAG_MESSAGE_FILE
   git push private refs/tags/ACREAGE_REFERENCE_VALIDATED
   ```

7. Verify private branch SHA, annotated tag object and peeled tag commit resolve as intended. Do not overwrite an existing tag; inspect any conflict and stop that publication step if unresolved.
8. Preserve durable private artifacts before releasing this campaign's workspaces. Close completed agents through the supported lifecycle where available; if closure is unavailable, report it honestly and reuse sessions rather than claiming slots were released. Leave unrelated historical workspaces and archive material untouched.
9. Leave a clean committed worktree and compact Phase 26 handoff naming frozen references, constraints, acceptance rules and deferred empirical risks. This is preparation only: perform no shrinking, packing experiments, compression routing, edge moves, or further project stage.

The freeze explicitly states **design-validation evidence, not fabricated-hardware proof**. End the bounded goal after Phase 25.

### Proposed Goal Mode objective for the future execution turn

> Execute this approved PiSXMe Phase 24 completion → Phase 25 acreage-freeze plan and its incorporated clarifications from the verified reva-clean succession lineage. Close every required acceptance row on one integrated candidate, privately back up and tag the exact validated freeze, preserve evidence and clean up campaign resources, then end the bounded goal before Phase 26. Do not resume the legacy whole-product goal.

**Current stop condition:** this plan is saved for approval record only. Do not create/resume a goal or start commissioning, implementation, or validation until Rey instructs execution to begin.
