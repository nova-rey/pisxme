# Phase 14/15 footprint prerequisite

Status: `IN_PROGRESS`

The clean project now has a deterministic package-footprint assignment path for
the selected electrical ICs. It creates project-local package footprints and
assigns them by exact MPN, preserving the single clean-library namespace.
Generated instances also pass through `phase14_annotation_normalize.py`, which
keeps descriptive block names in Value/MPN while emitting legal unique KiCad
references for native annotation and netlist export.

The exact JAE M.2 B-key footprint sub-gate is now closed locally. It is derived from
the dimensioned JAE drawing by moving the eight-position key void to positions
12–19 as required by SATA-IO TP053. The exact Amphenol `10171746-00021LF`
USB-C service connector sub-gate is also closed locally with its manufacturer-
derived 16-contact plus shell pattern. The dual 12 V input pattern is also
closed locally as Molex `0039300020`, using the manufacturer SD-5569-002
drawing: two 4.2 mm-pitch through-hole contacts plus two mechanical mounting
MagJack patterns are now locally verified against their selected authority
receipts, including the CM5 manufacturer model and EDAC-specific hole groups.
SERVICE ESD electrical selection is now TI `TPD2EUSB30DRTR`; its DRT-specific
land pattern is closed locally as a three-pad Texas DRT-3 pattern based on the
TI package drawing and maintained KiCad footprint data.
SXM2 identity and coarse array match are documented, but its local
pattern remains `REV_A_EMPIRICAL_RISK` for drawing-only fields because the
released Rev-W PDF cannot be captured through the available CDN path.

No power copper or signal routing is created by this step.
