# Phase 24 RTL9210B-CG Path-B qualification

## Current checkpoint — V760 five-net SPI fixture (2026-09-09)

V760 is the current positive five-net SPI fixture. It uses the V748 vertical
U2 endpoint field and the V754 source fan-out. Native KiCad 10.0.5 DRC reports
0 violations and 40 unrelated expected opens. The saved-board audit
`phase24_rtl9210b_spi_full_v760_audit.py` passes all five native endpoint
connectivity assertions and five source-track negative controls. This closes
the isolated SPI routing fixture, not the complete RTL9210B or Path-B gate.

V761 places Y1/C1/C2/R1 in an in-board support pocket on the V760 geometry.
V762-V766 are rejected first-pass crystal routes; they exposed source-pad,
transition, and corridor interactions. V767 routes XTAL_IN, XTAL_OUT, and
RSET without signal DRC errors. V768/V769 are rejected GND branches; V770
removes the final GND clearance issue. V771/V772 clean fixture annotation,
and V772 reports zero native DRC violations with 35 expected unrelated opens.
The saved-board V772 support audit passes XTAL_IN, XTAL_OUT, RSET, and GND
connectivity, with negative controls passing for the three signal nets.

V773 is a rejected first rail/control placement: C3/RSET and R2/R3/SPI
corridors collided. V774/V777 are electrically clean control-placement
variants with only C4 silkscreen warnings. V775/V776/V778 are rejected
control-route implementations; direct F.Cu and the first B.Cu handoff class
cross the proven SPI source/endpoint field. The next control route must use
an outboard return corridor or adjust only the control resistor placement.

V779 tested split upper/lower F.Cu control corridors from the V777 placement.
Native DRC found real PEDET/CLKREQ_N crossings and shorts at the resistor
approaches, a no-connect U1-pad contact, and source-field interaction. It is
rejected as a route implementation. The next class must move the control
resistors farther from the QFN perimeter and U2 endpoint columns.

V783 is a negative generator result: a conservative F.Cu-only obstacle search
could not find a PEDET route to the V777 R2 endpoint in the saved field. It
did not alter the board and is not a native DRC result. Mixed-layer routing
and/or local control-resistor relocation remain the next bounded experiments.

V784/V785 are rejected control-route variants. V786 and V787 progressively
removed their crossings but retained one native control-corridor failure each.
V788 is the current positive disposable control basis. It moves R2/R3 to a
separated top pocket and uses distinct PEDET/CLKREQ_N return corridors.
Native DRC has zero electrical violations and three inherited silkscreen
warnings. `phase24_rtl9210b_controls_v788_audit.py` passes native U1-to-R2/R3
connectivity and removal negative controls. This is local control closure
only; it does not close the complete RTL9210B Path-B qualification.

V789/V790 are rejected PERST_N route trials. Native DRC showed that the outer
B.Cu corridor to J1.50 is not the limiting geometry; the source transition
collides with the accepted CLKREQ_N launch or the retained SPICLK via. The
next bounded class is a co-authored U1-side PERST_N/CLKREQ_N/SPI escape.

V791/V792 are rejected co-authored U1-side trials. V791 retained control/SPI
clearances; V792 added PEDET, CLKREQ_N, and ISOLATEB contacts near the QFN.
The native reports preserve the result: the outer PERST_N corridor is not the
limiting geometry, but the QFN departure fanout still needs a dedicated
allocation.

V808 is the current positive orientation-180/co-moved-support control basis.
It has zero native DRC violations, and
`phase24_rtl9210b_orientation180_v808_audit.py` proves PEDET U1.8→R2.1,
CLKREQ_N U1.13→R3.1, and PERST_N U1.14→J1.50 with independent track-removal
negative controls. The 42 incomplete connections are inherited from the
disposable, otherwise unrouted fixture. SPI, rails, USB, lane, flash, and
firmware gates remain open.

V809/V810 extend the V808 rotated basis with SPICS. V809 was rejected for a
PEDET-shelf crossing; V810 moves the upper SPICS leg to B.Cu, includes the
U2 GND return, and passes native DRC with zero violations. Its saved-board
audit and track-removal negative control pass for U1.24→U2.1. V811–V813 are
rejected SPISO/SPICS source co-routing attempts; the remaining SPI source
allocation is still open.

V793/V794/V795 are rejected PERST_N QFN-escape variants. Their outer route
sections remain clear, but the local departure repeatedly contacts adjacent
U1 no-connect/control pads or the retained SPI/PEDET field. This establishes
the next experiment as a complete three-net QFN escape allocation, not a
single-net PERST adjustment.

V796/V797 are rejected orientation-180 control experiments. V796 used
uncoupled direct corridors; V797 reordered them but retained conflicts with
the crystal/RSET pocket and J1 lane pads. The orientation class remains a
credible next placement experiment only with its support pocket co-moved
with the QFN; no Path-A or production conclusion changes.

V748 is the current positive placement basis for the remaining RTL9210B SPI
allocation. Starting from the native-clean V730 U1-at-90-degree basis, U2 was
rotated 90 degrees and placed with its SPI endpoint column at x=105 mm. The
native KiCad 10.0.5 DRC reports zero violations and 45 expected/incomplete
connections. Its ordered endpoint field is U2.1 SPICS y=80.0, U2.2 SPISO
y=78.8, U2.5 SPISI y=75.2, U2.6 SPICLK y=74.0, and U2.7 SPISO3 y=72.8.
This is a placement discriminator only; no SPI channel is claimed closed by
V748.

V746 and V747 are rejected disposable three-channel allocations from the
same U1/U2 placement family. V746 had a source-field SPISO/SPISO3 crossing
and a clearance violation. V747's alternate B.Cu SPICS corridor produced
two source-field shorts with SPISO and SPISO3. Both are route-implementation
failures preserved as raw evidence, not package or architecture rejection.
The next experiment should route against the V748 vertical endpoint field
with a co-authored source escape, retaining the standing 0.20 mm track and
ordinary-via rules.

V749 routes SPISO3 alone from U1 to the vertical U2.7 endpoint with an
ordinary F.Cu/B.Cu/F.Cu transition and reports zero native DRC violations and
44 expected opens. V750 adds SPICLK through a separate outboard B.Cu channel;
it also reports zero native DRC violations and 43 expected opens. These are
positive channel-allocation evidence, not full SPI closure. SPICS, SPISO, and
SPISI still require co-authored routing and saved-board connectivity audits.

