# PiSXMe Rev A Clean — current progress checkpoint

## CURRENT HIERARCHY AUTHORING PROBE — 2026-09-12

The generic Phase 3 scaffold now emits native KiCad root child-sheet
project/page `instances` records that were absent from its generated root
objects. The regression validates the isolated generated root directly, and
fresh KiCad Light validation from `7165ea11` passes with zero severity-error
findings. Receipt:
`PHASE24_NATIVE_HIERARCHY_SERIALIZATION_PROBE_RECEIPT_20260912.md`.

This is an authoring-path correction, not full ERC closure; the canonical clean
schematic remains at 311 warnings / 0 errors and Phase 24 remains OPEN.

## CURRENT LIVE-CONTRACT DIAGNOSTIC — 2026-09-12

The fail-closed live contract map found duplicate hierarchical labels
`BRIDGE_3V3` and `BRIDGE_1V1` in `REGULATORS` and `STORAGE`. This contradicts
the older exact-set receipt and is now the next source-authority investigation;
no label repair has been promoted. See
`PHASE24_LIVE_CONTRACT_DUPLICATE_LABEL_DIAGNOSTIC_20260912.md`.

## CURRENT JMS583 LOCAL ESCAPE — 2026-09-12

The frozen U11/Y10 support placement now uses a tightly scoped 0.10 mm
XIN/XOUT escape rule. Fresh KiCad Light passes the complete ten-branch support
audit, native endpoint audit, saved-board scope audit, trace-removal negative
control, and dual-mode storage USB3 connectivity. Native DRC reports 612/409
on the inherited acreage baseline with no shorting, solder-mask-bridge, or
JMS583-local crossing findings; the two remaining crossing records are the
pre-existing JMS_AVDDL/USB_RXN1 full-board route. Receipt:
`PHASE24_JMS583_FINE_ESCAPE_RECEIPT_20260912.md`.

## CURRENT PATH-B AUTHORITY LIGHT RECHECK — 2026-09-12

Fresh KiCad Light validation passes the RTL9210B authority audit, V1603
six-net connectivity and six negative controls, and loads the stored Path-B
parity/metrics artifacts. Receipt:
`PHASE24_PATHB_AUTHORITY_LIGHT_RECHECK_RECEIPT_20260912.md`.

## CURRENT STORAGE-CONTRACT LIGHT RECHECK — 2026-09-12

Fresh KiCad Light validation passes the dual-mode mode-control contract, the
JMS583/selector/TE M-key library audit, and the dual-mode schematic audit.
Receipt: `PHASE24_STORAGE_CONTRACT_LIGHT_RECHECK_RECEIPT_20260912.md`. These
focused gates do not close the remaining JMS583 physical support escape.

## CURRENT PATH-B DFM/NATIVE-DRC RECHECK — 2026-09-12

Fresh KiCad Light validation of the committed RTL9210B V1603/V1517 integrated
candidate reports 0 native DRC violations and 0 unconnected items, with no
shorting or track-crossing findings. The MIC2545A DFM audit remains PASS.
Receipt: `PHASE24_PATHB_DFM_RECHECK_RECEIPT_20260912.md`. This is an isolated
Path-B gate, not full-acreage or JMS583 closure.

## CURRENT FRESH-LIGHT ERC CROSS-CHECK — 2026-09-12

Fresh KiCad Light 10.0.6 ERC from ref `4d31c1bc` reports 367 findings, with
the same canonical classes and counts 132/126/30/23 as local KiCad 10.0.5.
The additional findings are version-specific library/link classifications.
Receipt: `PHASE24_ERC_LATEST_LIGHT_RECEIPT_20260912.md`.

## CURRENT JMS583 PLACEMENT TEST — STANDARD RULES INSUFFICIENT — 2026-09-12

The bounded native-pad local support placement (U11 fixed; Y10 north-west;
L10 north-east) passes all ten JMS583 support endpoint checks and the negative
control in fresh KiCad Light. The standard-geometry route still has concrete
XIN/XOUT QFN pad-field shorts/crossings and an inherited AVDDL/USB3 B.Cu
crossing. The tightest local native pad clearance is 0.0754 mm versus the
0.10 mm pad requirement. This is now an evidence-backed local JMS583 QFN
escape-rule boundary, not an untested placement hypothesis. See
`PHASE24_JMS583_SUPPORT_ESCAPE_BLOCKER_20260912.md`.

## CURRENT PARALLEL-RESUME VALIDATION — 2026-09-12

Fresh KiCad Light validation from committed ref `65240bf6` reproduces the
JMS583 three-branch failure (`XIN`, `XOUT`, `JMS_VDDREG_5V`) and passes the
other seven support branches. The same worker passes the RTL9210B V1603
six-net audit and all six negative controls. Receipt:
`PHASE24_PARALLEL_RESUME_VALIDATION_RECEIPT_20260912.md`.

## CURRENT DEPENDENT GATE — JMS583 LOCAL SUPPORT ESCAPE — 2026-09-12

Fresh KiCad Light validation of the committed cumulative storage baseline
reproduces the corrected audit result: `XIN`, `XOUT`, and `JMS_VDDREG_5V` are
open; the other seven required JMS583 support branches pass. Multiple
materially different full-support route/placement classes have been rejected
for native shorts/crossings or collateral loss of accepted branches. This is
a scoped local QFN escape/manufacturability decision, not a Path-B orientation,
macro-floorplan, or storage-architecture blocker. See
`PHASE24_JMS583_SUPPORT_ESCAPE_BLOCKER_20260912.md` for the exact evidence and
bounded continuation options. Canonical copper remains unchanged.

## CURRENT STORAGE SUPPORT PROBE — THREE-CORRIDOR V2 REJECTED — 2026-09-12

The V2 three-corridor trial passes the complete JMS support endpoint audit and
negative control, but native KiCad 10.0.5 DRC is 644/409 with source-field
shorts/crossings involving reset and adjacent U11 support pads. It is rejected
route evidence; canonical copper is unchanged. Receipt:
`PHASE24_JMS_THREE_CORRIDORS_V2_REJECT_RECEIPT_20260912.md`.

## CURRENT PATH-B AUDIT — V1603 NEGATIVE CONTROL CORRECTION — 2026-09-12

The V1603 six-net audit now removes all actual saved copper for each
disposable negative control, handling redundant/zero-length REFCLK segments.
Local KiCad 10.0.5 and fresh Light validation pass all six native links and
all six negative controls. Receipt:
`PHASE24_RTL9210B_V1603_AUDIT_FIX_RECEIPT_20260912.md`.

