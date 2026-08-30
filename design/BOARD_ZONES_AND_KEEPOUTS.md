# PiSXMe board zones and keepouts

The placement-study board `pisxme/PiSXMe.kicad_pcb` is intentionally unrouted.
Zones are represented as `Dwgs.User`/`Cmts.User` rectangles. The cooler and
backplate rectangles are deliberately not KiCad copper/pad keepout zones,
because the SXM2 connector itself must occupy that XY region. Electrical
keepouts will be added after the real connector/retention geometry is frozen.
There are no production pours or final power planes.

## Provisional coordinate map

Board origin is the lower-left of a 220 mm × 140 mm serviceable outline.

| Name | Study rectangle (mm) | Purpose |
|---|---|---|
| `TOPSIDE_COOLER_KEEP_OUT` | x 10–160, y 22.5–117.5 | External cooler-owned top volume; 150 × 95 mm XY reservation |
| `UNDERSIDE_BACKPLATE_KEEP_OUT` | same XY footprint | Backplate, bolt, nut, washer, and underside component reservation |
| `SXM2_MODULE_ZONE` | inside cooler reservation | SXM2 receptacle, V100 package envelope, retention datum work |
| `PCIE_X1_CORRIDOR` | x 141–168, y 54–86 | One PCIe TX pair, one RX pair, REFCLK pair, reset escape |
| `CM5_ZONE` | x 160–210, y 45–108 | CM5 40 × 55 mm land pattern/body envelope and service edge |
| `HIGH_CURRENT_POWER_ZONE` | x 5–70, y 5–140 | Dual Mini-Fit inputs, fuses, reverse protection, V100 distribution |
| `CM5_BUCK_ZONE` | x 175–215, y 108–138 | TPSM63606 and its power-loop components |
| `IO_ZONE` | x 160–210, y 5–45 and I/O edge | Ethernet/USB access outside PCIe corridor |
| `COOLING_CONTROL_ZONE` | x 190–218, y 5–38 | 2 fan headers, pump/aux header, thermal/control wiring |
| `DEBUG_ZONE` | east/south service edge | UART, reset/power-good test points, indicators |

## Layer policy

- `L1/F.Cu`: future PCIe/REFCLK route and selected short controls; keep the
  corridor geometrically boring.
- `L2`: continuous GND under the PCIe corridor; no high-current split or
  switching return interruption.
- `L3/L4`: power and low-speed partitioning as determined by the final fab
  stackup; do not use the study stackup as production impedance authority.
- `L5`: preferred additional GND reference/return plane.
- `L6/B.Cu`: low-speed and power access, subject to the cooler/backplate and
  service constraints.

## Corridor prohibitions

The PCIe corridor prohibits switching inductors, buck switch nodes, high-
current connector pin fields, high-current via arrays, magnetic Ethernet
components, unrelated clocks, copper-plane transitions, test stubs, and
mounting-hole antipads. The two V100-transmitter AC-coupling capacitors may
sit at the corridor entrance only when the final impedance and return-path
review approves their exact placement.

## Mechanical representation limits

The current board contains representative CM5 STEP geometry from the official
CM5 package and a preserved reference SXM2 connector model. It does not contain
an authoritative V100 module/cooler/backplate model. The rectangle keepouts are
therefore deliberate collision contracts, not proof of fit for a named cooler.
