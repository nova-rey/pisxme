"""V1146: pair XTAL_IN upper source escape with accepted V1144 XTAL_OUT."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_XTALOUT_VIA_CLEARANCE_V1144.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_XTALIN_UPPER_WITH_XTALOUT_V1146.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): p=p.GetPosition(); return p.x/1e6,p.y/1e6
def pad(b,r,n): return next(p for f in b.GetFootprints() if f.GetReference()==r for p in f.Pads() if p.GetPadName()==n)
def tr(b,n,l,ps):
    for a,z in zip(ps,ps[1:]):
        q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,p):
    q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('XTAL_IN');u=xy(pad(b,'U1','53'));y=xy(pad(b,'Y1','1'));c=xy(pad(b,'C1','1'))
tr(b,n,F,[u,(93.0,67.2),(92.5,66.2),(91.5,66.0)]);via(b,n,(91.5,66.0))
tr(b,n,B,[(91.5,66.0),(85.5,66.0),(85.5,62.0)]);via(b,n,(85.5,62.0));tr(b,n,F,[(85.5,62.0),c,y])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT,'U1.53',u,'Y1.1',y,'C1.1',c)
