# MPA placement producer receipt

Base: `505aa1f8` (committed integrated candidate). Worker: qualified
`pisxme-kicad-light:v1`, 1 CPU/1 GiB. This candidate materializes the binding
MPA plan only: U13 rotated 180 degrees at (180,135); C30/C32/C33/C31 moved
to (103.5,116/120/128/132) and rotated 180 degrees; F2 moved to (18,145);
D2 moved to (35,145). No routes, rules, topology, or other components changed.

Candidate SHA-256: `b3884f741a6f47aedc3f591b9182347583671f3110097499e14da21ed40ac59b`

Targeted native DRC after placement materialization: 494 violations / 499
unconnected items, RC 5. This is a producer placement candidate, not an
integrated closure result; routing implementation and fresh Light validation
remain required.
