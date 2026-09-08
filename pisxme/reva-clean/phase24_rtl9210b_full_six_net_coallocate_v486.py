"""V486: move TX_N endpoint transition clear of REFCLK_N."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_FULL_SIX_NET_COALLOCATE_V485.kicad_pcb';out=H/'PHASE24_RTL9210B_FULL_SIX_NET_COALLOCATE_V486.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.13208)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(src));u=b.FindFootprintByReference('U1')
for x in list(b.GetTracks()):
 if x.GetNetname()=='LANE0_TXN':b.RemoveNative(x)
n=b.FindNet('LANE0_TXN');p=u.FindPadByNumber('67');pp=p.GetPosition();a=(pcbnew.ToMM(pp.x),pcbnew.ToMM(pp.y));q=(115,67.4);s(b,n,F,a,(a[0],q[1]));s(b,n,F,(a[0],q[1]),q);v(b,n,q);s(b,n,B,q,(120,67.4));v(b,n,(120,67.4));s(b,n,F,(120,67.4),(120,80));s(b,n,F,(120,80),(142,80));v(b,n,(142,80));s(b,n,B,(142,80),(142,59.2));s(b,n,B,(142,59.2),(133.75,59.2));v(b,n,(133.75,59.2));s(b,n,F,(133.75,59.2),(135.25,62.725))
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
