# Phase 24 JMS583 per-net support trials

Basis: `PHASE24_DUAL_MODE_STORAGE_FULL7_XAVDDH_LEFT_EXIT.kicad_pcb`, the
current USB3/XAVDDH integration basis. Each trial adds one native pad-to-pad
support connection using the existing direct-join helper; no expected graph
edges or PCB net ownership changes are used.

| net | native DRC | shorts | crossings | result |
|---|---:|---:|---:|---|
| JMS_REXT | 855 | 4 | 20 | REJECTED |
| JMS_AVDD33 | 863 | 3 | 24 | REJECTED |
| JMS_RESET_N | 857 | 2 | 20 | REJECTED |
| JMS_VBUS_SENSE | 853 | 3 | 20 | REJECTED |
| JMS_VDDREG_5V | 854 | 3 | 21 | REJECTED |
| LXO | 853 | 3 | 20 | REJECTED |

`JMS_VCCO` and `JMS_VCCK` are not silently treated as passes: the legacy
helper has no job mapping for those nets and fails closed. The raw candidate
boards and native reports are retained beside this matrix. The evidence
rejects direct joins as an implementation class; the next work is explicit
per-pad QFN escape allocation for the remaining support rails.
