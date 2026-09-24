# Protected-bus Heavy preflight startup failure

- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Base: `4afbd3ce`
- Capability: `pisxme-kicad-heavy:v2`, `sha256:39fdae0176135aec42a0dacc8fb250bf8cbf915e01ad67a342e8f8bb2de44344`
- Result: no candidate produced.

The bounded preflight launched the isolated Heavy container and pcbnew, but `pisxme-heavy-gui launch` stopped while waiting for KiCad to finish applying startup defaults. The retained `setup.png` shows the first-run KiCad Setup modal; `launch.log` records the startup-default wait. pcbnew exited before a session file or route could be acquired. The isolated PCB has no diff and no route/validation receipt. This is a reproducible startup/setup execution failure, not a structural corridor contradiction.

Retained raw files: `output/setup.png`, `output/launch.log`, `output/pcbnew.log`, and workspace status. Container stopped after evidence preservation.
