# PiSXMe M6 Architecture-Unblocker Current Checkpoint

Date: 2026-08-28

Status: DISPOSABLE STUDIES COMPLETE; M6 NOT PASSED; ACTIVE SOURCE UNCHANGED

## Scope

This receipt supersedes the earlier provisional Ethernet/SATA replan evidence for
current-source parity. The active Rev A schematic and PCB were not modified. No
architecture was promoted and no M7-M10 work was started.

Source basis:

- staged M2 source snapshot: `/private/tmp/pisxme_m6_staged_m2_source.kicad_pcb`
- SHA-256: `b6e7e78ec8fa516eff15bbfda51dd848399073d2d4b47474e1d7e6fbf1a2fc78`
- outline: 240 x 140 mm in the staged M2 snapshot

## Candidate 1 — native Ethernet + FAST-A + SERVICE

Disposable file:

`/private/tmp/pisxme_m6_candidate1_staged_m2/PiSXMe_Candidate1_Ethernet_FASTA_SERVICE.kicad_pcb`

- SHA-256: `844d9fb9e51e9ef2cf9f934cdc9758a8c124b85941cfad61b6af1eb5e433ac9e`
- FAST-B connector/support branch removed in the copy (`J10`, `U8`, `U10`,
  `U18`, `C18`, `R6`)
- CM5IO-derived Ethernet proxy geometry added (`J12`, `U19`, `U20`, `C20`)
- 283 segment records: F.Cu 187, B.Cu 85, In3.Cu 11
- 98 parsed via records
- Ethernet segment records: 0
- native KiCad 10.0.5 DRC: 1,299 violations and 179 unconnected items

Disposition: **FAIL / NOT ROUTABLE EVIDENCE**. The copy proves only that the
FAST-B removal and Ethernet placement delta can be expressed mechanically. It
does not prove an Ethernet corridor, pair geometry, return-path quality, or a
clean FAST-A reconstruction. Candidate 1 is not eligible for active-source
promotion.

## Candidate 2 — native Ethernet + internal SATA + SERVICE

Disposable file:

`/private/tmp/pisxme-candidate2-fullboard-v2/PiSXMe_Candidate2_fullboard_v2.kicad_pcb`

- SHA-256: `dd5798eab07a74c4ecd81d4fe7ee236abb9b0d4c2fef0374e75c9df98a4efd0f`
- based on the current 240 x 140 mm source snapshot
- external USB-A branches and their support footprints removed in the copy
- proxy blocks present: `J12` MagJack, `U19` Ethernet ESD, `U20` JMS578,
  `J13` SATA-only 2242 envelope
- 248 segment records: F.Cu 160, B.Cu 77, In3.Cu 11
- 74 parsed via records
- Ethernet segment records: 0
- SATA segment records: 0
- native KiCad 10.0.5 DRC: 1,108 violations and 113 unconnected items

Disposition: **FAIL / NOT ROUTABLE EVIDENCE**. This is a placement/proxy study,
not a pin-accurate full-board implementation. It does not establish MagJack
pair routing, USB3-to-SATA routing, M.2 connector correctness, SSD power, or
underside mechanical clearance. The earlier JMS578 coupon remains topology-only
evidence and is not full-board proof.

## Current comparison

| Item | Active dual USB3 snapshot | Candidate 1 | Candidate 2 |
|---|---:|---:|---:|
| Ethernet route records | 0 | 0 | 0 |
| SATA route records | 0 | 0 | 0 |
| Parsed segments | 314 | 283 | 248 |
| Parsed vias | 122 | 98 | 74 |
| DRC violations | existing M6 debt | 1,299 | 1,108 |
| Unconnected items | existing M6 debt | 179 | 113 |
| Full-board routability proof | no | no | no |

Raw via/segment reductions are not treated as wins because both replacement
copies delete large portions of the old design while leaving the replacement
high-speed interfaces unrouted.

## M6 decision

The current evidence does **not** justify selecting
`REVA_ETHERNET_PLUS_ONE_USB3` or `REVA_ETHERNET_PLUS_INTERNAL_SATA` as the active
Rev A architecture. It also does not justify reconstructing dual USB3 by force.

The M6 architecture gate remains open. The next bounded task must produce a
current-source, pin-accurate, clearance-checked disposable candidate with:

1. real CM5IO Ethernet connectivity and routed four-pair topology;
2. either a clean FAST-A/SERVICE rebuild or a pin-accurate JMS578 plus real
   SATA-only B-key socket study;
