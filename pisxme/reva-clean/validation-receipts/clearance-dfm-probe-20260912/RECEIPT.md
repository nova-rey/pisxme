# Phase 24 Clearance DFM Probe

Base SHA: 1ea6671211b884e710789fd37f2f8d5186f72a57
Worker image: pisxme-kicad-light:v1
KiCad: 10.0.6
Raw DRC SHA256: 7a16802734bd7a0d7d85ce09bcf31787d100a3021c482624488bc0307c04bdd4
Counts: violations=340 unconnected=499
Clearance=138 copper_edge=16

First 20 clearance-family findings:
1. copper_edge_clearance: Rectangle on Edge.Cuts; Track [CM5_5V] on F.Cu, length 16.0000 mm
2. copper_edge_clearance: Rectangle on Edge.Cuts; Track [CM5_5V] on F.Cu, length 10.1771 mm
3. copper_edge_clearance: Rectangle on Edge.Cuts; Track [CM5_5V] on F.Cu, length 9.0000 mm
4. copper_edge_clearance: Rectangle on Edge.Cuts; Track [CM5_5V] on F.Cu, length 5.0000 mm
5. copper_edge_clearance: Rectangle on Edge.Cuts; Track [CM5_5V] on F.Cu, length 3.5000 mm
6. copper_edge_clearance: Rectangle on Edge.Cuts; Via [CM5_5V] on F.Cu - B.Cu
7. copper_edge_clearance: Rectangle on Edge.Cuts; Via [CM5_5V] on F.Cu - B.Cu
8. copper_edge_clearance: Rectangle on Edge.Cuts; Track [CM5_5V] on B.Cu, length 18.0000 mm
9. copper_edge_clearance: Rectangle on Edge.Cuts; Pad 1 [ETH_CT4] of C51 on F.Cu
10. copper_edge_clearance: Rectangle on Edge.Cuts; Pad 2 [ETH_CT_BRANCH_4] of C51 on F.Cu
11. copper_edge_clearance: Rectangle on Edge.Cuts; Pad 1 [ETH_CT3] of C50 on F.Cu
12. copper_edge_clearance: Rectangle on Edge.Cuts; Pad 2 [ETH_CT_BRANCH_3] of C50 on F.Cu
13. copper_edge_clearance: Rectangle on Edge.Cuts; Pad 1 [ETH_CT2] of C49 on F.Cu
14. copper_edge_clearance: Rectangle on Edge.Cuts; Pad 2 [ETH_CT_BRANCH_2] of C49 on F.Cu
15. copper_edge_clearance: Rectangle on Edge.Cuts; Pad 1 [ETH_CT1] of C48 on F.Cu
16. copper_edge_clearance: Rectangle on Edge.Cuts; Pad 2 [ETH_CT_BRANCH_1] of C48 on F.Cu
17. clearance: Pad 110 [CM5_REFCLK_P] of J7 on F.Cu; Track [CM5_REFCLK_N] on F.Cu, length 2.2171 mm
18. clearance: Track [CM5_REFCLK_P] on F.Cu, length 2.3400 mm; Pad 108 [POWER_GND] of J7 on F.Cu
19. clearance: Track [JMS_RESET_N] on F.Cu, length 23.6000 mm; Pad 2 [POWER_GND] of C85 on F.Cu
20. clearance: Via [SERVICE_VBUS_SENSE] on F.Cu - B.Cu; Via [SERVICE_RD_A] on F.Cu - B.Cu

Classification:
- All 20 are copper/routing or board-edge interactions: tracks, vias, pads, or Edge.Cuts.
- No text/silk/mechanical-only item appears in this first-20 clearance sample.
- Separate silk_over_copper family has 28 findings; a capacitor reference-field relocation/removal (C7 near C8) is a possible disjoint DFM candidate, but was not edited or promoted.
- No candidate commit or patch produced; no nets/rules/USB3/U11/U12/power/J1 touched.
