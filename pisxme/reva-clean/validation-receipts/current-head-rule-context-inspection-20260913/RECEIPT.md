# Current-head rule and checker context inspection

- Integrated PCB head: `17dd81d2`
- Current documentation head: `04d722ea`
- KiCad Light image: `pisxme-kicad-light:v1` (KiCad 10.0.6)

The selected project sidecar contains four net classes: `Default`,
`HS_PCIE_90R`, `HS_USB3_90R`, and `PCIE_PERST_CONTROL`. The board-local
`.kicad_dru` contains one scoped JMS XIN/XOUT rule at 0.10 mm clearance and
track width. No explicit `drc_exclusions` or severity-ignore map is present
in the selected project's current JSON sidecar. The five ignored checker
classes reported by the hostile review therefore remain an acceptance gap;
they are not authorized dispositions.

Current input hashes:

```text
f965a4a405f1f2c0fa54a96a22d4bffaa0ee04e5787ad21db31c9c3bcf990143  PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pro
d5473e6262fdf3b53d5de051626f0ed76dedf7257ba591f79ab8ad55f5b411ec  PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_dru
ef3d2901c3f3f6c164e6d5d8cd0b5b34cc4cb461be092e765fd77b0036c0cd2c  PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb
6eef63bd3d2b0b9fafc0150d3c34f636ce24a48b2ecbd3d28a5f0bfec167e9f1  PiSXMe_RevA_Clean.kicad_sch
```

This is context evidence only. It does not replace a fresh exact-head Light
DRC/ERC/parity run, and it authorizes no rule relaxation or physical waiver.
