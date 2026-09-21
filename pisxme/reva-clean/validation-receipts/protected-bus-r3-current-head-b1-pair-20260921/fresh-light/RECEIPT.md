# Fresh Light validation of canonical B1 integration

- Validated commit: `7a623b22`
- Worker image: `pisxme-kicad-light:v1`
- Fresh checkout: `/home/nyx/eda-workspaces/validation-validation-protected-bus-b1-7a623b22-20260921T074925Z`
- Command: `kicad-cli pcb drc --format json --output /workspace/output/integrated-b1-drc.json /workspace/project/pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`

Native Light parsed the canonical integrated candidate and reported `919` violations and `435` unconnected items, including `29` shorting items. This confirms the integration is reproducible and that the candidate remains materially incomplete. The B1 package cannot close; remaining branch routing, physical opens/shorts, resistance, thermal, DFM, and full acceptance rows remain open.
