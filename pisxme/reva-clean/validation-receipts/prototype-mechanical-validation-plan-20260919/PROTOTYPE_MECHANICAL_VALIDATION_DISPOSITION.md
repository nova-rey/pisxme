# PiSXMe Rev-A prototype mechanical validation disposition

**Artifact:** `PISXME-P24-PROTOTYPE-MECHANICAL-VALIDATION-20260919-R1`  
**Package:** `P24-PROTOTYPE-MECHANICAL-VALIDATION-PLAN`  
**Status:** `SIGNED_BOUNDED_PROTOTYPE_VALIDATION_DISPOSITION`  
**Scope:** pre-fabrication verification plan and accepted-risk disposition for the unresolved mechanical/service rows. This receipt contains no fabricated measurements, hardware result, production qualification, field observation, CAD edit, DRC waiver, or Phase 26 work.

## Authority and current evidence

This disposition uses the private Library mechanical packet `a0e68bdc822bad2eca47471649fa3f9417518f1b`, the signed mechanical envelope contract `eff269f2b84044ca521c55116b1971a23558a873`, and the MPA M2 decision `a37a95b6f808eb79175eb45389a6b12343dfaee823eb36ee8932412edbb36091`. The current board is `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`, SHA-256 `338ab87eda178e9569b2230f855219011479bdab47b18637d6d26087cbe2c799`, on `reva-clean` HEAD `5ed438c87451d6208ab7f99481ac557e547be322`.

Existing evidence is scoped: L10/Y10 XY bounds, M2 representation, and CM5/Ethernet 2D edge checks have receipts; exact L10/Y10 Z, J8 accessory/service, physical TE M-key/2280 insertion-retention, selected cooler/backplate assembly, J1 local mating/service, and CM5/Ethernet 3D service fit remain unproven. A renderer pass is not assembly proof.

The selected J3 authority for this plan is TE `1-2199230-4` M-key. The older JAE/B-key entry in the signed mechanical contract is a stale provenance conflict and must be corrected through Storage/Mechanical Authority; it does not authorize replacing the current J3. The MPA binds J3 at `(220,165)`, the full card/service envelope `[220,149]–[300,171]`, and J8 at `(205,140)`.

## Requirement-to-test disposition

The machine-readable JSON contains the complete traceability rows. The following table is the compact decision record.

| ID | Verification class | Prototype sample | Pre-fabrication state | Closure evidence |
|---|---|---:|---|---|
| `MECH-PROT-L10-Y10-Z` | first-article dimensional verification | 1 board, 3 readings/feature | `UNPROVEN_Z_ACCEPTED_AS_REQUIRES_PROTOTYPE_VALIDATION` | selected MPN/drawing, calibrated height readings with uncertainty, adjacent clearance and photo record |
| `MECH-PROT-J8-SERVICE` | design plus functional/service check | 1 board/accessory, 3 operations plus permitted modes | `TOPOLOGY_AND_POSITION_BOUND; ACCESSORY_AND_SERVICE_UNPROVEN` | authority-selected header/shunt, keying/pin matrix, passive continuity/mode record, service photos |
| `MECH-PROT-J3-M2-INSERT-RETENTION` | interface/mechanical validation | 1 board/card, 3 insertion/removal cycles | `REPRESENTATION_BOUND; PHYSICAL INSERTION_RETENTION_UNPROVEN` | TE M-key identity, card seating/keying/retention/service record and released force/torque comparison |
| `MECH-PROT-J1-SXM2-SERVICE-LINKED` | linked mating/rework validation | 1 board/module, 3 controlled cycles | `2D_BOUND; LOCAL_MATING_AND_SERVICE_UNPROVEN` | 4.00 mm stack, 5.10 mm rework boundary, mating and hidden-joint service record |
| `MECH-PROT-COOLER-BACKPLATE` | assembly plus thermal characterization | 1 assembly, 3 install/remove cycles, 1 thermal run | `REV-A-BOUNDARY-ONLY; SELECTED-ASSEMBLY_UNPROVEN` | exact cooler/backplate/enclosure identities, dry-fit/torque record, thermal/current logs under separate power authority |
| `MECH-PROT-CM5-ETH-SERVICE` | first-article assembly/service check | 1 board/module/cable, 3 operations | `2D_EDGE_CHECKS_SCOPED_PASS; 3D_ASSEMBLY_SERVICE_UNPROVEN` | module seating, connector/cable bend/service record; any Ethernet functional result is a separate receipt |
| `MECH-PROT-FIRST-ARTICLE-DFM` | prototype manufacturing/assembly verification | 1 first article | `PLAN_DEFINED; NO FIRST-ARTICLE RESULT` | AOI/optical/X-ray/workmanship traveler and exact BOM/lot record |

## Common test controls

All fit checks are unpowered. Use released manufacturer drawings and selected MPNs; a footprint name or renderer image cannot establish mating. Instruments require current traceable calibration, with ID, date, resolution and U95 uncertainty retained. Apply uncertainty to dimensional limits rather than inventing a new limit. Use manufacturer force/torque limits where released; otherwise record force/torque as characterization only.

The sequence is: verify board/MPN/authority identities; perform unpowered dimensional and dry-fit checks; perform J8 passive continuity and mode checks only after its accessory is selected; complete first-article inspection; then, only after mechanical and continuity safety checks, run the separate current-limited V100 first-power/thermal procedure. No test powers the board during insertion, removal, or installation changes.

Stop immediately for a mis-keyed or binding connector/card, visible contact/PCB damage, unexpected continuity or short, force above a released limit, cooling loss/leakage/smoke/abnormal heating, or invalid calibration. Preserve the state and route the smallest affected row to Package, Storage, Mechanical/DFM, MPA, Power/V100, or Unblocker as appropriate. No failed test authorizes a waiver, silent DNP change, envelope shrink, or unreviewed CAD edit.

Retain raw CSV/force/height/thermal logs, instrument certificates, fixture drawings, board serial and exact MPN/lot records, photos/video, assembly traveler, failure/NCR records, commands/toolchain where CAD is revalidated, and SHA-256 manifests. Restricted vendor material remains in the private Library.

## Regression and closure

Any CAD, BOM, MPN, fixture, placement, enclosure, cooler, or connector change reruns only its dependent dimensional/Heavy/Light checks, with current-head reconciliation and exact source/rule/library/toolchain identity. Material CAD candidates go through isolated producer, serialized canonical integration, and fresh Light validation; unchanged green fixtures are not repeatedly rerun.

This package returns `CANDIDATE_READY` to Root. It may be marked complete as a **plan artifact** after the JSON and hash manifest are integrated. It does not claim hardware validation. The remaining empirical rows stay `REQUIRES_PROTOTYPE_VALIDATION` until records exist. Phase 24 overall remains subject to every acceptance row on one integrated SHA; this artifact authorizes no Phase 25 freeze and does not begin Phase 26.

## Signature

I attest that this is a bounded verification disposition and that no measurement, hardware operation, production qualification, or field observation is claimed without a retained record.

**Signer role:** Hardware Validation / Mechanical package owner  
**Signer ID:** `hardware_validation_mechanical`  
**Signed:** 2026-09-19  
**Attestation:** adjacent `SHA256SUMS`
