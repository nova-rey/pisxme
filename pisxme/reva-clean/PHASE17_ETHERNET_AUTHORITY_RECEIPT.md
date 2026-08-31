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
| TD0_P | J7.12 | U6.1 | J2.1 |
| TD0_N | J7.10 | U6.2 | J2.2 |
| TD1_P | J7.4 | U6.3 | J2.3 |
| TD1_N | J7.6 | U6.4 | J2.4 |
| TD2_P | J7.11 | U9.1 | J2.5 |
| TD2_N | J7.9 | U9.2 | J2.6 |
| TD3_P | J7.3 | U9.3 | J2.7 |
| TD3_N | J7.5 | U9.4 | J2.8 |

Regression coverage is `validation/phase3/test_phase17_ethernet_authority.py`.
This closes the Phase 17 schematic/net authority prerequisite. The PCB must
be regenerated from this netlist before Ethernet routing; no PCB-only net
renaming is permitted.
