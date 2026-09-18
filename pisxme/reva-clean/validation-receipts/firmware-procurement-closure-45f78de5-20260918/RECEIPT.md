# Phase 24 Path-A firmware, provisioning, procurement, and lifecycle closure

- **Package:** `P24-FIRMWARE-PROCUREMENT-PROVENANCE-CLOSURE`
- **Assigned base:** `45f78de58ff43d3d074c62d95a973cbf4419a17d`
- **Reconciled current HEAD:** `95429738d7f3476a58fe687755c7a3d6e7c97a98` (later evidence-only commits changed no listed Path-A source inputs)
- **Result:** `CANDIDATE_READY — authority/provenance packet complete; prototype and release-time gates remain explicitly scoped`
- **Scope:** Path-A evidence only. No schematic/PCB/rule changes. RTL9210B Path B remains isolated and unpromoted.

## Decision and authority reconciliation

The records agree on the selected production implementation:

`CM5 USB 3 -> TI TUSB9261IPVP SATA bridge -> SATA selector -> TE M-key socket` and
`CM5 USB 3 -> JMicron JMS583-QHFA3A NVMe bridge -> selector -> the same socket`,
with the Path-A mode matrix and power-off isolation rules. The records do not
authorize RTL9210B-CG production integration.

| Record | Revision/source SHA-256 | Disposition |
|---|---|---|
| `PHASE24_DUAL_MODE_STORAGE_PIN_MATRIX.md` | `b6a9c520d68636a2d99904ccc9a1aa253d216bdff0eda7ce7e74468ba9711876` | Path-A selector/mode contract |
| `PHASE24_RTL9210B_PARALLEL_COMPARISON_V1560.md` | `2e1d3c3ee99bc14b1ef7304ca02890bfbab54065cac43a57231a4f92b5354c80` | Isolated comparison; Path A protected |
| `PHASE24_RTL9210B_QUALIFICATION.md` | `4a628b13bd27fbc95ac1f448d8a504c3bc236fe8b5631a75dc52e68a5be6cf25` | Path-B promotion gates open |
| `authority-inventory/rtl9210b/RTL9210B_PATHB_AUTHORITY.md` | `428f30154052ca89a7dbd166b38efcfa8e918874976a6307dc2efad00474645f` | Explicitly not production-CAD authority |
| `PHASE24_DUAL_MODE_STORAGE_PIN_MODE_MATRIX.md` | `5c548c24521f8debf43d99a71b7dff0b8459af599879a73742bf53a509e46da6` | Library mode/pin cross-reference |

The older `CONTINUE BOTH` language means continue an isolated Path-B
qualification experiment while protecting Path A. It is not a production
selection conflict. Path-B firmware, procurement, and programming evidence is
therefore `NOT_APPLICABLE` to the selected Path-A production acceptance.

## Exact component, firmware, and provisioning matrix

| Function | Exact selected identity | Technical/provenance result | Remaining disposition |
|---|---|---|---|
| SATA bridge U7 | TI `TUSB9261IPVP`, 64-pin PVP/HTQFP | **PASS:** identity, package, datasheet and implementation/DEMO guides; `SATA_BRIDGE_AUTHORITY.md` | **External evidence gap:** TI SLLC416 payload is export-gated and no lawful payload/hash is retained. **Prototype validation:** program SPI flash and validate on assembled hardware. |
| SATA firmware policy | TI `SLLC416`, `01.00.00.0M`, U1/U2 disabled | **PASS:** selected Rev-A baseline policy; `SLLC414`, `01.00.00.0E`, is the FlashBurner utility | **Open release record:** exact formatted-image hash, tool version, no-swap/polarity record, access/rights record, and programming receipt. No custom firmware is required by the design. |
| NVMe bridge U11 | JMicron `JMS583-QHFA3A`; JLC assembly identity `C25701682` | **PASS:** mask-ROM baseline and pin/package authority; optional SPI NVRAM is DNP and not a boot dependency | **Procurement/lifecycle gap:** captured JLC stock was zero and no authorized major-distributor source was verified. Obtain traceable prototype lot/suffix evidence. Future JMicron image rights are not a Rev-A dependency. |
| Selector U12 | TI `HD3SS6126RUAR`, package `RUA0042A` | **PASS:** exact technical identity and package authority | Release-time exact-MPN/lifecycle refresh; no firmware/programming requirement. The separate retained 0.40/0.50-mm package geometry issue remains owned by the library/geometry lane. |
| Selector U13 | TI `HD3SS3412RUAR`, package `RUA0042A` | **PASS:** exact technical identity and selector mode authority | Release-time exact-MPN/lifecycle refresh; no firmware/programming requirement. |
| Mode control U14 | TI `SN74LVC1G17DBVR` | **PASS:** technical identity and mode-control role | Final BOM/procurement refresh; no firmware/programming requirement. |
| M-key socket J3 | TE `1-2199230-4` | **PASS:** identity and application specification retained | Exact procurement/lot refresh and final land-pattern parity remain release/DFM evidence. |
| SXM2/J1 and power/protection cohort | Existing selected exact identities in authority inventory | **PASS:** outside this package's firmware scope | Their power, package, and fabrication gates remain with the owning queues. |

