# Append-only project bible

## 2026-08-30 — Phase 16 PCIe routing checkpoint

- Added the native-loaded Phase 16 PCIe candidate and focused regression.
- Preserved exact PER0/REFCLK/PERST/PET0 net graphs and the transmitter-side
  AC-coupling split at 0.13208 mm track width with ordinary 0.50/0.30 mm vias.
- Native DRC has zero target-net shorts, crossings, or dangling vias. Two
  authoritative CM5 SMD breakout clearance findings remain explicitly marked
  `REV_A_EMPIRICAL_RISK`; inherited acreage DRC debt is not conflated with
  this focused route gate.

## 2026-08-30 — Phase 17 Ethernet authority checkpoint

- Promoted the eight CM5 Ethernet MDI boundaries to native global named nets
  and corrected the generated symbol pin-Y convention and instance UUID path.
- Native ERC is zero and the XML netlist proves J7-to-ESD-to-MagJack mapping
  for all eight pairs; PCB regeneration is required before routing.

## 2026-08-30 — SERVICE ESD procurement recorded

- Added TI `TPD2EUSB30DRTR` current procurement evidence to the matrix and
  kept its package-specific land-pattern gate explicit.


## 2026-08-30 — SERVICE ESD electrical authority corrected

- Replaced the four-pin USB2 ESD placeholder with TI `TPD2EUSB30DRTR`, using
  the actual two-I/O-plus-ground interface and documented active procurement.
- Explicitly kept its exact DRT land pattern gated; no generic SOT-23 pattern
  is being treated as equivalent.


## 2026-08-30 — Native netlist export gate closed

- Reproduced and fixed underscore-bearing KiCad references generically.
- Native KiCad 10.0.5 netlist export now completes without annotation warnings;
  added an isolated regression test and receipt.
- Corrected the service-authority rerun path so the USB-C footprint cannot be
  assigned to the separate unresolved service ESD placeholder.


## 2026-08-30 — KiCad annotation normalization path added

- Identified underscore-bearing generated references as the cause of KiCad
  native annotation/netlist-export warnings.
- Added a generic normalization stage and regression test mapping them to legal
  unique references while retaining descriptive Value/MPN fields.


## 2026-08-30 — High-current input connector authority selected

- Selected two Molex `0039300020` / `39-30-0020` Mini-Fit Jr. 5569
  right-angle 2-position headers for the independent 12 V inputs.
- Recorded active-series, multi-distributor procurement evidence and the
  through-hole assembly implication; exact land-pattern materialization remains
  a required Phase 14 PCB step.


## 2026-08-30 — Phase 14 CM5 and MagJack pattern gates verified

- Added machine checks for the clean CM5 200-pad footprint/model and EDAC
  18-pad MagJack footprint, including rejection of the legacy Trxcom pattern.
- Kept SXM2 exact mask/paste/A1 and high-current input connector authority open.


## 2026-08-30 — Phase 14 service authority regression correction

- Updated the Phase 8 audit to require the selected Amphenol
  `10171746-00021LF` instead of the retired generic USB2 placeholder.


## 2026-08-30 — Ethernet MagJack authority replacement

- Closed the former exact `TRJG0926HENL` procurement gap with EDAC
  `A70-112-331N126`, backed by the EDAC manufacturer drawing and a current
  exact Mouser record showing New Product lifecycle, MOQ 1, and immediate
  stock. The original Trxcom part remains an immutable reference only.
- Recorded the EDAC electrical/mechanical contract, procurement evidence,
  `MEDIUM` sourcing risk, LINK-PP backup, URLs, and provenance under
  `pisxme/reva-clean/authority-inventory/primary-docs/ethernet-magjack/`.
- Explicitly rejected reuse of the legacy footprint: its two 3.20 mm plus two
  1.70 mm non-plated holes do not reproduce the EDAC drawing's two 3.25 mm
  plus four 1.02 mm hole groups. Phase 3 must generate and parity-check the
  EDAC land pattern in the clean namespace.

## 2026-08-30 — Phase 3 clean-library extraction checkpoint

- Added a deterministic extractor for the approved CM5IO `ComputeModule5-CM5`
  and Ethernet symbol definitions, rewriting them into the local
  `PiSXMeRevAClean` namespace and removing donor footprint/model references.
- Copied the approved CM5 carrier footprint/model into the project-local
  library and added the EDAC MagJack footprint derived from the EDAC drawing;
  the EDAC footprint keeps the exact EDAC hole groups and has no unvalidated
  3D model attached.
- Added a structural CM5 symbol-pin to footprint-pad parity check: 200 numeric
  symbol pins equal 200 numeric footprint pads. Native KiCad PDF parse/export
  for the root and all ten child sheets also passed; Phase 3 connectivity/ERC
  remains open.

## 2026-08-30 — EDAC hole-group authority correction

- Corrected the EDAC authority record to retain the complete manufacturer
  mechanical pattern: two 3.25 mm holes, two 1.60 mm holes, and four 1.02 mm
  guide holes. The clean generated footprint and its receipt already carry
  all eight holes; the authority narrative now matches the artifact.

## 2026-08-30 — Phase 3 native contract connectivity

- Added deterministic local contract symbols and native wire connectivity to
  all ten clean child sheets. Every child interface label now terminates on a
  real passive pin in the local `PiSXMeRevAClean` namespace.
- Fresh KiCad 10.0.5 ERC reduced the scaffold from 78 to 40 violations; the
  remaining records are root sheet-pin/child hierarchy association failures.
  The Phase 3 receipt records this as an open technical gate rather than
  suppressing ERC or treating the scaffold as production connectivity.
- Added all ten contract definitions to the project-local symbol library and
  kept the selected CM5/EDAC production assets separate from these fixtures.

## 2026-08-28 — M2 right-edge outline expansion checkpoint

- Expanded only the active board's congested right edge from 220 × 140 mm to 240 × 140 mm and moved J9/J10/J11 to x=230 mm so their bodies remain inside the new edge. CM5, PCIe, power, ESD-support placement, routing, zones, schematic, and manufacturing outputs were not changed.
- Structural evidence: J9/J10 retain approximately 1.65 mm edge margin and J11 approximately 3.30 mm; signal segment counts and the In1/In2/In3/In4 signal-layer policy are unchanged. Isolated native DRC completed with 785 inherited violations and 178 unconnected items, so this is not a routing or release signoff.
- M6 owns all connector-side copper reconstruction and must revalidate mating, cable, courtyard, return-path, and signal-termination behavior before the expansion becomes release geometry.

## 2026-08-22 — UART and recovery routing checkpoint

- Routed the actual CM5 net-bearing UART/recovery pads: J2 pad 51 `/UART_RX`, J2 pad 55 `/UART_TX`, and J2 pad 93 `/CM5_nRPIBOOT`. The route uses a deliberate upper/perimeter escape with F.Cu/B.Cu transitions for UART and a short F.Cu control route for recovery.
- The internal UART header J8 was moved to `(214,81)` and rotated 90 degrees so its plated through-hole pads remain clear of existing USB/PCIe through-layer copper. The nRPIBOOT test point TP3 was moved to `(145,125)` to keep recovery access out of the V100 power trunk and the regulator output cluster. No schematic nets or logical assignments changed.
- Final measured routes are `/UART_RX` 125.660 mm with 2 vias, `/UART_TX` 146.460 mm with 2 vias, and `/CM5_nRPIBOOT` 55.860 mm with no vias. Lock-free KiCad 10.0.5 DRC on a project copy returned 67 inherited library/silkscreen findings and zero new electrical, clearance, crossing, mask, hole, dangling, or sliver findings. Receipt: `routing/UART_RECOVERY_ROUTING_RECEIPT.md`.

## 2026-08-22 — local low-speed control subset checkpoint

- Routed `/GATE_A`, `/GATE_B`, and `/RT_1MHZ` as a deterministic local-control subset. The gate-B path was deliberately kept around the existing VCAP_B and high-current copper; the RT timing path enters U1 from below rather than crossing the CM5 feedback pads.
- The checkpoint adds 8 F.Cu segments and no vias. Lock-free KiCad 10.0.5 DRC on a project copy returned 68 inherited library/silkscreen findings and no new shorts, crossings, clearances, mask bridges, hole conflicts, dangling routes, or copper slivers. Longer low-speed/control trunks remain for the next pass. Receipt: `routing/LOW_SPEED_LOCAL_CONTROL_RECEIPT.md`.

## 2026-08-22 — SERVICE USB2 routing checkpoint

- Routed the CM5 USB2 SERVICE data pair through U15 to both reversible J11 USB-C orientations. To remove a real conflict with the already committed FAST-A/FAST-B corridors and lower-right power/debug copper, J11 and U15 were moved to the clear right-edge gap at `(210.5,40)` and `(196,40)`; no schematic nets or USB role logic changed.
- The deterministic checkpoint adds 28 segments and 6 F.Cu↔B.Cu vias. `/USB_SERVICE_DP` is 112.4712 mm total and `/USB_SERVICE_DM` is 105.2728 mm total. The route uses F.Cu/B.Cu only and does not enter the PCIe or USB3 corridors.
- Lock-free KiCad 10.0.5 DRC on a project copy returned 68 inherited library/silkscreen findings and no new service-route shorts, crossings, clearances, hole conflicts, mask bridges, dangling items, or copper slivers. The two remaining SERVICE CC1/CC2 unconnected items are intentionally deferred to the low-speed/control routing class. Receipt: `routing/SERVICE_USB2_ROUTING_RECEIPT.md`.

## 2026-08-21 — USB peripheral 5 V routing checkpoint

- Routed the independent `/USB_5V_PERIPH` output from U16 to both FAST-A/FAST-B source-switch input pairs and the SERVICE current limiter. The deterministic checkpoint adds 20 segments and 4 vias; U13 was moved from `(184,132)` to `(184,138)` to keep its input out of the FAST-B RX2 escape window and away from the recovery test pad.
- Lock-free KiCad 10.0.5 DRC on a project copy returned 69 inherited library/silkscreen findings and 379 expected unconnected items, with zero new shorts, crossings, clearances, mask bridges, hole conflicts, dangling routes, or width violations. Receipt: `routing/USB_5V_ROUTING_RECEIPT.md`.

## 2026-08-21 — CM5 5 V output routing checkpoint

- Routed the U1 `/CM5_5V` output to the buck's separated output pads, C5/C6/C7, the CM5 feedback branch, and all six official CM5 +5 V contacts on J2. The deterministic checkpoint adds 29 segments and 2 vias; the long contact-to-buck trunk stays left of the FAST-B USB3 transition field and the local output manifold stays left of the USB-C control packages.
- Lock-free KiCad 10.0.5 DRC on a project copy returned 69 inherited library/silkscreen findings and 386 expected unconnected items, with zero new shorts, crossings, clearances, solder-mask bridges, hole conflicts, dangling routes, or width violations. Receipt: `routing/CM5_5V_ROUTING_RECEIPT.md`.

## 2026-08-21 — CM5 protection-side power routing checkpoint

- Corrected and routed the LM74700 U2/U3 protected-bus input/cathode pads plus C8/C9 VCAP/fused support paths. The deterministic checkpoint adds 22 local-power segments and 4 vias while leaving CM5/USB output rails, ground zones, and control nets for later classes.
- Lock-free KiCad 10.0.5 DRC on a project copy returned 69 inherited library/silkscreen findings and 398 expected unconnected items, with zero new shorts, crossings, clearances, mask bridges, or width violations. Receipt: `routing/CM5_POWER_ROUTING_RECEIPT.md`.

## 2026-08-21 — CM5 power-pin correction before regulator routing

- Before continuing the power class, an audit against the preserved official CM5IO netlist found that J2 pads 77/79/81/83/85/87 were stranded on a legacy `/5V` net rather than the U1 `/CM5_5V` buck output, while the official CM5 3.3 V output pads 84/86 were unassigned. The schematic generator, active schematic, and active PCB were corrected to expose and assign those exact pins; no high-speed or connector geometry changed.
- This is a genuine source-connectivity correction. It is recorded separately in `routing/CM5_POWER_PIN_CORRECTION.md` and must be validated before the CM5/USB rail routing checkpoint.

## 2026-08-21 — V100 high-current power routing checkpoint

- After correcting the protected power-source net names, routed the dual raw 12 V branches, branch fuses/protection entries, protected `/VPROT_12V` bus, distributed 13-transition SXM2 power feed, and CM5-buck input islands. The checkpoint adds 76 power segments and 39 power vias; the protected main trunk is 5.0 mm on B.Cu, with via arrays at branch and SXM2 transitions.
- Lock-free KiCad 10.0.5 DRC on a project copy returned 69 inherited library/silkscreen findings and 401 expected unconnected items, with zero new power-route shorts, clearances, solder-mask bridges, dangling items, hole-spacing errors, or width violations.
- Combined high-speed review was recorded before accepting the power class. PCIe/FAST-A remain measured; FAST-B's 5.209–9.586 mm SuperSpeed skews remain an explicit SI risk, not a hidden DRC success claim. No L2 reference-plane slot was introduced by the new power copper.

## 2026-08-21 — cooling-header protected supply correction

- A second power-source audit found J5/J6/J7 cooling-header supply pins on `/12V_FAN` with no source or net tie. Their intended protected 12 V supply is now `VPROT_12V` in the schematic generator, active schematic, and active PCB.
- This is a net-source correction before routing, not an added feature; fan/pump control nets and connector placement are unchanged.

## 2026-08-21 — protected V100 power-bus net correction

- Before beginning high-current routing, the active design was audited for a power-net boundary inconsistency. The SXM2 connector's 130 V100 power contacts were on `/12V`, while the protected dual-input bus and buck inputs were on `/VPROT_12V`, with no schematic tie.
- The authoritative topology is input connector → fuse → LM74700/MOSFET protection → protected V100 bus. The J1 PWR contract was corrected to `VPROT_12V` in the generator and schematic, and the active unrouted PCB was normalized to the same net without changing pin mapping or adding an implicit short.
- A lock-free KiCad 10.0.5 DRC run on a project copy returned normally (69 inherited non-unconnected findings and 499 expected unconnected items). High-current copper routing starts only after this checkpoint.

## 2026-08-20 — Initial KiCad inventory

- KiCad 10.0.5 is installed at `/Applications/KiCad/KiCad.app`.
- The official IPC server preference was found disabled and enabled for this integration.
- The bridge runtime target is Homebrew Python 3.11 with `kicad-python==0.7.1` and the MCP SDK.
- Direct inspection found broad PCB IPC coverage, CLI DRC/ERC/export coverage, and a broken/missing released schematic binding; this limitation is preserved in `CAPABILITY_MAP.md`.

## 2026-08-20 — Bridge implementation and live verification

- Added the modular `kicad-codex-bridge` MCP server using official `kicad-python==0.7.1`, KiCad IPC socket discovery/token caching, descriptor-driven protobuf introspection/raw calls, bundled `kicad-cli`, and a project-root-scoped atomic file layer.
- Registered the server globally with the current `codex mcp add` CLI using `KICAD_PROJECT_ROOT`; direct MCP stdio discovery returned 61 tools.
- Live KiCad 10.0.5 control succeeded on `/tmp/kicad/api.sock`: PCB inspection, footprint creation/move/rotation, pad inspection, board text/graphic/track/via creation, selection, save/save-as, readback, DRC, raw `GetVersion`, and Gerber export were verified on the disposable fixture.
- KiCad JSON DRC completed with six fixture violations; this is validation evidence, not a clean-design claim. ERC completed through `kicad-cli` against an untouched bundled KiCad schematic template.
- Schematic live IPC remains unavailable in this installed official wheel; footprint flip/mirror is also not faked because no native KiCad 10.0.5 IPC operation was exposed.

## 2026-08-20 — SXM2 reference archaeology

- Acquired and preserved `bbenchoff/SXM2toPCIe` at commit `3173b02c085218d66c4a2a9e5492853fb53ee097` under `references/SXM2toPCIe`; the upstream nested worktree remained clean.
- Opened a separate working copy through the live KiCad 10.0.5 IPC bridge and verified the PCB/schematic parse, local library resolution, and logical netlist agreement.
- Recorded the critical nonclaim: the pinned PCB is largely unrouted between J2 and the PCIe edge. KiCad DRC reported 73 violations and 285 unconnected items; ERC reported 472 violations. No upstream source was fixed.
- Added machine-readable SXM2/PCIe mapping, source manifest, constraints, power-tree evidence, conceptual board-zone annotation, and the hardware-archaeology report. CM5 integration remains intentionally out of scope.

## 2026-08-20 — Independent PCIe x1 architecture study

- Created branch `codex/pcie-x1-architecture` for the clean-room x1 design phase; no final combined-board schematic or PCB layout was created.
- Acquired the public LiuXinyu12378 carrier reference at commit `27dd1229889f4f0c03324b419931d2d466fccde4` and the official Raspberry Pi CM5IO revision-2 KiCad archive (ZIP SHA-256 `48b14a6757b0edc0ac110331445f35a4212b5ce432bdcec6605c99431b59496b`); both are ignored immutable observation references.
- Confirmed from the official CM5 datasheet that CM5 is a PCIe Gen2 host, direct-IC TX/RX must cross by function, CM5 TX coupling is internal, V100/peripheral TX needs external 220 nF coupling near the source, PCIe is 90 Ω, within-pair matching is ideally 0.1 mm, `CLKREQ#` and `PERST#` are mandatory, and `WAKE#` is currently unsupported in software.
- Derived an independent one-lane topology and corridor: lane 0 first candidate, no lanes 1–15, no card-edge branch, Gen2 first bring-up, no retimer, adjacent CM5 provisionally preferred, six layers recommended for the power/return budget, and zero high-speed vias preferred.
- Recorded unresolved gates instead of guessing: V100 common-clock/SSC compatibility, V100-side impedance tolerance, CM5 `CLKREQ#` policy, V100 power sequencing/current capacity, and underside cooler/connector clearance.
- Added clean-room requirements, provenance, architecture, placement options, stackup study, machine-readable signal map, logical topology diagram, board constraints, and independent zone sketch under `design/`.

## 2026-08-20 — PCIe interface, mechanical envelope, and first PiSXMe schematic

- Created branch `codex/pcie-x1-interface-mechanical` from the independent x1 architecture commit. The prior reference branches and immutable upstream material were not modified.
- Resolved the first schematic policy from official CM5 documentation: direct CM5-generated 100 MHz REFCLK, Gen2 first bring-up, local always-requested CM5 `CLKREQ#`, direct CM5 `/PERST`, unused `WAKE#`/slot presence, and external 220 nF coupling only on the V100 transmitter direction.
- Preserved the official Raspberry Pi CM5 STEP package at `references/RaspberryPi-CM5-step/` with ZIP SHA-256 `2b4d26c6b30607c68099ad60df6fb8b8c8d04e9461f325c7c77dc421d2855005`.
- Added the phase-2 interface contract, clock/sideband analysis, AC-coupling analysis, mechanical envelopes, combined placement concept, board architecture, power architecture/tree, hostile review, ERC report, and conceptual mechanical SVG.
- Created a new blank-template-derived `pisxme/PiSXMe.kicad_sch` and matching project file. KiCad 10.0.5 parsed it and exported netlist/PDF; ERC is intentionally preserved as non-clean (19 violations: 8 errors, 11 warnings) because connector/control symbols and final hierarchy remain gated on V100/CM5 validation.
- Kept the principal blocker explicit: public NVIDIA material describes the SXM2 system interface as NVLink, so direct reverse-engineered PCIe operation, endpoint clock acceptance, and power sequencing require real-module bring-up before PCB release.

## 2026-08-20 — Cooler-agnostic PiSXMe component placement study

- Created branch `codex/cooler-agnostic-placement` for the cooler-independent Rev-A placement phase. External cooling remains interchangeable: the board contract reserves a 150 × 95 mm cooler-owned topside footprint plus a matching underside backplate/retention volume and does not choose a heatsink or waterblock.
- Selected real Rev-A component candidates: Amphenol `74221-101LF` SXM2 receptacle, two Amphenol `10164227-1004A1RLF` 4.0 mm CM5 connectors, dual Molex `39301062` Mini-Fit Jr. inputs, TI `TPSM63606RDLR` CM5 buck, TI `LM74700QDBVRQ1`/`CSD19536KCS` protection candidates, Littelfuse fuse positions, and JST cooling/debug headers. The exact CM5 1004 connector CAD download was blocked by the manufacturer CDN and was not replaced with the 1001 model.
- Generated a new 220 × 140 mm six-layer `pisxme/PiSXMe.kicad_pcb` with real land patterns, CM5 STEP body, mechanical zones, cooling contract drawings, and serviceable adjacent-CM5 placement. No production PCIe routing, power pours, final planes, Gerbers, or restricted reference geometry were used.
- Replaced the old schematic placeholder pass with an MPN-resolved architectural schematic and local symbol/footprint tables. KiCad 10.0.5 exported the schematic PDF/netlist and reported 0 ERC errors; 110 warnings remain explicitly classified as grid cleanup, intentional low-speed isolated labels, and library-link configuration.
- KiCad placement DRC reported 120 violations and 0 unconnected items; violations are recorded as pre-routing study properties, not suppressed as production sign-off. Top/bottom/front/isometric 3-D renders and an annotated placement SVG are preserved under `pisxme/renders/`.
- Final unresolved gates remain real V100 endpoint/clock/reset/power validation, full CM5/SXM2 pin audit, exact V100/cooler/backplate geometry, exact 1004 connector model alignment, fabricator-specific impedance stackup, and high-current copper/thermal design.

## 2026-08-20 — Final electrical and manufacturing signoff audit

- Created the 400-pad SXM2 audit CSV/MD from the published 40x10 map and preserved source disagreements rather than normalizing them.
- Corrected the earlier Molex power-input MPN from 39301062 (six circuits) to 39301082 (eight circuits), corrected the fuse-holder choice, replaced the invalid 220 pF coupling identifier with a 220 nF candidate, and selected 2.54 mm Molex fan headers.
- Corrected the TPSM63606 pin contract in the schematic generator and produced an independent unrouted placement-study PCB with no tracks, vias, or copper zones.
- Routing readiness remains NOT_READY_FOR_ROUTING pending hydrated KiCad ERC/DRC validation, pin-level power implementation, critical-footprint audit, and fab-returned impedance geometry.

## 2026-08-20 — Routing-readiness blocker closure

