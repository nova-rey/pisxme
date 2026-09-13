# Queue update — P24-POWER-SOURCE-CONTRACT

Root-owned transition request:

| Package | Requested state | Dependency | Reason |
|---|---|---|---|
| `P24-POWER-SOURCE-CONTRACT` | `WAITING` | `authority:power-current-limiter-selection`; `package:P24-POWER-CONNECTOR-QUALIFICATION` | No exact 12-V active limiter/protection MPN is authority-selected; exact six-loop assembly remains open |
| `P24-POWER-INPUT-ARCHITECTURE` | `WAITING` | `authority:power-source-contract`; `package:P24-POWER-CONNECTOR-QUALIFICATION` | PCB-only source additions would be synthetic connectivity |

The prior MPA placement decision remains retained and does not need to be
reopened. The producer cannot return `READY` until both dependencies resolve.
On resolution, the next step is one isolated source/schematic/PCB producer,
then serialized integration and fresh Light validation.