V751 attempted to add SPICS and SPISO to the V750 basis. Native DRC found
five violations: source-transition shorts involving SPICS/SPISO and
SPISO3/SPISO, plus one SPISO/SPICS B.Cu crossing. It is rejected as a
route-implementation failure. The failure is localized to the QFN source
field and return-shelf allocation; it does not invalidate the V748 placement
or the clean V749/V750 channel proofs.

V752 is an endpoint-free five-net QFN source-fanout probe. It confirms that
the outer/source channels can be spread to ordinary transition locations,
but native DRC reports two real 0.20 mm clearance failures between the
adjacent SPICLK/SPISI escapes (actual clearance 0.1505 mm). Its five
single-layer dangling-via warnings are expected because this fixture stops
at the transitions. V752 is rejected as a complete source fan-out; the next
attempt must co-author the adjacent SPICLK/SPISI dogbones before adding
endpoint corridors.

The earlier V702 U1.17 RTL_5V closure remains part of the inherited positive
support lineage; it is not the current SPI checkpoint.

The disposable saved-board lineage `PHASE24_RTL9210B_SUPPORT_RELOCATION_5V_U117_V702.kicad_pcb`
is the current positive local support candidate. V702 adds a two-via F/B/F
handoff from U1.17 around the existing 3V3/1V1 barrier, while retaining the
V699 U1.33-to-C5 trunk. Native KiCad 10.0.5 DRC reports 0 violations and 24
unconnected pads. The V702 native endpoint audit passes, including a targeted
negative control that removes the new `(102.2,76.2)` handoff via and observes
the required connectivity failure. This closes only the U1.17 RTL_5V local
rail endpoint; the remaining RTL9210B source-field, control, SPI, reference,
lane, power, firmware, and productization gates remain open.

V703, V705, V706, and V707 are rejected disposable SPICS route trials from
the V702 basis. They exposed, respectively, 1V1-via, 1V1/5V-corridor,
upper-QFN/load-spine, and adjacent-SPISO conflicts. V707 reduced the result
to three native DRC violations but is not promoted. These are route
implementation failures, not package or architecture rejection; the next
SPI attempt must co-author the QFN source escape and retained rail field.

The V712 orientation discriminator rotates U1 180 degrees about the exposed
pad and moves U2 north/west, placing the SPI edge toward open acreage. After
native zone refill it has zero DRC violations and 45 expected opens. V718
adds SPICS plus an ordinary local GND return and still has zero native DRC
violations; its saved-board SPICS endpoint audit and trunk-removal negative
control pass. V713/V714/V715/V716/V719/V720/V722 remain rejected route
implementations. V712/V718 are disposable placement/channel bases only.


Status: **KEEP A / CONTINUE B**. Path A remains the protected production
architecture and is not modified. Path B is an active isolated candidate,
not authorized for destructive replacement or production integration.

V723, V724, and V725 are rejected SPISO-only continuations from V718.
V723's B.Cu endpoint approach conflicted with the SPICS source shelf; V724
reduced that conflict but placed the handoff too close to the SPICS source;
V725 moved it toward the QFN and clipped adjacent SPISO3/SPISO2 pads. These
are route-implementation results; the remaining task is a complete QFN
source-field allocation across all five SPI nets.

The current positive multi-channel basis is V735: U1 at 90 degrees with U2
at 90 degrees, SPICS and SPISO connected through separated F/B corridors,
native DRC 0, and saved-board endpoint/trace-removal audits passing. V736,
V737, V738, V739, V740, V741, V742, V743, V744, and V745 are rejected
three-channel route allocations with documented source-via or corridor
crossings. They do not reject the rotated placement; the next attempt must
co-author source-via spacing and the remaining SPI channels.

## Latest implementation evidence — 2026-09-09

V668 tested a distinct five-net source-field allocation on the native V595
support/rail base: staggered QFN escapes, separated B.Cu channels, and
bottom-side U2 returns. Native KiCad DRC found 49 violations and 11 opens,
including true source-field shorts/crossings. It is rejected as a route
implementation and retained in
`PHASE24_RTL9210B_SPI_CHANNELIZED_NATIVE_V668.md`. The result narrows the
next experiment to coherent U1/U2/flash support-island relocation or complete
source/rail regeneration. It does not change Path A or reject the RTL9210B
package/architecture.

V670 then applied the consultant-recommended V35/U2-left lower-3V3
co-author class. Native DRC found 24 violations and 21 opens, with the new
U1.39/U1.52 departures crossing retained RTL_1V1/RSET/XTAL/SPI geometry.
V670 is rejected as a route implementation; the V35 SPI/crystal/RTL_5V
basis remains the active source-field lineage. The next experiment must
reallocate the local RSET/3V3 support field coherently.

V674 retained every neighboring U1 pad net and compared four package
rotations. The 90° orientation produced one intentional dangling-tail
warning and no pad short/crossing/clearance error; the other rotations added
6–11 DRC violations. This confirms the RTL9210B package is escapable under
the standing rules. The integrated lower-3V3 work must now co-author the
90° U1.39 escape with the adjacent RTL_1V1 departure.

V676 is the retained adjacent-source basis for that co-authoring step. Starting
from V672, it routes U1.39 RTL_3V3 west to an ordinary transition and turns
U1.40 RTL_1V1 down to a separate transition. Native DRC found 12 findings and
24 expected/incomplete unconnected items, with no signal short, crossing,
clearance, solder-mask, or footprint errors. Its short B.Cu tails are
disposable transition stubs, not completed support routing; extend them to
their native rail collectors independently before treating the field as
connected. The raw receipt is
`PHASE24_RTL9210B_U139_U140_AROUND_V676.md`.