3. zero true signal opens/shorts in the candidate delta;
4. deliberate reference-plane and return-via evidence; and
5. mechanical clearance evidence for the right-edge I/O and any underside SSD.

Until that gate passes, keep M6 active, do not advance M7-M10, and do not alter
the active schematic, PCB, or manufacturing outputs.

## 2026-08-28 current-source correction

The historical follow-up paragraphs below that describe an active U16 local
support route are superseded. Reinspection of the current active PCB confirms
that no U16 FB/RT/PG reroute from disposable trial 4 is present; the active
source still contains the stale support copper documented in the U16 package
checkpoint. The only active-source copper correction after the package
prerequisites is the bounded M4 removal of 24 prohibited plane-layer signal
vias (current PCB SHA-256 `a53e6751a59eb530afd3b522672b5ce967515710bf7eece54a5aa4242e81316e`).
U16 remains open for coordinated schematic/PCB rebuild.

## 2026-08-28 active-source follow-up

The active PCB subsequently received a bounded package/parity correction for
the nine U16 support footprints (C10-C14 and R8-R11). The schematic and all
USB/PCIe copper remain unchanged. This correction does not promote either
Ethernet candidate and does not close M6; the earlier active-source statement
applies to the architecture studies and does not claim that no later bounded
prerequisite correction occurred.

## 2026-08-28 active-source U16 prerequisite follow-up

After the package correction, the active PCB received the bounded U16 local
support route from disposable trial 4: the stale package-crossing
`/VPROT_12V` diagonal was removed and FB/RT/PG were connected with six ordinary
through-vias. This is a prerequisite correction only; no Ethernet/SATA
architecture was promoted, no USB data or PCIe copper was changed, and M6
remains open pending the pin-accurate replacement-I/O route and full validation.

## 2026-08-28 active-source U1 package correction

The active U1 footprint was subsequently replaced with the local
manufacturer-derived TPSM63606RDLR land pattern, preserving pad UUIDs and net
intent. This exposes the actual side pins and four exposed PGND/thermal lands,
but intentionally leaves the old U1 support copper for the next disposable
reroute. M6 remains open; no Ethernet/SATA architecture was promoted and no
M7–M10 work is authorized.

Current active PCB hash after the bounded U1/U16 package-truth prerequisites:

`8bd0d56b148296f18f127bec296b7e4e70b82765686a3db24616a93983259476`

The corrected packages deliberately leave stale local support copper for the
next disposable reroute. Do not interpret the syntactically valid source as a
closed power or I/O gate.

## 2026-08-28 I/O-side outline steering

The active source remains 240 x 140 mm. A bounded width trade study evaluated
250/260/270/280 mm alternatives (the historical 220 mm outline is not active).
The first disposable replacement-I/O trial must remain at 240 x 140 mm. A
250-mm right-edge expansion is permitted only if a pin-accurate candidate proves
that the remaining failure is a genuine corridor or mating-envelope limit after
ESD/support placement is corrected. Larger widths have no current evidence of
benefit and are not part of the M6 work package.

This steering changes the M6 disposable-study decision space only; it does not
promote Ethernet, internal SATA, or any outline change into the active design.

## 2026-08-28 Candidate 1 insertion-boundary result

The bounded Candidate 1 attempt stopped before topology mutation. The disposable
file `/private/tmp/pisxme-v2-candidate1/PiSXMe_V2_Candidate1.kicad_pcb` is
byte-identical to the active source (`8bd0d56b...`). The active schematic has no
Ethernet nets, MagJack identity, or CM5IO-derived endpoint mapping that can be
inserted safely by a PCB-only edit. The official CM5IO Ethernet design is a
separate hierarchical design, so proxy footprints/copper would not be
pin-accurate evidence.

Disposition: **Candidate 1 remains untested, not passed and not rejected.** The
next architecture task is to establish an explicit schematic/net/footprint
insertion boundary from CM5IO, then rebuild the disposable 240 x 140 mm trial.
Do not remove FAST-B or route replacement copper until that boundary is verified.

## 2026-08-28 U16 support replacement trial result

Before the next Ethernet disposable study, a bounded U16 support-field
replacement was attempted in `/private/tmp/u16_support_replacement_trial.kicad_pcb`
using the active package-truth source. Native KiCad 10.0.5 DRC found 1433
violations and 172 unconnected items; the trial contains true local shorts and
crossings and is rejected. This does not reopen the board-outline decision:
the failures are concentrated in the U16 support/legacy-corridor topology.
M6 remains open and M7-M10 remain prohibited.

