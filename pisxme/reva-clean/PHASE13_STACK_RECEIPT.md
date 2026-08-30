# Phase 13 stack finalization receipt

Status: `CLOSED`

## Selected fabrication basis

The current public JLCPCB calculator was exercised on 2026-08-30 using the
six-layer `JLC06161H-7628` template, nominal 1.6 mm board, 1 oz outer copper,
and 0.5 oz inner copper. The exact request and calculator capture are saved in
`authority-inventory/primary-docs/jlc/JLC06161H-7628-calculator-20260830.json`.

The stack is ordinary through-via only. L2 and L5 are solid GND reference
planes; L1 and L6 are the signal/component layers. The saved stack response and
input record provide the dielectric thicknesses, copper thicknesses, and Dk
values needed to reproduce the calculator request.

## Released constraint basis

| Interface | Target | Released pair geometry | Reference |
|---|---:|---:|---|
| PCIe Gen2 | 90 ohm differential | 5.2 mil width / 8 mil spacing | L1-L2 or L6-L5 |
| USB3 | 90 ohm differential | 5.2 mil width / 8 mil spacing | L1-L2 or L6-L5 |
| SATA | 100 ohm differential | 5.2 mil width / 8 mil spacing | L1-L2 or L6-L5 |
| 1000BASE-T | 100 ohm differential | 5.2 mil width / 8 mil spacing | L1-L2 or L6-L5 |
| USB2 | 90 ohm differential | 5.2 mil width / 8 mil spacing | L1-L2 or L6-L5 |

The calculator's current inverse path accepted both target values and returned
the recorded width/spacing pair. The separate earlier 90-ohm solved-Z capture
remains preserved. The UI capture did not provide an independently displayed
numeric solved-Z field, so fabrication coupon data remains required and is not
being represented as completed hardware evidence.

## Routing rules fixed by this gate

- Ordinary through vias only; no signal routing on In1/In2/In3/In4.
- High-speed pairs reference the immediately adjacent solid GND plane.
- Differential pairs remain symmetric through transitions and receive local
  functional return-via clusters.
- SATA and Ethernet use the 100-ohm target; PCIe, USB3, and USB2 use 90 ohm.
- Controlled impedance and a fab coupon are required on the eventual order.

## Sources and provenance

- Current calculator: <https://jlcpcb.com/pcb-impedance-calculator>
- Current calculator guide: <https://jlcpcb.com/help/article/user-guide-to-the-jlcpcb-impedance-calculator>
- Current JLC impedance capability/material page: <https://jlcpcb.com/impedance>
- Local stack API response: `authority-inventory/primary-docs/jlc/JLC06161H-7628-stack-api-20260830.json`
- Local input record: `authority-inventory/primary-docs/jlc/JLC06161H-7628_IMPEDANCE_INPUTS.md`

This receipt is a design-constraint authority, not a claim that fabricated
dielectric tolerances or a production coupon have already been measured.