V678 tested F.Cu joins from the V676 source transitions to the existing
collectors. Native DRC found one real RTL_3V3/RTL_1V1 source-field crossing
and single-layer source vias; reject it as a route implementation. The next
bounded class is the separately authored orientation-180 support lineage,
which has native-clean local support fields and different QFN pin ordering.
V679 and V680 tested two crystal-field implementations on that lineage. Both
were rejected by native DRC for real crystal-field shorts/crossings; neither
is evidence against the orientation-180 support placement itself. Their raw
receipts are retained for the next co-authored crystal/source-field attempt.
V681 tested a lower-shelf relocation with a dedicated B.Cu return corridor;
native DRC found 17 violations including crystal shorts/crossings and
board-edge/mounting-hole conflicts. Reject it as a placement implementation;
the next experiment must keep the crystal inside the support envelope and
co-author its escape with the existing fields.
V682/V683 then reused the native-clean support-relocation crystal geometry.
V682 showed that stitching vias alone did not physically connect C1 GND;
V683 added the missing same-net segment and passed native DRC with zero
violations. Retain V683 as the positive crystal-field basis; its 32 remaining
opens are outside the completed crystal network.
V684's direct inner-pad source route was rejected at nine native DRC
violations. V685 then separated the R2/R3 dogbones and approached outer U1.34
through an ordinary transition; native DRC reports zero violations and 30
remaining opens. Retain V685 as the positive RTL_3V3 edge-source basis; the
inner QFN branches and downstream rail endpoints remain open.
V686's first U1.39 inner branch contacted an existing RTL_1V1 via and was
rejected. V687 added the minimum lateral jog; native DRC reports zero
violations and 29 remaining opens. Retain V687 as the positive U1.39
RTL_3V3 branch basis; the remaining 3V3 endpoints are still open.
V688 attempted the U1.52 left-edge branch and was rejected at three native
DRC violations due to the C2 GND return and CLKREQ pull-up geometry. The next
3V3 class must co-author the crystal micro-island and U1.52 escape.
V689 translated the complete crystal micro-island left and rebuilt its nets;
native DRC found 11 real crystal-net shorts/crossings. Reject V689 as a route
implementation and retain the V683 crystal basis plus V687 U1.39 branch.
V692's B.Cu U1.52 route crossed the RSET collector and was rejected. V693
stepped left of that endpoint and passed native DRC with zero violations and
28 remaining opens. Retain V693 as the positive U1.52 branch basis.
V694's first load corridor contacted SPISI and was rejected. V695 moved the
U1.20 descent outside the QFN pad field and passed native DRC with zero
violations and 26 remaining opens, closing U1.20/C3/U2 RTL_3V3 load routing.
Retain V695 as the positive 3V3 load basis.
V696's direct RTL_5V route was rejected for an RTL_1V1 crossing and 3V3-via
clearance. V697/V698 developed the split overpass; V699 removed the final
redundant via and passes native DRC with zero violations and 25 remaining
opens. Retain V699 as the positive U1.33-to-C5 RTL_5V basis; U1.17 remains
open.
V690 moved only C2 and rebuilt XTAL_OUT/GND alongside U1.52; native DRC found
15 violations including crystal shorts and 3V3/CLKREQ and 1V1/GND contact.
Reject the C2-only class. The next experiment must co-author the complete
crystal/support micro-island with verified pad geometry.

V672 provides a positive interior RSET basis with nine inherited warnings and
no signal DRC violations. V673 layered lower RTL_3V3 onto it and found 12
violations/21 opens; it is rejected because the U1.52 departure contacts
RSET and the U1.39 departure violates adjacent USB_DM. The next experiment
must co-author those two QFN source escapes with RSET, rather than add them
independently.

V671 tested the next bounded class by moving R1/RSET and re-authoring the
U1.51 route. Native DRC found 15 violations and 24 opens: the proposed
perimeter collided with lower RTL_1V1 and reached the board edge. V671 is
rejected as a route implementation; the next class is an interior,
co-authored RSET/lower-3V3 field.

## Decision summary

The retained RTL9210B-CG Rev. 1.1 document says the controller combines USB,
PCIe and SATA hosts and automatically switches USB-to-PCIe or USB-to-SATA via
the M.2 PEDET interface. It supports USB 3.1 Gen 2, USB 2.0, UASP, PCIe Gen3
x2, SATA Gen1/2/3, SPI flash, and a 25 MHz reference. This directly addresses
the main reason Path A has four high-speed controllers/switches.

The practical unresolved item is not the SATA/NVMe topology. It is
productization of a virgin RTL9210B: exact Realtek-approved production
firmware/configuration package, licensing/redistribution rights, and a
repeatable initial-programming path for a bare QFN part. Community tools and
binary artifacts prove that the ecosystem exists, but do not close those
rights or variant-compatibility questions.

## Exact proposed Path-B mapping

```text
CM5 USB3 TX/RX + USB2 D+/D-
        -> RTL9210B-CG USB_TXP0/N0, USB_RXP0/N0, HSDP/HSDM
RTL9210B SATA_TXOP/TXON (68/67) -> M.2 contacts 49/47 (SATA-A)
RTL9210B SATA_RXIP/RXIN (64/65) <- M.2 contacts 43/41 (SATA-B)
RTL9210B PCIe_TXOP/TXON_0 (68/67) -> M.2 PETp0/PETn0
RTL9210B PCIe_RXIP/RXIN_0 (64/65) <- M.2 PERp0/PERn0
RTL9210B PCIE_REFCLKP/N (61/62) -> M.2 REFCLKP/N
RTL9210B PERSTBPIN (14) -> M.2 PERST#
RTL9210B CLKREQB (13) <-> M.2 CLKREQ# with required pull-up
RTL9210B GPIO6/PEDET (8) <-> M.2 contact 69 / CONFIG1, with socket/platform pull-up rules
```

The earlier compact mapping above used the SATA pair labels incorrectly and
is superseded by this physical-contact table. The M.2 names are
platform/socket-side PCIe names; the same contacts carry the SSD-side SATA
names. The community M.2 XML and the M.2 reference table both put the PCIe
TX launch on contacts 49/47 and PCIe RX return on 43/41:

| RTL9210B signal | Socket contact | Platform-side name | SSD-side SATA name |
|---|---:|---|---|
| `TXOP/TXON` pins 68/67 | 49/47 | `PETp0/PETn0` | `SATA-A+/SATA-A-` |
| `RXIP/RXIN` pins 64/65 | 43/41 | `PERp0/PERn0` | `SATA-B-/SATA-B+` |
| `REFCLKP/N` pins 61/62 | 55/53 | `REFCLKp/REFCLKn` | not used in SATA |

This table records physical contact authority and avoids treating PCIe
platform-side names as SSD-side directions. The SATA polarity convention and
the RTL9210B mode-specific interpretation of the shared pins still require
the current application circuit or a controlled hardware test; no Path-B
fixture may silently swap these pairs.

Contact 69 is the standard M.2 PEDET/CONFIG1 contact: SATA modules tie it
low, while PCIe modules leave it unconnected and the platform supplies the
pull-up. That establishes the socket-side convention, not yet the complete
RTL9210B pull-up, empty-socket, or power-sequencing circuit.

### WIP hierarchy mapping conflict

The retained community `RTL9210B_ROOT.xml` is **not** a mapping oracle. Its
native netlist attaches RTL pins 68/67 to CN6 contacts 43/41 and attaches RTL
pins 64/65 through C89/C90 toward contacts 49/47. That is opposite the
platform-side M-key contact convention above, where controller TX launches to
49/47 and controller RX returns on 43/41. This is a concrete WIP-CAD mapping
conflict, not a reason to invent a third mapping. The root XML is retained as
negative corroborating evidence and is excluded from production authority.

