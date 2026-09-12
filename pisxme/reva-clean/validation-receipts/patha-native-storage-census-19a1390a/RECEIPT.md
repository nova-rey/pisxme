# Phase 24 Path-A authority reconciliation and native storage census

Date: 2026-09-12
Base SHA: `19a1390a2bca36515b6cc1a08a9d5c0b7e6d88d8`
Selected integrated PCB: `pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
Canonical schematic: `pisxme/reva-clean/PiSXMe_RevA_Clean.kicad_sch`
Tool image: qualified `pisxme-kicad-light:v1`, KiCad 10.0.6

## Storage authority reconciliation

The four existing authority records were read from the committed base and
hashed. They agree on the following disposition:

- Path A is the protected/current production implementation:
  `CM5 USB -> HD3SS6126 -> TUSB9261/JMS583 -> HD3SS3412 -> one M-key socket`.
- RTL9210B Path B is an isolated, unpromoted alternative. Its production
  integration gate is disposed for this campaign; its isolated evidence is
  retained and no Path-B CAD is consumed here.
- Path A's selector, M-key contact ownership, mode-control, and JMS583 support
  obligations remain the applicable implementation contract. Route, physical
  connectivity, full DRC/ERC, mode-state, firmware, procurement, power/inrush,
  thermal, and hardware gates remain open where their receipts say so.

| Record | Revision | SHA-256 |
|---|---|---|
| `PHASE24_DUAL_MODE_STORAGE_PIN_MATRIX.md` | `a7d98223e7533cf94e28d4245c56255d8cdf5c63` | `b6a9c520d68636a2d99904ccc9a1aa253d216bdff0eda7ce7e74468ba9711876` |
| `PHASE24_RTL9210B_PARALLEL_COMPARISON_V1560.md` | `aa11e340d7f9e9c39dbf86a6197656bee06e16c4` | `2e1d3c3ee99bc14b1ef7304ca02890bfbab54065cac43a57231a4f92b5354c80` |
| `PHASE24_RTL9210B_QUALIFICATION.md` | `df206677fc2c42ff726ca4992359742a52ddbbed` | `4a628b13bd27bfc95af1f448d8a504c3bc236fe8b5631a75dc52e68a5be6cf25` |
| `authority-inventory/rtl9210b/RTL9210B_PATHB_AUTHORITY.md` | `8fc3b4edaf0f943e3f4962076289083130459c61` | `428f30154052ca89a7dbd166b38efcfa8e918874976a6307dc2efad00474645f` |

## Native census

Command:

```text
python3 phase24_patha_native_storage_census.py \
  PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb \
  validation-receipts/patha-native-storage-census-19a1390a/patha-native-storage-census.json
```

The native saved-board census covered 292 pads belonging to `U7/U11/U12/U13/U14/J3`.
It reports 26 required Path-A endpoint pairs: 11/11 JMS583 support and CM5
USB3 branches are connected; all four U7-to-capacitor SATA branches, all four
capacitor-to-U13 Port-B branches, all four U13-to-J3 shared-lane branches, and
both STORAGE_SEL plus AUTO_PEDET mode-control branches remain open in this
integrated baseline. The source-side JMS583 support pairs tested here are
connected. This is a route/open inventory, not a closure claim.

Fresh native DRC on the same PCB reports `433` violations and `499`
unconnected items, exits with violation code `5`, and retains the raw report
and stdout in this directory. The focused source schematic audit reports the
existing `J3 missing label M2_GND` finding; library and mode audits pass. No
rule severity was changed, expected edge was injected, or Path-B source was
used.

All retained files are covered by `SHA256SUMS`.
