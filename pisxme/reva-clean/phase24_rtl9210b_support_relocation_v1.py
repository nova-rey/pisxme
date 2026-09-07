"""Disposable Path-B class change: move the RTL9210B source/support island.

This is a placement discriminator only.  Copper touching the old local
island is removed so stale coordinates cannot masquerade as a valid route.
Production CAD and Path A are never modified.
"""
from pathlib import Path
import re
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_1V1_CRYSTAL_RSET_STAGED_V4.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SUPPORT_RELOCATION_V1.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
DX, DY = 18.0, 18.0
MOVED = {"U1", "C1", "C2", "R1", "R2", "R3", "Y1"}
LOCAL_NETS = {"RTL_1V1", "RTL_3V3", "RTL_5V", "RSET", "XTAL_IN",
              "XTAL_OUT", "PEDET", "CLKREQ_N", "RESET_N", "PERST_N"}
SCRUBBED = HERE / ".phase24_support_relocation_v1_scrubbed.kicad_pcb"

def point(item):
    if isinstance(item, pcbnew.PCB_VIA):
        q = item.GetPosition()
        return [(q.x / 1e6, q.y / 1e6)]
    return [(q.x / 1e6, q.y / 1e6) for q in (item.GetStart(), item.GetEnd())]

def in_old_local(item):
    return any(62 <= x <= 88 and 45 <= y <= 72 for x, y in point(item))

def scrub_serialized():
    text = BASE.read_text()
    spans = []
    for m in re.finditer(r"\n\s+\((segment|via)\b", text):
        start = m.start() + 1
        depth = 0
        for i in range(start, len(text)):
            if text[i] == "(": depth += 1
            elif text[i] == ")":
                depth -= 1
                if depth == 0:
                    block = text[start:i + 1]
                    names = re.findall(r'\(net "([^"]+)"\)', block)
                    coords = [(float(x), float(y)) for x, y in
                              re.findall(r'\((?:start|end|at)\s+([-\d.]+)\s+([-\d.]+)', block)]
                    if any(n in LOCAL_NETS for n in names) and any(
                            62 <= x <= 88 and 45 <= y <= 72 for x, y in coords):
                        spans.append((start, i + 1))
                    break
    for a, z in reversed(spans):
        text = text[:a] + text[z:]
    SCRUBBED.write_text(text)

def main():
    scrub_serialized()
    board = pcbnew.LoadBoard(str(SCRUBBED))
    delta = pcbnew.VECTOR2I_MM(DX, DY)
    for ref in MOVED:
        fp = next((item for item in board.GetFootprints()
                   if str(item.GetReference()) == ref), None)
        if fp is None:
            raise RuntimeError(f"missing footprint {ref}")
        q = fp.GetPosition()
        fp.SetPosition(pcbnew.VECTOR2I(q.x + int(DX * 1e6),
                                       q.y + int(DY * 1e6)))
    board.BuildListOfNets()
    board.Save(str(OUT))
    print(OUT)

if __name__ == "__main__":
    main()
