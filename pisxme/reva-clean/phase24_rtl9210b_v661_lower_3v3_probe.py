"""V663 disposable: lower U1 RTL_3V3 source-escape discriminator."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; base=H/'PHASE24_RTL9210B_V35_U2_LEFT_RAILS_5V_PLUS_3V3_PROBE.kicad_pcb'; out=H/'PHASE24_RTL9210B_V663_LOWER_3V3_SOURCE_ESCAPE_PROBE.kicad_pcb'
F,B,I=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.In2_Cu; W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(base));n=b.FindNet('RTL_3V3')
# Keep the proven upper field; add lower pad exits on two separated In2 paths.
for a,e,y in [((94.05,68.4),(90.5,68.4),51.5),((94.8,73.95),(93.8,75.2),49.5)]:
 t(b,n,F,a,e);v(b,n,e);t(b,n,I,e,(e[0],y));t(b,n,I,(e[0],y),(93.0,54.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
