"""Record native-loaded geometry differences between V735 and V1279."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
CASES = {
    "V735": H / "PHASE24_RTL9210B_SPI_U1_ROTATE90_SPICS_SPISO_V735.kicad_pcb",
    "V1279": H / "PHASE24_RTL9210B_XTAL_IN_LIVE_PAD_V1279.kicad_pcb",
}
OUT = H / "PHASE24_RTL9210B_V735_V1279_GEOMETRY_COMPARISON.md"

def mm(v): return round(pcbnew.ToMM(v), 3)
def rows(board):
    out = []
    for f in board.GetFootprints():
        if f.GetReference() != "U1": continue
        for p in f.Pads():
            if p.GetNumber() in {"8", "13", "14", "18", "19", "20", "22", "23", "24", "25", "33", "34", "51", "52", "53", "54", "64", "65", "67", "68"}:
                q = p.GetPosition()
                out.append((p.GetNumber(), p.GetNetname(), mm(q.x), mm(q.y)))
    return sorted(out, key=lambda x: int(x[0]))

lines = ["# RTL9210B V735/V1279 native geometry comparison", "",
         "Coordinates are read after KiCad transforms from native PCB pads; no schematic ordering or synthetic connectivity is used.", ""]
for name, path in CASES.items():
    b = pcbnew.LoadBoard(str(path))
    u = next(f for f in b.GetFootprints() if f.GetReference() == "U1")
    lines += [f"## {name}", f"- PCB: `{path.name}`",
              f"- U1 position: ({mm(u.GetPosition().x)}, {mm(u.GetPosition().y)}) mm",
              f"- U1 orientation: {u.GetOrientationDegrees()} degrees", "",
              "| Pad | Net | X (mm) | Y (mm) |", "|---:|---|---:|---:|"]
    lines += [f"| {n} | {net or '(unassigned)'} | {x} | {y} |" for n, net, x, y in rows(b)]
    lines.append("")
lines += ["## Independent evidence", "",
          "- V735 native DRC report: zero DRC violations (its unconnected-pad findings remain explicitly open).",
          "- V735 audit: SPICS and SPISO native endpoints plus source-trace negative controls pass.",
          "- V735 is a rotated-U1 support comparison, not evidence that the current four-lane V1279 routing can be copied without regeneration."]
OUT.write_text("\n".join(lines) + "\n")
print(OUT)
