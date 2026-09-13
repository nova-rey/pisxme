# SXM2/J1 evidence refresh — 2026-09-13

This is a Librarian refresh for the Phase 24 J1 package/net question. It adds
no public PiSXMe CAD and retains metadata and extracted facts only for public
reference material whose redistribution terms are not being mirrored.

## Acquisition and provenance

The following sources were fetched or resolved again on 2026-09-13:

| ID | Source and exact revision | Class | Retained material / hash |
|---|---|---|---|
| `sxm2-benchoff-article-20260912` | Brian Benchoff, “Reverse Engineering the NVIDIA SXM2 Socket”, HTML, retrieved 2026-09-13; article describes mid-2025 work | public reverse-engineering, Tier 3 | extracted facts and URL; prior retained HTML hash `9fa2b322672dcb01eb6f59c3ae0375299b7e72bc5e053959517508894d1cf8e4` |
| `sxm2-benchoff-repo-3173b02c` | `bbenchoff/SXM2toPCIe`, `main` and `HEAD` at `3173b02c085218d66c4a2a9e5492853fb53ee097` (2025-09-21) | public implementation precedent, Tier 3 | metadata/extracted facts only; PCB `341b028c0e9baaad633133cdf7dde5192d0b96abdd0ce7ed0246abbcb4d306e20` |
| `xiaoyu-sxm2-pinout-definition-c05541e` | `xiaoyu9733/sxm2-pinout-definition`, `main`, `HEAD`, and `v1.0.0` at `c05541e1846b47f51d05a2149ff044d4d2eba727` (2025-02-09) | claimed independent dataset, Tier 4 | README only; `cc9920792af34f995706c1864bb728af7464c58ae8617ed0246abbcb4d306e20`; no map or schematic available |
| `amphenol-74221101lf-product` | Amphenol/FCI `74221-101LF` product page, current page retrieved 2026-09-13 | manufacturer product authority, Tier 1 | URL and extracted facts only |
| `amphenol-74221-drawing-w` | Amphenol/FCI drawing `74221`, Rev W, Released, EC `ELX-V-40495-1`, approval 2021-04-13 | manufacturer mechanical authority, Tier 1 | URL and extracted facts only; direct CDN capture remains HTTP 403 |
| `cn108280004b` | CN108280004B, priority 2018-01-22, grant/publication 2021-10-29 | public patent corroboration, Tier 2 | citation and extracted facts only |
| `3890p-sxm2-to-pcie-riser-85b0e24` | `3890p/SXM2-to-PCIE-Riser-card`, `HEAD` `85b0e248923ec4114ff464c2400e7cb6de5af40c`, latest commit 2025-02-10 | unverified public implementation, Tier 4 | metadata and hashes only; Altium PCBdoc files not copied |

The repository's actual retained implementation-file hashes are recorded in
`Library/provenance/sources.json`; no upstream file is copied here.

Live repository checks returned Benchoff `HEAD=main=3173b02c...` and Xiaoyu
`HEAD=main=v1.0.0=c05541e...`. The Xiaoyu repository tree contains only
`README.md`, so its title/description is not independent contact evidence.

A broader identifier search also found `3890p/SXM2-to-PCIE-Riser-card`. Its
README explicitly calls the project unverified. The 400-pad connector record
in `4090ovo(003).pcbdoc` was parsed as a separate public implementation
signal source: 130 `+12V`, 168 `GND`, 5 `+5V`, 16 unassigned, and the rest
signal/auxiliary nets. It disagrees with the Benchoff contact map at 65
contacts, including A2/A3, E7/F7, E18, multiple PCIe lanes, J7/J39, and
K18/K19. The file names a `84740-002LF` plug and does not establish the
orientation/side transformation or hardware provenance needed to resolve the
differences. It is retained as a conflicting, low-confidence warning and
cannot corroborate or override the Benchoff map.

## Mechanical correspondence

The current selected PiSXMe PCB at source commit `acdc52c47d520b053e791b030945d6fa95d5348a`
uses `PiSXMeRevAClean_SXM2_74221_101LF` for J1. The footprint has 400 unique
physical pad identifiers: every member of the ordered set `{A..H,J,K} ×
{1..40}`. Its J1 block has 307 named nets and 93 intentionally unassigned
physical pads. The current PCB SHA256 is
`75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c`.

