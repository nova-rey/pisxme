"""V753: isolated opposite-dogbone probe for adjacent SPICLK/SPISI pads."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SPI_U2_ROTATE90_VERTICAL_PROBE_V748.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SPI_QFN_ADJACENT_PAIR_DOGBONES_V753.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
clk=b.FindNet('SPICLK'); isi=b.FindNet('SPISI')
# The pair initially leaves the 0.4 mm-pitch pads vertically, then dogbones
# in opposite directions before any transition or long corridor is added.
for n,pts in ((clk,[(100.8,66.05),(100.8,64.5),(100.4,64.0),(104.0,60.0)]),
              (isi,[(101.2,66.05),(101.2,64.5),(101.6,64.0),(106.0,60.0)])):
 for a,z in zip(pts,pts[1:]): t(b,n,a,z)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
