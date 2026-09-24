# Heavy session lifecycle unblocker

- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Outcome: `SELF_UNBLOCK`
- Classification: actionable worker-runtime/session-lifecycle failure.

Heavy v2 pcbnew exited after session acquisition before the first qualified screenshot or route. The timeout repair extended startup but did not establish a persistent documented Heavy session. Setup dialogs and a dead recorded PID were retained; no crash/OOM/parse evidence or PCB diff exists. The same image/controller passed the synthetic routing qualification, so this is not structural CAD evidence.

Next bounded method: start `/usr/local/bin/pisxme-heavy-session bash` as a persistent worker shell, verify private Xvfb/configuration and live shell, then invoke `pisxme-heavy-gui launch --timeout 120`; capture live PID and pre-route screenshot before the authorized J5.2→F2 route. Save, reopen, and perform fresh Light validation. No CAD/rule/product changes are authorized.
