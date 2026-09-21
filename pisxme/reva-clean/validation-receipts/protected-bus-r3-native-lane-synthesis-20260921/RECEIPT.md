# R3 constraint-aware native lane synthesis receipt

- Base: `2daad584`.
- Worker/image: `root-mediated-native-lane-author-20260921`, `pisxme-kicad-light:v1`, KiCad 10.0.6.
- Method: short F.Cu pad escapes, ordinary F.Cu→In2/In4 via transitions, unique ordered In2 fused lanes into x=103.5..112, and distinct In4 return lanes; no global rules or unrelated edits.
- Native DRC: 1120 violations, 379 unconnected items, exit code 5.
- Movement: opens improved 435→379, but DRC increased and the candidate is not acceptable. No integration claim.
- Disposition: retain evidence and return the geometry to MPA for one bounded corridor revision; do not repeat this exact route family.
