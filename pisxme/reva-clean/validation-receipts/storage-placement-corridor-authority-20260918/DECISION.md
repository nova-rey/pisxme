# Binding storage placement and corridor authority

- **Decision ID:** `PISXME-P24-STORAGE-PLACEMENT-CORRIDOR-20260918-R1`
- **Originating package:** `P24-STORAGE-PLACEMENT-CORRIDOR-AUTHORITY`
- **Authority:** Macro Placement Authority / Storage-SI placement scope
- **Decision state:** `BINDING_DECISION`
- **Decision basis:** current `reva-clean` HEAD `ac16d1c4`; selected integrated PCB `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`; PCB SHA-256 `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c`.

## Authority boundary

The selected production storage implementation remains Path A: CM5 USB →
HD3SS6126 → TUSB9261/JMS583 → HD3SS3412 → the fixed TE M-key socket J3.
RTL9210B Path B remains isolated, unpromoted evidence. The current IC in this
placement scope is U11, JMicron JMS583-QHFA3A. The package request's JMS581DL
wording does not change the current Path-A identity or authorize an architecture
change.

No schematic, PCB, rule, library, connector, M-key, protected-bus, CM5, PCIe,
USB3, or storage-mode architecture decision is reopened here.

## Binding placement

| Ref | Position (mm) | Side | Rotation | Disposition |
|---|---:|---|---:|---|
| U11 JMS583 | `(140.00, 135.00)` | top | `0°` | **fixed** |
| Y10 25 MHz crystal | `(138.20, 126.40)` | top | `0°` | **fixed** |
| L10 4.7 uH | `(143.00, 127.80)` | top | `0°` | **move and freeze** |

The existing L10 position `(142.00,130.00)` is superseded by this decision
because it physically overlaps U11's courtyard. At the current native geometry:

- U11 courtyard: `x=135.40..144.60`, `y=130.40..139.60`.
- Existing L10 courtyard: `x=140.40..143.60`, `y=128.60..131.40`.
- The overlap is `x=140.40..143.60`, `y=130.40..131.40`, or `3.20 × 1.00 mm`.
- At the binding position L10 courtyard is `x=141.40..144.60`,
  `y=126.40..129.20`. It has `1.20 mm` separation to U11's north courtyard
  edge and `1.50 mm` separation to Y10's east courtyard edge.

Native pad transforms at the binding position are:

- L10.1 `LXO`: `(141.85,127.80)`.
- L10.2 `JMS_VDDREG_5V`: `(144.15,127.80)`.
- U11.64 `LXO`: `(143.00,131.40)`.
- U11.1 `JMS_VDDREG_5V`: `(136.35,132.00)`.
- U12.1 `JMS_VDDREG_5V`: `(163.50,131.80)`.

A bounded all-footprint courtyard scan of the current board reports no
courtyard intersection for the binding L10 box with any other defined
courtyard. This is a placement authority result; it is not a route or DRC pass.

## Fixed and movable cohorts

Fixed system anchors and protected structures:

- board outline, six-layer stack and layer roles;
- J1 SXM2, J3 M-key socket, J7 CM5, and the M.2 2280 service envelope;
- U7 TUSB9261, U12 HD3SS6126, U13 HD3SS3412, U14 mode-control support;
- U11 and Y10; all validated U11 USB3/PCIe/clock source orientations;
- J1 PCIe/reference/reset copper, CM5 USB3/PERST corridors, J3 storage-power
  contacts/copper, protected-bus copper, planes and zones;
- all existing support parts except L10 are fixed for this bounded decision:
  C80–C93 and R80–R83 remain at their current positions.

Only L10 moves. No support cohort may be silently relocated during
implementation. A new physical contradiction must return as an implementation
failure packet to this authority.

## Package-edge ownership and routing intent

U11 remains at 0° top-side so its package edges continue to own the same
functions:

- north edge: XIN/XOUT crystal pair, XAVDDH, VCCK, PCIe reset/clock-request,
  VCCO and LXO; the Y10 clock escape remains the short north-west pair;
