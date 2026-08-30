# Human-routing cleanup baseline

Date: 2026-08-28  
Branch: `codex/usb-a-active-migration`  
Commit: `d57418e0d517368088f5aafa69378854783b5b30`

## Preservation

The pre-cleanup active board and schematic are preserved in `baseline/`.
The prior RC2 package remains separate and must not be overwritten.

| File | SHA-256 |
|---|---|
| `pisxme/PiSXMe.kicad_pcb` | `1f4f7f64226b93e9d40988f8a5b0ef141c7a5f65e5a438f4e661f9b67e1be4b0` |
| `pisxme/PiSXMe.kicad_sch` | `22beeb5cd4471c2e8a54f39595f0fbfbe085e9e436f6df5538cb5c5739d26b19` |
| `pisxme/PiSXMe.kicad_pro` | `d3a7b822ae1cfa8eb3da075e11ff9f763c3940218c92a5acded2e4f718e858c2` |

## Board inventory

The active PCB is 220 x 140 mm with 49 footprints, 520 routed segments, 169
explicit via records, 40 explicit zones/zone records including nested zone
objects, and the established six-layer stack. The prior project-level via
census reports 165 functional vias; the parser-visible total is retained here
as a separate structural count until the final census reconciles zone and
stitching records.

## Protected geometry

- PCIe PER0, PET0, and REFCLK are frozen.
- FAST-A and FAST-B USB3/USB2 production routes are frozen.
- SXM2, CM5, cooler/backplate keepouts, board outline, dual 12 V inputs, and
  the distributed V100 power concept are protected.

## Cleanup order

1. Correct F1/Q1 cooler intrusion and reroute only affected power nets.
2. Correct J5/J6/J7 physical spacing and reroute affected cooling nets.
3. Add functional F.SilkS labels.
4. Census and simplify low-speed/control routing without touching protected
   high-speed geometry.
5. Re-run DRC/ERC/parity and regenerate RC3 only if the active board passes.

The baseline DRC/ERC evidence is inherited from the RC2 closure because no
active design mutation had yet occurred at baseline capture.