- Created branch `codex/routing-readiness-blocker-closure` from the prior electrical/manufacturing signoff. The source project remains production-unrouted: zero tracks, vias, and zones; no Gerbers or board order were produced.
- Diagnosed the KiCad 10.0.5 CLI behavior. The reliable procedure is a complete lock-free project copy run from its project directory; direct board DRC can still hang after stale-lock cleanup. The status is `CLI_WORKAROUND_VALIDATED`, with JSON and human-readable receipts preserved under `validation/`.
- Refreshed final receipts: ERC completed with 0 errors and 185 warnings; DRC completed with 211 errors, 20 warnings, and 0 unconnected items on the unrouted placement study. These are evidence receipts, not clean signoff.
- Captured the current JLCPCB `JLC06161H-7628` stack and 85 ohm calculator result: 5.2 mil width, 2.78466796875 mil pair gap, 84.9965876269 ohm returned. The individual API response does not encode order-specific tolerance; the official CM5 90 ohm guidance remains an explicit reconciliation gate.
- Corrected the SXM2 audit: the 400-pad map contains 130 nominal 12 V contacts, 170 ground contacts, 31 published NC contacts, and two unresolved auxiliary contacts K18/K19. K19 is not GND; no speculative K18/K19 circuit was added. Contact-current arithmetic is below the 0.45 A/contact Amphenol rating, but connector/PCB thermal signoff remains open.
- Preserved official manufacturer-resource URLs and recorded the released Amphenol MEG-Array contact-performance evidence. Exact 74221 land-pattern/mask/paste/orientation and several assembly-critical footprints remain unverified; no third-party CAD was promoted to authority.
- Reviewed V100 clock/reset/power evidence and working carrier active circuitry. The direct Gen2 x1 topology remains a rational Rev-A experiment, but exact V100 sequencing, SSC/common-clock acceptance, and K18/K19 behavior still require hardware validation. Final decision: `NOT_READY_FOR_ROUTING`.

## 2026-08-21 — Standard PCIe endpoint and manufacturer-land-pattern blocker closure

- Created branch `codex/standard-pcie-sxm2-signoff` without modifying immutable upstream references or routing the production PCB.
- Adopted the explicit Rev-A policy that V100 SXM2 is a standard PCIe endpoint behind a non-standard connector. Direct Gen2 x1 data, common-clock REFCLK, direct PERST#, local always-requested CM5 CLKREQ#, and one external 220 nF capacitor per V100 TX conductor remain the contract.
- Created an independent Amphenol-derived 74221-101LF footprint with exactly 400 circular pads, 10 x 40 at 1.27 mm pitch, 0.635 mm pads, 0.150 mm solder-mask margin, no vias in pads, and a 5.10 mm rework allowance. The active PCB still contains its older embedded study footprint; this distinction is preserved and the footprint signoff remains `NOT_VERIFIED`.
- Reviewed working/reference carriers for active logic. No universal PCIe bridge, retimer, redriver, CPLD, or protocol-conversion block was found to be required for a short single-GPU link; larger platform management/fanout logic is not treated as transport necessity.
- Rebased the board target to 90 ohm differential per CM5 documentation. The public JLC calculator failed to return a 90 ohm W1/S1 result, so the historical 85 ohm response was explicitly rejected as a routing substitute.
- Updated the Amphenol contact-current audit with the manufacturer's all-contact test context: 0.45 A/contact was characterized on specified solid 3 oz test boards at 25°C still air and ≤30°C rise. PiSXMe arithmetic remains 0.192–0.212 A per nominal V100 +12 V contact at 300–330 W, but PCB thermal equivalence is not claimed.
- Added standard-endpoint basis, active-logic review, community-contact record, manufacturer resource README, critical-footprint final audit, ERC/DRC receipts, JLC calculator attempt, hostile review, and the final routing-readiness gate. Current decision remains `NOT_READY_FOR_ROUTING` due the active footprint import/A1 verification, missing JLC 90 ohm result, ERC hygiene findings, and pre-routing courtyard/footprint closure.

## 2026-08-21 — Final routing-readiness closure

- Created branch `codex/close-routing-readiness` and kept the PiSXMe PCB production-unrouted: zero tracks, vias, and copper zones.
- Replaced the embedded J1 study footprint with the manufacturer-derived Amphenol `74221-101LF` model: 400 pads, 1.27 mm pitch, 0.635 mm copper land, 0.150 mm solder-mask margin per side, no pad vias, manufacturer A1 convention, and 5.10 mm rework allowance. UUID and active-footprint comparison artifacts are preserved.
- Corrected the active CM5 connector land pattern to the official Amphenol `10164227-1004A1RLF` two-row 0.4 mm geometry, corrected the Littelfuse fuse-holder hole pattern, and corrected the TI TPSM63606 RDL package model to include central PGND lands. All critical footprints are now manufacturer-verified or datasheet-derived-and-checked; none remains library-only or unresolved.
- Closed the JLC `JLC06161H-7628` 90 ohm geometry gate using the live public calculation API: L1 width 0.13208 mm / 5.2 mil, pair gap 0.085328 mm / 3.359375 mil, calculated 89.995806 ohm, with a 90.14944 ohm coated independent cross-check. The `PCIe_90R_L1_L2` KiCad pre-routing class is configured.
- Reran KiCad 10.0.5 from fresh lock-free project copies. ERC is 0 errors and 184 warnings with zero multiple-net-name findings; every remaining warning is documented as an intentional boundary label or reproducible CLI library-context limitation. DRC is 0 errors, 20 documented library-context warnings, 0 courtyard/clearance/silk/unconnected findings, and zero genuine pre-routing blockers.
- Final hostile review found no concrete evidence-backed routing blocker. Routing readiness is `READY_FOR_ROUTING`; V100 undocumented sequencing and first-hardware behavior remain explicit Rev-A risks, not claims of prior hardware validation.

## 2026-08-21 — Modular USB-C external I/O revision

- Created branch `codex/modular-usbc-io` for the intentionally production-unrouted I/O revision; the board remains at zero tracks, vias, and copper zones and no production Gerbers were generated.
- Confirmed from the official CM5 datasheet that USB3 ports 0 and 1 are independent 5Gbps interfaces and that USB2 is an independent interface separate from PCIe. Added USB-C FAST A for storage, FAST B for a commodity USB 2.5GbE adapter, and SERVICE for USB2 host/recovery use while retaining internal UART and nRPIBOOT access.
- Added the selected Type-C architecture: Amphenol `10137064-00011LF` FAST receptacles, Amphenol `10171746-00021LF` SERVICE receptacle, TI `HD3SS3212IRKSR` SuperSpeed orientation muxes, `TPS25821DSSR` 1.5A host VBUS/CC source controllers, `TUSB320LAIRWBR` SERVICE DRP controller, `TPS2553DBVR` 0.5A SERVICE limiter, TI USB ESD arrays, and dedicated `U16 TPSM63606RDLR` USB 5V rail.
- Corrected the FAST-port protection topology from duplicated SuperSpeed arrays to two official four-line `TPD4EUSB30` orientation-branch arrays plus one `TPD2EUSB30A` USB2 companion-pair array per FAST port; the CM5 D+/D− pins, receptacle contacts, and ESD pins now share the intended nets. Current lock-free KiCad 10.0.5 ERC reports 0 errors, 48 warnings (30 reproducible local-library context warnings and 18 intentional boundary labels), with zero multiple-net-name findings. Current lock-free DRC reports 36 local-library context warnings, zero geometry/courtyard/clearance/unconnected findings, and zero genuine pre-routing blockers.
- Updated the active-board signoff to `READY_FOR_ROUTING`; remaining gates are routing-time controlled impedance/plane implementation, manufacturer CAD overlays for the USB receptacles, SERVICE firmware/role validation, and first-hardware USB SI/EMI and driver testing.

## 2026-08-21 — Production-routing baseline

- Began branch `codex/modular-usbc-io` routing from commit `bcb184e17169e1c04dd6e230010ba5d330ab3321`; the original placement board remains preserved as the pre-routing checkpoint.
- Recorded the exact 220 × 140 mm board, six-layer declaration, KiCad 10.0.5 tool path, 36-footprint placement, and zero tracks/vias/zones in `routing/ROUTING_BASELINE.md`.
- Discovered that the placement-study generator intentionally stripped PCB pad nets and that the active board still carried generic stackup metadata rather than the captured JLC06161H-7628 dielectric/copper values. These are mandatory pre-routing materialization corrections before any production copper is added.

## 2026-08-21 — Materialize routing netlist

- Repaired the placement-study PCB structure after support footprints had been inserted inside the CM5 footprint block.
- Restored schematic connectivity onto the active board using explicit physical aliases for the SXM2, CM5, and USB-C connectors.
- Active PCB now contains 135 named nets and 741 assigned pads; no production copper has been added.
- Corrected active stackup metadata to the captured JLC06161H-7628 six-layer dielectric/copper values.
- Routing remains gated on KiCad validation and deliberate checkpointed copper work.

## 2026-08-21 — PCIe x1 routing checkpoint

- Routed the first production copper class: PER0, PET0 through the two external V100 TX coupling capacitors, and common-clock REFCLK. The active board now contains 60 route segments and 12 through-vias; all other production nets remain unrouted and no copper zones have been added.
- Used the final `PCIe_90R_L1_L2` geometry: 0.13208 mm track width, 0.085328 mm pair gap, and 0.20 mm unrelated-copper clearance on the JLC06161H-7628 six-layer basis.
- Measured pair skews are 0.0003 mm for PER0, 0.0214 mm for PET0 after coupling, 0.0035 mm for the raw capacitor legs, and 0.0430 mm for REFCLK. The CM5 connector fanout required controlled F.Cu/In3.Cu or F.Cu/B.Cu transitions, so the earlier zero-via preference is recorded as unattainable at this fixed placement rather than implied.
- Lock-free-copy KiCad 10.0.5 DRC reports no route crossings, shorts, clearance, width, drill, or via violations for the added PCIe copper. The receipt retains 499 expected unconnected items and 68 pre-existing library/silkscreen study findings; final return-plane continuity remains gated on the later ground/zones phase.

## 2026-08-21 — FAST-A USB routing checkpoint

- Routed the first independent CM5 USB 3 port through the HD3SS3212 mux to J9, including the USB 2 companion pair and both duplicated reversible USB-C USB 2 contact rows. FAST-B, SERVICE, power, zones, and final ground implementation remain unrouted.
- Reworked pair geometry after the first connected-only pass exposed material intra-pair mismatch. The final measured FAST-A/CM5 USB3 skews are 0.000–0.300 mm and the USB 2 DP/DM mismatch is 0.006 mm; no production route is accepted solely because it is connected.
- The FAST-A route contains 181 segments and 40 vias. Lock-free-copy KiCad 10.0.5 DRC reports 68 inherited findings (54 library-footprint and 14 silkscreen-over-copper) plus 499 expected unconnected items, with zero new shorts, crossings, clearance, width, hole, via, or other routing violations.
- Preserved the ordered route pipeline in `tools/route_usb_fast_a_final.py` and the measured receipt in `routing/USB3_FAST_A_RECEIPT.md`; the active board remains a checkpointed intermediate, not a released manufacturing package.

## 2026-08-21 — FAST-B USB routing checkpoint

- Routed the second independent CM5 USB 3 port through the HD3SS3212 mux to J10, including its USB 2 companion, moved FAST-B ESD device U18, and both duplicated reversible USB-C USB 2 contact rows. PCIe and FAST-A are retained; power, SERVICE, control, ground, and zones remain unrouted.
- Moved U18 from the crowded U11 area to PCB coordinate (204,127) without changing its logical pad assignments. The final USB2 fanout uses separate pad escapes and inner-layer transitions and is DRC-clean.
- Measured FAST-B route lengths from the active board: CM5 RX 69.4900/69.9900 mm (0.5000 mm skew), CM5 TX 69.0100/69.9100 mm (0.9000 mm), U9-to-J10 RX1 59.9142/69.5000 mm (9.5858 mm), TX1 40.2910/45.5000 mm (5.2090 mm), RX2 67.2361/74.5000 mm (7.2639 mm), TX2 23.7500/33.2500 mm (9.5000 mm), and USB2 DP/DM 115.4844/123.2770 mm (7.7925 mm). The dense U9/U10/U11/J10 placement mismatch is explicitly carried forward to the combined high-speed review; no same-layer meander was accepted after it created real crossings.
- The FAST-B route set contains 153 segments and 46 vias. Lock-free-copy KiCad 10.0.5 DRC reports 69 inherited findings (54 library-footprint and 15 silkscreen-over-copper) plus 499 expected unconnected items, with zero new shorts, crossings, clearances, width, hole, via, or other route violations.
- Preserved the ordered replay pipeline in `tools/route_usb_fast_b_final.py`, the auditable individual scripts under `tools/test_usb_b_*.py`, the validation receipt at `validation/usb-fast-b-drc.json`, the top SVG/3D render under `validation/render-usb-fast-b/`, and the measured receipt at `routing/USB3_FAST_B_RECEIPT.md`. This remains an intermediate routing checkpoint and is not a released manufacturing package.
# 2026-08-22 — CLKREQ# and CM5 VBUS-enable routing checkpoint

- Added the `/CM5_CLKREQ_N` route from CM5 J2 pad 102 to the local R1 strap,
  using a short F.Cu escape, In2.Cu trunk, and F.Cu return with two vias.
- Added the `/CM5_VBUS_EN` fanout from CM5 J2 pad 111 to the FAST-A/FAST-B
  TPS25821 enable pads, using an In4.Cu trunk and pad-aware F.Cu branches.
- The final trial was retained only after lock-free KiCad DRC produced no new
  electrical, clearance, crossing, hole, solder-mask, dangling, or sliver
  violations beyond the inherited library/silkscreen findings.
- This checkpoint intentionally adds no copper zones and does not close the
  remaining low-speed, ground, thermal, or final-validation work.
# 2026-08-22 — PCIe/V100 power-enable routing checkpoint

- Added the distributed `/PCIE_PWR_EN` route from CM5 J2 pad 106 to both
  TPSM63606 enable inputs and both LM74700 protection-controller enables.
- The fanout uses a right-edge In3.Cu trunk, an In1.Cu distribution branch,
  and short F.Cu pad-aware stubs. The route was deliberately reworked around
  PCIe clock vias, USB SuperSpeed escape vias, high-current copper, and the
  regulator switching/power pads.
- The accepted geometry has 18 segments and 6 vias and is clean in the
  lock-free KiCad DRC copy workflow apart from the inherited library and
  silkscreen findings.
- This checkpoint does not add zones and does not close PERST#, USB-C control,
  fan/pump, ground, thermal, or final-validation work.
# 2026-08-22 — PERST# routing checkpoint

- Added `/PERST_N` from CM5 J2 pad 109 to SXM2 J1 E18.
- The accepted route is 144.4588 mm across 14 segments and 2 vias, with an
  In4.Cu trunk and F.Cu escapes. The SXM2 side follows row-gap escape paths
  above the connector-side REFCLK fanout and places the layer transition
  outside the BGA footprint.
- Lock-free KiCad DRC reports no new electrical, clearance, crossing, hole,
  solder-mask, dangling, or sliver findings beyond inherited
  library/silkscreen findings.
- This checkpoint does not add zones and does not close USB-C control,
  fan/pump, ground, thermal, or final-validation work.

# 2026-08-22 — USB3 pass-2 placement/fanout gate

- Began `codex/usb3-pass2` from the frozen PCIe pass-2 checkpoint and preserved
  `routing/usb3-pass2/PiSXMe-before-usb3-pass2.kicad_pcb`; the active board
  remains unchanged with zero USB3 segments/vias.
- Verified the FAST-A/FAST-B CM5-to-mux, HD3SS3212, TPD4EUSB30, and Type-C A/B
  net map from the schematic. Isolated CM5 escapes and isolated mux-to-ESD
  differential pairs pass KiCad 10.0.5 electrical DRC in disposable copies.
- The complete FAST-A fanout does not pass when those individually valid routes
  are combined: KiCad reports real pair crossings/shorts/clearance errors, and
  a layer-aware trial exhausts the F.Cu/B.Cu channel for the remaining pair.
  This is a concrete local USB placement/channel blocker, not a PCIe conflict;
  no PCIe copper was modified and FAST-B was intentionally gated.
- No production USB3 route is claimed. The phase stops at a documented
  placement/layer decision rather than accepting a via-heavy or unreferenced
  route that would violate the established 90-ohm L1/L2 design basis.

# 2026-08-22 — FAST-A CC1 routing checkpoint

- Added `/USB_FAST_A_CC1` from J9 A5 to U4 TPS25821 pad 9 using a DRC-guided
  low-speed path with F.Cu escapes, an In2.Cu trunk, and two through-vias.
- The accepted path is approximately 66.8 mm of copper and remains electrically
  separate from the existing PCIe and USB SuperSpeed routes.
- Lock-free KiCad 10.0.5 DRC reports only the inherited 54 library-footprint
  and 13 silkscreen findings, with no new shorts, crossings, clearance, hole,
  mask, dangling, or sliver violations.
- This checkpoint adds no zones and does not close the remaining FAST-A/FAST-B
  control nets, power housekeeping, ground, thermal, or final-validation work.

# 2026-08-22 — FAST-A POL routing checkpoint

- Added `/USB_FAST_A_POL` from U4 TPS25821 pad 7 to U5 HD3SS3212 pad 9 using
  F.Cu endpoint escapes, an In4.Cu detour, and two through-vias. The path is
  approximately 55.05 mm and is isolated from the existing high-speed routes.
- Lock-free KiCad 10.0.5 DRC reports only the inherited 54 library-footprint
  and 13 silkscreen findings, with no new electrical or geometric violations.
- REF, CC2, VBUS, remaining control, ground, thermal, and zone work remains
  intentionally open for later checkpoints.

# 2026-08-22 — FAST-A REF routing checkpoint

- Added `/USB_FAST_A_REF` from U4 TPS25821 pad 8 to R5 pad 1 with a short
  8.81 mm F.Cu route that stays above the CC1/POL local entries.
- The combined FAST-A POL/REF checkpoint remains DRC-clean apart from the
  inherited 54 library-footprint and 13 silkscreen findings. No new shorts,
  crossings, clearances, or fabrication-rule findings were introduced.
- FAST-A CC2/VBUS, remaining control, ground, thermal, and zone work remains
  intentionally open.

# 2026-08-22 — FAST-A CC2 routing checkpoint

- Added `/USB_FAST_A_CC2` from J9 B5 to U4 TPS25821 pad 11. Because the local
  connector-to-controller area is occupied by accepted USB2/SuperSpeed
  escapes, the low-speed control net uses a three-via F.Cu/In1.Cu/In2.Cu
  detour around the board-edge routing region.
- The accepted path is approximately 109.96 mm with no branches or test-point
  stubs. It does not alter PCIe or USB3 geometry and remains outside the PCIe
  corridor.
- Lock-free KiCad 10.0.5 DRC reports 67 total findings: only the inherited 54
  library-footprint and 13 silkscreen findings remain. No new clearance,
  short, crossing, dangling-via, or solder-mask violations were introduced.
- FAST-A VBUS, FAST-B controls, SERVICE controls, ground, thermal, zones, and
  final routed validation remain intentionally open.

# 2026-08-22 — FAST-A VBUS routing checkpoint

- Added `/USB_FAST_A_VBUS` using a local F.Cu connector-side zone, a 2.50 mm
  U4 pad-12 escape, and an explicit 0.30 mm In1.Cu trunk with two ordinary
  through-vias. The accepted trunk is approximately 83.545 mm and uses no
  blind/buried vias.
- The final route is detoured around fixed FAST-B vias and the FAST-A CC2
  corridor. It does not alter PCIe or USB SuperSpeed geometry.
- Lock-free KiCad 10.0.5 DRC with zone refill/save reports 67 total findings,
  351 remaining unrouted items, and zero FAST-A VBUS-specific unconnected
  items. No new electrical or geometric violations were introduced; the only
  findings are the inherited 54 library-footprint and 13 silkscreen issues.
- FAST-B controls, SERVICE controls, ground, thermal, remaining power zones,
  and final routed validation remain intentionally open.

# 2026-08-22 — FAST-B REF routing checkpoint

- Added `/USB_FAST_B_REF` from U8 TPS25821 pad 8 to R6 pad 1. The accepted
  path is approximately 15.390 mm across four segments, with a short F.Cu
  escape, an In2.Cu detour through the local controller/capacitor congestion,
  and two ordinary through-vias.
- The route avoids the adjacent U8 CC1/CC2 pads, the CM5 5 V output capacitor,
  and the existing USB SuperSpeed vias without touching the PCIe corridor.
- Lock-free KiCad 10.0.5 DRC reports 67 total findings and 350 remaining
  unconnected items. No FAST-B REF-specific unconnected, short, clearance,
  crossing, mask, or via findings were introduced; only the inherited 54
  library-footprint and 13 silkscreen findings remain.
- FAST-B CC1/CC2/POL/VBUS, SERVICE controls, ground, thermal, remaining power
  zones, and final routed validation remain intentionally open.

# 2026-08-22 — FAST-B POL routing checkpoint

- Added `/USB_FAST_B_POL` from U8 TPS25821 pad 7 to U9 HD3SS3212 pad 9. The
  accepted path is approximately 36.803 mm across five segments, with an
  In2.Cu detour below the local controller/capacitor and USB SuperSpeed
  congestion and two 0.40/0.30 mm ordinary through-vias.
- The path avoids the U8 adjacent pads, the CM5 USB3 RX-N escape, the local
  USB 5 V copper, and the existing SuperSpeed via field without touching the
  PCIe corridor.
- Lock-free KiCad 10.0.5 DRC reports 67 total findings and 349 remaining
  unconnected items. No FAST-B POL-specific unconnected, short, clearance,
  crossing, mask, drill, or via findings were introduced; only the inherited
  54 library-footprint and 13 silkscreen findings remain.
- FAST-B CC1/CC2/VBUS, SERVICE controls, ground, thermal, remaining power
  zones, and final routed validation remain intentionally open.

# 2026-08-22 — FAST-B CC1 routing checkpoint

- Added `/USB_FAST_B_CC1` from J10 A5 to U8 TPS25821 pad 9. The accepted path
  is approximately 63.293 mm across nine segments, with F.Cu endpoint
  escapes, an In3.Cu/B.Cu detour around the J10 shield and existing USB
  routes, and three ordinary through-vias.
- The J10-side route stays below the connector contact row and outside the
  shield pad. No PCIe or USB SuperSpeed geometry was changed.
- Lock-free KiCad 10.0.5 DRC reports 67 total findings and 348 remaining
  unconnected items. No FAST-B CC1-specific unconnected, short, clearance,
  crossing, mask, drill, or via findings were introduced; only the inherited
  54 library-footprint and 13 silkscreen findings remain.
- FAST-B CC2/VBUS, SERVICE controls, ground, thermal, remaining power zones,
  and final routed validation remain intentionally open.

# 2026-08-22 — FAST-B CC2 routing checkpoint

- Added `/USB_FAST_B_CC2` from J10 B5 to U8 TPS25821 pad 11. The accepted
  path is approximately 58.107 mm across seven segments, with a narrow F.Cu
  U8 escape, an In4.Cu central route, and two 0.40/0.30 mm ordinary
  through-vias. The source-side via was moved below the C5 ground-pad edge to
  preserve manufacturable clearance.
- The J10-side route stays below the connector contact row and avoids the
  existing FAST-B USB3 DM/RX geometry. PCIe and accepted high-speed routes are
  unchanged.
