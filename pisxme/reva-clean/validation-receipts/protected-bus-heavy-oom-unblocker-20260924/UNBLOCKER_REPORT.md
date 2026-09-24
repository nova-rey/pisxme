# Heavy v2 OOM lifecycle unblocker

- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Classification: implementation/runtime
- Root cause: Heavy pcbnew was killed by the 1 GiB cgroup limit (exit 137/OOMKilled), leaving a stale session JSON. UID 1000 versus image UID 1001 and KiCad configuration permissions are not the cause; the image copies configuration into writable `/tmp` HOME and no permission error appears.

Evidence from the exact board and image: forced UID 1000 with 1 GiB was killed during startup; a 2 GiB isolated run kept pcbnew alive with RSS about 2.05 GiB and ended only on intentional probe termination; default UID 1001 with 2 GiB also stayed alive. The existing Heavy controller and private Xvfb remain qualified.

Bounded fix: run one Heavy CAD container at 2 GiB, reserve host headroom, verify `docker inspect .State.OOMKilled == false`, then require live PID, pre-route screenshot, native route/save, reopen, and fresh Light validation. No CAD/rule/product changes.
