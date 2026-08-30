"""Focused native regression for the Phase 15 high-current escape."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
PYTHON = "/home/nyx/pisxme-toolchain-environment/bin/pisxme-pcbnew-python"
BOARD = ROOT / "ACREAGE_REGULATOR_POWER_ESCAPE_PHASE15.kicad_pcb"
REPORT = ROOT / "ACREAGE_REGULATOR_POWER_ESCAPE_PHASE15-drc.rpt"


def main():
    subprocess.run([PYTHON, "phase15_thermal_vias.py"], cwd=ROOT, check=True)
    subprocess.run([PYTHON, "phase15_power_escape.py"], cwd=ROOT, check=True)
    subprocess.run(["xvfb-run", "-a", "kicad-cli", "pcb", "drc",
                    "--exit-code-violations", str(BOARD)], cwd=ROOT, check=False)
    report = REPORT.read_text()
    assert "shorting_items" not in report
    assert "tracks_crossing" not in report
    assert report.count("[unconnected_items]") == 280
    print("Phase 15 power-escape regression: PASS; no shorts/crossings; 280 unrouted baseline items")


if __name__ == "__main__":
    main()
