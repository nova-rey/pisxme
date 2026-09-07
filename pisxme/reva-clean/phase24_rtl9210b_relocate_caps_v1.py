"""Disposable coherent rail-cap relocation for the moved RTL9210B island."""
from pathlib import Path
import re
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SUPPORT_RELOCATION_ROUTE_V2.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SUPPORT_RELOCATION_CAPS_V1.kicad_pcb"
SCRUBBED = HERE / ".phase24_caps_v1_scrubbed.kicad_pcb"
DX, DY = -10.0, 18.0

def main():
    text = BASE.read_text(); spans = []
    for m in re.finditer(r"\n\s+\((segment|via)\b", text):
        start = m.start() + 1; depth = 0
        for i in range(start, len(text)):
            if text[i] == "(": depth += 1
            elif text[i] == ")":
                depth -= 1
                if depth == 0:
                    block = text[start:i + 1]
                    pts = [(float(x), float(y)) for x, y in re.findall(
                        r'\((?:start|end|at)\s+([-\d.]+)\s+([-\d.]+)', block)]
                    if ('RTL_1V1' in block and
                        (any(y <= 42 and x >= 104 for x, y in pts) or
                         (m.group(1) == "segment" and
                          all(x >= 103 and y >= 70 for x, y in pts)))):
                        spans.append((start, i + 1))
                    break
    for a, z in reversed(spans): text = text[:a] + text[z:]
    SCRUBBED.write_text(text)
    board = pcbnew.LoadBoard(str(SCRUBBED))
    delta = pcbnew.VECTOR2I(int(DX * 1e6), int(DY * 1e6))
    for ref in ("C3", "C4", "C5"):
        fp = next(x for x in board.GetFootprints()
                  if str(x.GetReference()) == ref)
        q = fp.GetPosition()
        fp.SetPosition(pcbnew.VECTOR2I(q.x + delta.x, q.y + delta.y))
    net = board.FindNet("RTL_1V1")
    def add_seg(a, z, layer):
        t = pcbnew.PCB_TRACK(board); t.SetStart(pcbnew.VECTOR2I_MM(*a))
        t.SetEnd(pcbnew.VECTOR2I_MM(*z)); t.SetLayer(layer)
        t.SetWidth(pcbnew.FromMM(0.20)); t.SetNet(net)
        t.SetNetCode(net.GetNetCode()); board.Add(t)
    add_seg((103.2, 71.2), (108.0, 71.2), pcbnew.B_Cu)
    add_seg((103.2, 70.4), (103.2, 71.2), pcbnew.B_Cu)
    add_seg((108.0, 71.2), (113.4, 69.0), pcbnew.B_Cu)
    via = pcbnew.PCB_VIA(board); via.SetPosition(pcbnew.VECTOR2I_MM(113.4, 69.0))
    via.SetWidth(pcbnew.FromMM(0.60)); via.SetDrill(pcbnew.FromMM(0.30))
    via.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); via.SetNet(net)
    via.SetNetCode(net.GetNetCode()); board.Add(via)
    board.Save(str(OUT)); print(OUT)

if __name__ == "__main__": main()
