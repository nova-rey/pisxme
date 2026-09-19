# L10/U11 3D, assembly, and service-envelope evidence

- Package: `P24-MECHANICS-L10-U11-LOCAL-CORRECTION`
- Integrated candidate: `51e712ce4b794758ba48fa1f36fba48d2e83890e`
- Board audited: `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- No CAD edits were made for this receipt.

## Geometry evidence

Native `pcbnew` geometry audit recorded the binding local placement and the surrounding envelopes:

- L10 position `(143.00,127.80)`, F.CrtYd `[141.355,126.355]–[144.645,129.245]`.
- U11 F.CrtYd `[135.355,130.355]–[144.645,139.645]`; L10-to-U11 courtyard gap is `1.110 mm`.
- Y10 F.CrtYd `[136.455,125.005]–[139.945,127.795]`; L10-to-Y10 gap is `1.410 mm`.
- L10, U11, and Y10 have large board-edge margins: minimum `50.805`, `40.405`, and `52.255 mm`, respectively.
- No L10/U11/Y10 courtyard overlap is present. The remaining recorded overlaps are inherited J7/C14, C5/C6, and C7/C8 pairs outside this local correction.
- J3, J8, C5/C6, C7/C8, J7/C14, and board-edge courtyard coordinates are retained in `mech_audit.json` for assembly review.

## 3D render

KiCad Heavy 10.0.6 rendered the integrated board successfully to `INTEGRATED_3D_TOP.png` using image `pisxme-kicad-heavy:v1`, digest `sha256:be9cfe7295fe16a3196cd45fa26fa3aa8acbd7e1121ab55504eb2fc5f2034a8e`.

The render is a visual sanity check only. The board contains no 3D models for L10, U11, Y10, J1, J3, or J8; only J7's referenced model is present in the project corpus. Therefore connector mating height, cooler/backplate clearance, component-height stackup, and cable/service access are **UNPROVEN**, not PASS.

This is the exact remaining evidence gap: released/project-local 3D models or authoritative mechanical height/envelope data for the affected parts and mating assemblies are required before full 3D/assembly/service closure. The 2D courtyard/edge evidence passes for the local placement.

Raw audit and rendered image are preserved beside this receipt.
