# P24-POWER-CONNECTOR-QUALIFICATION-CLOSURE

Status: `CANDIDATE_READY_WITH_BOUNDED_OPEN_ASSEMBLY_QUALIFICATION`

Package: `P24-POWER-CONNECTOR-QUALIFICATION-CLOSURE`  
Base state: `b87bdeae87e9641bba7d0858ba69ae9d080239bb`  
CAD changed: **no**  
Prepared: `2026-09-14T00:02:31Z`

## Result

The exact Molex connector family, mating housing, terminal material/plating,
16-AWG applicability, and crimp acceptance contract are now established from
manufacturer records and the existing private Library. The remaining gaps are
product-specific assembly and protection qualification; they cannot be closed
from connector-family documents alone and are recorded with bounded resume
conditions below. This receipt does not claim fabricated-hardware or production
qualification.

Recommended exact assembly record for authority confirmation:

- PCB header: six Molex `0039300020` / `39-30-0020`, 5569 family, two positions
  per header; one 12-V contact and one return per header.
- Cable housing: six Molex `39012020` (`5557-02R`), dual-row 2-circuit,
  polarized, positive-lock, natural nylon receptacle.
- Female contacts: six pairs of Molex `39000080` (bag) or its manufacturer
  packaging alternative `39000079` (reel), 5556 series, 16-AWG, phosphor bronze,
  tin plated on mating and termination interfaces. Reel/bag is a procurement
  packaging choice, not an electrical alternative.
- Wire: 16-AWG stranded copper minimum, with insulation diameter compatible with
  the selected terminal/tooling range.

## Field disposition

| Field | State | Evidence / binding requirement | Remaining condition |
|---|---|---|---|
| Mating housing and family | `CLOSED_CONTRACT` | Molex `39012020`, series 5557, 2 circuits, 4.20-mm pitch, polarized and locking, `-40..105 °C`; Molex test summary names `39012020` as the 2-circuit receptacle tested with 5569 family | Package Authority should record the exact part in the final BOM |
| Terminal plating/material | `CLOSED_CONTRACT` | Molex `39000080`: phosphor bronze, tin/tin, 0.889-µm mating and 0.914-µm termination minimums, 16 AWG; `39000079` is the reel packaging alternative | Confirm procurement package (bag or reel) in the BOM |
| Crimp tooling and acceptance | `CLOSED_REQUIREMENT` | Molex `ATS-638190900-001`, tool `63819-0900`, covers 5556 16 AWG and lists `39-00-0080`/`39-00-0079`; IPC/WHMA-A-620 Class 2. For 16 AWG: 3.00--3.30-mm strip, 1.06--1.16-mm conductor crimp height, 1.92-mm reference width, 2.82-mm insulation height, 2.89-mm reference width, 68.5-N minimum pull force | Assembly lot must produce inspection/pull-test records; no lot exists in this design repo |
| Harness length and loop resistance | `OPEN_ASSEMBLY_QUALIFICATION` | V2.2 authority requires 16 AWG minimum and `R_loop <= 20 mOhm` for each complete wire loop; Molex requires application derating for wire length, wire construction and crimp quality | Select/record exact cable part or one-way length and measure/derive hot loop resistance at declared operating temperature. Resume when a signed harness schedule and six loop measurements/calculations are attached |
| Fuse I2t coordination | `OPEN_AUTHORITY_DEPENDENCY` | Existing `0297015.U` is a 15-A, 32-V MINI fuse with typical melting I2t 270 A2s and 4.58-mOhm cold resistance; this is legacy/provisional evidence and is not sufficient to qualify the six independently limited branches | Power Authority must select the active 6.4-A limiter and coordinate fuse I2t, limiter fault time/SOA, harness and connector withstand. Resume on an authority packet naming exact MPNs and worst-case coordination |
| Ambient and airflow installation | `OPEN_THERMAL_QUALIFICATION` | Molex family requirements use +30 °C maximum rise over ambient and require derating for ambient, PCB copper, adjacent heating and wire length; housing operating range is `-40..105 °C` | Thermal/Power Authority must declare PiSXMe ambient/airflow class and produce six-header/contact/limiter temperature margins on the selected installation |
| Six-header installation | `OPEN_MPA_THERMAL_DEPENDENCY` | 5569 is a through-hole right-angle header family; the selected exact local pattern and six-loop source references are governed by the MPA/source-contract workstream | MPA must bind six nonconflicting positions/orientations, solder/assembly access, spacing and protected corridors; thermal authority then validates the resulting installation |
| Source provenance | `CLOSED_WITH_PROVENANCE_CONDITION` | Private Library brief `molex-5556-ps004-v21-20260913.md`, Library commit `c27ee33f`, preserves Molex `PS-5556-004-001` Rev B1, ECM 851282, dated 2026-03-24 and URL | Exact public PDF byte hash remains unavailable because direct NYX fetch was non-equivalent; no substitute hash is claimed |

## Why the remaining gaps are irreducible here

The connector manufacturer specifies family limits and test methods, but does
not select PiSXMe's cable routing length, ambient/airflow installation, six
header placement, or coordination with a future active limiter. The exact
current-limiter package is separately waiting on Power Authority. Assigning
those values here would silently promote implementation assumptions into a
power contract. The existing V2.2 `20 mOhm` loop-resistance ceiling remains
binding; only the actual assembly that satisfies it is unqualified.

## Resume conditions

1. **Package Authority / harness owner:** select the six identical 16-AWG
   harness branches, record wire insulation/part, one-way length and complete
   loop-resistance budget at operating temperature, and attach six measured or
   conservatively calculated values below `20 mOhm`.
2. **Power Authority:** name the active current limiter for A--F, state its
   worst-case current limit and fault timing, and coordinate it with the exact
   fuse/holder or replace the legacy 15-A fuse contract. No passive sharing.
3. **MPA + Thermal Authority:** bind six source/header placements and declare
   ambient/airflow, then demonstrate connector, solder, copper, harness and
   protection temperature margins.
4. After those records return, Root may clear the connector qualification
   dependency and proceed to the single isolated source/PCB producer. No CAD
   edits are authorized by this receipt.

## Source register

- Private Library brief and provenance: `PiSXMe-Library/Library/briefs/molex-5556-ps004-v21-20260913.md`, Library commit `c27ee33f`.
- Molex `39012020` product record: https://www.molex.com/en-us/products/part-detail/39012020
- Molex `39000080` product record: https://www.molex.com/en-us/products/part-detail/39000080
- Molex 5556 product specification `PS-5556-001-001`: https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/productspecificationpdf/555/5556/PS-5556-001-001.pdf?inline=
- Molex 5556 application tooling `ATS-638190900-001`: https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/applicationtoolingspecificationpdf/638/63819/ATS-638190900-001.pdf?inline=
- Molex dual-wire test summary `55560010-TS-000`: https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/testsummarypdf/555/5556/55560010-TS-000.pdf
- Molex 5569 drawing family: https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/salesdrawingpdf/556/5569/039303045_sd.pdf
- Littelfuse 0297015 authority record: `authority-inventory/primary-docs/power/LITTELFUSE_0297015U_17861650001_AUTHORITY.md`; exact product URL and distributor I2t record are retained there.
- Internal six-loop authority: `validation-receipts/power-envelope-authority-redesign-20260914/POWER_ENVELOPE_AUTHORITY_V2.2_CANDIDATE.json`.

No restricted reference files were copied into the public development repo.
