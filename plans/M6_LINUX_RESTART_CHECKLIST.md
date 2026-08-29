# M6 Linux restart checklist

1. Read `HANDOFF_LINUX_WORKSTATION.md`, `TOOLING_STATUS.md`, and
   `references/REFERENCE_INDEX.md`.
2. Verify branch/HEAD/status and active-source hashes before edits.
3. Verify Linux KiCad 10, `pcbnew`, SKiDL, kinet2pcb, bridge dependencies, and
   project-local symbol/footprint tables.
4. Pass flat source-authority fixture, genuine hierarchy fixture, and custom
   symbol pin-to-pad fixture with native KiCad validation.
5. Reuse the official CM5IO Ethernet source and the preserved JMS578/M.2
   references; validate manufacturer pin maps. Do not invent proxy nets.
6. Build source-bound islands in this order: **ETHERNET**, **STORAGE**,
   **SERVICE**.
7. Keep SERVICE USB2 fixed-UFP/recovery only; no TUSB320/DRP/VBUS source.
8. Keep M.2 SATA explicitly 3.3 V and SATA-only; verify the real B-key socket
   and underside 2242/2280 mechanical envelope.
9. Generate a disposable PCB only through the proven schematic/netlist path;
   validate pad nets, parity, ERC/DRC, SI/PI, and mechanics before migration.
10. Do not resume old FAST-A/FAST-B routing. Do not modify active PiSXMe source
    or start M7 until the M6 gate is explicitly closed.
