# CM5 buck regulator audit

Selected module: TI `TPSM63606RDLR`, 6 A, 3–36 V input, 1–16 V output, no spread-spectrum variant. Primary authority: [TPSM63606 datasheet](https://www.ti.com/lit/ds/symlink/tpsm63606.pdf) and [TI product page](https://www.ti.com/product/TPSM63606).

## Correct pin contract

| Pins | Function | Required connection |
|---:|---|---|
| 1,16 | VIN1/VIN2 | protected 12 V; place separate close input capacitors at both pins |
| 2 | SW | no external copper beyond the minimum required; keep away from PCIe |
| 3,4 | CBOOT/RBOOT | leave per TI recommended application unless slew-rate tuning is explicitly needed |
| 5 | VLDOIN | tie to an appropriate output-bias point per TI; add the recommended local capacitor |
| 6,11 | AGND | connect to PGND at the module thermal/ground arrangement |
| 7 | VCC | internal LDO output; do not load externally |
| 8,9 | VOUT1/VOUT2 | 5 V output plane and output capacitors |
| 10 | FB | midpoint of feedback divider |
| 12 | RT | resistor to AGND; do not leave open |
| 13 | PG | open-drain power-good with 10–100 kΩ pull-up |
| 14 | EN/SYNC | defined enable/UVLO state; do not leave floating |
| 15 | NC | no-connect or ground exactly as TI permits |
| 17–20 | PGND | input/output capacitor return and thermal ground |

The prior custom symbol incorrectly represented several of these pins and omitted the required RT/VLDOIN semantics. It is not a production-ready buck symbol until corrected.

## Rev A operating point

- Input: protected regulated 12 V.
- Output: 5.0 V for CM5, with a conservative 6 A-rated implementation even though CM5's expected requirement is lower.
- Feedback starting values from the TI 5 V example: `RFBT=40.2 kΩ`, `RFBB=10.0 kΩ`; include the required feed-forward capacitor only if it matches the selected layout/application values.
- Switching frequency: start at 1 MHz using the TI example RT value, approximately 13 kΩ, unless the final EMI review chooses a different value.
- Input: at least two close 10 µF, 50 V X7R/X7S capacitors, one associated with each VIN pin, plus local bulk.
- Output: design for at least 30 µF effective capacitance at 5 V after DC-bias and tolerance; use multiple capacitors rather than relying on one nominal value.
- PG pull-up: 10–100 kΩ to a defined logic rail.

## Placement and thermal gate

The module must sit in a dedicated CM5 buck zone, with a solid PGND/thermal copper region, thermal vias as permitted by the package/assembly process, and the shortest VIN/SW/VOUT loops shown in TI's recommended layout. The SW node is a hard keepout from the PCIe L1/L2 corridor. Thermal dissipation and load transient validation remain required on the prototype.

