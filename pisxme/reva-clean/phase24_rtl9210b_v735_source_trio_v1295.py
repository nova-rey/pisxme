"""V1295: add rotated-U1 RTL_1V1/RTL_3V3 source trio to V735."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_SPI_U1_ROTATE90_SPICS_SPISO_V735.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V735_SOURCE_TRIO_V1295.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def r(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));one=b.FindNet('RTL_1V1');three=b.FindNet('RTL_3V3')
# Pad 25 is the rightmost member of the rotated source row.  Escape to the
# right, outside the adjacent DEVSLP/no-connect pads, then use a lower B.Cu
# corridor so it does not cross the RTL_3V3 upper corridor.
r(b,one,F,[(98.4,66.05),(98.4,63.0)]);v(b,one,(98.4,63.0));r(b,one,B,[(98.4,63.0),(98.4,59.0),(123.4,59.0),(123.4,52.0)]);v(b,one,(123.4,52.0));r(b,one,F,[(123.4,52.0),(123.4,51.0)])
r(b,three,F,[(94.8,66.05),(94.0,66.05)]);v(b,three,(94.0,66.05));r(b,three,B,[(94.0,66.05),(94.0,57.0),(120.4,57.0),(120.4,52.0)]);v(b,three,(120.4,52.0));r(b,three,F,[(120.4,52.0),(120.4,51.0)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