The standalone `phase24_rtl9210b_m2_mapping_audit.py` asserts only the native
socket contact labels and AC-coupling boundary; it does not bless the WIP
hierarchy's reversed associations.
`phase24_rtl9210b_wip_hierarchy_conflict_audit.py` independently detects and
quarantines that conflict, including a mutation negative control.

The chip pad 69 is the exposed ground pad. It is not M.2 contact 69. The
shared lane-0 assignments above are explicit in the retained pin tables.
PCIe lane 1 (56-59) is not required for a single-lane M-key NVMe design and
must be left according to the final Realtek application circuit, not guessed.

## Support-circuit audit

Closed from the retained Rev. 1.1 document at the qualification level:

- 25 MHz crystal/reference: pins 53/54, clock supply pin 52.
- SPI flash: CS 24, CLK 19, SI 18, SO 23, optional quad pins 21/22.
- Reset: active-low RST_INPIN pin 3.
- Mode: PEDET pin 8, `1 = PCIe`, `0 = SATA`.
- PCIe: REFCLK 61/62, PERSTB 14, CLKREQB 13, hot-plug pin 10.
- Internal rails: 5 V input pins 33/17; internal 3.3 V and 1.1 V outputs
  are for the controller only. External 3.3 V/1.1 V rail connections and
  decoupling must follow the latest approved application circuit.
- RSET pin 51 and exposed ground pad 69 are required design items.
- `ISOLATEBPIN` pin 12 controls PCIe main power in PCIe mode and SATA power
  in SATA mode; SSD 3.3 V power/inrush remains a board-level requirement.
- USB supports SuperSpeed and USB 2.0; no USB-C connector or CC circuit is
  needed for this fixed internal CM5 connection.

Still open for production implementation: exact BOM values/layout from the
latest Realtek application circuit, M.2 socket sideband handling, SSD
3.3-V/inrush budget, thermal measurement, and validation of nonselected
interface behavior when the socket is empty or unpowered.

KiCad 10.0.5 successfully exported native XML netlists from the retained
community `RTL9210b_0.kicad_sch` and `M.2_0.kicad_sch`; those receipts are in
`authority-inventory/rtl9210b/RTL9210B_0.xml` and `M.2_0.xml`. This confirms
the CAD sources parse natively and that their RTL9210B pin names and M.2
PEDET contact are inspectable. It is not a PCB connectivity or ERC/DRC pass.

The support portion of `RTL9210B_0.xml` was independently audited by
`phase24_rtl9210b_corroborating_support_audit.py`. The extracted native
evidence now confirms the WIP source contains USB2/USB3, shared lane-0,
REFCLK/PERST/CLKREQ, PEDET, ISOLATEB, 25-MHz crystal, SPI-flash connector,
RSET, switched rails, and explicit unused-pin records. The detailed extraction
is in `authority-inventory/rtl9210b/RTL9210B_CORROBORATING_SUPPORT_NETLIST.md`.
This narrows B1 and the future fixture plan, but does not close B1–B5: the
source remains a WIP community implementation and still does not establish
PiSXMe M-key sideband ownership, released land-pattern authority, SSD
power/inrush validation, or authorized virgin-chip provisioning.

A secondary-hosted RTL9210 68-pin V203 demo schematic also explicitly lists
an RTL9210B-CG variant and corroborates candidate support values including a
2.2-uH regulator inductor and 12-kOhm RSET. It is retained as
`authority-inventory/rtl9210b/RTL9210B_DEMO_CORROBORATION.md`, but remains
non-authoritative because it is a different host design and does not close
the M-key sideband, SSD power, firmware-rights, or released-land-pattern
gates.

## Firmware and programming

The community firmware repository contains RTL9210B-specific configurations,
firmware binaries, a Windows `UTHSB_MPtool` flow, device configuration dumps,
and an SPI-flash recovery method. It also documents device-specific configs,
Windows-only updater limitations, and known stability-sensitive firmware
versions. This closes technical feasibility of update/recovery research, but
not legal provenance or repeatable virgin-chip provisioning.

Required bring-up experiment before Path-B promotion:

1. Obtain a traceable RTL9210B-CG lot and Realtek/OEM-authorized firmware,
   configuration, and updater package.
2. Assemble an isolated board with accessible SPI flash pads and UART/JTAG
   test pads; program a known-good image/config into a virgin part.
3. Record chip marking, flash MPN, image/config hashes, updater version, and
   USB descriptors in SATA and NVMe modes.
4. Exercise reset, empty socket, forced mode if supported by firmware,
   Linux UASP/TRIM/SMART, sustained I/O, suspend/resume, and recovery.
5. Only then generate production RTL9210B symbol/footprint and integrate it.

## Risk ledger

| Item | State | Evidence / next action |
|---|---|---|
| SATA/PCIe auto-selection | CLOSED at technical qualification | Rev. 1.1 mode table explicitly specifies PEDET and polarity |
| Shared lane-0 pin identity | CLOSED at technical qualification | Rev. 1.1 PCIe and SATA tables agree on 64/65/67/68 |
| Physical M-key contact direction | OPEN / corrected | Platform-side M.2 authority requires TX→49/47 and RX→43/41; retained WIP root XML reverses those associations |
| USB2/USB3 bridge function | CLOSED at technical qualification | Rev. 1.1 USB table and feature summary |
| QFN-68 package existence | CLOSED, corroborated | Rev. 1.1 package statement plus JLC listing |
| Land pattern | OPEN | Community SMD footprint is useful but has bad `through_hole` metadata; recreate and audit |
| Exact support BOM/layout | OPEN | Need current Realtek-authorized application circuit |
| Bare-chip procurement | MEDIUM/OPEN | JLC lists C5143573, QFN-68, SMT; stock/price not exposed in the retrieved page |
| Firmware exists | CLOSED, corroborating | Retained configs/binaries and firmware ecosystem |
| Virgin initial programming | OPEN/HIGH | Community flow targets working enclosures and device-specific configs; run isolated experiment |
| Firmware rights/provenance | OPEN/HIGH | Do not redistribute community binaries without authorization |
| Linux/UASP/TRIM/SMART | MEDIUM | UASP is documented; validate kernel behavior on hardware |
| SSD 3.3-V/inrush/thermal | OPEN | Recalculate for selected SSD envelope and measure |
| Path-A preservation | CLOSED | No Path-A schematic/PCB files were changed |

## Path A vs Path B

