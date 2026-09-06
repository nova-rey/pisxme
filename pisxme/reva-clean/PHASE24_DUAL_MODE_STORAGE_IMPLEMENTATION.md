# Phase 24 dual-mode storage implementation

Status: `IN PROGRESS — native symbol/connector integration landed; mode
control, copper fixture, and full electrical validation remain open`
(2026-09-06).

The active implementation is the storage-local two-bridge topology:

`CM5 USB -> HD3SS6126RUAR -> {TUSB9261 SATA | JMS583-QHFA3A NVMe}
-> HD3SS3412RUAR -> TE 1-2199230-4 M-key Socket 3`.

The selected JMS583 is factory mask-ROM qualified for baseline use. Its
optional SPI NVRAM remains DNP. This does not close procurement: JLC's exact
part listing currently reports zero stock and broker listings are not an
authorized source.

## Land-pattern artifacts

`phase24_generate_dual_mode_storage_libraries.py` emits native
footprints from retained authorities:

- `JMS583_QFN64_8x8.kicad_mod`: QFN64, 0.4-mm pitch, 8-mm body, 64 pads.
- `HD3SS6126_RUA0042A.kicad_mod` and `HD3SS3412_RUA0042A.kicad_mod`: TI
  RUA0042A, 42 pads plus exposed pad 43. Separate names preserve distinct
  pin ownership despite the common package drawing.
- `TE_1-2199230-4_MKEY.kicad_mod`: 67 contacts with the TP-053 M-key gap.

The generated files are review candidates until native pad-by-pad comparison
against the TE DXF/application drawing and TI/JMicron package pages is signed
off. The library audit is intentionally structural; it does not assert PCB
connectivity.

## Current evidence

`STORAGE.kicad_sch` now contains U7 plus native U8 JMS583, U9 HD3SS6126,
U10 HD3SS3412, and J3 TE 1-2199230-4. The B-key J3 is removed. The saved
sheet parses under KiCad 10.0.5, and `phase24_dual_mode_storage_schematic_audit.py`
passes; its negative-control copy fails when a required M-key label is removed.
Native ERC currently reports 205 violations, so this is not an ERC pass. The
report is retained as evidence and includes inherited abstract-sheet issues,
off-grid generated symbol endpoints, and isolated labels requiring cleanup.

`PHASE24_DUAL_MODE_STORAGE_PLACEMENT.kicad_pcb` is a disposable native
placement candidate derived from the selected storage macro ancestor. It
contains the M-key J3 and U11/U12/U13 footprints with physical pad nets. KiCad
10.0.5 loads it and reports 1,013 violations / 482 unconnected items; this is
expected evidence that the candidate is not routed or promoted. Existing U8/U9
references on the ancestor were preserved, so the new storage silicon uses
U11/U12/U13 consistently.

## Remaining implementation gates

1. Add native symbols whose pin numbers exactly match the retained TI tables,
   JMS583 datasheet, and TP-053 socket table.
2. Replace the old B-key J3 in the authoritative `STORAGE.kicad_sch`; do not
   patch a PCB-only connector.
3. Add the two selector truth tables and a latched AUTO/FORCE SATA/FORCE NVMe
   control circuit. Validate inactive-state isolation and PEDET-empty safety.
4. Complete the JMS583 reference circuit: rails, 25-MHz crystal, REXT, reset,
   VBUS detect, USB/PCIe AC coupling, internal-regulator inductor, and DNP
   optional SPI NVRAM.
5. Recalculate the storage 3.3-V budget for NVMe inrush/transient and both
   bridges before PCB regeneration.
6. Build and route a complete native fixture, then integrate only after forced
   SATA, forced NVMe, AUTO, empty, reset, and inactive-state audits pass.

No production PCB change is claimed by the footprint generation alone.

## USB3 fixture discriminator — 2026-09-06

`phase24_usb3_dual_mode_isolated_fixture.py` created a disposable native
fixture containing only J7, U12, U11, and the two JMS583 TX coupling
capacitors. The fixture uses saved pad coordinates and native copper; it does
not inject graph edges. It was rejected as a route implementation, not as an
architecture decision: the first attempt drove straight into the dense U12
QFN pad field, producing six track crossings and twenty shorting findings in
native DRC. The remaining findings include inherited package mask/clearance
and unconnected pads because this is a deliberately partial fixture.

The next implementation must use package-side dogbones and layer-separated
escapes outside the U12 pad field, then reconnect the four USB2 pins from an
explicit CM5 port-0 source. The current CORE_CM5 sheet exposes `CM5_USB3`
and SERVICE USB2 but does not yet expose CM5 port-0 USB2 `USB3-0-D_P/N` as
hierarchical storage nets. That is an authority/interface omission to repair
before production regeneration; `CM5_USB2_DP/DM` must not be invented as a
replacement without tying them to the actual CM5 port-0 pads.

## CM5 USB2 source correction — 2026-09-06

