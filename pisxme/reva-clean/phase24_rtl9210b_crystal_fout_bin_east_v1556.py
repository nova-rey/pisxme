"""V1556: corrected 0-degree crystal split with east-offset XIN B.Cu trunk."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RTL3V3_REHOME_U152_V1523.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_CRYSTAL_FOUT_BIN_EAST_V1556.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE)); V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
for name in ('XTAL_IN','XTAL_OUT'):
 n=b.FindNet(name)
 for o in list(b.GetTracks()):
  if o.GetNetCode()==n.GetNetCode(): b.RemoveNative(o)
def tr(net,pts,l):
 for a,z in zip(pts,pts[1:]):
  t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(net); t.SetNetCode(net.GetNetCode()); b.Add(t)
def via(net,x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(V(x,y)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(net); q.SetNetCode(net.GetNetCode()); b.Add(q)
no=b.FindNet('XTAL_OUT'); tr(no,[(94.05,67.6),(92.8,67.6),(92.8,62.8),(91,62.8),(91,62),(91,60.5),(89.4,59)],F)
ni=b.FindNet('XTAL_IN'); tr(ni,[(94.05,67.2),(93.6,67.2),(93.6,66.2)],F); via(ni,93.6,66.2); tr(ni,[(93.6,66.2),(96,66.2),(96,61.4),(88,61.4)],B); via(ni,88,61.4); tr(ni,[(88,61.4),(88,59)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
