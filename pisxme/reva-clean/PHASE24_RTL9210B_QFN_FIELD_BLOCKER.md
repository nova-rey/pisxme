# RTL9210B Path-B QFN field disposition

## Current evidence

The active saved-board base is `PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb`.
Native DRC is 0 violations for the accepted composite V1418/V1420 primitives,
and its saved-board audit passes two source-removal negative controls. Ten
unconnected pad groups remain.

The remaining U1.66 GND connection is a package-field problem. Native pad
geometry is:

| pad | net | center | size |
|---|---|---|---|
| U1.65 | LANE0_RXN | (94.05, 72.0) | 0.9 x 0.2 mm |
| U1.66 | GND | (94.05, 72.4) | 0.9 x 0.2 mm |
| U1.67 | LANE0_TXN | (94.05, 72.8) | 0.9 x 0.2 mm |
| U1.68 | LANE0_TXP | (94.05, 73.2) | 0.9 x 0.2 mm |
| U1.69 | GND exposed pad | (98.0, 70.0) | 4.8 x 4.8 mm |

The pad pitch is 0.4 mm with 0.2 mm pad-to-pad gap. The active local DRC
contract requires 0.2 mm clearance and 0.2 mm track width. A standard
through-via outside the pad cannot be reached from U1.66 without crossing or
shorting U1.65/U1.67/U1.68 or the existing JTAG/PEDET/PCIe field.

## Experiments checked

Direct, west, left-first, orthogonal, local-zone, R1-relocation, coupled
RSET/RTL_1V1, coupled QFN regeneration, and REFCLK-adjacent field trials
were preserved in `PHASE24_STATUS.md` and their native DRC reports. The best
U1.66 direct trial still failed; the priority-corrected GND zone had native
DRC zero but left U1.66 unconnected. No severity or validation rule was
relaxed.

## Disposition

Path B is not promoted to production CAD under the current RTL9210B footprint,
clearance, and ordinary-through-via contract. The shortest credible technical
unblock is a manufacturer-verified alternate RTL9210B land-pattern/package
escape that provides a legal U1.66 fanout, followed by complete regeneration
and revalidation of the lane/REFCLK/support field. A second option is a
controlled local package/clearance rule change, which requires explicit user
approval and manufacturing review. Leaving U1.66 open is not acceptable.

Path A remains preserved and available as the fallback architecture. This
report is a Path-B disposition, not a waiver of the overall Phase 24 gate.
