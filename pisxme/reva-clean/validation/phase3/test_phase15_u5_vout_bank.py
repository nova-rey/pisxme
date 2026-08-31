"""Focused native regression for the U5 1.1 V output capacitor bank."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
PYTHON = "/home/nyx/pisxme-toolchain-environment/bin/pisxme-pcbnew-python"
BOARD = ROOT / "ACREAGE_U5_VOUT_PHASE15.kicad_pcb"
REPORT = ROOT / "ACREAGE_U5_VOUT_PHASE15-drc.rpt"


def main():
    subprocess.run([PYTHON, "phase15_thermal_vias.py"], cwd=ROOT, check=True)
    subprocess.run([PYTHON, "phase15_power_escape.py"], cwd=ROOT, check=True)
    subprocess.run([PYTHON, "phase15_u3_controls.py"], cwd=ROOT, check=True)
    subprocess.run([PYTHON, "phase15_u4_u5_controls.py"], cwd=ROOT, check=True)
    subprocess.run([PYTHON, "phase15_u5_vout_bank.py"], cwd=ROOT, check=True)
    subprocess.run(["xvfb-run", "-a", "kicad-cli", "pcb", "drc",
                    "--exit-code-violations", "--output", REPORT.name,
                    str(BOARD)], cwd=ROOT, check=False)
    report = REPORT.read_text()
    assert "[clearance]" not in report
    assert "[shorting_items]" not in report
    assert "[tracks_crossing]" not in report
    assert report.count("[unconnected_items]") == 230
    assert "Pad 8 [/REGULATORS/BRIDGE_1V1] of U5" not in report
    assert "Pad 9 [/REGULATORS/BRIDGE_1V1] of U5" not in report
    probe = r'''
import pcbnew
b = pcbnew.LoadBoard("ACREAGE_U5_VOUT_PHASE15.kicad_pcb")
out = "/REGULATORS/BRIDGE_1V1"
refs = [f"C{i}" for i in range(26, 42)]
for ref in refs:
    f = b.FindFootprintByReference(ref)
    assert any(p.GetNetname() == out for p in f.Pads()), ref
vias = [x for x in b.GetTracks() if x.Type() == pcbnew.PCB_VIA_T]
    assert len(vias) == 72
    assert sum(x.GetNetname() == out for x in vias) == 21
assert sum(x.GetNetname() == "POWER_GND" for x in vias) == 28
assert any(x.GetNetname() == out and x.GetLayer() == pcbnew.In2_Cu
           for x in b.GetTracks())
'''
    subprocess.run([PYTHON, "-c", probe], cwd=ROOT, check=True)
    print("Phase 15 U5 VOUT-bank regression: PASS; both VOUT lands tied; 71 vias; 230 unrouted items")


if __name__ == "__main__":
    main()