The reference footprint
`SXMtoPCIe/74221-101LF/AMPHENOL_74221-101LF.kicad_mod` at the pinned Benchoff
revision has the same 400 identifiers. A parser compared each identifier's
local `(at x y)` coordinate against the PiSXMe J1 block:

* shared identifiers: 400/400;
* coordinate mismatches: 0;
* transform: identity `(x_local,y_local)=(x_reference,y_reference)`;
* checked examples: A1 `(24.765,-5.715)`, A2 `(23.495,-5.715)`, B1
  `(24.765,-4.445)`, E7 `(17.145,-0.635)`, E18 `(3.175,-0.635)`, and K40
  `(-24.765,5.715)`.

This is a parsed geometric correspondence, not an inference from artwork.
The phrase “393 J1 pad identifiers” does not match the current physical PCB
block: current evidence is 400 physical pads, 307 named nets, and 93 no-net
pads. The native schematic's J1 abstraction contains nine pins (A2, A3, E7,
F7, E18, G1, G2, PWR, GND); it is not a 393-contact electrical symbol.
This discrepancy must remain explicit in any acceptance report.

## Contact classification and cross-correlation

The structured record `Library/indexes/sxm2-benchoff-contact-map.json` contains
all 400 contacts:

* 130 published 12-V contacts: rows 22, 23, 25, 26, 28, 29, 31, 32, 34,
  35, 37, 38, and 40 across all ten columns;
* 170 GND contacts: signal-region grounds plus complete rows 21, 24, 27,
  30, 33, 36, and 39;
* 64 published PCIe data contacts (PER/PET), 2 REFCLK contacts E7/F7, and
  1 reset contact E18;
* 31 source-declared NC/project-unknown contacts in rows 15–20;
* 2 auxiliary/protection unknown contacts K18/K19.

Benchoff's article and its KiCad implementation are one reverse-engineering
family. The article reports purchased-hardware continuity probing and states
that NVIDIA documentation is NDA-restricted; it is strong precedent but not
NVIDIA-official authority. Amphenol independently corroborates the 74221-101LF
identity, 400-position 10×40 geometry, 1.27-mm pitch, 4-mm receptacle, and
0.45-A/contact product rating, but assigns no SXM2 electrical function. The
patent independently corroborates an SXM2 test-board use of FCI 74221-101LF
and a PCIe/NVLink test topology, but publishes no contact map. Xiaoyu provides
no usable second dataset at its pinned revision. No contact-level conflict was
established between the selected Benchoff map and the manufacturer/patent
records. The 3890p implementation is an explicit low-confidence conflicting
dataset, so the overall evidence set contains unresolved conflicts outside
the bounded selected x1/power contract. The absence of a documented connector
orientation and source hardware prevents treating those conflicts as a valid
reassignment.

## Authority disposition

The existing package/net authority reassessment
`authority-inventory/primary-docs/sxm2/SXM2_J1_AUTHORITY_REASSESSMENT_20260912.md`
is consistent with this refresh: evidence is sufficient for the bounded J1
contract used by Phase 24. It authorizes 130 `12V_PROTECTED` contacts, 170
`POWER_GND` contacts, and the selected x1 contacts A2/A3, G1/G2, E7/F7, E18;
it retains the other published PCIe lanes, 31 source-declared unknown/NC
contacts, and K18/K19 as unassigned. No schematic, footprint, or net
correction is warranted by this refresh. This does not establish fabricated
hardware behavior, V100 undocumented auxiliary semantics, power thermal
adequacy, procurement, or full-board closure.

## Retrieval and licensing disposition

The private Library stores source metadata, revisions, hashes of lawfully
retained local material, and extracted facts. It does not mirror the article,
patent, manufacturer PDF, or third-party CAD/STEP into the public development
repository. Benchoff states article text CC-BY-SA-4.0 and hardware design files
WTFPL 3.0 modified for nerds; the pinned repository also carries its own
license and SnapMagic/third-party model terms. Those terms do not change the
authority classification or permit treating precedent as product proof.
