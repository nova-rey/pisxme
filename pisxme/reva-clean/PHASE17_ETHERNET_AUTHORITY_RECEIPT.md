# Phase 17 Ethernet authority repair receipt

Status: `CLOSED`

Native KiCad 10.0.5 ERC reports zero violations in
`phase17-erc.rpt`. The eight MDI pairs are now global named boundaries in
both `CORE_CM5.kicad_sch` and `ETHERNET.kicad_sch`; the aggregate `CM5_GBE`
port is no longer used as a substitute for independent pair connectivity.

The generated-symbol authoring path was corrected in `phase6_ethernet.py`:
symbol pin Y coordinates now follow KiCad's schematic coordinate convention,
and each instance pin UUID is unique and cannot collide with its symbol
instance UUID. The migration `phase17_ethernet_pin_authority.py` applies the
same correction to the existing Ethernet child and is idempotent.

The native XML netlist `materialize.xml` proves the exact mapping:

| Pair | CM5 | ESD | MagJack |
|---|---|---|---|
| TD0_P | J7.12 | U6.1 | J2 logical pin 1 -> physical pad 1 |
| TD0_N | J7.10 | U6.2 | J2 logical pin 2 -> physical pad 2 |
| TD1_P | J7.4 | U6.3 | J2 logical pin 3 -> physical pad 3 |
| TD1_N | J7.6 | U6.4 | J2 logical pin 4 -> physical pad 6 |
| TD2_P | J7.11 | U9.1 | J2 logical pin 5 -> physical pad 7 |
| TD2_N | J7.9 | U9.2 | J2 logical pin 6 -> physical pad 8 |
| TD3_P | J7.3 | U9.3 | J2 logical pin 7 -> physical pad 9 |
| TD3_N | J7.5 | U9.4 | J2 logical pin 8 -> physical pad 10 |

Regression coverage is `validation/phase3/test_phase17_ethernet_authority.py`.
This closes the Phase 17 schematic/net authority prerequisite. The EDAC
manufacturer land-pattern numbering is non-ordinal relative to the logical
symbol and matches the official CM5IO U3 launch: logical MDI 1..8 maps to
physical 1,2,3,6,7,8,9,10; logical center taps 9..12 map to 11..14; LEDs map
to 15..18 and shields to 19/20. `phase14_materialize_pcb.py` applies this
complete alias map. The PCB must be regenerated from this netlist before
Ethernet routing; no PCB-only net renaming is permitted.

## CM5IO reference-alignment correction — 2026-09-03

The official CM5IO source was rechecked at the placed-footprint level. Its
left protector carries TD3/TD2 and its right protector carries TD1/TD0. The
clean references are intentionally placed to preserve that copper oracle:
`U6` is the right protector carrying TD0/TD1, and `U9` is the left protector
carrying TD2/TD3. The exact EDAC physical MDI sequence is `1,2,3,6,7,8,9,10`;
center taps are `11..14`, LEDs `15..18`, and shields `19/20`.

This supersedes the earlier disposable-only interpretation that treated the
temporary fixture assignment as a production alias. The corrected native
netlist, local EDAC alias map, and regenerated mapping regression now agree.

## Current-source authoring correction — 2026-09-03

The regenerated transplant fixture now preserves the clean production
mapping at the physical footprint as well as in the native XML netlist. The
official 180-degree transform reaches the opposite side of each local USON;
therefore U6 and U9 use 270-degree local footprint orientation with their
native clean mappings, rather than a 90-degree footprint with swapped pad
net labels. The generic correction is implemented in
`phase17_cm5io_transplant_fixture.py` and
`phase17_apply_cm5io_mdi_from_geometry.py`.

The generated MDI boundary labels are global labels, not ordinary local
labels. Current native netlist export and
`validation/phase3/test_phase17_ethernet_authority.py` pass with all
duplicated flow-through pads represented: U6 1/10, 2/9, 4/7, 5/6 and the
corresponding U9 groups. This corrects stale fixture evidence; it does not
close the acreage routing gate.
