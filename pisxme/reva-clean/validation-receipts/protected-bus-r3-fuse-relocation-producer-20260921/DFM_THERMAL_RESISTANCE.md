# R3 DFM / thermal / resistance receipt

- Base: `00380ada`
- Authority: `PISXME-P24-PROTECTED-BUS-MPA-20260921-R3`
- Board candidate: `PHASE24_R3_FUSE_RELOCATION_CANDIDATE.kicad_pcb`

## DFM geometry

- Fuse banks: F1-F3 y=15; F4-F6 y=40; F7-F9 y=65 mm.
- Holder courtyard rectangle measured from native footprint: 24.25 x 24.25 mm.
- Inter-bank gap: 25.00 - 24.25 = 0.75 mm.
- Column pitch: 28.00 mm.
- Fixed anchors: J1=(150,90), J5=(12,25), J6=(12,50), J9=(12,75).
- Native DRC includes courtyard and PTH/courtyard findings; therefore DFM gate is `FAIL_PENDING_MECHANICAL_REVIEW`, with geometry receipt retained.

## Trace-only hot-neck extraction

| branch | raw F.Cu mm | return escape mm | trace estimate mOhm | authority allocation |
|---:|---:|---:|---:|---:|
| B1 | 20.888 | 12.258 | 9.170 | 0.650 mOhm |
| B2 | 42.901 | 10.114 | 13.887 | 0.650 mOhm |
| B3 | 66.163 | 8.001 | 18.922 | 0.650 mOhm |
| B4 | 20.888 | 12.258 | 9.170 | 0.650 mOhm |
| B5 | 42.901 | 10.114 | 13.887 | 0.650 mOhm |
| B6 | 66.163 | 8.001 | 18.922 | 0.650 mOhm |
| B7 | 20.888 | 12.258 | 9.170 | 0.650 mOhm |
| B8 | 42.901 | 10.114 | 13.887 | 0.650 mOhm |
| B9 | 66.163 | 8.001 | 18.922 | 0.650 mOhm |

The estimate uses copper resistivity 0.00001724 ohm-mm2/mm and 35 um copper, with the authored widths. It excludes fuse, via barrel, pad, field, and protection contributions; all branch values exceed the 0.65 mOhm allocation before those terms, so the electrical hot-path gate is `UNPROVEN/CONTRADICTED_BY_TRACE_ONLY_ESTIMATE`.

## Thermal

`UNPROVEN_REQUIRES_PROTOTYPE_VALIDATION`: no thermal solver or hardware measurement was run by the qualified Light worker. The candidate contains no thermal claim.
