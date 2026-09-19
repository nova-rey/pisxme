# CM5/Ethernet assembly and service evidence reconciliation

Package-level disposition: **UNPROVEN**. The integrated r3 2D CM5/Ethernet closure is PASS, but the signed Mechanical/DFM Authority contract explicitly retains assembly/service fields as UNPROVEN. No CAD or routing changes were made.

## PASS

- C48-C51 integrated edge clearance: zero copper-edge-clearance findings.
- C7/C8 integrated courtyard separation: target overlap absent.
- Integrated r3 targeted Light validation: 264 violations, 393 unconnected, zero shorts; remaining DRC findings are outside this package.

## UNPROVEN and exact gaps

- C7/C8 and C48-C51 have no project-local 3D body models or authoritative body-height records; their 2D XY/edge geometry is evidenced, but the Z assembly envelope is not.
- L10/Y10 exact MPN, body height, and model remain absent.
- J8 remains populated/in-BOM with DNP=false, but its mating accessory, keying, operator access, service procedure, and height are not established. FORCE_SATA and FORCE_NVME simultaneous selection remains prohibited.
- J1 connector identity and external mating dimensions are bound, but exact local 3D mating/rework assembly and prototype mating evidence are absent.
- J3 2280 insertion/retention/service sweep remains open; J3/MECH_M2_2280 courtyard/PTH findings remain and are not waived.
- The selected V100/SXM2 cooler/backplate, thermal path, airflow/liquid routing, and enclosure/service fit remain prototype-validation items.
- The retained mechanical audit identifies stale BOM mismatch; current candidate BOM/CPL/assembly release reconciliation is still missing.

The signed authority contract is applied without promoting any missing evidence to PASS.