## CURRENT STORAGE AUDIT — CORRECTED LIGHT BASELINE — 2026-09-12

Fresh Light validation from committed ref `7c67d297` confirms the corrected
audit now targets the cumulative candidate: XIN, XOUT, and JMS_VDDREG_5V are
open while the other required JMS support branches pass. The audit fails
closed before its negative-control phase, as required. Receipt:
`PHASE24_STORAGE_SUPPORT_AUDIT_LIGHT_V3_RECEIPT_20260912.md`.

## CURRENT STORAGE SUPPORT PROBE — STRAIGHT CRYSTAL + VDDREG V1 REJECTED — 2026-09-12

The fixed-Y10 straight crystal escape combined with the outer VDDREG route
passes all ten JMS support endpoint checks and the negative control, but native
KiCad 10.0.5 DRC is 641/409 with five shorts and four crossings. It is
rejected physical route evidence; the cumulative AVDDL-U12 baseline remains
authoritative. Receipt:
`PHASE24_JMS_STRAIGHT_VDDREG_V1_REJECT_RECEIPT_20260912.md`.

## CURRENT STORAGE SUPPORT PROBE — NORTH V1 REJECTED — 2026-09-12

Replaying the co-located north support strategy against the live cumulative
candidate connects VDDREG but drops already-accepted XIN, XOUT, AVDD33, VCCO,
and VCCK branches. Native KiCad 10.0.5 DRC is 611/404. It is rejected
route/placement evidence; the cumulative AVDDL-U12 baseline remains current.
Receipt: `PHASE24_JMS_SUPPORT_NORTH_V1_REJECT_RECEIPT_20260912.md`.

## CURRENT STORAGE BASELINE — FRESH LIGHT VALIDATION — 2026-09-12

Fresh Light validation from committed ref `218533a1` reproduces the current
storage baseline: JMS_REXT, reset, AVDD33, AVDDL, VCCO, VCCK, and LXO pass;
XIN, XOUT, and JMS_VDDREG_5V remain open. The complete-support audit and
negative-control path ran under KiCad 10.0.6. Receipt:
`PHASE24_STORAGE_BASELINE_LIGHT_V2_RECEIPT_20260912.md`.

## CURRENT STORAGE SUPPORT PROBE — OUTER VDDREG V1 REJECTED — 2026-09-12

An outer two-layer ordinary-via escape connects the complete JMS support audit
and negative control, including `JMS_VDDREG_5V`, but native KiCad 10.0.5 DRC
remains 653 violations / 409 unconnected items. It is worse than the
594/412 cumulative baseline and is rejected route evidence. Receipt:
`PHASE24_JMS_VDDREG_OUTER_V1_REJECT_RECEIPT_20260912.md`.

## CURRENT STORAGE SUPPORT PROBE — CRYSTAL V1 REJECTED — 2026-09-12

The local Y10 relocation trial reconnects both `XIN` and `XOUT`, but the
explicit full-support audit still fails `JMS_VDDREG_5V`; native KiCad 10.0.5
DRC is 637 violations / 410 unconnected items, including a local LXO-via
clearance defect. The candidate is rejected route evidence and is not current
authority. Receipt:
`PHASE24_JMS_CRYSTAL_LOCAL_V1_REJECT_RECEIPT_20260912.md`.

## CURRENT ERC PROBE — DUPLICATE STORAGE LABELS REJECTED — 2026-09-12

Replacing 20 exact duplicate STORAGE `NC_*` labels with named JMS labels was
tested in isolation and rejected: native ERC changed from 311 to 317 warnings
because `multiple_net_names` fell 23->6 while `isolated_pin_label` rose
126->149. No canonical source changed. Receipt:
`PHASE24_STORAGE_DUPLICATE_LABEL_REJECT_RECEIPT_20260912.md`.

## CURRENT ERC ALIAS REPAIR — 2026-09-12

The authoritative `STORAGE.kicad_sch` now uses the identity-preserving aliases
`POWER_GND` for the exact former `TME` label and `AUTO_PEDET` for the exact
former `M2_CONFIG1` label. Local native KiCad 10.0.5 ERC is 311 violations / 0
errors, and the exported 361-net netlist is exactly unchanged. Receipt:
`PHASE24_STORAGE_ALIAS_PROMOTION_RECEIPT_20260912.md`.

The `M2_3V3` to `STORAGE_3V3` rename was tested separately and rejected because
it split eight M.2 power pads into a distinct net. It remains historical
rejected evidence, not a current TODO or a permitted cleanup.

## CURRENT STORAGE USB3 STATE — 2026-09-12

The east-pocket U12 source handoff and V6 coupled support topology are the
current storage USB3 implementation candidates. The actual-pad audit passes
all ten required links, and native KiCad 10.0.5 reports no USB3-specific
shorts or track crossings. V6's U11 fanout uses a documented local 0.15 mm
trace exception; longer corridors use 0.20 mm traces and ordinary 0.60/0.30
mm through vias. Receipt:
`PHASE24_STORAGE_MKEY_USB3_SUPPORT_V6_RECEIPT_20260912.md`.

The current storage-local U14 repair removes a genuine `STORAGE_3V3` trunk
through `STORAGE_SEL` with an east-side detour. All ten USB3 links remain
passing; native DRC is 426 violations / 421 unconnected items and the former
U14 short is absent. Fresh Light validation reports 428/421 under KiCad
10.0.6. Receipt: `PHASE24_U14_STORAGE_SEL_SHORT_REPAIR_RECEIPT_20260912.md`.

The open gate is now completion of the remaining storage support/power/control
connections and reconciliation of inherited board findings. Earlier V2–V4,
TX-channel, and U12 migration failures remain historical route evidence only;
they do not describe the current blocker. Their raw reports and receipts are
preserved for archaeology.

