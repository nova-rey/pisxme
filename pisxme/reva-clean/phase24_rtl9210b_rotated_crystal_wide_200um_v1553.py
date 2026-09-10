"""V1553: 0.20 mm compliant, widely separated rotated-QFN escapes."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_ROTATED_U163_1V1_V1403.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_ROTATED_CRYSTAL_WIDE_200UM_V1553.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE)); V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
for o in list(b.GetTracks()): b.RemoveNative(o)
for o in list(b.Zones()): b.RemoveNative(o)
for f in list(b.GetFootprints()):
 if f.GetReference() not in {'U1','Y1','C1','C2','R1'}: b.RemoveNative(f)
def tr(net,pts,l):
 for a,z in zip(pts,pts[1:]):
  t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(net); t.SetNetCode(net.GetNetCode()); b.Add(t)
def via(net,x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(V(x,y)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(net); q.SetNetCode(net.GetNetCode()); b.Add(q)
ni=b.FindNet('XTAL_IN'); tr(ni,[(95.2,73.95),(93.2,76.5)],F); via(ni,93.2,76.5); tr(ni,[(93.2,76.5),(84.4,76.5)],B); via(ni,84.4,76.5); tr(ni,[(84.4,76.5),(84.4,61.8),(87.3,61.8),(87.3,63)],F)
no=b.FindNet('XTAL_OUT'); tr(no,[(95.6,73.95),(97.4,75.4)],F); via(no,97.4,75.4); tr(no,[(97.4,75.4),(90.4,75.4)],B); via(no,90.4,75.4); tr(no,[(90.4,75.4),(90.4,61.8),(88.7,61.8),(88.7,63)],F)
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
