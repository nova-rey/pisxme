# Phase 24 storage support audit receipt — 2026-09-10

Basis: `PHASE24_STORAGE_CM5_USB4_MONOTONIC_V54_STORAGE_GND_SOLID.kicad_pcb`
and `STORAGE.kicad_sch`.

## Correct invocation and result

The initial triage accidentally passed the PCB path to
`phase24_jms583_support_audit.py`, which expects the schematic authority, and
did not set the environment-selected PCB paths for the VBUS/VCCO audits. That
produced false failures and did not constitute design evidence.

The corrected commands were:

```text
flatpak run --command=python3 org.kicad.KiCad phase24_jms583_support_audit.py STORAGE.kicad_sch
PISXME_VBUS_AUDIT_PCB=PHASE24_STORAGE_CM5_USB4_MONOTONIC_V54_STORAGE_GND_SOLID.kicad_pcb \
  PISXME_VBUS_AUDIT_NEG=vbus-v54-neg.kicad_pcb \
  flatpak run --command=python3 org.kicad.KiCad phase24_jms583_vbus_divider_audit.py
PISXME_VCCO_ZONE_AUDIT_PCB=PHASE24_STORAGE_CM5_USB4_MONOTONIC_V54_STORAGE_GND_SOLID.kicad_pcb \
  PISXME_VCCO_ZONE_AUDIT_NEG=vcco-v54-neg.kicad_pcb \
  flatpak run --command=python3 org.kicad.KiCad phase24_jms583_vcco_zone_audit.py
```

Results:

- `PASS JMS583 required support network authority`
- `PASS VBUS divider native connectivity; PASS trace-removal negative control`
- `PASS VCCO zone native connectivity; PASS zone-removal negative control`

The broader JMS583 support audit sweep also passes the AVDD33, AVDDL,
crystal, production-width crystal, complete-support, ground-return, LXO,
physical-endpoint, PCB-net-authority, reset-delay, reset, REXT, support
cohort, VCCK, VCCO, VDDREG, and XAVDDH checks with their documented negative
controls. These results close the support-authority invocation issue; they do
not close the board's remaining native DRC/open routing findings.
