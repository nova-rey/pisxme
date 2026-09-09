"""V1278: route RTL9210B RSET from U1.51 to R1.1."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_COUPLED_5V_1V1_SOURCEFIELD_V1277.kicad_pcb';OUT=H/'PHASE24_RTL9210B_RSET_LIVE_PAD_V1278.kicad_pcb';F,W=pcbnew.F_Cu,pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RSET');g=b.FindNet('GND')
for a,z in [((94.8,66.05),(92.0,66.05)),((92.0,66.05),(90.0,64.0)),((90.0,64.0),(88.0,63.8)),((88.0,63.8),(88.0,65.0))]:
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
q=pcbnew.PCB_TRACK(b);q.SetStart(P(89.2,65.0));q.SetEnd(P(89.2,66.0));q.SetLayer(F);q.SetWidth(W);q.SetNet(g);q.SetNetCode(g.GetNetCode());b.Add(q)
q=pcbnew.PCB_VIA(b);q.SetPosition(P(89.2,66.0));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(g);q.SetNetCode(g.GetNetCode());b.Add(q)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