## 2026-08-28 second U16 topology trial result

The disposable U16 relocation/routing trial at
`/private/tmp/pisxme-u16-topology-trial-73566/PiSXMe_U16_topology_trial.kicad_pcb`
also failed native KiCad 10.0.5 DRC (857 violations, 177 unconnected). The
failure is local support-field crowding and stale-zone interaction; it is not
evidence that the 240 mm outline is too narrow. No active source was changed.

## 2026-08-28 CM5IO Ethernet insertion boundary

The local official CM5IO PCB was read as the pin-accurate disposable source.
CM5 pads 3/4/5/6/9/10/11/12 carry `TRD3_P`, `TRD1_P`, `TRD3_N`, `TRD1_N`,
`TRD2_N`, `TRD0_N`, `TRD2_P`, and `TRD0_P`, respectively. CM5IO uses two
`TPD4EUSB30` arrays for pairs 0/1 and 2/3, an integrated-magnetics
`TRJG0926HENL` MagJack (`MagJack-A70-112-331N126`), a 100 nF common center-tap
capacitor, and 470 ohm LED current-limit resistors. Its Ethernet pairs are
short, F.Cu-only, and use zero signal vias; PiSXMe trace geometry must still be
recalculated for the PiSXMe six-layer stackup. The official shield is tied to
GND, but PiSXMe must make an explicit enclosure/ESD shield decision.

This mapping is the boundary for disposable Candidate 1 work. It is not yet an
active schematic migration or M6 pass.

## 2026-08-28 prior disposable Candidate 1 artifacts reclassified

The temporary workspace contains earlier Ethernet-plus-FAST-A studies,
including `/private/tmp/pisxme_m6_candidate1_routed_plus20.kicad_pcb` and
`/private/tmp/pisxme_candidate1_plus20/PiSXMe_Candidate1_plus20_io_shifted_study.kicad_pcb`.
Their native KiCad 10.0.5 DRC results were 1440 violations/154 unconnected
and 1234 violations/187 unconnected, respectively. The generator used
PCB-only disposable net-name/footprint insertion without an active schematic
hierarchy, so these are failed exploratory artifacts, not pin-accurate
promotion evidence. Candidate 1 remains unproven until a fresh source-bound
trial passes the M6 gate.

## 2026-08-28 fresh Candidate 1 reroute trial result

A fresh disposable PCB-only trial was generated at
`/private/tmp/pisxme-candidate1-reroute/PiSXMe_Candidate1.kicad_pcb` after
removing the FAST-B branch and inserting CM5IO-derived Ethernet footprints.
Native KiCad 10.0.5 DRC reported **1322 violations and 186 unconnected
items**. The trial is rejected as promotion evidence: it inserts proxy
Ethernet nets in the PCB without a matching schematic hierarchy and retains
generic clearance, width, mask, dangling, and shorting failures. No active
source, schematic, zones, or manufacturing output was changed.

This is evidence that the first one-port conversion attempt is not yet a
viable source-bound architecture; it does not justify forcing the old
dual-USB topology or promote the internal-SATA candidate.

## 2026-08-28 M6 architecture-unblocker disposition

The current evidence does not authorize promotion of either Ethernet
replacement architecture into the active Rev A source. The official CM5IO
Ethernet boundary is now known, but no fresh pin-accurate Candidate 1 trial
passed the route/DRC/mechanical gates. Earlier temporary Candidate 1 files are
failed PCB-only studies, and both U16 support-field trials were rejected by
native DRC. Therefore M6 remains **BLOCKED**, M7-M10 remain prohibited, and
the 240 x 140 mm outline remains the active baseline with 250 mm only as a
measured-clearance fallback.

Next executable work package:

1. Rebuild U16 support topology from a cleared local field (remove stale zones
   and corridors before placing pin escapes).
2. Confirm the Ethernet nets and footprint in a disposable schematic/PCB
   insertion boundary, then route Candidate 1 with FAST-A and SERVICE.
3. Accept Candidate 1 only with zero true signal opens/shorts, deliberate
   return paths, controlled pair geometry, and mechanical clearance evidence.
4. If that fails for a demonstrated I/O pinch point, run the separate
   Ethernet-plus-internal-SATA candidate; otherwise do not mutate the active
   source.