The first full JMS583 support-cohort graft on the repaired base passes its
support audit, including negative control, and reduces unconnected items to
401; the USB3 ten-link audit remains passing. It is not promoted because
native DRC rises to 453 from placement/clearance defects. Receipt:
`PHASE24_JMS583_SUPPORT_COHORT_V1_RECEIPT_20260912.md`.
The corrected shared `JMS_VDDREG_5V` tree connects U11/U12 to L10 and passes
its native audit plus negative control without shorts/crossings; the USB3
ten-link audit remains passing. Native DRC is 431/421, so it is retained as a
support primitive rather than promoted. Receipt:
`PHASE24_JMS_VDDREG_TREE_RECEIPT_20260912.md`.
The VCCK local primitive connects U11 to C82 and passes its native audit plus
negative control; all ten USB3 links remain passing. Native DRC is 426/420,
with no new shorting or crossing class. Receipt:
`PHASE24_JMS_VCCK_LOCAL_RECEIPT_20260912.md`.
The AVDD33 local join passes its dedicated audit and the USB3 ten-link audit,
but is rejected because its x=148 mm transition corridor crosses existing
CM5 USB3 channels on both copper layers; native DRC is 435/419. Receipt:
`PHASE24_JMS_AVDD33_LOCAL_REJECT_RECEIPT_20260912.md`.
The AVDD33 rehome moves C80 into the storage island and provides an outward
U11 escape with no short/crossing findings. Its AVDD33 audit and negative
control pass, all ten USB3 links pass, and native DRC is 431/419. Receipt:
`PHASE24_JMS_AVDD33_REHOME_RECEIPT_20260912.md`.
The VCCO rehome moves C81 to (150,148) and clears the CM5_PERST collision.
Its native audit and negative control pass, all ten USB3 links pass, and
native DRC is 430/419 with no new short/crossing class. Receipt:
`PHASE24_JMS_VCCO_REHOME_RECEIPT_20260912.md`.
The corrected reset branch uses a dedicated B.Cu low-speed channel and returns
to C85/R81 without crossing accepted support or USB3 routes. Its native audit
and negative control pass, all ten USB3 links pass, and native DRC is 437/417
with no short/crossing class. Receipt:
`PHASE24_JMS_RESET_LOCAL_RECEIPT_20260912.md`.
The JMS_REXT support primitive rehomes R80 to the east storage pocket and
connects U11.39 to R80.1 without changing USB3 copper. Its native endpoint
audit and trace-removal negative control pass, and the USB3 actual-pad audit
passes. It remains a support primitive pending complete JMS583 support
closure; its native board census is 544/416. Receipt:
`PHASE24_JMS_REXT_LOCAL_RECEIPT_20260912.md`.
Fresh `kicad-light` validation from committed ref `95c600bb` reproduces both
audits; KiCad 10.0.6 reports 546/416 for the inherited candidate census. The
worker result is retained as independent validation, not closure.
The corrected JMS_XAVDDH trial escapes west from U11.52, uses ordinary
through-vias, and returns to a rehomed C84. Endpoint and trace-removal audits
pass, but fresh Light validation finds a local solder-mask bridge at the QFN
escape (562/415 under KiCad 10.0.6), so it is rejected route evidence.
Receipt:
`PHASE24_JMS_XAVDDH_LOCAL_RECEIPT_20260912.md`.
The V3 XAVDDH trial used a local 0.15 mm segment, then returned to normal
0.20 mm routing. Endpoint and negative-control audits pass, but fresh Light
validation finds an XAVDDH-to-XIN QFN short and a B.Cu crossing of accepted
USB3 copper (562/415); it is rejected route evidence. Receipt:
`PHASE24_JMS_XAVDDH_LOCAL_V3_RECEIPT_20260912.md`.
The cumulative-support correction adds missing AVDD33 to the current REXT
base, rehomes C80 to `(155,146)`, and uses an ordinary-via B.Cu corridor to
avoid CM5_PERST. The accumulated JMS support audit and negative control pass;
native DRC is 555/415 with no JMS support short/crossing finding. Receipt:
`PHASE24_JMS_SUPPORT_ACCUMULATED_AVDD33_RECEIPT_20260912.md`.
Fresh `kicad-light` validation from committed ref `42a68b11` reproduces the
accumulated JMS-support and USB3 audit passes at 557/415 under KiCad 10.0.6.
The LXO primitive adds the native U11.64-to-L10.1 join with an ordinary-via
transition and local 0.15 mm escape. Its endpoint and negative-control audits
pass; native DRC is 564/414 with no LXO short/crossing finding. Receipt:
`PHASE24_JMS_LXO_LOCAL_RECEIPT_20260912.md`.
Fresh `kicad-light` validation from committed ref `c11202b3` reproduces the
LXO, accumulated-support, and USB3 audit passes at 566/414 under KiCad 10.0.6.
The U11-to-C83 AVDDL local leg is now authored from that cumulative base;
its native endpoint and negative-control audits pass, with no AVDDL
short/crossing finding. Native DRC is 581/413; the U12/J3 AVDDL branch remains
open. Receipt: `PHASE24_JMS_AVDDL_LOCAL_RECEIPT_20260912.md`.
Fresh `kicad-light` validation from committed ref `3aa5994f` reproduces the
AVDDL, accumulated-support, and USB3 audit passes at 583/413 under KiCad 10.0.6.
The U12.36-to-C83.1 AVDDL branch is now added to the U11 AVDDL primitive;
its native endpoint and negative-control audits pass, with no AVDDL
short/crossing finding. The corrected cumulative candidate passes both U11 and
U12 endpoint audits and negative controls; native DRC is 592/412. The first
generated version dropped the U11 branch and is rejected evidence. Broader
same-net fanout remains open. Receipt:
`PHASE24_JMS_AVDDL_U12_LOCAL_RECEIPT_20260912.md`.
Fresh `kicad-light` validation from committed ref `7f822b9f` reproduces both
AVDDL endpoint audits, accumulated support, and USB3 at 594/412 under KiCad
10.0.6; the corrected cumulative candidate is the current support basis.
The attempted VDDREG restoration connected U11/U12 to L10 in isolation but
created a native USB_TXP1 short and VCCK B.Cu crossing, so it is rejected
route evidence (617/410). No VDDREG copper was promoted.

## CURRENT AUTHORITATIVE OVERRIDE — 2026-09-12

The live canonical schematic is at **311 native ERC warnings / 0 errors**.
The current actionable ERC census is 132 `endpoint_off_grid`, 126
`isolated_pin_label`, 30 `same_local_global_label`, 23
`multiple_net_names`, and 0 `lib_symbol_mismatch`; the duplicate POWER_INPUT
wire family and PWR_FLAG namespace mismatch are closed with exact native
netlist parity. Older counts below
are historical snapshots and are not current open work.
The coordinate-exact STORAGE `NC_*` label probe reduced ERC to 305 warnings
but changed exported netlist structure (11 extra names / 11 changed node
sets), so it is rejected evidence; canonical ERC remains 311/0. Receipt:
`PHASE24_STORAGE_REDUNDANT_NC_LABEL_REJECT_RECEIPT_20260912.md`.

