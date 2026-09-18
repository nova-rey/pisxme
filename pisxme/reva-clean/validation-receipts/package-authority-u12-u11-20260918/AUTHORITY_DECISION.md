# P24 U12/U11 package authority decision

- Decision ID: `P24-PACKAGE-AUTHORITY-U12-U11-20260918-R1`
- Queue package: `P24-PACKAGE-AUTHORITY-U12-U11`
- Evidence class: package and assembly authority; no CAD mutation
- Source state: current canonical `reva-clean` source at receipt generation
- Decision owner: PiSXMe Package/DFM Authority, using Librarian-indexed primary evidence
- Scope: U12 HD3SS6126RUAR package geometry and U11 JMS583-QHFA3A land treatment

This packet resolves the two named authority dependencies for downstream queue
use. It does not promote the existing U12 footprint, does not alter the PCB,
and does not claim production assembly qualification.

## U12 decision — `P24-U12-PACKAGE-GEOMETRY`

**RESOLVED to the TI RUA0042A 0.50-mm contract.** TI's SLAS975A datasheet
and package outline `RUA0042A`, drawing `4219139/A` dated 03/2020, are primary
manufacturer evidence. The package is a 42-pin WQFN, nominal body 9.00 x
3.50 mm. The example land pattern specifies 42 lands of 0.60 x 0.25 mm,
0.50-mm pitch, 3.30-mm row-center spacing, and exposed pad 43 of 2.05 x
7.55 mm. TI's example stencil is 0.125 mm with 69% printed solder coverage.

The retained project footprint has the correct count, nominal land size, and
exposed pad size, but its signal pad centers use 0.40-mm increments: side rows
span -3.20..+3.20 mm and end rows span -0.60..+0.60 mm. Its side-row centers
are +/-1.80 mm, rather than the 3.30-mm center spacing in the TI example. The
read-only geometry audit in `GEOMETRY_AUDIT.json` reproduces these values from
the exact footprint hash.

Disposition: the retained `HD3SS6126_RUA0042A.kicad_mod` is **rejected as
package-authoritative and must not be routed or promoted**. A separate
isolated CAD producer must regenerate the footprint from this contract, then
prove pin numbering, orientation, package clearance, native DRC, and
connectivity before integration. This authority package makes the requirement
known; it is not the producer candidate.

## U11 decision — `P24-U11-LAND-TREATMENT`

**RESOLVED WITH A PROTOTYPE DISPOSITION.** JMicron PDS-17001 Rev 2.1 Figure 4
is primary package evidence. It specifies QFN64 8 x 8 mm, 0.400-mm terminal
pitch, terminal width `b=0.150..0.250 mm`, terminal length `L=0.300..0.500
mm`, exposed-pad dimensions `D2/E2=4.360..4.560 mm` (nominal 4.460 mm), and
package warpage maximum 0.08 mm.

The retained project footprint measures 64 signal pads plus EP 65, 0.400-mm
pitch, 0.70 x 0.20 mm signal lands, 4.46 x 4.46 mm exposed copper, and a
9.2 x 9.2 mm courtyard. Those values are compatible with the package outline
as a derived prototype land pattern. JMicron does not publish a complete PCB
land-pattern, solder-mask, stencil, or courtyard recommendation in the
retained datasheet.

For the missing land-treatment details, TI's primary general QFN/SON note
SLUA271C is precedent and assembly guidance, not JMicron-specific authority:
TI prefers copper-defined/NSMD lands while accepting SMD; 0.20-mm pad width
is a guide for 0.40-mm pitch printing; typical stencil thickness is
0.100--0.150 mm with 0.125 mm as a guide; and exposed-pad paste should be
windowed to approximately 50--70% coverage to reduce float and voiding. The
note calls for application-specific process development.

Binding prototype disposition:

1. The retained U11 signal copper and 0.400-mm package geometry are permitted
   for prototype implementation, with the named local 0.10-mm escape rule
   remaining separately scoped and subject to native DRC.
2. Use copper-defined/NSMD intent where the fabricator supports it; retain the
   measured 0.20-mm signal pad width and 0.400-mm pitch. The project may use
   its current explicitly modeled mask openings only after the integrated DFM
   check confirms the mask web and fabricator capability.
3. The current full-area EP paste aperture is **not production-ready**. The
   stencil producer must replace it with a windowed aperture targeting
   approximately 50--70% coverage and record the exact window geometry.
4. Prototype fabrication is permitted only with DFM review, a documented
   reflow profile, and post-reflow inspection/X-ray plan. These are prototype
   validation gates and do not claim production qualification or empirical
   hardware success.

## Dependency and implementation disposition

| Dependency | Disposition | What is unlocked | Remaining work |
|---|---|---|---|
| `P24-U12-PACKAGE-GEOMETRY` | **RESOLVED** to TI 0.50-mm contract | U12 package identity/geometry authority and isolated footprint producer | Regenerate footprint; re-prove pin map and validate integrated candidate |
| `P24-U11-LAND-TREATMENT` | **RESOLVED_WITH_PROTOTYPE_DISPOSITION** | U11 package/prototype land treatment can be used by library/provenance closure | DFM/stencil producer must window EP paste and validate assembly assumptions |

The source files and hashes are listed in `AUTHORITY_DECISION.json`; the
read-only audit is `GEOMETRY_AUDIT.py` and `GEOMETRY_AUDIT.json`. Restricted
or third-party reference CAD was not copied into the public project. Private
Library records are indexed under
`package-authority-u11-u12-20260918`.
