# MIC2545A-1YM `ISOLATEB` support fixture receipt

Date: 2026-09-10

Fixture: `PHASE24_MIC2545A_SUPPORT_FIXTURE.kicad_pcb`  
Generator: `phase24_mic2545a_support_fixture.py`  
Native DRC: `PHASE24_MIC2545A_SUPPORT_FIXTURE-drc.rpt`  
DFM audit: `PHASE24_MIC2545A_DFM_AUDIT.json`

## Result

`DISPOSABLE_ELECTRICAL_FIXTURE_PASS`

Native KiCad DRC reports zero violations, zero unconnected pads, and zero
footprint errors. The independent saved-board DFM audit also passes all
eight pad sizes, pitch, row spacing, layer, mask/paste settings, courtyard,
and silkscreen assertions. The fixture's saved-board audit uses native connectivity
from pads, tracks, vias, and zones; it does not synthesize graph edges.

## Verified physical ownership

The fixture uses the Microchip/Micrel MIC2545A/2549A datasheet mapping:

- pin 1 `EN` → `ISOLATEB` source;
- pins 5 and 7 `IN` → common `SSD_3V3_IN` source rail;
- pins 6 and 8 `OUT` → common `SSD_3V3` load rail;
- pin 3 `GND` → ground return;
- pin 4 `ILIM` → 76.8 Ω current-limit resistor to ground;
- pin 2 `FLG` intentionally left unused in this electrical fixture.

Both duplicated `IN` pins and both duplicated `OUT` pins are joined by
physical copper. The negative control removes the physical `IN` 5↔7 join;
the native connectivity assertion then fails as required. The fixture also
uses a deliberate B.Cu output escape to avoid crossing the input rail and a
local input bypass/ground return.

## Scope and remaining gate

This proves the corrected electrical pin ownership and a routing pattern in a
disposable board. The fixture's 1.27-mm pitch, 5.40-mm row spacing, and
1.55×0.60-mm pads match Microchip's current recommended 3BX SOIC land
pattern. The fixture now authors explicit zero solder-mask expansion,
−0.05-mm paste margin, and F.CrtYd/F.SilkS geometry. KiCad's report still
lists generic no-courtyard checks among ignored checks for the other simple
fixture footprints, so visual/assembly-house DFM review remains open, as do
SSD 3.3-V source sizing, inrush/fault policy, and RTL9210B production
integration.

Source: <https://ww1.microchip.com/downloads/en/DeviceDoc/mic2545a.pdf>
