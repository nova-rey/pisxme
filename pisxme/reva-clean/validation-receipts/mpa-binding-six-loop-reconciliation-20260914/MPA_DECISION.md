# MPA binding six-loop reconciliation — 2026-09-14

Authority basis: Macro Placement Authority receipt `validation-receipts/mpa-binding-storage-corridor-20260913/RECEIPT.md`, reconciled to current source head `4e38ecf3` and Power Authority V2.2.

## Binding placement

Retain the existing binding anchors and local placements: U13 `(180,135,180°)`; C30 `(103.5,116,180°)`, C32 `(103.5,120,180°)`, C33 `(103.5,128,180°)`, C31 `(103.5,132,180°)`; F2 `(90,60,0°)`; D2 `(110,60,0°)`. Fixed board outline, J1/J3/J5/J6/J7, U1/U2/Q1/Q2/C4/F1/U7/U11/U12/U14, U11 support, GATE_B copper, CM5 USB3/PERST, V100_PET0, J1 PCIe/reference, J3 storage-power copper, and power/ground zones remain protected. U4/U5 cohorts remain power-authority owned.

## Six-loop power corridor delta

The V2.2 architecture requires six physical 12-V/return loops, each independently limited to 6.4 A. The previous Branch-A/B corridor is therefore a protected logical basis only. A producer must place/route six qualified 0039300020 header pairs after Package Authority confirms exact assembly geometry. Reserve six non-overlapping source-to-protection corridors and six independent returns to the protected bus; no passive-sharing merge before independent limiting/fault handling.

## Storage corridors

Retain the binding existing ownership: U7 to C30–C33 short F.Cu escapes then separate B.Cu lanes; separated C30–C33 to U13 TX/RX corridors clear of USB_RXN1; U13 SATA ports to J3 ordered differential corridors; STORAGE_SEL lower/east U12.9/U13.9 to U14.4; AUTO_PEDET J3.69 to J8.2; MODE_IN U14.2 to J8.4. Use ordinary through-vias, preserve validated high-speed corridors, and keep the authorized fine-pitch exception scoped.

## Rejected hypotheses preserved

The prior exact-pad route remains rejected by its receipt (22 shorts, 32 crossings); the AUTO_PEDET-only candidate is scoped partial evidence and does not close the integrated corridor. No shared vias, synthetic connectivity, global rule relaxation, or controlled-impedance widening is authorized.

## Decision

This is one binding placement/corridor plan for the next producer. It does not claim routability, DRC, connectivity, connector qualification, or fabricated-hardware behavior. If the six-loop topology exposes a structural contradiction, return one bounded evidence packet to MPA; do not launch unrestricted route variants.
