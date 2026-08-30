# Hostile power / thermal review after high-speed studies

Date: 2026-08-22

## Findings

| Attack | Result |
|---|---|
| 12 V branch rating | Two 15 A protected branches are adequate for the nominal arithmetic only when both are present; the 13.75 A stress branch leaves little margin. |
| SXM2 contacts | 0.192/0.212 A average per +12 V contact is below the 0.45 A Amphenol test rating, but sharing and spreading are unmeasured. |
| distributed feed | 13 feed transitions at 1.92/2.12 A idealized average are plausible; 26 vias imply two per feed, but local current crowding remains possible. |
| narrowest copper | `/VPROT_12V` contains short 0.25 mm pad-escape segments. They are the controlling local bottlenecks. |
| protection | LM74700/MOSFET and fuse dissipation remain unmeasured and can dominate local heating. |
| CM5/USB buck | Both TPSM63606 regions have a 6 A rating and local support routing; actual loss/airflow/transient performance is unmeasured. |
| high-speed interaction | No active power edit was made during this phase; the baseline high-current manifolds remain outside the intended PCIe corridor. |

## Decision

The power architecture is plausible for a monitored Rev-A bring-up, with
documented current/thermal risk. It is not enough to override the high-speed
blockers or to claim fabrication readiness. The first prototype would require
temperature measurements at the SXM2 connector field, fuse terminals,
protection MOSFETs, and both regulator modules under sustained load.
