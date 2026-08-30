# Phase 14/15 footprint prerequisite

Status: `IN_PROGRESS`

The clean project now has a deterministic package-footprint assignment path for
the selected electrical ICs. It creates project-local package footprints and
assigns them by exact MPN, preserving the single clean-library namespace.

The gate is intentionally not closed: exact M.2 socket, SXM2 connector, CM5,
MagJack, USB-C, and high-current passive/connector land patterns must be
present locally before a production PCB can receive routed nets. The generated
package outlines are datasheet-derived placeholders for this prerequisite and
are not a substitute for manufacturer land-pattern review.

No power copper or signal routing is created by this step.
