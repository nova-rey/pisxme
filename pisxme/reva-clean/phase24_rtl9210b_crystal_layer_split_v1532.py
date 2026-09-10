"""V1532: split the adjacent crystal channels at the QFN edge."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RTL3V3_REHOME_U152_V1523.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_CRYSTAL_LAYER_SPLIT_V1532.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE)); V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def tr(net,pts,l):
 for a,z in zip(pts,pts[1:]):
  t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(net); t.SetNetCode(net.GetNetCode()); b.Add(t)
def via(net,x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(V(x,y)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(net); q.SetNetCode(net.GetNetCode()); b.Add(q)
for name in ('XTAL_IN','XTAL_OUT'):
 n=b.FindNet(name)
 for o in list(b.GetTracks()):
  if o.GetNetCode()==n.GetNetCode(): b.RemoveNative(o)
no=b.FindNet('XTAL_OUT'); tr(no,[(94.05,67.6),(93.0,67.6)],F); via(no,93.0,67.6); tr(no,[(93.0,67.6),(93.0,62.8),(91.0,62.8)],B); via(no,91.0,62.8); tr(no,[(91.0,62.8),(91.0,62.0),(91.0,60.5),(89.4,59.0)],F)
ni=b.FindNet('XTAL_IN'); tr(ni,[(94.05,67.2),(93.4,67.2),(93.4,66.2),(92.4,66.2),(92.4,63.2),(88.0,63.2),(88.0,62.0),(88.0,59.0)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
