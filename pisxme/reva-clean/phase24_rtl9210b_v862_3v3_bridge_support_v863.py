"""V863: RTL_3V3 bridge/support power collector on V862."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V860_5V_ADD_U133_V862.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V862_3V3_BRIDGE_SUPPORT_V863.kicad_pcb'
F,L=pcbnew.F_Cu,pcbnew.In2_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(x,y));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3')
# Bridge-side pads and support resistors/cap join the In2 collector.
for a,z in [((105,71.6),(107,71.6)),((105,77.6),(107,77.6)),((121.2,75),(122.5,75)),((121.2,80),(122.5,80)),((120.4,51),(120.4,49.5))]:
 tr(b,n,F,a,z); via(b,n,*z)
for a,z in [((107,71.6),(107,77.6)),((107,71.6),(122.5,71.6)),((122.5,71.6),(122.5,75)),((122.5,75),(122.5,80)),((122.5,71.6),(120.4,49.5))]: tr(b,n,L,a,z)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
