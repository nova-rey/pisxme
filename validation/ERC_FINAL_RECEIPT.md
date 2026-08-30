# Final ERC receipt — modular USB-C I/O revision

Date: 2026-08-21  
KiCad: `10.0.5`  
Project: `pisxme/PiSXMe.kicad_sch`  
Validation method: fresh lock-free copy of the complete `pisxme` project,
executed from the copied project directory with its project and local symbol/
footprint tables present.

## Commands

```text
/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli sch erc \
  --format json --output validation/ERC_modular_usbc.json PiSXMe.kicad_sch

/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli sch erc \
  --format report --output validation/ERC_modular_usbc.rpt PiSXMe.kicad_sch
```

The commands were run from a temporary project copy; the reports were copied
back to the workspace as receipts.

## Result

| Finding | Count | Classification |
|---|---:|---|
| ERC errors | **0** | pass |
| ERC warnings | **48** | all explained below |
| Multiple-net-name findings | **0** | pass; USB orientation branches are distinct |
| Pin-not-connected errors | **0** | pass; CM5 WAKE# and TPSM63606 NC are marked correctly |
| Dangling no-connect markers | **0** | pass |

Remaining warning groups:

- `footprint_link_issues`: 30. KiCad CLI 10.0.5 does not resolve the local
  `PiSXMe` nickname in its isolated validation context. The active board
  embeds the footprints and the source library is copied into the validation
  project; this is a reproducible CLI context limitation.
- `isolated_pin_label`: 18. These are intentional boundary/optional labels
  for documented power, debug, keepout, USB shield/NC, or CM5 interface
  contracts. They are not floating required electrical nets.

The generator's custom-symbol Y-coordinate defect was corrected. A generated
netlist audit confirms that USB-C FAST A/B RX1, TX1, RX2, and TX2 contacts
remain separate through their HD3SS3212 orientation paths, and that each
FAST USB2 companion pair joins its CM5 D+/D− pins through the connector-side
`TPD2EUSB30A` protection device.

## Gate result

**PASS WITH DOCUMENTED TOOL-CONTEXT WARNINGS.** There are zero errors, zero
multiple-net conflicts, zero unexplained warnings, and zero warnings requiring
a design change. This receipt validates the placement-study schematic; it is
not a substitute for the routed-board ERC pass in the next phase.
