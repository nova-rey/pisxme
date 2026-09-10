"""V1474: route the QFN GND return above the support-field rows."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U163_RXN_REHOME_V1469.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_GND_RETURN_TOPRIGHT_OUTER_V1474.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20); b=pcbnew.LoadBoard(str(BASE))
def n(s): q=b.FindNet(s); assert q is not None; return q
def p(x,y): return pcbnew.VECTOR2I_MM(x,y)
def seg(s,a,z,l):
 q=n(s); t=pcbnew.PCB_TRACK(b); t.SetStart(p(*a)); t.SetEnd(p(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(q); t.SetNetCode(q.GetNetCode()); b.Add(t)
def via(s,xy):
 q=n(s); v=pcbnew.PCB_VIA(b); v.SetPosition(p(*xy)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(q); v.SetNetCode(q.GetNetCode()); b.Add(v)
# Start at the exposed-pad top-right edge, move just outside the support
# field, then use an outer B.Cu corridor above the existing rows.
seg('GND',(100.40,67.60),(101.50,67.60),F); via('GND',(101.50,67.60)); seg('GND',(101.50,67.60),(101.50,69.20),B); seg('GND',(101.50,69.20),(122.00,69.20),B); seg('GND',(122.00,69.20),(122.00,78.00),B); seg('GND',(122.00,78.00),(115.60,78.00),B)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
