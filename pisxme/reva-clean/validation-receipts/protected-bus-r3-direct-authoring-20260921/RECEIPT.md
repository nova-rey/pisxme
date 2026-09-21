# Protected-bus R3 direct authoring receipt

- Base canonical SHA: `588d1b3e`
- Isolated candidate commit: `b83915fbe34f25a986373e8fbd2f2d6c26d51640`
- KiCad: `10.0.6` via `pisxme-worker start kicad-light`
- Authoring command: `/opt/pisxme-venv/bin/python3 /workspace/project/pisxme/reva-clean/produce_mpa_r2_source.py`
- Candidate: `/home/nyx/eda-workspaces/protected_bus_source_r3_producer/project/pisxme/reva-clean/PHASE24_PROTECTED_BUS_R3_CANDIDATE.kicad_pcb`
- Candidate SHA-256: `b90727125372218786ecf832e9e102f0ad49c9a6b87ccd5d4d7dcc58a8e39918`
- Native DRC report: `r3-candidate-drc.json`
- DRC report SHA-256: `f5769a4417b65a4277c7b559b54610b9362cc6efc8ebacd6f816fd5c212a5d92`
- Result: **FAIL / candidate rejected for integration**

The direct authoring process completed with exit code 0 and removed one F.Cu `POWER_GND` zone as authorized by MPA R2. Native Light DRC then reported **264 violations** and **499 unconnected items**. This isolated candidate does not close the protected-bus acceptance rows and must not be integrated. The failure is evidence that zone removal alone is insufficient; the next method must implement complete positive/return corridor routing and revalidate against the 8.50 mOhm contract.
