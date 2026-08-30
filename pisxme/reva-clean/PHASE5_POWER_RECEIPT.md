# PiSXMe Rev A Clean — Phase 5 power architecture receipt

Checked: 2026-08-30. Status: `PISXME_REVA_CLEAN_PHASE5_CLOSED_WITH_REV_A_EMPIRICAL_RISK`.

The schematic-only power architecture contains two mandatory cold-plug 12 V
inputs, two TI `LM74700QDBVRQ1` reverse-current branches, one protected merged
12 V rail, and three `TPSM63606RDLR` converters for CM5 5 V, bridge 3.3 V,
and bridge 1.1 V rails. MPNs are present on every generated power-stage
instance; the bridge IC is not reused as a regulator.

The exact six-pin LM74700 mappings, external N-channel MOSFET/gate/VCAP
components, branch fuses, branch SMBJ18A TVS devices, and fused-input labels
are now represented. The
exact 20-pin TPSM63606 package maps are also represented for U3/U4/U5.
The controller enable policy, VIN/VOUT/AGND/PGND support wiring, FB/RT/EN/PG
passive networks, and 1.1-V divider/output-capacitor network are now complete
in the native schematic. Native ERC=0 and the machine-readable power-net audit
prove those connections. The machine-checkable design-envelope calculation
closes nominal rail/current, TVS clamp margin, shared-branch FET loss, 1.1-V
divider, and effective-C budget. The protected rail handoff to `J1.A3` is
explicit through a cross-sheet global label and is included in the netlist
audit. Residual physical items—branch sharing, routed-copper drop,
fuse/holder temperature, exact ceramic DC-bias at temperature, and
vendor-layout thermal overlay—are classified `REV_A_EMPIRICAL_RISK` and are
binding constraints for later routing and fabrication validation.

The 25.25-A source/load figure is a Rev-A design envelope rather than a
vendor-rated V100 endpoint guarantee. Startup ordering, brownout response,
PG-to-system-reset policy, and V100 endpoint sequencing remain
`REV_A_EMPIRICAL_RISK`; they are not being represented as proven hardware
behavior by this schematic gate.

Power copper/routing is now permitted by the Phase 5 gate, subject to the
recorded limits and the later Phase 14/15 acceptance gates.
