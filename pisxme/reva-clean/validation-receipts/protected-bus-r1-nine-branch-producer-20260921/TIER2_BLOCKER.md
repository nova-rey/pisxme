# Tier-2 blocker: R1 nine-branch corridor candidate

The exact R1 anchor and layer plan is represented, but native validation rejects the routed candidate:

- Baseline board: 257 DRC / 393 unconnected.
- Representative branch producer: 1052 DRC / 449 unconnected.
- Full nine-branch producer: **1220 DRC / 391 unconnected**.

The full report retains clearance, hole-clearance, track-width, solder-mask, shorting, dangling-via, and unconnected findings. The producer did not relax rules or edit unrelated/high-speed geometry. The remaining blocker is physical routability of the exact nine branch lanes, return-lane join, and protected J1 ladder on the current board geometry; no alternate placement or topology is authorized by R1. This is a concrete Tier-2 implementation blocker, not a completion claim or HPQ admission.
