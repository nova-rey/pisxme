"""Derive a transformed RTL9210B QFN escape-cell map from native KiCad pads."""
from pathlib import Path
import math
import sys
import pcbnew


def mm(value):
    return value / 1_000_000.0


def main(path):
    board = pcbnew.LoadBoard(str(path))
    fp = board.FindFootprintByReference("U1")
    if fp is None:
        raise SystemExit("missing U1")
    ep = fp.FindPadByNumber("69").GetPosition()
    lines = [f"PCB={path}", f"EXPOSED_PAD={mm(ep.x):.4f},{mm(ep.y):.4f}"]
    wanted = {"13", "14", "16", "17", "18", "19", "20", "21", "22",
              "23", "24", "25", "33", "34", "36", "39", "40", "50",
              "51", "52", "53", "54", "55", "60", "61", "62", "63",
              "64", "65", "66", "67", "68"}
    pads = sorted((p for p in fp.Pads() if p.GetNumber() in wanted),
                  key=lambda p: (p.GetPosition().y, p.GetPosition().x))
    for pad in pads:
        p = pad.GetPosition(); dx = p.x - ep.x; dy = p.y - ep.y
        norm = math.hypot(dx, dy) or 1.0
        # The pad center to package-center vector identifies the outward side.
        ox, oy = dx / norm, dy / norm
        lines.append(
            f"{pad.GetNumber()} {pad.GetNetname()} center={mm(p.x):.4f},{mm(p.y):.4f} "
            f"size={mm(pad.GetSize().x):.4f},{mm(pad.GetSize().y):.4f} "
            f"orientation={pad.GetOrientation().AsDegrees():.1f} "
            f"outward={ox:.4f},{oy:.4f}")
    out = Path(path).with_name("PHASE24_RTL9210B_ESCAPE_CELL_MAP_NATIVE_V15.txt")
    out.write_text("\n".join(lines) + "\n")
    print(out)


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name(
        "PHASE24_RTL9210B_ROTATE_U1_90_V15.kicad_pcb"))
