"""V1471: move the RTL9210B GND edge-via beyond the local rail field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U163_RXN_REHOME_V1469.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_GND_RETURN_OUTBOARD_V1471.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20); b=pcbnew.LoadBoard(str(BASE))
def n(s): q=b.FindNet(s); assert q is not None; return q
def p(x,y): return pcbnew.VECTOR2I_MM(x,y)
def seg(s,a,z,l):
 q=n(s); t=pcbnew.PCB_TRACK(b); t.SetStart(p(*a)); t.SetEnd(p(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(q); t.SetNetCode(q.GetNetCode()); b.Add(t)
def via(s,xy):
 q=n(s); v=pcbnew.PCB_VIA(b); v.SetPosition(p(*xy)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(q); v.SetNetCode(q.GetNetCode()); b.Add(v)
# Leave the U1.69 package field free.  The F.Cu dogleg clears the local
# RTL_3V3 shelf, then the B.Cu trunk stays east of CLKREQ/RTL_1V1 before
# meeting the existing GND return via at (114.4,78.0).
seg('GND',(100.40,72.40),(100.40,73.00),F); seg('GND',(100.40,73.00),(103.00,73.00),F); via('GND',(103.00,73.00)); seg('GND',(103.00,73.00),(109.00,73.00),B); seg('GND',(109.00,73.00),(109.00,79.00),B); seg('GND',(109.00,79.00),(114.40,79.00),B); seg('GND',(114.40,79.00),(114.40,78.00),B)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
