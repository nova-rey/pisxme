# Protected-bus split-route Heavy v2 candidate

- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Base: `f27f892b`
- Worker: `protected-bus-split-route-click-20260924`
- Capability: `pisxme-kicad-heavy:v2`, 2.75 GiB
- Image digest: `sha256:39fdae0176135aec42a0dacc8fb250bf8cbf915e01ad67a342e8f8bb2de44344`
- Board: `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- Scope: one J5.2 to ordinary-via segment, then In2.PWR via to F2.1 raw pad

## GUI method and evidence

1. `Route -> Route Single Track`, click J5.2 at board `(16.2,25.0)`, place the ordinary via near `(24.5,25.0)`, double-click to commit, then press `Escape` twice to leave route mode.
2. Select `In2.PWR` while idle.
3. Disable `All items`, enable only `Vias`, click the via, and inspect `Track & Via Properties`.
4. Properties verified `Net=PWR_SRC_J5_P2`, position `(24.514048,24.273596)`, via diameter `0.6 mm`, hole `0.3 mm`.
5. Re-enter `Route -> Route Single Track`, left-click the verified via, and live status showed `Routing Track: PWR_SRC_J5_P2`, `Track Width: 0.2000 mm`.
6. Move to F2.1 raw pad `(57.6,13.75)`, click/double-click the pad to finish with no endpoint via. Re-enable `All items` before endpoint selection.
7. Save, close, reopen, and capture the reopened board.

Raw screenshots and GUI session records are in `raw/`.

## KiCad-aware checks

- Base native Light DRC from the committed project: `919` violations, `435` unconnected items.
- Heavy live state after route: `1351` pads, `96` vias, `366` track segments, `434` unrouted.
- Saved board SHA-256 before candidate commit: `aa527f46133a7e3db89bf435c67fa84ae24d302d537798789bb90e0bdb394438`.
- Save/reopen completed with Heavy v2; the reopened screenshot is `raw/post-reopen.png`.
- Heavy only proves the GUI transaction. Fresh Light DRC/connectivity validation is required from the candidate commit before integration.

## Commands

```sh
/home/nyx/pisxme-eda-workers/scripts/pisxme-worker prepare \
  /home/nyx/PiSXMe f27f892b protected-bus-split-route-click-20260924
/home/nyx/pisxme-eda-workers/scripts/pisxme-worker start kicad-heavy \
  protected-bus-split-route-click-20260924 \
  /home/nyx/eda-workspaces/protected-bus-split-route-click-20260924 1 2.75g -- bash -lc 'sleep 1200'
/usr/local/bin/pisxme-heavy-gui launch \
  /workspace/project/pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb \
  --session /workspace/output/gui-session.json --timeout 120
/usr/local/bin/pisxme-heavy-gui screenshot /workspace/output/gui-session.json /workspace/output/pre-route.png
/usr/local/bin/pisxme-heavy-gui close /workspace/output/gui-session.json
/usr/local/bin/pisxme-heavy-gui launch \
  /workspace/project/pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb \
  --session /workspace/output/gui-session-reopen.json --timeout 60
/usr/local/bin/pisxme-heavy-gui screenshot /workspace/output/gui-session-reopen.json /workspace/output/post-reopen.png
```

