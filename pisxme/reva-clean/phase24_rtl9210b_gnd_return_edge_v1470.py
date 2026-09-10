"""V1470: attach the local RTL9210B exposed-pad GND to the return network."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U163_RXN_REHOME_V1469.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_GND_RETURN_EDGE_V1470.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20); b=pcbnew.LoadBoard(str(BASE))
def n(s): q=b.FindNet(s); assert q is not None; return q
def p(x,y): return pcbnew.VECTOR2I_MM(x,y)
def seg(s,a,z,l):
 q=n(s); t=pcbnew.PCB_TRACK(b); t.SetStart(p(*a)); t.SetEnd(p(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(q); t.SetNetCode(q.GetNetCode()); b.Add(t)
def via(s,xy):
 q=n(s); v=pcbnew.PCB_VIA(b); v.SetPosition(p(*xy)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(q); v.SetNetCode(q.GetNetCode()); b.Add(v)
# U1.69 occupies x=95.6..100.4, y=67.6..72.4.  Leave the package field
# through-via-free and take the GND return from its bottom edge.
seg('GND',(100.40,72.40),(101.00,72.40),F)
via('GND',(101.00,72.40))
seg('GND',(101.00,72.40),(101.00,78.00),B)
seg('GND',(101.00,78.00),(114.40,78.00),B)
via('GND',(114.40,78.00))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
