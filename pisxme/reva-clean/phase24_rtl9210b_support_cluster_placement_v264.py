"""V264: scrub support copper, then move the coherent RTL9210B support island."""
from pathlib import Path
import re
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V261.kicad_pcb"
SCRUB = HERE / ".phase24_v264_support_scrubbed.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SUPPORT_CLUSTER_PLACEMENT_SCRUBBED_V264.kicad_pcb"
NETS = {"RTL_1V1", "RTL_3V3", "RTL_5V", "RSET", "XTAL_IN", "XTAL_OUT",
        "PEDET", "CLKREQ_N", "SPICS", "SPISO", "SPISI", "SPICLK", "SPISO3"}
MOVES = {"R2": (94.0, 53.0), "R3": (96.0, 53.0), "C3": (102.5, 53.0),
         "C4": (104.5, 53.0), "Y1": (91.5, 62.0), "C1": (92.8, 63.5),
         "C2": (92.8, 65.0), "R1": (94.0, 69.5), "U2": (87.5, 70.0)}


def scrub(text):
    spans = []
    for match in re.finditer(r"^\t\((?:segment|via)\b", text, re.MULTILINE):
        depth = 0
        end = None
        for index in range(match.start(), len(text)):
            if text[index] == "(":
                depth += 1
            elif text[index] == ")":
                depth -= 1
                if depth == 0:
                    end = index + 1
                    break
        block = text[match.start():end]
        if any(f'(net "{net}")' in block for net in NETS):
            spans.append((match.start(), end))
    for start, end in reversed(spans):
        text = text[:start] + text[end:]
    return text


def main():
    SCRUB.write_text(scrub(BASE.read_text()))
    board = pcbnew.LoadBoard(str(SCRUB))
    for ref, (x, y) in MOVES.items():
        footprint = board.FindFootprintByReference(ref)
        if not footprint:
            raise RuntimeError(f"missing footprint {ref}")
        footprint.SetPosition(pcbnew.VECTOR2I_MM(x, y))
    board.BuildListOfNets()
    board.Save(str(OUT))
    print(OUT)


if __name__ == "__main__":
    main()
