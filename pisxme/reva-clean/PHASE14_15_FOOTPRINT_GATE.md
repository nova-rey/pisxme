# Phase 14/15 footprint prerequisite

Status: `IN_PROGRESS`

The clean project now has a deterministic package-footprint assignment path for
the selected electrical ICs. It creates project-local package footprints and
assigns them by exact MPN, preserving the single clean-library namespace.

The exact JAE M.2 B-key footprint is now present locally. It is derived from
the dimensioned JAE drawing by moving the eight-position key void to positions
12–19 as required by SATA-IO TP053. The gate remains open for the exact SXM2
comparison, CM5, MagJack, USB-C, and high-current connector patterns.

No power copper or signal routing is created by this step.
