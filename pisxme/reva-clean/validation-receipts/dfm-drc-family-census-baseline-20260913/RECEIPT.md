# Integrated DRC/DFM family census — 2026-09-13

Source result: fresh current-head baseline `0cc8230f`, selected PCB SHA `9938f35c69c9f314fe91498a4858022a4b4d75611d89c68a79c48fd09a11856e`, qualified KiCad 10.0.6 Light.

Native DRC reports 302 violations and 499 unconnected items. Violation families are: clearance 138; track width 118; copper-edge clearance 15; track dangling 9; via dangling 7; courtyard overlap 6; PTH inside courtyard 5; tracks crossing 2; co-located holes 2. No shorting-items class was reported in this baseline.

This census defines the repair queue. Width repairs must respect controlled-impedance and authorized fine-escape scope; clearance, courtyard, hole, dangling, and crossing repairs require region ownership and must preserve existing protected copper. It is not a waiver or closure result.
