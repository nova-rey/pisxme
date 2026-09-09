"""V34: disposable four-net orthogonal CM5 USB3 source-field regeneration."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_VBUS_LEFT_V32_FILLED.kicad_pcb'
OUT=R/'PHASE24_STORAGE_CM5_USB4_SOURCE_V34.kicad_pcb'
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(b,r,n):
 q=b.FindFootprintByReference(r).FindPadByNumber(str(n)).GetPosition();return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
b=pcbnew.LoadBoard(str(BASE))
def route(name,padnum,mid,end,tail):
 n=b.FindNet(name)
 for t in list(b.GetTracks()):
  if t.GetNetCode()==n.GetNetCode():b.RemoveNative(t)
 def seg(a,z,l):
  t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.15));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
 def via(q):
  v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.55));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
 seg(xy(b,'J7',padnum),mid,pcbnew.F_Cu);seg(mid,end,pcbnew.F_Cu);via(end);seg(end,tail,pcbnew.B_Cu)
route('CM5_USB3_RX_N','128',(67.5,103.9),(67.5,88),(155,137.8))
route('CM5_USB3_RX_P','130',(72.5,104.3),(72.5,90),(157,137.4))
route('CM5_USB3_TX_N','140',(65.5,106.3),(65.5,92),(159,136.2))
route('CM5_USB3_TX_P','142',(74.5,106.7),(74.5,94),(161,135.8))
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
