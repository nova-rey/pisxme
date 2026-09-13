# P24-J1-CONTRACT authority packet

- Result: **CANDIDATE_READY**
- Base source commit: `c06876d2bb3c244d29ad04e883a253eefd35c265`
- Scope: J1 connector/footprint provenance and bounded contact contract. No CAD, routing, or net-assignment edits were made.
- Selected component: Amphenol/FCI `74221-101LF`.

## Mechanical correspondence

The request's “393 J1 pad identifiers” is reconciled explicitly: the selected PCB contains **400 physical J1 pads** in the A1–K40 convention; **7** are currently named product signal contacts, leaving **393** other physical contacts. The packet maps all 400, so seven contacts are not silently omitted.

The exact identifier set is `{A,B,C,D,E,F,G,H,J,K} x {1..40}`. The selected PCB block contains 400/400 unique identifiers and independently reproduces the expected 1.27-mm grid with maximum local-coordinate error **0.0 mm**. The retained reference crosscheck records 400/400 shared identifiers, zero coordinate mismatches, and identity transform `(x_local,y_local)=(x_reference,y_reference)` against the pinned Benchoff 74221 footprint (`4ce457338f36b60a55fcce5f77f4688807e2a13b3dccc3a82c739d4de33ad436`). This is a parser/coordinate result, not visual inference.

## Bounded contract result

| Class | Count | PiSXMe disposition |
|---|---:|---|
| 12-V contacts | 130 | `12V_PROTECTED`, all indexed power rows corroborated |
| Ground contacts | 170 | `POWER_GND`, all indexed ground set corroborated |
| Selected x1 PCIe data | 4 | A2/A3 and G1/G2, assigned to CM5/V100 lane 0 |
| REFCLK | 2 | E7/F7, assigned to CM5_REFCLK_P/N |
| PERST | 1 | E18, assigned to CM5_PERST |
| Unimplemented published PCIe contacts | 60 | remain unassigned for selected x1 product |
| Source-declared NC/project-unknown | 31 | remain no-net |
| Auxiliary/protection unknown | 2 | K18/K19 remain no-net |
| **Total** | **400** | exact physical matrix |

The selected x1 signal assignments match the indexed reference values: A2/A3 = PERp0/PERn0, G1/G2 = PETp0/PETn0, E7/F7 = REFCLK+/REFCLK-, and E18 = /PERST. The current PCB has no contract mismatch in this bounded set.

## Evidence and conflict disposition

Benchoff's article and KiCad implementation are one reverse-engineering family based on purchased-hardware probing; they are strong public precedent, not NVIDIA-official documentation. Amphenol/FCI product and Rev-W drawing evidence independently establish the 400-position 10x40, 1.27-mm, 4-mm-class connector and 0.45-A/contact rating, but do not assign SXM2 functions. CN108280004B corroborates use of FCI `74221-101LF` in an SXM2 test-board topology, but does not publish a contact map. The pinned Xiaoyu repository contains only a README at its recorded revision and supplies no usable independent map.

The 3890p/4090ovo implementation is retained as a low-confidence conflicting warning: it names a different `84740-002LF` plug and does not document connector orientation or source hardware, so it cannot override the selected map. No authoritative contact-level conflict was found for the bounded contract.

## Authority disposition

**SUFFICIENT_FOR_BOUNDED_J1_CONTRACT.** The existing authority record `authority-inventory/primary-docs/sxm2/SXM2_J1_AUTHORITY_REASSESSMENT_20260912.md` remains consistent. No schematic, footprint, or net correction is warranted. Preserve 31 NC/project-unknown contacts, K18/K19, and the 60 intentionally unimplemented PCIe contacts as no-net. Reuse this packet as scoped evidence; it does not prove fabricated-hardware behavior, undocumented V100 auxiliary semantics, power adequacy, procurement readiness, or full-board DRC/connectivity.

## Reproducibility inputs

See `J1_CONTRACT_AUTHORITY_PACKET.json` for all hashes, source revisions, and the complete 400-row machine-readable map in `J1_CONTACT_MAP.csv`. Key inputs include selected PCB SHA `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c`, project footprint SHA `d67e826c787d498b8459d51197d300904504ec3ace7c505fc08821d3c4d99305`, Library map SHA `e22be34f61e8a094fcaa5dea051f76d7ae1df3fef29d5b805f793134b0180ca2`, and retained crosscheck SHA `644ebd8750421d035db723c94f0ad32803a05957fc62c6f1c1d561bab6de2af0`.
