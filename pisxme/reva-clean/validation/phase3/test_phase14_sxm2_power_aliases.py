"""Regression for the explicit Rev-A SXM2 endpoint power expansion."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
PCBNEW_PY = "/home/nyx/pisxme-toolchain-environment/bin/pisxme-pcbnew-python"


def main() -> None:
    subprocess.run([PCBNEW_PY, str(ROOT / "phase14_materialize_pcb.py")],
                   cwd=ROOT, check=True, text=True, capture_output=True)
    probe = r'''
import pcbnew
from collections import Counter
b = pcbnew.LoadBoard("ACREAGE_CANDIDATE.kicad_pcb")
f = b.FindFootprintByReference("J1")
assert f is not None and len(list(f.Pads())) == 400
power_rows = {22,23,25,26,28,29,31,32,34,35,37,38,40}
ground_rows = {21,24,27,30,33,36,39}
cols = set("ABCDEFGHJK")
def row(p):
    return int("".join(c for c in p.GetNumber() if c.isdigit()))
def col(p):
    return "".join(c for c in p.GetNumber() if c.isalpha())
power = [p for p in f.Pads() if row(p) in power_rows and col(p) in cols]
ground = [p for p in f.Pads() if row(p) in ground_rows and col(p) in cols]
assert len(power) == 130 and all(p.GetNetname() == "12V_PROTECTED" for p in power)
assert len(ground) == 70 and all(p.GetNetname() == "/V100_PCIE/V100_GND" for p in ground)
assert not any(p.GetNetname() == "/V100_PCIE/V100_PER0_N" for p in power)
expected = {
 "A2": "/V100_PCIE/V100_PER0_P", "A3": "/V100_PCIE/V100_PER0_N",
 "E7": "/V100_PCIE/V100_REFCLK_P", "F7": "/V100_PCIE/V100_REFCLK_N",
 "G1": "/V100_PCIE/V100_PET0_P", "G2": "/V100_PCIE/V100_PET0_N",
 "E18": "/V100_PCIE/V100_PERST",
}
assert {p.GetNumber(): p.GetNetname() for p in f.Pads() if p.GetNumber() in expected} == expected
print(Counter(p.GetNetname() or "<none>" for p in f.Pads()))
'''
    result = subprocess.run([PCBNEW_PY, "-c", probe], cwd=ROOT,
                            check=True, text=True, capture_output=True)
    print("Phase 14 SXM2 power aliases: PASS; 130 power pads; 70 ground pads; signal pads preserved")


if __name__ == "__main__":
    main()
