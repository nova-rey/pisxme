# Protected-bus CAD authoring runtime receipt

The two failed producer handoffs were not active CAD workers: `pisxme-worker status` reported an empty `container_status`, and only setup/baseline artifacts existed. The launcher is one-shot and runs exactly one argv command after `--`; a baseline invocation cannot be followed by an implicit authoring handoff.

Root proved the supported path directly:

`/home/nyx/pisxme-eda-workers/scripts/pisxme-worker start kicad-light protected-bus-r3-corridor-retry-20260921 /home/nyx/eda-workspaces/protected-bus-r3-corridor-retry-20260921 1 1g -- kicad-cli version`

Result: `10.0.6`.

The Build Engineer inspection also verified direct argv execution imports `pcbnew` and reports `10.0.6-10.0.6~ubuntu24.04.1`; no CAD or global configuration changed. Producers must pass their authoring script directly in the same `start` invocation.
