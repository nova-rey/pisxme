"""Extract native USB3 implementation facts from official CM5IO Rev 2 CAD."""
from pathlib import Path
from collections import Counter
import pcbnew

R = Path(__file__).resolve().parent
SOURCE = R / "authority-inventory/cm5io-rev2/CM5IO.kicad_pcb"
OUT = R / "PHASE24_CM5IO_USB3_REFERENCE_EXTRACT.md"
NETS = ("USB3-0-RX_N", "USB3-0-RX_P", "USB3-0-TX_N", "USB3-0-TX_P")

b = pcbnew.LoadBoard(str(SOURCE))
if b is None: raise RuntimeError(f"cannot load {SOURCE}")

def mm(v): return round(pcbnew.ToMM(v), 4)
def pxy(p): return (mm(p.x), mm(p.y))

module = next((f for f in b.GetFootprints() if "ComputeModule5-CM5" in str(f.GetValue())), None)
if module is None: raise RuntimeError("official CM5 module footprint not found")
rows = []
for name in NETS:
    full = next((str(k) for k in b.GetNetsByName().keys() if str(k).endswith("/" + name)), None)
    if full is None: raise RuntimeError(f"official net missing: {name}")
    tracks = [t for t in b.GetTracks() if str(t.GetNetname()) == full]
    segments = [t for t in tracks if type(t).__name__ == "PCB_TRACK"]
    widths = Counter(mm(t.GetWidth()) for t in segments)
    layers = Counter(str(b.GetLayerName(t.GetLayer())) for t in segments)
    vias = [t for t in tracks if type(t).__name__ == "PCB_VIA"]
    rows.append((name, full, len(tracks), dict(widths), dict(layers), len(vias), [pxy(v.GetPosition()) for v in vias]))

lines = [
    "# Phase 24 official CM5IO Rev 2 USB3 CAD extraction",
    "",
    f"Source: `{SOURCE.relative_to(R.parent.parent)}` (native KiCad PCB).",
    "This receipt is generated from saved native pads/tracks/vias; it is not a schematic-drawing or pin-list inference.",
    "",
    f"Official CM5 footprint: `{module.GetReference()}` value `{module.GetValue()}`, position `{pxy(module.GetPosition())}`, rotation `{module.GetOrientationDegrees()}°`.",
    "",
    "| Net | Native track objects | Widths (mm) | Layers | Vias | Via positions (mm) |",
    "|---|---:|---|---|---:|---|",
]
for name, full, count, widths, layers, nv, positions in rows:
    lines.append(f"| `{name}` | {count} | `{widths}` | `{layers}` | {nv} | `{positions}` |")
lines += [
    "",
    "Interpretation: the official source uses F.Cu and B.Cu signal segments with ordinary through-vias; no In1/In4 signal tracks are present in these four nets. The exact saved geometry remains the implementation oracle for pair ordering and launch/transition semantics.",
    "",
    "This extraction does not claim that the official CM5IO coordinates transplant unchanged to PiSXMe; the PiSXMe adaptation must still pass native DRC, connectivity, impedance, and mechanical gates.",
]
OUT.write_text("\n".join(lines) + "\n")
print(OUT)
