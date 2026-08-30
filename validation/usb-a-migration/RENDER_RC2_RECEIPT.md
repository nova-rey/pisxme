# RC2 render receipt

Date: 2026-08-27

`renders-rc2/PiSXMe-RC2-top.png` is a fresh KiCad CLI top render from the
current USB-A board. `migration-top.png` and `migration-iso.png` are retained
same-placement supporting views from the migration checkpoint; they predate
the final silkscreen-only cleanup but show the Type-A mechanical envelope.

The CLI 3D renderer did not complete a fresh isometric/bottom render within
the local model-loading run, so no stale image is presented as a fresh RC2
render. This limitation is recorded for external review.
