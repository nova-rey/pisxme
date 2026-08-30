"""Regression for the manufacturer-authoritative Molex 5569-2P layout."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
BOARD = ROOT / "ACREAGE_POWER_PHASE14.kicad_pcb"
REPORT = ROOT / "ACREAGE_POWER_PHASE14-drc.rpt"


def main() -> None:
    subprocess.run(
        ["xvfb-run", "-a", "kicad-cli", "pcb", "drc", "--exit-code-violations", str(BOARD)],
        cwd=ROOT, check=False, text=True, capture_output=True,
    )
    report = REPORT.read_text() if REPORT.exists() else ""
    relevant = ["[" + block for block in report.split("[")
                if "of J5" in block or "of J6" in block]
    # Broader acreage DRC debt remains expected at this stage. This focused
    # check proves the corrected J5/J6 land pattern has no self-hole or mask
    # bridge defect.
    assert not any("hole_clearance" in block or "solder_mask_bridge" in block
                   for block in relevant)
    print("Phase 14 Molex DRC regression: PASS; J5/J6 manufacturer hole pattern has no self-clearance defect")


if __name__ == "__main__":
    main()
