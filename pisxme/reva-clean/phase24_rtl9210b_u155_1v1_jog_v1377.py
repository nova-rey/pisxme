"""V1377: lateral-jog U1.55 perimeter escape around the 3V3 branch."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U150_1V1_UPPER_V1374.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_U155_1V1_JOG_V1377.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20); P=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_1V1'); assert n
tr(b,n,F,(94.05,68.0),(92.8,68.0)); via(b,n,(92.8,68.0)); tr(b,n,B,(92.8,68.0),(91.5,68.0)); tr(b,n,B,(91.5,68.0),(91.5,64.0)); tr(b,n,B,(91.5,64.0),(97.8,63.6))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
