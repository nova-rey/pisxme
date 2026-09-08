"""V489: add a native-pad-derived RSET support route to the V488 basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_CRYSTAL_SUPPORT_V488.kicad_pcb';out=H/'PHASE24_RTL9210B_RSET_SUPPORT_V489.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(src));n=b.FindNet('RSET');u=b.FindFootprintByReference('U1');p=u.FindPadByNumber('51');q=p.GetPosition();a=(pcbnew.ToMM(q.x),pcbnew.ToMM(q.y))
s(b,n,F,a,(a[0],66.8));s(b,n,F,(a[0],66.8),(98.4,67.5));v(b,n,(98.4,67.5));s(b,n,B,(98.4,67.5),(98.4,73.5));v(b,n,(98.4,73.5));s(b,n,F,(98.4,73.5),(101.4,72.0));s(b,n,F,(101.4,72.0),(101.4,71.0))
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
