"""V599: test an all-F.Cu outer route for SPICS."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
base=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V595_CLKREQ_LOCAL.kicad_pcb'
out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V599_SPICS_OUTER_FCU.kicad_pcb'
W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(pcbnew.F_Cu);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
b=pcbnew.LoadBoard(str(base));n=b.FindNet('SPICS')
for a,z in [((102.05,61.2),(101.2,61.2)),((101.2,61.2),(101.2,45.0)),((101.2,45.0),(83.3,45.0)),((83.3,45.0),(83.3,70.0))]: seg(b,n,a,z)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