The accepted isolated Path-B RTL9210B V1603 candidate currently passes native
KiCad DRC with 0 violations and 0 unconnected items, plus its six-net audit
and six copper-removal negative controls. The dual-mode storage mode-contract
audit passes. The M.2 power-owner audit must be run against a full storage
candidate with the correct connector reference; its default historical J3
fixture reported nine unreached pads and is not a verdict on the isolated
V1603 board, which contains a partial J1 launch rather than that full storage
power population. Production parity and full-board validation remain open.

## CURRENT PARALLEL WORKSTREAM BASELINE — 2026-09-11

The reproducible cluster census is saved in
`PHASE24_ERC_CLUSTER_CENSUS_20260912.json` and is generated by
`phase24_erc_cluster_census.py` from
`PHASE24_CURRENT_LIVE_AFTER_ALIAS_PROMOTION_erc.rpt`. It records
132 `endpoint_off_grid`, 126 `isolated_pin_label`, 30
`same_local_global_label`, and 23 `multiple_net_names` warnings after the
promoted STORAGE duplicate-label repair. Findings are
sheet- and coordinate-clustered there; no current `unconnected_wire_endpoint`,
`no_connect_dangling`, or `lib_symbol_mismatch` cluster remains. These four
ERC families are independent analysis workstreams, while canonical source
integration and authoritative ERC/netlist/parity validation remain serialized.
The census now also records duplicate warning coordinates; 53 repeated
isolated-label coordinate/name signatures are present in the live report.
Source inspection confirmed repeated storage label records at the same
connector coordinates and off-grid root contract geometry. Both hypotheses
were proven in disposable native ERC/netlist comparisons and promoted; see
`PHASE24_STORAGE_LABEL_DEDUP_PROMOTION_RECEIPT_20260912.md` and
`PHASE24_ROOT_GRID_PROMOTION_RECEIPT_20260912.md`.

## Current checkpoint — identity-driven contract probe rejected — 2026-09-11

The identity-driven disposable regeneration preserved all live root/child port
sets and reduced `unconnected_wire_endpoint` findings from 147 to 144, but
native ERC reported four real `pin_not_connected` errors on sparse regulator
and storage support ports. It was not promoted. Receipt:
`PHASE24_LIVE_CONTRACT_REGEN_PROBE_REJECT_RECEIPT_20260911.md`.

## Current checkpoint — PWR_FLAG authority substitution rejected — 2026-09-11

The repair helper was corrected to process all four embedded PWR_FLAG copies,
but the installed-library substitution probe was rejected by native ERC: it
introduced 115 footprint-link issues, 75 library-symbol issues, and two real
pin-to-pin errors. The original embedded definitions remain canonical; the
probe and details are preserved in
`PHASE24_PWR_FLAG_REPAIR_PROBE_REJECT_RECEIPT_20260911.md`.

## Current checkpoint — live ERC recheck pinned — 2026-09-11

Fresh native KiCad 10.0.5 full-severity ERC on the canonical clean root reports
862 warnings and zero errors. The raw report and hash are pinned in
`PHASE24_LIVE_ERC_RECHECK_RECEIPT_20260911.md`. This does not close Phase 24;
the warning classes remain open and unwaived. The next actionable gate is a
controlled live contract/source-authoring repair followed by matching netlist
export and PCB parity.

## Current checkpoint — native hierarchy regression repaired and passing — 2026-09-11

The generic native hierarchy regression now passes end-to-end under the
installed Flatpak KiCad toolchain. Its disposable generated hierarchy has
zero severity-error ERC findings and no hierarchy mismatch. The test now
handles the explicit fixture path, the ten authoritative child sheets, and
direct root signal links correctly. This does not promote generated output or
close live full ERC. Receipt:
`PHASE24_NATIVE_HIERARCHY_REGRESSION_RECEIPT_20260911.md`.

## Current checkpoint — combined live-port grid probe rejected — 2026-09-11

The combined live-port reconciliation plus coherent-grid transform was tested
only in a disposable copy and rejected by native ERC at 749 findings,
including seven hierarchy pin-not-connected errors. Canonical sources were
untouched. Receipt: `PHASE24_LIVE_PORT_GRID_PROBE_REJECT_RECEIPT_20260911.md`.

The next hierarchy repair must be native-authored and live-port complete; no
further text-level coordinate mutation is being promoted.

## Current checkpoint — partial coherent-grid transform rejected — 2026-09-11

The fresh disposable coherent-grid probe was rejected by native KiCad ERC at
746 findings, including two hierarchy `pin_not_connected` errors. It did not
modify production sources. Partial coordinate transformation is insufficient;
the next authoring repair must include explicit current live port-set mapping.
Receipt: `PHASE24_COHERENT_GRID_PROBE_REJECT_RECEIPT_20260911.md`.

## Current checkpoint — legacy root rewriter rejected — 2026-09-11

The old root-stub rewriter was tested only in a disposable workspace probe.
Native ERC rejected it at 997 findings: the 416 off-grid findings remained,
isolated-label findings increased, and footprint-link findings appeared. It
is not a production repair path. Receipt:
`PHASE24_ROOT_REPAIR_PROBE_REJECT_RECEIPT_20260911.md`.

## Current checkpoint — RTL9210B native netlist authority passes — 2026-09-11

The saved native RTL9210B/M.2 netlist authority audit passes, including its
PEDET-removal negative control. RTL9210B and M.2 XML source hashes are pinned
in the receipt. This closes only the focused Path-B netlist assertion gate;
production parity, firmware/procurement, integrated routing, and full Phase
24 remain open.

Receipt: `PHASE24_RTL9210B_NETLIST_AUTHORITY_RECEIPT_20260911.md`.

## Current checkpoint — CM5 required-net NC cleanup consolidated — 2026-09-11

The source cleanup has removed only required-net contradictions: four USB3,
four Ethernet, and 15 `POWER_GND` no-connect records. Native ERC is now 862
warnings / 0 errors with zero connected-NC findings; 11 standalone dangling
NC records remain open. A fresh native netlist export is also saved. Receipt:
`PHASE24_CM5_NC_REPAIR_CONSOLIDATED_RECEIPT_20260911.md`.

## Current checkpoint — POWER_GND no-connect contradictions removed — 2026-09-11

Removed the exact 14 `No Connect` records co-located with authoritative
`POWER_GND` labels in `CORE_CM5.kicad_sch`. Native ERC fell from 863 to 862
warnings with zero errors, and the final connected-NC finding disappeared.
The remaining 11 dangling NC records are separate and remain open. Receipt:
`PHASE24_POWER_GND_NC_REPAIR_RECEIPT_20260911.md`.

## Current checkpoint — stale CM5 Ethernet no-connects removed — 2026-09-11

