# PiSXMe power architecture V1

Status: coherent first-schematic power policy, not a released 300 W power design. Copper width, thermal rise, connector derating, fuse curves, and sequencing must be validated before hardware release.

## Recommended input architecture

Use one regulated external 12 V supply feeding two keyed, high-current Mini-Fit-family 8-position connectors (GPU-style dual 8-pin harness arrangement). Molex documents the Mini-Fit family at up to 13 A per circuit depending on the exact terminal, wire, and application conditions; the final connector, crimp, PCB land, temperature, and harness derating remain design inputs. **SPEC-DERIVED family capability:** [Molex Mini-Fit connectors](https://www.molex.com/en-us/products/connectors/wire-to-board-connectors/mini-fit-connectors).

At 300 W, the V100 load is approximately 25 A at 12 V before conversion and transient margin. Splitting the input across two connectors gives a practical contact/current path and avoids obsolete peripheral Molex wiring. A modern 12V-2x6 connector is technically attractive but less convenient for a first prototype and should be reconsidered if the enclosure/harness requires it.

The input chain should be:

```text
dual 12 V connectors
      │
      ├─ branch fusing / current distribution (value TBD by measured inrush)
      ├─ reverse-polarity / ideal-diode protection
      ├─ TVS and input bulk sized to the actual PSU/harness
      ├─ V100 12 V plane + local bulk/ceramic decoupling
      └─ 12 V → CM5 5 V synchronous buck
```

Do not route the input switch node or its high-current return through the PCIe corridor. Keep the bulk-current return adjacent to the SXM2 power contacts and use L2/L5 ground continuity under the high-speed channel.

## CM5 rail

The CM5 datasheet specifies a regulated 5 V input, a monotonic rise, and a design budget accommodating up to approximately 2.5 A on 5 V. **SPEC-DERIVED:** [CM5 datasheet](https://datasheets.raspberrypi.com/cm5/cm5-datasheet.pdf). Use a dedicated 12 V-to-5 V synchronous buck rated for at least 5 A continuous in the final thermal environment, with current limit, soft-start, UVLO, and power-good. The 5 A choice is margin, not a claim that the CM5 consumes 5 A continuously.

Target first-pass budget:

| rail | load assumption | policy |
|---|---:|---|
| V100 12 V | up to 300 W / ~25 A nominal, with transient margin | direct protected distribution; verify actual module power behavior |
| CM5 5 V | up to 2.5 A design envelope plus margin | 5 A buck target; route separately from PCIe corridor |
| CM5 3.3 V / 1.8 V | CM5-generated and limited external loads | do not use as a high-power peripheral rail |
| fans/pump/USB | application-specific | separate switched branches and current monitoring where useful |

The modular USB revision resolves the USB portion of this table: `U16`
provides a dedicated 5V peripheral rail, FAST A/B each have a 1.5A Type-C
source switch, and SERVICE has a 0.5A USB2 current limiter with source/sink
backfeed interlock. See `design/USB_POWER_BUDGET.md`.

CM5 power sequencing follows the datasheet: 5 V rises first, `PMIC_EN`/power control then permits internal rails, with the documented minimum timing relationship. The exact PiSXMe supervisor implementation is still to be selected.

## V100 enable and sequencing

`PCIE_PWR_EN` from CM5 pin 106 goes only to a low-voltage supervisor/control block. It must not directly drive the SXM2 300 W rail. The V100 rail should be enabled after input protection is valid and before CM5 releases `/PERST`; `V100_PWR_GOOD` should be a defined input to the reset policy. Exact V100 enable polarity, current-limit behavior, and module-specific sequencing are **UNKNOWN** and must be established from the actual module or a validated carrier.

## Protection and monitoring

Reserve, but do not freeze values yet:

- input fuses or resettable/current-limited branches;
- reverse-polarity/ideal-diode stage;
- TVS selected for the actual 12 V supply and cable inductance;
- input and SXM2-side bulk capacitors with ripple-current rating;
- CM5 buck UVLO/soft-start/current limit;
- shunt or Hall current monitor on the V100 branch;
- V100 12 V, CM5 5 V, and supervisor power-good test points;
- temperature sensors at the V100 power entry, buck inductor, and board hot spots.

## High-current geometry policy

- Use broad, short copper from both connector branches to the SXM2 contacts.
- Keep switch-node copper minimal and physically far from L1 PCIe/REFCLK.
- Do not place power MOSFET thermal vias or an inductor directly beneath L1 PCIe pairs if they would disrupt the L2 return plane.
- Use multiple ground contacts and stitching around power transitions, but do not punch arbitrary via fences through the high-speed corridor.
- Validate temperature rise with the actual connector, copper weight, plane neck-downs, and enclosure airflow.

## Power blockers

The 300 W figure is an NVIDIA V100 SXM2 maximum-power specification, not proof that a chosen module needs exactly 300 W in this board. **SPEC-DERIVED maximum:** [NVIDIA V100 datasheet](https://images.nvidia.com/content/technologies/volta/pdf/tesla-volta-v100-datasheet.pdf). Before release, measure module behavior, confirm the rail/enable interface, and validate the connector and fuse system under load. The power architecture is therefore coherent enough for a schematic, but not yet a production current rating.
