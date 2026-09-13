# Regulator and power authority packet — 2026-09-13

Source candidate: `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`, SHA256 `9938f35c69c9f314fe91498a4858022a4b4d75611d89c68a79c48fd09a11856e`. Read-only authority analysis used host KiCad 10.0.5; qualified closure remains KiCad 10.0.6 Light.

U3 is locally supported, but U4/U5 support banks are stranded: BRIDGE_3V3 has zero tracks/vias and support distances about 118–130 mm; BRIDGE_1V1 has zero tracks/vias and distances up to about 106 mm. FB/RT/PG routes and local PGND thermal-via groups are absent. `12V_PROTECTED` has only 6 segments/1 via in the integrated baseline. The regulator overlay and power acceptance rows remain OPEN.

The actionable disjoint producer boundary is U3 cohort C5–C9/R3–R6, U4 C14–C19/R11–R14, U5 C23–C47/R19–R22, local protected-12-V trunks, VIN/VOUT/FB/RT/PG routing, AGND/PGND separation, thermal-via arrays, and local returns. J1/J3/U7/U11–U14, USB3, storage rails, MPA Branch-B components, and protected high-speed corridors remain excluded.

Open authority evidence includes connector single-contact current versus the 28.5 A/34.3 A budget, branch sharing/fuse I²t/transient, effective MLCC capacitance, U5 1.1-V thermal behavior, and board-specific PDN/thermal results. No fabricated-hardware claim is made.