The omission was repaired in the schematic authoring path. CM5 carrier pads
134/136 (`USB3-0-D_P/N`, the USB2 companion of port 0) now export explicit
`CM5_STORAGE_USB2_DP/DM` global nets from `CORE_CM5`; the storage selector
uses those same nets. Native root netlist export now shows J7.134 to U12.8
and J7.136 to U12.7 on the same nets. U12-to-JMS583 USB3 names were also
normalized to `USB_TXP1/TXN1` and `USB_RXP1/RXN1`. The prior isolated PCB
fixture predates this source correction and remains rejected evidence.

The follow-on isolated fixture was regenerated with the corrected source and
package-side dogbone intent. It is still rejected as implementation evidence:
the U12 pad-field direct shorts were removed, but the current B.Cu lane order
crosses at the staggered through-via escapes. Native DRC reports 11 crossing
findings and 22 shorting findings in the current route, plus expected partial
fixture/unconnected/package-rule findings. The next bounded repair is to make
the B.Cu corridor ordering match the staggered escape ordering; no component
or architecture change is indicated.

The fifth isolated routing iteration corrected the B.Cu destination ordering
and reduced native DRC shorting findings to 17. Remaining crossings are
localized to the CM5 source fanout, the final U12 dogbones, and the separate
U11 selector-side pair fanouts. These are still route implementation defects;
the next experiment will partition those corridors by permitted copper layer.

## TI RUA0042A footprint correction — 2026-09-06

The retained TI package drawing identifies RUA0042A as 9.0 x 3.5 mm with a
17/4/17/4 perimeter. The previous generated footprint was a square,
10/10/10/10 construction and placed pads 11 and 21 at the same coordinate.
The generator now emits the documented perimeter, and the selector geometry
audit passes for both selectors. The placement candidate was regenerated from
that corrected library.

The latest isolated native USB3 fixture uses the corrected pad positions and
orthogonal package-side dogbones. Native DRC reports zero shorting findings;
seven track crossings remain in the final dogbones/selector continuation and
are not accepted as a routing pass.

The TI example board layout also specifies 0.60 mm perimeter-pad length;
the generator now uses 0.60 x 0.25 mm pads for both selectors. The geometry
audit still passes after this correction and the isolated native fixture
remains zero-short. Track-width findings in the fixture are retained and
must be resolved against the approved JLC routing rule before promotion.

The sixth iteration split RX/TX source fanout layers, but native DRC showed
the B.Cu source trunk now colliding with the selector-side U11/U12
continuation. It is rejected as a shared-corridor route implementation; the
next fixture must reserve separate local corridors for source escape and
selector continuation.

The seventh/eighth escape trial uses actual CM5 pad-order monotonic routing
and outward-Y U12 dogbones. It removes the prior source-field crossing class,
but native DRC still finds via-to-neighbor clearance at the dense package
edge and inherited selector-continuation crossings. It is rejected as a
fixture route implementation. The next bounded repair moves the vias farther
outside the package and gives selector continuation a separate corridor.

The subsequent orthogonal SMD-pad-escape experiment is retained as
`PHASE24_DUAL_MODE_STORAGE_USB3_ISOLATED17-drc.rpt` and rejected. It used
native pad/via/track objects, but introduced real collisions between the
selector continuation, CM5 source fanout, and cap-side return corridors.
That result is a route implementation failure, not evidence against the
dual-mode architecture or the corrected TI package. The committed generator
remains at the preceding zero-short baseline; no production PCB was promoted.

The local-cap/F.Cu corridor experiments are retained as
`PHASE24_DUAL_MODE_STORAGE_USB3_ISOLATED18-drc.rpt` and
`PHASE24_DUAL_MODE_STORAGE_USB3_ISOLATED19-drc.rpt`. Moving C86/C87 locally
reduced the artificial detour, but the F.Cu selector paths still intersected
native CM5-source escape vias and package-edge corridors. They are rejected
as a route implementation class. The saved generator remains the committed
zero-short baseline pending a proper two-layer via-handoff construction.

The explicit via-handoff trial is retained as
`PHASE24_DUAL_MODE_STORAGE_USB3_ISOLATED21-drc.rpt` and rejected. Native DRC
found shorts between handoff vias and the inherited CM5 source corridor, plus
crossing split-cap paths. The experiment confirms that handoff vias must be
planned with a reserved corridor; inserting them into existing copper is not
a valid repair. The generator was restored to the committed zero-short
baseline.

The JMS583 package audit then exposed that the prior generator had silently
emitted only 42 pads for the 64-pin device. The generator was corrected to
emit a 16/16/16/16 QFN64 perimeter, and the placement candidate was
regenerated. Structural audits now pass against the corrected native U11
package. USB3 isolated report
`PHASE24_DUAL_MODE_STORAGE_USB3_ISOLATED24-drc.rpt` is retained from the
first route against that corrected geometry: it reports no selector/source
shorting items and five localized track crossings. It is not a route pass,
but it supersedes results obtained with the malformed 42-pad footprint.
