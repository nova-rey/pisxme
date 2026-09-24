# Protected-Bus Direct Heavy Launch Timeout

- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Base: `11d839eb3da8b6daf4f5716d625fd1143a6338c6`
- Worker: `pisxme-kicad-heavy:v2`
- Result: no candidate, no validation artifact, no canonical mutation.

A fresh Heavy container was prepared and started with a 2.75 GiB limit. A
bounded `pisxme-heavy-gui launch` was invoked with a 45-second host timeout.
`pcbnew` appeared during the launch, but the launch command exited at the
bound without producing a session file or output artifact. The worker was
then cleaned up and released through the supported lifecycle.

This is a repeated Heavy launch/control failure after the earlier >40-minute
launch stall. It does not establish physical impossibility of the corrected
MPA corridor. Further Heavy replay is paused pending Unblocker diagnosis of
the launch/control path.
