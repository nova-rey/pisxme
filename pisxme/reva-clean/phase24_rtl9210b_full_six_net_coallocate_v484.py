"""V484: clear REFCLK support pads and TXP endpoint corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_FULL_SIX_NET_COALLOCATE_V480.kicad_pcb';out=H/'PHASE24_RTL9210B_FULL_SIX_NET_COALLOCATE_V484.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.13208)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(src));u=b.FindFootprintByReference('U1')
for name in ('REFCLK_P','REFCLK_N'):
 for x in list(b.GetTracks()):
  if x.GetNetname()==name:b.RemoveNative(x)
for name,pad,q in [('REFCLK_P','61',(111,71)),('REFCLK_N','62',(112,70.1))]:
 n=b.FindNet(name);p=u.FindPadByNumber(pad);pp=p.GetPosition();a=(pcbnew.ToMM(pp.x),pcbnew.ToMM(pp.y));s(b,n,F,a,(a[0],q[1]));s(b,n,F,(a[0],q[1]),q);v(b,n,q)
n=b.FindNet('REFCLK_P');s(b,n,B,(111,71),(111,55));s(b,n,B,(111,55),(138,55));s(b,n,B,(138,55),(138,56));v(b,n,(138,56));s(b,n,F,(138,56),(137.25,62.725))
n=b.FindNet('REFCLK_N');s(b,n,F,(112,70.1),(118,70.1));s(b,n,F,(118,70.1),(118,54));s(b,n,F,(118,54),(136.0,54));s(b,n,F,(136,54),(136.75,66));v(b,n,(136.75,66));s(b,n,F,(136.75,66),(136.75,62.725))
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
