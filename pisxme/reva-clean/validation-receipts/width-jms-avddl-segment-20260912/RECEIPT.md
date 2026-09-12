# Integrated JMS_AVDDL width repair

- Base candidate: `4aa63e55`.
- Scope: one existing F.Cu `JMS_AVDDL` segment UUID `9b2560e2-5de6-4bee-a602-e30e5f51e8b3`, width 0.15 mm → 0.20 mm, length 1.4 mm. No other geometry, nets, pads, rules, or schematic changes.
- Toolchain: KiCad Light 10.0.6, qualified image.
- Fresh DRC: 352 violations / 499 unconnected items (from 353/499); no new classes or shorts.
- This is a bounded non-controlled-impedance rail repair; full power/return acceptance remains open.
