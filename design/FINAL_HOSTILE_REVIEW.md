# Final hostile electrical/manufacturing review

## Findings

- **SXM2:** lane-0, REFCLK, PERST#, 12 V, and ground identities are sufficiently mapped for a contract, but the public source is reverse-engineered and K18/K19 remain unresolved.
- **PCIe:** TX/RX direction and CM5 pin identities are coherent. The clock is common-clock and direct. V100 endpoint acceptance of CM5 SSC/clock-management behavior is still a bring-up risk.
- **AC coupling:** the old capacitor MPN was wrong by three orders of magnitude; it is a confirmed design issue and must be corrected before schematic release.
- **CLKREQ#:** the local ground strap makes CM5 request the clock continuously, but it does not prove V100 low-power compatibility. Firmware must initially disable clock power management/ASPM.
- **PERST#:** direct connection is reasonable as a topology, but timing and voltage-domain behavior are not experimentally verified for the V100 module.
- **Power:** the prior connector MPN was wrong; the high-current schematic is still no-pin/architectural in places. This alone prevents routing readiness.
- **Buck:** the prior custom TPSM63606 symbol omitted or misrepresented pins. VIN1/VIN2, VLDOIN, VCC, RT, PG, EN/SYNC, AGND, PGND, and SW must be corrected before ERC can mean anything.
- **Manufacturing:** real six-layer candidates exist, but the current geometry is not a fab-returned impedance result. The 74221-101LF and 0.4 mm CM5 connectors need DFM/X-ray review.
- **Mechanics:** the cooler-agnostic and backplate contracts remain compatible with adjacent CM5 placement in concept, but the exact assembly collision model is not a reason to relax electrical signoff.

## Disposition

No production routing should start from the current schematic/PCB. Correct the component MPNs and pin-level symbols, hydrate the project, rerun ERC/DRC in KiCad, obtain the fab-returned stackup/geometry, and repeat the review.

