# Nine-branch Molex source schematic contract

- **Package:** `P24-POWER-INPUT-NINE-BRANCH-SCHEMATIC-CONTRACT`
- **Decision:** `PISXME-P24-NINE-BRANCH-SCHEMATIC-20260918` revision 1.0
- **Base:** `369b28f67dfb371589a73e8eda1e5dc166eedb3b`
- **Status:** `BINDING_SOURCE_TO_PRODUCER_WITH_VALIDATION_GATES`
- **Canonical CAD changed:** no
- **Signed authority:** Nine-Branch Power Contract Authority under the signed Product/Power source-bus and Molex V2 decisions, 2026-09-18

## Decision

The approved three-header Molex architecture is materialized as nine named positive/return contact-pair branches. Each branch has one positive-series Littelfuse fuse for independent fault isolation. The fuse is not treated as a 5 A current regulator; the 4.444 A continuous and 5.000 A/100 ms values are per-contact design screens, and the 7 A Molex loaded-circuit screen plus measured balance/thermal evidence governs. A single fuse per connector remains rejected.

After the nine fuse outputs join, the candidate uses one common ordinary protection cohort: existing U1/Q1/D1/C3 (`LM74700QDBVRQ1`, `CSD19536KCS`, `SMBJ18A`, `100 nF`) may be reused subject to the complete hot-path and SOA/thermal gates. Existing U2/Q2/D2/C4 are not credited as a parallel second common stage. This contract authorizes producer evaluation and exact connectivity; it does not claim the 10 mOhm path, thermal, surge, or hardware gates pass.

## Branch identity contract

The three headers are reserved as J5, J6, and J9 because J7/J8 are assigned elsewhere. For each header, pads 1–3 are the positive contacts and pads 4–6 are the return contacts in the pin-1 orientation of the audited `Molex_5569-06A2_2x03_P4.20mm_Horizontal` footprint. Harness continuity must verify this assignment before hardware operation.

| Branch | Pair | Positive net | Return net | Fused positive | Fuse | Target continuous / peak | Contact screen |
|---|---|---|---|---|---|---:|---:|
| `B1` | `J5.1 ↔ J5.4` | `PWR_SRC_J5_P1` | `PWR_RET_J5_P4` | `PWR_FUSED_J5_P1` | `F1` | 4.444 / 5.000 A | ≤7.000 A |
| `B2` | `J5.2 ↔ J5.5` | `PWR_SRC_J5_P2` | `PWR_RET_J5_P5` | `PWR_FUSED_J5_P2` | `F2` | 4.444 / 5.000 A | ≤7.000 A |
| `B3` | `J5.3 ↔ J5.6` | `PWR_SRC_J5_P3` | `PWR_RET_J5_P6` | `PWR_FUSED_J5_P3` | `F3` | 4.444 / 5.000 A | ≤7.000 A |
| `B4` | `J6.1 ↔ J6.4` | `PWR_SRC_J6_P1` | `PWR_RET_J6_P4` | `PWR_FUSED_J6_P1` | `F4` | 4.444 / 5.000 A | ≤7.000 A |
| `B5` | `J6.2 ↔ J6.5` | `PWR_SRC_J6_P2` | `PWR_RET_J6_P5` | `PWR_FUSED_J6_P2` | `F5` | 4.444 / 5.000 A | ≤7.000 A |
| `B6` | `J6.3 ↔ J6.6` | `PWR_SRC_J6_P3` | `PWR_RET_J6_P6` | `PWR_FUSED_J6_P3` | `F6` | 4.444 / 5.000 A | ≤7.000 A |
| `B7` | `J9.1 ↔ J9.4` | `PWR_SRC_J9_P1` | `PWR_RET_J9_P4` | `PWR_FUSED_J9_P1` | `F7` | 4.444 / 5.000 A | ≤7.000 A |
| `B8` | `J9.2 ↔ J9.5` | `PWR_SRC_J9_P2` | `PWR_RET_J9_P5` | `PWR_FUSED_J9_P2` | `F8` | 4.444 / 5.000 A | ≤7.000 A |
| `B9` | `J9.3 ↔ J9.6` | `PWR_SRC_J9_P3` | `PWR_RET_J9_P6` | `PWR_FUSED_J9_P3` | `F9` | 4.444 / 5.000 A | ≤7.000 A |

## Protection and joins

Each `F1`–`F9` is Littelfuse `0297015.U`, 15 A / 32 VDC MINI 297 fast-blow, in holder `178.6165.0001` using the authorized project footprint `PiSXMeRevAClean:ATO_FuseHolder_17861650001`. The retained source record gives a typical 308 A²s I²t; exact fault clearing, holder/contact rise, copper withstand, harness inductance and installed thermal behavior remain validation gates.

The positive sequence is:

```text
header positive pad → branch source net → one branch fuse → fused positive net
→ 12V_BRANCH_JOIN → SMBJ18A TVS / LM74700QDBVRQ1 + CSD19536KCS
→ 12V_PROTECTED → authority-mapped J1 +12V field
```

The return sequence is:

```text
header return pad → distinct branch return net → POWER_RETURN_JOIN
→ POWER_GND → authority-mapped J1 GND field
```

The source window is 11.4–12.6 V, with 40 A continuous and 45 A for 100 ms. The protected bus is bounded to 11.05 V sustained / 11.00 V peak and 12.60 V maximum. The complete source-to-J1 positive-plus-return path remains ≤10.0 mΩ hot, with the existing 4.0/2.0/2.5/1.5 mΩ allocation. No N−1 or passive-sharing credit is allowed.

## Ownership and release

`POWER_INPUT.kicad_sch` is owned by the isolated `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`; this package makes no canonical edits. The producer may implement only this branch/net/component contract and return a candidate with a fresh native netlist, ERC/DRC, complete path extraction and hashes. Root owns serialized integration. Product/Power Authority must review any deviation, especially a replacement common protection stage, branch-reference change, or new active fault monitor.

Prototype validation is still required for harness/crimp identity, branch balance, 40 A continuous operation, 45 A/100 ms behavior, fuse I²t/thermal action, common FET/TVS SOA, path resistance, protection shutdown, and V100 sequencing. No fabricated measurement or production qualification is claimed.

## Evidence

- Molex V2 architecture: `132bd0c98b1b71379712112f764baef147064edb490893be81d40c5bd4e89770`
- Audited 2x3 footprint candidate: `014a8f9b4ad6a1583aec43a5c0fb2a603e305970adf463eea26cd6afa54c7051`
- Signed source-bus contract: `8060e16a6b08ce4e571a6d9cd93b9fa8fe39e0cb43ebf96a705f062c61110614`
- Littelfuse authority: `d2e617125ae28bef0e977f69211e3c5a08eabce184f172b91e5d4bc20fcab389`
- Existing canonical source before producer work: `075ae680e3754e06bf995739db15cf30774432f8cf9fb487b5df20b3034c286b`

**Result:** `CANDIDATE_READY_WITH_REQUIRES_PROTOTYPE_VALIDATION`.