- Lock-free KiCad 10.0.5 DRC reports 67 total findings and 347 remaining
  unconnected items. No FAST-B CC2-specific unconnected, short, clearance,
  crossing, mask, drill, or via findings were introduced; only the inherited
  54 library-footprint and 13 silkscreen findings remain.
- FAST-B VBUS, SERVICE controls, ground, thermal, remaining power zones, and
  final routed validation remain intentionally open.

# 2026-08-22 — FAST-B VBUS routing checkpoint

- Added `/USB_FAST_B_VBUS` from U8 TPS25821 pad 12 into the J10 VBUS field.
  The accepted path is approximately 54.553 mm across seven segments, with a
  short F.Cu source escape, two ordinary 0.60/0.30 mm through-vias, a B.Cu
  lower-perimeter current corridor, and a local F.Cu connector-side VBUS zone.
- The path was iterated against the existing USB 5 V feed, FAST-B CC1/CC2
  transitions, and the J10/U18 pad field. The final DRC-verified path has no
  VBUS-specific short, crossing, clearance, mask, edge, or via findings.
- Lock-free KiCad 10.0.5 DRC reports 67 total findings and 343 remaining
  unconnected items. The inherited findings are 54 library-footprint and 13
  silkscreen warnings; no new electrical/geometry findings were introduced.
- FAST-B high-speed and control routing is now complete. SERVICE controls,
  ground, thermal, remaining power zones, and final routed validation remain
  intentionally open.

# 2026-08-22 — combined high-speed review checkpoint

- Reviewed the complete routed PCIe, FAST-A, and FAST-B high-speed set before
  power routing. Current KiCad DRC reports 67 non-unconnected findings, 343
  expected unconnected items, zero shorts, zero crossings, and zero
  high-speed clearance/width violations; the remaining findings are the
  inherited 54 library-footprint and 13 silkscreen findings.
- PCIe matching remains tight: PER0 0.0003 mm, PET0 0.0214 mm, and REFCLK
  0.0430 mm pair mismatch. FAST-B remains the high-speed risk, with measured
  U9-to-J10 mismatch of 5.2090 mm TX1 and 9.5858 mm RX1 under the fixed
  placement. This is documented for final signal-integrity review rather than
  hidden.
- The PCIe corridor remains free of the new FAST-B VBUS path. Final L2 GND
  continuity, return stitching, and power-plane interaction remain mandatory
  checks before release.

# 2026-08-22 — FAST-B TX2 connector continuation checkpoint

- Closed the previously missing U11-to-J10 `/USB_FAST_B_TX2_P` and
  `/USB_FAST_B_TX2_N` legs. The measured total lengths are 46.1589 mm and
  51.5355 mm respectively, with 5.3766 mm mismatch and four ordinary
  through-vias per conductor.
- The final connector approach was iterated around the J10 VBUS/CC2 field and
  U18 pad field. Lock-free KiCad 10.0.5 DRC reports 67 inherited findings,
  341 remaining unconnected items, and zero new electrical or geometric
  findings. This closes the FAST-B SuperSpeed copper class.
- The larger FAST-B skew remains an explicit post-route signal-integrity risk;
  ground-plane and power-zone implementation must not cut through these
  corridors.

# 2026-08-22 — routed DRC and release-gate checkpoint

- Completed the first routed-board DRC cleanup without changing signal
  geometry: explicit solid GND zone connections remove the starved-thermal
  errors, and only the affected tiny-footprint reference fields are hidden to
  remove silkscreen-over-pad errors.
- Final routed DRC receipt: 0 error-severity findings, 54 understood
  local-library warnings, and 31 intentional NC/zone/ground connectivity
  records.
- Preserved a 54-footprint CPL/inventory and added post-route PCIe/USB and
  power audits. The board is not ready for a Rev-A fab package because actual
  USB3 inner-layer impedance/skew remains unqualified, despite PCIe/power
  routing being reviewable.

# 2026-08-22 — routed parity and render checkpoint

- Reran final routed DRC on the exact post-label-cleanup board: 0 error-severity findings, 54 local-library warnings, and 31 intentional connectivity records.
- Ran schematic-parity validation and preserved 321 warnings: 199 J1 full-connector abstraction records, 68 custom-footprint mismatches, 50 board metadata mismatches, and four board-only protection/test/mechanical footprints. No represented ordinary PCIe/USB/power/control net rename was found.
- Generated top, bottom, front, and isometric KiCad 3D renders and a 54-footprint CPL/inventory. Production release remains NOT_READY_FOR_REV_A_FAB_PACKAGE because USB3 layer/skew qualification and full J1 parity are not closed.

# 2026-08-22 — production-readiness gate clarification

- Added the schematic-parity result to the production gate matrix. The routed study remains NOT_READY_FOR_REV_A_FAB_PACKAGE for two concrete electrical/documentation reasons: USB3 actual-layer/skew qualification and the intentionally abstracted full 400-pad J1 not being machine-parity-clean.

# 2026-08-22 — materialize final routed PCB cleanup

- Verified the recovered working board against the committed blob and found that the DRC-cleanup board edits were not yet materialized in the prior audit commit. Committed the exact final board next so its solid GND connections, silkscreen cleanup, and routed-study labels match the preserved DRC/3D/parity receipts.

# 2026-08-22 — preserve high-speed rework baseline

- Opened `codex/high-speed-rework` from the materialized routed-board commit and preserved the complete first-pass PCB as `validation/PiSXMe-high-speed-rework-baseline.kicad_pcb` before any placement or copper rework. The baseline records the measured PCIe and USB3 routes so later improvements remain auditable.

# 2026-08-22 — high-speed rework root causes and placement decision

- Classified the PCIe 100+ mm span as primarily fixed J2/cooler-mechanical geometry plus avoidable routing detours, and classified FAST-B's 14.8766 mm mismatch as a real asymmetric connector-side topology. Disposable placement studies rejected a 5 mm inward J2 shift and a 270-degree rotation because they consume the cooler/power/service envelope. Candidate A, fixed J2 with a fresh local re-route, remains the selected surgical path; no production copper was changed in this checkpoint.

# 2026-08-22 — routed rework validation and connectivity closure

- Preserved the original routed baseline at object hash `477b50deb84c515c3be1d70322e378c970967031`; the active rework PCB now hashes `a0719fe4e924a18c174e8b4e1d17e804be33b0d6` after only the explicit no-connect net cleanup. Disposable shorter PCIe and length-matched FAST-B trials introduced real crossings/shorts and were rejected. No unsafe trial copper was copied into the active board; PCIe remains 107--122 mm with two transitions per conductor and FAST-B remains at 14.8766 mm maximum pair mismatch.
- Corrected the schematic no-connect at the actual CM5 J2 pin-104 (`PCIE_nWAKE`) endpoint and reran lock-free KiCad 10.0.5 ERC: 0 errors, 46 explained warnings (30 project-local footprint-link context warnings and 16 intentional isolated labels). Removed the shared `/NC` PCB net from ten explicitly unconnected pads, reducing routed DRC connectivity records from 31 to 22 without changing signal or power geometry.
- Reran routed DRC and schematic parity on disposable full-project copies: 0 geometric DRC errors, 54 local-library warnings, 22 remaining shield/ground-zone/VBUS connectivity records, and 321 parity warnings with no represented ordinary PCIe/USB/power/control net mismatch. A disposable shield/GND stitching trial created 42 real DRC errors and was discarded. Thermal/current review remains `PASS_WITH_DOCUMENTED_MARGIN/RISK` for monitored Rev-A bring-up only. Production readiness remains `NOT_READY_FOR_REV_A_FAB_PACKAGE`; no Gerbers were released or ordered.
- Generated fresh top, bottom, front, and isometric KiCad 10.0.5 renders from the corrected active PCB. Net-only cleanup did not change the cooler-agnostic mechanical placement: CM5, SXM2 field, USB-C edge group, power/fan access, and published cooling/backplate envelope remain visually unchanged.

# 2026-08-22 — high-speed placement redesign baseline

- Created branch `codex/high-speed-placement-redesign` from `a17cf51cb55d57190001196fbb88fd7bbb931d37` and preserved the complete first-pass routed board as `placement/PiSXMe-routed-reference.kicad_pcb`. This phase is placement-only: the SXM2/cooler/power anchors remain fixed while CM5 and USB high-speed endpoints are explored in disposable copies before any production rerouting.

# 2026-08-22 — CM5 placement candidates and lightweight route trials

- Built a disposable placement-study board and exact endpoint map, explored six CM5 orientations/translations including expanded-outline alternatives, and trialed the top three geometries. Candidate C, J2 at `(197.5,70,180°)`, produced the best compact PCIe result: approximately 63–68 mm, zero high-speed vias, and an ACCEPTABLE direct L1/L2 corridor. USB mux/ESD pin-order crossings remain intentionally deferred to the next routing phase; no production copper was created.

# 2026-08-22 — materialize corrected high-speed placement winner

- Rejected the first Candidate C USB support placement after placement DRC exposed overlaps with the rotated J2 body. Repositioned muxes, ESD, USB buck, and USB2 support into legal upper/lower-right corridors, verified the CM5 STEP envelope, and materialized only placement plus affected-net rip-up on `pisxme/PiSXMe.kicad_pcb`. The corrected placement DRC has 57 findings/499 expected unconnected records, zero new courtyard overlaps, zero pad shorts, and zero new hole-clearance blockers. Production routing remains intentionally absent.

# 2026-08-22 — placement receipt wording correction

- Clarified that the three non-library placement-study records in the final receipt are silk records, not track violations. No board geometry or placement was changed.

# 2026-08-22 — PCIe pass-2 production route checkpoint

- Preserved Candidate C placement and routed only the PCIe x1 interface plus
  the two V100 TX AC-coupling legs. PER0 is 74.3581/74.3895 mm with 0.0314 mm
  skew and zero vias; PET0 is 54.0182/53.9915 mm with 0.0266 mm skew and two
  vias per conductor; REFCLK is 80.1659/80.1738 mm with 0.0079 mm skew and two
  vias per conductor. The eight transitions are limited to the fixed endpoint
  order crossovers.
- KiCad 10.0.5 lock-free project-copy DRC reports no PCIe-named violation,
  clearance error, crossing/short, keepout, or new via/hole error. The board
  remains intentionally unrouted for USB, power, low-speed nets, and final
  zone refill. PCIe is classified ACCEPTABLE_FOR_REV_A because PER0 and
  REFCLK remain above the preferred 70 mm GOOD band despite clean geometry and
  sub-0.032 mm pair skew.

# 2026-08-22 — USB3 fanout placement redesign

- Opened `codex/usb3-fanout-placement` from the frozen USB3-pass checkpoint and
  preserved the active PCIe-pass PCB as
  `placement/usb3-fanout/PiSXMe-usb3-fanout-baseline.kicad_pcb`. Reconstructed
  the CM5, HD3SS3212, TPD4EUSB30, and USB-C physical pin ordering and tested
  four-orientation local candidates for each FAST port.
- Selected FAST-A U5 `(202.5,78,180°)` with U6/U7 `(205,66,180°)` /
  `(214,66,180°)` and J9 `(210.5,58)`. Selected FAST-B U9
  `(202.5,106,0°)` with U10/U11 `(200.5,122,180°)` /
  `(214,122,180°)` and J10 unchanged. The selected direct centerline trials
  reduced high-speed-specific shorting findings to 6 for FAST-A and 1 for
  FAST-B; they are feasibility evidence, not production routes.
- Materialized placement only on `pisxme/PiSXMe.kicad_pcb`. Segment/via
  extraction is byte-identical to baseline (149 segments, 28 vias), proving
  PCIe was untouched. KiCad 10.0.5 placement DRC has zero courtyard, pad,
  hole, keepout, or USB/PCIe copper blockers; 60 total findings are 54
  library-context warnings and six cosmetic silk findings. Production USB3
  routing remains intentionally deferred to the next phase.

# 2026-08-22 — USB3 pass-3 fanout routing blocker

- Opened `codex/usb3-pass3` from `53364864f98bb05733c0882efa0bbfe8d7438aca`
  and preserved the active Candidate-C placement plus frozen PCIe routing.
- Attempted FAST-A SuperSpeed routing only in a disposable copy. The explicit
  mux-to-shunt-ESD-to-Type-C trial exposed one TX1 P/N short, five track
  crossings, and one additional 0.20 mm clearance error beyond the 60-finding
  baseline. The failure is at the eight-conductor 0.5 mm-pitch U5 escape, not
  in PCIe or in the ESD logical topology.
- FAST-B was not attempted because U9 has the same constrained source fanout.
  No USB3 production copper was added to `pisxme/PiSXMe.kicad_pcb`; it remains
  at 149 segments and 28 vias, and the frozen PCIe hash remains
  `94d5ec937de700caf337f0d653a692dbcb0fe9c04a3eaccecec62fe6761f0b`.
- Preserved baseline DRC at `validation/DRC_USB3_PASS3_BASELINE.json` and the
  negative trial at `routing/usb3-pass3/trials/FAST_A_FANOUT_BLOCKED_TRIAL.kicad_pcb`.
  USB3 production routing is blocked until local fanout placement, controlled
  layer policy, or manufacturing/via policy is deliberately reopened.

# 2026-08-23 — HD3SS3212 polarity-remap reference study

- Preserved TI TIDA-00987 design material, the official CM5IO source/PDF, the
  MIT-licensed ModuCard carrier, and the prototype cm5MiniITX source under the
  reference tree. TI's exact lesson is that deliberate differential polarity
  remapping, including the corresponding A-side relationship, is a valid way
  to keep the HD3SS3212/ESD/Type-C fanout straight; the HD3SS3212 data sheet
  requires the polarity relationship to remain consistent from Port A to the
  selected B/C paths.
- Derived a PiSXMe trial map that keeps TX normal and inverts RX consistently
  across A/B/C, rotates U9 to 180 degrees for FAST-B, and assigns the ESD
  shunt pads physically as TX_P, TX_N, RX_N, RX_P. Disposable FAST-A and
  FAST-B copies show improved pair ordering, but their naive centerline
  fanouts still have inter-branch DRC errors (109 total/55 errors for A;
  137 total/83 errors for B). The active schematic, active PCB, and frozen
  PCIe copper remain unchanged; USB3 production readiness stays
  `NOT_READY_FOR_USB3_PRODUCTION_ROUTING` pending a proper constrained fanout
  or controlled second-layer comparison.

# 2026-08-23 — reference-derived USB3 fanout coupon closure

- Acquired and preserved TI’s current public HD3SS3212 layout/checklist/S-parameter materials, official CM5IO evidence, MIT-licensed ModuCard at upstream commit `2d96d2e238e6e020c98220d49595c7a6028a35cf`, and cm5MiniITX at `479fee1dd5831eab652e72c031d0c806a2091c44`. Quantitatively measured the open KiCad boards and annotated TI’s published layout figures without importing their geometry.
- Confirmed the external consensus: use HD3SS3212-supported polarity remapping, route through the flow-through ESD package, use a short local escape, and return to controlled geometry; zero or a small number of symmetric USB3 transitions is normal, while dozens of vias are not required. TI’s exact local width/gap/clearance remain unknown because the public Gerber endpoint is login-gated.
- Built separate disposable PiSXMe-method and TI-method coupons using the selected mux/ESD/Type-C pad coordinates for one representative TX pair. Both have zero DRC errors, zero unconnected items, zero vias, and four documented library-context warnings. The staged proof uses 0.100 mm local width for the bounded escape and 0.13208 mm main geometry; it is not a full-port signoff.
- Ran reference-derived full FAST-A/B trials on disposable copies with the polarity map and bounded local escape. FAST-A retains 148 USB-related DRC records; FAST-B retains 151, including real crossings, shorts, and clearance/mask conflicts. The active board remains production-unrouted for USB3, and the active PCIe records are byte-equivalent to the frozen 244afbe baseline (71 records; hash `954915...cfeb`). Final phase decision remains `NOT_READY_FOR_USB3_PRODUCTION_ROUTING`; the exact remaining blocker is the unresolved four-channel mux/ESD/Type-C fanout, not generic USB3 uncertainty.

# 2026-08-23 — attached TI TIDCCK4 source and corrected USB3 package coupon

- Preserved the user-supplied TI TIDA-00987 source archive at
  `references/usb3/TIDA-00987/TIDCCK4-attached-source-archive.zip` with SHA256
  `e5a4f836967bd1e92fdee2e40ea187f6aca150094213933a75da1573142a2357` and
  extracted its Altium project under the immutable reference tree. Imported
  `TIDA-00987E1.PcbDoc` successfully into a disposable KiCad 10.0.5 board;
  no active PiSXMe source was replaced.
- Measured the TI source's inspected SuperSpeed region: four copper layers,
  1.58464 mm board thickness, 0.2286 mm trace width, approximately 0.1905 mm
  minimum local F.Cu edge gap, 133 F.Cu segments, 16 B.Cu segments, and two
  symmetric layer-transition vias on each of two source paths.
- Found the active PiSXMe HD3SS3212 and DQA ESD footprints are physically
  wrong for their selected MPNs: the active mux is a two-row 5 mm model rather
  than the RKS0020A perimeter pattern, and the active DQA model is a
  horizontal two-row pattern rather than the two-side package. Added
  analysis-only corrected footprints, package comparison artifacts, and a
  corrected four-pair coupon; the active schematic/PCB and frozen PCIe remain
  byte-identical to the branch base.
- The corrected coupon uses explicit TI-style polarity remapping, flow-through
  ESD pads, a short local jog around the ESD ground pad, no vias, and
  PiSXMe's 0.13208 mm main-route width. Under its explicit bounded local DRC
  rule KiCad reports zero violations and zero unconnected items; the default
  0.20 mm rule reports eight local clearance errors and no opens/shorts. USB3
  production readiness remains `NOT_READY_FOR_USB3_PRODUCTION_ROUTING` until
  a full two-port trial uses the corrected footprints and closes schematic/PCB
  parity.

# 2026-08-23 — high-speed via-policy amendment

- Established `design/HIGH_SPEED_VIA_POLICY.md` as authoritative for all
  remaining PiSXMe PCIe and USB3 work. Via count is a cost term, not a hard
  objective: prioritize correct connectivity/polarity, intentional reference
  planes, no crossings/pathological fanout, direct paths, pair symmetry,
  impedance continuity, then minimal transitions and vias.
- A clean zero-via route remains excellent, but a deliberate symmetric
  transition per conductor is equally acceptable when it produces the better
  electromagnetic path. Repeated layer bouncing, unexplained transitions,
  and HDI/microvias used only to reduce a reasonable through-via count remain
  unacceptable.
- USB3 fanout work must now explicitly permit the topology
  `fine-pitch escape -> symmetric referenced transition -> controlled route`
  when that is cleaner than forced F.Cu routing. Future receipts must report
  vias per conductor, total port vias, the reason for each transition, layers
  and reference planes before/after, return-path stitching, stub treatment,
  and whether removing the transition improves or worsens the path.
- The existing PCIe copper remains frozen and unchanged by this amendment.

# 2026-08-23 — corrected-footprint full-port parity trials

- Opened `codex/full-port-corrected-footprint-trials` from the preserved
  `90f0ab0d980a9a332e91967cb0f2d1a02441d39f` state. Verified the disposable
  TI-derived HD3SS3212 RKS0020A footprint (20 perimeter signal pads plus
  thermal pad) and DQA side-row ESD footprint for trial use. The active
  `PiSXMe.kicad_pcb` and `PiSXMe.kicad_sch` hashes remained
  `21a4a6a877b212f1d55a3456a47e93c14b2ca3ad` and
  `8437c0241976153a724c8935be8b16b650cc8edf` before and after.
- Built complete disposable FAST-A and FAST-B corrected-package trials using
  the exact CM5 USB3 launch coordinates, legal polarity remapping, bounded
  0.100 mm local escape, and flow-through DQA assignments. FAST-A DRC found
  54 violations (17 crossings, 8 shorts, 23 mask bridges); FAST-B found 84
  (28 crossings, 10 shorts, 38 mask bridges). These are real fanout failures,
  not warnings that can be waived; the one-pair corrected coupon passing does
  not prove the complete reversible Type-C topology.
- Added a disposable symmetric F.Cu-to-B.Cu layer-transition coupon. It has
  zero error-severity geometry findings and zero unconnected pads, with only
  twelve silkscreen warnings. This proves a controlled transition can solve a
  local crossing in principle, but it is not a full-port or JLC stackup SI
  signoff.
- Final decision remains `NOT_READY_TO_REPLACE_ACTIVE_USB3_FOOTPRINTS`. The
  exact remaining blocker is the unproven complete RKS-to-two-DQA-to-reversible
  Type-C fanout at the fixed placement. No active USB3 footprint, schematic,
  production USB3 copper, or frozen PCIe copper was changed.

# 2026-08-23 — mux relocation full-port proof

- Built final disposable complete FAST-A and FAST-B reversible Type-C trials
  using the corrected TI-derived HD3SS3212 RKS0020A and DQA footprints,
  legal polarity remapping, bounded 0.100 mm local escape, and deliberate
  signal-layer transitions where the topology required them.
- Selected the relocation winners FAST-A A9 at `(187.5, 82)` and FAST-B B8 at
  `(187.5, 120)`; ESD devices remain adjacent to their receptacles.
- All four final relocation boards have zero copper shorts, pair crossings,
  clearance violations, and pad-overlap violations. Remaining findings are
  three silkscreen-over-copper warnings plus one library-context warning per
  disposable board, and expected connectivity records from stripped trial
  support circuitry.
- Result is `MUX_RELOCATION_SOLVES_USB3`; the controlled-via fallback branch
  was not entered. This is a fanout-placement proof, not production USB3
  routing approval: the next phase must materialize corrected footprints,
  calculate non-L1 geometry/reference planes, add ground-return stitching,
  and rerun DRC/SI on the active board.
- Active PCB and schematic remain unchanged; frozen PCIe remains untouched.

# 2026-08-23 — USB3 production routing pass opened

- Opened `codex/usb3-production-routing` from the successful relocation proof
  checkpoint `505914ccf2bd76756a836487266b5badfdd703ae`. Captured the active
  220 × 140 mm board baseline, corrected-footprint migration targets, and a
  machine-checkable PCIe route fingerprint before changing the active PCB.
- The USB3 pass is explicitly scoped to corrected HD3SS3212/DQA footprints,
  winning mux/ESD placement, FAST-A/B SuperSpeed, and their USB2 companions.
  V100 power, regulators, SERVICE, low-speed routing, final zones, global
  stitching, and PCIe remain frozen/out of scope.

# 2026-08-23 — USB3 production SuperSpeed materialization checkpoint

- Materialized the verified TI-derived RKS0020A/DQA footprints and the proven
  relocated FAST-A/B mux/ESD placement onto the active PCB. U7 was retained at
  `(204.5,68)` for the real J2 center-hole constraint; U11 was retained at the
  validated `(201,136)` proof coordinate because `(214,136)` creates actual
  J10 fanout crossings.
