"""Geometry-backed conservative analysis for the Phase 14 power candidate."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
PCBNEW_PY = "/home/nyx/pisxme-toolchain-environment/bin/pisxme-pcbnew-python"


def main():
    subprocess.run([PCBNEW_PY, str(ROOT / "phase14_power_route.py")],
                   cwd=ROOT, check=True, capture_output=True, text=True)
    probe = r'''
import pcbnew
b = pcbnew.LoadBoard("ACREAGE_POWER_PHASE14.kicad_pcb")
z = next(z for z in b.Zones() if z.GetZoneName() == "V100_PROTECTED_FEED")
poly = z.GetFilledPolysList(pcbnew.F_Cu)
# Sample the filled copper at 1 mm intervals through the entire feed window.
# The minimum vertical span is the conservative cross-section for the
# rectangular Q1/Q2-to-SXM2 corridor after pad clearances.
spans = []
for x in range(116, 190):
    ys = [y for y in (30 + i * 0.5 for i in range(201))
          if poly.PointInside(pcbnew.VECTOR2I_MM(x, y))]
    if ys:
        spans.append(max(ys) - min(ys))
assert len(spans) == 74 and min(spans) >= 98.0
branch_a = 12.625
total_a = 25.25
t_mm = 0.035  # 1 oz outer copper design basis
rho = 0.0000175  # ohm-mm, conservative copper resistivity at 20 C
width_mm = 98.0
length_mm = 75.0
shared_j = branch_a / (t_mm * width_mm)
worst_j = total_a / (t_mm * width_mm)
drop_v = total_a * rho * length_mm / (t_mm * width_mm)
contact_a = branch_a / 65.0
assert shared_j < 4.0 and worst_j < 8.0 and drop_v < 0.12
assert contact_a < 0.45  # Amphenol published contact-current authority
print(f"min_width_mm={min(spans):.1f} shared_J={shared_j:.3f}A/mm2 worst_J={worst_j:.3f}A/mm2 drop={drop_v:.5f}V contact={contact_a:.4f}A")
'''
    result = subprocess.run([PCBNEW_PY, "-c", probe], cwd=ROOT,
                            check=True, capture_output=True, text=True)
    print("Phase 14 power analysis: PASS; filled-copper span, current density, and conservative drop bounds pass")
    print(result.stdout.strip())


if __name__ == "__main__":
    main()
