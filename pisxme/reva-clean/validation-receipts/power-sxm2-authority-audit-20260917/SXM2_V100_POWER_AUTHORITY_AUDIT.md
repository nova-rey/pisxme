# V100/SXM2 power-authority audit

- Package: `P24-POWER-SXM2-AUTHORITY-AUDIT`
- Workstream base assigned by Main Queue: `668807f0`
- Evidence audited at current HEAD: `8626eee2a42bfb6f183c796045bd8be008d98884`
- Date: 2026-09-17
- CAD changed: **no**
- Assurance level: PiSXMe Rev A is a **prototype/open-hardware carrier**. This record contains no fabricated-hardware measurement or production-qualification claim.

## Decision-relevant conclusion

The strongest public NVIDIA evidence establishes that the V100 SXM2 is a 300 W maximum-power device and uses the NVIDIA NVLink system interface. It does not publish a six-channel input contract, per-contact current allocation, independent current regulation, a 6.000--6.400 A branch window, a 57 mOhm limiter allocation, or a standalone SXM2 input sequencing/current-limit specification.

The Amphenol contact rating and the reverse-engineered map establish physical contact capacity and a useful candidate map. They do not establish six independently regulated channels. Benchoff's working public carrier used two 2x3 PCIe power headers and direct high-current delivery; this is secondary engineering evidence, not an NVIDIA design mandate.

Accordingly, the six-loop precision-limiter requirements remain **unproven implementation/agent-created constraints**, not foundational NVIDIA/SXM2 requirements. Product/Power Authority should select the simplest protected, adequately rated 12 V distribution architecture that satisfies the binding 300 W sustained and bounded peak product envelope, connector/harness/copper/thermal limits, and any later authoritative sequence or auxiliary requirement. This audit does not itself authorize a CAD change or bind the replacement topology.

## Source and provenance matrix

| ID | Source and revision | Authority / use | What it establishes | What it does not establish |
|---|---|---|---|---|
| `NVIDIA-V100-DS-2019` | NVIDIA, *Tesla V100 GPU Accelerator* datasheet, Dec 2019; URL `https://images.nvidia.com/content/technologies/volta/pdf/tesla-volta-v100-datasheet.pdf`; SHA-256 `ca694a4789eae7feb9ce909fe0f2207cbe82f5da1448922d4855e346680c59d3` | A, manufacturer product contract | V100 SXM2 system interface is NVIDIA NVLink; V100 SXM2 maximum power consumption is 300 W; passive thermal solution is listed | Input rail voltage, contact groups, per-contact current, branch sharing, current limiter, enable polarity, sequence, or auxiliary rail contract |
| `NVIDIA-V100-PRODUCT` | NVIDIA V100 product page, retrieved 2026-09-17, `https://www.nvidia.com/en-gb/data-center/tesla-v100/` | A, corroboration | Lists V100 SXM2 and 300 W maximum power | Detailed electrical pin/rail/sequence contract |
| `AMPHENOL-74221` | Amphenol/FCI 74221-101LF manufacturer drawing and application data, indexed in private Library brief `sxm2-j1-amphenol-rev-w-corpus-20260912.md` | B, component contract | 400-position 10-row 1.27 mm MEG-Array geometry; generic contact rating recorded as 0.45 A/contact under stated manufacturer conditions | SXM2 functional assignments, grouping, simultaneous thermal derating in this application, independent regulation, or NVIDIA limits |
| `BENCHOFF-ARTICLE` | Benchoff, *Reverse Engineering the NVIDIA SXM2 Socket*, `https://bbenchoff.com/pages/SXM2PCIe.html`, retrieved 2026-09-12, SHA-256 `9fa2b322672dcb01eb6f59c3ae0375299b7e72bc5e053959517508894d1cf8e4` | Secondary reverse-engineering evidence | Empirical contact map; published 12 V/GND/PCIe/REFCLK/PERST observations; carrier used two 2x3 PCIe power headers; unmapped contacts remain | NVIDIA authority, guaranteed ratings, exact sequence, per-group current, independent regulation, or current limiting |
| `BENCHOFF-KICAD` | `https://github.com/bbenchoff/SXM2toPCIe`, pinned `3173b02c085218d66c4a2a9e5492853fb53ee097` | Secondary implementation reference | Complete public KiCad implementation and corresponding contact/physical evidence | Permission to copy expressive CAD, NVIDIA approval, production qualification, or a six-loop requirement |
| `XIAOYU-PINOUT` | `https://github.com/xiaoyu9733/sxm2-pinout-definition`, pinned `c05541e1846b47f51d05a2149ff044d4d2eba727` | Independent check; insufficient as fetched | Repository currently contains only README-level material; no usable independent contact table was found | Corroboration of individual contacts or power grouping |
| `CN108280004B` | Public patent, FCI 74221-101LF in an SXM2 test-board interface | Corroborating mechanical/topology evidence | Connector use in an SXM2 test-board context | NVIDIA V100 power limits, rail/sequence details, or branch regulation |
| `DGX1-GUIDE` | NVIDIA DGX-1 user guide, archived docs, `https://docs.nvidia.com/dgx/archives/dgx1-user-guide/introduction-to-dgx1.html` | A system-level context | DGX-1 uses eight SXM2 modules and four 1600 W supplies (3+1 redundancy) | Per-GPU branch topology or six-loop requirement |
| `PISXME-POWER-V2` | Internal candidate `POWER_ENVELOPE_AUTHORITY_V2.0_CANDIDATE.{md,json}`, first introduced at commit `90420b83ff54f5a3db9633482bc16627671c07f3` | E/F, historical internal design | Origin of proposed six-loop, 8 A/circuit, 6.4 A branch and 40/45 A source screens | External or user requirement; no NVIDIA source is cited for independent loops |
| `PISXME-LIMITER` | Internal limiter authority `POWER_LIMITER_SELECTION_AUTHORITY.md`, commit `1a39f6b2c3be9d310c601604d3b0efc3b8cc9b20` and retained no-go `dd2e7eed7cdd6bb04d98225c691c127171b9ff5a` | E/F, downstream derivative | Repeats six-loop, 6.000--6.400 A, 57 mOhm and no-passive-sharing contract for HPQ5 | Independent origin or external authority; it cannot prove its own premise |

