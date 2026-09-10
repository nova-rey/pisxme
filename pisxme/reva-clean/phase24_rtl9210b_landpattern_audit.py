"""Bounded DFM audit of the corrected RTL9210B-CG QFN qualification land pattern."""
from pathlib import Path
import json
import pcbnew

HERE = Path(__file__).resolve().parent
BOARD = HERE / "PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED.kicad_pcb"
MOD = HERE / "authority-inventory/rtl9210b/RTL9210B-CG_QUALIFICATION.kicad_mod"
REPORT = HERE / "PHASE24_RTL9210B_LANDPATTERN_AUDIT.json"

board = pcbnew.LoadBoard(str(BOARD))
fp = board.FindFootprintByReference("U1")
assert fp, "U1 missing"
pads = list(fp.Pads())
assert len(pads) == 69, f"expected 69 pads, found {len(pads)}"
assert all(p.GetAttribute() == pcbnew.PAD_ATTRIB_SMD for p in pads), "non-SMD pad present"
assert all(p.GetLayerSet().Contains(pcbnew.F_Cu) for p in pads), "pad not on F.Cu"
ep = fp.FindPadByNumber("69")
assert ep and ep.GetNetname() == "GND", "exposed pad 69 is not GND"
assert abs(pcbnew.ToMM(ep.GetSize().x) - 4.8) < 0.01
assert abs(pcbnew.ToMM(ep.GetSize().y) - 4.8) < 0.01
assert MOD.exists() and '(attr smd)' in MOD.read_text(errors="replace")
assert 'through_hole' not in MOD.read_text(errors="replace")

for number in range(1, 69):
    p = fp.FindPadByNumber(str(number))
    assert p and p.GetAttribute() == pcbnew.PAD_ATTRIB_SMD, f"pad {number} invalid"

report = {
    "board": BOARD.name,
    "footprint": fp.GetValue(),
    "pad_count": len(pads),
    "all_pads_smd": True,
    "all_pads_fcu": True,
    "exposed_pad": {"number": "69", "net": ep.GetNetname(), "size_mm": [4.8, 4.8]},
    "source_module": MOD.name,
    "source_attr_smd": True,
    "source_through_hole_metadata_absent": True,
    "verdict": "PASS_ISOLATED_LANDPATTERN_DFM",
}
REPORT.write_text(json.dumps(report, indent=2) + "\n")
print("RTL9210B-CG corrected QFN land-pattern DFM audit PASS")
print("69 pads, all SMD/F.Cu; exposed pad 69 is GND, 4.8 x 4.8 mm")
print(f"wrote {REPORT}")
