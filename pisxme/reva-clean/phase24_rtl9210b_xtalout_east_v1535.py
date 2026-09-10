"""V1535: XTAL_OUT layer handoff east of the QFN while retaining XIN."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_XTALIN_CLEANFIELD_V1534.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_XTALOUT_EAST_V1535.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE)); V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); n=b.FindNet('XTAL_OUT'); F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def tr(a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(V(x,y)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
tr((94.05,67.6),(94.8,67.6),F); via(94.8,67.6); tr((94.8,67.6),(94.8,63.0),B); tr((94.8,63.0),(91.0,63.0),B); via(91.0,63.0); tr((91.0,63.0),(91.0,62.0),F); tr((91.0,62.0),(91.0,60.5),F); tr((91.0,60.5),(89.4,59.0),F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
