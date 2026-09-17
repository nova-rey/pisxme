# SXM2/V100 carrier architecture sanity check — 2026-09-17

**Requesting package:** bounded foundational power-constraint provenance audit
(`P24-POWER-ARCHITECTURE-PROVENANCE-AUDIT`; Root Foreman).

**Role boundary:** Librarian evidence only. This brief does not select PiSXMe
power architecture, override NVIDIA/SXM2 authority, or authorize CAD changes. It
compares public carrier practice at a high level and preserves licensing limits.

## Acquisition and provenance

The Library already contained the Benchoff reverse-engineering family and the
Liu/Xiaoyu/3890p metadata. A live identifier search on 2026-09-17 refreshed
these heads and added the Tongde/OSHWHub and commercial-carrier records below.
No third-party PCB, schematic, artwork, STEP, or other expressive CAD was
copied into the private Library or public development repository.

| ID | Source / revision | Class and tier | Retention and limitations |
|---|---|---|---|
| `sxm2-benchoff-article-20260912` | Brian Benchoff, “Reverse Engineering the NVIDIA SXM2 Socket”, HTML, <https://bbenchoff.com/pages/SXM2PCIe.html>; live page rechecked 2026-09-17 | Public reverse engineering; Tier 3 | Existing extracted facts and prior lawful local hash retained. One evidence family; explicitly not NVIDIA-official. |
| `sxm2-benchoff-repo-3173b02c` | `bbenchoff/SXM2toPCIe`, `main`/`HEAD` `3173b02c085218d66c4a2a9e5492853fb53ee097`; <https://github.com/bbenchoff/SXM2toPCIe> | Public implementation precedent; Tier 3 | Existing metadata and hashes only; no new source bytes. Same family as article. |
| `oshwhub-mtf-tongde-v3-20260917` | MTF Electronics Studio, “SXM2 to PCIE adapter board”, OSHWHub, <https://oshwhub.com/mtf-electronics-studio/sxm2-to-pcie>; page retrieved/search-indexed 2026-09-17 | Public implementation precedent; Tier 3 | Page declares CC BY-NC-ND 3.0. Metadata and extracted facts only; no project files or images retained. |
| `sxm2-liuxinyu-repo-27dd1229-20260917` | `LiuXinyu12378/SXM2_to_PCIE_adapter`, `main`/`HEAD` `27dd1229889f4f0c03324b419931d2d466fccde4`; <https://github.com/LiuXinyu12378/SXM2_to_PCIE_adapter> | Public empirical implementation; Tier 3/4 | README facts only; no source files or images copied. Claims are author/seller evidence, not independent qualification. |
| `sxm2-ai-cooling-dual-8pin-20260917` | AI-Cooling, “SXM2转PCIe转接卡”, product page, <https://www.ai-cooling.com/?product=198>; page posted 2025-09-30, retrieved 2026-09-17 | Commercial implementation claim; Tier 4 | Product-page text only; no design files or measurements retained. “300 W without frequency reduction” is vendor claim. |
| `3890p-sxm2-to-pcie-riser-85b0e24` | `3890p/SXM2-to-PCIE-Riser-card`, `HEAD` `85b0e248923ec4114ff464c2400e7cb6de5af40c`; <https://github.com/3890p/SXM2-to-PCIE-Riser-card> | Unverified/conflicting implementation; Tier 4 | Existing metadata only. Its contact assignments conflict with the selected map and do not establish power architecture. |
| `nvidia-v100-datasheet-2019` | NVIDIA Tesla V100 datasheet, December 2019; existing private authority copy | Manufacturer product authority; Tier 1 | Existing private hash/evidence. Supplies V100 SXM2 maximum-power fact (300 W), not a branch-regulation prescription. |

## High-level observations

### Benchoff reference carrier

The article describes the reverse-engineered source carrier as a single-SXM2
board with one populated Amphenol MEG-Array connector, the NVLink connector
left unpopulated, and **two 2x3 PCIe power headers** feeding the carrier. The
article calls the circuit simple and mentions only small fan-PWM circuitry in
addition to the connector and PCIe conversion. It does not describe six
independent precision-current loops, calibrated branch regulation, or a
per-contact current servo. The corresponding repository is a complete KiCad
implementation, but it is the same reverse-engineering family and cannot
serve as NVIDIA product authority.

This is evidence of a multi-contact/common-input carrier pattern, not proof
that copying the board would satisfy PiSXMe's 300 W, thermal, protection, or
prototype requirements.

### Tongde / OSHWHub Version 3 family

