# Phase 24 native hierarchy regression receipt — 2026-09-11

Command:

`flatpak run --command=python3 org.kicad.KiCad validation/phase3/test_native_hierarchy_authoring.py`

Result: **PASS**.

The regression now uses an explicit disposable golden-fixture path compatible
with Flatpak, checks exactly the ten authoritative child sheets, accounts for
the generator's direct root signal links, and runs native KiCad ERC directly
at severity `error`. The disposable generated hierarchy completed with zero
native ERC violations and no hierarchy label mismatch.

This validates the generic scaffold regression only. It does not promote the
disposable generated hierarchy or close the live schematic's remaining full
ERC warnings and Phase 24 gates.