| Criterion | Path A: TUSB9261 + JMS583 + 2 selectors | Path B: RTL9210B-CG |
|---|---|---|
| Major bridge/switch ICs | 4 | 1 |
| Native auto SATA/NVMe | External mode control and selectors | PEDET-native, firmware-dependent |
| High-speed routing | USB selector + two bridge branches + socket selector | One USB bridge to socket |
| BOM/assembly | Higher count, more QFN/QFN-like escapes | Lower count, QFN-68 plus flash/support |
| Documentation confidence | Higher for TI parts; JMS583 still open | Strong technical PDF, weaker public provenance |
| Firmware risk | TUSB9261 documented; JMS583 config risk remains | High: initial programming and rights |
| Procurement | JMS583 stock risk; selectors sourceable | JLC identity/SMT listing, current stock/price unresolved |
| Performance | CM5 USB-limited; TUSB9261 SATA <=3 Gb/s | CM5 USB-limited; SATA Gen3/PCIe bridge capability |
| Validation burden | Mode isolation across two switches/bridges | Firmware, mode, and unpowered-state behavior |
| Productization | More conventional/documentable | Smaller but dependent on Realtek/OEM package rights |

Current recommendation: **CONTINUE BOTH pending narrowly defined experiments** —
traceable virgin-chip programming and mode bring-up, plus acquisition of the
current Realtek application circuit. If that experiment closes, Path B is the
preferred migration candidate because it removes both external high-speed
selectors and the second bridge. Until then Path A remains the protected
implementation path.

A third-party 21ic listing advertises V004/V008 reference schematics, a power
consumption report, and a layout guide. The download is login-gated in the
current environment and has therefore been recorded only as a recovery lead
in `authority-inventory/rtl9210b/RTL9210B_REFERENCE_PACKAGE_LEAD.md`; none of
its advertised files are treated as retrieved or authoritative.

## Sources

