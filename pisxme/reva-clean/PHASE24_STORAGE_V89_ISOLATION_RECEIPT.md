# V89 anomaly isolation — 2026-09-10

The V89 DRC short at `XOUT`/`JMS_XAVDDH` is not present in a freshly
refilled V79 baseline (601 violations / 350 opens), and it is not caused by
the source pickup alone.

* V79 plus only the `U14.5` F.Cu pickup, ordinary via, and In1 trunk:
  603 violations / 350 opens; no `shorting_items` entry.
* V79 plus only the J3-side power drops and their In1 return: 607 violations /
  342 opens; the `XOUT`/`JMS_XAVDDH` short appears.
* Full V89: 607 violations / 341 opens; the same short appears.

All variants use native saved-board pads/tracks/vias, and the focused power
audit uses KiCad connectivity only. This isolates the next investigation to
the J3-side through-via/drop implementation or a KiCad regeneration
interaction triggered by those objects. It does not justify accepting V89 or
claiming the short is inherited. No DRC rule was changed.
