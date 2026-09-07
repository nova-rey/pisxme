"""Disposable 90-degree U1 placement alternative from the V8 baseline."""
from pathlib import Path
import re
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_ROTATED_SUPPORT_RELOCATION_V8.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_ROTATE_U1_90_V15.kicad_pcb"
SCRUB = HERE / ".phase24_rotate_u1_90_scrubbed_v15.kicad_pcb"
NETS = {"RTL_1V1", "RTL_3V3", "RTL_5V", "RSET", "XTAL_IN", "XTAL_OUT",
        "PEDET", "CLKREQ_N", "RESET_N", "PERST_N", "SPICS", "SPISO",
        "SPISO3", "SPICLK", "SPISI"}


def main():
    text = BASE.read_text(); spans = []
    for match in re.finditer(r"\n\s+\((segment|via)\b", text):
        start = match.start() + 1; depth = 0
        for i in range(start, len(text)):
            if text[i] == "(": depth += 1
            elif text[i] == ")":
                depth -= 1
                if depth == 0:
                    block = text[start:i + 1]
                    points = [(float(x), float(y)) for x, y in re.findall(
                        r"\((?:start|end|at)\s+([-\d.]+)\s+([-\d.]+)", block)]
                    if any(n in block for n in NETS) and any(
                            80 <= x <= 120 and 55 <= y <= 82 for x, y in points):
                        spans.append((start, i + 1))
                    break
    for start, end in reversed(spans): text = text[:start] + text[end:]
    SCRUB.write_text(text)
    board = pcbnew.LoadBoard(str(SCRUB))
    u1 = board.FindFootprintByReference("U1")
    exposed = u1.FindPadByNumber("69").GetPosition()
    u1.SetOrientationDegrees(90)
    rotated = u1.FindPadByNumber("69").GetPosition()
    u1.SetPosition(pcbnew.VECTOR2I(u1.GetPosition().x + exposed.x - rotated.x,
                                   u1.GetPosition().y + exposed.y - rotated.y))
    board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
