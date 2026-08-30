# PiSXMe Rev A Clean — Phase 5 power architecture receipt

Checked: 2026-08-30. Status: `PISXME_REVA_CLEAN_PHASE5_IN_PROGRESS`.

The schematic-only power architecture contains two mandatory cold-plug 12 V
inputs, two TI `LM74700QDBVRQ1` reverse-current branches, one protected merged
12 V rail, and three `TPSM63606RDLR` converters for CM5 5 V, bridge 3.3 V,
and bridge 1.1 V rails. MPNs are present on every generated power-stage
instance; the bridge IC is not reused as a regulator.

The current schematic proves only the component identities and top-level rail
names. It does not yet prove the Phase 5 gate: the LM74700 symbols still need
their exact six-pin mapping, external N-channel MOSFET/gate/VCAP networks, and
enable policy; each TPSM63606 needs its exact 20-pin mapping, VIN/VOUT/AGND/
PGND support, FB/RT/EN/PG networks, input/output capacitors, and vendor-layout
values; fuse/TVS coordination and the distributed high-current SXM2 feed also
remain open. Native ERC=0 is therefore only a syntax/connectivity result, not
power-authority closure.

No power copper or routing is authorized until those circuit-level items and
their calculations are closed.
