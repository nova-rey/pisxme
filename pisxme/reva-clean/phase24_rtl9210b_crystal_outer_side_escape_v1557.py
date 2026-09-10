"""V1557: outer-side crystal escapes from the 0-degree RTL9210B QFN row."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RTL3V3_REHOME_U152_V1523.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_CRYSTAL_OUTER_SIDE_ESCAPE_V1557.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE)); V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
for name in ('XTAL_IN','XTAL_OUT'):
 n=b.FindNet(name)
 for o in list(b.GetTracks()):
  if o.GetNetCode()==n.GetNetCode(): b.RemoveNative(o)
def tr(net,pts,l):
 for a,z in zip(pts,pts[1:]):
  t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(net); t.SetNetCode(net.GetNetCode()); b.Add(t)
def via(net,x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(V(x,y)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(net); q.SetNetCode(net.GetNetCode()); b.Add(q)
ni=b.FindNet('XTAL_IN'); tr(ni,[(94.05,67.2),(93.0,68.4)],F); via(ni,93.0,68.4); tr(ni,[(93.0,68.4),(86.8,68.4),(86.8,61.4)],B); via(ni,86.8,61.4); tr(ni,[(86.8,61.4),(88.0,61.4),(88.0,59.0)],F)
no=b.FindNet('XTAL_OUT'); tr(no,[(94.05,67.6),(95.5,66.2)],F); via(no,95.5,66.2); tr(no,[(95.5,66.2),(97.0,66.2),(97.0,60.2),(90.4,60.2)],B); via(no,90.4,60.2); tr(no,[(90.4,60.2),(90.4,59.0),(89.4,59.0)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
