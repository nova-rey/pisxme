# Heavy v2 2 GiB OOM during PiSXMe board load

- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Base: `87c26208`
- Image: `pisxme-kicad-heavy:v2`, `sha256:39fdae0176135aec42a0dacc8fb250bf8cbf915e01ad67a342e8f8bb2de44344`
- Result: no candidate.

With one isolated Heavy container at 2 GiB, the board reached the loaded PCB view and a pre-route screenshot was captured. Docker then reported `State.OOMKilled=true`; the recorded pcbnew PID became stale before route interaction. No PCB diff or validation receipt exists. This confirms the board needs more than the 2 GiB cgroup during GUI load; it is a resource failure, not a CAD or corridor result.