The Benchoff article/repository, Amphenol records, patent, and the second GitHub repository are indexed in the private Library. Restricted or reference CAD is not copied into the public development repository.

## Real requirements and unresolved boundaries

| Requirement | Class | Status and evidence |
|---|---|---|
| V100 SXM2 maximum power: 300 W | A, external manufacturer | **BOUND** by NVIDIA datasheet/product page. Product requirement of 300 W sustained remains a PiSXMe C-level requirement; a 330 W design peak is a separate internal product allowance pending Product/Power confirmation. |
| SXM2/NVLink interface identity | A | **BOUND** by NVIDIA datasheet. This does not define the power contact contract. |
| Safe delivery of the declared product load | A/B/C | **BOUND as a design objective**, with current, voltage-drop, copper, connector, thermal, protection and bring-up calculations required. Exact source voltage and topology remain Product/Power design choices unless a stronger contract is found. |
| Amphenol contact geometry/rating | B | **BOUND within manufacturer conditions**; 0.45 A/contact is a connector rating, not a claim that every SXM2 power contact is to be run at that value simultaneously or that 130 contacts form six channels. Application derating remains required. |
| Published contact map (130 12 V, 170 GND in Benchoff map) | Secondary | **Useful but non-NVIDIA evidence**. It supports parallel physical distribution and preserves unknown contacts as unknown. It does not prescribe branch allocation. |
| 12 V as the V100 input rail | F/secondary | **Not publicly bound by the NVIDIA sources inspected**. It is a reasonable carrier design convention and appears in the reverse-engineered carrier, but must be recorded as a PiSXMe architecture choice until a higher-authority SXM2 source is obtained. |
| Standby/auxiliary rails, enables, reset polarity and sequencing | F/unknown | **UNPROVEN** for standalone SXM2. No public NVIDIA standalone contract was found. Retain as bring-up/evidence work; do not invent polarity, timing, or rail assignments. |
| Per-contact/group current limit | F/unknown | **UNPROVEN**. Contact count and map do not provide this contract. |
| Independent current regulation or current limiting | F/unknown | **UNPROVEN and not implied** by contact multiplicity. |
| Six independent loops; no passive sharing; 6.000 A minimum; 6.400 A ceiling; <=57 mOhm hot allocation | E/F | **UNPROVEN as foundational requirements**. These first appear as internal PiSXMe architecture/limiter screens, not in an NVIDIA, connector, standard, or user product source. They must not veto a simpler prototype architecture without a new A--D derivation. |
| Production supplier guarantee, population statistics, lifetime calibration, exhaustive production fixture | E/F | **Not required for prototype fabrication**. Replace with calculations, ratings, worst-case margins, safe protection and explicit `REQUIRES PROTOTYPE VALIDATION` bring-up procedures. |

