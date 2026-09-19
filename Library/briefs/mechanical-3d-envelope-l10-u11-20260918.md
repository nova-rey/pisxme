# Mechanical 3D and service-envelope evidence — L10/U11/Y10/J1/J3/J8

- **Queue package:** `P24-MECHANICS-L10-U11-LOCAL-CORRECTION`
- **Role:** Librarian evidence packet; no CAD mutation
- **Retrieved:** 2026-09-18
- **Integrated candidate inspected:** `51e712ce4b794758ba48fa1f36fba48d2e83890e`
- **Selected PCB:** `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- **Selected PCB SHA-256:** `770e2cd43cf88f1d329d0623c890939f4ec4a2f0230552bbbadeacf32817683d`

## Finding

The private Library and current integrated receipt provide authoritative package
and 2D envelope evidence for U11, J1, and J3, plus project-derived 2D
placement evidence for all named references. They do **not** close the complete
3D/assembly/service acceptance row. L10 and Y10 have generic project values
rather than selected vendor MPNs and therefore have no authoritative body
height or mating model. J8 is a project-defined four-hole mode strap with no
selected connector/strap MPN or service contract. The V100 cooler/backplate
record intentionally closes only the Rev-A scope boundary; it does not prove
fit for a named cooler or backplate.

## Current geometry and model state

Values below are from the native `mech_audit.json` and current footprints. They
are project-derived evidence, not a substitute for package authority.

| Ref | Current identity and position | 2D evidence | 3D / height state | Mechanical disposition |
|---|---|---|---|---|
| L10 | `4.7uH`, `L_2520_6332Metric`, `(143.00,127.80)`, 0 deg | Footprint body/courtyard bbox `3.70 x 4.1036 mm`; F.CrtYd `[141.355,126.355]–[144.645,129.245]` | **UNPROVEN**; no selected MPN, datasheet, model, or max height | Keep local courtyard/placement evidence; package authority must identify the actual inductor or set a bounded prototype envelope before assembly closure |
| U11 | JMicron `JMS583-QHFA3A`, `JMS583_QFN64_8x8`, `(140.00,135.00)`, 0 deg | Body 8 x 8 mm; project footprint 64 signal pads + EP65, 0.400 mm pitch, EP 4.46 x 4.46 mm, courtyard 9.2 x 9.2 mm | **PARTIAL PASS**; PDS-17001 Rev 2.1 Figure 4 gives package height `A max 0.900 mm`, body D/E 8.000 mm, EP/terminal limits | Current 2D placement is valid for this package basis; EP stencil window, assembly/reflow/X-ray remain prototype DFM gates |
| Y10 | `25MHz +/-30ppm`, `Crystal_3225_4Pad`, `(138.20,126.40)`, 0 deg | Project footprint body/courtyard bbox `3.45 x 4.0536 mm`; F.CrtYd `[136.455,125.005]–[139.945,127.795]`; nominal footprint description 3.2 x 2.5 mm | **UNPROVEN**; JMS583 datasheet establishes 25 MHz, +/-30 ppm, ESR <=55 ohm, but not the selected crystal package or height; no MPN/model | Do not claim vertical clearance or assembly fit until the actual crystal MPN/package is selected and dimensioned |
| J1 | Amphenol/FCI `74221-101LF`, `(150.00,90.00)`, 0 deg | 400-pad A1–K40 footprint; project footprint bbox `67.05 x 27.59 mm`; F.CrtYd `67.09 x 27.63 mm`; 1.27 mm grid | **HEIGHT PASS / FULL MATING UNPROVEN**; manufacturer product/drawing authority gives 4.00 mm receptacle/mated stack; no local manufacturer 3D model; mated V100/cooler service envelope remains open | Connector identity, grid, and 2D envelope are established. Use 5.10 mm perimeter rework allowance and preserve the SXM2/cooler contract; do not assert named cooler or module fit |
| J3 | TE `1-2199230-4` 4.2H M-key, `(220.00,165.00)`, 0 deg | Current F.CrtYd `[218.955,159.455]–[250.545,170.545]`; footprint bbox `[208.825,157.5214]–[250.525,170.525]`; 67-position pad field and M.2 retention holes are present | **HEIGHT PASS / FULL CABLE-SSD UNPROVEN**; TE 114-115006 Rev C identifies 2199230 as 4.2H; exact customer 2D DXF is retained; no 3D model or complete SSD/cable assembly model | M.2 body/retention and connector height are bounded; mating, retention screw, SSD/cable bend, and service access need final assembly evidence |
| J8 | Project `MODE_JUMPER_1x04`, `(245.00,150.00)`, 0 deg; value `AUTO / FORCE SATA / FORCE NVMe` | 4.00 x 4.00 mm courtyard; 1.70 mm pads, 0.90 mm drills at +/-1.27 mm; through-hole | **UNPROVEN**; no selected header/strap MPN, mating housing, plug height, or service-access contract | Current J8 is a storage mode strap, not a UART connector. Older J8/UART notes are superseded for this board. Package/DFM authority must decide solder strap versus populated header and record access/clearance |

The local Light/Heavy evidence is retained in
`validation-receipts/l10-u11-3d-assembly-service-20260918/`: Heavy rendered
successfully with `pisxme-kicad-heavy:v1`, digest
`sha256:be9cfe7295fe16a3196cd45fa26fa3aa8acbd7e1121ab55504eb2fc5f2034a8e`,
but the board contains no models for L10, U11, Y10, J1, J3, or J8. The render
is a sanity check and does not close mating, height, cooler/backplate, or
service access.

## Authority and provenance

| Source ID | Publisher / revision | Local reference and SHA-256 | Useful facts / limits |
|---|---|---|---|
| `jms583-pds17001-rev2.1` | JMicron, PDS-17001 Rev 2.1, Figure 4 | `authority-inventory/primary-docs/storage-upgrade/jms583/JMS583-datasheet-rev2.1.pdf`; `27a491efa2361a5b3363d61ebf43b0983ce0c2407a49a5e949a3ff9b83b88529` | QFN64 8 x 8; A max 0.900 mm; 0.400 mm terminal pitch; EP/terminal dimensions; 25 MHz crystal electrical limits. Does not identify Y10's physical package or L10. |
| `pisxme-u11-u12-footprints-current-head` | PiSXMe project-derived package record | `PiSXMe_RevA_Clean.pretty/JMS583_QFN64_8x8.kicad_mod`; `11918576998884d5885debb500966b20804f7d14394212379fad31d0e5669c05` | Measured U11 footprint and courtyard; prototype land treatment remains DFM-scoped. |
| `amphenol-74221101lf-product` / `amphenol-74221-drawing-w` | Amphenol/FCI product page and released Rev W drawing | Metadata in private Library; drawing is remote-only because CDN returned 403 | Active 400 contacts, 10 x 40 at 1.27 mm, 4.00 mm receptacle/mated stack, 0.45 A/contact. Exact local manufacturer model is unavailable; current 2D pattern is project-derived and pad-by-pad contract is separately recorded. |
| `amphenol-gs-12-100-rev-r` / `amphenol-gs-20-033-rev-j` | FCI product and application specifications | Remote-only metadata; no local copyrighted copy | 74221/84740 4.0 mm pair; pad, mask, no-via, and approximately 5.10 mm rework guidance. These do not provide the V100 cooler or chassis envelope. |
| `sxm2-j1-project-footprint` | PiSXMe derived J1 footprint | `PiSXMe_RevA_Clean.pretty/PiSXMeRevAClean_SXM2_74221_101LF.kicad_mod`; `d67e826c787d498b8459d51197d300904504ec3ace7c505fc08821d3c4d99305` | 400-pad 40 x 10 pattern and project courtyard; not a redistributed manufacturer ECAD model. |
| `te-114-115006-rev-c` | TE, Application Specification 114-115006 Rev C, 04 Jan 2023 | `authority-inventory/primary-docs/storage-upgrade/connectors/te/TE-114-115006-application-spec-revC.pdf`; `3919d7af08573732ab864840b67a9a8520405a29e90d886ae5fef236d76586eb` | 2199230 is the 4.2H family; M.2 application, solder and module insertion/removal guidance; no complete mating cable model. |
| `te-1-2199230-4-customer-dxf` | TE customer 2D CAD, c-1-2199230-4-b3-2d | `authority-inventory/primary-docs/storage-upgrade/connectors/te/cad/TE-1-2199230-4-2d-dxf.zip`; `89ab400716590e16d7b43165ecb0e4e7835bb6b0b077d00ecca7c9af1150b787` (inner DXF `0f81aa94b47308e4775902dd6422150927e9c77a7489e71925b9a1b67338e371`) | Package/PCB drawing basis; exact local derived footprint hash `a370a3406738f21ec4c9724c16bdd98e24d5312845730f4300704df104b737c9`. No 3D model. |
| `v100-cooler-backplate-reva-contract` | PiSXMe mechanical authority, checked 2026-08-29 | `authority-inventory/primary-docs/mechanics/V100_COOLER_BACKPLATE_AUTHORITY.md`; `0e35f6adeea4af1a8b01c9b0dfc2a9b57c0ad91a045eee7e5fd732fe255e4797` | Closes Rev-A scope: cooler mounts to V100 module; no carrier-mounted cooler/backplate pattern or generic underside exclusion is authoritative. Does not prove fit for any named cooler. |
| `pisxme-mechanical-envelope-receipt` | PiSXMe native geometry evidence | `validation-receipts/l10-u11-3d-assembly-service-20260918/RECEIPT.json`; `8070073ee07643a9d3e618148e53846f28c6152ec09d3b250dd9dae9b42f7283` and `mech_audit.json`; `3aab7f076f08d6da0e897d3e8223655d2d56db29b7770470288b0ee3168ae54a` | Exact current placements, courtyards, board edge, and model absence; explicitly records 2D PASS and full 3D/assembly/service UNPROVEN. |
| `pisxme-m2-socket-authority` | TE/JAE/SATA-IO project authority set | JAE drawing `4b4ccf5359a38faf65b9b5eb9b1598d533dc3f57222727df58e573824480649b`; SATA-IO TP053 `9d419572e7fba7cf1c7b1207f38cae3c47c04210695293fb516c484b4fd09abf` | M.2 2280/B-key conventions and retention context; current selected J3 is TE M-key, so do not substitute JAE/B-key geometry. |

## Gap commission for Researcher

The Library search found no selected vendor part number for L10 or Y10 and no
selected connector/strap part number for J8. This is a bounded knowledge gap,
not permission to choose a substitute. Researcher should search the current
schematic/BOM history, private Library, retained reference implementations,
and manufacturer catalogs for exact project-intended MPNs and dimensioned
package drawings/models:

1. `MECH-3D-GAP-L10-Y10`: exact 4.7-uH inductor and 25-MHz +/-30-ppm crystal
   MPN, body dimensions, maximum height, and lawful 3D/2D source.
2. `MECH-3D-GAP-J8`: intended mode-strap hardware (solder link, pin header,
   or other part), mating/actuation envelope, and service-access requirement.

Researcher must return `NOT_FOUND` with search coverage if no exact project
selection exists. Generic 2520/3225 package names do not close these gaps.

## Acceptance disposition

- **2D local placement / courtyard / edge:** `PASS_FOR_LOCAL_CORRECTION` for
  L10/U11/Y10 and the named connector footprints at the inspected candidate.
- **U11 package height:** `PASS` to 0.900 mm maximum under PDS-17001 Rev 2.1;
  assembly paste/reflow/X-ray remains open.
- **J1 connector height/identity:** `PASS` for the 4.00 mm Amphenol contract;
  full mated V100/cooler/service envelope remains `UNPROVEN`.
- **J3 connector height/identity:** `PASS` for TE 4.2H and exact 2D customer
  drawing basis; SSD retention/cable bend/service remains `UNPROVEN`.
- **L10, Y10 package height and J8 mating/service:** `UNPROVEN`.
- **Complete `mechanical_3d_assembly_service` row:** **OPEN**. The evidence is
  sufficient to continue independent authority and implementation work, but
  not sufficient to close the row or claim Phase 24 acceptance.

No source CAD or restricted/vendor bytes were copied into the public repository;
this brief retains metadata, hashes for lawful local project/source material,
and links/references for remote-only material.
