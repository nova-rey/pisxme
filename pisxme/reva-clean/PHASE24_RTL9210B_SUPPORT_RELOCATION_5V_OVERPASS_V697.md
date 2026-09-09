# RTL9210B Path-B V697 — intermediate 5V overpass

V697 split the RTL_5V transition around the RTL_1V1 B.Cu barrier. Native DRC
removed the crossings but left two redundant single-layer vias. Retain only
as intermediate evidence; V699 removes the redundant vias.
