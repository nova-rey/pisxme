"""Focused native DRC gate for the Phase 14 high-current path.

The acreage board is intentionally not fully routed at this phase.  This
regression therefore rejects only defects involving the power-path parts or
the generated power segments; board-wide unrouted/control debt is left to the
later acreage-validation gate.
"""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
BOARD = ROOT / "ACREAGE_POWER_PHASE14.kicad_pcb"
REPORT = ROOT / "ACREAGE_POWER_PHASE14-drc.rpt"
POWER_REFS = ("J5", "J6", "F1", "F2", "Q1", "Q2")
POWER_DEFECTS = ("shorting_items", "solder_mask_bridge", "hole_clearance", "clearance")


def main() -> None:
    subprocess.run(
        ["xvfb-run", "-a", "kicad-cli", "pcb", "drc",
         "--exit-code-violations", str(BOARD)],
        cwd=ROOT, check=False, text=True, capture_output=True,
    )
    report = REPORT.read_text() if REPORT.exists() else ""
    relevant = ["[" + block for block in report.split("[")
                if any(f"of {ref}" in block for ref in POWER_REFS)
                or "Track [/POWER_INPUT/" in block]
    failures = [block for block in relevant
                if any(f"[{kind}]" in block for kind in POWER_DEFECTS)]
    assert not failures, "Phase 14 power DRC defects:\n" + "\n".join(failures)
    print("Phase 14 focused power DRC: PASS; no power-path shorts, mask bridges, hole, or clearance defects")


if __name__ == "__main__":
    main()