Removed exactly four stale no-connect markers from required CM5 Ethernet pins.
Fresh native ERC fell from 867 to 863 warnings with zero errors, and all four
corresponding connected-NC findings disappeared. One unrelated connected-NC
GND finding remains open. Receipt:
`PHASE24_ETHERNET_NC_REPAIR_RECEIPT_20260911.md`.

## Current checkpoint — stale CM5 USB3 no-connects removed — 2026-09-11

Removed exactly four stale `No Connect` records from the required CM5 USB3
pins in `CORE_CM5.kicad_sch`. Fresh native ERC fell from 871 to 867 warnings
with zero errors; all four corresponding `no_connect_connected` findings
disappeared, and the native authority regression still passes. The remaining
five connected-NC findings are unrelated Ethernet/GND records and remain
open. Receipt: `PHASE24_USB3_NC_REPAIR_RECEIPT_20260911.md`.

## Current checkpoint — storage library audit passes — 2026-09-11

The native-storage library audit passes for JMS583, both USB/SATA selector
footprints, and the TE M-key connector. Contact numbering and the M-key gap
are correct in the saved local footprints. This closes only the focused
library shape/numbering subgate; integrated Path-B parity, switched-mode
connectivity, firmware, power/inrush, and full Phase 24 remain open.
Receipt: `PHASE24_STORAGE_LIBRARY_AUDIT_RECEIPT_20260911.md`.

## Current checkpoint — authoritative ERC receipt and gate map — 2026-09-11

Fresh native KiCad 10.0.5 ERC on the live clean schematic found 871 warnings
and zero errors. The hashable report is
`PHASE24_CLEAN_SCHEMATIC_ERC_AUTHORITATIVE_20260911.rpt` (SHA-256
`78f89b43551773f3a2f763bde9bb172a96f6d91981572e23e1036dc9d3f1ae61`); the
schematic hash is `e3327d274738551ba143d138452d816f8ee5cdb52dee2283e63e39eb9a994b5c`.
The remaining warning classes are still open and unwaived.

The hardware-auditor gate map confirms the earliest advanceable gate is
controlled schematic truth/ERC/netlist/parity. It also confirms the accepted
RTL9210B placement has no structural contradiction. The current Path-B
census is now target-selectable so exact candidate-specific evidence can be
generated rather than silently using the older integrated filename.

## Current checkpoint — native authority regression passes — 2026-09-11

The repository Phase 24 native-authority regression passed against the clean
schematic. KiCad 10.0.5 native ERC with `--severity-error` found zero errors.
This closes the severity-error/native-authority subgate only; the full ERC
warning set, matched integrated Path-B parity, acreage integration, and the
remaining Phase 24 gates remain open. Receipt:
`PHASE24_NATIVE_AUTHORITY_TEST_RECEIPT_20260911.md`.

## Current checkpoint — parity scope corrected — 2026-09-11

The generic pad-parity audit was run against the historical
`ACREAGE_CANDIDATE.kicad_pcb` and correctly reported 109 mismatches. That
board is not the accepted RTL9210B Path-B candidate, so the result is a
wrong-baseline diagnostic rather than a Path-B verdict. The result and exact
failure class are recorded in
`PHASE24_PAD_PARITY_SCOPE_RECEIPT_20260911.md`. The independent Ethernet
support parity audit passes. Production parity remains OPEN until an
integrated Path-B board and matching native netlist are audited together.

## Current checkpoint — Path-B candidate revalidated — 2026-09-11

Fresh KiCad 10.0.5 native DRC on the accepted isolated RTL9210B candidate
reports 0 violations, 0 unconnected items, and 0 footprint errors. The
MIC2545A saved-board audit passes its support connectivity checks and two
actual trace-removal negative controls. U1 orientation, local QFN rule, and
V1603 downstream launch remain closed. This is a revalidation receipt only;
production parity, acreage integration, and the remaining Phase 24 gates stay
open.

## Current checkpoint — PWR_FLAG normalization rejected — 2026-09-11

A disposable attempt to replace embedded `PWR_FLAG` definitions with the
installed KiCad `power.kicad_sym` authority was rejected. Although it removed
one library mismatch, it introduced a real `pin_to_pin` warning from the
different KiCad unit serialization. The canonical source remains unchanged;
the two standard PWR_FLAG mismatches are still open and unwaived pending a
unit-compatible native repair.

## Current checkpoint — Ethernet contract library synchronized — 2026-09-11

The canonical `PiSXMeRevAClean:ETHERNET_Contract` library symbol had a stale
`GBE_LED` pin not present in the live ETHERNET child contract. A fail-closed
source repair synchronized the canonical library to the live three-port
contract (`CM5_GBE`, `GBE_SHIELD`, `ETH_POWER`) without changing the child,
root, PCB, or Ethernet topology. Disposable and live native KiCad ERC both
report 871 warnings / 0 errors, down from 872; `lib_symbol_mismatch` fell
from 3 to 2. The Ethernet authority audit remains CLOSED. The two remaining
library mismatches are standard `PWR_FLAG` evidence and remain open.

## Current checkpoint — STORAGE contract pin authority repaired — 2026-09-11

The live `STORAGE_Contract` embedded symbol had one stale pin name: pin 4 was
`M2_3V3` while the root sheet pin, child hierarchical label, and current
storage rail use `STORAGE_3V3`. The fail-closed
`phase24_repair_storage_contract_name.py` changed only that five-byte name;
UUIDs, placement, wires, bridge-rail labels, PCB assets, and storage
architecture are unchanged.

The disposable copy produced the same 872-warning/0-error native ERC result,
and the exported netlist diff contains only the intended pin-4 name change.
This closes the identified contract-name contradiction, not the overall ERC
or Phase 24 gates. Remaining warnings are still open and unwaived.

## Current checkpoint — live contract-port audit prevents blind promotion — 2026-09-11

The live source was compared by native-loaded hierarchy names and embedded
contract definitions. `CORE_CM5` has 15 hierarchical labels but its embedded
contract definition has 12 pins; `REGULATORS` has 6 versus 4; and `STORAGE`
has 7 versus 5. The added live labels are not simply missing wires at the old
contract body: storage rail labels are separately authored with local wires
at y=157/207. A disposable order-based repair produced five real native
`pin_not_connected` errors and was rejected.

No production contract merge was made. The remaining repair must map each
live hierarchical label and intended instance explicitly, then regenerate
the corresponding contract definition/instance without moving actual circuit
geometry. The canonical source remains unchanged; the ERC gate remains open
and unwaived.

## Current checkpoint — generator hierarchy association discriminator passes — 2026-09-11

