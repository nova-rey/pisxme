"""V1152: separate XTAL_IN and XTAL_OUT B.Cu lanes from V1144."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / 'PHASE24_RTL9210B_XTALOUT_VIA_CLEARANCE_V1144.kicad_pcb'
OUT = H / 'PHASE24_RTL9210B_XTAL_LANE_SEPARATION_V1152.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.20)

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p): return p.x / 1e6, p.y / 1e6
def pad(board, ref, name):
    return next(p for f in board.GetFootprints() if f.GetReference() == ref
                for p in f.Pads() if p.GetPadName() == name)
def tr(board, code, layer, points):
    for a, z in zip(points, points[1:]):
        q = pcbnew.PCB_TRACK(board); q.SetStart(P(*a)); q.SetEnd(P(*z))
        q.SetLayer(layer); q.SetWidth(W); q.SetNetCode(code); board.Add(q)
def via(board, code, point):
    q = pcbnew.PCB_VIA(board); q.SetPosition(P(*point));
    q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3))
    q.SetLayerPair(F, B); q.SetNetCode(code); board.Add(q)

b = pcbnew.LoadBoard(str(BASE))
co = b.FindNet('XTAL_OUT').GetNetCode()
ci = b.FindNet('XTAL_IN').GetNetCode()
old = [item for item in list(b.GetTracks()) if item.GetNetCode() == co]
assert old, 'V1144 XTAL_OUT copper not found'
for item in old:
    b.Remove(item)
assert not [item for item in b.GetTracks() if item.GetNetCode() == co], 'XTAL_OUT removal incomplete'

uout = xy(pad(b, 'U1', '54').GetPosition())
uin = xy(pad(b, 'U1', '53').GetPosition())
# XTAL_OUT uses x=86.0 B.Cu; XTAL_IN uses x=87.5 B.Cu.
tr(b, co, F, [uout, (93.4, 67.6), (91.5, 67.6)])
via(b, co, (91.5, 67.6))
tr(b, co, B, [(91.5, 67.6), (86.0, 68.0), (86.0, 58.0)])
via(b, co, (86.0, 58.0))
tr(b, co, F, [(86.0, 58.0), (89.4, 59.0), (90.5, 59.0),
              (90.5, 60.5), (91.0, 62.0)])

tr(b, ci, F, [uin, (93.0, 67.2), (90.5, 66.8)])
via(b, ci, (90.5, 66.8))
tr(b, ci, B, [(90.5, 66.8), (87.5, 68.0), (87.5, 75.0),
              (85.5, 75.0), (85.5, 62.0)])
via(b, ci, (85.5, 62.0))
tr(b, ci, F, [(85.5, 62.0), (86.5, 61.0), (87.0, 60.0),
              (87.0, 59.0), (84.0, 59.0)])

b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT))
print(OUT, 'removed XTAL_OUT items', len(old), 'U1.53', uin, 'U1.54', uout)
