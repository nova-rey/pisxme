# Current-head L10/U11 mechanical 3D and service validation

- Integrated board: `eedf9e723b5069fcbb495834b1f8cb9b15a7ec4e`
- Mechanical authority: `eff269f2b84044ca521c55116b1971a23558a873`
- Board SHA-256: `9d874cb56f7a7f2a11481f1bed893775d741a073763b8297c94c82ec9e3d119f`
- CAD edits: none.

## Results

- L10 XY bound: **PASS** at `(143.00,127.80)`; courtyard and edge bound match the authority contract. Z height remains **UNPROVEN**.
- Y10 XY bound: **PASS**; courtyard and edge bound match the authority contract. Z height remains **UNPROVEN**.
- L10/U11 local gap: **1.110 mm**; L10/Y10 gap: **1.410 mm**.
- J1 2D courtyard and 5.10 mm rework-guidance bounding check: **PASS**; exact 3D/mating/hidden-joint assembly remains **UNPROVEN**.
- J8 source population remains in-BOM/on-board/DNP=false, but its courtyard overlaps the explicit M.2 envelope by `4.09 x 3.14 mm`; exact accessory, keying, height, and service procedure remain **UNPROVEN**.
- J3 manufacturer contract is recognized, but J3 overlaps the explicit M.2 envelope by `30.64 x 11.09 mm`; insertion, retention, cable access, and service fit remain **OPEN**.
- Rev-A cooler contract remains module-mounted only. Selected cooler/backplate/standoff fit and thermal assembly remain **REQUIRES_PROTOTYPE_VALIDATION**.
- Native Light DRC: **264 violations**, **393 unconnected**, **0 shorting_items**, **4 courtyard overlaps**, **5 PTH-inside-courtyard**, **0 copper-edge-clearance**.
- Heavy render: top and isometric renders completed successfully. This is a renderer/tool pass only; it is not a mating or thermal assembly pass.
- Model census: 4 model records, 2 resolvable records, and no exact models for L10, Y10, U11, J1, J3, J8, or `MECH_M2_2280`.

## Exact remaining gaps

1. Exact L10/Y10 manufacturer identity, body height, and 3D or dimensioned package evidence.
2. J8 selected hardware/accessory, mating/keying, height, operator access, and service procedure.
3. J3 populated 2280 card insertion/removal and retention/service sweep; current overlap remains an integrated mechanical finding.
4. J1 exact connector 3D/mating and hidden-joint rework proof.
5. Selected module cooler, standoff/backplate, enclosure, and thermal/service assembly evidence.

These are recorded as `UNPROVEN`, `OPEN`, or `REQUIRES_PROTOTYPE_VALIDATION`; no waiver or fabricated hardware result is claimed.