The corrected disposable generator probe now emits the contract symbol,
child labels/wires, sheet pins/wires, and direct-root links on one coherent
2.54 mm/native-grid coordinate map. Native KiCad 10.0.5 ERC reports zero
`pin_not_connected` and zero `endpoint_off_grid` hierarchy findings. Its 110
remaining findings are scaffold-level `unconnected_wire_endpoint`,
`isolated_pin_label`, and library-symbol warnings; no root/child association
error remains. This closes the authoring-path discriminator, not the live
production ERC gate. The canonical clean hierarchy is still unchanged at 872
warnings and 0 errors. A controlled live-source regeneration/merge with
netlist and native hierarchy comparison remains required.

## Current checkpoint — coherent generator grid path isolated — 2026-09-11

The generic `phase3_scaffold.py` authoring path now emits 2.54 mm contract
pitch and native-grid sheet anchors/connection stubs. A fresh disposable
native KiCad hierarchy generated from that path reports 9 off-grid findings,
but 59 disconnected pins remain because legacy direct-root links were not
transformed to the new sheet coordinate map. This is not promoted production
authority. The next implementation target is to transform those links by
the same coordinate map, then rerun native hierarchy/ERC and netlist
comparison. The canonical clean source and its 872-warning report remain
unchanged.

## Current checkpoint — hierarchy grid discriminator classified — 2026-09-11

The disposable native KiCad grid probe did not justify a production
coordinate rewrite. A broad root-graph snap increased ERC findings from the
canonical 872 warnings to 1132 by detaching hierarchy-associated geometry.
A child-contract-only snap, with the root graph preserved, produced 946
findings and 56 `pin_not_connected` results because the embedded contract
symbol still used its original 3 mm pin pitch. These are route/authoring
experiment results, not production-board changes.

The discriminator closes the narrow hypothesis that labels or wires can be
snapped independently. Any repair must regenerate the contract symbol pin
geometry, child labels/wires, and parent sheet pins/wires as one coherent
native-grid authoring path, then compare hierarchy connectivity and netlist
before promotion. The canonical schematic and its 872-warning report remain
unchanged; the Phase 24 ERC gate remains open and unwaived.

## Current checkpoint — canonical storage-library namespace repaired — 2026-09-11

The canonical `PiSXMe_RevA_Clean_complete.kicad_sym` now contains the eight
storage definitions embedded by `STORAGE.kicad_sch`, added by the auditable
`phase24_reconcile_storage_library.py` path. Existing canonical symbol
definitions were preserved; the earlier broad rebuild that replaced an
unrelated Ethernet-contract variant was discarded. Native KiCad ERC now
reports zero `lib_symbol_issues` and zero missing-library-symbol messages.
The remaining report is now 872 warnings (0 errors), after qualifying the 20
storage passive/crystal footprint references against the registered local
library. It consists of existing off-grid, isolated-label, endpoint, naming,
no-connect, and power/Ethernet symbol-mismatch findings; the footprint-link
class is absent. These remain open authority work; no severity was waived.
Storage library package audit passes, and Path-B routing/support work
continues from the accepted candidate.

Receipts: `PHASE24_CLEAN_SCHEMATIC_ERC_LIBRARY_REPAIRED.rpt` and
`PHASE24_CLEAN_SCHEMATIC_ERC_FOOTPRINTS_REPAIRED.rpt`.

## Current checkpoint — local QFN exception integrated — 2026-09-10

The accepted RTL9210B orientation and V1603 downstream launch are unchanged.
The six U1 high-speed departures now use the authorized local 0.15 mm
trace/clearance exception, returning immediately to the normal 0.20 mm
board routing. Existing ordinary 0.60/0.30 mm through-vias were retained.
Native integrated DRC is 0/0/0, and the saved-board six-net audit plus six
trace-removal negative controls pass. The corrected standalone fixture also
passes native DRC and its physical scope/connectivity audit. Fine-breakout
implementation is closed; overall Phase 24 remains open for the independent
Path-B and full-board gates.

## Current next action — corrected ISOLATEB support authority — 2026-09-11

An open-acreage U3 support candidate was evaluated using the accepted U1/V1603
baseline. It has complete native connectivity (0 unconnected items) and 20
native DRC findings. The remaining failures are identifiable physical
corridor crossings/local-rule receipts; it is not promoted, but is the best
current disposable integration basis.

With the candidate-local QFN rule applied, the same saved candidate reports 11
native DRC violations and 1 unconnected item. The rule removes only the
authorized local 0.15-mm width/clearance accounting; the remaining findings
are real corridor crossings and one board-GND transition.

After adding the real board-GND continuation and removing two redundant
single-layer vias, the candidate reports 10 native DRC violations and 0
unconnected items. All remaining findings are explicit same-layer corridor
crossings.

The latest coherent outboard U3 relocation trial is rejected at 31 native DRC
violations and 2 unconnected items, improving the prior 38/3 trial. Remaining
failures are localized to occupied B.Cu corridors and two local ground joins;
this is disposable route evidence, not a change to the frozen RTL9210B/V1603
authority.

The subsequent local ground-spine repair, including an outboard B.Cu perimeter
return to the existing board-GND transition at (115.6,78.0), improved the same
candidate to 24 native DRC violations and 0 unconnected items. The remaining
findings are physical corridor/clearance issues; this remains disposable
implementation evidence.

The latest real-pad full-board support attempt is rejected at 38 native DRC
violations and 3 unconnected items. It improved the prior 6-open result but
still crosses occupied SPI/control/power corridors. This is route-implementation
evidence only; the next bounded repair is coherent local support-island
translation, with U1 orientation and V1603 launch frozen.

The MIC2545A fixture correction is complete: U3.2/FLG is netless rather than
incorrectly tied to GND. Native DRC, physical duplicated-pin joins, negative
control, and DFM pass. The prior combined-placement trial is rejected. The
latest full-board overlay reports 37 native DRC violations and 6 unconnected
items; the preceding overlay reported 36 violations and 6 opens. Neither is
production authority. Build one fresh co-routed U1.12-to-U3.1 support candidate
next, retaining the frozen
RTL9210B orientation, local QFN rule, and V1603 launch.

The disposable combined U1/MIC2545A fixture now passes native KiCad DRC
0/0/0 and its saved-board audit: U1.12→U3.1, IN 5/7, OUT 6/8, rail, ILIM,
and ground ownership are physically connected; U3.2/FLG is netless; and the
ISOLATEB trace-removal negative control fails as required. This is a geometry
and authority proof only; full-board promotion remains the next gate.

