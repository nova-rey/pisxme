# Phase 14 materialization status

Checked: 2026-08-30. Status: `OPEN`.

`phase14_materialize_pcb.py` exports the native KiCad 10 hierarchical
netlist, upgrades a disposable copy of the acreage floorplan to the frozen
six-layer/1.6 mm board, loads every assigned project-local footprint, and
assigns all directly name-matched pads. The current candidate contains 17
components and 78 native nets and has zero tracks by design.

The only intentionally unresolved component-pad mapping is `J1.PWR` and
`J1.GND`. The selected 74221-101LF symbol uses abstract V100 power/ground
pins, while the manufacturer connector drawing and current local comparison
do not establish which of the 400 contacts carry those functions. This is the
existing SXM2 `REV_A_EMPIRICAL_RISK`; no arbitrary pad assignment is made.
It must be closed by the approved pinout/land-pattern authority or remain the
only explicitly classified Rev-A empirical risk before Phase 14 power routing.

The first no-route candidate DRC is not a routing gate: the candidate has no
copper routes and reports the expected unrouted/placement violations. Native
root schematic ERC remains zero after the Ethernet and regulator corrections.
