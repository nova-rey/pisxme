# Phase 24 component, firmware, programming, and provenance lane

Date: 2026-09-13  
Acceptance row: `component_firmware_provenance`  
Result: **OPEN — evidence sufficient for identity and baseline firmware policy;
release provisioning and procurement are not closed**  
CAD/architecture modified: **no**

## Scope and source state

This bounded review checked the private PiSXMe Library first and reconciled its
evidence against the current public project checkout. No broad external
research was commissioned because the existing Library brief and authority
records answer the Path-A selection and baseline firmware questions. The
private corpus is the `PiSXMe-Library` repository, current branch `Library`,
HEAD `b521af194da4e1455c776132e77f282f5247841c`; the task-specific brief is
`Library/briefs/pisxme-component-firmware-provenance-20260913.md` at commit
`ae9132d6072f1557a709f47c542fe3c6d9baac38`. Its source metadata and
cross-links are in `Library/provenance/sources.json` at the current Library
HEAD.

The public project was inspected at `nova-rey/pisxme` branch `reva-clean`,
HEAD `e1de060962b76eabcfd4e83612326c708bd80f4f`. The selected source files
have these hashes:

| Artifact | SHA-256 |
|---|---|
| `PiSXMe_RevA_Clean.kicad_sch` | `6eef63bd3d2b0b9fafc0150d3c34f636ce24a48b2ecbd3d28a5f0bfec167e9f1` |
| `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb` | `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c` |
| `PiSXMe_RevA_Clean.kicad_pro` | `ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356` |
| `PiSXMe_RevA_Clean.kicad_dru` | `38e5c7521d964bfa91ee610dc6b7ca39b767b04b8990e94ea91dfe826d21f6a3` |
| `PiSXMe_RevA_Clean.pretty/TUSB9261IPVP_HTQFP64.kicad_mod` | `46abdf12a23b9ae89285b9de9af0902eca43d1c1394296b59a7d16a3ff61d481` |
| `PiSXMe_RevA_Clean.pretty/JMS583_QFN64_8x8.kicad_mod` | `11918576998884d5885debb500966b20804f7d14394212379fad31d0e5669c05` |
| `PiSXMe_RevA_Clean.pretty/HD3SS6126_RUA0042A.kicad_mod` | `9490928521cf2d8677da7bf188fc265664095d99978ae7c1f038da07adf33ffd` |
| `PiSXMe_RevA_Clean.pretty/HD3SS3412_RUA0042A.kicad_mod` | `b08bbf124876cb5e121a83f9290548c234d4b062a315423532f2aac2036433e0` |
| `PiSXMe_RevA_Clean.pretty/SN74LVC1G17DBVR.kicad_mod` | `not present as a standalone file; PCB uses its embedded/local footprint` |

## Path-A authority and Path-B disposition

The selected implementation is Path A: `TUSB9261IPVP` SATA plus
`JMS583-QHFA3A` NVMe, with `HD3SS6126RUAR` / `HD3SS3412RUAR` selectors and
the TE M-key socket. The checked authority records agree on that protected
production baseline and do not authorize RTL9210B production integration:

| Record | Revision commit | SHA-256 | Finding |
|---|---|---|---|
| `PHASE24_DUAL_MODE_STORAGE_PIN_MATRIX.md` | `a7d98223` | `b6a9c520d68636a2d99904ccc9a1aa253d216bdff0eda7ce7e74468ba9711876` | Path-A selector/mode topology and support obligations |
| `PHASE24_RTL9210B_PARALLEL_COMPARISON_V1560.md` | `aa11e340` | `2e1d3c3ee99bc14b1ef7304ca02890bfbab54065cac43a57231a4f92b5354c80` | Path B is a protected, isolated comparison candidate |
| `PHASE24_RTL9210B_QUALIFICATION.md` | `df206677` | `4a628b13bd27bfc95af1f448d8a504c3bc236fe8b5631a75dc52e68a5be6cf25` | Path-B promotion gates remain open; Path A preserved |
| `authority-inventory/rtl9210b/RTL9210B_PATHB_AUTHORITY.md` | `8fc3b4ed` | `428f30154052ca89a7dbd166b38efcfa8e918874976a6307dc2efad00474645f` | Explicitly not production-CAD authority |
| `authority-inventory/PHASE2_AUTHORITY_INVENTORY.md` | `890c9c8e` | `290a9349cd94e034cfb5280c6e9a300cc4540b6199ebfcb1a8d4e39d439e8dbb` | SATA bridge selection is TUSB9261; JMS578/ASM1153E rejected |

The older phrase `CONTINUE BOTH` in the Path-B comparison means continue an
isolated qualification experiment while protecting Path A. It does not
conflict with the current campaign disposition that the Path-B production
integration gate is out of scope. Issue #2 and the current campaign state
therefore retain Path-B evidence without reopening architecture selection.

## Component and provisioning evidence