## 2026-08-29 continuation evidence — disposable architecture trials

The active source remains unchanged after the M4 PCB correction and bounded
U16 schematic endpoint correction. Current active hashes are:

- PCB `a53e6751a59eb530afd3b522672b5ce967515710bf7eece54a5aa4242e81316e`;
- schematic `d31ff8e96fd1df211f5528f0b4c70f8b7a7891d68383d4561bfae83116bf5bbb`.

The isolated U16 schematic check found zero ERC errors but only library-link
warnings in the temporary copy; it is not an active M1 closure.

The +20 mm disposable Candidate 1 file
`/private/tmp/pisxme_candidate1_trial.kicad_pcb` was independently checked with
KiCad 10.0.5 and reported 1326 violations / 185 unconnected items. It uses
PCB-only Ethernet proxy insertion and therefore is rejected as promotion or
architecture proof. Candidate 2
`/private/tmp/pisxme_candidate2_eth_sata_260.kicad_pcb` remains a placement proxy
with no routed Ethernet or SATA pairs, no pin-accurate JMS578 implementation,
and no verified M.2 socket or underside mechanical envelope.

These results do not justify promoting Ethernet, internal SATA, or a 260 mm
outline, and they do not justify restoring the blocked dual-USB topology by
fiat. The next valid M6 study must be source-bound: establish the CM5IO
Ethernet schematic/net boundary, clear stale local zones, then route FAST-A
and SERVICE with measured return paths on the 240 mm baseline. A 250 mm trial
is conditional on a measured corridor or mating-clearance failure; +20 mm and
larger remain unapproved.

## 2026-08-29 Candidate 1 +20 mapping follow-up

The disposable mapping study
`/private/tmp/pisxme_candidate1_260_mapping.kicad_pcb` assigned the official
CM5IO Ethernet pad mapping and placed two ESD arrays plus a MagJack on a
260 x 140 mm outline. It removed the FAST-B branch and reduced the disposable
reference count from 62 to 60, but deliberately added no Ethernet copper.
The study found that +20 mm improves MagJack edge/cable placement while the
CM5-to-ESD fanout pinch point remains essentially unchanged. It is therefore
**UNPROVEN placement/net-mapping evidence**, not a routability result. Native
DRC was unavailable in that isolated generator environment; no promotion or
active-source change is authorized.

A fresh native KiCad 10.0.5 DRC of the disposable Candidate 2 file
`/private/tmp/pisxme_candidate2_eth_sata_260.kicad_pcb` reported **1111
violations and 114 unconnected items**. The copy still contains proxy
Ethernet/JMS578/M.2 objects and no meaningful routed Ethernet or SATA
topology, so this result is a rejection of the disposable artifact, not a
comparison-quality architecture result.

## 2026-08-29 Candidate 1 routed follow-up (rejected)

Disposable `/private/tmp/pisxme_m6_candidate1_routed_plus20.kicad_pcb` used the
official CM5IO-derived Ethernet pad mapping and added temporary routes on a
260 x 140 mm copy after removing FAST-B. Pair metrics were:

| Pair | Conductor lengths | Signal vias |
|---|---:|---:|
| TRD0 | 20.31 / 20.49 mm | 0 / 0 |
| TRD1 | 22.93 / 26.50 mm | 2 / 2 |
| TRD2 | 24.65 / 25.02 mm | 0 / 0 |
| TRD3 | 27.57 / 28.56 mm | 2 / 2 |

The generated topology contains 44 Ethernet segment primitives, 20 crossing
instances, and 15 unique cross-net pair combinations. It is rejected as route
evidence. The result confirms that +20 mm does not cure the fanout through
local edits; a clean source-bound coupon requires a deliberately restructured
ESD placement/orientation and route topology.

## 2026-08-29 current-source U16 wording correction

Direct inspection of the current PCB (SHA-256
`a53e6751a59eb530afd3b522672b5ce967515710bf7eece54a5aa4242e81316e`) shows
that U16 FB, RT, and PGOOD do have active F.Cu/B.Cu segment and via records.
Older checkpoint prose saying that these nets have no active segments is
superseded. The routes are not M3/M6 closure evidence because native DRC on the
active board did not complete within the bounded run and the full support,
plane, thermal, and parity checks remain outstanding. The safe disposition is
**CONNECTED BUT UNVALIDATED**, not absent.
