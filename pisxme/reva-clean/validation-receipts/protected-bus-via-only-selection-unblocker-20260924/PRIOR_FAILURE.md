# Protected-bus split-route attempt — wrong-net control failure

- Specialist workspace: `/home/nyx/eda-workspaces/protected-bus-split-route-operator-20260924`
- Heavy v2, 2.75 GiB, private Xvfb; `OOMKilled=false`.
- First native transaction J5.2 to the ordinary via completed and was captured (`first-route-committed.png`, `first-via-placed.png`).
- The second transaction was launched from the wrong copper/net: GUI status showed `Routing Track: 12V_IN_A` instead of `PWR_SRC_J5_P2`; it was cancelled. A Track and Via Dimensions modal from the wrong-net probe was also cancelled.
- No In2 continuation to F2.1, save/reopen, candidate SHA, or validation occurred. No canonical CAD changed.
- Classification: bounded GUI net-selection/operator failure; not a topology, geometry, DRC, or resource result.
- Required next action: change operator/control method and explicitly select the committed `PWR_SRC_J5_P2` via/net before any continuation. Do not save or integrate this workspace.
