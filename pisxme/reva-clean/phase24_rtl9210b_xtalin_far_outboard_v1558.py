"""V1558: far-outboard XTAL_IN transition with an upper B.Cu return."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RTL3V3_REHOME_U152_V1523.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_XTALIN_FAR_OUTBOARD_V1558.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE)); V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
n=b.FindNet('XTAL_IN')
for o in list(b.GetTracks()):
 if o.GetNetCode()==n.GetNetCode(): b.RemoveNative(o)
def tr(net,pts,l):
 for a,z in zip(pts,pts[1:]):
  t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(net); t.SetNetCode(net.GetNetCode()); b.Add(t)
def via(net,x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(V(x,y)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(net); q.SetNetCode(net.GetNetCode()); b.Add(q)
tr(n,[(94.05,67.2),(100.9,66.8)],F); via(n,100.9,66.8); tr(n,[(100.9,66.8),(100.9,58.0),(88.0,58.0)],B); via(n,88.0,58.0); tr(n,[(88.0,58.0),(88.0,59.0)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
