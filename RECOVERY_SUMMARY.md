# Mac PiSXMe recovery summary

- Generated: 2026-08-29 (final copy pass)
- Source: `/Users/Cooper/Documents/ChatGPT/sxm2`
- SMB mount used: `/Users/Cooper/mnt/pisxme-recovery`
- Destination: `/srv/pisxme-recovery/raw-mac-recovery`
- Transfer method: native `mount_smbfs` to a user-owned mountpoint, followed by bounded per-file copies. A late iCloud-materialized footprint batch was completed to the same NYX recovery path over SSH after SMB metadata operations stalled; SMB itself remained verified and usable.
- Active PiSXMe design was not modified, moved, or deleted.

## SMB verification

- Mount: WORKING
- Remote read/write/delete test: PASSED
- Temporary test file was created, observed on NYX, read back, and deleted.
- The SMB mount remains active for continued NYX access; it was not unmounted in this pass.

## Transfer totals

- Files currently present in recovery root: 208
- Bytes currently present: 49,673,435
- Useful reference files present: 18
- Custom PiSXMe footprints present: 30
- Conflict copies preserved under `conflicts/`
- SHA-256 checksum run: COMPLETED at `/srv/pisxme-recovery/SHA256SUMS`

## Critical file status

Recovered and checksum-verified against the currently readable Mac source:

- `server.py`
- `bridge/core.py`
- `bridge/schematic_backend.py`
- `tests/test_schematic_backend.py`
- `tests/test_schematic_integration.py`
- `tests/test_bridge.py`
- `pyproject.toml`
- `requirements.txt`
- `pisxme/PiSXMe.kicad_sch`
- `pisxme/PiSXMe.kicad_pcb`
- `pisxme/PiSXMe.kicad_pro`
- `pisxme/PiSXMe.kicad_sym`
- `pisxme/PiSXMe.kicad_dru`
- all 30 custom `*.kicad_mod` files under `pisxme/footprints/`
- `pisxme/fp-lib-table`
- `pisxme/sym-lib-table`
- `HANDOFF_LINUX_WORKSTATION.md`
- `TOOLING_STATUS.md`
- `bible.md`

No critical KiCad source/tooling files remain unavailable among the final checked paths. The design-rule file, bridge regression test, and all 30 custom footprints materialized late and were copied without changing source.

## Preserved material

The recovery tree includes bridge/tooling source and tests, design/validation/planning context, active KiCad source snapshots, SKiDL/tooling experiments, and useful references that were readable during the copy pass.

Important conflict/delta copies are retained instead of silently overwriting prior recovery data at:

`/srv/pisxme-recovery/raw-mac-recovery/conflicts/mac-materialized-20260829/`

## Disposition

- Recovered: all currently readable high-value source/tooling/context/reference files selected for this pass.
- Intentionally skipped: Git metadata, lock files, `.kicad_prl`, caches, virtualenvs, Python bytecode, editor swap files, transient logs, and other disposable/generated session artifacts.
- AppleDouble metadata files created by macOS tar streaming were removed from the recovery footprint directory; source files were not touched.
- No source files were moved, deleted, or changed.
- Recovery of the selected high-value material is complete for the final readable inventory.

For the NYX Codex thread, use:

`/srv/pisxme-recovery/raw-mac-recovery/`