The OSHWHub page describes a family of SXM2-to-PCIe boards with direct PCIe
and NVLink variants compatible with P100/V100/PG199. It states that the work
was reverse-engineered from V100 PCIe and SXM2 boards, identifies “Tongde
Version 3” as the current most-stable variant, and describes 4-layer and
6-layer 10 cm x 10 cm small-board options while recommending six layers.
The accessible page text does **not** publish a connector count, branch-current
allocation, precision limiter topology, or a validated power-plane budget.
Those fields remain unknown; they must not be filled from the page title or
from the board images. The CC BY-NC-ND notice prohibits treating the source
as a reusable CAD donor.

### LiuXinyu public carrier family

The README explicitly prioritizes full-load power capacity and describes an
upgrade as “3x8-pin + PCIe” with a theoretical 525 W rating. A later bullet
says “dual 8PIN power supply + PCIe” for up to 525 W, so the exact connector
count is internally inconsistent and is not adopted as a PiSXMe fact. Both
statements nevertheless describe external, high-capacity 12 V input(s), not
six precision-regulated branch channels. The README also states PCIe x16
operation, no NVLink, multiple 4-layer/6-layer ENIG board variants, and
fan/temperature features on some variants. Its long-duration temperature and
stable-operation statements are author/seller claims without an independent
test report.

### Commercial dual-8-pin carrier claim

AI-Cooling's product page states dual 6+2-pin power connectors, a claimed
300 W load without frequency reduction, and a six-layer impedance-optimized
board. The page does not disclose precision branch regulation, six independent
loops, exact protection, copper geometry, or test instrumentation. It is useful
as a commercial-practice sanity check only.

### Conflicting/unverified public design

The existing 3890p record contains an unverified 400-pad connector design with
130 +12 V and 168 GND assignments, but its signal/auxiliary assignments
conflict with the selected Benchoff map and its orientation/source hardware are
not established. It is not used as power or contact authority.

## Comparison for Power Authority

| Reference | External power entry reported | Distribution / regulation disclosed | Protection or sensing disclosed | Board / thermal evidence | Confidence and use |
|---|---|---|---|---|---|
| Benchoff source carrier | 2 x 2x3 PCIe headers | Common carrier delivery is described; no precision per-loop regulation reported | Fan PWM circuitry mentioned; no complete protection bill reported | Complete KiCad reference; no independent power qualification | Strong public precedent for simplicity; not NVIDIA authority |
| Tongde V3 / OSHWHub | Not published in accessible text | Not published; no six-loop claim found | Not published | 4/6-layer, 10x10 cm options; six-layer recommended | Useful family-level sanity check; CC BY-NC-ND; no CAD reuse |
| LiuXinyu family | “3x8-pin + PCIe” headline versus “dual 8-pin + PCIe” bullet; theoretical 525 W | High-capacity external-input pattern; no precision loops disclosed | MCU temperature/fan support on some variants; complete protection not disclosed | 4/6-layer ENIG; author reports full-load thermal operation | Empirical author claim; exact connector statement conflicted |
| AI-Cooling product | Dual 6+2-pin | No precision loops disclosed | Not disclosed | Six-layer; vendor claims 300 W without frequency reduction | Commercial marketing evidence; independent test absent |
| PiSXMe current six-loop concept | Internal two-circuit/derived six-loop records | Six independent 6.000--6.400 A precision windows and 57 mOhm allocation were imposed by project authority records | Detailed limiter/FET/fault qualification in HPQ #5 | Substantial routing and qualification burden | Requires provenance audit; not justified by these public precedents alone |

## Bounded conclusion for the requesting authority

Across the examined public carrier family, the observable pattern is one or
more adequately rated external 12 V inputs feeding a common or distributed GPU
power field, with ordinary board protection/sensing and cooling provisions.
The records found no public requirement that an SXM2 V100 carrier use six
independently precision-regulated 6 A channels, no-passive-sharing control, or
a 57 mOhm hot limiter allocation. That absence is not proof that such controls
are never needed; it means the six-loop contract cannot claim precedent as its
source.

A defensible prototype still needs a source and connector/harness capacity
calculation, contact and copper temperature-rise checks, voltage-drop and
transient margins, reverse/inrush/short protection, rail and sequencing
checks, and a defined first-power measurement plan. Public carrier practice
only answers the architectural-complexity sanity question. It does not close
those PiSXMe-specific safety and product checks.

The 300 W V100 SXM2 figure is manufacturer product evidence in the existing
private Library. The carrier references do not establish the complete V100
rail/sequence/contact contract or a measured 330 W transient allowance.
Product/Power Authority must bind those requirements separately.

## Licensing and non-copy disposition

The Library retains source identifiers, URLs, revisions, retrieval dates,
license/access status, and extracted high-level facts. It does not mirror
OSHWHub's CC BY-NC-ND project, third-party images, GitHub CAD, or commercial
product material. The brief is evidence for comparison and authority review,
not a license to copy implementation expression.
