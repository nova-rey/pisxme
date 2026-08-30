"""Focused native regression for the U3 quiet-control island."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
PYTHON = "/home/nyx/pisxme-toolchain-environment/bin/pisxme-pcbnew-python"
BOARD = ROOT / "ACREAGE_U3_CONTROLS_PHASE15.kicad_pcb"
REPORT = ROOT / "ACREAGE_U3_CONTROLS_PHASE15-drc.rpt"


def main():
    subprocess.run([PYTHON, "phase15_thermal_vias.py"], cwd=ROOT, check=True)
    subprocess.run([PYTHON, "phase15_power_escape.py"], cwd=ROOT, check=True)
    subprocess.run([PYTHON, "phase15_u3_controls.py"], cwd=ROOT, check=True)
    subprocess.run(["xvfb-run", "-a", "kicad-cli", "pcb", "drc",
                    "--exit-code-violations", str(BOARD)], cwd=ROOT, check=False)
    report = REPORT.read_text()
    assert "shorting_items" not in report
    assert "tracks_crossing" not in report
    assert "[clearance]" not in report
    assert report.count("[unconnected_items]") == 264
    probe = r'''
import pcbnew
b = pcbnew.LoadBoard("ACREAGE_U3_CONTROLS_PHASE15.kicad_pcb")
vias = [x for x in b.GetTracks() if x.Type() == pcbnew.PCB_VIA_T]
assert len(vias) == 20
assert {x.GetNetname() for x in vias if x.GetNetname() != "POWER_GND"} == {
    "/REGULATORS/FB_CM5_5V", "/REGULATORS/RT_CM5_5V", "/REGULATORS/PG_CM5_5V"}
'''
    subprocess.run([PYTHON, "-c", probe], cwd=ROOT, check=True)
    print("Phase 15 U3-control regression: PASS; 20 vias; 264 unrouted items")


if __name__ == "__main__":
    main()