- Production SuperSpeed copper now uses F.Cu/B.Cu only, corrected bounded
  local escape areas, matched ordinary through-via transitions, and eight
  deliberate /GND return vias. No USB3-specific short, crossing, clearance,
  pad-overlap, or pair-rule error remains in the lock-free CLI receipt.
- The frozen PCIe route geometry remains identical to the pre-USB3 baseline;
  the schematic is unchanged. B.Cu/In4 power-plane continuity and aggregate
  branch skew remain explicit next-phase SI/power-zone review items. USB2
  FAST-port companions were completed after this checkpoint; VBUS, regulators,
  SERVICE, remaining low-speed routing, and final zones remain intentionally
  incomplete.

# 2026-08-23 — USB3 production routing accepted

- Completed the production FAST-A and FAST-B USB2 companion nets after the
  SuperSpeed freeze. All four reversible Type-C D+/D− nets are connected with
  no USB2-specific shorts, crossings, clearance, pad, solder-mask, hole, or
  unconnected finding in the lock-free KiCad 10.0.5 DRC copy.
- The active checkpoint contains 333 segments, 128 vias, six planned copper
  zones, and 28 non-keepout fine-escape rule areas. The USB2 branches use
  three ordinary through-vias per net and In2/In3 stems; they are documented as
  lower-speed companion connectivity, not SuperSpeed impedance evidence.
- PCIe `/PER0`, `/PET0`, and `/REFCLK` normalized segment/via geometry is
  byte-identical to the frozen baseline. The schematic is unchanged.
- Final USB3-scope decision is `USB3_PRODUCTION_ROUTING_ACCEPTED`. This does
  not release the board for fabrication: V100/CM5/USB power, SERVICE, fans,
  final plane refill, thermal review, and remaining low-speed work are next.
## 2026-08-23 — functional integration-routing pass opened

- Forked `codex/integration-functional-routing` from the accepted USB3/PCIe checkpoint `80cedb1f43e7d8af81c1919177bc25af53e11d70`.
- Captured live-board SHA-256, KiCad 10.0.5 lock-free DRC/ERC receipts, and a machine-readable open-net inventory before changing copper.
- The board remains pre-final-zone: accepted PCIe and USB3 are protected; remaining classes are power, service, recovery, control, cooling, debug, and low-speed routing.

## 2026-08-23 — V100 protected 12 V integration checkpoint

- Rebuilt the accepted PCIe/USB3 baseline before adding power and replaced the
  failed numeric-net experiment with name-bearing `/RAW_A_12V`, `/RAW_B_12V`,
  `/FUSED_A_12V`, `/FUSED_B_12V`, and `/VPROT_12V` copper.
- Added the dual-fuse/protection paths, broad protected V100 bus, 13
  distributed SXM2 power-field transitions, and independent CM5/USB buck
  input feeds: 77 segments and 39 vias.
- The USB-buck feed was intentionally moved onto In2.Cu so the accepted B.Cu
  USB3 routes remain untouched. Lock-free KiCad 10.0.5 DRC found no new power
  short, crossing, or clearance issue; only the pre-existing PET0/J2
  clearance and inherited library/silkscreen findings remain.
- The short 0.25 mm TPSM63606 pad escapes are not bulk-current bottlenecks,
  but remain explicitly deferred to final-zone/thermal review.

## 2026-08-23 — CM5 5 V integration checkpoint

- Corrected the previous study-coordinate error by routing the six actual J2
  `/CM5_5V` contacts (pads 77/79/81/83/85/87) in the active 180-degree CM5
  placement. The route adds 27 segments and two through-vias.
- The contact field escapes on F.Cu, then the main trunk uses In2.Cu so it
  avoids the frozen USB3 B.Cu fanout and the U17 ground island. Lock-free DRC
  reports no CM5 5 V short, crossing, clearance, or open-net record.

## 2026-08-23 — USB peripheral 5 V source-routing checkpoint

- Replaced the stale USB-rail study geometry with current U16/U4/U8
  coordinates and name-bearing `/USB_5V_PERIPH` copper: 19 segments and three
  through-vias.
- The dedicated rail uses F.Cu pad escapes and an In2.Cu distribution trunk;
  the long FAST-A rise uses the far-right corridor to avoid all accepted
  USB3 through-via fields and the CM5 5 V route. FAST-A and FAST-B input
  islands are connected with no new USB 5 V error.
- U13 SERVICE input remains intentionally grouped with the next SERVICE
  VBUS/role-routing checkpoint. Final regulator thermal and plane review are
  deferred to the final-zone phase.

## 2026-08-23 — functional integration routing checkpoint

- Completed the ordinary functional routing pass without changing frozen
  PCIe or accepted USB3 geometry. The active board now contains the dual
  protected 12-V distribution, CM5 5-V, USB peripheral 5-V, SERVICE USB2
  data/CC/role/recovery paths, UART, reset/CLKREQ/power controls, mux
  controls, fan tach/PWM, and cooling-header routes.
- Current structural state is 680 segments, 260 vias, 40 zone/rule-area
  records, 54 footprints, and a 220 x 140 mm outline. The current PCB hash is
  `419c1f28b689ff03c69bb672f23e6fff189384e50f86db6659c6554ad686671e`.
- PCIe plus USB3 normalized geometry remains identical to the accepted
  `80cedb1` fingerprint. No high-speed route was used as a shortcut for the
  integration copper.
- Lock-free KiCad 10.0.5 validation reports 0 ERC errors and 46 inherited /
  explained warnings. DRC has no new electrical short, clearance, keepout,
  USB2, USB3, or differential-pair issue; 348 open records are preserved in
  the final machine-readable inventory for final GND/VBUS/chassis/protected
  12-V zones and inherited accepted endpoint records.
- Final zone/pour, B.Cu USB3 reference preservation, thermal-via/current
  qualification, and release-package validation remain explicitly deferred.
## 2026-08-25 — final zones/release review baseline

- Started `codex/final-zones-release-review` from `613901a`.
- Captured the pre-zone board at `release/final-pass/PiSXMe-before-final-zones.kicad_pcb`.
- Baseline PCB SHA-256: `419c1f28b689ff03c69bb672f23e6fff189384e50f86db6659c6554ad686671e`.
- Frozen PCIe/accepted USB3 fingerprints remain governed by
  `validation/integration-pass/HIGH_SPEED_PRESERVATION.json`.
- Final zones, thermal vias, release outputs, and external-review artifacts are
  not yet implemented; no order or external submission is authorized.

## 2026-08-25 — final-plane implementation checkpoint

- Materialized the final-plane candidate on `codex/final-zones-release-review`:
  full GND reference planes on F.Cu/In1/In4, bounded protected-12-V In3
  manifolds, bounded CM5 5-V and USB 5-V In2 regions, and local VBUS source
  closures. Frozen PCIe and accepted USB3 geometry remained unchanged.
- The candidate has no new real short, clearance, crossing, plane-isolation,
  mask-bridge, thermal, hole, or drill DRC defect. ERC remains 0 errors with
  46 categorized library/intentional warnings.
- `/3V3` closure was tested with ordinary through-via In2 and In3 alternatives;
  both produced real conflicts against frozen USB3/control/power geometry.
  The 9 mandatory control-power opens remain a release blocker. No HDI,
  via-in-pad, or frozen high-speed reroute was introduced silently.
- USB-C `CHASSIS_GND` shell chaining was also tested and rejected after real
  conflicts. The 5 shell relationships remain an explicit chassis/shield
  blocker rather than being waived as ground.
- Final thermal/current records classify V100 distribution as
  `PASS_WITH_REV_A_MARGIN/RISK`; regulator/protection results are analytical
  only and require hardware measurement. Manufacturing outputs and external
  review packet are held. No order, upload, or publication is authorized.
## 2026-08-26 — blocker-closure via census and shell/3V3 trials

- Branched as `codex/blocker-closure-via-audit` from the final-plane state at
  `46458a1`.
- Enumerated all 260 vias from the final-plane baseline. Every via has a
  classified signal, return, connector-breakout, or current-spreading role;
  no redundant/orphan via was proven removable.
- Tested a bounded F.Cu `/3V3` distribution region. The least-invasive
  successful closure is a short U5 local escape plus two ordinary 0.40/0.30
  mm through-vias; the local rule remains bounded and is not a global
  clearance change.
- Tested USB-C shield closure. The direct S1/S2-to-`/GND` strategy closes all
  shell relationships without a new real DRC class and follows a working
  open CM5-carrier precedent. Long F.Cu/In2 shell trunks were rejected after
  measured crossings/shorts/clearance failures.
- PCIe and accepted USB3 geometry remain protected. The active promotion and
  combined DRC/ERC rerun are the next gates; no release package is claimed
  until those receipts pass.
## 2026-08-26 — blocker-closure promoted and release-package gate opened

- Promoted the bounded low-current `/3V3` closure: a 0.100 mm local U5
  escape, two matched 0.40/0.30 mm ordinary through-vias, and the bounded
  F.Cu distribution region. The final active DRC has zero `/3V3` endpoint
  records.
- Promoted the direct USB-C shell-to-`/GND` strategy in both schematic and
  PCB. The final active DRC has zero `CHASSIS_GND` endpoint records. A future
  metal enclosure may need a system-level EMI review; that is not an open PCB
  net in this Rev-A candidate.
- Rationalized the final-plane via set from 260 to 241: removed 16 exact
  co-located high-current duplicates and six isolated/dangling stale vias,
  retained two required `/3V3` vias, and added one required `/PERST_N` via.
  The final census has zero unknown classifications.
- Final lock-free KiCad 10.0.5 validation reports 0 ERC errors and 46
  categorized warnings. DRC reports no real copper, clearance, keepout,
  crossing, hole, drill, or differential-pair defect; the remaining records
  are documented library-context, cosmetic silkscreen, zone-self, and
  inherited USB3 endpoint abstractions.
- Active hashes and the exact connected high-speed preservation comparison are
  recorded under `release/blocker-closure/`. Internal manufacturing/review
  package generation is now permitted for inspection only; no order, upload,
  or public release is authorized.
## 2026-08-26 — release bookkeeping parity checkpoint

- Re-ran lock-free KiCad 10.0.5 ERC/DRC after making the accepted CLKREQ#
  strap explicit: R1 is populated as Yageo `RC0603FR-070RL`. TP3 is identified
  as Keystone Electronics `5000`; TP1/TP2 remain PCB-only no-net markers.
- The current final DRC receipt explicitly separates 57 `violations` from 82
  `unconnected_items` (91 raw error-severity records total). It does not call
  the 66 GND/VBUS zone-context records a clean DRC; they remain visible plane
  review items. The 16 inherited USB3 endpoint-island records remain the
  accepted abstraction category.
- Corrected stale release identity/parity records to bind the active PCB,
  schematic, and design-rule hashes to the promoted closure state. D1 remains
  an intentionally un-netted PCB-only TVS placeholder and is visible as a
  pre-fabrication review item rather than being silently included in the BOM.

## 2026-08-26 — internal external-review packet generated

- Regenerated the internal schematic PDF, six copper-layer SVG plots, Gerbers,
  Excellon drill files/maps, BOM/CPL, and four 3D views from the active
  blocker-closure board. Source identity is bound by the active PCB,
  schematic, and design-rule SHA-256 records.
- Added the final hostile via and chassis/ESD reviews. The 241-via population
  is rationally explained with zero unknowns; shell-to-digital-ground is
  closed for Rev-A while enclosure EMI remains a stated risk.
- Prepared `external-review/PiSXMe-RevA-RC1/` as an internal peer-review
  packet. D1 remains a visible fabrication gate, raw DRC zone-context and
  inherited endpoint records remain visible, and no order/upload/publication
  is authorized.

## 2026-08-26 — RC1 archive integrity checkpoint

- Created `manufacturing/release/PiSXMe-RevA-RC1.zip` from the review packet;
  ZIP integrity passed with 117 files and the SHA-256 recorded in
  `manufacturing/release/RC1_ARCHIVE_RECEIPT.md`.
- The external-review decision is intentionally scoped to peer review only.
  The packet is not a fabrication release: D1's un-netted placeholder,
  visible plane-context records, thermal measurement gaps, and enclosure EMI
  behavior remain explicit review/fabrication-gate items.

## 2026-08-26 — review packet high-speed record correction

- Marked the older route-study metrics as historical and replaced the packet's
  current high-speed preservation copy with the blocker-closure receipt. This
  prevents pre-closure route counts and pending B.Cu wording from being read
  as the active board state.
- Rebuilt `PiSXMe-RevA-RC1.zip` after that documentation correction and
  retained the previous archive as a recoverable `-v1` copy.
## 2026-08-26 — external-review visual closure

- Added six KiCad 10.0.5 source-board close-ups covering PCIe, FAST-A,
  FAST-B, USB-C/chassis, the bounded `/3V3` closure, and the regulator area.
  Their exact render pivots and SHA-256 values are recorded in the
  reproducibility receipt and checksum manifest; the layer-resolved SVGs
  remain the copper-inspection authority.
- Rebuilt the internal peer-review archive with the close-ups and an explicit
  index. ZIP integrity passed with 123 files and 12,480,785 uncompressed
  bytes; the prior close-up-free archive is retained as `-v2` and the first
  archive remains retained as `-v1`.
- The active board, schematic, design rules, and frozen connected PCIe/USB3
  geometry were not changed by this visual/package step. External review is
  authorized only as an internal packet; fabrication ordering, upload, and
  public release remain prohibited.
## 2026-08-26 — final evidence consistency correction

- Clarified that the older 260-via functional breakdown is a retained
  pre-cleanup baseline, while `VIA_CENSUS_FINAL.md` is authoritative for the
  active 241-via board. This removes an otherwise confusing sum mismatch in
  the via assessment without changing PCB copper or any design hash.
## 2026-08-27 — architecture sanity audit baseline

- Opened `codex/architecture-sanity-audit` from `88b8688` and recorded
  immutable SHA-256 guards for the active PiSXMe PCB, schematic, and design
  rules. This audit does not modify those files.
- Preserved the current Raspberry Pi CM5 IO Board revision-2 KiCad package
  under `references/cm5/official-cm5io-rev2/` with source and board hashes.
- Added a read-only reference-via census tool and generated machine-readable
  counts for PiSXMe, TI TIDA-00987, official CM5IO, ModuCard, and cm5MiniITX.

## 2026-08-27 — USB-A simplification audit closure

- Preserved the active PiSXMe PCB, schematic, and design rules byte-for-byte
  while completing the architecture minimality and via audit.
- Added quantitative via audits for the preserved TI source proxy, official
  CM5IO Rev 2, ModuCard, cm5MiniITX, and the active 241-via board.
- Built a disposable direct USB-A SuperSpeed variant. Both independent ports
  route cleanly with 0 signal vias, 0 unconnected items, 0 DRC violations,
  and 0.109838 mm maximum trial pair skew; the trial intentionally omits
  final VBUS/ESD/USB2 implementation and is not a fabrication design.
- The audit found no second-SXM2, NVLink, x16, unused-lane, Ethernet, HDMI,
  MIPI, microSD, or hub baggage. It recommends `SWITCH_FAST_PORTS_TO_USB_A`
  for a future revision because fixed Type-A preserves the two native 5 Gbps
  CM5 links while removing the current Type-C mux/branch complexity.
- D1 remains a documented pre-fabrication provenance gate; it was not altered
  in this read-only audit.

## 2026-08-27 — conductor-level via census completion

- Expanded the active-board USB3 via audit from grouped families to the
  individual CM5-side and FAST-port net paths, including endpoints, via
  counts, and inferred F.Cu/B.Cu layer sequences.
- Confirmed the direct USB-A trial remains a disposable SuperSpeed-only
  proof: no active PCB/schematic/rules file changed.

## 2026-08-27 — active USB-A migration baseline

- Opened `codex/usb-a-active-migration` from the architecture-sanity audit
  closure and preserved the active USB-C PiSXMe PCB and schematic under
  `migration/usb-a/pre-migration/` with matching SHA-256 values.
- Recorded the 54-footprint, 241-via, 220 x 140 mm baseline and the frozen
  PCIe fingerprints before authorizing active FAST-A/FAST-B simplification.
- The migration will replace only the unnecessary reversible USB-C FAST
  architecture; SERVICE USB-C, V100/SXM2, and PCIe remain protected.

## 2026-08-27 — USB-A schematic migration checkpoint

- Replayed the direct FAST-A/FAST-B Type-A schematic migration from the
  preserved USB-C source after correcting the cleanup boundary so the U16
  USB 5 V buck support network remains intact.
- Added the project `USB_A_FAST` symbol and removed unused embedded FAST
  Type-C and HD3SS3212 definitions from the active schematic.
- Schematic ERC now reports 0 errors, 0 multiple-net-name findings, and 44
  warnings limited to documented CLI footprint-link, isolated-label, and
  intentional-NC categories. No warning requires a design change.

## 2026-08-27 — USB-A active footprint and placement checkpoint

- Materialized the direct fixed-orientation USB-A FAST-A/FAST-B placement on
  the active PCB from the preserved USB-C baseline.
- Replaced J9/J10 with Würth 692122030100 Type-A receptacles, removed U5/U9
  HD3SS3212 and U7/U11 duplicate high-speed ESD footprints, retained U4/U8
  TPS2553 current limiting and U6/U10 corrected flow-through ESD.
- Reconciled the schematic footprint links for U6/U10 to
  `TPD4E05U06_DQA_TI_FLOWTHROUGH` and retained the corrected Type-A port
  symbol/net mapping.
- Placement-only DRC evidence has zero shorts, courtyard overlaps, and
  hole-clearance violations; stale/incomplete zones and missing functional
  connections remain intentionally deferred to direct USB-A routing.

## 2026-08-27 — USB-A functional routing checkpoint

- Materialized direct USB 3 Type-A SuperSpeed routing for FAST-A and FAST-B
  from the CM5 through the retained per-port ESD devices to the fixed host
  receptacles, preserving the frozen PCIe geometry and SERVICE USB-C block.
- Completed the FAST-A/FAST-B USB2 companion paths on bounded inner-layer
  corridors with short pad escapes; no USB-A functional route was left to
  inherit the deleted reversible Type-C fanout.
- Moved the FAST-B ILIM resistor away from the CM5 connector NPTH as part of
  the local migration cleanup. Full-board zone closure, D1 disposition, and
  remaining integration controls are still separate closure work.

## 2026-08-27 — USB-A integration routing checkpoint

- Closed the active direct USB-A functional integration routes without touching
  frozen PCIe or retained SERVICE architecture.
- Rebuilt CM5 5 V, FAST-A/FAST-B VBUS, SERVICE VBUS, UART, CLKREQ, fan, and
  control handoffs with explicit layer choices around the fixed high-speed
  copper.
- Native filled-board DRC on the isolated copy reports zero true geometric
  routing defects; remaining records are inherited library/silkscreen,
  zone-connectivity, and intentional same-net flow-through ESD abstractions.

## 2026-08-27 — USB-A RC2 closure and external-review package

- Completed the active FAST-A/FAST-B migration from reversible USB-C to direct
  Würth 692122030100 USB3 Type-A host ports, retaining per-port ESD and
  current-limited VBUS while leaving SERVICE USB-C and PCIe protected.
- Reconciled J9/J10 schematic indentation so the internal BOM contains all 46
  populated schematic instances; CPL contains 49 board rows with MECH1/TP1/TP2
  explicitly documented as DNP board-only markers.
- Fresh native-refill DRC reports zero genuine geometric violations; ERC has
  zero errors and only documented project-library/intentional-label/NC
  warnings. The remaining USB3 route-length/skew margin is disclosed as an
  external-review risk rather than hidden.
- Generated the non-public `PiSXMe-RevA-RC2` source, Gerber, drill, BOM/CPL,
  evidence, render, and review packet without ordering or publishing it.

## 2026-08-28 — human-factors audit of USB-A RC2

- Inspected the active RC2 board as a physical object with the manufacturer
  STEP model for the Würth 692122030100 USB3 Type-A receptacle. The active
  `0°` J9/J10 orientation is outward-facing at the right edge; the rotated
  negative-control trial was rejected because this mixed SMT/PTH footprint
  overlaps its own pad fields when rotated.
- Identified two concrete physical blockers that were not electrical DRC
  findings: F1/Q1 enter the contractual cooler-owned XY reservation, and the
  10 mm-wide J5/J6/J7 outlines overlap at 8 mm center pitch. Functional
  F.SilkS access labels and mating-housing/plug envelopes also remain
  incomplete.
- Preserved active PCB, schematic, project, and rules hashes exactly; no PCIe,
  USB, power, schematic, or RC2 release files were modified. The human-factors
  decision remains `HUMAN_FACTORS_NOT_ACCEPTABLE` pending a dedicated
  power/protection placement correction, cooling-header spacing correction,
  label pass, and final mating-envelope evidence.

## 2026-08-28 — approved Rev-A redesign execution baseline

- Approved implementation authority is `Approved Plans/PiSXMe_RevA_Verified_Redesign_Work_Package.md`.
- Execution is staged M1 through M10 with a validation gate and checkpoint
  commit at every milestone; the settled CM5-to-V100 PCIe Gen2 x1 basis is
  preserved unless contradictory evidence appears.
- Initial source baseline is the active `codex/usb-a-active-migration`
  checkout. No design source or release artifact was changed before this
  checkpoint.
2026-08-28 — M1 schematic/library truth checkpoint

- Applied the approved M1-only source truth corrections: TPS2553 physical pin numbering, fixed UFP retirement markers for U12/U13/U14, true three-pin TPD2EUSB30A DRT instances for U15/U17/U18, corrected Q1/Q2 and U4/U8/U16 PCB pad-net maps, and explicit U16 support components (input/output capacitance, VLDOIN, feedback, RT, and PG pull-up) in schematic and PCB.
- Existing copper/routing was intentionally not changed. KiCad netlist export succeeds and ERC reports zero errors (warnings remain from the pre-existing project-local library configuration and intentional isolated labels). DRC/parity remains non-gating at this checkpoint because the inherited architectural PCB contains unresolved source/board abstractions and the newly added local support parts are not yet routed; M2–M9 own those closures.

2026-08-28 — M2 floorplan checkpoint

- Applied only the approved mechanical origins for F1/Q1/F2/Q2, J5/J6/J7, and U16. The cooler intrusion and 8 mm fan-header pitch are removed at the placement level; all copper affected by these moves remains intentionally pending the bounded power/interface reroute milestones.

2026-08-28 — M3 power-support checkpoint

- Materialized the unambiguous TPS2553 input bypass and FAST-A/B port-bulk capacitor positions. The cold-plug policy remains explicit; TVS stand-off/clamp and protected-bus bulk selection stay an external-review gate until the source maximum and package/thermal choices are fixed.

2026-08-28 — M4 layer-policy checkpoint

- Removed only prohibited routed segments from In1/In4 and non-power segments from In2/In3, leaving replacement routing to M5/M6. This makes the intended ground/reference-layer policy explicit without inventing unreviewed copper.

