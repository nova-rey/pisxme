"""V424: regenerate CLKREQ from the actual U1.13 pad with a right-side dogleg."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_PEDET_NATIVE_ESCAPE_V418.kicad_pcb'
out=H/'PHASE24_RTL9210B_CLKREQ_RIGHT_CLEARANCE_V424.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(src))
for x in list(b.GetTracks()):
 if x.GetNetname()=='CLKREQ_N': b.RemoveNative(x)
n=b.FindNet('CLKREQ_N')
seg(b,n,F,(104.4,58.05),(104.4,59.0)); seg(b,n,F,(104.4,59.0),(108.0,59.0)); seg(b,n,F,(108.0,59.0),(108.0,55.5)); via(b,n,(108.0,55.5))
seg(b,n,B,(108.0,55.5),(97.5,55.5)); seg(b,n,B,(97.5,55.5),(97.5,76.0)); seg(b,n,B,(97.5,76.0),(137.5,76.0)); via(b,n,(137.5,76.0)); seg(b,n,F,(137.5,76.0),(136.5,70.275))
via(b,n,(101.4,55.5)); seg(b,n,F,(101.4,55.5),(101.4,53.0))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
