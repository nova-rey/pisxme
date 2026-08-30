# PiSXMe Rev A Clean — Phase 6 Ethernet receipt

Checked: 2026-08-30. Status: `PISXME_REVA_CLEAN_PHASE6_CLOSED`.

The Ethernet child contains the CM5IO-derived four-pair Gigabit MDI topology,
center-tap and LED nets, explicit shield nets, and connector-boundary
8-channel ESD protection. Selected MPNs are EDAC `A70-112-331N126` and TI
`TPD4E004DRYR` (1.6 pF/channel authority).

`validation/phase3/test_phase6_ethernet_audit.py` proves the selected part
instances and all four MDI pairs/ESD channels. Native KiCad 10.0.5 root ERC
passes with zero violations. No placement or routing was introduced.
