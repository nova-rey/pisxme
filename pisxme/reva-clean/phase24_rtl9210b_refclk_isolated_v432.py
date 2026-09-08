"""V432: isolate and regenerate RTL9210B REFCLK P/N from native pads."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_CLKREQ_QFN_CLEARANCE_V431.kicad_pcb'; out=H/'PHASE24_RTL9210B_REFCLK_ISOLATED_V432.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(src))
for x in list(b.GetTracks()):
 if x.GetNetname() in {'REFCLK_P','REFCLK_N','LANE0_RXP','LANE0_RXN','LANE0_TXP','LANE0_TXN'}: b.RemoveNative(x)
def route(name,source,jack,q1,q2):
 n=b.FindNet(name); seg(b,n,F,source,q1); via(b,n,q1); seg(b,n,B,q1,q2); via(b,n,q2); seg(b,n,F,q2,jack)
route('REFCLK_P',(109.95,61.6),(137.25,62.725),(112.5,61.6),(132.0,61.6))
route('REFCLK_N',(109.95,61.2),(136.75,62.725),(112.5,61.2),(131.0,61.2))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
