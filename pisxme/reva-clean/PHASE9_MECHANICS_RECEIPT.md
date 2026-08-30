# PiSXMe Rev A Clean — Phase 9 mechanical receipt

Checked: 2026-08-30. Status: `PISXME_REVA_CLEAN_PHASE9_CLOSED`.

The clean mechanical evidence now includes the selected SXM2 400-pad
courtyard, a JAE M.2 2280 retention envelope with optional 2242 datum, and a
conservative V100 cooler/backplate envelope of 150 x 95 mm with +45 mm top
reservation. The V100 envelope is explicitly `REV_A_EMPIRICAL_RISK`; no
proprietary NVIDIA CAD or unsupported exact-fit claim is made. The M.2 and
SXM2 authoritative dimensions remain tied to their local Phase 2 drawings;
their unavailable exact 3D archives are not replaced by donor models.

`validation/phase3/test_phase9_mechanics_audit.py` proves the envelope facts
and 400-pad SXM2 courtyard. No production placement or routing was introduced.