## Safe pause / GitHub checkpoint — 2026-09-10

The active RTL9210B Path-B routing work is paused at the validated local
support/launch checkpoint. No route search is running. The latest committed
checkpoint is `21a3002c` (`phase24: record MIC2545A support pin authority`).
The accepted orientation remains U1 RTL9210B-CG, 0 degrees, top side, pin 1
southwest, V1517 lineage; orientation search is closed.

The current isolated candidate is
`PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED.kicad_pcb` (generated from the
V1523 support baseline). Native KiCad DRC reports 0 violations, 0
unconnected items, and 0 footprint errors. The saved-board six-net audit
passes all six U1-to-J1 high-speed mappings and six actual-trace-removal
negative controls. The route-policy metrics are in
`PHASE24_RTL9210B_PATHB_V1603_METRICS.json`.

This is an isolated Path-B implementation checkpoint, not Phase 24 closure.
Open gates are full Path-B authority/procurement/firmware/bring-up,
production parity, acreage integration, and the remaining Phase 24 native
validation. Path A remains preserved. Historical disposable experiments are
not current routing authority.

Resume from `21a3002c`. The next productive action is a corrected disposable
MIC2545A support fixture: both duplicated `IN` pins and both duplicated `OUT`
pins must be physically joined, with native connectivity and a negative
control. The authoritative pin correction is recorded in
`authority-inventory/rtl9210b/MIC2545A_ISOLATEB_SUPPORT_AUTHORITY.md`.
Do not reopen U1 orientation or revive rejected route bases.

## Post-pause audit — 2026-09-10

The saved-board census `phase24_rtl9210b_pathb_census.py` passes against the
actual pads, tracks, vias, and zones: all asserted U1/J1 net identities and
six endpoint connections pass, six actual-trace-removal negative controls
fail as required, and no legacy `PiSXMe:` namespace is present. The current
native DRC receipt reports 0 violations, 0 unconnected pads, and 0 footprint
errors. This strengthens the isolated Path-B CAD gate only; it does not close
firmware, procurement, production parity, acreage integration, or full Phase
24 validation.

The corrected local RTL9210B QFN land pattern also passes
`phase24_rtl9210b_landpattern_audit.py`: 69 SMD/F.Cu pads, GND exposed pad
69 at 4.8 x 4.8 mm, and no `through_hole` metadata in the source module.
This is isolated CAD/DFM evidence; traceable production land-pattern
confirmation remains open.

## Generator transition correction — 2026-09-10

The layer-transition audit found one real RTL_3V3 B.Cu/F.Cu handoff in the
V1523 baseline without a via at (99.6, 66.05). The generator was corrected
to remove that adjacent-QFN stub and place the through-via at (99.6, 66.8),
outside the USB_DM/RTL_1V1 pad envelope. Regenerated native DRC is 0
violations, 0 unconnected pads, and 0 footprint errors; the layer-transition
audit reports zero un-viaed handoffs. Endpoint connectivity and all six
negative controls remain passing. This is a local implementation correction,
not an orientation or architecture change.

## MIC2545A support fixture — 2026-09-10

The disposable `PHASE24_MIC2545A_SUPPORT_FIXTURE.kicad_pcb` now passes native
KiCad DRC with zero violations, zero unconnected pads, and zero footprint
errors. Its saved-board audit proves physical duplicated-pin joins for
MIC2545A `IN` 5/7 and `OUT` 6/8, and its trace-removal negative control passes.
Its 1.27-mm pitch, 5.40-mm row spacing, and 1.55×0.60-mm pads match
Microchip's current recommended 3BX SOIC land pattern; mask/paste/courtyard
DFM geometry is now authored explicitly, but final assembly-house review and
production RTL9210B integration remain open. Receipt:
`PHASE24_MIC2545A_SUPPORT_FIXTURE_RECEIPT.md`.

The independent `phase24_mic2545a_dfm_audit.py` now passes against the saved
PCB: all eight pads are SMD/F.Cu with 1.55×0.60-mm dimensions, 1.27-mm pitch,
5.40-mm row spacing, explicit mask/paste settings, and present courtyard and
silkscreen graphics. This closes the disposable footprint geometry audit;
assembly-house review and production integration remain open.

The first MIC2545A-to-Path-B integration trial is rejected as
`REJECTED_ROUTE_IMPLEMENTATION`: native DRC found 22 violations and 4 opens
from the attempted U1.12 and SSD_3V3 corridor geometry. It does not invalidate
the corrected support circuit or frozen V1517/V1603 baseline. Receipt:
`PHASE24_MIC2545A_INTEGRATION_TRIAL_REJECT.md`.

Native pad inspection records the specific next escape class in
`PHASE24_RTL9210B_ISOLATEB_ESCAPE_ANALYSIS.md`: U1.12 is in a 0.4-mm-pitch
0.2×0.9-mm pad row, so lateral escape is not legal at the current route
width/clearance. The next repair must use a pad-end vertical escape and an
outboard ordinary via before attaching the local support network.

The first shifted-corridor source-escape probe is also rejected as a route
implementation: native DRC found 17 violations, specifically crossings into
PEDET/PERST_N and via/ground-zone clearance conflicts. Its raw board/report
are preserved with the escape analysis; no copper from either probe is
promoted.

The latest opposite-side jog reduces the isolated escape probe to two native
crossings, specifically the existing `RTL_5V` and `PERST_N` pad-row
departures. The next in-scope repair is a coordinated local reroute of those
adjacent departures around U1.12; no new MIC2545A topology or RTL9210B
orientation search is warranted.

The left-dogbone escape variant also fails native DRC with four violations
(PEDET via collision, CLKREQ_N crossing, and JTAG_TDO/pad-row clearance).
Simple ISOLATEB escape variants are exhausted; the next repair is coordinated
source-row rerouting or a bounded local support relocation.

The canonical blocker packet for this recoverable routing issue is
`PHASE24_RTL9210B_ISOLATEB_UNBLOCKER_PACKET.md`. The custom unblocker agent
was unavailable because the agent-thread limit was reached; local blocker
analysis was performed instead. The next bounded implementation is a
co-routed U1 south-row repair or, if that is not viable, relocation of only
the nearest support/via field. No orientation or architecture decision is
being reopened, and no rejected probe copper is authority.

The first relocation-class probe is also rejected as
`REJECTED_ROUTE_IMPLEMENTATION`: `PHASE24_RTL9210B_MIC2545A_SUPPORT_RELOCATED.kicad_pcb`
has 26 native DRC violations and 5 unconnected items. It confirms that
moving MIC2545A alone, without co-planning U1 south-row departures and the
existing PEDET/power corridors, is insufficient. The next attempt must use
one physical channel plan for those handoffs; orientation and architecture
remain closed.

