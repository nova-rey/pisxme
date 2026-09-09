"""Shifted CM5IO-style USB3 escape around the actual SXM2 courtyard."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_NETLIST_REGENERATED_V3.kicad_pcb'; OUT=R/'PHASE24_STORAGE_USB3_CM5IO_SHIFTED_V1.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.15)
JOBS=(('CM5_USB3_RX_N','128','16',(73,100),(145,100)),('CM5_USB3_RX_P','130','15',(75,104),(147,104)),('CM5_USB3_TX_N','140','12',(77,108),(149,108)),('CM5_USB3_TX_P','142','11',(79,112),(151,112)))
def V(x,y):return pcbnew.VECTOR2I_MM(x,y)
def xy(p):q=p.GetPosition();return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def via(b,n,x,y):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(x,y));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def tr(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
b=pcbnew.LoadBoard(str(BASE));j=b.FindFootprintByReference('J7');u=b.FindFootprintByReference('U12')
names={x[0] for x in JOBS}
for t in list(b.GetTracks()):
 if t.GetNetname() in names:b.RemoveNative(t)
for name,jp,up,sv,tv in JOBS:
 n=b.FindNet(name); src=xy(j.FindPadByNumber(jp)); dst=xy(u.FindPadByNumber(up)); sx,sy=sv;tx,ty=tv
 tr(b,n,F,[src,(sx,src[1]),sv]);via(b,n,*sv)
 tr(b,n,B,[sv,(tx,sy)]);via(b,n,*tv)
 tr(b,n,F,[tv,(tx,dst[1]),dst])
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
