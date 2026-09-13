# Path-A corrected storage producer receipt

Date: 2026-09-13
Disposition: REJECTED — bounded producer candidate has real shorts/crossings and materially worsens native DRC.

## Basis and scope

- committed producer base: `c8710a84`
- source PCB: `pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- candidate: `PHASE24_PATHA_STORAGE_CORRECTED_U13_NATIVE.kicad_pcb`
- worker: `south-band-storage-corrected`, qualified `pisxme-kicad-light:v1`, KiCad 10.0.6
- edits were limited to newly emitted copper on the 12 Path-A storage nets. No footprint, schematic, J1, power, U12, or project-rule edits were made.
- all endpoint centers were obtained from the loaded native board with `pcbnew` at generation time; retained coordinate log is `native-pad-coordinates.txt`.

The route set covered U7.57/56/60/59 to C30/C31/C32/C33 pad 2, C30/C31/C32/C33 pad 1 to native U13.38/37/36/35, and native U13.2/.3/.6/.7 to J3.49/.47/.41/.43. The corrected U13 SATA pads were used for the connector legs; the C30-C33-to-U13 bridge legs retain their native TUSB SATA pads.

## Validation

Baseline full Light DRC from the untouched committed base: **312 violations / 499 unconnected items**.
Candidate full Light DRC: **973 violations / 499 unconnected items**.

Candidate violation census: 499 clearance, 125 track-width, 104 solder-mask-bridge, 89 hole-clearance, 67 `shorting_items`, 35 `tracks_crossing`, 16 copper-edge-clearance, 9 co-located-hole, 9 dangling-track, 7 dangling-via, 6 courtyard-overlap, 5 PTH-inside-courtyard, and 2 library-footprint issues.

Focused native endpoint audit reports PASS for all 12 required endpoint pairs, but that scoped connectivity result cannot override the full-board shorts/crossings. The unchanged 499 unconnected count and 67 real shorting items reject this candidate. Representative defects include U7 adjacent-pad shorts, C30-C33 pad-1/pad-2 shorts, U13 adjacent SATA-pad shorts, and J3 adjacent-contact/power-ground shorts.

Commands:

```text
kicad-cli pcb drc --format json --severity-all --exit-code-violations --output patha-corrected-drc.json PHASE24_PATHA_STORAGE_CORRECTED_U13_NATIVE.kicad_pcb
python3 phase24_sata_native_connectivity_audit.py PHASE24_PATHA_STORAGE_CORRECTED_U13_NATIVE.kicad_pcb
```

No integration, canonical commit, or promotion was performed.
