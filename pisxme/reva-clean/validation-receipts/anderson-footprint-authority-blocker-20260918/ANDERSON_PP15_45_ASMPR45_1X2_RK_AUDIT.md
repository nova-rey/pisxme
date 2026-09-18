# Anderson Powerpole PP15/45 prototype footprint audit — BLOCKED

Status: `BLOCKED_FOOTPRINT_LAND_DATA_MISSING`

Prototype engineering audit for released Anderson assembly `ASMPR45-1X2-RK`
(Powerpole PP15/45, single-row 1x2, standard DC 2-wire, right-angle PCB
contacts). This is not production AVL qualification. No canonical PiSXMe CAD
file was changed and no guessed footprint was emitted.

## Selected assembly and polarity

The official Anderson product page identifies `ASMPR45-1X2-RK` as the single-row
1x2 standard assembly. The official PP15/45 data sheet maps assembly positions
to `RED / STD` at position 1 and `BLK / STD` at position 2, and identifies the
right-angle contacts as `3-5912P1` (bottom row) and `3-5913P1` (top row).

| Position | Housing | PCB contact | Row | Electrical assignment |
|---|---|---|---|---|
| 1 | Red | `3-5913P1` | 45 A right-angle top | Not assigned by Anderson; harness authority must assign positive/return |
| 2 | Black | `3-5912P1` | 45 A right-angle bottom | Not assigned by Anderson; harness authority must assign positive/return |

Red/black is a mechanical color convention; it is not a manufacturer pin
number declaration.

## Released dimensions captured

Values are transcribed from official Anderson sources in `SOURCE_MANIFEST.sha256`.
They describe the mechanical pattern, but do not close the PCB land pattern.

| Item | Released value | Source |
|---|---:|---|
| Contact pitch / right-angle and vertical typical spacing | 7.9 mm / 0.31 in TYP | B02021S rev. 6 sheet 2; DS-PP1545 p. 32 |
| PCB staple accessory holes | 1.20 mm / 0.047 in diameter | B02021S rev. 6 sheet 2; retention accessory holes |
| Mounting-wing accessory screw holes | 4.57 mm / 0.180 in diameter | B02021S rev. 6 sheet 2 |
| Row/reference features | 5.23, 6.86, 7.32, 14.78, 18.24, 24.31, 26.16 mm | B02021S rev. 6 sheet 2 |
| Housing/contact references | 28.1, 36.5, 28.6, 16.3, 5.8 mm | B02021S rev. 6; DS-PP1545 p. 32 |
| Stacked housing width reference | 15.8 mm REF | B02021S rev. 6 sheet 2 |
| Contact tail feature references | 1.27 mm / 0.050 in TYP; 5.7 mm / 0.23 in TYP | B02021S rev. 6 sheet 2 |
| Vertical housing reference | 29.7 mm / 1.17 in REF | B02021S rev. 6; DS-PP1545 p. 32 |

## Coordinate and hole audit

B02021S rev. 6 shows a sample PCB layout and centerline relationships, including
7.9 mm typical spacing and the auxiliary-hole diameters. It does **not** provide
a complete contact land definition.

| Required KiCad geometry | Released status | Result |
|---|---|---|
| Contact-tail coordinates in a declared 1x2 datum/origin | Pattern relationships shown, but no unambiguous tail datum/origin | BLOCKED |
| Finished contact drill diameter or slot length/width for `3-5912P1` | Missing | BLOCKED |
| Finished contact drill diameter or slot length/width for `3-5913P1` | Missing | BLOCKED |
| Plated vs. NPTH declaration for contact holes | Missing | BLOCKED |
| Copper pad shape, pad length/width, and minimum annulus | Missing | BLOCKED |
| Solder-mask expansion / paste treatment | Missing | BLOCKED |
| `1.20 mm` staple-hole coordinates and plating | Diameter given; complete datum coordinates and plating absent | BLOCKED for authoritative retention |
| `4.57 mm` wing-hole coordinates and plating | Diameter given; complete datum coordinates and plating absent | BLOCKED for authoritative accessory |

The 1.20 mm and 4.57 mm holes are accessory features and must not be used as
contact drills. A prototype footprint cannot safely choose circular versus
oblong contact holes, plated/non-plated status, pad annulus, or solder-mask
clearance from this released drawing alone. No `.kicad_mod` was created.

## Mating envelope and service assumptions

For board keepout planning only, released references indicate about 36.5 mm
overall right-angle housing/contact length, 28.6 mm secondary length, 16.3 mm
PP15/45 housing reference, 15.8 mm stacked-housing width reference, and 7.9 mm
typical contact spacing. These are envelope references, not a 3D model or
validated board-edge keepout. The product pages state standard housings, up to
10,000 mating cycles, -20 C to 105 C, and up to 45 A per pole. No current,
thermal, resistance, harness, creepage, clearance, latch-access, bend-radius,
or strain-relief qualification is implied.

## Required release evidence to unblock

1. Anderson/authorized land-pattern drawing for both contacts with finished
   drill/slot dimensions and tolerances.
2. Declared datum/origin and contact-tail center coordinates for the
   `ASMPR45-1X2-RK` 1x2 configuration.
3. Copper pad dimensions/annulus, plated-hole declaration, and solder-mask
   expansion/paste requirements.
4. Retention-hole coordinates and intended staple/wing installation details,
   including plating/NPTH status.

Until these arrive, the smallest safe result is this audit only; do not turn the
released references into a guessed footprint.
