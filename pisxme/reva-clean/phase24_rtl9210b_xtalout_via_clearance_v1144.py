"""V1144: move the successful V1143 XTAL_OUT transition clear of rail vias."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_QFN_GND_ATTACH_V1123.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_XTALOUT_VIA_CLEARANCE_V1144.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): p=p.GetPosition(); return p.x/1e6,p.y/1e6
def pad(b,r,n): return next(p for f in b.GetFootprints() if f.GetReference()==r for p in f.Pads() if p.GetPadName()==n)
def tr(b,n,l,ps):
    for a,z in zip(ps,ps[1:]):
        q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,p):
    q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('XTAL_OUT');u=xy(pad(b,'U1','54'));y=xy(pad(b,'Y1','2'));c=xy(pad(b,'C2','1'))
tr(b,n,F,[u,(93.4,67.6),(91.5,67.6)]);via(b,n,(91.5,67.6))
tr(b,n,B,[(91.5,67.6),(88.0,68.0),(88.0,58.0)]);via(b,n,(88.0,58.0))
tr(b,n,F,[(88.0,58.0),(y[0],58.0),y,(90.5,59.0),(90.5,60.5),c])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT,'U1.54',u,'Y1.2',y,'C2.1',c)
