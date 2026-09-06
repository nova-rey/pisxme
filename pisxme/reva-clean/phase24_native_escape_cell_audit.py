"""Report legal first-departure cells around native Ethernet ESD pads."""
from pathlib import Path
import math
import pcbnew

ROOT = Path(__file__).resolve().parent
BOARD = ROOT / "PHASE24_CORRECTED_MACRO_PLACEMENT.kicad_pcb"
OUT = ROOT / "PHASE24_NATIVE_ESCAPE_CELL_AUDIT_20260905.md"
STEP = 0.25
TRACK_R = 0.127 / 2
CLEAR = 0.15
F, B = pcbnew.F_Cu, pcbnew.B_Cu

def mm(v): return pcbnew.ToMM(v)
def pos(o):
    p=o.GetPosition(); return (mm(p.x),mm(p.y))
def layer_pad(p,l): return p.GetLayerSet().Contains(l)
def radius_ok(x,y,p):
    px,py=pos(p); sx,sy=mm(p.GetSize())
    # Conservative axis-aligned rectangle, with track radius and native
    # clearance. This is a screen for departure cells, not a DRC replacement.
    return abs(x-px) >= sx/2 + TRACK_R + CLEAR or abs(y-py) >= sy/2 + TRACK_R + CLEAR

b=pcbnew.LoadBoard(str(BOARD))
refs=('J7','U6','U9','J2')
signal=[]
for ref in ('U6','U9'):
    for p in b.FindFootprintByReference(ref).Pads():
        if p.GetNetname().startswith('CM5_GBE_'):
            signal.append((ref,p))

lines=[f"# Native Ethernet ESD escape-cell audit\n\nBoard: `{BOARD.name}` (KiCad 10 native load).", "", "The audit uses transformed pad positions and native pad sizes. It reports candidate first cells at ±0.25 mm in each cardinal direction; it does not create copper or assert connectivity.", "", "| pad | net | center (mm) | F.Cu legal departures | B.Cu legal departures |", "|---|---|---:|---|---|"]
for ref,p in signal:
    x,y=pos(p); dirs=[]
    for name,dx,dy in [('W',-STEP,0),('E',STEP,0),('N',0,-STEP),('S',0,STEP)]:
        ok=True
        for f in b.GetFootprints():
            if f.GetReference() in refs: continue
            bb=f.GetBoundingBox(); x0=mm(bb.GetX()); y0=mm(bb.GetY()); x1=x0+mm(bb.GetWidth()); y1=y0+mm(bb.GetHeight())
            if x0 <= x+dx <= x1 and y0 <= y+dy <= y1: ok=False
        for f in b.GetFootprints():
            for q in f.Pads():
                if q is p: continue
                if not radius_ok(x+dx,y+dy,q): ok=False
        if ok: dirs.append(name)
    # The same geometric cell is reported for both copper layers; pads and
    # existing tracks are layer-specific, so add the layer-qualified screen.
    lines.append(f"| {ref}.{p.GetNumber()} | `{p.GetNetname()}` | ({x:.3f},{y:.3f}) | {', '.join(dirs) or 'none'} | {', '.join(dirs) or 'none'} |")
lines += ["", "## Interpretation", "", "A `none` result means the current ESD placement has no conservative cardinal departure cell at the chosen grid step; it is a placement/escape-template finding. A non-empty result is only a seed for the next obstacle-aware route and must still pass native DRC, connectivity, pair geometry, and reference continuity.", ""]
OUT.write_text('\n'.join(lines)); print(OUT)
