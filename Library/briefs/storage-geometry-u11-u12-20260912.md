# Storage U11/U12 geometry evidence brief

Date: 2026-09-12  
Question: What numeric fabrication and package constraints from the requested
public sources bound the PiSXMe U11 JMS583 and U12 HD3SS6126 storage geometry?

## Finding

The requested JLCPCB pages provide usable Tier-1 manufacturer capability bounds
for a six-layer FR-4 board. The requested TI pages provide Tier-1 package
identity and package drawing numbers for U12. They do not authorize a layout or
resolve a package conflict in the retained project footprint.

The critical conflict is U12 pitch. TI identifies RUA as a 42-pin WQFN with
nominal body 9.00 x 3.50 mm, 0.8 mm maximum height, and 0.50 mm pitch. The
retained project footprint has the matching 42 signal pads, 0.60 x 0.25 mm
lands, and 2.05 x 7.55 mm thermal land, but its pad centers advance at 0.40 mm.
This is unresolved package evidence, not permission to change the footprint or
to route from it.

## Component context

| Ref | Retained project identity | Numeric package evidence | Status |
|---|---|---|---|
| U11 | `JMS583-QHFA3A`, `JMS583_QFN64_8x8` | QFN64, 8.0 x 8.0 mm, 0.40 mm pitch, 0.15-0.20 mm terminal width, 4.46 x 4.46 mm exposed pad; project-derived from the existing JMicron authority record | Package basis established; paste, mask, and courtyard production review remain open |
| U12 | `HD3SS6126RUAR`, `HD3SS6126_RUA0042A` | TI RUA WQFN, 42 pins, nominal 9.00 x 3.50 mm, body limits 8.9-9.1 x 3.4-3.6 mm, height 0.6-0.8 mm, generic pitch 0.50 mm, thermal pad 43 | Critical 0.40-vs-0.50 mm pitch conflict open |

The retained U12 footprint matches TI's example signal land size (0.60 x
0.25 mm) and exposed thermal land (2.05 x 7.55 mm); its 0.40 mm pad-center
pitch does not match the TI generic package-view pitch. The local footprint
hash is `9490928521cf2d8677da7bf188fc265664095d99978ae7c1f038da07adf33ffd`.
The U11 footprint hash is
`11918576998884d5885debb500966b20804f7d14394212379fad31d0e5669c05`.

## Fabrication bounds relevant to these escapes

JLCPCB's general capability page (`jlcpcb-capabilities-20260912`) states
multilayer 1-oz trace/space minimum 0.09/0.09 mm, 2-oz minimum 0.15/0.15 mm,
minimum drill 0.15 mm, minimum via diameter 0.25 mm, via-hole spacing 0.20 mm,
pad-to-track clearance 0.10 mm, different-net SMD pad spacing 0.15 mm,
via-to-track clearance 0.20 mm, and multilayer 1-oz PTH annular ring 0.20 mm
recommended / 0.15 mm absolute minimum. The stated standard process does not
support blind or buried vias. The page advertises ±10% impedance tolerance.

The six-layer page (`jlcpcb-6layer-20260912`) lists board thicknesses 0.8,
1.0, 1.2, 1.6, and 2.0 mm; ±10% thickness tolerance at 1.0 mm and above;
±0.1 mm below 1.0 mm; 0.09 mm trace/space; 0.15/0.25 mm minimum via
hole/diameter; via-in-pad support; and 1/2-oz outer with 0.5/1/2-oz inner
copper. Its example stackup is SIG/GND/PWR/SIG/GND/SIG.

These capability values support the existing bounded U11 local exception of
0.10/0.10 mm XIN/XOUT copper and ordinary 0.60/0.30 mm through-vias as a
manufacturing comparison. They do not close native DRC, assembly, or package
identity gates. The JLC pages disagree on six-layer maximum board dimensions
(656 x 586 mm on the general page versus 660 x 475 mm on the six-layer page);
this does not affect local U11/U12 geometry.

## U12 package drawing facts

`ti-hd3ss6126-ds-slas975a` is the TI datasheet SLAS975A (November 2013,
revised August 2015) with package outline RUA0042A dated 03/2020. Numeric
package facts are:

- RUA WQFN, 42 signal pins; nominal body 9.00 x 3.50 mm; generic package
  view says 0.50 mm pitch and 0.8 mm maximum height.
- Package outline limits: 8.9-9.1 mm body length, 3.4-3.6 mm body width, and
  0.6-0.8 mm height.
- TI example board layout: 42 lands at 0.6 mm with 0.25 mm land width;
  exposed pad 43 with 2.05 x 7.55 mm callouts; 0.20 mm typical vias are
  optional by application.
- The package thermal pad must be soldered to the PCB. If vias are placed
  under paste, TI recommends filling, plugging, or tenting them.
- TI's example stencil is based on 0.125 mm thickness and 69% printed solder
  coverage under the package.

The TI product page (`ti-hd3ss6126-product-20260912`) independently confirms
the RUA 42-pin package and 3.5 x 9 mm size, and links the same Rev. A datasheet
dated August 31, 2015. It is the same manufacturer evidence family, not an
independent pitch authority.

## Classification, confidence, and limits

- JLC capability pages: primary manufacturer evidence, Tier 1, confidence high
  for advertised capability values and medium for applying them to this exact
  board without DFM review.
- TI datasheet and product page: primary manufacturer/package evidence, Tier 1,
  confidence high for U12 package body, pin count, thermal-pad requirement,
  and published land/stencil examples.
- Retained U11/U12 footprints and project package numbers: project-derived
  evidence, Tier 3, confidence high for what is stored and measured, but not
  sufficient to overrule a conflicting manufacturer package drawing.
- No requested source provides a JMS583 package drawing; no new U11 external
  package assertion is made here.
- No source reconciles U12's retained 0.40 mm pitch with TI's 0.50 mm pitch.
  Package authority must resolve this before U12 geometry is treated as
  authoritative.

References: `Library/indexes/storage-geometry-u11-u12-20260912.json`;
`Library/provenance/sources.json`; project-derived
`pisxme/reva-clean/authority-inventory/primary-docs/storage-upgrade/jms583/JMS583_QFN_LOCAL_ESCAPE_MANUFACTURING_BASIS.md`;
`pisxme/reva-clean/PHASE24_JMS583_LAND_PATTERN_RECONCILIATION.md`;
`pisxme/reva-clean/PiSXMe_RevA_Clean.pretty/JMS583_QFN64_8x8.kicad_mod`;
`pisxme/reva-clean/PiSXMe_RevA_Clean.pretty/HD3SS6126_RUA0042A.kicad_mod`.

Public source URLs:

- https://jlcpcb.com/capabilities/Capabilities
- https://jlcpcb.com/6-layer-pcb
- https://www.ti.com/lit/ds/symlink/hd3ss6126.pdf
- https://www.ti.com/product/HD3SS6126
