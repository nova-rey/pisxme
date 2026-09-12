# Fresh current-head Light validation — 2026-09-12

Candidate: `b58201e81947dcc7032117480eecaf57b68c53a6` at validation launch.
Image: `pisxme-kicad-light:v1`, digest
`sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`.

Command executed by the qualified launcher:
`kicad-cli pcb drc --exit-code-violations -o /workspace/output/current-head-drc.json /workspace/project/pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`

Result: 340 violations / 499 unconnected items. This is a fresh integrated
census; Phase 24 remains open.
