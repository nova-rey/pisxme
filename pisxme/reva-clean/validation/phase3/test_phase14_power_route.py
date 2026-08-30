from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
PCBNEW_PY = "/home/nyx/pisxme-toolchain-environment/bin/pisxme-pcbnew-python"


def main():
    result = subprocess.run([PCBNEW_PY, str(ROOT / "phase14_power_route.py")],
                            cwd=ROOT, check=True, text=True,
                            capture_output=True)
    assert "protected feed zone" in result.stdout
    probe = r'''
import pcbnew
b = pcbnew.LoadBoard("ACREAGE_POWER_PHASE14.kicad_pcb")
zones = {z.GetZoneName(): z for z in b.Zones()}
assert set(zones) == {"V100_PROTECTED_FEED", "V100_RETURN_PLANE_L2", "V100_RETURN_PLANE_L5"}
assert zones["V100_PROTECTED_FEED"].GetNetname() == "12V_PROTECTED"
assert zones["V100_RETURN_PLANE_L2"].GetNetname() == "POWER_GND"
assert zones["V100_RETURN_PLANE_L5"].GetNetname() == "POWER_GND"
assert zones["V100_RETURN_PLANE_L2"].GetLayer() == pcbnew.In1_Cu
assert zones["V100_RETURN_PLANE_L5"].GetLayer() == pcbnew.In4_Cu
assert all(z.IsFilled() for z in zones.values())
q1 = b.FindFootprintByReference("Q1"); q2 = b.FindFootprintByReference("Q2")
j1 = b.FindFootprintByReference("J1")
assert q1 and q2 and j1
assert any(p.GetNetname() == "12V_PROTECTED" for p in q1.Pads())
assert any(p.GetNetname() == "12V_PROTECTED" for p in q2.Pads())
assert sum(p.GetNetname() == "12V_PROTECTED" for p in j1.Pads()) == 130
assert len(list(b.GetTracks())) == 0
'''
    subprocess.run([PCBNEW_PY, "-c", probe], cwd=ROOT, check=True,
                    text=True, capture_output=True)
    print("Phase 14 power-route candidate: PASS; protected zone and two return planes filled")


if __name__ == "__main__":
    main()
