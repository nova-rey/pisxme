# Molex 39301082 prototype footprint validation

- Candidate commit: `fbe2cbd62863adad5716faff6fe5cde0821f895f`
- Scope: isolated footprint geometry and prototype DFM assumptions
- Result: `PASS_SCOPED_WITH_PROTOTYPE_ASSUMPTIONS`

Verified mechanically against the released Molex 5569 drawing data recorded by Footprint Authority:

- 8 electrical holes: 1.80 mm drill
- two mounting NPTHs: 3.00 mm drill
- 4.20 mm pitch in both axes
- 12.60 mm contact span
- 7.30 mm peg centerline from contact-row datum
- circuit-1 datum retained in the footprint's lower-right component-side convention
- 18.00 mm nominal housing width and 12.80 mm body-depth envelope represented by fab/courtyard geometry

The candidate uses a 2.60 mm copper land, 0.20 mm mask expansion, 3.60 mm NPTH keepout, 0.20 mm courtyard margin, and no paste on through-hole pads. These are explicit prototype fabrication assumptions, not manufacturer claims; they remain subject to the selected board-fabrication process and final mechanical inspection.

This receipt does not claim production AVL, vendor STEP parity, or fabricated-hardware fit. Harness bend/service clearance, assembly access, and thermal/current closure remain producer and integrated-validation requirements. The footprint is sufficient to release the protected-bus producer from the former external authorization dependency.
