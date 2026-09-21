# Protected-bus R3 corridor producer launch stall

The first requeued corridor producer completed only the fresh Light baseline and never started a CAD authoring process. Its isolated worker was reset to detached base `9b995ad2b48582a72b1f4d5ca4a35047d3d72b97`; canonical CAD was untouched.

- KiCad: 10.0.6
- Baseline DRC: 257 violations
- Baseline unconnected: 393
- Baseline raw report: `/home/nyx/eda-workspaces/p24-protected-bus-corridor-producer/output/base-9b995ad2-drc.json`
- Structural observation: base contains legacy two-contact J5/J6 and F1/F2; J9 and F3-F9 are absent.

This is a capability/launch failure, not a routing result. The package was reassigned to a fresh KiCad Engineer retry; no candidate or acceptance claim follows from this receipt.
