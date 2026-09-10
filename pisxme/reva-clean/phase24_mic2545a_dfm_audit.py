"""Audit the saved MIC2545A disposable footprint against Microchip's land pattern."""
from pathlib import Path
import json
import pcbnew

HERE = Path(__file__).resolve().parent
BOARD = HERE / "PHASE24_MIC2545A_SUPPORT_FIXTURE.kicad_pcb"
REPORT = HERE / "PHASE24_MIC2545A_DFM_AUDIT.json"
TOL = 0.01

b = pcbnew.LoadBoard(str(BOARD))
fp = b.FindFootprintByReference("U3")
assert fp, "missing U3"
pads = {int(p.GetNumber()): p for p in fp.Pads()}
assert set(pads) == set(range(1, 9)), f"unexpected pad set: {sorted(pads)}"

def mm(v):
    return pcbnew.ToMM(v)

xs = {round(mm(pads[n].GetPosition().x), 3) for n in range(1, 9)}
ys = sorted(round(mm(pads[n].GetPosition().y), 3) for n in range(1, 5))
assert len(xs) == 2 and round(max(xs) - min(xs), 3) == 5.4, xs
assert [round(ys[i + 1] - ys[i], 3) for i in range(3)] == [1.27] * 3, ys

for number, p in pads.items():
    assert p.GetAttribute() == pcbnew.PAD_ATTRIB_SMD, f"pad {number} not SMD"
    assert p.IsOnLayer(pcbnew.F_Cu), f"pad {number} not F.Cu"
    assert round(mm(p.GetSize().x), 3) == 1.55, (number, mm(p.GetSize().x))
    assert round(mm(p.GetSize().y), 3) == 0.60, (number, mm(p.GetSize().y))
    assert abs(mm(p.GetLocalSolderMaskMargin())) < TOL
    assert round(mm(p.GetLocalSolderPasteMargin()), 3) == -0.05
    assert abs(p.GetLocalSolderPasteMarginRatio()) < TOL

layers = {g.GetLayer() for g in fp.GraphicalItems()}
assert pcbnew.F_CrtYd in layers, "missing F.CrtYd geometry"
assert pcbnew.F_SilkS in layers, "missing F.SilkS geometry"

REPORT.write_text(json.dumps({
    "board": BOARD.name,
    "footprint": "U3",
    "device": "MIC2545A-1YM",
    "source": "Microchip DS20006921A, Drawing C04-2057-3BX Rev K",
    "pitch_mm": 1.27,
    "row_spacing_mm": 5.40,
    "pad_length_mm": 1.55,
    "pad_width_mm": 0.60,
    "solder_mask_margin_mm": 0.0,
    "paste_margin_mm": -0.05,
    "courtyard_and_silkscreen": "PRESENT",
    "verdict": "PASS",
}, indent=2) + "\n")
print("MIC2545A saved-board DFM audit: PASS")
print(f"wrote {REPORT}")