The staggered source-row funnel probe is preserved as
`PHASE24_RTL9210B_SOURCE_ROW_STAGGERED_FUNNEL.md`. Its reserved 1.0-mm via
rows and parallel B.Cu handoffs are separated, but native DRC still reports
two real adjacent-U1 pad-end clearance violations (9 total fixture findings,
4 intentional remote opens). This narrows the remaining capacity problem to
the first QFN handoff; the next production-worthy repair must re-author that
handoff geometry or use an explicitly approved finer local escape rule.

The directional variant of the same funnel (ISOLATEB west, neighboring
controls east) was also rejected: native DRC found 11 findings, including
four U1 pad-clearance violations. The downstream channels remain separable;
the remaining blocker is specifically the frozen 0.4-mm QFN source handoff
under the production 0.20-mm trace/clearance envelope.

The authorized local exception has now been implemented in
`PHASE24_RTL9210B_FINE_QFN_ESCAPE_FIXTURE.kicad_pcb`: native DRC is 0/0/0,
all five source-to-handoff connections and five actual trace-removal
negative controls pass, and the scope guard proves 0.15-mm geometry is
confined to the QFN window with 0.20-mm handoff tracks. The receipt records
the selected rule and the earlier DFM rejection as superseded historical
evidence. Apply this proven primitive to the integrated support field next;
do not alter U1 orientation or V1603.

The first coordinated local reroute of U1.12 `ISOLATEB`, `CLKREQ_N`,
`PERST_N`, and `RTL_5V` is rejected: native DRC found 12 violations and zero
opens. The exact conflicts are recorded in
`PHASE24_RTL9210B_LOCAL_DEPARTURE_REPAIR.md`; the accepted baseline remains
untouched.

## Support parity consolidation — 2026-09-10

Claude's bounded review identified the missing consolidated support audit.
The new native audit passes 14 mapped support groups against actual saved-
board connectivity. The integrated candidate now restores the V12 `TP6`
endpoint for `RESET_N`; only `ISOLATEB` and `PERST_N` remain boundary/control
findings. Receipt:
`PHASE24_RTL9210B_PATHB_SUPPORT_PARITY_RECEIPT.md`.

The retained RTL9210B reference XML narrows `ISOLATEB` to a documented
corroborating pattern: U1.12 enables a MIC2545A-1YM SSD high-side switch.
This is recorded in `RTL9210B_ISOLATEB_CORROBORATION.md`; it remains a
candidate until PiSXMe rail/inrush/fault authority is reconciled.

Date: 2026-09-10

## Paused state

The active work is Phase 24 RTL9210B Path-B implementation, isolated from
Path A and production CAD. Claude's accepted Path-B baseline remains U1
RTL9210B-CG at 0 degrees, top-side, pin 1 southwest, on the V1517 lineage.
The pause point is after the V1590 local QFN escape primitive and the V1591
handoff-to-J1 launch diagnostic.

## Evidence completed

- V1590: all six U1 high-speed source pads reach explicit west handoff pads;
  native connectivity and six trace-removal negative controls pass. Native
  DRC has zero shorts, crossings, and footprint errors; stripped-support
  warnings/opens are intentional fixture findings.
- V1591: starting from those handoffs, the native obstacle search placed four
  nets toward the actual J1/M.2 launch before no legal remaining launch was
  available. No incomplete route was promoted.
- Path-B authority, corroborating support, M.2 mapping, native netlist, and
  hierarchy-conflict audits remain passing. Path A and unrelated board work
  remain preserved.

## Current open gate

The bounded physical-envelope launch experiment is now successful as the
V1603 local primitive: all six U1-to-J1 high-speed nets are natively connected
with zero high-speed DRC errors and negative controls pass. The next work is
integrating this launch with the complete Path-B support network and acreage
candidate. The current integrated candidate has zero V1603 launch DRC errors;
native integrated six-net connectivity and negative controls pass. Remaining
support-field warnings/opens are still open and must be closed before Phase 24
promotion. Orientation search remains closed and no validation severity or
layer rule may be relaxed.

The current baseline is now `PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED`:
it applies the accepted launch to the clean V1517 support board. Native DRC
has zero high-speed errors; seven support opens and two inherited warnings
remain. Continue by repairing RTL_1V1/XTAL_IN support in this local field,
then rerun the integrated audit.

The current generated candidate now passes the local repair: native DRC is
0 violations / 0 unconnected items, and the integrated six-net audit with
six negative controls passes. The generator uses the V1523 RTL_3V3 support
baseline, accepted V1603 launch, east-side RTL_1V1 closure, and V1534/V1526
crystal corridors. Continue with broader Path-B support, production parity,
and Phase 24 validation; do not reopen U1 orientation.

`PHASE24_STATUS.md` now has a current-state override documenting this clean
V1603/V1523 candidate; older V1517/V1583 prose remains historical evidence.

The V1523-source-hand-off trial is rejected: preserving the old RTL_1V1
corridor causes REFCLK_P crossings, while a near-QFN RXP via escape shorts
RXN/TXN under the production via envelope. This is a local source-field
implementation failure, not a contradiction of the frozen orientation or
V1603 launch. Continue from `21b6c1f0` with a co-authored 1V1/source-field
departure outside the QFN south-edge pair envelope.

## Resume point

Resume from the pushed checkpoint containing this note. Historical rejected
experiments and raw evidence remain immutable; do not use the old V1517
overlay routes as current production authority.

## CURRENT PATH-B SUPPORT CANDIDATE — 2026-09-11

The disposable open-acreage MIC2545A support candidate now has native KiCad
DRC 0 violations and 0 unconnected items. The remaining QFN source handoff
uses the authorized local exception: 0.15 mm immediate escape geometry and a
single local 0.40/0.20 mm ordinary through-via for `CLKREQ_N`; normal board
geometry remains 0.20 mm trace/clearance and 0.60/0.30 mm vias. The candidate
sidecar rule records the local via exception; it does not change validation
severity or global board rules.

Saved-board support connectivity passes for U3/MIC2545A, R15, C18, the U1
`ISOLATEB` handoff, both switched-output pins, and the existing J1 rail. Two
actual trace-removal negative controls pass; GND is independently retained by
the filled-zone connection and is audited as such. This is an integrated
Path-B candidate checkpoint, not Phase 24 closure: schematic parity, full
support-field authority, production integration, and broader Phase 24 gates
remain OPEN.
