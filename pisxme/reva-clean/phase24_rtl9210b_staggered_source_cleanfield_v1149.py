"""V1149: exact native removal of rail source branches, then staggered XTAL sources."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_XTALOUT_VIA_CLEARANCE_V1144.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_STAGGERED_SOURCE_CLEANFIELD_V1149.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return p.x/1e6,p.y/1e6
def pad(b,r,n): return next(p for f in b.GetFootprints() if f.GetReference()==r for p in f.Pads() if p.GetPadName()==n)
def norm(a,z): return frozenset(((round(a[0],4),round(a[1],4)),(round(z[0],4),round(z[1],4))))
def ends(item):
    if type(item).__name__=='PCB_VIA':
        p=(item.GetX()/1e6,item.GetY()/1e6); return p,p
    return xy(item.GetStart()),xy(item.GetEnd())
def tr(b,code,l,ps):
    for a,z in zip(ps,ps[1:]):
        q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNetCode(code);b.Add(q)
def via(b,code,p):
    q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNetCode(code);b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); codes={n:b.FindNet(n).GetNetCode() for n in ('RTL_3V3','RTL_1V1','XTAL_IN','XTAL_OUT')}
remove={
codes['RTL_3V3']:{norm((94.05,66.8),(93.0,66.8)),norm((93.0,66.8),(93.5,64.8)),norm((93.5,64.8),(100.5,64.8)),norm((93.0,68.4),(100.9,68.4)),norm((93.0,66.8),(93.0,68.4)),norm((93.5,64.8),(93.5,64.8))},
codes['RTL_1V1']:{norm((94.05,68.0),(92.8,68.0)),norm((92.8,68.0),(92.8,69.3)),norm((92.8,69.3),(92.8,75.0)),norm((92.8,69.3),(92.8,69.3))}}
for item in list(b.GetTracks()):
    code=item.GetNetCode(); a,z=ends(item)
    if code in remove and norm(a,z) in remove[code]: b.Remove(item)
v3,v1,ni,no=(codes[n] for n in ('RTL_3V3','RTL_1V1','XTAL_IN','XTAL_OUT'))
# Move rail transitions to leave the staggered crystal source vias room.
tr(b,v3,F,[(94.05,66.8),(92.0,66.8),(92.0,65.0)]);via(b,v3,(92.0,65.0));tr(b,v3,B,[(92.0,65.0),(100.5,65.0),(100.5,64.0)])
tr(b,v1,F,[(94.05,68.0),(95.0,68.0)]);via(b,v1,(95.0,68.0));tr(b,v1,B,[(95.0,68.0),(95.0,75.0),(102.5,75.0)])
# Source-only proof: XTAL_IN transitions at x=91.0, XTAL_OUT remains V1144.
tr(b,ni,F,[(94.05,67.2),(93.0,67.2),(92.0,67.2),(90.5,66.8)]);via(b,ni,(90.5,66.8));tr(b,ni,B,[(90.5,66.8),(90.5,65.8)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
