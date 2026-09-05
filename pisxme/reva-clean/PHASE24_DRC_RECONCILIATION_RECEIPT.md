# Phase 24 fresh native DRC reconciliation

Fresh `kicad-cli pcb drc --severity-all --refill-zones` was rerun on the
serialized Phase 24 candidates, counting report sections globally.

| Candidate | DRC violations | Unconnected | Shorts | Crossings | Decision |
|---|---:|---:|---:|---:|---|
| `PHASE24_LOCAL_REPAIRS_CLOCK_COMPLETE` | 205 | 156 | 0 | 0 | clean baseline |
| `PHASE24_BRIDGE_1V1_CAP_CHAIN` | 205 | 145 | 0 | 0 | best accepted basis |
| `PHASE24_BRIDGE_1V1_FIELD_JOIN` | 208 | 144 | 0 | 0 | retained, clearance cost |
| `PHASE24_BRIDGE_1V1_R22_JOIN` | 210 | 142 | 1 | 0 | rejected |
| `PHASE24_U7_CFG_JOIN_CURRENT` | 235 | 136 | 4 | 7 | rejected |
| `PHASE24_CM5_GROUND_TOP4` | 235 | 134 | 8 | 10 | rejected |

The clean working basis for subsequent repairs is therefore
`PHASE24_BRIDGE_1V1_CAP_CHAIN.kicad_pcb`. Earlier incremental notes that
claimed zero shorts/crossings without counting the full report are superseded.
No severity or native finding is waived.
