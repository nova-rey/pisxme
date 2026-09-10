"""V1475: use the exposed-pad right shelf below the QFN right pads."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U163_RXN_REHOME_V1469.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_GND_RETURN_RIGHT_SHELF_V1475.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20); b=pcbnew.LoadBoard(str(BASE))
def n(s): q=b.FindNet(s); assert q is not None; return q
def p(x,y): return pcbnew.VECTOR2I_MM(x,y)
def seg(s,a,z,l):
 q=n(s); t=pcbnew.PCB_TRACK(b); t.SetStart(p(*a)); t.SetEnd(p(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(q); t.SetNetCode(q.GetNetCode()); b.Add(t)
def via(s,xy):
 q=n(s); v=pcbnew.PCB_VIA(b); v.SetPosition(p(*xy)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(q); v.SetNetCode(q.GetNetCode()); b.Add(v)
# U1.69 right edge is x=100.40.  The x=101.00/y=69.20 shelf clears the
# right-pad row (pad 29 is centered at 101.95/68.80), then the B.Cu route
# stays above the existing y=70.4..79.5 support rows until x=122.
seg('GND',(100.40,69.20),(101.00,69.20),F); via('GND',(101.00,69.20)); seg('GND',(101.00,69.20),(122.00,69.20),B); seg('GND',(122.00,69.20),(122.00,78.00),B); seg('GND',(122.00,78.00),(115.60,78.00),B)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
