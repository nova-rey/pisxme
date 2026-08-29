# M6 architecture blocker report

Status: `M6_BLOCKED` and not promoted to active source.

The current Rev A I/O neighborhood cannot be repaired safely in place. FAST-A
and FAST-B connector-side USB3 fragments do not terminate at corrected ESD
geometry, USB2 paths are fragmented, and disposable fanout attempts failed
without violating the approved reference-plane/topology policy. Earlier
Ethernet/SATA candidates used proxy objects and therefore did not prove source
authority or routability.

The approved restart direction is native CM5 Gigabit Ethernet, internal JMS578
USB3-to-SATA, SATA-only M.2 storage, and fixed-UFP SERVICE USB2. Before any
PCB integration, the schematic-authoring path must prove native KiCad parsing,
hierarchy, custom pin maps, and schematic-derived PCB nets on Linux.
