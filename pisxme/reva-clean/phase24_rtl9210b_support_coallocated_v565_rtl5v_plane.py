"""V565: test a local In2 RTL_5V island with three explicit pad escapes."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V562.kicad_pcb';out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V565_RTL5V_PLANE.kicad_pcb'
F=pcbnew.F_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(F);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,a):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*a));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());v.SetWidth(pcbnew.FromMM(.6));v.SetDrill(pcbnew.FromMM(.3));b.Add(v)
b=pcbnew.LoadBoard(str(src));n=b.FindNet('RTL_5V')
for a,z in [((102.8,58.05),(101.2,58.05)),((102.05,64.8),(101.2,64.8)),((124.4,61.0),(123.2,61.0))]:tr(b,n,a,z);via(b,n,z)
z=pcbnew.ZONE(b);z.SetLayer(pcbnew.In2_Cu);z.SetNet(n);z.SetNetCode(n.GetNetCode());z.SetPadConnection(pcbnew.ZONE_CONNECTION_THERMAL);z.SetLocalClearance(pcbnew.FromMM(.20));z.SetMinThickness(pcbnew.FromMM(.20));poly=pcbnew.SHAPE_POLY_SET();c=pcbnew.SHAPE_LINE_CHAIN()
for q in [(100.8,56.8),(123.5,56.8),(123.5,64.5),(100.8,64.5)]:c.Append(P(*q))
c.SetClosed(True);poly.AddOutline(c);z.SetOutline(poly);b.Add(z)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
