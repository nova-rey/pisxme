"""V1472: use the U1.45 north-side GND departure for the QFN return."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U163_RXN_REHOME_V1469.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_GND_RETURN_NORTH_V1472.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20); b=pcbnew.LoadBoard(str(BASE))
def n(s): q=b.FindNet(s); assert q is not None; return q
def p(x,y): return pcbnew.VECTOR2I_MM(x,y)
def seg(s,a,z,l):
 q=n(s); t=pcbnew.PCB_TRACK(b); t.SetStart(p(*a)); t.SetEnd(p(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(q); t.SetNetCode(q.GetNetCode()); b.Add(t)
def via(s,xy):
 q=n(s); v=pcbnew.PCB_VIA(b); v.SetPosition(p(*xy)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(q); v.SetNetCode(q.GetNetCode()); b.Add(v)
# U1.45=(97.20,66.05) is already joined to U1.69.  Exit north from that
# pad, transition outside the top QFN row, and join the existing GND via.
seg('GND',(97.20,66.05),(97.20,65.00),F); via('GND',(97.20,65.00)); seg('GND',(97.20,65.00),(94.00,65.00),B); seg('GND',(94.00,65.00),(94.00,62.00),B)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
