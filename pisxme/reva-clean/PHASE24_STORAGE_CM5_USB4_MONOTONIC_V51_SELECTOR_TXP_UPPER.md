# Phase 24 Path-A V51 selector-side TX_P upper detour

**REJECTED — route implementation experiment.** V51 moved only
`TUSB_SATA_TXP` above the M.2 launch corridor from the V50 parent.

Native SATA endpoint connectivity passed and native shorting entries were
zero, but DRC remained **601 violations / 399 opens** and the upper detour
introduced additional crossings/clearance conflicts with the V100 power
corridors and the opposite selector-side SATA TX path. No production PCB or
validation rule changed. V50 remains the preferred disposable parent.
