# R3 all-branch geometry clone producer receipt

- Base: `7a3ebddd`.
- Worker/image: `root-mediated-authoritative-power-import-20260921`, `pisxme-kicad-light:v1`, KiCad 10.0.6.
- Method: clone the existing authoritative J5/P1 source, fused, and return geometry to all nine MPA-ordered branch nets using offsets `(28 mm * column, 25 mm * connector row)`. No global rule changes and no unrelated copper edits.
- Cloned items: 10 source, 12 fused, and 9 return segments per derived branch.
- Native DRC: 1040 violations, 391 unconnected items, exit code 5.
- Movement: unconnected count improved from 435 on canonical baseline to 391; DRC remains failing and no integration candidate is claimed.
- Disposition: retain as bounded producer evidence; release package for the next method/authority review.
