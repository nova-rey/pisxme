"""V556: test an In2 RTL_1V1 plane with ordinary-via pad escapes."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V546.kicad_pcb';out=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V556.kicad_pcb'
F=pcbnew.F_Cu;W=pcbnew.FromMM(.13208)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(F);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,a):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*a));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());v.SetWidth(pcbnew.FromMM(.6));v.SetDrill(pcbnew.FromMM(.3));b.Add(v)
b=pcbnew.LoadBoard(str(src));n=b.FindNet('RTL_1V1')
for a,z in [((104.0,65.95),(104.0,67.2)),((106.0,65.95),(105.4,68.0)),((107.2,65.95),(108.5,67.2))]:tr(b,n,a,z);via(b,n,z)
z=pcbnew.ZONE(b);z.SetLayer(pcbnew.In2_Cu);z.SetNet(n);z.SetNetCode(n.GetNetCode());z.SetPadConnection(pcbnew.ZONE_CONNECTION_THERMAL);z.SetLocalClearance(pcbnew.FromMM(.25));z.SetMinThickness(pcbnew.FromMM(.20));poly=pcbnew.SHAPE_POLY_SET();c=pcbnew.SHAPE_LINE_CHAIN()
for q in [(97,56),(114,56),(114,73),(97,73)]:c.Append(P(*q))
c.SetClosed(True);poly.AddOutline(c);z.SetOutline(poly);b.Add(z)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