Authoritative source hashes:

- `authority-inventory/primary-docs/bridge/SATA_BRIDGE_AUTHORITY.md` — `87b1ba01924480d2c8dbbe086d02bc979a780f5355ec1243f89177fd3ddc2fc1`
- `authority-inventory/primary-docs/bridge/TUSB9261_FIRMWARE_RECEIPT.md` — `297154baa6ebfffd4230739081d0b5db5bc38c70d5b5712551ceee431731e04e`
- `authority-inventory/primary-docs/storage-upgrade/jms583/JMS583_DESIGN_AUTHORITY.md` — `5285cdf2e0e894970aee4565fe24d6f0d7b80b376bba6e51ceb58c3bd50f290a`
- `authority-inventory/PHASE2_PROCUREMENT_MATRIX.md` — `2a61e6ee31b9fc17cf4b812a2a20d62a61bb849745f5350b4c36962f5d7617d6`

## Configuration, mode, and authorization rules

1. U7 uses the TI default SLLC416 policy with U1/U2 disabled. SLLC414 is a
   programming utility, not the firmware image. No custom descriptor/GPIO
   behavior is required for Rev A.
2. U11 is factory mask-ROM (`JMS583-QHFA3A`); SPI NVRAM is optional/DNP and
   must not be treated as a boot prerequisite. No proprietary image is copied
   or promoted.
3. SATA/NVMe mode changes are power-off operations. The selected Path-A mode
   matrix remains the source of selector polarity, inactive-path isolation,
   M-key ownership, reset, clock-request, PEDET, and unused-lane behavior.
4. TI/JMicron documentation is retained under its stated terms. Export-gated
   TI payloads and any future JMicron image may be used only through lawful,
   authorized access; no repository artifact claims redistribution rights.
5. RTL9210B binaries/configurations remain isolated comparison evidence and
   cannot satisfy any Path-A firmware, procurement, or authorization row.

## Prototype versus release evidence

The current checkout contains no fabricated board and no programming run. The
following are intentionally **not claimed**:

- a TUSB9261 image hash or exact FlashBurner execution;
- a JMS583 prototype lot, authorized supply, or lifecycle guarantee;
- vendor authorization to redistribute gated/proprietary firmware;
- SATA/NVMe enumeration, UASP/BOT, discard/TRIM, reset, suspend/resume,
  cold-cycle, or long-duration I/O measurements;
- V100/SXM2 hardware operation.

Before prototype first power, the release record must retain the lawful image
or access reference, image/config hash, tool/version, SATA polarity/no-swap
configuration, and a bounded programming procedure. After hardware exists,
run the selected CM5 image and selected SSD through enumeration, UASP/BOT as
applicable, reset, suspend/resume, cold-cycle recovery, and only claimed
TRIM/discard behavior. Record commands, software/image identities, logs,
limits, and stop criteria. These are `REQUIRES PROTOTYPE VALIDATION` items,
not fabricated PASS claims.

At release, refresh exact MPN/suffix, lifecycle, authorized source, lot, and
assembly records for U7/U11/U12/U13/U14/J3 and other critical components.
The dated distributor snapshots in the procurement matrix are planning
provenance, not a purchase or reservation.

## Acceptance disposition

| Requirement | State | Reason |
|---|---|---|
| Path-A selection and Path-B exclusion | `PASS` | Five agreeing authority records; Path B isolated/unpromoted |
| Exact technical identities and baseline firmware policy | `PASS` | TI/JMicron/package records and hashes above |
| Firmware rights/provisioning release record | `UNPROVEN — external evidence gap` | TI download is export-gated; no payload/hash or rights record available in this checkout |
| Exact-MPN procurement/lifecycle release records | `UNPROVEN — release-time evidence` | Existing records are dated snapshots; no current purchase/lot was made |
| Fabricated-board storage behavior | `REQUIRES PROTOTYPE VALIDATION` | No hardware exists; no operation is claimed |
| RTL9210B Path-B production gate | `NOT_APPLICABLE` | Explicitly unpromoted alternative |

This packet satisfies the work-package completion criterion by making every
unavailable item explicit and assigning its correct disposition. It does not
turn those dispositions into a Phase 24 integrated-board PASS. The overall
`component_firmware_provenance`, `storage_mode_behavior`, and integrated
sequencing rows remain open until their own integrated or prototype evidence
exists.

## Reproduction

```sh
git -C /home/nyx/PiSXMe/pisxme/reva-clean rev-parse HEAD
sha256sum authority-inventory/primary-docs/bridge/SATA_BRIDGE_AUTHORITY.md \
  authority-inventory/primary-docs/bridge/TUSB9261_FIRMWARE_RECEIPT.md \
  authority-inventory/primary-docs/storage-upgrade/jms583/JMS583_DESIGN_AUTHORITY.md \
  authority-inventory/PHASE2_PROCUREMENT_MATRIX.md \
  PHASE24_DUAL_MODE_STORAGE_PIN_MATRIX.md \
  PHASE24_RTL9210B_PARALLEL_COMPARISON_V1560.md \
  PHASE24_RTL9210B_QUALIFICATION.md
```