2026-08-28 — M5 high-speed gate blocked

- Stopped before PCIe/USB rerouting because the post-M4 source has 499 unconnected items and 322 schematic-parity records, including geometry that requires an interactive, pair/skew-aware route review. Netlist export succeeds and ERC has zero errors, but the high-speed topology is not safe to synthesize automatically. M6 and later milestones are gated on a reviewed KiCad reroute and a subsequent DRC/parity pass.

2026-08-28 — M5 native-board-stream integrity recheck

- Found and repaired 114 stray closing parentheses introduced by the M4 text rip-up. The repair preserved all non-parenthesis PCB bytes and restored a balanced KiCad board stream; KiCad statistics now parse 150 through-vias instead of the 7 vias visible before repair. Native DRC consequently exposes 855 violations and 118 unconnected items, including clearance, mask-bridge, isolated-copper, crossing/shorting, dangling-via, and dangling-track classes. This supersedes the earlier under-parsed M5 counts and blocks M6 until the layer-policy board is rebuilt and high-speed topology is re-established as native KiCad connectivity.

2026-08-28 — M5 reproducible DRC baseline

- Fresh KiCad 10.0.5 DRC on clean HEAD `ee7002d` (PCB SHA-256 `7ad9dddc47bd2e786e82cea02dc52bf8ad34a6aaf0370dc9a81a4e6d842d7c64`) reports 856 violations and 118 unconnected items. The one-count difference from the first post-repair receipt is recorded as a reproducibility correction; the gate remains failed.
- The same fresh run with `--schematic-parity` reports 348 parity records. This is the current parity baseline; it is not evidence of a clean PCB/schematic contract.

2026-08-28 — independent M5 gate audit

- Independent read-only review confirms the M5 verdict is FAIL: the repaired board parses, but native DRC reports 856 violations, 118 unconnected items, and 348 schematic-parity records. It also confirms a separate U16 package-parity defect: schematic C12/C13 are 1210 and C14/R8–R11 are 0603, while the PCB uses `PiSXMe:M1_1206` for all seven parts. M6 remains gated until a valid M4 reconstruction and explicit U16 footprint parity correction are reviewed.

2026-08-28 — corrected M4 native reconstruction

- Rebuilt the active PCB and schematic baseline from balanced M3 commit `b7a36ef` using a balanced-expression layer filter. The resulting board is natively parseable with 406 routed segments, 165 KiCad-recognized through-vias, zero In1/In2/In4 signal segments, and only `/VPROT_12V` on In3. Native DRC is 811 violations, 157 unconnected items, and 348 parity records; ERC is zero errors with 86 warnings. This supersedes malformed M4/M5 board-stream checkpoints while preserving them in Git for rollback. M5 SERVICE/routing changes must be replayed separately.

2026-08-28 — U16 support package parity correction

- Corrected C10/C11/C12/C13/C14/R8–R11 PCB package identifiers and nominal pad geometry to match their schematic-declared KiCad 1206/1210/0603 packages, preserving UUIDs and net assignments. Native DRC/parity changed to 1,420 violations, 156 unconnected items, and 339 parity records; U16 support routing and TI layout validation remain open.

2026-08-28 — M5 SERVICE migration checkpoint

- Reapplied the approved fixed-device SERVICE architecture to the balanced M4 board: removed U12/U13/U14 and obsolete SERVICE control traces/vias, retained J11 USB2 recovery, and added R12/R13 5.1 kOhm Rd plus C19 1 uF VBUS bypass. Native parse/statistics pass with 153 through-vias; netlist export passes; ERC remains zero errors with 95 warnings; DRC/parity is 812/150/348. USB2/high-speed routing remains gated.

2026-08-28 — U16 local support placement checkpoint

- Moved the nine U16 support footprints into the local regulator field while keeping U16 fixed and adding no copper. Native DRC is 810 violations and 149 unconnected items; package parity remains corrected and routing/SI/thermal closure is still open.

2026-08-28 — current M5 gate recheck after U16 placement

- Re-ran KiCad 10.0.5 against clean HEAD `4b19de6` (PCB SHA-256 `abcf70753c129a1e7099f04f7700f63b4e4c80fbac31d56a664b17835204b29f`). Native parse/statistics pass; ERC is 0 errors/95 warnings; DRC is 810 violations with 149 unconnected items and 348 schematic-parity records.
- Verified current routed-layer use: F.Cu 290 segments, B.Cu 90, In3.Cu 11 `/VPROT_12V` power segments, and no In1/In2/In4 signal segments. Verified 153 through vias (129 F.Cu-B.Cu, 8 each F.Cu-In1/In2/In3; no blind/buried/microvias). The literal `/GND` via count is five, but that count is misleading as a board-wide return/stitching metric because signal/power vias also provide through-stack continuity.
- Independent PCIe review found no contradictory evidence against the settled CM5-to-V100 PCIe Gen2 x1 basis. PER0 remains a good frozen route; PET0 and REFCLK have balanced lengths but lack local return vias; PERST retains three orphan vias and one sideband open for M7. M5 remains blocked pending a disposable, clearance-checked local-return-via study and native gate review. M6 USB reconstruction is not authorized from this state.

2026-08-28 — M5 PCIe transition-return correction

- Added six deliberately placed `/GND` F.Cu-B.Cu through vias at the PET0 and REFCLK transition fields only; PER0, PET0 raw legs, and unrelated routing remain frozen.
- Disposable candidate study and native KiCad 10.0.5 DRC found no candidate-specific short, clearance, hole, or connectivity violation. Current global DRC remains 811 violations / 149 unconnected records and is not a release claim.
- M5 high-speed transition scope is complete; PERST_N and PCIE_PWR_EN remain deferred to M7. See `validation/PiSXMe_M5_transition_return_checkpoint.md`.

2026-08-28 — M6 USB ESD truth precondition

- Corrected U15/U17/U18 schematic footprint fields to `PiSXMe:TPD2EUSB30A_DRT` and removed only the eight F.Cu segments attached to the NC pads 6/7/9/10 of U6/U10; signal and GND pads remain unchanged.
- Native validation after this focused edit: 159 through-vias, 0 blind/buried/microvias, 0 ERC errors, 810 DRC violations, 146 unconnected records, and 345 parity records. USB branches remain frozen for the M6 rebuild.
- See `validation/PiSXMe_M6_ESD_truth_checkpoint.md`.

2026-08-28 — M6 USB rebuild gate blocked

- Re-verified the current USB source after the ESD/package precondition. U6/U10
  are six-pad flow-through footprints with corrected netless/pad assignments,
  but the existing FAST-A/B USB3 branches do not terminate at the current
  device pads and FAST-A/B/SERVICE USB2 still contain vias or mixed-layer
  fragments. A bounded route reconstruction could not be made
  clearance-checked and pair-symmetric without changing frozen corridors, so
  no USB copper was changed and M6 remains FAIL. See
  `validation/PiSXMe_M6_USB_rebuild_checkpoint.md`.

2026-08-28 — M6 USB census correction

- Balanced source parsing confirms each FAST-A/B USB3 conductor currently has
  four signal vias, each FAST-A/B USB2 conductor has four vias, and each
  SERVICE USB2 conductor has four vias across mixed/fragmented branches. This
  exact census supersedes earlier informal USB-via counts and reinforces the
  M6 hard gate without changing the active board.

2026-08-28 — M6 disposable corridor study

- A target-only disposable A* study, using current U6/U10/J2/J9/J10 pad
  coordinates and non-target copper as obstacles, failed to find a
  clearance-safe FAST-A ESD-to-J9 path on F.Cu and again on a B.Cu fallback.
  The result is feasibility evidence for the fixed-placement fanout blocker,
  not a release route or DRC claim. No active PCB copper changed.

2026-08-28 — M6 I/O architecture replan

- The fixed dual-USB topology remains blocked after the disposable F.Cu/B.Cu
  corridor failures. Candidate 1 (native CM5 Ethernet plus FAST-A plus
  SERVICE) was rejected for promotion because its disposable mapped board had
  1,331 DRC violations, 156 unconnected items, 26 Ethernet unconnected items,
  and no Ethernet copper route.
- A pin-accurate disposable JMS578 coupon using the stock 6 x 6 mm QFN-48
  footprint connected all eight USB3/SATA differential nets with zero
  unconnected items. Its 70 fixture DRC violations are not full-board proof;
  they are retained as coupon limitations.
- The next M6 design basis is therefore native CM5 Gigabit Ethernet,
  JMS578 USB3-to-SATA, a clearly SATA-only B-key M.2 socket, and SERVICE
  USB2 recovery, with both external USB3 host branches removed. Candidate 2
  remains an M6 migration basis, not a passed gate. CM5/V100/PCIe, board
  outline, power concept, PER0, and M4 layer philosophy remain frozen.
- No active schematic or PCB source was changed by this architecture decision.

2026-08-28 — M6 architecture-unblocker current-source recheck

- Rebuilt the disposable Candidate 1 and Candidate 2 studies from the staged
  M2 240 x 140 mm source snapshot, preserving the active source unchanged.
- Candidate 1 (native CM5 Ethernet + FAST-A + SERVICE) contains the CM5IO-derived
  proxy footprints but zero Ethernet segment records; native KiCad 10.0.5 DRC is
  1,299 violations / 179 unconnected items. It is not routability evidence.
- Candidate 2 (native Ethernet + JMS578/M.2 SATA proxy + SERVICE) contains zero
  Ethernet or SATA segment records; native DRC is 1,108 violations / 113
  unconnected items. It is a placement/proxy study only, not a passed full-board
  candidate. The earlier JMS578 coupon remains topology-only evidence.
- Neither replacement architecture is promoted. M6 remains open and M7-M10 are
  still prohibited until a pin-accurate, current-source, clearance-checked
  candidate closes true signal opens/shorts and return-path/mechanical gates.
- See `validation/PiSXMe_M6_architecture_unblocker_current_checkpoint.md`.

2026-08-28 — U16 support footprint package correction

- Replaced the nine U16 support placeholders C10-C14/R8-R11 from the local
  `PiSXMe:M1_1206` geometry with their declared standard 1206/1210/0603
  capacitor and resistor land patterns.
- No copper, zones, USB routing, PCIe routing, or schematic content changed.
- A disposable local-net trial confirms the FB, RT, and PG nets can be joined,
  but full U16 routing and TI-layout validation remain open; this is not a
  release or M6-pass claim.

2026-08-28 — bounded U16 local support routing

- Removed the package-crossing `/VPROT_12V` diagonal in the active PCB and
  added the bounded FB/RT/PG support topology from disposable trial 4.
- Added six ordinary F.Cu-to-B.Cu vias with short pad escapes and local B.Cu
  trunks; no USB data, PCIe, zones, rules, or schematic content changed.
- Native active-board DRC exceeded the bounded runtime, so this is an
  implementation checkpoint only.  M3/M6 promotion still requires native DRC,
  TI loop/thermal review, and the pin-accurate I/O architecture gate.
2026-08-28 — bounded U1 package truth correction

- Replaced the active U1 TPSM63606 placeholder land pattern with the local
  manufacturer-derived RDL0020A/B3QFN geometry, preserving the existing pad
  UUIDs and schematic net intent.
- The correction exposes the real side-pin and four-pad exposed PGND/thermal
  field required by the module package. Existing U1 copper was intentionally
  not rerouted in this checkpoint; VIN/VOUT/FB/RT/EN/PG and thermal closure
  remain open for a disposable rebuild.
- Active PCB parses balanced with no duplicate UUIDs. Native DRC remains
  non-gating and was not claimed as passing.

2026-08-28 — bounded U16 package truth correction

- Replaced the active U16 TPSM63606 placeholder land pattern with the same
  manufacturer-derived RDL0020A/B3QFN geometry used for U1, preserving U16
  pad UUIDs and correcting pad 7 to the schematic's `/VCC_INTERNAL_NC` net.
- Existing U16 copper was intentionally not rerouted in this checkpoint;
  VIN/VOUT/EN/FB/RT/PG, exposed PGND/thermal lands, and local loop geometry
  remain open for the next disposable closure trial.
- The active PCB remained syntactically balanced; native DRC is still
  non-gating and no pass is claimed.

2026-08-28 — I/O-side outline expansion steering study

- Re-read the active source after the U1/U16 package-truth prerequisites. The
  active outline is 240 x 140 mm; 220 x 140 mm is historical. No Edge.Cuts,
  connector placement, copper, zones, or manufacturing artifact was changed.
- Evaluated 250/260/270/280 mm width candidates as +10/+20/+30/+40 mm from
  the active 240 mm baseline. 250 mm is the only conditional fallback; 260 mm
  or larger has no measured routing or mating benefit in current evidence.
- Keep 240 x 140 mm for the first pin-accurate M6 replacement-I/O trial. Only
  promote 250 mm if that trial demonstrates a genuine width-limited corridor
  or mating-envelope failure after stale USB endpoint geometry and support
  placement are corrected.
- This is a planning/evidence checkpoint, not an outline promotion or M6 pass.

2026-08-28 — corrected-package U16 closure trial rejected

- Disposable `/private/tmp/u16_power_closure_trial_corrected2.kicad_pcb` used
  the manufacturer-derived U16 package and connected VIN/VOUT/EN/FB/RT/PG in
  the local support field.
- The trial still produced same-layer VIN/VOUT/EN/RT/PGOOD conflicts and
  inadequate pad-escape margin within x approximately 194.5..210 mm. It is
  rejected; the failure is local support placement/legacy-route topology, not
  a board-outline limit.
- Active source was not modified by the trial. Re-place U16 support and remove
  adjacent legacy fragments before the next closure attempt; M6 remains open.

2026-08-28 — Candidate 1 Ethernet insertion boundary

- A bounded Candidate 1 disposable attempt stopped before any topology edit.
  `/private/tmp/pisxme-v2-candidate1/PiSXMe_V2_Candidate1.kicad_pcb` is
  byte-identical to active source `8bd0d56b...`.
- The active schematic has no Ethernet nets, MagJack identity, or CM5IO-derived
  endpoint mapping. Adding proxy copper/footprints would be speculative, so
  FAST-B removal and FAST-A/SERVICE rebuild were not performed.
- Candidate 1 is therefore untested, not passed or rejected. Establish the
  schematic/net/footprint insertion boundary from official CM5IO before any
  replacement-I/O disposable mutation; M6 remains open.

2026-08-28 — U16 support replacement disposable rejected

- `/private/tmp/u16_support_replacement_trial.kicad_pcb` (SHA-256
  `f06ebda1233f9d97f694f53f7868574537a87105d9d430cd354e81ae3ac8d525`) was a
  disposable re-placement/routing trial for the corrected U16 package.
- Native KiCad 10.0.5 DRC reported 1433 violations and 172 unconnected items.
  The trial has true GND-to-USB_5V_PERIPH, PCIE_PWR_EN-to-USB_5V_PGOOD and
  VPROT_12V-to-GND shorts, plus RT/PG/FB crossings and stale FAST-B VBUS
  geometry. It is rejected and is not closure evidence.
- Active source, schematic, zones, and manufacturing outputs were unchanged.
  Rebuild the complete U16 local corridor in a fresh disposable study; do not
  infer that board-width expansion is required.

2026-08-28 — second U16 topology disposable rejected

- `/private/tmp/pisxme-u16-topology-trial-73566/PiSXMe_U16_topology_trial.kicad_pcb`
  moved U16 to `(214,130)`, removed stale local routes, and attempted a
  bounded pin-accurate support topology.
- Native KiCad 10.0.5 DRC reported 857 violations and 177 unconnected items
  (499 clearance, 35 shorting-item, 152 solder-mask bridge). PGOOD/RT/EN
  crowding, FB-to-ground-pad interference, wrong resistor-pad vias, control
  crossings, and stale-zone contamination caused rejection.
- Active source, schematic, zones, and manufacturing outputs were unchanged.
  The result confirms the need for a complete U16 local rebuild, not an
  automatic board-width expansion or M6 pass.

2026-08-28 — CM5IO Ethernet boundary extracted

- Official CM5IO maps CM5 pads 3/4/5/6/9/10/11/12 to TRD3_P, TRD1_P,
  TRD3_N, TRD1_N, TRD2_N, TRD0_N, TRD2_P and TRD0_P.
- The reference implementation uses two TPD4EUSB30 arrays, a
  TRJG0926HENL integrated-magnetics MagJack, 100 nF center-tap decoupling,
  470 ohm LED resistors, and zero Ethernet signal vias on F.Cu.
- This is a disposable insertion boundary only. PiSXMe six-layer impedance,
  shield treatment, MagJack availability, and active schematic migration remain
  open; no active source was changed.

2026-08-28 — prior Candidate 1 disposable artifacts reclassified

- Temporary Ethernet-plus-FAST-A studies exist under `/private/tmp`, including
  `pisxme_m6_candidate1_routed_plus20.kicad_pcb` (1440 violations/154
  unconnected) and `pisxme_candidate1_plus20/...io_shifted_study.kicad_pcb`
  (1234 violations/187 unconnected) from native KiCad 10.0.5 DRC.
- Their PCB-only generator inserted disposable net names/footprints without an
  active schematic hierarchy. They are failed exploratory artifacts, not
  pin-accurate promotion evidence; Candidate 1 remains unproven until a fresh
  source-bound trial passes the M6 gate.

2026-08-28 — M6 architecture-unblocker disposition

- No Ethernet replacement architecture is promoted. The official CM5IO
  Ethernet boundary is known, but no fresh Candidate 1 trial passed route,
  DRC, and mechanical gates; prior temporary studies were PCB-only and failed.
- Both U16 support-field trials were rejected by native DRC. M6 remains
  blocked, M7-M10 remain prohibited, and 240 x 140 mm remains the active
  outline baseline with 250 mm only as a measured-clearance fallback.
- Next bounded work is a complete U16 local rebuild, then a pin-accurate
  Ethernet + FAST-A + SERVICE disposable route. Candidate 2 Ethernet + internal
  SATA is allowed only if Candidate 1 fails for a demonstrated I/O pinch point.
  Active source and manufacturing outputs remain unchanged.

2026-08-28 — bounded M4 prohibited signal-via cleanup

- Removed exactly 24 signal vias whose layer pairs violated the approved layer
  policy: eight `/CM5_USB3_1_*` F.Cu-In3 vias, eight FAST-A USB2 F.Cu-In2/In1
  vias, and eight FAST-B USB2 F.Cu-In1/In2 vias. No segments, footprints,
  zones, schematic content, GND vias, or power vias were changed; the removed
  endpoints remain intentionally open for M6 reconstruction.
- Structural census after the edit: balanced PCB stream, SHA-256
  `a53e6751a59eb530afd3b522672b5ce967515710bf7eece54a5aa4242e81316e`, 400
  segments, 62 footprints, 14 zones, and 141 physical vias. All 141 are
  ordinary F.Cu-B.Cu through vias; zero signal vias reference In1/In2/In3/In4.
  Four `(vias allowed)` keepout properties are not physical via records.
- This is a narrow M4 policy correction, not an M6 route solution. USB topology
  remains blocked and no DRC or release-gate claim is made.

2026-08-28 — U16 active-source status rechecked

- The active source contains no accepted U16 local-support reroute. Earlier
  wording describing a bounded trial topology as active is superseded; the
  corresponding topology was disposable only.
- FB, RT, and PGOOD remain stale/misaligned relative to the corrected U16
  package, and the schematic wire/label truth is not aligned for a PCB-only
  patch. The latest corrected-topology disposable trial was rejected at
  1,279 DRC violations / 175 unconnected items. U16 remains open for a
  coordinated M1/M3 schematic and PCB rebuild.

2026-08-28 — fresh Candidate 1 reroute trial rejected

- Disposable `/private/tmp/pisxme-candidate1-reroute/PiSXMe_Candidate1.kicad_pcb`
  removed FAST-B and inserted CM5IO-derived Ethernet proxy footprints/routes.
- Native KiCad 10.0.5 DRC reported 1322 violations and 186 unconnected items.
  Because the trial used PCB-only proxy Ethernet nets without a matching
  schematic hierarchy and retained generic clearance/width/mask/dangling and
  shorting failures, it is rejected as promotion evidence. Active source,
  schematic, zones, and manufacturing outputs were unchanged.

2026-08-28 — coordinated U16 disposable trial rejected

- `/private/tmp/pisxme-u16-coordinated/PiSXMe_U16_trial.kicad_pcb` used a
  coordinated support-field placement and pin-accurate escapes. Native KiCad
  10.0.5 DRC reported 1346 violations and 182 unconnected items.
- Target-net inspection still found PGOOD/FB/RT/EN/VIN/VOUT crossings and
  shorts with adjacent pads and stale zones. The trial was rejected; no active
  source or schematic change was accepted.

2026-08-28 — M6 checkpoint terminology corrected

- Corrected the M6 USB checkpoint's stale U6/U10 description: the active
  TPD4E05U06 flow-through footprints have 10 pads, with USB3 on 1/2/4/5,
  GND on 3/8, and NC on 6/7/9/10. This documentation correction does not
  change the active PCB or schematic and does not alter the M6 gate.

2026-08-28 — M6 architecture checkpoint stale active-route wording corrected

- Reinspection of the active PCB confirms that the U16 FB/RT/PG reroute
  described in older follow-up paragraphs is not present in the active source.
  Those paragraphs are superseded; U16 remains open for a coordinated
  schematic/PCB rebuild.
- The active-source copper correction after the package prerequisites is the
  bounded M4 removal of 24 prohibited plane-layer signal vias, yielding PCB
  SHA-256 `a53e6751a59eb530afd3b522672b5ce967515710bf7eece54a5aa4242e81316e`.

2026-08-29 — M6 continuation: proxy architecture trials remain rejected

- A native KiCad 10.0.5 check of disposable
  `/private/tmp/pisxme_candidate1_trial.kicad_pcb` reported 1326 violations
  and 185 unconnected items. The copy removed FAST-B and inserted Ethernet
  proxy nets/footprints without a matching schematic hierarchy; it is not
  promotion evidence.
- Disposable Candidate 2
  `/private/tmp/pisxme_candidate2_eth_sata_260.kicad_pcb` remains a placement
  proxy: Ethernet and SATA pairs are unrouted, the JMS578 and M.2 objects are
  not vendor-verified, and the underside mechanical envelope is unvalidated.
- Active source remains unchanged except for the bounded U16 schematic label
  correction; PCB SHA-256 remains
  `a53e6751a59eb530afd3b522672b5ce967515710bf7eece54a5aa4242e81316e`, and
  schematic SHA-256 is
  `d31ff8e96fd1df211f5528f0b4c70f8b7a7891d68383d4561bfae83116bf5bbb`.
- No Ethernet/SATA architecture or +20 mm outline is promoted. M6 remains
  open pending a source-bound, pin-accurate replacement-I/O trial.

2026-08-29 — final disposable U16 trial rejected

