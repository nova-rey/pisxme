# Phase 24 RTL9210B-CG parallel implementation comparison — V1560

Date: 2026-09-10  
Scope: isolated Path B qualification; Path A remains protected.

## Decision

**CONTINUE BOTH pending a narrowly defined Path-B experiment.**

RTL9210B-CG is a genuine simplification candidate, not a rejected idea: one
controller can provide the fixed CM5 USB2/USB3 host connection and native
SATA-or-PCIe operation at one M-key socket. It is not yet production-CAD
authority. The current isolated route chain V1549–V1558 is rejected by native
DRC at the QFN source/transition field; this is route implementation evidence,
not a Path-A regression or an architectural rejection.

Path A remains the fallback/reference implementation and has not been changed:

```text
CM5 USB -> HD3SS6126 -> TUSB9261 SATA / JMS583 NVMe
          -> HD3SS3412 -> one M-key socket
```

Path B under evaluation is:

```text
CM5 USB2 + USB3 -> RTL9210B-CG -> one M-key socket
                      |\
                      | +-- SATA lane 0, native PEDET-selected mode
                      +---- PCIe lane 0 + REFCLK/PERST/CLKREQ
```

Mode changes remain power-off operations. Path B does not consume CM5 native
PCIe or a second CM5 USB host port.

## Evidence checked

The following saved audits were rerun on 2026-09-10 and passed:

```text
phase24_rtl9210b_authority_audit.py
phase24_rtl9210b_corroborating_support_audit.py
phase24_rtl9210b_m2_mapping_audit.py
phase24_rtl9210b_native_netlist_audit.py
phase24_rtl9210b_wip_hierarchy_conflict_audit.py
```

The first audit parsed 69 symbol pins and verified the local footprint is an
SMD 69-pad QFN with exposed pad 69. The native netlist and mapping audits
confirm the saved CAD is parseable and the corrected M-key contact mapping is
explicit. The WIP hierarchy audit detects and quarantines the community
source's reversed lane association; it is not silently reused.

Current route evidence is `PHASE24_RTL9210B_QFN_FIELD_BLOCKER.md` and the
V1549–V1558 receipts. The best source-field attempts still fail under the
approved ordinary-through-via, no-via-in-pad contract. No board rule was
weakened and no Path-A file was promoted or modified.

## Proposed signal and mode mapping

| RTL9210B-CG | Socket contact | Function | Status |
|---|---:|---|---|
| 68 TXOP / SATA_TXOP | 49 | PCIe PETp0 or SATA TX+ | technically corroborated |
| 67 TXON / SATA_TXON | 47 | PCIe PETn0 or SATA TX− | technically corroborated |
| 64 RXIP / SATA_RXIP | 43 | PCIe PERp0 or SATA RX− naming | technically corroborated; polarity must follow final application circuit |
| 65 RXIN / SATA_RXIN | 41 | PCIe PERn0 or SATA RX+ naming | technically corroborated; polarity must follow final application circuit |
| 61/62 | 55/53 | PCIe REFCLK P/N | open final AC-coupling/termination review |
| 14 | PERST# | endpoint reset | open timing/application review |
| 13 | CLKREQ# | endpoint clock request | open pull-up/unpowered-state review |
| 8 GPIO6/PEDET | 69 / CONFIG1 | SATA-versus-PCIe detection | technical function supported; exact empty-socket network open |
| 3 | local reset | active-low reset | support implementation open |
| 18/19/21/22/23/24 | local SPI flash | startup image/configuration | virgin programming open |

Pin 69 on the chip is the exposed ground pad. It is not M.2 contact 69.
The local package and matrix preserve that distinction.

The retained Rev. 1.1 technical document states that PEDET selects PCIe
(logic 1) versus SATA (logic 0), and that the controller supports USB2,
USB3, PCIe Gen1/2/3 x2, SATA Gen1/2/3, external SPI flash, and a 25-MHz
crystal. These are technical qualification facts. They do not by themselves
close the PiSXMe application circuit, firmware rights, or production release.

## Support-circuit qualification

Evidence supports the following required local blocks:

- USB2 D+/D− and USB3 TX/RX from CM5.
- 25-MHz crystal/reference network.
- external SPI flash with exposed programming access.
- active-low reset, RSET, VBUS/5-V input, internal 3.3-V/1.1-V regulator
  support, decoupling, and exposed-pad GND.
- PEDET/CONFIG1 mode input, PCIe REFCLK, PERST#, CLKREQ#, and ISOLATEB.
- single-lane M-key PCIe/SATA socket launch; lane 1 is not used by Rev A.

The saved community schematic and independent support-netlist extraction
corroborate this block, but the source is explicitly WIP. The exact final
support values/layout and nonselected-interface behavior remain OPEN until a
traceable application package or controlled hardware bring-up closes them.

## Firmware and programming ledger