A 300 W / 12 V arithmetic result of 25 A is a conditional engineering calculation, not proof that NVIDIA mandates a 12 V source. Any source-current target must include the selected source voltage, conversion efficiency, transient allowance, derating and protection policy.

## Six-loop provenance disposition

| Existing requirement | Earliest located origin | A--F classification | Disposition for governing contract |
|---|---|---|---|
| Six independent power loops | Internal candidate `POWER_ENVELOPE_AUTHORITY_V2.0_CANDIDATE` at `90420b83` (2026-09-13), later repeated by limiter authorities | E (architecture choice), with F risk where later records treat it as external | **UNPROVEN; recommended demotion from foundational invariant pending Product/Power decision** |
| No passive current sharing | Same internal V2.0 candidate/branch policy lineage; no NVIDIA or connector source found | E/D only if Product/Power proves a safety derivation; currently F as an asserted premise | **UNPROVEN; do not infer from contact count** |
| 6.000 A minimum per loop | First located in the downstream limiter authority lineage (`454de823`, 2026-09-13) and later HPQ4 records | E/F, component/architecture screen | **UNPROVEN; a limiter-selection contract cannot establish product origin** |
| 6.400 A maximum per loop | Internal V2.0 branch screen at `90420b83`; later HPQ4 records | E/D candidate screen, not external | **UNPROVEN; retain only if Product/Power re-derives it from real product/protection constraints** |
| Independent precision current regulation/limiting | Internal V2.0 candidate and limiter-selection lineage beginning `90420b83`/`454de823` | E/F | **UNPROVEN; no NVIDIA/SXM2 evidence found** |
| <=57 mOhm hot limiter allocation | Limiter candidate authority `454de823`, later HPQ4 records | E/F, implementation loss allocation | **UNPROVEN and downstream; cannot govern architecture** |
| Prescribed current for each SXM2 power-contact group | No authoritative origin located; inferred from contact rows/branch architecture | F | **UNKNOWN / no foundational veto**. Preserve unknown contact behavior and require bring-up evidence. |

Repeated downstream authority records are not independent corroboration: they restate the original internal candidate and cannot elevate E/F assumptions to A--D.

## Contact multiplicity versus independent regulation

The published map has many parallel 12 V and GND contacts. That means the connector can distribute current across multiple physical contacts when the application wiring, copper and thermal conditions are valid. It does **not** mean that each row, group, or contact must receive a separate regulator, nor that a prescribed equal current must be forced through each group. A common protected 12 V bus can feed multiple contacts; branch fusing/sensing may be added if Product/Power Authority derives a fault or service requirement. Independent regulation requires an explicit electrical contract or a defensible safety/product derivation, neither of which was found here.

## Prototype assurance boundary and recommendation

Before prototype fabrication, require a signed Product/Power architecture record containing: selected input voltage/source and connector/harness rating; protected distribution and fault policy; source and branch continuous/peak budget; worst-case voltage-drop and copper/via temperature-rise calculations; thermal path and passive/active cooling assumptions; return-plane strategy; and explicit first-power limits and measurements. Mark undocumented V100 sequence/auxiliary behavior `REQUIRES PROTOTYPE VALIDATION` rather than fabricating a pass.

The simplest defensible candidate for authority comparison is a conventional adequately rated 12 V source or standard high-current GPU-style inputs feeding ordinary fuse/reverse-polarity/TVS/inrush/sensing protection and a calculated common protected 12 V plane to the mapped J1 contacts. It must be compared against any intermediate architecture using real source, connector, copper, thermal, fault and bring-up evidence. This audit recommends that the six-loop precision limiter be removed from the critical path unless Product/Power Authority independently re-derives it from A--D evidence.

No public reference CAD or artwork is being proposed for copying. The architecture decision remains with Product/Power Authority; this package supplies the evidence boundary and provenance correction.

## Validation performed

- Inspected the current project authority files, internal power candidates, limiter records, private Library briefs, and Git history.
- Checked earliest relevant internal origins with `git log -S` and read the originating candidate records.
- Retrieved/verified the NVIDIA V100 datasheet/product facts and recorded its SHA-256; no vendor PDF was added to the public repository.
- Confirmed the Xiaoyu repository at its pinned revision contains no usable independent contact table.
- No CAD, schematic, footprint, rules, net contract, queue state, or HPQ state was changed by this workstream.
