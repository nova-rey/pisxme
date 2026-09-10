# Phase 24 Path-A V48 U7 RX_N upper escape

**REJECTED — single-net escape introduces a real short.** V48 starts from
V46 and moves only `BRIDGE_SATA_RX_N` above the U7 TX_N segment. The complete
SATA endpoint audit passes and native DRC remains 601 violations / 399
opens, but DRC reports `BRIDGE_SATA_RX_N` shorting the existing
`BRIDGE_SATA_TX_P` via at `(94.3,130.0)`. The local RX_P crossing also
remains. No production authority or validation rule changed.

V46 remains the preferred disposable parent. The next attempt must regenerate
the U7 RX/TX source field as a coordinated pair, not another isolated jog.