- Realtek RTL9210B-CG Rev. 1.1 PDF, retained under `authority-inventory/rtl9210b/community-lz1/rtl9210b.pdf`.
- [JLCPCB C5143573 listing](https://jlcpcb.com/partdetail/RealtekSemicon-RTL9210BCG/C5143573).
- [HynixCJR/LZ-1-Backplane](https://github.com/HynixCJR/LZ-1-Backplane), corroborating WIP CAD.
- [congatec AN43 M.2 pinout/reference designs](https://www.congatec.com/fileadmin/user_upload/Documents/Application_Notes/AN43_M.2_Pinout_Descriptions_and_Reference_Designs.pdf), platform-side Key-M contact and PEDET convention cross-check.
- [PCI-SIG specifications](https://pcisig.com/specifications), governing M.2 specification index; the detailed standard remains licensed.
- [bensuperpc/rtl9210](https://github.com/bensuperpc/rtl9210), firmware/configuration and recovery evidence.
- [damnnfo/rtl9210b-firmware](https://github.com/damnnfo/rtl9210b-firmware), firmware/config artifacts.

## Current parallel-candidate checkpoint — 2026-09-08

Path B remains isolated and is still not production-CAD authority. The
current retained evidence was rerun against the live checkout:

```text
authority_audit.py                    PASS
corroborating_support_audit.py       PASS
m2_mapping_audit.py                   PASS
native_netlist_audit.py               PASS
native_netlist_audit.py --negative    PASS (fails as intended)
wip_hierarchy_conflict_audit.py       PASS
pdf_pin_audit.py                      PASS
pdf_pin_audit.py --negative           PASS (fails as intended)
```

The isolated support-route sequence remains an implementation discriminator,
not a promotion: V627 rejects via-in-pad at the strict QFN USB field, and the
latest V653 crystal relocation is rejected for real crystal/rail clearance and
shorting classes. These are route/support-field failures; Path A and the
production storage source are unchanged. The remaining Path-B decision gates
are the authorized application circuit/land-pattern review, complete
support-field route, traceable virgin-part programming, firmware provenance,
SSD power/inrush/thermal validation, and hardware mode testing.

## Live requalification checkpoint — 2026-09-06

The live JLCPCB page was rechecked and its identity/assembly facts are now
captured verbatim as a local source receipt. This improves procurement
confidence but does not convert the page's PCBA-only listing into a verified
quantity-1 bare-chip supply or close firmware rights.

The Path-B evidence package was re-run against the current checkout before
any production-CAD change:

```text
phase24_rtl9210b_authority_audit.py                         PASS
phase24_rtl9210b_corroborating_support_audit.py              PASS
phase24_rtl9210b_m2_mapping_audit.py                         PASS
phase24_rtl9210b_native_netlist_audit.py                    PASS
phase24_rtl9210b_native_netlist_audit.py --negative-control  PASS (fails as intended)
phase24_rtl9210b_wip_hierarchy_conflict_audit.py             PASS
phase24_rtl9210b_pdf_pin_audit.py                           PASS
phase24_rtl9210b_pdf_pin_audit.py --negative-control        PASS (fails as intended)
```

The PDF audit independently checks the retained Rev. 1.1 document for
PEDET's explicit `1 = PCIe / 0 = SATA` mode table, the shared 64/65/67/68
SATA/PCIe lane identity, REFCLK 61/62, PERST 14, CLKREQ 13, ISOLATEB 12,
25-MHz clock, RSET 51, exposed ground pad 69, USB pins, SPI pins, and the
document's explicit Realtek-FAE dependency for exact flash sizing. Its
negative control mutates PEDET text and fails as intended. This strengthens
the technical pin/mode authority but does not close firmware rights,
authorized provisioning, or the production application-circuit gate.

The original isolated implementation baseline is materialized in
`PHASE24_RTL9210B_BRINGUP_FIXTURE.md`. Its saved native PCB has the corrected
QFN-68/M-key mapping, support/test net boundary, and exposed programming
access. The fixture audit and negative control pass; its original native DRC
receipt reports zero violations and 56 intentionally unrouted items. That
receipt is historical baseline evidence. Current routed-fixture work is
tracked in `PHASE24_RTL9210B_SUPPORT_ROUTE_EXPERIMENTS_20260907.md` and the
live Phase 24 status, where the GND-plane candidate has 45 unconnected items.
Neither count is waived; the current fixture remains a design-evidence
candidate, not a routed production candidate.

The retained native straight-line RTL9210B PCB fixture remains rejected by
its raw KiCad report (`102` DRC violations, including crossings and a short).
That fixture is incomplete and is classified as route-implementation failure;
it is not evidence against the controller architecture. No Path-A source or
production PCB was changed.

The earlier apples-to-apples recommendation was **CONTINUE BOTH**; it is
superseded by the native lower-QFN DFM result documented below.
Path B materially reduces the high-speed IC count and removes both external
selectors, but it has not yet closed the two productization gates that matter:
traceable virgin-part programming/configuration and authorized firmware
provenance. The current JLC/LCSC listing is an assembly/procurement lead, not
an independently verified stock-depth or quantity-1 quote; JLC itself states
that live quantity and price appear during the order/product-detail flow
([JLC parts guidance](https://jlcpcb.com/help/article/searching-for-products)).

The previously proposed standalone Path-B bring-up fixture is retained as
historical qualification context, not a production prerequisite. The next
production action is to preserve Path A and continue the approved plan.
The next narrowly defined experiment was a standalone Path-B bring-up fixture
with the corrected SMD QFN-68 land pattern, complete support circuit, exposed
SPI-flash/programming access, and the corrected M-key lane mapping. It must be
held outside production CAD until a traceable RTL9210B-CG lot can be
programmed and verified in both SATA and NVMe modes. This preserves Path A as
the fallback while advancing the candidate on the evidence that can actually
change the decision.

## Path-B DFM status — route allocation remains open

U1.39 and U1.40 have 0.4 mm center spacing and 0.2 x 0.9 mm pads. The strict
ordinary-via/0.20-mm-clearance contract makes a via-between-pads escape
unavailable, but that does not prove the package cannot be escaped: the pads
may leave the QFN on separated F.Cu channels before transitioning elsewhere.
V663, V664, and the 2026-09-09 V665 discriminator all rejected their specific
source-field allocations with real crossings/shorts; none is a clean complete
QFN escape proof. V665's 37 violations were caused by the proposed
RTL_3V3 channel colliding with retained 1V1/SPI geometry.

Disposition: **PACKAGE DFM CLAIM CLOSED; COMPLETE SOURCE-FIELD ROUTE OPEN**.
V666 is a clean native discriminator using the real audited footprint: U1.39
and U1.40 leave on separated planar F.Cu channels under unchanged 0.20-mm
width/clearance and ordinary-via rules, with 0 DRC violations, 0 unconnected
items, and 0 footprint errors. No via-in-pad or rule relaxation was used. The
complete integrated QFN field still requires coordinated allocation and
native DRC/connectivity; V666 is not full Path-B closure. Path A remains the
protected fallback; Path B remains a serious comparison candidate.
## CURRENT ROUTING CHECKPOINT — V780–V782 (2026-09-09)

The V780–V782 disposable route trials are rejected implementation variants,
not architecture decisions. V780 shorted SPICS into the crystal-support GND
pad; V781 avoided that pocket but failed native crossings/clearances near the
QFN endpoint field and reference planes; V782 failed native crossings between
the outboard PEDET/CLKREQ_N B.Cu corridors and retained SPISI, plus local U1
pad and resistor-feed clearances. The last clean combined support basis is
V772. Preserve all reports as raw evidence and continue with a new local
control-channel allocation from V772/V777.

## CURRENT ROUTING CHECKPOINT — V814 (2026-09-09)

V814 is rejected route evidence. It paired the SPICS and SPISO source
dogbones from the clean V810 basis, but native DRC found three real local
conflicts: SPICS crosses the retained U2 GND branch and PEDET shelf, and the
SPISO transition via is too close to the SPICS lower jog. The report contains
3 violations and 40 expected incomplete connections. V810 remains the last
clean combined basis; V814 does not change the Path-B architecture decision
and no production CAD or Path-A artifact changed.

V815/V817/V818/V819 tested separate SPISO transitions against V810 and were
rejected by native DRC (1, 2, 1, and 1 real violations). V820 co-authored the
two adjacent departures and was rejected with 3 native violations: one
crossing plus dangling SPICS transition artifacts. These results are saved
route evidence only; they do not close SPI or reject Path B. V810 remains the
last clean combined basis.
V821 tested translating U2's SPI-flash endpoint 10 mm south; its placement
probe passes native DRC with 0 violations and 42 expected incomplete
connections. V822's direct five-net probe is rejected with 11 native
violations and 37 expected incomplete connections. The move remains a
candidate placement class, not a promoted route.
V823 is the first clean two-net source allocation after V810. Native DRC
reports 0 violations and 40 expected incomplete connections; its saved-board
audit passes SPICS and SPISO endpoint assertions and trace-removal negative
controls. This is a positive routing primitive, not full SPI or Path-B closure.
V824 added staggered source transitions for the remaining three SPI nets but
was rejected by native DRC with 14 violations and 37 expected incomplete
connections. The failures are source-field/corridor implementation issues;
no Path-A or production artifact changed.
V825 returned to the V777/V772 placement class to retain the complete SPI
field while testing separated control-resistor approaches. Native DRC rejects
the first route with 7 violations and 34 expected incomplete connections,
including CLKREQ_N/SPISI, PEDET/SPISO-transition, and C5 GND interactions.
It is route evidence only; the V772 complete-SPI/support basis remains valid.
V828 tested outboard F.Cu control columns while retaining the complete V772
SPI/support field. Native DRC rejected it with 4 violations and 33 expected
incomplete connections, including control-to-SPI clearance, PEDET-to-M.2
launch conflict, and a U2 GND thermal issue. It is route evidence only.
V829 tested immediate local control-resistor placement beside U1 and was
rejected with 4 native violations and 33 expected incomplete connections.
V830 angled the launches but was rejected with 10 violations and 33 expected
incomplete connections. These remain local control-route evidence only;
V772 remains the complete-SPI/support basis.
V831 tested a vertically split local control pair with opposing QFN dogbones
and was rejected by native DRC with 6 violations and 33 expected incomplete
connections. The failures are local pad-field/mask/clearance interactions;
the next class must move the control pair coherently away from the SPI field.
V832's far-outboard control-island placement passes native DRC with 0
violations and 35 expected incomplete connections. V833's first B.Cu route
is rejected with 6 violations and 33 expected incomplete connections because
the source vias/corridors intersect retained SPI geometry and reach the board
edge. The placement remains feasible; the route is rejected.
Correction: V832's Y=90 resistor coordinates are outside the disposable
Y=40–85 outline, so its zero-violation result is not mechanical feasibility
evidence.
V842 tested a 90-degree U2 rotation for a pin-order alternative. Native DRC
rejected the placement with 11 violations and 45 expected incomplete
connections because the rotated flash field overlaps retained R1/Y1 support
geometry and a GND thermal region. It remains local placement evidence only.
V838 tested a perimeter PERST_N route from V837 and was rejected with 3
native violations and 32 expected incomplete connections. V839 offset the
source transition but was rejected with 4 violations and 32 expected
incomplete connections, including SPISO/SPISO3 corridor shorts and adjacent
U1 pad-field clearance. PERST_N remains open.
V840 reduced the PERST_N route to 2 native violations and 32 expected
incomplete connections; its outer corridor is clear but the source track
contacts U1 pad 15. V841 changed the dogbone direction and was rejected with
4 violations. V840 remains the better candidate; PERST_N source escape is
still open.
V834 is the corrected in-outline control placement probe and passes native
DRC with 0 violations and 35 expected incomplete connections. V835 and V836
are rejected route implementations with 5 and 3 violations respectively.
V837 reverses the control endpoint order and passes native DRC with 0
violations and 33 expected incomplete connections; its saved-board audit
passes PEDET/CLKREQ_N endpoints and trace-removal negative controls. Full
PERST_N and remaining support validation remain open.
V843 co-moved the crystal/RSET support from the 90-degree rotated U2 field
and passes native DRC with 0 violations and 45 expected incomplete
connections. V844's 270-degree orientation has no electrical DRC violations
and only 3 silkscreen warnings; its SPISI/SPICLK/SPISO3 order is monotonic
relative to U1. V845's direct three-net probe was rejected with 9 native
findings and 42 expected incomplete connections. The orientation remains a
candidate routing basis.
V846's ordered three-net 270-degree fanout was rejected with 10 native
findings and 42 expected incomplete connections. V847 moved the controls
clear and was rejected with 7 native violations and 42 expected incomplete
connections, dominated by SPISI transition/reference-zone clearance. The
270-degree placement remains a candidate source-field basis.
V826 tested B.Cu-separated PEDET/CLKREQ_N approaches on V777 and was rejected
with 6 native violations and 33 expected incomplete connections. V827 moved
the source transitions laterally and was rejected with 9 violations and 33
expected incomplete connections. These are local control-routing failures;
V772 remains the valid complete-SPI/support basis.

V850 is a valid partial routing primitive, not a closure result. It derives
the board from V844, removes stale local SPI/GND tracks, relocates the local
PEDET/CLKREQ_N controls, and routes SPISI, SPICLK, and SPISO3 in monotonic
source-to-target order to the 270-degree U2 field. Native KiCad DRC reports no
electrical violations (one isolated B.Cu GND-fill warning only), and the
saved-board audit passes each endpoint plus a disposable trace-removal
negative control for each net. SPISO, SPICS, PERST_N, and complete support
validation are still open; Path A/production CAD are unchanged. The next
experiment extends this clean basis to the remaining two SPI nets.
V851 extends the three-net V850 primitive through SPISO and SPICS. Native
saved-board connectivity and trace-removal negative controls pass for all five
SPI nets, with no signal short/crossing, but native DRC rejects the candidate
for one GND thermal-starvation error plus the inherited isolated B.Cu-fill
warning. V852's ordinary-via B.Cu separation is rejected by a real
SPISO/SPICS source-escape short. The five-net field is connectivity-positive,
but not yet a DRC pass; the next class must stagger source vias outside the
adjacent F.Cu fanout.
V853 is rejected as a route implementation: its outward SPICS escape enters
the U1 exposed GND pad/thermal field, producing six related GND/clearance
violations and the inherited isolated-fill warning. It retains 40 incomplete
items and no new endpoint failure. The next class must stagger the two source
escapes left of the U1 field before dropping to B.Cu.
V854 tested that left-side vertically staggered B.Cu source escape and was
rejected with 19 native violations, dominated by U1 exposed-pad/adjacent-pad
and zone-clearance conflicts. It is route-implementation evidence only. The
270-degree placement retains useful endpoint-order information, but the next
active basis returns to V772's complete-SPI/support field for a distinct
control/source escape class.
V855 tested a V772/V837-based PERST_N left-side source dogbone. Native DRC
rejected it with 5 violations, including one true B.Cu crossing against the
SPI corridor and four U1-field clearance/short/mask conflicts. It is rejected
route evidence; V772/V837 remain the complete-SPI/control basis.
V856 made the PERST_N source escape straight right and reduced native DRC to
one violation where its via touched the parallel CLKREQ_N corridor. V857
doglegs upward before the via and passes native DRC with 0 violations and 32
expected incomplete items. Its saved-board audit passes all five SPI endpoint
pairs plus PERST_N and all six trace-removal negative controls. This closes a
local PERST_N routing primitive only; complete RTL9210B support/control and
Path-B integration remain open.
The V857 support re-audit passes XTAL_IN, XTAL_OUT, RSET, and plane-backed GND
endpoint assertions, with trace-removal negative controls passing for the
three signal support nets. V857 is consequently a native-clean local basis for
SPI, PERST_N, crystal/RSET, and reviewed ground support. Its 32 incomplete
items remain open Path-B source, rail, control, and CM5-side connections.
V858/V859 tested the RTL_5V source-to-C5 power-plane probe and were rejected
for local source/via clearance and collisions with accepted SPI/PERST fields.
V860 narrowed the source to 0.20 mm and moved its ordinary transition into
the measured SPI-channel gap. Native DRC passes with 0 violations and 31
expected incomplete items; the saved-board audit proves U1.17→C5.1 and a
trace-removal negative control. U1.33 and the remaining RTL_5V/RTL_3V3/RTL_1V1
endpoints remain open.
V863 tested a combined RTL_3V3 bridge/support collector and was rejected by
an In2 crossing against RTL_5V plus U2/SPI clearance conflicts. V864 moved the
collector outboard but was rejected by three real F.Cu/In2 crossings against
PEDET, CLKREQ_N, and RTL_5V. These are rail-route allocation failures; the
next experiment isolates U2.8 before rebuilding a collector.
V865 reduced the RTL_3V3 bridge probe to one PEDET clearance violation.
V866 moved the transition but exposed a PEDET crossing and CLKREQ clearance;
V867 collided with existing SPISI and PERST_N B.Cu corridors, and V868 reduced
this to one PERST_N B.Cu crossing. V869 lifted the B.Cu jog above PERST_N and
passes native DRC with 0 violations and 29 expected incomplete items. Its
saved-board audit proves U2.8→C3.1 and a trace-removal negative control;
remaining RTL_3V3 endpoints are open.
V870 extends the clean V869 RTL_3V3 spine from U2.8 to U2.3. Native DRC
passes with 0 violations and 28 expected incomplete items; the saved-board
audit proves U2.3/U2.8/C3.1 and a trace-removal negative control. U1-side
RTL_3V3 and the R2/R3 supply endpoints remain open.
V871 adds U1.39 to the validated RTL_3V3 bridge spine. Native DRC passes with
0 violations and 27 expected incomplete items; the saved-board audit proves
U1.39/U2.3/U2.8/C3.1 and a targeted U1.39 source-trace negative control.
Remaining U1 RTL_3V3 pads and R2/R3 supply endpoints remain open.
V872/V873 tested U1.20 upward/stepped RTL_3V3 escapes and were rejected by
SPI-field and RTL_5V-transition crossings. V874/V875 tested local U1.34/U1.39
joins and were rejected for RTL_5V via clearance. V876's diagonal-left U1.34
departure passes native DRC with 0 violations and 26 expected incomplete
items; its saved-board audit proves U1.34/U1.39/U2.3/U2.8/C3.1 and a
source-trace negative control.
V861 added U1.33 to the V860 RTL_5V network but was rejected for a dangling
In2 track caused by an incorrect junction coordinate. V862 corrected that
join to the actual V860 transition. Native DRC passes with 0 violations and
30 expected incomplete items; the complete RTL_5V audit passes U1.17/U1.33/C5.1
and its trace-removal negative control.
V877/V878 tested U1.52 lower-side escapes and were rejected by the existing
XTAL_IN and RSET support corridors. V879 scrubbed only those support routes as
a placement discriminator; U1.52 then joins the 3V3 spine with native DRC 0,
30 expected incomplete items, and a saved-board audit pass for
U1.52/U1.39/U2.3/U2.8/C3.1 plus a source-trace negative control. The increased
open count is deliberate crystal/RSET scrub evidence, not an accepted
omission.
V880 translated the complete Y1/C1/C2/R1 support block 8 mm west without
native violations. V881's first support route was rejected for crystal-field
crossings and RSET/GND conflicts. V882 moved that block a further 18 mm
northwest; V883 was rejected for RSET proximity/crossing, while V884 isolated
the RSET geometry but exposed the relocated GND-return requirement. V885
confirmed that support scrub plus the clean RSET route leaves only the expected
GND return findings. V886's single-via return and V887's two-via return were
rejected for crossings or pad clearance. V888 is the accepted GND-return
primitive: native DRC reports 0 violations and 29 expected incomplete items;
the saved-board audit proves C1.2/C2.2/R1.2 connectivity through three local
GND vias and passes a zone-independent trace-removal negative control. XTAL_IN
and XTAL_OUT remain intentionally open for the next support-routing trial.
V889 tested direct outer F.Cu crystal corridors and was rejected for the
existing U1.52 RTL_3V3 escape and a far-side XTAL_IN pad landing. V890 and
V891 repeated the trial with only the U1.52 departure scrubbed; V891 removed
that conflict but still failed the U1.55-adjacent XTAL_OUT source escape and
the residual RTL_3V3 corridor. These are route-implementation failures, not
evidence against the relocated support placement. V888 remains the accepted
GND-return base for the next U1 source-escape strategy.
V892 corrected the source-escape shape using a perpendicular XTAL_OUT
dogbone and the scrubbed U1.52 discriminator. Native DRC reports 0 violations
and 26 expected incomplete items. The saved-board audit passes XTAL_IN,
XTAL_OUT, RSET, and GND support connectivity and both source-trace negative
controls. This is the accepted complete relocated crystal-support primitive;
the scrubbed U1.52 RTL_3V3 departure remains to be restored without regression.
V893/V894/V895/V896 tested restored U1.52 RTL_3V3 corridors and were rejected
by crystal, RSET, JTAG, PEDET, or existing SPI-field crossings. V897/V898
tested ordinary B.Cu XTAL_IN transitions and were rejected by existing SPI
vias or XTAL_OUT clearance. V899/V900 repeated east-shifted B.Cu variants;
V901 separated the F.Cu lanes but still crossed at the source. V902/V903/V904
tested early and late XTAL_OUT B.Cu transitions; native DRC rejected each for
QFN/via clearance or source-lane crossings. These remain route-implementation
failures. V892 remains the accepted crystal/GND primitive, with U1.52
restoration still open.
V905/V906 tested staggered crystal source transitions with the known U1.52
3V3 escape; native DRC rejected the pair for via clearance and a dangling
relocated 3V3 transition. V907 moved the 3V3 join on B.Cu but collided with
the inherited SPISO field and the XTAL_IN corridor. V908 moved the 3V3
collector to low F.Cu; it was rejected by SPISO/XTAL_IN clearance and a
dangling 3V3 via. The source-escape repair remains a package-region routing
problem; no electrical topology or placement rejection is implied.
V914 transplanted the native V772 source dogbones, moved XTAL_IN to B.Cu at
the first clean escape, retained XTAL_OUT on its separate F.Cu corridor, and
reused the existing U1.52 3V3 via without duplication. Native DRC reports 0
violations and 25 expected incomplete items. The saved-board audit passes
XTAL_IN, XTAL_OUT, RSET, GND, and RTL_3V3 support, with independent source
trace-removal negative controls for both crystal nets. V914 is the accepted
complete relocated RTL support primitive for the next support rail.
V909/V910 tested east and staggered three-channel restorations and were
rejected for QFN, XTAL, or inherited SPI-field interactions. V911 scrubbed
only the inherited SPI copper as a discriminator and still exposed source
lane separation issues. V912/V913 corrected route construction but retained
duplicate-via or source-lane defects. V914 then used the native V772 source
dogbones, separated XTAL_IN onto B.Cu, and reused the existing U1.52 via;
native DRC is 0 with 25 expected incomplete items and the full saved-board
support audit plus both crystal negative controls pass. V914 is the current
accepted support base.
V915 tested a two-pad RTL_1V1 In2.PWR attachment to C4 and was rejected by
the existing RTL_3V3 source field and RTL_5V/SPI plane corridors. V916 moved
the plane trunk north and tightened the escapes; native DRC reduced the result
to two violations, specifically U1.36 crossing the existing 3V3 vertical
departure and U1.40 shorting the adjacent 3V3 via. RTL_1V1 remains open; the
next trial must use a different U1 pad-side escape.
V918 tested the U1.25 north-side RTL_1V1 escape and was rejected by the
inherited SPICS fanout. V919 moved the via west but was still rejected by the
adjacent DEVSLP pad and SPICS geometry. V920 scrubbed only the inherited SPI
copper as a discriminator; the same U1.25/C4 In2.PWR attachment then passed
native DRC with 0 violations and 29 expected incomplete items. This confirms
the power escape is clean when its local corridor is owned; SPI regeneration
around it is the next required implementation step.
V917 tested alternate U1.36/U1.40 pad-side escapes with an In2.PWR trunk;
native DRC rejected the candidate for the U1.36/RTL_3V3 field, the U1.40 /
USB_TXP0 neighbor, and the relocated GND return. RTL_1V1 remains open; this
candidate does not alter the accepted V914 support base.