| Question | Current state | Classification |
|---|---|---|
| Firmware/config artifacts exist | RTL9210B-specific binaries/configs are retained and hashed locally | CLOSED as ecosystem evidence |
| Update of an already-working enclosure | UTHSB_MPtool-style Windows flow is documented by the corroborating ecosystem | PLAUSIBLE, untested here |
| Initial programming of virgin bare chip | No authorized, repeatable PiSXMe procedure or image/config contract | OPEN / HIGH |
| Recovery | SPI flash access and CH341A-style recovery are corroborated | PLAUSIBLE, untested here |
| Redistribution | Rights for retained community binaries/configs are not established | OPEN / HIGH |
| Fixed-board SATA/NVMe auto-selection | PEDET/native mode behavior is technically supported | OPEN for final network, sequencing, and hardware validation |

The next discriminating experiment is narrow: obtain a traceable lot and an
authorized image/config/updater package; assemble an isolated QFN fixture with
accessible SPI flash, reset, and test points; record markings, flash MPN,
hashes, tool version, USB descriptors, and SATA/NVMe/empty/reset behavior.
Do not copy community firmware into production release artifacts without a
rights decision.

## Procurement snapshot

| Source | Evidence | Risk |
|---|---|---|
| JLC/LCSC C5143573 | Exact `RTL9210B-CG`, QFN-68, SMT/PCBA lead; current page does not expose reproducible stock depth, price, or lead time | MEDIUM/HIGH |
| OKmarts | Marketplace lead around US$21.88, stated 5–7 day dispatch and limited/MOQ language | HIGH; corroborating only |
| eBay Lons Micro | Marketplace lead around US$8.45, displayed >10 units | HIGH; lot/traceability unproven |
| DigiKey/Mouser/Arrow/Newark | No exact current authorized bare-chip source established in the saved review | HIGH |

No purchase was made. The part is physically obtainable as a prototype lead,
but an authorized, stable production source is not closed. The local footprint
was recreated rather than copied from the community footprint because the
community file carries incorrect `through_hole` metadata. Exact Realtek/OEM
land-pattern authorization remains an OPEN release gate.

## Apples-to-apples comparison

| Criterion | Path A: TUSB9261 + JMS583 + two selectors | Path B: RTL9210B-CG |
|---|---|---|
| Major bridge/switch ICs | 4 high-speed devices | 1 bridge |
| High-speed route topology | USB branch selection plus SATA/PCIe selection | One bridge-to-socket path |
| Storage acreage | Larger; multiple support islands | Smaller in principle; SPI/rail support still local |
| BOM/assembly | More packages and escapes | Fewer ICs, but QFN-68 and SPI flash |
| SATA performance | TUSB9261 path limited to SATA up to 3 Gb/s | SATA Gen3 capability in technical evidence; CM5 USB remains system bottleneck |
| Automatic mode | External selectors/control; validation burden higher | Native PEDET concept, firmware/application validation required |
| Documentation confidence | TI high; JMS583 detailed but supply/firmware gates remain | Technical PDF/CAD corroboration good; released authority weaker |
| Procurement | JMS583 stock risk; TI parts have better channel visibility | JLC plus marketplace leads; authorized supply not closed |
| Firmware risk | TUSB9261/JMS583 provisioning still needs closure | Highest: image/config rights and virgin programming |
| Validation burden | More switched states and bridges | Fewer signal paths, more firmware/unpowered-state risk |
| Productization | Conventional and easier to source/document | Potentially superior if Realtek/OEM provisioning is authorized |

## Risk ledger and gate

**Closed for technical comparison:** shared lane identity, PEDET concept,
USB2/USB3 function, package identity at corroborated level, M-key mapping
with WIP conflict quarantined, and Path-A preservation.

**Open:** complete ordinary-via source-field route; Realtek-authorized
package/land pattern; final support BOM/application circuit; exact empty and
inactive state behavior; SSD 3.3-V transient/thermal budget; traceable supply;
virgin programming; firmware rights; isolated and integrated native
ERC/DRC/connectivity; SATA/NVMe hardware bring-up.

**Rejected evidence:** V1549–V1558 route classes, the WIP reversed-lane CAD,
and the malformed community `through_hole` footprint. These remain useful
history and are not current TODOs.

## Recommendation and next action

Recommendation: **CONTINUE BOTH**, with Path A protected as fallback. Do not
destructively migrate Path A. Path B's next bounded experiment must change
the QFN fanout/land-pattern strategy within the approved fabrication contract
or obtain an authorized assembly/package drawing; repeated coordinate-only
via sweeps are not informative. In parallel, preserve Path A's live storage
repair work and do not treat its current native power-collector candidate as
accepted while it adds new SATA-field shorts/crossings.

This report is a qualification comparison, not a Phase 24 pass and not a
production-CAD promotion.

