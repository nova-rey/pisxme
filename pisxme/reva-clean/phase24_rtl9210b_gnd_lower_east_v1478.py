"""V1478: lower-east GND launch below the QFN support field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_U163_RXN_REHOME_V1469.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_GND_LOWER_EAST_V1478.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20); b=pcbnew.LoadBoard(str(BASE))
def n(s): q=b.FindNet(s); assert q; return q
def p(x,y): return pcbnew.VECTOR2I_MM(x,y)
def seg(a,z,l):
 q=n('GND'); t=pcbnew.PCB_TRACK(b); t.SetStart(p(*a)); t.SetEnd(p(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(q); t.SetNetCode(q.GetNetCode()); b.Add(t)
def via(xy):
 q=n('GND'); v=pcbnew.PCB_VIA(b); v.SetPosition(p(*xy)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(q); v.SetNetCode(q.GetNetCode()); b.Add(v)
# Leave the exposed pad at its lower-right edge, clear of pad 20, then use a
# short B.Cu dogleg below the support row to the existing GND return vias.
seg((100.40,72.40),(100.80,72.40),F); seg((100.80,72.40),(100.80,73.20),F); via((100.80,73.20))
seg((100.80,73.20),(104.00,73.20),B); seg((104.00,73.20),(104.00,78.00),B); seg((104.00,78.00),(114.40,78.00),B)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
