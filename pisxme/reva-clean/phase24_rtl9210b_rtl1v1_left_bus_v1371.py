"""V1371: split RTL_1V1 source escapes into right and left buses."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U2_3V3_SUPPORT_V1370.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_RTL1V1_LEFT_BUS_V1371.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20); P=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_1V1'); assert n
# U1.50 uses the clear right/top source pocket.
tr(b,n,F,(95.2,66.05),(96.6,66.05)); tr(b,n,F,(96.6,66.05),(96.6,64.8)); via(b,n,(96.6,64.8)); tr(b,n,B,(96.6,64.8),(102.0,64.8))
# U1.55/U1.60/U1.63 share a left-side F.Cu bus and one B.Cu handoff.
for y in (68.0,70.0,71.2): tr(b,n,F,(94.05,y),(92.5,y))
tr(b,n,F,(92.5,68.0),(92.5,71.2)); via(b,n,(92.5,71.2)); tr(b,n,B,(92.5,71.2),(102.0,71.2)); tr(b,n,B,(102.0,71.2),(102.0,64.8))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
