# Protected Bus R3 Current-Head B2 Candidate Receipt

- Producer base: `a9589e16`
- Candidate SHA-256: `35b0ceda719a4e73be4e090d2cccb78bd0ac83c2aaabca5f185e358d6022422b`
- Worker/image: `pisxme-kicad-light:v1`
- KiCad: `10.0.6`
- Candidate: `PHASE24_PROTECTED_BUS_R3_CURRENT_HEAD_B2_PAIR.kicad_pcb`
- Scope: J5 P2 / F2 B2 branch only; B1 and unrelated copper preserved
- Native DRC: 984 violations; 428 unconnected items
- DRC report SHA-256: `40dabe50f8c041bf5ae264b4403dcc127de8928b818aced8608bef371e3b6d1a`
- Targeted native ownership: PWR_SRC_J5_P2 pads J5.2 + F2.1-4; PWR_FUSED_J5_P2 pads F2.5-8; PWR_RET_J5_P5 pad J5.5; 2 fused vias + 2 return vias
- Result: `REJECTED_FOR_INTEGRATION`; DRC worsened versus current-head B1 baseline (919/435), despite branch-local ownership being correct.
