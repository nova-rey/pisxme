"""V1479: lower-west GND launch, avoiding the QFN lower support pads."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_U163_RXN_REHOME_V1469.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_GND_LOWER_WEST_V1479.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20); b=pcbnew.LoadBoard(str(BASE))
def n(): q=b.FindNet('GND'); assert q; return q
def p(x,y): return pcbnew.VECTOR2I_MM(x,y)
def seg(a,z,l):
 q=n(); t=pcbnew.PCB_TRACK(b); t.SetStart(p(*a)); t.SetEnd(p(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(q); t.SetNetCode(q.GetNetCode()); b.Add(t)
def via(xy):
 q=n(); v=pcbnew.PCB_VIA(b); v.SetPosition(p(*xy)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(q); v.SetNetCode(q.GetNetCode()); b.Add(v)
seg((100.40,72.40),(100.40,73.50),F); seg((100.40,73.50),(99.80,73.50),F); via((99.80,73.50))
seg((99.80,73.50),(97.50,73.50),B); seg((97.50,73.50),(97.50,77.50),B); seg((97.50,77.50),(114.40,77.50),B); seg((114.40,77.50),(114.40,78.00),B)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