- east edge: PCIe and REFCLK differential groups toward the selector/M-key
  side; preserve the validated high-speed source corridors;
- south edge: USB2/USB3 differential groups into the U12/CM5 storage corridor;
- west edge: VDDREG/VBUS/sense/reset and low-speed support departures toward
  the local support field.

L10 is the north-east support part. Reserve these implementation corridors:

1. `LXO`: U11.64 leaves the QFN field on its existing authorized local escape,
   turns north/east outside the U11 and Y10 courtyards, and enters L10.1 from
   the west/south-west. Keep LXO separate from VDDREG and all clock/PCIe/USB3
   differential corridors.
2. `JMS_VDDREG_5V`: L10.2 is the shared star support point for U11.1 and U12.1.
   Use a dedicated top-side handoff around the north of the U11/Y10 field,
   then ordinary-width copper and ordinary through-vias outside the local
   pad-field escape. Do not route through a courtyard, under a package body,
   or through the U11 XIN/XOUT corridor.
3. U11 north-west XIN/XOUT remains a paired monotonic clock corridor to Y10.
   It retains the already authorized local fine-pitch rule only in its existing
   scope and returns to normal rules at the handoff.
4. U11 south USB3, east PCIe/REFCLK, U7-to-U13 SATA, U13-to-J3 M-key, and
   STORAGE_SEL/MODE_IN corridors remain protected and are not consumed by L10
   support routing.
5. All layer changes use ordinary through-vias only. No synthetic connection,
   shared via, global rule relaxation, controlled-impedance width change, or
   power-plane cut is permitted.

## Decision rationale

The existing U11/Y10 orientation is supported by the native pad map and the
retained ten-branch JMS583 support/negative-control evidence. Reorienting U11
would move PCIe/REFCLK, USB3, and clock groups away from their already validated
edge ownership and is therefore rejected. Moving Y10 would reopen the closed
clock decision without a demonstrated contradiction.

Retaining L10 at `(142,130)` is rejected by the direct courtyard collision
above. Moving L10 to `(143,127.80)` removes that manufacturing collision,
keeps it in the north-east U11 support pocket, preserves a short local LXO
launch, and leaves a clear north handoff for the shared VDDREG rail. A farther
east move would lengthen both support paths without removing any additional
constraint and is rejected.

## Implementation and validation handoff

The storage producer shall apply this single L10 transform in an isolated
committed-base KiCad workspace, regenerate only the affected LXO/VDDREG copper,
and return a candidate with:

- native pad-to-pad connectivity for U11.64→L10.1, U11.1→L10.2,
  U12.1→L10.2;
- trace-removal negative controls for each affected branch;
- native DRC focused on courtyard, clearance, shorts, crossings, vias,
  solder-mask and board-edge findings;
- full ten-branch JMS583 support, USB3, Path-A storage and mechanical/DFM
  rechecks in fresh KiCad Light;
- changed-scope report proving no fixed cohort or protected corridor changed.

A candidate that fails these checks is returned once to this authority with
exact geometry and failure evidence. It is not permission for an orientation
search or unrestricted routing variants.

## Evidence references

- `PHASE24_JMS583_LOCAL_SUPPORT_PLACEMENT_DECISION_20260912.md` — prior U11/Y10
  local placement and native pad transforms.
- `PHASE24_JMS583_FINE_ESCAPE_RECEIPT_20260912.md` — authorized local escape
  scope and ten-branch support evidence.
- `PHASE24_JMS583_LAND_PATTERN_RECONCILIATION.md` — JMS583 QFN64 package basis.
- `validation-receipts/patha-native-storage-census-19a1390a/RECEIPT.md` —
  selected Path-A topology and endpoint contract.
- `validation-receipts/mpa-binding-storage-corridor-20260913/RECEIPT.md` —
  protected integrated storage corridor and fixed-cohort authority.
- `validation-receipts/baseline-current-head-0cc8230f-20260913/RECEIPT.md` —
  exact-head baseline distinction and open Path-A state.