| Ref/function | Authority and exact revision | Current result |
|---|---|---|
| U7 SATA bridge | TI `TUSB9261IPVP`; `SATA_BRIDGE_AUTHORITY.md` and `TUSB9261_FIRMWARE_RECEIPT.md`, project revision `bd2862e9`; TI Rev-I datasheet `a67457f3c9349bdc2a3b9eabb5f63a3b25d033afc62669fe91f8370ffb67bdec`; implementation guide Rev-E `a2ebc049ab266a6a81cc4ea83b8d75118d3cf22476f22798b8135a69ad6dffa5`; DEMO guide `525f9d77d1984dcdb5ef43e66a0cedf95789fbf7fe72d9bc6d1bf19cd9b39007` | **Identity/technical authority PASS.** Rev-A policy is TI `SLLC416` (`01.00.00.0M`, 2018-09-03); `SLLC414` (`01.00.00.0E`, 2013-10-24) is the FlashBurner utility. The gated binary and a board programming run are absent. Formatted image hash, tool version, access/rights record, no-swap polarity record, and reproducible programming receipt remain OPEN. |
| U11 NVMe bridge | JMicron `JMS583-QHFA3A`; `JMS583_DESIGN_AUTHORITY.md`, project revision `6f14e511`; official PDB-18001 Rev 1.00 `c472cdcb93cc02eedcdb2e31256b48c95e601fe4a98b662ae627e6d695006824`; retained PDS-17001 Rev 2.1 `27a491efa2361a5b3363d61ebf43b0983ce0c2407a49a5e949a3ff9b83b88529` | **Identity/package and baseline firmware prerequisite PASS.** The selected suffix is a factory mask-ROM device; optional SPI NVRAM is DNP and not a boot dependency. Authorized prototype procurement, lifecycle/suffix confirmation, and any future JMicron image rights remain OPEN/HIGH. |
| U12 selector | TI `HD3SS6126RUAR`, SLAS975A / package RUA0042A; retained datasheet `ce9c29d4c051738737e76a24ca40202e926db58a8b4665581bf905a4bd11b2ee` | **Identity/technical package evidence PASS.** The retained 0.40-mm footprint versus TI's 0.50-mm package drawing is a separate live geometry conflict; procurement refresh and package resolution remain open in their owning rows. No firmware/programming required. |
| U13 selector | TI `HD3SS3412RUAR`, retained datasheet `4013014d39f23f4d4a42fe4f918e392339488542224ebb2cd67ecd536b14e0ef` | **Identity/technical package evidence PASS.** No firmware/programming required; exact procurement remains a release task. |
| U14 mode control | TI `SN74LVC1G17DBVR`, project mode matrix and TI datasheet `c76fa723fac4502423967a1aa087dd669106b52b8de620c024b26e56f5d59309` | **Technical identity PASS; final BOM/procurement and native mode behavior OPEN.** |
| J3 M-key socket | TE `1-2199230-4`, TE application specification Rev C and project `TE_MKEY_AUTHORITY.md` | **Identity evidence present.** Exact customer-CAD pad parity and current traceable procurement remain separate open gates. |
| J1 SXM2 receptacle | Amphenol/FCI `74221-101LF`, Rev-W manufacturer drawing/product record plus private SXM2 evidence | **Identity and bounded project contract present.** Reverse-engineered mapping is not NVIDIA authorization; procurement refresh and empirical V100 risk remain open. |
| Power/protection critical parts | Existing Microchip/TI/Molex/Littelfuse/CSD/TVS authority inventory | **Manufacturer/package basis present.** Exact values, lifecycle/lot traceability, current procurement, reference-layout compliance, and physical validation belong to their acceptance rows. |

## Procurement and firmware boundary

The exact TUSB9261 part has prior DigiKey/Mouser snapshots in the Phase 2
records; those are dated planning observations, not a current purchase or
reservation. JMS583 exact assembly identity `C25701682` is recorded but the
captured JLC stock was zero; broker listings are not authorized supply. The
selectors and connectors have dated distributor evidence, but the selected
BOM still needs a release-time exact-MPN/lifecycle/traceability refresh.

TI's E2E Flash Burner thread 538818 (`ti-e2e-tusb9261-flashburner-538818`,
retrieved 2026-09-13, Tier 2 manufacturer support guidance) establishes that
an EVM is not required for SPI programming, that raw SLLC416 lacks the
SPI-valid header, that SLLC414 formats the image, and that image SATA polarity
must match the board. It does not provide a PiSXMe formatted-image hash,
production authorization, or programming result. TI's download payloads are
export-gated and were not copied. No proprietary firmware or community
RTL9210B binaries were copied or promoted.

## Acceptance classification

`component_firmware_provenance` remains **OPEN** on the integrated candidate.
The evidence closes the selected Path-A identities, technical package/pin
authority, and baseline JMS583 mask-ROM policy. It does not close:

1. authorized JMS583 prototype procurement and suffix/lifecycle traceability;
2. TUSB9261 firmware download access/rights, formatted-image hash or lawful
   retrieval command, exact FlashBurner version, no-swap configuration, and a
   reproducible programming record;
3. release-time exact-MPN procurement/assembly records for critical parts; or
4. fabricated-hardware operation, Linux UASP/BOT/TRIM, suspend/resume, reset,
   cold-cycle, or vendor authorization.

These are genuine evidence gaps or release gates, not reasons to reselect
Path B and not waivers for the Phase 24 acceptance row. The lane can continue
independently while storage/power geometry is `WAITING_ON #2`.

## Reproduction commands and provenance

Commands used in this review:

```sh
git -C /home/nyx/PiSXMe/pisxme/reva-clean rev-parse HEAD
git -C /home/nyx/PiSXMe/pisxme/reva-clean log -1 --format='%H %cI %s' -- <path>
sha256sum <project-authority-or-component-file>
git -C /home/nyx/PiSXMe-Library rev-parse HEAD
git -C /home/nyx/PiSXMe-Library log -1 --format='%H %cI %s' -- <library-file>
```

All local hashes above are SHA-256 of files retained in the project or private
Library. External manufacturer and support material is represented by URL,
revision/date, extracted facts, and license/access disposition; restricted
firmware payloads are not redistributed. This receipt is evidence only and
does not assert a Phase 24 pass or fabricated-hardware proof.
