# R3 local insulated copper reinforcement construction

- Authority: `PISXME-P24-PROTECTED-BUS-MATERIAL-SELECTION-20260921`
- Current candidate base: `4e87f09d`; retained mesh source: `86568f8b`.
- Material: proposed C11000 copper foil/strap, 1.00 mm thick, 8.00 mm wide, 82.00 mm long.
- Insulation: proposed 0.10 mm polyimide film on both faces.
- Positive field: x=99..107, y=5..87 mm; return field: x=113..121, y=5..87 mm.
- Positive/return separation: 6.00 mm.
- Four bonded transitions per polarity at y=15/40/65/82 mm, 2.4/1.2 mm bonded through-hole landing pads.
- Board landing rails: positive F.Cu/B.Cu/In2; return In1/In4. Existing mesh branch routing and signal copper were retained.

## Model result

- Foil resistance: `0.177` mOhm.
- Foil plus four modeled bonds: `0.337` mOhm.
- Effective PCB neck: `0.499` mOhm, margin `0.151` mOhm.
- Complete path: `8.099` mOhm, margin `0.401` mOhm.
- Foil current density at 40 A: `2.960` A/mm2.
- 45 A/100 ms pulse model delta-T: `0.030` K.

The continuous temperature rise, bond resistance, attachment, creepage, service
sequence, and mechanical retention remain unproven until Package/DFM and prototype
qualification. Native Light DRC is currently failing and blocks release.