- `/private/tmp/u16_final_disposable_20260828_v3` connected U16 FB/RT/PG but
  native KiCad 10.0.5 DRC still reported 824 violations, 163 unconnected
  items, 337 schematic-parity issues, 15 shorting-item violations, and 2 track
  crossings. PGOOD-to-ground and RT/EN local conflicts remain.
- The trial is disposable only; active PCB SHA-256 remains
  `a53e6751a59eb530afd3b522672b5ce967515710bf7eece54a5aa4242e81316e` and no
  active PCB, manufacturing output, branch, or commit was changed.

2026-08-29 — no-zone U16 isolation trial rejected

- `/private/tmp/u16_final_disposable_20260829_v4` removed zones and stale local
  U16 copper to isolate support-field geometry. Native KiCad 10.0.5 DRC found
  249 violations, 418 unconnected items, and 337 schematic-parity issues; the
  unconnected count is expected for a zone-free copy.
- FB was clean, but RT retained two crossings and PGOOD retained five real
  violations, including shorts to U16 ground pad 18/ground via and PGOOD/RT
  corridor crossings. The trial is rejected; active PCB remained unchanged.

2026-08-29 — Candidate 1 +20 mapping follow-up remains unproven

- `/private/tmp/pisxme_candidate1_260_mapping.kicad_pcb` assigned the official
  CM5IO Ethernet pad mapping and placed two ESD arrays plus a MagJack after
  removing FAST-B, but added no Ethernet copper. The +20 mm outline improved
  MagJack edge/cable placement without materially widening the CM5-to-ESD
  pinch point. This is placement/net-mapping evidence only; no routability or
  promotion claim is made.
- A fresh native KiCad 10.0.5 DRC of disposable
  `/private/tmp/pisxme_candidate2_eth_sata_260.kicad_pcb` reported 1111
  violations and 114 unconnected items. Because it remains a proxy study with
  no meaningful routed Ethernet/SATA topology, it is rejected and cannot
  justify architecture promotion.

2026-08-29 — Candidate 1 routed +20 follow-up rejected

- `/private/tmp/pisxme_m6_candidate1_routed_plus20.kicad_pcb` removed FAST-B and
  added temporary CM5IO-derived Ethernet routes on a 260 x 140 mm copy.
- Pair lengths were TRD0 20.31/20.49 mm, TRD1 22.93/26.50 mm, TRD2
  24.65/25.02 mm, and TRD3 27.57/28.56 mm; TRD1 and TRD3 used two signal
  vias per conductor.
- The route contained 44 Ethernet segments, 20 crossing instances, and 15
  unique cross-net pair combinations. It is rejected; +20 mm did not cure the
  fanout without a restructured ESD placement/topology.

2026-08-29 — current U16 support graph is present but unvalidated

- Direct current-PCB inspection (SHA-256
  `a53e6751a59eb530afd3b522672b5ce967515710bf7eece54a5aa4242e81316e`) finds
  six segment records each for `/USB_5V_PERIPH_FB`, `/USB_RT_1MHZ`, and
  `/USB_5V_PGOOD`, with F.Cu/B.Cu transitions and vias.
- Older wording that these active nets were absent is superseded. Their graph
  is **CONNECTED BUT UNVALIDATED** because active-board native DRC did not
  complete and support, plane, thermal, and parity signoff remain open.

2026-08-29 — Mac-side execution paused for Linux tooling handoff

- No M6 implementation was resumed. The active Rev A source remains unchanged;
  the current blocker is the missing proof that schematic-authoring tooling can
  produce authoritative KiCad 10 connectivity and source-derived PCB nets.
- The approved I/O direction for the next M6 attempt is native CM5 Gigabit
  Ethernet, internal JMS578 USB3-to-SATA with a SATA-only M.2 socket, and
  SERVICE USB2 recovery; the legacy external FAST USB routes are not to be
  restarted.
- Mac-side `kicad-sch-api`/SKiDL experiments remain evidence only. The next
  gate is reproducible Linux installation and flat, hierarchy, custom pin-map,
  and schematic-to-PCB authority fixtures before any PiSXMe source edit.
- Handoff documents and durable evidence are in `HANDOFF_LINUX_WORKSTATION.md`,
  `TOOLING_STATUS.md`, `references/REFERENCE_INDEX.md`,
  `plans/M6_LINUX_RESTART_CHECKLIST.md`, and `validation/m6/`.

2026-08-29 — public recovery repository handoff

- A public preservation repository is being created from the locally recovered,
  byte-verified active source and readable tooling/evidence. The original
  iCloud-backed checkout contains File Provider dataless placeholders, so the
  publication includes an explicit `RECOVERY_MANIFEST.md` rather than guessing
  or fabricating unavailable files.
- This is a documentation/recovery publication only; no M6 implementation,
  PCB, schematic, manufacturing artifact, or Git history in the active checkout
  is being changed.

2026-08-29 — Mac recovery material integrated on NYX

- Verified all 208 entries in `/srv/pisxme-recovery/SHA256SUMS`, then copied the
  recovered project-shaped tree additively into the NYX checkout on
  `recovery/mac-import-20260829`. All 39 pre-existing tracked overlaps were
  byte-identical, so no recovered file displaced differing repository content.
- Restored the recovered bridge, tests, tooling, design and validation evidence,
  active project rule file, and all 30 custom footprint files. The authoritative
  schematic, PCB, project, and symbol-library bytes remain unchanged from the
  handoff baseline.
- Preserved `conflicts/mac-materialized-20260829/` as an archive rather than
  promoting its variants. Two AppleDouble metadata blobs and one zero-byte
  temporary file were quarantined under
  `conflicts/mac-recovery-artifacts-20260829/`; the staging recovery remains
  untouched.
- The canonical `design/COMPONENT_SOURCING_REALITY_V2.md` recovered as zero
  bytes, while a non-empty differing copy remains in the conflict archive. No
  authority choice was inferred; deliberate provenance review is still required.
- Native KiCad 10.0.5 parsed the recovered active schematic and board. Netlist
  export succeeded; baseline validation reported 94 ERC violations, 803 DRC
  violations, and 182 unconnected items, consistent with the documented open
  design debt rather than a recovery parse failure.
- A dedicated `/home/nyx/venvs/pisxme-bridge` Python 3.11 environment contains
  the four pinned bridge dependencies and pytest. With the KiCad Flatpak Symbols
  extension exposed through `KICAD_SYMBOL_DIR`, 11 of 12 recovered tests passed.
  The remaining test is non-portable because it hard-codes the Mac path
  `/Users/Cooper/Documents/ChatGPT/sxm2`; recovered source was not rewritten in
  this import to conceal that defect.
- The existing external disposable toolchain validator was rerun after import:
  `pcbnew` load/save and source-defined pad-net mapping passed, native ERC and DRC
  both reported zero violations, and KiCad generated 13 Gerbers plus one Excellon
  drill file. Those outputs remain outside the repository under
  `/home/nyx/pisxme-toolchain-environment/fixture/`.

2026-08-29 — clean Rev A rebuild plan approved

- Recorded the approved clean-rebuild program in
  `Approved Plans/PiSXMe_RevA_Clean_Rebuild_Plan.md`.
- The plan freezes the recovered `pisxme/PiSXMe.*` design as
  `LEGACY_DONOR_REFERENCE` and establishes `pisxme/reva-clean/` as the only new
  implementation path. It also requires the isolated `PiSXMeRevAClean` library
  namespace, evidence-based CM5 orientation selection, acreage validation before
  compression, and routing plus assembly-complexity rejection gates.
- This checkpoint records planning authority only. No legacy schematic, PCB,
  footprint, rule, routing, zone, or manufacturing source was modified.

2026-08-29 — clean Rev A Phase 0 recovery checkpoint validated

- Preserved the 172-file, checksum-verified recovery import in commit
  `8e6d029` before any portability change; `/srv/pisxme-recovery/SHA256SUMS`
  reports 208/208 entries OK, including the 30 custom footprint files.
- Created the clean-rebuild branch from that import and made the bridge path
  containment test portable with a temporary host-local root. The recovered
  bridge/backend/integration suite is now 12/12 passing under Python 3.11 with
  KiCad Flatpak symbols exposed.
- KiCad 10.0.5 native legacy parse remains reproducible at 94 ERC violations,
  803 DRC violations, and 182 unconnected items; these are frozen baseline
  evidence, not clean-design acceptance. The disposable SKiDL/PCB fixture
  generated a zero-violation native DRC report, 25 Gerber files, and one
  Excellon drill file; outputs remain outside the repository.
- No legacy design source was edited. Phase 0 is accepted on the private
  checkpoint branch pending the private push and recovery tag.

2026-08-29 — clean Rev A Phase 1 donor extraction validated

- Added `pisxme/reva-clean/donor-extraction/PHASE1_DONOR_MANIFEST.md` with
  KEEP, FIX_WHILE_TRANSPLANTING, and DISCARD dispositions for PCIe/SXM2,
  mechanics/cooling, CM5/I/O, storage/SERVICE, power/protection, regulators,
  footprints, and rules.
- Added `PHASE1_RECONCILIATION_RECEIPT.md` with the frozen legacy hashes,
  current-source geometry census, and explicit treatment of stale via/count and
  footprint-audit records. No legacy source or routed geometry was promoted.
- Phase 1 gate is `PASS_WITH_EXPLICIT_FIX_QUEUE`; exact authority closure,
  independent clean-library validation, and undocumented V100 behavior remain
  later gates by design.

2026-08-29 — clean Rev A Phase 2 authority inventory bounded

- Materialized the official Raspberry Pi CM5IO Rev 2 archive under
  `pisxme/reva-clean/authority-inventory/cm5io-rev2/` (30 files; source ZIP
  SHA-256 `48b14a...b59496b`) and native-parsed its schematic under KiCad
  10.0.5. The reference board parsed with 76 DRC violations and 0 unconnected
  items; this is upstream observation only.
- Materialized primary CM5IO, JMS578, TI power/protection/high-speed, and V100
  documents with recorded hashes. JMS578’s primary brief confirms the bridge
  family and UASP but does not close firmware, package procurement, or Linux
  behavior.
- Added `PHASE2_AUTHORITY_INVENTORY.md`. Phase 2 remains
  `BLOCKED_PENDING_EXACT_AUTHORITIES` for the exact B-key socket, SXM2
  land-pattern overlay, cooler/backplate, Ethernet ESD selection, selected
  current JLC stackup, and remaining bridge/procurement evidence. No clean
  schematic or PCB synthesis was started.

2026-08-29 — clean Rev A Phase 2 authority closure sprint disposition

- Replaced the preliminary Phase 2 inventory with an authority-by-authority
  disposition and added `PHASE2_PROCUREMENT_MATRIX.md`.
- Closed the JAE B-key SATA M.2 socket authority, TI TPD4E004DRYR Ethernet ESD
  choice, Amphenol 74221-101LF connector identity, and current JLC06161H-7628
  six-layer/impedance basis. Added local source receipts for M.2, SXM2,
  mechanics, Ethernet ESD, JMS578, and JLC calculator evidence.
- Classified the proprietary V100 cooler/backplate envelope and unverified
  local SXM2 land-pattern transplant as explicit `REV_A_EMPIRICAL_RISK`.
- JMS578 was rejected after the out-of-stock LCSC listing and incomplete
  firmware/Linux evidence failed the approved gate. TI `TUSB9261IPVP` is now
  the selected replacement: active exact DigiKey/Mouser stock, TI firmware
  resources and FlashBurner, implementation/EVM documentation, and explicit
  USB/SATA/reset behavior. Phase 2 is closed; the TI firmware download receipt
  records the export-gated binary resources and the remaining Phase 7 Linux
  qualification tests. No Phase 3 schematic or PCB was modified.

2026-08-30 — Phase 2 closure evidence strengthened and Phase 3 held

- Added the locally captured exact JAE `SM3ZS067U410` drawing and current JLC
  impedance-template API response for `JLC06161H-7628`, including hashes and
  the exact API request fields. Reframed the JLC record correctly: Phase 2
  closes the current stack/target basis; Phase 13 owns returned route geometry
  and fabrication coupon evidence.
- Added `PHASE2_CLOSURE_RECEIPT.md`, which explicitly classifies only the
  cooler/backplate, SXM2 legacy land-pattern transplant, and unavailable exact
  CM5IO MagJack as `REV_A_EMPIRICAL_RISK`; no obtainable drawing, calculator
  source, or procurement question is hidden under that label.
- Removed an unvalidated Phase 3 scaffold created before this evidence review.
  The clean schematic, PCB, project, and libraries remain absent; Phase 3 is
  not started until the strengthened authority checkpoint is independently
  re-audited.

2026-08-30 — Phase 3 architecture scaffold started

- After the strengthened Phase 2 checkpoint, created the native
  `PiSXMe_RevA_Clean` project shell with exactly the ten plan-defined child
  sheets, isolated `PiSXMeRevAClean` library tables, and architecture,
  interface, net-class, and source-authority ledgers.
- The scaffold is intentionally not a production schematic: child-sheet pins,
  real block connectivity, selected local assets, pin/pad parity, and a
  schematic-derived PCB fixture remain open. No placement or routing was
  introduced, and the legacy donor remains immutable/reference-only.

2026-08-30 — Phase 3 native scaffold receipt

- Generated the native `PiSXMe_RevA_Clean` root plus exactly ten named child
  sheets from a local deterministic scaffold generator. KiCad 10.0.5 plotting
  and root parsing complete under Xvfb; namespace and machine-path scans are
  clean outside frozen evidence.
- This is not a Phase 3 pass: ERC reports 78 expected unconnected scaffold
  interfaces, and no production symbols, footprints, components, PCB,
  placement, routing, or parity fixture exists. The receipt records the open
  gate and required next work.

2026-08-30 — removed disposable SKiDL probe logs

- Removed the untracked `skidl.erc` and `skidl.log` files created by an
  exploratory environment probe; they were not design evidence or project
  outputs.

2026-08-30 — Phase 3 hierarchy gate blocked

- Audited the clean root and ten child sheets with KiCad 10.0.5. Native ERC
  remains at 40 root-only hierarchy violations while all child sheets load
  without hierarchy errors.
- Tested the documented root/sheet and child-symbol instance-path forms,
  including project `instances` records; none produced a passing association.
  The clean hierarchy is therefore blocked at the earliest Phase 3 gate and
  no later phase, placement, routing, or PCB artifact was introduced.
- Unblock requires a native KiCad-authored saved root/child association or a
  reproducible installed KiCad authoring route. This is a blocker receipt, not
  a validated checkpoint.

2026-08-30 — Phase 3 native hierarchy association closed

- Reproduced the root hierarchy failure with KiCad 10.0.5 and isolated the
  cause: the generated contract symbol was appended after the child
  `(lib_symbols)` section, making each child unloadable and presenting as root
  `hier_label_mismatch` errors.
- Corrected the generic authoring path by inserting each contract definition
  inside `(lib_symbols)`, using KiCad's native inverted library Y coordinates,
  and generating real root wires to every sheet pin.
- Native KiCad 10.0.5 root ERC now reports zero violations across all ten
  children. Added `validation/phase3/test_native_hierarchy_authoring.py`;
  generation, serialization assertions, and native ERC all pass. No
  placement, routing, PCB, or Phase 4 work was introduced.
- Regenerated the contract instances with deterministic per-sheet references
  (`X_CORE_CM5`, `X_V100_PCIE`, and so on); hierarchy regression and native ERC
  remain passing after the netlist-reference cleanup.

2026-08-30 — Phase 3 architecture gate closed

- Added a generic EDAC extraction rule that removes donor-only shield pins
  19/20 because the selected A70-112-331N126 manufacturer layout defines
  P1–P18 as electrical contacts and shield features as mechanical NPTH.
- Added machine-readable parity evidence: CM5 200/200 and EDAC 18/18;
  native reopen/ERC, non-empty KiCad XML netlist, clean namespace/path scan,
  and zero PCB-only/proxy nets by construction all pass.
- Recorded `PISXME_REVA_CLEAN_PHASE3_CLOSED` in the Phase 3 exit receipt.
  No placement, routing, PCB, or Phase 4 work was introduced by this gate.

2026-08-30 — strengthened Phase 3 parity evidence

- Added a disposable native-format schematic-to-PCB parity fixture and
  regression test proving PCB-only/proxy nets are rejected at the architecture
  boundary while the clean project remains PCB-free.

2026-08-30 — Phase 4 SXM2 authority isolation started

- Added a project-local SXM2 symbol/footprint extraction and a lane-0 mapping
  receipt for Amphenol `74221-101LF` Rev-W. The 400-pad land pattern remains
  explicitly `REV_A_EMPIRICAL_RISK`; no placement or routing was introduced.

2026-08-30 — Phase 4 V100 lane-0 schematic gate closed

- Added the schematic-only V100 island: lane 0 PER0/PET0, two transmitter-side
  PET0 coupling capacitors, REFCLK, PERST, and the documented SXM2 contacts.
- Added the machine-readable Phase 4 audit and receipt. Native KiCad reopen
  and ERC pass with zero violations; no PER1+, x16, NVLink, switch, or
  redriver baggage exists. No placement or routing was introduced.

2026-08-30 — Phase 5 power architecture gate closed

- Added schematic-only dual LM74700 protected inputs, protected 12 V merge,
  CM5 5 V, TUSB9261 3.3/1.1 V rail contracts, and the V100 power contract.
- Added the machine-readable power audit and receipt; native KiCad ERC passes
  with zero violations. No PCB placement or routing was introduced.

2026-08-30 — Phase 6 Ethernet schematic gate closed

- Added the four-pair CM5IO-derived Ethernet island with EDAC
  `A70-112-331N126` and TI `TPD4E004DRYR` connector-boundary ESD.
- Added the Ethernet audit and receipt; native KiCad ERC passes with zero
  violations. No placement or routing was introduced.

2026-08-30 — Phase 7 storage schematic gate closed

- Added schematic-only CM5 USB3 to TI TUSB9261IPVP to SATA to JAE B-key M.2
  storage connectivity, with dedicated bridge rails/reset/config contracts.
- Added the storage audit and receipt; native KiCad ERC passes with zero
  violations and NVMe/USB2 SERVICE paths are excluded.

2026-08-30 — Phase 8 SERVICE schematic gate closed

- Added the USB2 UFP service connector, boundary ESD, host VBUS sense, and
  two 5.1 kOhm Rd resistors; source/DRP/SuperSpeed circuitry is excluded.
- Added the SERVICE audit and receipt; native KiCad ERC passes with zero
  violations. No placement or routing was introduced.

2026-08-30 — Phase 9 mechanical envelope gate closed

- Added clean V100 cooler/backplate and M.2 2280 retention envelopes plus
  SXM2 courtyard audit. Proprietary/uncaptured 3D remains explicitly
  empirical risk; no donor model was promoted as exact authority.

2026-08-30 — Phase 10 orientation study closed

- Added native topside and underside CM5 placement-study boards with V100,
  SXM2, M.2, and cooler anchors; both contain zero routing.
- Selected the underside-CM5 candidate for Phase 11 floorplanning, subject to
  later mating and assembly review.

2026-08-30 — Phases 11/12 acreage floorplan closed

- Added a native 300 x 180 mm no-routing acreage floorplan with central V100
  reservation, edge power/service neighborhoods, Ethernet/storage zones, and
  M.2 service envelope.
- Corrected inherited CM5/M.2 conflicts and recorded the remaining SXM2/
  cooler 2D courtyard overlap as intentional vertical stacking requiring
  physical confirmation.

2026-08-30 — Phase 13 current JLC stack finalized

- Exercised the current public JLCPCB calculator with the exact six-layer
  `JLC06161H-7628` template and saved the selected-template capture plus
  inverse-calculation evidence for 90-ohm and 100-ohm differential targets.
- Released 5.2 mil width / 8 mil pair spacing as the Rev-A starting constraint,
  with ordinary through vias, adjacent L2/L5 GND references, and mandatory
  fabrication coupon verification. No fabricated-board result is implied.

2026-08-30 — Phase 14/15 entry checkpoint rehydrated

- Replayed the deterministic clean authoring pipeline after the Phase 3
  regression test exposed that its fixture-generation step intentionally
  rebuilds downstream child sheets. Reapplied the SXM2/V100 lane-0 and PET0
  coupling authoring path, then reran the Phase 4–11 audits.
- Native root ERC with error severity reports zero violations; no power or
  signal routing has been claimed or started by this checkpoint.

2026-08-30 — Phase 3 regression harness isolation corrected

- The hierarchy generator is now exercised in a disposable copy while native
  ERC checks the live clean project. This prevents validation from erasing
  downstream island authoring and preserves the Phase 4 audit contract.

2026-08-30 — Phase 14/15 footprint prerequisite started

- Added a deterministic exact-MPN package-footprint assignment path for the
  selected LM74700QDBVRQ1, TPSM63606RDLR, TUSB9261IPVP, and TPD4E004DRYR
  instances, plus a machine-readable pad-count audit.
- Kept Phase 14/15 open because connector/socket land patterns and complete
  pin-to-pad authority are still required before real routed copper.

2026-08-30 — Phase 14 JAE B-key socket pattern derived

- Derived the selected JAE `SM3ZS067U410ABR1000` B-key footprint from the
  dimensioned drawing and SATA-IO TP053 by placing the eight-position void at
  physical positions 12–19. The clean STORAGE instance now references the
  project-local 67-contact pattern and the extraction regression passes.
- This does not close the full routing gate; SXM2 and remaining connector
  land-pattern authority still require independent review.

2026-08-30 — Phase 14 SXM2 authority comparison refreshed

- Rechecked Amphenol's current product authority for `74221-101LF`: active,
  400-position, 1.27 mm array, 4 mm height, and current distributor stock.
- Compared the clean 400-pad/40 x 10/1.27 mm pattern to the released Rev-W
  metadata. Mask, paste, and A1 details remain explicit empirical risk because
  the manufacturer CDN blocks local drawing capture; no exact ECAD promotion or
  routing was performed.

2026-08-30 — Phase 14 M.2 socket sub-gate closed

- Updated the M.2 authority receipt to reference the clean JAE B-key footprint
  and its 67-pad/12–19-void regression evidence. The overall routing gate
  remains open pending remaining connector patterns and complete pin-pad review.
2026-08-30 — Phase 14 USB-C service connector authority closed

- Promoted Amphenol `10171746-00021LF` as the exact USB2 SERVICE receptacle.
- Added manufacturer-derived local footprint, exact MPN assignment, procurement
  receipt, and regression test; native root ERC remains clean.

2026-08-30 — Phase 14 SERVICE ESD and passive footprint authority closed

- Assigned TI `TPD2EUSB30DRTR` to the project-local Texas DRT-3 three-pad
  footprint using the documented 1.0 x 0.8 mm / 0.7 mm-pitch package geometry.
- Corrected the generic service authoring path so the old USB-C connector
  footprint cannot leak onto the ESD or Rd resistors; both Rd parts now use a
  separate project-local 0402 footprint.
- Added exact-MPN regression coverage; the clean root native ERC remains zero.

