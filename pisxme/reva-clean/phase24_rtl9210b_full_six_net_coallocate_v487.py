"""V487: move REFCLK_N endpoint vertical beyond TX_N launch."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_FULL_SIX_NET_COALLOCATE_V486.kicad_pcb';out=H/'PHASE24_RTL9210B_FULL_SIX_NET_COALLOCATE_V487.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.13208)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(src));u=b.FindFootprintByReference('U1')
for x in list(b.GetTracks()):
 if x.GetNetname()=='REFCLK_N':b.RemoveNative(x)
n=b.FindNet('REFCLK_N');p=u.FindPadByNumber('62');pp=p.GetPosition();a=(pcbnew.ToMM(pp.x),pcbnew.ToMM(pp.y));q=(112,70.1);s(b,n,F,a,(a[0],q[1]));s(b,n,F,(a[0],q[1]),q);v(b,n,q);s(b,n,F,q,(118,70.1));s(b,n,F,(118,70.1),(118,54));s(b,n,F,(118,54),(136.5,54));s(b,n,F,(136.5,54),(136.5,66));s(b,n,F,(136.5,66),(136.75,66));v(b,n,(136.75,66));s(b,n,F,(136.75,66),(136.75,62.725))
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
