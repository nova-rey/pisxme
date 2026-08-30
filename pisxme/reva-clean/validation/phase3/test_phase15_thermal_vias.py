from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
PYTHON = "/home/nyx/pisxme-toolchain-environment/bin/pisxme-pcbnew-python"


def main():
    result = subprocess.run([PYTHON, str(ROOT / "phase15_thermal_vias.py")],
                            cwd=ROOT, check=True, text=True,
                            capture_output=True)
    assert "12 ordinary 0.50/0.30" in result.stdout
    probe = '''
import pcbnew
b = pcbnew.LoadBoard("ACREAGE_REGULATOR_PHASE15.kicad_pcb")
vias = [x for x in b.GetTracks() if x.Type() == pcbnew.PCB_VIA_T]
assert len(vias) == 12
thermal = vias
assert all(v.GetNetname() == "/REGULATORS/POWER_GND" for v in thermal)
assert all(v.GetLayer() == pcbnew.F_Cu and
           v.GetLayerSet().Contains(pcbnew.In1_Cu) and
           v.GetLayerSet().Contains(pcbnew.B_Cu) for v in thermal)
assert all(v.GetWidth(pcbnew.F_Cu) == pcbnew.FromMM(0.50) for v in thermal)
assert all(v.GetDrill() == pcbnew.FromMM(0.30) for v in thermal)
assert all(z.IsFilled() for z in b.Zones())
'''
    subprocess.run([PYTHON, "-c", probe], cwd=ROOT, check=True)
    print("Phase 15 thermal-via regression: PASS")


if __name__ == "__main__":
    main()
