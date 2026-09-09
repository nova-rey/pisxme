"""V1150: source-only XTAL_IN escape with local 3V3/RSET departures removed."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_XTALOUT_VIA_CLEARANCE_V1144.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_XTALIN_SOURCE_ONLY_V1150.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return p.x/1e6,p.y/1e6
def norm(a,z): return frozenset((tuple(round(v,4) for v in a),tuple(round(v,4) for v in z)))
def ends(item):
    if type(item).__name__=='PCB_VIA':
        p=(item.GetX()/1e6,item.GetY()/1e6); return p,p
    return xy(item.GetStart()),xy(item.GetEnd())
def pad(b,r,n): return next(p for f in b.GetFootprints() if f.GetReference()==r for p in f.Pads() if p.GetPadName()==n)
def tr(b,code,layer,ps):
    for a,z in zip(ps,ps[1:]):
        q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(layer);q.SetWidth(W);q.SetNetCode(code);b.Add(q)
def via(b,code,p):
    q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNetCode(code);b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); names=('RTL_3V3','RSET','XTAL_IN'); codes={n:b.FindNet(n).GetNetCode() for n in names}
targets={
codes['RTL_3V3']:{norm((94.05,66.8),(93.0,66.8)),norm((93.0,66.8),(93.0,68.4)),norm((93.0,68.4),(100.9,68.4)),norm((93.0,66.8),(93.0,66.8))},
codes['RSET']:{norm((94.8,66.05),(92.5,66.05)),norm((92.5,66.05),(92.5,64.0)),norm((92.5,64.0),(88.0,64.0)),norm((88.0,64.0),(88.0,65.0))}}
to_remove=[]
for item in list(b.GetTracks()):
    if item.GetNetCode() in targets and norm(*ends(item)) in targets[item.GetNetCode()]: to_remove.append(item)
assert len(to_remove)>=5, f'expected local 3V3/RSET branches, found {len(to_remove)}'
for item in to_remove: b.Remove(item)
ni=codes['XTAL_IN']; u=xy(pad(b,'U1','53').GetPosition())
# Upper source departure is measured from the saved native pad; no support path is implied here.
tr(b,ni,F,[u,(93.0,67.2),(90.5,66.8)]);via(b,ni,(90.5,66.8));tr(b,ni,B,[(90.5,66.8),(90.5,68.8)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT,'removed',len(to_remove),'U1.53',u)
