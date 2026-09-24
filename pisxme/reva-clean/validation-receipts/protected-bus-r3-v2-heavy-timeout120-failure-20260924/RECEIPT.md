# Protected-bus Heavy timeout-120 execution failure

- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Base: `9c41420d`
- Capability: `pisxme-kicad-heavy:v2`, `sha256:39fdae0176135aec42a0dacc8fb250bf8cbf915e01ad67a342e8f8bb2de44344`
- Result: no candidate produced.

The existing qualified launcher was rerun with `--timeout 120`. It eventually created a session record after first-run setup handling, but the recorded pcbnew PID exited before the first qualified screenshot/route interaction. No PCB diff, route receipt, or native validation was produced. Captured files include `gui-session.json`, setup/confirmation screenshots, `pcbnew.stderr`, `direct.stderr`, and PID evidence in the isolated workspace. No structural corridor conclusion is drawn.
