# Phase 14 materialization status

Checked: 2026-08-30. Status: `PHASE14_POWER_PATH_CLOSED_WITH_REV_A_EMPIRICAL_RISK`.

`phase14_materialize_pcb.py` exports the native KiCad 10 hierarchical
netlist, upgrades a disposable copy of the acreage floorplan to the frozen
six-layer/1.6 mm board, loads every assigned project-local footprint, and
assigns all directly name-matched pads. The current materialized acreage
contains 70 components and 241 native nets; the separate Phase 14 route
candidate adds nineteen power-only B.Cu segments and filled power/return zones.

The selected 74221-101LF symbol uses abstract V100 power/ground pins. The
materializer now expands those abstract pins onto the published
reverse-engineered SXM2 rows: 12 V rows 22/23/25/26/28/29/31/32/34/35/37/38/40
and ground rows 21/24/27/30/33/36/39, across all ten columns. The V100 return
is now explicitly tied to the shared `POWER_GND` net before PCB materialization.
This prevents a
single guessed contact from becoming the distributed feed. The endpoint map
is not NVIDIA/Amphenol authority and remains `REV_A_EMPIRICAL_RISK`; it must
be continuity-checked against the actual V100 module before fabrication.

Regression coverage is `validation/phase3/test_phase14_sxm2_power_aliases.py`:
it requires 400 pads, exactly 130 protected-power and 70 ground contacts, no
power-pad signal contamination, and exact lane-0/control pad net names.

The first no-route candidate DRC is not a routing gate: the candidate has no
copper routes and reports the expected unrouted/placement violations. Native
root schematic ERC remains zero after the Ethernet and regulator corrections.
