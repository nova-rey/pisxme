"""Focused native regression for separated U4/U5 control islands."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
PYTHON = "/home/nyx/pisxme-toolchain-environment/bin/pisxme-pcbnew-python"
BOARD = ROOT / "ACREAGE_U4_U5_CONTROLS_PHASE15.kicad_pcb"
REPORT = ROOT / "ACREAGE_U4_U5_CONTROLS_PHASE15-drc.rpt"

def main():
    subprocess.run([PYTHON, "phase15_thermal_vias.py"], cwd=ROOT, check=True)
    subprocess.run([PYTHON, "phase15_power_escape.py"], cwd=ROOT, check=True)
    subprocess.run([PYTHON, "phase15_u3_controls.py"], cwd=ROOT, check=True)
    subprocess.run([PYTHON, "phase15_u4_u5_controls.py"], cwd=ROOT, check=True)
    subprocess.run(["xvfb-run", "-a", "kicad-cli", "pcb", "drc",
                    "--exit-code-violations", "--output", REPORT.name,
                    str(BOARD)], cwd=ROOT, check=False)
    report = REPORT.read_text()
    assert "[clearance]" not in report
    assert "[shorting_items]" not in report
    assert "[tracks_crossing]" not in report
    assert report.count("[unconnected_items]") == 254
    probe = r'''
import pcbnew
b = pcbnew.LoadBoard("ACREAGE_U4_U5_CONTROLS_PHASE15.kicad_pcb")
assert b.FindFootprintByReference("U4").GetPosition() == pcbnew.VECTOR2I_MM(200, 105)
assert b.FindFootprintByReference("U5").GetPosition() == pcbnew.VECTOR2I_MM(225, 105)
assert b.FindFootprintByReference("R22").GetPosition() == pcbnew.VECTOR2I_MM(236, 145)
vias = [x for x in b.GetTracks() if x.Type() == pcbnew.PCB_VIA_T]
assert len(vias) == 35
for name in ("/REGULATORS/FB_BRIDGE_3V3", "/REGULATORS/RT_BRIDGE_3V3", "/REGULATORS/PG_BRIDGE_3V3", "/REGULATORS/FB_BRIDGE_1V1", "/REGULATORS/RT_BRIDGE_1V1", "/REGULATORS/PG_BRIDGE_1V1"):
    assert any(x.GetNetname() == name for x in vias), name
'''
    subprocess.run([PYTHON, "-c", probe], cwd=ROOT, check=True)
    print("Phase 15 U4/U5-control regression: PASS; 35 vias; 254 unrouted items")

if __name__ == "__main__": main()
