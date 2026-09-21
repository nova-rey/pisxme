# R3 distributed mesh extraction and DFM receipt

- Base: `c574c287`
- Architecture: distributed laminated F.Cu/B.Cu/In2 positive mesh and In1/In4 return mesh.
- Holder envelope: 24.25 mm; bank pitch 25.00 mm; inter-bank gap 0.75 mm.
- Positive transition columns: [104, 106.5, 109, 111.5].
- Offset return columns: [103, 105.5, 108, 110.5].
- Branches: nine, with 2x3 ordinary 0.60/0.30 mm arrays at source/fuse transitions.
- Native DRC DFM gate: FAIL (`1529` violations, `426` unconnected), including courtyard, hole-clearance, and co-location findings.

## Extraction

- Copper model: 35 um, rho `0.00001724 ohm-mm2/mm`.
- Via barrel model: `0.195117 mOhm` per 0.60/0.30 mm through via.
- Effective nine-branch PCB neck: `0.977 mOhm`; provisional allocation `0.650 mOhm`.
- Complete R3 budget: `8.577 mOhm`; contract limit `8.500 mOhm`.
- Raw pad bottleneck current density at 40 A: `519.5 A/mm2`.
- 4 mm three-layer mesh current density at 40 A: `95.2 A/mm2`.
- Temperature rise: `UNPROVEN`; no thermal solver or hardware measurement was run.

The model is a geometry/via extraction receipt, not fabrication evidence. Since the
ordinary 1 oz mesh remains above both electrical limits and native DRC fails, the
remaining authorized decision is Product/Power authorization of heavier copper or
a busbar source field, or a lower-resistance fuse/holder package.
