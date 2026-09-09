"""V1148: stagger XTAL source vias after moving adjacent rail departures."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_XTALOUT_VIA_CLEARANCE_V1144.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_STAGGERED_SOURCE_V1148.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): p=p.GetPosition(); return p.x/1e6,p.y/1e6
def pad(b,r,n): return next(p for f in b.GetFootprints() if f.GetReference()==r for p in f.Pads() if p.GetPadName()==n)
def pts(item):
    if hasattr(item,'GetX'): return (item.GetX()/1e6,item.GetY()/1e6),(item.GetX()/1e6,item.GetY()/1e6)
    return xy(item.GetStart()),xy(item.GetEnd())
def tr(b,code,l,ps):
    for a,z in zip(ps,ps[1:]):
        q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNetCode(code);b.Add(q)
def via(b,code,p):
    q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNetCode(code);b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); codes={n:b.FindNet(n).GetNetCode() for n in ('RTL_3V3','RTL_1V1','XTAL_IN','XTAL_OUT')}
# Delete only the two old U1 source departures and their local transitions.
for item in list(b.GetTracks()):
    code=item.GetNetCode(); a,z=pts(item)
    if code==codes['RTL_3V3'] and ((a,z)==((94.05,66.8),(93.0,66.8)) or (a,z)==((93.0,66.8),(93.0,68.4))): b.Remove(item)
    if code==codes['RTL_1V1'] and ((a,z)==((94.05,68.0),(92.8,68.0)) or (a,z)==((92.8,68.0),(92.8,69.3)) or (a,z)==((92.8,69.3),(92.8,75.0))): b.Remove(item)
for item in list(b.GetTracks()):
    if item.GetNetCode() in (codes['RTL_3V3'],codes['RTL_1V1']) and hasattr(item,'GetX'):
        x,y=item.GetX()/1e6,item.GetY()/1e6
        if (x,y) in ((93.0,66.8),(92.8,69.3)): b.Remove(item)
# New rail departures are deliberately outboard.
tr(b,codes['RTL_3V3'],F,[(94.05,66.8),(95.5,66.8)]);via(b,codes['RTL_3V3'],(95.5,66.8));tr(b,codes['RTL_3V3'],B,[(95.5,66.8),(100.5,65.0),(100.5,64.0)])
tr(b,codes['RTL_1V1'],F,[(94.05,68.0),(95.0,68.0)]);via(b,codes['RTL_1V1'],(95.0,68.0));tr(b,codes['RTL_1V1'],B,[(95.0,68.0),(95.0,75.0),(102.5,75.0)])
# Staggered source transitions: XTAL_IN above/left, XTAL_OUT at the accepted V1144 lane.
tr(b,codes['XTAL_IN'],F,[(94.05,67.2),(93.0,67.2),(91.0,66.8)]);via(b,codes['XTAL_IN'],(91.0,66.8))
tr(b,codes['XTAL_OUT'],F,[(94.05,67.6),(93.4,67.6),(91.5,67.6)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
