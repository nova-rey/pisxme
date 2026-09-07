# RTL9210B-CG firmware and programming matrix

Status: technical feasibility demonstrated; production provisioning remains
OPEN/HIGH.

## Evidence inventory

| Artifact | SHA-256 | What it proves | What it does not prove |
|---|---|---|---|
| `RTL9210B_v1.34.39.032625.bin` | `93fe6b1768bdf2de077aa68d9dc8142cbac7c8f8d6e5c48cacf5b573fabfdaef` | A binary labelled for the RTL9210B ecosystem is obtainable | Realtek authorization, exact silicon-lot compatibility, or redistribution rights |
| `RTL9210B_gd_v4.30.23.071922.bin` | `9ed12b703075abb1a606787b870078c1bb9663a6807eee2df408eb2b24d259cc` | A second firmware artifact exists | Same limitations; version/config compatibility is not established |
| `RTL9210B_CG.cfg` | `768701d44ca61fa6020aed23fb9a58d1c6493ae703c00fc4c0762be4da25b9ac` | CG-specific USB identity/config fields are documented in a usable text artifact | It is not a complete production configuration contract |
| `RTL9210B_CG_upqi.cfg` | `a1ac8986f276c5508cfe7fa7763b4558cb2e06dcfcd89ceaf83bea98e61e525a` | A real device-family configuration example exists | It is vendor/product-specific and must not be copied into PiSXMe |
| `RTL9210B_CG_SABRANT_EC-SNVE.cfg` | `e416c678da9a2ddeef56f0f120888afaeb32e24f36cb87b38d07611593c21b9d` | Another product-specific configuration example exists | It is not PiSXMe authority |

These files are retained from public/community sources named in
`authority-inventory/rtl9210b/README.md`; their hashes make later provenance
comparison possible. They are not licensed or approved for redistribution by
this repository.

## Required distinction

| Case | Evidence currently available | Status |
|---|---|---|
| A. Update an already-working enclosure | Community README/config/binary ecosystem and Windows updater references | Technically plausible; not tested here |
| B. Initially program a virgin RTL9210B on PiSXMe | No authorized, repeatable bare-chip SPI/programming procedure captured | OPEN/HIGH |
| C. Configure PiSXMe fixed USB + shared M-key SATA/NVMe behavior | PEDET/shared-lane technical evidence; no PiSXMe-specific production config | OPEN |
| D. Recover/unbrick a failed device | Community recovery/update references and SPI-flash access precedent | Plausible, but no controlled PiSXMe recovery run |
| E. Redistribute firmware/config in an open product | Public artifacts exist, but license/permission chain is not established | OPEN/HIGH |

The live public updater guidance narrows the technical conclusion: the
published flow is for a connected, already-working enclosure, uses a
Windows-only updater, and asks the operator to dump the existing device
configuration before flashing. It does not document programming a virgin
RTL9210B-CG plus blank SPI flash on a custom PCB. The SPI command description
in the retained Rev. 1.1 technical document proves that a standard serial
flash interface exists, but not the complete Realtek production image,
configuration contract, or provisioning authorization.

## Narrow experiment that can change the decision

Obtain a traceable RTL9210B-CG lot and Realtek/OEM-authorized image/config
package. Assemble a disposable board with an accessible SPI flash footprint and
test pads. Record chip marking, flash MPN, image/config hashes, programming
tool/version, USB descriptors, and SATA/NVMe mode behavior. Exercise empty
socket, reset, UASP/TRIM/SMART, sustained I/O, and recovery. Do not place any
community binary in the production repository or release artifacts without a
rights decision.
