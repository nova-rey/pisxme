# PiSXMe Rev A Clean — Phase 7 storage receipt

Checked: 2026-08-30. Status: `PISXME_REVA_CLEAN_PHASE7_CLOSED`.

The storage child contains one CM5 USB3 path into TI `TUSB9261IPVP`, its
`BRIDGE_3V3`/`BRIDGE_1V1`/reset/config contracts, one SATA differential link,
and JAE `SM3ZS067U410ABR1000` as the B-key SATA-only M.2 socket. The primary
mechanical envelope is 2280; the design carries no NVMe path and does not use
the CM5 USB2 SERVICE interface.

`validation/phase3/test_phase7_storage_audit.py` proves the selected MPNs,
USB3/SATA polarity-named interfaces, M.2 3.3 V rail, and explicit NVMe/SERVICE
exclusions. Native KiCad 10.0.5 root ERC passes with zero violations.

Firmware image choice, UASP/BOT/TRIM, suspend/reset, and real SSD behavior
remain the approved Phase 7 hardware/software validation work; this receipt
does not claim physical enumeration.
