# Mechanical 3D gap follow-up — L10/Y10/J8/cooler

- **Queue package:** `P24-MECHANICS-L10-U11-LOCAL-CORRECTION`
- **Knowledge dependency:** `knowledge:P24-MECHANICAL-3D-MODEL-ENVELOPES`
- **Retrieved:** 2026-09-18
- **Role:** Librarian bounded external-evidence follow-up; no CAD mutation
- **Basis candidate:** `51e712ce4b794758ba48fa1f36fba48d2e83890e`

## Result

The bounded search materially narrows the L10 and Y10 gaps. It does not
authorize a component selection or close the complete 3D/assembly/service row.
J8 is narrowed to a 2.54-mm four-position strap/header decision. The cooler
search found no authoritative named carrier-mounted cooler or backplate
contract; the existing Rev-A module-mounted cooler boundary remains the
applicable project authority.

## L10 — narrowed to a package-authority check

The JMicron JMS583 reference-board material identifies the 4.7-uH input
inductor as `GNR2512PA-4R7M / 1.7A@Imax /NM` (secondary web mirror of a
JMicron-authored reference drawing; no reference CAD copied). GOTREND's
released `GNR-SERIES-AE-V1R1` manufacturer document identifies the
`GNR2512PA-4R7` family as 4.70 uH, M tolerance, 2.20 x 2.70 mm maximum body,
1.20 mm maximum height, 1.700 A typical saturation current, 1.500 A typical
40-C-rise current, and 240 mOhm maximum DCR. The current PiSXMe local footprint
is a generic two-pad 3.2 x 2.8 mm courtyard with no selected MPN; its pad
pattern has not been mechanically overlaid against GOTREND's land dimensions.

**Disposition:** `NARROWED_CANDIDATE_FOUND`; package/footprint authority must
compare the current pads and courtyard with the released drawing and either
promote `GNR2512PA-4R7M` as the intended candidate or retain L10 as generic.
No schematic or PCB edit is authorized by this evidence.

## Y10 — narrowed to compatible manufacturer candidates

The JMS583 reference drawing specifies a 25-MHz crystal with 10-pF load
capacitance. ECS's released ECX-32 material lists
`ECS-250-10-33-JGN-TR` as a 3.20 x 2.50 mm, 4-pad, 25-MHz crystal with
20-ppm tolerance, 30-ppm stability, 10-pF load capacitance, and 40-ohm ESR.
Those values are compatible with the current JMS583 electrical screen
(25 MHz, +/-30 ppm, ESR <=55 ohm), subject to the actual oscillator load
calculation and package pin mapping. The current Y10 remains generic
(`25MHz +/-30ppm`) and has no selected MPN. The historical `Y1`
`ECS-400-18-33-JGN-TR3` record is explicitly rejected as a Y10 source: the
manufacturer identifies it as a 40-MHz part, despite sharing the 3225 family.

**Disposition:** `NARROWED_CANDIDATE_FOUND`; package authority must select the
exact ECS variant or another equivalent, verify pad numbering and load
capacitance, and record its body height/model. The current generic footprint
does not close the row by itself.

## J8 — mechanical function narrowed, service contract remains open

The retained JMicron reference drawing uses a `DIP-2.54-1X4 /NM` four-position
header footprint for UART. This corroborates the current J8 four-position
2.54-mm through-hole pitch, but it is not evidence that PiSXMe's current J8
storage-mode strap requires a populated connector. The current J8 value is
`AUTO / FORCE SATA / FORCE NVMe`; its selected header/strap MPN, population
state, mating/actuation height, and service access remain unspecified.

**Disposition:** `NARROWED_FUNCTION_ONLY`; the authority can close this gap by
recording either a DNP/solder-link service contract or an exact 1x4 2.54-mm
header and mating envelope. Librarian does not choose between them.

## Cooler/backplate/service envelope

The bounded search found no public manufacturer or NVIDIA source that defines a
complete named V100 SXM2 cooler, carrier backplate, fastener, chassis, and
service envelope. Commercial listings and photographs remain contextual. The
existing PiSXMe authority therefore remains valid: Rev A assumes a cooler
mounted to the V100 module and does not impose a carrier-mounted cooler or
generic underside keepout. If the acceptance row requires a named cooler,
Mechanical/Thermal Authority must first create that product requirement and
supported assembly contract.

**Disposition:** `PROJECT-AUTHORITY-BOUNDARY`; no external evidence closes the
named-cooler gap, and no carrier cooler constraint should be invented.

## Source records

| ID | Class | Source/revision | Local reference and SHA-256 | Use |
|---|---|---|---|---|
| `gotrend-gnr-series-ae-v1r1` | primary manufacturer | GOTREND `GNR-SERIES-AE-V1R1`, latest edit 2022-12-08 | `Library/sources/public/gotrend-gnr2512pa-20260918/GNR-SERIES-AE-V1R1.pdf`; `1e47446de74a906df44dfa98ade75c8e80c3b021eacac5bc0aa500b5998a5c93` | L10 package dimensions and electrical limits |
| `ecs-ecx32` | primary manufacturer | ECS `ECX-32` datasheet | `Library/sources/public/ecs-ecx32-20260918/ecx-32.pdf`; `7f56a768dd3d45948b254a36510ee2158a57ecbdf1b3cdcaaff2c6d49b0e6ee3` | Y10 package and candidate electrical limits |
| `jms583-reference-web-mirror` | secondary/reference mirror | JMicron `JMS583 QFN64-8X8-BUS POWER`, Rev 1.8 drawing/release material mirrored by Scribd; retrieved 2026-09-18 | Remote only: `https://www.scribd.com/document/1042530297/Jms583-Qfn64-8x8-Bus-Power-v1-8` | L10 `GNR2512PA-4R7M`, Y10 25-MHz/10-pF, and 2.54-mm 1x4 reference context; no CAD copied |
| `ecs-250-10-33-jgn-tr` | primary manufacturer product record | ECS product page, current record retrieved 2026-09-18 | Remote only: `https://ecsxtal.com/products/crystals/surface-mount-crystals/ecs-250-10-33-jgn-tr/` | Confirms candidate 25 MHz / 10 pF / 3.2 x 2.5 mm / 40 ohm |
| `v100-cooler-backplate-reva-contract` | project authority | PiSXMe Rev-A cooler/backplate authority, checked 2026-08-29 | `pisxme/reva-clean/authority-inventory/primary-docs/mechanics/V100_COOLER_BACKPLATE_AUTHORITY.md`; `0e35f6adeea4af1a8b01c9b0dfc2a9b57c0ad91a045eee7e5fd732fe255e4797` | Retains module-mounted cooler boundary |

## Dependency disposition

`knowledge:P24-MECHANICAL-3D-MODEL-ENVELOPES` remains **OPEN**, but its
Researcher gap is narrowed. L10 and Y10 now have manufacturer-backed package
candidates for authority review; J8 has a bounded hardware-contract choice;
the cooler issue is a project requirement/boundary question rather than a
missing generic public model. The full acceptance row remains open until
Package/Mechanical Authority records those decisions and a fresh integrated
assembly/service validation is run.

No public development repository files or CAD were changed.