2026-08-30 — Phase 14 materialization exposed two authoring defects

- Added a native pcbnew materialization harness for a disposable six-layer
  candidate; it imports 17 assigned components and 78 netlist nets without
  mutating the floorplan.
- Corrected Ethernet ESD to two six-pin TI TPD4E004DRYR devices, covering all
  four MDI pairs, and corrected the two bridge supply rails from mistaken
  TUSB9261 placeholders to TPSM63606RDLR modules.
- Native root ERC returned zero after both corrections. SXM2 abstract PWR/GND
  contact assignment remains explicitly open pending authoritative pinout.
2026-08-30 — Native CM5 authority promoted and acreage materialization corrected

- Promoted the authoritative Raspberry Pi CM5 two-unit, 200-pin symbol into
  `CORE_CM5.kicad_sch`, preserving exact pin names/numbers and marking only
  unmapped interface pins no-connect. Native KiCad 10 ERC is zero.
- Added a regression fixture for the two-unit native CM5 authoring path and
  corrected the pcbnew materializer for KiCad UTF8 identifiers. The candidate
  now materializes all 20 schematic components and 218 nets on six copper
  layers; the sole intentional unresolved contact mapping is SXM2 J1 PWR/GND,
  retained as the documented Rev-A empirical-risk item.

2026-08-30 — Phase 5 power gate made fail-closed

- Corrected the Phase 5 receipt to `IN_PROGRESS`: native ERC and MPN presence
  do not prove the required LM74700 external MOSFET/VCAP path or TPSM63606
  20-pin support network.
- Strengthened the power audit so it requires package-pin evidence and the
  documented fuse/MOSFET support components before Phase 5 can pass.

2026-08-30 — Phase 5 power implementation contract recorded

- Added `PHASE5_POWER_NETWORK_SPEC.md` from the preserved LM74700-Q1 and
  TPSM63606 datasheets, including exact pin maps, external FET/fuse/TVS
  topology, regulator support requirements, and the pre-routing acceptance
  gate.
- Corrected the Molex authority receipt to record that its project-local
  land pattern is now materialized; this does not close the separate circuit
  completion gate.

2026-08-30 — Phase 5 fuse authority gap closed

- Added current Littelfuse authority and procurement evidence for the separate
  `0297015.U` 15 A MINI blade fuse and `178.6165.0001` four-hole PCB holder.
- Kept the electrical rating, I2t, derating, inrush, and holder land-pattern
  integration explicitly open for the Phase 5 circuit gate; the parts are not
  collapsed into a fictitious two-pad component.

2026-08-30 — ROOT_HIERARCHY_ASSOCIATION continuation closed

- The native KiCad fixture remained green, and the clean CM5 promotion was
  corrected to parse the authoritative two 100-pin units independently.
- Clean-root KiCad 10 ERC is zero with J7 present; native netlist export and
  pcbnew materialization now include the 200-pin CM5 footprint. Phase 3 status
  records the generic authoring-path correction and regression test.

2026-08-30 — Phase 5 power network and calculation gate closed

- Completed the native dual-input LM74700/CSD19536KCS/SMBJ18A protection
  networks and all three TPSM63606 support networks, including the 1.1 V
  divider and sixteen 22-uF output capacitors. Native ERC and the XML netlist
  audit pass with the protected rail handed to SXM2 J1.A3.
- Added reproducible design-envelope calculations. Corrected the worksheet's
  low-voltage input arithmetic to 2.10 A, making the total 25.25 A and equal
  branch envelope 12.625 A; a single branch is explicitly over the 15 A fuse
  envelope. Sharing, copper, thermal, and exact ceramic DC-bias confirmation
  remain binding `REV_A_EMPIRICAL_RISK` constraints for later gates.
- Added native bridge round-trip regression coverage and local project
  footprints/support authority for the newly represented power components.

2026-08-30 — Phase 3/SXM2 hierarchy and materialization correction

- Corrected the native SXM2 symbol row orientation and separated overlapping
  root V100/STORAGE sheet-pin wires; KiCad 10 netlist export now preserves the
  intended A2/A3, E7/F7, G1/G2, and E18 mappings with zero native ERC errors.
- Added the explicit, non-authoritative reverse-engineered SXM2 endpoint power
  map to disposable PCB materialization: 130 protected-power and 70 ground
  contacts, with stale donor pad nets cleared before assignment.
- Added `test_phase14_sxm2_power_aliases.py` and updated the Phase 5 audit to
  test logical J1.PWR rather than misidentifying signal contact A3 as power.

2026-08-30 — Phase 14 power-route candidate and V100 return-net correction

- Corrected the V100 endpoint return to the shared global `POWER_GND` net and
  verified native KiCad ERC remains zero; the prior isolated V100 ground net
  could not support a valid board return plane.
- Added `phase14_power_route.py`, a disposable candidate generator with a
  broad protected-feed zone and filled inner return-reference planes, plus a
  machine-checkable Phase 14 candidate regression.
- Kept Phase 14 open: filled-zone geometry, current density, voltage drop,
  branch sharing, contact current, thermal margin, and hostile DRC evidence
  remain required before routing closure.

2026-08-30 — Phase 14 candidate artifact checkpoint

- Committed the generated `ACREAGE_POWER_PHASE14.kicad_pcb` alongside its
  deterministic generator and regression so the filled-zone candidate is
  reproducible from the validated materialized board.

2026-08-30 — Phase 14 power-return continuity verified

- Promoted the clean V100 return and dual 12 V input returns onto shared
  global `POWER_GND`; native netlist and Phase 5 regression now require J1.GND,
  both input headers, and both LM74700 grounds on that net.
- Refreshed the Phase 14 filled candidate after the return-net correction.

2026-08-30 — Phase 14 filled-copper analysis added

- Added geometry sampling of the filled V100 protected-feed polygon and
  conservative 1 oz copper current-density/sheet-resistance calculations.
- The candidate reports 99.5 mm sampled minimum span, 3.681 A/mm2 shared
  branch density, 8.31 A/mm2 worst continuous single-branch density, and 10.89 mV
  conservative drop bound; connector-contact, thermal, and full-board DRC
  closure remain open.

2026-08-30 — Phase 14 connector-contact bound added

- Added the balanced-feed contact calculation: 12.625 A per branch across 65
  empirical power contacts is 0.194 A/contact, below Amphenol's published
  0.45 A/contact rating. Continuity and current-sharing measurements remain
  required for final Phase 14 closure.

2026-08-30 — Phase 14 thermal bound added

- Added the CSD19536KCS datasheet 62 C/W junction-to-ambient bound to the
  geometry-backed power analysis. At 40 C ambient it estimates 66.7 C shared
  branch junction and 146.7 C single-branch fault junction, below 175 C; the
  result remains a test-board/design bound pending fabricated-board thermal
  and sustained-sharing measurements.

2026-08-30 — Phase 14 provisional branch-track rejection

- DRC caught provisional wide branch legs crossing adjacent fuse-holder,
  connector, CM5, and regulator pads in the acreage placement. Those tracks
  were removed; the candidate retains only the validated filled power/return
  zones and remains unrouted until a clearance-safe production placement is
  established.

2026-08-30 — Phase 14 canonical power-budget correction

- Rebased the Phase 14 geometry/contact/thermal analysis on the repository
  `design/FINAL_POWER_BUDGET.json` authority: 28.5 A continuous and 34.3 A
  peak across two 15 A branches.
- Balanced continuous operation estimates 14.25 A/branch, 0.219 A/contact,
  and 78.3 C FET junction at 40 C ambient. The 34.3 A single-branch case is
  explicitly a fuse-clearing transient, not a sustained thermal pass.

2026-08-30 — Phase 14 canonical-budget arithmetic corrected

- Corrected the machine analysis to the exact 1 oz geometry arithmetic:
  4.155 A/mm2 shared density, 8.309 A/mm2 continuous single-branch density,
  10.91 mV sheet-drop bound, and 74.0 C shared FET junction at 40 C ambient.
- The 236.9 C peak single-branch θJA result remains a fuse-clearing transient
  requirement, not an accepted sustained operating condition.

2026-08-30 — Phase 14 routing candidate held fail-closed

- A second B.Cu/ordinary-via routing experiment was rejected after native DRC
  showed pad/hole crossings and the KiCad Python ABI serialized two protected
  vias with the wrong hierarchical net. The canonical candidate is therefore
  zone-only with zero tracks/vias until a clearance-safe production placement
  and stable net-assignment path are available.

2026-08-30 — Phase 14 Molex land-pattern defect found

- Native DRC showed the local `0039300020` pattern's 3.0 mm mounting holes
  overlapping the 2.4 mm electrical-hole clearance envelope. The electrical
  MPN selection remains valid, but its local land pattern is reopened against
  the official Molex drawing and is excluded from routing/release authority.

2026-08-30 — Phase 14 Molex land-pattern authority corrected

- Replaced the incorrect horizontal 4.20 mm/two-peg local pattern with the
  Molex SD-5569-002 2-circuit component-side layout: pad 1 at (0,0), pad 2
  at (0,+5.50), and one NPTH retention peg at (0,-7.30); electrical and peg
  drills are 1.80 mm and 3.00 mm.
- Added a focused native DRC regression for J5/J6. Fresh materialization and
  routing-candidate DRC no longer report Molex self-hole or solder-mask bridge
  violations; the broader acreage candidate remains Phase 14-open.
- Corrected the local authority provenance to the exact MPN drawing
  `039300020_sd.pdf` / `55690002-SD` and forced the materializer to reload
  J5/J6 from the project-local footprint rather than stale donor geometry.

2026-08-30 — Phase 14 Littelfuse holder land-pattern gap found

- Native DRC exposed overlapping local geometry in the selected four-pin
  `178.6165.0001` holder footprint at F1/F2. The electrical selection remains
  valid, but the local pattern is reopened against Littelfuse `CVP-PE40-0006`.
- The manufacturer drawing's 5.8 mm and 3.5 mm hole-pattern dimensions are
  now recorded as the land-pattern authority; routing and release remain held
  until the local footprint is regenerated and independently checked.

2026-08-30 — Phase 14 Littelfuse holder geometry corrected

- Corrected the local `178.6165.0001` four-pin holder to the manufacturer
  `CVP-PE40-0006 Rev A` 5.8 mm by 3.5 mm hole rectangle with 1.4 mm drills.
- Materialization now assigns duplicated contacts 1/3 to each input net and
  2/4 to each fused-output net. Native DRC removes the holder self-overlap;
  external placement/courtyard interactions remain open.

2026-08-30 — Phase 14 Littelfuse eight-hole authority correction

- Independent exact-MPN review found that `178.6165.0001` is an eight-solder-hole
  FLR holder with a central mechanical spigot, not a four-hole pattern.
- Regenerated the local footprint at the manufacturer-derived coordinates with
  conservative central NPTH clearance; materialization maps pads 1-4 to input
  and 5-8 to fused output. Phase 14 remains open pending broader DRC and power
  validation.

2026-08-30 — Phase 14 power escape and mechanical correction

- Moved both ideal-diode MOSFETs outside the conservative V100 cooler
  reservation and kept the protected feed as a broad F.Cu corridor.
- Added a clearance-safe stepped B.Cu escape for J6 around its adjacent return
  contact and the CM5 service connector. Fresh native DRC has no power-route
  shorting item; broader regulator/control unrouted debt remains open.

2026-08-30 — Phase 14 power-path gate closed

- Frozen candidate passed current-density, voltage-drop, balanced branch,
  connector-contact, conservative thermal, no-single-neck, and focused native
  power DRC checks. The focused report has no power-path short, mask bridge,
  hole-clearance, or clearance defect.
- Closed Phase 14 for design purposes with `REV_A_EMPIRICAL_RISK` retained only
  for continuity of the public reverse-engineered 130/70 V100 contact map and
  later fabricated-board thermal/bring-up confirmation. Broader acreage DRC
  and unrouted control debt remain later validation work.

2026-08-30 — Phase 15 TPSM63606 package authority corrected

- TI RDL0020A layout review found the clean footprint had its PGND/thermal
  lands on the perimeter instead of using the four central pads 17-20.
- Promoted the datasheet-derived 1-16 perimeter plus four central thermal-land
  geometry into the clean namespace and added regression coverage. Regulator
  routing remains unstarted until the vendor-layout overlay is implemented.

2026-08-30 — Phase 15 first routing prototype rejected

- A straight-line fanout prototype was tested on an isolated Phase 15 board.
  Native DRC exposed real cross-net shorts from the long direct segments and
  compact placement; the prototype was deleted and no DRC relaxation was made.
- The Phase 14 artifact was regenerated against the corrected TPSM footprint;
  Phase 15 must restart with layer-aware local loops and deliberate return vias.

2026-08-30 — Phase 15 thermal-via base checkpoint

- Added four 0.50/0.30 mm ordinary through vias per TPSM63606, centered in
  the four TI RDL0020 central PGND lands, with same-net F.Cu links across the
  separate exposed lands.
- Native save/reload regression passes for all 12 exact `/REGULATORS/POWER_GND`
  vias. Fresh native DRC reports no thermal-via diameter, drill, annular,
  mask, short, or dangling-via defect; VIN/VOUT and control routing remain
  open, so Phase 15 is not closed.

2026-08-30 — Phase 15 pad-edge high-current escape checkpoint

- Added module-scoped VIN/VOUT pad-edge escapes for U3/U4 and the U5 VIN
  capacitor bank. The native focused regression passes with no shorting or
  crossing items and reduces the regulator-base unrouted count from 296 to
  280. Bootstrap, feedback, RT, PG, VCC_INTERNAL, and final thermal-margin
  evidence remain open; Phase 15 is not closed.

2026-08-30 — Phase 15 pad-edge authority correction

- Independent KiCad review found U3 VOUT was tied through the inward pad-8
  edge. Corrected the generator to select U3 pad 9 and compute the true pad
  edge from pad geometry; regression now asserts the two exact `(54.95,80.00)`
  edge starts and the native no-short/no-crossing result still passes.

2026-08-30 — Phase 15 U3 quiet-control island checkpoint

- Added U3 FB/RT/PG routing with eight deliberate ordinary through-via
  transitions and separated B.Cu corridors. Native DRC has no route-specific
  clearance, short, or crossing defect; the focused regression verifies 20
  total vias and 272 unrouted items. U4/U5 control routing and full Phase 15
  overlay/thermal closure remain open.

2026-08-30 — Phase 15 native regulator hierarchy association checkpoint

- Native KiCad XML proved the regulator child had been split from root
  `12V_PROTECTED`/`POWER_GND`, while all three internal VCC pins shared one
  child-local net. Added authoritative child global labels for the two power
  rails and isolated VCC as U3/U4/U5-specific internal nets.
- Preserved the native child serialization; the scaffold rebuild path had
  silently dropped support instances and was replaced with an idempotent
  native-format association repair. Headless materialization now requires a
  host-Xvfb native export before Flatpak pcbnew consumes the XML.
- Regenerated Phase 14/15 candidates. Native hierarchy, net-authority,
  materialization, power-route, thermal-via, and focused regulator escape
  regressions pass; power continuity now reaches the actual root nets.

2026-08-30 — Phase 15 separated U4/U5 control checkpoint

- The original U4/U5 10 mm placement left no clean package-side control
  corridor beside U7. A validated candidate separates the modules to
  `(200,105)` and `(225,105)`, with module-scoped support rows and separated
  ordinary through-via trunks.
- U4/U5 FB/RT/PG routing and U4 C18-to-VOUT compensation produce zero native
  clearance, shorting, or crossing findings; the focused regression verifies
  35 vias and 254 unrouted acreage items. U5 VOUT-bank routing, effective
  capacitance, thermal margin, and full Phase 15 closure remain open.

2026-08-30 — Phase 15 U5 output-bank routing checkpoint

- Added a deterministic 4x4 placement and In2.Cu feed for schematic-authority
  capacitors C26-C41 on U5's 1.1 V output. The route leaves the true right
  output land and avoids the existing FB control escape.
- Native DRC and the focused regression pass with zero clearance, shorting, or
  track-crossing findings; the candidate has 69 ordinary through vias, 18 on
  the output net, 28 on the PGND return, and 237 baseline unconnected acreage
  items. Effective
  capacitance, ground-return stitching, thermal margin, and vendor-layout
  overlay evidence remain open, so Phase 15 is not closed.

2026-08-30 — Phase 15 U5 output-return stitching checkpoint

- Added sixteen local PGND return vias for C26-C41, each just outside the
  authoritative capacitor ground land with a short F.Cu link to avoid native
  solder-mask bridges. The focused native regression passes with 69 total
  vias, 18 on VOUT, 28 on PGND, zero route-specific clearance/short/crossing
  findings, and 237 baseline unconnected acreage items.
- Effective-capacitance, thermal-margin, and three-rail TI overlay evidence
  remain open; this is not Phase 15 closure.

2026-08-30 — Phase 15 compact U5 output-bank refinement

- Moved the first three C26-C41 rows beside U5 and kept only the fourth row
  offset to clear the authoritative U5 PG support resistor. Native DRC and
  the focused regression pass with 69 vias, 237 baseline unrouted items, and
  no route-specific clearance, shorting, or crossing findings.
- The geometry is closer to TI's qualitative arrangement, but exact overlay,
  DC-bias evidence, and board-specific thermal proof remain open.

2026-08-30 — Phase 15 measured overlay checkpoint

- Added `phase15_overlay_measure.py` and measured native regulator-to-COUT
  maximum center distances of 7.4 mm (U3), 16.3 mm (U4), and 51.7 mm (U5).
- A tighter U5 vertical bank was rejected by native DRC because it entered U7
  pads; the passing candidate keeps the first three rows near U5 and records
  the fourth-row envelope as a Rev-A placement limitation. The PG support
  island is fixed at x=236 mm with a passing native route regression.

2026-08-30 — Phase 15 output-capacitor lifecycle correction

- Replaced the previous Murata output-capacitor MPN with active TDK
  `C3225X7R1C226M250AC`, a TI-listed 1210/22-uF/25-V/X7R part. Mouser's EOL
  flag for the Murata candidate made it unsuitable as Rev-A authority despite
  remaining stock; TDK distributor stock and active status are recorded in
  `TPSM63606_SUPPORT_AUTHORITY.md`.
- Native Phase 5 power audit and COUT regression pass. The 90% values remain
  nominal derating screens; ±20% tolerance screens are 31.7/47.5/253.4 uF,
  so exact DC-bias/tolerance closure remains explicitly open.

2026-08-30 — Phase 15 active-cap lifecycle and tolerance audit

- Confirmed the active TDK MPN in the native regulator sheet and corrected the
  Phase 15 receipt's stale 36-via wording to the validated 35-via result.
- The COUT regression now reports both nominal 90% derating and the separate
  ±20% tolerance screen, preventing the latter from being hidden by the
  nominal pass.

2026-08-30 — Phase 15 TDK voltage-field correction

- Corrected the active TDK `C3225X7R1C226M250AC` description from 25 V to its
  manufacturer-sheet value of 16 V (`1C` voltage code). Rail requirements are
  5/3.3/1.1 V, so the selected part remains electrically suitable; no MPN or
  footprint change was required.

2026-08-30 — Phase 15 local TDK authority receipt

- Added `TDK_C3225X7R1C226M250AC_AUTHORITY.md` with exact voltage/package
  fields, dated multi-distributor stock evidence, manufacturer-sheet
  provenance, and the explicit graphical-curve limitation.

2026-08-30 — Phase 15 TI EVM layout authority preserved

- Saved TI's public `TPSM63606EVM` user guide and `SLVRBI7` Altium/gerber
  archive locally under the power authority inventory, with SHA256 recorded
  for the archive. The EVM's four-layer/2-oz basis and 110-uF effective
  47-uF-capacitor example are explicitly kept separate from Rev-A claims.

2026-08-30 — Phase 15 generator lifecycle correction

- Updated `phase14_regulator_support_native.py` so native support-network
  regeneration emits the active TDK output-capacitor MPN rather than the
  rejected Murata candidate.
- Extended the Phase 5 audit to fail if the obsolete MPN returns to either
  the native regulator sheet or its authoring path.

2026-08-30 — Phase 15 receipt and COUT regression correction

- Corrected the regulator receipt's U4/U5/thermal-via count to the validated
  35-via checkpoint.
- Strengthened `phase15_capacitance_check.py` to require the exact native
  schematic reference sets C7/C8, C16/C17/C19, and C26-C41 before applying
  the derated effective-capacitance floor calculation.

2026-08-30 — Phase 15 thermal screening checkpoint

- Added `phase15_thermal_screen.py` using TI SLVSGB4B's conservative 33.1 C/W
  metric, 50 C ambient, the 90% design-envelope efficiency assumption, and
  the 125 C operating-junction limit. The calculated margins are 19.8/50.7/
  71.0 C for U3/U4/U5.
- This is a screening calculation against TI's reference thermal board, not
  proof for the JLC six-layer copper stack or fabricated Rev-A hardware;
  board-specific thermal closure remains empirical risk.

2026-08-30 — Phase 15 capacitor and TI-overlay evidence checkpoint

- Added `phase15_capacitance_check.py`, which machine-checks the native
  schematic's 2/3/16 output-capacitor counts and the documented 90% derated
  floors of 39.6/59.4/316.8 uF against TI's 30/50/300 uF minimums.
- Added `PHASE15_TI_LAYOUT_OVERLAY.md` to compare the three regulator
  candidates against TI SLVSGB4B pages 31-32. Thermal margin and exact
  geometric/DC-bias closure remain open; no Phase 15 pass is claimed.

2026-08-30 — Phase 15 EVM scale-reference evidence

- Recorded the measured TI EVM VOUT-capacitor reference (5.85 mm maximum
  regulator-to-capacitor-center distance) and the SHA256 of the retained
  official layout archive in the Phase 15 overlay and regulator receipt.
- Kept the imported EVM board disposable: it is measurement evidence only,
  not a Rev-A design artifact or a claim of geometric equivalence. The Rev-A
  U4/U5 placement exceptions and board-specific thermal/DC-bias risks remain
  open and explicit.

2026-08-30 — Phase 15 VOUT-land and pull-up connectivity correction

- Added explicit perimeter VOUT-land ties for U3, U4, and U5 after native
  DRC identified that duplicate TPSM63606 VOUT lands were not all connected.
- Connected the U4/U5 output pull-up returns to their local output copper and
  kept the U5 trunk-head through-via connected on both F.Cu and In2.Cu.
- Native final DRC now reports zero route crossings, shorts, dangling tracks,
  and dangling vias; focused regressions cover both VOUT-land associations.
  Phase 15 remains open only for switch-node, exact DC-bias, and
  board-specific thermal/reference-overlay closure.

2026-08-30 — Phase 15 switch-node containment audit

- Added a fail-closed board audit proving the TPSM63606 SW/CBOOT/RBOOT nets
  have no external copper or component pads in the final regulator candidate,
  consistent with TI's internal-bootstrap/default-slew guidance.
