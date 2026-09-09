"""V33: orthogonal staggered CM5 USB3 RX source escape."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_VBUS_LEFT_V32_FILLED.kicad_pcb'
OUT=R/'PHASE24_STORAGE_CM5_USB_RX_ESCAPE_V33.kicad_pcb'
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(b,r,n):
 q=b.FindFootprintByReference(r).FindPadByNumber(str(n)).GetPosition();return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
b=pcbnew.LoadBoard(str(BASE))
def route(name,ref,num,mid,end,tail):
 n=b.FindNet(name)
 for t in list(b.GetTracks()):
  if t.GetNetCode()==n.GetNetCode():b.RemoveNative(t)
 def seg(a,z,l):
  t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.15));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
 def via(q):
  v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.55));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
 seg(xy(b,ref,num),mid,pcbnew.F_Cu);seg(mid,end,pcbnew.F_Cu);via(end);seg(end,tail,pcbnew.B_Cu)
route('CM5_USB3_RX_N','J7','128',(68.5,103.9),(68.5,88.0),(155.0,137.8))
route('CM5_USB3_RX_P','J7','130',(71.5,104.3),(71.5,90.0),(157.0,137.4))
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
