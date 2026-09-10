"""V1370: direct U2.3 descent; avoid the adjacent SPISO pad field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U120_3V3_V1064_TRANSPLANT_V1368.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_U2_3V3_SUPPORT_V1370.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20); P=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3'); assert n
tr(b,n,F,(113.8,76.4),(113.8,77.2)); via(b,n,(113.8,77.2))
tr(b,n,F,(119.8,76.4),(121.0,76.4)); tr(b,n,F,(121.0,76.4),(121.0,77.2)); via(b,n,(121.0,77.2))
tr(b,n,B,(113.8,77.2),(121.0,77.2)); tr(b,n,F,(121.0,77.2),(121.2,75.0)); tr(b,n,F,(121.0,77.2),(121.2,80.0))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
