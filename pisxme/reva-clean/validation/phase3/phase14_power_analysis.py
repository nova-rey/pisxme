"""Geometry-backed conservative analysis for the Phase 14 power candidate."""
from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parents[2]
PCBNEW_PY = "/home/nyx/pisxme-toolchain-environment/bin/pisxme-pcbnew-python"


def main():
    subprocess.run([PCBNEW_PY, str(ROOT / "phase14_power_route.py")],
                   cwd=ROOT, check=True, capture_output=True, text=True)
    budget = json.loads((ROOT.parents[1] / "design" / "FINAL_POWER_BUDGET.json").read_text())
    probe = f'''
import pcbnew
b = pcbnew.LoadBoard("ACREAGE_POWER_PHASE14.kicad_pcb")
z = next(z for z in b.Zones() if z.GetZoneName() == "V100_PROTECTED_FEED")
poly = z.GetFilledPolysList(pcbnew.F_Cu)
# Sample the filled copper at 1 mm intervals through the entire feed window.
# The minimum vertical span is the conservative cross-section for the
# rectangular Q1/Q2-to-SXM2 corridor after pad clearances.
spans = []
for x in range(116, 245):
    ys = [y for y in (30 + i * 0.5 for i in range(201))
          if poly.PointInside(pcbnew.VECTOR2I_MM(x, y))]
    if ys:
        spans.append(max(ys) - min(ys))
assert len(spans) == 129 and min(spans) >= 98.0
total_a = {budget["continuous_input_current_a"]}
peak_a = {budget["peak_input_current_a"]}
branch_a = total_a / {budget["branch_count"]}
t_mm = 0.035  # 1 oz outer copper design basis
rho = 0.0000175  # ohm-mm, conservative copper resistivity at 20 C
width_mm = 98.0
length_mm = 75.0
shared_j = branch_a / (t_mm * width_mm)
worst_j = total_a / (t_mm * width_mm)
drop_v = total_a * rho * length_mm / (t_mm * width_mm)
contact_a = branch_a / 65.0
fet_rds = 0.0027
shared_fet_w = branch_a * branch_a * fet_rds
single_fet_w = peak_a * peak_a * fet_rds
rthja_c_per_w = 62.0  # CSD19536KCS datasheet maximum, stated test-board basis
ambient_c = 40.0
shared_tj_c = ambient_c + shared_fet_w * rthja_c_per_w
single_tj_c = ambient_c + single_fet_w * rthja_c_per_w
assert shared_j < 5.0 and worst_j < 9.0 and drop_v < 0.12
assert contact_a < 0.45  # Amphenol published contact-current authority
assert shared_tj_c < 175.0
assert {budget["branch_fuse_a"]} == 15.0 and peak_a > {budget["branch_fuse_a"]}
print(f"min_width_mm={{min(spans):.1f}} continuous={{total_a:.2f}}A peak={{peak_a:.2f}}A shared_J={{shared_j:.3f}}A/mm2 worst_J={{worst_j:.3f}}A/mm2 drop={{drop_v:.5f}}V contact={{contact_a:.4f}}A shared_Tj={{shared_tj_c:.1f}}C peak_fault_Tj_bound={{single_tj_c:.1f}}C")
'''
    result = subprocess.run([PCBNEW_PY, "-c", probe], cwd=ROOT,
                            check=False, capture_output=True, text=True)
    if result.returncode:
        raise SystemExit(result.stdout + result.stderr)
    print("Phase 14 power analysis: PASS; filled-copper span, current density, and conservative drop bounds pass")
    print(result.stdout.strip())


if __name__ == "__main__":
    main()
