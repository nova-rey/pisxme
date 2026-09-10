"""V1527: XTAL_IN north/outboard B.Cu corridor on V1523."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RTL3V3_REHOME_U152_V1523.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_XTALIN_OUTER_V1527.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE)); V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); n=b.FindNet('XTAL_IN'); F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def tr(a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(V(x,y)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
tr((94.05,67.2),(97.0,67.2),F); via(97.0,67.2); tr((97.0,67.2),(97.0,56.0),B); tr((97.0,56.0),(86.0,56.0),B); tr((86.0,56.0),(86.0,62.0),B); via(86.0,62.0); tr((86.0,62.0),(88.0,62.0),F); tr((88.0,62.0),(88.0,59.0),F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
