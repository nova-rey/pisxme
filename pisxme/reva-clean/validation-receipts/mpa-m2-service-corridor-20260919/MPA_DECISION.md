# MPA binding decision: J3/J8/M.2 insertion and service corridor

- **Originating work package:** `P24-MPA-M2-SERVICE-CORRIDOR`
- **Decision:** `BINDING_DECISION`
- **Decision authority:** Macro Placement Authority, with Storage/Mechanical contract reconciliation required at integration
- **Board base SHA:** `3d95d6c08f60b667d8d3d061fefcb1dfda269b53`
- **Board:** `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- **Board SHA-256:** `9d874cb56f7a7f2a11481f1bed893775d741a073763b8297c94c82ec9e3d119f`

## Binding placement

1. **J3 remains fixed** at `(220.000, 165.000)`, top side, `0 deg`, as the selected Path-A TE `1-2199230-4` M-key socket. Its contact field, retention datum, local escape, and U13-to-J3 high-speed corridors are fixed for this package.
2. **MECH_M2_2280 remains fixed** at `(260.000, 160.000)`, B.Cu mechanical layer, `0 deg`. Its explicit full-card envelope is `[220.000,149.000]–[300.000,171.000]` mm, with retention datum at approximately `(297.500,160.000)`.
3. **J8 moves** from `(245.000,150.000)` to `(205.000,140.000)`, top side, `0 deg`. This is the single local placement change. It puts the populated four-contact mode/service interface outside the full 2280 card body envelope while retaining a short local connection to fixed U14 at `(210.000,150.000)`.
4. U14 and its mode-control support remain fixed. No other support cohort moves in this authority package.

## Physical interpretation and required representation correction

`MECH_M2_2280` is the **full populated 2280 card and insertion/service envelope**, not a freely movable clearance proxy. The current overlap with its associated J3 socket is intrinsic to the socket/card mating stack: the measured J3 footprint/courtyard is approximately `[219.000,159.500]–[250.500,170.500]` mm and the full card envelope is `[220.000,149.000]–[300.000,171.000]` mm. The resulting reported overlap (`30.64 x 11.09` mm) is therefore not solved by sliding J3 away from the card. J3 is the card's mating interface.

The integration producer shall preserve the complete card outline and retention datum as mechanical drawing evidence, while representing the connector mating volume separately from the card-body no-go volume. It shall audit the TE socket/card stack height and retention hardware against the released TE application data before accepting the mechanical result. The raw associated J3 courtyard overlap and J3 PTH-inside-courtyard finding remain open until that representation and stack audit are validated; this decision grants no blanket DRC waiver.

The signed mechanical contract currently names JAE `SM3ZS067U410ABR1000`/B-key for J3, while the current selected Path-A schematic/PCB and storage authority use TE `1-2199230-4`/M-key. That is a stale authority-record conflict. Integration must correct the mechanical contract provenance to the current TE M-key authority before closure; it does not authorize replacing the current J3 with the stale JAE/B-key part.

## Corridors and protected geometry

- Card insertion/removal is from the board right edge toward J3 along the full `[220,300] x [149,171]` mm envelope. Keep this region free of unrelated populated parts, hardware, cable loops, and retention obstructions.
- J8's new service access is from the top-side north/west side of the storage island around `(205,140)`. Keep the four holes, jumper access, and a practical operator approach clear of U14, U13, J3, and the card body.
- Route `FORCE_SATA`, `AUTO_PEDET`, `FORCE_NVME`, and `MODE_IN` from J8 to fixed U14/J3 control endpoints in a short local control corridor north/east of U14 and outside the J3 card-body envelope. Use normal rules and ordinary through-vias only; do not enter J3 high-speed pad fields.
- Protect existing U13-to-J3 PCIe/SATA differential corridors, J3 `STORAGE_3V3` launches, U11/U12 support copper, CM5 USB3, `CM5_PERST`, J1 PCIe/reference copper, and existing power/ground planes. No route deletion or global rule change is authorized by this decision.
- Preserve J1 `(150,90)`, J5 `(12,25)`, J6 `(12,45)`, J7 `(35,130)`, U7 `(96,124)`, U11 `(140,135)`, U12 `(165,135)`, U13 `(180,135)`, and U14 `(210,150)` as fixed anchors for this package.

## Rationale

The Heavy receipt records J8/card-envelope overlap of `4.09 x 3.14` mm and J3/card-envelope overlap of `30.64 x 11.09` mm, plus PTH-inside-courtyard findings for all four J8 pads and the J3 retention pad. Moving J8 to `(205,140)` removes the independent populated service interface from the card body and leaves U14 nearby. Moving J3 would destroy the selected socket/card datum and cannot remove the inherent connector-to-card mating overlap. The correct implementation boundary is therefore one local J8 relocation plus an explicit full-card versus connector-mating mechanical representation and stack audit.

## Non-negotiable constraints

- Preserve Path-A dual-mode storage topology, populated `J8` (`DNP=false`), and prohibition on simultaneous `FORCE_SATA` and `FORCE_NVME`.
- Preserve TE M-key J3 identity and current net/pad ownership; resolve the stale JAE/B-key contract text through Storage/Mechanical Authority.
- Preserve full 2280 body envelope, right-edge insertion direction, retention datum, and card service access.
- No global rule relaxation, no synthetic connectivity, no DRC suppression, no silent envelope shrink, and no Phase 26 work.
- Revalidate the candidate in an isolated producer, then run targeted native Light DRC/connectivity and Heavy insertion/retention/service checks on the integrated current HEAD.

**Authoritative baseline declaration:** For `P24-MPA-M2-SERVICE-CORRIDOR`, J3 and the complete 2280 insertion envelope are fixed at the current Path-A datum; J8 is bound to `(205.000,140.000), 0 deg, top side`; the only permitted local placement change is J8 relocation, and the card/connector overlap must be resolved by explicit mechanical-interface representation and stack validation rather than by moving the socket or shrinking the card envelope.
