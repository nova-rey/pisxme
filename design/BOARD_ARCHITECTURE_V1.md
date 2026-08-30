# PiSXMe board architecture V1

Status: placement and partitioning concept only. No production PCB placement, plane geometry, or routing is included.

## Zones

1. **SXM2 socket/module zone:** populated Meg-Array, V100 module mechanical envelope, adjacent ground/current contacts, and cooler contact keepout.
2. **PCIe x1 corridor:** one TX pair, one RX pair, REFCLK pair, and short reset escape. L1 over solid L2 GND; no high-current switching components.
3. **CM5 connector/module zone:** two board-to-board connectors, 40 × 55 mm module keepout, M2.5 mounting access, and external-antenna/RF decision.
4. **V100 high-current power zone:** dual high-current 12 V entry, fuse/protection, bulk capacitance, current distribution, and the V100 enable/power-good supervisor.
5. **CM5 5 V conversion zone:** 12 V-to-5 V synchronous buck, input/output bulk, EMI containment, and 5 V test points. Place it outside the PCIe corridor.
6. **Ethernet/USB I/O zone:** connector access, cable bend space, USB power switching, and magnetics. Route this around the PCIe corridor.
7. **Fan/pump/control zone:** fan headers, tach/PWM, pump header, temperature monitoring, and status LEDs.
8. **Debug/bring-up zone:** CM5 UART, reset/power-good test points, V100 enable visibility, and low-speed strap/control resistors.

## Placement relationships

```text
V100 thermal + SXM2 power  →  PCIe corridor  →  CM5 B2B/module  →  Ethernet/USB/debug edge
                         CM5 buck is lateral to the module, not beneath the corridor
```

The corridor is a protected geometric reservation, not merely a net class. The only high-speed components permitted in it are the two external 220 nF V100-TX capacitors. Keep inductors, switch nodes, MOSFET power loops, high-current vias, magnetics, and mounting-hole antipads out of it.

## Stack and return-path policy

- L1: PCIe/REFCLK and selected short controls.
- L2: uninterrupted GND beneath the corridor.
- L3/L6: power distribution and low-speed power islands, arranged so they do not split L2.
- L4: control and general signals.
- L5: solid GND.

The exact width/gap is deferred to the selected fabricator's controlled-impedance calculator and coupon. The official CM5IO 4-layer design is useful evidence that 90 Ω routing is practical, but it is not a geometry source for this different board.

## Modular USB-C I/O revision

The former generic Ethernet/USB placeholder is replaced by three real board-edge interfaces:

- `J9 USB3-A` / FAST A: independent CM5 USB3 port 0 for storage, including its USB2 companion D+/D− path.
- `J10 USB3-B` / FAST B: independent CM5 USB3 port 1 for a commodity USB 2.5GbE adapter, including its USB2 companion D+/D− path.
- `J11 SERVICE`: USB2 dual-role/recovery port with hardware VBUS interlock.

The ports occupy the right board edge outside the PCIe corridor. A second
`TPSM63606RDLR` module (`U16`) supplies the USB peripheral 5V rail; the CM5
rail remains isolated. No USB hub, native RJ45, microSD, or USB-PD circuitry is
part of this revision.

## Bring-up provisions

- CM5 UART/debug access and boot/configuration access.
- `TP_PERST`, `TP_CLKREQ`, `TP_PWR_EN`, `TP_V100_PWR_GOOD`.
- Low-speed reset control option and power-good indicators.
- V100 rail voltage/current test points and optional shunt monitor.
- Fan/tach and pump headers if cooling requires them.
- No direct probe stubs on PET/PER/REFCLK; high-speed measurement requires dedicated launch structures only in a later SI plan.

## Explicit exclusions

- no lanes 1–15;
- no conventional PCIe card edge;
- no slot-presence emulation;
- no redriver/retimer in V1;
- no final production USB-C vendor-CAD overlay until connector verification and assembly review;
- no production plane or route geometry in this phase.

## Rev-A cooler-agnostic placement update

The board now uses a formal cooler-owned contract rather than a selected V100
cooler. The serviceable provisional outline is 220 mm × 140 mm. Reserve
150 mm × 95 mm and at least +45 mm above the board for external cooling, with
the same XY footprint below for a possible backplate and retention hardware.
Keep CM5, power entry, tall inductors, I/O, and debug outside that volume.

The placement study contains actual part choices: Amphenol `74221-101LF`, two
Amphenol `10164227-1004A1RLF` CM5 connectors, dual Molex `39301082` Mini-Fit
headers, TI `TPSM63606RDLR` rails, TI `LM74700QDBVRQ1` + `CSD19536KCS`, three
Amphenol USB-C receptacles, and JST/Molex cooling/debug headers. The board is
six-layer, unrouted, and has no final power pours. The full contract is in
[`mechanical/COOLING_MECHANICAL_CONTRACT.md`](../mechanical/COOLING_MECHANICAL_CONTRACT.md).