- A native no-connect serialization experiment was discarded after KiCad
  ERC did not associate the generated markers with the child pin endpoints;
  no speculative schematic change was retained.

2026-08-30 — Phase 15 regulator-routing gate closed

- Closed Phase 15 with the final native DRC and focused audits: zero route
  crossings, shorts, dangling tracks, or dangling vias; switch-node audit
  passes; output-land and pull-up connectivity is explicit.
- Classified only bounded Rev-A empirical risks: exact TDK DC-bias/temperature
  capacitance sum, constrained U4/U5 capacitor envelopes, and board-specific
  thermal response. No fabricated-hardware claim is made, and later routing
  must preserve the accepted regulator keepouts.

2026-08-30 — Phase 16 PCIe net-authority correction

- Added the generic five-link root authoring contract for direct PER0, REFCLK,
  and PERST connectivity; PET0 remains split across its two coupling capacitors.
- Corrected Phase 4 instance pin UUID generation so pin identities cannot alias
  the containing symbol UUID. Native KiCad export and the Phase 16 regression
  prove J7-to-SXM2 identity and preserve the PET0 split.

2026-08-30 — Phase 16 routing rejection and netlist regression hardening

- Rejected the first PCIe PCB candidate after native DRC found 422 violations,
  including signal crossings, pad-field shorts, and incorrect escape geometry.
- Strengthened the schematic authority regression from partial membership checks
  to exact direct-net node sets and exact PET0 capacitor-side separation.
- No invalid Phase 16 PCB candidate was retained; routing remains open and
  Phase 17 is not started.

2026-08-30 — Phase 16 PET0 source-side authority correction

- Linked CM5 PET0 source-side ports across the root to the V100 child while
  keeping C1/C2 as the only electrical breaks to the SXM2 endpoint.
- Regenerated the Phase 14/15 materialized candidates from the corrected
  netlist; exact netlist regression passes for all direct paths and both PET0
  source/endpoint sides.
- The attempted PCIe geometry remains rejected by native DRC; no Phase 16
  routing gate or later phase was claimed.

2026-08-30 — Phase 17 EDAC MagJack land-number authority correction

- Corrected the generic schematic-to-PCB materializer with the EDAC J2
  logical-pin-to-physical-pad 19-minus-pin map for all 18 contacts.
- Regenerated the Phase 16 baseline through the full required pipeline and
  verified MDI pairs on physical pads 18..11 plus center taps, LEDs, and
  shields with the native pcbnew ABI regression.

2026-08-30 — Phase 17 Ethernet routing candidate rejection

- Rejected perimeter and dogbone candidates under native DRC; the frozen
  Ethernet placement creates source-order permutations, existing power and
  regulator crossings, NPTH keepout conflicts, and ESD pad-field shorts.
- Phase 17 remains open with the no-improvised-maze gate intact; no invalid
  copper candidate was committed.

2026-09-03 — Published Phase 17 blocker report

- Added the readable repository-root `blocker.md` report and preserved the
  current rejected-route evidence for private GitHub review.

2026-09-03 — Phase 17 Ethernet placement-repair sprint

- Reopened Phase 11/12 only for Ethernet as authorized and tested nine compact
  CM5-adjacent arrangements plus a complete west-edge MagJack island.
- The best order-preserving U9/U6/J2 candidate still has native DRC-confirmed
  crossings/shorts at the J7 breakout, TPD4E004 pad fields, and J2 connector
  boundary; it was rejected and no invalid copper was accepted.
- Phase 17 remains the earliest failed gate. Phase 18+ work remains prohibited
  pending an Ethernet-local escape/package decision.

2026-09-03 — Phase 17 Ethernet ESD package unblocker

- Independent footprint review identified Littelfuse SP3019-04HTG as the
  preferred next disposable candidate: active SOT-23-6L gullwing, four
  separated signal pins, low published capacitance, and multi-distributor
  availability.
- Recorded manufacturer, lifecycle, package, and procurement evidence in
  `PHASE17_ETHERNET_ESD_REPLACEMENT_RESEARCH.md`; no clean schematic or
  production PCB promotion has occurred.
- A disposable SP3019 geometry trial was run through native KiCad DRC; it
  remains rejected with 335 violations and 238 unconnected items. Its
  datasheet-derived trial footprint is explicitly non-authoritative and was
  not promoted.
- The disposable trial project shell was checkpointed with its PCB and DRC
  report so the rejected experiment is reproducible.
- The SP3019 routing generator was refined to use pair-separated monotonic
  corridors; the resulting native trial still fails and remains disposable.

2026-09-03 — Independent Phase 17 SP3019 blocker correction

- Published the specialist finding that the prior SP3019 trial was malformed,
  not a proof of geometric impossibility: it lacked required via transitions,
  omitted TD0_P copper, floated ESD ground, and used an unverified impedance
  width.
- Updated `blocker.md` with the corrected bounded topology and the exact next
  experiment: authoritative land pattern, explicit ordinary vias, all eight
  pairs, 100 ohm stack calculation, and complete MagJack-side routing.

2026-09-03 — Phase 17 SP3019 authoritative fixture experiment

- Repaired the KiCad 10 Flatpak generator path to use native typed footprint
  copies and `FindPadByNumber`; the corrected manufacturer-footprint fixture
  now saves with both SP3019 instances and explicit pin-2 Ethernet ground.
- Preserved a reproducible J7/J2 disposable-fixture extraction helper and ran
  native DRC on the full eight-pair trial. The candidate remains open, with 96
  violations and 76 unconnected items, including real launch crossings/shorts
  and missing required via/dogbone transitions.
- Published the exact evidence and bounded continuation options in
  `blocker.md`. SP3019 was not promoted, the clean PCB/schematic was not
  changed, and Phase 18+ remains gated.

2026-09-03 — Phase 17 minimal Ethernet fixture isolation

- Added a reproducible disposable base extractor that preserves the
  authoritative J7 Ethernet pad coordinates and J2 launch while removing
  unrelated CM5 pads and prior acreage routing from the fixture.
- Re-ran the corrected SP3019 fixture against the isolated base. Native DRC
  narrowed the result to 65 violations and 21 unconnected items; the
  remaining failures are Ethernet-local routing/topology defects, not the
  prior malformed-footprint or unrelated-connector evidence.
- Kept SP3019 unpromoted and the clean PCB/schematic unchanged.

2026-09-03 — Phase 17 Ethernet fixture routing audit

- The isolated base was independently checked: the regenerated disposable J7
  copy contains exactly eight Ethernet source pads. This removes the stale
  unrelated-pad contamination from the earlier report.
- Independent high-speed review confirms the remaining failure is local
  topology: the trial has no ordinary F.Cu/B.Cu transitions, uses incorrect
  J2 upper-launch coordinates, and retains pair crossings/center-tap shorts.
- The next repair remains bounded to the disposable fixture: reorient the
  launch, use exact J2 coordinates, add symmetric through-via/dogbone and GND
  return transitions, then rerun native DRC and route metrics.

2026-09-03 — Phase 17 Ethernet reorientation experiment

- Tried a distinct disposable placement with relocated J7/J2 and separated
  F.Cu/B.Cu pair corridors. Native DRC recorded 105 violations and 4
  unconnected pads, including true J2-launch shorts/crossings and invalid
  transition geometry.
- Rejected this corridor construction without relaxing clearance or layer
  rules. SP3019 remains an open candidate; the clean board/schematic remain
  unchanged.

2026-09-03 — Phase 17 Ethernet explicit-transition correction

- Corrected the disposable through-via dimensions to the board's ordinary
  minimum (0.50 mm diameter, 0.30 mm drill) and reran native DRC.
- The resulting experiment recorded 86 violations and 4 unconnected pads.
  True source/via fanout and J2 support-pad shorts/crossings remain, so this
  route is rejected; no clearance or layer rule was weakened.

2026-09-03 — Phase 17 separated Ethernet placement experiment

- Tried a further disposable placement with J7/J2 separated on a large
  fixture, monotonic F.Cu/B.Cu pair groups, and explicit transitions. Native
  DRC improved to 74 violations and 4 unconnected pads.
- Rejected the experiment because genuine four-pair fanout/launch crossings
  and shorts remain. The clean PCB/schematic remain unchanged and SP3019 is
  not promoted.

2026-09-03 — Phase 17 current fixture audit checkpoint

- Re-audited the saved disposable PCB after the separated-placement trial:
  J7 has exactly eight Ethernet pads, U6/U9 have six pads each with explicit
  ground and NC pin 5, and all eight CM5 Ethernet nets are present.
- Native DRC remains 74 violations and 4 unconnected pads. This is preserved
  as failed fixture evidence only; no production promotion or later phase was
  started.

2026-09-03 — Phase 17 Ethernet return-path correction

- Joined the two external SP3019 ground-return vias with an ordinary B.Cu
  GND spine and reran native DRC. The fixture now has zero unconnected pads.
- Native DRC still reports 79 true pair crossings/shorts, so this remains a
  failed disposable experiment. SP3019 was not promoted and production files
  were not changed.

2026-09-03 — Phase 17 Ethernet source-fanout correction

- Moved the B.Cu source transitions onto separated external lanes and fixed
  the B.Cu segment construction. Native DRC now reports 0 unconnected pads
  and 76 remaining true crossings/shorts/clearance violations.
- The fixture remains failed and disposable; SP3019 was not promoted and the
  clean PCB/schematic remain unchanged.

2026-09-03 — Phase 17 TI ESDS304 alternative authority

- Added a project-local disposable `ESDS304DBVR` SOT-23 DBV footprint derived
  from TI DBV0005A mechanical and land-pattern data, with explicit mask,
  paste, and courtyard layers.
- Recorded TI's active-production status, pin map, Ethernet 1G application,
  capacitance, and passive topology in the ESD replacement research note.
- This is an alternative candidate only; no clean production asset was
  changed and no ESDS304 routing pass has been claimed.

2026-09-03 — Phase 17 ESDS304 endpoint alignment rerun

- Aligned the disposable generator to the corrected TI DBV0005A pad
  coordinates and regenerated the fixture.
- Native DRC reports 104 violations and 7 unconnected items. Rejected this
  route construction for true crossings/shorts and connector-launch defects.
- Kept ESDS304 unpromoted and the clean production assets unchanged.

2026-09-03 — Phase 17 ESDS304 large-acreage escape experiment

- Built a new disposable fixture with corrected TI DBV0005A geometry, remote
  ESD placement, separate F.Cu/B.Cu channels, ordinary transitions, local
  ground returns, and a dedicated J2 launch zone.
- Native DRC reports 92 violations and 8 unconnected items, including real
  shelf crossings, source/ESD interactions, connector-launch failures, and
  incomplete connectivity.
- Rejected the candidate and preserved the generator, PCB, and DRC report as
  evidence. No clean production asset was changed.

2026-09-03 — Phase 17 ESDS304 authority-only proof

- Added and ran a native KiCad machine-check for the corrected TI DBV0005A
  footprint and disposable U9/U6 mapping.
- Verified package pad positions/sizes, mask/paste layers, courtyard, all
  eight MDI nets, and explicit ETH_GND; the authority check passes.
- Kept routing open because the latest candidate still fails native DRC. No
  production asset was changed.

2026-09-03 — Phase 17 ESDS304 authority-note correction

- Corrected the research note's DBV0005A row-separation typo from 1.9 mm to
  the TI-authoritative 2.6 mm value. The machine-check and footprint already
  used the corrected geometry.

2026-09-03 — Phase 17 ESDS304 footprint-authority correction

- Specialist review found the disposable ESDS304 footprint did not match TI
  DBV0005A: its pads were distributed on the wrong sides and overlapped.
- Corrected the local footprint to the TI-authoritative 5-pad arrangement,
  dimensions, paste/mask, and expanded courtyard, then regenerated the
  disposable fixture.
- Fresh native DRC reports 100 violations and 11 unconnected items. Rejected
  the route construction as failed, while retaining ESDS304 as an electrically
  credible alternative. The result does not reject the part itself.
- Updated `blocker.md` to distinguish invalid prior evidence from the
  corrected negative routing result. Production assets remain untouched.

2026-09-03 — Phase 17 fallback ESD solution class

- Researched TI ESDS311DYFR as the next authorized alternative: active
  single-channel SOD-323, explicitly Ethernet 10/100/1000 capable, with a
  simple shunt topology and captured Mouser/Digi-Key availability.
- Recorded its higher 4.5 pF capacitance and eight-device assembly cost as
  reasons it remains fallback-only pending a disposable fixture.
- No production asset was changed.

2026-09-03 — Phase 17 ESDS311 disposable fixture

- Built the authorized eight-device TI ESDS311DYFR SOD-323 fallback fixture
  with explicit Ethernet nets, ground returns, ordinary transitions, and the
  EDAC connector launch.
- Corrected the initial SMD-to-B.Cu termination to use local F.Cu dogbones
  and ordinary vias at each line pad.
- Native DRC still reports 212 violations and 24 unconnected items. Rejected
  the fixture as a route construction; ESDS311 was not promoted and the clean
  board/schematic remained untouched.

2026-09-03 — Phase 17 final bounded disposition

- Completed the authorized disposable alternatives: SP3019, corrected
  ESDS304, and ESDS311, including separated placements and ordinary-via
  transition repairs.
- No candidate passed native DRC and complete connectivity. The common
  failure is the CM5/J7 to ESD to EDAC launch geometry under the frozen
  F.Cu/B.Cu-only contract, not missing package authority.
- Recorded three bounded user-controlled continuation options and the
  recommendation in `blocker.md`.
- No production asset was changed; Phase 18+ remains unopened.

2026-09-03 — Phase 17 BCM54210PE remap authority investigation

- Checked Broadcom BCM54210 public authority and official Raspberry Pi CM5IO
  Rev 2 wiring evidence before changing Ethernet mapping.
- Established a fail-closed remap boundary: intact differential pairs only,
  conditional complete-pair MDI/MDIX variants, conditional P/N inversion,
  and no individual-conductor mixing or unproven arbitrary permutation.
- Recorded the legal trial table and evidence limits in
  `PHASE17_BCM54210PE_REMAP_AUTHORITY.md`.
- No production asset was changed; Phase 17 routing remains open.

2026-09-03 — Phase 17 BCM54210PE remap closure boundary

- Verified the exact CM5 feature claim from Raspberry Pi: automatic MDI
  crossover, pair-skew correction, and pair-polarity correction.
- Compared it with the official CM5IO four-intact-pair, 1:1 MagJack wiring and
  Broadcom's public BCM54210 authority.
- Recorded that no exact-device public mapping table authorizes arbitrary
  four-pair PCB permutation; polarity remains an intact-pair operation and
  skew correction does not legalize copper crossings.
- Added the fail-closed candidate matrix and updated the GitHub-readable
  blocker report. No clean PCB/schematic or Phase 18+ artifact was changed.
- Distinguished Broadcom family-level lifecycle claims from the exact CM5
  `BCM54210PEB1KMLG` variant; captured the distributor-hosted EOL notice and
  retained the exact-device remap question as unresolved.
- Added independent specialist confirmation that only CM5IO-style 1:1 pair
  assignment is publicly authorized; recorded exact MOQ/LTB/LTS and authorized
  inventory evidence. No clean design asset changed.

2026-09-03 — Phase 17 official CM5IO Rev 2 CAD oracle extraction

- Downloaded the official Raspberry Pi “CM5 IO Board, revision 2, KiCAD
  files” archive and recorded its SHA-256 in the authority inventory.
- Inspected the native CM5IO schematic and PCB, extracting the exact U1/U2
  `TPD4EUSB30`, EDAC `A70-112-331N126`, CM5 pin map, orientations, positions,
  F.Cu 0.127 mm MDI routing, PoE tap support, LEDs, shields, and GND use.
- Added a generator and receipt for a disposable official Ethernet fixture;
  no production clean asset changed.
- Native DRC of the official source and exact-copy fixture reports zero
  unconnected items and no MDI crossing/short/dangling-via findings; warnings
  are limited to official POE spacing and library-configuration overrides.
- The initial isolated extractor hit a KiCad Flatpak SWIG track-container
  lifetime defect and was replaced by an exact-copy oracle fixture; no
  production asset changed.

2026-09-03 — Phase 17 official-oracle transplant boundary

- Independent native-CAD audit confirmed the official MagJack footprint is
  `TRJG0926HENL`, not the selected EDAC `A70-112-331N126`; mounting/shield
  hole dimensions differ and the donor footprint remains reference-only.
- Confirmed the official ESD value/BOM versus hidden sourcing/datasheet fields
  contain a material identity conflict; no guessed ESD promotion was made.
- Recorded that the official CM5IO topology is closed as a routing oracle but
  PiSXMe adaptation remains open pending separately-authorized EDAC/ESD
  footprint parity. No clean PCB/schematic was modified.

2026-09-03 — Published current Phase 17 oracle blocker report

- Updated the GitHub-readable blocker report from terminal-blocked wording to
  the recoverable official-oracle/transplant state.
- Preserved exact CM5IO source, native DRC, ESD metadata conflict, and
  MagJack land-pattern mismatch as the next bounded work boundary.
- No clean PCB/schematic or Phase 18+ artifact was changed.

2026-09-03 — Phase 17 CM5IO MDI transplant experiment

- Resolved the official CM5IO ESD value ambiguity to active TI
  `TPD4EUSB30DQAR` using current TI product/package authority and major
  distributor evidence; saved the Rev-G datasheet and SHA-256.
- Corrected the clean TPD4E004 symbol/net mapping to TI's actual 6-pin
  pinout and corrected the EDAC shield-pad representation in the authoring
  path; regenerated the disposable mapping candidate and passed native
  mapping parity.
- Rigidly transformed 189 official CM5IO MDI segments onto the PiSXMe CM5
  and EDAC physical contact coordinates. Focused regression passed; native
  DRC found no MDI crossings, shorts, dangling vias, or footprint errors.
- Rejected the first mixed support overlay because its improvised GND/CT/
  shield paths crossed MDI geometry. No production acreage asset or Phase 18+
  artifact was promoted.

2026-09-03 — Phase 17 official-support adaptation experiment

- Tested a common center-tap In2 island, local GND copper return islands,
  outer B.Cu shield return, and valid fixture outline around the passing MDI
  transplant.
- Native DRC rejected the detached-zone construction with 82 violations and
  13 unconnected support pads; the failed artifact is preserved as evidence.
- Kept the official complete CM5IO fixture as the passing support oracle and
  left the clean production PCB/schematic and Phase 18+ work unpromoted.

2026-09-03 — Phase 17 explicit support-fanout follow-up

- Replaced broad detached support zones with explicit same-net B.Cu
  center-tap fanout, compact GND islands, ordinary return vias, and an outer
  shield route.
- Reduced the adapted fixture to 18 native DRC violations and 7 unconnected
  support pads, but rejected it because the remaining support connections are
  not yet proven.
- Preserved the passing MDI result and did not promote clean production or
  Phase 18+ assets.

2026-09-03 — Phase 17 complete CM5IO-derived fixture

- Repaired the EDAC support fanout with explicit B.Cu center-tap routing,
  official local USON GND escape geometry, ordinary return vias, and an outer
  shield return.
- Native DRC reached 0 unconnected pads and no true short, crossing,
  hole-clearance, dangling-via, outline, silkscreen, or footprint errors;
  only documented warnings remain.
- Closed the disposable fixture gate while keeping the clean acreage
  promotion and Phase 18+ work gated pending production-path adaptation.

2026-09-03 — Phase 17 acreage EDAC-launch blocker

- Promoted the clean Ethernet ESD authoring path to active TI
  `TPD4EUSB30DQAR`; native netlist and focused pin mapping passed.
- Rejected blind application of the CM5IO disposable connector launch because
  its temporary common-tap/EDAC assignment does not match the authoritative
  EDAC A70-112-331N126 MDI groups and center-tap pads.
- Preserved the 628-violation diagnostic DRC and published the exact,
  recoverable EDAC-side launch adaptation boundary in `blocker.md`.
- Did not promote the clean acreage PCB or begin Phase 18+.

2026-09-03 — Phase 17 pin-accurate EDAC launch trial

- Built a narrower disposable fixture retaining the passing CM5IO
  CM5-to-ESD geometry while using the production EDAC MDI pad groups 1..8.
- Regenerated the connector-side 0.127 mm F.Cu launch at the actual EDAC pad
  coordinates and ran native KiCad DRC.
- Rejected the trial at 20 violations and 17 unconnected items, including
  pair crossings/shorts; preserved the report and kept production and later
  phases gated.

2026-09-03 — Phase 17 EDAC connector-side layer split trial

- Tried ordinary F.Cu-to-B.Cu transitions for TD1 and TD3 while retaining
  pair integrity and the approved layer contract.
- Reduced the launch-specific DRC count from 20 to 14, but retained two
  crossings, three net shorts, and 17 unconnected items; rejected the trial.
- Kept the CM5IO source/ESD oracle and all production/later-phase assets
  gated; the next experiment is the official MagJack comparison.

2026-09-03 — Phase 17 CM5IO/EDAC authority-alignment correction

- Rechecked the official CM5IO PCB U1/U2/U3 placement against the EDAC
  manufacturer land pattern and found that the official MDI pads are
  1,2,3,6,7,8,9,10, with center taps on 11..14.
- Corrected the clean alias map and aligned production references as U6
  carrying TD0/TD1 at the official right protector position and U9 carrying
  TD2/TD3 at the official left position.
- Regenerated the native schematic netlist and acreage footprint map; the
  Ethernet pin-mapping regression passed.
- Regenerated the CM5IO-derived fixture using the reference-aligned refs;
  native DRC and focused MDI regression passed again with zero unconnected
  pads and no MDI crossings/shorts.
- Isolated official MDI geometry into a serialized data snapshot after
  identifying a KiCad Python multi-board wrapper/net-assignment hazard. The
  full acreage candidate still contains unrelated floorplan DRC conflicts and
  remains unpromoted; Phase 18+ remains gated.

2026-09-03 — Phase 17 corrected acreage application diagnostic

- Applied all 189 CM5IO MDI vectors through a single-board geometry snapshot
  path after confirming KiCad Python multi-board net wrappers could collapse
  distinct nets.
- Corrected mapping regression passed; full-board DRC remained contaminated by
  the current floorplan, with 539 violations and 477 unconnected items,
  including Ethernet shorts against neighboring power/keepout geometry.
- Classified the remaining issue as a local Ethernet placement/floorplan
  blocker, preserved the dirty candidate, and kept Phase 18+ gated.

2026-09-03 — Phase 17 routed-ancestor restore boundary

- Exported 320 routed Phase 16 copper items by stable net name and restored
  them onto the corrected clean materialization before applying the official
  CM5IO Ethernet vectors.
- Native DRC remained invalid at 835 violations and 460 unconnected items;
  the evidence includes inherited Phase 16/acreage debt and Ethernet
  collisions with neighboring power/keepout geometry.
- Preserved the snapshot/export/restore scripts and kept Phase 17 open; no
  Phase 18+ work started.
