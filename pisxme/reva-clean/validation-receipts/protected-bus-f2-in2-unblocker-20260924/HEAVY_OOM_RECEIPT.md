# BLOCKED — protected-bus Heavy F2 In2 producer

- Status: `BLOCKED`
- Base: `e9f84b92aadd6ba97e274b96626173f5a2794c45`
- Workspace: `/home/nyx/eda-workspaces/protected-bus-r3-heavy-f2-in2-20260924`
- Image: `pisxme-kicad-heavy:v2`
- Image digest: `sha256:39fdae0176135aec42a0dacc8fb250bf8cbf915e01ad67a342e8f8bb2de44344`
- Container memory limit: `2304 MiB`
- Container: `pisxme-protected-bus-r3-heavy-f2-in2-20260924`

## Evidence

The persistent Heavy session was started with private Xvfb and `pcbnew` became controllable after the first-run KiCad Setup dialog was dismissed. The live session record and pre-route screenshots are retained. KiCad 10.0.6 reported the selected board and the GUI router was entered through `Route -> Route Single Track`; the source pad resolved to `PWR_SRC_J5_P2` at `(16.2,25.0)`.

At the first authorized layer transition toward the ordinary through-via near `(24.5,24.5)`, the `pcbnew` process was OOM-killed. The container remains running for evidence inspection but Docker reports `OOMKilled=true`; no save, reopen, candidate commit, or validation was performed.

The board SHA-256 after termination is identical to the base workspace board:
`9cc9b010fe665b51fefabb1a87b60cd6805b5808fe8a23f8a5ae8d70337faf9`.

No canonical files were modified. This is a Heavy resource/runtime blocker, not evidence of a routing or corridor contradiction.

## Retained artifacts

- `gui-session.json`
- `pre-route.png`
- `pre-route2.png`
- `after-via.png`
- `container-inspect.json`
- `container-stats.txt`
- `SHA256SUMS`

## Required next action

Change capability/resource method through the established Unblocker path before another Heavy attempt. Do not promote a candidate or compare integrated validation counts from this run.
